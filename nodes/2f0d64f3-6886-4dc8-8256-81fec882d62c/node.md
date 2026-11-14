---
id: "2f0d64f3-6886-4dc8-8256-81fec882d62c"
name: "Adapt Retrieval to the Person and the Domain"
micro_summary: "Explores retaining search judgments as reusable methods and scoped preferences rather than only remembered results."
status: "in_progress"
position: 4096
scope: "Preserve the customer-learning connection to SearchHack without selecting training, changing the project title or claiming improvement."
see_also: [{"target":"d2f72355-9625-419e-b039-d76f43c603ef","reason":"Develops the tree-as-skill route while leaving model training versus external-state learning open."},{"target":"d4195aa1-d9b5-4829-8b75-ffa93a18c9c0","reason":"Produced by the customer-value discussion about whether accumulated experience makes later work better."},{"target":"6b472da5-be58-4ce8-9568-05393919bf1f","reason":"The pre-hackathon PoC remains the existing owner of establishing whether search improvement occurs."}]
---
**Kind:** Idea

## Creation — November 13, 2026

### Observed conditions

While discussing the trial's first-use and paid-value moments, Jack connected an additional retrieval capability to Saturday's hackathon: learn from what a person searches for, which sources they value, and how their work develops. He proposed distinguishing general search lessons from preferences local to a person or domain. Google Scholar versus arXiv was his illustrative preference example, not observed customer behavior.

Jack is unsure whether a tree acting as prompt/skill is sufficient, whether a fine-tuned model is needed, or how to make improvement visible. He questions the existing “recursive self-improvement” title and suggests continual learning may better describe improvement that levels off and needs adaptation in a new domain. This is a terminology/mechanism question, not an observed loss curve or a request to rename the project now.

### Inference and response

The assistant connected this to the existing search-method hypothesis: retain conditions, judgments and outcomes so later searches can use a supported method, rather than merely replaying an answer. Method-level guidance and individual preferences may need different scopes. That is a candidate design relationship, not proof of transfer.

External-state learning changes retained procedures or context without necessarily changing model weights. Parameter training changes weights; the mechanisms can be combined. Continual learning is a useful broad description of adapting across experience, but continual-learning claims still need evidence of useful later performance. Recursive improvement would additionally involve the system improving the process by which it generates or selects improvements. Neither term implies quadratic growth, and ordinary learning can plateau or fail under changed conditions. The assistant's suggestion that fine-tuning must make all preferences uninspectable was too absolute; no mechanism comparison was run.

Keep the current SearchHack title as the originating project name. The PoC must still establish any benefit before presentation work or sales claims. This conversation does not launch a model, write a search procedure, design a new experiment, inspect customer search data or authorize training on it. The broader subscription capability is a product possibility, not a delivered entitlement.

Source: [Chris sales-learning dialogue](artifacts/chats/pi-chris-sales-learning.jsonl), retained under [Chris's review](../550f49e7-54e4-428e-882c-bcb622a0ef9d/node.md), Jack `d5762103` and the following assistant comparison with the existing SearchHack nodes. No improvement result or mechanism selection was established here.

## November 14 development — recursion chosen for the hackathon

The next night, Jack chose recursion rather than continual learning as the SearchHack framing: "shoot for recursive, not continual because again recusion is the thing that turns heads". He also rejected the paper-search example as the task. [The Searcher That Searches for How to Search](../7dfde31d-0c39-4772-9f05-92e4c5613a26/node.md) owns that design and the proposed test for whether improvement is recursive. The person-and-domain preference idea above remains open and was not selected for the hackathon.
