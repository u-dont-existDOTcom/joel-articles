"""His answer to question 3 ("3a", 2026-11-04 10:39 UTC, ../joel-20261104-1039-message.txt), into the article.

Question 3 asked whether the two drug names his "Who this is for" leaves out go back: a) "Put them back in brackets:
'People with DAWS, after tapering off dopamine agonist drugs (like pramipexole or ropinirole), present with ...'". That
version, checked by itself before he was asked, reads Human Written, 0.0% AI (High):
https://www.pangram.com/history/0faeb569-0041-45d3-9986-b77b3f490b83. The two "owner_open" entries in FIDELITY-KEYS.json
go, since nothing is left out any more.

  python3 articles/neuro-de-armoring/humanize/fix-20261104/q3/apply_q3.py [--check]
Writes HUMANIZED-SO-FAR.md, FIDELITY-KEYS.json, APPLIED-Q3.json and read/READ-RECORD.json.
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
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
KEYS = H / 'FIDELITY-KEYS.json'
BEFORE = '72e9e3165af5'
OLD = 'after tapering off dopamine agonist drugs, present with'
NEW = 'after tapering off dopamine agonist drugs (like pramipexole or ropinirole), present with'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    assert (HERE.parent / 'joel-20261104-1039-message.txt').read_text(encoding='utf-8').rstrip().endswith('3a 4a')
    md = ARTICLE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert sha.startswith(BEFORE), 'the article changed'
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    (i,) = [b['i'] for b in bl if b['text'].startswith("Who this is for: Uridine isn't for everyone with depression.")]
    assert raw[i].count(OLD) == 1
    raw[i] = raw[i].replace(OLD, NEW)
    out = '\n\n'.join(raw) + '\n'
    after = hashlib.sha256(out.encode('utf-8')).hexdigest()
    keys = json.loads(KEYS.read_text(encoding='utf-8'))
    left = [o for o in keys.get('owner_open', []) if o.get('term') not in ('pramipexole', 'ropinirole')]
    rec = {'about': 'his answer 3a: the two drug names back in brackets in his "Who this is for"', 'his_answer': '3a',
           'before_sha256': sha, 'after_sha256': after, 'block': i, 'where': sr.where(bl, i), 'before': OLD, 'after': NEW,
           'tested': 'https://www.pangram.com/history/0faeb569-0041-45d3-9986-b77b3f490b83',
           'owner_open_removed': ['pramipexole', 'ropinirole']}
    print(json.dumps(rec, ensure_ascii=False, indent=1))
    if a.check:
        return
    ARTICLE.write_text(out, encoding='utf-8')
    if left:
        keys['owner_open'] = left
    else:
        keys.pop('owner_open', None)
    KEYS.write_text(json.dumps(keys, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'APPLIED-Q3.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    d = HERE / 'read'
    d.mkdir(parents=True, exist_ok=True)
    cr.record(d, findings=[], coverage=[cr.phash(sr.blocks(out)[i]['text'])], dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: his "Who this is for" with the two names back (his answer 3a), read in place '
                      'by the lead session (E284, E331)' % after[:8])


if __name__ == '__main__':
    main()
