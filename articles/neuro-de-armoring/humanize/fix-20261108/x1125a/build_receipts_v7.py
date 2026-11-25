"""The receipts for the three small steps (texts_x1125a.V7: Electrolytes, the Cognitive Warning's second paragraph, the
5-HTP warning), each version 4 less my glosses and a phrase that could be read two ways, with version 4's reads and
parts (build_receipts_x1125a.py), and for the Cognitive Warning with its neighbour's small step.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1125a/build_receipts_v7.py
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_receipts_x1125a as R  # noqa: E402

T, B = R.T, R.B
OUT = HERE / 'v7'
OUT.mkdir(exist_ok=True)
B.HERE = OUT
T.V4 = dict(T.V4, elec=T.V7['elec'], proj=T.V7['proj'], htp=T.V7['htp'])
bad = R.elec() + R.htp()
R.REGISTER_ONLY = True
R.proj()
R.cog()
R.REGISTER_ONLY = False
p = R.PARTS['proj']
p['spec'] = {("So during this protocol" if k == 'So the rule' else k): ((v[0], v[1], 'So during this protocol') if
                                                                         k == 'So the rule' else v)
             for k, v in p['spec'].items()}
bad += R._build('PROJ4', T.plain(T.V4['proj']), ['proj'], {})
bad += R.pair('cog', 'proj', {'proj': 'Your armored brain also'})
print('\n'.join(bad) or 'receipts: PASS')
