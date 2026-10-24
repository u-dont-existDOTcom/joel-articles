# What turn 106's fixes and answers teach

Joel, 2026-10-24 22:55 UTC (`JOEL-20261024-2255.md`, beside this file): "i fixed the whole section and now it's 100% high conf human, learn some lessons", and "i hope you are always saving all our trials and errors so we can look back and see what actually works later, right? that's at least half the point of all this".

His five places read Human in his own checks: When to Change the Strategy, You Don't Need an Inner Monologue, the crisis stretch, First Social Connections, Done Right, and Speak Toward What You Are Building. Each one before and after is in `../t106-installs/OLD-SECTIONS.json` and `../t106-installs/HIS-SECTIONS.json`. What he changed, by kind:

## What his rewrites do

1. **A stuck paragraph's point goes into a neighbor.** 98.7 (a session goes well and nothing changes in your week) had used its six tries. He kept its point as an example inside the relief paragraph, "integrating the benefits into regular life (like texting a friend that you're having a rough day rather than saying you're fine)", and its own paragraph went.
2. **My quips and tidy closers go.** "(this article included)", "I'd take that!", "especially if you also slept well for once", "If it still says no, that's your answer.", "(nobody's taking attendance)", "Those aren't free, and you can't always take them back", and Speak Toward's whole last paragraph ("it seemed extra").
3. **His own humor and sayings come in.** "(so that you feel even more silly!?)", "the rest of the gang that shows up", "just like that Pink Elephant", "I'm giving you permission now to quit school and flunk the tests", "Curiosity killed the cat", "busy little bees", "60 YEARS", "'assume' makes an 'ass' out of 'u' and 'me'", "decide reparenting is a scam". They're silly, exaggerated or proverbial, never the knowing aside of item 2, and they're his to add. My rule stays: no wry humor of mine.
4. **Causes and options get named concretely.** "those weeks were mostly reading about it and getting ready, which can feel a lot like doing it" became "the strategy was not actually implemented, just read about or played around with lightly. Or there wasn't the right environment to really practice it, like no alone time." "Leaving? Quitting? Moving?" became "Leaving a relationship? Quitting a job?"
5. **"I'd" stays where it's his judgment, and an instruction is said plainly.** He kept "I'd want to quit too", "I'd borrow that grown-up first", "I'd change course sooner" and "I'd hear it out first". "Before either one, I'd look for what exactly is in the way" became "Before going with either of those paths, look for what exactly is in the way", and "I'd work on that one thing" became "it makes sense to work on that blocker". 98.7's d5, with its "I wouldn't" and "I'd guess", passed his check alone, and the same paragraph with them said flat had read 100% AI (`../t105-tries/REVIEWS.md`).
6. **"We" for the work the reader and he share.** "we still want to know if we are fixing the problem at a deeper level", "that's when we ask the Adult Protector to start paying attention", "we honestly label that as harm".
7. **A story only he has.** "like that guy who found me in a random park crying one time, and asked me "What's wrong?"" took the place of my "other people and things you have to do, and help when you reach for it".
8. **A question to the reader, and his own verdict.** "So, what would you tell my dad?", "might that be a double standard to look into?", "That sounds like a substantially worse deal to me."
9. **Qualifiers that cover every case go.** "I don't think any of it can tell you what dying will be like for you", "If a hospital held you against your will, or a treatment hurt you, no wonder asking for help feels scary.", "His point wasn't that dying is wonderful."
10. **Long paragraphs split, short sentences run in a row.** When to Change the Strategy's P4 became two paragraphs, and "Some things shift in a day. Others take about as long as learning guitar."

## My picks against his answers on the ideas page

- 28 of 33 reader's-edit items and 32 of 39 hedge items matched (`../t106-installs/PICKS-VS-ANSWERS.json`).
- 11 of the 12 misses were picks to keep something he then changed, and 8 of those were his own lines, kept because they were his or he had checked them (E10, E13, H2, H12, H18, H26, H31, H32). He judges his own lines on their merits: "wow i can't believe i wrote tha... oh that was from GPT, i humanized it but didn't notice how jarring that last stupid sentence was". The other three were headings I thought weren't needed (E9, E16) and a cut I thought was right (E1, below).
- Where he kept a line the readers flagged, it carried something: H1 "it isn't a hedge, it's a further understanding"; H4 "it wouldn't even make sense anymore after cutting that"; H5 "i wouldn't want someone to think the image is enough"; H10 "it's an objection that so many people have raised to me"; H11 "it's naming a massive religious movement of fakery that i might get lumped into"; H21 "people may not just listen to my commands, they have their own ideas"; H25 "cutting that could be sacriligeous"; H28 "people often do fight too many battles that's why i say when feasible"; H30 ""doesn't require" is vague, this clarifies that"; H37 "you should understand the diff between real info being conveyed and a generic takeback".
- Two of the reasons were wrong: my note on H14 ("it doesn't tell the reader the detective work can wait, that's what the prior sentence said") and the reader on H15 ("your reader needs fixing").
- E1: a heading has to cover everything under it. "One Grown-Up, Three Jobs" left out the Céline song and forced adulthood.

## What changes

- **E258 (Inner Child), in the gate:** my pick on one of his lines judges the line as I would judge mine. That it's his, or that he checked it, is a fact for the note, not a reason to keep it.
- **The hedge read's brief** keeps his reasons above as cases that stay (a further understanding, a word that clarifies a vague one, an objection people really raise, a movement the article could be lumped in with, a deliberate takeback because readers have their own ideas), and asks the reader to say what a line tells the reader before calling it a takeback.
- **The reader's edit brief:** a proposed heading names everything under it.
- **Folding a point (item 1)** goes into `docs/FIXING-AN-ARTICLE.md` as a step: when a paragraph of mine uses its tries, its one point can move into a neighbor as an example, before cutting it.

## Where the trials and errors are kept

Every Pangram check is kept: in `../../tools/pangram-ledger.jsonl`, with my prediction before it, the result, its link and, for a miss, my explanation, and for the early turns in `../../tools/PREDICTIONS.md` and `../../tools/pangram-runs/`. `../../tools/SCORECARD.md` is built from them. Each turn's drafts, tell panels, API batches and installs are in `tNNN-*` folders here, his messages word for word in `tNNN-answers/`, and the lessons in `docs/HUMANIZATION-GATE.md`. This file adds what his fixes changed and how my picks did against his answers.
