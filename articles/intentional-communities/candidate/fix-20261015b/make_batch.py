"""Batch 287g (2026-10-15): Joel's section 4 paragraphs of 11:04 UTC (his "27: this passes") and section 4 whole; and
the section 13 v5 paragraphs whose gate records came back clean in round r3 (s13/review-r3/), alone or with a
neighbor when under 50 words, the first one with its heading. Run from candidate/: python3 fix-20261015b/make_batch.py

Writes drafts.json and GATE.json here; then, from the repo root:
  python3 tools/humanization/pangram_gate.py articles/intentional-communities/candidate/fix-20261015b/drafts.json \
      articles/intentional-communities/candidate/fix-20261015b/GATE.json \
      articles/intentional-communities/candidate/fix-20261015b/gui/b287.js --name B287 KEY...
"""
import json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import blocks, section, plain  # noqa: E402

art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
drafts, gate = {}, {}
JOEL = 'Joel, 2026-10-15 11:04 UTC: "27: this passes:" (joel-20261015/joel-20261015-1104-message.txt)'

s4 = [t for _, t in blocks(art, '# The Four Parts That Have to Pl/ork Together')]
pa = next(t for t in s4 if t.startswith('Inner-child reparenting means'))
pb = next(t for t in s4 if t.startswith('And this reparenting journey'))
drafts['J4-P11d'] = pa
gate['J4-P11d'] = {'kind': 'owner', 'joel': JOEL + ', his reparenting paragraph'}
drafts['J4-P11dP12d'] = pa + '\n\n' + pb
gate['J4-P11dP12d'] = {'kind': 'owner', 'joel': JOEL + ', his two paragraphs (the second is under 50 words)'}
drafts['S4v113'] = section(art, '# The Four Parts That Have to Pl/ork Together')
gate['S4v113'] = {'kind': 'section', 'parts': ['J4-P11d', 'J4-P11dP12d', 'installed'], 'repeats': 0,
                  'repeats_note': 's13/review-r3/REPEATS.md (2026-10-15): nothing on his two new paragraphs (B68, B69); the '
                                  "section's other repeats as answered on 2026-10-14 (fix-20261014b/gate/REPEATS-DISPOSITIONS.md)"}

v5 = (C / 's13' / 'v5.md').read_text(encoding='utf-8')
P = [p.strip() for p in re.split(r'\n\s*\n', v5) if p.strip()]
heads = [i for i, p in enumerate(P) if p.startswith('#')]
def para(h, n):  # n-th paragraph (1-based) under the h-th heading (0-based)
    return P[heads[h] + n]
M = {}
for x in 'ab':
    labs = dict(re.findall(r'^\s*T(\d+):\s*([SB ]+)\s*$', (C / 's13' / 'review-r3' / ('MARCH-labels-%s.txt' % x)).read_text(), re.M))
    for k, v in labs.items():
        M.setdefault(int(k), []).append(v.strip())
order = [(h, n) for h in range(len(heads)) for n in range(1, (heads[h + 1] if h + 1 < len(heads) else len(P)) - heads[h])]
T = {hn: i + 1 for i, hn in enumerate(order)}
NOTE = {
    (0, 1): 'trace r3 T1 called "Even if it’s just three people around somebody’s kitchen table, that counts." added; trace r2 T1 called the same words an instance of the published claim. Traces disagree on unchanged words: the published sentence decides (gate, section 3 lesson), and the line only illustrates "small group".',
    (0, 2): 'trace r3 T1 called "That’s relational pl/ork." a new label; it names the article’s own section 4 term for working through conflict and jealousy (the r2 stance check quoted section 4 for it), and both stance checks of r3 read it with the whole article and raised nothing.',
}
GOOD = [((0, 1), (0, 2)), ((0, 2),), ((0, 3),), ((2, 2),), ((2, 3),), ((2, 4),), ((3, 6), (3, 7)), ((3, 7),), ((3, 8),), ((4, 3),)]
NAMES = {'S13v5-1P1P2': ((0, 1), (0, 2)), 'S13v5-1P2': ((0, 2),), 'S13v5-1P3': ((0, 3),), 'S13v5-3P2': ((2, 2),),
         'S13v5-3P3': ((2, 3),), 'S13v5-3P4': ((2, 4),), 'S13v5-4P6P7': ((3, 6), (3, 7)), 'S13v5-4P7': ((3, 7),),
         'S13v5-4P8': ((3, 8),), 'S13v5-5P3': ((4, 3),)}
for key, parts in NAMES.items():
    md = [para(*hn) for hn in parts]
    if key == 'S13v5-1P1P2':
        md = [P[heads[0]]] + md
    text = '\n\n'.join(plain(x) for x in md)
    drafts[key] = text
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write('\n\n'.join(x for x in md if not x.startswith('#')) + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    lint = re.search(r'verdict: (\w+)', r.stdout).group(1)
    marches = [m for hn in parts for m in M[T[hn]]]
    rec = {'kind': 'draft', 'march': marches, 'march_note': 's13/review-r3/MARCH-labels-a.txt and -b.txt, paragraphs ' +
           ', '.join('T%d' % T[hn] for hn in parts), 'cold': 'OK', 'cold_note': 's13/review-r3/SENSE-a.md, SENSE-b.md: OK',
           'grounding': 'OK', 'grounding_note': 's13/review-r3/trace-T*.md' + ''.join('; ' + NOTE[hn] for hn in parts if hn in NOTE),
           'stance': 0, 'stance_note': 's13/review-r3/STANCE-pub.md, STANCE-sofar.md: no conflict in these paragraphs',
           'lint': lint, 'missing': [], 'words': len(text.split())}
    gate[key] = rec
for k in gate:
    gate[k].setdefault('words', len(drafts[k].split()))
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, v in gate.items():
    print(k, v['words'], v['kind'], v.get('lint', ''), v.get('march', ''), drafts[k][:60].replace('\n', ' / '))
