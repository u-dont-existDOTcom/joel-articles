# The bad trips guide's headings, for Substack's narrow contents sidebar (round 47)

His message, 2026-11-21 01:06 UTC: "continue, also make sure the headings are fitting in the ToC based on the inner child lane's work on that article".

The inner child lane measured the sidebar in his post (gate inner-child-2026-11-16a): each heading is one line, cut off with "…" past about 26 characters for an h1, 24 for an h2, 22 for an h3 and 20 for an h4 ([toc_sidebar.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/tools/humanization/toc_sidebar.py)). In the bad trips guide **46 of the 62 headings are cut off** ([as it stands](TOC-AS-IT-STANDS.md)).

## How it was done

- **Fable** named every heading with [the headings brief](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/tools/humanization/headings_brief.md) the inner child lane made from his picks there (lesson inner-child-2026-11-20b), his order and levels kept: 11 kept as they are, 51 shortened, all fitting ([its brief](PROMPT-WRITER.md); its headings are in the table below).
- **32 situations** a reader brings were written by a fresh reader who saw the text with the headings taken out, with the sections that answer each; a second reader checked that key and added 12 answering sections (gate inner-child-2026-11-17b; the situations are listed at the end).
- **Fresh readers** saw only one contents, as the sidebar shows it, and said where they'd look first, sure or a guess, and where next ([their brief](PROMPT-READER.md)).
- **My pick** is Fable's with three headings back in his words where Fable's readers went wrong; it was read by two more fresh readers (gate inner-child-2026-11-17a: read the pick itself).

## What the readers found

| Contents | Readers | First pick right (of 32) | Guesses | Right by the 2nd pick |
|---|---|---|---|---|
| His, as the sidebar cuts it | 2 | 23, 24 | 14, 14 | 28, 27 |
| Fable's | 2 | 26, 26 | 9, 6 | 30, 30 |
| My pick | 2 | 28, 27 | 8, 10 | 29, 31 |

- With the headings whole in the sidebar, readers guessed far less (14 of 32 on his as cut, 6 to 10 on the two that fit) and got more first picks right.
- Fable's "MDMA Jaw Tension?" lost the reader who drank too much water on MDMA (both readers of his contents found it under "MDMA: Jaw Tension Is the…"); "MDMA: Magnesium Alarm", his words, got both back, though both readers called it a guess ("alarm" could be a warning or a remedy).
- "Hang Up" (Fable's "Trip After Trip? Hang Up") read as a phone call to both of its readers: my pick is his "Trip After Trip?".
- Still weak in every version: ZHoly3O (no reader knew what it is), and "My Acute Rescue Remedies" next to "Medical and Brain Rescue" (two parents with "Rescue").

## The two serotonin headings in a row (his answer, 2026-11-21 13:04 UTC)

His message: "done. learn lessons. why would you put 2 serotonin syndrome headings in a row / continue".

**Why it happened.** Fable named each heading to read on its own, so it turned his "Suspected Serotonin Syndrome (SS)" into "Serotonin Syndrome (SS)?" and his "Recognizing serotonin toxicity", the heading right under it, into "Is It Serotonin Toxicity?": the same question twice. My pick took both from Fable. Nothing compared a heading with the one it sits under or the one before it; the readers were only asked where they would look, and their scores came out fine, because a reader who opens either heading lands in the right place. When readers mentioned the pair in their replies, I didn't act on it.

**What changed** (lessons bad-trips-2026-11-21a to c, [the lesson file](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/docs/lessons/2026-11-21-1304-bad-trips.md)):

- [The headings brief](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/tools/humanization/headings_brief.md) has rule 11: no two headings in a row say or ask the same thing; a parent names the topic and its children name their parts.
- [toc_check.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/tools/humanization/toc_check.py) lists every heading that shares a word with the one it sits under or the one before it, and every heading a reader marked hard, and fails until each one is changed or kept with the reason it stays.
- Readers now end with a "HARD:" line for each of the three hardest headings and for each pair that says the same thing, and a changed heading is read again by fresh readers before it goes to him.
- His round 47 picks never reached me: the page had no database when he answered, so they were kept only in the browser he used. The page now sends them when it opens there, and it saves the headings themselves, not only which column he clicked, so they still read right if the columns change.

**The picks read after his answer.** Each one was read by two fresh readers; the serotonin pair went in the second.

| Contents | What changed from the one before | First pick right (of 32) | Guesses | Right by the 2nd pick |
|---|---|---|---|---|
| My pick (on the page he answered) | as on the page | 28, 27 | 8, 10 | 29, 31 |
| Second | "Medical and Brain Rescue" → "Medical Emergencies"; "Seizure: What Else Helps" → "What Else Helps"; "MDMA: Magnesium Alarm" → "MDMA: Jaw and Water"; "Is It Serotonin Toxicity?" → "How to Recognize It"; "Do This Immediately" → "What to Do Right Away"; "Remedies Needing Caution" → "Some Need More Caution"; "Gut-Toxin & Die-Off Tools" → "Toxic Gut or Die-Off?"; "Creatine for Brain & Bliss" → "Creatine Is Blissful" | 27, 27 | 4, 8 | 31, 30 |
| Third | "If Someone Might Get Hurt" → "If Support Isn't Enough"; "Who to Contact, and When" → "Who to Contact"; "My Acute Rescue Remedies" → "Remedies for a Hard Trip"; "Some Need More Caution" → "Which Need Caution?"; "Feeling Good Forever?" → "Bliss Can Be a Bypass Too" | 24, 25 | 7, 7 | 29, 29 |
| Fourth | "If Support Isn't Enough" → "If Someone Might Get Hurt"; "Which Need Caution?" → "Remedies Needing Caution" | 27, 27 | 6, 5 | 30, 31 |
| Fifth | "Medical Emergencies" → "Medical First Aid"; "What Else Helps" → "Beyond Rescue Medicine" | 27, 26 | 4, 6 | 30, 30 |
| Sixth | "Beyond Rescue Medicine" → "What Else May Help" | 27, 27 | 4, 8 | 29, 30 |

The serotonin part in the sixth: "Serotonin Syndrome (SS)?", then "How to Recognize It" and "What to Do Right Away" under it.

**Every heading the check or a reader flagged in the sixth pick, and its fate:**

| Heading | Why it was flagged | Fate |
|---|---|---|
| Remedies Needing Caution | shares a word with the heading above it or before it | kept: "Remedies" is the parent's topic word, but this names its own part, the ones not to use casually (humic acid eaten, cinnamon, acacia with mimosa); the shorter "Some Need More Caution" and "Which Need Caution?" told the readers of the second and third picks nothing |
| Remedies Needing Caution | a reader marked it hard | kept: one reader of the fifth pick found it close to "Remedies for a Hard Trip" above it, but the parent is what to reach for and this is what to be careful with; no reader of the sixth pick flagged it |
| Shungite, Charcoal Water | shares a word with the heading above it or before it | kept: it shares only "water" with "Ocean Water Calms" before it, and they are different remedies (his text compares the two) |
| Shungite, Charcoal Water | a reader marked it hard | kept: it isn't "Activated Charcoal" (line 20): it is water left after charcoal, and his text says it is different from swallowing charcoal; shungite is the name a reader who uses it looks for, and the text says what each one is |
| Need to Stop the Trip? | shares a word with the heading above it or before it | kept: "trip" is the guide's own word; the parent eases a hard trip, this one ends it |
| Niacin: A Final Trip Killer | shares a word with the heading above it or before it | kept: "trip" is the guide's own word; Beach Morning Glory sits between it and its parent, and "Final" says what sets niacin apart, that it is the last thing to try |
| Niacin: A Final Trip Killer | a reader marked it hard | kept: his own words, with the remedy's name first; "Final" says what the parent doesn't, that niacin is the last thing to try; for "I want this trip to stop right now" all four readers of the fifth and sixth picks opened its parent first, sure, and three of the four tried niacin next |
| Shadow Thoughts | shares a word with the heading above it or before it | kept: five headings sit between it and its parent, and they are different things: shadow work is the practice, shadow thoughts are the dark thoughts that come up; his term |
| Plan a Trip or Ceremony | shares a word with the heading above it or before it | kept: "trip" is the guide's own word; "Trip After Trip?" is about trips coming back again and again, this one is about planning one |
| Zeolite and ZHoly3O | a reader marked it hard | kept: ZHoly3O is the name of his ferment, linked in the text; the round 47 page tells him both readers of Fable's list couldn't tell what it is, so it stays his call |
| Metta NMT Sniffer: Chill! | a reader marked it hard | kept: the name of his own sniffer, which the text explains, with his playful "Chill!" for what it does |
| Bliss Can Be a Bypass Too | a reader marked it hard | kept: it sits eleven headings below line 45, in another part, and says another thing: line 45 is what to do while a trip feels blissful, this one is chasing good feelings as a way around shadow work |
| Inner Signal to the Rescue! | a reader marked it hard | kept: his to decide: four of the ten readers of the second to sixth picks couldn't tell what "Inner Signal to the Rescue!" is; with "App" it runs past the sidebar's room and is cut to "to the Resc…", and "Inner Signal App Can Help!" fits (190 of 217) and says it is an app, so it goes to him beside his pick |
| If Someone Might Get Hurt | a reader marked it hard | kept: it tested best: both readers of the second pick found the friend who keeps walking out the door here, and the third pick's "If Support Isn't Enough" lost him for both; it sits beside "Call Medics For:" because both are reasons to call (harm here, the body there), and line 43 is for the helper, in another part |
| What Else May Help | a reader marked it hard | kept: his own words; under "Active Seizure" they say it is more help for a seizure, and the aura is its first line; one of the two readers flagged it, against both for "Beyond Rescue Medicine", and "At the Aura and During It" would sound like the parent's own steps |
| (Re)defining "Bad Trip" | a reader marked it hard | kept: his own heading, untouched and fitting; both readers still opened it second for "someone told me a bad trip is just shadow work" |
| Spiritual ≠ "Ass-Kicking" | a reader marked it hard | kept: his own sign and his phrase, shortened to fit; both readers opened it first, and sure, for "someone told me a bad trip is just shadow work so I should push through it" |
| Call Medics For: | a reader marked it hard | kept: his own words; the parent asks when to get outside help and this names one answer, medics, and what for (its siblings name the others: someone might get hurt, who to contact); both readers of the sixth pick opened it first or next in seven of the nine situations that need it |
| Get Mental-Health Help If: | a reader marked it hard | kept: "Lingering Symptoms?" asks what this aftermath is, this one says when it needs a professional; both readers opened the two in that order for "it's been a week and nothing feels real" |
| Helping? Anchor, Not Guru | a reader marked it hard | kept: "Get One Human Anchor" is for the one tripping, this is for the one helping; "anchor" is his word in both, and "Alone at 3 a.m." sits between them |

In the fifth pick both readers couldn't tell what "Beyond Rescue Medicine" covered: back to his own words "What Else May Help" in the sixth pick, since both readers of the fifth couldn't tell what "Beyond Rescue Medicine" covered; re-read by two fresh readers.

**Next, when his picks arrive** ([read_answers.py](read_answers.py)): his headings are worked out again from his picks with the columns he saw and compared with what the page saved; his contents gets the same check (the serotonin pair is fixed whichever way he picked it, from the headings read above) and two fresh readers; then the headings go into the guide with their evidence tag lines.

## The evidence tags

His round-46 answer put a short evidence tag on each remedy heading. In a heading, "[Tried by Me and Friends]" alone takes more than an h3's room, so the remedy's name would be cut: each tag goes on its own line just under its heading. They go in with the headings he picks, each heading checked with its tag line and first paragraph.

## Each heading: his, and my pick

| Id | Level | His heading | My pick | Sidebar |
|---|---|---|---|---|
| B65 | h1 | Inner Signal App to the Rescue! | Inner Signal to the Rescue! | fits |
| B91 | h1 | When to Bring In Outside Help | When to Get Outside Help | fits |
| B93 | h2 | Call medics for: | Call Medics For: | fits |
| N-SF-1 | h2 | Risk of Harm: When Peer Support Isn't Enough | If Someone Might Get Hurt | fits |
| B261 | h2 | Who to Contact, and When | (as it is) | fits |
| B99 | h1 | Acute Medical and Neurological Rescue | Medical and Brain Rescue | fits |
| B102 | h2 | If Someone Says "My Brain Feels Damaged": DMSO + Humic Acid + Electrolytes First | "My Brain Feels Damaged" | fits |
| B108 | h2 | Active Seizure | (as it is) | fits |
| R32-SEIZE | h3 | What Else May Help: At the Aura, and Alongside Rescue Medicine | Seizure: What Else Helps | fits |
| B113 | h2 | MDMA: Jaw Tension Is the Magnesium Alarm | MDMA: Magnesium Alarm | fits |
| B121 | h2 | Chest Pain and Injury | (as it is) | fits |
| B125 | h2 | Recent Oral Toxic Ingestion | Swallowed Too Much? | fits |
| B129 | h2 | Suspected Serotonin Syndrome (SS) | Serotonin Syndrome (SS)? | fits |
| B131 | h3 | Recognizing serotonin toxicity | Is It Serotonin Toxicity? | fits |
| B135 | h3 | Do this immediately when serotonin toxicity is reasonably suspected: | Do This Immediately | fits |
| B138 | h1 | My Acute Rescue Hierarchy of Remedies | My Acute Rescue Remedies | fits |
| B217 | h2 | Some Remedies Require More Caution | Remedies Needing Caution | fits |
| B150 | h2 | Gut-Toxin and Parasite-Die-Off Tools | Gut-Toxin & Die-Off Tools | fits |
| B152 | h3 | Zeolite and Ferment in ZHoly3O | Zeolite and ZHoly3O | fits |
| B159 | h3 | Actual Activated Charcoal | Activated Charcoal | fits |
| B164 | h2 | Nausea Smoothers When the Person Wants to Preserve the Trip | Nausea Smoothers | fits |
| B166 | h3 | Coffee Cherry for Nausea and Brain Recharge | Coffee Cherry | fits |
| B180 | h2 | Mental Stabilizers That Don't Abort the Trip | Too Intense? Stabilizers | fits |
| B181 | h3 | Metta NMT Sniffer Makes the Trip Chill & Lovey! | Metta NMT Sniffer: Chill! | fits |
| B183 | h3 | Humic Acid Brings Brain to Optimal Function | Humic Acid for the Brain | fits |
| H54-CREATINE-H | h3 | Creatine Is Blissful and Good for the Brain | Creatine for Brain & Bliss | fits |
| H54-MANGO-H | h3 | Mango Leaf Tea Relaxes Without Killing the Trip | Mango Leaf Tea Relaxes | fits |
| R30-OILS1 | h3 | Authentic Calming Essential Oils (or a Lime Peel) | Essential Oils or a Lime | fits |
| B199 | h3 | DMSO | (as it is) | fits |
| R30-RUE1 | h3 | Syrian Rue Oil Makes the Trip Gentle & Sweet | Syrian Rue Oil: Gentler | fits |
| B185 | h3 | Ocean Water to calm & protect the energetic field | Ocean Water Calms | fits |
| B189 | h3 | Shungite, Aged Ozonated-Charcoal Water, or Boiled Charcoal Water | Shungite, Charcoal Water | fits |
| B169 | h2 | When the Goal Is to Stop a Psychedelic Trip | Need to Stop the Trip? | fits |
| B170 | h3 | Beach Morning Glory--Ipomoea pes-caprae | Beach Morning Glory | fits |
| B210 | h3 | A Final Trip Killer: Niacin (a Form of Vitamin B3) | Niacin: A Final Trip Killer | fits |
| B227 | h1 | Tripsitting Yourself or Others | (as it is) | fits |
| B233 | h2 | Psychological First Aid: The First Five Minutes | The First Five Minutes | fits |
| B294 | h2 | Grounding Menu: Choose One or Two Things | Grounding Menu | fits |
| B253 | h2 | Get One Human Anchor | (as it is) | fits |
| B271 | h3 | Alone at 3 a.m. | (as it is) | fits |
| B279 | h2 | For the Person Helping: Calm Anchor, Not Guru | Helping? Anchor, Not Guru | fits |
| B281 | h3 | Do | What to Do and Say | fits |
| B285 | h3 | When What They Say Turns Toward Harm | When Talk Turns to Harm | fits |
| B315 | h2 | No Rash Actions: Visions Are Not Commands | No Rash Actions | fits |
| B323 | h2 | When the Trip Feels Amazing: Euphoric Certainty | If the Trip Feels Amazing | fits |
| R30-SHADOW | h1 | Shadow Work | (as it is) | fits |
| B376 | h2 | Dealing With Sorrow: Missing Versus Sending Love | Dealing With Sorrow | fits |
| B385 | h2 | Hand on Heart and Gratitude 🫶🏿 | Hand on Heart, Gratitude | fits |
| B390 | h3 | Touch, Consent, and Compassion | Ask Before You Touch | fits |
| B394 | h2 | Demons, Jinn, Entities, and Shadow Forces | Demons, Jinn, and Entities | fits |
| B405 | h2 | Abuse Memories, Recovered Memories, and Certainty | Abuse Memories Surface? | fits |
| B410 | h2 | Dealing With Shadow Thoughts | Shadow Thoughts | fits |
| B416 | h3 | The Joker Poem | (as it is) | fits |
| B329 | h2 | (Re)defining "Bad Trip" | (as it is) | fits |
| B332 | h2 | Spiritual ≠ "Getting Your Ass Kicked" | Spiritual ≠ "Ass-Kicking" | fits |
| B338 | h2 | The Other Bypass: Feeling Good Forever | Feeling Good Forever? | fits |
| B419 | h1 | After the Storm | (as it is) | fits |
| B424 | h2 | What Kind of Aftermath Is This? | Lingering Symptoms? | fits |
| B96 | h2 | Bring in mental-health support when: | Get Mental-Health Help If: | fits |
| B347 | h2 | Trip After Trip? Hang up the phone, get off the Healing Treadmill | Trip After Trip? | fits |
| B364 | h1 | Planning a Trip or Ceremony? Give It a Beginning and an End | Plan a Trip or Ceremony | fits |
| B432 | h1 | Appendix: Additional Resources | Appendix: More Resources | fits |

## Sentences in the text that name a heading

- "(more on that in Active Seizure)", in the DMSO section: Active Seizure keeps its heading.
- "(see Mental Stabilizers That Don't Abort the Trip)", in the Grounding Menu's Smell line: it takes the new name of that section, with a link to it.

## The 32 situations

1. my friend took too much and his lips are turning blue and he's barely breathing
2. my friend is having a seizure right now after taking something, what do I do
3. my friend on MDMA is sweating and his eyes keep jerking and his muscles are twitching
4. my jaw is clenched really tight on MDMA and I can't relax it
5. I drank a ton of water on MDMA and now I have a headache and feel confused
6. I took too much and don't know what to do, how do I figure out how bad it is
7. I feel like my brain is damaged and I can't explain it, something is really wrong
8. his face is drooping and his speech is slurred after he took something
9. I have chest pain on a stimulant and I'm scared it's my heart
10. I'm on antidepressants and took MDMA, now I'm shaking and burning up
11. I think my friend might hurt himself, he keeps trying to walk out the door
12. he says he's God and can kill people and I'm scared of him
13. I need a hotline or someone to talk to right now, I'm tripping alone and scared
14. I want this trip to stop right now, nothing is working
15. my stomach is wrecked, I feel toxic and the nausea is making the trip hellish
16. I keep throwing up and have diarrhea on ayahuasca, is this normal or dangerous
17. I want to calm down but not end my trip, what can I smell or take
18. I took too much ayahuasca and feel out of it and bad
19. should I take charcoal to bring down my trip or will it wreck it
20. my friend is panicking and going in circles, how do I help without making it worse
21. can I hug my friend or hold his hand while he's freaking out
22. I think a demon is attacking me and I can't stop being terrified
23. it feels like the best insight ever and I want to quit my job and tell everyone tonight
24. I saw memories of abuse on a trip and I want to confront my family tomorrow
25. I keep seeing the dark side of everything in my head, is something wrong with me
26. someone told me a bad trip is just shadow work so I should push through it, is that right
27. I'm heartbroken and grieving during my trip and it hurts so much
28. it's been a week since my trip and nothing feels real, like I'm watching myself
29. I can't sleep since the trip and I keep having nightmares and weird thoughts
30. the trip ended last night, what should I do today and should I do another ceremony
31. I'm planning a mushroom ceremony with friends next month, how do I set it up safely
32. my friend took a lot and he's scared, should I call an ambulance or keep him here
