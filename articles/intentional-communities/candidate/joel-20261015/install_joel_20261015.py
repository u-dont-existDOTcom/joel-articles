"""Install Joel's answers of 2026-10-15 09:33 UTC (joel-20261015-0933-message.txt). Run from candidate/.

- 27: nothing to change in section 4 ("i actually could not reproduce the pangram failure on this part").
- 28 b: section 10's last paragraph opens "Whenever a community or a federation creates or applies a rule" (my
  option b, his pick: it ties the paragraph to the federation section and keeps every community's rules in).
- 29 ("rebuild the diagram pls"): section 4's diagram, image 7, rebuilt from its own SVG (images/image7-v2.svg); the
  article keeps the Substack image until he uploads the new one.
"""
import json, pathlib

C = pathlib.Path(__file__).resolve().parents[1]
art_path = C / 'HUMANIZED-SO-FAR.md'
art = art_path.read_text(encoding='utf-8')
Q = '2026-10-15 09:33 UTC, his answers to 27 to 29 (joel-20261015/)'


def rep(t, a, b):
    assert t.count(a) == 1, (a[:60], t.count(a))
    return t.replace(a, b)


OLD = "Whenever you create or apply a rule, it's best practice"
NEW = "Whenever a community or a federation creates or applies a rule, it's best practice"
old_par = next(p for p in art.split('\n') if p.startswith(OLD))
art = rep(art, OLD, NEW)
new_par = old_par.replace(OLD, NEW)
art = rep(art, '<!-- CANDIDATE: section 10 v3 (2026-10-14 21:19):',
          '<!-- CANDIDATE: section 10 v4 (2026-10-15 09:33): v3 with "Whenever a community or a federation creates or applies '
          'a rule" (Joel\'s 28 b; both cold reads of v3 had found the paragraph a jump from the federation paragraphs). '
          'Pangram 285g: the paragraph Human alone, the section 100% Human (fix-20261015/PREDICTIONS.md). Before: section '
          '10 v3 (2026-10-14 21:19):')
art_path.write_text(art, encoding='utf-8')

L = json.load(open(C / 'OWNER-EDITS.json', encoding='utf-8'))
have = {e['id']: e for e in L['entries']}
e = have['s10-joel-20261014-2119']
assert e['must_contain_exact'] == [old_par], e['must_contain_exact']
e['must_contain_exact'] = [new_par]
e['what'] += ' (2026-10-15: its opening is "Whenever a community or a federation creates or applies a rule", his 28 b; entry s10-joel-20261015-28b checks it.)'
n = {'id': 's10-joel-20261015-28b', 'status': 'applied', 'words': 'proposed',
     'what': 'Section 10, the last paragraph: "Whenever a community or a federation creates or applies a rule" for "Whenever you create or apply a rule" (my option b, his pick).',
     'joel': '28 b', 'when': Q,
     'must_contain': [NEW], 'must_not_contain': ["Whenever you create or apply a rule, it's best practice"]}
assert n['id'] not in have
L['entries'].append(n)
json.dump(L, open(C / 'OWNER-EDITS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('installed; ledger entries', len(L['entries']))
