# Emoji pass over the whole article (2026-10-01, turn 9)

Joel, 02:40 UTC: "for emojis yeah you can put them in the whole article and then i'll see if you are doing it right. on average i'm thinking prob each section should have at least 1 emoji but i wouldn't make that a rule obviously just an average because it's nice but you don't want to abuse with emojis, i mean some sentences demand them like i might put 2 in a paragraph sometimes as you've seen. I'd actually add a hugging emoji after "i still love you" since it's responding to the disbelief emoji in P6. And after "I hate you!" i'd add an angry emoji and after "I love you" respond with some lovey emoji or hug emoji"

## How the placements were chosen
- Joel's three picks went in as he said: 😡 and 🥰 in Love Doesn't Wait P3, 🤗 in P6.
- Claude picked thirteen more, about one per section that had none: warmth, a joke, a practical step, a pointer. None in the sections that already had his own (Catch the Hook, Borrow One Competency, Not Every Hero).
- A fresh cold reader (Sonnet) judged all sixteen for tone, rendering and repeats. It called three of Claude's misfits, and they changed before any Pangram check:
  - ☯️ at "yin-yang symbol": may not render in older email apps, and only repeats the words. Became 💆 at the end of that paragraph.
  - 🤷 after "Where were we?": could read as "whatever" about a real checking habit. Became 😊 after "Seat belt's on."
  - 📞 after "before you call next time": only labels the word "call". Taken out.
- Then every paragraph with an emoji was checked on Pangram 4.0 alone (if 50 words or more) and in its section, headings included. All on try 1.

## Results

| section | emoji | the paragraph alone | the section | kept |
|---|---|---|---|---|
| the opening | 🎶 after "put a song on" | 100% Human (89) | 100% Human (223) | yes |
| The Chicken-and-Egg Problem | 🙈 after "bathroom vacationing" | 100% Human (84) | 100% Human (748) | yes |
| My Journey | 👇 at the map | (14 words) | 100% Human (491) | yes |
| When the Present-Day Adult Is Dangerous | 🔥 after the Human Torch | 100% Human (104) | 100% Human (504) | yes |
| You Don't Need an Inner Monologue | 😉 after "you might not be some people" | **100% AI** (73); 100% Human without it on 2026-09-27 | 100% Human (231) | no |
| Your Body Might Need Some Love First | 💆 after the self-massage | 100% Human (69) | 100% Human (175) | yes |
| Also Look Outward | 😅 after "Try again." | 100% Human (83) | 100% Human (443) | yes |
| Write It. Don't Send It Yet. | 😌 after "Breathing easier." | (45 words) | 100% Human (498) | yes |
| When Healing Turns Into Checking | 😊 after "Seat belt's on." | 100% Human (92) | 100% Human (340) | yes |
| Noticing Counts (with its h1) | 😄 after Elmo | 100% Human (68) | **30% AI** (163), span on the h1, h2 and P1 | no |
| Borrow Love | 🐶 after "So let the dog go first." | **56% AI** (102), span from the emoji to the end; 100% Human without it on 2026-09-26 | **69% AI** (418) | no |
| A Smaller Doorway: Goodwill | 🙏 after the wish | (49 words) | 100% Human (129) | yes |
| Love Doesn't Wait | Joel's 😡 🥰 🤗 | P3 (36), P6 (49) | 100% Human (437) | yes |

Noticing Counts, two diagnostics: with the h1 and no emoji, 100% Human (163); with the emoji and no h1, 100% Human (154). It took both.

## What this shows
- An emoji can flip Pangram on text that passed. So each one gets its paragraph alone and its section checked, like any other change (`docs/HUMANIZATION-GATE.md`, step 9, E96).
- The three that flipped were a wink after a quip, a dog in the middle of a paragraph after a short line, and a grin after a joke, with a stacked heading above. Three cases don't make a rule. The ones that held were a pointer, a sound, a face reacting to an emotional line, a body cue, and Joel's own picks on dialogue.
- The checked texts are in `tools/pangram-runs/2026-10-01-turn9-a.json` and `-c.json`, the predictions and results in `tools/PREDICTIONS.md`, and the flips in `tools/humanization/calibration/` as `FAIL_emoji_*`, with their controls as `PASS_emoji_*`.

## Joel's rulings (2026-10-01 04:53 UTC) and what changed (turn 10)
- **Banned:** pointers ("those look super ai, only after seen them from ai slop, don't ever use those"), 😉 ("looks like mainly used by AI (or by scammers)"), and gratuitous ones like the 🐶 ("we don't need an emoji just because it could be there"). He asked for a banned list, "which would be most of them": `tools/humanization/EMOJI-LIST.md`.
- **Came out:** 👇 at the map (a pointer), and 🎶, 💆 and 🔥, which only repeated a word ("song", "massage", "burning"), like the dog. Those paragraphs are back to text that had passed before.
- **His replacements,** checked in place (turn 10, try 1 each):

| Section | Change | Paragraph alone | Section |
|---|---|---|---|
| You Don't Need an Inner Monologue | "you might not be some people (hehe)." for the 😉 | 100% Human (74) | 100% Human (232) |
| Noticing Counts | "You'll sound a bit like Elmo :)" for the 😄 | 100% Human (68) | with its h1, 100% Human (163) |

So the emoji that fails can be the problem, not the spot: the same lines pass with ASCII. He says the other emojis he tried after "some people" all tested as AI.
