# Intentional Communities: current state

Registered 2026-10-13 from the community humanization lane (branch `claude/emulate-lessons-20260930`, commit `6775ed15`), at Joel's answer to question 20: "yes register the article but i don't want to separate it from the rules co-developed in inner child lane... so don't register if it would cause that to fork..."

## Now (2026-10-25)

The working copy is `candidate/joel-20261024/answer65/WORKING.html`: his editor HTML of 2026-10-20 with his answers 57 to 65 and his kibbutz image, as an essay and then a How-To Manual. It read Human Written as one text (0 of 72 windows AI, https://www.pangram.com/feed/954042b6-e624-4c7f-87d7-db15c547d5c8), and `master.md` is that version (PROMOTION-RECEIPT-20261017.md). His post gets it through `exports/COPY-TO-SUBSTACK.html` (receipt `exports/HELPER-RECEIPT-20261025.json`). The sections below are the history of how the article got here.

## Goal

Humanize Joel's published intentional-communities Substack article section by section, so that every paragraph and every section reads Human in Pangram's web app and the meaning stays the published one, except where Joel changes it himself.

## Authority / baseline

- Registered working source master: `original.md`, the published Substack text (97,920 UTF-8 bytes, SHA-256 `5d2892335ba53e93147caf5588a11e660d3ff2180d1ab1b23ff9fc5b2eb99aa6`). Like Inner Child Therapy's raw Substack master, it is the baseline, not the humanized article.
- The humanized article: `candidate/HUMANIZED-SO-FAR.md`, the working candidate (role `active_humanized_article`). Nothing in it is accepted until Joel says so.
- Joel's edits and rulings: `candidate/OWNER-EDITS.json`, checked by `tools/humanization/check_owner_edits.py` on every render.
- Rules: the repository's shared rules only (`AGENTS.md`, `SKILL.md`, `docs/HUMANIZATION-GATE.md`, `tools/humanization/`), the same ones the Inner Child lane runs and adds to. This folder holds the article's rulings and records, not a copy of the rules.

## Completed

- Sections 1 to 12 are humanized candidates in `candidate/HUMANIZED-SO-FAR.md`. Sections 4 and 12 are Joel's own texts of 2026-10-13 (with his answers of 2026-10-14); section 5 is his of 2026-10-06; the others carry his edits and answers where he gave them. Every candidate section read 100% Human in Pangram's web app when it was installed (`DETECTOR-EVIDENCE.json`; for the changes of 2026-10-14, `candidate/fix-20261014/RESULTS.md`).
- 2026-10-14: Joel's Rule Scoring Sheet answers and 13 fixes from the sweep of 2026-10-13 are in (sections 2, 3, 4, 6, 7, 8, 9, 11, 12), each changed paragraph Human alone and each section 100% Human in Pangram's web app. His answers of 21:19 UTC (questions 22 to 26) are in too: his own section 11 text and section 10 paragraph, and small cuts in sections 4, 9 and 11; sections 4, 9, 10 and 11 read 100% Human.
- 2026-10-15: his answers 27 to 29 (section 10 v4; section 4's diagram rebuilt, waiting for his Substack upload) and, at 11:04, his two section 4 paragraphs (section 4 v11.3, 100% Human in batch 287g). Section 13 started: baseline all AI (batch 286g), drafts v1 to v6 through four gate rounds; 2 of 10 checked v5 paragraphs read Human (287g); not in the article yet. After his 13:10 answers (30 b: the visitor and founder lines stay as published; 31 a: paragraph by paragraph), Emulate rounds b to f, drafts v7 to v13 and gate rounds r5 to r9: 20 of its 27 paragraphs read Human alone or beside a neighbor that does (batches 289g to 292g, 23 of 28 checks Human).
- 2026-10-15, after his 18:28 answer (32 b: his research sentence stays as published): section 13 drafts v14 to v22, Emulate rounds g to i, gate rounds r10 to r15. Every part of v21 read Human on its own text and the whole section read 56% AI (298g); v22 rebuilds the two stretches that read AI everywhere (the land subsection; H4-P9 to H5-P2) from Emulate, and its review round r15 is done, its fixes next. Not in the article yet.
- 2026-10-16, after his 18:22 message (33 a; his cut of "How do you know?"; "continue into next section now"): section 14 ("Dissolution and Exit") is a humanized candidate in `candidate/HUMANIZED-SO-FAR.md` (v5; every group Human and the whole section 100% Human, high, batch 306g). Section 13 had one more bounded pass (drafts v23 to v26, rounds r16 to r18, batch 304g): every changed group Human, the land subsection Human; the whole section reads 38% AI (56% before), in two long stretches. Not in the article yet.
- 2026-10-16, after his 21:05 message (34 a, "learn from how emulate fixes it"; links he can click; the diagram is uploaded): Emulate round j on section 13's two stretches that read AI, each sent whole, and drafts v27 to v31 with the meaning put back inside Emulate's sentences. Section 13 is a humanized candidate in `candidate/HUMANIZED-SO-FAR.md` (v31): the whole section 100% Human, high (batch 311g; it read 38% AI in 304g), its meaning reviews done (rounds r19 and r20).
- 2026-10-17, after his 2026-10-16 23:38 message (the questions page's layout bug and hidden questions; his "if the community uses them" back; "it's all fairly borderline human. so we should fix it"; the book not leaning on Christian's order; the dedup): section 13 is in the article as v34 (every paragraph Human alone, batches 312g to 318g, `tools/humanization/paragraphs_alone.py` PASS; the whole section 100% Human, high, 0.06, batch 317g; the values stretch that read AI inside the section in 316g reads Human without the monologue too) and section 14 as v8 (every paragraph Human alone; the whole section 100% Human, 316g), each deduplicated. The questions page lists questions 35 to 38.
- 2026-10-17, after his 02:07 message (35 b, 36 a, 37 a, 38 b his own section 14 paragraph; "accept 13 and 14"; his standing dedup rule: cut only when no important meaning is lost or there's no good way to merge): sections 13 (v34) and 14 (v9) are accepted (`EDITORIAL-STATUS.json`); section 10 is v5 (his 36 a, Human alone and as a section, batch 320g).
- 2026-10-17, after his 13:11 message (39 his sentence in section 4; 40 a; 41 a, and rules that depend on the article's style; 42 his lines for section 16's last stretch; his corrections in sections 15 and 16; the PsyPost study): section 16 is in the article as v28 (every changed paragraph Human, the whole section 100% Human, 413g), so every section is in; section 15 v13, section 12 v14 (the study), section 8 v30 and section 1 (the sweep of his "this"/"quietly" rules) 100% Human (412g); section 4 v11.4 (414g, 100% Human). New checks for each correction (`docs/HUMANIZATION-GATE.md`); questions 43 to 45 open.
- 2026-10-17, after his 17:16 message (43 his way with exclamations; 44c the screenshot as material, and the anomie point; 45 the whole-article faithfulness pass): section 12 v15 (his P2 as written, his screenshot with his caption; 415g 100% Human), section 9 v17 (the published limit back; 415g), section 15 v14 (five exclamations his way, two published phrases back; 417g) and section 16 v29 (five exclamation changes, the published "declaring"; 419g), each 100% Human. Five fresh readers compared the whole rewrite with the published article (`candidate/fix-20261017b/faithful/`, `TRIAGE.md`): the argument holds; fixes where Pangram agreed; questions 46 to 51 for the rest. Section 2 is unchanged (its paragraph is question 47).
- 2026-10-17, after his 19:14 answer ("i agree with your excl 13 14 ideas"): section 13 v35, still accepted (`candidate/fix-20261017c/`): 15 marks to periods, "There's lots you can do!" out, one mark the list missed the same way; two cuts held back after the march reads (each its paragraph's only break) and back to him in question 48. Every changed paragraph Human, the section 100% Human (420g).
- 2026-10-17, after his 21:37 and 23:10 answers: sections 8 v31 then v32 (his 54 sentence), 13 v37b, 15 v17 and 16 v30 (`candidate/fix-20261017d/`); section 2 waits on question 56.
- Owner edits: 88 pass, 3 waiting (section 2's opening, the anomie paragraph, the promotion).

## Current checkpoint

Joel accepted the humanized article (45 a), so `master.md` is the registered master (`PROMOTION-RECEIPT-20261017.md`): `candidate/HUMANIZED-SO-FAR.md`, the working copy, without its version notes (`candidate/fix-20261017d/make_master.py`); `original.md`, the published text, stays as the published source. Section 2 v3.6b is the last change: his 2026-10-18 01:29 UTC first paragraph (56 a) and aside (55 b), and the anomie paragraph after his second paragraph (46 a); batch 428g read every changed paragraph Human and the section 100% Human (`candidate/fix-20261018/b428/`); his screenshot stays in section 12 (with it, one AI window). Next: the master merged into his Substack editor HTML (`candidate/joel-20261018/substack-editor-20261018-0129.html`) with `tools/humanization/substack_merge.py`, and the copy helper from the canonical generator (`docs/SUBSTACK-HELPER-DELIVERY-GATE.md`). The lane's notes are `STATUS.md` (newest entry on top) and `candidate/STATUS.md`.

## Remaining

- The Substack merge and copy helper (Joel uploads the PsyPost screenshot in section 12 himself).
- Claim-level citation review (`CITATIONS.json`, pending) when Joel asks for it.

## Blockers / unresolved

- Open items for Joel are on the lane's questions page (`candidate/OWNER-QUESTIONS.md`). The article's image 7 link is still the old one until the new address is known.
- Pangram checks run in the desktop app's browser pane, signed in to Joel's account; the API key is out of credits.

## Evidence / artifacts

- `IMPORT-RECEIPT-20261013.md`: what was imported, from where, and why the rules don't fork.
- `candidate/sN/`: each section's predictions, parts, batch files, review rounds and install scripts; `candidate/in-context/`: the side-by-side page maps; `candidate/prediction-review/`: the prediction scorecard data.
- `DETECTOR-EVIDENCE.json`, `EDITORIAL-STATUS.json`, `CITATIONS.json`, `SOURCE-EVIDENCE.json`, `OWNER-LOCKS.json`, `ARCHITECTURE.md`.

## Next safe action

Work on a branch from `main` in this folder (`claude/community-joel-1017`, pull request 189, until it merges; 187 merged 2026-10-17 15:49 UTC). Continue with the handoff's next step (`candidate/HANDOFF-community-article.md`): wait for Joel's answers to questions 52 to 54, then do what each answer says there. Before every push, run `python3 scripts/register_article_artifacts.py --article intentional-communities --write` and the repository's checks.
