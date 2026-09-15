# Inner Child Therapy — humanization writer state

Updated: 2026-09-15

Status: **ACTIVE PARAGRAPH-LEVEL OWNER-TEACHING LOOP / article still unregistered**

## Current episode state

Episode 001 produced the first prospective retrieval-first transfer success. The exact candidate tested Human / low confidence, while both the model cold read and Joel independently identified its final tidy sentence as still model-shaped. That sentence was deleted because the following paragraph already carried the leadership function.

Episode 002 then transferred the lesson to a different source paragraph in one pass. The repaired paragraph 1 plus model-generated paragraph 2 remained owner-reported Human / low confidence.

Episode 003 is the first clear detector-instability teaching case. The exact model candidate at SHA-256 `95cd572da40a2588744d7958ec5fb3938880eb42de092fbfc9ed40ad7c7684d4` initially tested AI / low confidence. Four fresh Pangram 4 API repeats on the exact same bytes then returned Human, Human, Human, AI, all at Medium confidence. The repeat experiment therefore establishes that this candidate sits on an unstable detector boundary.

Joel supplied an aligned same-thought rewrite at SHA-256 `04378a6a51cc40b8bab131f72480c28e8cc3969d16612f9ba0448cc1083d7ef1`, owner-reported Human / low confidence.

Exact Episode 003 bytes, repeat results, and call accounting are frozen in `experiments/EPISODE-003-RESULT-20260915.json`.

## Direct owner correction — instability is not acceptance

The prior inference that we should stop rewriting the Episode 003 model candidate because its single AI result might be detector noise is **superseded**.

The correct distinction is:

- the 3-Human / 1-AI repeat distribution means the detector label is unstable and must not be described as reliable evidence that the prose is intrinsically AI-authored;
- but Joel's production goal is not majority-Human or pass-once behavior. He wants Pangram to recognize the intended delivery boundary as solidly Human rather than randomly flip;
- therefore a candidate already shown to flip AI across fresh exact repeats is **not an accepted production humanization endpoint**;
- detector instability is a reason to continue faithful repair or use a stronger owner-aligned realization, not a reason to preserve the borderline candidate;
- the known-green calibration guard does not protect a candidate whose current exact repeat evidence is contradictory;
- short-boundary noisiness affects confidence and testing strategy. It does not convert a demonstrated flip into completion.

This correction is about the acceptance criterion, not detector authorship provenance. Pangram red does not prove AI authorship, and Pangram green does not override editorial defects. Meaning, fidelity, owner language, and article architecture still outrank detector optimization.

## Current production method

1. Retrieve the closest literal owner-teaching demonstrations before generation.
2. Preserve the complete source thought and paragraph job.
3. Cold-read the whole natural boundary. If a credible model-shaped feature remains, repair it before paying Pangram.
4. Use Pangram to validate a fully considered candidate, not to draft by trial and error.
5. If fresh exact repeats expose a real Human/AI flip, preserve the repeat distribution and treat the candidate as detector-unstable rather than averaging the labels into a pass.
6. Continue faithful repair until the intended delivery boundary meets Joel's standing Humanization gate. Do not manufacture quirks, factual changes, or owner imitation merely to create detector margin.
7. Use repeat testing selectively when instability is already demonstrated or when a repeat will change the acceptance decision; do not repeatedly buy confidence on every short paragraph.

## Episode 003 disposition

The model candidate `95cd572d…684d4` is **rejected as a production baseline because it is detector-unstable**.

Joel's aligned rewrite `04378a6a…d7ef1` is the current teaching target and is owner-reported Human / low confidence. It has **not** been established as repeat-stable, so do not call it robustly certified yet.

The correct next certification unit should be the natural reader-visible boundary actually intended for delivery, not an arbitrarily tiny snippet. If that boundary itself shows contradictory fresh results, keep humanizing rather than treating the contradiction as a reason to stop.

## Authority boundary

The raw Substack editor source is hash-bound and the owner-teaching experiments are durable, but the Inner Child Therapy article family is still unregistered. These teaching candidates are non-authoritative experimental realizations until the complete article family is created and registered. Do not silently promote them into a canonical master before that authority step.
