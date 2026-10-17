"""The appendix's baseline (2026-10-17): the published "Appendix: Watch These, Then Read These" as it stands in
HUMANIZED-SO-FAR.md (the same bytes as original.md's end), read by Pangram in groups of at least 50 words by spaces (its entries
are short, so each group is a run of entries, with the headings among them) and as a whole. Batch 329g.
Run from candidate/: python3 appendix/make_baseline.py"""
import hashlib, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

bl = [b.strip() for b in re.split(r'\n\s*\n', (HERE / 'v0.md').read_text(encoding='utf-8')) if b.strip()]
assert bl[0].startswith('# Appendix')
P = lambda b: plain(b.lstrip('#').strip())
# runs of blocks by index, each at least 56 words by spaces (Pangram's own count came in 6% under ours: 47 for a run of 50)
RUNS = {'A': range(1, 6), 'B': range(6, 10), 'C': range(10, 15), 'D': range(15, 22), 'E': range(22, 26), 'F': range(26, 30),
        'G': range(30, 34)}
GROUPS = {g: [bl[i] for i in r] for g, r in RUNS.items()}
drafts, gate = {}, {}
for g, parts in GROUPS.items():
    t = '\n\n'.join(P(b) for b in parts)
    k = 'APX-' + g
    drafts[k] = t
    gate[k] = {'kind': 'owner', 'joel': 'the published text of the appendix', 'parts': [b[:30] for b in parts], 'words': len(t.split())}
    assert len(t.split()) >= 56, (k, len(t.split()))
drafts['APXv0'] = '\n\n'.join(P(b) for b in bl)
gate['APXv0'] = {'kind': 'section', 'parts': ['installed'], 'repeats': 0, 'repeats_note': 'a measurement of the published appendix, not an install',
                 'words': len(drafts['APXv0'].split())}
(HERE / 'b329' / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'b329' / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'b329' / 'drafts.json'),
                    str(HERE / 'b329' / 'GATE.json'), str(HERE / 'b329' / 'b329.js'), '--name', 'B329'] + list(drafts),
                   capture_output=True, text=True)
print(r.stdout[-300:], r.stderr[-800:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(HERE / 'b329' / 'b329-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
for k, v in gate.items():
    print(k, v['words'], drafts[k][:80].replace('\n', ' / '))
