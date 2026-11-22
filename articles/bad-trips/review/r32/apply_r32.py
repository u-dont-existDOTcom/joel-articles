#!/usr/bin/env python3
"""apply_r32.py - round 32's answers (Joel, exported 2026-11-09 20:08:42 UTC; ANSWERS-R32-20261109-2008.json) put into the
guide.

- SEIZE-HEAD, "a": the heading "### What Else May Help: At the Aura, and Alongside Rescue Medicine" before the aura
  paragraph, so first aid, the rescue medicine and when to call medics stand above it.
- GROUND-ORDER, approved, with his comment "we can remove the 2nd line about love becomes practical first": the order
  paragraph moves to the Grounding Menu, after "Grounding is love becoming practical. ...", without its last sentence
  ("When the nervous system is on fire, love becomes practical first.").
- GROUND-ROOM, revised: "this is too much boilerplate stuff that ai added in to my guide. help mne locate more boilerplate
  stuff that could be removed. i want to remove room section, familiar object section, this line: "Say the date, place,
  and approximate time."". So Room and its three lines, A familiar object and its five lines, and that line of Time go;
  Room's move, which the card asked about, falls away with it. His other thought ("more useful would be smelling a nice
  natural scent like lime peel or something, but idk i feel like this is all said in multiple places also") and his ask
  to locate more boilerplate go to round 33.
- SHADOW-START, "b": the definition ("Shadow work to me is neither BDSM nor ...") and "Begin with my Inner Child Therapy
  guide ..." open the Shadow Work part, right under its heading; The Other Bypass ends on "... and honest conversation."

  python3 apply_r32.py      write the guide after round 32 and print what changed
"""
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parent.parent
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
BLOCKS = json.loads(BJ.read_text(encoding='utf-8'))
before_md = MD.read_text(encoding='utf-8')
assert '\n\n'.join(b['md'] for b in BLOCKS) + '\n' == before_md, 'the blocks and the guide disagree'
A = json.loads((HERE / 'ANSWERS-R32-20261109-2008.json').read_text(encoding='utf-8'))
R = json.loads((HERE / 'REVIEW-R32.json').read_text(encoding='utf-8'))
assert A['review_id'] == R['review_id'] == 'bad-trips-r32'
assert hashlib.sha256((HERE / 'PAGE-R32.md').read_bytes()).hexdigest() == A['article']['sha256']
I = {x['id']: x for x in A['items']}
assert I['SEIZE-HEAD']['comment'].strip().lower() == 'a'
assert I['GROUND-ORDER']['status'] == 'approved' and '2nd line about love becomes practical' in I['GROUND-ORDER']['comment']
assert I['GROUND-ROOM']['status'] == 'revise' and 'remove room section, familiar object section' in I['GROUND-ROOM']['comment']
assert I['SHADOW-START']['comment'].strip().lower() == 'b'


def ids():
    return [b['id'] for b in BLOCKS]


def unit(bid):
    return BLOCKS[ids().index(bid)]


def move(group, to_before):
    k = ids().index(group[0])
    assert ids()[k:k + len(group)] == group, (group, ids()[k:k + len(group)])
    taken = BLOCKS[k:k + len(group)]
    del BLOCKS[k:k + len(group)]
    j = ids().index(to_before)
    BLOCKS[j:j] = taken


def cut(bid, expect_start):
    b = unit(bid)
    assert b['md'].startswith(expect_start), (bid, b['md'][:80])
    BLOCKS.remove(b)


def swap(bid, old, new):
    b = unit(bid)
    assert b['md'].count(old) == 1, (bid, old)
    b['md'] = b['md'].replace(old, new)


# SEIZE-HEAD: the heading he picked, before the aura paragraph
HEAD = '### What Else May Help: At the Aura, and Alongside Rescue Medicine'
assert ids()[ids().index('B112') + 1] == 'N-WARN'
BLOCKS.insert(ids().index('N-WARN'), {'id': 'R32-SEIZE', 'kind': 'h3', 'md': HEAD, 'text': None})

# GROUND-ORDER: the order to the menu, after its first paragraph, without "love becomes practical first"
swap('B252', ' When the nervous system is on fire, love becomes practical first.', '')
assert unit('B252')['md'] == ('A useful order is **room → body → human → time → meaning**. Most people begin with meaning '
                              'because the experience feels cosmic.')
assert ids()[ids().index('B295') + 1] == 'B296'
move(['B252'], 'B296')

# GROUND-ROOM, his revision: Room, A familiar object, and Time's date line go
cut('B299', '**A familiar object**')
cut('B300', '- Choose it ahead of time, while calm and regulated')
cut('B305', '**Room**')
cut('B306', '- Name five ordinary objects.')
swap('B310', '- Say the date, place, and approximate time.\n', '')
assert unit('B310')['md'] == ('- Remember that these states usually rise, peak, and change.\n'
                              '- Put every big decision into tomorrow\'s notebook.')

# SHADOW-START: the definition and where to begin open the Shadow Work part
assert ids()[ids().index('R30-SHADOW') + 1] == 'B376'
assert unit('B344')['md'].startswith('Shadow work to me is neither BDSM') and unit('B345')['md'].startswith('Begin with my')
move(['B344', 'B345'], 'B376')

MD.write_text('\n\n'.join(b['md'] for b in BLOCKS) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
after = MD.read_text(encoding='utf-8')
print('words: %d -> %d' % (len(before_md.split()), len(after.split())))
for a, z in (('B110', 'B111'), ('B294', 'B297'), ('B307', 'B311'), ('R30-SHADOW', 'B376'), ('B342', 'B346')):
    if z not in ids():
        z = ids()[ids().index(a) + 4]
    print(' '.join(ids()[ids().index(a):ids().index(z) + 1]))
