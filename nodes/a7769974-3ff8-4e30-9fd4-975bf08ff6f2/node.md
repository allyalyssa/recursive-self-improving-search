---
id: "a7769974-3ff8-4e30-9fd4-975bf08ff6f2"
name: "Team Backgrounds and a Proposed Work Split"
micro_summary: "Records what Alyssa and Amala reported about their experience and the assistant's proposed division of the build among the three teammates."
status: "in_progress"
scope: "Preserve the teammates' self-reported backgrounds and the unselected proposal for dividing the SearchHack build, without claiming that roles were assigned."
see_also: [{"target":"e9cf4b7a-3426-4266-a93e-e9aa6491ee9d","reason":"Holds the four guards that the proposed split gives to Amala."},{"target":"9a2b74d6-d0f2-44a5-b6d3-a35fbf465439","reason":"Holds Jack's remark from the same introductions about known-answer scoring and a later unknown-answer comparison."},{"target":"420ced74-9291-45ef-b2ec-546f2224c283","reason":"Holds the plateau answer that the proposed split gives to Alyssa."}]
position: 9216
---
**Kind:** Idea

## Creation — November 14, 2026

### Observed conditions

On the day of the event Jack pasted a speech-to-text transcript into a Pi session and labelled it "hackathon team intros". It has no speaker labels, so who said what is read from the content. It spelled the teammates' names "Olesa" (once "Alyssa") and "Abula". Jack corrected them: "Alyssa not Olesa, Amala not Abula".

Jack opened by saying that SiftText trees on him record what he has done and so his skill set, then asked the others for theirs.

**Alyssa** gave an introduction as experienced in "training LSTMs and um analyzing data sets" and described:

- An LSTM project on synaptic homeostasis during sleep: "we trained like a bidirectional LSTM and then we kept adding or reducing parameters based on how well it worked".
- An LSTM project on orthographic density and the N400, where "we kind of kept adjusting the AI models and like retraining the LSTM". The transcript garbles the stopping point.
- Data work that is mostly EEG and neuromodulation: "mostly like P300s, like spellers, M400s, and like linguistics". A current project looks at ERPs and alpha waves in people reconstructing images, using RDMs and RSA.
- Dataset sizes: "the biggest one I've done is like 5,000 participants". The current university datasets are smaller, about 70 participants in one.

The transcript has Alyssa saying "I've been all like three times" before these. The assistant reads that as three LSTM projects, of which two were described.

**Amala** said "I do a lot more with coding and technical parts". Asked to go into depth on reward hacking, Amala described "a lot of work in looking at different models and looking at their benchmarks [...] and essentially looking at how models are a board hack based on these benchmarks". The assistant reads "a board hack" as a transcription of "reward hack".

Asked about datasets, Amala answered "Not for this, but for a different project": an ocean buoy project. Existing models for choosing where to put a buoy are "just best guesses", and Amala has "worked with a lot of boy data to try to come up with a model that um looks given a latitude longitude coordinate and a radius". The description stops there because Jack interjected. His reply is recorded in [Choose the PoC Task and Success Evidence](../9a2b74d6-d0f2-44a5-b6d3-a35fbf465439/node.md).

These are the teammates' own spoken reports. Nothing was checked independently, and the transcription is unreliable on technical terms: it wrote "boy" for buoy.

### Inference and response

After reading this tree, the assistant proposed dividing the build by background:

- **Amala:** the referee and the four guards from [Define and Prevent Reward Hacking in the Search Loop](../e9cf4b7a-3426-4266-a93e-e9aa6491ee9d/node.md), plus trying to break each new method version before it is trusted.
- **Alyssa:** the hunt set and the score table. That covers the split between practice and unseen hunts, the improvement curve, whether a gain is real or a lucky run, and the plateau call from [Detect a Plateau in the Improvement Loop](../420ced74-9291-45ef-b2ec-546f2224c283/node.md).
- **Jack:** the loop itself: Telem wiring, the searchers, the improver and the method-version nodes.

The assistant also pointed out that the referee work depends on the scored task and referee, which this tree does not yet record.

Jack answered with the name corrections and "ok save this to hackathon tree following epistemic state mahcine node". The assistant reads that as a request to save, not as assigning the roles. The split is the assistant's inference from short spoken introductions, and the session does not show either teammate being asked about it. No roles are recorded as assigned.

## Source

Pi session `01a1db79-c926-7284-80b0-36135ff23ffd`, November 14, 2026, retained at `artifacts/chats/pi-searchhack-team-intros.jsonl`. The pasted transcript is that session's first user message. No audio recording was supplied.
