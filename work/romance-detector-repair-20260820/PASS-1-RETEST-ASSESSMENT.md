# Romance detector repair — pass 1 retest assessment

Updated: 2026-08-20

Status: **article-specific candidate evidence only**. Canonical `main:articles/romance/master.md` remains unchanged.

## Exact candidate measurements

The materialized candidate family is bound by `materialized/candidate-manifest.json`.

### Part 1

- candidate SHA-256: `51f4823cab86943cfa022c9139f97ed9f871cf4e7a5318ee8212816171f84e00`
- words: 10,235
- Pangram 4.0 / `STAGE_SUCCESS`
- Human: `0.919354856`
- AI: `0.0806451589`
- AI-assisted: `0.0`
- exact stored-text match: yes
- evidence branch: `u-dont-existDOTcom/pangram-humanization-lab:evidence/romance-pass1-retest-20260820`
- exactly one new detector submission for this candidate boundary; no automatic repeat

Prior registered Part-1 boundary:

- Human: `0.9205247164`
- delta: `-0.0011698604` Human fraction = **-0.11698604 percentage points**

Disposition: **REVERT the sole Part-1 edit.** The rewrite from `Sex drives are independently alive and always changing...` to `Sex drives have lives of their own...` slightly worsened Pangram and also replaced more distinctive owner-shaped wording with more generic language. Reverting that one edit restores the exact already-measured registered Part-1 boundary, so no new Part-1 paid call is needed.

### Part 2

- candidate SHA-256: `30f61fb0c490ec1275f3c39c834a38a956041865b63e5592c270d51cc22d5498`
- words: 10,166
- Pangram 4.0 / `STAGE_SUCCESS`
- Human: `0.9137498736`
- AI: `0.0862501487`
- AI-assisted: `0.0`
- exact stored-text match: yes
- evidence branch: `u-dont-existDOTcom/pangram-humanization-lab:evidence/romance-pass1-retest-20260820`
- exactly one new detector submission for this candidate boundary; no automatic repeat

Prior registered Part-2 boundary:

- Human: `0.8983033895`
- delta: `+0.0154464841` Human fraction = **+1.54464841 percentage points**

Disposition: **KEEP the Part-2 repair direction provisionally.** The batch improved materially, but because seven local operations changed together, this result does not identify a causal phrase or prove every operation helped.

## Post-detector architecture / fidelity gate

The materializer's invariant audit passed:

- source master hash verified;
- headings identical;
- native-object markers identical;
- Markdown link destinations identical;
- no protected anchor missing.

Manual full-context recheck also preserves:

- Crucible coercion/control safety exit;
- Primal masculine/feminine owner argument;
- father opening and Bear terminal callback;
- children/stepchildren obligations;
- Gandarussa passage;
- H./Hâle/Hale identity separation;
- section order and stopping point.

No intended claim, certainty, actor, chronology, or causal reassignment was introduced by pass 1.

## Editorial dispositions after reading the literal candidate

Keep provisionally:

1. combined Anami / jade-egg source progression;
2. `Muses & Directors` reduction of repeated metaphor explanation while preserving lived examples and safety callback;
3. removal of the economy-specialization analogy while preserving complementarity;
4. removal of the first duplicate surrender explanation and repeated `gently`;
5. more direct opening of `After leaving`;
6. more direct spiritual-practice opening.

Two further `After leaving` corrections are justified independently of Pangram:

1. Prefer the original owner-shaped `one-dimensionalizing them` over the candidate's more generic `flatten them into one character`; this restores distinctive language without changing the proposition.
2. Delete `Staying curious about what happened can be therapeutic in itself.` The preceding neutral-observer sentence already completes the practical move; this sentence is interpretive aftercare and repeats the therapeutic implication rather than changing the reader's position.

These two changes should be made as a candidate-only pass before any further detector measurement.

## Efficient next detector step

Do **not** pay for Part 1 again after reverting its only edit: exact reversion returns to the already-measured registered Part-1 SHA/result.

If Joel authorizes another paid measurement, create a Part-2-only pass with the two `After leaving` corrections above, preserve every other accepted Part-2 edit, make it Git-durable, and buy exactly **one** new Pangram-4 Part-2 measurement. Do not run isolated sentence probes first.

A new Part-2 result remains detector evidence only; 100% Human would still require the article-wide semantic/architecture/fidelity gate before any authority change.
