# Regeneration version 4 — fixed-set trial and stop decision

**Decision:** Stop generation and do not train either adapter. Version 4 could not meet its predeclared 28/40 overall gate after 32 of the fixed 40 passages: it accepted 16/32, so even eight further successes would yield at most 24/40. The remaining eight passages were not sampled. No version 4 result entered training. The server is retained solely for records recovery under `GPT-SHUTDOWN-DIRECTIVE.md` on the handoff branch.

## Results

The source set was the same frozen 40 training-split regeneration passages used for version 3; the human-source manifest SHA-256 is `56869801ee7f95dfea1681170c745cacf112f93c117a185177c515568c80b089`. Version 3 Chinese notes accepted 24/40; version 3 English slots accepted 0/40. Version 4 processed 32/40 before its early stop and accepted 16/32. On those **same 32 processed passages**, version 3 Chinese notes accepted 23/32 and version 4 accepted 16/32. These denominators matter: 16/32 is an observed rate, while 24/40 is only the maximum version 4 could have reached if all eight untried passages passed.

| Genre | Version 3 Chinese, full 40 | Version 3 English slots, full 40 | Version 3 Chinese, matched 32 | Version 4, matched 32 |
|---|---:|---:|---:|---:|
| Email | 1/1 | 0/1 | 1/1 | 0/1 |
| Essays/journal | 5/17 | 0/17 | 4/11 | 4/11 |
| Letters | 3/4 | 0/4 | 3/4 | 3/4 |
| Practical | 8/8 | 0/8 | 8/8 | 4/8 |
| Technical | 7/10 | 0/10 | 7/8 | 5/8 |
| **Total** | **24/40** | **0/40** | **23/32** | **16/32** |

In the matched 32, 13 passed both Chinese methods, six failed both, three failed version 3 and passed version 4, and ten passed version 3 and failed version 4. This is a paired comparison of data-generation admissions, not a writing-quality evaluation. The version 3 Chinese method missed its own 28/40 overall gate; the English-slot method failed parsing on all 40, including its one retry. The version 4 method used a whole-passage Chinese round trip and still reached the early-stop rule.

Version 4 final rejection reasons can overlap: copy/list guard 11, source-language requirement 1, no draft 1, `human_claims_in_ai` 3, `ai_claims_in_human` 4. On first attempts, the recorded reasons were copy/list guard 12, language 1, no draft 1, forward fidelity 2, reverse fidelity 6; 19 cases used their permitted retry. The saved trial summary recorded `EARLY_STOP_THRESHOLD_IMPOSSIBLE`, 32 processed, 16 accepted, 152 raw model requests, and 1,366.89 seconds of trial runtime. No version 4 Pangram or Emulate call was made. The pilot used 48 Pangram credits in the earlier version 2 spot check and zero new Emulate words. No adapter was trained or evaluated.

## Recovery and cost checkpoint

The shutdown directive at handoff commit `b529de83bb9298a2f2c7ff8e65231c0ad9b905c1` requires copying and verifying all nonweight pilot records off the instance and publishing the archives before destruction. The instance-side archive selection included six version 4, six slot, and 2,749 remainder entries, with two credential paths excluded and zero read errors. Model-weight and partial-download entries were inventoried by path and size only. The three requested archives, inventory, exclusion list and `SHA256SUMS` were created at `/workspace/reverse-pilot-20260929/shutdown-export/`. The remainder archive is approximately 649 MB and was split into 14 parts of no more than 45 MiB. **None of these shutdown archives has yet been copied off-instance, checked locally, or published.** The previously copied version 3 Chinese archive remains off-instance with SHA-256 `df7cbef3f7ff2eb594dffa4ded0cebfd150ea25ab682465750a51e593f11d615`.

The recovery instance 53306647 was started at approximately 2026-09-30 01:20:30 UTC and its Stop action accepted at approximately 02:15 UTC, within the directive's one-hour total run limit. The Vast console subsequently offered **Start**, showed **Inactive**, and displayed its storage-only rate of **$0.109/hour**. The instance and its records remain intact; it was **not destroyed** because the off-instance checks and Git publication are incomplete. Restarting would exceed the current directive's cumulative one-hour run allowance and needs a new owner instruction.

At the signed-in billing check at 2026-09-30 02:18 UTC, replacement instance 53306647 showed $9.74 total: $6.54 GPU (14.86 billed hours over the pilot), $2.32 storage, $0.87 download and under $0.01 upload. Original pilot instance 53303444 showed $0.13 total ($0.11 GPU, $0.02 storage) and was no longer listed among active instances. Vast's displayed account usage was $9.87, including another unrelated instance below $0.01. These are interim, rounded provider figures; storage continues at the stopped rate and final costs cannot yet be stated. The wallet displayed $10.13. No new purchase was made.

The remaining recovery gate is a permitted transfer route that does not use a file picker. A temporary local SSH key was prepared, but its public key was **not added to the Vast instance** because browser security review requires explicit approval for that access change. The key has no access unless installed. The user has been asked for that approval. The Jupyter file-browser/editor route was rejected by automatic review in light of the user's instruction not to open file pickers, and a direct browser file download was blocked by the browser client. The shutdown directive therefore forbids destruction now. This report is a truthful trial and recovery checkpoint, not `PILOT-RESULTS.md` or a claim of pilot closure.
