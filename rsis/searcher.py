import json
import time
import uuid

from . import method as M
from .config import ATTEMPT_BUDGET
from .llm import Chat, parse_obj, tool
from .telem import PROVIDERS, Telem

MAX_TURNS = 30

SEARCH_TOOL = tool("web_search", "Search the web through the Telem router. Omit providers to use the method's default route.", {
    "query": {"type": "string"},
    "also": {"type": "array", "items": {"type": "string"}, "maxItems": 4,
             "description": "Extra query variants run concurrently in the same Telem batch call. Each is billed per provider."},
    "providers": {"type": "array", "items": {"type": "string", "enum": PROVIDERS},
                  "description": "Pin this search to these providers. Each provider is billed separately."},
    "auto_routing": {"type": "boolean", "description": "Let Telem choose providers for this query."},
    "tier": {"type": "string", "enum": ["minimalist", "default", "extended"]},
    "num_results": {"type": "integer", "minimum": 1, "maximum": 20},
    "include_domains": {"type": "array", "items": {"type": "string"}, "description": "Restrict to these host names."},
    "published_after": {"type": "string"}, "published_before": {"type": "string"}}, ["query"])
FETCH_TOOL = tool("fetch_pages", "Fetch full text of up to 5 URLs through Telem.", {
    "urls": {"type": "array", "items": {"type": "string"}}}, ["urls"])
SUBMIT_TOOL = tool("submit", "Submit your final list. Each find needs the URL that supports it. Wrong finds cost points.", {
    "finds": {"type": "array", "items": {"type": "object", "properties": {
        "name": {"type": "string"}, "evidence_url": {"type": "string"}}, "required": ["name", "evidence_url"]}},
    "notes": {"type": "string", "description": "What worked and what did not, in two or three sentences."}}, ["finds"])


def run_search(m, query, args, telem):
    r = m["routing"]
    providers = args.get("providers")
    auto = args.get("auto_routing", r.get("auto_routing") if not providers else False)
    return telem.search(query, also=args.get("also"), providers=providers or (None if auto else r.get("providers")), auto_routing=auto,
                        tier=args.get("tier", r.get("tier", "default")),
                        num_results=args.get("num_results", r.get("num_results", 8)),
                        include_domains=args.get("include_domains"),
                        published_after=args.get("published_after"), published_before=args.get("published_before"))


def attempt(m, hunt, budget=ATTEMPT_BUDGET, role="searcher"):
    """One agent's full try at one hunt. Returns the log; the referee scores it separately."""
    chat = Chat(role)
    telem = Telem(budget)
    system = (f"You are a web search agent working on an open hunt. Follow your search method.\n\n{M.render(m)}\n\n"
              f"You have ${budget:.2f} of Telem search budget. Every tool result reports what is left. "
              "When the budget runs out or you are done, call submit. Only submit items you have evidence for.")
    messages = [{"role": "system", "content": system}, {"role": "user", "content": hunt["question"]}]
    tools = [SEARCH_TOOL, FETCH_TOOL, SUBMIT_TOOL]
    trace, finds, notes = [], [], ""
    t0 = time.time()
    for _ in range(MAX_TURNS):
        msg = chat.complete(messages, tools=tools)
        messages.append({**msg, "role": "assistant", "content": msg.get("content") or ""})
        calls = msg.get("tool_calls") or []
        if not calls:
            messages.append({"role": "user", "content": "Call submit with your finds now."})
            continue
        done = False
        for c in calls:
            name = c["function"]["name"]
            args = parse_obj(c["function"].get("arguments"))
            try:
                if name == "web_search":
                    out = run_search(m, args.pop("query", "") or hunt["question"], args, telem)
                elif name == "fetch_pages":
                    out = telem.fetch(args.get("urls", []))
                elif name == "submit":
                    finds = [f for f in args.get("finds", []) if isinstance(f, dict)]
                    notes, done = args.get("notes", ""), True
                    out = {"ok": True}
                else:
                    out = {"error": f"unknown tool {name}"}
            except Exception as e:
                out = {"error": str(e)[:500]}
            trace.append({"tool": name, "args": args, "summary": {k: out[k] for k in out if k not in ("results", "pages")}})
            messages.append({"role": "tool", "tool_call_id": c["id"], "content": json.dumps(out)[:12000]})
        if done:
            break
    return {"attempt_id": uuid.uuid4().hex[:10], "method": m["id"], "hunt": hunt["name"], "kind": hunt["kind"],
            "pool": hunt["pool"], "finds": finds, "notes": notes, "telem_calls": telem.calls,
            "telem_spent": round(telem.spent, 4), "telem_session": telem.session_id, "trace": trace,
            "url_providers": {u: sorted(p) for u, p in telem.url_providers.items()},
            "seconds": round(time.time() - t0, 1), "tokens": chat.usage}
