"""Section 13's side-by-side page for Joel: v32, now in the article, beside the published section (2026-10-17), each
paragraph with the Pangram check that read its exact text alone (Joel's rule of 2026-10-01; batches 312g and 314g) and, where
v32 changed it, what changed and why (v32-fixes.json). Run from the repo root:
  python3 articles/intentional-communities/candidate/s13/make_page_v32.py
"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
C = REPO / 'articles' / 'intentional-communities' / 'candidate'
S13 = C / 's13'
sys.path.insert(0, str(C / 'tools'))
import page_checks  # noqa: E402

H = '# Your Little Forming Group Already Is the Community'
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
v32 = (S13 / 'v32.md').read_text(encoding='utf-8').strip() + '\n'
assert v32.strip() in art, 'install v32 first (s13/install/install_s13_v32.py)'
orig = (C.parent / 'original.md').read_text(encoding='utf-8')
oa = orig.index(H); ob = orig.index('\n# ', oa + 5)


def paras(md):
    out = []
    for x in [p.strip() for p in re.split(r'\n\s*\n', md) if p.strip()]:
        if x.startswith('#'):
            out.append((x, []))
        else:
            out[-1][1].append(x)
    return out


P = paras(orig[oa:ob]); R = paras(v32)
MAP = [
    [([1], [1]), ([2, 3], [2]), ([4, 5], [3]), ([6], [4])],
    [([1, 2], [1]), ([3], [2]), ([4], [3]), ([5], [4]), ([6], [5])],
    [([1, 2], [1]), ([3], [2]), ([4, 5, 6], [3, 4]), ([7], [5])],
    [([1, 2], [1]), ([3], [2]), ([4], [3]), ([5], [4]), ([6, 7], [5]), ([8], [6, 7]), ([9], [8]), ([10], [9])],
    [([1], [1]), ([2], [2]), ([3], [3]), ([4], [4])],
]
checks = page_checks.alone(v32, [S13 / 'b314', S13 / 'b312'])
CHECK = {p: g for p, g in checks}
fixes = json.loads((S13 / 'v32-fixes.json').read_text(encoding='utf-8'))
v31 = [x.strip() for x in re.split(r'\n\s*\n', (S13 / 'v31.md').read_text(encoding='utf-8')) if x.strip()]
WHY = {}
for f in fixes:
    WHY.setdefault(f['id'], []).append(f['why'])
IDS = [['H1-P1', 'H1-P2', 'H1-P3', 'H1-P4'], ['H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4'],
       ['H3-P1', 'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5'], ['H4-P%d' % i for i in range(1, 10)], ['H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']]
r314 = json.loads((S13 / 'b314' / 'b314-results.json').read_text(encoding='utf-8'))
whole = r314['S13v32']
WHOLE = 'https://www.pangram.com/history' + whole[5]
start = lambda t: ' '.join(re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', t).split()[:6])
blocks = []
for hi, ((h, pps), (_, rps), m) in enumerate(zip(P, R, MAP)):
    rows = []
    for pp, rr in m:
        for j, r in enumerate(rr):
            text = rps[r - 1]
            pid = IDS[hi][r - 1]
            g = CHECK.get(text) or []
            notes = [page_checks.note(g[0])] if g else ['no check of this text alone yet']
            if text not in v31:
                notes += ['Changed this turn: ' + '; '.join(WHY.get(pid, ['see v32-fixes.json']))]
            row = {'label': '', 'article': start(text), 'notes': notes}
            if j == 0:
                row['source'] = [start(pps[k - 1])[:60] for k in pp]
            rows.append(row)
    blocks.append({'headings': [h], 'rows': rows})
out = {'title': 'Your Little Forming Group Already Is the Community · section 13 (v32, in the article) beside the published one',
       'meta': 'Community article · section 13 · v32, 2026-10-17 · in the article, not accepted until you say so',
       'intro': ['Your published section is on the left; v32, now in the article, is on the right. Each row shows the check that read '
                 'that paragraph alone (your rule: every paragraph passes alone), and what changed this turn.',
                 'The whole section reads %s (314g, %s words, AI likelihood %.2f): %s' % (whole[0].replace(' Written', ''),
                                                                                                  whole[2], whole[1], WHOLE),
                 'What changed since your 23:38 message: your "if the community uses them" is back in the budget questions (with your '
                 'words the section read Human; my own rewording had been the trouble); the short visit lost its "congratulations" '
                 'punchline, the one paragraph that read AI alone; the book is recommended for the nuts and bolts, not for its order; '
                 'the repeats are cut where another place says the point better; and seven phrases readers kept stopping at are plainer.'],
       'blocks': blocks}
mp = S13 / 'page' / 'ic13-v32.json'
mp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(C / 'community-section13-side-by-side.html'), '--article', str(C / 'HUMANIZED-SO-FAR.md'),
                    '--source', str(C.parent / 'original.md'), '--against-source'], capture_output=True, text=True)
print(r.returncode, (r.stdout + r.stderr)[-800:])
