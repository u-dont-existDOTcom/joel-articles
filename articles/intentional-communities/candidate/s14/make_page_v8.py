"""Section 14's side-by-side page for Joel: v8, now in the article, beside the published section (2026-10-17), each paragraph
with the Pangram check that read its exact text alone (batches 315g and 313g, and 305g-x and 306g for text unchanged since
v5), the whole section's check (316g), and what the dedup changed. v8 is v7 with v5's P2: both shorter versions of P2 read
AI alone (313g, 315g). Run from the repo root:
  python3 articles/intentional-communities/candidate/s14/make_page_v8.py"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
C = REPO / 'articles' / 'intentional-communities' / 'candidate'
S14 = C / 's14'
sys.path.insert(0, str(C / 'tools'))
import page_checks  # noqa: E402

v8 = (S14 / 'v8.md').read_text(encoding='utf-8')
assert v8.strip() in (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'), 'install v8 first (s14/install/install_s14_v8.py)'
pub = [b.strip() for b in re.split(r'\n\s*\n', (S14 / 'v0.md').read_text(encoding='utf-8')) if b.strip() and not b.startswith(('#', '[image'))]
new = [b.strip() for b in re.split(r'\n\s*\n', v8) if b.strip() and not b.startswith(('#', '[image'))]
assert len(pub) == 7 and len(new) == 6
checks = {p: g for p, g in page_checks.alone(v8, [S14 / 'b315', S14 / 'b313', S14 / 'b306', S14 / 'b305'])}
r316 = json.loads((C / 's13' / 'b316' / 'b316-results.json').read_text(encoding='utf-8'))
w = r316['S14v8']
CHANGED = {
    1: 'Kept as in v5, with one repeat: the seventh question asks again about "people\'s food, housing and care", which the '
       'fourth and fifth questions already ask. Both versions without the repeat read AI alone: six words out (313g, AI '
       'likelihood 0.78, https://www.pangram.com/history/3ac9ccfc-bc5a-4080-bfab-993bf61feb65) and the list as short statements '
       '(315g, 0.96, https://www.pangram.com/history/da77a942-f71b-48de-b843-453427682fee). Question 38 on the questions page '
       'asks you.',
    4: 'Changed: your last paragraph ("Even after the community ends as a legal entity, some of what people learned to give one '
       'another may go on.") said this paragraph\'s opening again, so its own part is in the first sentence here, and the '
       'section ends on your father. "The Farm\'s communal economy" says whose economy (two readers stopped at it).',
}
start = lambda t: ' '.join(re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', t).split()[:6])
SRC = {0: [0], 1: [1], 2: [2], 3: [3], 4: [4, 6], 5: [5]}
rows = []
for i, t in enumerate(new):
    g = checks.get(t) or []
    rows.append({'label': '', 'article': start(t), 'source': [start(pub[k]) for k in SRC[i]],
                 'notes': ([page_checks.note(g[0])] if g else ['no check of this text alone yet']) + ([CHANGED[i]] if i in CHANGED else [])})
out = {'title': 'Dissolution and Exit · section 14, v8 beside the published one',
       'meta': 'Community article · section 14 · v8, 2026-10-17 · in the article, not accepted until you say so',
       'intro': ['Your published section is on the left; v8, now in the article, is on the right, deduplicated as you asked at 23:38. '
                 'Each row shows the check that read that paragraph alone.',
                 'The whole section reads %s (316g, %s words, AI likelihood %.2f): https://www.pangram.com/history%s'
                 % (w[0].replace(' Written', ''), w[2], w[1], w[5]),
                 'The four short breaks ("Who would?", "That\'s a lot of loose ends!", "Who wants that?", "(as you may have noticed!)") '
                 'are mine; question 37 on the questions page asks whether they\'re you.'],
       'blocks': [{'headings': ['# Dissolution and Exit'], 'rows': rows}]}
mp = S14 / 'page' / 'ic14-v8.json'
mp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(C / 'community-section14-side-by-side.html'), '--article', str(C / 'HUMANIZED-SO-FAR.md'),
                    '--source', str(C.parent / 'original.md'), '--against-source'], capture_output=True, text=True)
print(r.returncode, (r.stdout + r.stderr)[-800:])
