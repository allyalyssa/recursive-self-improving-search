---
id: "9ec1b5d1-69ee-4649-b30f-680e04c0fed9"
name: "Build the Hackathon Around the Recursive Searcher"
micro_summary: "Commits the SearchHack build to the recursive framing and the design choices Jack selected."
status: "in_progress"
scope: "Record Jack's commitments for the November 14 build; the work completes when the build is attempted and its outcome recorded."
see_also: [{"target":"7dfde31d-0c39-4772-9f05-92e4c5613a26","reason":"decided from The Searcher That Searches for How to Search, which keeps the proposed mechanism and its unselected parts."},{"target":"bf8823dd-9e4e-4bed-8430-ca258d5471fd","reason":"The model whose light form the hackathon agents' nodes will follow."}]
position: 8192
---
**Kind:** Agreed Work

## Creation — November 13–14, 2026

### Observed conditions

In the Claude Code session that produced [The Searcher That Searches for How to Search](../7dfde31d-0c39-4772-9f05-92e4c5613a26/node.md), Jack made four choices for the SearchHack build.

- **Recursion is the framing.** He had considered continual learning the day before. He chose: "shoot for recursive, not continual because again recusion is the thing that turns heads". He added that he was unsure how to pull it off or prove it.
- **The core design.** "the searcher that searches for how to search is correct": the search method is used to find improvements to itself.
- **Repeated failures link to nodes.** On the proposed per-attempt record: "failure seen before can be a link to a node."
- **Agents' nodes follow a light state machine.** The assistant recommended that the agents' nodes use the kinds, keep one new node per method version, keep discarded versions with reasons and keep evidence apart from inference. Its mapping was Goal for the hunt, Idea for a candidate version, Probe for a trial round, What We Learned for a lesson with its tested scope, Question only for a consequential unexplained pattern and Agreed Work for adopting a version. It recommended skipping the checker, hosted review and approval gate for speed. Jack replied "sounds good".

### Inference and response

These are commitments for the November 14 build, not results. The task, referee, comparison and recursion test remain open in the Idea and in [Choose the PoC Task and Success Evidence](../9a2b74d6-d0f2-44a5-b6d3-a35fbf465439/node.md). Following the state machine's shape is not evidence that it improves search. This work resolves when the build is attempted and its outcome is recorded, whether or not recursion is shown.

## Source

Claude Code session `feef5eb9-2574-4813-9a7a-3a66a476810e`, retained under the Idea at `artifacts/chats/claude-searchhack-recursive-design.jsonl`. The commitments were moved here from that node's first save at Jack's request.

## November 14 development — models for the improver and searchers

### Observed conditions

On the morning of the event, while answering [Can the Improver Be a Stronger Model Than the Searchers](../8955e243-3ef1-4938-9a32-65729724f2db/node.md), the assistant recommended a one-round bake-off between a cheap and a strong improver. Jack replied: "fuck it good model improver (gpt 6 astra medium) then terra 6.1 high for the searcher next".

### Inference and response

This adds a fifth commitment for the build: GPT 6 Astra at medium effort runs the improver and Terra 6.1 at high effort runs the searchers. It replaces the Idea's unselected proposal that the improver use the same cheap model as the searchers. The bake-off was not run. The assistant's advice to keep both models fixed all day and disclose them in the demo was not separately answered. The guards from [Define and Prevent Reward Hacking in the Search Loop](../e9cf4b7a-3426-4266-a93e-e9aa6491ee9d/node.md) and the plateau matrix in [Detect a Plateau in the Improvement Loop](../420ced74-9291-45ef-b2ec-546f2224c283/node.md) are answers held by those Questions.

Source: Claude Code session `4e8b589f-0715-428e-a9d1-de646827b5e8`, retained at [the plateau node's copy](../420ced74-9291-45ef-b2ec-546f2224c283/artifacts/chats/claude-searchhack-questions-answered.jsonl).
