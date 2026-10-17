"""The lane's records after Joel's message of 2026-10-17 23:10 UTC (52 to 54, and the scorecard), from what install_2310.py put
in: the owner-edits ledger, the evidence runs, the unincorporated ideas, the STATUS.md entry (newest on top) and the current
state. Idempotent. Run from candidate/ after install_2310.py (and promote.py, if 45 a ran): python3 fix-20261017d/records_2310.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
A = C.parent
R = {}
for b in ('b421', 'b425'):
    r = json.loads((HERE / b / ('%s-results.json' % b)).read_text(encoding='utf-8'))
    al = HERE / b / 'aliases.json'
    for k, v in (json.loads(al.read_text()) if al.exists() else {}).items():
        r.setdefault(k, r[v])
    R.update(r)
link = lambda k: 'https://www.pangram.com/history' + R[k][5]
rec = lambda k: '%d words, AI likelihood %.2f, %s UTC, %s' % (R[k][2], R[k][1], R[k][4], link(k))
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
inn = lambda f: (HERE / f).read_text(encoding='utf-8').strip() in art
S2 = next((k for k, f in (('S2v35c', 's2-v35c.md'), ('S2v35b', 's2-v35b.md'), ('S2v35', 's2-v35.md')) if inn(f)), None)
S8 = inn('s8-v32.md')
PROMOTED = (A / 'master.md').exists() and (A / 'PROMOTION-RECEIPT-20261017.md').exists()
WHEN = '2026-10-17 23:10 UTC (joel-20261017/joel-20261017-2310-message.txt)'

# the ledger
p = C / 'OWNER-EDITS.json'
raw = p.read_text(encoding='utf-8')
d = json.loads(raw)
E = {e['id']: e for e in d['entries']}
if S2:
    E['s2-joel-20261017-2137-47-5']['status'] = 'superseded'
    E['s2-joel-20261017-2137-47-5']['what'] += ' Superseded at 23:10 UTC by his own opening (52 a, s2-joel-20261017-2310-52a).'
if S2 in ('S2v35b', 'S2v35c'):
    e = E['s2-joel-20261017-2137-46a']
    e['status'] = 'applied'
    e['what'] += (' In at 23:10 UTC with his opening (425g): %s.' % ('the anomie paragraph and his screenshot and caption'
                  if S2 == 'S2v35c' else 'the anomie paragraph; the screenshot stays in section 12 (with it, the section read AI)'))
if PROMOTED:
    E['all-joel-20261017-2137-45a']['status'] = 'applied'
    E['all-joel-20261017-2137-45a']['what'] += ' Done at 23:10 UTC, when section 2 settled 46: master.md is the registered master.'
new = []
if S2:
    new.append({'id': 's2-joel-20261017-2310-52a', 'status': 'applied', 'words': 'his',
                'what': 'Section 2: his opening as he wrote it (P1 and P2, with his 53 aside), the published link on "the U.S. Surgeon '
                        'General" kept. Pangram 425g: his P1 with his P2 Human, his P2 alone Human, the section 100% Human.',
                'joel': '52 this is human: ... 53 fixed (fact checked with gemini)', 'when': WHEN,
                'must_contain': ['Suddenly the longing to escape loneliness which inspired my father’s movie is everywhere again',
                                 'even put out an advisory, saying roughly half of American adults experience loneliness',
                                 '(it\'s literally listed in the UN Convention Against Torture). Folks may disagree about politics'],
                'must_not_contain': ['Or about the loneliness under it, at least.', 'is starvin’ them']})
if S8:
    new.append({'id': 's8-joel-20261017-2310-54', 'status': 'applied', 'words': 'his',
                'what': 'Section 8: his sentence after the truthfulness line. Pangram 425g: the paragraph Human, the section 100% Human.',
                'joel': '54 actually i would change it to: "Make sure kids understand ... And those who are known to lie a lot are '
                        'especially targeted by abusers who know their accusations won\'t be believed."', 'when': WHEN,
                'must_contain': ['if they are known to be honest. And those who are known to lie a lot are especially targeted by '
                                 'abusers who know their accusations won\'t be believed.']})
for n in new:
    if n['id'] not in E:
        d['entries'].append(n)
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if raw.endswith('\n') else ''), encoding='utf-8')

# the evidence runs
F = A / 'DETECTOR-EVIDENCE.json'
raw = F.read_text(encoding='utf-8')
ev = json.loads(raw)
have = {(r.get('section'), r.get('version')) for r in ev['runs']}
P = 'section %d as installed in articles/intentional-communities/candidate/HUMANIZED-SO-FAR.md'
add = []
if S2:
    add.append((2, {'S2v35c': 'v3.5c', 'S2v35b': 'v3.5b', 'S2v35': 'v3.5'}[S2] + ' (2026-10-17 night)',
                'CANDIDATE: section 2 with Joel\'s 23:10 opening%s; every changed paragraph Human alone or with its neighbor, the whole '
                'section 100%% Human (%s).' % ({'S2v35c': ', the anomie paragraph and his screenshot (46 a)',
                                                'S2v35b': ' and the anomie paragraph (46 a)', 'S2v35': ''}[S2], rec(S2))))
if S2 == 'S2v35c':
    add.append((12, 'v16 (2026-10-17 night)', 'CANDIDATE: section 12 without the screenshot and caption, which moved to section 2; the '
                'whole section 100%% Human (%s).' % rec('S12v16')))
if S8:
    add.append((8, 'v32 (2026-10-17 night)', 'CANDIDATE: section 8 with Joel\'s 54 sentence; the paragraph Human, the whole section '
                '100%% Human (%s).' % rec('S8v32')))
for s, v, r in add:
    if (s, v) not in have:
        ev['runs'].append({'section': s, 'version': v, 'passage': P % s, 'service': 'Pangram web app (dashboard)', 'record': r})
F.write_text(json.dumps(ev, ensure_ascii=False, indent=1) + ('\n' if raw.endswith('\n') else ''), encoding='utf-8')

# the unincorporated ideas: the anomie paragraph is in
if S2 in ('S2v35b', 'S2v35c'):
    u = A / 'UNINCORPORATED-IDEAS.md'
    t = u.read_text(encoding='utf-8')
    o = 'Disposition: waiting on question 52.'
    if o in t:
        t = t.replace(o, 'Disposition: in, at 23:10 UTC, after his own opening for section 2 (52 a) made the section read 100% Human with '
                         'it (batch 425g).')
        u.write_text(t, encoding='utf-8')
print('ledger, evidence, ideas written; section 2:', S2, '; section 8:', S8, '; promoted:', PROMOTED)
