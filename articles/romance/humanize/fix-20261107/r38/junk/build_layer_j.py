#!/usr/bin/env python3
"""The junk pass's outcome, paragraph by paragraph: each section's try that read Human High in every window (texts/, or
t2/ where the first try had one short Medium window), its changed paragraphs mapped to the post's paragraph numbers,
with the paragraph's links put back (the check texts carry a link's words only). A change of model text that keeps the
meaning goes into MINE-R38J.json (a layer of whole/build.py after MINE-R38.json); a change that might change the meaning
goes to CARDS-T8.json for the eighth marking page, with its section's check.

  python3 build_layer_j.py   ->  MINE-R38J.json, CARDS-T8.json
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parents[1]
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
LINK = re.compile(r'\[([^\]]+)\]\(((?:[^()\s]|\([^()\s]*\))+)\)')
plain = lambda t: LINK.sub(r'\1', t)
repl = {int(k): v for k, v in json.loads((FIX / 'whole' / 'REPLACEMENTS.json').read_text(encoding='utf-8')).items()}
if (HERE / 'MINE-R38J.json').exists():   # take this layer back out of REPLACEMENTS.json first
    for ch in reversed(json.loads((HERE / 'MINE-R38J.json').read_text(encoding='utf-8'))['changes']):
        now = repl[ch['live']]
        k = now.index(ch['after'][0])
        repl[ch['live']] = now[:k] + [ch['before']] + now[k + 1:]
post = {}
for line in (FIX / 'live-check' / 'LIVE-POST-BLOCKS-20261123.jsonl').read_text(encoding='utf-8').splitlines():
    r = json.loads(line)
    if r.get('n') is not None:
        post[r['n']] = r['text']
cur = lambda n: repl.get(n, [post[n]])
H = 'https://www.pangram.com/history/'
# section: (folder of its High try, its check, items, card id or None for the article)
DONE = {
    'r38-09-labels-are-descriptive-not-prescriptive': ('texts', H + 'd350c49e-7388-4195-9c0e-d68d1a7d06c1', 'B47', None),
    'r38-10-should-you-be-in-a-relationship-at-all': ('texts', H + '14dd222c-80ab-4081-8c71-22c7f7b8ef8a', 'B50, B54', 'J-B54'),
    'r38-24-peeking-thru-the-window-p1': ('texts', H + '83f2bd73-ac4a-45e6-a812-25d6593e9d78', 'B123', None),
    'r38-25-peeking-thru-the-window-p2': ('texts', H + '389d4b27-460e-41f4-95d1-b7a19ebcc09a', 'B128', None),
    'r38-29-things-get-tricky-fast': ('texts', H + '8d300648-e283-4b37-842c-ff05f7caeaf5', 'B148', None),
    'r38-33-anti-ptsd-can-be-just-as-dangerous-as-pt-p2': ('texts', H + 'f6992267-1ad3-4d02-812b-4b8049fc7455', 'B170, B173', None),
    'r38-34-seeing-idealization-right': ('t2', H + '4fca819f-3ceb-4696-9101-4cad8af7c8ae', 'B178', None),
    'r38-44-don-t-make-your-partner-your-whole-world-p1': ('texts', H + '48f4f1be-52c4-4b12-bfcc-fd3a822766a4', 'B217', 'J-B217'),
    'r38-46-disconnect-to-connect': ('texts', H + '8adb74f8-50a4-44bb-bc10-a791b91a8969', 'B230', None),
    'r38-47-babies-growing-up-again': ('texts', H + '6581e774-d26b-4cff-b3f5-0dae7f0746b3', 'B232, B234', None),
    'r38-51-different-levels-in-different-domains-ca-p2': ('texts', H + 'd76c7885-a0df-4467-ab2e-66c7100182cc', 'B255', 'J-B255'),
    'r38-64-twin-flames': ('texts', H + '02df440f-5b80-48d2-aa8f-33d2ced8a343', 'B330', None),
    'r38-89-gaslighting-in-the-dark': ('t2', H + '62a78ddb-899a-4516-97bc-07c037572eac', 'B459', None),
    'r38-90-after-leaving': ('texts', H + '8078da4a-e14e-412d-9a7c-f81454fe4558', 'B465', None),
    'r38-92-tough-love-p1': ('t2', H + '85106123-7f10-4138-b9bd-ccb72ddfc237', 'B477', None),
}


def live_of(par):
    hits = [(n, i) for n in post for i, x in enumerate(cur(n)) if norm(plain(x)) == norm(par)]
    assert len(hits) == 1, (par[:70], hits)
    return hits[0]


def relink(before, new_plain):
    out = new_plain
    for text, url in LINK.findall(before):
        if out.count(text) == 1:
            out = out.replace(text, '[%s](%s)' % (text, url))
        else:
            raise SystemExit('a link\'s words "%s" are not once in the new paragraph: %s' % (text, new_plain[:80]))
    return out


mine, cards = [], {}
for key, (where, link, items, card) in DONE.items():
    old = (FIX / 'r38' / 'checks' / ('CHECK-%s.txt' % key)).read_text(encoding='utf-8').strip().split('\n\n')
    new = (HERE / where / ('%s.txt' % key)).read_text(encoding='utf-8').strip().split('\n\n')
    assert len(old) == len(new), key
    for i, (o, n) in enumerate(zip(old, new)):
        if o == n:
            continue
        live, idx = live_of(o)
        before = cur(live)[idx]
        ch = {'card': card or 'R38J-%s' % key[4:6], 'kind': 'para', 'live': live, 'before': before,
              'after': [relink(before, n)], 'his_checks': [link], 'section_key': key, 'paragraph': i + 1, 'items': items}
        if card:
            cards.setdefault(card, []).append(ch)
        else:
            ch['why'] = 'the passage a reader flagged (%s, r30/junk/VETTED.md), fixed his way; the section then read Human High' % items
            mine.append(ch)
(HERE / 'MINE-R38J.json').write_text(json.dumps({
    'about': 'My tested fixes of the partly real junk passages (r30/junk/VETTED.md) that keep the meaning, 2026-11-24: each '
             'in a section that read Human High in every window afterwards (ledger batch romance-r38j). A layer after '
             'r38/MINE-R38.json; the fixes that might change the meaning are cards on the eighth marking page.',
    'whose': 'mine', 'changes': mine}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'CARDS-T8.json').write_text(json.dumps(cards, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('in:', len(mine), 'paragraph changes;', 'cards:', ', '.join('%s (%d)' % (c, len(v)) for c, v in cards.items()))
for c in mine:
    print('  live %d %s' % (c['live'], c['after'][0][:70]))
