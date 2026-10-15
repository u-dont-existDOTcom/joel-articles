"""Batch 299g (2026-10-15, after Joel's 32 b): section 13 v21 read 56% AI as a whole (298g,
https://www.pangram.com/history/5e450ea7-ed52-402b-bae4-de06d266aec7) though every part reads Human on its own text. Runs
of two paragraphs across the first AI window (H1-P3 through H3-P4), and the last three subsections whole, to find which run
the windows key on; the first two subsections whole fail the linter's landing rule (B7/B13), so they go as pairs. The
section lessons say a stretch can pass alone and fail in the section (docs/HUMANIZATION-GATE.md, 248g), so these show where
to look, not what passes. A span's records are its parts' records
(s13/b298/GATE.json, from rounds r4 to r14); the cold reads and stance checks of round r14 covered the whole of v21.
Run from candidate/: python3 s13/b299/make_batch.py
"""
import json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
REPO = C.parents[2]
S13 = C / 's13'
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

v21 = (S13 / 'v21.md').read_text(encoding='utf-8')
blocks = [b.strip() for b in re.split(r'\n\s*\n', v21) if b.strip()]
heads = [i for i, b in enumerate(blocks) if b.startswith('#')]
cov = (S13 / 'b298' / 'COVERAGE.md').read_text(encoding='utf-8')
g298 = json.loads((S13 / 'b298' / 'GATE.json').read_text(encoding='utf-8'))
d298 = json.loads((S13 / 'b298' / 'drafts.json').read_text(encoding='utf-8'))
keys = re.findall(r'^\| (?:H\d-P\d+b?|heading "[^"]+")[^|]*\| (\S+) \(', cov, re.M)
drafts, gate = {}, {}
IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1', 'H3-P2',
       'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8', 'H4-P9', None,
       'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
pos = {pid: i for i, pid in enumerate(IDS) if pid}
def span(first, last):
    """blocks from first to last (paragraph ids), with any heading between them"""
    return blocks[pos[first]:pos[last] + 1]
def with_head(pid):
    return blocks[pos[pid] - 1:pos[pid]]
PROBES = {
 'S13v21-1P3P4': span('H1-P3', 'H1-P4'),
 'S13v21-2P1P2': span('H2-P1', 'H2-P2'),
 'S13v21-2P3P3b': span('H2-P3', 'H2-P3b'),
 'S13v21-2P4h3P1': span('H2-P4', 'H3-P1'),
 'S13v21-3P2P3': span('H3-P2', 'H3-P3'),
 'S13v21-H3': with_head('H3-P1') + span('H3-P1', 'H3-P5'),
 'S13v21-H4': with_head('H4-P1') + span('H4-P1', 'H4-P9'),
 'S13v21-4P9h5P2': span('H4-P9', 'H5-P2'),
 'S13v21-H5': with_head('H5-P1') + span('H5-P1', 'H5-P4'),
}
for key, md in PROBES.items():
    text = '\n\n'.join(plain(x) for x in md)
    parts = [k for k in dict.fromkeys(keys) if all(t in text for t in d298[k].split('\n\n'))]
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write('\n\n'.join(x for x in md if not x.startswith('#')) + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    lint = re.search(r'verdict: (\w+)', r.stdout).group(1)
    march = [m for k in parts if 'march' in (g298[k] or {}) for m in g298[k]['march']]
    drafts[key] = text
    gate[key] = {'kind': 'draft', 'march': march, 'march_note': 'the parts\' readings: ' + ', '.join(parts),
                 'cold': 'OK', 'cold_note': 's13/review-r14/SENSE-a.md, SENSE-b.md: OK for all 27 paragraphs of v21',
                 'grounding': 'OK', 'grounding_note': 'the parts\' traces (s13/b298/GATE.json): ' + ', '.join(parts),
                 'stance': 0, 'stance_note': 's13/review-r14/STANCE-pub.md, STANCE-sofar.md: no conflicts in v21',
                 'lint': lint, 'missing': [], 'words': len(text.split())}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, v in gate.items():
    print(k, v['words'], v['lint'], len(v['march']), 'readings;', drafts[k][:60].replace('\n', ' / '))
