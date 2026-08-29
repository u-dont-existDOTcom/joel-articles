# Romance reader-gap / Obsidian pilot

Status: **EXPERIMENT / DIAGNOSTIC ONLY.** Nothing in this directory is article authority or edit authorization.

Frozen article under test:

- article: `romance`
- canonical master: `articles/romance/master.md`
- SHA-256: `f1c2b9a3f0f3d9e123c3870ca5d741af8ed99bbf6f138e68b845de04b1a12a2c`
- required structural map remains: `articles/romance/ARCHITECTURE.md`

## Question being tested

Does a promise-first + blind-prefix reader-question layer reveal material editorial negative space that the existing Mermaid architecture map, multiscale editorial ledger, and whole-article cold/independent-reader audits do not make easy to see?

The experiment is not trying to maximize completeness. A reader question can be valid and still deserve `out-of-scope`, `leave-implicit`, `interlink`, or `reject` rather than new prose.

## Existing-work composition

This pilot does not introduce a new article theory. It composes:

- the existing Mermaid section/function map;
- the existing multiscale reader-state/question and paragraph-job ledger;
- the existing argument/evidence ledger for factual premises and countermodels;
- lightweight RST-style relation labels when useful;
- IBIS-style question/answer/argument objects;
- Obsidian JSON Canvas only as a spatial diagnostic view.

## Pilot passes

### A. Promise-first

Read only the opening promise/scope first. Generate the material questions a reasonable intended reader would expect the guide to resolve. Only then compare those questions with the full article.

This catches omissions the body never raises and therefore cannot remind an ordinary whole-article audit to look for.

### B. Blind-prefix

At selected consequential boundaries, preserve the reader's actual information state by looking only backward. Record the strongest live question at that point, then check whether later prose answers, redirects, or leaves it unresolved.

A whole-article model has hindsight and can underreport temporary confusion because it already knows what comes later.

### C. Coverage controls

The register deliberately contains questions that the article **does answer**. If the method classifies those as gaps, the pilot is over-generating and should be repaired or abandoned.

## Initial read result

The full frozen article was read before classification. The first repair hypothesis was rejected: the article does contain meaningful repair material later through outside help, individual practices, honesty, scheduled non-combative discussion, counseling, and temporary separation.

The higher-value remaining candidates are:

1. **G001 — longitudinal health:** how a reader knows a relationship is becoming healthier rather than merely more intense or entangled.
2. **G002 — trigger vs incompatibility:** the middle boundary between a workable growth edge, fundamental incompatibility, and danger.
3. **G005 — love vs idealization/attachment:** the article contains many pieces of this distinction but no compact reader-facing discriminant.
4. **G006 — romance after children arrive:** children organize the article from the opening onward, but the dedicated Children section mostly addresses obligations and breakup/co-parenting rather than maintaining the couple while parenting.

Secondary candidates are ordinary-conflict repair (G003), tolerable mismatch (G004), shared money/labor/logistics (G007), and boundary-vs-control distinctions (G008).

These are **questions for editorial review, not findings that prose must be added**.

## Controls already passing conceptually

- **C001:** “What if I do not already have a commune/community?” — directly answered in Two Pillars.
- **C002:** “What if I am already entangled?” — anticipated and answered by the next major section, `If you’re already in it`.
- **C003:** later sexual incompatibility/libido divergence — discussed early and revisited through fit/discernment.
- **C004:** avoiding partner-as-whole-world — receives a dedicated treatment plus community follow-through.

The blind-prefix sequence also correctly predicts several next-section moves, including Starting → Crucible, Twin Flames → Two Pillars, and Doing It Consciously → If You’re Already In It. That is useful evidence that the method can recognize existing architecture instead of only manufacturing omissions.

## Files

- `reader-gap-register.json` — diagnostic source register for questions, controls, and prefix probes.
- `romance-reader-gap.canvas` — generated Obsidian JSON Canvas view.
- `../../../..//scripts/generate_editorial_gap_canvas.py` — generic deterministic generator.
- `../../../..//tests/test_generate_editorial_gap_canvas.py` — minimal fail-closed regression tests.

## Generate / validate

From repository root:

```bash
python scripts/generate_editorial_gap_canvas.py \
  articles/romance/experiments/reader-gap-pilot/reader-gap-register.json \
  --out articles/romance/experiments/reader-gap-pilot/romance-reader-gap.canvas

python scripts/generate_editorial_gap_canvas.py \
  articles/romance/experiments/reader-gap-pilot/reader-gap-register.json \
  --check-only
```

Then open the repository root as an Obsidian vault and open `romance-reader-gap.canvas`. No Obsidian community plugin is required for the Canvas itself.

## Success criteria

Keep/invest further only if the pilot does at least one of the following better than the existing workflow:

- reveals two or more material high-confidence gaps that survive owner/editor review;
- makes a distributed partial answer visibly obvious enough to change an editorial decision;
- catches an ordering problem that a whole-article/hindsight audit missed;
- routes a real question to an interlink instead of causing duplicated prose;
- makes it materially easier for Joel to inspect the article's negative space.

Fail or simplify the architecture if it mostly produces generic “what about X?” questions, duplicates the multiscale ledger, encourages overcompletion, or creates more maintenance than editorial information.

## Next experiment if this survives review

Do **not** build Bases or a plugin yet. First run the same blind-prefix protocol through a genuinely fresh reader context/model and compare its question set with this first pass. The important measurement is not agreement between models; it is whether independently generated high-value questions survive full-text coverage checking and improve editorial judgment.
