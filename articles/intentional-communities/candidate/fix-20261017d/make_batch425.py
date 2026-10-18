"""Batch 425g (2026-10-17 night, after Joel's message of 23:10 UTC): his section 2 opening (52 a, with his 53 aside) and his section
8 sentence (54), each changed paragraph alone (50 words or more) and with each neighbor under its heading when one of the two is
under 50, and the sections whole in ptext's section() format: section 2 three ways (v3.5 as he pasted it; v3.5b with the anomie
paragraph after his P2; v3.5c with the anomie paragraph, his screenshot and caption, his 46 a), section 8 v32. Everything changed
is his words or his pick, so each part is an owner record; the anomie paragraph's own checks are 421g's (the same text). The
sections need their repeats checks (REPEATS-s2b.md, REPEATS-s8b.md). Run from candidate/: python3 fix-20261017d/make_batch425.py"""
import hashlib, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain, section  # noqa: E402

JOEL = 'Joel, 2026-10-17 23:10 UTC (joel-20261017/joel-20261017-2310-message.txt): '
SKIP = re.compile(r'^(\[image \d+\]|\[Professor Baby Sheep|Double click to interact with video|<!--)')
H2, H8 = '# Communes Are Hot Again', '# The Grown Children Get the Final Review'
G421 = json.loads((HERE / 'b421' / 'GATE.json').read_text(encoding='utf-8'))
D421 = json.loads((HERE / 'b421' / 'drafts.json').read_text(encoding='utf-8'))


def paras(md):
    out, h = [], 0
    for b in [b.strip() for b in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if b.strip()]:
        if b.startswith('#'):
            h += 1
            out.append((h, None, b))
        elif not SKIP.match(b) and not b.startswith('[caption]'):
            out.append((h, plain(b), b))
    return out


drafts, gate = {}, {}


def checks(name, sec_md, starts, joel):
    hp = paras(sec_md)
    i = next(k for k, (_, p, _) in enumerate(hp) if p and p.startswith(starts))
    rec = {'kind': 'owner', 'joel': JOEL + joel}
    ps = [p for _, p, _ in hp]
    keys = []
    if len(ps[i].split()) >= 50:
        drafts[name] = ps[i]; gate[name] = dict(rec); keys.append(name)
    for j in (i - 1, i + 1):
        if not (0 <= j < len(hp)) or hp[j][0] != hp[i][0]:
            continue
        if ps[j] is None:   # the heading over it, when the two reach Pangram's 50 words
            t = plain(hp[j][2].lstrip('#').strip()) + '\n\n' + ps[i]
            if len(t.split()) >= 50:
                drafts[name + '+head'] = t; gate[name + '+head'] = dict(rec); keys.append(name + '+head')
        elif min(len(ps[i].split()), len(ps[j].split())) < 50:
            a, b = sorted((i, j))
            k = '%s+%s' % (name, 'prev' if j < i else 'next')
            drafts[k] = ps[a] + '\n\n' + ps[b]; gate[k] = dict(rec); keys.append(k)
    return keys


J52 = ('52 "this is human" (his section 2 opening; the published link on "the U.S. Surgeon General" kept), with 53 "fixed (fact '
       'checked with gemini)" (his aside in P2)')
v35 = (HERE / 's2-v35.md').read_text(encoding='utf-8')
v35b = (HERE / 's2-v35b.md').read_text(encoding='utf-8')
v35c = (HERE / 's2-v35c.md').read_text(encoding='utf-8')
s8 = (HERE / 's8-v32.md').read_text(encoding='utf-8')
P = {}
P['a'] = checks('S2v35-P1', v35, 'Suddenly the longing to escape loneliness', J52) + checks('S2v35-P2', v35, 'Whether you want to call', J52)
P['b'] = checks('S2v35b-P1', v35b, 'Suddenly the longing to escape loneliness', J52) + checks('S2v35b-P2', v35b, 'Whether you want to call', J52)
P['c'] = checks('S2v35c-P1', v35c, 'Suddenly the longing to escape loneliness', J52) + checks('S2v35c-P2', v35c, 'Whether you want to call', J52)
P8 = checks('S8v32-truth', s8, 'Protecting children is the duty of adults', '54 "actually i would change it to: ..." (his sentence after "if '
            'they are known to be honest.")')
# the anomie paragraph's checks are 421g's (the same texts, asserted)
for k in ('S2v34-A46', 'S2v34-A46+next'):
    gate[k] = dict(G421[k], read='batch 421g (fix-20261017d/b421/b421-results.json)')
for md in (v35b, v35c):
    hp = [p for _, p, _ in paras(md)]
    j = hp.index(D421['S2v34-A46'])
    assert hp[j] + '\n\n' + hp[j + 1] == D421['S2v34-A46+next']
REP = {k: (HERE / ('REPEATS-%s.md' % k)) for k in ('s2b', 's8b')}
drafts['S2v35'] = section(v35, H2)
drafts['S2v35b'] = section(v35b, H2)
drafts['S2v35c'] = section(v35c, H2)
drafts['S8v32'] = section(s8, H8)
NOTE = 'fix-20261017d/DISPOSITIONS-2310.md (%s)'
for key, parts, rep in (('S2v35', P['a'], 'REPEATS-s2b.md'), ('S2v35b', P['b'] + ['S2v34-A46', 'S2v34-A46+next'], 'REPEATS-s2b.md'),
                        ('S2v35c', P['c'] + ['S2v34-A46', 'S2v34-A46+next'], 'REPEATS-s2b.md'), ('S8v32', P8, 'REPEATS-s8b.md')):
    gate[key] = {'kind': 'section', 'parts': ['installed'] + parts, 'repeats': 0, 'repeats_note': NOTE % rep}
for k in drafts:
    gate[k]['words'] = len(drafts[k].split())
seen, aliases = {}, {}
for k in list(drafts):
    if drafts[k] in seen:
        aliases[k] = seen[drafts[k]]; del drafts[k]
    else:
        seen[drafts[k]] = k
for k in gate:
    if gate[k]['kind'] == 'section':
        gate[k]['parts'] = list(dict.fromkeys(aliases.get(p, p) for p in gate[k]['parts']))
for k in aliases:
    del gate[k]
for k in drafts:
    print(k, gate[k]['words'], gate[k]['kind'], '|', drafts[k][:70].replace('\n', ' / '))
print('aliases:', aliases)
print(len(drafts), 'items,', sum(gate[k]['words'] for k in drafts), 'words')
ONLY2 = '--section2' in sys.argv   # section 2 first, while section 8's repeats check runs (section 8 goes in 426g)
if ONLY2:
    for k in [k for k in drafts if k.startswith('S8')]:
        del drafts[k]
if (ONLY2 and REP['s2b'].exists() or all(f.exists() for f in REP.values())) and (HERE / 'DISPOSITIONS-2310.md').exists():
    out = HERE / 'b425'
    out.mkdir(exist_ok=True)
    (out / 'aliases.json').write_text(json.dumps(aliases, indent=1) + '\n', encoding='utf-8')
    (out / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (out / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(out / 'drafts.json'),
                        str(out / 'GATE.json'), str(out / 'b425.js'), '--name', 'B425'] + list(drafts), capture_output=True, text=True)
    print(r.stdout[-1800:], r.stderr[-1500:])
    if r.returncode == 0:
        items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
        (out / 'b425-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
else:
    print('waiting for the repeats checks and their dispositions:', [str(f.name) for f in REP.values() if not f.exists()])
