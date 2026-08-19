# Idiolect Preservation Protocol — minimum-dose humanization

## Purpose

AI can leave an article semantically similar while making its author less recoverable from the prose. Malik and Awan's *The Assistant Erased You: Measuring Loss of Authorship Signals in AI-Mediated Communication* (arXiv:2608.00926v1, 2026-08-02) measures that loss as **Idiolect Erasure Rate (IER)**: the percentage-point drop in closed-set authorship-attribution accuracy between held-out originals and aligned AI rewrites.

This protocol converts that research into Joel-byline editorial practice. Its primary purpose is **preventing unnecessary idiolect erasure**, not requiring a classifier to approve prose. Joel's current instructions, owner-final prose, meaning, article architecture, and editorial quality remain controlling.

## Research implication

The paper's operationally important result is not merely that models can “sound generic.” Under heavy rewriting, personal blogs and workplace email lost substantial recoverable authorship signal even while the rewritten text remained semantically similar. Grammar-only correction caused much less erasure. Explicitly telling the assistant to preserve the author's voice reduced surface erasure but left most deep authorship signal unrecovered.

Therefore:

> A preserve-voice instruction is a constraint on the worker, not evidence that the result preserved the voice.

The paper also found strong corpus dependence. Standardized Reuters news retained far more attribution than personal or workplace writing under some instruments, partly because topic remained predictive. No model, prompt, or score can be assigned one context-free “voice preservation” number.

## Production prevention rule

Idiolect preservation is achieved primarily by **how the edit is performed**:

- reuse good natural owner prose rather than regenerating it;
- preserve the owner's actual thought route, sequence, under-specification, and stopping point;
- move intact prose when movement solves the architecture;
- use the minimum coherent edit dose;
- remove unnecessary model aftercare, abstract summary, and completion rather than replacing them with new generated polish;
- restore owner wording or localize the repair when a rewrite becomes smoother but less distinctly Joel.

Authorship measurement is secondary evidence. It can warn about drift only when the underlying instrument can reliably recognize the relevant natural-owner condition in the first place.

Closed-set LUAR/SVM/IER calibration is **research tooling, not a routine production-humanization stage**. Do not recruit more comparison authors, expand calibration corpora, or launch new attribution experiments merely to accept or reject current prose. Consult `../docs/IDIOLECT-VALIDATION-STATUS.md` for the current evidence boundary.

The dependency-free single-author retention proxy is also **optional and non-blocking**. Run it only when the comparison boundary is meaningful, the reference corpus is relevant, the cost is trivial, and the result could change a real editorial decision. If no validated or decision-useful retention gate exists, record that limitation and continue under owner authority, semantic fidelity, architecture, cold review, and Pangram's own detector boundary.

## Three independent acceptance axes

Record these separately when applicable. Never collapse them into one verdict.

1. **Semantic/editorial fidelity**
   - claims, allegations, opinions, certainty, actors, chronology, causality, attribution, memories, links, media, rhetorical functions, and article architecture survive;
   - the revised passage still performs its paragraph and section jobs;
   - owner-final language and current owner corrections retain their authority.
2. **Detector status**
   - Pangram or another detector measures only the exact tested reader-visible boundary under its recorded version and conditions;
   - detector output is secondary evidence and never proves authorship, quality, or fidelity.
3. **Authorship-signal retention**
   - when measured, a candidate is compared with a held-out, genre-relevant corpus of actual Joel writing under a named, versioned instrument;
   - this measures movement relative to that corpus, not whether Joel literally wrote the candidate or whether a familiar reader would recognize him;
   - when no valid or decision-useful measurement exists, record `not measured / no validated gate` rather than treating absence of a metric as editorial failure.

Possible combinations matter:

- A passage may be Pangram Human while less attributable to Joel.
- A passage may resemble Joel's corpus while changing his argument.
- A passage may preserve meaning while becoming stylistically generic.
- A passage may retain idiolect but remain detector-red.

No axis certifies another.

## Minimum necessary edit dose

Classify the transformation before rewriting. Use the lowest dose that solves the actual defect.

| Dose | Transformation | Default rule |
|---|---|---|
| `D0` | No reader-visible prose change | Preserve exact text; no idiolect measurement required |
| `D1` | Mechanical spelling, punctuation, capitalization, spacing, or literal agreement correction | Preserve wording and sentence architecture; metric normally unnecessary |
| `D2` | Local repair of a sentence or short span | Reuse owner wording and the existing thought route; optional comparison may be useful when several sentences or distinctive language change |
| `D3` | Sectional reconstruction, rerouting, consolidation, or substantial assistant rewriting | Run the full fidelity/architecture gates and apply the prevention rules. Retention measurement is optional/non-blocking unless a validated, relevant instrument already exists and could change a real decision |
| `D4` | Full regeneration or article-wide rewrite | Presume high erasure risk; preserve natural-owner material and minimize regeneration. Use retention evidence when valid and decision-useful, but do not make unvalidated measurement a publication prerequisite |

Dose concerns transformation, not only length. One short sentence may carry a unique memory, joke, accusation, coined term, moral judgment, or cadence and therefore deserve stricter protection than a longer neutral bridge.

Do not escalate the dose merely because a model can produce smoother prose. Structural movement and sentence rewriting are separate operations. Move an intact owner passage when movement solves the architecture; do not rewrite it automatically.

## Reference-corpus authority

An idiolect profile is only as valid as the prose admitted to it.

Preferred provenance:

1. `owner-authored untouched`;
2. `owner-edited final`;
3. natural published prose independently confirmed as Joel's;
4. `assistant-produced owner-accepted` only when the declared target is the current hybrid publication voice rather than Joel's natural authorship.

Do not silently mix those targets. Label the corpus as `natural-owner`, `current-hybrid`, or another explicit purpose.

Corpus rules:

- Match genre and register when feasible. A polemic, personal essay, research-conversational guide, tender transcript, and private message can have materially different profiles.
- Exclude the evaluated original and near duplicates from the profile. Exact-hash exclusion is necessary but not sufficient.
- Prefer multiple independent samples. Fewer than three samples, fewer than 1,000 reference words, or an evaluation boundary under 50 words is weak evidence and must be labeled as such.
- Keep quoted source material, copied research prose, templates, repeated boilerplate, and other authors' language from dominating the corpus.
- Keep the raw private corpus outside Git unless Joel explicitly chooses a repository destination. Reports should preserve hashes, counts, instrument version, and aggregate measurements rather than source prose.
- Never use article subject matter as proof of style. Topic-sensitive measurements can reward repeated nouns and facts rather than idiolect.

## Optional routine measurement: retention proxy, not IER

The implementation lives in `u-dont-existDOTcom/pangram-humanization-lab` and is intentionally local and non-billable:

```bash
pangram-lab idiolect-retention \
  --profile-dir path/to/private-joel-reference-texts \
  --original path/to/original-visible-text.txt \
  --candidate path/to/candidate-visible-text.txt \
  --output path/to/idiolect-retention.json
```

This routine report compares one original and one candidate with one author profile. It is a **single-author retention proxy**, not IER, because it does not test attribution among multiple known authors.

It is an optional diagnostic, not the prevention engine and not a mandatory gate.

The current instrument records:

- profile-sample, corpus, original, and candidate SHA-256 identities;
- sample and word counts;
- token-change fraction and length ratio;
- lexical-set overlap, explicitly not semantic similarity;
- similarity to the profile under a topic-sensitive `surface` channel;
- similarity under a more content-light function-word, punctuation, contraction, casing, rhythm, and reduced-syntax channel;
- quality flags;
- no raw source prose;
- no calibrated pass threshold.

Interpret the **candidate's movement relative to the original**, not an isolated absolute score. Negative movement on both channels is evidence to inspect the edit. It is not automatic proof of failure. Positive movement is not proof of improvement, authorship, or fidelity.

## Benchmark measurement: closed-set IER

Use the separate benchmark command only for research with at least two authors, disjoint profile/evaluation material, and aligned originals/rewrites:

```bash
pangram-lab idiolect-ier path/to/dataset.json \
  --output path/to/closed-set-ier.json
```

True IER requires:

- a closed set of candidate authors;
- a trained/profiled attribution method;
- held-out original evaluation texts;
- aligned rewrites of those same texts;
- baseline attribution accuracy meaningfully above chance;
- IER reported as baseline accuracy minus rewrite accuracy in percentage points;
- corpus, condition, assistant, attributer, and instrument version reported together.

The lab's dependency-free closed-set implementation is a valid attribution-drop calculation for its named surface/content-light instrument. It is not numerically equivalent to the paper's TF-IDF/linear-SVM or LUAR models. Never present Joel-only proxy results as IER.

A closed-set benchmark may improve the reusable anti-erasure system if it answers a predeclared research question. It is not required merely because an article contains D3/D4 edits.

## Editorial procedure for `D3` and `D4`

1. **Freeze authority.** Record the authoritative original, reader-visible comparison boundary, current revision/hash, and owner locks.
2. **Map meaning.** Complete the source–meaning–context–destination ledger, protected rhetorical functions, claim/certainty assignments, and actor → action → object relations.
3. **Define the target.** State whether the desired voice is natural Joel, current hybrid publication voice, or a section-specific register.
4. **Preserve before generating.** Identify natural owner prose, thought routes, transitions, under-specification, jokes, memories, and stopping points that can survive intact. Do not rebuild what can be moved or locally repaired.
5. **Make the smallest coherent change.** Prefer owner wording, owner realizations, intact movement, local repair, and deletion of unnecessary model aftercare over new generation.
6. **Run editorial gates first.** Semantic sanity, reality contact, curious-reader chain, architecture regression, fidelity, provenance, orphan/dependency audit, and cold prose-shape review remain blocking.
7. **Decide whether retention measurement is useful.** Check the current validation status. Run the optional proxy or another already-validated instrument only when the corpus/boundary are meaningful and the result could alter a real decision. Otherwise record `not measured / no validated gate` and do not create a research detour.
8. **Diagnose drift rather than imitate tics.** Whether drift is found by human review or optional measurement, inspect whether the candidate:
   - replaced an owner route with abstract summary;
   - standardized sentence rhythm or paragraph endings;
   - removed natural under-specification;
   - expanded caveats or interpretive aftercare;
   - converted lived observation into complete framework prose;
   - replaced contractions or ordinary syntax with institutional language;
   - routed a thought to the wrong section;
   - regenerated prose that only needed to be moved or lightly repaired.
9. **Reduce dose before decorating.** Restore owner language, recover the actual owner realization, localize the repair, or preserve a necessary neutral bridge. Never manufacture errors, fake concreteness, autobiographical detail, catchphrases, unusual punctuation, slang, or corpus tics to raise similarity.
10. **Run Pangram under its own rules.** Use the exact reader-visible boundary, current version, cache, paid-call cap, and durable evidence. Do not use the idiolect result to predict or substitute for Pangram.
11. **Select under authority.** When candidates are equally faithful and coherent, prefer the lower-dose candidate. If valid retention evidence already exists, it may be one tie-breaker. A clearly better owner-selected sentence outranks the metric.
12. **Report all applicable axes.** State fidelity/architecture and detector status. State authorship-retention evidence when measured; otherwise state that no validated or decision-useful retention gate was used.

## No universal pass threshold

Do not create or imply a global threshold such as “retain 90%” or “similarity must exceed 0.7.” The local score depends on:

- corpus composition and size;
- genre/register match;
- passage length;
- topic overlap;
- quoted material and formatting;
- attribution method;
- instrument/version;
- baseline profile fit of the original;
- edit purpose and dose.

A useful measured result includes the original baseline, candidate movement, both channels, quality flags, and human inspection. Thresholds require separate calibration against owner judgments and held-out known-good/known-bad cases for a defined genre and instrument.

## Failure-resistant interpretation

Do not infer any of the following:

- `Pangram Human` means Joel's idiolect survived.
- High profile similarity means Joel wrote or approved the text.
- Low profile similarity authorizes changing owner-final prose.
- Absence of an idiolect measurement means a faithful, architecture-sound edit failed.
- A low token-change fraction guarantees fidelity.
- A preserve-voice prompt succeeded because it named voice.
- One author profile can validate every genre.
- A surface proxy reproduces deep authorship representation.
- The paper proves familiar human readers cannot recognize an author.
- Erasure is always harmful; reduced attributability may be desirable for privacy or anonymity.

For Joel's byline, preservation is the chosen objective. It is not a universal moral rule.

## Required report block

For substantial humanization/reconstruction, record:

```text
Edit dose: D0 / D1 / D2 / D3 / D4
Authoritative original: <path/revision/SHA-256>
Candidate: <path/revision/SHA-256>
Target voice: natural-owner / current-hybrid / named register
Reference corpus: <identity/provenance/genre/counts/hashes, or not used>
Corpus exclusions/contamination risks: <... or not applicable>
Semantic/editorial fidelity: PASS / FAIL / unresolved, with reasons
Architecture regression: PASS / FAIL / unresolved, with reasons
Pangram: exact boundary/version/result or not run/not required
Authorship retention: <instrument/result/limitations, or not measured — no validated/decision-useful gate>
Interpretation: <directional evidence only when unvalidated; no uncalibrated pass claim>
Substantive claim changes: none / exact list
Remaining weakness or unavailable evidence: <...>
```

## Repository boundary

- `joel-articles` owns this editorial protocol, source authority, corpus provenance policy, edit-dose classification, article acceptance, and promoted article lessons.
- `pangram-humanization-lab` owns the implementation, tests, metadata-only idiolect reports, closed-set research harness, detector evidence, and method limitations.
- Neither repository may use a metric to silently soften, qualify, remove, or otherwise alter Joel's argument.
