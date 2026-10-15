"""Section 13's side-by-side page for Joel: draft v13 beside the published section, with what Pangram said about each
paragraph (batches 287g to 292g). v13 isn't in the article; the page reads it from a copy of the article with v13 in
place of section 13 (page/article-with-v13.md). Run from the repo root:
  python3 articles/intentional-communities/candidate/s13/make_page_v13.py
"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
C = REPO / 'articles' / 'intentional-communities' / 'candidate'
S13 = C / 's13'
H = '# Your Little Forming Group Already Is the Community'
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
a = art.index(H); b = art.index('\n# ', a + 5)
v6 = (S13 / 'v13.md').read_text(encoding='utf-8').strip() + '\n'
tmp = S13 / 'page' / 'article-with-v13.md'
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
R_ = {}
for b in ('fix-20261015b/gui/b287-results.json', 's13/b288/b288-results.json', 's13/b289/b289-results.json',
          's13/b290/b290-results.json', 's13/b291/b291-results.json', 's13/b292/b292-results.json'):
    R_.update(json.loads((C / b).read_text(encoding='utf-8')))
def res(k, what, batch):
    x = R_[k]
    if 'result' in x:
        head, _, rest = x['result'].replace('**', '').partition(' (')
        conf = rest.split(';')[0].split(', ')[-1] if 'AI Detected' not in rest else 'two windows'
        return '%s, %s: %s (%s) %s' % (batch, what, head, conf, x['link'])
    lab = 'Human' if x['headline'] == 'Human Written' else 'AI'
    return '%s, %s: %s (%s; %d words) %s' % (batch, what, lab, x['windows'][0].split(', ')[1].lower(), x['words'], x['link'])
CHECKED = {
 (0, 1): [res('S13v12-1P1P2', 'with the next paragraph', '292g'), res('S13v12-1hP1P2', 'with the heading and the next paragraph', '292g'),
          'Under 50 words: it counts once the next paragraph reads Human alone.'],
 (0, 2): [res('S13v12-1P2', 'alone', '292g'), res('S13v9-1P2', 'alone, the version before', '289g'),
          'Next: a fresh Emulate version, the way the other paragraphs passed.'],
 (0, 3): [res('S13v5-1P3', 'alone', '287g')], (0, 4): [res('S13v9-1P4', 'alone', '290g')],
 (1, 1): [res('S13v9-2P1', 'alone', '289g'), res('S13v9-2P1h', 'with its heading', '289g')],
 (1, 2): [res('S13v10-2P1P2', 'with the paragraph before', '291g')], (1, 3): [res('S13v10-2P3', 'alone', '291g')],
 (1, 4): [res('S13v10-2P3P3b', 'with the paragraph before', '291g'), res('S13v10-2P3bP4', 'with the next paragraph', '291g')],
 (1, 5): [res('S13v10-2P4', 'alone', '291g')],
 (2, 1): [res('S13v12-3P1', 'alone', '292g'), res('S13v12-3hP1', 'with its heading', '292g'), 'The heading over it is next.'],
 (2, 2): [res('S13v5-3P2', 'alone', '287g')],
 (2, 3): ['Fixed after the reviews of round r9 (v13); its reviews come next, then Pangram.'],
 (2, 4): [res('S13v9-3P4', 'alone', '289g')], (2, 5): [res('S13v9-3P4P5', 'with the paragraph before', '289g')],
 (3, 1): [res('S13v6-4P1', 'alone', '288g'), res('S13v6-4P1h', 'with its heading', '288g')],
 (3, 2): [res('S13v9-4P2', 'alone', '290g'), res('S13v9-4P1P2', 'after The Farm', '290g')],
 (3, 3): [res('S13v9-4P3P4', 'with the next paragraph', '290g')], (3, 4): [res('S13v9-4P4', 'alone', '289g')],
 (3, 5): [res('S13v9-4P5', 'alone', '290g')], (3, 6): [res('S13v9-4P6', 'alone', '289g')],
 (3, 7): [res('S13v12-4P7', 'alone', '292g')],
 (3, 8): ['Its meaning reviews are clean; the march read keeps finding no break, so v13 gives it a new one. Reviews next.'],
 (3, 9): [res('S13v9-4P9', 'alone', '290g')],
 (4, 1): [res('S13v12-5P1', 'alone', '292g'), res('S13v12-5hP1', 'with its heading', '292g')],
 (4, 2): [res('S13v10-5P2', 'alone, the version before', '291g'), 'Rebuilt from a fresh Emulate version (round f), fixed after round r9; reviews next.'],
 (4, 3): ['Fixed after round r9; reviews next. The aside about your research is question 32 (my pick: cut it).'],
 (4, 4): [res('S13v10-5P4', 'alone, the version before', '291g'), 'Rebuilt from a fresh Emulate version (round f), fixed after round r9; reviews next.'],
}
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
out = {'title': 'Your Little Forming Group Already Is the Community · section 13, draft v13 beside the published one',
       'meta': 'Community article · section 13 · draft v13, 2026-10-15 · not in the article yet',
       'intro': ['Your published section is on the left; my draft (v13) is on the right. It is not in the article yet.',
                 'How it was made, after your 31 a: each paragraph that read AI went to Emulate again, your meaning was put '
                 'back word by word, the reviews ran, and each paragraph went to Pangram as soon as its own reviews were '
                 'clear. 20 of the 27 paragraphs now read Human, each row with its check. The other seven are in review or '
                 'going to a fresh Emulate version; then the headings and the whole section.',
                 'What is Emulate\'s and what is mine: the sentence shapes are Emulate\'s; the words that carry your points '
                 'back are mine, and so are the breaks the march read asked for (asides like "(Hopefully not all at '
                 'once!)" and "It\'s boring stuff, I know.").'],
       'blocks': blocks}
mp = S13 / 'page' / 'ic13-v13.json'
mp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(C / 'community-section13-side-by-side.html'), '--article', str(tmp),
                    '--source', str(C.parent / 'original.md'), '--against-source'], capture_output=True, text=True)
print(r.returncode, (r.stdout + r.stderr)[-800:])
