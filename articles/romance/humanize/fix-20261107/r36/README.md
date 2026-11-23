# r36: his sixth-page answers, "honestly" put right, and the section recheck (2026-11-23)

His message of 2026-11-23 19:36 UTC brought the sixth marking page's answers
(`../../../review/teach-20261123/ANSWERS-T6.json`) and a correction: "yeah i mean you can't just switch honestly for
compassionately always that's working sometimes, but like authentically, genuinely, those are more real synonyms, and
honestly is also ok sometimes just it's overused".

## What went into the fixed version

[apply_t6.py](apply_t6.py) writes [HIS-T6.json](HIS-T6.json), the layer `../whole/build.py` applies after r35:

| Card | What went in | Its check |
|---|---|---|
| J-B10 (What we mean by love) | my fix, approved | [Human, High](https://www.pangram.com/history/46351c02-95e5-41d5-8044-3413fb07cc47) |
| J-B84 (It always goes deeper) | the line cut, approved | his paragraph before it, [Human, High](https://www.pangram.com/history/c12ff059-dc9e-432d-bc7f-bddb2219ebaf) in his check |
| J-B201 (Slow & steady) | my fix, approved | [Human, High](https://www.pangram.com/history/ef1f216b-1b56-4d93-8744-c471e85a5933) |
| J-B220 (Don't make your partner your whole world) | my fix, approved | [Human, High](https://www.pangram.com/history/b7aa8694-67eb-4170-9bb3-3ef562c34919) |
| J-B379 (Attraction and exclusivity) | my fix, approved | [Human, High](https://www.pangram.com/history/2b637949-e160-4da0-a203-c7a0332a367d) |
| J-B412 (Psychedelic Timing) | my fix, approved | [Human, High](https://www.pangram.com/history/74a3b94f-ed02-4fc4-9fd8-44aeb688bb8c) |
| J-B453 (Ending consciously) | my fix, approved | [Human, High](https://www.pangram.com/history/ab01adee-1d7d-4259-a060-215bce4186e2) |
| Q-B442 (What will honesty produce?) | his own version | [Human, High](https://www.pangram.com/history/48952c2b-ff84-4e2c-97f8-c6bff836ceac) (his check) |
| Q-B257 (Different levels) | his own version | [Human, High](https://www.pangram.com/history/126e846d-7968-4de2-a5ba-4124a5685dae) (his check) |
| Q-B480 (Tough Love) | no change: "makes sense to me as is" | on the keep-as-is list |
| 366 (Jealousy on trial) | his "honestly" back, his own sentence | [Human, High](https://www.pangram.com/history/8f1e5924-1921-4136-8815-d09f45d295e5) (his check), and the section pass |
| 440 (After leaving) | his "honestly" back, his own sentence | [Human, High](https://www.pangram.com/history/f72e86ef-fd45-4fa2-934d-14e776d8021a) (his check) |

Then [MINE-R36.json](MINE-R36.json): 455's "blossom in its own time" (r34), a word about when where the sentence meant how,
became the real synonym he named, "blossom genuinely": [Human, High](https://www.pangram.com/history/7d938af3-9db2-4af5-aab9-78d28ea6e517)
by itself (ledger romance-r34-p487, try 2; its receipt in `work/`). The article now says "honestly" twice, both his. The
other two model-text uses keep their r34 words: 15 drops it ("willing to find out with you") and 433 says "fairly", where
the next sentence asks for both sides.

The keep-as-is list (`../whole/KEEP-AS-IS.json`, new): B480's sentence and his "It is its own reward" and "Asking that
question out loud" (his answers), his two uses of "honestly" (my reading, not asked), and J-B84's cut.

## The section recheck

Every section whose text changed since the section pass (r32) was checked once more by itself ([sections.py](sections.py),
[CHANGED.json](CHANGED.json), predictions by [predict_r36.py](predict_r36.py), ledger batch romance-r36). The flaws section
is left out: its text now is the one r33 rechecked ([Human; High, Medium, High](https://www.pangram.com/history/dd319996-2440-46c1-8d80-73e1e132add4)).

| Section | What changed | Recheck |
|---|---|---|
| What we mean by love, part 1 | J-B10 | [Human, High](https://www.pangram.com/history/d14e0dfc-1307-4c2e-8063-8b550584a2f8) |
| What we mean by love, part 2 | J-B10 | [Human, High](https://www.pangram.com/history/a50e2d8d-4961-4593-b22d-a1ca724fa063) |
| Talk about making love before you do it, part 2 | r34: 15 | [Human; High with three Medium one-sentence windows](https://www.pangram.com/history/e73ea65d-815d-462a-85cc-d81e2ab597f0) |
| It always goes deeper | J-B84 | [Human, High](https://www.pangram.com/history/5e5fc9cb-9f54-40af-be31-0adb5fdc34ed) |
| Slow & steady isn't KO'd yet, part 2 | J-B201 | [Human, High](https://www.pangram.com/history/a15f0e43-ed73-48c9-a182-60b319914e94) |
| Don't make your partner your whole world, part 2 | J-B220 | [Human, High](https://www.pangram.com/history/5cf2621a-fd06-4234-99ba-536ca6007797) |
| Different levels in different domains, part 2 | his B257 | [Human, High](https://www.pangram.com/history/8d39d55d-de90-469c-8300-7ab12604de33) |
| Attraction and exclusivity | J-B379 | [Human, High](https://www.pangram.com/history/03535531-f841-42f5-b9a5-d7b6531b5c7e) |
| Psychedelic Timing | J-B412 | [Human, High](https://www.pangram.com/history/81232e47-1773-418d-a930-d8998ed24480) |
| What will honesty produce? | his B442 | [Human, High](https://www.pangram.com/history/16945f4c-ddb9-46d6-a68d-0836eb065551) |
| Ending consciously | J-B453 | [Human, High](https://www.pangram.com/history/c144c4d7-b42b-462d-80a5-9249b46b0645) |
| Gaslighting in the dark | r34: 433 | [Human, High](https://www.pangram.com/history/a22f8aa7-5aa8-42e1-afa8-4e6c7c9e4903) |
| What I gained from loss | r35: B473 | [Human, High](https://www.pangram.com/history/33fc2537-5294-4dd8-b9e4-70a7b04c5dfa) |
| Tough Love, part 2 | r36: 455 | [Human, High](https://www.pangram.com/history/9faa89e4-8136-44a3-8c44-250a0236f640) |

Thirteen read Human High in one window. "Talk about making love", part 2, reads Human with three Medium windows of one
sentence each ("One person may mainly think of bonding ...", "It doesn't have to mean the same thing every time.", "If
our libidos later diverge ..."), none of them the sentence r34 changed, which sits in a High window; it read one High
window in the section pass. No Low window anywhere, so it is done by his measure (a Medium window is acceptable when
there is no Low one; gate neuro-2026-11-06c).

## His two versions, as lessons

Lesson romance-2026-11-23h (`docs/lessons/2026-11-23-1936-romance.md`): his fixes of B257 and B442 changed only the
flagged words and their order, with words the passages already had, where my r35 tries explained more and read AI. Way 24
and new lines of way 10 in `tools/humanization/his_fixes_brief.md` say it; a Fable writer given them rewrote both
passages blind, and both read Human High by themselves (`../r30/replay5/RESULTS.md`).
