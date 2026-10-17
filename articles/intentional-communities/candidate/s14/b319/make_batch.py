"""Batch 319g (2026-10-17): section 14 v9, Joel's P2 of his 02:07 UTC message (question 38 b), alone and in the whole
section. His P2 is his own text (gate kind "owner"); the section's other paragraphs are installed and passed alone (305g-x,
315g), and its repeats were answered in round r6 (his cut takes out the one repeat left). Run from candidate/:
python3 s14/b319/make_batch.py"""
import hashlib, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

bl = [b.strip() for b in re.split(r'\n\s*\n', (C / 's14' / 'v9.md').read_text(encoding='utf-8')) if b.strip() and not b.startswith('[image')]
assert bl[0] == '# Dissolution and Exit' and len(bl) == 7
P2 = [b for b in bl if b.startswith('If the community dissolves')][0]
drafts = {'S14v9-P2': plain(P2), 'S14v9': '\n\n'.join(plain(b) for b in bl)}
JOEL = '2026-10-17 02:07 UTC, question 38 b: "simple i just deleted the 2nd one and it\'s still human on pangram" (joel-20261017/joel-20261017-0207-message.txt)'
gate = {'S14v9-P2': {'kind': 'owner', 'joel': JOEL},
        'S14v9': {'kind': 'section', 'parts': ['S14v9-P2', 'installed'], 'repeats': 0,
                  'repeats_note': 's14/review-r6/DISPOSITIONS-r6.md answered both repeats; his P2 takes out the repeated question 38 asked about'}}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b319.js'), '--name', 'B319'] + list(drafts), capture_output=True, text=True)
print(r.stdout[-400:], r.stderr[-800:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(HERE / 'b319-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
print({k: len(t.split()) for k, t in drafts.items()})
