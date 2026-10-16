"""Section 13's side-by-side page for Joel: draft v22 beside the published section. Each paragraph v22 keeps from v21 shows
the check that read its exact text Human (s13/b298/COVERAGE.md); the paragraphs v22 rebuilt from Emulate round i say where
they are. v22 isn't in the article; the page reads it from a copy of the article with v22 in place of section 13
(page/article-with-v22.md). Run from the repo root:
  python3 articles/intentional-communities/candidate/s13/make_page_v22.py
"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
C = REPO / 'articles' / 'intentional-communities' / 'candidate'
S13 = C / 's13'
H = '# Your Little Forming Group Already Is the Community'
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
a = art.index(H); b = art.index('\n# ', a + 5)
v6 = (S13 / 'v22.md').read_text(encoding='utf-8').strip() + '\n'
tmp = S13 / 'page' / 'article-with-v22.md'
tmp.write_text(art[:a] + v6 + art[b:], encoding='utf-8')
orig = (C.parent / 'original.md').read_text(encoding='utf-8')
oa = orig.index(H); ob = orig.index('\n# ', oa + 5)

def paras(md):
    out, cur = [], None
    for x in [p.strip() for p in re.split(r'\n\s*\n', md) if p.strip()]:
        if x.startswith('#'):
            cur = x; out.append((cur, []))
        else:
            out[-1][1].append(x)
    return out
P = paras(orig[oa:ob]); R = paras(v6)
MAP = [
    [([1], [1]), ([2, 3], [2]), ([4, 5], [3]), ([6], [4])],
    [([1, 2], [1]), ([3], [2]), ([4], [3]), ([5], [4]), ([6], [5])],
    [([1, 2], [1]), ([3], [2]), ([4], [3]), ([5, 6], [4]), ([7], [5])],
    [([1, 2], [1]), ([3], [2]), ([4], [3]), ([5], [4]), ([6, 7], [5]), ([8], [6, 7]), ([9], [8]), ([10], [9])],
    [([1], [1]), ([2], [2]), ([3], [3]), ([4], [4])],
]
cov = (S13 / 'b298' / 'COVERAGE.md').read_text(encoding='utf-8')
COV = {}
for m in re.finditer(r'^\| (H\d-P\d+b?)[^|]*\| (\S+) \((\d+g)\) \| (\S+) \|', cov, re.M):
    COV[m.group(1)] = (m.group(2), m.group(3), m.group(4))
IDS = [['H1-P1', 'H1-P2', 'H1-P3', 'H1-P4'], ['H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4'],
       ['H3-P1', 'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5'],
       ['H4-P%d' % i for i in range(1, 10)], ['H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']]
NEW = {'H3-P1', 'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', 'H4-P9', 'H5-P1', 'H5-P2'}
R21 = 'https://www.pangram.com/history/0b7c2345-0629-47ef-b66a-75f5f9be2e22'
R22 = 'https://www.pangram.com/history/edf0cb54-e5f7-428f-8e37-253d2954eea1'
CHECKED = {}
for hi, ids in enumerate(IDS):
    for j, pid in enumerate(ids, start=1):
        if pid in NEW:
            run = R21 if pid.startswith('H3') else R22
            note = ('Rebuilt from a fresh Emulate version of the whole stretch (round i), after the stretch read 100% AI as a whole '
                    'though each of its paragraphs read Human alone: ' + run + '. Reviews done (round r15); their fixes come next, '
                    'then Pangram alone, the stretch, and the whole section.')
            if pid == 'H5-P2':
                note += ' A second way of this paragraph (from Emulate\'s other call) is in review too.'
            CHECKED[(hi, j)] = [note]
        else:
            key, batch, link = COV[pid]
            CHECKED[(hi, j)] = ['%s: reads Human (%s) %s' % (batch, key, link)]
blocks = []
for hi, ((h, pps), (_, rps), m) in enumerate(zip(P, R, MAP)):
    rows = []
    for pp, rr in m:
        for j, r in enumerate(rr):
            start = ' '.join(re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', rps[r - 1]).split()[:6])
            notes = []
            notes += CHECKED[(hi, r)]
            row = {'label': '', 'article': start}
            if j == 0:
                row['source'] = [' '.join(re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', pps[k - 1]).split()[:5]) for k in pp]
            row['notes'] = notes
            rows.append(row)
    blocks.append({'headings': [h], 'rows': rows})
out = {'title': 'Your Little Forming Group Already Is the Community · section 13, draft v22 beside the published one',
       'meta': 'Community article · section 13 · draft v22, 2026-10-15 · not in the article yet',
       'intro': ['Your published section is on the left; my draft (v22) is on the right. It is not in the article yet.',
                 'Where it stands: every paragraph and heading of v21 read Human on its own text, and the whole section read 56% '
                 'AI (https://www.pangram.com/history/5e450ea7-ed52-402b-bae4-de06d266aec7). Checked in stretches, the land '
                 'subsection read 100% AI as a whole (' + R21 + ') and so did the run from the visitors\' rights paragraph through '
                 'the removal questions (' + R22 + '), while other stretches moved with what surrounded them. v22 rebuilds those '
                 'two stretches from a fresh Emulate version of each stretch whole, with your meaning put back; their reviews '
                 'are done and their fixes come next. Rows the draft keeps from v21 show the check that read them Human.',
                 'What is Emulate\'s and what is mine: the sentence shapes are Emulate\'s; the words that carry your points back '
                 'are mine, and so are the breaks the march read asked for. Your own sentences are yours as you wrote them.'],
       'blocks': blocks}
mp = S13 / 'page' / 'ic13-v22.json'
mp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(C / 'community-section13-side-by-side.html'), '--article', str(tmp),
                    '--source', str(C.parent / 'original.md'), '--against-source'], capture_output=True, text=True)
print(r.returncode, (r.stdout + r.stderr)[-800:])
