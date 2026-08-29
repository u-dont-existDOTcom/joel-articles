# Obsidian Editorial Gap Map — rejected proposal

Status: **REJECTED after owner usability test, 2026-08-29.** Do not adopt Obsidian as an editorial dependency for `joel-articles`.

## Decision

The Romance pilot established that the **reader-question / blind-prefix audit itself is useful**, but the Obsidian Canvas representation is not.

Owner inspection of the reduced Canvas found it visually noisy, edge-heavy, difficult to parse, and materially worse than the compact comparison/report view. The spatial graph did not make the editorial decisions easier to understand.

Therefore:

- keep Mermaid `ARCHITECTURE.md` as the required compact structural map;
- retain the optional reader-question audit as a text/structured diagnostic;
- do **not** require Obsidian, Canvas, Bases, Graph View, or an Obsidian vault for article work;
- do **not** build an Obsidian plugin or additional Canvas-generation tooling;
- do **not** revive this proposal merely because a future article has many cross-links. Any replacement visualization must first prove that it is clearer than the compact textual/table representation.

The reusable surviving method is documented in `docs/READER-QUESTION-AUDIT.md`.

## What the pilot validated

The useful part was not spatial mapping. It was preserving a reader's actual information state:

1. freeze the questions reasonably implied by the opening promise;
2. reveal the article sequentially so future text is genuinely unavailable;
3. freeze only material live questions at each checkpoint;
4. after the full article is revealed, classify each question as answered, answered later, partial, thin, unanswered, intentionally out of scope, or rejected by the article;
5. distinguish an unanswered question from an article defect;
6. retain only the small unresolved set plus a few answered controls.

The Romance blind run showed useful discrimination: most live questions were later judged answered or not defects, while a small number survived as genuine review candidates. It also falsified several plausible-looking hidden hypotheses rather than simply accumulating omissions.

## Why Obsidian failed this use case

The reduced Canvas still produced too many crossing edges, labels, and competing node columns. The reader had to visually trace relationships that were easier to understand in a compact comparison table. The visualization added handling cost without adding decision clarity.

That result also supports an earlier repository principle: long articles should not become paragraph-level mega-graphs. Negative-space diagnosis is better represented as a bounded question ledger/report than as a dense general-purpose graph.

## Authority boundary

This decision changes no Romance prose, owner lock, article state, article architecture, source evidence, detector evidence, or publication status. The Obsidian pilot remains historical experimental evidence only.
