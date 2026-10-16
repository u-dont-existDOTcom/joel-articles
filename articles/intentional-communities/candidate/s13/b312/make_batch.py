"""Batch 312g (2026-10-16, Joel's message of 23:38 UTC): section 13 as installed (v31), every paragraph alone, and v31 with
his "if the community uses them" back in the budget questions.

Why: Joel, 23:38: "yes i want "if the community uses them" back in section 13. it's good to see that removing that one
thing is how you got it to human, that means it's all fairly borderline human. so we should fix it. ... no ai tells you
see, and it has human tells? isn't that part of the rules?" The rule is his of 2026-10-01 (docs/HUMANIZATION-GATE.md,
"Every paragraph passes alone"): a section that passes with a paragraph that fails alone doesn't count, because "usually
there are still ai tells you're missing in the paragraph". Section 13's paragraphs were checked in groups and as a whole,
never one by one. This batch finds the ones that fail alone (a paragraph under 50 words goes with the one before it), plus
the stretch that read AI in v30 (310g: the heading through H1-P3's first sentence) on its own.

Run from candidate/: python3 s13/b312/make_batch.py"""
import hashlib, json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
REPO = C.parents[2]
S13 = C / 's13'
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
HEADS = {0: 'H1', 5: 'H2', 11: 'H3', 17: 'H4', 27: 'H5'}


def load(name):
    bl = [b.strip() for b in re.split(r'\n\s*\n', (S13 / name).read_text(encoding='utf-8')) if b.strip()]
    assert len(bl) == len(IDS)
    return {(p or HEADS[i]): b for i, (p, b) in enumerate(zip(IDS, bl))}


V31 = load('v31.md')
OLD_Q = 'How long will your cash reserves last?'
NEW_Q = 'How long will your cash reserves last, if the community uses them?'
assert V31['H1-P4'].count(OLD_Q) == 1
V31Q = dict(V31, **{'H1-P4': V31['H1-P4'].replace(OLD_Q, NEW_Q)})
WHOLE = [(p or HEADS[i]) for i, p in enumerate(IDS)]
PARAS = [p for p in IDS if p]


def words(t):
    return len(re.findall(r'\w+', t))


ITEMS = {}
for i, p in enumerate(PARAS):
    # Pangram's 50-word minimum counts words split on spaces ("Don't" is one word): batch 312g's first run stopped at
    # H1-P1, 51 words by \w+ but 46 by spaces, with the button disabled
    if len(plain(V31[p]).split()) >= 50:
        ITEMS['S13v31-' + p] = ('v31', [p])
    elif i == 0 or PARAS[i - 1].split('-')[0] != p.split('-')[0]:
        nxt = PARAS[i + 1]
        ITEMS['S13v31-%s+%s' % (p, nxt.split('-')[1])] = ('v31', [p, nxt])
    else:
        prev = PARAS[i - 1]
        ITEMS['S13v31-%s+%s' % (prev, p.split('-')[1])] = ('v31', [prev, p])
first = V31['H1-P3'].split('. ')[0] + '.'
assert first.startswith('Until that’s happened') and first.endswith('yet.')
ITEMS['S13v31-open'] = ('v31', ['H1', 'H1-P1', 'H1-P2', 'H1-P3s1'])
ITEMS['S13v31q'] = ('v31q', WHOLE)
TEXT = {'v31': dict(V31, **{'H1-P3s1': first}), 'v31q': V31Q}

g31 = json.loads((S13 / 'install' / 'GATE-v31.json').read_text(encoding='utf-8'))
g304 = json.loads((S13 / 'b304' / 'GATE.json').read_text(encoding='utf-8'))
MARCH_Q = (g31['S13v31-H1']['march'] + g31['S13v31-H2']['march'] + g31['S13v31-H3']['march'] + g304['S13v26-H4']['march']
           + g31['S13v31-H5']['march'])


def lint(md):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


drafts, gate = {}, {}
for key, (way, parts) in ITEMS.items():
    md = [TEXT[way][p] for p in parts]
    drafts[key] = '\n\n'.join(plain(x) for x in md)
    if way == 'v31':
        gate[key] = {'kind': 'section', 'parts': ['installed'], 'repeats': 0,
                     'note': 'installed text (v31, s13/install/GATE-v31.json), checked alone for the every-paragraph rule',
                     'words': words(drafts[key])}
    else:
        gate[key] = {'kind': 'screen', 'march': MARCH_Q, 'lint': lint('\n\n'.join(x for x in md if not x.startswith('#'))),
                     'march_note': "v31's marches (GATE-v31.json; H4 from b304): the only change is five words at the end "
                                   "of one question in H1-P4, whose break (\"This is the boring stuff!\") stays",
                     'words': words(drafts[key])}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b312.js'), '--name', 'B312'] + list(ITEMS), capture_output=True, text=True)
print(r.stdout[-1500:], r.stderr[-1500:])
pool, defs = [], []
for k in ITEMS:
    idx = []
    for p in drafts[k].split('\n\n'):
        if p not in pool:
            pool.append(p)
        idx.append(pool.index(p))
    assert '\n\n'.join(pool[i] for i in idx) == drafts[k]
    defs.append([k, idx, hashlib.sha256(drafts[k].encode('utf-8')).hexdigest()])
(HERE / 'run312-compact.js').write_text('const P = ' + json.dumps(pool) + ';\nconst defs = ' + json.dumps(defs) +
                                        ';\nwindow.__run("B312", defs.map(([k, ix, s]) => [k, ix.map(i => P[i]).join("\\n\\n"), s])); "started"',
                                        encoding='utf-8')
print(len(ITEMS), {k: g['words'] for k, g in gate.items()})
