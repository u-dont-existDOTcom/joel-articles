"""The reviews for make_tighten.py's changes (Joel's 48 a and 51 a of 2026-10-17 21:37 UTC), before any Pangram check:
- march-r1/: every changed paragraph before and after, for two fresh readers (a cut or rework that takes away a paragraph's only
  break leaves a run of steps, E173);
- TONE-PROMPT-tighten.txt: a fresh reader reads each change for how it sounds (his 51 a: "make sure it reads well");
- article-with-tighten.md: the article with this message's owner changes (article-with-drafts.md) and the tightened sections 13 v36,
  15 v16 and 16 v31 in place, and the cold reads of sections 13 and 15 (SENSE-PROMPT-s13.txt, SENSE-PROMPT-s15.txt). Section 16's
  one change is a capital, read by the march and the tone check.
Run from the repo root: python3 articles/intentional-communities/candidate/fix-20261017d/make_gate_tighten.py"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
sys.path.insert(0, str(HERE))
from ptext import plain  # noqa: E402
from make_tighten import CHANGES, SRC  # noqa: E402

RV = str(REPO / 'tools' / 'humanization' / 'reviewer' / 'reviewer.py')
HEAD = {'s13': '# Your Little Forming Group Already Is the Community', 's15': '# What This Looks Like From Sénégal',
        's16': '# Practice Comes Before Property'}
NAME = {'s13': 'Your Little Forming Group Already Is the Community', 's15': 'What This Looks Like From Sénégal',
        's16': 'Practice Comes Before Property'}


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if b.strip()]


pairs = []
for s, (src, dst) in SRC.items():
    a, b = blocks(src.read_text(encoding='utf-8')), blocks(dst.read_text(encoding='utf-8'))
    assert len(a) == len(b), s
    for x, y in zip(a, b):
        if x != y:
            pairs.append((s, x, y))
M = HERE / 'march-r1'
if not (M / 'MARCH-labels-a.txt').exists():
    M.mkdir(exist_ok=True)
    ids, texts = [], []
    for i, (s, x, y) in enumerate(pairs, 1):
        ids += ['%s-c%d-was' % (s, i), '%s-c%d-new' % (s, i)]
        texts += [plain(x), plain(y)]
    (M / 'march-in.md').write_text('\n\n'.join(texts) + '\n', encoding='utf-8')
    (M / 'march-ids.json').write_text(json.dumps(ids, indent=1) + '\n', encoding='utf-8')
    subprocess.run([sys.executable, RV, 'march', str(M / 'march-in.md'), str(M / 'MARCH-PROMPT.txt'), '--style',
                    str(C.parent / 'STYLE.json'), '--about', 'a friendly first-person article about starting an intentional community'],
                   check=True)
tone = ['You are helping a writer, Joel, tighten three sections of his long, conversational blog essay about building intentional '
        'communities. These sections were rewritten by an AI tool that pads (says a point twice, adds a filler line) and asks and '
        'answers its own questions ("So which is it? Well, in a way, it\'s both.", "Why bother?") or stresses words in capitals. '
        'Joel\'s instruction: "make sure it reads well ... lmk if you see anything that really looks weird". His voice: '
        'conversational, warm, blunt, funny, a little hippie; he writes like he talks.',
        '',
        'Below are %d changed paragraphs, each BEFORE and AFTER. For each, read the AFTER paragraph as a reader would and answer on one '
        'line: "Change N: FINE", or "Change N: WEIRD" with the sentence that now sounds off and why (flat where it should be lively, '
        'a gap where something was cut, a lost point, a sentence that doesn\'t follow) and a better fix that keeps the change\'s aim. '
        'Don\'t comment on anything else in the paragraphs.' % len(pairs),
        '',
        'Write your answer to %s with a single Write call (at most 400 words), then reply with only the lines that aren\'t FINE.'
        % (HERE / 'TONE-tighten.md'), '']
for i, (s, x, y) in enumerate(pairs, 1):
    tone += ['### Change %d (section "%s")' % (i, NAME[s]), '', 'BEFORE:', x, '', 'AFTER:', y, '']
(HERE / 'TONE-PROMPT-tighten.txt').write_text('\n'.join(tone), encoding='utf-8')
art = (HERE / 'article-with-drafts.md').read_text(encoding='utf-8')
for s, (src, dst) in SRC.items():
    a = art.index(HEAD[s])
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', art[a + 3:])
    old = re.sub(r'<!--.*?-->\n?', '', art[a:a + 3 + m.start()], flags=re.S).strip()
    assert old == re.sub(r'<!--.*?-->\n?', '', src.read_text(encoding='utf-8'), flags=re.S).strip(), s
    art = art[:a] + dst.read_text(encoding='utf-8').strip() + '\n' + art[a + 3 + m.start():]
(HERE / 'article-with-tighten.md').write_text(art, encoding='utf-8')
for s in ('s13', 's15'):
    subprocess.run([sys.executable, RV, '--article', str(HERE / 'article-with-tighten.md'), 'sense-section',
                    str(HERE / ('SENSE-PROMPT-%s.txt' % s)), '--section', HEAD[s], '--report', str(HERE / ('SENSE-%s.md' % s))], check=True)
print(len(pairs), 'changed paragraphs:', ', '.join('%s c%d' % (s, i) for i, (s, _, _) in enumerate(pairs, 1)))
