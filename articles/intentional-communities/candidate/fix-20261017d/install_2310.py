"""Install Joel's texts of 2026-10-17 23:10 UTC (make_2310.py) where batch 425g read them Human: section 2 with his opening in the
fullest form that passed (v3.5c: with the anomie paragraph and his screenshot and caption, his 46 a, and then section 12 v16
without them; else v3.5b, the anomie paragraph without the screenshot; else v3.5, as he pasted it), and section 8 v32 (his 54
sentence, checked in 427g after its repeats check). A section goes in only if Pangram read it whole Human with no AI window and every check of its changed paragraphs Human
(the anomie paragraph's own checks are 421g's). Idempotent. Run from candidate/: python3 fix-20261017d/install_2310.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
ART = C / 'HUMANIZED-SO-FAR.md'
R = {}
for b in ('b421', 'b425', 'b427'):
    if not (HERE / b / ('%s-results.json' % b)).exists():
        continue
    r = json.loads((HERE / b / ('%s-results.json' % b)).read_text(encoding='utf-8'))
    al = HERE / b / 'aliases.json'
    for k, v in (json.loads(al.read_text()) if al.exists() else {}).items():
        r.setdefault(k, r[v])
    R.update(r)
G = json.loads((HERE / 'b425' / 'GATE.json').read_text(encoding='utf-8'))
if (HERE / 'b427' / 'GATE.json').exists():   # section 8 went in 427g, after its repeats check
    G.update(json.loads((HERE / 'b427' / 'GATE.json').read_text(encoding='utf-8')))
ok = lambda k: k in R and R[k][0].startswith('Human') and R[k][3].startswith('Human') and '; AI' not in R[k][3]
link = lambda k: 'https://www.pangram.com/history' + R[k][5]
good = lambda key: ok(key) and all(ok(p) for p in G[key]['parts'] if p != 'installed')
J = 'Joel\'s message of 23:10 UTC (joel-20261017/joel-20261017-2310-message.txt'
H2, H8, H12 = '# Communes Are Hot Again', '# The Grown Children Get the Final Review', '# The Math of Absorption, and Who This Isn’t For'
S2 = next((k for k in ('S2v35c', 'S2v35b', 'S2v35') if good(k)), None)
WHAT = {
    'S2v35c': 'his opening and, after his P2, the anomie paragraph (his 46 a of 21:37) with his screenshot and caption, moved here from section 12',
    'S2v35b': 'his opening and, after his P2, the anomie paragraph (his 46 a of 21:37); his screenshot stays in section 12 (with it, 425g read the section AI)',
    'S2v35': 'his opening as he pasted it; the anomie paragraph (his 46 a) waits (with it, 425g read the section AI)',
}
SECT = []
if S2:
    SECT.append((S2, H2, HERE / {'S2v35c': 's2-v35c.md', 'S2v35b': 's2-v35b.md', 'S2v35': 's2-v35.md'}[S2], '<!-- CANDIDATE: section 2 v3.2',
                 'CANDIDATE', 'section 2 v3.5%s (2026-10-17, after %s, 52 a and 53): %s; his P1 ("Suddenly the longing to escape '
                 'loneliness which inspired my father\'s movie ...") with the published link on "the U.S. Surgeon General" kept, his P2 '
                 'with his aside "(it\'s literally listed in the UN Convention Against Torture)" (question 55 asks about its source)'
                 % ({'S2v35c': 'c', 'S2v35b': 'b', 'S2v35': ''}[S2], J, WHAT[S2])))
if S2 == 'S2v35c':
    SECT.append(('S12v16', H12, HERE / 's12-v16.md', '<!-- CANDIDATE: section 12 v15', 'CANDIDATE',
                 'section 12 v16 (2026-10-17, after %s, with his 46 a of 21:37): v15 without the screenshot and its caption, which moved '
                 'to section 2' % J))
SECT.append(('S8v32', H8, HERE / 's8-v32.md', '<!-- CANDIDATE: section 8 v31', 'CANDIDATE',
             'section 8 v32 (2026-10-17, after %s, 54): his sentence after "Make sure kids understand what they say will be taken '
             'seriously if they are known to be honest.": "And those who are known to lie a lot are especially targeted by abusers who '
             'know their accusations won\'t be believed."' % J))
md = ART.read_text(encoding='utf-8')
for key, h1, path, old_note, word, what in SECT:
    if key != 'S12v16' and not good(key):
        print(key, 'not installed'); continue
    new = path.read_text(encoding='utf-8').strip()
    if new in md:
        print(key, 'already in'); continue
    a = md.index(h1)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', md[a + 3:])
    md = md[:a] + new + '\n' + md[a + 3 + m.start():]
    i = md.index(old_note)
    src = {'S12v16': '421g', 'S8v32': '427g'}.get(key, '425g')
    note = ('<!-- %s: %s. Pangram web app (%s): every changed paragraph Human alone or with its neighbor, the whole section %s (%s). '
            'Records: fix-20261017d/. Before: -->\n' % (word, what, src, R[key][0].replace(' Written', ''), link(key)))
    md = md[:i] + note + md[i:]
    print(key, 'installed')
ART.write_text(md, encoding='utf-8')
print('section 2:', S2)
