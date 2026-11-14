import os
import threading

from .http import post_json

credits_used = 0
_lock = threading.Lock()


def search(query, max_results=5, include_answer=True, exclude_domains=None):
    global credits_used
    body = {"query": query, "search_depth": "basic", "max_results": max_results,
            "include_answer": include_answer, "chunks_per_source": 2}
    if exclude_domains:
        body["exclude_domains"] = exclude_domains
    r = post_json("https://api.tavily.com/search", body, {"Authorization": f"Bearer {os.environ['TAVILY_API_KEY']}"})
    with _lock:
        credits_used += (r.get("usage") or {}).get("credits", 1)
    return r
