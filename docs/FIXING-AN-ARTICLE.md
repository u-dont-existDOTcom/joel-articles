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
- Give a question's sub-items numbers (72.1, 72.2) and its options letters (A, B), so an answer like "72.1 B" can't be misread. Letters for both overlapped in question 72 (Joel, 2026-10-21: "your numbering/lettering options are overlapping a bit").

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
- **Keep the inner figures apart.** Before an article's final check, run the conflation sweep (the gate's section "What Joel's answers of 2026-10-21 17:56 UTC taught"): write the article's own map of its figures in its own words, build the prompt with `tools/humanization/conflation_sweep_prompt.py`, and give it to a fresh Opus reader. Fix a finding in drafted text with as few words as possible, each with its own Pangram check; a finding in Joel's words, or one where either reading fits his map, goes to him. In the Inner Child article "inner parent" names the adult the reader builds, so its name for the internalized voice is "the parent you inherited" (turn 81).

- **Safety lines: say one once, where it changes what the reader does.** Joel, 2026-10-23, on the Inner Child guide: "all the extra extra ridiculous safety language which gets repeated everywhere", and after cutting 26 of them, "let's never make those mistakes again pls". A caution, disclaimer or reassurance goes in only if it changes what the reader does in that exercise or situation, isn't a sometimes-true point said as a rule ("X doesn't replace Y"), and isn't already said elsewhere. General guidance on pace, stopping and help lives in one place, as in public self-help books. A queue item's safety note is a reason, not text to add. The linter's O45 fails the "doesn't replace" shape and flags the rest for a reader (gate E247 and E250, Inner Child lane). Cutting one can cost a paragraph its one loose beat, so check each cut paragraph alone after the cut (E248, Inner Child lane).

## 5. Clarity

**Standard for every article, as it's written and before it's published (Joel, 2026-10-23 16:55 UTC):** "let's make sure this kind of check is standard for articles as we write them and as we finalize before publishing in future". The whole-article clarity read finds what passes Pangram but is hard to understand, his own words included, and the reader's edit finds what a reader has to work through: `docs/CLARITY-READ.md` (when, the tool `tools/humanization/clarity_read.py`, and what to do with the readers' plain versions and proposals).

1. **When:** once a full draft exists (a new article, or a long new section), before its whole-article Pangram check; and on the final candidate before publishing, before the final whole-article check; and after a large batch of changes to a published article.
2. **Fresh readers, a third of the article each,** with his own clarity fixes as the examples of what counts; then check every flag against the whole article before it goes to him (in Nibbāna's first read, 7 of 36 flags were explained elsewhere).
3. **The plain versions are suggestions, not the text that goes in.** He rewrote 14 of Nibbāna's 28 when they read AI, and his rewrites passed (gate E241). Send him the numbered list and put in his answers word for word.
4. **The reader's edit goes with it (Joel, 2026-10-23 18:13 UTC: "the clarity check for articles should also include the readability check from GPT that i started doing in the inner child article").** Part 2 of `docs/CLARITY-READ.md`: a fresh reader with its own brief (`clarity_read.py make --kind edit`) looks for what a reader has to work through even where each sentence is clear (too many decisions in one passage, a second subject without a heading, warnings that explain instead of changing what the reader does, paragraphs that perform, explaining past understanding) and proposes moves, headings, labels and real repeats, never new jokes, examples or teaching. Check each against the whole article and his earlier answers, give him the list with your pick for each, and put in what he picks word for word; nothing goes in without his pick (gate E248).

## 6. Pangram

The spending rule is `docs/PANGRAM-PRODUCTION-BUDGET-20261020.md`. In practice:

1. **Write the prediction before every check** (`tools/humanization/pangram_ledger.py predict`), then record the result.
2. **Big checks are free through Substack, and you make the drafts.** A whole article, a large section, or many paragraphs at once go into temporary Substack drafts that you make yourself in the app's browser, where Joel is signed in (up to 99,999 characters each, split at h1 boundaries, real contiguous text only). Title each one plainly, such as "Inner Child, draft A (temp, delete after)", never with "Pangram" in it (gate E205). Never Publish; delete the drafts once the results are recorded (gate E204, the budget rule has the steps). The Pangram label comes from the Pangram extension in Joel's own browser (Brave, on his laptop), so open the secret links there through Claude in Chrome when it's connected; otherwise send him the links and ask for the result pages (the label next to the author's name, clicked twice, then "View Full Analysis"), since those checks aren't in his Pangram history. Don't check dozens of paragraphs one at a time on pangram.com (gate E200).
3. **Find the suspect part by clicking segments.** In Pangram 4.1, when a result is Mixed or AI, or a section is suspected, click each Human and Likely human row in All Segments. The suspect one opens a bar with its AI and Human shares (his screenshot of 2026-10-21: Likely human, Low, AI 36%, Human 64%).
4. **Pay for a check only for one paragraph** (on pangram.com, or through the API, open again since 2026-10-21; the API gives windows, not the GUI's sentence shading), after a segment points at it and with a named cause: up to six tries per paragraph lineage, each with its own diagnosis, and stop when there's no credible one.
5. **The humanizing rules** are the gate, `docs/HUMANIZATION-GATE.md`: screen first, plain words, the tell list, the lean process.
6. **Don't use a community humanizer skill** (such as humanize-kit) on his articles; the gate is the method (E206).
7. **Fresh readers name the tells, not the writer** (`tools/humanization/tell_panel.py`). Before you say a paragraph has no tells left, name a human tell, or ask Joel's help, give the paragraph alone to three fresh readers, Codex from his laptop and a Sonnet and a Haiku agent, with one open question and no list of tells. Fix every sentence two of them flag, run the panel on the draft before its check, and link the panel's PANEL.md in any help request. Joel, 2026-10-23, after the three readers he asked found at once the tells of a paragraph I had said had none left: "so why don't you fix your process before asking for help" (E253, Inner Child lane). A flag on a safety instruction is about its wording: keep the instruction and say it plainly, and if two of your drafts still fail, get the next one from a writer of another family (`tell_panel.py rewrite-prompt`, for Codex). GPT fixed a paragraph that way on its first try after four drafts of mine had kept the same overcareful shape (E256, Inner Child lane).

## 7. Saving and handing over

- Push every step with `tools/humanization/lane_push.py`, after setting `CURRENT-STATE.md`'s next step with `tools/humanization/lane_state.py`, so Joel's other account can pick up from GitHub at any point.
- New questions go on the article's `OWNER-QUESTIONS.md`.
- When his change alters what the guide teaches, not just its wording, and he wants it in the InnerSignal map too, file it in `u-dont-existDOTcom/universal-dev-architecture`'s `suggested-fixes/innerSignalGraph/` lane (its `patterns/suggested-fix-queue.md`; turn 78's gratitude item is an example).
- Send him the files he needs to read (the article page, the questions page, the Substack copy files), never a repository path.
- Keep it lean: a small change takes the short path, and two paragraphs don't take hours.
