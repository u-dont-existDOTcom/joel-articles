#!/usr/bin/env python3
"""Turn 112: OWNER-EDITS.json after his answers of 2026-10-25 21:40 UTC (apply_t112.py). One new entry records 108.1 (his
version of Borrow Love's third paragraph, with the links it keeps) and 108.2 (A, no change), with what the article must and
mustn't contain now. Applied once; it refuses to run again."""
import json
import pathlib

P = pathlib.Path(__file__).resolve().parents[2] / 'OWNER-EDITS.json'
data = json.loads(P.read_text(encoding='utf-8'))
assert not any(e['id'] == 'joel-112-20261025' for e in data['entries']), 'already applied'
data['entries'].append({
    'id': 'joel-112-20261025',
    'status': 'applied',
    'what': '108.1: his own version of Borrow Love\'s third paragraph, word for word with his characters ("this version passes", '
            'his check), the two links his earlier version had kept on "psychological trick" and "Solomon’s paradox". 108.2: A, '
            'Just Like Me\'s second paragraph stays his sentence alone. Installed by experiments/t112-installs/apply_t112.py.',
    'joel': '2026-10-25 21:40 UTC (experiments/t112-answers/JOEL-20261025-2140.md)',
    'where': 'Borrow Love—or Borrow the Perspective of Care; Just Like Me',
    'must_contain': [
        'Or put somebody you care about into your exact life, your family, all the conditions you face, and then step outside '
        'it and ask what you’d tell them as a friend. This [psychological trick](https://pubmed.ncbi.nlm.nih.gov/21728454/) has '
        'a rich history around it, and even has a name, [Solomon’s paradox](https://pubmed.ncbi.nlm.nih.gov/24916084/), after '
        'the biblical king everybody brought their disputes to, who then wrecked his own life.',
    ],
    'must_not_contain': ['your bank account and all', 'cheap trick for becoming the outsider to your own mess'],
})
P.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('added joel-112-20261025')
