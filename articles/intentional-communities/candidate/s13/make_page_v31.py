"""Section 13's side-by-side page for Joel: v31, now in the article, beside the published section (2026-10-16). The
paragraphs of the first, second, third and last subsections show the check that read their subsection Human with its exact
text (309g for the first, whose text is v29's; 310g for the others); the visitor subsection, unchanged since v26, keeps the
checks of 304g and b298/COVERAGE.md; the whole section is 311g's. Run from the repo root:
  python3 articles/intentional-communities/candidate/s13/make_page_v31.py
"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
C = REPO / 'articles' / 'intentional-communities' / 'candidate'
S13 = C / 's13'
H = '# Your Little Forming Group Already Is the Community'
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
a = art.index(H); b = art.index('\n# ', a + 5)
v6 = (S13 / 'v31.md').read_text(encoding='utf-8').strip() + '\n'
tmp = S13 / 'page' / 'article-with-v31.md'
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
R308 = json.loads((S13 / 'b308' / 'b308-results.json').read_text(encoding='utf-8'))
R309 = json.loads((S13 / 'b309' / 'b309-results.json').read_text(encoding='utf-8'))
R310 = json.loads((S13 / 'b310' / 'b310-results.json').read_text(encoding='utf-8'))
R311 = json.loads((S13 / 'b311' / 'b311-results.json').read_text(encoding='utf-8'))
def says(r, key, batch):
    conf = r['windows'][0].split(', ')[1].lower() if len(r['windows']) == 1 else 'high'
    return '%s: %s (%s, %s, %d words) %s' % (batch, r['headline'].replace(' Written', ''), key, conf, r['words'], r['link'])
SUBCHECK = {0: says(R309['S13v29-H1'], 'S13v29-H1, the same text in v31', '309g'), 1: says(R310['S13v30-H2'], 'S13v30-H2, the same text in v31', '310g'),
            2: says(R310['S13v30-H3'], 'S13v30-H3, the same text in v31', '310g'), 4: says(R310['S13v30-H5'], 'S13v30-H5, the same text in v31', '310g')}
GROUP4 = {'H4-P2': 'S13v26-4P1P2', 'H4-P6': 'S13v26-4P6P7', 'H4-P7': 'S13v26-4P6P7', 'H4-P9': 'S13v26-4P9h5P2'}
CHECKED = {}
for hi, ids in enumerate(IDS):
    for j, pid in enumerate(ids, start=1):
        if hi in SUBCHECK:
            CHECKED[(hi, j)] = ['Its subsection as a whole, %s' % SUBCHECK[hi]]
        elif pid in GROUP4:
            r = R304[GROUP4[pid]]
            CHECKED[(hi, j)] = ['304g: %s (%s) %s' % (r['headline'].replace(' Written', ''), GROUP4[pid], r['link'])]
        else:
            key, batch, link = COV[pid]
            CHECKED[(hi, j)] = ['%s: reads Human (%s) %s' % (batch, key, link)]
SUBNOTE = {3: 'The visitor subsection, unchanged since 10-16 18:22: read alone, its first 173 words read AI (304g, ' + R304['S13v26-H4']['link'] + '); inside the whole section all of it reads Human (311g, ' + R311['S13v30a']['link'] + ').'}
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
out = {'title': 'Your Little Forming Group Already Is the Community · section 13 (v31, in the article) beside the published one',
       'meta': 'Community article · section 13 · v31, 2026-10-16 · in the article, not accepted until you say so',
       'intro': ['Your published section is on the left; v31, now in the article, is on the right.',
                 'The whole section reads 100% Human, high (311g, 2,324 words, AI likelihood 0.10): ' + R311['S13v30a']['link'] + '. '
                 'Before this turn it read 38% AI (304g). Each row shows the check that read its text Human.',
                 'What changed since your 21:05 message (34 a): Emulate rewrote the two long stretches that read AI, each sent whole. '
                 'Where I put your meaning back by rebuilding the published sentence, the AI came back (the last subsection read 0.84 '
                 'AI, https://www.pangram.com/history/9589c085-6585-4321-9fbb-37b809262f16); put back inside Emulate\'s own sentences, it '
                 'read 0.00 (' + R308['S13v28-H5']['link'] + '). Then the meaning reviews: 21 trace items and 2 stance conflicts, '
                 'fixed in a few words each; a second round of traces found nothing more to fix.',
                 'One fix I left out, kept unless you say otherwise: the budget paragraph asks "How long will your cash reserves last?" '
                 'without your "if the community uses them". Adding ", if you have any?" brought back two AI stretches in the whole '
                 'section (' + R310['S13v30']['link'] + ').',
                 'What is Emulate\'s and what is mine: the sentence shapes in the rewritten stretches are Emulate\'s; the words that '
                 'carry your points back are mine, and so are the breaks the march read asked for. Your own sentences are yours as '
                 'you wrote them.'],
       'blocks': blocks}
mp = S13 / 'page' / 'ic13-v31.json'
mp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(C / 'community-section13-side-by-side.html'), '--article', str(tmp),
                    '--source', str(C.parent / 'original.md'), '--against-source'], capture_output=True, text=True)
print(r.returncode, (r.stdout + r.stderr)[-800:])
