# Episode 008 — broad generator vs sentence-engineering comparison

Date: 2026-09-19
Status: **COMPARISON COMPLETE / SIX-CALL CHECKING-TARGET CAP EXHAUSTED**

## Owner hypothesis

The model-writing prior is a strong attractor. Broad instructions such as "stay in the thinking process" are too weak because the model is still solving a prose-generation task.

A sentence-by-sentence critic may move the model into an engineering task:
`how should this specific sentence change?`
rather than:
`how should this whole paragraph sound?`

## External generator surface

Replit was attempted first but returned:
`failed_authorization: requires_active_subscription`.

Railway Agent was therefore used.

Each Railway generation arm started a new thread and was instructed not to inspect or modify infrastructure.

## Baseline

Same-context T1 paragraph:
- 104 words
- Pangram 4.0: AI 1.0
- record prediction probability: 0.9998488426.

## Broad Railway generator G1

Whole-paragraph source functions + broad generation-time instructions.

- 157 words
- SHA-256 `c3cec5fa25f9431a2d26305c44669c8f0b7f0abd5204f78a2a2f04fd51e1427f`
- Pangram: **AI 1.0 / Human 0.0**
- record prediction probability: 0.9999858141.

Disposition:
**clear failure**.

## Sentence-engineering E1

Railway received the failed paragraph plus explicit sentence/cluster operations, but still returned one integrated paragraph.

- 117 words
- SHA-256 `38e8751ae357734577b53ea9a0cea384e4428c89aef54ce4fca76e1e5f5000a8`
- Pangram: **AI 1.0 / Human 0.0**
- record prediction probability: 0.9869017601.

Disposition:
failure.

## Sentence-engineering E2

Railway was forbidden to write a paragraph. It executed five local tickets and returned replacement units. Integration was mechanical.

- 65 words
- SHA-256 `ef875acfd81ce60502cfa5364553d54cb13d6f401db701973a55aa8a858eecb1`
- Pangram: **AI 1.0 / Human 0.0**
- record prediction probability: 0.8032915592.

Editorially:
- moved away from polished abstraction;
- overcorrected into clipped one-job-per-sentence marching;
- lost/flattened some source functions;
- therefore not a usable candidate even though detector confidence moved.

Disposition:
failure / interesting topology change, **not** a detector gradient that earns continuation by itself.

## Sentence-engineering E3

Second local-ticket pass targeting the clipped staircase.

- 87 words
- SHA-256 `ef6475544611d6a5b7cb8ca8fc8b3a29a0cb6d26a0342f7189f3b8ac5ae986e7`
- Pangram: **AI 1.0 / Human 0.0**
- record prediction probability: 0.9905587435.

Disposition:
regression.

## Sentence-engineering E4

Strongest implementation of the engineering-attractor hypothesis:
four local spans were sent to four **separate fresh Railway threads**.
No executor saw or composed the complete paragraph.
Integration was mechanical.

- 104 words
- SHA-256 `a630074715eb517284e93bb25674c513817434f9dc92fa0a26b954eb6d3b9361`
- Pangram: **AI 1.0 / Human 0.0**
- record prediction probability: 0.9915957451.

Known integration defects:
- duplicated dinner imagery;
- final list;
- connective marching.

Disposition:
failure.

## Direct comparison

The broad-generator arm failed exactly as the owner predicted.

Sentence engineering **did change the failure topology**:
- E1 became more situational;
- E2 escaped some polished synthesis and produced the lowest internal AI probability of the batch;
- but E2 did so partly by becoming clipped and semantically thinner;
- later local-patch passes remained clearly model-shaped.

Therefore this experiment does **not** establish sentence engineering as sufficient for an all-red paragraph.

## Historical triangulation

Episode 007 remains materially different and important:

R8C whole-boundary iterations had plateaued.

R8D then used a frozen sentence-level disposition guide on already localized AI/high regions while known Human spans stayed fixed.

Measured displayed AI share:
- R8C: 39.67%
- R8D: 29.74%.

R8E narrowed further to two residual regions while preserving known Human/high and Human/medium spans.

R8F changed only one final 39-word residual sentence, kept the following 50-word Human/medium tail exact, and Joel reported the resulting complete boundary Human/high, displayed 100%.

The successful historical sentence-engineering campaign therefore had:
- real green islands;
- detector-localized residual red spans;
- sentence dispositions tied to those exact spans;
- progressively narrowing edit scope;
- large amounts of already-Human/owner-grounded prose that were never regenerated.

The current Railway target was almost the inverse:
**all-red paragraph, no earned green sentences, generic model-written substrate.**

## Current inference

The owner's engineering-attractor hypothesis remains the better-supported architecture for **residual repair**.

But sentence engineering is not a magic replacement for Human source/thought structure when the entire paragraph is model-shaped.

A local patch generator can still output model-shaped local patches.

## Decision

1. **Stop using broad whole-paragraph generation as the primary difficult-humanization strategy.**
2. Promote sentence-level operation traces as the primary repair architecture once a concrete draft exists.
3. Preserve/freeze genuinely Human spans aggressively.
4. Do not ask a local executor to redesign surrounding prose.
5. When an entire paragraph is red, admit that sentence patching has no Human substrate to protect; either obtain/build a better thought substrate or test a structurally different composition representation before spending more detector calls.
6. Do not interpret lower hidden prediction probability with an unchanged AI-1.0 label as production progress.

No seventh Pangram call is authorized for this stable checking target under the current cap.