#!/usr/bin/env python3
"""Turn 125: Joel's answers on the sense-read marking page (his export of 2026-11-04 16:11 UTC,
experiments/t125-answers/ANSWERS-20261104-1611.json, made on experiments/t124-sense/GUIDE-PAGE.md, whose SHA-256 it names)
put into HUMANIZED-ARTICLE-SO-FAR.md:
  - the 15 cards he approved, each as its card had it (experiments/t124-sense/CARDS.json; the card's text and his export's
    "my_version" checked to agree);
  - SR-516, his own version ("in very powerful meditations and altered states."), word for word;
  - SR-11 and SR-69, which he rejected, and SR-373, which he answered, stay as they are, and go on KEEP-AS-IS.json with his
    words, so no later pass flags them again (lesson E340);
  - SR-212b and SR-384, the two I advised leaving, he left undecided: they stay as they are.
Writes the article, OWNER-EDITS.json (one joel-125-* entry a card) and KEEP-AS-IS.json, and APPLIED.json, the record of
each card's fate. Run once; it refuses an article it has already changed.
  python3 articles/inner-child-therapy/experiments/t125-apply/apply_t125.py"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART_DIR = HERE.parents[1]
ART = ART_DIR / 'HUMANIZED-ARTICLE-SO-FAR.md'
LEDGER = ART_DIR / 'OWNER-EDITS.json'
KEEP = ART_DIR / 'KEEP-AS-IS.json'
SENSE = HERE.parent / 't124-sense'
ANS = json.loads((HERE.parent / 't125-answers' / 'ANSWERS-20261104-1611.json').read_text(encoding='utf-8'))
WHEN = '2026-11-04 16:11 UTC (experiments/t125-answers/ANSWERS-20261104-1611.json)'
assert ANS['review_id'] == 'inner-child-t124-sense-read'
assert ANS['article']['sha256'] == hashlib.sha256((SENSE / 'GUIDE-PAGE.md').read_bytes()).hexdigest(), 'answers made on another page copy'
ITEMS = {it['id']: it for it in ANS['items']}
CARDS = {c['cid']: c for c in json.loads((SENSE / 'CARDS.json').read_text(encoding='utf-8'))}

md = ART.read_text(encoding='utf-8')
if 'in very powerful meditations and altered states.' in md:
    sys.exit('already applied')
changes, applied = [], {}
for cid, it in ITEMS.items():
    c = CARDS[cid]
    if it['status'] == 'approved':
        assert c['kind'] == 'fix', cid
        pairs = [(c['old'], c['new'])] + [tuple(x) for x in c.get('extra', [])]
        assert len(pairs) == 1, cid   # SR-11, the one card with two places, he rejected
        old, new = pairs[0]
        assert it['before'].replace('**', '').count(old) == 1 and it['my_version'] == it['before'].replace(old, new), cid
        changes.append((cid, old, new, ''))
        applied[cid] = {'fate': 'approved', 'old': old, 'new': new}
    elif it['status'] == 'revise':
        assert cid == 'SR-516'
        old, new = 'in very powerful meditations.', 'in very powerful meditations and altered states.'
        assert it['your_version'] == it['before'].replace(old, new), 'his version changes more than the card\'s words'
        changes.append((cid, old, new, 'his own version'))
        applied[cid] = {'fate': 'his version', 'old': old, 'new': new, 'his_version': it['your_version']}
    elif it['status'] == 'rejected':
        applied[cid] = {'fate': 'rejected, kept as it is', 'comment': it['comment']}
    elif it['status'] == 'answered':
        applied[cid] = {'fate': 'answered, kept as it is', 'question': it['question'], 'answer': it['comment']}
    else:
        applied[cid] = {'fate': 'undecided; my advice was to leave it, so it stays as it is', 'advice': it['advice']}
assert sorted(applied) == sorted(CARDS), set(CARDS) ^ set(applied)
for cid, old, new, _ in changes:
    assert md.count(old) == 1, (cid, old)
    md = md.replace(old, new)
ART.write_text(md, encoding='utf-8')

led = json.loads(LEDGER.read_text(encoding='utf-8'))
have = {e['id'] for e in led['entries']}
for cid, old, new, how in changes:
    c, it = CARDS[cid], ITEMS[cid]
    e = {'id': 'joel-125-%s' % cid.lower(), 'status': 'applied',
         'what': ('His own version on the sense-read marking page, card %s (%s), word for word.' if how else
                  'Card %s of the sense-read marking page (%s), which he approved: "%%s" to "%%s".' % (cid, c['title'])) % (
                      (cid, c['title']) if how else (old, new)),
         'joel': WHEN + (': "%s"' % it['comment'] if it.get('comment') else ''), 'where': it['where'],
         'must_contain': [new], 'must_not_contain': [old]}
    assert e['id'] not in have
    led['entries'].append(e)
LEDGER.write_text(json.dumps(led, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

keep = json.loads(KEEP.read_text(encoding='utf-8'))
n = max(int(k['id'][1:]) for k in keep['keep'])
adds = [
    {'kind': 'spacing', 'quote': 'should be handling--we see this',
     'what': 'His double hyphen, as he typed it (card SR-11 would have made it a spaced dash). He wants his two hyphens, not an em dash.',
     'joel': ITEMS['SR-11']['comment'], 'where': 'card SR-11, the sense-read marking page of turn 124'},
    {'kind': 'spacing', 'quote': 'can turn into a kind of test--"First impressions',
     'what': 'As the one before: his double hyphen, as he typed it.', 'joel': ITEMS['SR-11']['comment'],
     'where': 'card SR-11, the sense-read marking page of turn 124'},
    {'kind': 'choice', 'quote': 'Even if every case is different',
     'what': 'Not a slip for "debatable" (card SR-69): his "even if" says one coherent lesson can\'t be drawn from many different cases, except that there may be something to the afterlife idea; and an experience can\'t be debated.',
     'joel': ITEMS['SR-69']['comment'], 'where': 'card SR-69, the sense-read marking page of turn 124'},
    {'kind': 'choice', 'quote': 'I still played around with half-hanging out the windows',
     'what': 'Not a contradiction with the bars just before it (card SR-373): he hung out of the windows before the bars went on and after, less far after.',
     'joel': ITEMS['SR-373']['comment'], 'where': 'card SR-373, the sense-read marking page of turn 124'},
]
for a in adds:
    n += 1
    keep['keep'].append(dict({'id': 'K%d' % n}, **a, when='2026-11-04 16:11 UTC', basis='his answer'))
KEEP.write_text(json.dumps(keep, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'APPLIED.json').write_text(json.dumps({'answers': WHEN, 'cards': applied}, ensure_ascii=False, indent=1) + '\n',
                                   encoding='utf-8')
print('applied %d changes (%d approved, %d his version); %d kept on KEEP-AS-IS.json (K%d to K%d); %d left as they are' % (
    len(changes), sum(1 for v in applied.values() if v['fate'] == 'approved'), sum(1 for v in applied.values() if v['fate'] == 'his version'),
    len(adds), n - len(adds) + 1, n, sum(1 for v in applied.values() if v['fate'].startswith('undecided'))))
