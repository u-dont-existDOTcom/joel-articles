"""The receipts for version 10 (texts_x1125a.V10): the plant medicines, uridine and the DMSO item, each as it is in the
article with one word made plain after the comparison read (read-1125a/READER-1.md, F1.2, F1.17, F1.1). Parts and
reads as each paragraph's last receipt had them.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1125a/build_receipts_v10.py
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_receipts_v6 as M  # noqa: E402

R, T, B, S = M.R, M.T, M.B, M.S
OUT = HERE / 'v10'
OUT.mkdir(exist_ok=True)
B.HERE = OUT
M.OUT = OUT
V = T.V10
T.V4 = dict(T.V4, ethno=V['ethno'], uri=V['uri'])
R.REGISTER_ONLY = True
for k in R.ALL:
    R.ALL[k]()
R.REGISTER_ONLY = False
bad = R._build('ETHNO10', T.plain(V['ethno']), ['ethno'], {})
bad += R._build('URI10', T.plain(V['uri']), ['uri'], {})
p = M.P('dmso')
spec = {k: v for k, v in p['spec'].items() if not k.startswith(('My full', 'Your lungs count too'))}
old = p['spec']['Your lungs count too']
spec['Your lungs need'] = ('a smoker breathes in only a little at a time and stops at the first sign, and knows his '
                           'reference has the rest', old[1], 'Your lungs need to be clean too')
bad += M.build('dmso', 'v2', T.plain(V['dmso']), p['where'], p['who'], spec, p['opens'], p['checked'],
               [(6, '4, 7')], [(6, 'ANYWAY: weak on any day; CAN\'T TELL: how much is much, and what to do')],
               p['same'], p['place'], name='DMSO10')
print('\n'.join(bad) or 'receipts: PASS')
