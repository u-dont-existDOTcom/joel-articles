"""Batch 458g (2026-10-18): HG31 with only its B34 fix in the Pattern 4-6 window (457g: without the B25, B28 and B34 fixes it read Human; with B28's it read AI). Before that, 457g: diagnostic versions of the sections whose fixes keep reading AI (which fix is it?), and HG36's B11. The chosen samples, each section screened whole with its triaged fixes, and every paragraph of
those texts not checked before, in the same batch (make_b454's way); with every refix section that is ready
(make_b446.collect(): HG33's edit).

  HG06  rf-l/HG06.fixed.json   the forces paragraph from emu-ac (the best of three samples), 2 fixes
  HG26  rf-l/HG26.fixed.json   the get-help paragraphs from emu-ac (the best of three), 1 fix ("concerning")
  HG31  rf-m/HG31.fixed.json   the reframing questions from emu-ad (the better of two), 2 fixes
  HG36  rf-p/HG36.fixed.json   B10-B12 put back from emu-s, 2 fixes; and rf-p/HG36.interim.json, the installed text with B10-B12
                               as published (if Joel's own three paragraphs read Human, they stay)
  HG37  rf-v/HG37.fixed.json   its three pasted fixes reworded, B26 from the chosen sample (rf-t or rf-u)
  HG14  rf-v/HG14.fixed.json   its four AI paragraphs from the chosen samples
  HG15  rf-v/HG15.fixed.json   p10, p11 and p23-p24 from the chosen samples
  HG24  rf-o/HG24.fixed.json   B36-B37 as published, B42-B48 from emu-aa, both triages
  HG17  rf-v/HG17.fixed.json   the script in seven small windows, the better sample per window
A section whose file isn't there yet is left out (the builder says which).
Predictions: a section screen with a new sample 0.72 (refix samples so far: 32 of 44 Human); an edit under 18% changed 0.85
(triaged edits: 20 of 24); a paragraph check by tools/para_chance.py.
Run from humanize/: python3 fix-20261018/make_b455.py [--batch N] [--write]"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
sys.path.insert(0, str(HERE))
import install_fixed as I  # noqa: E402,F401  (puts tools/humanization on the path)
import paragraphs_alone as PA  # noqa: E402
import para_chance as PC  # noqa: E402
import make_b446 as B  # noqa: E402
from mkbatch import write_batch  # noqa: E402

B.PC = PC
rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
num = int(sys.argv[sys.argv.index('--batch') + 1]) if '--batch' in sys.argv else 458
dirs = [d for d in sorted(HERE.glob('b4*')) if list(d.glob('*-results.json'))]
seen = set(PA.results(dirs))
drafts, gate, preds, held = B.collect()
import re  # noqa: E402
for nm in [k for k in list(drafts) if re.search(r'-rfix\d*$', k)]:
    key = re.sub(r'-rfix\d*$', '', nm)
    base = {'kind': 'emulate', 'emulate': gate[nm].get('emulate'), 'published': gate[nm].get('published'), 'fixed': [gate[nm]['reviews']], 'lint': 'REVIEW'}
    B.para_items(key, REPO / gate[nm]['reviews'], dict(base, section='%dg %s (this batch)' % (num, nm)), 'checked with its edit (%s, this batch)' % nm,
                 seen, drafts, gate, preds, 'e')
g434 = json.loads((HERE / 'b434' / 'GATE.json').read_text(encoding='utf-8'))
g441 = json.loads((HERE / 'b441' / 'GATE.json').read_text(encoding='utf-8'))
g444 = json.loads((HERE / 'b444' / 'GATE.json').read_text(encoding='utf-8'))
REC = lambda key: (g434.get(key + '-fix') or g441.get(key + '-fix') or g444.get(key + '-fix') or {})
PLAN = [('HG31', HERE / 'rf-z' / 'HG31.v3.json', 'HG31-smp3', 'B34 fix kept, the B25 and B28 fixes let stand (457g: Human without all three, AI with B28\'s)')]
TAGS = {'HG31-smp3': 'z'}
CHANCE = {'HG31-smp3': 0.75}
for key, fx, name, why in PLAN:
    if not fx.exists():
        held.append((key, '%s not built yet' % rel(fx))); continue
    d = json.loads(fx.read_text(encoding='utf-8'))
    text = '\n\n'.join(p for u in d['units'] for p in u['paras'])
    files = sorted({u['file'] for u in d['units'] if u.get('file')})
    rec = REC(key)
    base = {'kind': 'emulate', 'emulate': (rec.get('emulate') or []) + [rel(f) for f in files if pathlib.Path(f).exists()],
            'published': rec.get('published'), 'fixed': [rel(fx)], 'lint': 'REVIEW'}
    drafts[name] = text
    gate[name] = dict(base)
    c = CHANCE.get(name, 0.72)
    preds[name] = ('Human' if c >= 0.5 else 'AI', c, why + ('; Joel\'s published paragraphs read AI in 429g as part of the section' if name.endswith('-pub') else
                                                          '; refix samples so far: 32 of 44 Human whole'))
    if '-dg' not in name:  # a diagnostic is screened whole only
        B.para_items(key, fx, dict(base, section='%dg %s (this batch)' % (num, name)), 'checked with its screen (%s, this batch)' % name,
                     seen, drafts, gate, preds, TAGS.get(name, 's'))
print(len(drafts), 'texts:', ' '.join(drafts))
print('held:', ' '.join('%s (%s)' % x for x in held) or '-')
if '--write' in sys.argv:
    intro = ('Pangram\'s web app. The chosen Emulate samples of the windows that read AI, each section screened whole with its triaged '
             'fixes and every paragraph not checked before in the same batch; HG33\'s edit. Predictions written before the run.')
    write_batch(HERE, num, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
