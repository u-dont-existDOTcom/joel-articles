# Humanization Cold-Audit Gate

Status: **BLOCKING** for substantial production humanization before a candidate may be described as cold-audit clean.

Use with `HUMANIZATION-PRESERVATION-GATE.md`, `HUMANIZATION-ARCHITECTURE-GATE.md`, `project-sources/PRODUCTION-HUMANIZATION-PREFLIGHT.md`, `project-sources/RHYTHM-AND-THOUGHT-SHAPE.md`, and `project-sources/VOICE-REFERENCE.md`.

## 1. Audit the prose, not the drafting history

Cold audit should be detector-blind and rationale-blind as far as practical. Withhold detector scores/windows, experiment history, and prior defenses of the prose. If the current context already knows them, record `context-contaminated`; saying “read it cold” does not erase anchoring.

## 2. No bare self-certification

Before a PASS, identify the three strongest credible model-shape candidates in the natural boundary, or all candidates if fewer than three exist. Anchor each span, diagnose the actual pattern, and give one disposition:

- `repair` — real editorial defect;
- `preserve-exact-realization-with-specific-reason` — the **current realization itself**, not merely its underlying meaning/function, is genuinely required by evidence, safety, architecture, owner intent, quotation/provenance, or genre;
- `unresolved` — plausible defect but insufficient evidence to clear or repair it.

An unresolved substantive defect means the prose is not cold-audit clean. A PASS cannot consist only of `I see no remaining problem`.

**Preservation authority cannot discharge the humanization audit.** `This function is source-protected`, `this distinction is required`, `preservation passes`, or `the source is dense` may justify retaining the cognition; none, by itself, justifies the present wording, cadence, paragraph allocation, checklist topology, or other realization. If the meaning must stay but the packaging is model-shaped, repair the packaging.

Before dispositioning the candidates independently, aggregate them at paragraph/section scale. Several individually `mixed` features can form one definite cumulative failure. In particular, repeated question/command/verdict/lesson units, compact distinctions, efficient causal summaries, and short hard stops can collectively become instruction-manual/listicle cadence even when none is independently disqualifying.

## 3. Saturated same-context audits are provisional

After repeated rewrites, detector-localized editing, or accumulated preservation rationale, the drafting context may still diagnose useful problems but cannot independently certify that none remain. Label its result `PROVISIONAL SAME-CONTEXT AUDIT`. When a genuinely fresh reader is practically available, use the independent-final-reader rule in `SKILL.md` before final promotion/publication quality claims. If unavailable, state the limitation instead of claiming unqualified cleanliness.

## 4. Preserve genre; do not inflate anecdotes

Humanization must not make a research/practical article more autobiographical merely because personal passages appear detector-favorable.

Personal experience may supply a reason for inquiry, origin of a judgment/hypothesis, concrete consequence/test, provenance distinction, or necessary example. It is not a general cure for model-shaped prose and is not a substitute for external evidence.

Before adding a personal passage ask: what article function does it perform, what substantive thought would be lost without it, and would the article become more memoir-like than its intended function warrants? If the real reason is detector optimization, do not add it.

## 5. Fresh owner language is not synonymous with anecdote

When owner input is genuinely needed, request the missing authorial cognition: judgment, reasoning route, priority, ranking criterion, distinction, uncertainty, disagreement, selection principle, desired reader action, or what can be cut. Ask for lived experience only when lived experience itself performs a real article function. Never request a personal story merely to influence a detector.

## 6. Preserve function, not inherited model packaging

The preservation gate protects meaning, provenance, agency, certainty, chronology, unique examples, protected functions, links/media, and necessary context. It does not make every inherited bridge, list, recap, caveat shell, paragraph count, or modality-card wrapper a protected function.

During an authorized humanization pass, do not create preservation units for realization-only model scaffold merely because it appears in the registered working candidate. Preserve the underlying semantic/protected units. If a generic bridge, exhaustive list, duplicated aftercare block, recap, balanced caveat wrapper, or first-person skin adds no unique function, authorize its removal/consolidation explicitly in the change whitelist and prove that every real function survives.

Registered authority determines the controlling article/source. It does not imply that every current prose realization is owner-final or stylistically untouchable.

## 7. Technical prose may stay technical

Research/practical writing legitimately needs mechanisms, evidence distinctions, citations, warnings, and instructions. Do not convert necessary technical material into autobiography. The repair target is unnecessary packaging: false symmetry, duplicate caveat architecture, comprehensive closure, generic recap, or taxonomy that exists mainly to complete the form.

## 8. Reader model and why-now are blocking

Before a PASS on any new or substantially rewritten section, state explicitly:

- **primary reader at this exact point:** who the prose is talking to;
- **reader state:** what the reader has just learned, felt, or is trying to do;
- **why now:** what preceding thought creates the need for this section/sentence now;
- **reader consequence:** what understanding, decision, recognition, or action changes because this passage exists.

If those answers are unclear, conflict with the article's audience contract, or require inventing a clinician/helper/evaluator audience that the surrounding article did not establish, the passage fails reader-facing realization even when every sentence is locally coherent.

Ask the plain question Joel used in the Inner Child safety correction: **Who are you talking to, and why would they care about what you're saying?** Treat inability to answer from the visible article as a structural defect, not a request for more explanatory aftercare.

## 9. Owner-source wording must survive public-facing context

Owner interviews, chat answers, and editorial explanations are source pools, not transcripts. A sentence can be exact owner language and still be wrong for publication because it was spoken to the editor/model rather than to the reader.

Cold-read the **literal first paragraph under every heading** and every paragraph whose source material was moved. Ask:

- Could a reader understand the first sentence without seeing the private conversation?
- Do pronouns and deictic phrases (`this`, `that`, `it`, `here`, `earlier`, `what I mean`) have visible antecedents?
- Does a referenced term or distinction actually appear before the sentence that refers back to it?
- Is the prose telling the reader why something matters, or telling the editor/model why Joel supplied it?
- Did movement/consolidation delete the antecedent that made a once-valid sentence coherent?

If exact owner wording says things like `this is important because it connects with my other articles`, or otherwise carries private-chat rationale, preserve the thought/provenance but rewrite the wrapper into self-contained reader-facing prose. Verbatimness is not a coherence exemption.

## 10. Publish the conclusion, not the backstage research diary

Source notes often contain epistemic process language: `I thought X`, `I had heard Y`, `I checked it`, `I wasn't sure what the word was`, `the check I did here showed...`. That history can be useful internally without belonging in the article.

Default publication rule: state the best current conclusion directly, with the necessary uncertainty/evidence limit. Keep the `thought → checked → corrected` sequence only when that sequence itself performs a real reader-facing function—for example, a methodological article, a material change-of-mind that advances the argument, a common misconception worth dramatizing, or provenance that the reader needs to assess the claim.

During cold audit, flag research-process narration that exists merely because the source interview contained it.

## 11. The paid-call surprise test is secondary

`Would an AI result surprise me?` cannot override an identified editorial defect. First complete the adverse-span audit, genre/anecdote check, inherited-scaffold check, reader-facing realization check, and research-process compression check; only then use subjective surprise as an additional readiness question.

## Required receipt

```text
Natural boundary: <span>
Audit context: fresh / context-contaminated
Detector/rationale blindness: yes / no
Genre target: <type>
Strongest candidate 1: <span + diagnosis + disposition>
Strongest candidate 2: <span + diagnosis + disposition>
Strongest candidate 3: <span + diagnosis + disposition>
Cumulative mixed-pattern aggregation: NONE / <pattern + disposition>
Primary reader here: <who>
Reader state / live pressure: <what is happening for them here>
Why now: <preceding thought that creates this need>
Reader consequence: <what changes for the reader>
Anecdote-inflation check: PASS / FAIL
Fresh owner input needed: judgment/reasoning/etc. / lived example genuinely needed / none
Inherited-scaffold check: PASS / FAIL
Reader-facing realization check: PASS / FAIL
Heading-opening / antecedent check: PASS / FAIL
Research-process compression check: PASS / FAIL
Technical/evidence density preserved: PASS / FAIL
Same-context status: CLEAN / PROVISIONAL
Independent-reader status: PASS / findings / unavailable
Largest remaining weakness: <exact>
Cold-audit conclusion: CLEAN / PROVISIONAL / FAIL
```

This gate was added after the Somatic Therapies r07 workflow showed that a preservation-clean, preflight-passing candidate could still contain obvious model-shaped guide structure while the same drafting context certified it as clean and began drifting toward additional anecdotes as the next humanization strategy. It was hardened again after later Somatic review showed two additional failure modes: direct owner-interview wording could retain private-chat framing that did not make sense to a public reader, and internal research-process narration could be copied into prose even when only the final conclusion belonged in the article.
