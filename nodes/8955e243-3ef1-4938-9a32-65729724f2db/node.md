---
id: "8955e243-3ef1-4938-9a32-65729724f2db"
name: "Can the Improver Be a Stronger Model Than the Searchers"
micro_summary: "Asks whether the improver agent should use a stronger model for generating ideas from the trees, or the same model as the searchers."
status: "resolved"
scope: "Settle which model runs the improver relative to the searchers, keeping Jack's choice separate from the assistant's untested evidence and advice."
see_also: [{"target":"9ec1b5d1-69ee-4649-b30f-680e04c0fed9","reason":"Jack's model choice is recorded there as a commitment for the November 14 build."},{"target":"452c250b-a0a5-467b-876d-5ae4dda67695","reason":"Jack's floor-model direction: build against the weakest model; this question asks whether the improver role is an exception."},{"target":"f12a53f8-8dc2-4c1b-b482-cfde6778d2bb","reason":"RSI-top reports cheap models with its harness approaching frontier-model scores on its kernel task; the authors' numbers, not about this project."}]
position: 1024
---
**Kind:** Question

## Creation — November 14, 2026

### Observed conditions

In a Claude Code session the night before the SearchHack event, Jack asked the assistant to explain the recursive project. The assistant read the SiftText nodes, then walked a hypothetical "find every Olympic medallist who later sat in a national parliament" hunt through one improvement round and showed example score records. All of that was synthetic; nothing was run. Jack then asked the assistant to save open questions, the first being:

> "can the improver be a better model at generating ideas from trees or should they all be the same (jvbaii nodes)"

The parenthetical "jvbaii nodes" is Jack's dictated wording; its meaning was not clarified in the session and is not interpreted here.

At the end of his list of three questions Jack added a note: "perhaps more research coudl answer this? or i think idea basins and the recent blog post and our overall research findings the internet + nodes we already have might already have the answer, idk. question not for you but for next model". He framed the questions as work for a later model, not for the assistant that saved them.

### Inference and response

The assistant's earlier proposal in [The Searcher That Searches for How to Search](../7dfde31d-0c39-4772-9f05-92e4c5613a26/node.md) was that the improver use the same cheap model as the searchers, so that the method rather than model strength does the work, and that a flat curve by 2 PM would justify a stronger improver model, disclosed. Jack selected recursion and the core design, not that model choice. So the improver's model is undecided, and this question stays open.

The decision it needs: which model runs the improver, and how a gain would be attributed to the method rather than to the stronger idea generator. The assistant did not research this, and no comparison was run. Jack's note points the next model to existing nodes and the Bespoke Labs post as possible sources.

## Source

Claude Code session `806eebdc-8059-4465-9101-d683b6efe555`, November 14, 2026 (local time, about 1 AM), retained at `artifacts/chats/claude-searchhack-open-questions.jsonl` under [Can the Improver Be a Stronger Model Than the Searchers](../8955e243-3ef1-4938-9a32-65729724f2db/node.md).

## November 14 development — stronger improver chosen

### Observed conditions

On the morning of the event, Jack asked a new Claude Code session to "tackle the questions 1 by 1". The assistant read [Exploration Collapse Findings From RSI-top and Bespoke](../f12a53f8-8dc2-4c1b-b482-cfde6778d2bb/node.md), [Develop Search Improvement Against a Floor Model](../452c250b-a0a5-467b-876d-5ae4dda67695/node.md), [Short Chats Against Idea Basins](../a1952904-c571-4fb9-af12-330b2ed10ca6/node.md) and [Study Fork-and-Flush](../c83b7182-abe0-444a-9a4d-e5b05812a4ef/node.md), and ran web searches. It reported, from secondary sources it did not verify against the papers:

- A Decagon write-up on the GEPA prompt optimizer reports that a small reflection model left the prompt essentially unchanged, while the reflection model is called far less often than the task model.
- Search summaries of the Darwin Gödel Machine paper report that with a fixed improver, gains plateaued early (39% against 50% on SWE-bench).

It answered that a stronger improver does not break the recursion if the improver searches with the current method version and keeps one model for the whole run, disclosed. It named the risk as the stronger model writing a good method from its own knowledge, producing one jump then a flat curve; this was its inference. It noted that the Fork-and-Flush authors expect idea basins to persist as models scale. It recommended a one-round bake-off between a cheap and a strong improver before choosing.

Jack replied:

> "fuck it good model improver (gpt 6 astra medium) then terra 6.1 high for the searcher next"

### Inference and response

Jack chose a stronger improver and skipped the recommended bake-off. The assistant then advised keeping both models fixed all day and saying so in the demo; Jack did not respond to that advice. No comparison between improver models was run, so whether the stronger improver helps, or what share of any gain it explains, is unmeasured. The question of attributing a gain to the method rather than the improver now falls to the recursion test held in [The Searcher That Searches for How to Search](../7dfde31d-0c39-4772-9f05-92e4c5613a26/node.md).

## Completion

Answered by Jack's decision on November 14, 2026: the improver is a stronger model than the searchers. GPT 6 Astra at medium effort runs the improver and Terra 6.1 at high effort runs the searchers. The commitment is recorded in [Build the Hackathon Around the Recursive Searcher](../9ec1b5d1-69ee-4649-b30f-680e04c0fed9/node.md). This settles the choice for the build, not whether a stronger improver is better.

November 14 development and Completion source: Claude Code session `4e8b589f-0715-428e-a9d1-de646827b5e8`, retained at [the plateau node's copy](../420ced74-9291-45ef-b2ec-546f2224c283/artifacts/chats/claude-searchhack-questions-answered.jsonl).
