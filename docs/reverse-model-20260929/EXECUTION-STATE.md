# Reverse model pilot — execution checkpoint

Status: OPEN / RUNNING — access restored. Pinned Instruct download COMPLETE and actual two-step rank64 MoE fit PASS. Initial 12 production passages processed, eight pairs accepted. Sixteen new passages at batch16 and the pinned Base download are running under supervisors. Full generation, both trainings, model evaluation and final reporting remain OPEN.

Authority: Joel's two uploaded directives, approval to continue with 40 GB VRAM, and instruction to use his replacement instance with more disk. This is an experiment and authorizes no canonical article edits.

## Frozen experiment
- Base: handoff/claude-dangerous-adult-20260924-1631 at d9bbbfb08bfbf8210084e0d468208f4cb6b3aa93.
- Working branch: gpt/reverse-pilot-20260929 only. No force-push.
- Models: Qwen/Qwen3-30B-A3B-Base at 1b75feb79f60b8dc6c5bc769a898c206a1c6a4f9; Qwen/Qwen3-30B-A3B-Instruct-2507 at 0d7cf23991f47feeb3a57ecb4c9cee8ea4a17bfe. Both Apache-2.0, qwen3_moe, 48 layers, 128 experts, eight active experts. Updated non-thinking instruct checkpoint follows the worker clarification; the earlier pilot named Qwen3-30B-A3B.
- Human sources: OANC written material (unrestricted use/redistribution) and MASC (CC BY 3.0 US). MASC overlaps OANC: cross-corpus source identity/content deduplication precedes document splits. Gutenberg contribution is zero.
- No GPT/Claude/Joel text or filter labels in training. Only the frozen open instruct model generates and judges pairs. Regeneration receives notes in a fresh request with no original.
- 1,200 passages, 100–250 words; document-level 1,000/100/100 split before generation; one-third paraphrase, two-thirds notes/regeneration; reject either-direction fidelity failures.
- Both conditions: rank 64 attention and expert feed-forward layers, two epochs, target-only loss, same accepted data/settings. Routers remain frozen.
- Evaluation: A+B learning inputs and first saved Emulate outputs; 20 general cases; temperature 0.8, one output per model. E_holdout remains excluded.
- Hard caps: $100 cash, $40 GPU, 500 Pangram credits, 3,000 Emulate words. Trained adapters and credentials stay private.
- Output: PILOT-RESULTS.md, all outputs/scores/prompts/manifests/logs, ten comparisons, verified branch publication, private adapter backup, GPU shutdown.

## Current evidence
Replacement instance: A100 PCIe 40 GB, 195 GB free disk at bootstrap, $0.549/hour console rate. The original instance was stopped before the owner replaced it. No second instance was provisioned by the worker.
Fresh complete machine AGENTS read; capabilities, GPU, disk, RAM/CPU limits and packages recorded. Python 3.12.14, torch 2.10.0+cu128, transformers 5.5.0, PEFT 0.18.1, TRL 0.23.1, bitsandbytes 0.50.2, accelerate 1.15.0, Unsloth 2026.9.11, Unsloth-Zoo 2026.9.7. No stack reinstall.
The actual Instruct rank64 fit covers all 48 attention and expert feed-forward layers: 2,570,059,776 trainable parameters, all BF16. Fused expert gate/up and down weights are actual bitsandbytes Params4bit tensors. Both optimizer steps passed with finite losses and gradients; the second step checks every trainable adapter tensor for finite nonzero gradients. Peak allocated memory was 26.108 GiB. This is a 1,024-token discarded random-token probe, not proof of completed training or all production sequence lengths. Exact receipt: environment/gpu-fit.json.
Official corpus archives complete. Frozen 1,200-passage source manifest passes document-group and content-uniqueness assertions: 1,000/100/100; 400 paraphrase and 800 notes-regeneration; OANC 1,056 and MASC 144. One malformed OANC metadata record excluded. Cross-corpus grouping records 141 links. All pinned original Instruct weights verified; exact download receipt saved. Initial production generation processed 12 passages in 1,462.009 seconds, accepted eight training pairs. Three rejections include truncation; one fails forward fidelity alone. Exact prompts, responses, rejection reasons and accepted data are copied off-instance. No quality claim about trained models; new Pangram and Emulate usage remains zero.

The resumable Qwen generation pipeline is authored and syntax checked. Every model call contains one fresh user message; regeneration receives only notes. Exact prompts, outputs, timing, truncation and both directional judgments are saved. Invalid or truncated judgments reject a pair. An initial small production batch will measure throughput before the full run.

## Recovery sequence
1. Verify completed archives, licenses and actual 4-bit GPU load/backward/optimizer memory.
2. Build source manifest, deduplicate MASC/OANC source documents, split, sample; preserve attribution and hashes.
3. Generate/filter using open instruct model and spot-check 20 AI drafts in Pangram.
4. Train both comparable adapters; checkpoint and measure costs.
5. Freeze evaluation inventory and first Emulate mappings; generate/serve/score all conditions.
6. Publish report and evidence, verify private adapter copies, stop GPU.
Ordinary engineering failures remain execution work. Pause only at a directive's actual human/access/material-choice/budget/private-destination boundary.

## Governance
Live default-branch universal AGENTS and Joel Articles skill/map/governance read, with task-specific lab guidance. Universal routing dependencies resolved from a full current checkout. Decision experiment assurance; focused fit/data checks, not a release campaign. Test-cost observer started before substantive testing.
Actual available browser control is the signed-in local desktop Brave session; a Cloud Browser surface was unavailable. This transport difference is recorded explicitly.

## Evaluation and transfer checkpoint
All 53 A/B learning inputs and 51 chronological first Emulate outputs are frozen against overnight commit 45caa139a94bc5919e26a7026dca05118acc2229, with exact input/output hashes. Thirteen exact first Emulate outputs now have reusable Pangram-alone results, hash-bound against the newer overnight commit 0994f82d0b5ca594f12994870b975da95739316f; no additional paid scans. A22 and A25 had no saved output. A direct A22 API request confirmed HTTP 400 `too_short` / minimum 40 words, with zero charge; A25 is shorter and was not redundantly submitted. Owner selection about a 51-case common comparison versus expanded originals is pending; this does not block training.

Installed Xet checkpoint downloading emitted repeated stall/retry warnings. Whole-file HTTP also disconnected partway through large files. A ranged 8 MiB transfer succeeded; the original pinned checkpoint is now downloading with distribution-package aria2, eight resumable connections per file and four concurrent files. Every file must match the pinned LFS SHA-256 before cache installation. Raw transport logs are private. The only environment change is the aria2 distribution package, recorded on the instance; Python/CUDA packages remain unchanged. Actual GPU backward/fit evidence remains pending. Training/evaluation scripts are authored and syntax checked, not runtime-certified.

Post-training meaning evaluation, frozen general-case selection, result assembly and tells scoring are authored and syntax checked. None has produced a model quality result. General selection is predeclared as the 20 shortest accepted held-out AI counterparts before detector scoring, within a 2,800-word initial allowance; report its short-paragraph sampling limitation. Meaning scoring requires both training manifests COMPLETE and the same dataset hash. Invalid/truncated open-judge responses stay unscored.

At the previous checkpoint, the managed segmented downloader was verified RUNNING with aria2 1.37.0. The fit service was STOPPED until transfer completion; a managed benchmark controller was verified RUNNING and waiting. It launches only 12 production pairs after the new two-step fit report PASS and fit service EXITED. Controller and fit code are published; all individual adapter tensors are checked for finite nonzero gradients after the first optimizer update. Transfer at that checkpoint: about 11 GiB of new retained pieces plus one previously verified 3.7 GiB shard. Billing at that checkpoint: replacement $0.91 total, including GPU $0.54, storage $0.13, download $0.24; provider values are rounded/delayed.

## Browser access interruption — 2026-09-29 06:28 UTC

Last successful terminal observation showed the managed downloader and waiting benchmark controller RUNNING, with fit STOPPED. The previously cached first shard and newly completed third shard were verified against the pinned model revision; other retained shards were still transferring. No complete model load or successful optimizer step was observed.

The selected desktop browser subsequently reported unavailable. Current browser inventory contains only the in-app browser. A recovery navigation to the Vast console reached its signed-out login form, which is positioned for the owner's human sign-in. No browser storage, credentials, alternate SSH access, or security-warning bypass was used. Required server inspection and console shutdown cannot be performed through the currently authenticated surfaces. Background services may continue, but that is unverified; no shutdown claim is made. The owner was informed of the approximately $0.55/hour continuing-charge risk and asked to reconnect the browser or sign in, or stop the replacement instance without destroying it if recovery is delayed.

Latest published GPU fit code (ff40515) requires all 16 pinned weight files verified, preserves abandoned public-model partials outside the Hub blobs directory before loading, and records actual device placement and expert quantization/layout. Publication is verified. Installation of these latest additions on the instance is **unverified**: the last observed remote checkout was 3d997b8; a subsequent fast-forward/copy command was submitted but its result was lost with browser access. Do not confuse published source with deployed code.

On restored access, first inspect the three supervisor services, download manifest, GPU-fit report, current remote commit and copied GPU-fit source. Deploy the published fit source without restarting a healthy segmented downloader. If the loader started with stale partials and invokes its unsafe-partial recovery, stop only the fit and its orphan download children, preserve the suspect partials, install the current guard and resume from verified complete weights. Require the actual two-step gradient/memory report before the benchmark controller may generate pairs. Continue the full owner-authorized pilot after access restoration; this checkpoint is not pilot completion.

Local measured verification at this interruption: 5,220.97 seconds elapsed, 559.71 seconds of observed tests (10.72%), 23 focused runs, two failure-discovering runs, zero full/mutation or forced redundant green reruns. Remote fit telemetry remains to be recovered separately.


## Access restored and bounded scale test — 2026-09-29 14:54 UTC

The signed-in Vast console and existing Brave Jupyter terminal are available. Three original pilot supervisors had exited successfully while browser access was unavailable. Remote tracked checkout was clean at d5ee5d3; fast-forward to e31b1ae and installation of the latest fit guard completed without rerunning the passed fit. Completed fit/download/first-benchmark services now have autostart=false.

The next production batch processes exactly 16 new source passages at batch16, preserving the same model, prompts, sampling temperature and bidirectional open-model filters. Initial generation manifest/status are preserved under generated/run-history before later runs overwrite their summary files. Batch16 and a separate pinned Base downloader were verified RUNNING. Before the Base transfer, actual free disk was 126,750,175,232 bytes. No package changes were made during recovery.

Replacement instance costs at this checkpoint: $6.08 total, $4.40 GPU for 9.99 hours, $1.08 storage, $0.59 download for 90.7 GB, and upload below $0.01. Values are rounded and delayed. The full run is not admitted until actual batch16 timing and available credit support it within all caps. No top-up has been performed. A fresh larger-batch measurement changes runtime/budget admission; another unchanged fit would not.

Universal root and project/lab authority read fresh this turn; selected controls reloaded from current universal checkout 8eae0dce2d4e3c4a61135f01647158594689f911 after compaction. Parent outcome remains OPEN. Next actor is the worker, continuing generation throughput and budget checks, then both comparable trainings and required scoring. The earlier ACCESS_BLOCKED checkpoint is historical.

Detector reuse refresh: connected GitHub read of the current overnight Pangram log, followed by exact output-hash validation at dcc04891815680d70a838f5ad3cf5ec24865fb8e, yields 48 reusable first-Emulate-alone results (48 of 51 saved outputs). No new paid scan, no E_holdout access, and no baseline text change.
