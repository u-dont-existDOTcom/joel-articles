"""His answers to Neuro De-Armoring Cards, 4 November (2) (ANSWERS-20261104-1352.json, exported 13:52:26 UTC, with his
message of 13:53 UTC, ../joel-20261104-1353-message.txt: "290 has conflicts" and "6a"), into the article.

- Y-83b, revised: his version of Scott's paragraph goes in as he wrote it. His comment: "the only change i needed to flip
  the low conf human all to high conf was to merge the sentences with a ", but" ... again it's the way it flows", with his
  check: https://www.pangram.com/history/6716a87f-8df3-4107-ab4c-5df53a83ef6d (not checked again: he checked it).
- W-17, approved: "in practice" in the 5-HTP and uridine warning.
- 6a: the five generic lines stay; nothing to change.

The fidelity check runs before and after each card, as in apply_cards_x1104.py. The comparative read of W-17's sentence
beside his post's (E284, E294) is mine: "that, in practice, can change" says what his post says, marked as experience. No
finding. His version is his own words, which the comparison gate reads from the answers file.

  python3 articles/neuro-de-armoring/humanize/fix-20261104/cards/apply_cards_x1104c.py [--check]
Writes HUMANIZED-SO-FAR.md, FIDELITY-KEYS.json, APPLIED-CARDS-C.json and read-c/READ-RECORD.json.
"""
import argparse
import copy
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
F = HERE.parent
H = F.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import compare_read as cr  # noqa: E402
import fidelity_keys as fk  # noqa: E402
import suggestion_review as sr  # noqa: E402
from apply_cards_x1104 import delta  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
KEYS = H / 'FIDELITY-KEYS.json'
REVIEW = HERE / 'REVIEW-X1104C.json'
ANSWERS = HERE / 'ANSWERS-20261104-1352.json'
BY = 'fix-20261104/cards/ANSWERS-20261104-1352.json, card %s (%s 2026-11-04)'
HIS_CHECK = 'https://www.pangram.com/history/6716a87f-8df3-4107-ab4c-5df53a83ef6d'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    assert (F / 'joel-20261104-1353-message.txt').read_text(encoding='utf-8').rstrip().endswith('6a')
    md = ARTICLE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    review = json.loads(REVIEW.read_text(encoding='utf-8'))
    answers = json.loads(ANSWERS.read_text(encoding='utf-8'))
    assert answers['review_id'] == review['review_id'] and sha == review['article']['sha256'] == answers['article']['sha256']
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    keys = json.loads(KEYS.read_text(encoding='utf-8'))
    work = copy.deepcopy(keys)
    prev = fk.check(work, md)
    assert prev['pass'], prev
    A = {x['id']: x for x in answers['items']}
    applied = []
    for s in review['suggestions']:
        ans = A[s['id']]
        if s['id'] == 'Y-83b':
            assert ans['status'] == 'revise' and ans['your_version'].strip()
            i = s['spans'][0]['block']
            assert raw[i] == bl[i]['text'] == ans['before']
            raw[i] = ans['your_version'].strip()          # his version, as he wrote it (no typo to fix)
            how = 'his version'
        else:
            assert ans['status'] == 'approved' and ans['my_version'] == s['edits'][0]['after']
            i = s['edits'][0]['block']
            assert raw[i] == bl[i]['text'] == s['edits'][0]['before']
            raw[i] = s['edits'][0]['after']
            how = 'approved'
        now = '\n\n'.join(raw) + '\n'
        r = fk.check(work, now)
        d = delta(prev, r)
        if any(d.values()):
            work.setdefault('owner_changes', []).append(dict({'by': BY % (s['id'], how)}, **{k: v for k, v in d.items() if v}))
            r = fk.check(work, now)
        applied.append({'id': s['id'], 'block': i, 'how': how, 'fidelity_change': {k: v for k, v in d.items() if v}})
        prev = r
    out = '\n\n'.join(raw) + '\n'
    final = fk.check(work, out)
    after = hashlib.sha256(out.encode('utf-8')).hexdigest()
    rec = {'about': 'his answers to Neuro De-Armoring Cards, 4 November (2): Y-83b his version, W-17 approved; 6a, nothing '
                    'to change', 'answers': ANSWERS.name, 'his_check': HIS_CHECK, 'before_sha256': sha, 'after_sha256': after,
           'cards': applied, 'fidelity_pass': final['pass']}
    print(json.dumps(rec, ensure_ascii=False, indent=1))
    assert final['pass'], final
    if a.check:
        return
    ARTICLE.write_text(out, encoding='utf-8')
    KEYS.write_text(json.dumps(work, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'APPLIED-CARDS-C.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    nb = sr.blocks(out)
    (i17,) = [c['block'] for c in applied if c['id'] == 'W-17']
    d = HERE / 'read-c'
    d.mkdir(exist_ok=True)
    cr.record(d, findings=[], coverage=[cr.phash(nb[i17]['text'])], dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: W-17\'s sentence read beside his post\'s by the lead session (E284, E294)'
                      % after[:8])


if __name__ == '__main__':
    main()
