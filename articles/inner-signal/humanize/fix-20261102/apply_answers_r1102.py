"""Put Joel's answers to Hypnosis Guide Cards, 2 November (REVIEW-R1102) into the hypnosis guide, and record the read.

His export of 2026-11-02 18:15 UTC (ANSWERS-20261102-1816.json here, word for word), sent with his message of 18:16 UTC
(joel-20261102-1816-message.txt): all three approved, no comments. Each card goes in as it showed it (its edits' "after";
an empty "after" takes the paragraph out): W-92b his inner child guide's party example after the rent line, W-283b the
script cut (his paragraph above it ends at "the body's flow."), R-638 Appendix E's repeated prayer cut.

The lead session read the changed paragraphs in place beside his inner child guide and his published version: W-92b is
his inner child guide's paragraph word for word after the guide's own first two sentences; the two cuts leave his words
as they were, and nothing else in their paragraphs changed.

  python3 articles/inner-signal/humanize/fix-20261102/apply_answers_r1102.py [--check]
Writes HUMANIZED-SO-FAR.md, APPLIED-R1102.json and answers-r1102/read/READ-RECORD.json.
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text  # noqa: E402

GUIDE = H / 'HUMANIZED-SO-FAR.md'
REVIEW = HERE / 'review' / 'REVIEW-R1102.json'
ANSWERS = HERE / 'ANSWERS-20261102-1816.json'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    review = json.loads(REVIEW.read_text(encoding='utf-8'))
    answers = json.loads(ANSWERS.read_text(encoding='utf-8'))
    md = GUIDE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert sha == review['article']['sha256'] == answers['article']['sha256'], 'the guide changed since the cards page'
    assert answers['review_id'] == review['review_id']
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl)
    A = {x['id']: x for x in answers['items']}
    assert set(A) == {s['id'] for s in review['suggestions']}
    new_raw, fates, lost = {}, {}, []
    for s in review['suggestions']:
        x = A[s['id']]
        assert x['status'] == 'approved' and not x['comment'], s['id']
        for e in s['edits']:
            i = e['block']
            assert e['before'] == bl[i]['text'] and i not in new_raw, (s['id'], i)
            new_raw[i] = [set_block_text(raw[i], e['after'], lost)] if e['after'] else []
        fates[s['id']] = 'approved: the card\'s version went in'
    assert not lost, lost
    out = []
    for i, r in enumerate(raw):
        out += new_raw.get(i, [r])
    new = '\n\n'.join(out) + '\n'
    after = hashlib.sha256(new.encode('utf-8')).hexdigest()
    changed_text = [e['after'] for s in review['suggestions'] for e in s['edits'] if e['after']]
    rec = {'answers': ANSWERS.name, 'answers_sha256': hashlib.sha256(ANSWERS.read_bytes()).hexdigest(),
           'before_sha256': sha, 'after_sha256': after, 'fates': fates, 'changed_blocks': sorted(new_raw),
           'blocks': [len(bl), len(out)]}
    print(json.dumps(rec, indent=1))
    if a.check:
        return
    GUIDE.write_text(new, encoding='utf-8')
    (HERE / 'APPLIED-R1102.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    now = {b['text'] for b in sr.blocks(new)}
    assert all(t in now for t in changed_text)
    d = HERE / 'answers-r1102' / 'read'
    d.mkdir(parents=True, exist_ok=True)
    cr.record(d, findings=[], coverage=sorted({cr.phash(t) for t in changed_text}), dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: the %d paragraphs his three approved cards of 2 November changed '
                      '(W-92b, W-283b, R-638), read by the lead session in place beside his inner child guide and his '
                      'published version (E284, E294)' % (after[:8], len(changed_text)))


if __name__ == '__main__':
    main()
