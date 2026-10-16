"""Batch 298g (2026-10-15, after Joel's 32 b): section 13 whole, draft v21, after every paragraph has a Human check on its
own text. This first finds, for each paragraph and heading of v21, the Pangram check that covers it: a Human reading of
exactly that text alone (a paragraph under 50 words: in a pair whose other paragraph reads Human alone; a heading: over its
first paragraph), from batches 287g to 297g. It stops if any part has none. The section's repeats are answered in
s13/review-r12/DISPOSITIONS-r12.md (E172), with v20 and v21 carrying the fixes. Writes COVERAGE.md, drafts.json and
GATE.json (the parts' own gate records copied from their batches). Run from candidate/: python3 s13/b298/make_batch.py
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
S13 = C / 's13'
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain, section  # noqa: E402

H = '# Your Little Forming Group Already Is the Community'
BATCHES = [('287g', C / 'fix-20261015b', 'gui/b287-results.json')] + [
    ('%dg' % n, S13 / ('b%d' % n), 'b%d-results.json' % n) for n in range(288, 298)]
texts, gates, res, where = {}, {}, {}, {}
for name, d, rf in BATCHES:
    dr = json.loads((d / 'drafts.json').read_text(encoding='utf-8'))
    gt = json.loads((d / 'GATE.json').read_text(encoding='utf-8'))
    rs = json.loads((d / rf).read_text(encoding='utf-8'))
    for k, v in dr.items():
        texts[k] = v['text'] if isinstance(v, dict) else v
        gates[k] = gt.get(k)
        where[k] = name
    for k, v in rs.items():
        human = v.get('headline') == 'Human Written' or str(v.get('result', '')).replace('*', '').startswith('Human')
        res[k] = (human, v.get('link'), v.get('words'))

v21 = (S13 / 'v21.md').read_text(encoding='utf-8')
blocks = [b.strip() for b in re.split(r'\n\s*\n', v21) if b.strip()]
IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1', 'H3-P2',
       'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8', 'H4-P9', None,
       'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
assert len(IDS) == len(blocks)
P = [(i, pid, plain(b)) for i, (pid, b) in enumerate(zip(IDS, blocks))]


def passing(text):
    """keys whose checked text is exactly this and read Human, latest batch first"""
    ks = [k for k, t in texts.items() if t == text and res.get(k, (False,))[0]]
    return sorted(ks, key=lambda k: where[k], reverse=True)


rows, parts, missing = [], [], []
for n, (i, pid, t) in enumerate(P):
    if pid is None:   # a heading: over its first paragraph (the section's own heading, over the first two)
        nxt = P[n + 1][2] if pid is None and n + 1 < len(P) else ''
        cands = passing(t + '\n\n' + nxt) or passing(t + '\n\n' + nxt + '\n\n' + P[n + 2][2])
        label = 'heading "%s"' % t
    else:
        cands = passing(t)
        label = pid
        if len(t.split()) < 50 or not cands:
            prev = P[n - 1][2] if n > 0 and P[n - 1][1] else None
            nxt = P[n + 1][2] if n + 1 < len(P) and P[n + 1][1] else None
            pair = (passing(prev + '\n\n' + t) if prev else []) + (passing(t + '\n\n' + nxt) if nxt else [])
            if len(t.split()) < 50:
                cands = pair
                label += ' (under 50 words: with a neighbor)'
    if not cands:
        missing.append(label)
        rows.append('| %s | none | |' % label)
        continue
    k = cands[0]
    parts.append(k)
    rows.append('| %s | %s (%s) | %s |' % (label, k, where[k], res[k][1]))
cov = ('# Section 13 v21: the check that covers each part (built by make_batch.py)\n\n'
       'Each row: a paragraph or heading of v21, and the latest Pangram check that read exactly its text Human.\n\n'
       '| part | check | link |\n|---|---|---|\n' + '\n'.join(rows) + '\n')
(HERE / 'COVERAGE.md').write_text(cov, encoding='utf-8')
print(cov)
if missing:
    sys.exit('not covered: ' + ', '.join(missing))
art = (S13 / 'review-r12' / 'article-with-v19.md')
full = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
a = full.index(H); b = full.index('\n# ', a + 5)
article = full[:a] + v21.strip() + '\n' + full[b:]
sec = section(article, H)
drafts = {'S13v21': sec}
gate = {}
for k in dict.fromkeys(parts):
    drafts[k] = texts[k]
    gate[k] = gates[k]
for k in list(gate):   # a part whose stance or grounding is "same claims as KEY" needs KEY's record beside it
    for f in ('stance', 'grounding'):
        v = gate[k].get(f)
        if isinstance(v, str) and v.startswith('same claims as '):
            ref = v[len('same claims as '):]
            gate.setdefault(ref, gates[ref])
gate['S13v21'] = {'kind': 'section', 'parts': list(dict.fromkeys(parts)), 'repeats': 0,
                  'repeats_note': 's13/review-r12/REPEATS.md (the repeats check with the section in place) answered in '
                                  's13/review-r12/DISPOSITIONS-r12.md; the fixes in v20 and v21 passed rounds r13 and r14'}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('S13v21:', len(sec.split()), 'words;', len(gate['S13v21']['parts']), 'parts')
