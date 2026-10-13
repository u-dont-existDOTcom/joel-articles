"""Install section 9 v13 in HUMANIZED-SO-FAR.md (in place of the published section, which is what it held), and add
Joel's section 9 paragraphs (P9 to P12, 2026-10-09 05:02 UTC) to OWNER-EDITS.json so the ledger check holds them.
Run from candidate/."""
import json, pathlib
C = pathlib.Path(__file__).resolve().parents[2]
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
pub = (C.parent / 'sections/010-original.md').read_text(encoding='utf-8').strip()
new = (C / 's9/section-v8.md').read_text(encoding='utf-8').strip()
start = art.index('# The Best Model I’ve Seen: Zapatistas')
end = art.index('# From One Community to a Movement')
assert art[start:end].strip() == pub, 'section 9 in the article is not the published text; stop'
note = ('<!-- CANDIDATE: section 9 v13 (2026-10-09), Joel\'s P9 to P12 of 05:02 UTC in (four obvious typos fixed in his P12 '
        'under his rule: s9/joel-0502/joel-0502-fixed.json). Pangram web app (the final test): the section 100% Human '
        '(1,086 words scanned, 06:29:14 UTC, batch 182g); every paragraph passes alone or beside a neighbor that passes alone. '
        'Gate: traces E, F and G, stance d6, cold read d6, abstract-agent judge d6 (s9/review-d6/); the kept findings are on '
        'the side-by-side page. Records: s9/PREDICTIONS-s9.md (batches 147g to 182g), s9/section-v8.md. Not accepted until '
        'Joel says so. -->\n')
art = art[:start] + note + new + '\n\n' + art[end:]
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
L = json.load(open(C / 'OWNER-EDITS.json', encoding='utf-8'))
have = {e['id'] for e in L['entries']}
E = [
 {'id': 's9-joel-20261009-0502', 'what': 'Section 9: Joel\'s P9 to P12 of 2026-10-09 05:02 UTC (s9/joel-0502/joel-20261009-0502.json), '
  'with four obvious typos fixed in P12 under his rule (s9/joel-0502/joel-0502-fixed.json). [applied: section 9 v13, 2026-10-09]',
  'status': 'applied',
  'must_contain_exact': ['which was split into Rebel Zapatista Autonomous Municipalities and the Good Government Juntas.',
                         'The original idea was to have power vested in the local communities, but it had crept up and consolidated itself at higher levels over time for practical reasons.',
                         'Institutions get more and more layers and offices as they age.',
                         "except usually it goes one way without reversal, unless there's a revolution.",
                         'But there is a special reason the Zapatistas were successfully able to reverse this degeneration.',
                         "And that's not me saying that.",
                         'as something ready-made, shake & bake.'],
  'must_not_contain': ['rein in my enthusiasm', 'leadership book']},
]
for e in E:
    if e['id'] not in have: L['entries'].append(e)
json.dump(L, open(C / 'OWNER-EDITS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('installed; ledger entries', len(L['entries']))
