# Reverse model pilot — execution checkpoint

Status: OPEN — downloads and actual GPU fit verification; generation, both trainings, evaluation and final reporting remain unexecuted.

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
Meta-only PEFT construction covers attention plus fused expert gate/up and down parameters at rank 64: 2,570,059,776 trainable parameters. This proves parameter coverage/count only. PEFT emits an expert-layer compatibility warning; actual load/backward and gradient coverage must pass before training.
Official corpus archives complete. Frozen 1,200-passage source manifest passes document-group and content-uniqueness assertions: 1,000/100/100; 400 paraphrase and 800 notes-regeneration; OANC 1,056 and MASC 144. One malformed OANC metadata record excluded. Cross-corpus grouping records 141 links. Pinned instruct checkpoint is still downloading in the single workspace cache. The fit is stopped while a segmented downloader verifies all original weights; no PASS claim yet. No training pairs or scores; new Pangram and Emulate usage is zero.

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

Managed segmented downloader is verified RUNNING with aria2 1.37.0. The fit service remains STOPPED until transfer completion; a managed benchmark controller is verified RUNNING and waiting. It launches only 12 production pairs after the new two-step fit report PASS and fit service EXITED. Controller and fit code are published; all individual adapter tensors are checked for finite nonzero gradients after the first optimizer update. Last observed transfer: about 11 GiB of new retained pieces plus one previously verified 3.7 GiB shard. Billing at this checkpoint: replacement $0.91 total, including GPU $0.54, storage $0.13, download $0.24; provider values are rounded/delayed.
