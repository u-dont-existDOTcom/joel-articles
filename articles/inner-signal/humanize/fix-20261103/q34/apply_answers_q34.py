"""Joel's answers to question 34 (2026-11-03 14:52 UTC, `joel-20261103-1452-message.txt`), into the guide.

Question 34 was five spots in his own words that the word-by-word read questioned (../nonsense/FINDINGS.md). His answers:
- 34.1 "ok i've heard many people say playing asleep, you can play anything...": kept.
- 34.2 "that's a real clarity problem. change it to: "That hand movement grounds and aligns the distractible mind."":
  his sentence, as he wrote it, in place of "That hand movement is the mental escape into the body's flow."
- 34.3 "agree": the change the question showed, "especially when the questions led to them (which NLP tends to do)".
- 34.4 "agree keep": kept.
- 34.5 "i meant coordination": "repeated correction between" -> "repeated coordination between".

  python3 articles/inner-signal/humanize/fix-20261103/q34/apply_answers_q34.py [--check]
Writes HUMANIZED-SO-FAR.md, APPLIED-Q34.json and read/READ-RECORD.json.
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
BEFORE = '010b9fc3c6e6bb1273736c47b00c89a7f50f0de20b5a0e161ced5b33cb65c5d1'
KEPT = {
    '34.1': ('surrendering to the hypnotist while playing asleep',
             "ok i've heard many people say playing asleep, you can play anything..."),
    '34.4': ('before taking off the kid gloves, so to speak', 'agree keep'),
}
EDITS = [
    ('34.2', "That hand movement is the mental escape into the body's flow.",
     'That hand movement grounds and aligns the distractible mind.',
     'that\'s a real clarity problem. change it to: "That hand movement grounds and aligns the distractible mind."'),
    ('34.3', 'especially when they were led to (which NLP tends to)',
     'especially when the questions led to them (which NLP tends to do)', 'agree'),
    ('34.5', 'repeated correction between intuition, subconscious response, and conscious analysis',
     'repeated coordination between intuition, subconscious response, and conscious analysis', 'i meant coordination'),
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
    for q, (probe, words) in KEPT.items():
        hits = [b['i'] for b in bl if probe in b['text']]
        assert len(hits) == 1, (q, hits)
        fates[q] = {'block': hits[0], 'where': sr.where(bl, hits[0]), 'kept': probe, 'his answer': words}
    for q, old, new, words in EDITS:
        hits = [b['i'] for b in bl if old in b['text']]
        assert len(hits) == 1, (q, hits)
        i = hits[0]
        t = bl[i]['text']
        assert t.count(old) == 1
        raw[i] = set_block_text(raw[i], t.replace(old, new), lost)
        fates[q] = {'block': i, 'where': sr.where(bl, i), 'before': old, 'after': new, 'his answer': words}
    assert not lost, lost
    new_md = '\n\n'.join(raw) + '\n'
    after = hashlib.sha256(new_md.encode('utf-8')).hexdigest()
    assert len(sr.blocks(new_md)) == len(bl)
    rec = {'before_sha256': sha, 'after_sha256': after, 'answers': fates}
    print(json.dumps(rec, ensure_ascii=False, indent=1))
    if a.check:
        return
    GUIDE.write_text(new_md, encoding='utf-8')
    (HERE / 'APPLIED-Q34.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    olds = {b['text'] for b in bl}
    changed = [b['text'] for b in sr.blocks(new_md) if b['text'] not in olds]
    d = HERE / 'read'
    d.mkdir(parents=True, exist_ok=True)
    cr.record(d, findings=[], coverage=sorted({cr.phash(t) for t in changed}), dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: the %d paragraphs his answers to question 34 changed, each read in '
                      'place by the lead session (E284, E294, E331)' % (after[:8], len(changed)))


if __name__ == '__main__':
    main()
