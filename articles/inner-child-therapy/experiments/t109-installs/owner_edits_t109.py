#!/usr/bin/env python3
"""Turn 109: OWNER-EDITS.json for Joel's answers of 2026-10-25 14:20 UTC. The three entries whose strings the installs
moved or replaced carry the new strings, each with a history note, and one new entry records what went in."""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import apply_t109 as A  # noqa: E402

P = HERE.parents[1] / 'OWNER-EDITS.json'
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
WHEN = 'Turn 109 (his answers of 2026-10-25 14:20 UTC, experiments/t109-answers/JOEL-20261025-1420.md)'
data = json.loads(P.read_text(encoding='utf-8'))
by = {e['id']: e for e in data['entries']}
assert not any(e['id'].startswith('joel-109-') for e in data['entries']), 'already applied'

md = re.sub(r'<!--.*?-->', '', ART.read_text(encoding='utf-8'), flags=re.S)
i = md.index('### Hear the Guard First')
j = md.index('\n### ', i + 10)
guard = [p.strip() for p in md[i:j].split('\n\n')[1:] if p.strip()]
assert len(guard) == 7


def history(e, note):
    e.setdefault('history', []).append(WHEN + ': ' + note)


# his P2 of Hear the Guard First: its eight sentences, now in the plain-path paragraph and the performance paragraph
e = by['bus-p2-joel']
old = e['must_contain_exact']
assert len(old) == 1
his = [s for s in re.split(r'(?<=[.!?"”)])\s+(?=[A-Z"“(])', old[0]) if s]
assert len(his) == 8
e['must_contain_exact'] = his
history(e, '104 A moved his sentences, word for word, into the new first paragraph (sentences 3 to 6) and the performance paragraph (1, 2, 7 and 8), so each sentence is required now rather than the paragraph.')
e = by['bus-h3']
e['must_contain_exact'] = ['### Hear the Guard First'] + guard
e['order'] = ['Two Common Guarding Patterns', 'Hear the Guard First', 'Whichever protective part showed up', 'A harder voice can seem more fitting',
              'That part might say this will just be one more performance', "That part doesn't have to move out.",
              "If it's been calling all this stupid", "A new roommate doesn't win you over", 'Blaming yourself can be doing a job like that, too.']
history(e, '104 A: the section in its new shape, the plain path first and then one situation a paragraph (entry joel-109-20261025).')
e = by['photos-h2-joel-20261017']
p1 = [s for s in e['must_contain_exact'] if s.startswith('If picturing your little one feels fake')]
p2 = [s for s in e['must_contain_exact'] if s.startswith('While you look, notice what your body does')]
assert len(p1) == 1 and len(p2) == 1
e['must_contain_exact'] = [A.PH1_NEW if s == p1[0] else (s.replace(A.PH2_OLD, A.PH2_NEW) if s == p2[0] else s) for s in e['must_contain_exact']]
history(e, '105.2: his own first sentence for P1 and his two for the start of P2 ("this is the part that reads ai and it\'s actually redundant also"), with "Pema Chödrön\'s" for his "Pema Chodron\'s".')

data['entries'].append({
    'id': 'joel-109-20261025', 'status': 'applied',
    'what': "105.1: his own end of How This Relates to IFS P7 (his friend Pink's account), word for word but for \"explained\" (his \"expalined\") and a doubled space. 105.2: his own start of Use Childhood Photographs Gently. 104 A: Hear the Guard First in the plain-path-first shape, every sentence kept and used once, \"That part might say\" for \"It might say\". Installed by experiments/t109-installs/apply_t109.py.",
    'joel': '2026-10-25 14:20 UTC: "104 a yes this makes it much more of a readable guide, good."; "105.1 replace with ..."; "105.2 ok so this is the part that reads ai and it\'s actually redundant also ... change it to ..."',
    'where': 'How This Relates to IFS; Use Childhood Photographs Gently; Hear the Guard First',
    'must_contain_exact': [A.IFS_NEW, A.PH1_NEW],
    'must_contain': [A.PH2_NEW],
    'must_not_contain': ['Some practitioners are gentle about it', "I wouldn't trust a model more just because", 'expalined',
                         'Yes, yes, it might feel a bit strange', 'notice what your body does and what feelings or urges show up',
                         'It might say this will just be one more performance'],
})
P.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('owner edits updated:', len(data['entries']), 'entries')
