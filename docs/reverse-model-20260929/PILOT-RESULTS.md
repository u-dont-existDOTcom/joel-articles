# Reverse-model pilot — data-generation result

**Outcome: stopped at the version 4 gate.** No adapter was trained or evaluated. The original plan's Base-versus-Instruct model comparison was not reached. The generation methods could not make enough admissible pairs under the predeclared rules, so no detector score or writing-quality claim about a trained rewriter is supported.

## Same fixed 40-passage trial

The 40 training-split regeneration passages were frozen before the version 3 and version 4 trials. Version 3 Chinese notes accepted 24/40, below its 28/40 gate. Version 3 English atomic slots accepted 0/40 because both permitted notes attempts failed strict format parsing for every passage; no slot drafts or meaning judgments ran. Version 4 used a whole-passage Chinese round trip. It accepted 16/32 before the early-stop rule: even eight further successes could yield only 24/40, below the 28/40 gate. The remaining eight were deliberately not sampled. On the exact 32 passages version 4 attempted, version 3 Chinese notes accepted 23/32.

| Genre | Version 3 Chinese, full 40 | Version 3 English slots, full 40 | Version 3 Chinese, matched 32 | Version 4, matched 32 |
|---|---:|---:|---:|---:|
| Email | 1/1 | 0/1 | 1/1 | 0/1 |
| Essays/journal | 5/17 | 0/17 | 4/11 | 4/11 |
| Letters | 3/4 | 0/4 | 3/4 | 3/4 |
| Practical | 8/8 | 0/8 | 8/8 | 4/8 |
| Technical | 7/10 | 0/10 | 7/8 | 5/8 |
| **Total** | **24/40** | **0/40** | **23/32** | **16/32** |

In the matched 32, 13 passed both Chinese methods, six failed both, three passed only version 4, and ten passed only version 3. Version 3 Chinese final rejection reasons, which can overlap, were reverse-meaning judgment 7, forward-meaning judgment 4, non-Chinese notes 4, no draft 4, truncated draft 2, and copy/list guard 2. Version 4 final rejection reasons, also overlapping, were copy/list guard 11, source-language requirement 1, no draft 1, `human_claims_in_ai` 3, and `ai_claims_in_human` 4. Version 4 used 152 saved raw model requests and 1,366.89 seconds of trial runtime. The [version 3 trial](consultation/REGEN-V3-TRIAL.md) and [version 4 trial](consultation/REGEN-V4-TRIAL.md) give the request-level diagnostics and precise denominators.

No version 3 or 4 paid detector diagnosis was run after the stop gates. Total pilot Pangram use was 48 credits from the earlier 20-draft spot check; new Emulate use was zero words. These were data-generation diagnostics only. No detector result was used as a training label or admission filter.

## Records and reproducibility

The human-source manifest SHA-256 is `56869801ee7f95dfea1681170c745cacf112f93c117a185177c515568c80b089`. The previously copied private version 3 Chinese archive has SHA-256 `df7cbef3f7ff2eb594dffa4ded0cebfd150ea25ab682465750a51e593f11d615`. The three shutdown archives, inventory, credential exclusion path list, per-file hashes and reassembly instructions are in [archives/](archives/README.md): version 4 `46f7d033d04165d0903500fc8dca6df148edfbf6a34a8d7f2e7209f3d426d976`, English slots `04ae558bf9e9ad31c4e63a012f8df79e78e454641405a79954f2e64c77aa1665`, and the rejoined remainder `e47c1c0906ad6a9726d6192a8060ee562610181df61a2546f3d888fa819b95ea`. Model weights and resumable Hugging Face downloads were inventoried by path and size, then omitted because the pinned public model revisions can be downloaded again. Two credential paths were excluded from the published records. The source passages are OANC and MASC material with redistribution permitted under their licenses, already carried on this branch.

## Costs and shutdown

Vast's post-destruction charges page displayed the following rounded amounts:

| Instance | GPU | Storage | Download | Upload | Total |
|---|---:|---:|---:|---:|---:|
| Replacement pilot instance `53306647` | $6.70 | $2.48 | $0.87 | $0.01 | $10.06 |
| Original pilot instance `53303444` | $0.11 | $0.02 | $0.00 | $0.00 | $0.13 |
| **Pilot total** | **$6.81** | **$2.50** | **$0.87** | **$0.01** | **$10.19** |

The replacement's billing breakdown recorded 15.22 GPU hours, 22.82 storage hours, 134.1 GB downloaded and 1.9 GB uploaded over the pilot, not just the final recovery run. The displayed account usage was $10.19, including an unrelated older instance charged under $0.01, so component rounding may make the account and pilot totals appear equal. The remaining credit balance was $9.80. No worker credit purchase or payment-setting change occurred. All cash, GPU, Pangram and Emulate caps were respected.

The Vast audit log records deletion of replacement instance `53306647` at **2026-09-30 03:44 UTC**. The original pilot instance had already been deleted at 2026-09-29 04:50 UTC. A post-deletion console check showed **zero instances** and a **$0.00/hour current spending rate**, confirming that both GPU and storage billing had stopped. Vast notes that recent charges can be delayed; the amounts above are the final displayed figures at the post-deletion check, not an assertion about later provider adjustments. The one-hour extension approved for records recovery ran from 03:09 to 03:31 UTC, after which the GPU was stopped pending GitHub verification. The temporary SSH key was deleted from Vast and its local private-key files removed.

The pilot stopped before adapter training. Claude will design the separate Venice API data-generation phase; this report does not authorize or run that phase.
