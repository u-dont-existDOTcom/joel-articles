"""Batch 320g (2026-10-17): section 10 v5, question 36 a (Joel's pick at 02:07 UTC: "(with private details protected)" in
his last paragraph of 2026-10-14), the paragraph alone and the whole section. Gate kind "owner", as 28 b's change was
(fix-20261015/GATE.json: "my wording, his pick"). Run from candidate/: python3 joel-20261017/b320/make_batch.py"""
import hashlib, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

bl = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 's10-v5.md').read_text(encoding='utf-8')) if b.strip()]
bl = [b for b in bl if not b.startswith(('[image', '<!--'))]
assert bl[0] == '# From One Community to a Movement', bl[0]
P = [b for b in bl if b.startswith('Whenever a community or a federation creates or applies a rule')]
assert len(P) == 1
drafts = {'S10v5-P9': plain(P[0]), 'S10v5': '\n\n'.join(plain(b) for b in bl)}
JOEL = '2026-10-17 02:07 UTC: "36a" (my wording, his pick; joel-20261017/joel-20261017-0207-message.txt)'
gate = {'S10v5-P9': {'kind': 'owner', 'joel': JOEL},
        'S10v5': {'kind': 'section', 'parts': ['S10v5-P9', 'installed'], 'repeats': 0,
                  'repeats_note': 'the change adds four words inside one sentence; section 10 had no repeats inside it (fix-20261014b/gate/REPEATS.md)'}}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b320.js'), '--name', 'B320'] + list(drafts), capture_output=True, text=True)
print(r.stdout[-400:], r.stderr[-800:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(HERE / 'b320-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
print({k: len(t.split()) for k, t in drafts.items()})
