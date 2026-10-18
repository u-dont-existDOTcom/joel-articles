"""Install this turn's sections into HUMANIZED-SO-FAR.md (Joel's message of 2026-10-17 17:16 UTC): section 9 v17, section 15
v14 and section 16 v29, each in place of the section now there, with a new CANDIDATE note in front of the old one. Section 12
v15 went in already (install_44c.py); section 2 stays as it is (question 47). Each section goes in only if its whole-section
check and every check of its changed paragraphs (the exact final text) read Human: section 9 in 415g, section 15 in 415g and
417g, section 16 in 415g, 417g, 418g and 419g. Idempotent. Run from candidate/: python3 fix-20261017b/install_1716.py [S16-KEY]"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
ART = C / 'HUMANIZED-SO-FAR.md'
R = {}
for b in ('b415', 'b417', 'b418', 'b419'):
    f = HERE / b / ('%s-results.json' % b)
    if f.exists():
        R.update(json.loads(f.read_text(encoding='utf-8')))
link = lambda k: 'https://www.pangram.com/history' + R[k][5]
G417 = json.loads((HERE / 'b417' / 'GATE.json').read_text(encoding='utf-8'))
S16 = sys.argv[1] if len(sys.argv) > 1 else None
SECT = [
    ('# The Best Model I’ve Seen: Zapatistas', HERE / 's9-v17.md', 'S9v17', ['S9v17-evid'], '<!-- CANDIDATE: section 9 v16',
     'section 9 v17 (2026-10-17, after Joel\'s 17:16 message): v16 with the published limit back after the Escuelita evidence, '
     '"I\'m not claiming the Zapatistas already proved my whole model." (the faithfulness pass; cut on 2026-10-14 as a repeat of '
     'his P13, which covers only the economy)'),
    ('# What This Looks Like From Sénégal', C / 's15' / 'v14.md', 'S15v14b', [p for p in G417['S15v14b']['parts'] if p != 'installed'],
     '<!-- CANDIDATE: section 15 v13',
     'section 15 v14 (2026-10-17, after Joel\'s 17:16 message): v13 with five exclamations his way (his 43; '
     'fix-20261017b/make_excl.py) and two fixes from the faithfulness pass ("Being in community isn\'t automatically '
     'liberating. It all depends on who is allowed to belong without pretending.", "whatever prosperity came through you '
     'later"); "No, not that either!" stays (question 47)'),
]
if S16:
    G418 = json.loads((HERE / ('b419' if S16 == 'S16-e' else 'b418') / 'GATE.json').read_text(encoding='utf-8'))
    SECT.append(('# Practice Comes Before Property', C / 's16' / 'v29.md', S16, [p for p in G418[S16]['parts'] if p != 'installed'],
                 '<!-- CANDIDATE: section 16 v28',
                 'section 16 v29 (2026-10-17, after Joel\'s 17:16 message): v28 with the changes 418g read Human one at a time '
                 '(fix-20261017b/make_batch418.py, %s): five exclamations his way (his 43) and the faithfulness pass\'s "rather than by '
                 'declaring"; the rest are question 47' % S16))
md = ART.read_text(encoding='utf-8')
for h1, path, key, parts, old_note, what in SECT:
    bad = [k for k in [key] + parts if k not in R or not R[k][0].startswith('Human') or '; AI' in R[k][3]]
    assert not bad, (key, bad)
    new = path.read_text(encoding='utf-8').strip()
    if new in md:
        print(key, 'already in')
        continue
    a = md.index(h1)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', md[a + 3:])
    b = a + 3 + m.start()
    md = md[:a] + new + '\n' + md[b:]
    i = md.index(old_note)
    note = ('<!-- CANDIDATE: %s. Pangram web app: every changed paragraph Human alone or with its neighbor, the whole section %s '
            '(%s). Records: fix-20261017b/. Before: -->\n' % (what, R[key][0].replace(' Written', ''), link(key)))
    md = md[:i] + note + md[i:]
    print(key, 'installed')
ART.write_text(md, encoding='utf-8')
