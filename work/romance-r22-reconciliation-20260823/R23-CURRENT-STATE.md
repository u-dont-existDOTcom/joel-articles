# Romance r23 current state

Updated: 2026-08-24

## Status

Editorial reconciliation for the currently approved local changes is complete through exact natural-boundary materialization and cold read. The complete r23 master / Part 1 / Part 2 files are not yet materialized in this connector-only runtime. No Pangram call has been made on r23.

Registered `main:articles/romance/master.md` remains unchanged. PR #46's branch copy of `articles/romance/master.md` has been restored to the exact registered-main blob so stale conservative prose cannot be accidentally merged as the article master.

## Known-green rollback baseline

Exact r22:
- source: `task/romance-detector-repair-20260820:work/romance-detector-repair-20260820/materialized-preservation-r22-patient-affection/candidate-master.md`
- Git blob: `9f6bf7ed77093569a98fe606fda96ac277839f99`
- Markdown SHA-256: `f0f9a47eba2ac9ab1a56bdd6793316d41e7c23072b0b0c030285caf5e12f83c9`
- Markdown whitespace words: 20,282
- Part 1 SHA-256: `5ed333800b9ae7b402f26aa03e751ef8296c7e27ab70e39bc39bb9896b23e62d`; Pangram 4.0 Human `1.0`, zero AI windows
- retained Part 2 SHA-256: `9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85`; Pangram 4.0 Human `1.0`

Do not describe the two half results as a measured whole-article score.

## r23 authorized delta

Exactly five editorial features / six frozen replacement operations:
- `R23-01` prospective libido-divergence planning;
- `R23-02A` Affection simmer / taking-for-granted / five-years-ago / anti-homework rewrite;
- `R23-02B` changed-sex-life curiosity / new-normal / feeling-wanted rewrite;
- `R23-03` student-report attribution + jade-egg preliminary-training relation;
- `R23-04` owner-final Two Pillars sentence: `But sometimes a friend who actually knows us both sees the pattern before either of us does.`;
- `R23-05` `I can hear a whole future in those two words—...`.

Exact old/new spans and hashes: `R23-FIVE-OWNER-EDITS-MANIFEST.json`.

Everything else is invariant relative to exact r22.

## Exact independently materialized changed boundaries

All were reconstructed directly from exact r22 plus the frozen whitelist, committed, read back from GitHub, and verified by matching returned Git blob identity to the independently computed expected Git blob identity.

- Talk + Affection: SHA-256 `a1c88e60e068101c268b8e0dc45558ec796fe6d8224de86c8b5ec64c5238e564`; 777 words; Git blob `da9a1a9264e6ed42f46b0df1f2879bf31656dd46`; cold read PASS.
- Spiritual practice: SHA-256 `9722c938f9258316cef1efbe67768abee063f64923976711498bbaff57d106fb`; 290 words; Git blob `cb2b548692599cff9ad06421e54ef39fb516d3af`; cold read PASS.
- Two Pillars: SHA-256 `e89362da826bd77d747733512a935cf19c1ddf6d492175755931826968360113`; 734 words; Git blob `36b1981da211f1bba292ee390e287ebe7bd57c5c`; cold read PASS.
- Choosing Together through Attraction/exclusivity: SHA-256 `a1bd65fc862a879170d6651f52f4d0da50150bf56de1f4f9e26437d30dd6cb8f`; 1,437 words; Git blob `543ef3e542de4d23ead2da674daa339cc747b56b`; cold read PASS.

See `r23-boundary-candidates/boundary-manifest.json` and `R23-BOUNDARY-COLD-READ-20260824.md`.

Boundary preservation status:
- forward traceability PASS;
- reverse traceability PASS;
- unexplained substantive deltas 0;
- headings unchanged;
- links/native objects unchanged inside changed boundaries;
- independent-final-reader audit not required for bounded D2 reconciliation.

## Closed proposals

Do not re-add unless Joel explicitly reopens them.

Already covered elsewhere in r22:
- slow/brakes purpose clause;
- Muses analytical/prose-function addition;
- Psychedelics sober stress-test list.

Rejected:
- generic three-sentence Two Pillars block;
- Attraction/exclusivity history→vow bridge;
- already-in-it stay-in-conversation diagnostic.

## Materializer

`materialize_r23_five_owner_edits.py` is the current frozen assembly tool.

It now blocks unless all of these hold:
- exact r22 SHA-256 `f0f9a47eba2ac9ab1a56bdd6793316d41e7c23072b0b0c030285caf5e12f83c9`;
- exact r22 whitespace word count 20,282;
- exactly six frozen replacements, each old span once;
- expected r23 whitespace word count 20,364;
- exact heading list unchanged;
- native objects exactly 11 → 11;
- Markdown links exactly 22 → 22;
- protected father quote, Gandarussa, children-war warning, Bear callback, and Rumi terminal line all present;
- each old span absent / new span present exactly once after transformation;
- extracted changed-boundary SHA-256s exactly match the four independently materialized fixtures above.

On success it writes the full r23 master, the same four natural boundaries, a candidate manifest, and final preservation receipt. It makes no detector call.

Runtime prerequisite: repository checkout with the exact task ref fetched as `origin/task/romance-detector-repair-20260820`.

## Detector state

r23: **UNMEASURED**, not failed.

Do not spend four section-level Pangram calls and treat them as certification. Romance has demonstrated composition sensitivity; the meaningful certification targets are the resulting exact r23 Part 1 / Part 2 halves after full assembly.

Before paid work:
1. recover exact Pangram cache / pending / ambiguous / reservation / section-call-ledger state;
2. use the current trusted private self-hosted executor route, not GitHub-hosted Actions or Browserbase;
3. freeze exact r23 half identities and Pangram 4.0 spec;
4. do not repeat already-paid or ambiguous work;
5. keep r22 exact halves as rollback anchors.

Current Pangram lab state also records that a prior ~10-credit full-Part2 request encountered insufficient balance after the trusted route itself was proven. Re-check current balance/accounting before assuming a full-half call can run.

## Repository hygiene completed

- stale conservative `articles/romance/master.md` change removed from PR #46; branch master is exact registered-main blob;
- dead `R23-MATERIALIZATION-TRIGGER*.md` files removed;
- temporary workflows from failed connector-trigger experiments are not part of PR #46;
- README and `RECONCILIATION-LEDGER.md` now route to current function-first r23 state;
- conservative/holistic failure artifacts remain only as historical evidence and are explicitly non-authoritative.

## Next executable step

In a runtime with repository checkout access:

1. fetch `task/romance-detector-repair-20260820` to `origin/task/romance-detector-repair-20260820`;
2. run `python work/romance-r22-reconciliation-20260823/materialize_r23_five_owner_edits.py` from the PR #46 branch;
3. commit/read back `materialized-r23-five-owner-edits/`;
4. verify the final receipt and candidate SHA;
5. create exact r23 reader-visible Part 1 / Part 2 using the same split contract as r22;
6. only then recover detector accounting and decide whether to certify both changed halves.

Do not alter registered main or publish/export before that gate is complete.
