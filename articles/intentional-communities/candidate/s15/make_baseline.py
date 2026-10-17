"""Section 15's baseline (2026-10-17, the overnight run of Joel's 02:07 UTC message): the published text of "What This Looks
Like From Sénégal" as it stands in HUMANIZED-SO-FAR.md, read by Pangram as a whole and in groups of at least 50 words by
spaces (a short paragraph goes with its neighbor, each heading with the paragraph under it). The images, the two captions and
the page's embed lines are left out of the groups; the whole section keeps the captions, as a reader sees them. Batch 321g.
Run from candidate/: python3 s15/make_baseline.py

Every text is Joel's published wording, so each record is an owner record; the whole section is a measurement of the
published text, not an install.
"""
import hashlib, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

SKIP = re.compile(r'^(\[image \d+\]|\[Professor Baby Sheep|Double click to interact with video)')
bl = [b.strip() for b in re.split(r'\n\s*\n', (HERE / 'v0.md').read_text(encoding='utf-8')) if b.strip()]
reader = [b for b in bl if not SKIP.match(b)]
prose = [b for b in reader if not b.startswith('[caption]')]
IDS = ['H1'] + ['H1-P%d' % i for i in range(1, 6)] + ['H2'] + ['H2-P%d' % i for i in range(1, 8)] + ['H3'] + ['H3-P%d' % i for i in range(1, 9)]
assert len(prose) == len(IDS), (len(prose), len(IDS))
T = dict(zip(IDS, prose))
GROUPS = {'A': ['H1', 'H1-P1', 'H1-P2'], 'B': ['H1-P3', 'H1-P4'], 'C': ['H1-P4', 'H1-P5'],
          'D': ['H2', 'H2-P1', 'H2-P2'], 'E': ['H2-P3', 'H2-P4'], 'F': ['H2-P5', 'H2-P6'], 'G': ['H2-P6', 'H2-P7'],
          'H': ['H3', 'H3-P1'], 'I': ['H3-P2'], 'J': ['H3-P3'], 'K': ['H3-P4'], 'L': ['H3-P5'], 'M': ['H3-P6', 'H3-P7'],
          'N': ['H3-P8']}
drafts, gate = {}, {}
for g, ids in GROUPS.items():
    t = '\n\n'.join(plain(T[i]) for i in ids)
    k = 'S15-' + g
    drafts[k] = t
    gate[k] = {'kind': 'owner', 'joel': 'the published text of section 15, What This Looks Like From Sénégal', 'parts': ids,
               'words': len(t.split())}
    assert len(t.split()) >= 50, (k, len(t.split()))
drafts['S15v0'] = '\n\n'.join(plain(re.sub(r'^\[caption\]\s*', '', b)) for b in reader)  # a caption as the reader sees it
gate['S15v0'] = {'kind': 'section', 'parts': ['installed'], 'repeats': 0,
                 'repeats_note': 'a measurement of the published section, not an install', 'words': len(drafts['S15v0'].split())}
(HERE / 'b321' / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'b321' / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'b321' / 'drafts.json'),
                    str(HERE / 'b321' / 'GATE.json'), str(HERE / 'b321' / 'b321.js'), '--name', 'B321'] + list(drafts),
                   capture_output=True, text=True)
print(r.stdout[-300:], r.stderr[-800:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(HERE / 'b321' / 'b321-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
for k, v in gate.items():
    print(k, v['words'], drafts[k][:70].replace('\n', ' / '))
