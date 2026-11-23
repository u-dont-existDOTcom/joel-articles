"""The fresh readers' briefs for x1123b's texts (texts_x1123b), as make_briefs_x1123a.py makes them.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1123b/make_briefs_x1123b.py KEY ...
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'x1123a'))
sys.path.insert(0, str(HERE))
import make_briefs_x1123a as M  # noqa: E402
import texts_x1123b as T  # noqa: E402

M.HERE = HERE
M.T = T
M.SPEC['agm2'] = M.SPEC['agm']
for k in ('lma4', 'lma5', 'lma6'):
    M.SPEC[k] = M.SPEC['lma']
for k in ('agm3', 'agm4'):
    M.SPEC[k] = M.SPEC['agm']

if __name__ == '__main__':
    M.main(sys.argv[1:])
