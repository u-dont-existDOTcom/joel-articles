# Romance detector repair — pass 4 state

Updated: 2026-08-20

Status: **candidate_not_owner_final; measurement blocked by self-hosted Pangram credit balance**. Canonical `main:articles/romance/master.md` remains unchanged.

## Authority carried forward

- Registered Part 1 remains byte-identical at SHA-256 `ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8` and reuses its existing measured Pangram result. No Part-1 call is authorized or needed.
- Best completed Part-2 measurement remains pass 3:
  - SHA-256 `c6ef42419a3db2e82b1ff4f9370fc85bca4fa8c061c61dd6a1b5d28171d9908c`
  - 10,043 words
  - Pangram 4.0 / `STAGE_SUCCESS`
  - Human `0.9153165817`
  - AI `0.0846834108`
  - AI-assisted `0.0`
  - exact stored-text match
  - paid Part-2 measurement #3

## Pass-4 editorial target

Pass 4 starts from the exact Git-durable pass-3 candidate and targets the three historically AI-labeled Part-2 regions that pass 3 never edited:

1. **Money / competence polarity** — removes the generic `Micromanaging everything...` summary, keeps the strong polarity claim, and moves the thought into Joel's first-person experience: earning more is not the problem; treating money as proof that one partner is the competent adult can effeminate him inside the relationship. The reverse successful-woman-shrinking failure remains.
2. **Female influence → direct male leadership transition** — preserves female influence and the owner's claim that women often prefer direct male direction, while replacing the `gentle, almost hypnotic leadership` explanatory packaging with a more conversational lived exchange.
3. **Historical exclusivity → personal experiment transition** — preserves the historical/property claim but removes `Those origins still matter` plus the generic `I haven't done any of this perfectly` disclaimer and moves directly into the concrete experiment of trying to stop being attracted to anyone else before marrying B.

No factual/source claim was intentionally weakened, no Primal Attraction argument was neutralized, and no protected function was removed.

## Exact pass-4 materialization

Git-durable materialized candidate:

- master SHA-256: `b1541c6b6aee5cf289bc50d00ae6422b681fc6f64327729cd2f03a00bef3c779`
- Part 1 SHA-256: `ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8`
- Part 2 SHA-256: `a21b9670bc0cc61b4fc850761ca57ffa5dc5d1a02bdd5df90b820d6f9d437a0e`
- Part 2 words: 9,985
- headings/native markers/Markdown link destinations/protected anchors: invariant audit passed

Artifacts: `work/romance-detector-repair-20260820/materialized-pass4/`.

## Correct Pangram routing

Current owner correction routes new programmatic Pangram work through:

- public lab: `u-dont-existDOTcom/pangram-humanization-lab`
- evidence branch: `automation/pangram-fixed-batch`
- private executor: `u-dont-existDOTcom/pangram-private-executor`
- runner: `[self-hosted, linux, x64, pangram]`

Fresh route proof immediately before this task succeeded on an uncached 60-word Pangram-4 input with `paid_api_calls: 1`, `cache_hits: 0`, and estimated 1 credit / $0.05. This proves the route and key are operational.

## Cross-transport call accounting

Before pass 4, the fixed-batch ledger was seeded with the three already-paid Part-2 measurements across transports so changing transport could not reset the six-call cap.

The pass-4 self-hosted runner then durably reserved slot #4:

- audit: `romance-detector-repair-20260820`
- section: `part2`
- measurement key: `romance-detector-repair-20260820-part2-pass4_PASS4`
- exact text SHA-256: `a21b9670bc0cc61b4fc850761ca57ffa5dc5d1a02bdd5df90b820d6f9d437a0e`
- estimated credits for the 9,985-word boundary: 10
- safety ledger state after reservation: 4/6

The fixed-batch spec is immutable on `automation/pangram-fixed-batch`:

- `experiments/romance-detector-repair-20260820-part2-pass4.json`
- spec SHA-256 `c06f501b5706c7e44d0e30c31ba1c807d500d0670fc345b427e4f6cea162e878`

Private request:

- `pangram-private-executor:requests/romance-detector-repair-20260820-part2-pass4.json`

## Actual self-hosted result

The real pass-4 POST reached the self-hosted Pangram API path, but Pangram returned:

- HTTP 402
- `Insufficient credits`
- no task ID
- no detector result
- cache status `failed`

This is **not** Browserbase, not GitHub-hosted Actions, not an origin-401 issue, and not an ambiguous submit. It is a self-hosted Pangram API credit-balance failure for the actual 9,985-word request.

The fresh one-credit smoke success plus this ten-credit request failure means the supported conclusion is: **the trusted self-hosted route works, but the available Pangram balance was insufficient for this full Part-2 request at the time of execution.** It does not establish that the account had literally zero credits.

## No-retry boundary

Do not automatically resubmit pass 4. There is no pending task to resume and no ambiguity to recover. Reuse the exact immutable spec and candidate after sufficient self-hosted Pangram credits are available; do not create a new audit identity or text merely to bypass the failed balance check.

Do not route ordinary measurement through Browserbase or GitHub-hosted Actions as a workaround.

## Current next safe action

Keep pass 4 frozen and editorially provisional. No further detector-driven prose change is justified without new measurement feedback. Once the trusted self-hosted route has enough balance for the 9,985-word boundary, re-run the exact pass-4 request under the same audit/section/candidate identity, with explicit review of the existing failed cache/ledger so the retry is deliberate rather than automatic.
