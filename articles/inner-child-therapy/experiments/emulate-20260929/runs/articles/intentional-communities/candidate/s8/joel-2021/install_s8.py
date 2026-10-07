"""Install section 8 v27 in HUMANIZED-SO-FAR.md (in place of the published section, which is what it held), and add
Joel's section 8 edits to OWNER-EDITS.json so the ledger check holds them. Run from candidate/."""
import json, pathlib
C = pathlib.Path(__file__).resolve().parents[2]
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
pub = (C.parent / 'sections/009-original.md').read_text(encoding='utf-8').strip()
new = (C / 's8/section-d10.md').read_text(encoding='utf-8').strip()
start = art.index('# The Grown Children Get the Final Review')
end = art.index('# The Best Model I’ve Seen: Zapatistas')
assert art[start:end].strip() == pub, 'section 8 in the article is not the published text; stop'
note = ('<!-- CANDIDATE: section 8 v27 (2026-10-07), Joel\'s edits of 15:05 and 20:21 UTC in: his P3, P10, P18, P21 and '
        'the last subsection (his first paragraph there carries the published P26\'s point); P7 cut and the subheading '
        '"Communal Parenting Adds On"; P27 and P28 at the top without their heading, and P28\'s first sentence cut (his OK, '
        '20:21). His typos "althoug" and "able to access to" fixed under his rule; the page\'s strike marking that came along '
        'in his first P10 taken out. Pangram web app (the final test): the section 100% Human (1,812 words scanned, 20:24:18 '
        'UTC, batch 146g). Records: s8/PREDICTIONS-s8.md, s8/cand-v27.json, s8/joel-1505/, s8/joel-2021/. Not accepted until '
        'Joel says so. -->\n')
art = art[:start] + note + new + '\n\n' + art[end:]
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
L = json.load(open(C / 'OWNER-EDITS.json', encoding='utf-8'))
have = {e['id'] for e in L['entries']}
E = [
 {'id': 's8-joel-20261007-1505', 'what': 'Section 8: Joel\'s texts and rulings of 2026-10-07 15:05 UTC (s8/joel-1505/joel-20261007-1505.json): his P3, P18 and P21, '
  'P7 cut with the subheading "Communal Parenting Adds On", P13\'s "boss", P27 and P28 moved to the top. [applied: section 8 v27, 2026-10-07]',
  'status': 'applied',
  'must_contain_exact': ["All of the community's design and implementation will ultimately be reviewed by the kids, once they're grown",
                         'The Buddha even taught his son honesty as the most important first lesson.',
                         'hopefully including non-intrusive help from outside the home community.',
                         "Older kids can't be allowed to quietly boss the younger ones around there."],
  'must_contain': ['Communal Parenting Adds On'],
  'must_not_contain': ['The Mother Is Primary. The Village Is Real.', 'My view is that moms raise their own kids',
                       'that the home community does not control', 'Discuss Child-Rearing Values Before Children Are Caught Between Them']},
 {'id': 's8-joel-20261007-2021', 'what': 'Section 8: Joel\'s texts and OKs of 2026-10-07 20:21 UTC (s8/joel-2021/joel-20261007-2021.json): his new P10, '
  'his first paragraph of the last subsection with the published P26\'s point, P18 "children", P22 "a commitment they make as adults", '
  'P25\'s last line shortened, and P28\'s first sentence cut ("p28 looks better now yes"). [applied: section 8 v27, 2026-10-07]',
  'status': 'applied',
  'must_contain_exact': ["so they weren't as dogmatic as I originally thought.",
                         "since that attachment is formed already from years of nursing.",
                         'we may see more evolution than if they simply return and continue what their parents started.',
                         'Protecting children is the duty of adults, but it requires children to help also.',
                         'which means belonging is a commitment they make as adults.',
                         'Belonging and freedom should go hand in hand.'],
  'must_not_contain': ["goodwill doesn't answer those questions", "Goodwill doesn't answer those questions",
                       'No upbringing can provide perfect freedom', 'a commitment they choose on their own',
                       'it requires them to help also']},
]
for e in E:
    if e['id'] not in have: L['entries'].append(e)
json.dump(L, open(C / 'OWNER-EDITS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('installed; ledger entries', len(L['entries']))
