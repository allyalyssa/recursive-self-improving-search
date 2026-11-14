---
id: "f12a53f8-8dc2-4c1b-b482-cfde6778d2bb"
name: "Exploration Collapse Findings From RSI-top and Bespoke"
micro_summary: "Records what two November 2026 autoresearch studies show about stalled agents and history indexes."
status: "resolved"
scope: "Capture the bounded reads of two sources as design leads for SearchHack, not as evidence about SiftText or web search."
see_also: [{"target":"c83b7182-abe0-444a-9a4d-e5b05812a4ef","reason":"Existing review of Fork-and-Flush idea basins; both new sources build on that work."},{"target":"9b2ff11d-f8bd-4aec-b03f-c7052c3bdd8d","reason":"RSI-top acts on a flat best score rather than detecting a basin, a simpler comparator for that deferred question."},{"target":"87e216ba-5f84-408a-a381-c15b71b4937b","reason":"RSI-top's partial dashboards and separate lineages are a tested form of varying what each agent reads."},{"target":"452c250b-a0a5-467b-876d-5ae4dda67695","reason":"RSI-top reports cheap models with its harness approaching frontier-model scores, relevant to the floor-model direction."}]
position: 1024
---
**Kind:** What We Learned

## Observed conditions

On November 13–14, 2026, Jack linked the Bespoke Labs post [How models explore ideas](https://bespokelabs.ai/blog/how-models-explore-ideas) (November 10, 2026) and asked the assistant to read [RSI-top](https://rsi-top.github.io/), which the post cites. The assistant read the full text of both pages in a browser and viewed the post's idea maps. RSI-top is a Stanford project page with a code link and no paper PDF; its code was not read.

**Bespoke Labs** placed AutoResearchExam submissions into "idea basins" by summarising each submission's code and clustering the summaries on a 2D map. It reports that:

- runs visit 1.5 to 2 basins on average, and 47% never leave their first;
- about half of switches return to an idea already tried, gaining about as much as staying;
- a switch to a new basin is followed by about nine times the gain of a refinement step, concentrated in the first six hours;
- 58% of runs never visit the basin holding their task's best solution.

**RSI-top** wraps evolutionary code-search frameworks on Anthropic kernel optimisation and MLE-bench. It reports that:

- runs were stalled 84% to 92% of the time;
- the bottleneck is how the agent sees its own history, since full history overflows, summaries lose detail and resets lose attempts;
- a fixed set of LLM-designed, script-computed metrics gives one row per trajectory, and agents open full trajectories only on demand;
- when the best score stays flat, a cohort intervenes, each agent seeing a random subset of metrics, proposing eight directions with stated probabilities and grounding them in different lineages;
- Flash-class models with the harness came close to frontier-model scores at roughly 4 to 14 times lower cost on the kernel task.

Metric definitions are fixed before the run, and the frameworks' own selection and mutation rules are unchanged.

## Inference and response

The assistant drew three design leads for [The Searcher That Searches for How to Search](../7dfde31d-0c39-4772-9f05-92e4c5613a26/node.md): use a flat-best-score trigger for the improver, give agents different views and lineages to resist shared-history inertia, and keep a numeric per-attempt index beside written lessons. It also noted that nothing on the RSI-top page modifies the harness itself, despite the name; letting the search method be rewritten is the proposed difference.

Both studies concern code optimisation and ML tasks, not web search. Their numbers are the authors' reports, unreproduced here. They support design choices, not a claim that SiftText or this project improves search.

## Completion and source

The bounded read is complete. Source: Claude Code session `feef5eb9-2574-4813-9a7a-3a66a476810e`, retained under [The Searcher That Searches for How to Search](../7dfde31d-0c39-4772-9f05-92e4c5613a26/node.md) at `artifacts/chats/claude-searchhack-recursive-design.jsonl`.
