# Blind two-way preservation trace, section 2 (intentional communities)

## Method

- Opened only the original paste file and the 14 named rewrite files. The other files in the candidate folder (notes, build script, fixlog, owner-edits, the combined C-pair files, the assembled section files) were not opened; only a directory listing was taken.
- Completeness check: a word-level diff (Python difflib) of each rewrite against its matching original paragraph, run on those same named files. It surfaced nothing beyond what the read-through found.
- Marks. SAME = same wording (punctuation and case aside). SAME-MEANING = reworded, same meaning and strength. SHIFTED = meaning, scope, strength, voice or attribution changed. DROPPED = in the original, absent from the rewrite. ADDED = in the rewrite, absent from the original.
- Per the brief: no judgment of improvement, no suggested rewrites.

## Which original paragraph each file answers

| Rewrite file | Original paragraph (line in paste file) |
|---|---|
| C1a, C1b | line 3, "The longing that shaped my father's film ..." |
| C2 | line 5, "I'm less interested in declaring an official 'epidemic' ..." |
| C3 | line 7, "Look at Google Trends ..." |
| C4 | line 9, "I can't prove AI caused that turn ..." |
| none | line 11, "It's poppin' on Instagram too!" (unchanged, no rewrite file) |
| trace-C6 | line 13, "Another large influencer later floated the commune idea ..." |
| C7 | line 17, "Not everybody in the comments was trying to join ..." |
| trace-C8 | line 19, "The commune comments became a miniature political-philosophy seminar ..." |
| trace-C9a, trace-C9b | line 21, "Although that comment applies more to large socialism experiments ..." |
| C10 | line 23, "Communal ownership therefore needs ..." |
| C11a, C11b | line 25, "The desire to return to a natural way of living together ..." |
| C12 | line 27, "I'm not currently recruiting anyone ..." |

---

## C1a and C1b (original line 3)

Original: "The longing that shaped my father's film is suddenly everywhere again. The U.S. Surgeon General's 2023 advisory reported that roughly half of American adults experience loneliness and treated social connection as a public-health issue rather than a sentimental extra."

C1a: "The same longing that pushed my father to make that film is in the air again. In 2023, the U.S. Surgeon General's advisory reported that roughly half of American adults experience loneliness, and treated social connection as a public-health issue rather than a sentimental extra."

C1b: "The same longing that pushed my father to make that film is in the air again. In 2023, the U.S. Surgeon General's advisory reported that roughly half of American adults experience loneliness, and made social connection a public-health issue."

### Forward

| # | Original unit | C1a | C1b | What the rewrite does |
|---|---|---|---|---|
| 1 | "The longing that shaped my father's film": the longing influenced the film | SHIFTED | SHIFTED | Both: "The same longing that pushed my father to make that film". "shaped [the film]" (influence on the film) becomes "pushed my father to make" (motive for his making it); "my father's film" becomes "that film". |
| 2 | "suddenly" | DROPPED | DROPPED | Both: "is in the air again", no "suddenly". |
| 3 | "everywhere" (ubiquity) | SHIFTED | SHIFTED | Both: "in the air" (diffuse presence; the "everywhere" claim is gone). |
| 4 | "again" (it is a return) | SAME | SAME | Both keep "again" and add "same". |
| 5 | The U.S. Surgeon General's advisory (the source) | SAME | SAME | |
| 6 | "2023" dating the advisory | SAME-MEANING | SAME-MEANING | "2023 advisory" becomes "In 2023, the ... advisory reported"; same year, now attached to the reporting. |
| 7 | "reported that roughly half of American adults experience loneliness" | SAME | SAME | "roughly half" kept. |
| 8 | the advisory "treated social connection as a public-health issue" | SAME | SHIFTED | C1b: "made social connection a public-health issue"; "treated ... as" (regarded) becomes "made ... a" (turned it into). |
| 9 | "rather than a sentimental extra" | SAME | DROPPED | C1b stops at "public-health issue". |

### Reverse (ADDED)

- Both: "pushed my father to make that film". Gives the longing a motivating role in the father's decision to make the film. The original says it "shaped" the film.
- Both: "The same longing". "same" states identity with the earlier longing; the original carries it only through "again".
- Both: "in the air". New figure in place of "suddenly everywhere".
- C1b only: "made" (unit 8). The advisory is credited with making the issue, not treating it as one.

### Sources

- C1a: none. The advisory clause matches the original's claims word for word.
- C1b: "made social connection a public-health issue" against "treated social connection as a public-health issue rather than a sentimental extra". "made" credits the advisory with changing the issue's status instead of framing it, and the contrast "rather than a sentimental extra" is gone.

### Sense

- Both: "that film" has no antecedent inside the paragraph. The original identified the film through its maker ("my father's film").

---

## C2 (original line 5)

Original: "I'm less interested in declaring an official "epidemic" than in the obvious fact underneath it: a lot of people can't tolerate isolated modern life anymore. They may disagree about politics, food, God, sex, and whether shoes are oppressive, but they agree that something about the current arrangement is starving them."

C2: "Whether you want to call it an epidemic or not, it's obvious that a lot of people simply cannot tolerate modern life in isolation any more. This seems to be true regardless of politics, food, God, sex, or whether shoes are oppressive. People agree that the way things are now is starvin' them."

### Forward

| # | Original unit | Mark | What the rewrite does |
|---|---|---|---|
| 1 | "I'm less interested in ... than in ...": the author's stated priority, first person | DROPPED | No first-person stance. Replaced by "Whether you want to call it an epidemic or not", a concession addressed to the reader ("you"). |
| 2 | "declaring an official 'epidemic'" ("declaring", "official", scare quotes) | SHIFTED | "call it an epidemic": official declaring becomes casual naming; "official" and the quotation marks are gone; whether to use the label is now the reader's choice ("you want"). |
| 3 | "the obvious fact underneath it" | SAME-MEANING | "it's obvious that ...". "obvious" kept; "fact" and "underneath it" (the fact sits under the label) are not expressed. |
| 4 | "a lot of people" | SAME | |
| 5 | "can't tolerate" | SHIFTED | "simply cannot tolerate": "simply" adds force. |
| 6 | "isolated modern life" | SAME-MEANING | "modern life in isolation" (can also be read as "taken by itself"; see Sense). |
| 7 | "anymore" | SAME | "any more". |
| 8 | "They may disagree about politics, food, God, sex, and whether shoes are oppressive": people differ on these ("may") | SHIFTED | "This seems to be true regardless of politics, food, God, sex, or whether shoes are oppressive." The claim is now independent of the topics. The statement that they disagree is gone; "and" becomes "or". |
| 9 | the joke item "whether shoes are oppressive" | SAME | Kept. |
| 10 | "but they agree": contrast; "they" = the "lot of people" | SHIFTED | "People agree". "but" gone; "they" (that group) becomes bare "People" (reads as a wider group). |
| 11 | "something about the current arrangement": some aspect | SHIFTED | "the way things are now". "something about" (some aspect) is dropped, so the whole state of affairs is blamed; "current arrangement" becomes "the way things are now". |
| 12 | "is starving them" | SAME-MEANING | "is starvin' them" (respelled; register only). |

### Reverse (ADDED)

- "Whether you want to": addresses the reader.
- "simply": intensifier on "cannot".
- "seems to be true": a hedge the original does not put on the agreement claim.
- "the way things are now": a wider object of blame than "something about the current arrangement".
- "starvin'": dialect respelling (no change in meaning).

### Sources

- none (no source named in the paragraph).

### Sense

- "call it an epidemic": "it" has no antecedent inside the paragraph. The intended referent (loneliness) is in the previous paragraph, whose closing words are "a sentimental extra" (C1a) or "a public-health issue" (C1b).
- "This seems to be true regardless of politics, food, God, sex, or whether shoes are oppressive": reads as true regardless of the topics themselves. Nowhere does it say that people hold differing views on them; the reader has to infer it.
- "modern life in isolation": "in isolation" can be read as "alone" or as "considered by itself".
- "People agree ..." directly after "a lot of people": reads as a broader group than "a lot of people".

---

## C3 (original line 7)

Original: "Look at Google Trends for "ecovillage" and "intentional community." Interest had been drifting downward for years, then bent upward sharply in the mid-2020s."

C3: "If you look at Google Trends for terms like "ecovillage" or "intentional community", you can see that after a long decline in interest, the curve has bent upward dramatically in the mid-2020s."

### Forward

| # | Original unit | Mark | What the rewrite does |
|---|---|---|---|
| 1 | "Look at Google Trends" (an instruction to check the source) | SAME-MEANING | "If you look at Google Trends ... you can see that": the instruction becomes a conditional, and the claim becomes what the look shows. |
| 2 | "for "ecovillage" and "intentional community"": exactly two named search terms | SHIFTED | "terms like "ecovillage" or "intentional community"": the two terms become examples of a wider set; "and" becomes "or". |
| 3 | "Interest had been drifting downward" | SHIFTED | "a long decline in interest": "drifting downward" (gentle) becomes "decline". |
| 4 | "for years" | SAME-MEANING | "long" (the unit "years" is not stated). |
| 5 | "then bent upward" | SAME-MEANING | "the curve has bent upward": adds "the curve"; "bent" becomes "has bent". |
| 6 | "sharply" | SHIFTED | "dramatically" (a stronger intensity word). |
| 7 | "in the mid-2020s" | SAME | |

### Reverse (ADDED)

- "terms like": extends the claim to a class of terms beyond the two named.
- "you can see that": presents the whole characterization as what the tool displays.
- "the curve": new object.
- "dramatically": see unit 6.

### Sources (Google Trends)

- "terms like "ecovillage" or "intentional community"" against the original's two named terms: broader.
- "dramatically" against "sharply": stronger.
- "you can see that after a long decline ..., the curve has bent upward" against "Look at Google Trends ... Interest had been drifting downward for years, then bent upward sharply": the author's description is now attributed to what the tool shows.
- "a long decline" against "drifting downward for years": different characterization of the earlier trend.
- Quotation marks: the same two search terms are quoted; none added.

### Sense

- Minor: "has bent upward dramatically in the mid-2020s" puts a present perfect with a past-period phrase.

---

## C4 (original line 9)

Original: "I can't prove AI caused that turn. The timing is still hard to ignore. Around the same period, AI stopped being a tech-news curiosity and began reorganizing people's jobs, feeds, relationships, and expectations of the future. Suddenly "maybe we should form a village" sounded less like a 1972 leftover and more like a backup plan."

C4: "I have no proof that the rise of AI is connected to this uptick, but it's hard to ignore the coincidence in timing. AI became serious around this time, and now it's radically changing the way we live. Suddenly "maybe we should form a village" sounded less like a 1972 leftover and more like a backup plan."

### Forward

| # | Original unit | Mark | What the rewrite does |
|---|---|---|---|
| 1 | "I can't prove" | SAME-MEANING | "I have no proof that". |
| 2 | "AI caused that turn": the hypothesized relation is causation | SHIFTED | "the rise of AI is connected to this uptick". "caused" becomes "is connected to" (a weaker relation); "AI" becomes "the rise of AI"; "that turn" becomes "this uptick". |
| 3 | "The timing is still hard to ignore" | SHIFTED | "but it's hard to ignore the coincidence in timing". "still" becomes "but" (same meaning); "the timing" becomes "the coincidence in timing" (the timing is labelled a coincidence). Minor. |
| 4 | "Around the same period" | SAME-MEANING | "around this time". |
| 5 | "AI stopped being a tech-news curiosity" | SHIFTED | "AI became serious". The "tech-news curiosity" image is gone; "serious" is a different and vaguer claim. |
| 6 | "began reorganizing" (it began in that period) | SHIFTED | "now it's radically changing": "began" in that period becomes "now" (ongoing at present); "reorganizing" becomes "changing"; "radically" is added. |
| 7 | "people's jobs, feeds, relationships, and expectations of the future": four named areas | DROPPED | Replaced by "the way we live" (generic; "we" includes the author, where the original says "people's"). |
| 8 | "Suddenly "maybe we should form a village" sounded less like a 1972 leftover and more like a backup plan." | SAME | Verbatim. |

### Reverse (ADDED)

- "the rise of AI" and "is connected to": a different hypothesis than "AI caused".
- "uptick": a label for the movement, in place of "turn".
- "the coincidence in timing".
- "AI became serious".
- "now": a present-time claim.
- "radically": intensifier.
- "the way we live": generic scope, with "we".

### Sources (Google Trends)

- The movement is called "this uptick". The original calls it "that turn", directly after saying interest "bent upward sharply". Across the two rewrites the same movement is "dramatically" (C3) and an "uptick" (C4).

### Sense

- Tense: "now it's radically changing the way we live. Suddenly "maybe we should form a village" sounded ..." goes from present to past.
- "AI became serious": it is not stated in what sense.
- "this time" and "this uptick": antecedents are in the previous paragraph (the mid-2020s curve), not in this one.

---

## trace-C6, the second influencer (original line 13)

Original: "Another large influencer later floated the commune idea, and the comments began turning into a recruitment board. People were finding prospective members under a post the way they might normally find a used sofa. It was chaotic, sincere, and revealing."

trace-C6: "Then another large influencer brought it up. People flooded the comments, essentially trying to find other people to join their communes, the way you'd normally find a second-hand sofa."

### Forward

| # | Original unit | Mark | What the rewrite does |
|---|---|---|---|
| 1 | "Another large influencer" | SAME | |
| 2 | "later" | SAME-MEANING | "Then". |
| 3 | "floated the commune idea": a tentative proposal, with the idea named | SHIFTED | "brought it up". "floated" becomes "brought up" (tentativeness not carried); "the commune idea" becomes "it". |
| 4 | "the comments began turning into a recruitment board": a gradual change, as a metaphor | SHIFTED | "People flooded the comments". "began turning into" (in progress) becomes "flooded" (a surge in volume); the "recruitment board" metaphor is gone, its sense carried by the next clause. |
| 5 | "People were finding prospective members under a post" | SHIFTED | "essentially trying to find other people to join their communes". "were finding" (it was happening) becomes "trying to find" (an attempt); "prospective members" becomes "other people to join their communes"; "under a post" becomes "the comments". |
| 6 | "the way they might normally find a used sofa": the simile | SAME-MEANING | "the way you'd normally find a second-hand sofa". "they might" becomes "you'd" (the hedge "might" is not carried; "they" becomes generic "you"); "used" becomes "second-hand". |
| 7 | "It was chaotic, sincere, and revealing." (the author's evaluation, three adjectives) | DROPPED | Absent. No file in the set of 14 carries it. |

### Reverse (ADDED)

- "flooded": a volume claim.
- "essentially": a hedge on the characterization.
- "their communes": the commenters are described as having communes of their own, plural.
- generic "you".

### Sources

- Influencer's post: "brought it up" against "floated the commune idea". Different, and weaker on how tentative the proposal was; the thing raised is not named.
- Commenters: "People flooded the comments" is stronger than "the comments began turning into a recruitment board", which gives no volume.
- Commenters: "their communes" attributes ownership of communes to the commenters, which the original does not state.
- Commenters: "trying to find" is weaker than "were finding".
- No quotation marks added.

### Sense

- "brought it up": "it" has no antecedent inside the paragraph. The nearest nouns in the preceding unchanged paragraph are "a commune", "a village" and "a million followers"; the original named "the commune idea".

---

## C7, the oldest objection (original line 17)

Original: "Not everybody in the comments was trying to join. The oldest objection arrived almost immediately: maybe most people don't want the responsibility anarchism requires, and communal property becomes "owned by everyone, cared for by nobody.""

C7: "Not everyone commented with interest. The oldest response to this idea came up pretty quickly: the idea that maybe most people don't want the responsibility that would be required of them if we actually had a functioning anarchism where we could have true communal ownership of property. Communal property becomes "owned by everyone, cared for by nobody.""

### Forward

| # | Original unit | Mark | What the rewrite does |
|---|---|---|---|
| 1 | "Not everybody in the comments was trying to join." | SHIFTED | "Not everyone commented with interest." "was trying to join" (acting to join) becomes "commented with interest" (expressing interest); "in the comments" becomes "commented". |
| 2 | "The oldest objection" | SHIFTED | "The oldest response to this idea". "objection" (oppositional) becomes "response" (neutral); "to this idea" is added; "oldest" kept. |
| 3 | "arrived almost immediately" | SHIFTED | "came up pretty quickly" (weaker than "almost immediately"). |
| 4 | "maybe most people don't want the responsibility": both "maybe" and "most" | SAME | Kept: "the idea that maybe most people don't want the responsibility". |
| 5 | "anarchism requires" | SHIFTED | "that would be required of them if we actually had a functioning anarchism where we could have true communal ownership of property". A conditional ("if we actually had"), "functioning", "true communal ownership of property" (anarchism tied to communal ownership), "of them". |
| 6 | "and communal property becomes "owned by everyone, cared for by nobody."": the second half of the objection | SHIFTED | A standalone sentence, "Communal property becomes "owned by everyone, cared for by nobody."" No longer inside "maybe ...", no longer tied to the objection. The quoted phrase itself is unchanged. |

### Reverse (ADDED)

- "to this idea".
- "pretty quickly" (weaker than the original's timing).
- "if we actually had a functioning anarchism".
- "true communal ownership of property".
- "required of them".
- The standalone, unhedged sentence "Communal property becomes ...".

### Sources (the commenter)

- The objection's content is enlarged with a definition and a counterfactual ("if we actually had a functioning anarchism where we could have true communal ownership of property"), which the original does not report.
- "Communal property becomes "owned by everyone, cared for by nobody."" now stands outside the objection and outside "maybe". It reads as a flat claim, and the quotation marks no longer sit inside the commenter's objection.
- "response" against "objection", "pretty quickly" against "almost immediately", "commented with interest" against "was trying to join": each states the commenters' behavior differently (see units 1 to 3).

### Sense

- "this idea": no antecedent inside the paragraph.
- "this idea" and then "the idea that maybe ...": two different referents in successive sentences.
- "Communal property becomes ...": whose voice it is (the commenter's or the author's) is unclear.
- "The oldest response ... came up pretty quickly": "oldest" can read as "first in the thread" or "longest-standing". The original's "oldest objection" carries the same ambiguity; "response" no longer signals opposition until the clause after the colon.
- The long conditional "the responsibility that would be required of them if we actually had a functioning anarchism where we could have true communal ownership of property" is dense.

---

## trace-C8, the political philosophy line (original line 19)

Original: "The commune comments became a miniature political-philosophy seminar, as Instagram comments sometimes do."

trace-C8: "This led to some interesting comment-thread discussions about political philosophy, which you don't normally find on Instagram."

### Forward

| # | Original unit | Mark | What the rewrite does |
|---|---|---|---|
| 1 | "The commune comments" as the subject; "became" | SHIFTED | "This led to some ... comment-thread discussions". The subject is replaced by "This"; "commune" is not stated; "some" narrows the whole set of comments to some discussions; "became" becomes "led to". |
| 2 | "a miniature political-philosophy seminar": a joke metaphor, with "miniature" | SHIFTED | "discussions about political philosophy": the metaphor and "miniature" are gone, replaced by a literal description. |
| 3 | "as Instagram comments sometimes do": an aside that this sometimes happens on Instagram | SHIFTED | "which you don't normally find on Instagram": the claim about Instagram reverses, from "happens sometimes" to "not normally found". |

### Reverse (ADDED)

- "This led to": a causal link to something unnamed.
- "interesting": an evaluation attributed to the author. The original's evaluation is the joke "miniature ... seminar".
- "which you don't normally find on Instagram": a new claim about Instagram.
- generic "you".

### Sources (comment threads and commenters)

- "interesting" against the original's joke.
- "This led to" gives the discussions a cause the original does not state.
- "which you don't normally find on Instagram" against "as Instagram comments sometimes do": opposite emphasis about Instagram comments.

### Sense

- "This led to ...": "This" has no clear antecedent (the objection? the flood of recruiters? the influencer's post?).
- Cross-file: the next paragraph (C9) says "this comment", and this paragraph ends on "comment-thread discussions", which makes C9's referent harder to pin down.

---

## trace-C9a and trace-C9b (original line 21)

Original: "Although that comment applies more to large socialism experiments than small communes, that objection deserves a serious answer. Some people really would rather let somebody else take responsibility. Shared ownership can blur responsibility until the same three people maintain everything while everybody else discusses freedom. Informal leaders then gain power partly because everyone keeps handing it to them."

trace-C9a: "While this comment is more applicable to large-scale experiments in socialism than to small communes, it's worth responding to anyway, as some people just prefer not to be responsible. Shared ownership can blur responsibility until the same three people maintain everything while everybody else discusses freedom. Informal leaders then gain power partly because everyone keeps handing it to them."

trace-C9b: "While this comment is more applicable to large-scale experiments in socialism than to small communes, it's worth responding to anyway, as some people just prefer not to be responsible. Shared ownership can blur responsibility until the same three people maintain everything while everybody else discusses freedom, and those few end up as the de facto leaders, partly because everyone else keeps handing them the job."

### Forward

| # | Original unit | C9a | C9b | What the rewrite does |
|---|---|---|---|---|
| 1 | "Although that comment" | SAME-MEANING | SAME-MEANING | "While this comment": "Although" becomes "While"; "that" becomes "this". |
| 2 | "applies more to large socialism experiments than small communes" | SAME-MEANING | SAME-MEANING | "is more applicable to large-scale experiments in socialism than to small communes". |
| 3 | "that objection deserves a serious answer" | SHIFTED | SHIFTED | "it's worth responding to anyway". "deserves a serious answer" becomes "worth responding to" (weaker; "serious" gone); "that objection" becomes "it"; "anyway" is added. |
| 4 | "Some people really would rather let somebody else take responsibility." ("Some"; "really") | SHIFTED | SHIFTED | "as some people just prefer not to be responsible". "really" becomes "just"; "let somebody else take responsibility" becomes "not to be responsible" (the handing-off to someone else is gone); the statement becomes a reason clause introduced by "as". |
| 5 | "Shared ownership can blur responsibility until the same three people maintain everything while everybody else discusses freedom." | SAME | SAME | Verbatim in both. In C9b it is joined to the next unit with ", and". |
| 6 | "Informal leaders" | SAME | SHIFTED | C9b: "those few ... the de facto leaders". "informal" becomes "de facto" (same meaning); the identity of the leaders with the three people is now stated outright. |
| 7 | "then gain power" | SAME | SHIFTED | C9b: "end up as the de facto leaders". "then" is gone; "gain power" becomes "end up as ... leaders" ("power" is not stated). |
| 8 | "partly because" | SAME | SAME | Kept in both. |
| 9 | "everyone keeps handing it to them" ("it" = power) | SAME | SHIFTED | C9b: "everyone else keeps handing them the job". "it" (power) becomes "the job"; "everyone" becomes "everyone else". |

### Reverse (ADDED)

- Both: "anyway"; "as" (a stated reason); "just".
- C9b only: "those few"; "de facto"; "else"; "the job". The three maintainers are now said to be the leaders, and what is handed to them is "the job" instead of power.

### Sources

- Both: the commenter's claim ("applies more to large socialism experiments than small communes") is reported the same way. No flag on what the comment is said to claim.
- Both: the author's valuation of the comment is stated differently: "worth responding to anyway" against "deserves a serious answer" (weaker, not stronger).
- No quotation marks added.

### Sense

- Both: "this comment" has no clear single referent. C7 introduces the objection as "response" and "idea", not "comment"; the paragraph just before (C8) ends on "comment-thread discussions". In the original, "that objection" in the same sentence helps match "comment" to the objection; in the rewrite "it's worth responding to" does not.
- C9b only: "handing them the job": "the job" could be maintaining everything or being the leader.

---

## C10 (original line 23)

Original: "Communal ownership therefore needs named stewardship, visible duties, consequences for chronic freeloading, and enough relational capacity to confront the problem before resentment becomes the real government. A community cannot run on the assumption that removing bosses removes passivity, selfishness, theft, or learned helplessness."

C10: "Communal ownership needs named stewardship and visible duties, and consequences for chronic freeloading. It also needs enough relational capacity to confront the problem before resentment becomes the real government. It's naive to think that simply eliminating the possibility of having a "boss" will eliminate the potential for people to be passive, selfish or thieving, or to fall into learned helplessness."

### Forward

| # | Original unit | Mark | What the rewrite does |
|---|---|---|---|
| 1 | "therefore": the inference from the previous paragraph | DROPPED | Not carried. |
| 2 | "Communal ownership ... needs" | SAME | |
| 3 | "named stewardship" | SAME | |
| 4 | "visible duties" | SAME | |
| 5 | "consequences for chronic freeloading" | SAME | |
| 6 | "enough relational capacity to confront the problem before resentment becomes the real government" | SAME | "It also needs enough relational capacity ..." ("also" added; split into its own sentence). |
| 7 | "A community cannot run on the assumption that": a claim about what a community can't do | SHIFTED | "It's naive to think that": a claim of impossibility becomes an evaluative judgment ("naive") on people who think so. |
| 8 | "removing bosses" | SHIFTED | "simply eliminating the possibility of having a "boss"". "simply" is added; removing bosses becomes eliminating the possibility of having one; "boss" is put in quotation marks. |
| 9 | "removes passivity, selfishness, theft, or learned helplessness" | SHIFTED | "will eliminate the potential for people to be passive, selfish or thieving, or to fall into learned helplessness". The traits removed become "the potential" for them; "will" is added; "theft" becomes "thieving"; "to fall into" is added. All four items are kept. |

### Reverse (ADDED)

- "naive" (a judgment on holders of the assumption).
- "simply".
- "the possibility of having a "boss"" and "the potential for" (a second layer of possibility).
- "will".
- Quotation marks around "boss".
- "also".

### Sources

- No source claims in this paragraph. New quotation marks appear around "boss"; the original has none, and they are not attributed to anyone.

### Sense

- "the problem" now sits in a different sentence from "chronic freeloading", with "It also needs" between.
- "eliminating the possibility ... will eliminate the potential": two abstractions stacked.

---

## C11a and C11b (original line 25)

Original: "The desire to return to a natural way of living together has outrun the knowledge. People know they're lonely and exhausted. They usually don't know why so many earlier communities failed, why the same conflicts keep returning, or how quickly beautiful land becomes irrelevant once money, children, jealousy, and ownership enter the picture."

C11a: "Another problem is that the desire to go back to a more "natural" way of living together has outstripped people's knowledge of how to actually do it. People know they're lonely and exhausted. Most don't know why past attempts have failed, or why the same conflicts keep coming back, or how quickly beautiful land stops mattering once money, kids, jealousy and questions about ownership come into the mix."

C11b: "Another problem is that the desire to go back to a more "natural" way of living together has outstripped people's knowledge of how to actually do it. People know they're lonely and exhausted. Most don't know why past attempts have failed, or why the same conflicts keep coming back. They don't see how quickly beautiful land stops mattering once money, kids, jealousy and ownership come into it."

### Forward

| # | Original unit | C11a | C11b | What the rewrite does |
|---|---|---|---|---|
| 1 | "The desire ... has outrun the knowledge": a plain statement, no valence | SAME-MEANING | SAME-MEANING | The claim itself carries over. Both open "Another problem is that ...", which labels it a problem and places it in a series; that framing is not in the original (listed under ADDED). |
| 2 | "return to" | SAME-MEANING | SAME-MEANING | "go back to". |
| 3 | "a natural way of living together", with "natural" unquoted | SHIFTED | SHIFTED | "a more "natural" way of living together". "more" is added and "natural" goes into quotation marks, so the author asserts it less directly. |
| 4 | "has outrun the knowledge" | SAME-MEANING | SAME-MEANING | "has outstripped people's knowledge of how to actually do it". The knowledge is specified (whose, and of what). |
| 5 | "People know they're lonely and exhausted." | SAME | SAME | Verbatim. |
| 6 | "They usually don't know": a frequency qualifier | SHIFTED | SHIFTED | "Most don't know". "usually" (how often) becomes "Most" (how many people). Close, not identical. |
| 7 | "why so many earlier communities failed" | SHIFTED | SHIFTED | "why past attempts have failed". "so many" is DROPPED; "earlier communities" becomes "past attempts" (same meaning); "failed" becomes "have failed". |
| 8 | "why the same conflicts keep returning" | SAME-MEANING | SAME-MEANING | "keep coming back". |
| 9 | "how quickly beautiful land becomes irrelevant" | SAME-MEANING | SHIFTED | C11a: "how quickly beautiful land stops mattering", inside the same list under "Most don't know". C11b: a separate sentence, "They don't see how quickly beautiful land stops mattering". "usually"/"Most" does not reach it, "know" becomes "see", and "They" has two possible referents. |
| 10 | "money, children, jealousy, and ownership" | SHIFTED | SAME-MEANING | "children" becomes "kids" (both). C11a: "ownership" becomes "questions about ownership". C11b keeps "ownership". |
| 11 | "enter the picture" | SAME-MEANING | SAME-MEANING | C11a: "come into the mix". C11b: "come into it". |

### Reverse (ADDED)

- Both: "Another problem is that" (a label and a series position).
- Both: "more" and the quotation marks around "natural".
- Both: "people's" and "of how to actually do it".
- C11a only: "questions about" (before "ownership").
- C11b only: "They don't see" as a new sentence with no frequency qualifier.

### Sources

- No named sources. New quotation marks around "natural" in both; the original does not quote it, and the quotes suggest it is somebody's term.

### Sense

- Both: "past attempts": attempts at what is not stated (the reader has to take it from "how to actually do it"). "more "natural"": no comparison term.
- C11b: "They don't see ...": "They" could be "People" (everyone) or "Most".
- C11b: "come into it": "it" has no clear referent (the land? the situation?).

---

## C12 (original line 27)

Original: "I'm not currently recruiting anyone or founding a community. That makes this easier to write because I'm not trying to get you onto my land. I do plan to buy land, and people may naturally end up living around me. Every warning in this article applies to me too."

C12: "I am not currently recruiting for a community or attempting to start one, which makes it easier for me to write an article like this, since I'm not trying to get you onto my land. I do plan to buy land, and people may naturally end up living near me. But all of the warnings in this article apply to me, too."

### Forward

| # | Original unit | Mark | What the rewrite does |
|---|---|---|---|
| 1 | "not currently recruiting anyone" | SHIFTED | "not currently recruiting for a community". The object narrows from "anyone" to recruiting for a community. |
| 2 | "or founding a community" | SAME-MEANING | "or attempting to start one" ("attempting" added). |
| 3 | "That makes this easier to write" | SAME-MEANING | "which makes it easier for me to write an article like this". "this" (this article) becomes "an article like this"; "for me" is added. |
| 4 | "because I'm not trying to get you onto my land" | SAME | "since": "because" becomes "since" (same meaning). |
| 5 | "I do plan to buy land" | SAME | |
| 6 | "people may naturally end up living around me" ("may"; "naturally") | SHIFTED | "living near me". "around" becomes "near". Minor. "may" and "naturally" kept. |
| 7 | "Every warning in this article applies to me too." | SAME-MEANING | "all of the warnings in this article apply to me, too". "Every" becomes "all of the"; "But" is added. |

### Reverse (ADDED)

- "attempting".
- "for me".
- "an article like this".
- "But" (a contrast marker).
- "near" (in place of "around").

### Sources

- none.

### Sense

- none.
