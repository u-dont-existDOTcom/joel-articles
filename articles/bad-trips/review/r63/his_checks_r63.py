"""his_checks_r63.py - his Pangram check on round 63's TEACH-B173, as read from the page his link opens (2026-11-27, the
built-in browser, his account's history API: the text checked, the headline, each window). From the repo root:

  python3 articles/bad-trips/review/r63/his_checks_r63.py

The text is his version from his answers file, matched to the page's text by SHA-256, so no paragraph is retyped.
"""
import hashlib
import json
import pathlib

ART = pathlib.Path(__file__).resolve().parents[2]
HERE = ART / 'review' / 'r63'
ANS = HERE / 'ANSWERS-R63-20261127-2003.json'

his = {x['id']: x for x in json.loads(ANS.read_text(encoding='utf-8'))['items']}['TEACH-B173']['your_version']

CHECKS = [
    {'id': '09e42ca2-b7ef-4439-92f3-402dd6f78314', 'what': 'his version of B173 by itself',
     'text': his, 'sha256': '0e8961b382917976a54560153acbdb5f4c88b47e7683eb53d135d46452d86762',
     'utc': '2026-11-27T19:58:48Z', 'version': '4.1', 'headline': 'Human Written', 'ai': 2.1e-35,
     'windows': [['Human', 'High', 84]]},
]

out = []
for c in CHECKS:
    got = hashlib.sha256(c['text'].encode('utf-8')).hexdigest()
    assert got == c['sha256'], (c['id'], got)
    out.append({k: v for k, v in c.items() if k != 'text'} | {'words_local': len(c['text'].split()),
                'link': 'https://www.pangram.com/history/' + c['id']})
(HERE / 'HIS-CHECKS-R63.json').write_text(json.dumps({'about': __doc__.strip().splitlines()[0], 'checks': out},
                                                      ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('his text matches his page by SHA-256')
