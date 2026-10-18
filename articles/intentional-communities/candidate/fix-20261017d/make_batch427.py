"""Batch 427g (2026-10-17 night): section 8 with Joel's 23:10 sentence (54), held back from 425g while its repeats check ran.
The changed paragraph (152 words) alone and section 8 v32 whole, in ptext's section() format. His words, so the paragraph is
an owner record; the section needs its repeats check (REPEATS-s8b.md, answered in DISPOSITIONS-2310.md). Section 2 isn't in
this batch: it waits for question 56. Run from candidate/: python3 fix-20261017d/make_batch427.py"""
import hashlib, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain, section  # noqa: E402

JOEL = ('Joel, 2026-10-17 23:10 UTC (joel-20261017/joel-20261017-2310-message.txt): 54 "actually i would change it to: ..." '
        '(his sentence after "if they are known to be honest.")')
H8 = '# The Grown Children Get the Final Review'
SKIP = re.compile(r'^(\[image \d+\]|\[Professor Baby Sheep|Double click to interact with video|<!--)')
s8 = (HERE / 's8-v32.md').read_text(encoding='utf-8')
blocks = [b.strip() for b in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', s8, flags=re.S)) if b.strip()]
paras = [plain(b) for b in blocks if not b.startswith('#') and not SKIP.match(b) and not b.startswith('[caption]')]
i = next(k for k, p in enumerate(paras) if p.startswith('Protecting children is the duty of adults'))
NEW = ("And those who are known to lie a lot are especially targeted by abusers who know their accusations won't be "
       "believed.")
assert NEW in paras[i] and len(paras[i].split()) >= 50
assert all(len(paras[j].split()) >= 50 for j in (i - 1, i + 1))   # so no neighbor pair is needed
drafts = {'S8v32-truth': paras[i], 'S8v32': section(s8, H8)}
gate = {'S8v32-truth': {'kind': 'owner', 'joel': JOEL},
        'S8v32': {'kind': 'section', 'parts': ['installed', 'S8v32-truth'], 'repeats': 0,
                  'repeats_note': 'fix-20261017d/DISPOSITIONS-2310.md (REPEATS-s8b.md)'}}
for k in drafts:
    gate[k]['words'] = len(drafts[k].split())
    print(k, gate[k]['words'], gate[k]['kind'], '|', drafts[k][:70].replace('\n', ' / '))
if (HERE / 'REPEATS-s8b.md').exists() and 'Section 8' in (HERE / 'DISPOSITIONS-2310.md').read_text(encoding='utf-8'):
    out = HERE / 'b427'
    out.mkdir(exist_ok=True)
    (out / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (out / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(out / 'drafts.json'),
                        str(out / 'GATE.json'), str(out / 'b427.js'), '--name', 'B427'] + list(drafts), capture_output=True, text=True)
    print(r.stdout[-1800:], r.stderr[-1500:])
    if r.returncode == 0:
        items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
        (out / 'b427-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
else:
    print('waiting for REPEATS-s8b.md and its dispositions (a "Section 8" part in DISPOSITIONS-2310.md)')
