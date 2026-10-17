"""Batch 417g (2026-10-17 evening): the second round after 415g. 415g read these AI: section 2's P2 alone with the published
"starving" (0.60; Emulate's "starvin'" had held it) and so section 2 whole; section 15's "No, not that either." with its
neighbor (0.34); section 16's inner pl/ork paragraph without "That's it!" with the next one (0.88); and section 16 whole
(0.35), across "Less cinematic, I know." and "in one go." and across the inner pl/ork paragraph's end. Each of those changes
is taken back (make_excl.py, make_faithful.py) and its paragraph goes to Joel (question 47); section 2 stays as installed.
This batch reads what's left: section 16's money paragraph ("!" back, "by declaring" kept) alone and with the paragraph before
it, its "change how people survive" paragraph with the installed inner pl/ork paragraph, sections 15 and 16 whole as they now
stand, and section 2 with the anomie paragraph on its installed P2 (a screen, question 46).
Run from candidate/: python3 fix-20261017b/make_batch417.py"""
import hashlib, json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain, section  # noqa: E402

SKIP = re.compile(r'^(\[image \d+\]|\[Professor Baby Sheep|Double click to interact with video|<!--)')
NEW = (HERE / 'article-with-drafts.md').read_text(encoding='utf-8')
ANOM = (HERE / 'anomie' / 'article-with-anomie.md').read_text(encoding='utf-8')
G415 = json.loads((HERE / 'b415' / 'GATE.json').read_text(encoding='utf-8'))
R415 = json.loads((HERE / 'b415' / 'b415-results.json').read_text(encoding='utf-8'))
D415 = json.loads((HERE / 'b415' / 'drafts.json').read_text(encoding='utf-8'))


def own_whole(md):
    out = []
    for b in [b.strip() for b in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if b.strip()]:
        if SKIP.match(b):
            continue
        if b.startswith('[caption]'):
            b = re.sub(r'^\[caption\]\s*', '', b)
        out.append(plain(b.lstrip('#').strip()))
    return '\n\n'.join(out)


def block(md, h1):
    a = md.index(h1)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', md[a + 3:])
    return md[a:(a + 3 + m.start()) if m else len(md)]


def paras(md):
    out, h = [], 0
    for b in [b.strip() for b in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if b.strip()]:
        if b.startswith('#'):
            h += 1
        elif not SKIP.match(b) and not b.startswith('[caption]'):
            out.append((h, plain(b), b))
    return out


def lint(md_text):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md_text + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name, '--style',
                        str(C.parent / 'STYLE.json')], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


drafts, gate = {}, {}


def checks(name, sec_md, starts, rec):
    hp = paras(sec_md)
    i = next(k for k, (_, p, _) in enumerate(hp) if p.startswith(starts))
    ps = [p for _, p, _ in hp]
    if len(ps[i].split()) >= 50:
        drafts[name] = ps[i]; gate[name] = dict(rec, lint=lint(hp[i][2]), words=len(ps[i].split()))
    for j in (i - 1, i + 1):
        if 0 <= j < len(ps) and hp[j][0] == hp[i][0] and min(len(ps[i].split()), len(ps[j].split())) < 50:
            a, b = sorted((i, j))
            k = '%s+%s' % (name, 'prev' if j < i else 'next')
            drafts[k] = ps[a] + '\n\n' + ps[b]
            gate[k] = dict(rec, lint=lint(hp[i][2]), words=len(drafts[k].split()))


M4 = [dict(re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', (HERE / 'march-r4' / ('MARCH-labels-%s.txt' % x)).read_text(), re.M)) for x in 'ab']
s16 = block(NEW, '# Practice Comes Before Property')
rec = dict(G415['S16v29-H1P3'], march_was=[M4[0]['1'], M4[1]['1']], march=[M4[0]['2'], M4[1]['2']],
           march_note='fix-20261017b/march-r4 (the installed paragraph and this one)',
           grounding_note='no claim of mine: the published "declaring" for "because" (REPORT-FOREST.md [2]); its "!" as installed')
checks('S16v29b-H1P3', s16, 'Same with money', rec)
rec = dict(G415['S16v29-H2P4+next'])
checks('S16v29b-H2P4', s16, 'A group that practices together weekly', rec)
# keep only what 415g didn't already read Human (a pair whose exact text read Human there stays a 415g part)
for k in list(drafts):
    old = next((k2 for k2, t in D415.items() if t == drafts[k]), None)
    if old and R415[old][0].startswith('Human'):
        gate[old] = G415[old]
        del drafts[k], gate[k]
drafts['S16v29b'] = own_whole(s16)
drafts['S15v14b'] = own_whole(block(NEW, '# What This Looks Like From Sénégal'))
hp16 = {p for _, p, _ in paras(s16)}
hp15 = {p for _, p, _ in paras(block(NEW, '# What This Looks Like From Sénégal'))}
# the 415g parts whose text is still in the section and read Human
p16 = sorted(k for k in R415 if k.startswith('S16v29-') and R415[k][0].startswith('Human') and all(x in hp16 for x in D415[k].split('\n\n')))
p15 = sorted(k for k in R415 if k.startswith('S15v14-') and R415[k][0].startswith('Human') and all(x in hp15 for x in D415[k].split('\n\n')))
for k in p16 + p15:
    gate[k] = G415[k]
gate['S16v29b'] = {'kind': 'section', 'parts': ['installed'] + p16 + sorted(k for k in drafts if k.startswith('S16v29b-')),
                   'repeats': 0, 'repeats_note': 'fix-20261017b/DISPOSITIONS.md (the take-backs change nothing said twice)'}
gate['S15v14b'] = {'kind': 'section', 'parts': ['installed'] + p15, 'repeats': 0,
                   'repeats_note': 'fix-20261017b/DISPOSITIONS.md (the take-back changes nothing said twice)'}
# the anomie paragraph in section 2 as installed ("starvin'" stays until question 47)
MA = [dict(re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', (HERE / 'anomie' / ('MARCH-v2-labels-%s.txt' % x)).read_text(), re.M)) for x in 'ab']
drafts['S2-A46b'] = section(ANOM, '# Communes Are Hot Again')
gate['S2-A46b'] = {'kind': 'screen', 'march': [MA[0]['1'], MA[1]['1']], 'march_note': 'fix-20261017b/anomie/MARCH-v2-labels-a.txt and -b.txt (T1)',
                   'lint': G415['A46']['lint'], 'lint_note': G415['S2-A46']['lint_note']}
for k in gate:
    if k in drafts:
        gate[k].setdefault('words', len(drafts[k].split()))
out = HERE / 'b417'
out.mkdir(exist_ok=True)
(out / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(out / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(out / 'drafts.json'),
                    str(out / 'GATE.json'), str(out / 'b417.js'), '--name', 'B417'] + list(drafts), capture_output=True, text=True)
print(r.stdout[-900:], r.stderr[-1500:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(out / 'b417-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
for k in drafts:
    print(k, len(drafts[k].split()), gate[k]['kind'], gate[k].get('lint'), drafts[k][:60].replace('\n', ' / '))
print('parts 16:', p16); print('parts 15:', p15)
