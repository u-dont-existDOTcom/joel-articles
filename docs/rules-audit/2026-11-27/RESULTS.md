# The rules audit: what happened to each card

His answers: [the export of 2026-11-28 10:24 UTC](ANSWERS-20261128-1024.json) (33 approved, 4 to revise), on [the cards](QUESTIONS.md). Each approved fix and each revision is now a rule of the rule tree, written once ([the tree](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/README.md)); where a tool enforced the old rule, the tool changed too.

## S1. The smooth lesson: the accurate word, not the same word

- **His answer:** approved
- **His note:** "it's not that we always want to name what it stands for, it depends on the context. sometimes you want "it" and sometimes it's unclear what exactly it stands for either bc it was too late after the rferent or there were other things between the referent and it that it could stand for"
- **Now in the tree as:** [Each sentence, paragraph and idea shows how it follows](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-connect--each-sentence-paragraph-and-idea-shows-how-it-follows); [The word that says exactly what the thing does](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-accurate-word--the-word-that-says-exactly-what-the-thing-does); ["It" where it is clear, the name where it isn't](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-clear-it--it-where-it-is-clear-the-name-where-it-isnt); [A lesson's method is the reason he gave; one fix's shape is only an example](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-lesson-reason-not-feature--a-lessons-method-is-the-reason-he-gave-one-fixs-shape-is-only-an-example)

## S2. Your answer's words: what is relevant, not every word

- **His answer:** approved
- **Now in the tree as:** [Each sentence, paragraph and idea shows how it follows](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-connect--each-sentence-paragraph-and-idea-shows-how-it-follows); [Keep the meaning, scope and condition he gave, not every word](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-keep-what-he-meant--keep-the-meaning-scope-and-condition-he-gave-not-every-word)

## S3. A check of every new lesson against your words (my addition)

- **His answer:** approved
- **His note:** "we should also be checking if lessons interact or contradict each other, and we should do periodic reviews to see which lessons are overall helping vs which aren't"
- **Now in the tree as:** [Every new lesson is checked against his words](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-lesson-checked--every-new-lesson-is-checked-against-his-words); [A lesson's method is the reason he gave; one fix's shape is only an example](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-lesson-reason-not-feature--a-lessons-method-is-the-reason-he-gave-one-fixs-shape-is-only-an-example); [Lessons are reviewed from time to time for whether they help](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-review-lessons--lessons-are-reviewed-from-time-to-time-for-whether-they-help)

## C01. Near-miss step limit: a word or two, 20% / 40% refusals

- **His answer:** approved
- **His note:** "yes keep in midn that usually it makes sense to focus on the most AI sentences first, altho also keeping in mind that fixing one sentence can make a different sentence/part look better to pangram sometimes. and occasionally as you see in how i do it, pangram gets worse, but i only change strategy if i feel unsure that my fix was realyl good for the reader. if i'm sure it wa sgood, i keep going on that same strategy and try to find other things that are tripping pangram up before  i re-assess if i should change strat"
- **Now in the tree as:** [Start with the parts that read most AI](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-most-ai-first--start-with-the-parts-that-read-most-ai); [After a near miss, start from it and clear up everything unclear](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-start-from-near-miss--after-a-near-miss-start-from-it-and-clear-up-everything-unclear); [Make the next obvious fix, and keep a strategy that is good for the reader](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-keep-strategy--make-the-next-obvious-fix-and-keep-a-strategy-that-is-good-for-the-reader); [Fix what can be fixed before asking, then ask in his words](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-stuck-paragraph--fix-what-can-be-fixed-before-asking-then-ask-in-his-words)
- **Tools changed:** pangram_ledger.py: the 20% near-miss and 40% big-change refusals are notes now

## C03. "Payoff first" fixed as a form on every sentence and paragraph

- **His answer:** approved
- **His note:** "yes and this also has to do usually with connections between sentences, paragraphs, ideas. one classic fail eexample you keep making for some reason is a sentence that begins, "In one trial on.." like out of nowhere, totally unexpected. whenever i read AI articles people publish it always takes like so long for me to understand anything becauuse of how disconnected it all is"
- **Now in the tree as:** [The reader knows early why they are reading this](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-payoff-first--the-reader-knows-early-why-they-are-reading-this); [Each sentence, paragraph and idea shows how it follows](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-connect--each-sentence-paragraph-and-idea-shows-how-it-follows)
- **Tools changed:** sense_receipt.py: the opening refusal is gone

## C13. His list fixes made a template for every list

- **His answer:** approved
- **His note:** "yes unpacking lists does often help, although i wouldn't necessarily unpack every list robotically, that could be bloating things obviously like say we have a list of contraindications, we can list 15 meds and pangram is fine with that, no need to unpack each one, but if the list contains things that aren't so obvious and could use explaining, then that's part of the clarifying rule, and in general AI tends to have too much in its lists, because it wants to cover every part of the advice and avoid holes in the argument. there should be some balance there. sometimes we can say two things with one word, or sometimes one part of the list is more tangential or it's already expalined elsewhere or...  we can do some more testing on this to see what looks right in different cases"
- **Now in the tree as:** [Unpack a compressed list where its items need explaining](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-unpack-lists--unpack-a-compressed-list-where-its-items-need-explaining); [Don't fill a list to cover every hole](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-lists-not-overfull--dont-fill-a-list-to-cover-every-hole)

## C14. "Plain word" misreads "converted into"; join and plain word made compulsory

- **His answer:** approved
- **His note:** "and btw "for the thing" is an ai tell"
- **Now in the tree as:** [The word that says exactly what the thing does](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-accurate-word--the-word-that-says-exactly-what-the-thing-does); [Join sentences only where the stretch reads choppy](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-join-choppy--join-sentences-only-where-the-stretch-reads-choppy); [A phrase is a tell for what it does](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-phrase-tells--a-phrase-is-a-tell-for-what-it-does)
- **Tools changed:** pangram_ledger.py: no first-fix declaration; tells_lint.py: a note for "for the thing"

## C21. Shapes of one rewrite made recipes

- **His answer:** approved
- **His note:** "ok i notice you have been making some typos, "fix of your(s) did", that's weird for ai to make typos..."
- **Now in the tree as:** [The word that says exactly what the thing does](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-accurate-word--the-word-that-says-exactly-what-the-thing-does); [Point to the other section instead of saying it again](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-link-not-repeat--point-to-the-other-section-instead-of-saying-it-again); [Rework "X does not Y" statements, keeping what they deny](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-x-does-not-y--rework-x-does-not-y-statements-keeping-what-they-deny); [Read every paragraph and card before a page goes](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-read-page-before-sending--read-every-paragraph-and-card-before-a-page-goes); [A lesson's method is the reason he gave; one fix's shape is only an example](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-lesson-reason-not-feature--a-lessons-method-is-the-reason-he-gave-one-fixs-shape-is-only-an-example)

## C28. Details invented, or his content changed, to move Pangram

- **His answer:** approved
- **His note:** ""your(s)" again...   Dr. could be dropped especially if they were already introduced as such i suppose but this is a real hack and pangram hacks are ok if we need to use them, but i'd put this very much last as a rule, we want to have the rules that help the reader up front before the hacks"
- **Now in the tree as:** [Nothing is invented about his life, and no opinion is written as his](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-no-invented-life--nothing-is-invented-about-his-life-and-no-opinion-is-written-as-his); [When he shows a change, fix the process that missed it](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-learn-from-his-changes--when-he-shows-a-change-fix-the-process-that-missed-it); [Every window of the editor's text is aimed at Human High](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-every-window-high--every-window-of-the-editors-text-is-aimed-at-human-high); [A Pangram hack comes after every rule that helps the reader](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-hacks-last--a-pangram-hack-comes-after-every-rule-that-helps-the-reader); [Read every paragraph and card before a page goes](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-read-page-before-sending--read-every-paragraph-and-card-before-a-page-goes)

## C10. Word-by-word accounting in place of a meaning check

- **His answer:** approved
- **Now in the tree as:** [His harm-reduction warnings stay, by meaning and facts](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-his-warnings-stay--his-harm-reduction-warnings-stay-by-meaning-and-facts); [Keep the meaning, scope and condition he gave, not every word](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-keep-what-he-meant--keep-the-meaning-scope-and-condition-he-gave-not-every-word); [A word that names a concept isn't swapped for a different concept](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-concept-word-stays--a-word-that-names-a-concept-isnt-swapped-for-a-different-concept); [Meaning is judged by a reader; a list or pattern only finds candidates](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-rules-fit-capability--meaning-is-judged-by-a-reader-a-list-or-pattern-only-finds-candidates)
- **Tools changed:** fidelity_keys.py: a warning word the new line lacks is reported, not failed; numbers, doses and compounds stay exact

## C11. Overused words and shapes hard-failed by the linter

- **His answer:** to revise (done as his note says)
- **His note:** ""one" plus a noun... what i meant is, i often find AI using "one" where a human would use "a"  so if it sounds better to use "a" than "one" do that. "one time is too many" would still be "one time is too many" of course."
- **Now in the tree as:** [Overused AI words are read, not banned](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-overused-words--overused-ai-words-are-read-not-banned); ["One ordinary" and "one honest action" go wherever they appear](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-one-ordinary--one-ordinary-and-one-honest-action-go-wherever-they-appear); ["A" where a person would say "a", not "one"](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-one-for-a--a-where-a-person-would-say-a-not-one); [Rework "X does not Y" statements, keeping what they deny](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-x-does-not-y--rework-x-does-not-y-statements-keeping-what-they-deny)
- **Tools changed:** tells_lint.py: overused words are reported, not failed; a new note for "one" where "a" reads better; pangram_ledger.py: a try that adds an overused word gets a note, not a refusal

## C22. Counts standing in for judgment: threes, questions in a row, short lines, contrasts, repeats

- **His answer:** approved
- **Now in the tree as:** [Never cut something important, or keep something unclear, to pass Pangram](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-never-cut-important--never-cut-something-important-or-keep-something-unclear-to-pass-pangram); [A count sends the editor to read; it fails nothing](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-counts-send-to-read--a-count-sends-the-editor-to-read-it-fails-nothing); [Meaning is judged by a reader; a list or pattern only finds candidates](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-rules-fit-capability--meaning-is-judged-by-a-reader-a-list-or-pattern-only-finds-candidates)
- **Tools changed:** tells_lint.py: no count fails a draft by itself

## C23. One-case phrases made string tells

- **His answer:** approved
- **Now in the tree as:** [A phrase is a tell for what it does](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-phrase-tells--a-phrase-is-a-tell-for-what-it-does); [Kitchen details and added weekdays are AI signs](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-kitchen-and-weekdays--kitchen-details-and-added-weekdays-are-ai-signs)
- **Tools changed:** tells_lint.py and tells_registry.json: string tells with no words of his are notes

## C25. Headings sharing a word: toc_check string match

- **His answer:** approved
- **Now in the tree as:** [No two headings in a row say or ask the same thing](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-no-twin-headings--no-two-headings-in-a-row-say-or-ask-the-same-thing); [Meaning is judged by a reader; a list or pattern only finds candidates](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-rules-fit-capability--meaning-is-judged-by-a-reader-a-list-or-pattern-only-finds-candidates)
- **Tools changed:** toc_check.py: a fate only for pairs a reader marked as the same

## C04. Nothing below Human High: hard gate, Medium chased, approved changes held

- **His answer:** approved
- **His note:** "yes you start working on the parts that are most AI as i mentioned"
- **Now in the tree as:** [What he approved or agreed to is made at once](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-approved-goes-in--what-he-approved-or-agreed-to-is-made-at-once); [Start with the parts that read most AI](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-most-ai-first--start-with-the-parts-that-read-most-ai); [Every window of the editor's text is aimed at Human High](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-every-window-high--every-window-of-the-editors-text-is-aimed-at-human-high)
- **Tools changed:** apply_gate.py: a content change he approved goes in at once, recorded with what he approved

## C05. When a stuck paragraph goes to him: "ask as soon as" against "keep fixing"

- **His answer:** approved
- **His note:** "yes i want to make this a bit smarter i mean, don't even try if you have no idea what you're doing, but if you're hot on the trail and just need more budget then the budget should be flexible. sometimes i will spend more than 10 pangram calls myself because i'm trying to be granular enough to give you excellent minimal pair lessons, you can also use more pangram calls if that would help you learn"
- **Now in the tree as:** [About ten tries a paragraph, with reasons, and more when it pays](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-budget--about-ten-tries-a-paragraph-with-reasons-and-more-when-it-pays); [Fix what can be fixed before asking, then ask in his words](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-stuck-paragraph--fix-what-can-be-fixed-before-asking-then-ask-in-his-words)
- **Tools changed:** pangram_ledger.py: ten tries a paragraph, more with a named trail; the score comparison no longer stops a try

## C07. Pangram budget: six against ten, paid single paragraphs against free Substack

- **His answer:** approved
- **His note:** "maybe merge this with previous? in general merge any rules that could be merged"
- **Now in the tree as:** [Cut a repeat, a second explanation or filler when the article reads better without it](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-cut-repeats--cut-a-repeat-a-second-explanation-or-filler-when-the-article-reads-better-without-it); [Never cut something important, or keep something unclear, to pass Pangram](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-never-cut-important--never-cut-something-important-or-keep-something-unclear-to-pass-pangram); [Make the next obvious fix, and keep a strategy that is good for the reader](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-keep-strategy--make-the-next-obvious-fix-and-keep-a-strategy-that-is-good-for-the-reader); [Try a new strategy on one paragraph](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-one-paragraph-for-strategy--try-a-new-strategy-on-one-paragraph); [About ten tries a paragraph, with reasons, and more when it pays](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-budget--about-ten-tries-a-paragraph-with-reasons-and-more-when-it-pays); [A whole or half article is checked the free way](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-free-route-for-big-checks--a-whole-or-half-article-is-checked-the-free-way); [Every rule lives once, in this tree](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-tree-is-home--every-rule-lives-once-in-this-tree); [A lesson's method is the reason he gave; one fix's shape is only an example](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-lesson-reason-not-feature--a-lessons-method-is-the-reason-he-gave-one-fixs-shape-is-only-an-example)
- **Tools changed:** pangram_ledger.py (with C05); pangram_api.py: the size cap warns, and refuses only half an article or more

## C08. Safety, caution and reassurance lines: kept, cut, or sent to him?

- **His answer:** to revise (done as his note says)
- **His note:** "yes i'd like to be a bit more strict on the safety thing, in general we want to minimize the placement of caution statements -- sometimes we can just put all the cautions in one section rather than repeat them everywhere. there's always something that could hurt a reader. if i say drink water, that could hurt if they drink it wrong or too much, so we should question whether this caution statement is making the reader into an idiot. like i saw this IG video recently of a woman explaining how to relax, and she must have been brainwashed by AI bc she said, "breathe in now, if it feels safe" -- i commented, "you mean it might be safer not to breathe in?" this kind of stuff is annoying as hell"
- **Now in the tree as:** [Few cautions, each said once, none that treats the reader as an idiot](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-few-cautions--few-cautions-each-said-once-none-that-treats-the-reader-as-an-idiot); [A model's caution is checked against his words and its source](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-model-cautions-checked--a-models-caution-is-checked-against-his-words-and-its-source); [His harm-reduction warnings stay, by meaning and facts](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-his-warnings-stay--his-harm-reduction-warnings-stay-by-meaning-and-facts)

## C12. Whose words: his typed wording, kept lines, and the editor's own guesses

- **His answer:** approved
- **Now in the tree as:** [A model's text is the editor's to fix, even after he humanized it](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-model-text-is-mine--a-models-text-is-the-editors-to-fix-even-after-he-humanized-it); [What he wrote himself stays, with obvious slips fixed](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-his-own-text-stays--what-he-wrote-himself-stays-with-obvious-slips-fixed); [A lasting list of what he said stays as it is](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-keep-as-is-list--a-lasting-list-of-what-he-said-stays-as-it-is); [Two hyphens for every dash, straight quotes and apostrophes](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-dashes-and-quotes--two-hyphens-for-every-dash-straight-quotes-and-apostrophes)
- **Tools changed:** keep_as_is.py and render_article_so_far.py: an entry that is my own reading is a note, not a refusal

## C15. Human tell: defined narrower than he said, two definitions live

- **His answer:** to revise (done as his note says)
- **His note:** "well, if the model wrote a human tell that comes from a legit list of human tells from human tells, then that would still bea  human tell. the model is also trying to copy the style of the author so it should be trying to create these human tells itself, the ones that it creates based on the author's writing (if there is author writing to look at hopefully), should then be categorized as "human tell attempts" which the author would then approve reject or modify before they can be categorized as human tells. this should be higher priority to develop to better match the author's voice and make the prose sound more human (it isn't required to pass pangram, but it's required to have better writing in any article where it's appropriate (i.e. maybe not an academic study))"
- **Now in the tree as:** [What counts as a human tell](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-human-tell--what-counts-as-a-human-tell); [The editor tries human tells in the author's style, and the author approves them](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-human-tell-attempts--the-editor-tries-human-tells-in-the-authors-style-and-the-author-approves-them); [Nothing is invented about his life, and no opinion is written as his](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-no-invented-life--nothing-is-invented-about-his-life-and-no-opinion-is-written-as-his); [Fix what can be fixed before asking, then ask in his words](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-stuck-paragraph--fix-what-can-be-fixed-before-asking-then-ask-in-his-words)

## C24. Glosses: never in brackets, always in the first sentence, or taken out

- **His answer:** approved
- **Now in the tree as:** [Explain a term where the reader first needs it](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-gloss--explain-a-term-where-the-reader-first-needs-it)
- **Tools changed:** tells_lint.py: brackets around a gloss are never failed

## C02. Per-sentence receipts and link-word checks before every Pangram try

- **His answer:** approved
- **His note:** "something like this already exists maybe merge"
- **Now in the tree as:** [Each sentence, paragraph and idea shows how it follows](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-connect--each-sentence-paragraph-and-idea-shows-how-it-follows); [Sense first, then make it read well, then see whether Pangram agrees](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-reads-well-first--sense-first-then-make-it-read-well-then-see-whether-pangram-agrees)
- **Tools changed:** pangram_ledger.py and suggestion_review.py: no refusal for a missing receipt; sense_receipt.py checks only what is present and wrong, and the link-position test is gone

## C16. Contents order: ask him first, move by move, tree tests

- **His answer:** approved
- **Now in the tree as:** [Sort the contents with his reasons, and show him the whole order once](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-contents-order--sort-the-contents-with-his-reasons-and-show-him-the-whole-order-once)

## C17. Fresh-reader passes required before every check

- **His answer:** to revise (done as his note says)
- **His note:** "and not just against my own fixes in that article of course but any fixes in the repo that could be useful for that context we should also try to make some kind of graph for the fixes so that it's easy to find which fixes might be most helpful, although maybe graph is the wrong approach, i'm not sure how to make the fixes searchable exactly. i'm curious how we can mimic the way pangram analyzes text statistically.  and quizzes are only offered if you think they would be more helpful than trying first thru pangram"
- **Now in the tree as:** [The editor reads its own text against his fixes](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-read-against-his-fixes--the-editor-reads-its-own-text-against-his-fixes); [His fixes are easy to search for the ones that could help](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-fixes-searchable--his-fixes-are-easy-to-search-for-the-ones-that-could-help); [Work out how to mimic the way Pangram reads text](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-mimic-pangram--work-out-how-to-mimic-the-way-pangram-reads-text)
- **Tools changed:** sense_receipt.py: the fresh reads are optional and their marks judged; his_fixes_brief.md says the same

## C18. What needs a card: tallies, prefixes and standing questions

- **His answer:** approved
- **Now in the tree as:** [A model's text is the editor's to fix, even after he humanized it](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-model-text-is-mine--a-models-text-is-the-editors-to-fix-even-after-he-humanized-it); [Ask only where his opinion is really needed](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-ask-when-needed--ask-only-where-his-opinion-is-really-needed); [A tested change that keeps the meaning goes in and is reported](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-tested-change-goes-in--a-tested-change-that-keeps-the-meaning-goes-in-and-is-reported)
- **Tools changed:** suggestion_review.py: a plain reason on a card, no fixed prefixes; approval_record.py: no approval count

## C20. Tell panel forced after two AI reads

- **His answer:** approved
- **His note:** "this sounds like some other rule you can merge"
- **Now in the tree as:** [Make the next obvious fix, and keep a strategy that is good for the reader](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-keep-strategy--make-the-next-obvious-fix-and-keep-a-strategy-that-is-good-for-the-reader); [A reader's flag is a lead to weigh](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-flags-are-leads--a-readers-flag-is-a-lead-to-weigh); [Fix what can be fixed before asking, then ask in his words](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-stuck-paragraph--fix-what-can-be-fixed-before-asking-then-ask-in-his-words)
- **Tools changed:** pangram_ledger.py: no tell-panel refusal

## C26. Every-word read with planted errors before publication

- **His answer:** approved
- **Now in the tree as:** [A close word-by-word read for sense before a post](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-close-read--a-close-word-by-word-read-for-sense-before-a-post); [A model's text is the editor's to fix, even after he humanized it](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-model-text-is-mine--a-models-text-is-the-editors-to-fix-even-after-he-humanized-it)

## C27. Blocking gates from August and September with no words of his

- **His answer:** approved
- **His note:** "some of this can be mergeed"
- **Now in the tree as:** [Never cut something important, or keep something unclear, to pass Pangram](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-never-cut-important--never-cut-something-important-or-keep-something-unclear-to-pass-pangram); [A rewrite of his sentences is compared with his text once per pass](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-check-rewrite-once--a-rewrite-of-his-sentences-is-compared-with-his-text-once-per-pass); [The old gate is history](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-old-gate-historical--the-old-gate-is-history)

## C30. Workflow rules stretched from one remark

- **His answer:** approved
- **Now in the tree as:** [For a Substack check, he gets a link he only has to open](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-preview-link--for-a-substack-check-he-gets-a-link-he-only-has-to-open); [A turn doesn't stop while there is work the editor can do](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-keep-working--a-turn-doesnt-stop-while-there-is-work-the-editor-can-do); [A lane's changes merge on their own](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-lane-changes-merge-themselves--a-lanes-changes-merge-on-their-own); [Each turn starts by reading what is addressed to the lane](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-mailbox-check--each-turn-starts-by-reading-what-is-addressed-to-the-lane)

## C06. Cuts and merges made without showing him

- **His answer:** approved
- **Now in the tree as:** [Cut a repeat, a second explanation or filler when the article reads better without it](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-cut-repeats--cut-a-repeat-a-second-explanation-or-filler-when-the-article-reads-better-without-it); [Every cut or merge can be seen and put back](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-cuts-shown--every-cut-or-merge-can-be-seen-and-put-back)

## C09. One content answer stretched to other text or to every article

- **His answer:** approved
- **Now in the tree as:** [A content answer changes what he named](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-change-what-he-named--a-content-answer-changes-what-he-named)

## C19. Evidence and source rules stricter than he said

- **His answer:** approved
- **His note:** "one thing i notice is you tend to try to look up studies to give evidence, which can be good, but sometimes it can look weird if that's not what the reader would expect there. so try to make sure that is appropriate in context and if unclear you can ask the author. probably also good at the beginning of any article to ask how much research evidence shoudl go into the article. you can brainstorm this also"
- **Now in the tree as:** [In a science article, get the science right before the wording](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-science-first--in-a-science-article-get-the-science-right-before-the-wording); [No benefit or risk wider or vaguer than the sources show](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-claims-match-sources--no-benefit-or-risk-wider-or-vaguer-than-the-sources-show); [Cite a study only where the reader expects evidence, and ask at the start how much research the article carries](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-studies-where-expected--cite-a-study-only-where-the-reader-expects-evidence-and-ask-at-the-start-how-much-research-the-article-carries); [Once he says his experience stands, it is written as his](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-his-experience-stands--once-he-says-his-experience-stands-it-is-written-as-his); [A missing citation isn't assumed cut on purpose](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-citations-not-assumed-cut--a-missing-citation-isnt-assumed-cut-on-purpose)

## C29. Always-cut rules built from a few of his picks

- **His answer:** approved
- **His note:** "i also wanted to help you make more human jokes, we never did that lesson, we should do that (of course trying to copy author's voice)"
- **Now in the tree as:** [Cut a repeat, a second explanation or filler when the article reads better without it](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-cut-repeats--cut-a-repeat-a-second-explanation-or-filler-when-the-article-reads-better-without-it); [A lesson on writing more human jokes](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-humor-lesson--a-lesson-on-writing-more-human-jokes); [His jokes stay unless he cuts them](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-his-jokes-stay--his-jokes-stay-unless-he-cuts-them); [Nothing is invented about his life, and no opinion is written as his](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-no-invented-life--nothing-is-invented-about-his-life-and-no-opinion-is-written-as-his)

## C31. A test result that shows less than the rule says

- **His answer:** approved
- **His note:** "can merge with some other rules"
- **Now in the tree as:** [Sense first, then make it read well, then see whether Pangram agrees](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-reads-well-first--sense-first-then-make-it-read-well-then-see-whether-pangram-agrees)

## OLD-GATE. The old gate (September to early November): mark it historical

- **His answer:** approved
- **His note:** "can merge with some other rules"
- **Now in the tree as:** [A list only where one is really needed](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-lists-only-when-needed--a-list-only-where-one-is-really-needed); [A manual-like march is broken by making each point read well](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-break-manual-march--a-manual-like-march-is-broken-by-making-each-point-read-well); [What he approved or agreed to is made at once](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-approved-goes-in--what-he-approved-or-agreed-to-is-made-at-once); [Every window of the editor's text is aimed at Human High](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-every-window-high--every-window-of-the-editors-text-is-aimed-at-human-high); [A reader's flag is a lead to weigh](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-flags-are-leads--a-readers-flag-is-a-lead-to-weigh); [Before a recheck, say which parts are likely to come back AI](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-predict-before-recheck--before-a-recheck-say-which-parts-are-likely-to-come-back-ai); [Overused AI words are read, not banned](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-overused-words--overused-ai-words-are-read-not-banned); [Ask only where his opinion is really needed](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-ask-when-needed--ask-only-where-his-opinion-is-really-needed); [When unsure how a rule applies, give him examples to score](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-examples-to-score--when-unsure-how-a-rule-applies-give-him-examples-to-score); [The old gate is history](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-old-gate-historical--the-old-gate-is-history)

## EMULATE. Emulate: retired, but parts still read as active

- **His answer:** approved
- **Now in the tree as:** [Cut a repeat, a second explanation or filler when the article reads better without it](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-cut-repeats--cut-a-repeat-a-second-explanation-or-filler-when-the-article-reads-better-without-it); [Emulate is no longer used on his writing](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-emulate-retired--emulate-is-no-longer-used-on-his-writing)

## LEFTOVERS. Three leftovers that contradict newer text

- **His answer:** approved
- **Now in the tree as:** [Suggestions go to him on a marking page](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-marking-page--suggestions-go-to-him-on-a-marking-page); [The old gate is history](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/rules/TREE.md#r-old-gate-historical--the-old-gate-is-history)
