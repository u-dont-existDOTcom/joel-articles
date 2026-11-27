# r48: one person answers each question once (the game's v0.9.3), and the lessons go to the universal rules

His message, 2026-11-27 16:17 UTC, after playing v0.9.2 on his own:

> it's weird, so it gives the question then i click i have my answer in mind then it asks what the answer is based on,
> then once again it brings thes ame question and button says i have answered it. and yes add that uda rule and any
> other lessons for uda

Nothing in the article changed.

## The game's v0.9.3

In his private repository `love-honestly`, on the branch of
[its draft pull request](https://github.com/u-dont-existDOTcom/love-honestly/pull/2), which now carries v0.6.0 to
v0.9.3. Nothing is merged or deployed: his site still serves v0.5.4.

- The game for one person had copied the couples' three steps for a question (form the answer in private, label what it
  rests on, say it aloud). The private step is there so two people answer before hearing each other; alone, the third
  step only asked the same question again.
- Now one person answers on step 1, aloud or in writing ("I have answered it", which counts the card as played), then
  says what the answer rests on, then goes on to the follow-up. The question shows on step 1, and smaller on step 2,
  and not again. The setup line for one person gives the new order.
- The game for two people doesn't change: its question comes back on the shared screen, where both say their answers
  to each other.
- Seen while playing it on a phone: the one-person follow-up button broke "follow-up" at its hyphen; it now stays whole.
- [What changed in v0.9.3](https://github.com/u-dont-existDOTcom/love-honestly/blob/claude/v0.6.0-article-update/versions/v0.9.3/CHANGES.md).

Checks: `build.py --check`; `check.mjs --mutants` (seven deliberate breakages caught); `browser-check.mjs`, 156 checks,
run twice (section 9 plays the game for one person in the new order; the new section 12 checks that the question shows
on step 1 and step 2 only, that answering counts the card as played, that a game saved on the old third screen goes
on, and that two people still share their answers on the shared screen). Not run: the container gate (needs Docker).
SHA-256 of v0.9.3: `e2db6db3553fb009a08e4a78bd42858ff43bcca15eccab7f91770981adc16d0c`.

Sent to him: the file in chat (`love-honestly-v0.9.3-candidate.html`), a picture of one card for one person step by
step, and the private page of the account that ran this turn, republished as v0.9.3.

## The lessons in the universal rules

[Draft pull request 506](https://github.com/u-dont-existDOTcom/universal-dev-architecture/pull/506) in
universal-dev-architecture, labelled for its maintainer lane:

- the rule owed since 2026-11-25 (lesson romance-2026-11-25c): an interactive file or page he opens from a chat is
  tested inside the chat's sandboxed frame, through its first full step;
- a batch waiting for his approval is read for him first, and only what is his to decide goes to him (25d); what he is
  asked to judge goes to him whole, in the reply too (26c);
- a correction he asks for in one tool reaches every copy of the same fault, the same turn (25a);
- four screen-design lessons filed in the design repository's lane for its agent: the biggest text says what the screen
  is about (26d), labels are read alone (26b), an attached explanation earns its place (26a), and a step carried over to
  another mode stays only where its reason holds (27a, this turn's lesson).

Lesson 25b (a rewording brief says that everything else stays) is already a universal rule
(`patterns/transformation-preservation-proof.md`), so it wasn't repeated.

## Lesson

romance-2026-11-27a: a step carried over from one mode to another stays only where its reason still holds
([the lesson](../../../../../docs/lessons/2026-11-27-1617-romance.md)).

## Next

His OK on a version of the game (v0.9.3 carries v0.9.1's and v0.9.2's changes), or his changes to it; then the pull
request is merged, the innerself site vendors the file, and the site is deployed with his go-ahead.
