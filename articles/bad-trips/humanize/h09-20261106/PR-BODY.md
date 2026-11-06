Bad trips guide, 2026-11-06 turn 15 (Joel's message of 17:30 UTC).

**The rule (gate E373).** Round 10's card asked Joel for his version of the room stretch, calling its sentences his. They were the guide's AI text he had humanized. His answer: "don't say 'those are your words so you need to fix it' -- your job is to do the fixing, that's the whole point here. and 'my words' for an AI article, are not my words, unless those were human before we started humanizing". Now, in every lane:
- `docs/HUMANIZATION-GATE.md`: E373, with notes at E282, E311, E370 and E372, which it corrects.
- `docs/FIXING-AN-ARTICLE.md` section 2, `AGENTS.md`'s marking-page rule and `SKILL.md`'s whose-words step say it.
- `tools/humanization/suggestion_review.py` (1.8): on pages built from 2026-11-06, a stretch to edit needs `"whose": "his own: ..."` or `"he asked: ..."`, and card, type or introduction text calling the text "your words", "your sentences", "yours to change" and the like is refused unless the card says it is his own.
- `tools/humanization/pangram_ledger.py predict`: `--his` takes only "his own: what and where"; `--unchanged` is for text checked as the article has it or as he sent it.
- `tools/humanization/sense_receipt.py make --his` needs `--whose "his own: ..."`; a receipt made from today with sentences marked his says so.
- Tests for all three. `OWNER-EDITS.json`'s room entries now check his decisions (no quips, the hand on the shoulder, sips, quiet, no "Lower the sound."), not the AI wording.

**Round 10 withdrawn.** Its page now says so; `review/r10/REVIEW-R10.md` too.

**The room stretch, fixed by me.** Eight versions (receipts, fresh newcomer reads of every draft, two tell panels, the linter clear from try 7), checked in his Pangram account: all AI, 100%. The whole Psychological First Aid section in place reads AI in one 453-word window, his dangers paragraph included. `articles/bad-trips/humanize/h09-20261106/RESULTS.md`. Next: the section as a whole.

Overlap: the gut lane's open pull request 308 adds a paragraph just above the `AGENTS.md` paragraph this changes, and sections elsewhere in `SKILL.md` and the gate; merging it after this one will need that one spot taken by hand (keep both).

Checks: `python3 -m unittest discover -s tests` (588, OK), `python3 scripts/audit_codex_github.py --root . --fail-on error` (0 errors).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01QAY8FUZDTAj8NLkkWxD5ih
