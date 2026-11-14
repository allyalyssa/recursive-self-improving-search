---
id: "9b2ff11d-f8bd-4aec-b03f-c7052c3bdd8d"
name: "Detect Idea Basins Before Restarting"
micro_summary: "Asks whether score and proposal behavior can justify ending a search-agent session."
status: "deferred"
deferred_reason: "Revisit after a working PoC produces trajectories and a restart decision is worth optimizing; no detector is needed merely to preserve the proposal."
see_also: [{"target":"c83b7182-abe0-444a-9a4d-e5b05812a4ef","reason":"Documents a stall trigger defeated by small gains and one ineffective diversification directive."}]
scope: "Preserve the open stopping-policy question without installing a classifier or claiming a diagnosis."
position: 1024
---
Kind: Question.

## Creation

### Observed conditions
Jack wanted to end an agent when it entered an idea basin but said he did not know how to detect that. He suggested a decision model as one possibility.

### Inference and response
The assistant offered score flattening and increasing attempt similarity as possible signals, and fixed-schedule forks as a simpler comparator. None was tested or selected here.

The paper's non-significant result for a particular "different approach" directive does not show that all injected context is ineffective. Likewise, a flat score alone does not establish an idea basin. The detector's evidence, cost and false restarts remain open.

Source: current Pi session, user records `e4f393b0`, `7c183177`; root conversation artifact.
