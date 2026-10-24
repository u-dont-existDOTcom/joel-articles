"""Batch n9 (Nibbāna): Joel's answer of 2026-10-24 23:40 UTC to N7 (../joel-20261024-2340-message.txt: "n7a").

N7 asked about "The later Buddhist philosopher Milindapañha compared rebirth to one lamp being used to light another.":
the Milindapañha is a book (King Milinda's questions to the monk Nāgasena, whose lamp simile it is), and his link goes to
it. A (his answer, my pick): "The later Buddhist text Milindapañha ...", one word changed, the link and italics staying on
Milindapañha.

  (install_n1.py calls apply() after batch n8)
"""
import json
import pathlib

N9 = pathlib.Path(__file__).resolve().parent
EDITS = [('The later Buddhist philosopher <a ', 'The later Buddhist text <a ', 'N7 A',
          'The Milindapañha is a book, King Milinda\'s questions to the monk Nāgasena, whose lamp simile it is.')]


def apply(work):
    recs = []
    for old, new, answer, why in EDITS:
        assert work.count(old) == 1, (answer, work.count(old))
        work = work.replace(old, new)
        recs.append({'answer': answer, 'old': old.replace(' <a ', ''), 'new': new.replace(' <a ', ''), 'why': why,
                     'source': '../joel-20261024-2340-message.txt'})
    (N9 / 'EDITS-n9.json').write_text(json.dumps(recs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return work, recs
