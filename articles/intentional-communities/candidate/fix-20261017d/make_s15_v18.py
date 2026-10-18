"""Section 15 v18 (2026-10-17 night, Joel's 51 a: "make sure it reads well"): v17 (installed) without "So which is it? Well, in a
way, it's both." His new P1 already answers the paradise question ("No, not quite."), so asking it again two paragraphs on reads
as a recap (the repeats check of 21:37 flagged it, REPEATS-s15.md), and the next sentence says the "both" itself ("It's possible
for a society to be spiritually alive, generous, funny and super communal, while still becoming cruel to those who break its
social categories."). A cut, so the march labels go in the record and Pangram decides (pangram_gate.py, "cut_of"); the meaning
reviews still run first: march round r4 (both versions), and a cold read of the section with it (SENSE-PROMPT-s15d.txt).
Run from the repo root: python3 articles/intentional-communities/candidate/fix-20261017d/make_s15_v18.py"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

RV = str(REPO / 'tools' / 'humanization' / 'reviewer' / 'reviewer.py')
H15 = '# What This Looks Like From Sénégal'
OLD = 'So which is it? Well, in a way, it\'s both. It\'s possible for a society'
NEW = 'It\'s possible for a society'
v17 = (C / 's15' / 'v17.md').read_text(encoding='utf-8')
assert v17.count(OLD) == 1
v18 = v17.replace(OLD, NEW)
(C / 's15' / 'v18.md').write_text(v18, encoding='utf-8')
blocks = lambda md: [b.strip() for b in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if b.strip()]
pick = [(x, y) for x, y in zip(blocks(v17), blocks(v18)) if x != y]
assert len(pick) == 1
M = HERE / 'march-r4'
M.mkdir(exist_ok=True)
(M / 'march-in.md').write_text('\n\n'.join(plain(t) for t in pick[0]) + '\n', encoding='utf-8')
(M / 'march-ids.json').write_text(json.dumps(['s15-p3-was', 's15-p3-new'], indent=1) + '\n', encoding='utf-8')
subprocess.run([sys.executable, RV, 'march', str(M / 'march-in.md'), str(M / 'MARCH-PROMPT.txt'), '--style', str(C.parent / 'STYLE.json'),
                '--about', 'a friendly first-person article about starting an intentional community'], check=True)
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
a = art.index(H15)
m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', art[a + 3:])
assert re.sub(r'<!--.*?-->\n?', '', art[a:a + 3 + m.start()], flags=re.S).strip() == re.sub(r'<!--.*?-->\n?', '', v17, flags=re.S).strip()
(HERE / 'article-with-s15v18.md').write_text(art[:a] + v18.strip() + '\n' + art[a + 3 + m.start():], encoding='utf-8')
subprocess.run([sys.executable, RV, '--article', str(HERE / 'article-with-s15v18.md'), 'sense-section', str(HERE / 'SENSE-PROMPT-s15d.txt'),
                '--section', H15, '--report', str(HERE / 'SENSE-s15d.md')], check=True)
print('s15/v18.md, march-r4/MARCH-PROMPT.txt, SENSE-PROMPT-s15d.txt')
