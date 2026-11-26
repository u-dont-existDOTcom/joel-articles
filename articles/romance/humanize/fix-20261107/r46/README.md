# r46: the biggest text says what the screen is about (the game's v0.9.1)

His message, 2026-11-26 23:26 UTC, with a screenshot of the one-person label screen at desktop width:

> ok i tried playing by myself. one thing i would change is the top text should be the biggest heading, because people
> read the biggest one first and that's the one that explains what this is about. sending screenshot

Nothing in the article changed. Everything below is in his private repository `love-honestly`, on the branch of
[its draft pull request](https://github.com/u-dont-existDOTcom/love-honestly/pull/2), which now carries v0.6.0 to
v0.9.1. Nothing is merged or deployed: his site still serves v0.5.4.

## What he saw, and v0.9.1

v0.9.0's label screen for one person opened with a small line, "Where this card leaves you", over the biggest text,
"Pick the one that fits best." The biggest text was the instruction, and what the screen is about was the smallest.

- The heading is now **"Where does this card leave you?"**; the line under it reads "Pick the one that fits best. Each
  one says what it means, and your choice stays on this phone."; the small line on top is gone. Labels unchanged.
- In his screenshot the line under the heading began further right than the heading (it sat in a centred column on a
  wide screen). On every left-aligned card it now starts where the heading starts: the one-person label screen and the
  couples' "Mark this privately.", two-phone label and "Which label did ... choose?" screens. Same words. The centred
  "Pass the phone" cards stay centred.
- The text cut off at the bottom of his screenshot is the crop: measured at 655 to 1280 pixels, nothing runs off the
  screen.
- [What changed in v0.9.1](https://github.com/u-dont-existDOTcom/love-honestly/blob/claude/v0.6.0-article-update/versions/v0.9.1/CHANGES.md).

## Put to him

His rule would also change the "What is this answer based on?" step, in both modes: there the card's question is the
biggest text and "What is this answer based on?" is smaller, under it. My recommendation: apply it (that heading big,
the question shown smaller as what is being answered), since the screen asks for the basis, not the answer. Not built
until he says.

## Checks

- `build.py --check`; `check.mjs --mutants`: four deliberate breakages caught (the old small line back, the
  instruction as heading again, the alignment rule gone, a couples' screen changed).
- `browser-check.mjs`: 104 checks, run twice; its new section 10 measures, at 390, 768, 1024 and 1280 pixels, that the
  one-person label screen's heading is its first and biggest text and that the line under it starts where it starts,
  the same on the couples' label screen, and that the "Pass the phone" line is still centred.
- Not run: the repository's container gate (needs Docker).
- SHA-256 of v0.9.1: `448e0187d580430ebc472949d20d9e2e2ec1902f28aa4a9a2b14ed6589995c64`.

## Next

His word on v0.9.1 and on the evidence step; then the pull request is merged, the innerself site vendors the file, and
the site is deployed with his go-ahead.
