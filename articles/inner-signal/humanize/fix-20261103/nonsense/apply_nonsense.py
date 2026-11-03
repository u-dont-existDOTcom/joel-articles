"""Fix what the nonsense read found in our words (Joel, 2026-11-03 13:46 UTC: "i also noticed the tag questions part above
says "oily" instead of old. do we have more nonsense in here (from emulate i guess)? how are you not catching this?").

Two passes read the whole guide (reads/, pass2/reads/). The second carried nine planted errors of the "oily" kind
(CANARIES.json) and found all nine, so its silence elsewhere is worth something. Every finding was read in place and
traced: his published guide of 28 September (the AI-drafted guide he published), his own paragraphs, his inner child
guide, Emulate's output, or ours (FINDINGS.md). Fixed here, in our words:

- Love doesn't have to wait for trust, P1: "Their trust can question your promises, remember when you failed to protect
  them, and take its time." (trust doing the questioning; both passes) -> "They can question your promises, remember
  when you failed to protect them, and take their time."
- Working with your guards, P3: "Often what you're experiencing is a very charming guard." (both passes read "charming"
  as a slip; in his published guide it was irony: "the protector making an appearance in its usual charming way") ->
  "Often it's a guard, making an appearance in its usual charming way."
- Methods to explore with a trained person present, P3: "one or more of trauma-specific variants" -> "one or more of the
  trauma-specific variants".
- Future pacing, P2: the full stop missing after "Implementation Intention".
- Unwinding object, P1: "Imagine an object unwinding – maybe some yarn, some bubbles, or some knots that you place beside
  you." (bubbles don't unwind) -> his published picture, "Imagine some yarn unwinding, some bubbles settling, or some
  knots that you place beside you."
- Finding a hypnotist who can work with you, P14: "use this app or" goes ("this app" points at nothing; Emulate's
  sentence, run HG35-fxw2 of 18 October).

Questioned but his own words, so his call (question 34): "playing asleep", "the mental escape into the body's flow",
"when they were led to (which NLP tends to)", "taking off the kid gloves", and his published "repeated correction
between intuition, subconscious response, and conscious analysis".

  python3 articles/inner-signal/humanize/fix-20261103/nonsense/apply_nonsense.py [--check]
Writes HUMANIZED-SO-FAR.md, APPLIED-NONSENSE.json and read/READ-RECORD.json.
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text  # noqa: E402

GUIDE = H / 'HUMANIZED-SO-FAR.md'
BEFORE = 'bb5fc57de174b36c9e1bed333354a0f79e2c74811564f505a505950c5b5e7300'
EDITS = [
    ('trust', 'Their trust can question your promises, remember when you failed to protect them, and take its time.',
     'They can question your promises, remember when you failed to protect them, and take their time.'),
    ('charming', 'Often what you\'re experiencing is a very charming guard.',
     'Often it\'s a guard, making an appearance in its usual charming way.'),
    ('the variants', 'recommend one or more of trauma-specific variants', 'recommend one or more of the trauma-specific variants'),
    ('full stop', 'I will choose new small behaviors using an Implementation Intention',
     'I will choose new small behaviors using an Implementation Intention.'),
    ('yarn', 'Imagine an object unwinding – maybe some yarn, some bubbles, or some knots that you place beside you.',
     'Imagine some yarn unwinding, some bubbles settling, or some knots that you place beside you.'),
    ('this app', 'You might even be able to use this app or ask around', 'You might even be able to ask around'),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    md = GUIDE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert sha == BEFORE, 'the guide changed'
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    lost, fates = [], {}
    for name, old, new in EDITS:
        hits = [b['i'] for b in bl if old in b['text']]
        assert len(hits) == 1, (name, hits)
        i = hits[0]
        t = bl[i]['text']
        assert t.count(old) == 1
        if name == 'full stop':
            assert t.endswith(old), 'the sentence should end the block'
        raw[i] = set_block_text(raw[i], t.replace(old, new), lost)
        fates[name] = {'block': i, 'where': sr.where(bl, i), 'before': old, 'after': new}
    assert not lost, lost
    new_md = '\n\n'.join(raw) + '\n'
    after = hashlib.sha256(new_md.encode('utf-8')).hexdigest()
    rec = {'before_sha256': sha, 'after_sha256': after, 'fixes': fates}
    print(json.dumps(rec, ensure_ascii=False, indent=1))
    if a.check:
        return
    GUIDE.write_text(new_md, encoding='utf-8')
    (HERE / 'APPLIED-NONSENSE.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    olds = {b['text'] for b in bl}
    changed = [b['text'] for b in sr.blocks(new_md) if b['text'] not in olds]
    d = HERE / 'read'
    d.mkdir(parents=True, exist_ok=True)
    cr.record(d, findings=[], coverage=sorted({cr.phash(t) for t in changed}), dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: the %d paragraphs the nonsense read\'s fixes changed, each read in place '
                      'beside his published version by the lead session (E284, E294, E331)' % (after[:8], len(changed)))


if __name__ == '__main__':
    main()
