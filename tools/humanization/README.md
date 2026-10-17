# Shared humanization tools

Every article's humanization uses these (`AGENTS.md`; `docs/HUMANIZATION-GATE.md`). No tool here has an article's paths built in: each command takes the article's files as options. Run them from the repo root. The examples use the Inner Child article's files.

- `tells_lint.py`: the linter for the mechanical tells (the gate's step 5).
  `python3 tools/humanization/tells_lint.py DRAFT.txt [--source SOURCE-SECTION.txt] [--owner OWNER-LINES.txt] [--installed ARTICLE.md]`
  For a section check, `--installed` takes the article as installed, so only new text gets flags. An owner file's lines can be whole paragraphs (since 2026-10-03).
- `reviewer/`: builds the prompts for the reviewer-writer loop (`repeats --focus NAME --only` reports just what touches that part, 2026-10-14), the cold sense read (of a paragraph, or of a whole section with `sense-section`), first drafts and the grounding review (`reviewer/README.md`). The article and its source come from `--article` and `--source`, or from the `"article"` and `"source"` keys in the target.
  `python3 tools/humanization/reviewer/reviewer.py grounding DRAFT.txt articles/inner-child-therapy/tools/targets/love-doesnt-wait-p5.json OUT.txt`
- `check_owner_edits.py`: checks that every edit and claim in an article's `OWNER-EDITS.json` is in the article. `must_contain_exact` checks Joel's own lines character for character, apostrophes included (2026-10-02).
  `python3 tools/humanization/check_owner_edits.py --article articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md --ledger articles/inner-child-therapy/OWNER-EDITS.json`
- `render_article_so_far.py`: the whole article so far as one HTML page for Joel, with the owner-edits check when it's given `--ledger`. Send it at the end of every turn.
  `python3 tools/humanization/render_article_so_far.py OUT.html --article articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md --ledger articles/inner-child-therapy/OWNER-EDITS.json`
- `render_in_context.py`: the side-by-side page, for any article. It puts the source beside each paragraph and marks the changes, either against the version Joel last saw (`--since`) or against the source (`--against-source`). Each row is shown in its place: the section it goes in, the article paragraph before it and the one after it (2026-10-07). A draft that isn't in the article needs `"after"` or `"after_row"` in the map. Since 2026-10-08 a row can list `"repeats"`: what the article, or another row, already says. The page marks each in blue, says where, and stops if a quote isn't there (E151). Rows are labeled in plain words, and rows in the article show their source too (E152). Since 2026-10-08 (E154) a quote that's part of a source paragraph is shown inside the whole paragraph with the part marked, and a draft row can have a `"carries"` table: each draft sentence beside the guide words it carries, or "added by the writer", every quote checked. Send it with every turn that changes an article.
  `python3 tools/humanization/render_in_context.py MAP.json OUT.html --article ARTICLE.md --source SOURCE [--since REV | --against-source] [--source-label TEXT]`
- `stance_check_prompt.py`: the whole-article stance check (the gate's step 4): a prompt that has a fresh agent hold every stance-bearing sentence of a rewrite against the whole published article. Run it before any Pangram call on a candidate (Joel, 2026-10-02: "Did the reviewers not look at the article?").
  `python3 tools/humanization/stance_check_prompt.py --essay PUBLISHED.md --rewrite REWRITE.md --out prompt.txt [--scope TEXT] [--topic TEXT] [--report REPORT.md]`
- `build_sweep_prompt.py`: the fresh-context tell-sweep prompt, built from `docs/HUMANIZATION-TELL-INVENTORY.md`.
  `python3 tools/humanization/build_sweep_prompt.py TARGET.md [--previous PREVIOUS.md] [--next NEXT.md] > prompt.txt`
- `preservation_keys.py`: the words each preservation unit rests on, checked per paragraph before any trace; a key file whose unit leaves out the section's own term fails too (2026-10-12).
  `python3 tools/humanization/preservation_keys.py KEYS.json DRAFT.md`
- `meaning_sweep.py`: a fresh reader's sweep of rewritten sections against the published ones for the breaks Joel found in community section 12, with his own sentences marked so the reader leaves them alone (2026-10-12).
  `python3 tools/humanization/meaning_sweep.py --article ART.md --source PUB.md --section N --input IN.md --report REPORT.md --out PROMPT.txt --ledger OWNER-EDITS.json [--owner-text FILE]`
- `pause_tally.py`: the phrases two or more cold reads paused at and settled, counted across rounds, outside Joel's own sentences (2026-10-16: four readers in three rounds had paused at section 13's "How do you know?" and nothing counted it). With `--dispositions`, each one needs an answer there.
  `python3 tools/humanization/pause_tally.py REPORT.md ... --draft DRAFT.md --ledger OWNER-EDITS.json [--owner-text FILE] [--dispositions DISPOSITIONS.md]`
- `pangram_gate.py`: the Pangram web-app batch and its History reader, written only for texts whose gate record passes (march with a break, cold read, grounding, stance check, linter; E167, 2026-10-12). Use it for every web-app check.
  `python3 tools/humanization/pangram_gate.py DRAFTS.json GATE.json OUT.js --name NAME KEY [KEY ...]`
- `pangram_round.py`: one screen round for a new paragraph in one command (E181, Joel 2026-10-17 01:15: "idk why that had to take 38 mins tho"): each candidate alone, beside the paragraph before it and at the end of its section, with the drafts and gate files, a pending row per check in PREDICTIONS.md, and pangram_gate.py run on them.
  `python3 tools/humanization/pangram_round.py --article A --heading H --round NAME --out-prefix PREFIX --predictions P --date D --section-march M DRAFT.txt:MARCH ...`
  With `--spec SPEC.json`, paragraphs for several sections go in one batch, each linted against its own article (turn 65: one wait in the browser instead of three). After a section's only paragraph the pair isn't built, since it would be the section again.
- `pangram_score.py`: fills a batch's "(pending)" PREDICTIONS.md rows from what its OUT-read.js returned (the result, time, link, and hit or miss), so no result is typed by hand (turn 65).
  `python3 tools/humanization/pangram_score.py READ.json articles/X/tools/PREDICTIONS.md`
- `pangram_links_check.py`: fails a message or page that reports an AI result from Pangram without the check's link (E175, Joel 2026-10-15: "give me the pangram check links when you tell me to check something on pangram").
  `python3 tools/humanization/pangram_links_check.py MESSAGE.md [MORE.md ...]`
- `pangram_batch_gen.py`: the older action-list batch of up to three Pangram checks (no gate check; use `pangram_gate.py`), each text's SHA-256 checked before the click.
  `python3 tools/humanization/pangram_batch_gen.py drafts.json out.json KEY1 KEY2 KEY3`
- `emulate_humanize.py`: the Emulate API tool (`docs/EMULATE-FALLBACK.md`, section 3). It runs on Joel's laptop, where the key is.
  `python3 emulate_humanize.py balance`, or `python3 emulate_humanize.py humanize IN.txt OUT`
- `git-hooks/pre-push`: runs CI's content-integrity steps on each pushed commit and refuses the push if one fails (E158, 2026-10-09). Install it once per clone, from the repository root:
  `ln -sf ../../tools/humanization/git-hooks/pre-push .git/hooks/pre-push`

What they read:
- `calibration/`: texts with known Pangram results, the reviewer's labeled examples and the linter's test set.
- `JOEL-FIXES-CATALOGUE-20260928.md`: Joel's own before-and-after fixes; `reviewer.py draft` puts them in every first-draft prompt.
- `TELL-CALIBRATION-20260927.md` and `REVIEWER-VALIDATION-20260928.md`: how the tell list and the reviewer were tested.
- `tells_registry.json`: every tell the documents name, with its quotes; a mechanical one names its linter rule and an example, which `tests/test_tells_registry.py` runs (2026-10-11, from `TELLS-COVERAGE-20261011.md`). `EMOJI-LIST.md`: Joel's emoji bans and allowlist; the linter reads the allowlist from it (O26).

Each article keeps its own data: the humanized article, its source, `OWNER-EDITS.json`, the reviewer targets and the side-by-side maps. Inner Child's are in `articles/inner-child-therapy/`, with the targets in `tools/targets/`, the maps in `tools/in-context/` and the Pangram predictions in `tools/PREDICTIONS.md`.

The reviewer's examples come from the Inner Child article, and its prompt files still describe that article. Before using it on another kind of writing, see "How to read it" in `docs/HUMANIZATION-GATE.md`.
