"""Section 14's side-by-side page for Joel: v7, now in the article, beside the published section (2026-10-17), each paragraph
with the Pangram check that read its exact text alone (batches 313g and 315g, and 305g-x and 306g for text unchanged since
v5), and what the dedup changed. Run from the repo root:
  python3 articles/intentional-communities/candidate/s14/make_page_v7.py"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
C = REPO / 'articles' / 'intentional-communities' / 'candidate'
S14 = C / 's14'
sys.path.insert(0, str(C / 'tools'))
import page_checks  # noqa: E402

v7 = (S14 / 'v7.md').read_text(encoding='utf-8')
assert v7.strip() in (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'), 'install v7 first (s14/install/install_s14_v7.py)'
pub = [b.strip() for b in re.split(r'\n\s*\n', (S14 / 'v0.md').read_text(encoding='utf-8')) if b.strip() and not b.startswith(('#', '[image'))]
new = [b.strip() for b in re.split(r'\n\s*\n', v7) if b.strip() and not b.startswith(('#', '[image'))]
assert len(pub) == 7 and len(new) == 6
checks = {p: g for p, g in page_checks.alone(v7, [S14 / 'b315', S14 / 'b313', S14 / 'b306', S14 / 'b305'])}
r315 = json.loads((S14 / 'b315' / 'b315-results.json').read_text(encoding='utf-8'))
w = r315['S14v7']
CHANGED = {
    1: 'Changed this turn: the second question about food, housing and care is gone (the first questions ask it); the outside cash '
       'or benefits keep their place. With that one out, eight questions in a row read AI alone (313g, '
       'https://www.pangram.com/history/3ac9ccfc-bc5a-4080-bfab-993bf61feb65), so the last items are short statements now, every '
       'item kept.',
    4: 'Changed this turn: your last paragraph ("Even after the legal entity ends, some of what people learned to give one '
       'another may continue.") said this paragraph\'s opening again, so its own part is in the first sentence here, and the '
       'section ends on your father. "The Farm\'s communal economy" says whose economy (two readers stopped at it).',
}
start = lambda t: ' '.join(re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', t).split()[:6])
SRC = {0: [0], 1: [1], 2: [2], 3: [3], 4: [4, 6], 5: [5]}
rows = []
for i, t in enumerate(new):
    g = checks.get(t) or []
    rows.append({'label': '', 'article': start(t), 'source': [start(pub[k]) for k in SRC[i]],
                 'notes': ([page_checks.note(g[0])] if g else ['no check of this text alone yet']) + ([CHANGED[i]] if i in CHANGED else [])})
out = {'title': 'Dissolution and Exit · section 14, v7 beside the published one',
       'meta': 'Community article · section 14 · v7, 2026-10-17 · in the article, not accepted until you say so',
       'intro': ['Your published section is on the left; v7, now in the article, is on the right, deduplicated as you asked at 23:38. '
                 'Each row shows the check that read that paragraph alone.',
                 'The whole section reads %s (315g, %s words, AI likelihood %.2f): https://www.pangram.com/history%s'
                 % (w[0].replace(' Written', ''), w[2], w[1], w[5]),
                 'The four short breaks ("Who would?", "That\'s a lot of loose ends!", "Who wants that?", "(as you may have noticed!)") '
                 'are mine; question 37 on the questions page asks whether they\'re you.'],
       'blocks': [{'headings': ['# Dissolution and Exit'], 'rows': rows}]}
mp = S14 / 'page' / 'ic14-v7.json'
mp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(C / 'community-section14-side-by-side.html'), '--article', str(C / 'HUMANIZED-SO-FAR.md'),
                    '--source', str(C.parent / 'original.md'), '--against-source'], capture_output=True, text=True)
print(r.returncode, (r.stdout + r.stderr)[-800:])
