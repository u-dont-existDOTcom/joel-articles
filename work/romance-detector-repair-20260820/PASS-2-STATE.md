# Romance detector repair — pass 2 state

Updated: 2026-08-20

Status: **candidate work only**. Canonical `main:articles/romance/master.md` remains unchanged.

## Why pass 2 exists

Pass 1 produced exact Pangram-4 measurements:

- Part 1 candidate `51f4823cab86943cfa022c9139f97ed9f871cf4e7a5318ee8212816171f84e00`: Human `0.919354856`, slightly worse than the registered Part-1 Human `0.9205247164`.
- Part 2 candidate `30f61fb0c490ec1275f3c39c834a38a956041865b63e5592c270d51cc22d5498`: Human `0.9137498736`, up from registered `0.8983033895`.

The post-detector architecture/fidelity audit therefore rejected the sole Part-1 rewrite and provisionally retained the Part-2 repair direction.

## Exact pass-2 changes

1. **Part 1:** restore the pass-1 sex-drive paragraph exactly to the registered wording. The materializer must reproduce SHA-256 `ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8`. This reuses the already-paid registered Part-1 Pangram result; no new Part-1 call is authorized or needed.
2. **Part 2 / After leaving:** replace the pass-1 generic `Don't flatten them into one character...` realization with the owner-shaped `one-dimensionalizing them` wording while keeping the more direct pass-1 paragraph movement.
3. **Part 2 / After leaving:** delete `Staying curious about what happened can be therapeutic in itself.` because the preceding neutral-observer sentence already completes the practical move; the sentence is interpretive aftercare rather than a new step in the thought.

Every other accepted Part-2 pass-1 edit remains unchanged for this measurement.

## Deterministic gate

`apply_pass2.py` starts only from the exact Git-durable pass-1 candidate family and fails unless all three pass-1 source hashes match. It then:

- asserts Part 1 returns exactly to the registered Part-1 detector SHA;
- preserves headings, native-object markers, Markdown link destinations, and protected Romance anchors;
- emits a candidate master, exact restored Part 1, and new Part 2;
- declares `part1: no_new_call_exact_registered_hash_restored` and `part2: one_new_pangram4_measurement_only`.

`tests/test_romance_pass2_materializer.py` exercises the real pass-1 materialized artifacts and verifies those invariants.

## API execution route

Pangram PR #111 merged the reusable `pangram-lab detect-file` command to `main`. It uses the existing Pangram API client/cache/checkpoint machinery: exact SHA gate, stable measurement key, authentication probe, Pangram-4/version gate, pending-task resume, ambiguous-submit refusal, and Git durability. Because the public Pangram cache stores exact detector text, this article run explicitly uses `--allow-public-cache`; the Romance candidate is already public-safe in the public article repository.

Task runner: `run_pass2_api.sh`.

It:

- materializes pass 2 and proves Part 1 exactly matches the registered SHA;
- commits/pushes the pass-2 candidate before detector work;
- reserves stable audit/section/measurement identity on `evidence/romance-pass2-api-20260820`;
- records that Part 2 has one prior new paid POST in this audit section and the six-call cap;
- invokes **Part 2 only** through `pangram-lab detect-file`;
- relies on content-addressed cache/checkpoint state to resume rather than duplicate a paid POST;
- records the successful API result in the audit ledger when complete.

Current article-branch CI, including the runner syntax/regression test plus authority/architecture/policy gates, passed at commit `7950c1cb8a0f8474bbfc19d94dc1d5332e8930fe`.

## Detector plan

- Do not submit Part 1.
- Materialize and push the pass-2 candidate family first.
- Use the fresh/resumable API evidence branch `evidence/romance-pass2-api-20260820`.
- Submit the exact pass-2 Part 2 once to Pangram 4 through the API route.
- If the paid action is ambiguous, recover/resume from durable cache state before any repeat; no automatic repeat.
- After the result is durable, run the article-wide semantic/architecture/fidelity gate again before any canonical authority change.
