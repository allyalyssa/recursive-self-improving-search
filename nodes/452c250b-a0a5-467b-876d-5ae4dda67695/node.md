---
id: "452c250b-a0a5-467b-876d-5ae4dda67695"
name: "Develop Search Improvement Against a Floor Model"
micro_summary: "Applies Jack's floor-first development idea to search learning and later model transfer."
status: "in_progress"
see_also: [{"target":"0964e159-53ba-4612-8b02-6a5d08d6ff24","reason":"Original lower-capability construction hypothesis and its unproven upward-transfer claim."},{"target":"2d831dd8-20d3-490c-832b-c513dd3de130","reason":"Existing staged target: avoid degradation first, then seek improvement without relying on human correction."}]
scope: "Preserve the chosen development target without selecting a model, budget or fine-tuning run."
position: 2048
---
Kind: Idea.

## Creation

### Observed conditions
Jack proposed bootstrapping with a weak model, then encoding what works into a larger model. He later confirmed: "And then build against the weakest model, yeah."

### Inference and response
Develop the search-improvement method against an explicitly chosen lower-capability reference model rather than relying on a frontier model to compensate for unclear instructions. Jack also wants improvement without continued human intervention.

DeepSeek is a cheap candidate in his parallel-agent idea, not a selected provider/model route or a verified capability floor. Stronger-model transfer and eventual training or distillation remain separate possibilities. No monotonic model ranking, training recipe, or transfer result was established.

Source: current Pi session, user records `e57eeaf4`, `e4f393b0`, `7c183177`; root conversation artifact.
