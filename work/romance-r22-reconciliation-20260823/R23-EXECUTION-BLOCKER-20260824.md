# Romance r23 execution blocker — 2026-08-24

Status: **editorial/preservation work is ready; exact full-file execution is blocked only by the current connector-only runtime. No background workflow remains installed. No Pangram call made.**

## What is complete

- Exact r22 known-green Markdown and exact detector-half identities recovered.
- Five r23 editorial features / six replacement operations frozen.
- Four changed natural boundaries independently materialized, Git-read-back byte-exact, preservation-clean, and cold-read PASS.
- Full Markdown materializer hardened against exact r22 identity, expected r23 word count, headings, 11 native objects, 22 Markdown links, protected anchors, replacement counts, and four independently verified boundary SHA fixtures.
- Exact reader-visible half contract recovered from the actual r22 Pangram inputs, not from a new Markdown normalizer.
- `materialize_r23_reader_halves.py` frozen to mutate only R23-01/02A/02B in Part 1 and R23-03/04/05 in Part 2, preserving the exact tested split topology.

See:
- `R23-CURRENT-STATE.md`
- `R23-FIVE-OWNER-EDITS-MANIFEST.json`
- `R23-BOUNDARY-COLD-READ-20260824.md`
- `R23-READER-HALF-CONTRACT.md`
- `materialize_r23_five_owner_edits.py`
- `materialize_r23_reader_halves.py`

## Why full r23 is not yet committed

The ChatGPT GitHub connector can read/write repository objects but cannot execute the repository-local materialization scripts. Connector-authored push / PR-edit triggers did not launch temporary GitHub Actions jobs. A one-shot scheduled workflow was then installed and given clean cron opportunities, but no run materialized output. It has been removed from `main` rather than leaving latent automation that could fire unpredictably later.

No temporary materialization workflow remains installed on `main` or PR #46.

## Exact next execution

A runtime with a repository checkout needs only:

1. check out `reconcile/romance-r22-20260823`;
2. fetch `task/romance-detector-repair-20260820` as `origin/task/romance-detector-repair-20260820`;
3. run `python work/romance-r22-reconciliation-20260823/materialize_r23_five_owner_edits.py`;
4. run `python work/romance-r22-reconciliation-20260823/materialize_r23_reader_halves.py`;
5. commit `work/romance-r22-reconciliation-20260823/materialized-r23-five-owner-edits/`;
6. read back and freeze the exact candidate-master / Part 1 / Part 2 SHA-256s.

Both scripts fail closed on source/hash/count/topology mismatch and make no detector call.

## Detector remains a separate gate

The trusted Pangram route is the private self-hosted executor. Current lab state records that the last ~10-credit full Romance request received self-hosted HTTP 402 before a task ID was created, after a 1-credit smoke succeeded. Therefore available balance for two new ~10k-word r23 half calls must not be assumed.

Once exact r23 half bytes are committed, recover current cache/reservation/call-ledger and available-account state before any paid submission. Do not use section scores as a substitute for half-boundary certification and do not route through GitHub-hosted Actions or Browserbase.
