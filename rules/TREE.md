# The rule tree for Joel's articles, version 1 (2026-11-28)

Every rule the AI editor follows on Joel's articles, each said once, in the branch that says what it protects. Where an older file disagrees with this tree, the tree holds.

## 1 For the reader

Rules that make an article easy and worthwhile to read; they come before anything about Pangram.

### 1.1 Make sense

The reader always knows what is being said, why they are reading it, and how it follows.

#### R-gauge-audience | Gauge the audience: it decides how much to explain
- **Rule:** Before deciding how much to explain, gauge who the article is for, from the article and from where it will be published. Where it sets out to teach general readers (his posts), terms and the links the prose leaves unsaid are explained for someone who doesn't know the subject; a research paper for peer review, or a comment on a forum of people who know the field (SuttaCentral's, say), assumes what its readers know. How much to explain, gloss or unpack follows from that. Only if the article and its venue both leave it open is he asked, in the same message as the research question (R-studies-where-expected).
- **Why:** Joel, 2026-11-28: "for "explain for someone who doesn't know" that depends of course on the article. like if you already see in the article i'm trying to teach people about stuff, then that determines the level of explanation required. gauge the audience. if it's a research paper for peer review obv that's not the same audience right... if it's a comment on SuttaCentral forums obviously i'm not going to explain everything the way i would in my nibbana post for the general readers."
- **Checked by:** judgment; the audience is noted when work on an article begins.
- **Stages:** start, sense
- **Links:** comes before R-explain-hidden-links; comes before R-gloss; comes before R-unpack-lists; goes with R-studies-where-expected
- **Status:** active
- **Record:** 2026-11-28, his message of 15:23 UTC.

#### R-payoff-first | The reader knows early why they are reading this
- **Rule:** At each sentence and paragraph, ask whether the reader knows early why they are reading it, without having to reach the end. The ways he has done it (opening on the reader's own case, the deciding limit first, the purpose before the means) are examples to consider, not forms to require. He is not asked again what "payoff first" means.
- **Why:** Joel, 2026-11-04: "the fix was to give the reader payoff sooner so they understand why they should read ... we have to read all the way to the end of the sentence before we understand why we were reading the sentence ... how come i keep explaining this and you keep forgetting?" Joel, 2026-11-21: "my goal is to make it read well and lead on so i'm not wondering all the time why i am reading this"
- **Checked by:** judgment; the linter only points at candidates.
- **Stages:** sense, humanize
- **Links:** goes with R-connect; comes before R-reads-well-first
- **Replaces:** audit card C03; gates E357, E368, E369, E374; the receipt's "opens" refusal; lesson bad-trips-2026-11-19 (limit first); "The means before the payoff" in the fixes brief; AGENTS.md "The point comes first in every sentence and paragraph"; his saved preferences
- **Status:** active
- **Record:** 2026-11-28, audit card C03, approved, with his note: "yes and this also has to do usually with connections between sentences, paragraphs, ideas."

#### R-connect | Each sentence, paragraph and idea shows how it follows
- **Rule:** The reader sees early how a sentence follows from the one before, and how paragraphs and ideas connect; this is judged by reading, not by where a link word sits. A sentence that starts "In one trial on..." out of nowhere is the failure he keeps finding.
- **Why:** Joel, 2026-11-22: "S2 doesn't follow from S1 ... what's connecting them? even "So" would connect" Joel, 2026-11-28: "one classic fail eexample you keep making for some reason is a sentence that begins, "In one trial on.." like out of nowhere, totally unexpected. whenever i read AI articles people publish it always takes like so long for me to understand anything becauuse of how disconnected it all is"
- **Checked by:** judgment.
- **Stages:** sense, humanize
- **Links:** builds on R-payoff-first; goes with R-reads-well-first
- **Replaces:** audit cards C02, C03; the "first five words" test in the receipt tool; lesson bad-trips-2026-11-22 (ties)
- **Status:** active
- **Record:** 2026-11-28, audit card C03, approved, with his note (quoted above).

#### R-explain-hidden-links | Explain for the reader the article is written for
- **Rule:** Compressed text is explained to the level the article's audience needs (R-gauge-audience): for readers who don't know the subject, the links the prose leaves unsaid are spelled out. An expansion has to clarify; it never pads.
- **Why:** Joel, saved preference: "just explain stuff to someone who doesn't already know the hidden links in your prose's thinking" and "expand IN A CLARIFYING WAY, not just expanding with filler, everything should have a purpose ... clarity is paramount"
- **Checked by:** judgment.
- **Stages:** sense, humanize
- **Links:** builds on R-gauge-audience; goes with R-gloss; goes with R-unpack-lists
- **Replaces:** his saved preferences
- **Status:** active
- **Record:** his saved preference; 2026-11-28, made to depend on the audience (his message of 15:23 UTC).

#### R-accurate-word | The word that says exactly what the thing does
- **Rule:** Use the accurate, natural word for what something does or is, whether or not the passage already has that word. A vaguer word, or one whose everyday sense could send the reader elsewhere, is replaced. A word is not swapped for a paraphrase to get past Pangram.
- **Why:** Joel, 2026-11-27: "it's not about using the same word. it's about using a word that's accurate. didn't i explain that? "change" doesn't mean much. "improves" is not what smoothes means, it's more vague." Joel, 2026-11-05: "i felt the first way you statted it sounded like ai trying to bypass pangram with a paraphrase that looked strangely out of place"
- **Example:** before "improves the trip" / after "smooth the trip"; before "turned straight into" / after "converted into"; before "tone" / after "receptors"
- **Checked by:** judgment.
- **Stages:** sense, humanize
- **Links:** goes with R-clear-it; goes with R-lesson-reason-not-feature; goes with R-emphasis-only-where-called-for
- **Replaces:** audit cards S1, C14, C21; ways 10 and 30 of the fixes brief; "The plain word" in SKILL.md and AGENTS.md; the three-part first-fix declaration; lessons bad-trips-2026-11-27j and l, neuro-2026-11-26 (plain word)
- **Status:** active
- **Record:** 2026-11-28, audit cards S1 and C14, approved.

#### R-clear-it | "It" where it is clear, the name where it isn't
- **Rule:** Whether to keep "it" or name what it stands for depends on the context. Name it when the thing it stands for is too far back, or when something in between could be taken for it; otherwise "it" is fine.
- **Why:** Joel, 2026-11-28: "it's not that we always want to name what it stands for, it depends on the context. sometimes you want "it" and sometimes it's unclear what exactly it stands for either bc it was too late after the rferent or there were other things between the referent and it that it could stand for"
- **Example:** before "it" / after "honesty"; before "won't look" / after "won't look at the truth"
- **Checked by:** judgment.
- **Stages:** sense, humanize
- **Links:** builds on R-accurate-word
- **Replaces:** audit card S1; way 10 of the fixes brief; lesson romance-2026-11-23h
- **Status:** active
- **Record:** 2026-11-28, audit card S1, approved, with his note (quoted above).

#### R-gloss | Explain a term where the reader first needs it
- **Rule:** A term this article's reader may not know (R-gauge-audience) is explained where they first need it, in whatever form reads easily: inside the sentence, in a bracket, or in a sentence after. Don't explain what the words around it already say, and don't put an explanation on every name in a list.
- **Why:** Joel (old gate, no date recorded): "it's actually harder to read now with these 2 parentheticals. can you fix the reader?" Joel, 2026-11-26: "the main issues in your version were lack of explanation, connection, clarity"
- **Checked by:** judgment; no bracket count and no tool refusal.
- **Stages:** sense, humanize
- **Links:** builds on R-explain-hidden-links
- **Replaces:** audit card C24; gates E264, E342, E360; SKILL.md "Never a bare (X)"; "at most one per passage" in CLARITY-READ.md; lesson neuro-2026-11-25a
- **Status:** active
- **Record:** 2026-11-28, audit card C24, approved.

#### R-join-choppy | Join sentences only where the stretch reads choppy
- **Rule:** Sentences are joined where a stretch reads choppy and joining makes it flow; joining is not a step to perform on every passage, and a sentence may hold more than one step.
- **Why:** Joel, 2026-11-05: "i basically just joined sentences to make it read more flowy and natural"
- **Checked by:** judgment.
- **Stages:** humanize
- **Links:** goes with R-counts-send-to-read
- **Replaces:** audit card C14; "Short sentences that carry one thought are joined" in AGENTS.md; "One step a sentence" in MAKING-SENSE.md
- **Status:** active
- **Record:** 2026-11-28, audit card C14, approved.

#### R-quote-what-is-said | Quotation marks where a "said" word wouldn't parse without them
- **Rule:** Where what a person, a feeling or an inner voice "says" is a bare word or phrase, it goes in quotation marks, so the sentence parses for a reader.
- **Why:** Joel, saved preference: ""Unlovable" is what shame "says" ... if you just say "Shame says unlovable" it doesn't parse for humans at all"
- **Example:** before "Shame says unlovable" / after ""Unlovable" is what shame "says""
- **Checked by:** judgment.
- **Stages:** sense, humanize
- **Replaces:** his saved preferences
- **Status:** active
- **Record:** his saved preference; narrowed on 2026-11-28 to his point, that the sentence has to parse, after the rules check found "always" read wider than his one case.

#### R-fit-his-chat-words | What he says in chat is fitted to the article
- **Rule:** Something Joel says in chat is not pasted into an article as it is. Its thought is kept and written so it makes sense to a reader in that place.
- **Why:** Joel, saved preference: "you can't just take what i say to you and publish it. it has to make sense in context"
- **Checked by:** judgment.
- **Stages:** sense
- **Links:** goes with R-keep-what-he-meant
- **Replaces:** his saved preferences; AGENTS.md "Reader-facing realization gate"
- **Status:** active
- **Record:** his saved preference.

#### R-contradictions-check | Every article is checked for statements that can't both hold
- **Rule:** In every article a fresh reader lists the statements that contradict each other. Each one the text doesn't explain goes to Joel as a question.
- **Why:** Joel, 2026-11-20: "let's make the contradictions check a standard step in joel-articles (especially for clearly contradictory statements that aren't explained)"
- **Checked by:** a fresh reader, then judgment.
- **Stages:** sense
- **Links:** goes with R-ask-when-needed
- **Replaces:** gate neuro-2026-11-20a; FIXING-AN-ARTICLE.md section 5 item 5
- **Status:** active
- **Record:** unchanged.

#### R-close-read | A close word-by-word read for sense before a post
- **Rule:** Before an article goes into his post, every word is read for sense, to catch a real word standing where another belongs. An obvious wrong word is fixed and he is told; a word whose intended meaning is unclear goes to him. The read is tested with planted errors, as it is now.
- **Why:** Joel, 2026-11-03: "do we have more nonsense in here (from emulate i guess)? how are you not catching this?" and "make sure this closer reading is also part of the general joel-articles skill"
- **Example:** before "oily" / after "old"
- **Checked by:** judgment.
- **Stages:** sense, show
- **Links:** goes with R-his-own-text-stays
- **Replaces:** audit card C26; gate E331; SKILL.md "Word-for-sense read before publication"; his saved preferences
- **Status:** active
- **Record:** 2026-11-28, audit card C26, approved; then 2026-11-28, his answers on the open questions (15:23 UTC): approved (the planted-error test stays).

### 1.2 Say it once

Each point is made in one place, and what repeats or only fills space goes.

#### R-cut-repeats | Cut a repeat, a second explanation or filler when the article reads better without it
- **Rule:** A repeat, a second explanation of something already explained, or filler that a model drafted is cut when the article reads better without it, whatever Pangram says, and anything only that copy said moves to the place that stays. An example, a term's explanation or a reason that adds understanding stays, and so does a qualifier the claim needs. A sentence that seems to restate or reassure is read for what it does before it is called a repeat. A cut is made only when no important meaning is lost; a sentence that implies something the reader should do is completed, not cut. A Pangram result is never the reason for a cut; the one exception he allowed is a title like "Dr." dropped as a hack, last (R-hacks-last).
- **Why:** Joel, 2026-11-06: "make the cuts regardless of pangram if it makes the guide read better, that was what we were supposed to do already prior" Joel (old gate, no date recorded): "overcompletion is when you already have it explained and then you explain it again." and "as much as possible we should be deduplicating because i feel the article is really too redundant" Joel, 2026-10-17: "you can only cut if it isn't losing important meaning or there's no good way to merge"
- **Checked by:** judgment.
- **Stages:** sense, humanize
- **Links:** goes with R-cuts-shown; goes with R-never-cut-important; goes with R-link-not-repeat
- **Replaces:** audit cards C06, C29; gates E209, E210, E257, E260, E328, E378; lessons bad-trips-2026-11-06a, bad-trips-2026-11-11 (every other place goes); "each sentence they can lose goes" in AGENTS.md; "Cut a sentence that restates, sums up or reassures" in the old gate; "Cut the hedge or the filler sentence" in EMULATE-FALLBACK.md; the two "My pick" lines in CLARITY-READ.md; his saved preferences
- **Status:** active
- **Record:** 2026-11-28, audit cards C06 and C29, approved; the repeat rule and the overcompletion rule made one, as his note on C07 asks ("in general merge any rules that could be merged").

#### R-cuts-shown | Every cut or merge can be seen and put back
- **Rule:** Every cut or merge is listed with its before and after, so he can put one back. A cut to text he wrote himself, or to a warning or caution, is proposed to him on the marking page with the "after" already made; any other cut of a model's text is made and listed.
- **Why:** Joel, 2026-11-20: "don't cut "sensitivity varies" ... if it gives the reader nothing to do, we can explain they should try less at first"
- **Checked by:** judgment; the list of cuts is part of the turn's report.
- **Stages:** show, record
- **Links:** builds on R-cut-repeats; goes with R-after-shows-result; goes with R-few-cautions
- **Replaces:** audit card C06; "without a Pangram reason or a card" in FIXING-AN-ARTICLE.md; AGENTS.md "Treat deletions and consolidations as explicit proposals"
- **Status:** active
- **Record:** 2026-11-28, audit card C06, approved.

#### R-link-not-repeat | Point to the other section instead of saying it again
- **Rule:** While working, look for places where a section should call out and link to another one, so the article doesn't repeat itself. A subject already covered is not brought back needlessly: where it fits, what is said about it stays with its first mention.
- **Why:** Joel, saved preference: "you should always be looking to see whether a section should be calling out and linking to another one to avoid duplication, redundancy etc." Joel, 2026-11-23: "didn't you already mention magnesium? is there no way to keep it with the previous mention?"
- **Checked by:** judgment.
- **Stages:** sense
- **Links:** goes with R-anchor-links; goes with R-shared-links-and-passages
- **Replaces:** his saved preferences (second half); audit card C21; "everything about it goes with its first mention" in the fixes brief; lesson bad-trips-2026-11-23i
- **Status:** active
- **Record:** his saved preference; 2026-11-28, audit card C21, approved.

#### R-shared-links-and-passages | Across his Substack, one link per thing and one copy per shared passage
- **Rule:** Whenever an article mentions something he has a reference link for, it links that link; an article that mentions another of his articles links it, and where it speaks of one part of that article, it links that part (the section's anchor), asking him when unsure which part; a passage several articles share is kept once.
- **Why:** Joel, 2026-11-20: "anytime i mention it in any article you already know to link that one, or if any article mentions another, it links that, or if there are things that should be like snippets that are the same in different articles we can store them once rather than twice" Joel, 2026-11-28: "for linking to other substack posts, if i'm specifcally talkinbg about one part of it, link to that part that's relevant (ask if unsure)"
- **Checked by:** judgment.
- **Stages:** sense, record
- **Links:** goes with R-link-not-repeat; goes with R-anchor-links
- **Replaces:** his saved preferences
- **Status:** open question: he is still deciding on a system to track this across the Substack. Until then, the links he has named are used wherever their subject comes up.
- **Record:** his saved preference; 2026-11-28, links to the part meant (his message of 15:23 UTC).

### 1.3 Lists

When a list helps the reader and when it reads like a machine's.

#### R-lists-only-when-needed | A list only where one is really needed
- **Rule:** Prose is the default; a list is used where the content really is a list.
- **Why:** Joel (old gate, no date recorded): "try to avoid that unless it's really needed"
- **Checked by:** judgment.
- **Stages:** sense, humanize
- **Links:** comes before R-unpack-lists
- **Replaces:** audit card OLD-GATE; "Lists themselves are fine" in the old gate
- **Status:** active
- **Record:** 2026-11-28, audit card OLD-GATE, approved.

#### R-unpack-lists | Unpack a list where its audience needs each item explained
- **Rule:** Whether a list stays a list depends on its audience (R-gauge-audience). Where the reader needs to know how to act on each item, or may not know what an item means, each item is unpacked into a particular thing said to this reader. Where they only need the names (fifteen medicines to avoid), it stays a list; don't unpack every list as a routine. His two list paragraphs are examples, not a form.
- **Why:** Joel, 2026-11-07: "high conf human on first try. seems like you didn't even try to make it less like a massive robotic compressed list." Joel, 2026-11-28: "i wouldn't necessarily unpack every list robotically, that could be bloating things obviously like say we have a list of contraindications, we can list 15 meds and pangram is fine with that, no need to unpack each one, but if the list contains things that aren't so obvious and could use explaining, then that's part of the clarifying rule" and "re: compressed, that rule looks too general. it depends on the audience. does the audience need to know how to act on each item? then you can't just use a compressed list. do they know what the items mean? etc."
- **Checked by:** judgment.
- **Stages:** sense, humanize
- **Links:** builds on R-gauge-audience; builds on R-explain-hidden-links; goes with R-lists-not-overfull
- **Replaces:** audit card C13; lessons bad-trips-2026-11-07j, bad-trips-2026-11-12a and f; the list frames in SKILL.md and AGENTS.md; "these six come before any other rewrite"
- **Status:** active
- **Record:** 2026-11-28, audit card C13, approved, with his note (quoted above); made to depend on the audience by his message of 15:23 UTC.

#### R-lists-not-overfull | Don't fill a list to cover every hole
- **Rule:** An AI list tends to hold too much. Look for a balance: one word can sometimes say two items, and an item that is beside the point or explained elsewhere can go. What the reader has to check for themselves stays, "etc." only ends a run of examples of one thing, and a firm don't stays firm where someone could get hurt.
- **Why:** Joel, 2026-11-28: "in general AI tends to have too much in its lists, because it wants to cover every part of the advice and avoid holes in the argument. there should be some balance there. sometimes we can say two things with one word, or sometimes one part of the list is more tangential or it's already expalined elsewhere" Joel, 2026-11-12: "putting back the symptoms that don't overlap which you cut"
- **Checked by:** judgment.
- **Stages:** sense, humanize
- **Links:** goes with R-unpack-lists
- **Replaces:** audit card C13; "fewer reasons" in lesson bad-trips-2026-11-12a; lesson bad-trips-2026-11-12e
- **Status:** open question: what looks right in different kinds of list is still to be tested with him ("we can do some more testing on this to see what looks right in different cases"). Until then, each list is judged on its own.
- **Record:** 2026-11-28, audit card C13, approved, with his note (quoted above).

### 1.4 Cautions and safety

How few cautions an article carries, where they sit, and which ones stay.

#### R-few-cautions | Few cautions, each said once, none that treats the reader as an idiot
- **Rule:** A safety, caution or reassurance line stays only where it changes what the reader does there, isn't said elsewhere, and doesn't treat the reader as an idiot. Anything could hurt somebody, so "it could hurt" is never by itself a reason for a caution. Sometimes the cautions can sit together in one section instead of being repeated through the article. A caution that fails is proposed to him on the marking page, cut or moved to that section, with the "after" already made (R-cuts-shown).
- **Why:** Joel, 2026-10-23: "all the extra extra ridiculous safety language which gets repeated everywhere" Joel, 2026-11-28: "i'd like to be a bit more strict on the safety thing, in general we want to minimize the placement of caution statements -- sometimes we can just put all the cautions in one section rather than repeat them everywhere. there's always something that could hurt a reader. if i say drink water, that could hurt if they drink it wrong or too much, so we should question whether this caution statement is making the reader into an idiot." and "she said, "breathe in now, if it feels safe" -- i commented, "you mean it might be safer not to breathe in?" this kind of stuff is annoying as hell"
- **Checked by:** judgment.
- **Stages:** sense, humanize
- **Links:** goes with R-safe-word; goes with R-model-cautions-checked; goes with R-cut-repeats; goes with R-cuts-shown
- **Replaces:** audit card C08; gate E247; "Reassurance lines are content, not scaffolding" and "Safety lines ... are not boilerplate however generic" in FIXING-AN-ARTICLE.md; his saved preferences
- **Status:** active
- **Record:** 2026-11-28, audit card C08, to revise, written as his note says; the rule on few cautions and the idiot test made one rule.

#### R-safe-word | "Safe" has to be needed and clear
- **Rule:** Each time "safe" appears, check that it needs to be there and that it is clear what it refers to and how the reader would make sure of it. "If it's safe" is an AI tell.
- **Why:** Joel, 2026-11-11: "pretty much any time you see the word "safe" make sure it needs to be there and there's no ambiguitiy about what it's referring to or how one would ensure that"
- **Checked by:** the linter points at the word; judgment decides.
- **Stages:** sense, humanize
- **Links:** goes with R-few-cautions
- **Replaces:** his saved preferences; tell W127
- **Status:** active
- **Record:** his saved preference.

#### R-model-cautions-checked | A model's caution is checked against his words and its source
- **Rule:** A caution a model wrote is also checked against what Joel himself has said on the subject and against its source. He is asked only when it contradicts those; whether it could hurt someone is not the test (R-few-cautions).
- **Why:** Joel, 2026-11-25: "i do not recommend calling poison control to see about giving charcoal" Joel, 2026-11-28: "there's always something that could hurt a reader."
- **Checked by:** judgment.
- **Stages:** sense
- **Links:** goes with R-few-cautions; goes with R-ask-when-needed
- **Replaces:** audit card C08; "For each instruction in a caution ... ask on the card" in FIXING-AN-ARTICLE.md
- **Status:** active
- **Record:** 2026-11-28, audit card C08, to revise: the card's "or following it could hurt or confuse the reader" is dropped, as his note says.

#### R-his-warnings-stay | His harm-reduction warnings stay, by meaning and facts
- **Rule:** A warning Joel wrote against a dangerous combination stays in the article. Its words may change while the humanizing is done, as long as every fact stays: what, when, how much. Amounts he wrote stay, and the editor adds none. Where it repeats another of his warnings, moving it to one place or cutting the repeat is proposed to him (R-few-cautions).
- **Why:** Joel, 2026-10-11: "it's not instructions FOR mixing, it's instructions AGAINST a dangerous combo. That's called harm reduction." Joel, 2026-11-04: "8a not sure why you had to ask that, the whole point is rewording stuff here"
- **Checked by:** judgment.
- **Stages:** sense, humanize
- **Links:** goes with R-keep-what-he-meant; goes with R-few-cautions
- **Replaces:** audit cards C08, C10; gates E162, E358; "No drug amounts or recipes, even inside a warning" and "held word for word" in FIXING-AN-ARTICLE.md; his saved preferences
- **Status:** active
- **Record:** 2026-11-28, audit cards C08 (to revise) and C10 (approved); then 2026-11-28, his answers on the open questions (15:23 UTC): approved (no amounts added).

### 1.5 Evidence and sources

What an article claims, what backs it, and how much research it carries.

#### R-science-first | In a science article, get the science right before the wording
- **Rule:** Before a science article is humanized, its claims are checked, so the wording isn't worked on twice.
- **Why:** Joel (no date recorded): "the first thing before humanizing a science article is to make sure the science is right"
- **Checked by:** judgment.
- **Stages:** start, sense
- **Links:** comes before R-reads-well-first
- **Replaces:** audit card C19; lesson neuro-2026-11-07a (its card for every open flag is dropped)
- **Status:** active
- **Record:** 2026-11-28, audit card C19, approved.

#### R-claims-match-sources | No benefit or risk wider or vaguer than the sources show
- **Rule:** A benefit or a risk is stated no wider and no vaguer than its sources show. Where the evidence tells forms or doses apart, the form or dose is named.
- **Why:** Joel, 2026-11-08: "you can't say "they help some people" since you showed zero evidence that they do ... the fact that the VA recommends them is not science" Joel, 2026-11-20: "don't make it seem like niacin in general or "certain formulations" causes liver injury. that's not true."
- **Checked by:** judgment.
- **Stages:** sense
- **Links:** builds on R-science-first
- **Replaces:** audit card C19; lessons neuro-2026-11-08g ("only against placebo, harms beside it"), bad-trips-2026-11-20b ("from the study that compared them")
- **Status:** active
- **Record:** 2026-11-28, audit card C19, approved.

#### R-studies-where-expected | Cite a study only where the reader expects evidence, and ask at the start how much research the article carries
- **Rule:** Looking up a study to back a point can be good, but it looks odd where the reader wouldn't expect one. Add evidence where it fits the context, and ask Joel when that is unclear. When work on an article begins, ask him one plain question, how much research evidence goes in: none (his experience and reasoning carry it); a little, only where a reader would expect a source; or full citations for every claim of fact. The answer decides whether studies are looked up at all, and where.
- **Why:** Joel, 2026-11-28: "one thing i notice is you tend to try to look up studies to give evidence, which can be good, but sometimes it can look weird if that's not what the reader would expect there. so try to make sure that is appropriate in context and if unclear you can ask the author. probably also good at the beginning of any article to ask how much research evidence shoudl go into the article. you can brainstorm this also"
- **Checked by:** judgment.
- **Stages:** start, sense
- **Replaces:** audit card C19; gate E212 (now one case)
- **Status:** active
- **Record:** 2026-11-28, audit card C19, approved, with his note (quoted above); then 2026-11-28, his answers on the open questions (15:23 UTC): approved (the one question with three answers).

#### R-his-experience-stands | Once he says his experience stands, it is written as his
- **Rule:** When Joel says a point rests on his experience and stands, it is written as his, and no further source objection is sent on it.
- **Why:** Joel, 2026-11-24: "I don't care if the science isn't clear on this yet but I and everyone I know are totally clear about this."
- **Checked by:** judgment.
- **Stages:** sense, show
- **Links:** goes with R-claims-match-sources
- **Replaces:** audit card C19; lessons bad-trips-2026-11-24b and i
- **Status:** active
- **Record:** 2026-11-28, audit card C19, approved.

#### R-citations-not-assumed-cut | A missing citation isn't assumed cut on purpose
- **Rule:** A citation missing from his version stays out when it makes sense that he removed it or when nothing left rests on it; otherwise it goes back where its claim is, or he is asked.
- **Why:** Joel, 2026-11-06: "if it's not needed fine, if it is put it back ... don't assume a citation was removed on purpose unless it makes sense that it owuld be, ask the user if unsure"
- **Checked by:** judgment; the check of key facts warns when a citation's year is lost.
- **Stages:** sense, record
- **Links:** goes with R-keep-what-he-meant
- **Replaces:** gate E380; AGENTS.md "A citation missing from Joel's version"
- **Status:** active
- **Record:** 2026-11-28, audit card C19, approved (kept as it was).

### 1.6 Voice

What makes the prose sound like Joel and like a person.

#### R-human-tell | What counts as a human tell
- **Rule:** A human tell is something a model tends not to write. It comes from Joel's writing, from other human writing, or from a list of real human tells; a phrase any model writes isn't one, whoever wrote it.
- **Why:** Joel, 2026-11-26: "in general, if AI wrote it, it can't be a human tell, right? fix that rule... you could make a human tell if you have a list of real human tells or if you're copying from human writing perhaps" Joel, 2026-11-27: ""it's the same kind of thing" isn't a human tell, ai can write that also ... post-ashwa is a human tell bc ai doesn't tend to reduce the full name"
- **Checked by:** judgment.
- **Stages:** humanize, show
- **Links:** comes before R-human-tell-attempts
- **Replaces:** audit card C15; the four older definitions (budget file, old gate, tell panel, lesson neuro-2026-11-24); way 28's "what only he could" clause; "none of it is your own writing"
- **Status:** active
- **Record:** 2026-11-28, audit card C15, to revise, written as his note says.

#### R-human-tell-attempts | The editor tries human tells in the author's style, and the author approves them
- **Rule:** Copying the author's style, the editor tries to write human tells itself, from the author's own writing where there is some. Each one it makes up is a "human tell attempt", shown to the author on the marking page, until the author approves, rejects or changes it; only then does it count as a human tell. A tell taken from a real list of human tells counts as one already (R-human-tell). This is for better writing in any article where it fits (perhaps not an academic study); passing Pangram doesn't need it. He asked for it as a higher priority to develop.
- **Why:** Joel, 2026-11-28: "if the model wrote a human tell that comes from a legit list of human tells from human tells, then that would still bea  human tell. the model is also trying to copy the style of the author so it should be trying to create these human tells itself" and "should then be categorized as "human tell attempts" which the author would then approve reject or modify before they can be categorized as human tells. this should be higher priority to develop to better match the author's voice and make the prose sound more human"
- **Checked by:** Joel's answer on each attempt.
- **Stages:** humanize, show, record
- **Links:** builds on R-human-tell; goes with R-humor-lesson; goes with R-no-invented-life; goes with R-marking-page
- **Replaces:** audit card C15
- **Status:** to build, and of the things still to build it stays the higher priority (card C15). His fixes teach the Pangram rules first (R-his-kept-words-teach-pangram); his words are used now wherever the editor knows them, and he is asked once when to start building the attempts.
- **Record:** 2026-11-28, audit card C15, to revise, written as his note says.

#### R-humor-lesson | A lesson on writing more human jokes
- **Rule:** Joel and the editor do a lesson on making jokes that sound human, in the author's voice.
- **Why:** Joel, 2026-11-28: "i also wanted to help you make more human jokes, we never did that lesson, we should do that (of course trying to copy author's voice)"
- **Checked by:** Joel.
- **Stages:** humanize, record
- **Links:** goes with R-human-tell-attempts; goes with R-his-jokes-stay
- **Replaces:** audit card C29 (his note)
- **Status:** to build
- **Record:** 2026-11-28, audit card C29, approved, with his note (quoted above).

#### R-his-jokes-stay | His jokes stay unless he cuts them
- **Rule:** A joke of Joel's stays unless he cuts it. A line that only explains his joke, or only comments on the text, is offered to him as a cut on his page.
- **Why:** Joel, 2026-11-03: "that's the joke yeah you forgot."
- **Checked by:** judgment; the keep-as-is list.
- **Stages:** sense, humanize, show
- **Links:** goes with R-keep-as-is-list; goes with R-humor-lesson
- **Replaces:** audit card C29; "goes even when it's his joke" in CLARITY-READ.md
- **Status:** active
- **Record:** 2026-11-28, audit card C29, approved.

#### R-no-invented-life | Nothing is invented about his life, and no opinion is written as his
- **Rule:** In his voice, only life facts he has stated are used, and general advice is never told as his story. An opinion is never written as his unless he gave it; a joke or a human tell the editor writes in his voice is an attempt he approves (R-human-tell-attempts). A particular (a number, a place, a person, an exact detail) goes in only when the article or Joel supplies it. Where the reader needs one that isn't there, he is asked; he is never asked for one only to get past Pangram (R-no-lived-experience-needed).
- **Why:** Joel, saved preference: "don't confabulate things about my life" Joel (old gate, no date recorded): "debug that, stoop confabulating my life story. i didn't say that. it was general advice as per the guide."
- **Checked by:** judgment.
- **Stages:** humanize
- **Links:** goes with R-human-tell-attempts; goes with R-hacks-last; goes with R-no-lived-experience-needed
- **Replaces:** audit card C28; his saved preferences; gate E207; "give an example a number, a place or an oddly exact detail" in FIXING-AN-ARTICLE.md; "Name the person and the moment" and the fixed order of moves in the old gate
- **Status:** active
- **Record:** 2026-11-28, audit card C28, approved. The card's "Never write an opinion or a joke as yours" is kept for opinions; a joke in his voice goes to him as an attempt, after his notes on C15 and C29.

#### R-break-manual-march | A manual-like march is broken by making each point read well
- **Rule:** A stretch that marches like a manual is broken up by making each point read well, keeping every point; that also reads closer to the style he wants. A question or an exclamation goes in where the thought has one, never as a first move because such things have read Human.
- **Why:** Joel (old gate, no date recorded): "i had to do a lot of work breaking up the therapy manual style which pangram hates, but the point is, it also reads closer to the style I want anyway"
- **Checked by:** judgment.
- **Stages:** humanize
- **Links:** builds on R-reads-well-first; goes with R-human-tell-attempts
- **Replaces:** audit card OLD-GATE (cluster C33); "the first drafts use the moves that have read Human" and "Give a paragraph a clear break" in the old gate
- **Status:** active
- **Record:** 2026-11-28, audit card OLD-GATE, approved.

### 1.7 Headings and contents

Headings and the table of contents, read the way a reader scans them.

#### R-headings-answer-reader | A heading names what the reader is looking for
- **Rule:** A heading names the question, objection or curiosity its section answers for the reader scanning the contents; it is not a summary of the section. All headings follow one capitalization rule, title case.
- **Why:** Joel, saved preference: "we are thinking like the reader [...] wondering what question or objection or curiosity we are answering for them" and "Earning Trust, Day to Day should be title case... i mean, there should be a rule that the headings follow"
- **Checked by:** judgment; the heading-case tool warns.
- **Stages:** sense
- **Links:** goes with R-no-twin-headings
- **Replaces:** his saved preferences; the headings brief
- **Status:** active
- **Record:** his saved preference.

#### R-no-twin-headings | No two headings say the same thing, and twins are a sign to look at their sections
- **Rule:** No two headings in an article say or ask the same thing, ideally, wherever they sit; there may be exceptions. Two that do are a sign to read the prose of both sections: they may need merging, or one may be cut back and point to the other (R-link-not-repeat). Sameness is judged on meaning by a reader; a shared word only suggests pairs to look at.
- **Why:** Joel, 2026-11-21: "why would you put 2 serotonin syndrome headings in a row" Joel, 2026-11-28: "re: headings, really no two headings should say the same thing, ideally. there might be exceptions but in general i mean. that's also an indicator to check the prose in those sections to see if the sections should be merged or one should be reduced and point to the other or something like that."
- **Checked by:** the contents check lists candidates; a reader decides.
- **Stages:** sense
- **Links:** builds on R-headings-answer-reader; goes with R-link-not-repeat; goes with R-cut-repeats
- **Replaces:** audit card C25; the shared-word gate in the contents check; lesson bad-trips-2026-11-21 (headings)
- **Status:** active
- **Record:** 2026-11-28, audit card C25, approved; widened from "in a row" to the whole article by his message of 15:23 UTC.

#### R-contents-order | Sort the contents with his reasons, and show him the whole order once
- **Rule:** To reorder an article, first read the contents alone, then the guide and his answers for what each part holds. Ask him, in one message before sorting, only what those leave open. Sort with his heuristics and put the whole proposed order to him once, with a reason for each move and a pick. A section that moves gets its own Pangram check. Fresh readers are tested on the contents ("where would you look first?") only when he asks.
- **Why:** Joel, 2026-11-20: "i want to save those instructions in joel-articles repo so that next time you can do most of the work for me ... if unsure why i picked something you can ask me" Joel, 2026-11-21: "send me any qeustions that you can't find answered in the article"
- **Checked by:** judgment; Joel's answer on the proposed order.
- **Stages:** start, sense, show
- **Links:** goes with R-ask-when-needed; goes with R-anchor-links
- **Replaces:** audit card C16; the contents-order brief ("move by move", "ask him ... what each role and part holds", "needs no check"); gate E197; FIXING-AN-ARTICLE.md section 3 item 8
- **Status:** active
- **Record:** 2026-11-28, audit card C16, approved; then 2026-11-28, his answers on the open questions (15:23 UTC): approved (reader tests only when he asks).

#### R-text-under-link-heading | Text under a link heading gets a heading of its own in a contents proposal
- **Rule:** In a contents run, read what sits under each heading that is a link. Where text does, the proposal gives that text a heading of its own, keeps the link as a heading above it or as a plain line, and the readers test it; the heading goes on his picks page like every other, since headings are his to pick.
- **Checked by:** the readers' test of the contents.
- **Stages:** sense, show
- **Links:** builds on R-headings-answer-reader; goes with R-contents-order
- **Replaces:** lesson romance-2026-11-28a
- **Status:** active
- **Record:** 2026-11-28, lesson romance-2026-11-28a: the romance lane's own lesson from its readers (0 of 10 found the opening under the card-game link heading; 12 of 12 with a heading of its own), not from his words; his were "fix the ToC". One post so far.

#### R-anchor-links | Links to sections are catalogued and fixed when a heading changes
- **Rule:** Every link to a section of an article is catalogued, so a heading change fixes its links with no effort. A mention of a section links to it.
- **Why:** Joel, saved preference: "every time a heading changes, we have to fix the anchor links. make sure that's part of the protocol in joel-articles. so the anchor links should all be catalogued so this is automatic and easy."
- **Checked by:** the link tools warn about a broken section link.
- **Stages:** sense, record
- **Links:** goes with R-link-not-repeat
- **Replaces:** his saved preferences (first half); lesson toc-2026-11-23
- **Status:** active
- **Record:** his saved preference.

### 1.8 How his fixes differ from my drafts

The ways Joel's fixes read differently from the drafts he fixed, and how the editor uses them.

<!-- include: his_fixes_ways -->

#### R-read-against-his-fixes | The editor reads its own text against his fixes
- **Rule:** Before any check, the editor itself reads its text against his fixes: the ones in this article and any in the repository that could help in this context. A fresh reader before a text's first check is a help whose marks are each judged; it is not a gate rerun on every version. Any such reader runs on the lead's own model. A reading quiz without Pangram is offered only when the editor thinks it would help more than trying first through Pangram.
- **Why:** Joel, 2026-11-12: "have you systematically looked at all of the fixes i've shown you and what are the idfferences in how you write vs how i fix?" Joel, 2026-11-28: "and not just against my own fixes in that article of course but any fixes in the repo that could be useful for that context" and "and quizzes are only offered if you think they would be more helpful than trying first thru pangram"
- **Checked by:** judgment.
- **Stages:** sense, humanize, show
- **Links:** goes with R-fixes-searchable; goes with R-lesson-reason-not-feature; comes before R-reads-well-first
- **Replaces:** audit card C17; gates bad-trips-2026-11-12g, E294; "every sentence it marks is changed first" in AGENTS.md; "The fresh reads ... run again on each new version" in SKILL.md; lesson bad-trips-2026-11-21f
- **Status:** active
- **Record:** 2026-11-28, audit card C17, to revise, written as his note says.

#### R-fixes-searchable | His fixes are easy to search for the ones that could help
- **Rule:** His before-and-afters are kept in an index, one line each, saying what the passage lacked (from the ways his fixes differ from the editor's drafts) and what he did. Before the editor rewrites a passage, a reader picks from the index the fixes closest to it by meaning, and the editor reads those in full. A graph only if the index isn't enough.
- **Why:** Joel, 2026-11-28: "we should also try to make some kind of graph for the fixes so that it's easy to find which fixes might be most helpful, although maybe graph is the wrong approach, i'm not sure how to make the fixes searchable exactly."
- **Checked by:** nothing yet.
- **Stages:** humanize, record
- **Links:** goes with R-read-against-his-fixes; goes with R-mimic-pangram
- **Replaces:** audit card C17 (his note)
- **Status:** to build (the way he approved)
- **Record:** 2026-11-28, audit card C17, to revise, written as his note says; then 2026-11-28, his answers on the open questions (15:23 UTC): approved (the index).

## 2 His words and meaning

Rules that keep what Joel wrote, decided and meant.

### 2.1 Whose words

Which words are Joel's to keep and which are the editor's to fix.

#### R-model-text-is-mine | A model's text is the editor's to fix, even after he humanized it
- **Rule:** In an article a model drafted, the words are the model's unless they were his before the humanizing began. In wording he humanized himself, what he decided stays; the editor fixes the rest of that wording itself, tested, and it goes in like any tested change (R-tested-change-goes-in). He is asked only where the editor is unsure the fix still says what he was saying, or where a fix may only have made AI slop pass Pangram: passing that way is a sign the passage lacks the author's voice (R-slop-that-passed). It is never handed back to him as his words to fix.
- **Why:** Joel, 2026-11-06: "'my words' for an AI article, are not my words, unless those were human before we started humanizing ... otherwise it's AI words that i humanized" and "your job is to do the fixing, that's the whole point here" Joel, 2026-11-28: "right you only need to ask me if you're unsure if it still says what i was saying, OR if you think you might have just "fixed" some ai slop so it passes pangram, but it's an indicator that it lacks the author's voice."
- **Checked by:** judgment.
- **Stages:** humanize, show
- **Links:** goes with R-his-own-text-stays; goes with R-stuck-paragraph; goes with R-tested-change-goes-in; goes with R-slop-that-passed
- **Replaces:** audit cards C12, C26; gate E373; "words from his published text count as his even where an AI tool drafted them" in AGENTS.md and SKILL.md
- **Status:** active
- **Record:** 2026-11-28, audit card C12, approved; then 2026-11-28, his answers on the open questions (15:23 UTC): approved (a fix goes in and is reported), with his note.

#### R-his-own-text-stays | What he wrote himself stays, with obvious slips fixed
- **Rule:** Text Joel wrote himself stays. An obvious slip (a typo, a doubled word, a missing word) is fixed without asking; a word he invented is kept.
- **Why:** Joel, saved preference: "no need to ask me for obvious corrections" and "yes i know i invented a word, that's cool you can invent words for informal pieces like this if they sound right"
- **Checked by:** judgment.
- **Stages:** sense, humanize
- **Links:** goes with R-model-text-is-mine; goes with R-keep-as-is-list
- **Replaces:** audit card C12; his saved preferences; "goes to him with the smallest fix" in the old gate
- **Status:** active
- **Record:** 2026-11-28, audit card C12, approved.

#### R-keep-as-is-list | A lasting list of what he said stays as it is
- **Rule:** What Joel says stays as it is in an article (a joke, a chosen word, a cut he meant) goes on that article's keep-as-is list the turn he says it, and every pass reads the list before flagging anything. Only what he said goes on it; the editor's own guesses are notes that block nothing. A kept line readers can't follow is raised with him.
- **Why:** Joel, 2026-11-03: "i guess you need to somehow keep track of the jokes in an article more durably, add that as one of the rules in the repo, how to durably keep track of stuff you'd otherwise flag in an article"
- **Checked by:** the marking page blocks a card that changes kept words.
- **Stages:** start, show, record
- **Links:** goes with R-his-jokes-stay; goes with R-his-own-text-stays
- **Replaces:** audit card C12; gate E340; "my reading, not asked" entries; "never with a change" in lesson bad-trips-2026-11-25o; his saved preferences
- **Status:** active
- **Record:** 2026-11-28, audit card C12, approved.

### 2.2 Keep the meaning

The editor may change words; it may not change what he means.

#### R-never-cut-important | Never cut something important, or keep something unclear, to pass Pangram
- **Rule:** Nothing important is removed, and no version a reader can't follow is kept, to get a passage past Pangram. When the clear, faithful version reads AI, it stays, and the next try has to be clear, faithful and Human; the version a reader can't follow is never the fallback, nor the alternative offered to him. When no faithful version will pass, Joel gets the best faithful one and shows how to fix it.
- **Why:** Joel, saved preference: "from now on, never take out something important in order to pass pangram. give your best *faithful* version to me, i'll show you exactly how to fix it without doing that" Joel, 2026-10-29: "we never publish nonsense because it passes pangram. we come back and we try again if clarity loses on pangram." Joel, 2026-10-28: "the guide itself is now too incomprehensible, we went wrong somewhere"
- **Checked by:** judgment; the once-per-pass compare with his text (R-check-rewrite-once).
- **Stages:** sense, humanize, check
- **Links:** goes with R-stuck-paragraph; goes with R-check-rewrite-once; goes with R-hacks-last
- **Replaces:** his saved preferences; audit cards C22, C27; the old gate's loss rules; gates E284, E285, E291; AGENTS.md "Detector results are evidence, not editorial authority"
- **Status:** active
- **Record:** his saved preference; gates E284, E285 and E291 kept as they were. The rule against cutting and the rule against unclear versions made one on 2026-11-28 (his note on C07: "in general merge any rules that could be merged").

#### R-keep-what-he-meant | Keep the meaning, scope and condition he gave, not every word
- **Rule:** For each point of his, check that its sentence keeps the meaning, scope and condition he gave. Something relevant he said stays with his point, or has a reason to go, or he is asked when it's unclear whether it is relevant. A missing word is a lead to judge; it is not a failure in itself and is not put back by force.
- **Why:** Joel, 2026-11-27: "it's not that every word of my answer has to reach the sentence that says my point, but clearly if i'm saying something which is relevant and then you're removing that, you'd need to have a reason for removing it. if you're unsure, you'd ask." and "you forgot the most important part, sensitive skin... that's why i said under the armpits"
- **Checked by:** judgment; the tool only checks that a recorded drop has a reason.
- **Stages:** sense, humanize, record
- **Links:** goes with R-concept-word-stays; goes with R-fit-his-chat-words
- **Replaces:** audit cards S2, C10; "every word of four letters or more"; "A lost key word is restored, not outvoted"; gate E358; lessons bad-trips-2026-11-27k and m
- **Status:** active
- **Record:** 2026-11-28, audit cards S2 and C10, approved.

#### R-concept-word-stays | A word that names a concept isn't swapped for a different concept
- **Rule:** A concept word stays where another word would name a different concept. In his inner child writing, "protector" and "guard" are different terms. When he says to "smell" a remedy he means smell it, and the text must not let a reader think of snorting.
- **Why:** Joel, 2026-10-12: "we can't replace "dyads" with "romance" that's not the same concept" Joel, saved preference: "make sure we are not using "protector" to mean "guard"" and "NOT SNORTING IT, ppl keep thinking i mean snorting when i say smell"
- **Example:** before "romance" / after "dyads"
- **Checked by:** judgment.
- **Stages:** sense, humanize
- **Links:** builds on R-keep-what-he-meant
- **Replaces:** audit card C10; his saved preferences; gate E274 (protector and guard)
- **Status:** active
- **Record:** 2026-11-28, audit card C10, approved.

#### R-change-what-he-named | A content answer changes what he named
- **Rule:** When Joel answers on content, change what he named. Where his answer plainly contradicts another line of the same article, fix that too and tell him; but a change that adds or drops a drug, a caution, a dose or a source, or that changes an explanation he approved, is shown to him first. His answer is recorded for its article unless he says it is wider.
- **Why:** Joel, 2026-11-26: "i don't want to say never take 5-HTP with shrooms, that's up to them, and i don't think it shoul dbe a problem in this microdose protocol either"
- **Checked by:** judgment.
- **Stages:** sense, show, record
- **Links:** goes with R-approved-goes-in; goes with R-ask-when-needed
- **Replaces:** audit card C09; lessons neuro-2026-11-26 (cautions), neuro-2026-11-27 (everyday word), bad-trips-2026-11-23 (brand)
- **Status:** active
- **Record:** 2026-11-28, audit card C09, approved.

#### R-smaller-points-may-change | A smaller point may change if that helps the reader; the larger argument is his
- **Rule:** A supporting point that doesn't hold up or doesn't help the reader may be changed, after checking it against a source, and the change is explained to him. The larger argument is changed only by asking him.
- **Why:** Joel, 2026-11-04: "you are always totally free to change up what is being said if you can make it more helpful and clear ... obviously you wouldn't want to change the larger argument without asking, and if you do change the smaller points you'd explain to the author why"
- **Checked by:** judgment.
- **Stages:** sense, show
- **Links:** goes with R-claims-match-sources; goes with R-ask-when-needed
- **Replaces:** gates E344, E348; AGENTS.md "A supporting point that doesn't hold up"
- **Status:** active
- **Record:** unchanged.

#### R-check-rewrite-once | A rewrite of his sentences is compared with his text once per pass
- **Rule:** After a pass that rewrites his sentences (a humanizing pass, a reader's edit), a fresh reader reads the result beside his text once, sentence by sentence, at a size that fits the change, for every place it now reads worse: garbled, unclear, a point or a step lost, vaguer. Each such place is fixed or goes to him. The old per-edit ledgers, the fixed three writing rounds and the audit offers don't block work.
- **Why:** Joel, 2026-10-28: "the AI guide was making more sense by far" Joel, saved preference: "the point of this was that you would learn to do this better and quicker but it seems like it's getting slower"
- **Checked by:** a fresh reader, once per pass; the compare tool.
- **Stages:** humanize, check
- **Links:** builds on R-never-cut-important; goes with R-quicker-not-slower
- **Replaces:** audit card C27; AGENTS.md "After any rewrite of his sentences ... a fresh reader reads it beside his own text"; the compare read in FIXING-AN-ARTICLE.md section 5; the preservation gate, the architecture gate, the delivery gate, the cold-audit gate, the supervised-writing file's three iterations, the reader-question audit offers
- **Status:** active
- **Record:** 2026-11-28, audit card C27, approved, with his note: "some of this can be mergeed". The compare that two other rules each asked for is this one check. Then 2026-11-28, his answers on the open questions (15:23 UTC): approved, none of the old gates.

### 2.3 His changes and corrections

What the editor does when Joel changes or corrects something.

#### R-learn-from-his-changes | When he shows a change, fix the process that missed it
- **Rule:** When Joel shows a change and the editor agrees with it, the editor works out what the passage lacked (a named thing, the reason, the exact word) and fixes its own process so it could have made the change itself, apart from knowledge only he has. Where an edit of his is mixed, a fact only he has beside wording the editor could have fixed, the wording fix is learned from too (R-slop-that-passed).
- **Why:** Joel, saved preference: "it's a rule i hope that when i show you changes (and you agree) you need to fix yourself so you could have figured it out yourself (minus info you couldn't have, like my own experience)" Joel, 2026-11-03: "i'd like you to learn as much as possible from my edits and reorgs to see all the things you could have done yourself"
- **Checked by:** judgment; the lesson's test on his paragraphs.
- **Stages:** record
- **Links:** comes before R-lesson-tested; goes with R-lesson-reason-not-feature
- **Replaces:** his saved preferences; audit card C28
- **Status:** active
- **Record:** his saved preference.

#### R-his-kept-words-teach-pangram | When he keeps the editor's words, he is teaching Pangram, not his voice
- **Rule:** When Joel keeps the editor's words in a fix, that shows those words can pass Pangram; it doesn't show they match his voice. For now his fixes train the editor on what Pangram reads; using his words and idiosyncrasies would be better, and he sees that as the next training step, after the more important Pangram rules are down, since word choice can carry a passage past Pangram and hide a general rule it breaks. Where he has put his own words in and it is unclear which change moved the reading, and a lesson would rest on it, minimal pairs (one change per check) show what did what.
- **Why:** Joel, 2026-11-28: "regarding word choice, i notice i'm often trying to keep your words to show you that your words also can pass pangram, but that doesn't mean your word choice is matching my voice. so i'm training yoo to understand pangram at this point more than training you to write like me, so keep that in mind. if you used my words and idiosyncracies that would be better, but i'm thinking that is the next training step after we get the more important pangram rules down. because it's easy to overlook the general pangram rules otherwise as it might pass things just based on the word choice sometimes. sometimes i might be putting my words in rather than training you, in which case you might want to run some mimimal pairs to understand what did what."
- **Checked by:** judgment; minimal pairs in Pangram where a lesson rests on which of his changes moved the reading.
- **Stages:** humanize, record
- **Links:** goes with R-learn-from-his-changes; goes with R-lesson-reason-not-feature; comes before R-human-tell-attempts; comes before R-lesson-tested
- **Status:** active
- **Record:** 2026-11-28, his message of 15:23 UTC.

#### R-slop-that-passed | His edits of text that passed Pangram are kept and learned from
- **Rule:** Whenever Joel edits a section because it doesn't get his points across, the edit is recorded with the version he fixed and how it read in Pangram (docs/slop-that-passed/), and the editor works out, in specific terms, what that version lacked or did: his point missing, a description where the reader needed what to do, abstract or empty words, a tidy closer, a hedge that dilutes the point, a vague pointer, and so on. Each reason is the editor's reading until he confirms it. Text that reads Human High can still be AI slop; from these records the editor learns to see it before he does. An edit is put down to "what only he could add" only for the fact or story itself; whatever else the edit fixed is recorded as a fault the editor could have seen.
- **Why:** Joel, 2026-11-28: "i also want you to keep track of whenever i edit a section because it doesn't get my points across, try to develop some understanding of which sections might be ai slop even if they pass pangram high conf. you surely already have many of my edits like this saved but probably you haven't been using them if they didn't directly help with pangram, you prob just tagged them as "only author could do this" but should have tagged as "pangram passed ai slop" or whatever else you can figure out more specifically about why i might have edited it."
- **Checked by:** a fresh reader tags each edit; Joel confirms or corrects the reasons.
- **Stages:** sense, record
- **Links:** builds on R-learn-from-his-changes; goes with R-read-against-his-fixes; goes with R-fixes-searchable; goes with R-model-text-is-mine
- **Replaces:** the "only he could have known" tag in the old gate and the lessons (re-tagged 2026-11-28)
- **Status:** active
- **Record:** 2026-11-28, his note on the open questions (15:23 UTC); the record starts with his edit of the romance guide's "Things get tricky fast" and the re-tag of 27 places.

#### R-approved-goes-in | What he approved or agreed to is made at once
- **Rule:** A content change Joel approved goes into the article at once; humanizing the paragraph around it follows as its own work. A cut he agreed to is made.
- **Why:** Joel (old gate, no date recorded): "it made no difference taking those exclamation phrases out for pangram"
- **Checked by:** judgment.
- **Stages:** show, record
- **Links:** goes with R-change-what-he-named; goes with R-every-window-high
- **Replaces:** audit cards C04, OLD-GATE (cluster C34); gate E343; lesson neuro-2026-11-14 ("can't go in"); the apply step's refusal of approved content
- **Status:** active
- **Record:** 2026-11-28, audit cards C04 and OLD-GATE, approved.

## 3 Passing Pangram

Rules for getting the editor's text to read Human, after it reads well.

### 3.1 Order of work

What comes first when a text has to pass.

#### R-reads-well-first | Sense first, then make it read well, then see whether Pangram agrees
- **Rule:** An article is made to make sense before it is humanized, so a later sense fix doesn't force the humanizing to be done again. To humanize a passage, don't think about Pangram at first: fix it until it reads well and leads the reader on, then check. Before each Pangram try the editor reads its text for sense; a short note of that read for the passage is the record, and no tool refuses a small change, or content Joel gave, for lacking one. Sense and Pangram often agree; where they part, the reader decides (R-never-cut-important).
- **Why:** Joel, saved preference: "in general humanization should happen after the article makes sense, because otherwise we have to fix the sense and then depending how large that fix is, potentially re-humanize again" Joel, 2026-11-21: "my approach requires not even thinking about pangram at first ... once i fully make it look right, then i can chheck if pangram agrees" and "pangram can be fickle so when you're not fully fixed yet you might go back and forth on pangram results" Joel, 2026-11-04: "do we need to devise some kind of making sense protocol rather than attacking this problem case by case perhaps?"
- **Checked by:** judgment, then the Pangram check; the note of the sense read is kept with the record of Pangram checks.
- **Stages:** start, sense, humanize, check
- **Links:** builds on R-payoff-first; goes with R-connect; comes before R-hacks-last; goes with R-keep-strategy
- **Replaces:** audit cards C02, C31; gates E360, E365, E368, E369; the per-sentence receipt in MAKING-SENSE.md; "Each gap gets answered in the draft"; the receipt requirement in the ledger's predict step and on the marking page; "What reads as human to Pangram is what reads easily to his readers" in SKILL.md; his saved preferences
- **Status:** active
- **Record:** 2026-11-28, audit cards C02 and C31, approved, with his notes: C02 "something like this already exists maybe merge"; C31 "can merge with some other rules". The read for sense, sense before humanizing, and reading well before Pangram made one rule.

#### R-most-ai-first | Start with the parts that read most AI
- **Rule:** Work first on the sentences and parts that read most AI, then the Low windows, then the Medium ones. Keep in mind that fixing one sentence can make another part read better to Pangram.
- **Why:** Joel, 2026-11-28: "usually it makes sense to focus on the most AI sentences first, altho also keeping in mind that fixing one sentence can make a different sentence/part look better to pangram sometimes." Joel, 2026-11-04: "low windows can easily flip to AI in different segmentations"
- **Checked by:** judgment; the record of Pangram checks lists the windows.
- **Stages:** humanize, check
- **Links:** goes with R-every-window-high; goes with R-keep-strategy
- **Replaces:** audit cards C01, C04 (his notes)
- **Status:** active
- **Record:** 2026-11-28, audit card C04, approved, with his note: "yes you start working on the parts that are most AI as i mentioned"

### 3.2 Windows and confidence

How a Pangram result is read and what counts as done.

#### R-record-confidence | Every Pangram result is recorded with each window's confidence
- **Rule:** Each window's confidence (High, Medium or Low) is recorded and shown to him ("Human (Low)", not "Human"), read from the result's details and not from the page's colours.
- **Why:** Joel, 2026-10-26: "always we should be marking down the confidence if we have it, because less than high confidence means it's likely next pangram version will mark it ai (that happened in pangram 4.1 update)"
- **Checked by:** the record of Pangram checks.
- **Stages:** check, record
- **Links:** comes before R-every-window-high; goes with R-clickable-links
- **Replaces:** gate E278; his saved preferences (first half)
- **Status:** active
- **Record:** his saved preference.

#### R-every-window-high | Every window of the editor's text is aimed at Human High
- **Rule:** A window that reads AI, or Human at Low or Medium confidence, is work to do and doesn't count as done; one such reading is enough, with no second check to confirm it. The editor keeps fixing while it is on track. A paragraph of the editor's that is still short of High when its tries are spent stays out of the article and is reported as open work with its link, never as passed; a window reading Medium that is only a heading, a word or a phrase doesn't hold it out, while one with a whole sentence does. Content he approved still goes in at once (R-approved-goes-in), and its paragraph is then open work. Some pieces aren't worth fixing, because Pangram has bugs: a short "Why?" often reads Medium, and such pieces are left. A split at "Dr." may be closed by dropping the title, especially where the person was already introduced with it; that is a hack, so it comes last (R-hacks-last).
- **Why:** Joel, 2026-11-23: "actually i don't like the medium windows ... i often find the medium windows indicate other issues also" Joel (old gate, no date recorded): "if a section reads ai or human low, we don't need to check it again to verify that, we need to fix it" Joel, 2026-11-06: "some things are not worth fixing, pangram has some bugs, like "Why?" often reads as medium, etc." Joel, 2026-11-28: "unless it's just a heading or a word or phrase, but a whole sentence at least yeah that's more important to fix"
- **Checked by:** the record of Pangram checks; the apply gate holds out a paragraph short of High, but for a Medium window that is only a heading, a word or a phrase; judgment on what is still open.
- **Stages:** humanize, check, show
- **Links:** builds on R-record-confidence; goes with R-budget; goes with R-approved-goes-in; goes with R-hacks-last
- **Replaces:** audit card C04; his saved preferences; the apply step's absolute refusal; "put it on the article's later list" in SKILL.md; lessons gut-2026-11-06a, neuro-2026-11-06c, romance-2026-11-23i; audit card OLD-GATE; gates E306, E324
- **Status:** active
- **Record:** 2026-11-28, audit cards C04 and OLD-GATE, approved. The card's "splits at "Dr." are left" (a bare approval) is read with his typed note on C28, which holds over it: the title may be dropped, as a hack, last. Then 2026-11-28, his answers on the open questions (15:23 UTC): approved (it stays out until High), with his note on headings, words and phrases.

#### R-no-hiding-paragraphs | A paragraph that reads AI alone isn't hidden inside a section that passes
- **Rule:** A paragraph that fails Pangram by itself doesn't count as passed because the section around it passes.
- **Why:** Joel, saved preference: "i think we already have a rule that you can't hide AI paras inside other stuff to get it to pass right?"
- **Checked by:** the record of Pangram checks, which holds each paragraph's own check.
- **Stages:** check
- **Links:** goes with R-every-window-high; goes with R-stuck-paragraph
- **Replaces:** his saved preferences (first half)
- **Status:** active
- **Record:** his saved preference.

### 3.3 Strategy

How to choose the next try when a text still reads AI.

#### R-start-from-near-miss | After a near miss, start from it and clear up everything unclear
- **Rule:** After a near miss, the next try starts from it and fixes everything in it that a reader could take two ways, however many words that takes. Checking one change at a time is a useful habit for seeing which change moved the reading; no limit on changed words applies.
- **Why:** Joel, 2026-11-19: "i made 2 changes, and i checked each one. each was necessary to get to fully high conf human. first i clarified what "it" was referring to, then i clarified what "too weak" meant" and "i keep giving you the same lessons each time: clarify and make sure everything is explained as soon as possible so that reading more makes sense to do"
- **Checked by:** judgment.
- **Stages:** humanize, check
- **Links:** goes with R-keep-strategy; builds on R-clear-it
- **Replaces:** audit card C01; lesson bad-trips-2026-11-19b; the 20% and 40% refusals in the ledger; "a word or two per check" in AGENTS.md
- **Status:** active
- **Record:** 2026-11-28, audit card C01, approved.

#### R-keep-strategy | Make the next obvious fix, and keep a strategy that is good for the reader
- **Rule:** After an AI read, make the next obvious fix while one exists, whatever the count of reads; nothing forces a panel of readers after a set number of reads. When a fix was clearly good for the reader and Pangram reads worse, keep the same strategy and look for what else is tripping Pangram up. Change strategy when unsure the fix really was good for the reader, or when nothing else tripping Pangram can be found. When no strategy worth a try is left, the paragraph goes to him (R-stuck-paragraph).
- **Why:** Joel, 2026-11-05: "I do what i know works, and if it doesn't fix it, I just try to find the next obvious thing that shoudl work, and nearly every single time, that leads to passing pangram." Joel, 2026-11-28: "occasionally as you see in how i do it, pangram gets worse, but i only change strategy if i feel unsure that my fix was realyl good for the reader. if i'm sure it wa sgood, i keep going on that same strategy and try to find other things that are tripping pangram up before  i re-assess if i should change strat"
- **Checked by:** judgment.
- **Stages:** humanize, check
- **Links:** builds on R-reads-well-first; goes with R-budget; comes before R-stuck-paragraph
- **Replaces:** audit cards C01, C07 (the "latest score is the best" test), C20; gates E346, E361; the panel refusal in the ledger's predict step; for Pangram tries, the switch after tries "fail the same way" in AGENTS.md "Method fit and switching"
- **Status:** active
- **Record:** 2026-11-28, audit cards C01 and C20, approved, with his notes: C01 (quoted above); C20 "this sounds like some other rule you can merge".

#### R-flags-are-leads | A reader's flag is a lead to weigh
- **Rule:** What a fresh reader or reviewer flags is weighed on its merits; making sense and Pangram decide. No flag is applied to text that reads Human only because readers agreed on it.
- **Why:** Joel (old gate, no date recorded): "so your readers were all wrong, you don't need any lived experience, you just need it to MAKE SENSE"
- **Checked by:** judgment.
- **Stages:** sense, humanize
- **Links:** goes with R-read-against-his-fixes; goes with R-keep-strategy
- **Replaces:** audit cards C20, OLD-GATE (cluster C32); "Fix every sentence two of them flag"; "Every flag gets fixed, or answered in the record" in the old gate
- **Status:** active
- **Record:** 2026-11-28, audit cards C20 and OLD-GATE, approved.

#### R-one-paragraph-for-strategy | Try a new strategy on one paragraph
- **Rule:** A new strategy is tried on one paragraph checked alone, so it is clear whether the strategy works.
- **Why:** Joel, 2026-11-04: "just work on one paragraph at a time so you can see whether your strat is working"
- **Checked by:** judgment.
- **Stages:** humanize, check
- **Links:** goes with R-budget
- **Replaces:** audit card C07 (kept part); FIXING-AN-ARTICLE.md on single-paragraph checks
- **Status:** active
- **Record:** 2026-11-28, audit card C07, approved.

#### R-predict-before-recheck | Before a recheck, say which parts are likely to come back AI
- **Rule:** Before a text is rechecked, the editor names the few stretches most likely to come back AI.
- **Why:** Joel (old gate, no date recorded): "i was thinking you should predict which part comes back as AI?"
- **Checked by:** the record of Pangram checks holds the prediction beside the result.
- **Stages:** check, record
- **Links:** goes with R-budget
- **Replaces:** audit card OLD-GATE (cluster C32); "every whole-article check now comes with a part forecast"
- **Status:** active
- **Record:** 2026-11-28, audit card OLD-GATE, approved.

#### R-mimic-pangram | Work out how to mimic the way Pangram reads text
- **Rule:** Train a small stand-in on the record of Pangram checks (hundreds of texts with how each read), test it on checks it hasn't seen, and report how well it predicts Pangram. If it predicts well, it helps choose what to fix before a check is spent; it never takes Pangram's place.
- **Why:** Joel, 2026-11-28: "i'm curious how we can mimic the way pangram analyzes text statistically."
- **Checked by:** nothing yet.
- **Stages:** check, record
- **Links:** goes with R-fixes-searchable; goes with R-predict-before-recheck
- **Replaces:** audit card C17 (his note)
- **Status:** to build (the way he approved)
- **Record:** 2026-11-28, audit card C17, to revise, from his note; then 2026-11-28, his answers on the open questions (15:23 UTC): approved (the stand-in).

#### R-no-lived-experience-needed | Passing Pangram never needs his lived experience
- **Rule:** No card asks Joel for his experience to get a text past Pangram. His experience goes in where it would really help the reader.
- **Why:** Joel, 2026-11-27: "there's no need for me to give you some kind of human experience, that's not what pangram requires ... human experience is good to put in where it would genuinely be helpful for the reader"
- **Checked by:** judgment.
- **Stages:** humanize, show
- **Links:** goes with R-no-invented-life; goes with R-stuck-paragraph
- **Replaces:** lesson somatic-2026-11-27a; way 28's explanation of a miss
- **Status:** active
- **Record:** unchanged.

### 3.4 AI tells

Words and shapes that read as AI, each read by a person before anything changes.

#### R-counts-send-to-read | A count sends the editor to read; it fails nothing
- **Rule:** A list of three, a short plain statement, a run of questions and a contrast frame can each read as AI. Seeing one sends the editor to read, and the fix is by meaning: an item is cut only where it overlaps or is vague, a short line is joined to its sentence, questions are reordered until they flow. Nothing important is cut and no detail is invented to settle a count.
- **Why:** Joel (old gate, no date recorded): "it wasn't just the rule of 3 items in a sentence that mattered, tho it was also the vagueness of that "not now."" Joel, 2026-11-22: "the ai tell is the short plain statements. feels robotic"
- **Checked by:** the linter warns; judgment decides.
- **Stages:** humanize
- **Links:** goes with R-phrase-tells; goes with R-never-cut-important; goes with R-rules-fit-capability
- **Replaces:** audit card C22; gate E125; tell W124; the word and frame counts in the fixes brief, the tells list and the cold-audit gate
- **Status:** active
- **Record:** 2026-11-28, audit card C22, approved.

#### R-phrase-tells | A phrase is a tell for what it does
- **Rule:** A phrase tell is recorded as what the phrase does (a tidy closer, a line that could go anywhere, a pointer with nothing before it), with the phrase as its example. Entries with no words of his and no result behind them are dropped or demoted; the tells he named himself stay as he said them; "for the thing" is one he named.
- **Why:** Joel, 2026-11-02: "Ai is always saying this portable stuff that could go anywhere" Joel, 2026-11-28: "and btw "for the thing" is an ai tell"
- **Checked by:** judgment; the linter warns.
- **Stages:** humanize, record
- **Links:** goes with R-counts-send-to-read; goes with R-overused-words
- **Replaces:** audit card C23; tells W07, W08, W41, W60, W105 to W112, J90; audit card C14 (his note)
- **Status:** active
- **Record:** 2026-11-28, audit card C23, approved. 2026-11-28, audit card C14, approved, with his note (quoted above).

#### R-overused-words | Overused AI words are read, not banned
- **Rule:** "Honestly", "matters", "isn't proof of" and "doesn't prove", "I want", a "not Y" tail ("that's X, not Y") and "not X, but Y", and a negation in a heading are patterns AI overuses. Each is reported for a reader to judge: where a more specific word or a real synonym fits, use it, and where the word is the one meant, it stays. Nothing is reworded in a way that changes the meaning to avoid one. "Quietly" goes unless it says how something sounds.
- **Why:** Joel, 2026-11-23: "you can't just switch honestly for compassionately always that's working sometimes, but like authentically, genuinely, those are more real synonyms, and honestly is also ok sometimes just it's overused" Joel, saved preference: "Ai is always saying stuff "MATTERS" ... not saying never to use it but don't use it if a more specific word would give more sense" Joel, 2026-11-04: "there's also the Not X, but Y. pattern with AI, so we shouldn't overuse that either, but sometimes it is the most clear and natural way to phrase it" Joel (old gate, no date recorded): "remove "quietly" that's an ai tell"
- **Checked by:** the linter warns; judgment decides.
- **Stages:** humanize
- **Links:** goes with R-phrase-tells; goes with R-accurate-word; goes with R-one-for-a
- **Replaces:** audit cards C11, OLD-GATE ("quietly"); gate E259; tells W96, O9, O77; his saved preferences; AGENTS.md on "honestly" ("the only one nearby")
- **Status:** active
- **Record:** 2026-11-28, audit card C11, to revise: this part is the card's proposal (he approved the card's direction); his note was on "one" plus a noun, now R-one-for-a.

#### R-emphasis-only-where-called-for | Emphasis only where the context calls for it
- **Rule:** Emphasis added to sound human reads as AI. "Straight into" is a frequent one: it is emphatic, and it doesn't mean "converted into". An emphatic word goes in only where the context calls for more emphasis; otherwise the plain accurate word does the work (R-accurate-word).
- **Why:** Joel, 2026-11-28: "btw"straight into" is a high freq ai tell, sounds often like you're trying to sound human but straight into is emphatic, don't overuse emphasis to sound more human unless the context calls for more emphasis. it's not synonymous with "converted into""
- **Example:** before "turned straight into" / after "converted into"
- **Checked by:** the linter notes "straight into"; judgment decides.
- **Stages:** humanize
- **Links:** goes with R-accurate-word; goes with R-overused-words
- **Status:** active
- **Record:** 2026-11-28, his message of 15:23 UTC.

#### R-one-ordinary | "One ordinary" and "one honest action" go wherever they appear
- **Rule:** These two phrases are removed wherever they appear.
- **Why:** Joel, 2026-11-03: "we gotta remove "one ordinary" anywhere lol so ai"
- **Checked by:** the linter blocks.
- **Stages:** humanize
- **Links:** goes with R-one-for-a
- **Replaces:** audit card C11; his saved preferences
- **Status:** active
- **Record:** 2026-11-28, audit card C11, to revise (this part kept).

#### R-one-for-a | "A" where a person would say "a", not "one"
- **Rule:** AI often writes "one" where a person would write "a". Where "a" sounds better, use it; "one" stays where the number is the point.
- **Why:** Joel, 2026-11-28: "i often find AI using "one" where a human would use "a" so if it sounds better to use "a" than "one" do that. "one time is too many" would still be "one time is too many" of course."
- **Checked by:** judgment.
- **Stages:** humanize
- **Links:** goes with R-one-ordinary
- **Replaces:** audit card C11 ("one" plus a noun)
- **Status:** active
- **Record:** 2026-11-28, audit card C11, to revise, written as his note says.

#### R-x-does-not-y | Rework "X does not Y" statements, keeping what they deny
- **Rule:** The abstract kind of "X does not Y" (""I saw it" does not create a duty to act") is reworked by default, in any wording that keeps what it denies, and kept where it is the clearest way to say the thing; a plain negative is judged case by case. A denial of fact or of safety is not softened into a "might" for the detector.
- **Why:** Joel, saved preference: "let's make sure "X does not Y" is changed in general that's super ai, humans don't use that so much"
- **Checked by:** the linter warns; judgment decides.
- **Stages:** humanize
- **Links:** goes with R-overused-words; goes with R-keep-what-he-meant
- **Replaces:** audit cards C11, C21; his saved preferences; lesson bad-trips-2026-11-07d
- **Status:** active
- **Record:** 2026-11-28, audit cards C11 (to revise) and C21 (approved); then 2026-11-28, his answers on the open questions (15:23 UTC): approved (the abstract kind by default, a plain negative case by case).

#### R-kitchen-and-weekdays | Kitchen details and added weekdays are AI signs
- **Rule:** A kitchen detail reads as AI, and adding a day of the week to it makes two signs. A weekday the editor added goes; a real day in one of his own stories stays. A date range is not a human tell.
- **Why:** Joel, saved preference: ""in the kitchen" is what AI always says. kitchen this, kitchen that... how is a date range a human tell?"
- **Checked by:** the linter warns; judgment decides.
- **Stages:** humanize
- **Links:** goes with R-no-invented-life; goes with R-phrase-tells
- **Replaces:** his saved preferences; audit card C23
- **Status:** active
- **Record:** his saved preference; 2026-11-28, audit card C23, approved; then 2026-11-28, his answers on the open questions (15:23 UTC): approved.

#### R-dashes-and-quotes | Two hyphens for every dash, straight quotes and apostrophes
- **Rule:** In all his articles every dash becomes his two hyphens "--", with no spaces around them, as he types them, and curly quote marks and apostrophes are straightened.
- **Why:** Joel, 2026-11-04: "no everything should be the 2 dashes not em-dash, em-dash is ai" Joel, saved preference: "yes the curly apostrophes are an AI tell i know that"
- **Example:** his own: "handling--we see"
- **Checked by:** the linter blocks an em dash or a curly mark.
- **Stages:** humanize, show
- **Replaces:** audit card C12; his saved preferences; tell O15
- **Status:** active
- **Record:** 2026-11-28, audit card C12, approved; then 2026-11-28, his answers on the open questions (15:23 UTC): approved (no spaces).

### 3.5 Budget and routes

How many Pangram checks to spend and which way to run them.

#### R-budget | About ten tries a paragraph, with reasons, and more when it pays
- **Rule:** The try limit is there to stop blind tests. A paragraph gets up to about ten tries, each after the first with a named reason; a worse reading alone doesn't end it. Don't spend a try with no idea what to change. When hot on the trail, or when extra checks would teach something (his own fine-grained checks make the best paired examples), the budget stretches.
- **Why:** Joel, 2026-11-20: "so we shoudl raise the limit to 10 then? it seems like the point of the limit was to stop you from doing blind tests, but if your'e on the right track you should keep going" Joel, 2026-11-28: "don't even try if you have no idea what you're doing, but if you're hot on the trail and just need more budget then the budget should be flexible. sometimes i will spend more than 10 pangram calls myself because i'm trying to be granular enough to give you excellent minimal pair lessons, you can also use more pangram calls if that would help you learn"
- **Checked by:** the record of Pangram checks warns when a try has no reason; judgment on going past ten.
- **Stages:** check, record
- **Links:** goes with R-keep-strategy; comes before R-stuck-paragraph
- **Replaces:** audit cards C05, C07; the budget file's six and ten; "six is a hard maximum"; the ledger's "right track" score test; the old gate's two-call budget; his saved preferences
- **Status:** active
- **Record:** 2026-11-28, audit cards C05 and C07, approved, with his notes: C05 quoted above; C07: "maybe merge this with previous? in general merge any rules that could be merged"

#### R-free-route-for-big-checks | A whole or half article is checked the free way
- **Rule:** A whole article, or half of one, is checked through a temporary Substack draft that he runs his Pangram extension on. The paid routes take sections of about five or six paragraphs at most.
- **Why:** Joel, saved preference: "that should be done the free way to not waste my pangram credits" and "we don't do whole article checks with pangram GUI ... you can do a section check in the GUI tho, like 5-6 paragraphs or so"
- **Checked by:** the record of Pangram checks warns just over that size and blocks half an article or more.
- **Stages:** check
- **Links:** goes with R-preview-link; goes with R-run-own-checks
- **Replaces:** audit card C07; gate E218; his saved preferences; the 1,200-word refusal
- **Status:** active
- **Record:** 2026-11-28, audit card C07, approved.

#### R-preview-link | For a Substack check, he gets a link he only has to open
- **Rule:** The lane makes the temporary draft's secret preview link itself and gives it to him with whatever he needs to use it, so all he does is open it and run the check. Once the results are recorded, the lane deletes the drafts it made and says so.
- **Why:** Joel, 2026-10-26: "why is it that you know how to make the preview, while inner child lane only makews a draft without making a preview of it? make sure that's a durable instruction to save me some steps" Joel, 2026-10-21: "and yes delete the drafts once definitely done with them add taht to the rules."
- **Checked by:** judgment.
- **Stages:** check, show, record
- **Links:** builds on R-free-route-for-big-checks
- **Replaces:** audit card C30; gate E277; his saved preferences; "what goes to Joel is that link and nothing else"; "leaves the delete click to Joel" in the budget file
- **Status:** active
- **Record:** 2026-11-28, audit card C30, approved.

#### R-run-own-checks | The lane runs its own Pangram checks in the web app
- **Rule:** Paragraph and section checks are run by the lane itself in Pangram's web app with his account, without asking his OK each time and without handing them to him. The paid interface for programs isn't topped up unless a lane shows it really matters.
- **Why:** Joel, saved preference: "you don't need my ok each time to run the GUI pangram checks" Joel, 2026-11-04: "i'm not topping up the api unless you think it's really important because we have tons of gui credits still"
- **Checked by:** judgment.
- **Stages:** check
- **Links:** goes with R-free-route-for-big-checks; goes with R-record-confidence
- **Replaces:** gate E356; his saved preferences
- **Status:** active
- **Record:** his saved preference.

### 3.6 Hacks, last

Changes that move Pangram without helping the reader; allowed when needed, and only after everything above.

#### R-hacks-last | A Pangram hack comes after every rule that helps the reader
- **Rule:** A change made only because it moves Pangram is a hack. Hacks are allowed when needed, and they come last. A hack keeps every point and the meaning: it never cuts something important or leaves the text harder to follow (R-never-cut-important), never swaps the accurate word for a paraphrase (R-accurate-word), never softens a denial into a "might" (R-x-does-not-y) and never invents anything about his life (R-no-invented-life). Dropping "Dr." from a name, especially one already introduced with the title, is one.
- **Why:** Joel, 2026-11-28: "Dr. could be dropped especially if they were already introduced as such i suppose but this is a real hack and pangram hacks are ok if we need to use them, but i'd put this very much last as a rule, we want to have the rules that help the reader up front before the hacks"
- **Checked by:** judgment; the turn's report says which changes were hacks.
- **Stages:** humanize, check
- **Links:** builds on R-reads-well-first; goes with R-never-cut-important; goes with R-no-invented-life; goes with R-cut-repeats; goes with R-every-window-high
- **Replaces:** audit card C28; lesson neuro-2026-11-27 ("Dr." off)
- **Status:** active
- **Record:** 2026-11-28, audit card C28, approved, with his note (quoted above). The limits named here are the rules above it, after the rules check found the hack rule set none.

## 4 Working with Joel

Rules for what goes to Joel, how, and when.

### 4.1 When to ask

Which things need Joel and which the editor settles itself.

#### R-ask-when-needed | Ask only where his opinion is really needed
- **Rule:** Joel is asked where the meaning might change, where there is a downside to weigh, where the words are ones he wrote himself, or where only he knows the fact. The card says why in plain words. Look in the article and his earlier answers before asking, and settle disagreements between reviewers first. Rewording is the job and needs no question.
- **Why:** Joel, 2026-11-07: "you're asking me to approve things that are clearly good / you should be learning what you actually need to ask my opinion on, like if meaning might have changed or there's a downside to consider" Joel, 2026-10-25: "i have not really read yours or GPT's yet because it's a lot of reading and prob no point until you can agree"
- **Checked by:** judgment; no fixed labels and no count.
- **Stages:** show
- **Links:** goes with R-tested-change-goes-in; goes with R-stuck-paragraph
- **Replaces:** audit cards C18, OLD-GATE (cluster C34); the "ask_because" labels and their refusal; the five-approvals count in lesson bad-trips-2026-11-07; "only what both recommend"; his saved preferences
- **Status:** active
- **Record:** 2026-11-28, audit card C18, approved.

#### R-tested-change-goes-in | A tested change that keeps the meaning goes in and is reported
- **Rule:** A tested change that keeps the meaning, a bridge sentence or a structure change included, goes into the article without a card and is named in the turn's report. A fix to wording Joel humanized himself goes to him on a card only where it could change something he decided (R-model-text-is-mine).
- **Why:** Joel, 2026-11-07: "you're asking me to approve things that are clearly good"
- **Checked by:** judgment.
- **Stages:** show, record
- **Links:** builds on R-ask-when-needed; goes with R-clickable-links; goes with R-model-text-is-mine
- **Replaces:** audit card C18; gates gut-2026-11-07b, bad-trips-2026-11-07a; "New wording in his article ... is his call" in FIXING-AN-ARTICLE.md
- **Status:** active
- **Record:** 2026-11-28, audit card C18, approved.

#### R-stuck-paragraph | Fix what can be fixed before asking, then ask in his words
- **Rule:** A paragraph with AI tells the editor can see is fixed, not shown to him. When no next fix is left and no other strategy is worth a try (R-keep-strategy), one or two paragraphs he could teach the most from go to him, each as the best faithful version with what was tried, in his sentence: "I can't find any more AI tells here, and I see some human tells, like these... can you help show me the tells I'm missing?", naming the human tells found or saying plainly that none were.
- **Why:** Joel, saved preference: "why can't you fix them? why did you even show me these if you see AI tells in them? what is it you need help with?" and "for each thing you need help with, you always need to tell me"
- **Checked by:** judgment.
- **Stages:** humanize, show
- **Links:** builds on R-keep-strategy; builds on R-budget; goes with R-never-cut-important; goes with R-human-tell
- **Replaces:** audit cards C05, C15, C20; AGENTS.md "Ask him as soon as the first method is spent"; gate E373; lesson bad-trips-2026-11-07c; his saved preferences (second half), 10
- **Status:** active
- **Record:** 2026-11-28, audit card C05, approved. "Changes approach when tries fail the same way" is gone, after the rules check found it against his note on C01 (R-keep-strategy).

#### R-examples-to-score | When unsure how a rule applies, give him examples to score
- **Rule:** When it is unclear how a rule applies to his writing, the editor may give him a list of examples he can score; his scores become the rule's worked examples.
- **Why:** Joel, 2026-10-12: "if you're not clear about how to apply rules you can give me a list of examples i can score. put that in the joel-articles rules"
- **Checked by:** judgment.
- **Stages:** show, record
- **Links:** goes with R-ask-when-needed
- **Replaces:** AGENTS.md on examples to score; audit card OLD-GATE (cluster C34)
- **Status:** active
- **Record:** unchanged.

#### R-keep-working | A turn doesn't stop while there is work the editor can do
- **Rule:** A turn doesn't end with work the editor could still do and nothing for Joel to act on. When tries are spent, he gets a card the same turn.
- **Why:** Joel, 2026-11-14: "didn't understand why you gave me no cards and quit working tho"
- **Checked by:** judgment; the push tool warns when a turn ends on open windows.
- **Stages:** show
- **Links:** goes with R-stuck-paragraph; goes with R-every-window-high
- **Replaces:** lesson bad-trips-2026-11-14b; audit card C30 (kept part)
- **Status:** active
- **Record:** 2026-11-28, audit card C30, approved.

### 4.2 Cards and pages

How suggestions are put in front of Joel.

#### R-marking-page | Suggestions go to him on a marking page
- **Rule:** Editing suggestions go to Joel as the article itself, each suggestion highlighted where it applies and coloured by kind, with the suggestion, Approve, Reject and Revise, and a comment box. The page shows the whole article, not only the paragraphs asked about: a stretch is left out only when it would take a lot of space, never a single paragraph, and any cut is clearly marked. Lists of suggestions out of context are not the way, and he is never sent a data file to read.
- **Why:** Joel, 2026-10-25: "that was a good marking page save that so it's how we work in future editing work" Joel, 2026-11-22: "it would have helped if you just had the whole page so i could see the whole context, make that a rule from now on"
- **Checked by:** the marking-page tool blocks a page that doesn't name the whole article it shows.
- **Stages:** show
- **Links:** goes with R-after-shows-result
- **Replaces:** his saved preferences; gates E265, E280 to E282; audit card LEFTOVERS (the numbered list in CLARITY-READ.md); lesson romance-2026-11-22a
- **Status:** active
- **Record:** his saved preference.

#### R-after-shows-result | The "after" shows the result, with follow-on fixes already made
- **Rule:** When a cut or change is proposed, its "after" version shows the text as it would read, with any follow-on fix (a capital letter, a changed word) already made, not described.
- **Why:** Joel, saved preference: "instead of telling me "the sentence then starts with.." you actually make that change in the "after" version"
- **Checked by:** judgment.
- **Stages:** show
- **Links:** goes with R-cuts-shown; builds on R-marking-page
- **Replaces:** his saved preferences
- **Status:** active
- **Record:** his saved preference.

#### R-read-page-before-sending | Read every paragraph and card before a page goes
- **Rule:** Before a page goes to him, every paragraph on it is read in its section. What doesn't make sense or follow is fixed first in model text; what is left (his words, or what the editor can't fix) is named on its card with the best fix. Every text written for him (a card, a page, a message, and text a script put together) is also read for wrong, missing or garbled words before it goes.
- **Why:** Joel, 2026-11-22: "you should have alerted me to those if you codln't fix them" Joel, 2026-11-28: "ok i notice you have been making some typos, "fix of your(s) did", that's weird for ai to make typos..." and ""your(s)" again..."
- **Checked by:** judgment; a script that rewrites text for him is checked on what it writes.
- **Stages:** sense, show
- **Links:** goes with R-reads-well-first; goes with R-marking-page; goes with R-close-read
- **Replaces:** lesson romance-2026-11-22b
- **Status:** active
- **Record:** 2026-11-28: his notes on audit cards C21 and C28 added the read for typos; the rest unchanged.

#### R-test-copy-openable | A test copy of a page goes out only where it can be opened
- **Rule:** Before publishing a test copy of a picks page, open any claude.ai artifact in the browser pane. When it asks to sign in, make no copy: run the page headless from its file, read his page's store with the artifact tools, and say in the reply that the save itself wasn't tried.
- **Checked by:** judgment.
- **Stages:** show
- **Links:** goes with R-marking-page; goes with R-no-tabs
- **Replaces:** lesson romance-2026-11-28b; part of lesson toc-2026-11-24c
- **Status:** active
- **Record:** 2026-11-28, lesson romance-2026-11-28b, the romance lane's own: its test copy couldn't be opened (the pane wasn't signed in, which is his to do) and now sits unused among his artifacts.

#### R-title-length-marker | Where he writes his own title, show how long it can be
- **Rule:** A box where he can write his own title shows the length at which the contents sidebar cuts it off, and whether what he types fits.
- **Why:** Joel, saved preference: "I told you before but i'd still like to have some visible maker for "your own words" where it would show me how long it can be"
- **Checked by:** the page itself.
- **Stages:** show
- **Links:** goes with R-marking-page; goes with R-headings-answer-reader
- **Replaces:** his saved preferences
- **Status:** active
- **Record:** his saved preference.

### 4.3 Links and reports

How Joel is pointed to things.

#### R-clickable-links | A link he can click or a file, never a path
- **Rule:** Every document Joel is pointed to is a link he can click, to a page he can read, or a file sent to him. Each Pangram result the editor reports comes with the link to that result.
- **Why:** Joel, saved preference: "can you stop giving me paths to files that are relative to something? ... always give me a link to click or a file to look at" and "why are you not giving me the pangram link so i can see? always give me the links"
- **Checked by:** the link check warns about a path or a folder link in a message for him.
- **Stages:** show
- **Links:** goes with R-no-tabs
- **Replaces:** his saved preferences
- **Status:** active
- **Record:** his saved preferences.

#### R-references-explained | A reference he reads comes with what it is
- **Rule:** In anything written for Joel, a reference he can't be expected to know (a gate number, a card, rule or lesson code, a file) comes with what it is, in plain words, where it appears, or it isn't used. In the tree's human view, rules point to each other by name, and each code a rule replaces says what it is.
- **Why:** Joel, 2026-11-28: "many of these are referencing other things that iw asn't clear on, but hopefully clear for you, altho there should be a human view of the rule tree where everything makes sense, maybe with graphical links"
- **Checked by:** judgment; the human view names each linked rule and explains each code it shows.
- **Stages:** show
- **Links:** goes with R-clickable-links; goes with R-tree-is-home
- **Status:** active
- **Record:** 2026-11-28, his message asking for the tree.

#### R-no-tabs | Give him links; don't open tabs in his browser
- **Rule:** Nothing is opened in his browser for him to find later; he gets the links to click.
- **Why:** Joel, saved preference: "for future just give me the links to click because what happens is you open tabs then i'm not here then someone else opens tabs etc and it gets lost. only takes me a second"
- **Checked by:** judgment.
- **Stages:** show
- **Links:** goes with R-clickable-links
- **Replaces:** his saved preferences
- **Status:** active
- **Record:** his saved preference.

#### R-update-date | Updating a post updates its date
- **Rule:** Whenever one of his posts is updated, its "Last update" date is updated too, without asking.
- **Why:** Joel, saved preference: "you can always update that date when updating a post of course"
- **Checked by:** judgment.
- **Stages:** record
- **Replaces:** his saved preferences
- **Status:** active
- **Record:** his saved preference.

## 5 How the lanes work

Rules for the parallel work sessions, their shared repository, and the rules themselves.

### 5.1 Lanes and the repository

How lanes share one place and keep it working.

#### R-one-shared-place | Every lane reads from and feeds into the same place
- **Rule:** Each lane starts from the shared main copy, takes in what others changed every turn, and builds on another lane's change to a shared file, so no work is done twice.
- **Why:** Joel, saved preference: "i want to make sure each lane is feeding into and reading from the same place so i don't duplicate work" Joel, 2026-11-04: "make sure no other lane can make the same mistake you made next time"
- **Checked by:** the push tool blocks a push when the shared copy isn't merged in.
- **Stages:** start, record
- **Links:** goes with R-lessons-to-main; goes with R-lane-changes-merge-themselves
- **Replaces:** his saved preferences; gate E339
- **Status:** active
- **Record:** his saved preference.

#### R-lane-changes-merge-themselves | A lane's changes merge on their own
- **Rule:** A lane's proposed change merges itself once its checks pass, tools included, and doesn't wait for his click.
- **Why:** Joel, 2026-11-14: "that should happen automatically"
- **Checked by:** the repository's automatic merge.
- **Stages:** record
- **Links:** builds on R-one-shared-place
- **Replaces:** audit card C30; gate E379; lesson bad-trips-2026-11-14a
- **Status:** active
- **Record:** 2026-11-28, audit card C30, approved.

#### R-mailbox-check | Each turn starts by reading what is addressed to the lane
- **Rule:** At the start of every turn the lane checks what has been addressed to it.
- **Why:** Joel, 2026-10-31: "can we make sure you always check what is addressed to you in each turn?"
- **Checked by:** the push tool blocks a push with no record of the turn's check.
- **Stages:** start
- **Links:** goes with R-one-shared-place
- **Replaces:** audit card C30; AGENTS.md "Suggested fixes from other projects"
- **Status:** active
- **Record:** 2026-11-28, audit card C30, approved.

#### R-debug | Anything that isn't working as intended is debugged
- **Rule:** When a rule, tool or check isn't doing what it was meant to, it is debugged, not worked around.
- **Why:** Joel, saved preference: "any time something is not executing as intended it should be debugged"
- **Checked by:** judgment.
- **Stages:** record
- **Links:** goes with R-quicker-not-slower
- **Replaces:** his saved preferences; AGENTS.md on tells and their checks
- **Status:** active
- **Record:** his saved preference.

#### R-quicker-not-slower | The work is meant to get quicker as well as better
- **Rule:** The work should get quicker as the editor learns. A step that slows it has to earn its place.
- **Why:** Joel, saved preference: "the point of this was that you would learn to do this better and quicker but it seems like it's getting slower"
- **Checked by:** judgment; the periodic review of lessons.
- **Stages:** record
- **Links:** goes with R-review-lessons; goes with R-check-rewrite-once
- **Replaces:** his saved preferences
- **Status:** active
- **Record:** his saved preference.

#### R-push-access | Lanes may push to any of his repositories
- **Rule:** A lane may push to any of Joel's repositories.
- **Why:** Joel, saved preference: "i allow push access to any repos"
- **Checked by:** nothing; it is a permission.
- **Stages:** record
- **Replaces:** his saved preferences
- **Status:** active
- **Record:** his saved preference.

#### R-dead-embeds | Instagram embeds in a post are checked whenever a lane works on it
- **Rule:** Whenever a lane works on a post, and whenever Joel asks, each Instagram embed in it is checked on Instagram. A dead one goes to him with its post and the saved snapshot to offer in its place.
- **Why:** Joel, 2026-11-21: "add that the joel-articles rules to do that"
- **Checked by:** the embeds tool lists them; the check is made on Instagram.
- **Stages:** start, show
- **Replaces:** gates E341, embeds-2026-11-21a
- **Status:** active
- **Record:** unchanged.

### 5.2 Lessons and this tree

How a rule is made, checked, and kept in one place.

#### R-tree-is-home | Every rule lives once, in this tree
- **Rule:** This tree is the first rule file every lane reads. Rules that say the same thing are merged into one, and each old place points to the rule here that replaces it. A merged rule keeps every clause of the rules it joins, qualifiers included ("especially", "sometimes"), or its record says why one went.
- **Why:** Joel, 2026-11-28: "i also feel like there are a lot of rules that are overlapping and there's not very good organization of the rules like you should have some kind of rule tree or something" and "in general merge any rules that could be merged"
- **Checked by:** the tree's build blocks a rule id used twice or a link to an id that isn't here.
- **Stages:** start, record
- **Links:** goes with R-lessons-to-main; goes with R-lesson-checked
- **Replaces:** AGENTS.md "One set of humanization rules for every article"; the rule copies in AGENTS.md, SKILL.md, the briefs, the lessons and the old gate
- **Status:** active
- **Record:** 2026-11-28, his request for the tree; audit card C07, approved, with his note (quoted above).

#### R-replies-read | His replies on the tree are read and answered every turn
- **Rule:** The tree's human view has a reply box under every rule. The lane that keeps the tree reads his replies at the start of every turn, with the mailbox check, and each reply gets its fate in the tree the turn it is read: the rule changed, a question back to him, or the reason it stays. The replies and their fates are kept in Git.
- **Why:** Joel, 2026-11-28: "make the rule tree something i can reply to."
- **Checked by:** the reply record in Git (rules/replies/).
- **Stages:** start, record
- **Links:** goes with R-tree-is-home; goes with R-mailbox-check; goes with R-git-is-the-record
- **Status:** active
- **Record:** 2026-11-28, his message of 15:23 UTC.

#### R-lessons-to-main | A lesson is shared the turn it is made
- **Rule:** A new lesson goes into the shared copy, and into this tree as a new rule or a change to one, the turn it is made.
- **Why:** Joel, 2026-11-05: "make sure you merge lessons with main branch so everyone is sharing always"
- **Checked by:** the push tool merges a lesson once its checks pass.
- **Stages:** record
- **Links:** builds on R-one-shared-place; comes before R-lesson-checked
- **Replaces:** gates E367, gut-2026-11-06d
- **Status:** active
- **Record:** unchanged.

#### R-lesson-checked | Every new lesson is checked against his words
- **Rule:** Before a lesson is shared, a fresh reader checks it against what Joel actually said. A flag about his meaning goes to him; the rest are fixed, or the lesson says why they stand. It is also checked against the rules near it for overlap, interaction and contradiction. Two rules that contradict are settled by his words: what he typed holds over a bare approval of a card, his later typed words over his earlier ones, and where two bare approvals differ, the question goes to him. It takes about a minute and doesn't hold up article work.
- **Why:** Joel, 2026-11-27: "i often assume you're understanding the lessons" Joel, 2026-11-28: "we should also be checking if lessons interact or contradict each other"
- **Checked by:** a fresh reader with the rules-check brief; the tree's build blocks a "conflicts with" link.
- **Stages:** record
- **Links:** builds on R-lessons-to-main; goes with R-lesson-reason-not-feature
- **Replaces:** audit card S3; lesson bad-trips-2026-11-27n
- **Status:** active
- **Record:** 2026-11-28, audit card S3, approved, with his note: "we should also be checking if lessons interact or contradict each other, and we should do periodic reviews to see which lessons are overall helping vs which aren't"

#### R-lesson-reason-not-feature | A lesson's method is the reason he gave; one fix's shape is only an example
- **Rule:** A lesson's method is the reason Joel gave for his fix. Something that merely happened to be true of the fix becomes the method only where his words or the case show it is why the fix works. What one passing fix did is recorded as something to try where it fits, under that reason; one swap is not applied everywhere.
- **Why:** Joel, 2026-11-27: "it's not about using the same word. it's about using a word that's accurate. didn't i explain that?" Joel, 2026-11-23: "you can't just switch honestly for compassionately always that's working sometimes"
- **Checked by:** the fresh reader's check of each new lesson.
- **Stages:** humanize, record
- **Links:** builds on R-lesson-checked; goes with R-accurate-word; goes with R-learn-from-his-changes
- **Replaces:** audit cards S1, S3, C21; the checker's brief; lessons bad-trips-2026-11-07d ("It might feel like X. But more likely Y"), bad-trips-2026-11-23i; gate E366; the one-fix instructions in the fixes brief
- **Status:** active
- **Record:** 2026-11-28, audit cards S3 and C21, approved; the two rules made one (his note on C07: "in general merge any rules that could be merged").

#### R-review-lessons | Lessons are reviewed from time to time for whether they help
- **Rule:** From time to time the lessons are reviewed to see which are helping overall and which aren't, from his checks and from Pangram before and after.
- **Why:** Joel, 2026-11-28: "we should do periodic reviews to see which lessons are overall helping vs which aren't"
- **Checked by:** nothing yet.
- **Stages:** record
- **Links:** goes with R-lesson-tested; goes with R-quicker-not-slower
- **Replaces:** audit card S3 (his note)
- **Status:** to build
- **Record:** 2026-11-28, audit card S3, approved, with his note (quoted above).

#### R-lesson-tested | A lesson from his fixes is tested on the paragraphs he fixed
- **Rule:** The turn a lesson is drawn from his fixes, a fresh writer who hasn't seen his versions rewrites those paragraphs from the lessons alone, each rewrite is checked in Pangram, and what the rewrites miss becomes the next lesson.
- **Why:** Joel, 2026-11-22: "make sure whenever you learn lessons in this repo you see if you can apply them to pass pangram on the paragraphs that i fixed yourself without seeing my fixes exactly"
- **Checked by:** the Pangram checks of the rewrites, kept in the record.
- **Stages:** record, check
- **Links:** builds on R-learn-from-his-changes; goes with R-review-lessons
- **Replaces:** lessons romance-2026-11-22h, romance-2026-11-23e
- **Status:** active
- **Record:** unchanged.

#### R-rules-fit-capability | Meaning is judged by a reader; a list or pattern only finds candidates
- **Rule:** A question about meaning goes to a model or a person reading. A word list, a count or a pattern fits exact questions, and for meaning it only lists candidates for a reader to judge.
- **Why:** Joel, 2026-10-07: "why can't you simply look at a word and know it's an abstract concept, isn't that what LLMs are great at?"
- **Checked by:** the fresh reader's check of each new lesson.
- **Stages:** record
- **Links:** goes with R-counts-send-to-read; goes with R-lesson-checked
- **Replaces:** AGENTS.md "Method fit and switching"; audit cards C10, C22, C25
- **Status:** active
- **Record:** unchanged.

### 5.3 Handoffs and records

Where things are kept so any lane or account can pick them up.

#### R-git-is-the-record | What he comes back to lives in the repository, readable on GitHub
- **Rule:** Anything Joel will come back to (a scorecard, a questions page, his answers) lives in the repository as a page GitHub renders, with its numbers computed by code there. A published page is only a view of that file and is never the only place something can be read.
- **Why:** Joel, 2026-10-20: "i agree the scorecards should be on github, that should have been obvious ... we can't keep having misses like this where i'm lost when i move from one acct to the other."
- **Checked by:** judgment.
- **Stages:** record
- **Links:** goes with R-clickable-links; goes with R-one-shared-place
- **Replaces:** AGENTS.md on scorecards and artifacts
- **Status:** active
- **Record:** unchanged.

### 5.4 Retired

Old rules that no longer hold, kept here so no lane follows them.

#### R-emulate-retired | Emulate is no longer used on his writing
- **Rule:** Emulate writes no new text for his articles, its shape rules leave the writers' briefs, and his published words are never replaced by Emulate's. One thing stays: Emulate text already in an article gets the strict check for errors it brought in (typos, scare quotes, damaged citations).
- **Why:** Joel, 2026-11-03: "emulate doens't even pass pangram 4.1 very well anymore so that's pointless and emulate has done so much damage to my guides" Joel, 2026-10-25: "make those emulate checks more strict pls for future also"
- **Checked by:** the Emulate check, for text already in his articles.
- **Stages:** start, sense
- **Links:** goes with R-old-gate-historical
- **Replaces:** audit card EMULATE; gate E333; EMULATE-FALLBACK.md; his saved preferences
- **Status:** active
- **Record:** 2026-11-28, audit card EMULATE, approved.

#### R-old-gate-historical | The old gate is history
- **Rule:** The humanization gate written from September to early November is historical: each of its sections points to the rule here that covers its topic, and nothing in it blocks work. Three leftovers go with it: a lesson's headline says its correction, not the instruction he corrected; the numbered list of suggestions is replaced by the marking page; the August lesson contract for the somatic lane is historical.
- **Why:** Joel, 2026-11-21: "my approach requires not even thinking about pangram at first" Joel, 2026-10-25: "way too dificult, you're giving me half suggestion that are out of context"
- **Checked by:** judgment.
- **Stages:** start
- **Links:** goes with R-tree-is-home; goes with R-check-rewrite-once; goes with R-emulate-retired
- **Replaces:** audit cards OLD-GATE (clusters C32 to C34 and the stale list), C27; HUMANIZATION-GATE.md "Status: ACTIVE"; "the working humanization gate" in docs/INDEX.md; audit card LEFTOVERS; lesson gut-2026-11-06f's headline; the numbered list in CLARITY-READ.md; the task-time lesson contract in docs/INDEX.md
- **Status:** active
- **Record:** 2026-11-28, audit cards OLD-GATE and LEFTOVERS, approved, with his note on OLD-GATE: "can merge with some other rules"

## Words

What each term the rules use means.

- **lane:** one working session on one article or task, with its own branch of the repository.
- **main, the shared copy:** the one version of the repository that every lane starts from and feeds back into.
- **card:** one suggestion or question put to Joel, with Approve, Reject and Revise and a comment box.
- **round:** one marking page sent to Joel and his answers coming back.
- **marking page:** the whole article as a page, each suggestion highlighted where it applies, with its card under the paragraph.
- **Pangram:** the AI-text detector his articles have to pass.
- **window:** a stretch of text that Pangram scores on its own; one check returns a result for each window.
- **confidence:** how sure Pangram says it is about a window: High, Medium or Low.
- **Human High:** a window Pangram reads as human-written with High confidence; the aim for every window.
- **try:** one version of a paragraph sent to Pangram.
- **near miss:** a try in which at least one window read Human.
- **lineage:** one paragraph's tries in order, from the first version to the latest.
- **budget:** how many tries a paragraph gets before the editor stops and asks.
- **the ledger:** the record of Pangram checks: every text checked, what was predicted, and each window's result.
- **receipt:** the short note of the sense read made before a Pangram try.
- **fresh reader:** a model given only the text and a brief, with nothing from the conversation, so it reads as a new reader would.
- **tell:** a word or shape that makes text read as AI-written.
- **human tell:** something a model tends not to write, taken from real human writing.
- **human tell attempt:** a human tell the editor wrote in the author's style, waiting for the author to approve, reject or change it.
- **the linter:** the program that scans a text for known tells and warns or blocks.
- **keep-as-is list:** each article's lasting list of what Joel said stays exactly as it is.
- **fidelity keys:** the facts in a passage that must survive a rewrite (a number, a name, a condition, a citation), and the check that they did.
- **gate:** an older rule that blocked work until a check passed; also a numbered entry in the old gate.
- **the old gate:** the long humanization rule file written from September to early November, now historical.
- **lesson:** a rule learned from one of Joel's fixes or corrections, with his words and the date.
- **way:** one of the ways his fixes read differently from the drafts he fixed.
- **Substack draft route:** the free way to check a long text: a temporary draft, opened through a preview link, on which Joel runs his Pangram extension.
- **preview link:** the secret link that opens a Substack draft as a paying subscriber would see it.
- **API:** the paid interface through which a program sends text to Pangram.
- **GUI, web app:** Pangram's own website, where checks use his account's credits.
- **hack:** a change made only because it moves Pangram, with no gain for the reader.
- **gloss:** a short explanation of a term.
- **payoff:** what the reader gets from a sentence or paragraph, the reason to read it.
- **overcompletion:** explaining again something that is already explained.
- **anchor link:** a link to one section of an article.
- **contents:** an article's table of contents.
- **model text:** words a model drafted, including ones Joel later humanized.
- **Emulate:** a rewriting tool used earlier on his articles, now retired.
- **mailbox:** the places where messages and suggestions for a lane wait.
- **minimal pair:** two versions of a text that differ in one change, checked one after the other to show what that change does.
- **harm reduction:** advice that warns against a dangerous way of doing something people may do anyway.
