"""The receipts for x1125a's fourth batch (texts_x1125a.V9): the Cognitive Warning's first paragraph, one word made
plain, with each of its two neighbours: the paragraph after it (version 7's, in the article at Human High by itself)
and The Rule before it (version 4's), which has not yet been read beside a neighbour that reads Human.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1125a/build_receipts_v9.py
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_receipts_x1125a as R  # noqa: E402

T, B = R.T, R.B
OUT = HERE / 'v9'
OUT.mkdir(exist_ok=True)
B.HERE = OUT
T.V4 = dict(T.V4, cog=T.V9['cog'], proj=T.V7['proj'])
R.REGISTER_ONLY = True
for k in ('rule', 'cog', 'proj'):
    R.ALL[k]()
R.REGISTER_ONLY = False
p = R.PARTS['proj']
p['spec'] = {("So during this protocol" if k == 'So the rule' else k): ((v[0], v[1], 'So during this protocol') if
                                                                         k == 'So the rule' else v)
             for k, v in p['spec'].items()}
bad = R._build('PAIR-COG-PROJ9', T.plain(T.V4['cog']) + '\n\n' + T.plain(T.V4['proj']), ['cog', 'proj'],
               {'proj': 'Your armored brain also'})
bad += R._build('PAIR-RULE-COG9', T.plain(T.V4['rule']) + '\n\n' + T.plain(T.V4['cog']), ['rule', 'cog'],
                {'cog': 'none: the next warning in the list, on a new subject (how they will read other people)'})
print('\n'.join(bad) or 'receipts: PASS')
