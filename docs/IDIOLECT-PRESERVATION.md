# Idiolect Preservation in Joel-Byline Humanization

Status: **active editorial guard; quantitative layer provisional.**

This document integrates authorship-preservation research into the article workflow without turning stylometry into a new editorial authority.

Research basis: Malik and Awan, *The Assistant Erased You: Measuring Loss of Authorship Signals in AI-Mediated Communication* (arXiv:2608.00926, 2026). The authors show that AI rewriting can preserve semantic content while materially weakening computational authorship signals, that heavier rewriting erases substantially more than light correction, and that an explicit `preserve voice` prompt is not sufficient evidence of preservation.

The computational protocol and future experimental evidence belong in `u-dont-existDOTcom/pangram-humanization-lab`, beginning at `docs/IDIOLECT-PRESERVATION-PROTOCOL.md`.

## 1. The editorial problem

Joel-byline humanization is not a conversion from "AI text" to "generic human text."

The target remains:

- Joel's actual thought;
- correct claims, actors, causality, chronology, certainty, and attribution;
- the route by which the thought makes sense;
- protected rhetorical functions;
- Joel's natural register and idiosyncratic choices where they are real and useful;
- the smallest repair that solves the diagnosed problem.

A detector can improve while the prose becomes less Joel-like. That is a failed byline edit even when the candidate is semantically similar.

## 2. Always-on rule: minimize transformation dose

Default to the least rewriting that solves the actual defect.

Use this order when the underlying thought is sound:

1. no change;
2. P1 mechanical correction;
3. bounded local repair;
4. paragraph/section reconstruction only when the architecture requires it.

Do not escalate to broad "clarity," "professionalism," balance, symmetry, or completeness as a generic polishing pass.

When inherited model architecture is itself wrong, reconstruction can be more faithful than local preservation. Minimum-edit does **not** mean protecting an AI-shaped skeleton.

## 3. Preserve real idiosyncrasy, not simulated quirks

Potential authorship signal can live in ordinary features that models often normalize:

- characteristic word choices and conversationally sufficient modifiers;
- contractions and sentence joins;
- function-word preferences;
- punctuation and parenthetical rhythm;
- sentence-length variation and uneven emphasis;
- how a thought revises itself;
- where Joel stops instead of summarizing;
- register-specific directness, humor, tenderness, or technical density.

Preserve these when they are natural to the source and do not obscure meaning.

Never insert typos, awkwardness, fake hesitations, arbitrary fragments, catchphrases, slang, or strange punctuation to make text more "human" or more attributable. Humanization must recover actual author signal, not perform a stylometric costume.

## 4. A voice-preservation prompt is not a gate

Instructions such as `preserve the author's voice`, `sound like Joel`, or `keep his style` describe what the model was asked to do. They do not establish what the resulting text did.

Judge the literal output against:

- owner authority;
- source provenance;
- article architecture;
- the voice reference and relevant natural corpus;
- the cold prose-shape audit;
- detector evidence when requested;
- calibrated idiolect evidence when available.

Prompt wording is never acceptance evidence.

## 5. Natural-owner corpus hygiene

When a worker or tool compares prose to Joel's reference corpus, keep provenance classes distinct.

The primary natural-owner profile should favor:

- natural Joel-authored/publication prose with reliable provenance;
- owner-final prose known to be substantially Joel's;
- natural owner rewrites made for meaning/editorial reasons rather than to manipulate a detector.

Do not silently train the primary profile on:

- assistant-generated prose merely accepted by Joel;
- synthetic probes;
- detector-targeted owner minimal pairs;
- assistant/owner mixtures whose provenance cannot be separated.

Those artifacts remain useful as experiments and comparisons. They do not become evidence of native Joel style merely because Joel accepted them.

Keep register labels visible. Joel's research-conversational, practical, tender/personal, and polemical registers should not be collapsed into one average voice.

## 6. Quantitative idiolect evidence is conditional

Do not invent a Joel "voice score."

If `pangram-humanization-lab` later supplies a calibrated idiolect-retention measurement, verify that its evidence record shows:

- held-out natural-owner data;
- document/source-separated splits;
- baseline attribution meaningfully above chance;
- topic/content controls;
- register handling;
- style-sensitive attribution rather than semantic similarity alone;
- exact source/candidate identity.

Until those conditions are satisfied, computational authorship measurements are research diagnostics only.

Use `IER` only for the actual corpus-level attribution-accuracy drop defined by the research protocol. A single passage similarity or classifier probability is not IER.

## 7. Humanization acceptance order

For Joel-byline prose, apply the gates in this order:

1. **Owner/meaning gate** — claims, certainty, actors, causality, chronology, attribution, memories, and protected functions survive.
2. **Article architecture gate** — heading promise, paragraph jobs, live-question chain, placement, and stopping point still work article-wide.
3. **Idiolect guard** — the repair has not needlessly normalized real Joel-specific language or thought movement; use calibrated computational evidence only when its protocol is valid.
4. **Pangram gate when requested** — exact reader-visible intended delivery boundary must satisfy the repository's current Pangram acceptance rule.
5. **Minimum-dose comparison** — if multiple candidates pass the prior gates, prefer the faithful candidate that accomplishes the repair with less unnecessary transformation.

A Pangram pass cannot override gates 1–3.

## 8. Detector-red repair sequence

When a passage is detector-red:

1. diagnose the semantic/architectural problem before paraphrasing;
2. search the article/source pool for an existing Joel realization that belongs in the failing function;
3. make the smallest faithful repair;
4. re-run the article-wide architecture regression;
5. audit whether the change normalized distinctive owner language, rhythm, or reasoning;
6. test the exact reader-visible boundary when Pangram is required;
7. if a calibrated idiolect layer exists, compare retention as an independent axis rather than folding it into the Pangram score.

Do not spray stylistic changes across already-good prose to move a detector.

## 9. Pangram-green but less Joel-like

If Pangram becomes green but the candidate is materially less Joel-like by owner judgment, source comparison, or calibrated idiolect evidence:

- reject the candidate as a Joel-byline final;
- restore higher-authority owner wording as far as possible;
- localize the detector interaction;
- repair only the remaining failing function;
- preserve the disagreement in the detector/editorial record.

This is an expected multi-objective conflict, not evidence that one instrument is "wrong."

The IER paper uses `double erasure` for a narrower experimental condition: loss of human-author attribution plus failure of AI-text detection. In article records, use `double-erasure-like byline failure` only when useful and do not imply the exact research condition was measured.

## 10. Relationship to existing authority

This document adds an objective; it does not reorder authority.

- Joel's direct owner correction and registered article authority remain highest.
- Semantic fidelity and article function remain hard gates.
- `project-sources/VOICE-REFERENCE.md` remains the qualitative voice decision model.
- `project-sources/HUMANIZATION-AND-COHERENCE.md` remains the reconstruction protocol.
- `project-sources/FINGERPRINT-PASS.md` remains the cold/adversarial audit.
- Pangram remains secondary detector evidence with the current exact-boundary rules.
- `pangram-humanization-lab/docs/IDIOLECT-PRESERVATION-PROTOCOL.md` owns the quantitative research design and future scorer evidence.

The practical change is simple: **do not call prose humanized merely because it became less AI-detectable. It also has to remain Joel's.**
