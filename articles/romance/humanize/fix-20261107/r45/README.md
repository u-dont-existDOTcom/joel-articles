# r45: his four answers built into the game (v0.8.1 and v0.9.0, the game for one person)

His answers, 2026-11-26 22:17 UTC (sent again at 22:43), on the four items put to him in r44:

> 1. fine but remove the "why this card" for this... and look at other "why this cards" i'm wondering if they should all
> be removed unless they actually give some necessary context. with this card i don't think any context is needed.
> 2. b
> 3. ok
> 4. i need to watch what i do sounds like i'm afraid to do what i really want or something like that. can we have the
> full explanations shown?

Nothing in the article changed. Everything below is in his private repository `love-honestly`, on the branch of
[its draft pull request](https://github.com/u-dont-existDOTcom/love-honestly/pull/2), which now carries v0.6.0 to
v0.9.0. Nothing is merged or deployed: his site still serves v0.5.4.

## 1. "Why this card?": v0.8.1

- The rule I took from his message: a card keeps its "why" only where a player who has not read the guide could not
  tell what the question asks, or would be likely to take it wrongly, without it. A line that says what the guide
  thinks, tells its story or says why the topic matters goes.
- All 139 lines read beside their questions: 5 stay, 134 go ([each line and its fate](https://github.com/u-dont-existDOTcom/love-honestly/blob/claude/v0.6.0-article-update/versions/v0.8.1/whys.json)).
  The five: two safety lines (`conflict-06`, `altered-03`) and three that explain what the question points at
  (`spiritual-relationship-spirit`, Sobonfu Somé's idea; `children-05`, "a father's advice"; `clarity-undefined-thing`,
  "Why are you making this heavy?"). A card without one shows no button.
- The Warm card W03 (`love-wanted-for`) goes in as he was shown it, without its "why".
- [What changed in v0.8.1](https://github.com/u-dont-existDOTcom/love-honestly/blob/claude/v0.6.0-article-update/versions/v0.8.1/CHANGES.md).

## 2. The game for one person: v0.9.0

- "2. b": "Who is playing? Two of us / Just me" is the first question on the setup screen. "Just me" hides the second
  name, "One phone or two?" and the routes, and deals from every route.
- "3. ok": the screen before the first card, as written.
- "4.": "I need to watch what I do" is now **"Life will show me"** (explanation unchanged: "Thinking won't settle this.
  What I do in everyday life will show me."). Every label shows its explanation under its name, as the couples' labels
  do. My reply in r44 had listed the seven by name only, which is what he asked to see in full (lesson
  romance-2026-11-26c).
- 95 cards with one-person text: the 41 he approved (17 lines taking the plainer v0.8.0 wording, as FATES.md said they
  would), 18 Warm cards worded for one person by me, 22 played as they are, and the 14 one-person cards (without their
  "why"). A step per topic, an evidence map and a revisit for one.
- The couples' game is not changed: 28,800 deals and 2,560 swaps compared with v0.8.1.
- [What changed in v0.9.0](https://github.com/u-dont-existDOTcom/love-honestly/blob/claude/v0.6.0-article-update/versions/v0.9.0/CHANGES.md); [the one-person texts](https://github.com/u-dont-existDOTcom/love-honestly/blob/claude/v0.6.0-article-update/versions/v0.9.0/solo.json).

## Checks

- v0.8.1: `check.mjs --mutants` 25 checks, seven deliberate breakages caught; `browser-check.mjs` 66 checks.
- v0.9.0: `check.mjs --mutants` 28 checks, eight breakages caught; `browser-check.mjs` 91 checks, run twice (a whole
  one-person game on a phone, and in a frame that blocks forms, at 320 pixels).
- Not run: the repository's container gate (needs Docker).
- SHA-256: v0.8.1 `739441e6a672e75bcceddf4963e1212924165a6304b0c293f17013fb2bf78db8`; v0.9.0
  `9583d7f409043145f833ba845cfd45653f1a3745ad949e59de0de71c248a970b`.

## Wording of mine in v0.9.0

The setup line for one person, the step lines, the evidence map's lines, and the one-person wording of 18 Warm cards
(all named in v0.9.0's CHANGES.md). None changes what a card asks; none was put to him as a question.

## Next

His word on v0.9.0 (or his changes); then the pull request is merged, the innerself site vendors the file, and the site
is deployed with his go-ahead. Still owed: the seven older "why" lines of plain-words.json are moot now (their lines are
out); a suggestion to the universal rules that an HTML file sent in chat is tested in a frame that blocks forms.
