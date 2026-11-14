---
id: "9a2b74d6-d0f2-44a5-b6d3-a35fbf465439"
name: "Choose the PoC Task and Success Evidence"
micro_summary: "Holds the unresolved workload, comparison, scorer and meaning of recursive improvement."
status: "in_progress"
see_also: [{"target":"c5749fc3-e9ea-4a72-84d7-e2fbeac032c5","reason":"Construction fidelity and downstream efficacy must remain distinct; a package gain also differs from its cause."}]
scope: "Carry open design questions forward without pretending earlier assistant examples were an approved experiment."
position: 1024
---
Kind: Question.

## Creation

### Observed conditions
The assistant alternated between searching SiftText for known nodes and answering live web-research questions. It proposed practice and held-out tasks, no-memory/notes/vector/SiftText arms, repeated runs, and several different task counts. Jack did not select an exact workload, scorer, comparison set, sample size or budget. His latest instruction was PoC first.

### Inference and response
The next design must settle what the agent searches, what is allowed to change, and what independent observation would show improvement. A method version, an agent attempt and a search task are different objects; the graph must not conflate them.

Assistant-proposed evidence includes unseen-task performance against the same frozen starting procedure and a credible notes baseline, with matched model/tool/resource conditions and full improvement, retrieval and writing cost. Those are candidates, not an authorized specification. A known target UUID only scores record retrieval; it does not mechanically establish the quality of an open literature synthesis.

The recursion claim also needs a boundary: improving the task procedure is different from improving how the system proposes or selects future improvements. Candidate reuse, a branching graph, or one successful retry does not by itself establish either broader capability or SiftText's causal contribution. No result, including non-degradation, follows from a flat curve without an appropriate comparison.

Source: current Pi session's assistant proposals and user record `3063667d`; root conversation artifact.

## November 13–14 — lookup tasks rejected; checkable hunts proposed

### Observed conditions

In a Claude Code session the night before the hackathon, the assistant proposed paper-finding lookups with known answers, scored across a research-field switch. Jack rejected the "paper analogy" and asked for something grand and recursive. He then said: "i feel like the answers should be either long horizon or opaque or extremely difficult, almost i have the feeling it should be so hard we shouldnt even know the answer, is that possible? or nah, do we always need the answer?" His stated purpose was "ample time to improve our methods and show real improvement".

### Inference and response

The assistant answered that a task needs a referee, not a known answer, and separated three kinds: known but hard-to-find answers; unknown but checkable results; and unknown, uncheckable outputs graded by opinion, which it advised against for a one-day event. It proposed open hunts ("find every documented case of X") scored by verified, deduplicated finds with no ceiling. For the scored task it proposed hunts whose full answer a public database such as Wikidata can compute while the agent only has web search, with an open model-judged hunt as a closing showpiece. Database gaps would mark some true finds wrong; no such question was tested.

It also warned that each attempt must still take minutes, and that a growing list alone does not show method improvement: compare versions on the same fresh hunt and budget. Jack did not select a task, referee or comparison. Hackathon fit and the recursion test are carried by [The Searcher That Searches for How to Search](../7dfde31d-0c39-4772-9f05-92e4c5613a26/node.md). Source: that node's retained Claude Code session.

## November 14 — Jack prefers a general method across hunt kinds

### Observed conditions

While answering the reward-hacking question in [Define and Prevent Reward Hacking in the Search Loop](../e9cf4b7a-3426-4266-a93e-e9aa6491ee9d/node.md), Jack asked: "Or are we looking for a general method across many searches? Because I actually that would be preferred I think, if we could pull that off." The assistant answered that scoring every version on unseen hunts of mixed kinds would support a claim of better search in general. It proposed mixing at least two hunt kinds. Jack replied "ok next".

### Inference and response

This narrows the comparison toward mixed-kind unseen hunts, with Jack's preference stated tentatively. The task, its kinds, the referee, the sample size and the budget are still unselected.
