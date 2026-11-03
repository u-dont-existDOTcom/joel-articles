"""Batch l1103: fixes of ours for the Human (Low) windows the third free check read in our words (../free-whole/read/
WINDOWS.md; Joel's result pages of 2026-11-03 11:19 UTC), each read for overcompletion first (E328), then E321's order.
They go into CANDIDATE-MASTER.md for the fourth free check, not into the guide: for these windows a stretch check through
the API didn't predict the whole (F-361 and F-528 read Human High or Medium in their stretches on 2 November and Human (Low)
in both whole checks after), so the free whole check is the test that decides, and it costs no credits (E325).

- F-320 (Let the next response guide you, P1): "After that, it's about answering what happens, instead of reading out a
  script that has already decided what every part of you is going to say." said plainly: you answer what comes up, and you
  can't know ahead of time what every part of you will say (his published "instead of reciting a speech that has already
  decided what every part will say", kept as the reason); the next instruction says what to do ("put the screen away")
  instead of "without looking at the screen" (linter E186).
- The linter's E125 FAIL on the 15-minute practice's last sentence ("sit in silence, listening, and you can interrupt
  yourself") is a misread: "sit in silence, listening" is one action and "you can interrupt yourself" a second clause, not
  a list of three; that sentence is unchanged and its window read High.
- F-356 (The 15-minute daily practice, P1): "It's the same process (five steps), just for fifteen minutes or so." explained
  the sentence before it again ("You don't need to learn a second script for this."), and its five steps recap what the guide
  has taught by then (E328); it becomes "Just do the same practice, from the induction to coming all the way back, for
  fifteen minutes or so."
- F-522 and F-523 (Pattern 10): "You need both to be ethical with people" leads the paragraph about the two models instead
  of the questions (his published "Ethical practice needs both" as the paragraph's first point, his P22 order: the
  principle first), and the questions get a plain lead-in.
- F-610 (EFT tapping, P1): "One of the easiest ways to do EFT ... is to say something like" said plainly; and the last
  sentence, left on its own by the cut of "So treat the evidence with caution, and know that" (P5b-04), joined to the review
  sentence as his published caution ("treated cautiously beside first-line therapies"): EFT isn't one of them.

  python3 articles/inner-signal/humanize/fix-20261103/l1103/fixes_l1103.py   (writes ../free-whole-2/CANDIDATE-MASTER.md)
"""
import hashlib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text  # noqa: E402

GUIDE_SHA = 'e4c620ed660c6ddf7e2f141a9b9d15dc49307e57cf954f39715a8562808d1aae'
# id, a phrase that finds the block, the old text, the new text
EDITS = [
    ('F-320', 'The induction and the inner meeting get you to where you can listen.',
     "After that, it's about answering what happens, instead of reading out a script that has already decided what every "
     "part of you is going to say. Read through these sections, and then try doing the inner meeting without looking at the "
     "screen.",
     "From there, you answer whatever comes up, and you can't know ahead of time what every part of you is going to say. "
     "Read through these sections first, and then put the screen away and try the inner meeting."),
    ('F-356', "You don't need to learn a second script for this.",
     "It's the same process (gather your attention, notice what's here, respond, wait, and come all the way back), just for "
     "fifteen minutes or so.",
     "Just do the same practice, from the induction to coming all the way back, for fifteen minutes or so."),
    ('F-522', 'Milton Model language opens things up, and Meta Model questions ask what exactly someone means.',
     'Milton Model language opens things up, and Meta Model questions ask what exactly someone means.',
     'If you want to be ethical with people, you need both kinds of language: Milton Model language opens things up, and '
     'Meta Model questions ask what exactly someone means.'),
    ('F-523', 'You need both to be ethical with people, so when something sounds true but vague, ask:',
     'You need both to be ethical with people, so when something sounds true but vague, ask:',
     'When something sounds true but vague, ask:'),
    ('F-610', 'One of the easiest ways to do EFT',
     'One of the easiest ways to do EFT (Emotional Freedom Techniques, or tapping) is to say something like, “Even though I '
     'have this anxiety, I am willing to be kind to the part of me that is afraid,” while you tap gently on your body and '
     'stay with what you feel.',
     'With EFT (Emotional Freedom Techniques, or tapping), you tap gently on your body while you say something like, “Even '
     'though I have this anxiety, I am willing to be kind to the part of me that is afraid,” and you stay with what you feel.'),
    ('F-610b', 'One of the easiest ways to do EFT',
     'and noted that EFT was more effective than no intervention in several of them. There are first-line therapies for '
     'anxiety.',
     "and noted that EFT was more effective than no intervention in several of them, though it isn't one of the first-line "
     "therapies for anxiety."),
]


def apply(md):
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == GUIDE_SHA, 'the guide changed'
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    texts, lost, where = {}, [], {}
    for eid, find, old, new in EDITS:
        hits = [b['i'] for b in bl if find in b['text']]
        assert len(hits) == 1, (eid, hits)
        i = hits[0]
        t = texts.get(i, bl[i]['text'])
        assert t.count(old) == 1, (eid, 'old text not found once')
        texts[i] = t.replace(old, new)
        where[eid] = (i, sr.where(bl, i))
    for i, t in texts.items():
        raw[i] = set_block_text(raw[i], t, lost)
    assert not lost, lost
    return '\n\n'.join(raw) + '\n', sorted(texts), where


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    new, changed, where = apply(md)
    out = H / 'fix-20261103' / 'free-whole-2'
    out.mkdir(exist_ok=True)
    (out / 'CANDIDATE-MASTER.md').write_text(new, encoding='utf-8')
    nb = sr.blocks(new)
    for eid, (i, w) in where.items():
        print(eid, i, w)
    for i in changed:
        print('[%d] %s' % (i, nb[i]['text']))
    print('candidate', hashlib.sha256(new.encode('utf-8')).hexdigest())


if __name__ == '__main__':
    main()
