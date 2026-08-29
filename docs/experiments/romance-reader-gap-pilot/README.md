# Romance reader-gap / Obsidian pilot

Status: **EXPERIMENT / DIAGNOSTIC ONLY.** Nothing in this directory is article authority or edit authorization.

The pilot intentionally lives under `docs/experiments/`, not inside `articles/romance/`, because the registered article-family inventory is fail-closed: every file inside a registered article family must itself be registered. A disposable diagnostic Canvas should not acquire article-authority status merely because it visualizes an article.

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

## Blind-test architecture

The fresh-reader test is deliberately split into two stages so mechanical retrieval cannot contaminate editorial reasoning.

### Stage 1 — collector

The collector may access GitHub but performs **no editorial analysis**.

`scripts/compile_blind_reader_packet.py` verifies the exact canonical source SHA-256, splits the bytes into contiguous 90-line windows, hashes every window, and writes a deterministic manifest. Concatenating the windows must reproduce the exact canonical source SHA-256.

Use `COLLECTION-PROTOCOL.md` for this stage.

Generated windows are ephemeral and are **not committed to the repository**.

### Stage 2 — Pro reader

The Pro reader must have no GitHub/web access and no access to the complete packet. A human/controller reveals exactly one frozen window at a time. The reader freezes its checkpoint before receiving the next window.

This is stronger than placing the full article in context and merely instructing a model not to look ahead: unrevealed content is actually unavailable.

Use `FRESH-READER-BLIND-PROTOCOL.md` for this stage.

## Hosted validation of the collector

The PR-hosted regression run on 2026-08-29 passed **117/117 tests**. The new canonical integration test reads the checked-out `articles/romance/master.md`, verifies its exact SHA-256 against `f1c2b9a3f0f3d9e123c3870ca5d741af8ed99bbf6f138e68b845de04b1a12a2c`, compiles 90-line windows, and verifies that their exact byte reconstruction has the same SHA-256.

The workflow then stops at the repository's existing authority validator because of four pre-existing base-repository findings in unchanged article/governance files. Those are separate from this pilot and are not suppressed or repaired here.

## Pilot passes

### A. Promise-first

Read only the opening promise/scope first. Generate the material questions a reasonable intended reader would expect the guide to resolve. Only then compare those questions with the full article.

This catches omissions the body never raises and therefore cannot remind an ordinary whole-article audit to look for.

### B. Blind-prefix

At selected consequential boundaries, preserve the reader's actual information state by looking only backward. Record the strongest live question at that point, then check whether later prose answers, redirects, or leaves it unresolved.

A whole-article model has hindsight and can underreport temporary confusion because it already knows what comes later.

### C. Coverage controls

The register deliberately contains questions that the article **does answer**. If the method classifies those as gaps, the pilot is over-generating and should be repaired or abandoned.

### D. External benchmark

After the article-internal pass is frozen, compare surviving questions against mature relationship-assessment/education domains, relevant research, and a small sample of actual-reader questions. External prevalence is evidence of reader demand, not a completeness mandate.

## Initial read result

The full frozen article was read before classification. The first repair hypothesis was rejected: the article does contain meaningful repair material later through outside help, individual practices, honesty, scheduled non-combative discussion, counseling, and temporary separation.

The initial higher-value candidates were longitudinal relationship health, trigger-versus-incompatibility, love-versus-idealization/attachment, and maintaining romance after children arrive.

The external benchmark then materially changed the ranking. Ordinary-conflict repair and concrete money/labor/household alignment received substantially stronger independent support than the first pass gave them.

Current strongest review candidates are:

1. **G006 — partnership after children:** how the romantic relationship survives the transition from couple to parents, not only how children are protected if the couple separates.
2. **G003 — repair:** what successful repair after an ordinary fight actually consists of.
3. **G007 — practical merging:** money, labor, household responsibility, dependency, and related expectations before lives merge.
4. **G001/G002 cluster — health/workability:** how to tell whether the relationship is getting healthier and whether recurring pain is workable rather than merely intense, entangled, incompatible, or unsafe.
5. **G005 — love vs idealization/attachment:** a major distributed question whose answer may already be the article's whole architecture rather than a missing checklist.

These remain **questions for editorial review, not findings that prose must be added**.

## Controls already passing conceptually

- **C001:** “What if I do not already have a commune/community?” — directly answered in Two Pillars.
- **C002:** “What if I am already entangled?” — anticipated and answered by the next major section, `If you’re already in it`.
- **C003:** later sexual incompatibility/libido divergence — discussed early and revisited through fit/discernment.
- **C004:** avoiding partner-as-whole-world — receives a dedicated treatment plus community follow-through.

The blind-prefix sequence also correctly predicts several next-section moves, including Starting → Crucible, Twin Flames → Two Pillars, and Doing It Consciously → If You’re Already In It. That is useful evidence that the method can recognize existing architecture instead of only manufacturing omissions.

## Files

- `reader-gap-register.json` — diagnostic source register for questions, controls, and prefix probes.
- `romance-reader-gap.canvas` — generated Obsidian JSON Canvas view.
- `EXTERNAL-BENCHMARK.md` — established-work and actual-reader pressure test.
- `COLLECTION-PROTOCOL.md` — mechanical GitHub/source collection stage.
- `FRESH-READER-BLIND-PROTOCOL.md` — isolated Pro reader stage; no GitHub or unrevealed windows.
- `HANDOFF-PROMPTS.md` — copy/paste collector, Pro startup, window, and closeout instructions.
- `scripts/compile_blind_reader_packet.py` — deterministic source → hashed sequential-window compiler.
- `tests/test_compile_blind_reader_packet.py` — compiler regressions plus canonical Romance identity/coverage test.
- `scripts/generate_editorial_gap_canvas.py` — generic diagnostic Canvas generator.
- `tests/test_generate_editorial_gap_canvas.py` — fail-closed Canvas generator tests.

## Generate / validate Canvas

From repository root:

```bash
python scripts/generate_editorial_gap_canvas.py \
  docs/experiments/romance-reader-gap-pilot/reader-gap-register.json \
  --out docs/experiments/romance-reader-gap-pilot/romance-reader-gap.canvas

python scripts/generate_editorial_gap_canvas.py \
  docs/experiments/romance-reader-gap-pilot/reader-gap-register.json \
  --check-only
```

Then open the repository root as an Obsidian vault and open `docs/experiments/romance-reader-gap-pilot/romance-reader-gap.canvas`. No Obsidian community plugin is required for the Canvas itself.

## Compile blind reader packet

From repository root:

```bash
python scripts/compile_blind_reader_packet.py \
  articles/romance/master.md \
  --expected-sha256 f1c2b9a3f0f3d9e123c3870ca5d741af8ed99bbf6f138e68b845de04b1a12a2c \
  --lines-per-window 90 \
  --out-dir /tmp/romance-blind-reader-packet
```

Keep the resulting directory/ZIP outside the Pro conversation. Reveal its `window-*.md` files one at a time.

## Success criteria

Keep/invest further only if the pilot does at least one of the following better than the existing workflow:

- reveals two or more material high-confidence gaps that survive owner/editor review;
- makes a distributed partial answer visibly obvious enough to change an editorial decision;
- catches an ordering problem that a whole-article/hindsight audit missed;
- routes a real question to an interlink instead of causing duplicated prose;
- makes it materially easier for Joel to inspect the article's negative space.

Fail or simplify the architecture if it mostly produces generic “what about X?” questions, duplicates the multiscale ledger, encourages overcompletion, or creates more maintenance than editorial information.

## Next experiment

Do **not** build Bases or a plugin yet.

1. Run the collector stage and freeze the exact packet/receipt.
2. Run the Pro reader stage in a genuinely fresh reader context, revealing one window at a time.
3. Freeze the Pro output before exposing the register, Canvas, benchmark, PR body, or prior Romance discussion.
4. Compare independent surviving questions only after both passes are closed.

The important measurement is not agreement between models. It is whether independently generated high-value questions survive full-text coverage checking and improve editorial judgment.
