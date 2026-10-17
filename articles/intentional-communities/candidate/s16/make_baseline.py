"""Section 16's baseline (2026-10-17, the overnight run of Joel's 02:07 UTC message): the published text of "Practice Comes
Before Property" as it stands in HUMANIZED-SO-FAR.md (the same bytes as original.md), read by Pangram as a whole and in groups
of at least 50 words by spaces (a short paragraph goes with its neighbor, each heading with the paragraph under it). The
images and the caption are left out of the groups; the whole section keeps the caption, as a reader sees it. Batch 324g.
Run from candidate/: python3 s16/make_baseline.py

Every text is Joel's published wording, so each record is an owner record; the whole section is a measurement of the
published text, not an install.
"""
import hashlib, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

SKIP = re.compile(r'^\[image \d+\]')
bl = [b.strip() for b in re.split(r'\n\s*\n', (HERE / 'v0.md').read_text(encoding='utf-8')) if b.strip()]
reader = [b for b in bl if not SKIP.match(b)]
prose = [b for b in reader if not b.startswith('[caption]')]
IDS = (['H1'] + ['H1-P%d' % i for i in range(1, 4)] + ['H2'] + ['H2-P%d' % i for i in range(1, 7)] + ['H3'] +
       ['H3-P%d' % i for i in range(1, 12)])
assert len(prose) == len(IDS), (len(prose), len(IDS))
T = dict(zip(IDS, prose))
GROUPS = {'A': ['H1', 'H1-P1', 'H1-P2'], 'B': ['H1-P3'], 'C': ['H2', 'H2-P1', 'H2-P2'], 'D': ['H2-P3', 'H2-P4'],
          'E': ['H2-P5'], 'F': ['H2-P5', 'H2-P6'], 'G': ['H3', 'H3-P1', 'H3-P2', 'H3-P3'], 'H': ['H3-P4', 'H3-P5'],
          'I': ['H3-P6', 'H3-P7'], 'J': ['H3-P8'], 'K': ['H3-P9', 'H3-P10'], 'L': ['H3-P10', 'H3-P11']}
drafts, gate = {}, {}
for g, ids in GROUPS.items():
    t = '\n\n'.join(plain(T[i].lstrip('#').strip()) if i in ('H1', 'H2', 'H3') else plain(T[i]) for i in ids)
    k = 'S16-' + g
    drafts[k] = t
    gate[k] = {'kind': 'owner', 'joel': 'the published text of section 16, Practice Comes Before Property', 'parts': ids,
               'words': len(t.split())}
    assert len(t.split()) >= 50, (k, len(t.split()))
drafts['S16v0'] = '\n\n'.join(plain(re.sub(r'^\[caption\]\s*', '', b).lstrip('#').strip()) for b in reader)
gate['S16v0'] = {'kind': 'section', 'parts': ['installed'], 'repeats': 0,
                 'repeats_note': 'a measurement of the published section, not an install', 'words': len(drafts['S16v0'].split())}
(HERE / 'b324' / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'b324' / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'b324' / 'drafts.json'),
                    str(HERE / 'b324' / 'GATE.json'), str(HERE / 'b324' / 'b324.js'), '--name', 'B324'] + list(drafts),
                   capture_output=True, text=True)
print(r.stdout[-300:], r.stderr[-800:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(HERE / 'b324' / 'b324-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
for k, v in gate.items():
    print(k, v['words'], drafts[k][:70].replace('\n', ' / '))
