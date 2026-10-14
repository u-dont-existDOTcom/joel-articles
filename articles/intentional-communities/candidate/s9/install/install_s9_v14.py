"""Replace section 9 v13 with v14 in HUMANIZED-SO-FAR.md, and add Joel's 2026-10-09 22:08 UTC P13 and naming
ruling to OWNER-EDITS.json. Run from candidate/."""
import json, pathlib
C = pathlib.Path(__file__).resolve().parents[2]
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
old = (C / 's9/section-v8.md').read_text(encoding='utf-8').strip()
new = (C / 's9/section-v9.md').read_text(encoding='utf-8').strip()
start = art.index('<!-- CANDIDATE: section 9 v13')
end = art.index('# From One Community to a Movement')
block = art[start:end]
body = block[block.index('-->\n') + 4:].strip()
assert body == old, 'the article does not hold section 9 v13; stop'
note = ('<!-- CANDIDATE: section 9 v14 (2026-10-09), Joel\'s P9 to P12 of 05:02 UTC and his P13 of 22:08 UTC in (four '
        'obvious typos fixed in his P12 under his rule), and "Good Government Juntas (Boards)" at the first mention (P8, his '
        '22:08 answer). Pangram web app (the final test): the section 100% Human (1,034 words scanned, 22:11:41 UTC, batch '
        '184g); every paragraph passes alone or beside a neighbor that passes alone. Records: s9/PREDICTIONS-s9.md (batches '
        '147g to 184g), s9/section-v9.md, s9/joel-2208/. Not accepted until Joel says so. -->\n')
art = art[:start] + note + new + '\n\n' + art[end:]
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
L = json.load(open(C / 'OWNER-EDITS.json', encoding='utf-8'))
have = {e['id'] for e in L['entries']}
E = [
 {'id': 's9-joel-20261009-2208', 'what': 'Section 9: Joel\'s P13 and his answers of 2026-10-09 22:08 UTC (s9/joel-2208/joel-20261009-2208.json): '
  'his P13 in place of mine; "Good Government Juntas (Boards)" at the first mention; P7\'s "the closest thing to a whole example" kept '
  '("doesn\'t seem like a hedge to me, sounds just more conversational"). [applied: section 9 v14, 2026-10-09]',
  'status': 'applied',
  'must_contain_exact': ["Now, the Zapatistas also don't prove my whole money-free economy goal.",
                         'They still use money internally in some cases, not others, and they still use it externally for trade.',
                         "They've also benefitted from outside economic help, while at the same time making efforts to remain politically independent from donors and more self-sustaining.",
                         'a rehearsal for the Good Government Juntas (Boards).',
                         'the closest thing to a whole example'],
  'must_not_contain': ['So what do they show?', 'a rehearsal for the Good Government Boards']},
]
for e in E:
    if e['id'] not in have: L['entries'].append(e)
json.dump(L, open(C / 'OWNER-EDITS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('installed v14; ledger entries', len(L['entries']))
