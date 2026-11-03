# Healing the Gut: import receipt (2026-11-03)

- His post: "Healing the Gut Naturally", subtitle "A compilation of what I've learned so far", https://ibogaqueen.substack.com/p/healing-the-gut-naturally (post 176569317, paid subscribers only, 3,402 words by Substack's count), found through Substack's public archive search from his laptop on 2026-11-03.
- The master is the editor HTML Joel pasted into the chat on 2026-11-03 16:15 UTC (`source/substack-editor-20261103.html` = `master.html`, SHA-256 dad7b0cd540452cb44198782a69db94ace6b0f2b5ec58bb98bf8c233703cf2ea). His messages are in `experiments/t01-answers/joel-20261103-1615-messages.txt`.
- `humanize/MASTER-VISIBLE.md` is the reader-visible text of the master (headings, paragraphs, list items; links kept as their visible words), made with BeautifulSoup. The editor's video placeholders ("Double click to interact with video") are still in it; they are not reader text and are dropped before any Pangram check.
- `humanize/FIDELITY-KEYS.json`: `python3 tools/humanization/fidelity_keys.py extract humanize/MASTER-VISIBLE.md humanize/FIDELITY-KEYS.json` (53 numbers, 25 distinct; 62 terms; 24 warning sentences).
- Joel's own detector check before import: his Pangram extension share (https://www.pangram.com/feed/c710e38e-a6c1-4c81-bb71-5635745b4b21) states 59% of the post is AI-generated.
