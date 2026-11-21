#!/usr/bin/env python3
"""make_tags.py - turn 58's checks of the remedy headings he picked in round 47 with their evidence tags (his round-46
answer, shown to him under each heading on the round-47 page) on their own line, read with the section's first paragraph,
the way the reader meets them (CURRENT-STATE's plan since turn 56: each heading with its tag line and first paragraph,
checked before the tag goes in). Only the eight remedies whose paragraphs read Human: the six that read AI (zeolite,
activated charcoal, the oils, DMSO, beach morning glory, niacin) get their tags with their fixes. Creatine and mango leaf
tea go together, since mango's section is one 18-word line. Also the Grounding Menu's Body, Smell and Breath parts, whose
Smell line now names the stabilizers section by its new heading.

  python3 make_tags.py         writes TEST-<key>.txt and ITEMS-h66a.json
"""
import hashlib, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
B = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
IDS = {b['id']: i for i, b in enumerate(B)}
TAGS = {'B166': 'Tried by Me and Friends', 'B181': 'Tried by Me and Friends', 'B183': 'Tried by Me and Friends',
        'H54-CREATINE-H': 'Tried by Me', 'H54-MANGO-H': 'Tried by Me and Friends', 'R30-RUE1': 'Tried by Me and Friends',
        'B185': 'Tried by Me and Friends', 'B189': 'Tried by Me and Friends'}


def plain(md):
    md = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', md).replace('**', '')
    md = re.sub(r'(?<![\w*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![\w*])', r'\1', md)
    md = re.sub(r'^#{1,6}\s+', '', md)
    return re.sub(r'^-\s+', '', md, flags=re.M)


def unit(hid):
    i = IDS[hid]
    return [plain(B[i]['md']), '[%s]' % TAGS[hid], plain(B[i + 1]['md'])]


KEYS = {
    't1-coffee-1': unit('B166'),
    't2-sniffer-1': unit('B181'),
    't3-humic-1': unit('B183'),
    't4-creatine-mango-1': unit('H54-CREATINE-H') + unit('H54-MANGO-H'),
    't5-rue-1': unit('R30-RUE1'),
    't6-ocean-1': unit('B185'),
    't7-shungite-1': unit('B189'),
    't8-menu-smell-1': [plain(B[IDS[x]]['md']) for x in ('B297', 'B298', 'R33-SMELL', 'R33-SMELL-L', 'B301', 'B302')],
}
items = []
for k, parts in KEYS.items():
    t = '\n'.join(parts)
    (HERE / ('TEST-%s.txt' % k)).write_text(t + '\n', encoding='utf-8')
    items.append([k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()])
    print(k, len(t.split()), 'words')
(HERE / 'ITEMS-h66a.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
