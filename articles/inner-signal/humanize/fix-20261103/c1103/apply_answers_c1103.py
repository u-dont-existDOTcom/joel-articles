"""Put Joel's answer to Hypnosis Guide Cards, 3 November (REVIEW-C1103) into the hypnosis guide, and record the read.

His export of 2026-11-03 12:18 UTC (ANSWERS-20261103-1218.json here, word for word; with his message of 12:18 UTC,
../free-whole-2/joel-20261103-1218-message.txt): E-157, revise, his own version of Don't rush the repair, P2, which
renames the little one "Baby boopaloopa" (his coinage, E330) and joins the "impress me" line to the line before it. One
obvious typo fixed, his rule: the full stop left before "or impress me" ("anything. or impress" becomes "anything or
impress"), since his edit joined the two sentences.

  python3 articles/inner-signal/humanize/fix-20261103/c1103/apply_answers_c1103.py [--check]
Writes HUMANIZED-SO-FAR.md, APPLIED-C1103-ANSWERS.json and read/READ-RECORD.json.
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
REVIEW = HERE / 'REVIEW-C1103.json'
ANSWERS = HERE / 'ANSWERS-20261103-1218.json'
TYPO = ('anything. or impress', 'anything or impress')


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
    assert x['id'] == 'E-157' and x['status'] == 'revise' and x['your_version'].strip()
    i = review['suggestions'][0]['spans'][0]['block']
    assert bl[i]['text'] == x['before']
    v = x['your_version'].strip()
    assert v.count(TYPO[0]) == 1
    v = v.replace(*TYPO)
    lost = []
    raw[i] = set_block_text(raw[i], v, lost)
    assert not lost, lost
    new = '\n\n'.join(raw) + '\n'
    after = hashlib.sha256(new.encode('utf-8')).hexdigest()
    rec = {'answers': ANSWERS.name, 'answers_sha256': hashlib.sha256(ANSWERS.read_bytes()).hexdigest(),
           'before_sha256': sha, 'after_sha256': after, 'block': i, 'where': sr.where(bl, i),
           'fates': {'E-157': 'revise: his version went in ("Baby boopaloopa", his coinage, kept)'},
           'typos_fixed': ['the full stop before "or impress me", left when his edit joined the two sentences'],
           'his_text': x['your_version'], 'in_the_guide': v}
    print(json.dumps(rec, ensure_ascii=False, indent=1))
    if a.check:
        return
    GUIDE.write_text(new, encoding='utf-8')
    (HERE / 'APPLIED-C1103-ANSWERS.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    olds = {b['text'] for b in bl}
    changed = [b['text'] for b in sr.blocks(new) if b['text'] not in olds]
    d = HERE / 'read'
    d.mkdir(parents=True, exist_ok=True)
    cr.record(d, findings=[], coverage=sorted({cr.phash(t) for t in changed}), dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: the paragraph his answer to the cards of 3 November changed (E-157, his '
                      'own version), read by the lead session in place (E284, E294)' % after[:8])


if __name__ == '__main__':
    main()
