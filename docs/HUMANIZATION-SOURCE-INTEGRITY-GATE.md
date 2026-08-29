# Humanization source-integrity gate

Status: **BLOCKING for production humanization, detector repair, and source recovery.**

Owner correction: 2026-08-29.

## Core rule

**Human provenance is not insertion authority.** A passage does not belong in an article merely because Joel wrote it, a human wrote it, Pangram calls it Human, it resembles Joel's voice, or it improves a detector score.

Humanization means making the article's **actual authorized content** read naturally. It does not mean padding, replacing, or surrounding difficult prose with unrelated Human text.

## Source-relevance gate

Before prose from another document, article, chat, transcript, corpus sample, publication, or external source can enter production copy, it must independently earn its place by performing a real article function. At least one of these must be true:

1. it is the owner-authored realization of the **same unsuperseded claim, memory, instruction, distinction, example, or rhetorical function** already required at that location;
2. it is a quotation, formula, title, remembered wording, or other identity-bearing language whose exact wording itself matters;
3. it is evidence that the article genuinely needs to quote or attribute there, independent of detector considerations;
4. Joel explicitly directs a cross-article callback or reuse and the destination passes heading, paragraph-job, live-question, chronology, causality, and provenance checks.

If none applies, the source is **calibration/context only**. It may inform how to think or write, but its prose may not be transplanted into the article.

## Explicit prohibitions

Do not:

- copy a Human/Pangram-green sentence or paragraph from another article merely to lower the AI fraction;
- build a `Human spine` by stitching together unrelated Human snippets and then filling gaps around them;
- treat cancer, Romance, community, research, transcript, or other corpus prose as reusable Somatic prose merely because it is demonstrably Human;
- borrow another source's syntax, anecdotes, transitions, jokes, examples, or texture as detector camouflage;
- use an external factual source as a prose donor or `factual spine` when its actual job is only evidentiary support;
- preserve irrelevant imported text because removing it would worsen Pangram;
- count detector improvement produced by irrelevant imported Human text as a successful humanization result.

A candidate that improves Pangram by importing functionally unrelated Human prose is **SOURCE-CONTAMINATED / FIDELITY-REJECTED**, even if its detector result is 100% Human.

## What legitimate source recovery means

`Source recovery` means recovering higher-authority material for the **same article content/function**: for example, the owner's natural realization of the exact inner-child conflict being discussed, the original wording of a personal event already required by the article, or registered article/source evidence that restores an existing claim without changing its role.

It does **not** mean searching for any Human wording that can be made to fit approximately.

Good owner prose may still be reused substantially when it is genuinely the right source for the current thought. Relevance and placement come first; detector status comes last.

## External evidence boundary

Research sources normally contribute facts, evidence, attribution, and quotations when quotation itself is warranted. Their prose style is not a humanization resource. Synthesize the supported point in Joel's article voice unless the source must be quoted for a reader-facing reason.

The same rule applies to official guides, clinical pages, books, interviews, and other authored materials. `Human-written` is not a reason to copy their wording.

## Corpus and detector-research boundary

Human corpus passages are legitimate as:

- detector controls;
- Human→controlled-intervention baselines;
- idiolect/style calibration;
- evidence about model-shaped operations.

They are **not** publication building blocks unless they separately pass the source-relevance gate above.

Detector experiments may deliberately perturb Human text for research. Their successful cells do not automatically become article prose.

## Required production check

For every imported/recovered Human span in a production candidate, record:

- source identity and provenance;
- exact target article function;
- why this source belongs at this exact destination independent of Pangram;
- whether the wording is exact reuse, minimum normalization, quotation, or fresh synthesis;
- forward and reverse preservation mapping;
- confirmation that removing detector considerations would not change the decision to include it.

If the last answer is `no`, reject the insertion.

## Somatic R17–R58 correction

The stopped `experiment/somatic-r17-100-human-gate-20260828` line remains historical detector/editorial evidence only. In particular:

- the R17 syntax-transplant experiments correctly falsified syntax transplantation as a general method;
- R18's `Human spine` wording must **not** be promoted as a production method;
- later `source recovery` experiments are valid only to the extent that the recovered source independently carries the exact Somatic claim/function or required evidence at that location;
- no lesson from R17–R58 authorizes importing unrelated Human snippets, corpus prose, or external-source wording to improve Pangram;
- R17–R58 candidates remain non-authoritative and require source-integrity review before any future promotion consideration.

Preserve failed experiments and detector receipts as evidence. Retire the bad methodology, not the history.
