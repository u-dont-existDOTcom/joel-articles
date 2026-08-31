# Somatic Therapies — manual humanization writer state

Updated: 2026-08-31
Status: **CURRENT OWNER-DIRECTED WORKING ROUTE / non-authoritative experiment state**

This file exists to prevent the successful manual owner-correction loop from being lost across chats or workers. It is not article authority and does not overwrite `master.html`, owner locks, source evidence, or registered current state.

## Current owner correction

The manual humanization loop had been making better progress than the later supervised/fresh-writer architecture. The problem was not that manual iteration was inherently weak; the problem was that the writer later **forgot the accumulated corrections and reverted to default model prose architecture**.

Therefore the current writing route is:

**fresh attempt from the bounded meaning/function -> Joel reads/tests -> Joel supplies the highest-value correction -> writer treats that correction as new generative information -> reconstruct from scratch around it -> immediately persist the correction and generalized lesson here -> repeat.**

Do not replace this loop with a closed model-only sequence of semantic graph -> model writer -> model critic -> model rewrite unless Joel explicitly asks for that experiment again.

## Runtime role boundary — Chat writes, Codex executes

Owner correction, 2026-08-31: Joel does **not** want to conduct the editorial/humanization conversation with a Codex worker. Codex is not the reasoning/writing authority for this lane.

The runtime split is:

- **ChatGPT reasoning/writing chat:** talks with Joel, writes prose, interprets Joel's corrections, performs editorial reasoning, decides what the next attempt should change, and remains the humanization interlocutor.
- **Codex/execution worker:** mechanical implementation only when needed — repository edits already decided by the Chat/Joel loop, file movement, scripted validation, tests, hashes, packaging, or other execution the Chat cannot directly perform. It must not independently decide prose, infer new editorial architecture, reinterpret Joel's correction, or ask Joel to supervise its writing.
- **Joel:** interacts with the Chat writer. He should not be routed to a Codex worker merely because durable state or mechanical execution is required.

When Chat can persist a correction directly through connected GitHub, do so directly. Do not create a Codex handoff merely to save state.

If Codex is needed for local/repository execution, the Chat supplies it a bounded mechanical contract after the editorial decision has already been made. Codex returns execution evidence to the Chat; the Chat interprets that evidence and continues with Joel.

This role boundary applies to the current Somatic manual-humanization lane and should not be silently reversed by a later worker.

## What must persist between attempts

Before every new Somatic humanization attempt, read this file fresh. After every substantive Joel correction, update this file before the correction can be considered durably learned.

For each correction preserve four things:

1. **What Joel actually objected to.** Do not weaken it into a generic style preference.
2. **The underlying generative mistake.** What internal model operation produced the defect?
3. **What the next attempt must do differently at the level of thought movement.** Do not reduce this to banned words or sentence substitutions.
4. **Whether Joel validated the repair.** A model's own diagnosis is provisional until owner feedback or independent evidence confirms it.

Do not preserve rejected candidate prose as a template. Preserve the lesson, not the realization.

## Current accumulated lessons

### 1. Semantic obligations must not become visible content units

Repeated failure: the writer receives a list of required meanings and silently turns them into consecutive conceptual cards, sentences, or paragraphs.

The important correction is not merely `avoid tidy paragraphs`. It is:

> **Do not treat semantic obligations as rhetorical units that each need explicit realization. Several obligations may live inside one developing thought; some relations can remain implicit when the reader already has them.**

A finished section that can be mapped almost one-to-one from the supplied semantic checklist, in roughly the supplied order, is presumptively failed unless chronology/causality truly requires that order.

### 2. Surface casualness does not change the architecture

Contractions, first person, shorter sentences, casual vocabulary, fragments, or colloquial transitions do not humanize an underlying proposition -> qualification -> explanation/closure essay.

If the hidden outline is unchanged, throw the realization away instead of polishing it.

### 3. The recurring failure is over-completed explanatory packaging

High-risk shapes repeatedly recognized by Joel or durable detector/editorial work include:

- proposition -> qualification -> tidy explanation;
- setup -> qualification -> conclusion repeated paragraph after paragraph;
- balanced contrasts used to organize the thought;
- readiness converted into a checklist;
- conditional possibilities converted into an organized menu/taxonomy;
- a disclaimer explaining that an immediately preceding menu is not actually a sequence;
- polished bridges announcing how one domain relates to another;
- a paragraph explaining or summarizing the implication it has just demonstrated;
- significance staging before simply making the point;
- equalized paragraph completeness;
- explicit synthesis where the reader could make the connection unaided.

These are architecture diagnoses, not phrase bans.

### 4. Owner correction is new cognition, not edit feedback

When Joel says why an attempt fails, do not treat the correction as a request to tweak the bad draft. The correction changes the internal representation of the writing problem.

The normal response is to reconstruct from the semantic/function authority plus the new correction, not to preserve the failed candidate's sentence order and replace wording.

### 5. Closed model-only critique loops are weak at this bottleneck

A model can often diagnose the defect after Joel points to it and still regenerate the same defect on the next attempt. Separate model contexts can share the same generative priors. Formalizing the content into graphs, ledgers, paragraph jobs, or reverse outlines can itself push the prose toward abstract explanatory packaging.

Use self-critique as a secondary safety check, not as the main source of new writing cognition.

### 6. Preservation is a background constraint, not the composition outline

All required claims, attribution, certainty, actors, links, and prohibitions still have to survive. But the preservation inventory should be applied **after** a natural realization exists, not walked through during composition.

If preservation finds a missing unit, do not append a catch-up sentence or paragraph that exposes the checklist. Reconstruct the thought so the missing function lives naturally inside it.

### 7. Do not solve detector problems with donor prose or fabricated humanity

No unrelated Joel prose, Pangram-Human passages, transcripts, Cancer/Romance/Community prose, external human prose, invented autobiography, fake chronology, synthetic specificity, random roughness, typos, slang, or rhetorical devices may be imported merely to influence Pangram.

Human provenance is not insertion authority.

## Current Somatic Introduction failure lesson

The failed fresh Introduction of 2026-08-31 was AI/high-confidence according to Joel's Pangram test. Its defect was visible without the detector:

- opening judgment followed by qualification and a polished mind/body contrast;
- readiness rendered as a three-part checklist followed by a verdict;
- regulation / bodily resolution / EMDR rendered as a clean conditional menu plus sequencing disclaimer;
- inner-child work introduced as a polished cross-domain transfer and compressed into another tidy distinction/resolution.

The crucial correction is that the writer **honored the semantic packet too visibly**. The next attempt must not make the reader feel the preservation checklist underneath the prose.

## 2026-08-31 admission-gate failure — owner correction

Joel asked, `you believe that looks human?` This was a **question, not a rejection**. The Chat incorrectly converted it into a rejection before Joel had supplied that judgment.

The more important failure happened one turn earlier: the Chat delivered a candidate that its own active lesson contract should have blocked. On literal reread, that candidate still visibly reproduced the known package: premise/qualification/explanation, organized readiness logic, a conditional treatment menu, and a polished inner-child transfer. It therefore should not have reached Joel as a candidate worth testing.

Underlying generative mistake:

- the Chat treated the admission receipt as a soft self-review rather than a hard output interlock;
- it rationalized a draft that it did not positively believe had escaped the learned model architecture;
- it effectively used Joel as the first-line quality filter for a regression already detectable from the stored lessons;
- after Joel questioned the result, it inferred a rejection that he had not actually stated.

New operating rule:

> **Owner time is not the fallback QA layer for a known lesson. If the Chat cannot affirmatively defend that the literal candidate clears every active blocking lesson, the candidate is BLOCKED and must not be shown. `Maybe`, `better`, `worth testing`, `Joel can tell me`, or uncertainty about a known failure pattern are not admission states.**

Before delivery, every PASS must have literal-candidate evidence. Any doubt about whether A1/A2/A3/A6/A8 is actually absent is a FAIL for admission purposes, not a reason to externalize the uncertainty to Joel.

Owner-response classification is also blocking: do not silently translate a question, probe, hesitation, or request for explanation into `accepted`, `rejected`, or `corrected`. Record an owner judgment only when Joel actually supplies one or when the semantic content unambiguously entails it.

Validation status of this repair: **process correction is owner-confirmed; prose repair is not yet validated.**

## Manual iteration protocol

For the next attempt:

1. The **Chat writer**, not Codex, reads GitHub canonical article authority as usual.
2. The Chat writer reads this writer-state file fresh.
3. Use only the bounded semantic/function authority for the target span; do not retrieve rejected Introduction prose as a writing source.
4. Write **one** new realization. Do not run three autonomous model-only rewrites before Joel sees it.
5. Perform a light self-check only for obvious semantic loss, invented material, and the known architecture failures above. Do not build a new formal architecture around the draft.
6. Give Joel the candidate directly in Chat **only if the active admission gate is affirmatively satisfied; otherwise discard/reconstruct before delivery.**
7. Treat Joel's response as the primary next-step signal without inventing an acceptance/rejection he did not state.
8. Before writing again, persist any new substantive owner correction and the generative lesson here. Prefer direct connected-GitHub persistence; use Codex only if mechanical execution genuinely requires it.
9. Reconstruct rather than line-edit when the correction concerns thought movement.
10. Continue until Joel says the prose is good enough or authorizes a different route.

## Hard memory rule

A fresh writer must never say or assume `I know the humanization lessons from the prior chat` without reading this file and current GitHub lessons. Chat memory is not the durable store.

If the writer begins repeating a failure already recorded here, stop the attempt before delivery and reread the relevant lesson. The purpose of this file is specifically to prevent the cycle: progress with Joel -> context loss -> rediscovery -> regression.

## Relationship to the supervised-writing experiment

`docs/SUPERVISED-WRITING-ARCHITECTURE.md` and `SOMATIC-INTRO-SUPERVISED-WRITING-20260831.md` are retained as experimental history. They are **not the current primary Somatic writing route** after Joel's 2026-08-31 correction that the manual loop had been making more progress and that the main failure was forgetting what had been learned.

They may still supply secondary diagnostics or be revisited if Joel explicitly requests another supervised architecture experiment. They must not silently replace the manual owner-correction loop.
