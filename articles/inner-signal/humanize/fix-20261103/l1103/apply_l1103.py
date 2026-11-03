"""Put batch l1103's fixes into the hypnosis guide where the fourth free check read them in place (Joel's result pages of
2026-11-03 12:18 UTC, ../free-whole-2/read/WINDOWS.md), and record the read.

- In: F-320 (Let the next response guide you), F-356 (the 15-minute practice), F-610 and F-610b (EFT tapping). Their
  stretches have no window below Medium now; the third check read each Human (Low).
- Out: F-522 and F-523 (Pattern 10). The questions still read Human (Low) with the plain lead-in, and lower than before
  (calibrated 0.686 and AI likelihood 1.2e-4, from 0.784 and 4.6e-7), so the version that read better stays (E324), and
  the stretch goes to his page: two tries (F-528 on 2 November, this one) haven't cleared it.

The guide now is the candidate minus F-522 and F-523, plus his E-157 (../c1103/apply_answers_c1103.py, applied first).

  python3 articles/inner-signal/humanize/fix-20261103/l1103/apply_l1103.py [--check]
Writes HUMANIZED-SO-FAR.md, APPLIED-L1103.json and read/READ-RECORD.json.
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
sys.path.insert(0, str(HERE))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text  # noqa: E402
import fixes_l1103 as fx  # noqa: E402

GUIDE = H / 'HUMANIZED-SO-FAR.md'
BEFORE = 'c6847a080cdf100da6dedadaa7358a2f391720cb2fc0f74b9d9068a9dd410ff4'   # e4c620ed with his E-157
TAKE = ['F-320', 'F-356', 'F-610', 'F-610b']
LEAVE = {'F-522': 'Pattern 10 read worse (Human (Low), 0.686, from 0.784)', 'F-523': 'the same window'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    md = GUIDE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert sha == BEFORE, 'the guide changed'
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    texts, lost, fates = {}, [], {}
    assert sorted(TAKE + list(LEAVE)) == sorted(e[0] for e in fx.EDITS)
    for eid, find, old, new in fx.EDITS:
        if eid not in TAKE:
            fates[eid] = 'left out: ' + LEAVE[eid]
            continue
        hits = [b['i'] for b in bl if find in b['text']]
        assert len(hits) == 1, (eid, hits)
        i = hits[0]
        t = texts.get(i, bl[i]['text'])
        assert t.count(old) == 1, eid
        texts[i] = t.replace(old, new)
        fates[eid] = 'in (block %d, %s): its stretch read High or Medium in the fourth free check' % (i, sr.where(bl, i))
    for i, t in texts.items():
        raw[i] = set_block_text(raw[i], t, lost)
    assert not lost, lost
    new = '\n\n'.join(raw) + '\n'
    after = hashlib.sha256(new.encode('utf-8')).hexdigest()
    rec = {'before_sha256': sha, 'after_sha256': after, 'changed_blocks': sorted(texts), 'fates': fates,
           'check': {'part A': 'https://www.pangram.com/feed/c2f7a242-d7f1-40a5-8453-df9047c5947b',
                     'part B': 'https://www.pangram.com/feed/93dac4dd-cdea-49f2-8103-83211c1ebb4d'}}
    print(json.dumps(rec, ensure_ascii=False, indent=1))
    if a.check:
        return
    GUIDE.write_text(new, encoding='utf-8')
    (HERE / 'APPLIED-L1103.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    olds = {b['text'] for b in bl}
    changed = [b['text'] for b in sr.blocks(new) if b['text'] not in olds]
    d = HERE / 'read'
    d.mkdir(parents=True, exist_ok=True)
    cr.record(d, findings=[], coverage=sorted({cr.phash(t) for t in changed}), dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: the %d paragraphs batch l1103 changed (F-320, F-356, F-610), each read '
                      'in place beside his published version by the lead session (E284, E294)' % (after[:8], len(changed)))


if __name__ == '__main__':
    main()
