#!/usr/bin/env python3
"""Assemble the fixed version of the romance post for its whole-article check (2026-11-07): the live post's paragraphs
(LIVE-INDEX.txt: each paragraph's place, tag and the first 12 hex characters of the SHA-256 of its text with its
whitespace collapsed, read from the post page) with each section's and spot's best tested text in place.

Each check text (CHECK-<key>.txt) is aligned with the live paragraphs by those fingerprints: its unchanged paragraphs
anchor it, and difflib's opcodes between the live run and the check's paragraphs give every changed paragraph. Headings
stay where they are (the check texts left them out). Writes PLAN.json: per check, its live range and its operations."""
import difflib
import glob
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'

# The best tested text of each section and spot, in the post's order (CURRENT-STATE.md, the 2026-11-08 checkpoint). His S2
# and S17 are in the sections that read Human, High with them (#117; #136, with his doubled "example" taken out);
# Romance and Idealization are in their section checks (#122, #132), which take the places of S15's and S8's spot
# checks. Jealousy 366 to 370 is his T2 answer, in the section check that read it Human with no Low (#135). "Two
# Pillars" 332 (owner lock) stays as the live post has it.
CHECKS = [
    ('romance-s1#1', 'S1'), ('romance-low-sit#100', 'Situationships'), ('romance-low-labels#84', 'Labels'),
    ('romance-sec-bypass#117', 'Spirituality to bypass intimacy (his S2)'),
    ('romance-s3#3', 'S3'), ('romance-low-deeper#97', 'It always goes deeper'), ('romance-low-clar#71', 'The window of clarity'),
    ('romance-low-peek#67', 'Peeking thru the window'), ('romance-low-convo#107', 'The conversation about flaws'),
    ('romance-low-flaws#61', 'My flaws'), ('romance-low-tricky#68', 'Things get tricky fast'),
    ('romance-low-ideal#143', 'Beware idealization (S8, 145 to 151)'),
    ('romance-low-ptsd#73', 'Anti-PTSD'), ('romance-s6#30', 'S6'), ('romance-low-dam#70', 'Holding up a leaky dam'),
    ('romance-low-slow#96', 'Slow & steady'), ('romance-low-nitty#113', 'From flow to nitty gritty'),
    ('romance-sec-whole-world#44', 'Don’t make your partner your whole world'),
    ('romance-low-disc#88', 'Disconnect to connect'), ('romance-low-babies#101', 'Some babies grow up faster'),
    ('romance-low-levels#102', 'Different levels in different domains'), ('romance-s14#21', 'S14'),
    ('romance-low-muses#81', 'Muses & Directors'), ('romance-low-romance#122', 'Romance (S15, 285 to 287)'), ('romance-low-fantasy#99', 'Fantasy'),
    ('romance-low-queen#82', 'The Queen of Orgasms'),
    ('romance-sec-spiritual-sex#136', 'Can making love be a spiritual practice? (r20 and his S17)'),
    ('romance-s18#25', 'S18'), ('romance-s19#32', 'S19'),
    ('romance-low-choosing#106', 'What are you actually choosing together?'),
    ('romance-sec-vows#110', 'Which marriage vows are honest?'),
    ('romance-low-jeal#137', 'Jealousy on trial (his T2 answer)'), ('romance-low-artificial#104', 'Why all of this sounds artificial'),
    ('romance-low-gaslight#105', 'Gaslighting in the dark'), ('romance-s22#69', 'After leaving (S22)'),
    ('romance-low-loss#109', 'What I gained from loss'),
]
KEEP = {332: 'Two Pillars 332 (owner lock)'}


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def fp(s):
    return hashlib.sha256(norm(s).encode('utf-8')).hexdigest()[:12]


live = []
for line in (HERE / 'LIVE-INDEX.txt').read_text(encoding='utf-8').splitlines():
    i, tag, h = line.split()
    live.append((int(i), tag, h))
# A list item shows twice in the page's paragraph list (its <li> and the <p> inside it): the <p> is the duplicate.
dup = {i for k, (i, tag, h) in enumerate(live) if k and tag == 'P' and live[k - 1][1] == 'LI' and live[k - 1][2] == h}
content = [(i, tag, h) for (i, tag, h) in live if not tag.startswith('H') and i not in dup]
pos = {i: k for k, (i, tag, h) in enumerate(content)}
by_hash = {}
for k, (i, tag, h) in enumerate(content):
    by_hash.setdefault(h, []).append(k)

preds = {}
for line in LEDGER.read_text(encoding='utf-8').splitlines():
    d = json.loads(line)
    if d.get('type') == 'prediction':
        preds[d['id']] = d

plan = []
for pid, name in CHECKS:
    p = preds[pid]
    files = glob.glob(str(ROOT / ('articles/romance/humanize/fix-20261107/*/checks/CHECK-%s.txt' % p['key'])))
    assert len(files) == 1, (pid, files)
    text = pathlib.Path(files[0]).read_text(encoding='utf-8')
    if text.endswith('\n') and not p['text'].endswith('\n'):
        text = text[:-1]
    assert hashlib.sha256(text.encode('utf-8')).hexdigest() == p['sha256'], ('sha mismatch', pid)
    paras = [x for x in re.split(r'\n\s*\n', text) if x.strip()]
    hs = [fp(x) for x in paras]
    anchors = [(j, by_hash[h][0]) for j, h in enumerate(hs) if len(by_hash.get(h, [])) == 1]
    plan.append({'id': pid, 'name': name, 'key': p['key'], 'file': str(pathlib.Path(files[0]).relative_to(ROOT)),
                 'paras': paras, 'hashes': hs, 'anchors': anchors})
json.dump({'content': content, 'plan': plan}, open(HERE / 'PLAN-RAW.json', 'w', encoding='utf-8'), ensure_ascii=False)
for e in plan:
    a = e['anchors']
    rng = (content[a[0][1]][0], content[a[-1][1]][0]) if a else None
    print('%-28s %-34s paras %2d anchors %2d first-anchor j%s live range by anchors %s' % (
        e['id'], e['name'][:34], len(e['paras']), len(a), a[0][0] if a else '-', rng))

# Each check's live run (its first and last paragraph in the page's list), from its anchors and its section's headings;
# where a check has few or no unchanged paragraphs, from the section's bounds and the spot's own words found in the page
# (S1 27 to 28, S3 65, S6 102 to 103, S18 331).
RANGES = {
    'romance-s1#1': (27, 28), 'romance-low-sit#100': (33, 36), 'romance-low-labels#84': (38, 46), 'romance-s3#3': (65, 65),
    'romance-low-deeper#97': (69, 74), 'romance-low-clar#71': (105, 111), 'romance-low-peek#67': (113, 120),
    'romance-low-convo#107': (122, 128), 'romance-low-flaws#61': (130, 137), 'romance-low-tricky#68': (139, 141),
    'romance-low-ideal#143': (143, 151), 'romance-sec-bypass#117': (53, 62), 'romance-low-ptsd#73': (153, 162), 'romance-s6#30': (102, 103),
    'romance-low-dam#70': (175, 178), 'romance-low-slow#96': (180, 184), 'romance-low-nitty#113': (199, 201),
    'romance-sec-whole-world#44': (209, 216), 'romance-low-disc#88': (218, 224), 'romance-low-babies#101': (231, 241),
    'romance-low-levels#102': (243, 250), 'romance-s14#21': (258, 260), 'romance-low-muses#81': (262, 275),
    'romance-low-romance#122': (282, 290), 'romance-low-fantasy#99': (292, 297), 'romance-low-queen#82': (299, 302),
    'romance-sec-spiritual-sex#136': (304, 317),
    'romance-s18#25': (331, 331), 'romance-s19#32': (334, 335), 'romance-low-choosing#106': (341, 347),
    'romance-sec-vows#110': (349, 352), 'romance-low-jeal#137': (357, 370), 'romance-low-artificial#104': (404, 413), 'romance-low-gaslight#105': (431, 435),
    'romance-s22#69': (437, 441), 'romance-low-loss#109': (443, 456),
}
ops_all, taken = [], {}
for e in plan:
    lo, hi = RANGES[e['id']]
    run = [k for k, (i, tag, h) in enumerate(content) if lo <= i <= hi]
    for k in run:
        i = content[k][0]
        assert i not in KEEP, ('a kept paragraph is inside a check run', e['id'], i)
        assert i not in taken, ('two checks cover one paragraph', e['id'], taken.get(i), i)
        taken[i] = e['id']
    a = [content[k][2] for k in run]
    sm = difflib.SequenceMatcher(None, a, e['hashes'], autojunk=False)
    e['range'] = [lo, hi]
    e['ops'] = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            continue
        rec = {'op': op, 'live': [content[run[k]][0] for k in range(i1, i2)], 'new': e['paras'][j1:j2]}
        e['ops'].append(rec)
        ops_all.append(dict(rec, check=e['id'], name=e['name']))
    print('%-28s %-30s live %3d-%3d (%2d paras) -> %2d paras; ops: %s' % (
        e['id'], e['name'][:30], lo, hi, len(run), len(e['paras']),
        ', '.join('%s %s>%d' % (o['op'][0], '+'.join(map(str, o['live'])) or '-', len(o['new'])) for o in e['ops'])))
changed_live = sorted({i for o in ops_all for i in o['live']})
print('changed live paragraphs:', len(changed_live), '| ops:', len(ops_all))
print('CHANGED', ' '.join(map(str, changed_live)))
json.dump({'content': content, 'dup': sorted(dup), 'plan': plan, 'ops': ops_all, 'changed_live': changed_live,
           'keep': KEEP}, open(HERE / 'PLAN.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
