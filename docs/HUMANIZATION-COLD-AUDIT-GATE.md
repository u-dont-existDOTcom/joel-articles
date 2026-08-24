# Humanization Cold-Audit Gate

Status: **BLOCKING** for substantial production humanization before a candidate may be described as cold-audit clean.

Use with `HUMANIZATION-PRESERVATION-GATE.md`, `HUMANIZATION-ARCHITECTURE-GATE.md`, `project-sources/PRODUCTION-HUMANIZATION-PREFLIGHT.md`, `project-sources/RHYTHM-AND-THOUGHT-SHAPE.md`, and `project-sources/VOICE-REFERENCE.md`.

## 1. Audit the prose, not the drafting history

Cold audit should be detector-blind and rationale-blind as far as practical. Withhold detector scores/windows, experiment history, and prior defenses of the prose. If the current context already knows them, record `context-contaminated`; saying “read it cold” does not erase anchoring.

## 2. No bare self-certification

Before a PASS, identify the three strongest credible model-shape candidates in the natural boundary, or all candidates if fewer than three exist. Anchor each span, diagnose the actual pattern, and give one disposition:

- `repair` — real editorial defect;
- `preserve-with-reason` — genuinely required by evidence, safety, architecture, owner intent, or genre;
- `unresolved` — plausible defect but insufficient authority/evidence to change it.

An unresolved substantive defect means the prose is not cold-audit clean. A PASS cannot consist only of `I see no remaining problem`.

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

## 8. Owner-source wording must survive public-facing context

Owner interviews, chat answers, and editorial explanations are source pools, not transcripts. A sentence can be exact owner language and still be wrong for publication because it was spoken to the editor/model rather than to the reader.

Cold-read the **literal first paragraph under every heading** and every paragraph whose source material was moved. Ask:

- Could a reader understand the first sentence without seeing the private conversation?
- Do pronouns and deictic phrases (`this`, `that`, `it`, `here`, `earlier`, `what I mean`) have visible antecedents?
- Does a referenced term or distinction actually appear before the sentence that refers back to it?
- Is the prose telling the reader why something matters, or telling the editor/model why Joel supplied it?
- Did movement/consolidation delete the antecedent that made a once-valid sentence coherent?

If exact owner wording says things like `this is important because it connects with my other articles`, or otherwise carries private-chat rationale, preserve the thought/provenance but rewrite the wrapper into self-contained reader-facing prose. Verbatimness is not a coherence exemption.

## 9. Publish the conclusion, not the backstage research diary

Source notes often contain epistemic process language: `I thought X`, `I had heard Y`, `I checked it`, `I wasn't sure what the word was`, `the check I did here showed...`. That history can be useful internally without belonging in the article.

Default publication rule: state the best current conclusion directly, with the necessary uncertainty/evidence limit. Keep the `thought → checked → corrected` sequence only when that sequence itself performs a real reader-facing function—for example, a methodological article, a material change-of-mind that advances the argument, a common misconception worth dramatizing, or provenance that the reader needs to assess the claim.

During cold audit, flag research-process narration that exists merely because the source interview contained it.

## 10. The paid-call surprise test is secondary

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
