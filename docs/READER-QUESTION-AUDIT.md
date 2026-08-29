# Reader-question audit

Status: **ACTIVE OPTIONAL DIAGNOSTIC.** This is not article authority and is not a mandatory publication gate.

## Purpose

Use this method when a long article may contain important negative space that a positive structure map does not expose well: unanswered reader questions, answers that arrive too late, distributed answers that are hard to see, unstated boundaries, or questions that should be explicitly routed out of scope.

Mermaid remains the required compact article-architecture map. This audit complements it; it does not replace it.

## When to use

Use selectively for broad long-form articles, major publication-preparation passes, or cases where the article's promise is expansive enough that ordinary whole-article review may miss reader-state problems.

Skip for trivial/local edits, short pieces, or when the likely marginal value is low.

## Core protocol

### 1. Promise-first freeze

Before reading the body, give a genuinely fresh reader only the title, subtitle/opening, intended audience, and explicit scope statement.

Freeze the small set of material questions the opening reasonably promises or strongly implies. These are expected questions, not automatic defects.

### 2. Sequential blind-prefix pass

Reveal the article in sequential natural or fixed windows. Future text must be genuinely unavailable to the reader, not merely present in context behind an instruction not to look.

At each checkpoint, freeze up to a few **material live questions**: questions whose later handling could plausibly affect coherence, usefulness, section architecture, an interlink, or an explicit scope boundary.

A checkpoint may have zero questions. Do not generate generic `what about X?` prompts merely because a topic exists.

Do not revise earlier checkpoints after later text appears.

### 3. Final hindsight coverage pass

Only after the complete article is revealed may the reader use the whole text in hindsight.

Merge semantically duplicate questions and classify each surviving question as one of:

- `answered`
- `answered-later`
- `partial`
- `thin`
- `unanswered`
- `intentionally-out-of-scope`
- `question-rejected-by-article`

Name the actual section(s) supplying coverage.

Then separately classify whether the question represents:

- `candidate` article defect;
- `unclear` / needs owner-editor judgment;
- `not-a-defect`.

An unanswered question is never automatically an article defect.

### 4. Keep a reduced result

Do not persist every transient checkpoint question as a permanent task.

Retain only:

- genuine `candidate` questions;
- a small number of `unclear` questions worth owner review;
- a few answered controls showing that the method can recognize existing coverage;
- externally supported opportunities kept explicitly separate from article-internal findings.

## Independence requirements

Independence must be real. Do not call a second self-prompt inside the same saturated drafting conversation independent.

For a strong run:

- use a fresh model/context;
- withhold prior editorial rationales, gap hypotheses, architecture explanations, detector results, and external benchmark conclusions;
- prevent access to unrevealed future article text;
- reveal only the next source window after the current checkpoint is frozen.

Mechanical collection and editorial reasoning should be separated when practical. A deterministic collector may verify the canonical source identity and produce immutable windows; the reader should receive those windows sequentially without repository access.

## External-demand pass

External frameworks, research, search demand, reader comments, correspondence, or forums may be used **after** the article-internal blind result is frozen.

External support can show that a topic matters to readers. It does not convert that topic into an article defect.

Keep provenance distinct, for example:

- `article-internal`
- `framework-supported`
- `research-supported`
- `actual-reader-supported`

## Relationship to other repository controls

- `ARCHITECTURE.md` / Mermaid: positive structure, section order, protected functions, dependencies, stopping point.
- Multiscale editorial ledger: section/paragraph jobs, reader entry/exit state, recurrence, post-assembly proofread.
- Argument/evidence architecture: claims, evidence, competing explanations, certainty, premise failure.
- Reader-question audit: negative-space and reader-state diagnosis across the article.

Do not duplicate claim/evidence bookkeeping here.

## Romance pilot result

The 2026-08-29 Romance pilot validated the method but rejected its Obsidian visualization layer.

The blind reader independently reproduced the deepest workability/incompatibility/ending cluster, found a new sexual-fit trajectory question, recognized many delayed/distributed answers, and downgraded several plausible hidden hypotheses. Most surviving questions were ultimately judged not to be article defects.

The Obsidian Canvas representation was then rejected by the owner as visually noisy and harder to use than the compact comparison/report view. Do not require Obsidian for this method.

## Output preference

Prefer a compact table, Markdown report, or small structured JSON register. Add another visualization only if it demonstrably makes a real editorial decision easier than the compact representation.
