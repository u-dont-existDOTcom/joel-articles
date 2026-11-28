# The rule tree's open questions: his answers

His answers: [the export of 2026-11-28 15:23 UTC](ANSWERS-OPEN-20261128-1523.json) (12 approved), on [the questions](OPEN-QUESTIONS.md). Approve kept what the editor did until he answered; each rule below is as it now stands in [the rule tree](https://claude.ai/artifact/RPYerG1RZ1iNwECeaBTSZk).

## A model's text is the editor's to fix, even after he humanized it

- **His answer:** approved
- **His note:** "right you only need to ask me if you're unsure if it still says what i was saying, OR if you think you might have just "fixed" some ai slop so it passes pangram, but it's an indicator that it lacks the author's voice. i also want you to keep track of whenever i edit a section because it doesn't get my points across, try to develop some understanding of which sections might be ai slop even if they pass pangram high conf. you surely already have many of my edits like this saved but probably you haven't been using them if they didn't directly help with pangram, you prob just tagged them as "only author could do this" but should have tagged as "pangram passed ai slop" or whatever else you can figure out more specifically about why i might have edited it. here's one section i'm fixing now, "things get tricky fast" in romance article, i changed it to: "If you have trusted friends or family, their opinion on your new love might be really helpful, since they aren’t blinded by it the way you are. But accepting their opinions can be quite difficult, if they are critical. This happened to me with my first wife especially. Pretty much everyone was asking why I was with her, what I saw in her. And since she had two sides to her, I could easily point to the good that I saw. I didn’t want to think that she might end up going in the wrong direction. I wanted to help her be the best version of herself. The longer you wait to ask the opinion of your confidants, the harder it will be. Had I shown folks her OKCupid profile before even responding to her message, they might have shown me all the red flags in it that I overlooked. After we already had sex, I felt committed, so that was possibly too late. I’ll expand on the topic of not closing down your outside world in Don’t Make Your Partner Your Whole World. ""
- **The rule now:** In an article a model drafted, the words are the model's unless they were his before the humanizing began. In wording he humanized himself, what he decided stays; the editor fixes the rest of that wording itself, tested, and it goes in like any tested change (R-tested-change-goes-in). He is asked only where the editor is unsure the fix still says what he was saying, or where a fix may only have made AI slop pass Pangram: passing that way is a sign the passage lacks the author's voice (R-slop-that-passed). It is never handed back to him as his words to fix.
- **In the tree:** [A model's text is the editor's to fix, even after he humanized it](https://claude.ai/artifact/RPYerG1RZ1iNwECeaBTSZk#R-model-text-is-mine)

## Every window of the editor's text is aimed at Human High

- **His answer:** approved
- **His note:** "unless it's just a heading or a word or phrase, but a whole sentence at least yeah that's more important to fix"
- **The rule now:** A window that reads AI, or Human at Low or Medium confidence, is work to do and doesn't count as done; one such reading is enough, with no second check to confirm it. The editor keeps fixing while it is on track. A paragraph of the editor's that is still short of High when its tries are spent stays out of the article and is reported as open work with its link, never as passed; a window reading Medium that is only a heading, a word or a phrase doesn't hold it out, while one with a whole sentence does. Some pieces aren't worth fixing, because Pangram has bugs: a short "Why?" often reads Medium, and such pieces are left. A split at "Dr." may be closed by dropping the title, especially where the person was already introduced with it; that is a hack, so it comes last (R-hacks-last).
- **In the tree:** [Every window of the editor's text is aimed at Human High](https://claude.ai/artifact/RPYerG1RZ1iNwECeaBTSZk#R-every-window-high)

## A rewrite of his sentences is compared with his text once per pass

- **His answer:** approved
- **The rule now:** After a pass that rewrites his sentences (a humanizing pass, a reader's edit), a fresh reader reads the result beside his text once, sentence by sentence, at a size that fits the change, for every place it now reads worse: garbled, unclear, a point or a step lost, vaguer. Each such place is fixed or goes to him. The old per-edit ledgers, the fixed three writing rounds and the audit offers don't block work.
- **In the tree:** [A rewrite of his sentences is compared with his text once per pass](https://claude.ai/artifact/RPYerG1RZ1iNwECeaBTSZk#R-check-rewrite-once)

## Rework "X does not Y" statements, keeping what they deny

- **His answer:** approved
- **The rule now:** The abstract kind of "X does not Y" (""I saw it" does not create a duty to act") is reworked by default, in any wording that keeps what it denies, and kept where it is the clearest way to say the thing; a plain negative is judged case by case. A denial of fact or of safety is not softened into a "might" for the detector.
- **In the tree:** [Rework "X does not Y" statements, keeping what they deny](https://claude.ai/artifact/RPYerG1RZ1iNwECeaBTSZk#R-x-does-not-y)

## Kitchen details and added weekdays are AI signs

- **His answer:** approved
- **The rule now:** A kitchen detail reads as AI, and adding a day of the week to it makes two signs. A weekday the editor added goes; a real day in one of his own stories stays. A date range is not a human tell.
- **In the tree:** [Kitchen details and added weekdays are AI signs](https://claude.ai/artifact/RPYerG1RZ1iNwECeaBTSZk#R-kitchen-and-weekdays)

## Two hyphens for every dash, straight quotes and apostrophes

- **His answer:** approved
- **The rule now:** In all his articles every dash becomes his two hyphens "--", with no spaces around them, as he types them, and curly quote marks and apostrophes are straightened.
- **In the tree:** [Two hyphens for every dash, straight quotes and apostrophes](https://claude.ai/artifact/RPYerG1RZ1iNwECeaBTSZk#R-dashes-and-quotes)

## His harm-reduction warnings stay, by meaning and facts

- **His answer:** approved
- **The rule now:** A warning Joel wrote against a dangerous combination stays in the article. Its words may change while the humanizing is done, as long as every fact stays: what, when, how much. Amounts he wrote stay, and the editor adds none. Where it repeats another of his warnings, moving it to one place or cutting the repeat is proposed to him (R-few-cautions).
- **In the tree:** [His harm-reduction warnings stay, by meaning and facts](https://claude.ai/artifact/RPYerG1RZ1iNwECeaBTSZk#R-his-warnings-stay)

## A close word-by-word read for sense before a post

- **His answer:** approved
- **The rule now:** Before an article goes into his post, every word is read for sense, to catch a real word standing where another belongs. An obvious wrong word is fixed and he is told; a word whose intended meaning is unclear goes to him. The read is tested with planted errors, as it is now.
- **In the tree:** [A close word-by-word read for sense before a post](https://claude.ai/artifact/RPYerG1RZ1iNwECeaBTSZk#R-close-read)

## Sort the contents with his reasons, and show him the whole order once

- **His answer:** approved
- **The rule now:** To reorder an article, first read the contents alone, then the guide and his answers for what each part holds. Ask him, in one message before sorting, only what those leave open. Sort with his heuristics and put the whole proposed order to him once, with a reason for each move and a pick. A section that moves gets its own Pangram check. Fresh readers are tested on the contents ("where would you look first?") only when he asks.
- **In the tree:** [Sort the contents with his reasons, and show him the whole order once](https://claude.ai/artifact/RPYerG1RZ1iNwECeaBTSZk#R-contents-order)

## Cite a study only where the reader expects evidence, and ask at the start how much research the article carries

- **His answer:** approved
- **The rule now:** Looking up a study to back a point can be good, but it looks odd where the reader wouldn't expect one. Add evidence where it fits the context, and ask Joel when that is unclear. When work on an article begins, ask him one plain question, how much research evidence goes in: none (his experience and reasoning carry it); a little, only where a reader would expect a source; or full citations for every claim of fact. The answer decides whether studies are looked up at all, and where.
- **In the tree:** [Cite a study only where the reader expects evidence, and ask at the start how much research the article carries](https://claude.ai/artifact/RPYerG1RZ1iNwECeaBTSZk#R-studies-where-expected)

## His fixes are easy to search for the ones that could help

- **His answer:** approved
- **The rule now:** His before-and-afters are kept in an index, one line each, saying what the passage lacked (from the ways his fixes differ from the editor's drafts) and what he did. Before the editor rewrites a passage, a reader picks from the index the fixes closest to it by meaning, and the editor reads those in full. A graph only if the index isn't enough.
- **In the tree:** [His fixes are easy to search for the ones that could help](https://claude.ai/artifact/RPYerG1RZ1iNwECeaBTSZk#R-fixes-searchable)

## Work out how to mimic the way Pangram reads text

- **His answer:** approved
- **The rule now:** Train a small stand-in on the record of Pangram checks (hundreds of texts with how each read), test it on checks it hasn't seen, and report how well it predicts Pangram. If it predicts well, it helps choose what to fix before a check is spent; it never takes Pangram's place.
- **In the tree:** [Work out how to mimic the way Pangram reads text](https://claude.ai/artifact/RPYerG1RZ1iNwECeaBTSZk#R-mimic-pangram)
