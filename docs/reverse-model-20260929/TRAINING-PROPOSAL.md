# Reverse-model training proposal

**29 September 2026 · Proposal only · For Joel and Claude’s review**

All external sources below were checked on **2026-09-29**. Published prices are USD before tax. Experiment sizes and decision thresholds are proposed choices; hardware, throughput, work duration and project budgets are **estimates**, not measured results. No training, paid evaluation or deployment is authorized by this document.

## 1. Recommendation

Run a **1,600-example pilot comparing an 8B base model with its post-trained counterpart**, initially using the same small rewrite fine-tune. Start Write with **draft → rewrite**, but include a direct-generation experiment. Keep the general model independent of Joel’s voice. The pilot covers English; other languages require their own evaluation.

The proposition worth testing is that conditioning on a complete draft gives a base model enough substance to write coherently while a human target teaches different prose habits. Neither base-model superiority nor chat-model resistance is established. Reverse generation also cannot recover a unique original: several good human realizations can express the same content.

Success means **the same output preserves everything and passes in context**, clears applicable hard lint rules, and has appropriate register, acceptable latency and affordable serving. Separate good scores on different candidates do not count.

Claude’s four-call record supports this distinction: all outputs passed alone, but one failed in context and the context-passing version changed meaning. This is diagnostic evidence, not a reliable estimate of Emulate’s overall performance. The checked run log contains those four calls; no completed overnight study is incorporated. Its output-word counts differ from the narrative report, so the benchmark must adopt one documented counter.[R1]

Emulate documents one output per humanize call and a prompt→draft→humanize Write pipeline. Its own-model research claim supplies no reproducible architecture, training set or ablation evidence.[1]

## 2. Training rights before spending

**The proposed GPT/Claude corruption pipeline needs a permissions decision.** OpenAI’s Services Agreement restricts using outputs to develop competing models, with limited exceptions. Anthropic’s commercial terms restrict building competing products, including model training, without express approval. An independently served general rewriter does not obviously qualify for OpenAI’s stated exceptions. This is a contractual issue requiring confirmation, not a conclusion that this particular project is prohibited.[2]

Establish the applicable account/provider terms and obtain written permission where necessary, covering synthetic drafts, extracted outlines and judge-derived training labels. Routing calls through another provider is not evidence of permission.

An open-model-only pilot remains an alternative: use the licensed Qwen post-trained models below as corruption teachers. Label that result **feasibility on open-model drafts**; it cannot establish matched performance on Joel’s GPT/Claude workflow. Keep Emulate outputs exclusively as benchmark evidence. Confirm Pangram permits the intended preference-training use; its published terms do not explicitly settle that use.[3]

## 3. Human sources and amounts

Pre-November-2022 publication is useful evidence, not an absolute authorship guarantee. Require an identifiable author, historical edition/version and provenance; exclude later replacements, machine-generated material and uncertain attribution.

| Source | Verified available amount | Rights and proposed use |
|---|---|---|
| **Open American National Corpus (OANC)** | 14,623,927 words; 11,406,155 written. Includes 4,238,808 Slate journalism words, 3,349,714 biomedical words and 409,280 PLOS words. | Publisher grants unrestricted use and redistribution, including commercial use. Select **up to 4 million written words** across essays, news, technical and practical prose; exclude speech.[4] |
| **MASC** | 506,768 words, including **27,642 email words in 78 files**. | CC BY 3.0 US. Use email, letters and essays; deduplicate overlap with OANC. Email is a small supply, not millions of independent examples.[5] |
| **PG-19** | Training split: 28,602 books published before 1919; **1,973,136,207 word-level tokens**, not a measured post-filter word count. | Repository says Apache 2.0; underlying books still require jurisdiction-specific rights review. Select **up to 1 million words**, capped at 15% of targets to avoid antique prose dominating.[6] |
| **PMC Open Access subset** | Eligible pre-2022, license-filtered word count **not yet measured**. | Article licenses vary. Select **up to 1 million words** from verified CC0/CC BY articles, using permitted retrieval routes; deduplicate OANC overlap.[7] |
| **Permissioned modern writing** | Joel’s third-party collection has **not been inventoried**; additional email permissions are **not secured**. | Target **1.5 million words** of modern books, personal/practical essays and correspondence. Require appropriate training/processing rights and third-party privacy permission; possessing a copy is insufficient. |

These are acquisition ceilings, not a claim that 7.5 million usable words are already available. Count unique words after filtering. Modern books and email are the main acquisition gaps; do not fill them by repeatedly recycling a handful of writers.

For the pilot, collect roughly **1,000 distinct passages**, averaging an estimated 150 words, with all five genres represented. Split by **author, book, email thread and source document before making pairs**. Keep heading and real neighboring paragraphs. Limit each author’s share, deduplicate approximate matches, and preserve dialect, formality and genre. Joel’s material stays out of general training.

## 4. Making faithful reverse pairs

Use **960 regenerated pairs, 480 paraphrase pairs and 160 identity examples** in the 1,600-example training set. Identity examples teach restraint on already satisfactory prose. Allocate another 200 examples to development, from separate source groups.

For paraphrases, ask the teacher to express the original more clearly while retaining its paragraph plan; verify how much structure actually survives. For regeneration, extract a complete content record, then have a fresh teacher context write from that record **without seeing the original wording**. Include facts, examples, negation, qualifications, chronology, causal links, actor→action→object, quotations, numbers, units and URLs. Preserve relationships without demanding one sentence per point or the original paragraph order.

After permission is established, a starting teacher mix is **40% Claude, 40% GPT, 20% open models**. Recover exact model IDs, reasoning settings and prompt styles from actual drafting logs. Sample outline-based drafting, bare prompts, long contextual drafting and revision requests. Do not substitute a generic “sound AI” prompt for that distribution.

**Every accepted pair needs two-way meaning coverage:** the AI input supports every substantive human-target claim, and the target retains every substantive AI-input claim. Reject omissions, additions, reversals and uncertain cases; never invent missing target details or quietly trim the human original to make it fit.

At scale, combine exact checks for protected strings and values with an independently prompted judge that returns claim-to-span mappings in both directions. Check implied agency and certainty, not just matching entities. A second judge reviews disagreements, sensitive claims and a random 20%; humans audit 100 pilot pairs. Calibrate judges on deliberately broken examples, including Claude’s tick-box reversal. Set a proposed 95% critical-error detection target before trusting automated filtering; report residual disagreement rather than calling the process infallible.

Run the linter before paid scoring. Its `REVIEW` flags are not universal bans, and `CLEAR` does not certify meaning. Apply generic hard rules in both modes and Joel-specific bans only where requested. Judge `REVIEW`-flagged contrasts, lists and instructions in their genre.[R2] Sample both human and synthetic sides with Pangram; do not discard authentic writing merely because a detector dislikes it. Reserve detector-qualified selection for preference labels.

## 5. Models and training

Two candidate sizes give a controlled comparison without an expensive model sweep:

| Candidate family | Verified checkpoints and license | Context | Hardware estimate at a 4,096-token training length |
|---|---|---|---|
| **Qwen3 8B** | `Qwen3-8B-Base` and `Qwen3-8B`; 8.2B parameters; Apache 2.0.[8] | 32,768 native tokens | Serving: 24–48 GB GPU memory. LoRA: 48–80 GB, or approximately 24 GB with 4-bit frozen weights. Full tuning: approximately 4 × 80 GB with sharding. |
| **Qwen3 30B-A3B** | `Qwen3-30B-A3B-Base` and `Qwen3-30B-A3B`; 30.5B total, 3.3B active parameters; Apache 2.0.[9] | 32,768 native tokens | Serving: 80 GB at 16-bit precision. Quantized LoRA: approximately 48–80 GB. Full tuning: approximately 8 × 80 GB with sharding. |

The official chat checkpoints are fully post-trained controls; **our short task-specific SFT creates the lightly tuned versions**. Disable thinking in chat inference. These candidates were chosen for matched base/chat comparisons, not claimed to be the newest models. Active MoE parameters reduce computation, but all expert weights still need storage. Hardware estimates include assumptions about microbatching and activation checkpointing; verify peak memory before renting a larger allocation.

Start with supervised fine-tuning (SFT), training only on target-output tokens, for **1–3 epochs**. Inputs mark the target and read-only heading/neighbors; omit context in half the examples to support paragraph-only calls. Compare base and chat using the same examples and rank-64 LoRA, adapting attention and feed-forward projections. Compare paraphrase-only, regeneration-only and mixed data on matched source groups and token budgets. Judge structural improvement through blind readings of paragraph development, emphasis, transitions and repetition, alongside fidelity; sentence-length variance alone is inadequate.

LoRA cheaply changes a limited set of weight directions; full tuning changes all weights.[10] Joel’s unsuccessful GPT experiment cannot identify the cause without its actual platform, dataset, settings and checkpoints—even its use of LoRA needs confirmation. Weak pairs, formatting, insufficient updates and restrictive adaptation are competing explanations. Research finds LoRA/full-tuning differences in other tasks, but does not settle prose rewriting.[11] Include one matched full-tuning diagnostic on the better 8B starting checkpoint, selected on development data.

Then generate **four candidates for each of 200 training inputs**. A chosen response must preserve meaning, clear applicable hard lint rules and pass in context; a rejected one may drift or fail detection. Omit groups without a valid chosen candidate. Apply a small **direct preference optimization (DPO)** update, retaining SFT examples and monitoring length inflation and lost diversity.[12] Keep development/test outputs out of preference training. At full scale, consider 50,000 SFT examples and 5,000 four-candidate preference groups, subject to the pilot.

## 6. Frozen evaluation and Write mode

Freeze **100 AI paragraphs**: 30 from guide sections and Claude’s failed drafts, plus 70 general examples, 14 each from academic writing, books, email, news and essays. Match real source-model and prompt diversity. None of these passages, source documents, fixes or neighboring text may enter training/development. Do not read, copy or use `articles/inner-child-therapy/experiments/emulate-20260929/inputs/learning/E_holdout/`; Claude’s reservation remains intact.

Keep **20 separate Write prompts**, four per genre, targeting 300 words. Half should include a fact packet with explicit constraints. Fiction gets an invented-world consistency check, not an external-fact requirement.

Compare raw drafts, untuned chat rewriting, both SFT variants, the selected DPO model and Emulate. Choose checkpoints on development data, then run the frozen test once. Give each system one output per input. Repeat a fixed 20-paragraph subset three times for variability, counting every call rather than selecting the prettiest result.

The primary matched-input comparison gives both rewriters the **same paragraph**, then inserts each output into the unchanged real section. Separately test context-aware target rewriting and 20 whole-section rewrites. Emulate’s API has no separate read-only-context field, so do not disguise a richer-input advantage as a model-quality victory. Whole-section comparisons give both systems the same editable scope.[1]

Measure **Pangram alone, complete-section classification and target-overlapping windows**. A strict section pass requires `Human`, zero AI/AI-assisted fractions and human-written target windows; a green average must not hide a flagged target. Report neighboring-text failures separately without deleting them. Explicitly select `pangram-4`, retain the returned version and exact text, and map offsets against Pangram’s returned normalized text. Record humanizer flags too, without silently changing the primary endpoint.[13]

Measure complete meaning preservation with bidirectional, point-by-point judging; independently count exact facts, names, numbers and links. Report linter hits per 100 words by rule/severity, omissions, additions, expansion ratio, register match, complete-response latency (median/95th percentile, warm/cold), and cost per 1,000 **input and accepted output words**. Joel blindly reads 30 paired results; a second reader covers unfamiliar genres. Use document-grouped uncertainty intervals; 100 paragraphs cannot establish universal reliability.

For Write, compare **Emulate `/v1/write`, chat alone, chat→rewriter, and a direct-generation SFT variant** trained on detailed briefs derived only from training sources. Score prompt→draft and draft→rewrite fidelity separately: humanizing cannot repair an unsupported draft reliably. Prefer two steps unless direct generation preserves quality and reduces measured total latency by at least 25% on development, then survives the frozen Write test.

## 7. Pilot decision and budget

**Proposed scaling gate:** at least 90/100 strict contextual passes, at least 98/100 fully faithful outputs, zero major reversals or fabricated/protected-fact errors, and a joint success rate at least 10 percentage points above Emulate. Context-pass rate should be no more than five points below Emulate. These are pilot point-estimate gates, not statistical proof or release approval. Require no genre collapse in blind reading, warm median at most nine seconds on the matched 75–180-word subset, and an affordable serving configuration at the expected monthly volume.

Stop scaling if detector gains depend on distortion, if validated data plus the LoRA/full diagnostic show no useful joint improvement, or if permissions, latency or real-volume costs cannot meet the goal. An ambiguous result earns a specific corrective experiment on new data only when its expected value fits the remaining budget.

Pangram 4 costs **$0.05 per started 100-word block**, with a **20% bulk discount**: $0.04 per block. A 150-word standalone check plus a 600-word contextual check therefore costs **$0.32 in bulk**. The context is billed too.[14]

**Pilot detector estimate**, using that example length: 320 source-side checks for the corpus sample ($102.40); 400 development outputs ($128); 800 preference candidates ($256); 600 frozen-test outputs across six arms ($192); and a 280,000-billable-word allowance for Write, repeats, controls and section comparisons ($112). Total: **$790.40**, rising with longer sections. Cache exact text/model results and retain failed cases.

| Cost component | Pilot estimate | Full-scale estimate, additional after pilot |
|---|---:|---:|
| Pangram | $790–1,000 | $9,600–12,000 |
| Synthetic data and semantic judging | $150–400 | $1,500–4,000 |
| Training, candidate generation and serving tests | $100–400 | $1,000–4,500 |
| Emulate benchmark allowance | $50–100 | $200–500 |
| Storage and operating allowance | $50–100 | $200–500 |
| **Total, including roughly 25% contingency** | **$1,400–2,500** | **$16,000–27,000** |

Full detector estimate assumes 4 million billed words for source sampling, 16 million for 20,000 preference candidates, and 4–10 million for development/evaluation. These costs are avoidable only by reducing scans, negotiating rates or obtaining eligible credits; none is assumed. Generation/judging allowances are estimates, not quotations for unverified GPT/Claude model IDs.

Estimated pilot duration: **7–10 working days after rights clearance**, with **40–80 hours of human/engineering work**. Full version: another **4–8 weeks and 120–240 hours**, mainly data review, evaluation and serving work. Labor, legal advice and licensed-text acquisition are excluded from cash totals; their prices are unknown. At an illustrative labor rate of $50/hour—not a market quote—add $2,000–4,000 and $6,000–12,000 respectively. Approve the pilot separately; it creates no full-scale spending commitment.

## 8. Serving and unit economics

Both **Runpod Pods** and **Hugging Face Inference Endpoints with a custom container** can host our own merged checkpoint. This avoids assuming that a stock-model API accepts arbitrary adapters.[15]

For 300 output words, assume **400 output tokens**, a short contextual input and one warm request. The following are **unmeasured latency and busy-compute estimates**, excluding idle time, retries and semantic/detector calls:

| Configuration | Published hourly rate | Estimated completion | Estimated GPU cost/1,000 output words |
|---|---:|---:|---:|
| 8B, Runpod L40S 48 GB | $1.09 | 5–10 seconds | $0.005–0.010 |
| 8B, Hugging Face AWS L40S 48 GB | $1.80 | 5–10 seconds | $0.008–0.017 |
| 30B-A3B, Runpod H100 PCIe 80 GB | $2.89 | 6–15 seconds | $0.016–0.040 |

Rates come from current provider tables; actual checkpoint speed requires measurement.[16] For training, Runpod lists A100 80 GB Pods at $1.59/hour and A100 SXM clusters at $1.79/GPU-hour; do not mix Pod and cluster quotes.[16]

**Idle hosting changes the answer.** A continuously running $1.09/hour GPU costs $784.80 per 720-hour month: **$13.08/1,000 words at 60,000 words/month**. Emulate’s displayed annual Pro plan is $264/year for 60,000 words/month, equivalent to **$0.367/1,000 fully used words**; extra words cost $1/1,000. Monthly-cancel pricing was not verified.[17]

Therefore, private low-volume use needs session-based hosting, measured scale-to-zero behavior or an already-paid GPU. Cold starts may defeat the speed target. Do not recommend an always-on endpoint for Joel merely because its busy-compute cost looks cheap. Count initialization, idle time and training amortization: a $20,000 build adds $0.20/1,000 words even when spread over 100 million words.

The fast path returns one rewrite with deterministic protected-span checks. Optional semantic/Pangram verification has separate latency and pricing; it must not be hidden inside the cheap estimate. A failed check returns an explicit failure/original, counted as unsuccessful—not a falsely certified rewrite.

## 9. Joel’s optional mode and remaining risks

The catalogue records **125 entries, only 58 with an AI “before”**, and mixed authorship in some article comparisons.[R3] Recover exact pairs and distinguish Joel’s same-meaning edits from re-authoring that changes content. The latter cannot train a lossless rewriter. Start with retrieved examples and Joel’s bans; a small separate adapter comes later. An estimated **200–500 additional genuinely Joel-authored paragraphs** across relevant registers would provide better evidence than duplicating the current fixes. Keep a whole-article holdout and never use Joel-mode gains to claim general-model superiority.

A detector can learn this model’s signature. Preserve dated controls and retest after meaningful detector changes; a Pangram score does not make AI output human-authored. Prevent generic casualness, fake anecdotes, deliberate mistakes and obsolete book diction through blind genre evaluation. Test unfamiliar drafting models and leave-one-teacher-out development splits. Audit memorized passages against training sources. Maintain license/attribution manifests and deletion provenance. Emulate’s terms allow submitted material to improve/train its models, so do not send confidential evaluation material there without suitable permission.[18]

**Questions for Joel before a pilot:**

1. Is this principally a private writing tool or a service for other writers, and what monthly word volume should the cost test assume?
2. Is a separately approved pilot ceiling of $2,500, excluding labor and rights acquisition, acceptable?
3. What exact platform/configuration was the unsuccessful GPT fine-tune, and which current drafting model IDs/prompts should the pair generator match?
4. Which modern books, essays and correspondence in the available collection have permission for training and external processing?
5. Is occasional cold-start delay acceptable, or must the first request also meet the 5–9-second target?

## Source register

**Access date for every URL: 2026-09-29.** Repository evidence is pinned to base commit `2b10db4492d0ba06ee02aa0d07f1c3ce454f7fe8`; later overnight findings require a separate revision. Claude’s independent review has not yet been run.

- **[1]** Emulate [API](https://www.tryemulate.ai/docs/api); [research claim](https://www.tryemulate.ai/research/mode-collapse), published 2026-09-25.
- **[2]** [OpenAI Services Agreement](https://openai.com/policies/services-agreement/), §3.3 and “Permitted Exception”; [Anthropic Commercial Terms](https://www.anthropic.com/legal/commercial-terms), §D.4.
- **[3]** [Pangram terms](https://www.pangram.com/terms-of-service), updated 2025-08-14.
- **[4]** OANC [use grant](https://anc.org/data/oanc/) and [word counts](https://anc.org/data/oanc/contents/).
- **[5]** MASC [license](https://anc.org/data/masc/) and [genre counts](https://anc.org/data/masc/corpus/).
- **[6]** DeepMind [PG-19 dataset, counts and license](https://github.com/google-deepmind/pg19); Project Gutenberg [permissions and territorial limits](https://www.gutenberg.org/policy/permission.html).
- **[7]** [PMC Open Access subset](https://pmc.ncbi.nlm.nih.gov/tools/openftlist/), last modified 2026-08-24.
- **[8]** Official [Qwen3-8B-Base](https://huggingface.co/Qwen/Qwen3-8B-Base) and [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) cards.
- **[9]** Official [Qwen3-30B-A3B-Base](https://huggingface.co/Qwen/Qwen3-30B-A3B-Base) and [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B) cards.
- **[10]** Hu et al., [LoRA](https://arxiv.org/abs/2106.09685), 2021.
- **[11]** Biderman et al., [LoRA Learns Less and Forgets Less](https://arxiv.org/abs/2405.09673), 2024.
- **[12]** Rafailov et al., [Direct Preference Optimization](https://arxiv.org/abs/2305.18290), 2023.
- **[13]** Pangram [current detection schema and normalization](https://docs.pangram.com/api-reference/ai-detection).
- **[14]** Pangram [API prices](https://www.pangram.com/solutions/api) and [started-block billing](https://docs.pangram.com/api-reference/bulk-api).
- **[15]** Runpod [Pods](https://docs.runpod.io/pods/overview); Hugging Face [custom containers](https://huggingface.co/docs/inference-endpoints/guides/custom_container).
- **[16]** Runpod [GPU prices](https://www.runpod.io/pricing); Hugging Face [dedicated endpoint prices and billing](https://huggingface.co/docs/inference-endpoints/pricing).
- **[17]** Emulate [pricing and annual billing](https://www.tryemulate.ai/pricing).
- **[18]** Emulate [terms](https://www.tryemulate.ai/terms), effective 2026-09-26, §03–05.
- **[R1]** Repository [Claude API test](https://github.com/u-dont-existDOTcom/joel-articles/blob/2b10db4492d0ba06ee02aa0d07f1c3ce454f7fe8/articles/inner-child-therapy/experiments/emulate-20260929/runs/CLAUDE-API-TEST.md) and [run log](https://github.com/u-dont-existDOTcom/joel-articles/blob/2b10db4492d0ba06ee02aa0d07f1c3ce454f7fe8/articles/inner-child-therapy/experiments/emulate-20260929/runs/emulate.jsonl), dated 2026-09-29.
- **[R2]** Repository [tells_lint.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/2b10db4492d0ba06ee02aa0d07f1c3ce454f7fe8/articles/inner-child-therapy/tools/tells_lint.py), blob `dd64ea3c09f5ca6c49e60fdc9fd62eff896d481e`.
- **[R3]** Repository [Joel fixes catalogue](https://github.com/u-dont-existDOTcom/joel-articles/blob/2b10db4492d0ba06ee02aa0d07f1c3ce454f7fe8/articles/inner-child-therapy/tools/JOEL-FIXES-CATALOGUE-20260928.md), dated 2026-09-28.
