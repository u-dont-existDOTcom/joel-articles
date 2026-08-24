# Romance r23 exact reader-visible half contract

Status: **FROZEN PRE-DETECTOR CONTRACT.** No Pangram call made.

The r23 certification halves must be derived from the exact detector inputs that produced r22's Human `1.0` / Human `1.0` results. Do not regenerate reader-visible text from Markdown with a new normalizer and do not choose a new split point.

## Exact tested r22 source halves

### Part 1

- Repository: `u-dont-existDOTcom/joel-articles`
- Ref: `task/romance-detector-repair-20260820`
- Path: `work/romance-detector-repair-20260820/materialized-preservation-r22-patient-affection/part1.txt`
- SHA-256: `5ed333800b9ae7b402f26aa03e751ef8296c7e27ab70e39bc39bb9896b23e62d`
- whitespace words: 10,239
- Pangram 4.0: Human `1.0`, zero AI windows.

### Part 2

- Repository: `u-dont-existDOTcom/joel-articles`
- Ref: `task/romance-detector-repair-20260820`
- Path: `work/romance-detector-repair-20260820/materialized-semantic-r9/candidate-part-2.txt`
- SHA-256: `9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85`
- whitespace words: 9,892
- Pangram 4.0: Human `1.0`.

The retained split topology is exact: Part 1 ends after the initial patient paragraph (`I usually had some idea, so of course I answered. But enough moments become a pattern.`); Part 2 begins with `Key at first asked me innocently, "Can you be my guru?"`.

## r23 operation assignment

Only the reader-visible forms of the frozen r23 operations may change these exact half files.

Part 1:
- `R23-01`
- `R23-02A`
- `R23-02B`

Part 2:
- `R23-03`
- `R23-04`
- `R23-05`

Expected whitespace-word counts after those exact operations:
- r23 Part 1: **10,296** (`+57`)
- r23 Part 2: **9,917** (`+25`)

Total across the two exact detector inputs: 20,213 words.

The Affection `R23-02A` reader-visible old/new hashes differ from the Markdown span hashes because Markdown link syntax is absent from the tested text:
- reader old SHA-256 `edd35bb4e3eb76873753b42f94da01cc1275bf2044ab2abb6c92f3fa4648fd08`
- reader new SHA-256 `d32955c635ee71ab64c8a9689c5f204cae33a4b42bf3eac530c0867d0e7904b8`.

The other five exact replacement spans contain no Markdown syntax and therefore use the same frozen text/hash identity in Markdown and reader-visible form.

## Materializer

`materialize_r23_reader_halves.py` enforces this contract. It:
1. fetches the exact r22 Part 1 / Part 2 texts by Git ref/path;
2. fails closed unless their SHA-256 and word counts match the exact known-green identities above;
3. applies only the three assigned frozen operations per half, each exactly once;
4. fails if any old span survives or any new span is non-unique;
5. requires exact expected r23 word counts 10,296 / 9,917;
6. requires Part 2 to retain the exact `Key...guru` starting boundary and the changed headings to remain in their expected half;
7. writes `candidate-part-1.txt`, `candidate-part-2.txt`, updates the candidate manifest, and writes a reader-half receipt;
8. makes **no Pangram call**.

## Detector implication

After exact materialization and GitHub readback, these two files—not the four local natural-section files—are the composition-aware Pangram certification targets.

Before paid submission, recover exact Pangram cache/reservation/call-ledger state. A previous trusted self-hosted ~10-credit Romance request returned HTTP 402 before task creation, so available balance must not be assumed. Exact r22 remains the rollback anchor.
