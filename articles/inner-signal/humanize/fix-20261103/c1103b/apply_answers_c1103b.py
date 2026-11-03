"""Put Joel's answers of 2026-11-03 13:46 UTC into the hypnosis guide, and record the read.

His message (joel-20261103-1346-message.txt here, word for word): "33a" (the guide goes into his post now: done after this
and the nonsense read, ../../fix-20261103/live/) and his answers to Hypnosis Guide Cards, 3 November (2)
(ANSWERS-20261103-1346.json):
- E-523, revise, his own version of Pattern 10's two paragraphs: the first as it was; the second with his new-age example
  ("everyone is your mirror") and his own three questions. One obvious typo fixed, his rule: the second question mark in
  "or...? ? How" (left where he took questions out).
- His comment: "i also noticed the tag questions part above says "oily" instead of old. do we have more nonsense in here
  (from emulate i guess)? how are you not catching this?" Pattern 8's "they get oily very quickly" becomes "they get old
  very quickly", his word. ("oily" was in his published guide of 28 September: "They become oily very quickly, don't
  they?"; lesson E331.)

  python3 articles/inner-signal/humanize/fix-20261103/c1103b/apply_answers_c1103b.py [--check]
Writes HUMANIZED-SO-FAR.md, APPLIED-C1103B-ANSWERS.json and read/READ-RECORD.json.
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
REVIEW = HERE / 'REVIEW-C1103B.json'
ANSWERS = HERE / 'ANSWERS-20261103-1346.json'
TYPO = ('or...? ? How', 'or...? How')
OILY = ('but they get oily very quickly', 'but they get old very quickly')


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
    (x,) = answers['items']
    assert x['id'] == 'E-523' and x['status'] == 'revise'
    spans = [sp['block'] for sp in review['suggestions'][0]['spans']]
    assert x['before'] == '\n\n'.join(bl[i]['text'] for i in spans)
    v = [p.strip() for p in re.split(r'\n\s*\n', x['your_version'].strip())]
    assert len(v) == len(spans) == 2 and v[0] == bl[spans[0]]['text']
    assert v[1].count(TYPO[0]) == 1
    v[1] = v[1].replace(*TYPO)
    lost = []
    raw[spans[1]] = set_block_text(raw[spans[1]], v[1], lost)
    hits = [b['i'] for b in bl if OILY[0] in b['text']]
    assert len(hits) == 1, hits
    j = hits[0]
    raw[j] = set_block_text(raw[j], bl[j]['text'].replace(*OILY), lost)
    assert not lost, lost
    new = '\n\n'.join(raw) + '\n'
    after = hashlib.sha256(new.encode('utf-8')).hexdigest()
    rec = {'answers': ANSWERS.name, 'answers_sha256': hashlib.sha256(ANSWERS.read_bytes()).hexdigest(),
           'before_sha256': sha, 'after_sha256': after, 'blocks': {'E-523': spans[1], 'oily': j},
           'fates': {'E-523': 'revise: his version of the second paragraph went in (the first is unchanged in it)',
                     '33a': 'the guide goes into his post after this and the nonsense read (fix-20261103/live/)',
                     'oily': 'his comment: Pattern 8\'s "they get oily very quickly" now "they get old very quickly"'},
           'typos_fixed': ['the second question mark in "or...? ? How"'], 'in_the_guide': v[1]}
    print(json.dumps(rec, ensure_ascii=False, indent=1))
    if a.check:
        return
    GUIDE.write_text(new, encoding='utf-8')
    (HERE / 'APPLIED-C1103B-ANSWERS.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    olds = {b['text'] for b in bl}
    changed = [b['text'] for b in sr.blocks(new) if b['text'] not in olds]
    d = HERE / 'read'
    d.mkdir(parents=True, exist_ok=True)
    cr.record(d, findings=[], coverage=sorted({cr.phash(t) for t in changed}), dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: the paragraphs his answers of 13:46 UTC changed (E-523, his version; '
                      'Pattern 8\'s "oily", his word), read by the lead session in place (E284, E294)' % after[:8])


if __name__ == '__main__':
    main()
