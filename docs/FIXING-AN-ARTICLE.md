# Fixing one of Joel's articles: the working order

**ACTIVE (Joel, 2026-10-21 00:49 UTC):** "update the joel-articles guidance so that next time when i ask GPT to fix an article it can do it as well as you could."

This page is for any worker Joel asks to fix an article: GPT, Codex or Claude. It gives the order the Inner Child lane works in, and the checks that caught what earlier passes missed. The detailed rules stay where they are (`docs/INDEX.md` lists them); this page says when each one comes in. Where it and a gate disagree, the gate wins, and the gap goes to Joel's questions page.

## 1. Before changing anything

1. **Save Joel's message first, word for word,** in the article's `experiments/tNN-answers/` folder, with any screenshot he sent. Everything later quotes it.
2. **Read the article's state:** `CURRENT-STATE.md` (its next step), `OWNER-QUESTIONS.md` (what he has answered and what's open) and `OWNER-EDITS.json` (each of his edits, with the strings that prove it's in). Read the article's handoff note if there is one.
3. **Find his own changes first.** When he sends a version of the article (an upload, a Substack draft, the copy he gave another worker), compare it block by block with the repository's version before anything else. Every difference is a decision of his: moves, new headings, heading levels, cuts, new paragraphs. Put them in word for word and fix only obvious typos, listing each one. In turn 77 this found 28 changed paragraphs, a section move and four typos.
4. **When he says he tested something in Pangram, don't test it again.**

## 2. His words and his life

- His text goes in word for word, with his apostrophes, emoji and capitals as he typed them. Fix only obvious typos, and say which.
- Never add a fact about his life that he didn't state. If a paragraph needs one, ask.
- No drug amounts or recipes, even inside a warning.
- Plain words for the guide's therapy words. Never call the inner child "the kid".
- Reassurance lines are content, not scaffolding: this article's readers are often struggling. Don't cut one to tighten a paragraph.
- New wording in his article (a heading, a bridge sentence) is his call. Mark it as yours and ask.
- Every question offers "leave it" and "your words" where they fit, and says which option you'd pick and why.

## 3. Moving sections

What came up when GPT proposed the r03 structure (2026-10-20) and Claude reviewed it (`articles/inner-child-therapy/experiments/t77-answers/GPT-STRUCTURE-REVIEW.md`; applied in turn 78):

1. **Don't undo his own moves.** Compare his latest version with the one before it. A section he moved, and the back-references he wrote for it ("Remember those guards from The Urge to Escape, above?"), are decisions. GPT's M04 sent his altered-states run to the back, undoing the move he had made the day before.
2. **Order carries meaning.** A paragraph that says "don't wait until you're sorted out to reach out" has to come before the get-ready material. Moved to the back, the order says the opposite (his "mess and all" paragraph).
3. **A section stays with the image it extends.** Ask God for a Loan stays in Borrow Love, because the loan is that chapter's picture.
4. **Keep a paragraph with the one it carries on.** When Love Still Feels Missing's third paragraph opens "Taking the hostility out", which picks up the second's "least cruel response". GPT's map split them.
5. **Review every block that changes, not just the move titles.** A move list can hide changes inside it: GPT's M04 also moved two paragraphs within its chapter, and its special-case chapters put the suicide section's help paragraphs first. Claude's review missed both (gate E201). List every block whose place, level or wording changes (in GPT's files, `STRUCTURE-MAP.json`'s `nodes` against `old_nodes`, and `FINAL-ASSEMBLY.json`'s two orders) and give a view on each.
6. **After the moves, check every pointer.** Search the prose for "above", "below", "back in", "earlier", "next", "(see ...)" and every heading's name, check each against the new order, and change only the pointer words. In turn 78, "I'll talk more about those next" became "in the appendix", and "the same test as back in Timing Is Individual" became "as in Timing Is Individual, further down".
7. **Prove nothing was lost.** Compare the old and new article block by block. The only differences should be the ones you list: heading levels, renames, pointer repairs. Every lane note moves with its paragraph. Update the order checks in `OWNER-EDITS.json` and add an entry for the move. Turn 78's script is `articles/inner-child-therapy/experiments/t78-structure/t78_moves.py`.
8. **Ask once, with a pick:** take it all, take your version (with a reason for each change), take his own picks move by move, or none for now.
9. **A moved section gets its own Pangram check** (gate E197): his moves once exposed paragraphs of Claude's that had passed only in the old order.

## 4. Repeats

- Moving sections next to each other doesn't remove repeats. It can make them easier to notice.
- After big changes, run the whole-article repeats read: `tools/humanization/reviewer/reviewer.py repeats`, two separate readers, one run for the whole article (gate E172). Check every quote a reader reports against the article before acting on it.
- Cut only text a worker drafted, and only when the cut loses no meaning the article needs (`AGENTS.md`, code review rules). A repeat in Joel's own words goes to him as a question.

## 5. Pangram

The spending rule is `docs/PANGRAM-PRODUCTION-BUDGET-20261020.md`. In practice:

1. **Write the prediction before every check** (`tools/humanization/pangram_ledger.py predict`), then record the result.
2. **Big checks are free through Substack.** A whole article, a large section, or many paragraphs at once go into temporary Substack posts that Joel makes, up to about 9,999 words each, split at h1 boundaries, real contiguous text only. Give him the copy files and the steps in one message. Don't check dozens of paragraphs one at a time on pangram.com (gate E200).
3. **Find the suspect part by clicking segments.** In Pangram 4.1, when a result is Mixed or AI, or a section is suspected, click each Human and Likely human row in All Segments. The suspect one opens a bar with its AI and Human shares (his screenshot of 2026-10-21: Likely human, Low, AI 36%, Human 64%).
4. **Pay for a check on pangram.com only for one paragraph,** after a segment points at it and with a named cause: up to six tries per paragraph lineage, each with its own diagnosis, and stop when there's no credible one.
5. **The humanizing rules** are the gate, `docs/HUMANIZATION-GATE.md`: screen first, plain words, the tell list, the lean process.

## 6. Saving and handing over

- Push every step with `tools/humanization/lane_push.py`, after setting `CURRENT-STATE.md`'s next step with `tools/humanization/lane_state.py`, so Joel's other account can pick up from GitHub at any point.
- New questions go on the article's `OWNER-QUESTIONS.md`.
- When his change alters what the guide teaches, not just its wording, and he wants it in the InnerSignal map too, file it in `u-dont-existDOTcom/universal-dev-architecture`'s `suggested-fixes/innerSignalGraph/` lane (its `patterns/suggested-fix-queue.md`; turn 78's gratitude item is an example).
- Send him the files he needs to read (the article page, the questions page, the Substack copy files), never a repository path.
- Keep it lean: a small change takes the short path, and two paragraphs don't take hours.
