# Somatic Therapies — manual humanization writer state

Updated: 2026-09-02
Status: **CURRENT OWNER-DIRECTED WORKING ROUTE / non-authoritative experiment state**

This file exists to prevent the successful manual owner-correction loop from being lost across chats or workers. It is not article authority and does not overwrite `master.html`, owner locks, source evidence, or registered current state.

## Current owner correction

The manual humanization loop had been making better progress than the later supervised/fresh-writer architecture. The problem was not that manual iteration was inherently weak; the problem was that the writer later **forgot the accumulated corrections and reverted to default model prose architecture**.

Therefore the current writing route is:

**fresh attempt from the bounded meaning/function -> Joel reads/tests -> Joel supplies the highest-value correction -> writer treats that correction as new generative information -> reconstruct from scratch around it -> immediately persist the correction and generalized lesson here -> repeat.**

Do not replace this loop with a closed model-only sequence of semantic graph -> model writer -> model critic -> model rewrite unless Joel explicitly asks for that experiment again.

**2026-09-02 supersession / stop condition:** the frozen owner-teaching episode showed that this manual loop can itself saturate. Multiple Chat reconstructions remained model-shaped even after repeated substantive rewrites and two same-context cold clears. Once Joel says the attempts are not becoming less model-shaped, stop generating another model variant. The productive next move in this episode was owner re-authoring from the upstream article source, not more model paraphrase. See the post-hoc lesson section below.

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

## 2026-08-31 second owner correction — instruction accretion is not enforcement

Joel then pointed out that the positive-belief rule was substantively **already present in the prior contract**: the old gate already said any substantive FAIL blocked delivery and specifically named the same Somatic architecture as reject-before-owner. Therefore adding A9 cannot be treated as though a new sentence solved the failure.

This is a correction to the process architecture, not another style lesson.

Underlying failure:

- the weakness is not primarily missing policy text;
- the same Chat both generates the prose and judges whether its own generation violates abstract semantic rules, which creates a correlated self-certification failure mode;
- adding more instructions to that same judge can improve salience and traceability but cannot guarantee compliance;
- therefore **do not report a wording-only contract amendment as a reliable fix for an execution failure of an already-clear contract.**

Current mitigation:

1. **Candidate quarantine.** A newly generated Introduction is not yet an owner-facing candidate. Hold it as provisional text while the generation mindset is considered finished.
2. **Separate adversarial admission phase.** Re-read only the literal provisional candidate plus the active lesson contract. The purpose of this phase is to find a reason to block, not to defend the draft or balance strengths against defects.
3. **Fail closed on a credible known-pattern match.** One credible A1/A2/A3/A6/A8 failure blocks the candidate. Do not average it against semantic fidelity or general improvement.
4. **Independent verification when genuinely available.** A fresh independent context/model given only the literal candidate and active contract is stronger evidence than same-context self-certification and should be used when practically available without routing Joel into another writing workflow. A second self-prompt in the same saturated context is not independent verification.
5. **No false guarantee.** In a runtime where no genuinely independent verifier or platform-level output interlock exists, this remains a stronger fail-closed mitigation, not a mathematical guarantee. Do not tell Joel that another instruction line makes recurrence impossible.

This follows the established human-factors distinction between warnings/checklists and stronger error-proofing: a process defect should be addressed by changing the process and introducing a stop/constraint or independent check where possible, not merely by telling the same operator to be more vigilant.

Validation status: **owner has correctly challenged the sufficiency of the first enforcement repair. The stronger quarantine/adversarial mitigation is now active; its effectiveness on the next prose attempt is not yet owner-validated.**

## 2026-09-02 frozen owner-teaching episode — post-hoc lessons

Frozen raw trajectory:
`articles/somatic-therapies/experiments/trajectories/SOMATIC-INTRO-OWNER-TEACHING-TRAJECTORY-20260902-FROZEN.md`

Episode evidence:

- The Chat produced successive owner-facing Introduction attempts after **16**, **8**, and **6** substantive rewrite iterations respectively; each literal delivered candidate had also received two consecutive same-context cold clears.
- Joel still judged the sequence as not getting less model-shaped. His first explicit correction also identified repetition and the generated `I care` stance as fake.
- Joel then returned to the original AI Introduction on Substack and rewrote the thought himself rather than continuing to repair the Chat realization.
- Joel reported that first direct owner rewrite as Pangram **Human / high confidence** and said it was better writing than the model route would have produced even if the model had eventually sounded Human.
- Joel then continued revising that owner-authored realization for source precision, factual wording, mechanics, and an AI-shaped final synthesis. Those later exact bytes were **not** separately reported as a fresh Pangram measurement in this chat; do not inherit the earlier detector result onto them by inference.

### Lesson A — same-context cold clears are not human-shape certification

This episode directly falsified any stronger interpretation of the two-cold-clear rule. Multiple model candidates survived two unchanged same-context clears and still remained visibly model-shaped to Joel.

Use same-context cold passes as a **regression screen**, not as evidence that a passage has escaped the writer's own generative attractor. A cold-clear count can establish that the same context no longer sees a defect; it cannot establish that the defect is gone.

### Lesson B — stop model rewriting when the bounded packet itself becomes the attractor

The repeated model attempts changed wording, length, ordering, and compression while continuing to realize essentially the same bounded semantic packet in recognizably model-shaped form. Once Joel said the attempts were not becoming less model-shaped, continuing to generate variants was low-value.

A bounded meaning/function packet is useful custody, but it can still preserve inherited model-born conceptual topology. When repeated reconstruction cannot escape that topology, **stop model regeneration**. The next route should be genuinely new owner cognition, owner re-authoring from the upstream source, or an owner-authorized reopening of the semantic/architectural authority—not another paraphrase of the same packet.

### Lesson C — owner re-authoring may legitimately change the thought; the model may not do so silently

Joel's successful rewrite did not merely restyle the prior packet. He introduced and reorganized substantive material: the Levine source and Malawi observation, concrete bodily possibilities, the bike-learning analogy, an actual probabilistic three-step recovery sequence, his own epistemic position about the lack of a scientific roadmap, and a different direct relationship to inner-child work.

Those changes were legitimate because the owner made them. A model humanization pass may not infer equivalent semantic changes merely because changing the thought would improve style or detector performance. When the author rethinks the section, update authority from the author; do not pretend the result is only a stylistic rewrite.

### Lesson D — the target is better authorial writing, not merely detector-Human surface

Joel explicitly observed that even if the model had eventually made its version sound Human, his direct rewrite was better. The owner-reported Human/high-confidence result is useful corroboration, but the more important outcome was improved thought and prose.

Do not optimize the Somatic lane toward `make the existing model thought pass`. The real target is the strongest faithful owner-authored article. Detector status remains secondary evidence.

### Lesson E — do not manufacture first-person affect to simulate authorship

Joel explicitly rejected the repeated `I care ... I care ...` construction as fake. The failure was not merely repetition. The model inserted a generic caring-therapist persona as a humanizing surface device.

Use first person when it carries an actual owner judgment, experience, practice, or epistemic position supplied by Joel. Do not add first-person affect merely to make exposition sound personal.

### Lesson F — anti-patterns are diagnoses, not bans; logic comes first

The owner rewrite uses a numbered three-step sequence successfully because Joel is **actually making a sequential claim**. This does not contradict the existing warning against turning a semantic checklist into rhetorical cards.

Do not ban lists, sequences, or explicit structure merely because model prose often abuses them. Ask whether the structure is the author's real thought. Likewise, `tends to follow a general sequence` is probabilistic language and must not be misread as `mandatory stages`. Semantic logic outranks stylistic pattern-matching.

### Lesson G — compression does not cure repetition when the same topology remains

The later Chat candidates became shorter and removed some repeated wording, but Joel still saw the same model shape. Repetition can exist at the level of **thought function and architecture**, not only repeated words or sentences.

When compression leaves the same conceptual sequence intact, do not call that a repaired realization. Change the thought source or stop.

### Lesson H — do not turn the owner's successful surface features into a new model recipe

The owner rewrite contains concrete examples, `Bike Expert`, `kind of obvious`, an explicit sequence, personal epistemic positioning, and other features absent from the failed model attempts. Their value comes from the owner's actual thought and voice in that realization.

Do **not** convert those features into instructions such as `add an analogy`, `add a joke`, `add a list`, or `sound rougher`. Preserve them when owner-authored and functionally right; do not synthesize them as detector tactics.

### Lesson I — unfamiliar claims require source resolution, not automatic flattening

The Levine/Malawi material initially looked stronger and less familiar than expected, but the owner supplied the exact book page. The source supported Levine's description of an innate self-regulatory capacity and the park biologist's observation about captured animals trembling and breathing before release.

Do not weaken an unfamiliar owner claim merely because the model does not recognize it. Inspect the supplied source first. Then preserve the distinction between what the source literally supports, what it corroborates/reinforces, and any stronger owner interpretation.

### Lesson J — protect confirmed idiolect from normalization

`one-one` looked mechanically like a duplicated word, but Joel confirmed it was an intentional phrase he likes. Once confirmed, it is identity-bearing language, not a typo to normalize.

Do not silently standardize unusual owner wording solely because it resembles an error. Ask or preserve when its status is unclear; once owner-confirmed, keep it unless Joel changes it.

Validation status of these lessons: **episode-supported and owner-grounded.** Do not generalize the exact surface devices or detector outcome beyond this lane without new evidence.

## Manual iteration protocol

For the next attempt:

1. The **Chat writer**, not Codex, reads GitHub canonical article authority as usual.
2. The Chat writer reads this writer-state file fresh.
3. Use only the bounded semantic/function authority for the target span; do not retrieve rejected Introduction prose as a writing source.
4. Write **one** new realization into candidate quarantine. Do not run three autonomous model-only rewrites before Joel sees a valid candidate.
5. End the generation mindset. Perform the separate adversarial admission phase against the literal quarantined text, looking specifically for a blocking reason rather than reasons to accept.
6. Give Joel the candidate directly in Chat **only if the active admission gate is affirmatively satisfied; otherwise discard/reconstruct before delivery.**
7. Treat Joel's response as the primary next-step signal without inventing an acceptance/rejection he did not state.
8. Before writing again, persist any new substantive owner correction and the generative lesson here. Prefer direct connected-GitHub persistence; use Codex only if mechanical execution genuinely requires it.
9. Reconstruct rather than line-edit when the correction concerns thought movement.
10. Continue until Joel says the prose is good enough, authorizes a different route, **or says repeated model attempts are not becoming less model-shaped. In that saturation case, stop model generation and wait for genuinely new owner cognition/re-authoring rather than producing another variant.**

## Hard memory rule

A fresh writer must never say or assume `I know the humanization lessons from the prior chat` without reading this file and current GitHub lessons. Chat memory is not the durable store.

If the writer begins repeating a failure already recorded here, stop the attempt before delivery and reread the relevant lesson. The purpose of this file is specifically to prevent the cycle: progress with Joel -> context loss -> rediscovery -> regression.

## Relationship to the supervised-writing experiment

`docs/SUPERVISED-WRITING-ARCHITECTURE.md` and `SOMATIC-INTRO-SUPERVISED-WRITING-20260831.md` are retained as experimental history. They are **not the current primary Somatic writing route** after Joel's 2026-08-31 correction that the manual loop had been making more progress and that the main failure was forgetting what had been learned.

They may still supply secondary diagnostics or be revisited if Joel explicitly requests another supervised architecture experiment. They must not silently replace the manual owner-correction loop.
