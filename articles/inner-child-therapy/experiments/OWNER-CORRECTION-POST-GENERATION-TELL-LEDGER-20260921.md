# Owner correction — post-generation tell ledger is mandatory

Date: 2026-09-21
Status: **DIRECT OWNER CORRECTION / ACTIVE HUMANIZATION REVIEW RULE**

## Owner correction

Joel corrected the relational-thought architecture:

> you also need to give the tell ledger i didn't see that nor did i see your fixes for the tells

## Causal failure

The Human-facing tell library had previously failed when exposed to the writer as a simultaneous composition recipe.

The subsequent architecture correctly demoted tells to post-generation diagnostics, but the execution overcorrected: after switching to relational-thought generation, Chat ran independent-reader review and preservation/Pangram work without producing the explicit post-generation tell ledger and executing its repairs.

That skipped a required intermediate layer.

## Correct phase separation

### Generation phase

Do not give the writer:
- HT01–HT14 as a checklist;
- a sentence-job map;
- AI-tell scores;
- a preservation ledger as prose order.

Generate from:
- full context;
- live thought;
- owner examples/calibration;
- interacting scene/self-talk/parenthetical realization when source-earned.

### Diagnostic tell phase — after literal prose exists

Now inspect the literal candidate using the Human-facing tell catalog and AI-shaped operation evidence.

For every material span record:
- exact current text;
- current AI-shaped operation or risk;
- source-earned Human-facing tell(s) already working;
- missing/misapplied tell relation;
- disposition: KEEP / DELETE / REWRITE / MERGE / SUBORDINATE / MOVE;
- exact positive repair instruction;
- what protected meaning must remain;
- invalid simulations to reject.

### Chat executes the ledger

The tell ledger is not merely reported.

Chat performs the repairs itself, then reruns:
1. literal comprehension;
2. continuity;
3. preservation;
4. architecture/humanization;
5. second cold read;
6. Pangram when eligible.

If a tell repair changes prose, downstream prior passes are invalidated.

## Owner-facing visibility

When Joel explicitly asks for the tell ledger or the tell fixes:
- show the ledger;
- show the exact resulting fixed prose;
- distinguish owner-authored text from Chat's connective/repair text;
- do not hide tell repairs behind a generic statement that the paragraph was reviewed.

## Relationship to relational-thought generation

This rule does not restore tell-driven generation.

Correct order:

`relational-thought generation -> literal candidate -> post-generation tell ledger -> tell repairs -> review -> preservation -> Pangram`.

The tell catalog remains diagnostic/retrieval evidence, not a writer checklist.
