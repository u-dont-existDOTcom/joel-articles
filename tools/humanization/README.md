# Shared humanization tools

Every article's humanization uses these (`AGENTS.md`; `docs/HUMANIZATION-GATE.md`).

- `render_in_context.py`: the side-by-side page, for any article. It puts the source beside each paragraph and marks the changes, either against the version Joel last saw (`--since`) or against the source (`--against-source`). Send it with every turn that changes an article.
- `emulate_humanize.py`: the Emulate API tool (`docs/EMULATE-FALLBACK.md`, section 3). It runs on Joel's laptop, where the key is.

These tools still live in the Inner Child lane, until they move here: branch `handoff/claude-dangerous-adult-20260924-1631`, folder `articles/inner-child-therapy/tools/`.
- `tells_lint.py`;
- `reviewer/`;
- `calibration/`;
- `check_owner_edits.py`;
- `pangram_batch_gen.py`;
- `build_sweep_prompt.py`;
- `render_article_so_far.py`.
