"""The reviews for section 13 v35 (Joel's 19:14 UTC "i agree with your excl 13 14 ideas"; make_s13_v35.py):
- march-r1/: every changed paragraph before and after (its "-was" and "-new"), for two fresh readers: a cut or a mark that was
  the paragraph's only break would leave a run of steps (E173), and that paragraph goes back to him;
- article-with-s13v35.md: HUMANIZED-SO-FAR.md with v35 in place of v34, and SENSE-PROMPT-s13.txt, the cold read of the section.
No stance or grounding review: no position or claim changes (marks and three filler phrases out, his decision).
Run from the repo root: python3 articles/intentional-communities/candidate/fix-20261017c/make_gate.py"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
sys.path.insert(0, str(HERE))
from ptext import plain  # noqa: E402
from make_s13_v35 import CHANGES  # noqa: E402

RV = str(REPO / 'tools' / 'humanization' / 'reviewer' / 'reviewer.py')
H13 = '# Your Little Forming Group Already Is the Community'
V34 = (C / 's13' / 'v34.md').read_text(encoding='utf-8')
V35 = (C / 's13' / 'v35.md').read_text(encoding='utf-8')


def blocks(md):
    """(subsection, paragraph number under it, text) for every paragraph; the opening is "Opening"."""
    out, h, n = [], 'Opening', 0
    for b in [b.strip() for b in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if b.strip()]:
        if b.startswith('## '):
            h, n = b[3:].strip(), 0
        elif b.startswith('# '):
            continue
        else:
            n += 1
            out.append((h, n, b))
    return out


SHORT = {'Please Choose the Values Before Falling in Love With the View': 'Values', 'Resources, Land, and Exit Terms': 'Resources',
         'From Visitor to Member—Slowly': 'Visitor to Member', 'When Somebody Has to Go': 'When Somebody Has to Go', 'Opening': 'Opening'}
B34, B35 = blocks(V34), blocks(V35)
assert [(h, n) for h, n, _ in B34] == [(h, n) for h, n, _ in B35]
changed = []
for (h, n, a), (_, _, b) in zip(B34, B35):
    if a != b:
        where = '%s P%d' % (SHORT[h], n)
        assert any(c[0] == where for c in CHANGES), where
        changed.append((where, a, b))
assert {w for w, _, _ in changed} == {c[0] for c in CHANGES}
if (HERE / 'march-r1' / 'MARCH-labels-a.txt').exists():
    # round r1 was read (on the first v35, with the three changes make_s13_v35.py now holds back); its prompt and ids stay
    print('march-r1 was read already; not rewritten'); raise SystemExit(0)
ids, texts = [], []
for where, a, b in changed:
    mid = 's13-' + where.replace(' ', '')
    ids += [mid + '-was', mid + '-new']
    texts += [plain(a), plain(b)]
M = HERE / 'march-r1'
M.mkdir(exist_ok=True)
(M / 'march-in.md').write_text('\n\n'.join(texts) + '\n', encoding='utf-8')
(M / 'march-ids.json').write_text(json.dumps(ids, indent=1) + '\n', encoding='utf-8')
subprocess.run([sys.executable, RV, 'march', str(M / 'march-in.md'), str(M / 'MARCH-PROMPT.txt'), '--style',
                str(C.parent / 'STYLE.json'), '--about', 'a friendly first-person article about starting an intentional community'],
               check=True)
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
a = art.index(H13)
m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', art[a + 3:])
b = a + 3 + m.start()
assert re.sub(r'<!--.*?-->\n?', '', art[a:b], flags=re.S).strip() == re.sub(r'<!--.*?-->\n?', '', V34, flags=re.S).strip()
(HERE / 'article-with-s13v35.md').write_text(art[:a] + V35.strip() + '\n' + art[b:], encoding='utf-8')
subprocess.run([sys.executable, RV, '--article', str(HERE / 'article-with-s13v35.md'), 'sense-section',
                str(HERE / 'SENSE-PROMPT-s13.txt'), '--section', H13, '--report', str(HERE / 'SENSE-s13.md')], check=True)
print(len(changed), 'changed paragraphs:', ', '.join(w for w, _, _ in changed))
