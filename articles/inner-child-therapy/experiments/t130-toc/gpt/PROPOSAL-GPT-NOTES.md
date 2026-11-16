# Proposal notes

Proposed: 106 heading renames, one level change, and all 147 current sidebar section IDs retained exactly once in their existing reading order. Forty-one headings keep their wording. No sections move and no headings are dropped. The guide text is unchanged; this is a proposal for headings only.

The adult-building sequence stays Borrow → Protector → Nurturer → Guide. Each section stays with its images and embeds. S010 becomes h2, alongside the body-readiness section: self-hatred is a separate starting obstacle, not a body-treatment subtopic. S041 stays as a short bridge because its opening “This” needs the divine-love heading as its referent; merging it into Goodwill would change what that sentence appears to mean.

## Sidebar measurements

Every final heading, including every unchanged heading, was measured with the supplied `tool/toc_sidebar.py` at its proposed level. Candidates that were cut or tight were revised and remeasured before this version was settled. The final CLI pass read temporary Markdown generated directly from `PROPOSAL.json`; the measurements are preserved below and the temporary files have been removed. Width/room is measured text width against the room at that level, not a character estimate. “Fits” includes the requested 12px spare.

Final: **145 fits, 1 tight, 1 cut**. Running the same tool on the original labels here gives 40 fits, 1 tight, 106 cut; TOC-NOW’s annotations instead give 40 fits, 2 tight, 105 cut. The borderline difference is S058: this run measures its original heading at 217.2/217px. These are supplied-tool measurements, not a new live-browser check.

- S085 deliberately keeps “Listen To Your Body, Or Else!” (207.5/181px). The tool shows “Listen To Your Body, O…”, so the subject survives; only the comic warning is lost. Replacing it just to pass would weaken an explicit voice example in the brief.
- S137 deliberately keeps “Write It. Don’t Send It Yet.” (183.1/193px), with 9.9px spare instead of 12px. It is fully visible at the measured width; a narrower reader may lose its ending. The write/pause rhythm is worth retaining as a flagged exception.

## Changes, one reason per entry

Each row gives the original words, proposed words, reason, and final measurement. S010’s row also records the only level change.

| ID | Level | Original → proposed | Reason | Final width/room; status |
| --- | --- | --- | --- | --- |
| S002 | h2 | “Allow Céline to explain the “inner child:”” → “Céline and the Inner Child” | Brings the inner-child subject into view while keeping Céline attached to her song and the images it introduces. | 182.9/205px; fits |
| S003 | h2 | “The Chicken-and-Egg Problem” → “The Chicken-and-Egg” | Keeps Joel’s metaphor for needing an adult before you can build one; removes the word lost at the sidebar edge. | 157.1/205px; fits |
| S007 | h2 | “Dip Your Toes In Before You Go Deep” → “Dip Your Toes In” | Keeps the kiddie-pool invitation and makes the whole first-step label visible. | 118.2/205px; fits |
| S008 | h2 | “Your Body Might Need Some Love First” → “Body Needs Love First” | Keeps the body-first prerequisite visible instead of losing the remedy. | 160.6/205px; fits |
| S009 | h3 | “When Therapy Stirs Things Up” → “Therapy Stirs Things Up” | Keeps the therapy aftermath recognizable in full by removing the introductory word. | 171.9/193px; fits |
| S010 | h3 → h2 | “Notice the Part That Came Here” → ““No. I Hate Myself.”” | Uses the section’s opening objection so a reader who cannot feel self-love can find the response. Promote h3 → h2 so this independent starting objection is not nested under body care. | 139.9/205px; fits |
| S011 | h2 | “When the Present-Day Adult Is Dangerous to the Child” → “When Cruelty Feels Good” | Names the section’s actual concern, finding scaring or diminishing someone rewarding, rather than leaving the danger hidden; it avoids equating unwanted scary thoughts with malice. | 181.4/205px; fits |
| S012 | h3 | “Ill Will and Loving-Kindness” → “Ill Will & Loving-Kindness” | Keeps both the problem and the practice visible with a smaller conjunction. | 179.0/193px; fits |
| S014 | h3 | “The Spiritual Side of the Question” → “What Self Would Die?” | Uses the section’s central spiritual question rather than the vague “Question.” | 153.5/193px; fits |
| S015 | h3 | “This human life is the most precious opportunity” → “Precious Human Life” | Keeps the Buddhist emphasis on the value of this life while removing the hidden tail. | 147.2/193px; fits |
| S018 | h2 | “Borrow the Adult To Become the Adult” → “Borrowed Adulthood” | Uses Joel’s name for this practice instead of repeating “Adult” across the clipped label. | 146.5/205px; fits |
| S019 | h3 | “Don’t Sell Your Inner Adult To Buy An Outer Adult” → “Borrow, Don’t Sell Out” | Keeps the selling metaphor and borrowing context while exposing the warning against surrendering your own adulthood. | 156.7/193px; fits |
| S021 | h3 | “Borrow One Competency at a Time” → “Borrow One Capacity” | Uses “one capacity” from the text so the small first step survives intact. | 151.4/193px; fits |
| S023 | h2 | “Protecting and Building Trust With Your Little One” → “The Protector” | Makes the first adult role as recognizable as The Nurturer and The Guide; the text still explains protection and trust. | 97.5/205px; fits |
| S025 | h3 | “Making It Intentional” → “Plan Your Protector Act” | Names the actual planning exercise; “It” alone did not say what to open. | 166.7/193px; fits |
| S026 | h3 | “Protecting them from yourself” → “Repair Your Own Attacks” | Uses the section’s repair and internal-attack language to distinguish this from inherited criticism next. | 177.5/193px; fits |
| S027 | h3 | “Protecting from the Parent You Inherited” → “The Parent You Inherited” | Keeps Joel’s term and drops protection already supplied by The Protector parent heading. | 176.8/193px; fits |
| S028 | h4 | “Reframing attacks as unskillful attempts to help” → “Reframe the Critic” | Retains the original reframing task and names its target; Mr. Rogers and the image stay with this example. | 128.2/181px; fits |
| S029 | h3 | “Earning their trust, day to day” → “Earn Their Trust Daily” | Keeps the concrete day-to-day task fully visible. | 153.2/193px; fits |
| S031 | h3 | “Love Can Start Before It’s Trusted ❤️” → “Love Before Trust ❤️” | Keeps the section’s love/trust paradox and its heart while exposing both halves. | 150.6/193px; fits |
| S032 | h3 | “If the Love Isn’t Coming Yet” → “If Love Isn’t Coming Yet” | Drops dispensable words so the reader’s difficulty remains fully visible. | 169.3/193px; fits |
| S033 | h3 | “Borrow Someone Else’s Love” → “Borrow Their Love” | Keeps love received from another person distinct from your love for others in the next heading. | 131.0/193px; fits |
| S034 | h3 | “Borrow Your Love For Someone Else” → “Borrow Your Love” | Uses the contrasting “Your” to distinguish love you already feel for others from borrowed care you receive. | 128.2/193px; fits |
| S035 | h3 | “Shame can make you feel unlovable” → “Shame Says “Unlovable”” | Keeps the shame/unlovability problem visible as a message of shame rather than a verdict about the person. | 175.9/193px; fits |
| S036 | h4 | ““And So That’s the Way It Happened!”” → ““That’s How It Was!”” | Keeps a spoken story-ending refrain that fits; this proposed heading paraphrases the formula, whose exact words remain in the body. | 146.4/181px; fits |
| S037 | h3 | “How to Forgive Without Forgetting” → “Forgiving, Not Forgetting” | Keeps both sides of Joel’s distinction visible without turning forgiveness into an instruction to do it now. | 177.4/193px; fits |
| S039 | h3 | “Show Up When Nothing’s Wrong” → “Show Up Just for Joy” | Uses the section’s invitation to enjoy the little one so this reads as non-crisis contact, not another repair task. | 153.4/193px; fits |
| S040 | h3 | “A Smaller Doorway: Goodwill” → “Goodwill: A Smaller Door” | Puts the practice first while retaining the smaller-door metaphor from the text. | 176.2/193px; fits |
| S041 | h3 | “A Bigger Doorway: Divine Love” → “Divine Love: Bigger Door” | Puts the destination first and keeps the bigger-door metaphor; the heading must stay because its paragraph begins “This,” referring to divine love. | 176.5/193px; fits |
| S042 | h2 | “The Inner Guide: Becoming Your Own Shepherd” → “The Guide” | Names the third adult role in parallel with The Protector and The Nurturer; the shepherd explanation stays in the text. | 73.1/205px; fits |
| S043 | h3 | “Are you ready for the Guide?” → “Ready for the Guide?” | Keeps the readiness check visible by removing only “Are you.” | 149.1/193px; fits |
| S044 | h3 | “Between Spoiling and Clamping Down” → “Spoil or Clamp Down?” | Keeps both parenting extremes visible; the body describes the middle course. | 156.3/193px; fits |
| S045 | h3 | “Borrow the Guide to Build It” → “Borrow the Guide” | Removes the repeated building purpose already established by the chapter. | 124.0/193px; fits |
| S047 | h4 | “Remember When You Already Did It Well” → “You Did It Well Before” | Keeps the exercise about a real past success distinct from imagined future hindsight. | 155.8/181px; fits |
| S048 | h3 | “A Healthy Mind Is Not a Perfect Mind” → “Healthy, Not Perfect” | Keeps the section’s distinction visible, with The Guide as its parent context. | 143.9/193px; fits |
| S049 | h3 | “Guide Yourself To Divine Love” → “Toward Divine Love” | Keeps the destination visible; The Guide parent already supplies who guides you. | 141.4/193px; fits |
| S053 | h4 | “You Belong Everywhere and Nowhere” → “Belong Beyond People” | Uses the section’s point that there is more to belong to than people, retaining its existential scope. | 160.6/181px; fits |
| S056 | h3 | “When the Spiritual Relationship Hurts” → “A Teacher Betrayed You” | Names the actual situation in the opening sentence instead of the broader, clipped “Spiritual Relationship.” | 173.6/193px; fits |
| S058 | h1 | “Practicing With Your Little One” → “Pl/ork With Your Little One” | Uses Joel’s own play/work coinage for the practice chapter and preserves the little one. | 187.6/217px; fits |
| S059 | h2 | “Start With Whatever Showed Up” → “Whatever Showed Up” | Keeps Joel’s open invitation to meet what is present, without the words that push its object out of view. | 155.0/205px; fits |
| S062 | h2 | “You Don’t Need an Inner Monologue” → “No Inner Monologue?” | Makes the reader’s situation visible before the cutoff; the body still says not to invent a voice. | 152.4/205px; fits |
| S063 | h2 | “Use Childhood Photographs Gently” → “Childhood Photos, Gently” | Keeps both the practical route and Joel’s caution in view. | 180.1/205px; fits |
| S068 | h3 | “If it tells you to do something” → “If It Gives Instructions” | Names the specific answer form that needs checking, using the journaling parent for context. | 154.2/193px; fits |
| S069 | h2 | “Catch the Hook Before the Story Takes Over” → “Catch the Hook” | Preserves Joel’s shenpa/hook vocabulary and the immediate action. | 110.1/205px; fits |
| S070 | h2 | “What to Make of a Passing Feeling” → “A Passing Feeling” | Keeps the section’s subject in view; the text explains what such a feeling can and cannot tell you. | 126.0/205px; fits |
| S072 | h2 | “Gentle Meditation and Mantra” → “Meditation and Mantra” | Keeps both calming practices visible. | 159.6/205px; fits |
| S073 | h2 | “One Intention in the Morning, One Review at Night” → “Morning Aim, Night Review” | Keeps both halves of the daily routine in the sidebar. | 192.2/205px; fits |
| S074 | h2 | “Close the Session and Return to Life” → “Close the Session” | Makes the stopping procedure visible; returning to life remains its body instruction. | 126.9/205px; fits |
| S075 | h1 | “Discovering and Healing Old Patterns” → “Healing Old Patterns” | Drops the duplicative discovery phrase so the whole chapter subject fits. | 145.4/217px; fits |
| S076 | h2 | “Use hindsight to “re-do” traumatic memories in a healthier way” → “Re-do Trauma Memories” | Keeps both the exercise and its traumatic-memory subject visible, distinguishing it from Borrow Hindsight. | 176.5/205px; fits |
| S077 | h3 | “How should discipline have been done right?” → “Discipline Done Right?” | Keeps the section’s question about the corrected parental response visible. | 158.4/193px; fits |
| S078 | h2 | “Answering the Strict Disciplinarian” → “Answer the Disciplinarian” | Keeps both the reply exercise and its target in view. | 179.6/205px; fits |
| S079 | h1 | “When the Practice Gets Difficult” → “When Pl/ork Gets Difficult” | Uses Joel’s established practice term to keep the troubleshooting chapter visible. | 183.3/217px; fits |
| S080 | h2 | “When the Adult Voice Feels Fake” → “Adult Voice Feels Fake” | Keeps the exact difficulty visible by removing the lead-in. | 162.0/205px; fits |
| S081 | h2 | “Sometimes There Isn’t a Clear Child Yet” → “No Clear Little One Yet?” | Uses Joel’s “little one” for the reader who cannot identify a child, keeping “Yet” so this is not a fixed verdict. | 169.5/205px; fits |
| S082 | h2 | “When the Practice Feels Real but Stays Shallow” → “Real, but Still Shallow?” | Exposes the problem that was entirely hidden after “Feels Real.” | 158.9/205px; fits |
| S083 | h2 | “When the Urge to Escape Arrives” → “The Urge to Escape” | Keeps the reader’s impulse fully visible. | 140.5/205px; fits |
| S084 | h3 | “Physical Pain Makes It Harder” → “Physical Pain” | Keeps the cause of the escape urge visible; the parent supplies the difficulty. | 93.8/193px; fits |
| S086 | h2 | “When Healing Turns Into Checking” → “Healing or Checking?” | Exposes the repeated-checking problem without losing the distinction from healing. | 151.5/205px; fits |
| S087 | h2 | “How Would You Know It’s Helping?” → “Is It Helping Your Life?” | Uses the section’s daily-life test so the reader knows this is a progress check. | 159.9/205px; fits |
| S088 | h2 | “When to Change the Strategy” → “Change the Strategy?” | Keeps the decision point visible with fewer lead-in words. | 153.6/205px; fits |
| S089 | h3 | “How many tries would I give it?” → “How Many Tries?” | Keeps the question about persistence intact. | 123.4/193px; fits |
| S090 | h3 | “If you keep following the reparenting steps correctly without getting the expected results” → “Steps Right, No Results?” | Puts the distinctive mismatch first instead of hiding it after a long condition. | 173.2/193px; fits |
| S092 | h1 | “Altered States and Intensive Practice” → “Altered States & Practice” | Keeps the chapter’s two subjects in view. | 176.1/217px; fits |
| S093 | h2 | “Altered States Can Deepen Therapy or Escapism” → “Therapy or Escapism?” | Uses the altered-states parent to expose the crucial fork instead of repeating its subject. | 157.5/205px; fits |
| S094 | h3 | “For some people, reparenting starts feeling real in an altered state” → “When It Feels Real” | Keeps the shift into felt connection visible in the altered-states and therapy context. | 131.2/193px; fits |
| S095 | h2 | “Everyone has altered states: Prepare now” → “Involuntary Altered States” | Uses the opening paragraph’s distinction to separate unavoidable nightmares, sleep paralysis and related experiences from deliberately seeking a state. | 183.3/205px; fits |
| S096 | h3 | “Using spiritual attack for spiritual gain” → “Spiritual Attack: Love” | Keeps the spiritual-attack situation and the section’s loving response visible, without implying invulnerability in daily life. | 150.4/193px; fits |
| S098 | h2 | “When Escape Leaves Reality Behind” → “Losing Touch With Reality” | Uses the actual problem discussed by this section and its warning-sign children. | 184.3/205px; fits |
| S100 | h3 | “Is your paranoia a warning sign?” → “Paranoia: A Warning?” | Keeps paranoia and the question about a warning visible. | 152.2/193px; fits |
| S101 | h3 | “If you might be prone to mania or psychosis” → “Mania or Psychosis Risk” | Puts the two vulnerabilities first instead of losing both behind “prone to.” | 171.5/193px; fits |
| S103 | h3 | “If you keep coming back from trips confused or spaced out” → “Confused After Trips?” | Names the repeated aftermath hidden in the old label; the body still distinguishes recurrence, severity and sober episodes. | 156.5/193px; fits |
| S104 | h3 | “Before you quit a medication or alcohol” → “Quitting Meds & Alcohol” | Makes both withdrawal topics visible as a topic, retaining the body’s caution before stopping either. | 170.2/193px; fits |
| S106 | h3 | “Non-altered states can feel like this too” → “Social Media Hooks Too” | Names the section’s everyday example instead of the abstract “Non-altered states.” | 172.0/193px; fits |
| S107 | h2 | “My Psychedelic Experiences Came A Bit Too Soon” → “My Trips Came Too Soon” | Keeps Joel’s personal-story framing and timing lesson together in the altered-states chapter. | 180.3/205px; fits |
| S109 | h1 | “Bringing Reparenting Into Real Life” → “Reparenting in Real Life” | Puts the practice and its daily-life destination together. | 167.9/217px; fits |
| S110 | h2 | “Rediscover Play and Your Own Preferences” → “Play and Your Preferences” | Keeps both play and discovering your own tastes visible. | 189.6/205px; fits |
| S112 | h3 | “From Survival to Experimental Play” → “Your Own Preferences” | Names the reflection exercise in the text; actual experiments remain in the next section. | 161.5/193px; fits |
| S113 | h3 | “Let the Child Be Bad at Things” → “Okay to Be Bad at This” | Uses the text’s reassuring spoken line for permission to be a beginner. | 161.0/193px; fits |
| S114 | h2 | “Differentiation: Keeping Your Own Ground” → “Keep Your Own Ground” | Keeps the plain-language explanation of differentiation; the technical term remains in S117 and the body. | 168.5/205px; fits |
| S115 | h3 | “Untangling the Belonging Bargains” → “Belonging Bargains” | Keeps Joel’s complete coinage instead of losing “Bargains” after “Untangling.” | 137.1/193px; fits |
| S116 | h4 | “Four Pairs That Commonly Hook the Child” → “Four Pairs That Hook” | Keeps the four-pair map and hook vocabulary, with the child supplied by the surrounding guide. | 149.5/181px; fits |
| S118 | h3 | “Taking a Break From a Family, Group, or Relationship” → “Break From Your People” | Keeps the relationship break visible and covers family, group and partner in the differentiation context. | 172.7/193px; fits |
| S119 | h3 | “When Being Happy Feels Like Abandoning Someone” → “Happy While They Hurt?” | Names the precise bargain in the text: feeling guilty about happiness while someone else suffers. | 172.7/193px; fits |
| S120 | h2 | “Finding People and Building Trust” → “Find People, Build Trust” | Keeps both tasks visible. | 168.6/205px; fits |
| S121 | h3 | “First Social Connections, Done Right” → “Quit the Lovability Tests” | Uses the section’s test/flunk metaphor so readers can find the actual problem with new connections. | 171.0/193px; fits |
| S122 | h3 | “Opening Up Honestly to the Right People at the Right Pace” → “Open Up at Your Pace” | Makes paced disclosure visible rather than losing it behind “Honestly.” | 157.8/193px; fits |
| S123 | h4 | “Before You Tell the Hardest Stuff” → “Before You Tell Secrets” | Uses the section’s concrete disclosure stakes so the privacy question is visible. | 168.0/181px; fits |
| S125 | h3 | “Ask What Kind of Company They Want” → “Listen or Brainstorm?” | Uses two options from the section’s actual question to make the choice of support recognizable. | 150.3/193px; fits |
| S128 | h3 | “Hearthwork: Taking Turns Lending & Borrowing Adulthood” → “Hearthwork: Take Turns” | Keeps Joel’s framework name and its defining practice visible. | 171.7/193px; fits |
| S129 | h2 | “Finding a Therapist to Borrow Adulthood” → “Find a Therapist” | Removes the borrowing purpose already explained by the guide while keeping this navigation destination explicit. | 114.4/205px; fits |
| S130 | h3 | “Inner Child Reparenting therapists” → “Reparenting Therapists” | Makes the provider type fully visible within Find a Therapist. | 165.0/193px; fits |
| S131 | h3 | “If you want a licensed therapist” → “Licensed Therapists” | Keeps the licensing distinction visible within Find a Therapist. | 143.3/193px; fits |
| S132 | h3 | “Before choosing a therapist” → “Before Choosing One” | Uses the therapist parent to remove repetition, retaining the pre-selection interview cue. | 152.4/193px; fits |
| S134 | h2 | “Speaking Up and Handling Conflict” → “Speaking Up in Conflict” | Keeps the setting for the communication advice visible. | 166.5/205px; fits |
| S135 | h3 | “If Someone Has Actually Hurt or Threatened You” → “Hurt or Threatened?” | Puts both kinds of immediate harm in view; the body still begins with getting safe. | 143.1/193px; fits |
| S136 | h3 | “Speak Toward What You Are Building” → “What You Want More Of” | Uses the text’s phrase for where words point attention, preserving the constructive direction of the original. | 172.8/193px; fits |
| S138 | h3 | “If You Really Did Hurt Them” → “If You Hurt Them” | Preserves the conditional responsibility and the repair situation in fewer words. | 121.3/193px; fits |
| S139 | h3 | “Other Folks Also Have Hooks” → “Other Folks’ Hooks” | Keeps the other person and the hook concept together, with their capacity assessed by the children. | 134.9/193px; fits |
| S141 | h4 | “If a Relationship Keeps Making You Feel Less Safe” → “Less Safe With Them?” | Names the repeated relationship problem hidden in the former cutoff. | 158.4/181px; fits |
| S142 | h2 | “When One Life Has Ended and the Next Hasn’t Begun” → “Between Old & New Lives” | Keeps both sides of Joel’s metaphor for the gap after a breakup, move or loss, rather than reducing it to bereavement. | 182.4/205px; fits |
| S145 | h2 | “You Are Worthy of Love. Always.” → “Worthy of Love. Always.” | Retains the closing reassurance and “Always” that the current sidebar hides. | 173.2/205px; fits |
| S147 | h3 | “How This Relates to Similar Therapies” → “Lucia’s Reparenting” | Names the specific comparison actually made here, separating it from the Schema and IFS sections that follow. | 139.9/193px; fits |
| S149 | h3 | “Internal Family Systems (IFS)” → “Internal Family Systems” | Retains the full therapy name in view; IFS stays in its body. | 168.3/193px; fits |
| S150 | h3 | “Development of my framework” → “My Framework’s Roots” | Keeps this provenance section distinct from the therapy comparisons and credits around it. | 162.7/193px; fits |
| S151 | h3 | “Original Teachers and Practice Resources” → “Teachers and Resources” | Keeps both credits and practice resources visible. | 176.6/193px; fits |

## Words to check with Joel before implementation

These are concrete proposed choices to review, not requests to change the body text during this task.

- S011, “When Cruelty Feels Good”: check that this captures the threshold for the present-day adult being unsafe; the body also distinguishes malice from unwanted frightening thoughts.
- S019, “Borrow, Don’t Sell Out”: check the compression of his inner-adult/outer-adult trading metaphor; its warning against giving up your own judgment must stay clear.
- S036, “That’s How It Was!”: check before paraphrasing the deliberate story-ending formula in the heading. The body must continue to give his exact “And so that’s the way it happened!” practice.
- S053, “Belong Beyond People”: check the loss of the deliberate “Everywhere and Nowhere” paradox; this is the largest philosophical compression.
- S128, “Hearthwork: Take Turns”: check before shortening the subtitle of his named framework; the body retains lending and borrowing adulthood.
- S142, “Between Old & New Lives”: check that shortening his poetic title still evokes the unfinished transition rather than literal death.
- S085 and S137: keep their current wording in this proposal; ask before sacrificing the playful warning or the full write/pause sequence for a strict all-fits target.

## Named references in the body

No body references were edited. If these proposed headings are adopted, the following references need a separate text-edit pass:

| Target ID | Existing named heading | Proposed heading | Where the body points to it |
| --- | --- | --- | --- |
| S076 | Use hindsight to “re-do” traumatic memories in a healthier way | Re-do Trauma Memories | S046 names it as “Use Hindsight to Re-do Traumatic Memories In A Healther Way” and directs readers to the contents. |
| S093 | Altered States Can Deepen Therapy or Escapism | Therapy or Escapism? | S094 repeats the old title; it also says “further on” even though S093 precedes it. |
| S115 | Untangling the Belonging Bargains | Belonging Bargains | S081 names the old heading as the place to find and build the authentic self. |

S022 “Noticing Counts” remains unchanged, preserving the references in S013 and S059. S050 “Ask God for a Loan 🫶🏿” remains unchanged, preserving the named reference in S097; “Your Loan is PRE-APPROVED!” also remains in its body, where S145 and S148 point. S046 “Borrow Hindsight” remains unchanged for S076. S031’s “Chicken and Egg problem” remains recognizable under shortened S003 “The Chicken-and-Egg”.

Existing reference to check separately: S097 names “Timing Is Individual,” which is absent from the supplied contents. This proposal does not invent a heading or guess a replacement target.

## Unchanged headings, also measured

| ID | Level | Heading | Final width/room; status |
| --- | --- | --- | --- |
| S001 | h1 | “Understanding Reparenting” | 194.7/217px; fits |
| S004 | h2 | “Five Stages of Reparenting” | 191.5/205px; fits |
| S005 | h2 | “My Journey” | 84.3/205px; fits |
| S006 | h1 | “Safety and Readiness” | 153.7/217px; fits |
| S013 | h2 | “If You Want to Kill Yourself” | 190.1/205px; fits |
| S017 | h1 | “Building Your Inner Adult” | 176.3/217px; fits |
| S020 | h3 | “Signs of Manipulation” | 153.2/193px; fits |
| S022 | h3 | “Noticing Counts” | 113.8/193px; fits |
| S024 | h3 | “Talk to the hand!✋🏿” | 137.5/193px; fits |
| S030 | h2 | “The Nurturer” | 91.2/205px; fits |
| S038 | h4 | “Forgiving Yourself” | 130.2/181px; fits |
| S046 | h4 | “Borrow Hindsight” | 122.9/181px; fits |
| S050 | h4 | “Ask God for a Loan 🫶🏿” | 159.1/181px; fits |
| S052 | h4 | “The Joy In Sorrow” | 130.0/181px; fits |
| S054 | h3 | “Invite Your Little One In” | 165.4/193px; fits |
| S055 | h4 | “A Heart to Child Loop” | 151.9/181px; fits |
| S060 | h2 | “Make a Simple Vow” | 139.6/205px; fits |
| S061 | h3 | “Remind Yourself” | 117.0/193px; fits |
| S064 | h2 | “Journal With Each Hand” | 170.3/205px; fits |
| S065 | h3 | “Which thoughts to talk to” | 177.1/193px; fits |
| S066 | h3 | “If no answer comes” | 139.3/193px; fits |
| S067 | h3 | “If you do get an answer” | 167.2/193px; fits |
| S071 | h3 | “If it’s anxiety” | 89.6/193px; fits |
| S085 | h4 | “Listen To Your Body, Or Else!” | 207.5/181px; cut |
| S091 | h3 | “If you’d rather stop” | 134.9/193px; fits |
| S097 | h2 | “What to Do With a Peak” | 167.4/205px; fits |
| S099 | h3 | “If a past trip went badly” | 166.5/193px; fits |
| S102 | h3 | “Who counts as trusted” | 159.9/193px; fits |
| S105 | h3 | “What you mix” | 96.7/193px; fits |
| S111 | h3 | “Play Is Part of the Work” | 166.4/193px; fits |
| S117 | h3 | “Practicing Differentiation” | 176.2/193px; fits |
| S124 | h3 | “How To Let People In” | 151.9/193px; fits |
| S126 | h3 | “Dating While You Heal” | 158.2/193px; fits |
| S127 | h3 | “The Love Has to Move” | 159.9/193px; fits |
| S133 | h3 | “AI therapy” | 72.8/193px; fits |
| S137 | h3 | “Write It. Don’t Send It Yet.” | 183.1/193px; tight |
| S140 | h4 | “Can They Change?” | 135.1/181px; fits |
| S143 | h3 | “Missing Someone” | 126.0/193px; fits |
| S144 | h1 | “Conclusion and Appendix” | 181.5/217px; fits |
| S146 | h2 | “Appendix” | 67.3/205px; fits |
| S148 | h3 | “Schema Therapy” | 120.6/193px; fits |

## Completeness and scope checks

- Parsed the source IDs independently from TOC-NOW and compared their counts with PROPOSAL.json: 147 source IDs, 147 entries, no duplicates, no omissions, no extras.
- Entry order exactly matches TOC-NOW. Every entry has exactly `id`, `level`, and `heading`, and each level is 1–4. The only level change is S010, h3 → h2; it creates no skipped hierarchy level.
- S016, S057 and S108 are the three empty headings excluded by TOC-NOW; S051 is its excluded h5. They receive no new proposal entries. S051 stays with S050 and its gratitude/loan imagery, including the “Mo’ Money, Mo’ Problems” text.
- Measurement rows match every JSON heading and level exactly. Only S085 and S137 are exceptions to the 12px target, as disclosed above.
- All task file access stayed in this folder. No checkouts or dependency caches were created; only the two requested deliverables remain from the proposal work.
