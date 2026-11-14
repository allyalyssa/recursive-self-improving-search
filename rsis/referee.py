import re
import unicodedata
from difflib import SequenceMatcher

from . import tavily
from .config import REFEREE_DOMAINS
from .llm import Chat

WRONG_PENALTY = 0.5
MAX_GAP_CHECKS = 12


def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"^(the|a|an) ", "", s.strip())
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def match(name, truth):
    n = norm(name)
    if not n:
        return None
    best, best_r = None, 0.0
    for t in truth:
        for cand in [t["label"], *t["aliases"]]:
            c = norm(cand)
            if not c:
                continue
            if n == c:
                return t["qid"]
            r = SequenceMatcher(None, n, c).ratio()
            if r > best_r:
                best, best_r = t["qid"], r
    return best if best_r >= 0.9 else None


def gap_check(name, hunt, judge):
    """Independent check, through Tavily rather than the searcher's Telem route, for a find Wikidata lacks."""
    r = tavily.search(f"{name} {hunt['criterion']}", max_results=5, exclude_domains=REFEREE_DOMAINS)
    snippets = "\n".join(f"- {x['title']}: {x['content'][:300]}" for x in r.get("results", []))
    known = "; ".join(t["label"] for t in hunt["truth"])
    v = judge.json(
        "You check one claimed answer against web evidence. Reply as JSON {\"verdict\": \"yes\"|\"no\"|\"same\", \"reason\": str}. "
        "Say same if the claimed item is another name for one of the already-known items. "
        "Say yes only if it is a different item and the evidence clearly shows it satisfies the criterion.",
        f"Criterion: {hunt['criterion']}\nAlready-known items: {known}\nClaimed item: {name}\n"
        f"Tavily answer: {r.get('answer')}\nEvidence:\n{snippets}")
    status = {"yes": "verified_gap", "same": "duplicate"}.get(v.get("verdict"), "wrong")
    return status, v.get("reason", "")


def score(finds, hunt, url_providers, check_gaps=True):
    truth = hunt["truth"]
    seen, rows = set(), []
    judge = Chat("judge") if check_gaps else None
    gaps = 0
    for f in finds:
        if not isinstance(f, dict):
            continue
        name = (f.get("name") or "").strip()
        qid = match(name, truth)
        key = qid or norm(name)
        row = {"name": name, "url": f.get("evidence_url"), "providers": sorted(url_providers.get(f.get("evidence_url"), []))}
        if key in seen:
            row["status"] = "duplicate"
        elif qid:
            row["status"], row["qid"] = "correct", qid
            seen.add(qid)
        elif check_gaps and gaps < MAX_GAP_CHECKS:
            gaps += 1
            row["status"], row["reason"] = gap_check(name, hunt, judge)
            seen.add(key)
        else:
            row["status"] = "wrong"
        rows.append(row)
    correct = sum(r["status"] in ("correct", "verified_gap") for r in rows)
    wrong = sum(r["status"] == "wrong" for r in rows)
    total = len(truth) + sum(r["status"] == "verified_gap" for r in rows)
    return {"score": round(max(0.0, correct - WRONG_PENALTY * wrong) / max(total, 1), 4),
            "correct": correct, "wrong": wrong, "total": total,
            "duplicates": sum(r["status"] == "duplicate" for r in rows),
            "missed": [t["label"] for t in truth if t["qid"] not in seen], "rows": rows}
