"""Install section 2 v3.6 (Joel's 01:29 texts, fix-20261018/make_0129.py) on his own Pangram check: "i checked the section, it
passes as human when first part is this". My checks of it (batch 428g) wait: after his message the web app in the desktop app's
browser was signed out (it showed "Log in" and a "Verify you are human" box) and the API key had no credits (HTTP 402,
"Insufficient credits"). The anomie paragraph and the screenshot (his 46 a: "once section 2 reads 100% Human with it") need
those checks, so this installs v3.6 as he pasted it, and the screenshot stays in section 12. Then the ledger, the evidence
runs and the ideas file. Idempotent. Run from candidate/: python3 fix-20261018/install_0129.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
A = C.parent
ART = C / 'HUMANIZED-SO-FAR.md'
H2 = '# Communes Are Hot Again'
WHEN = '2026-10-18 01:29 UTC (joel-20261018/joel-20261018-0129-message.txt)'
new = (HERE / 's2-v36.md').read_text(encoding='utf-8').strip()
md = ART.read_text(encoding='utf-8')
if new not in md:
    a = md.index(H2)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', md[a + 3:])
    md = md[:a] + new + '\n' + md[a + 3 + m.start():]
    i = md.index('<!-- CANDIDATE: section 2 v3.2')
    note = ('<!-- CANDIDATE: section 2 v3.6 (2026-10-18, after Joel\'s message of 01:29 UTC (joel-20261018/joel-20261018-0129-message.txt, '
            '56 a and 55 b): his first paragraph as he wrote it ("i checked the section, it passes as human when first part is this"), '
            'with the published link on "the U.S. Surgeon General" kept and his bold on "public-health"; his P2 from 23:10 with his '
            '55 b aside, "(the UN\'s rules for prisoners literally ban more than 15 days of it)". Pangram: his own check of the '
            'section (01:29). My checks (batch 428g, fix-20261018/b428/) wait: the web app was signed out and the API key had no '
            'credits. The anomie paragraph and his screenshot (46 a) wait for those checks; the screenshot stays in section 12. '
            'Records: fix-20261018/. Before: -->\n')
    md = md[:i] + note + md[i:]
    ART.write_text(md, encoding='utf-8')
    print('section 2 v3.6 installed')
else:
    print('section 2 v3.6 already in')

# the ledger
p = C / 'OWNER-EDITS.json'
raw = p.read_text(encoding='utf-8')
d = json.loads(raw)
E = {e['id']: e for e in d['entries']}
e = E['s2-joel-20261017-2310-52a']
if e['status'] != 'superseded':
    e['status'] = 'superseded'
    e['what'] += (' At 01:29 UTC on the 18th his 56 a replaced the first paragraph and his 55 b the aside; the rest of his P2 is in '
                  '(s2-joel-20261018-0129-56a-55b).')
    e.pop('waits_for', None)
for k, w in (('s2-joel-20261017-2137-46a', 'a Pangram check of section 2 with it (batch 428g), which waits on Pangram: the web app '
              'was signed out after his 01:29 message and the API key had no credits'),):
    if 'batch 428g' not in E[k]['what']:
        E[k]['what'] += ' Since 01:29 UTC on the 18th it waits on %s.' % w
        E[k]['waits_for'] = 'Pangram (batch 428g)'
ID = 's2-joel-20261018-0129-56a-55b'
if ID not in E:
    d['entries'].append({
        'id': ID, 'status': 'applied', 'words': 'his',
        'what': 'Section 2 v3.6: his first paragraph as he wrote it (56 a, with the published link on "the U.S. Surgeon General" and his '
                'bold on "public-health"), and his P2 from 23:10 with the aside of his 55 b. Installed on his own Pangram check of the '
                'section ("it passes as human when first part is this"); my checks (batch 428g) wait on Pangram.',
        'joel': '55b / 56a: i checked the section, it passes as human when first part is this: "Communes Are Hot Again 🔥 / Suddenly, '
                'the longing to escape loneliness which inspired my father’s movie, is everywhere again. Back in 2023, ironically, ..."',
        'when': WHEN,
        'must_contain': ['Suddenly, the longing to escape loneliness which inspired my father’s movie, is everywhere again.',
                         'Back in 2023, ironically, just the year after Covid lockdowns ended,',
                         'and it treated social connection as a public-health issue.',
                         "(the UN's rules for prisoners literally ban more than 15 days of it). Folks may disagree about politics",
                         'something about the current arrangement is starving them.'],
        'must_not_contain': ['Or about the loneliness under it, at least.', 'is starvin’ them',
                             "(it's literally listed in the UN Convention Against Torture)"]})
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if raw.endswith('\n') else ''), encoding='utf-8')

# the evidence runs: his own check, said as his
F = A / 'DETECTOR-EVIDENCE.json'
raw = F.read_text(encoding='utf-8')
ev = json.loads(raw)
V = 'v3.6 (2026-10-18)'
if not any(r.get('section') == 2 and r.get('version') == V for r in ev['runs']):
    ev['runs'].append({'section': 2, 'version': V,
                       'passage': 'section 2 as installed in articles/intentional-communities/candidate/HUMANIZED-SO-FAR.md',
                       'service': 'Pangram web app, Joel\'s own check',
                       'record': 'CANDIDATE: Joel, 01:29 UTC: "i checked the section, it passes as human when first part is this" '
                                 '(no link). My checks of it (batch 428g) wait on Pangram: the web app was signed out and the API key '
                                 'had no credits.'})
    F.write_text(json.dumps(ev, ensure_ascii=False, indent=1) + ('\n' if raw.endswith('\n') else ''), encoding='utf-8')
print('ledger and evidence written')
