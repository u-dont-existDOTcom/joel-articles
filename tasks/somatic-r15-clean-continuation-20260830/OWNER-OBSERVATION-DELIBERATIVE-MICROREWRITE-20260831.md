# OWNER OBSERVATION — HIGH-COMPUTE MICRO-REWRITE

Date: 2026-08-31

Task: `somatic-r15-clean-continuation-20260830`

Status: **DIRECT OWNER PROCESS OBSERVATION / STRATEGY EVIDENCE, NOT DETECTOR RESULT**

Joel reports that his best model-only humanization progress has occurred in ChatGPT **Pro** mode and **Work Ultra** mode when he gives the model a very small writing scope and explicitly asks it to iterate repeatedly before answering.

The observed working pattern is approximately:

- one paragraph at a time rather than a whole article;
- high-compute Pro or Work Ultra mode;
- instruction to keep iterating/revising until the model itself believes the paragraph is done;
- substantial private deliberation before one final visible output;
- a single paragraph can occupy roughly ten minutes of model work;
- Joel estimates that such passes can produce prose that is roughly `70% humanized` by his own reading.

`70% humanized` here is an owner qualitative estimate. It is **not** an exact Pangram fraction and must not be entered into the detector ledger as one.

## Why this is new evidence for the current strategy review

The existing fresh Pro and Extra-High Somatic whole-article runs did not test this condition.

The recorded Pro run used one approximately 4,477-word prompt to request one complete whole-article revoice. It used GPT-5.6 Sol, `Pro, 5 of 5`, one user message, and ran from 2026-08-31T10:44:15Z to 10:55:55Z before returning one complete article.

The recorded Extra-High run similarly used one approximately 4,573-word prompt to request a complete whole-article revoice in one response. It used GPT-5.6 Sol, `Extra High, 4 of 5`, one user message, and completed after an extended generation/recovery interval.

Those runs therefore confounded high inference effort with a very large simultaneous coverage problem. Neither frozen prompt instructed the model to spend its effort repeatedly rewriting one paragraph until its own cold read stopped finding improvements.

The owner observation makes **scope × deliberation depth × repeated revision** a distinct untested production variable. It should not be dismissed merely because one-shot whole-document Pro/Extra-High rewriting failed.

## Strategy implication

Treat high-compute internal iteration as a candidate **search mechanism**, not a certification mechanism.

A strong writer may repeatedly generate, inspect, discard, and rebuild a tiny prose unit before emitting one final candidate. Separate preservation/provenance and cold-reader gates still determine whether that visible candidate is admissible. The writer's confidence that it is done cannot certify semantic fidelity or authorship.
