# r44: the game's Build button fixed, Spiritual Practice made a personal topic, and the 204 card texts read for him

His message, 2026-11-25 17:20 UTC:

> 200 cards is too much for me to read can you just tell me if any of them look like i should check? i already checked
> the cards that were in the game before more were added so that gives you a reference point for what i approve
>
> can we make spiritual practice personal instead of optional?
>
> i tried to biuld the game but build button did nothing (one phone)

Nothing in the article changed this round. Everything below is in his private repository `love-honestly`, on the branch
of [its draft pull request](https://github.com/u-dont-existDOTcom/love-honestly/pull/2), which now carries v0.6.0,
v0.7.0, v0.7.1 and v0.8.0. Nothing is merged or deployed: his site still serves v0.5.4.

## 1. "the build button did nothing"

- The cause: he opened the v0.7.0 file from the chat on his phone. A chat app shows an HTML file inside a frame that
  blocks form submission. "Build our game" was the setup form's submit button and the game started on the form's
  "submit", which the browser never sends in such a frame. The button did nothing and said nothing. "Join the game" had
  the same fault. On his site neither would have failed.
- Reproduced before it was fixed: the v0.7.0 file in a frame sandboxed with scripts allowed and forms not; a tap on
  "Build our game" leaves the setup screen as it was.
- Fixed in v0.7.1: the tap starts the game itself. Played in two such frames from the welcome screen through a whole
  card; Enter in a name field and "Join the game" work there too; outside a frame one game is built, once.
- Why the earlier checks missed it: every check opened the file as a page of its own (a local server with the site's
  headers, or the innerself build). None opened it the way he would, from a file card in the chat (lesson
  romance-2026-11-25c).
- He also has it as a private page of this account now ("Love, Honestly v0.8.0 (candidate)"), which opens from a link.
  The page differs from the file in two places only: its title, and its viewport line without `viewport-fit=cover`.

## 2. "can we make spiritual practice personal instead of optional?"

- In v0.7.1 the topic is no longer optional: its chip reads "Personal" and it begins ticked, the change v0.7.0 made for
  Attraction & Polarity (whose description to him was "no longer 'optional', its chip reads 'Personal'"). A saved setup
  gets it ticked once.
- The other reading (the chip only, the topic left unticked) was named to him in the same turn. It is one line.
- In v0.7.1 its four cards are all Unfiltered, so only an Unfiltered game changes. With v0.8.0's two Warm cards the
  topic reaches Warm and Deep games too, which is why those two cards were named to him.

## 3. "can you just tell me if any of them look like i should check?"

- All 204 items read by the lead (this session's model, itself) against the 112 cards of v0.7.0, the 95 he checked in
  the game and the 17 he approved on 2026-11-24, and against the guide as it is now (`whole/FIXED.md`).
- Six claims checked against the guide's lines: the father's advice and its two questions (line 37); "try not to wait
  for that" (869); "it takes a village" (897); the Buddha's advice to the married couple (639 to 641); the two Bible
  verses (745); the "sex dolls" line (153).
- Every proposed text scanned for the words and marks the card rules rule out: none in a Warm card, a plainer line, a
  new one-person card or a step.
- Result: nothing says what the guide doesn't, and nothing reads unlike the cards he approved. Four items went to him:
  [the four to check](https://github.com/u-dont-existDOTcom/love-honestly/blob/claude/v0.6.0-article-update/proposals/2026-11-25/TO-CHECK.md)
  (the Warm card with his "sex dolls" line, W03; where "On my own" goes; the screen one person sees first; the seven
  labels for one person). The three design points have a pick of mine each, and the one-person route is built with
  those picks if he says nothing.
- Three lines corrected before they went in, each named to him: the "why" of `promises-plain-yes` (what the guide uses
  the verses for), the "why" of `spiritual-pleasant-words` (the couple asked about future lives; "restrained" kept), and
  the plainer question of `conflict-06` (it keeps "crucible", with its plain meaning beside it).
- What became of every item:
  [the fates](https://github.com/u-dont-existDOTcom/love-honestly/blob/claude/v0.6.0-article-update/proposals/2026-11-25/FATES.md).

## 4. Built: v0.8.0, a candidate on top of v0.7.1

- 27 Warm cards (W03 held) and 92 plainer questions and follow-ups on 62 older cards. Nothing else changed.
- 131 cards, 36 of them Warm (9 of 104 before); every topic has at least two. "A lighter one instead" stays on the
  card's own topic in 1,883 of 1,905 swaps tried (974 of 2,776 in v0.7.1).
- Checks: `build.py --check`; `check.mjs --mutants` (30 checks, six deliberate breakages caught); `browser-check.mjs`
  (59 checks, Chrome, the site's headers), with a Warm game played to its end and the frame test again. v0.7.1 when it
  was built: 16 checks with five breakages caught, and 53 browser checks.
- One run of the browser check in five timed out in the two-phone part the v0.7.0 check already had: the game drew its
  deal's starting number at random, and now and then the first card was one with no everyday step to read. The check
  pins the number now.
- Not run: the repository's container gate (needs Docker).
- SHA-256: v0.7.1 `1620f28fde05a3149861d6fbcae25d2fcdb83335cfe7a8eebb39ceb173eabc86`; v0.8.0
  `a657f8533e501e041ce497759f4b23aa080005c7c74128da1f981d5db7715ce4`.
- [What changed in v0.8.0](https://github.com/u-dont-existDOTcom/love-honestly/blob/claude/v0.6.0-article-update/versions/v0.8.0/CHANGES.md);
  [what changed in v0.7.1](https://github.com/u-dont-existDOTcom/love-honestly/blob/claude/v0.6.0-article-update/versions/v0.7.1/CHANGES.md).

## Not done, and why

- The one-person route: an interface change of its own, and three points of its design are with him. Next: built with
  his answers or my picks; the 41 cards turned toward one person take the plainer line where v0.8.0 changed the
  couples' line; one-person wording for the Warm cards; the seven older "why" lines.
- The innerself site: untouched. It vendors a version only once he approves one.
- A suggestion for the universal rules (an HTML file sent in chat is opened in a frame that blocks forms, storage and
  dialogs, so it is tested there): owed, not filed this turn.
