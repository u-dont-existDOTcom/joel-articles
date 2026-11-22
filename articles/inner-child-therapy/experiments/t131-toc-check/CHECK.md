# Fable's check of the sidebar headings (2026-11-17, turn 131)

Joel, 2026-11-17 18:07 UTC, in the chat that ran turn 130, now set to Fable 5.2: "Check now with fable"
([his message](../t131-answers/JOEL-20261117-1807.md)). Turn 130 was Opus 5.5's: the contents of the Inner Child guide as
Substack's narrow sidebar shows it, three renamed versions, a reader test and a pick ([RESULTS.md](../t130-toc/RESULTS.md)).
This is Fable's check of that work.

## In short

- **Opus's pick holds up.** It had never been read as a whole. Read now by three fresh readers, it sent them to the
  right section first on 53 to 55 of 68 situations; your sidebar as it is today, 44 to 48.
- **Renaming helps more clearly than turn 130 showed.** Every renamed contents beat your current sidebar with every
  reader, on the old situations and on 30 new ones written by an agent that had seen only the guide's text.
- **Which renamed version you take doesn't change the score.** Opus's, GPT's and three versions of Fable's all land
  between 52 and 58. The choice between them is about your voice.
- **Fable's pick is Opus's pick with 39 headings changed and one small heading added.** Most changes keep more of your
  own words; five answer something the readers showed; 12 change only in their capitals.
- **Your order stays.** You reorganized the guide yourself between 4 and 14 November, and readers found things in it.
  I'd change one level and add one heading, nothing else.

The page with every option, where you pick heading by heading: https://claude.ai/artifact/RjHcYbik7oU9VdHcru1tB6
(built by [make_page.py](make_page.py) from [PAGE-OPTIONS.json](PAGE-OPTIONS.json); a view of [OPTIONS-PAGE.html](OPTIONS-PAGE.html)).

## "Check now": what was waiting on you

- **Your heading picks:** the page's store had no saved answers when I looked (18:08 UTC). If you picked in your
  browser, press Copy my answers and paste them in the chat. Anything saved there is kept by the new page.
- **Your live post:** changed today at 16:55 UTC in two paragraphs (in Mo' Money, Mo' Problems and in Before choosing a
  therapist). All 151 headings (147 of them listed in the sidebar) and their levels are as they were on 16 November, so
  the test below is on your current contents.
- **Pull request 438** (turn 129, the article chat) is still open, with no comments.

## What I checked in Opus's work

1. **Its numbers.** Recomputed from the nine saved reads: the table in RESULTS.md matches [SCORES.json](../t130-toc/SCORES.json).
2. **Its pick.** PROPOSAL-PICK.json mixed Opus's tested version with 17 of GPT's headings, and nobody had read the mix.
   That is the main gap, and the test below closes it.
3. **Its test.** Opus wrote the 38 situations and their answers, then drafted its own contents knowing them (it said so).
   So this time a Sonnet agent that saw only the guide's text, with every heading taken out, wrote 30 new situations
   ([SITUATIONS-HELDOUT.json](SITUATIONS-HELDOUT.json)). A second agent read the whole guide against all 68 for answering
   sections the keys had missed; I checked each of its quotes in the text and, before any reader ran, added ten
   sections to the old key and seven to the new one, and took one out of the new one
   ([EXPECTED-REVIEWED.json](EXPECTED-REVIEWED.json), [CHECKER-REPORT.json](CHECKER-REPORT.json)). On the old 38, the
   additions changed no reader's first-pick score.
4. **Every renamed heading against the section's text and your keep-as-is list.** What I'd change is in the tables below.
   One heading in Opus's pick finishes a sentence you asked to keep (K3, "...so that you:" running into Don't Sell Your
   Inner Adult To Buy An Outer Adult), and one changed a meaning ("Let the Child Be Bad", from bad at things).
5. **Two of GPT's headings in the pick that pull readers to the wrong section.** Opus's own results said GPT's quote
   heading "“No. I Hate Myself.”" had pulled both readers of another case away; it took the heading anyway, offering "If
   You Hate Yourself" in a note. This run shows the same pull for it, and a stronger one for GPT's "Shame Says “Unlovable”".
6. **Its process.** Three misses, fixed or recorded here: the question for you never went onto the lane's
   [questions page](../../OWNER-QUESTIONS.md) (it's there now as question 111); the keep-as-is list wasn't run against the
   renames; and two reader files were finished by Opus after a safety layer cut them (below).

## The test

Fresh readers (Sonnet agents) each saw one contents, exactly as the sidebar shows it: one line per heading, indented by
level, cut off with "…" where the room ends, no word counts. They saw the 68 situations in one mixed order
([SITUATIONS-MIXED.json](SITUATIONS-MIXED.json)) and named, for each, the line they'd open first, sure or a guess, and
the next. [make_reader_files.py](make_reader_files.py) writes what they saw; their replies are saved as they came back
in [reads/](reads/); [score_lines.py](score_lines.py) scores them by section id into [SCORES.json](SCORES.json).

| Contents | Readers | First pick right, of the 38 from turn 130 | of the 30 new | of all 68 | Guesses, of 68 | Right by the 2nd pick, of 68 (keys with the checker's additions) |
|---|---|---|---|---|---|---|
| Yours, as the sidebar cuts it today | 3 | 27, 28, 29 | 17, 20, 18 | 44, 48, 47 | 33, 32, 32 | 52, 52, 49 |
| Opus's pick | 3 | 33, 32, 32 | 22, 21, 21 | 55, 53, 53 | 31, 30, 28 | 58, 59, 56 |
| GPT's | 3 | 30, 32, 32 | 22, 22, 22 | 52, 54, 54 | 30, 35, 42 | 59, 59, 58 |
| Fable's, first version ([PROPOSAL-FABLE.json](PROPOSAL-FABLE.json)) | 3 | 34, 34, 33 | 20, 20, 21 | 54, 54, 54 | 26, 30, 28 | 57, 59, 57 |
| Fable's, four changes after those readers ([PROPOSAL-FABLE2.json](PROPOSAL-FABLE2.json)) | 3 | 33, 34, 34 | 22, 24, 22 | 55, 58, 56 | 27, 27, 24 | 59, 60, 60 |
| Fable's, one more change ([PROPOSAL-FABLE3.json](PROPOSAL-FABLE3.json)) | 3 | 32, 32, 31 | 21, 23, 22 | 53, 55, 53 | 26, 27, 30 | 60, 60, 58 |

What it shows:

- **Renamed against yours:** about 54 of 68 against about 46. The cases the renames won for every reader who saw them:
  getting a kick out of frightening people (When You're the Danger), have I grieved it enough (Healing or Checking?),
  social media (Social media hooks too), a session that stayed on the surface (Real but Shallow?). None or one of your
  three readers found each of those.
- **Between the renamed versions: nothing three readers can tell.** Fable's last two versions differ by one heading and
  landed three apart. Readers of the same contents also agree with each other more than three people would, since they
  are the same model, so a 3-of-3 on one situation is weaker than it looks. Opus's and Fable's readers split 0 to 3 on
  the strict-church case, though the two headings they chose between read the same in both contents.
- **Against turn 130:** your sidebar scored lower here on the same 38 situations (27 to 29, against 31 and 32). The
  readers' task changed (no word counts, answers by line number, 30 more situations mixed in), so compare within this
  run, not across the two.

Limits: the readers are AI models reading a contents, not people with a real problem; three per contents; Fable's
second and third versions were changed after seeing the first readers' misses, so they are flattered on those cases.

## Fable's pick

[PROPOSAL-FABLE-FINAL.json](PROPOSAL-FABLE-FINAL.json): the third version, with Between Spoiling and Clamping Down back
on Opus's "Spoil or Clamp Down?" (leaving it whole didn't help: 3 of 6 found the snacks-and-shows case, against 3 of 9
with the rename; on your current sidebar all 3 did, and nearly every miss went to The Urge to Escape). 140 of 147 fit,
3 fit with about one letter to spare, and 4 are left whole on purpose. It renames 102 of your headings; Opus's pick, 105.

The rule I held Opus's renames to: where the sidebar cuts your heading but the part still showing carries the point,
or the full phrase is the point, leave it. Where it has to be shorter, use your own words and your own capitals.
Use new words only where yours can't fit, and say so.

### Five changes that answer what readers did

| Yours | Opus's pick | Fable's pick | Why |
|---|---|---|---|
| Notice the Part That Came Here | “No. I Hate Myself.” | **If You Hate Yourself** | Not your words. The section opens with the reader who answers "No. I hate myself", and it sits under Your Body, which it isn't about, so it moves up a level (GPT's version and Opus's pick did the same). All 9 readers who saw this heading found the hate-yourself case under it, and none of them took the "I don't believe you" case there. GPT's quote heading, which Opus took, was found as well (6 of 6) but pulled 5 of 8 readers of the "I don't believe you" case over the two runs. Your own words, kept short, would be "The Part That Came Here". |
| Shame can make you feel unlovable | Shame Says “Unlovable” | **When Shame Gets Stuck** | Your phrase from the section ("Shame becomes toxic when it gets stuck"). GPT's "Shame Says “Unlovable”", which Opus took, pulled all 12 readers who saw it to this section for the someone-stopped-loving-you case, which belongs to Worthy of Love. Always. With this heading none of 3 came here for it (1 found the conclusion; on your sidebar as it is, 2 of 3 did), and all 3 still found the kept-a-secret case here. |
| A Healthy Mind Is Not a Perfect Mind | Ugly Thoughts Happen | **Healthy Mind, Not Perfect** | Your saying, shortened, with one small heading added under it (next card). The section holds two things, and one heading found only one of them: under Opus's "Ugly Thoughts Happen" alone, all 6 readers found the ugly-thought case and none of 6 the putting-off-decisions case; under GPT's "Healthy, Not Perfect" it was none of 3 and 3 of 3. With both headings: 6 of 6 and 5 of 6. Fits with about one letter to spare. |
| If Someone Has Actually Hurt or Threatened You | If Hurt or Threatened | **Really Hurt or Threatened** | Your "Actually" told real danger from a hurtful comment. Without it (Opus's "If Hurt or Threatened"), 2 of 6 readers with a hurtful comment online came here before Write It. Don’t Send It Yet.; with "Really", your word two headings down, none of 6 did. ("Actually Hurt or Threatened" is cut by half a letter.) Fits with about one letter to spare. |
| When One Life Has Ended and the Next Hasn’t Begun | When One Life Ends | **When Your Old Life Ends** | One word of mine ("Old"). Four readers said on their own that they couldn't tell a death from a breakup: two reading Opus's "When One Life Ends", one reading your heading as the sidebar cuts it, and one reading your words cut at "and". None of the 6 who saw this one said so, and all 6 found the breakup case (here or under Missing Someone). Your exact words, cut at "and", would be "When One Life Has Ended". |

And the heading to add: **Ugly Thoughts Happen**, one level under Healthy Mind, Not Perfect, above the paragraph that
starts "Forced adulthood can get into your head too". It would be the only heading in the pick that isn't in your post.

### Three left whole on purpose

| Yours | Opus's pick | Fable's pick | Why |
|---|---|---|---|
| Don’t Sell Your Inner Adult To Buy An Outer Adult | Don’t Buy an Outer Adult | **Don’t Sell Your Inner Adult To Buy An Outer Adult** | Left whole on purpose. The sentence above it runs on into this heading ("...so that you:"), which you asked to keep (keep-as-is K3), and the sidebar's own cut already reads "Don’t Sell Your Inner Adu…". All 9 readers found the teacher-making-your-decisions case with it cut like that (8 here, 1 under Signs of Manipulation). Opus's "Don’t Buy an Outer Adult" drops the selling half of your phrase. |
| You Belong Everywhere and Nowhere | You Belong Everywhere | **You Belong Everywhere and Nowhere** | Left whole on purpose: the sidebar's own cut already reads "You Belong Everywher…", close to Opus's "You Belong Everywhere", and the post keeps your "and Nowhere". |
| Listen To Your Body, Or Else! | Listen to Your Body! | **Listen To Your Body, Or Else!** | Left whole on purpose: the sidebar's own cut reads "Listen To Your Body, Or…", and the post keeps your "Or Else!". All 9 readers found the unexplained-symptoms case here or under Physical Pain. |

("“And So That’s the Way It Happened!”" was already left whole by Opus, for the same reason.)

### Nineteen that keep more of your words

| Yours | Opus's pick | Fable's pick | Why |
|---|---|---|---|
| Your Body Might Need Some Love First | Your Body May Need Love | **Body May Need Love First** | Keeps your "First": the heading is about what comes first. Opus's "Your Body May Need Love" drops it. |
| Borrow One Competency at a Time | One Skill at a Time | **Borrow One Competency** | Your words, cut at "at a Time". Opus's "One Skill at a Time" swaps your word competency for skill. |
| Protecting them from yourself | Protect Them From You | **Protecting them from you** | Your wording and your lower case. |
| Reframing attacks as unskillful attempts to help | Reframe the Critic | **Mr. Rogers’ reframe** | Your own name for it: the text calls it "the Mr. Rogers reframing trick", and Love Can Start Before It's Trusted points back to it by that name. Opus took GPT's "Reframe the Critic". |
| Earning their trust, day to day | Earning Trust Day to Day | **Earning trust, day to day** | Your wording, comma and lower case. |
| Borrow Your Love For Someone Else | Borrow the Love You Give | **Borrow Your Own Love** | Pairs with Borrow Someone's Love above it and fits with room; Opus's "Borrow the Love You Give" fits with under two letters to spare. |
| Show Up When Nothing’s Wrong | Show Up for No Reason | **When Nothing’s Wrong** | Your words, without "Show Up". Opus's "Show Up for No Reason" says something a little different (no reason, where you wrote no problem). |
| Use hindsight to “re-do” traumatic memories in a healthier way | Re-do Trauma Memories | **Re-do traumatic memories** | Your word "traumatic" (Opus took GPT's "Trauma"), your lower case. Borrow Hindsight points to this heading by these words. |
| When the Practice Gets Difficult | When Practice Gets Hard | **When Practice Gets Difficult** | Your word "Difficult" fits; no need for "Hard". |
| Physical Pain Makes It Harder | Pain Makes It Harder | **Physical Pain** | Your first two words. Opus's "Pain Makes It Harder" drops "Physical", the word a reader in pain looks for. |
| Using spiritual attack for spiritual gain | Turn Attack Into Gain | **Spiritual attack for gain** | Your words. Opus's "Turn Attack Into Gain" drops "spiritual". |
| When Escape Leaves Reality Behind | When Drugs Warp Reality | **Leaving Reality Behind** | Your image, kept. Opus's "When Drugs Warp Reality" is plainer but none of it is your wording. |
| Is your paranoia a warning sign? | Paranoia: A Warning? | **Is paranoia a warning?** | Your question, your lower case. |
| Let the Child Be Bad at Things | Let the Child Be Bad | **Let the Child Be Bad at It** | Opus's "Let the Child Be Bad" changes the meaning: bad at things became just bad. This keeps your sentence and fits. |
| First Social Connections, Done Right | Quit the Lovability Tests | **First Connections** | Your heading, shortened. Opus took GPT's "Quit the Lovability Tests", which isn't your wording; your own catchy line in the section is "flunk the tests", so "Flunk the Tests" would be the lively version in your words. |
| Before You Tell the Hardest Stuff | Before Telling Secrets | **The Hardest Stuff** | Your words. Opus's "Before Telling Secrets" brings in "secrets", which the section doesn't say. |
| Ask What Kind of Company They Want | Ask What They Need | **Ask What They Want** | Your word is want ("what kind of company they want"), not need. |
| Before choosing a therapist | Before You Choose | **Before choosing one** | Your words ("Before choosing a therapist"), lower case. |
| Other Folks Also Have Hooks | If They Can’t Hear You | **Other Folks Have Hooks** | Your rhyme kept: only "Also" goes. 7 of 9 readers found the comforting-your-partner case under it. Opus's "If They Can’t Hear You" did as well this time (3 of 3; neither of its 2 readers in turn 130), so this one is about keeping your words, not about finding. |

### Twelve where only the capitals change

Opus capitalized every renamed heading, so "If no answer comes" sat above "If It Tells You to Act". These follow the
capitals of the heading you wrote (two of them, Social media hooks too and My framework’s roots, are still Opus's words).
One reader of Opus's pick remarked on the lower-case headings without being asked. Whether you want one style everywhere
is a question for you (about 30 of your 147 headings are lower-case today).

| Yours | Opus's pick | Fable's pick |
|---|---|---|
| If it tells you to do something | If It Tells You to Act | **If it tells you to act** |
| How should discipline have been done right? | Discipline Done Right? | **Discipline done right?** |
| How many tries would I give it? | How Many Tries? | **How many tries?** |
| If you keep following the reparenting steps correctly without getting the expected results | Right Steps, No Results? | **Right steps, no results?** |
| For some people, reparenting starts feeling real in an altered state | Real in an Altered State | **Real in an altered state** |
| If you might be prone to mania or psychosis | Mania or Psychosis Risk | **Mania or psychosis risk** |
| If you keep coming back from trips confused or spaced out | Spaced Out After Trips? | **Spaced out after trips?** |
| Before you quit a medication or alcohol | Quitting Meds or Alcohol | **Quitting meds or alcohol** |
| Non-altered states can feel like this too | Social Media Hooks Too | **Social media hooks too** |
| Inner Child Reparenting therapists | Reparenting Therapists | **Reparenting therapists** |
| If you want a licensed therapist | Licensed Therapists | **Licensed therapists** |
| Development of my framework | My Framework’s Roots | **My framework’s roots** |

## Who organizes it better (your question of 13 November)

You do. Comparing your 4 November headings with the live post ([HEADINGS-4NOV-VS-LIVE.md](HEADINGS-4NOV-VS-LIVE.md)):
you moved Shame and Forgiveness into The Nurturer, the gratitude sections (Ask God for a Loan, The Joy In Sorrow) from
The Nurturer into The Inner Guide, Physical Pain under The Urge to Escape, the altered-state story into Altered States,
and more. That order is the one the readers used. Turn 130's readers wanted three sections moved that a situation here
tests, and all 18 readers found each where you put it: If You Want to Kill Yourself, When Therapy Stirs Things Up
(under Your Body) and When the Spiritual Relationship Hurts (under The Inner Guide). So I would not reorder anything.
Two small changes:

- **Notice the Part That Came Here: one level up**, out from under Your Body (it isn't about the body). Opus and GPT
  both did this. It sat at the same level under Your Body on 4 November too, so raising it doesn't undo a move you
  have made since.
- **One heading added** (Ugly Thoughts Happen, above).

What your reorganization left behind is four pointers in the text that now name the wrong place; they're listed on the
page and in turn 130's results, and they get fixed when the headings go in.

## What no contents fixed

- **Gratitude.** None of 18 readers looking for a real version of gratitude found Ask God for a Loan; all 18 went to
  The Joy In Sorrow. The word isn't in any heading. Your heading fits and it's yours, so I left it; if you want the
  practice findable from the sidebar, the word has to be in a heading somewhere.
- **"I don't believe you."** For the voice that answers kindness that way, 3 of 18 readers reached a section that
  speaks to it (1 of them Love Can Start Before It's Trusted itself); 9 went to When It Feels Fake.
- **Situations whose keys look too narrow,** so nearly every reader of every contents missed them. The 2 a.m. app:
  all 18 went to The Urge to Escape; the key says Dating While You Heal. Stress eating: 16 of 18 went to The Urge to
  Escape; the key says Remember When You Already Did It Well. Comforting yourself the way a friend does: 1 of 18 right;
  the key says Borrow Someone Else's Love or If the Love Isn't Coming Yet, and 14 of the 15 readers of a renamed contents
  chose the heading between them, Borrow Your Love For Someone Else, which also speaks to it. Worrying what people
  think: 1 of 18 right; 13 went to Belonging Bargains, the heading over the one the key counts.
- **Two new situations nobody found:** still feeling like a small kid when called lazy, after years of meditating (the
  key says My Journey and two other sections; 11 of 18 went to Answering the Strict Disciplinarian), and being moved to
  tears by a kindness (the key says The Joy In Sorrow; 13 of 18 went to Love Can Start Before It's Trusted).
- **The Urge to Escape pulls.** Short and plain, it took first picks from several other sections in every renamed
  contents. I don't have a better name for it.

## The safety-layer cut in turn 130

Two of turn 130's reader agents had their file writes cut by a safety classifier (READ-NOW-FULL-1.md and
READ-NOW-SIDEBAR-2.md). Opus then wrote those two files itself, from what the readers had sent back. UDA's rule
([safety-layer-cuts.md](https://github.com/u-dont-existDOTcom/universal-dev-architecture/blob/main/patterns/safety-layer-cuts.md))
is that a cut is a boundary: say which output was cut and don't produce it another way. This turn's scores don't
depend on those two files, but you should have been told then. This turn
the readers answered in their replies, by line number, and nothing was cut.

## What's next

Your picks on the page, then the headings and the pointer fixes go into your post as one checked change, with your OK.
