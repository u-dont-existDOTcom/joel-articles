#!/usr/bin/env python3
"""apply_r08.py - round 8's answer (Joel, exported 2026-11-06 00:27 UTC; ANSWERS-R08-20261106-0027.json) put into the
guide: his version of card ROOM-YOURS, the four room paragraphs of Psychological First Aid (B238 to B241).

Starts from the guide after round 7 (../../GUIDE-SO-FAR-blocks.json as main has it after pull request 307, whose page
form is PAGE-R08.md, the SHA-256 his export names) and writes the guide after round 8 (GUIDE-AFTER-R08.md and
GUIDE-AFTER-R08-blocks.json beside this script), which becomes ../../GUIDE-SO-FAR.md.

His version keeps his first two paragraphs as they were (the room's questions, B238, and the annoying room, B239) and
rewrites the last two: the fixes (B240) and the music (B241), the text of his check that read Human
(https://www.pangram.com/history/26e9138d-9b91-44e0-bb5c-7a21a7e4dddc). Word for word, with one double space made single
and the trailing spaces dropped. The first part he left to me ("an exercise for you to fix now"): that fix goes on
round 9's page as a card, and stays out of the guide until he answers it.

  python3 apply_r08.py            write the guide after round 8 and print what changed
"""
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parent.parent
BLOCKS = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
REVIEW = json.loads((HERE / 'REVIEW-R08.json').read_text(encoding='utf-8'))
ANSWERS = json.loads((HERE / 'ANSWERS-R08-20261106-0027.json').read_text(encoding='utf-8'))
OUT = HERE / 'GUIDE-AFTER-R08.md'
OUT_BLOCKS = HERE / 'GUIDE-AFTER-R08-blocks.json'

assert ANSWERS['review_id'] == REVIEW['review_id'] == 'bad-trips-r08', (ANSWERS['review_id'], REVIEW['review_id'])
assert hashlib.sha256((HERE / 'PAGE-R08.md').read_bytes()).hexdigest() == ANSWERS['article']['sha256']
ITEM = {x['id']: x for x in ANSWERS['items']}
assert set(ITEM) == {s['id'] for s in REVIEW['suggestions']} == {'ROOM-YOURS'}
card = ITEM['ROOM-YOURS']
assert card['status'] == 'revise' and card['advice'] == 'edit', (card['status'], card['advice'])

UNIT = {b['id']: b for b in BLOCKS}
IDS = ['B238', 'B239', 'B240', 'B241']


def plain(md):
    return re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'\1', md).strip()


assert '\n\n'.join(plain(UNIT[i]['md']) for i in IDS) == card['before'].strip()
his = [re.sub(r' {2,}', ' ', p).strip() for p in card['your_version'].split('\n\n')]
assert len(his) == 4, len(his)
assert his[0] == plain(UNIT['B238']['md']) and his[1] == plain(UNIT['B239']['md']), 'his first two paragraphs changed'
assert all('](' not in UNIT[i]['md'] for i in ('B240', 'B241')), 'a link in a paragraph he rewrote'
CHECKED = ("They're feeling overwhelmed, so dim the lights, and clear out the extra people around them.  If they're thirsty, "
           "offer water, and suggest they sip it rather than chug. Ask if they'd like a hand on the shoulder. Speak slowly "
           "and use fewer words. \n\nAsk \"Would you like music or is quiet best?\" If a track starts pulling the experience "
           "somewhere unwanted, go ahead and change it.")
assert hashlib.sha256(CHECKED.encode()).hexdigest() == 'b13ed91b71a2dbe4a454dc4eb4a00f9f7d22fccc1369e93f3996c16922ed5fe5'
assert [re.sub(r' {2,}', ' ', p).strip() for p in CHECKED.split('\n\n')] == his[2:], 'his version is not his Human check'
UNIT['B240']['md'], UNIT['B241']['md'] = his[2], his[3]

text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
OUT.write_text(text, encoding='utf-8')
OUT_BLOCKS.write_text(json.dumps([{'id': b['id'], 'kind': b['kind'], 'md': b['md'], 'text': None} for b in BLOCKS],
                                 ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
before = (ART / 'GUIDE-SO-FAR.md').read_text(encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before)), len(re.findall(r'\S+', text))
print('B240, B241: ROOM-YOURS, his version (his check 26e9138d, Human); B238, B239 unchanged')
print('1 card applied; %d words -> %d (%+d); %s sha256 %s' % (w0, w1, w1 - w0, OUT.name,
                                                              hashlib.sha256(text.encode()).hexdigest()))
