"""Batch 428g (2026-10-18 night, after Joel's message of 01:29 UTC): section 2 with his 56 a first paragraph and his 55 b
aside, each changed paragraph alone (50 words or more) and with the heading over it, or with a neighbor when one of the two is
under 50, and the sections whole in ptext's section() format, three ways: v3.6 as he pasted it, v3.6b with the anomie paragraph
after his P2, v3.6c with the anomie paragraph, his screenshot and caption (his 46 a). Everything changed is his words or his
pick, so each part is an owner record; the anomie paragraph's own checks are 421g's (the same text, asserted). The sections
need their repeats check (REPEATS-s2c.md, answered in DISPOSITIONS-0129.md). Run from candidate/: python3 fix-20261018/make_batch428.py"""
import hashlib, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain, section  # noqa: E402

JOEL = 'Joel, 2026-10-18 01:29 UTC (joel-20261018/joel-20261018-0129-message.txt): '
SKIP = re.compile(r'^(\[image \d+\]|\[Professor Baby Sheep|Double click to interact with video|<!--)')
H2 = '# Communes Are Hot Again'
OLD = C / 'fix-20261017d'
G421 = json.loads((OLD / 'b421' / 'GATE.json').read_text(encoding='utf-8'))
D421 = json.loads((OLD / 'b421' / 'drafts.json').read_text(encoding='utf-8'))


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


J1 = '56 a "i checked the section, it passes as human when first part is this" (his first paragraph; the published link on "the U.S. Surgeon General" kept)'
J2 = '55 b (his aside in P2: "(the UN\'s rules for prisoners literally ban more than 15 days of it)")'
V = {k: (HERE / ('s2-%s.md' % k)).read_text(encoding='utf-8') for k in ('v36', 'v36b', 'v36c')}
P = {}
for k, name in (('v36', 'S2v36'), ('v36b', 'S2v36b'), ('v36c', 'S2v36c')):
    P[k] = checks(name + '-P1', V[k], 'Suddenly, the longing to escape loneliness', J1) + checks(name + '-P2', V[k], 'Whether you want to call', J2)
for k in ('S2v34-A46', 'S2v34-A46+next'):
    gate[k] = dict(G421[k], read='batch 421g (fix-20261017d/b421/b421-results.json)')
for k in ('v36b', 'v36c'):
    hp = [p for _, p, _ in paras(V[k])]
    j = hp.index(D421['S2v34-A46'])
    assert hp[j] + '\n\n' + hp[j + 1] == D421['S2v34-A46+next']
drafts['S2v36'] = section(V['v36'], H2)
drafts['S2v36b'] = section(V['v36b'], H2)
drafts['S2v36c'] = section(V['v36c'], H2)
NOTE = 'fix-20261018/DISPOSITIONS-0129.md (REPEATS-s2c.md; the rest as fix-20261017d/DISPOSITIONS-2310.md, REPEATS-s2b.md)'
for key, parts in (('S2v36', P['v36']), ('S2v36b', P['v36b'] + ['S2v34-A46', 'S2v34-A46+next']),
                   ('S2v36c', P['v36c'] + ['S2v34-A46', 'S2v34-A46+next'])):
    gate[key] = {'kind': 'section', 'parts': ['installed'] + parts, 'repeats': 0, 'repeats_note': NOTE}
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
if (HERE / 'REPEATS-s2c.md').exists() and (HERE / 'DISPOSITIONS-0129.md').exists():
    out = HERE / 'b428'
    out.mkdir(exist_ok=True)
    (out / 'aliases.json').write_text(json.dumps(aliases, indent=1) + '\n', encoding='utf-8')
    (out / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (out / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(out / 'drafts.json'),
                        str(out / 'GATE.json'), str(out / 'b428.js'), '--name', 'B428'] + list(drafts), capture_output=True, text=True)
    print(r.stdout[-1800:], r.stderr[-1500:])
    if r.returncode == 0:
        items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
        (out / 'b428-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
else:
    print('waiting for the repeats check and its dispositions (REPEATS-s2c.md, DISPOSITIONS-0129.md)')
