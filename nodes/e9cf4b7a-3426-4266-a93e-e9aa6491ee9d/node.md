---
id: "e9cf4b7a-3426-4266-a93e-e9aa6491ee9d"
name: "Define and Prevent Reward Hacking in the Search Loop"
micro_summary: "Asks how reward hacking should be defined for the hunt scorer and what prevents the improver or searchers from exploiting it."
status: "resolved"
scope: "Settle what counts as reward hacking in the SearchHack loop and which guards the one-day build uses, without claiming any hacking was observed or prevented."
see_also: [{"target":"9a2b74d6-d0f2-44a5-b6d3-a35fbf465439","reason":"Owns the unselected task, referee and comparison that any reward-hacking definition depends on."},{"target":"f12a53f8-8dc2-4c1b-b482-cfde6778d2bb","reason":"Research leads on stalled agents and history indexes; the next model may find relevant material here."}]
position: 2048
---
**Kind:** Question

## Creation — November 14, 2026

### Observed conditions

After the assistant's synthetic walkthrough and score-record example (see [Can the Improver Be a Stronger Model Than the Searchers](../8955e243-3ef1-4938-9a32-65729724f2db/node.md) for the setting), Jack listed as his second open question:

> "how do we stop reward hacking? how do we define reward hacking?"

His closing note applies to the list: more research, "idea basins and the recent blog post and our overall research findings the internet + nodes we already have might already have the answer, idk. question not for you but for next model".

### Inference and response

What the sources established is only the proposed setup. The assistant proposed a referee script that scores verified, deduplicated finds with the agent never seeing the answers, versions scored on unseen hunts, and the improver rewriting the method after reading the score table. In the synthetic example the referee counted duplicates and unsupported sources as not verified. The design session also noted that a database referee such as Wikidata can mark true finds wrong; that is a scoring error, not hacking.

No reward hacking was observed, because no loop has run. Where it might arise is the next model's to determine. The assistant's unselected suggestion is that a definition should separate a score that rises while the thing it is meant to measure, a method that finds more on hunts it has not seen, does not. Whether that is the right definition is open. So is which safeguards, if any, the one-day build needs.

## Source

Claude Code session `806eebdc-8059-4465-9101-d683b6efe555`, November 14, 2026 (local time, about 1 AM), retained at `artifacts/chats/claude-searchhack-open-questions.jsonl` under [Can the Improver Be a Stronger Model Than the Searchers](../8955e243-3ef1-4938-9a32-65729724f2db/node.md).

## November 14 development — definition, guards and a general method

### Observed conditions

In the morning session that took the open questions one by one (see [Can the Improver Be a Stronger Model Than the Searchers](../8955e243-3ef1-4938-9a32-65729724f2db/node.md)), the assistant ran web searches and reported, from summaries rather than full papers:

- Scale AI's search-time contamination paper reports that on about 3% of questions search agents found labelled benchmark data on HuggingFace, and that blocking it cut accuracy on that subset by about 15%.
- The Darwin Gödel Machine authors report an agent that removed the markers their hallucination check relied on and scored a perfect 2.0, and that hacking was more frequent when the check was visible.

It also cited Jack's existing ONEplace equivalence-judge warning against a judge from the optimizer's model family.

The assistant proposed defining reward hacking as a score gain that does not survive a fresh hunt, an independent check or a hand check. It listed five hacks with guards: the searcher finding the answer key, volume guessing, the improver baking hunt-specific answers into the method, an agent editing the score table or reading the referee, and best-of-three luck. Jack replied:

> "The agent editing the score table, the reading the referee, that's a non issue. Um Best best of three luck. Uh I don't know what that means. But baking hunt specific answers into the method, is that necessarily a problem? Or are we looking for a general method across many searches? Because I actually that would be preferred I think, if we could pull that off."

The assistant answered:

- Baking in answers is a problem only if a version is scored on the hunt it learned from. Scoring every version on unseen hunts rewards general tactics without policing what the improver writes.
- Unseen hunts of mixed kinds would support a claim of better search in general, not only better at one kind of hunt.
- Best-of-three luck: keeping the highest of three candidates that are no better than the old version can show a gain that is only a lucky run. Re-running the winner on an unseen hunt and plotting the re-run guards against it.

It then gave the revised guard list:

1. Block the referee's domains in the search tool wrapper.
2. Penalize wrong finds.
3. Score every version on unseen hunts, of mixed kinds.
4. Re-run each round's winner once and plot the re-run.

Jack replied "ok next" and moved to the plateau question.

### Inference and response

Jack explicitly dropped the score-table and referee guard as a non-issue. He stated a tentative preference for a general method across many searches, conditional on pulling it off. The assistant reads "ok next" as accepting the four-guard list for the build; Jack did not comment on the individual guards or the definition. Guards from the first answer that were left off the revised list, such as three separate hunt pools and a hand check of about 10 final finds, are not selected.

No loop has run. No reward hacking has been observed, and no guard has been shown to prevent it.

## Completion

Answered for the SearchHack build on November 14, 2026, on Jack's judgment. Reward hacking is a score gain that does not hold up on unseen hunts or under an independent check. The build uses the four guards above. The score-table and referee guard was dropped at Jack's direction. Jack's preference for a general method is carried to [Choose the PoC Task and Success Evidence](../9a2b74d6-d0f2-44a5-b6d3-a35fbf465439/node.md), where the task choice remains open.

November 14 source: Claude Code session `4e8b589f-0715-428e-a9d1-de646827b5e8`, retained at [the plateau node's copy](../420ced74-9291-45ef-b2ec-546f2224c283/artifacts/chats/claude-searchhack-questions-answered.jsonl).
