Bad trips guide, turn 13 (Joel's round-8 answer, exported 2026-11-06 00:27 UTC).

- **His version in.** The room stretch's second part (B240, B241) as he wrote it, the text of his own check that read Human (`review/r08/apply_r08.py`). His first two paragraphs stay until he answers round 9.
- **His checks recorded.** Five checks from his history, with their texts matched by SHA-256 (`humanize/h08-20261106/HIS-CHECKS-READ-20261106.json`). They show three fixes, each turning a part to Human: the quips cut, the payoff first ("They're feeling overwhelmed, so ..."), and an exact act ("Ask if they'd like a hand on the shoulder" for "Ask before touching").
- **Lessons for every lane** (`docs/HUMANIZATION-GATE.md`, after the gut lane's E368 and E369):
  - E370: where he has asked for a guide's AI quips to go, his own lines that readers take for quips go too.
  - E371: the reason first, in plain words, and each instruction's exact act.
  - E372: a card asking for his version gives each paragraph its own reading and says every one is his to change.
- **His exercise, the first part.** My fix reads Human, 0% alone (07e19481). In place before his second part, the stretch reads AI, High, and so does his own stretch, so the stretch itself is the next work (`humanize/h08-20261106/RESULTS.md`). Round 9's page has the one card (Bad Trips Guide, Round 9, https://claude.ai/artifact/KrdxXmj483tg4kEhAk8waB; `review/r09/REVIEW-R09.md`).
- **Tool.** `suggestion_review_browser_test.py` now runs its checks on a page with a single card to approve and nothing else; it had stopped on such a page. Round 9 passes 56 of 56 and round 8 still passes 62 of 62.
- **Fidelity.** The fidelity keys record his cut of the "explain the universe" line as his (`humanize/h01/FIDELITY-KEYS-R08.json`); the check passes.

Overlaps:
- #308 (the gut lane's how-to-write-for-Pangram notes) also adds to `docs/HUMANIZATION-GATE.md`, under E368 and E369. This branch adds a separate section after theirs and changes only their closing number line, so the two merge side by side.
- `articles/INDEX.json` is registration: each branch adds its own files.

Checks: `python -m unittest discover -s tests` (584 tests, OK), the repository audit (0 errors), and the content validator through `lane_push.py`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01QAY8FUZDTAj8NLkkWxD5ih
