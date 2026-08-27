# Multiscale Editorial Ledger and Literal Proofread Gate

Status: required for substantial structural editing, article-wide reconstruction, and substantial humanization of a Joel-byline article. Trivial P1/local wording edits do not trigger it.

## Why this exists

A section map can be correct while the assembled prose still contains duplicated functions, misplaced paragraphs, empty headings, dangling transitions, or an unfinished setup. Preservation can also pass while an idea survives in the wrong place. Long-form editing therefore needs controls at more than one scale.

This gate composes existing repository controls rather than replacing them: the article Mermaid architecture map, source–meaning–context–destination ledger, purposeful-recurrence ledger, dependency audit, orphan audit, curious-reader chain, preservation proof, and cold audit all remain authoritative for their own jobs.

## 1. Global/article ledger

Before substantial restructuring, record the article's governing movement and the job of every consequential section. For each recurring idea, identify its **primary home** and classify every other appearance as one of:

- `setup` — introduces a need/question that the primary section later develops;
- `primary exposition` — the one place where the mechanism/argument is developed in full;
- `application` — applies the established idea to a different concrete problem;
- `payoff/callback` — briefly recalls the established idea because the later conclusion depends on it;
- `true duplicate` — performs substantially the same explanatory/rhetorical job again.

Do not deduplicate by keyword count. The same concept may legitimately recur. A true duplicate must be consolidated, removed with authority, or explicitly justified.

## 2. Section/subsection ledger

For every edited natural section, record:

- heading promise;
- reader state/question on entry;
- section exit state/question;
- each subsection's distinct job;
- dependencies on earlier/later sections;
- why the current subsection order is necessary;
- any function moved in or out and its destination.

A good paragraph or anecdote does not earn its location merely by being good. It must perform a distinct job under that heading at that point in the article.

## 3. Paragraph ledger

For every paragraph in the changed natural boundary, record one dominant job or live-question movement. Flag a paragraph when it:

- repeats the same job as an earlier paragraph;
- only recaps an inference already available to the reader;
- answers a question already closed;
- supplies evidence for a claim that moved elsewhere;
- depends on a missing antecedent or undefined referent;
- begins a list/setup it never completes;
- ends with an unfulfilled colon, dash, promise, or transition;
- exists primarily to glue over a structural misplacement;
- makes the next paragraph feel like a non sequitur.

If a paragraph has several important jobs, split the ledger row conceptually before deciding whether the prose itself should be split. Do not mechanically force one-sentence/one-function prose.

## 4. Literal post-assembly proofread

After all movement/consolidation and before calling the work editorially clean, read the **complete assembled natural boundary from top to bottom** without consulting detector windows or drafting rationale. This is not a summary check and cannot be certified from the Mermaid map alone.

Check at minimum:

- empty or duplicate headings;
- heading-level/parent-child continuity;
- unfinished bullets, lists, colons, quotations, examples, and promises;
- dangling `this/that/also/still/but/otherwise` relations after moves;
- missing definitions and antecedents;
- orphaned examples, links, media, callbacks, or conclusions;
- paragraph-to-paragraph non sequiturs;
- repeated function even when wording differs;
- setup without payoff and payoff without setup;
- whether the article reaches its intended stopping point once, rather than ending repeatedly.

A mechanical validator may assist but does not replace this read.

## 5. Humanization-specific enforcement

For substantial humanization/detector work, `HUMANIZATION-ARCHITECTURE-GATE.md` makes this gate blocking before detector eligibility and after detector-driven semantic edits. Detector-green prose that fails this ledger/proofread remains editorially invalid.

## Provenance

Promoted 2026-08-27 after Joel's manual Romance cleanup exposed a failure mode in which section-level preservation/architecture controls had passed while global organization still needed substantial owner repair and the assembled article retained two empty headings plus an unfinished Helen Fisher setup. The lesson is not to make a larger Mermaid graph; the existing map is intentionally structural. The durable repair is to couple it to explicit global, section, and paragraph ledgers plus a literal assembled-text proofread.
