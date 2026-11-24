# r38: his seventh-page answers (2026-11-24 02:06 UTC)

His answers: [ANSWERS-T7.json](../../../review/teach-20261124/ANSWERS-T7.json) (the page:
https://claude.ai/artifact/2YcdQ9tPPdAeEV1ZtU13NW). Nine cards approved, two questions answered.

## What went into the fixed version

[apply_t7.py](apply_t7.py) writes [HIS-T7.json](HIS-T7.json), the layer `../whole/build.py` applies after r37's:

| Card | What went in | Its check |
|---|---|---|
| M-07 "Then what? You block her?" | approved | [Human, High](https://www.pangram.com/history/d29e7a30-b543-45c9-a1af-c0eeeb7b3caf) |
| M-16 sex appeal "isn't the basis anymore" | approved | [Human, High](https://www.pangram.com/history/0b928214-0ed5-43e5-b495-f68bfc7028b9) |
| M-26 "how well we actually handle our own issues" | approved | [Human, High](https://www.pangram.com/history/39e78fb6-8b3e-4692-bec6-4cc4f261b23f) |
| M-28 "because if somebody starts with enough trauma" | approved | [Human, High](https://www.pangram.com/history/bd788843-ff5f-417c-9242-5aeee7123f33) |
| M-31 twin flames, and the women I still love | approved | [Human, High](https://www.pangram.com/history/8d070089-ca59-4476-a372-f3fbe75cb711) |
| M-35 "much stronger barriers than these" | approved | [Human, High](https://www.pangram.com/history/1867a533-baa4-4926-af33-d26bf54676fb) |
| M-54 "but woops, I came too fast" | approved | [Human, High](https://www.pangram.com/history/1b906fcb-7099-4a0e-8948-7d0db749969b) |
| M-68 "With H., I learned" | approved | [Human, High](https://www.pangram.com/history/231c824d-3dbe-44c5-be5d-3fe52fc88574) |
| M-82 "That drove me crazy, because" | approved | [Human, High](https://www.pangram.com/history/7a6a097c-d8a6-4c63-af8b-afd18d8193d8) |
| Q-67 Two Pillars, part 1 | his own fix ("damn this was an absolute disaster. i fixed it"), from his check: [his-67.txt](his-67.txt), the text Pangram holds for it (SHA-256 d5cab2e8...), replacing live 330 to 335 | [Human, High, one window, 0% AI](https://www.pangram.com/history/1deb924a-6175-4847-95eb-38e1871287c3) |

[mine_r38.py](mine_r38.py) writes [MINE-R38.json](MINE-R38.json), after it: Q-42, section 42's last clause, which a
fresh reader couldn't parse (junk-read B210), said from his answer ("Bee would accuse me of manipulating her, even though
I was making an effort not to, and ironically she actually wanted me to manipualte her more and called me her wife
because i wouldn't"): "without ever manipulating her. Bee would accuse me of manipulating her even when I was making an
effort not to, and ironically, she actually wanted me to manipulate her more." The wife part stays where the article
already tells it ("Romance Shouldn’t Be Adjudicated"). The section with it ([t42/](t42/), with its receipt):
[Human, High, one window](https://www.pangram.com/history/2d6004a1-e6e4-4270-9f50-2fb4f96c8d13), predicted first.

## Where the article stands

[sections.py](sections.py) cuts the fixed version (21,062 words) into its 93 section checks (`checks/`): 91 are texts a
check of mine read Human High in every window (the ledger), and the other two are his own fixes, which his checks read
Human High in one window (05, [4028a476](https://www.pangram.com/history/4028a476-97bc-4504-961b-dd80a7192238); 67,
[1deb924a](https://www.pangram.com/history/1deb924a-6175-4847-95eb-38e1871287c3)), word for word. No section has a window
below High.

## The blind test of his Two Pillars fix (his standing rule)

- Round 7 ([RESULTS](../r30/replay7/RESULTS.md)): the order as a way of its own, illustrated outside the test:
  [AI, 47%](https://www.pangram.com/history/70006aef-fd88-4cbe-9846-4e9dad3d00de).
- Round 8 ([RESULTS](../r30/replay8/RESULTS.md)): leave to cut a point the argument doesn't need, and the label, the
  repeat and the advice's place said in general words:
  [Human, 0% AI, with Medium and Low windows](https://www.pangram.com/history/0a1e1704-ae17-4fae-bd41-2015b5630118).
- Lesson romance-2026-11-24a (`docs/lessons/2026-11-24-0206-romance.md`): a section whose Medium windows survive
  word-level fixes needs its order and its unneeded lines fixed first; a blind writer gets it to Human, and what the
  section builds to, said from his experience, is his. His fix is way 28 of `tools/humanization/his_fixes_brief.md`.

## A slip this round

`r37/sections.py` wrote this round's cut over `r37/checks/` before r38 had its own copy; r37's files were put back from
Git, and both scripts now refuse to write over an existing `checks/` folder without `--again`.
