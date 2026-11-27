"""his_checks_r61.py - his two Pangram checks on round 61's TEACH-B155, as read from the pages his links open (2026-11-27,
the built-in browser, his account's history API: the text checked, the headline, each window). From the repo root:

  python3 articles/bad-trips/review/r61/his_checks_r61.py

The texts are rebuilt here from his answers file (his version, as he sent it) and the guide's B158 as it stood when he
checked, and each is matched to the page's text by SHA-256, so no paragraph is retyped.
"""
import hashlib
import json
import pathlib

ART = pathlib.Path(__file__).resolve().parents[2]
HERE = ART / 'review' / 'r61'
ANS = HERE / 'ANSWERS-R61-20261127-1534.json'

his = {x['id']: x for x in json.loads(ANS.read_text(encoding='utf-8'))['items']}['TEACH-B155']['your_version']
blocks = {x['id']: x for x in json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))}
b158 = blocks['B158']['md']
# B158 as it stood when he checked (turn 71's text; FROM-POST changes its last sentence after this)
b158_then = (ART / 'humanize' / 'h79-20261126' / 'TEST-a2-b158.txt').read_text(encoding='utf-8').strip()

CHECKS = [
    {'id': '00eb45f1-8b99-4337-929b-b4489859cf23', 'what': 'his version of B155 by itself',
     'text': his, 'sha256': '0e73132b4f62c1310467ecbb1816440186eab7ef924d86abd5e07a34eaba2c0a',
     'utc': '2026-11-27T15:31:52Z', 'version': '4.1', 'headline': 'Human Written', 'ai': 3.6e-26,
     'windows': [['Human', 'High', 65]]},
    {'id': '54b91410-ee03-4ebe-969b-03777505918f', 'what': 'B158 as the guide had it (turn 71), then his version of B155',
     'text': b158_then + '\n\n' + his, 'sha256': 'be71360674d78aebfc2c15c07245f3f7304a12fe837011ee1198afda9a2123d7',
     'utc': '2026-11-27T15:32:48Z', 'version': '4.1', 'headline': 'Human Written', 'ai': 5.6e-29,
     'windows': [['Human', 'High', 133]]},
]

out = []
for c in CHECKS:
    got = hashlib.sha256(c['text'].encode('utf-8')).hexdigest()
    assert got == c['sha256'], (c['id'], got)
    out.append({k: v for k, v in c.items() if k != 'text'} | {'words_local': len(c['text'].split()),
                'link': 'https://www.pangram.com/history/' + c['id']})
(HERE / 'HIS-CHECKS-R61.json').write_text(json.dumps({'about': __doc__.strip().splitlines()[0], 'checks': out},
                                                      ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('both texts match his pages by SHA-256; B158 in the guide unchanged since:', b158 == b158_then)
