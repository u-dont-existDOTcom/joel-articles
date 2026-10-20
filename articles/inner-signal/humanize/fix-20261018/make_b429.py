"""Batch 429g (2026-10-18, after Joel's 01:29 UTC "let's move onto the next article in the queue to humanize from emulate's
work"): the hypnosis guide's baseline, every h1 section as it stands in his Substack paste of 2026-09-28, before anything is
rewritten. The queue (articles/inner-child-therapy/experiments/emulate-20260929/ARTICLES.md, #2) says the baseline decides
which paragraphs get rewritten: "Paragraphs that already read Human in the Pangram baseline stay exactly as they are."
A section under 50 words goes with the next one (Pangram's reads under 50 words aren't reliable); the guide's opening line
goes with the first section. Run from humanize/: python3 fix-20261018/make_b429.py"""
import hashlib, json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
import sections as S  # noqa: E402

MD = H / 'HUMANIZED-SO-FAR.md'
SRC = H / 'source' / 'published-20260928.md'
ED = H / 'source' / 'substack-editor-20260928.html'
sha = lambda b: hashlib.sha256(b).hexdigest()
assert MD.read_bytes() == SRC.read_bytes(), 'the working copy has changed since the baseline; this batch is the published text'
SOURCE = ('source/published-20260928.md, SHA-256 %s (his Substack editor HTML of 2026-09-28, source/substack-editor-20260928.html, '
          'SHA-256 %s, as Markdown)' % (sha(SRC.read_bytes()), sha(ED.read_bytes())))

secs = S.sections(MD.read_text(encoding='utf-8'), ED)
assert secs[0][0] is None and len(secs) == 41
groups, i = [], 0
opening = secs[0][1]
secs = secs[1:]
while i < len(secs):
    g = [i]
    while sum(len(S.text_of(secs[k][1]).split()) for k in g) < 50 and g[-1] + 1 < len(secs):
        g.append(g[-1] + 1)
    groups.append(g)
    i = g[-1] + 1
drafts, gate, order = {}, {}, []
for g in groups:
    key = 'HG%02d' % (g[0] + 1) + ''.join('+%02d' % (k + 1) for k in g[1:])
    blocks = (opening if g[0] == 0 else []) + [b for k in g for b in secs[k][1]]
    drafts[key] = S.text_of(blocks)
    gate[key] = {'kind': 'baseline', 'source': SOURCE, 'words': len(drafts[key].split()),
                 'headings': [S.plain(secs[k][0]) for k in g]}
for k in drafts:
    print('%-10s %5d words  %s' % (k, gate[k]['words'], ' / '.join(gate[k]['headings'])[:90]))
print(len(drafts), 'items,', sum(g['words'] for g in gate.values()), 'words')
out = HERE / 'b429'
out.mkdir(exist_ok=True)
(out / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(out / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(out / 'drafts.json'),
                    str(out / 'GATE.json'), str(out / 'b429.js'), '--name', 'B429'] + list(drafts), capture_output=True, text=True)
print(r.stdout[-1200:], r.stderr[-1200:])
if r.returncode == 0:
    items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
    (out / 'b429-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
    print('items sha', sha((out / 'b429-items.json').read_bytes()))
