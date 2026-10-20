"""Install section 2 v3.6b after batch 428g (2026-10-18): Joel's 01:29 first paragraph (56 a) and aside (55 b), and after his
P2 the anomie paragraph (his 46 a). 428g read the paragraphs Human alone and with their neighbors and the section 100% Human
with the anomie paragraph (S2v36b); with his screenshot and caption as well (S2v36c), it read one AI window, 63 words in the
Instagram paragraphs, so the screenshot stays in section 12, as at 23:10 (v3.5b). Then the ledger, the evidence runs and the
ideas file. Idempotent. Run from candidate/: python3 fix-20261018/install_428.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
A = C.parent
ART = C / 'HUMANIZED-SO-FAR.md'
H2 = '# Communes Are Hot Again'
R = json.loads((HERE / 'b428' / 'b428-results.json').read_text(encoding='utf-8'))
link = lambda k: 'https://www.pangram.com/history' + R[k][5]
ok = lambda k: R[k][0] == 'Human Written' and '; AI' not in R[k][3] and not R[k][3].startswith('AI')
G = json.loads((HERE / 'b428' / 'GATE.json').read_text(encoding='utf-8'))
assert ok('S2v36b') and all(ok(p) for p in G['S2v36b']['parts'] if p in R), 'S2v36b did not pass'
assert not ok('S2v36c')
new = (HERE / 's2-v36b.md').read_text(encoding='utf-8').strip()
md = ART.read_text(encoding='utf-8')
if new not in md:
    a = md.index(H2)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', md[a + 3:])
    md = md[:a] + new + '\n' + md[a + 3 + m.start():]
    i = md.index('<!-- CANDIDATE: section 2 v3.6 (')
    note = ('<!-- CANDIDATE: section 2 v3.6b (2026-10-18, after Joel\'s message of 01:29 UTC (joel-20261018/joel-20261018-0129-message.txt, '
            '56 a and 55 b) and his 46 a of 21:37): v3.6 with the anomie paragraph after his P2. Pangram web app (428g): his first '
            'paragraph Human alone (%s) and with the heading (%s), his P2 Human alone (%s) and with the next (%s), the whole section '
            '100%% Human (%s). With his screenshot and caption there as well, one AI window, 63 words in the Instagram paragraphs '
            '(%s), so the screenshot stays in section 12. Records: fix-20261018/. Before: -->\n'
            % (link('S2v36-P1'), link('S2v36-P1+head'), link('S2v36-P2'), link('S2v36-P2+next'), link('S2v36b'), link('S2v36c')))
    md = md[:i] + note + md[i:]
    ART.write_text(md, encoding='utf-8')
    print('section 2 v3.6b installed')
else:
    print('section 2 v3.6b already in')

p = C / 'OWNER-EDITS.json'
raw = p.read_text(encoding='utf-8')
d = json.loads(raw)
E = {e['id']: e for e in d['entries']}
e = E['s2-joel-20261018-0129-56a-55b']
if '428g' not in e['what']:
    e['what'] = e['what'].replace('; my checks (batch 428g) wait on Pangram.',
                                  '. Pangram 428g: his first paragraph Human alone and with the heading, his P2 Human alone and with the '
                                  'next, the section 100% Human with the anomie paragraph (v3.6b).')
e = E['s2-joel-20261017-2137-46a']
if e['status'] != 'applied':
    e['status'] = 'applied'
    e['what'] += (' In at 01:56 UTC on the 18th with his 01:29 first paragraph (428g, S2v36b): the anomie paragraph; the screenshot stays '
                  'in section 12 (with it, 428g read one AI window, S2v36c).')
    e.pop('waits_for', None)
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if raw.endswith('\n') else ''), encoding='utf-8')

F = A / 'DETECTOR-EVIDENCE.json'
raw = F.read_text(encoding='utf-8')
ev = json.loads(raw)
V = 'v3.6b (2026-10-18)'
if not any(r.get('section') == 2 and r.get('version') == V for r in ev['runs']):
    ev['runs'].append({'section': 2, 'version': V,
                       'passage': 'section 2 as installed in articles/intentional-communities/candidate/HUMANIZED-SO-FAR.md',
                       'service': 'Pangram web app (dashboard)',
                       'record': 'CANDIDATE: section 2 with Joel\'s 01:29 first paragraph and aside and the anomie paragraph (46 a); every '
                                 'changed paragraph Human alone and with its neighbor, the whole section 100%% Human (%d words, AI likelihood '
                                 '%.2f, %s UTC, %s).' % (R['S2v36b'][2], R['S2v36b'][1], R['S2v36b'][4], link('S2v36b'))})
    F.write_text(json.dumps(ev, ensure_ascii=False, indent=1) + ('\n' if raw.endswith('\n') else ''), encoding='utf-8')

u = A / 'UNINCORPORATED-IDEAS.md'
t = u.read_text(encoding='utf-8')
o = 'Disposition: waiting on question 52.'
if o in t:
    u.write_text(t.replace(o, 'Disposition: in, 2026-10-18 01:56 UTC, after his own first paragraph for section 2 (56 a) made the section read '
                              '100% Human with it (batch 428g); his screenshot stays in section 12 (with it, one AI window).'), encoding='utf-8')
print('ledger, evidence, ideas written')
