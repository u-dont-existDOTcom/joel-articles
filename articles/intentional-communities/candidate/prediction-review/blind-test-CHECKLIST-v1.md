# What reads AI to Pangram: checklist v1 (from the section 9 and 10 misses only)

Pangram is an AI-text detector. For each text, decide whether it will come back **100% Human** ("Human") or not ("AI", which here also covers a mixed result). It reads the whole text; one small feature rarely decides it, but several together do. Speech markers ("Now,", "sure", "I'd like", "essentially", a parenthesis, "Yes.") do NOT cancel the signs below; several of them are signs themselves. Who wrote a text (a person, a model, an editor's fix) tells you nothing: read the words.

## Signs it will read AI (count them)

1. **Correction pairs.** "don't just/only X. Y too", "not only X but also Y", "X isn't what it's for. It's for Y", "The useful thing isn't X. It's Y", "and not just in theory". Example that read AI: "When two principles conflict, don't only store the final rule. Store the hard case itself, along with …"
2. **Self-answered questions.** "Do their communities use collective work …? Yes. But …", "So what do they show? That …".
3. **Concession pivots.** "X can make a community more capable, sure. But if …, it can also …"; "X, but it can also Y".
4. **Run-on lists.** A colon followed by four or more parallel items ("what happened, which principles were involved, what the first judgments were, …"), a list of three, or a list split into short sentences with the same subject ("They've set up … They run … They've also worked out …").
5. **Stock quips and set lines.** "another state, with a nicer logo", "a nice combination when you're trying to visit a revolution", an aphoristic closer ("Otherwise every generation gets to rediscover the same fight from scratch"), "the boring problem", "quietly turn into".
6. **Stock connectives and staging.** "One thing to notice about …", "It's also important to …", "I see the need to …", "Related to this, …", "One key to this whole thing", "we want to be …ing", "making sure that …".
7. **Abstract noun phrasing.** Nouns doing the work of verbs, with no person acting: "major necessities and public functions can be taken out of ordinary market purchase and governed collectively", "the movement of people and knowledge", "create gatekeepers and uneven dependence".
8. **Balanced pairs.** "help each other …, but also stay distinct enough that …", "X, and also keeps Y alive, so …".

## Signs it will read Human

1. Concrete first-person narrative with specific events, places and people ("We played basketball with Zapatista youth on an outdoor court. … I translated for my friends because my Spanish was better.") reads Human even with one formal phrase in it.
2. A list whose items are uneven and concrete ("a vehicle or a tool on loan, … a visit that's mainly for training or relationship building"), inside sentences of different shapes, can read Human.
3. A concrete sequence of steps ("inside the parent group first, then as a semi-autonomous project, and then … as a seed group nearby that still shares some tools, childcare, business or friendships") reads Human.
4. One sign word ("quietly") in otherwise specific prose doesn't flip it.

## Decide

- Two or more signs from the AI list → **AI**.
- One sign, and the text is general or argumentative (no concrete narrative or concrete items) → **AI**.
- No sign, or one sign inside concrete narrative or concrete items → **Human**.
- Near the line one word can flip a result, so when unsure, say **AI**: fewer than half of these texts came back 100% Human.
