"""Section 13's side-by-side page for Joel: draft v6 beside the published section, with what Pangram said about the
v5 paragraphs it checked (batch 287g). v6 isn't in the article; the page reads it from a copy of the article with v6
in place of section 13 (page/article-with-v6.md). Run from the repo root:
  python3 articles/intentional-communities/candidate/s13/make_page_v6.py
"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
C = REPO / 'articles' / 'intentional-communities' / 'candidate'
S13 = C / 's13'
H = '# Your Little Forming Group Already Is the Community'
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
a = art.index(H); b = art.index('\n# ', a + 5)
v6 = (S13 / 'v6.md').read_text(encoding='utf-8').strip() + '\n'
tmp = S13 / 'page' / 'article-with-v6.md'
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
    [([1, 2], [1]), ([3], [2]), ([4, 5], [3]), ([6], [4])],
    [([1, 2], [1]), ([3], [2]), ([4], [3]), ([5, 6, 7], [4])],
    [([1, 2], [1]), ([3], [2]), ([4], [3]), ([5], [4]), ([6, 7], [5]), ([8], [6, 7]), ([9], [8]), ([10], [9])],
    [([1], [1]), ([2], [2]), ([3], [3]), ([4], [4])],
]
Bres = json.loads((C / 'fix-20261015b' / 'gui' / 'b287-results.json').read_text(encoding='utf-8'))
def res(k, what):
    x = Bres[k]
    lab = 'Human' if x['headline'] == 'Human Written' else 'AI'
    return 'Pangram on v5 %s: %s (%s; %d words), %s UTC: %s' % (what, lab, x['windows'][0].split(', ')[1].lower(), x['words'], x['utc'][11:19], x['link'])
CHECKED = {(0, 1): [res('S13v5-1P1P2', 'with the heading and the next paragraph')],
           (0, 2): [res('S13v5-1P2', 'alone')], (0, 3): [res('S13v5-1P3', 'alone')],
           (2, 2): [res('S13v5-3P2', 'alone')], (2, 3): [res('S13v5-3P3', 'alone')], (2, 4): [res('S13v5-3P4', 'alone')],
           (3, 6): [res('S13v5-4P6P7', 'with the next paragraph')], (3, 7): [res('S13v5-4P7', 'alone')],
           (3, 8): [res('S13v5-4P8', 'alone')], (4, 3): [res('S13v5-5P3', 'alone')]}
CHANGED_SINCE_V5 = {(0, 4), (1, 1), (1, 3), (1, 4), (2, 1), (3, 1), (3, 2), (3, 4), (3, 5), (3, 9), (4, 1), (4, 2), (4, 4)}
blocks = []
for hi, ((h, pps), (_, rps), m) in enumerate(zip(P, R, MAP)):
    rows = []
    for pp, rr in m:
        for j, r in enumerate(rr):
            start = ' '.join(re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', rps[r - 1]).split()[:6])
            notes = []
            if (hi, r) in CHECKED:
                notes += CHECKED[(hi, r)]
                if (hi, r) in CHANGED_SINCE_V5:
                    notes.append('Changed since that check (v6), not checked again yet.')
            else:
                notes.append('Not checked in Pangram yet (its v5 version had a gate flag; v6 has the fix).')
            row = {'label': '', 'article': start}
            if j == 0:
                row['source'] = [' '.join(re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', pps[k - 1]).split()[:5]) for k in pp]
            row['notes'] = notes
            rows.append(row)
    blocks.append({'headings': [h], 'rows': rows})
out = {'title': 'Your Little Forming Group Already Is the Community · section 13, draft v6 beside the published one',
       'meta': 'Community article · section 13 · draft v6, 2026-10-15 · not in the article yet',
       'intro': ['Your published section is on the left; my current draft (v6) is on the right. It is not in the article: '
                 'the article still has your published section 13.',
                 'Pangram, batch 287g: of the ten v5 paragraphs whose reviews came back clean, two read Human and eight '
                 'read AI-Generated. Each row says what Pangram said about its v5 version, with the check\'s link.',
                 'How the draft was made: Emulate\'s wording with every point of yours put back, then four review rounds '
                 '(meaning traces, cold reads, the stance check, the march read). The reviewers keep the meaning, but the '
                 'result reads AI. Question 31 on the questions page asks how you want to go on.'],
       'blocks': blocks}
mp = S13 / 'page' / 'ic13-v6.json'
mp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(C / 'community-section13-side-by-side.html'), '--article', str(tmp),
                    '--source', str(C.parent / 'original.md'), '--against-source'], capture_output=True, text=True)
print(r.returncode, (r.stdout + r.stderr)[-800:])
