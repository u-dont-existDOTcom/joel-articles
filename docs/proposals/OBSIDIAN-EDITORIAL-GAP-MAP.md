# Obsidian Editorial Gap Map — proposal

Status: **PROPOSAL / NON-AUTHORITATIVE.** This document records a candidate editorial-analysis architecture. It does not alter article authority, required Mermaid maps, multiscale ledgers, argument/evidence rules, or owner-final prose.

## Decision summary

Do **not** replace the repository's Mermaid article architecture maps with Obsidian.

Use the layers for different jobs:

1. **Mermaid `ARCHITECTURE.md`** — compact, source-controlled structural truth about article movement, protected functions, section order, setup/payoff dependencies, and stopping point.
2. **Existing multiscale editorial + argument/evidence ledgers** — explicit granular bookkeeping for section/paragraph jobs, load-bearing claims, evidence, dependencies, recurrence, and premise failure.
3. **Obsidian Canvas** — optional human-facing diagnostic overlay for questions, assumptions, objections, rhetorical relations, reader paths, and especially *negative space*: material a reader may reasonably expect but the article does not currently supply.
4. **Obsidian Bases / structured question records** — optional filterable dashboard for unresolved, partial, intentionally out-of-scope, interlinkable, and resolved reader questions.

Obsidian is a view/workbench, not article authority. A Canvas finding is diagnostic evidence and never authorization to change owner-final prose.

## Why this adds something the current Mermaid map does not

The current architecture maps are deliberately positive representations: they show what is present, where it lives, and how consequential functions depend on one another. The multiscale ledger already records reader state/question on section entry and exit.

The remaining useful problem is **negative-space visibility**:

- What important question did the article cause a reader to ask but never answer?
- What question would a reasonable member of the intended audience expect from the title/thesis even if the draft never raises it explicitly?
- What premise is being assumed rather than established or named?
- What strong objection is not addressed?
- What concept is used before a reader has enough context to understand it?
- What answer exists, but arrives so late that the reader spends several sections confused?
- What material belongs in another Joel article and should be linked rather than repeated?
- What apparent gap is actually intentionally outside scope and should stay out?

A conventional section Mermaid graph becomes unreadable if all of these objects are added. Obsidian Canvas is better suited to a spatial overlay with many heterogeneous node types.

## Existing-work composition rather than reinvention

This proposal adapts established approaches instead of inventing a new theory of article structure:

- **Rhetorical Structure Theory (RST)** supplies useful relation concepts for textual coherence: evidence, elaboration, contrast, condition, cause/result, motivation, concession, sequence, etc. It is especially useful for asking whether a span has an intelligible function relative to another span.
- **IBIS / issue-based information systems** supply the useful pattern of questions/issues, positions/answers, and arguments supporting or opposing them.
- The repository's existing **argument/evidence architecture** remains the authority for load-bearing claims, source roles, competing explanations, certainty, and premise-failure impact.
- The repository's existing **multiscale editorial ledger** remains the authority for section and paragraph jobs, reader entry/exit questions, recurrence, and literal post-assembly proofread.

The genuinely new remainder is the integration: externalize the existing curious-reader model into durable question objects and expose them through a spatial Canvas / filterable dashboard without making the visualization authoritative.

## Recommended reader-question object

If this proceeds beyond a visual experiment, use one durable record per **material** reader question, not per sentence.

Candidate flat properties (compatible with Obsidian Properties/Bases):

```yaml
---
type: reader-question
article: romance
origin: blind-prefix
reader-mode: curious-novice
trigger-section: "[[master#Choosing together]]"
status: unanswered
importance: high
confidence: medium
answer-section: null
disposition: review
---
```

Suggested statuses:

- `answered`
- `partially-answered`
- `unanswered`
- `answered-too-late`
- `intentional-implicit`
- `out-of-scope`
- `interlink`
- `rejected-question`

Suggested origins:

- `expected-from-promise` — inferred from title/subtitle/intro/audience before reading the body
- `blind-prefix` — arises while reading only the article up to a section boundary
- `independent-reader`
- `external-search`
- `actual-reader` — comments, replies, email, conversation, etc.
- `owner`

Suggested reader modes are functional rather than demographic:

- `curious-novice`
- `skeptic`
- `practical-reader`
- `domain-expert`
- `personally-implicated`
- `sympathetic-reader`

Do not force every article through every reader mode. Select only those relevant to the article's real audience and purpose.

## Gap classes

A candidate question can expose several different defects. Keep these separate so “gap” does not become a generic instruction to add more prose.

- **promise gap** — title/heading/thesis creates an expectation the article does not fulfill
- **curiosity gap** — current prose naturally raises a material next question that never gets answered or redirected
- **bridge gap** — transition depends on an unstated reasoning step
- **definition/prerequisite gap** — the reader lacks a concept needed for the next move
- **boundary gap** — the reader cannot tell where a claim does or does not apply
- **objection/countermodel gap** — a strong reasonable alternative is not handled; route factual versions through the argument/evidence protocol
- **evidence gap** — a material claim lacks adequate support; existing argument/evidence architecture owns this diagnosis
- **example/contact gap** — an abstraction has no sufficient concrete anchor when one is needed
- **practical gap** — the article recommends or implies action without enough information to use the idea responsibly
- **ordering gap** — the answer exists but is positioned after prolonged unnecessary confusion
- **interlink gap** — the needed answer belongs in another Joel article
- **scope-signaling gap** — the omission is correct, but the boundary should be made explicit

A gap candidate does **not** imply that prose should be added. The disposition step protects against overcompletion.

## Four complementary audit passes

### 1. Promise-first expected-question pass

Give a fresh reader only the title, subtitle, opening, intended audience, and any explicit scope statement. Ask what material questions they would reasonably expect this article to resolve.

Then compare those expectations against the actual article.

This detects omissions that the draft itself never causes the model to notice because the draft silently avoids the subject.

### 2. Blind-prefix curiosity pass

At consequential section boundaries, give a fresh reader **only the article prefix up to that boundary**, not the future sections. Ask for the strongest live questions they would naturally carry forward.

Then map each question to later answer spans.

The prefix restriction matters: a model that sees the whole article has hindsight and can underreport moments of confusion because it already knows the later answer.

### 3. Counter-reader pass

For material claims or recommendations, run the smallest relevant set of opposing reader modes: skeptic, domain expert, personally implicated reader, practical reader, etc.

Route factual objections and premise/evidence disputes into the existing argument/evidence ledger rather than duplicating them in a parallel system.

### 4. External-demand pass

When useful, collect real question signals from search queries, forums/Reddit, comments, correspondence, related articles/books, and actual reader feedback. Cluster these against the article's question register.

External frequency is evidence of reader interest, not an obligation to satisfy SEO-style completeness. Questions may be marked `out-of-scope`, `interlink`, or `rejected-question` with reason.

## Canvas representation

A useful Canvas should remain sparse enough for visual reasoning.

Candidate node classes:

- article sections
- material reader questions
- assumptions/prerequisites
- objections/countermodels
- important claims
- examples/cases
- cross-article destinations

Candidate edge labels:

- `raises`
- `answers`
- `partially answers`
- `depends on`
- `supports`
- `contrasts`
- `concedes`
- `elaborates`
- `illustrates`
- `preempts`
- `returns to`
- `link instead`

Use RST-inspired relation names where they genuinely clarify textual function. Do not force a full RST annotation of every paragraph.

The Canvas can be generated from structured records. JSON Canvas supports file nodes that reference a Markdown file and a heading/block subpath, so section nodes can point directly to `master.md#Heading` rather than copying canonical prose into the Canvas.

## Obsidian components

### Canvas

Best component for this proposal. It provides manual spatial layout, file/text/web cards, groups, directed labeled edges, and an open `.canvas` JSON format.

### Bases

Potentially very useful for a gap dashboard if material questions become Markdown notes with structured properties. Example views:

- high-importance unanswered questions
- partial answers by section
- actual-reader questions not yet resolved
- external questions marked for interlink
- questions intentionally omitted with disposition rationale

### Graph View

Not recommended as the primary editorial map. Obsidian Graph View fundamentally visualizes note-link relationships. Those links are too semantically weak for the typed relationships needed here. Use Graph View only as a supplementary corpus-level discovery view if it becomes useful later.

## Authority and anti-drift rules

1. `master.md`, registered state, owner locks, source/evidence records, and current Joel corrections continue to outrank every visualization.
2. Mermaid `ARCHITECTURE.md` remains the required compact structural control surface.
3. Reader-question records are diagnostic objects; they never silently authorize additions, deletions, qualification, or argument changes.
4. Canvas files should preferably be **generated or disposable views**, not manually maintained competing truth.
5. Every material unanswered question requires a disposition before editing: answer here, move/link elsewhere, make scope explicit, bank, leave implicit, or reject.
6. Do not turn the system into a completeness maximizer. The repository's overcompletion and true-stopping-point rules remain in force.
7. Reuse the existing argument/evidence ledger for evidence and premise dependencies. Do not create parallel claim bookkeeping in Obsidian.

## Minimal experiment before deeper investment

Do not build a plugin or large vault architecture first.

Run one bounded experiment on the current Romance article:

1. Treat the local `joel-articles` checkout as an Obsidian vault without changing article authority.
2. Generate one `romance-reader-gap.canvas` from the existing `ARCHITECTURE.md` plus a temporary reader-question register.
3. Run only the promise-first and blind-prefix passes.
4. Limit durable question nodes to material questions that could plausibly change section architecture, add an interlink, expose a real omission, or justify an explicit scope boundary.
5. Compare the findings against the existing Mermaid map, multiscale ledger, and independent-reader audit.
6. Keep the architecture only if it surfaces useful editorial defects that the current workflow reliably misses or makes existing findings materially easier for Joel to inspect.

If the experiment succeeds, add the optional Bases dashboard and automate Canvas generation. If it does not, retain the question-audit logic without adopting Obsidian.

## Current recommendation

**Adapt/composition, not replacement or greenfield invention.**

For `joel-articles`, Obsidian has a higher potential payoff than in AskRigor because article editing benefits from spatial exploration and explicit negative-space objects. The best use is an **editorial observatory** over the canonical Git workflow, while Mermaid stays the compact formal architecture map.

The most promising novel operational idea is the **blind-prefix reader-question graph**: preserve the reader's actual information state at each section boundary, record the questions that state produces, then compare those questions to later coverage and disposition. This externalizes the repository's existing curious-reader rule without allowing hindsight or automatic overcompletion to erase the gaps it is meant to detect.
