#!/usr/bin/env python3
"""apply_r11.py - round 11's answer (Joel, exported 2026-11-06 20:51 UTC; ANSWERS-R11-20261106-2051.json) put into the
guide: PFA-PLAIN (the Psychological First Aid section's AI lines said plainly, eight paragraphs) and PFA-MOVE (the practice
paragraph next to its script), both approved with no comment.

The card worked on the page's plain text; the guide keeps its Markdown: B234 keeps its triage-app link, and B243 its
italic placeholders. Starts from the guide after his cuts of 19:43 (../../GUIDE-SO-FAR-blocks.json, whose page form is
PAGE-R11.md, the SHA-256 his export names) and writes the guide after round 11 into ../../GUIDE-SO-FAR.md and its blocks.

  python3 apply_r11.py      write the guide after round 11 and print what changed
"""
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parent.parent
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
BLOCKS = json.loads(BJ.read_text(encoding='utf-8'))
REVIEW = json.loads((HERE / 'REVIEW-R11.json').read_text(encoding='utf-8'))
ANSWERS = json.loads((HERE / 'ANSWERS-R11-20261106-2051.json').read_text(encoding='utf-8'))

assert ANSWERS['review_id'] == REVIEW['review_id'] == 'bad-trips-r11'
assert hashlib.sha256((HERE / 'PAGE-R11.md').read_bytes()).hexdigest() == ANSWERS['article']['sha256']
ITEM = {x['id']: x for x in ANSWERS['items']}
assert set(ITEM) == {s['id'] for s in REVIEW['suggestions']} == {'PFA-PLAIN', 'PFA-MOVE'}
assert all(ITEM[k]['status'] == 'approved' and not ITEM[k]['your_version'] for k in ITEM), 'not both approved as they were'
before_md = MD.read_text(encoding='utf-8')
assert '\n\n'.join(b['md'] for b in BLOCKS) + '\n' == before_md, 'the blocks and the guide disagree'
UNIT = {b['id']: b for b in BLOCKS}

NEW = {
    'B234': "The [triage app](https://ibogaqueen.com/1625-2/) gives you the order to do things in, and this section is about "
            "doing them in a way that takes pressure off the person.",
    'B238': UNIT['B238']['md'].replace(
        "Somebody might be touching them when they don't want it, or they're stuck beside someone they don't trust.",
        "Somebody might be touching them and they hate it, or they're stuck beside someone they're wary of."),
    'B242': "Then remind them where they are and what's happening, since a trip can make them lose track of it:",
    'B243': "> You're in *[place]*. It's *[date/time]*. You took *[substance, if known]*, and its effects will peak and then "
            "change. It's intense right now, and it'll pass. We can sort out the rest of your life tomorrow.",
    'B244': "If the state came from a practice, like meditation or fasting, the person can say:",
    'B245': "> I'm in an intense state, so I'm stopping the practice now, and my only job is to stay safe.",
    'B246': "Then help them pick one safe thing to try with their body and one calm person to stay with them, which the next "
            "two sections are about. Protect their sleep too, especially if they're euphoric or grandiose, and leave what it "
            "all meant until they've slept.",
    'B247': "A state from a practice has no drug wearing off on a schedule, so there's no telling how long it will last. Once "
            "they can eat safely, food and warmth help their body settle.",
}
assert NEW['B238'] != UNIT['B238']['md']


def plain(md):
    t = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'\1', md)
    t = re.sub(r'^>\s?', '', t, flags=re.M)
    return t.replace('*', '').strip()


# the card's text is the page's plain text: each new paragraph, made plain, must be what he approved
mine = ITEM['PFA-PLAIN']['my_version'].split('\n\n')
assert [plain(NEW[b]) for b in ('B234', 'B238', 'B242', 'B243', 'B244', 'B245', 'B246', 'B247')] == mine, 'not his approved text'
for b, md in NEW.items():
    UNIT[b]['md'] = md
# PFA-MOVE: B247 goes just before B246
ids = [b['id'] for b in BLOCKS]
i246, i247 = ids.index('B246'), ids.index('B247')
assert i247 == i246 + 1
BLOCKS[i246], BLOCKS[i247] = BLOCKS[i247], BLOCKS[i246]

text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(text, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before_md)), len(re.findall(r'\S+', text))
print('PFA-PLAIN: B234, B238, B242, B243, B244, B245, B246, B247 said plainly')
print('PFA-MOVE: B247 now before B246')
print('2 cards applied; %d words -> %d (%+d); GUIDE-SO-FAR.md sha256 %s' % (w0, w1, w1 - w0, hashlib.sha256(text.encode()).hexdigest()))
