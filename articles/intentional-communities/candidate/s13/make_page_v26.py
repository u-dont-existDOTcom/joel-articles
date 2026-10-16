"""Section 13's side-by-side page for Joel: draft v26 beside the published section, after batch 304g (2026-10-16). Each
paragraph v26 keeps from v21 shows the check that read its exact text Human (s13/b298/COVERAGE.md); each paragraph changed since
v21 shows the 304g group that read it Human, and the subsection notes say which stretches still read AI. v26 isn't in the
article; the page reads it from a copy of the article with v26 in place of section 13 (page/article-with-v26.md). Run from the
repo root:
  python3 articles/intentional-communities/candidate/s13/make_page_v26.py
"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
C = REPO / 'articles' / 'intentional-communities' / 'candidate'
S13 = C / 's13'
H = '# Your Little Forming Group Already Is the Community'
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
a = art.index(H); b = art.index('\n# ', a + 5)
v6 = (S13 / 'v26.md').read_text(encoding='utf-8').strip() + '\n'
tmp = S13 / 'page' / 'article-with-v26.md'
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
R304 = json.loads((S13 / 'b304' / 'b304-results.json').read_text(encoding='utf-8'))
GROUP = {'H1-P1': 'S13v26-1hP1P2', 'H1-P4': 'S13v26-1P3P4', 'H2-P2': 'S13v26-2P1P2', 'H3-P1': 'S13v26-3P1P2',
         'H3-P2': 'S13v26-3P1P2', 'H3-P3': 'S13v26-3P3', 'H3-P4': 'S13v26-3P4P5', 'H3-P5': 'S13v26-3P4P5',
         'H4-P2': 'S13v26-4P1P2', 'H4-P6': 'S13v26-4P6P7', 'H4-P7': 'S13v26-4P6P7', 'H4-P9': 'S13v26-4P9h5P2',
         'H5-P1': 'S13v26-4P9h5P2', 'H5-P2': 'S13v26-4P9h5P2'}
def says(key):
    r = R304[key]
    return '304g: %s (%s) %s' % (r['headline'].replace(' Written', ''), key, r['link'])
CHECKED = {}
for hi, ids in enumerate(IDS):
    for j, pid in enumerate(ids, start=1):
        if pid in GROUP:
            note = [says(GROUP[pid])]
            if pid == 'H5-P2':
                note.append('Way B of this paragraph, the casual one (in v26b): ' + says('S13v26b-4P9h5P2'))
            CHECKED[(hi, j)] = note
        else:
            key, batch, link = COV[pid]
            CHECKED[(hi, j)] = ['%s: reads Human (%s) %s' % (batch, key, link)]
SUBNOTE = {2: 'The land subsection as a whole: ' + says('S13v26-H3') + ' (it read 100% AI before, in 299g).',
           3: 'The visitor subsection as a whole: AI over its first 173 words (the heading and the first two paragraphs), Human over the other 536: ' + R304['S13v26-H4']['link'] + '. Its first two paragraphs read Human alone (the row above).',
           4: 'The last subsection as a whole reads AI, both ways: ' + R304['S13v26-H5']['link'] + ' and ' + R304['S13v26b-H5']['link'] + '. Its first three paragraphs read Human with the paragraph before them (the rows above), so what it adds is the last two paragraphs, unchanged since 10-15, which read Human alone. Question 34.'}
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
            if j == len(rr) - 1 and (pp, rr) == m[-1] and hi in SUBNOTE:
                notes = notes + [SUBNOTE[hi]]
            row['notes'] = notes
            rows.append(row)
    blocks.append({'headings': [h], 'rows': rows})
out = {'title': 'Your Little Forming Group Already Is the Community · section 13, draft v26 beside the published one',
       'meta': 'Community article · section 13 · draft v26, 2026-10-16 · not in the article yet',
       'intro': ['Your published section is on the left; my draft (v26) is on the right. It is not in the article yet.',
                 'Where it stands after this pass (batch 304g): every group that holds a paragraph changed since 10-15 reads Human, '
                 'the land subsection reads Human as a whole, and the stretch from the visitors\' rights paragraph through the '
                 'removal questions reads Human both ways. The whole section reads AI over 38% of its words (56% before): '
                 'https://www.pangram.com/history/9a7c5448-ae59-47ba-9133-72b1a8c76673, in two long stretches, from "Until that\'s '
                 'happened" through the values subsection and from "But if the person is endangering everyone else" to the end, and '
                 'the last two sentences of the visitors\' rights paragraph. Question 34 on the questions page asks what next. Each '
                 'row shows the check that read its text Human.',
                 'Changed this turn: "How do you know?" is cut (your 18:22 message), "Long list, huh?" puts back the break the values '
                 'paragraph lost, and "a budget of", "All of them" and "Six months will give you more data" are plain wording for '
                 'phrases two or more readers paused at.',
                 'What is Emulate\'s and what is mine: the sentence shapes in the land subsection and the removal stretch are '
                 'Emulate\'s; the words that carry your points back are mine, and so are the breaks the march read asked for. Your '
                 'own sentences are yours as you wrote them.'],
       'blocks': blocks}
mp = S13 / 'page' / 'ic13-v26.json'
mp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(C / 'community-section13-side-by-side.html'), '--article', str(tmp),
                    '--source', str(C.parent / 'original.md'), '--against-source'], capture_output=True, text=True)
print(r.returncode, (r.stdout + r.stderr)[-800:])
