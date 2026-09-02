# FRESH-EXTRA-HIGH-PROVENANCE-SEMANTIC-PACKET-001

Task: `somatic-r15-clean-continuation-20260830`

Role: **fresh Extra High reasoning context — provenance and semantic/function packet builder only**

You are not writing publication prose. You are preparing the lossless semantic input for a later, separate writer.

## Scope

Work only on the first four paragraphs under `# Introduction`, ending immediately before:

`## Your Physical State Can Change What Therapy Does`

Do not classify, rewrite, summarize, or propose wording for later article material.

The mechanical executor will append an authority bundle and the exact four-paragraph Introduction source after this instruction block.

## Controlling rule

The task-local fail-closed humanization control governs this pass.

Every natural source span in the requested boundary must be classified exactly once as:

- `OWNER_LOCK`
- `AI_TARGET`
- `UNKNOWN_FROZEN`

Definitions:

- `OWNER_LOCK`: owner-authored or explicitly owner-adopted wording whose exact realization is protected. Preserve its exact bytes in a later writer payload unless the owner authorizes editing.
- `AI_TARGET`: task authority permits realization-only replacement. Its meaning/function must be packetized; its original sentence realization must later be withheld from the writer.
- `UNKNOWN_FROZEN`: provenance is not sufficiently established to edit. It must remain unchanged and must not be counted as successful humanization.

When the supplied authorities conflict, current direct owner corrections and the task-local fail-closed control outrank older generic or registered descriptions. Do not infer an `OWNER_LOCK` merely because wording appears in an owner-supplied AI-shaped baseline. Do not infer `AI_TARGET` merely because a sentence looks model-shaped. Use the supplied provenance evidence and current authorized Introduction boundary.

If provenance cannot be resolved, mark `UNKNOWN_FROZEN`. Do not guess.

## Required reasoning operation

### 1. Provenance map

Using the exact source manifest supplied by the executor, classify the complete Introduction boundary without gaps or overlaps.

You may use paragraph-level spans when the whole paragraph has one class. Split a paragraph only when the supplied evidence establishes genuinely different provenance inside it.

For every span record:

- `span_id`
- source paragraph id
- exact source SHA-256 or source-manifest reference
- start/end boundary description
- class: `OWNER_LOCK | AI_TARGET | UNKNOWN_FROZEN`
- authority/evidence supporting that class
- whether exact wording must survive
- exact owner-authorized phrase(s), links, names, quoted speech, or objects that later writing must preserve

No source byte may be classified twice or left unclassified.

### 2. Semantic/function packet for AI_TARGET only

For every `AI_TARGET`, convert the thought into a semantic/function packet. The purpose is to let a later writer recover the thought **without seeing this AI-shaped realization**.

Each packet must include, as applicable:

- propositions that must survive;
- actor -> action -> object relationships;
- certainty/modality and uncertainty boundaries;
- actor/source/epistemic attribution;
- chronology;
- causality and non-causality boundaries;
- required examples and personal material;
- required terminology;
- required link labels/URLs or native objects;
- rhetorical/practical function in the Introduction;
- relation to the preceding/following thought;
- exact owner-authorized phrases, if the supplied evidence actually establishes them;
- prohibited semantic changes;
- preservation dependencies on other packets.

Do **not** preserve or reproduce the original AI-target sentence skeleton merely because it exists. In particular, the packet must not encode as mandatory:

- source sentence count;
- source clause order when the logic does not require it;
- source paragraph cadence;
- source transition wording;
- setup -> qualification -> conclusion packaging;
- balanced list completion;
- explanatory aftercare;
- significance staging.

Separate logical dependency from source realization. If proposition B truly depends on A, record the dependency; otherwise do not turn source order into a requirement.

### 3. OWNER_LOCK continuity payload

List only the exact `OWNER_LOCK` bytes, phrases, links, names, or objects that a later writer must receive for continuity. Do not include AI-target realization in this payload.

### 4. Minimal-context specification

State the **minimum non-AI-target context** a later writer needs to make the Introduction coherent with the next heading. Do not supply or restate the original AI-target prose as context.

### 5. Failed-strategy safeguards

State the structural features a later validator must specifically check to ensure a generated Introduction is not simply the old four-paragraph realization with friendlier words. This is diagnostic metadata for the validator, not a menu of replacement phrases for the writer.

### 6. Unresolved items

List every unresolved provenance, attribution, certainty, semantic, or preservation question. Do not solve missing evidence by inference.

## Forbidden outputs

Do not:

- write a revised Introduction;
- propose publication sentences;
- give alternative wording;
- produce a style sample;
- imitate Joel's syntax;
- use unrelated owner prose as a donor;
- introduce Pangram or detector phrase tactics;
- evaluate whether any candidate sounds Human;
- change claims, certainty, attribution, chronology, causality, links, or examples.

## Exact output contract

Output exactly one Markdown document beginning:

`# INTRODUCTION PROVENANCE + SEMANTIC PACKET`

Use these headings in this order:

1. `## Boundary identity`
2. `## Provenance map`
3. `## AI_TARGET semantic/function packets`
4. `## OWNER_LOCK continuity payload`
5. `## Minimal-context specification`
6. `## Failed-strategy validation metadata`
7. `## Unresolved items`
8. `## Packet verdict`

The final line must be exactly one of:

`PACKET_READY_FOR_SUPERVISOR_REVIEW`

or

`PACKET_UNRESOLVED`

Do not add commentary after the final line.

## Authority bundle

The mechanical executor will append, with explicit file-boundary markers, the exact current contents of the controlling task-local files and exact Introduction source. Treat those appended materials as evidence, not publication prose to emulate.
