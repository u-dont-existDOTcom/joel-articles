# Shared humanization tools

Every article's humanization uses these (`AGENTS.md`; `docs/HUMANIZATION-GATE.md`). No tool here has an article's paths built in: each command takes the article's files as options. Run them from the repo root. The examples use the Inner Child article's files.

- `tells_lint.py`: the linter for the mechanical tells (the gate's step 5).
  `python3 tools/humanization/tells_lint.py DRAFT.txt [--source SOURCE-SECTION.txt] [--owner OWNER-LINES.txt] [--installed ARTICLE.md]`
  For a section check, `--installed` takes the article as installed, so only new text gets flags. An owner file's lines can be whole paragraphs (since 2026-10-03).
- `reviewer/`: builds the prompts for the reviewer-writer loop, the cold sense read, first drafts and the grounding review (`reviewer/README.md`). The article and its source come from `--article` and `--source`, or from the `"article"` and `"source"` keys in the target.
  `python3 tools/humanization/reviewer/reviewer.py grounding DRAFT.txt articles/inner-child-therapy/tools/targets/love-doesnt-wait-p5.json OUT.txt`
- `check_owner_edits.py`: checks that every edit and claim in an article's `OWNER-EDITS.json` is in the article. `must_contain_exact` checks Joel's own lines character for character, apostrophes included (2026-10-02).
  `python3 tools/humanization/check_owner_edits.py --article articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md --ledger articles/inner-child-therapy/OWNER-EDITS.json`
- `render_article_so_far.py`: the whole article so far as one HTML page for Joel, with the owner-edits check when it's given `--ledger`. Send it at the end of every turn.
  `python3 tools/humanization/render_article_so_far.py OUT.html --article articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md --ledger articles/inner-child-therapy/OWNER-EDITS.json`
- `render_in_context.py`: the side-by-side page, for any article. It puts the source beside each paragraph and marks the changes, either against the version Joel last saw (`--since`) or against the source (`--against-source`). Each row is shown in its place: the section it goes in, the article paragraph before it and the one after it (2026-10-07). A draft that isn't in the article needs `"after"` or `"after_row"` in the map. Send it with every turn that changes an article.
  `python3 tools/humanization/render_in_context.py MAP.json OUT.html --article ARTICLE.md --source SOURCE [--since REV | --against-source] [--source-label TEXT]`
- `stance_check_prompt.py`: the whole-article stance check (the gate's step 4): a prompt that has a fresh agent hold every stance-bearing sentence of a rewrite against the whole published article. Run it before any Pangram call on a candidate (Joel, 2026-10-02: "Did the reviewers not look at the article?").
  `python3 tools/humanization/stance_check_prompt.py --essay PUBLISHED.md --rewrite REWRITE.md --out prompt.txt [--scope TEXT] [--topic TEXT] [--report REPORT.md]`
- `build_sweep_prompt.py`: the fresh-context tell-sweep prompt, built from `docs/HUMANIZATION-TELL-INVENTORY.md`.
  `python3 tools/humanization/build_sweep_prompt.py TARGET.md [--previous PREVIOUS.md] [--next NEXT.md] > prompt.txt`
- `pangram_batch_gen.py`: a browser batch of up to three Pangram checks, each text's SHA-256 checked before the click.
  `python3 tools/humanization/pangram_batch_gen.py drafts.json out.json KEY1 KEY2 KEY3`
- `emulate_humanize.py`: the Emulate API tool (`docs/EMULATE-FALLBACK.md`, section 3). It runs on Joel's laptop, where the key is.
  `python3 emulate_humanize.py balance`, or `python3 emulate_humanize.py humanize IN.txt OUT`

What they read:
- `calibration/`: texts with known Pangram results, the reviewer's labeled examples and the linter's test set.
- `JOEL-FIXES-CATALOGUE-20260928.md`: Joel's own before-and-after fixes; `reviewer.py draft` puts them in every first-draft prompt.
- `TELL-CALIBRATION-20260927.md` and `REVIEWER-VALIDATION-20260928.md`: how the tell list and the reviewer were tested.

Each article keeps its own data: the humanized article, its source, `OWNER-EDITS.json`, the reviewer targets and the side-by-side maps. Inner Child's are in `articles/inner-child-therapy/`, with the targets in `tools/targets/`, the maps in `tools/in-context/` and the Pangram predictions in `tools/PREDICTIONS.md`.

The reviewer's examples come from the Inner Child article, and its prompt files still describe that article. Before using it on another kind of writing, see "How to read it" in `docs/HUMANIZATION-GATE.md`.
