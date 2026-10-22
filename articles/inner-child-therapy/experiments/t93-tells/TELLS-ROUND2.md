# Round 2's AI windows: the tells, and what I took out (turn 93)

Joel, 2026-10-22 19:01 UTC, his answer to question 83: "i don't mind helping but as usual i like you to try yourself IF you know what looks like AI tells, then i can help you if you can't find the AI tells. so far your human tells have not been very good most times."

So this pass only takes things out. For each window that read AI in round 2 (checks t90s_A and t90s_B, the feed pages read again on 2026-10-22 for each window's words and confidence), I named the tell from the list in `docs/HUMANIZATION-GATE.md` ("What Pangram 4.1 flagged"):

- wry quips and joke similes;
- aphorisms and balanced closers;
- follow-ups that restate, sum up or reassure;
- explanations in parallel or signposting form, lists included;
- a generic "you" scenario;
- words on the risk lists.

Then I cut the tell, or said its point once in a plain clause. Nothing was added: no new asides, jokes, emojis or examples. Joel's words are proposals only (question 84 on `OWNER-QUESTIONS.md`). The lint ran on each changed paragraph against the article before the change. All are REVIEW or CLEAR, and the four first FAILs were reworded (below). The owner-edit check is at 181 passed, 0 failed.

**A correction.** Turn 92 told Joel that Two Common Guarding Patterns P1 read Human after its rework. It didn't. Window 207 (High, 95 words) covers it and the start of P2. Turn 92's list of window openings missed 207, 213 and 215, and that's where the mistake came from. `ROUND2-AI-WINDOW-BEGINS.json` has those three added now. `experiments/t92-results/CORRECTION-T93.md` corrects `ROUND2-RESULTS.json`, which stays as recorded. What the turn-90 rework did fix: Chicken-and-Egg P15, When to Change the Strategy P3 and P4, If You Want to Kill Yourself P6 and P7, Borrowed Adulthood P1 and The Inner Guide P5, plus three of the five Schema Hacks additions.

## What the cuts drop

These are points, not just words. Each one was inside a tell, so I cut it. Any of them can go back in another shape:

- "I wouldn't argue with the feeling" (Don't Give the Inner Adult Away P7);
- "Laugh if it's funny", meaning don't ban the jokes (P8);
- "before any imagery" (Before You Try to Go Deep P2);
- "really are trying to protect you" (Two Common Guarding Patterns P1; P2 still says they started out guarding you);
- GPT's three caveats on the Schema Hacks additions:
  - real responsibilities;
  - someone being upset isn't proof you hurt them;
  - you still won't know how they'll take it.

## Joel's words: the tells I'd fix, for his OK (question 84)

1. **Don't Give the Inner Adult Away P9**, "Borrow adulthood. Do not surrender it." (Low 18, with the next section's first question). It's a two-beat maxim that restates the heading. My pick: cut it.
2. **Before You Try to Go Deep P1** (Medium 17, Low 19, Low 26, from "Try looking" on). One sentence packs a list of four checks, and the last sentence ends on a catch-all ("or to do whatever helps you come back a bit"). My pick: cut the catch-all. The list is the content, so it stays.
3. **Your Body Might Need Some Love First P5** (Medium 25 on "A lot of the time you just know.) If you honestly can't tell yet, I wouldn't rush to call it healing or harm."). "A lot of the time you just know." is a reassurance, and it's my words from turn 38 that your paste kept. My pick: cut it.
4. **Use Childhood Photographs Gently P1** (High 40, its first two sentences). The opener "Maybe you've tried picturing your little one and thought, ..." is a made-up reader scenario, and an explanation follows it. My pick: "If picturing your little one feels fake, like you're just making it up, a real photo of you as a child can help, since there's no face or posture to invent." If it happened to you, your own moment would beat both.
5. **Untangling the Belonging Bargains P1** (Low 8 and Low 38, from "Most groups expect some conformity" to "that's the bargain"). Your GPT-deduped words of 2026-10-14 have three tells:
   - a reassuring aside ("which is ordinary");
   - two parallel "might" clauses;
   - a defining closer.

   My pick: cut "Most groups expect some conformity, which is ordinary." Your carried-forward "But if going along means betraying yourself, that's the bargain." stays.
6. **Untangling P3's last sentence** (Medium 19), "Self-differentiation is learning to notice when you're making that trade, and to keep your own ground instead." It's a definition used as a closer. My paragraph right after it read High, though, so this may be spill. My pick: leave it for the next check.
7. **How Much Happiness Do You Know Is Possible? P4** (High 31, its first two sentences). It has a list of three ("A meal can help, and so can a boundary or a kind sentence") and a question that pivots. My pick: drop "or a kind sentence".
8. **Related Clinical Work P1** (Low 65 from the end of the IFS section, High 25 on your last line). The list of ten approaches is mine, from your guide. Your last line is a formal disclaimer built as "rather than X or Y". My pick: cut "or claiming that their research validates it as a package". The list stays.

## Where I can't find a tell (for Joel's help)

- **Four single Low sentences that sit next to the real tells:**
  - "If you can't do that because you're basically the frightened kid, leave the deeper conversation until later." (Before You Try P1);
  - "While you're present and still choosing, stay with it." (Somatic Heart Opening P1);
  - "You ask hard things of it so it can grow, at its own pace." (The Inner Guide P1);
  - "This framework developed through the teachers and collaborators credited below and my own practice." (Related Clinical Work P1).

  I left them, since I think they're read along with their neighbours. If they're still AI next time, they're yours to look at.
- **Two Common Guarding Patterns P3's three ways of handling the expectation** (the pull, going along, insisting you don't need anybody). That's your 77.3 content. I cut the restating bits around it, but the list itself is the tell, and I can't remove it without losing the content. This is the third try.
- **Your Body Might Need Some Love First P4** (Low). I cut its quip. The gym line is a stock analogy, but it sets up your P5's "next few days". "Being present ... doesn't mean it wasn't too much" is a negation, but it's your turn-73 decision. If it still reads AI, it's for you.

## My paragraphs, item by item

The numbers are in the notes beside each paragraph in the article. "Third try" means the paragraph read AI in round 1 and again after its turn-87 or turn-90 rework. Two tries of one way is where the budget rule stops, so these are a different way: they cut the tell instead of rewording it. If a third try still reads AI, that paragraph goes to Joel.

### a01. Don't Give the Inner Adult Away P7 (third try)

- **Round 2:** High 27, Medium 7 and High 18, its last three sentences.
- **The tells:** a general point told as a little scenario ("and suddenly someone's an exception"), a reassuring turn ("I wouldn't argue with the feeling.") and a two-part advice closer.
- **Change:** "all its", "special attention" and "and suddenly" are out, the reassuring sentence is cut, and the advice is one clause.

  Was: A group can do it too, with all its praise and special attention, and suddenly someone's an exception to rules you'd use with anybody else. I wouldn't argue with the feeling. I'd give it a few days before deciding anything big, and check the facts in the meantime.

  Now: A group can do it too with praise, until someone's an exception to rules you'd use with anybody else. I'd take a few days to check the facts before deciding anything big.

### a02. Don't Give the Inner Adult Away P8 (third try)

- **Round 2:** Medium 50, all of it.
- **The tells:** a topic sentence built like P7's "A group can do it too", a sentence explaining the example, and a short knock-down ("Laugh if it's funny.").
- **Change:** The joke is now the first sentence's example; the explanation and the knock-down are cut.

  Was: Humor can sneak things past you too. "Ha, I'll just borrow your card, kidding... unless?" is a joke and a request at the same time. Laugh if it's funny. But if saying yes would cost you money, I'd answer it like they'd asked you straight out.

  Now: A joke can carry a request, like "Ha, I'll just borrow your card, kidding... unless?" If saying yes would cost you money, I'd answer it like they'd asked you straight out.

### a03. Before You Try to Go Deep P2 (first try)

- **Round 2:** Low 51 and High 40, from "If you can't" on.
- **The tells:** a then-and-now reframe closing on a balanced contrast ("instead of giving up on them") and a reassuring closer ("Even just ... counts.").
- **Change:** The contrast is cut, and the eyes-open hello is the gentler thing.

  Was: Now there's a grown-up around who can say, "Okay, that's enough for today," and try something gentler instead of giving up on them. Even just saying hi to them with your eyes open, before any imagery, counts.

  Now: Now there's a grown-up around who can say, "Okay, that's enough for today," and try something gentler, like saying hi to them with your eyes open.

### a04. Before You Try to Go Deep P3 (first try)

- **Round 2:** Medium 25, High 32, Medium 9, High 21 and Medium 9, all of it.
- **The tells:** two follow-ups that reassure or explain ("A couple of lines on your phone is plenty.", "After a while away, it gets hard to remember."), a "So" summary and an either-or closer.
- **Change:** The two follow-ups are cut, and the last two sentences are one.

  Was: If you do need one, I'd jot down why, and how far you'd gotten before it got to be too much. A couple of lines on your phone is plenty. After a while away, it gets hard to remember. So once that reason has changed and you want to come back, the note tells you where it was still okay. I'd start there, or somewhere a bit gentler.

  Now: If you do need one, I'd jot down why, and how far you'd gotten before it got to be too much. Once that reason has changed and you want to come back, start where the note says it was still okay, or a bit gentler.

### a05. Before You Try to Go Deep P4 (first try)

- **Round 2:** Low 74, all of it.
- **The tells:** a question answered with a short knock-down ("I really don't think so."), an aphorism that restates the first sentence ("waiting just means more of being alone") and a "So" closer.
- **Change:** The question and its knock-down are one plain sentence of mine, and the aphorism is cut.

  Was: Do you have to get yourself sorted out first, so you'll be better company? I really don't think so. If the hurt was being alone, waiting just means more of being alone. So I'd call somebody or show up somewhere, mess and all.

  Now: I wouldn't wait until you've got yourself sorted out. So I'd call somebody or show up somewhere, mess and all.

### a06. Your Body Might Need Some Love First P4 (first try)

- **Round 2:** Low 115, from its second sentence into his P5.
- **The tells:** a quip ("or stuff you'd rather never have met").
- **Change:** It's cut; the rest of the window is his P5.

  Was: This kind of work can bring up grief and fear, and sometimes hard dreams, or stuff you'd rather never have met.

  Now: This kind of work can bring up grief and fear, and sometimes hard dreams.

### a07. Borrow One Competency at a Time P9 (first try)

- **Round 2:** Low 12, Low 15, Medium 19 and High 30, all of it.
- **The tells:** wry quips ("Which, fair enough, you did take a while.", "two six-year-olds arguing") and a wry closer (the eye-roll).
- **Change:** All three are cut; his 😜 and the hearing-it-out line (2026-10-14) stay.

  Was: More like "Oh, so NOW you care?" Which, fair enough, you did take a while. Your first instinct might be "But I'm trying!", and then it's just two six-year-olds arguing. Some days, just hearing it out like a decent adult is the only thing you'll manage to borrow, and your little one might still roll their eyes at you. 🙄

  Now: More like "Oh, so NOW you care?" Your first instinct might be "But I'm trying!" Some days, just hearing it out like a decent adult is the only thing you'll manage to borrow.

### a08. Borrow Hindsight P1 (third try)

- **Round 2:** Low 83, all of it with P2's start.
- **The tells:** a reassuring gloss ("makes the whole thing feel less lonely") and a wry follow-up ("They've only lived a little longer than you.").
- **Change:** Both are cut, and the gospel point joins the gloss; his question is unchanged.

  Was: It's a question borrowed from your future self, and sometimes just asking it makes the whole thing feel less lonely. I wouldn't take their answer as gospel, though. They've only lived a little longer than you.

  Now: It's a question borrowed from your future self, and I wouldn't take their answer as gospel.

### a09. Borrow Hindsight P2 (third try)

- **Round 2:** High 16, Medium 6 and Low 13.
- **The tells:** an either-or pair ("kind about it, or maybe they'd just") and a rhetorical question opening the next step ("Can't picture them at all?").
- **Change:** One option, and the question is a plain "if".

  Was: Maybe they'd be kind about it, or maybe they'd just make you some food. Can't picture them at all? Then make the food yourself, and don't bother faking a feeling first.

  Now: Maybe they'd just make you some food. If you can't picture them, make the food yourself, and don't bother faking a feeling first.

### a10. Just Like Me P1 (first try)

- **Round 2:** Low 26, Low 2 and Low 21, its first four sentences.
- **The tells:** a script's step-by-step beat ("Name the feeling plainly. Lonely, say. Then think...", E64).
- **Change:** The steps are one sentence.

  Was: This one works best on a steadier day, when thinking about other people won't pull you out of your own shoes. Name the feeling plainly. Lonely, say. Then think of how many people are feeling that exact thing right now, and wanting it to stop, just like you.

  Now: On a steadier day, when thinking about other people won't pull you out of your own shoes, name the feeling plainly (lonely, say) and think of how many people are feeling that exact thing right now, and wanting it to stop, just like you.

### a11. Just Like Me P2 (first try)

- **Round 2:** Low 8 and Low 29, its last three sentences.
- **The tells:** a parallel negation ("isn't part of it, and neither is") and a wry closer ("if it ever comes").
- **Change:** The negation pair is one plain sentence, and the closer is cut.

  Was: Forgiving them isn't part of it, and neither is picturing their childhood. Getting in touch is a separate decision, for a much calmer day, if it ever comes.

  Now: I'd leave out forgiving them and picturing their childhood. Getting in touch is a separate decision, for a much calmer day.

### a12. The Parent You Inherited P4 (first try)

- **Round 2:** Low 85, all but its last sentence.
- **The tells:** a stock frame ("it helps to") and a wry aside ("(it doesn't have to be a flattering name)").
- **Change:** Both are out.

  Was: If answering the voice feels disloyal, it helps to give it a name of its own, like the Critic (it doesn't have to be a flattering name), so you're arguing with what it says and leaving your parents out of it.

  Now: If answering the voice feels disloyal, give it a name of its own, like the Critic, so you're arguing with what it says and leaving your parents out of it.

### a13. Start With Whatever Showed Up P8 (third try)

- **Round 2:** Low 22, High 27 and Medium 36, from "Roughly" on.
- **The tells:** a signposted checklist ("they'd ask two things." and two questions), a two-step instruction ("so listen to it, and then let your head check it") and a balancing closer ("I wouldn't let either one decide by itself").
- **Change:** Kahneman and Klein's two conditions are one sentence, and the tired head now says why neither decides alone.

  Was: Roughly, they'd ask two things. Is this the kind of situation that's predictable at all? And have you been in it enough times to learn it? A hunch might be catching something real that your head hasn't put into words yet, so listen to it, and then let your head check it. I wouldn't let either one decide by itself, though. Your head can get tired of not knowing and be glad to hand the whole thing over, to a hunch or to somebody who sounds sure.

  Now: Roughly, they'd ask whether the situation is predictable at all, and whether you've been in it enough times to learn it. A hunch might be catching something real that your head hasn't put into words yet, and your head can check it, unless it's tired of not knowing and glad to hand the whole thing over, to a hunch or to somebody who sounds sure.

### a14. Start With Whatever Showed Up P9 (first try)

- **Round 2:** Low 7, High 37, Low 18, Medium 27, High 21 and Medium 39, all of it.
- **The tells:** a signpost opener ("the same kind of listening"), a colon list, two-step advice ("hear it out and then go see"), a quip ("(Or they do, and you survive it.)") and a balanced pair ("and find out how right it was later").
- **Change:** Each is cut, with one example of the guess, and the danger and the doctor are one sentence.

  Was: Anxiety deserves the same kind of listening. A lot of the time it's a part of you that's trying to protect you, making a guess about what's coming: that you'll get overwhelmed, maybe, or that people will laugh at you. It can be right! It's probably been wrong before too, and you know some of those times. So when it's safe to find out, I'd hear it out and then go see. Maybe nobody laughs. (Or they do, and you survive it.) If it might be real danger, though, I'd get some distance first, and find out how right it was later. Same with something a doctor should look at.

  Now: Anxiety is often a part of you that's trying to protect you, making a guess about what's coming, like that people will laugh at you. It can be right! It's probably been wrong before too, and you know some of those times. When it's safe to find out, I'd go see. Maybe nobody laughs. If it might be real danger, though, or something a doctor should look at, I'd deal with that first.

### a15. Start With Whatever Showed Up P10 (first try)

- **Round 2:** Medium 39, High 21 and Medium 23, all of it.
- **The tells:** two parallel conditionals ("If ..., that's enough to stop. And if ..., I'd stop there too.") and a tidy follow-up.
- **Change:** They're one sentence.

  Was: If a part hesitates about being touched or about sex, that's enough to stop. And if it says no to going deeper in this work, or to an altered state, I'd stop there too. It might not be able to tell you why.

  Now: When a part hesitates about being touched or about sex, or says no to going deeper in this work or to an altered state, I'd stop, even if it can't tell you why.

### a16. Two Common Guarding Patterns P1 (third try)

- **Round 2:** Medium 23 and High 95, all of it, into P2 (turn 92 reported it fixed; that was wrong).
- **The tells:** an enumeration signpost that repeats the heading ("Two kinds of reaction...", "The first one") and a doubled "again, or ... again".
- **Change:** The first sentence is cut, and it starts "One is a skeptic".

  Was: Two kinds of reaction really are trying to protect you, more often than not. The first one is on duty all the time, and it can sound like a skeptic: "You're just making this up." It may have spent years keeping you from being humiliated again, or left again,

  Now: One is a skeptic, on duty all the time: "You're just making this up." It may have spent years keeping you from being humiliated or left again,

### a17. Two Common Guarding Patterns P2 (third try)

- **Round 2:** High 95 (its start), Medium 17, Low 5, Low 11, Low 15, High 23 and Medium 21.
- **The tells:** a short empathic knock-down ("I'd want out too.") and a "like X, or like Y" pair.
- **Change:** Both are cut; his yawn and Re-evaluation Counseling, "The skeptic and the pull both" and the part's "See? I knew it" stay.

  Was: Maybe it doesn't believe there's a grown-up around who could handle what's coming. I'd want out too. That yawn … If you treat either one like an enemy, or like proof that something's wrong with you, it'll probably just think "See? I knew it," and stay in charge.

  Now: Maybe it doesn't believe there's a grown-up around who could handle what's coming. That yawn … If you treat either one like an enemy, it'll probably just think "See? I knew it," and stay in charge.

### a18. Two Common Guarding Patterns P3 (third try)

- **Round 2:** Medium 21, High 68 and Medium 22, all but its last line.
- **The tells:** a follow-up that restates ("You just expect it") and a summary signpost ("So with any of these").
- **Change:** Both are cut. The three ways of handling the expectation stay (his 77.3).

  Was: You probably never said it to yourself in words. You just expect it, and it steers you before you know why. … So with any of these, I'd ask what it's protecting you from

  Now: You probably never said it to yourself in words, but it steers you before you know why. … With any of these, I'd ask what it's protecting you from

### a19. Two Common Guarding Patterns P4 (third try)

- **Round 2:** Low 52, from "Then nobody offers" on.
- **The tells:** a reassuring reframe and a tidy closer ("I'd just notice whether that's still true now.").
- **Change:** One sentence says what keeping quiet costs now.

  Was: Keeping quiet might have been the smartest thing you could do back then, with nobody safe to tell. I'd just notice whether that's still true now.

  Now: Keeping quiet might have been the smartest thing you could do back then, with nobody safe to tell, but now it can keep help away.

### b01. Untangling the Belonging Bargains P4 (second try)

- **Round 2:** High 46, Medium 16 and Low 13, all of it.
- **The tells:** a word on the risk list ("quieter"), a concession ("and that's worth sorting out"), a balanced contrast ("isn't help, though it can feel like loyalty") and a hedge ("doesn't by itself mean", O43).
- **Change:** The paragraph is the bargain itself, so his 82a paragraph after it has its "That's exactly why" pointing at the bargain; the small good thing is one sentence after his paragraph.

  Was: Some families run on a quieter bargain: "If I'm happy while someone I love is suffering, I'm abandoning them." You might really owe them help, and that's worth sorting out. Being miserable alongside them isn't help, though it can feel like loyalty. I'd try a small good thing, like a nice meal, and see what actually happens. Someone getting upset about it doesn't by itself mean you hurt them.

  Now: Some families run on a bargain like "If I'm happy while someone I love is suffering, I'm abandoning them."

### b02. Let the Child Be Bad at Things P3 (first try)

- **Round 2:** Low 56, from "Either way" into The Inner Guide P1.
- **The tells:** a wry closer ("You might catch yourself wondering when you became someone who does this.").
- **Change:** It's cut.

  Was: Either way, that's pl/ork in its most literal form: play becomes part of forming your identity. You might catch yourself wondering when you became someone who does this.

  Now: Either way, that's pl/ork in its most literal form: play becomes part of forming your identity.

### b03. The Inner Guide P1 (first try)

- **Round 2:** Low 56, Low 27 and Low 14, to "at its own pace".
- **The tells:** a balanced maxim ("keep the standard and drop the tone").
- **Change:** It's cut; the sentence before it says it.

  Was: Your parent's harsh tone doesn't come with the job, though. If you hear it coming out of you, keep the standard and drop the tone.

  Now: Your parent's harsh tone doesn't come with the job, though.

### b04. The Inner Guide P4 (third try)

- **Round 2:** Medium 65, its last three sentences.
- **The tells:** a second offered example ("Or maybe, ...") and a second instruction nested in the last one ("and if you need a minute, say when you'll be back").
- **Change:** Both are cut.

  Was: I'd try croaking to someone you trust, "Could you pick up some soup?" Or maybe, "I'd really like to just watch a movie with you." If you keep swinging between spoiling and clamping down, try staying warm while you say what happens next, like "Not now, we'll go after lunch," and if you need a minute, say when you'll be back.

  Now: I'd try croaking to someone you trust, "Could you pick up some soup?" If you keep swinging between spoiling and clamping down, try staying warm while you say what happens next, like "Not now, we'll go after lunch."

### b05. How Much Happiness Do You Know Is Possible? P3 (third try)

- **Round 2:** Medium 39, its last sentence.
- **The tells:** three instructions chained in one sentence.
- **Change:** Two sentences, with "If you meet".

  Was: Read people from different traditions, and if you get the chance, spend time around someone who's happy in a way that doesn't add up, and see how they treat people when their own day is going badly.

  Now: Read people from different traditions. If you meet someone who's happy in a way that doesn't add up, see how they treat people when their own day is going badly.

### b06. How Much Happiness Do You Know Is Possible? P5 (first try)

- **Round 2:** Low 28, its last two sentences.
- **The tells:** an aphorism closer that repeats the quote ("the limits ... are the limits").
- **Change:** It's cut.

  Was: But what if the experience is possible for me?" Don't assume the limits of what you've felt so far are the limits of what's possible.

  Now: But what if the experience is possible for me?"

### b07. Somatic Heart Opening P1 (first try)

- **Round 2:** Low 13, Low 30, High 32 and Low 10, to "stay with it".
- **The tells:** an aphoristic turn ("from the other side") and a reassuring negation ("and that doesn't mean the love failed").
- **Change:** Both are cut; the guide's Rumi line stays.

  Was: Being loved can open grief from the other side, too. Someone takes care of you, and you think, "Why does this make me sad?" It can be sadness for the care that was missing, and that doesn't mean the love failed.

  Now: Being loved can open grief, too. Someone takes care of you, and you think, "Why does this make me sad?" It can be sadness for the care that was missing.

### b08. When the Practice Feels Real but Stays Shallow P1 (first try)

- **Round 2:** Low 47, its last two sentences.
- **The tells:** a tidy closer ("before you write off the whole thing").
- **Change:** It's cut; his night line is unchanged.

  Was: And if nightmares start wrecking your sleep, do less of the practice, earlier in the day or for a shorter time, before you write off the whole thing.

  Now: If nightmares start wrecking your sleep, do less of the practice, earlier in the day or for a shorter time.

### b09. Write It. Don't Send It Yet. P7 (second try)

- **Round 2:** Low 18, Low 15 and Low 18, all of it.
- **The tells:** a hedged closer ("I still won't know how they'll take it, but it might change a word or two.").
- **Change:** It's cut.

  Was: What felt scared when I wrote it can read like a threat from over there. I still won't know how they'll take it, but it might change a word or two.

  Now: What felt scared when I wrote it can read like a threat from over there.

### b10. How This Relates to IFS P7 (first try)

- **Round 2:** Low 65, its last two sentences, into Related Clinical Work.
- **The tells:** a wry fragment tacked on ("Or safer, for that matter.").
- **Change:** One clause.

  Was: Having a big institute with certifications behind it doesn't make a model any truer, either. Or safer, for that matter.

  Now: Having a big institute with certifications behind it doesn't make a model any truer or safer.
