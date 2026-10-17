"""Install this turn's sections into HUMANIZED-SO-FAR.md once batch 415g has read every changed paragraph and section Human
(Joel's message of 2026-10-17 17:16 UTC): section 2 v3.3, section 9 v17, section 15 v14 and section 16 v29, each in place of
the section now there, with a new CANDIDATE note in front of the old one. Section 12 v15 went in already (install_44c.py).
Refuses unless every item of its sections read Human in b415-results.json. Idempotent.
Run from candidate/: python3 fix-20261017b/install_1716.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
ART = C / 'HUMANIZED-SO-FAR.md'
R = json.loads((HERE / 'b415' / 'b415-results.json').read_text(encoding='utf-8'))
link = lambda k: 'https://www.pangram.com/history' + R[k][5]
SECT = [
    ('# Communes Are Hot Again', HERE / 's2-v3.3.md', 'S2v33', '<!-- CANDIDATE: section 2 v3.2',
     'section 2 v3.3 (2026-10-17, after Joel\'s 17:16 message): v3.2 with "starving" for Emulate\'s "starvin\'" (the '
     'faithfulness pass; his section 5 rule: unusual spellings are cheating)'),
    ('# The Best Model I’ve Seen: Zapatistas', HERE / 's9-v17.md', 'S9v17', '<!-- CANDIDATE: section 9 v16',
     'section 9 v17 (2026-10-17, after Joel\'s 17:16 message): v16 with the published limit back after the Escuelita evidence, '
     '"I\'m not claiming the Zapatistas already proved my whole model." (the faithfulness pass; cut on 2026-10-14 as a repeat of '
     'his P13, which covers only the economy)'),
    ('# What This Looks Like From Sénégal', C / 's15' / 'v14.md', 'S15v14', '<!-- CANDIDATE: section 15 v13',
     'section 15 v14 (2026-10-17, after Joel\'s 17:16 message): v13 with the exclamations his way (his 43; '
     'fix-20261017b/make_excl.py) and the faithfulness pass\'s fixes ("Being in community isn\'t automatically liberating. It '
     'all depends on who is allowed to belong without pretending.", "whatever prosperity came through you later", "No, not that '
     'either.")'),
    ('# Practice Comes Before Property', C / 's16' / 'v29.md', 'S16v29', '<!-- CANDIDATE: section 16 v28',
     'section 16 v29 (2026-10-17, after Joel\'s 17:16 message): v28 with the exclamations his way (his 43: "That\'s it!" out, '
     'four marks to periods; two that are their paragraph\'s only turn are question 47) and the faithfulness pass\'s fixes '
     '("rather than by declaring "money is impure!"", "It can still change how people survive")'),
]
md = ART.read_text(encoding='utf-8')
for h1, path, key, old_note, what in SECT:
    keys = [k for k in R if k == key or k.startswith(key + '-')]
    bad = [k for k in keys if not R[k][0].startswith('Human')]
    assert key in R and not bad, (key, bad)
    new = path.read_text(encoding='utf-8').strip()
    if new in md:
        print(key, 'already in')
        continue
    a = md.index(h1)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', md[a + 3:])
    b = a + 3 + m.start()
    md = md[:a] + new + '\n' + md[b:]
    i = md.index(old_note)
    note = ('<!-- CANDIDATE: %s. Pangram web app, 415g: every changed paragraph Human alone or with its neighbor, the whole '
            'section %s (%s). Records: fix-20261017b/. Before: -->\n' % (what, R[key][0].replace(' Written', ''), link(key)))
    md = md[:i] + note + md[i:]
    print(key, 'installed')
ART.write_text(md, encoding='utf-8')
