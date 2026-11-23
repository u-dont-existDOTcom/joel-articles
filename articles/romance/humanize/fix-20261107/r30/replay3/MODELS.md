# Which model writes the blind rewrites (2026-11-23)

His question, 2026-11-23 16:58 UTC: "huh that's weird that opus isn't working? can we figure out why? what about fable?
i'm wondering if sonnet is good enough bc itt wasn't so useful in our tests before for this kind of thing as i recall."

## Why the Opus writers gave no answer

| Run (an Opus agent each time) | What it was given | Time | Answer |
|---|---|---|---|
| round 2 writer | the brief (15k characters, 21 ways), 8 items | about 14 minutes | yes |
| round 3, three writers | the brief (17k characters, 23 ways), 5 or 6 items | stopped after 20 to 27 minutes | none |
| round 3, bounded ("think briefly", under 1,500 words) | the same | stopped after about 20 minutes | none |
| one item of the same test, bounded | the same brief, 1 item | stopped after about 7 minutes | none |
| a tiny probe | read one small file and reply | 7 seconds | yes |
| one rewrite with no brief | the M-346 paragraph and one line of instructions | 36 seconds | yes |

So Opus agents run, and they rewrite a paragraph in seconds without the brief; given the full brief they don't finish,
even for one paragraph and even when told to be brief, and the time grew with the brief (14 minutes at 21 ways, nothing
in 20 minutes at 23). The agents' transcripts aren't kept in this session's files, so what they spend the time on can't
be read; the likeliest cause is that each sentence gets weighed against every way and its examples at length before
anything is written. An earlier lane saw the same shape with review agents that ran 25 to 30 minutes and stopped at the
output limit with no report (E178, `docs/HUMANIZATION-GATE.md`).

## Fable and Sonnet on the same test

Round 3's brief and paragraphs, each rewrite checked by itself in Pangram (his main account):

| Card | Sonnet ([CHECKS-R3.txt](CHECKS-R3.txt)) | Fable ([CHECKS-FABLE.txt](CHECKS-FABLE.txt)) | His version |
|---|---|---|---|
| M-73 | [Human, High](https://www.pangram.com/history/c65e536b-e589-4439-9a44-f53c3ae94c17) | [Human, High](https://www.pangram.com/history/91de6949-e207-483d-b7b9-cf221d152761) | [Human, High](https://www.pangram.com/history/c12ff059-dc9e-432d-bc7f-bddb2219ebaf) |
| M-214, its own window (the next paragraph read AI beside both) | [Medium](https://www.pangram.com/history/4a5f3b06-48ad-422d-a7c0-37b3187dddc0) | [High](https://www.pangram.com/history/095d62c8-0740-4195-b89f-b4ff5a991b59) | (no check named) |
| M-252 with M-253 | [Human (High, Medium)](https://www.pangram.com/history/da5c670e-0a19-4fb1-a60e-0fe1de260e23) | [Human, High](https://www.pangram.com/history/4dde1af9-1594-4142-8a21-794ee6662614) | (no check named) |
| M-346 | [Mixed, 77% AI](https://www.pangram.com/history/33ef19a3-6b9b-4ef2-aa54-a3d51fba9718) | [Mixed, 80% AI](https://www.pangram.com/history/37e3133e-8611-4885-a85b-c403bac06adb) | [Human, High](https://www.pangram.com/history/7df7a85b-4246-428d-b83a-34028f9a938b) |
| the flaws stretch | [AI, 100%](https://www.pangram.com/history/5fa5bc28-a67f-45b7-86c5-d31211495094) | [Human (High, Medium)](https://www.pangram.com/history/bf701281-9f3d-4ea9-b0f5-979dadc24199) | [Human, High](https://www.pangram.com/history/e7fa9711-caf2-469b-9c1a-6f4422e6ec39) |

Fable answered in 45 seconds, Sonnet in about a minute. Fable did better on three of the five and the same on two, and
read closer to his fixes: in the flaws stretch it moved the shut-down example up, kept his spoken "okay, what does that
mean:", and put the judgment question last on its own, where Sonnet turned the questions into reported ones ("Then ask
whether ..."), which read AI every time it was tried. Sonnet also cut more of his words (half of 214's second list). No
record in this repository compares the models as writers before today; on this test Sonnet is the weaker writer, as he
remembered. Blind rewrites go to Fable from now on (`AGENTS.md`, lesson romance-2026-11-23e).

## Round 4 and the one word in M-346

M-346 failed with every writer. A Fable writer given one exception to "add nothing" (the reason a question is asked may
be said when the paragraph already implies it) asked the dilemma itself ("if one of us falls in love with someone else,
is that already a betrayal, or a sign we need a serious talk?"), which moved that sentence from AI to Human, but the last
two questions still read AI ([Mixed, 67%](https://www.pangram.com/history/1c517bcf-92a0-4b83-bf90-59a6d811d052)). The
same text with one word of his fix, "compassionately" for "honestly", read
[Human, 0% AI](https://www.pangram.com/history/032efdc2-fdc9-4306-8618-7b7826337826) (windows High, Medium, Low): that
one word was most of what read AI ([../replay4/CHECKS-R4.txt](../replay4/CHECKS-R4.txt)). It is now in way 21 of
`tools/humanization/his_fixes_brief.md`.

## Curly or straight quote marks

His versions were typed with straight quote marks and the rewrites were checked with the article's curly ones, so the
two Sonnet rewrites still reading AI were checked again with straight marks ([../typo3/CHECKS.txt](../typo3/CHECKS.txt)):
no label changed (M-346 stayed Mixed at 78%; M-214's pair stayed at 45%), though M-214's own window went from Medium to
High. The typographic swap straightens them in the post anyway.
