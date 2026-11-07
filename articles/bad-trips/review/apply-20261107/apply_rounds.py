#!/usr/bin/env python3
"""apply_rounds.py - his answers to rounds 12 and 15 to 21 put into the guide (2026-11-07 12:08 UTC: "in this case i
approved every single suggestion you had from all those rounds"). Every card was approved with no comment and no
version of his own: round 19 from his export (../r19/ANSWERS-R19-20261107-1206.json), the others from each page's saved
decisions (../rNN/ANSWERS-RNN-20261107-db.json).

The cards worked on the pages' plain text; the guide keeps its Markdown (bold, italics, links). Each edit is checked
against the guide's current Markdown, and each changed block's plain text against the card's "after".

  python3 apply_rounds.py      write the guide (../../GUIDE-SO-FAR.md and its blocks) and print what changed
"""
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
REVIEW = HERE.parent
ART = REVIEW.parent
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
BLOCKS = json.loads(BJ.read_text(encoding='utf-8'))
before_md = MD.read_text(encoding='utf-8')
assert '\n\n'.join(b['md'] for b in BLOCKS) + '\n' == before_md, 'the blocks and the guide disagree'
UNIT = {b['id']: b for b in BLOCKS}


def answers(r):
    if r == 'r19':
        a = json.loads((REVIEW / 'r19/ANSWERS-R19-20261107-1206.json').read_text(encoding='utf-8'))
    else:
        a = json.loads((REVIEW / ('%s/ANSWERS-%s-20261107-db.json' % (r, r.upper()))).read_text(encoding='utf-8'))
    rev = json.loads((REVIEW / ('%s/REVIEW-%s.json' % (r, r.upper()))).read_text(encoding='utf-8'))
    assert a['review_id'] == rev['review_id'] == 'bad-trips-%s' % r
    items = {x['id']: x for x in a['items']}
    assert set(items) == {s['id'] for s in rev['suggestions']}, r
    for x in items.values():
        assert x['status'] == 'approved' and not x.get('your_version') and not x.get('comment'), (r, x['id'])
    return sorted(items)


def replace(bid, old, new):
    md = UNIT[bid]['md']
    assert md.count(old) == 1, (bid, old, md)
    UNIT[bid]['md'] = md.replace(old, new)


CUT = []
EDITS = {
    'r12': {'PFA-PRACTICE': lambda: (
        replace('B244', 'If the state came from a practice, like meditation or fasting, the person can say:',
                "If a practice like meditation or fasting brought this on, have them stop it now, since doing more of it only "
                "makes this stronger. There's no drug wearing off here, so it could be over soon or take a while."),
        CUT.extend(['B245', 'B247']))},
    'r15': {'CONTACT-TRIPSIT': lambda: replace('B264', 'browser-based harm-reduction chat for people using drugs and the people supporting them.',
                                               "a harm-reduction chat you open in your browser, for people using drugs and for whoever's looking after them."),
            'HELPER-PHRASE': lambda: replace('B83', 'A useful phrase is:', 'If it helps, you can say to yourself:'),
            'HELPER-GRIEF-CUT': lambda: CUT.append('B84')},
    'r16': {'NRA-LOCK': lambda: replace('B317', 'Use a 24–72 hour action lock.', 'Put yourself on a 24–72 hour action lock.'),
            'NRA-WRITE': lambda: replace('B319', 'Write it down. Protect sleep. Revisit it sober with one grounded person.',
                                         'Write it down, get some sleep, and go back over it sober with one grounded person.')},
    'r17': {'OTHER-PAIR': lambda: replace('B344', "Most negative mind-states aren't philosophical errors. They are young parts still waiting for love, protection, permission, and an explanation nobody gave them.",
                                          "Most negative mind-states aren't some error in your philosophy, they're just young parts of you that are still waiting for love and protection and permission, and for the explanation nobody ever gave them.")},
    'r18': {'WHY-LESSON': lambda: replace('B361', 'Sometimes the lesson is to lower the dose, stop the practice, sleep, eat, choose safer people, and admit that the room is bad.',
                                          'Sometimes the lesson is just to lower the dose or stop the practice, get some sleep and something to eat, pick safer people, and admit that the room is bad.'),
            'SESSION-FORCE-ONCE': lambda: (
                replace('B368', ' They do not force music, touch, interpretation, confession, prayer, or insight.', ''),
                replace('B284', 'interpretation, or insight.', 'interpretation, confession, or insight.'))},
    'r19': {'SORROW-MISSING': lambda: replace('B380', 'Missing is contraction: hunger, ache, self-reference, and the painful fantasy that love means needing the person to return.',
                                              "Missing someone is a contraction. There's hunger and ache in it, it keeps circling back to you, and there's the painful fantasy that loving them means needing them to come back."),
            'HAND-SIGNAL': lambda: replace('B386', 'The point is not to manufacture loving thoughts. Give the body one simple signal: love is here.',
                                           "There's no need to manufacture loving thoughts, you're just giving the body one simple signal: love is here."),
            'DEMON-TRAIN': lambda: replace('B400', 'Train before the emergency: send love to a frightening image, a hated person without approving what they did, your shame, your body, sickness, aging, fear, death, and the inner child.',
                                           'So train before you need it, sending love to a frightening image, to someone you hate (without approving of what they did), to your shame and your body, to sickness and aging and fear and death, and to the inner child.'),
            'DEMON-SAFETY-ONCE': lambda: CUT.extend(['B402', 'B403'])},
    'r20': {'ABUSE-TRUE': lambda: replace('B409', 'It may be psychologically true, symbolically true, literally true, partly true, or false in the form it first appeared.',
                                          'It could be true psychologically, or symbolically, or literally, or only partly true, or false in the form it first took.')},
    'r21': {'AMZ-DANGER-ONCE': lambda: (
        CUT.append('B325'),
        replace('B318', 'give away possessions, call your ex', 'give away possessions, make a grand purchase, call your ex'))},
}


def plain(md):
    md = re.sub(r'^\s*(?:-|\d+\.)\s+', '', md, flags=re.M)
    md = re.sub(r'^>\s?', '', md, flags=re.M)
    md = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', md)
    return re.sub(r'\s+', ' ', md.replace('*', '')).strip()


done = []
for r, cards in EDITS.items():
    assert answers(r) == sorted(cards), (r, answers(r))
    for cid in sorted(cards):
        cards[cid]()
        done.append('%s %s' % (r, cid))
# each changed block against the cards' plain "after" (list blocks: the item the card changed)
AFTER = {}
for r in EDITS:
    rev = json.loads((REVIEW / ('%s/REVIEW-%s.json' % (r, r.upper()))).read_text(encoding='utf-8'))
    for s in rev['suggestions']:
        for e in s.get('edits', []):
            if e.get('after'):
                AFTER.setdefault(r, []).append(re.sub(r'\s+', ' ', e['after']).strip())
for r, afters in AFTER.items():
    text = plain('\n'.join(b['md'] for b in BLOCKS if b['id'] not in CUT))
    for a in afters:
        assert a in text, (r, a)
BLOCKS[:] = [b for b in BLOCKS if b['id'] not in CUT]
text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(text, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before_md)), len(re.findall(r'\S+', text))
print('in: ' + ', '.join(done))
print('cut blocks: ' + ', '.join(CUT))
print('%d words -> %d (%+d); GUIDE-SO-FAR.md sha256 %s' % (w0, w1, w1 - w0, hashlib.sha256(text.encode()).hexdigest()))
