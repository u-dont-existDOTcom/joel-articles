# Abstract agents in sections 1–3 of the community essay

This sweeps sections 1–3 of `HUMANIZED-SO-FAR.md` for Joel's tell of 2026-10-02: an abstraction or feeling doing what a person does, as in “so the anger goes there”, which he fixed to “so the angry communard goes there”.

Test: the sentence describes something people do, and an abstract noun or feeling stands where they would be. Joel's words are the `joel` and `must_contain` text in `OWNER-EDITS.json`; “published” means close to `../original.md`; the rest is rewrite, traced in the s2 and s3 fix logs.

**Result: 5 instances, 1 worth fixing; 47 near misses.** A fix needs the paragraph's Pangram check and the preservation proof run again.

## Instances, strongest first

### 1. Fix: section 2, The Freeloader Problem, “Some of the commenters weren’t trying”

> The oldest objection, that maybe most people don’t want to take on the responsibility that anarchism requires and communal property becomes “owned by everyone, cared for by nobody,” showed up almost right away.

- **Agent and verb:** the objection *showed up*, on a timetable.
- **Who:** a rewrite: draft U3w3 of writers round 1 (“fresh Opus writers”), plus “that” (`s2/fixlog-v3.json`, C7b). It isn't in OWNER-EDITS. The published text has the same agent: “The oldest objection arrived almost immediately”.
- **Fix** (*they* are the commenters of the sentence before):

> Almost right away, they brought up the oldest objection, that maybe most people don’t want to take on the responsibility that anarchism requires and communal property becomes “owned by everyone, cared for by nobody.”

- **Opinion: fix.** It makes the anger sentence's move: the commenters drop out and their objection turns up on its own. The fix keeps who raised it and how fast, and closes the 25-word gap between subject and verb. Check it with the paragraph before on Pangram: on 10-01 a split of this sentence turned that pair 100% AI (`s2/r4/C6-C7fix.txt`).

### 2. Leave: section 3, The spiritual failure, “The Farm, in Tennessee, at”

> But in the early days, the community’s spirituality and social life followed the founder, Stephen Gaskin.

- **Agent and verb:** spirituality and social life *followed* a man.
- **Who:** Joel: the `joel` text and `must_contain` of s3-p6 (10-02, 00:52), where he wrote “followed the founder” over “was heavily influenced by”. The abstract subject was Emulate's (“revolved around”, `s3/r1/P6a.txt`).
- **Fix:** “the community followed the founder, Stephen Gaskin, in its spirituality and social life.”
- **Opinion: leave.** These are Joel's own words, from the same pass as the rule. *Followed* reads mostly as “took its lead from”, so few readers will see two abstractions trailing a man.

### 3. Leave: section 3, The secular failure, “Meeting procedure isn’t going to”

> Meeting procedure isn’t going to solve every problem, … It can’t make it so that two people don’t hate each other. It can only make it so …

- **Agent and verb:** meeting procedure *solves*, then *makes it so* twice.
- **Who:** a rewrite: Emulate (e2-emuB) plus “any” and “whoever raises it” (`s3/fixlog-s3.json`, v5-P3B and v7-P3). The published paragraph has the same subject.
- **Fix:** “You aren’t going to solve every problem with meeting procedure, …”, plus “It can’t make” → “Procedure can’t make” in the next sentence so the pronoun keeps its referent.
- **Opinion: leave.** Procedure is a tool here, as in “money won’t fix it”, and the claim is what the tool can and can't do. The person version says the same thing in more words and needs a second edit.

### 4. Leave: section 1, “We spent a lot of”

> The money was opaque and seemed to travel mostly upward toward Love.

- **Agent and verb:** the money *travels* toward a person.
- **Who:** the published text, word for word.
- **Fix:** “The money was opaque, and Love seemed to end up with most of it.”
- **Opinion: leave.** The missing mover is the point: the money was opaque, so the sentence reports only where it seemed to go. Naming a mover would claim more than Joel saw, and the fix loses the pun on Love's name.

### 5. Leave: section 1, “Zendik went in the other”

> Apparently kindergarten had already failed to teach me labor consciousness.

- **Agent and verb:** kindergarten, an institution, *failed to teach*.
- **Who:** the published text, word for word.
- **Fix:** “Apparently my kindergarten teachers had already failed to teach me labor consciousness.”
- **Opinion: leave.** “School never taught me that” is an idiom nobody notices. The joke's target is the institution and the commune's jargon, and teachers as the subject would aim it at real people.

## Near misses

Closest to the line:

- **S3, “Eventually, when people are together”:** “politics will become a way of carrying emotional material that people can’t name”. A copula: the carrying has no stated subject, and the people are in the clause. Emulate's softening of the published “politics begins carrying”, a full instance. Joel left it on 10-02.
- **S3, “The secular communes had a”:** “when the deep waters of jealousy … came up”. *Come up* means arise, which feelings do; the image is water rising. Emulate.
- **S1, “I just put a movie”:** “years of work, traveling to all kinds of communes …, trying to answer a question that for him was primary”. Dangling participles with the father understood; “for him” keeps him in view. It shares the anger sentence's “trying to” shape, so if Joel wants his father in the grammar: “years of work” → “years of his work”. Emulate-based.
- **S1, “I spent much of my”:** “those years gave me a great sample to compare against”. *Give* means provide, as any experience does. Rewrite of the published “it gave me”.
- **S1, “Even at East Wind, though,”:** “a nut butter factory that brought in a lot of their income”. The business idiom. The published sentence gave this to the woman; the rewrite gave it to the factory, the reverse of Joel's fix, but she stays in as the one hard to question, so the claim holds.
- **S3, “The Farm, in Tennessee, at”:** “the community’s doctrine ran deep into members’ intimate decisions”. *Run deep* measures extent, as with rivers. Emulate's phrase, kept in Joel's pass; it replaced the published “doctrine reaching into”, an instance.
- **S1, “From 1999 to 2001, my”:** “civilization to be defeated by a two-digit date”. A passive, and the villainous date is the Y2K joke. Published.
- **S2, “Whether you want to call”:** “something about the current arrangement is starvin’ them”. Causal, as famines starve people; a person as subject would invent a culprit. Published.
- **S2, “I have no proof that”:** “the rise of AI caused this turn”, “it started changing people’s jobs”. Causal verbs, and AI is the one non-human here that acts. Joel ruled on this list (s2-c4-list).

One line each, by reason:

- **Copula:** “the longing behind my father’s movie is everywhere again”; “the comment section started to become a recruitment board”; “The feelings just became agenda items”; Joel's “The commune comments became a … seminar” (s2-c8).
- **Verbs any subject takes:** “the responsibility that anarchism requires”; Joel's “Communal ownership entails”, “It requires” and “taking away the idea of a boss does not make everyone less passive” (s2-c10); “All of the warnings in this article apply to me”; “This comes about when”; “The danger starts when”; Joel's “The two failures mirror each other”, “power concentrating around whoever defines the path” and “inner being shaped by outer” (s3-p7); “interest climbed sharply”, a line on a chart; “irritated by the cult programming”.
- **Dead idioms:** the heading “The New Age May Dawn Suddenly”; “the escuelita in my title comes in”; “that still goes on”; “the sort of thing that doesn’t make it into the history books” (Joel approved it on 09-30); “Looking back”; “went in the other direction”; “went wrong”; “Keep Dying”; Joel's “This is how it often goes”.
- **Money as a thing moved:** “income went into the common purse”, the stock phrase for income-sharing (published).
- **A group, organization or document standing for its people:** “a Christian community that doesn’t use money internally”; “the community provided what members needed”; “the U.S. antiwar movement … needed somebody”; “a nonprofit … publishing what it found”; “whose Escuelita brought outsiders into their communities” (its organizers are in the clause, as “whose”); “The secular communities often buried hurt”; “The spiritual communities often put one person in charge”; “The advisory said … and it treated social connection as a public-health issue”; “the community realizes … and then funnels it”; “the group lets you push”; Joel's “Secular groups distribute power” and “Spiritual groups attempt” (s3-p7).

## Context

The published sections had nine cases, among them “Human pain still entered the group”, “The desire … has outrun the knowledge” and “the real subject sits nearby with its arms crossed”. The rewrite keeps one (No. 1) and softens one (the politics sentence). Two removals put people back as subjects: “People brought the usual human pain and suffering with them” (a section 1 v3 fix) and Joel's own “People want to go back … but they have no idea why”.

The two clearest cases in the rewrite, No. 1 and the anger sentence Joel fixed, both came from the system's fresh writers (`s2/writers-r1/U3/w3.txt`, `s3/proposal/P4/w1.txt`), not from Emulate.
