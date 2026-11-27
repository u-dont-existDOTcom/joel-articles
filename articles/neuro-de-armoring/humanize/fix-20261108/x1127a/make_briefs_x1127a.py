"""The fresh readers' briefs for this turn's two changed warnings (texts_x1127a.NEW: the herbs warning with 73a and his
line, the Precautions with 74b), as make_briefs_x1123a.py makes them: the needed read, the read against his fixes and
the fit read, into v1/needed/KEY, v1/his-fixes/KEY and v1/fit/KEY. The fit reads keep last turn's moments (x1126c/v1/fit:
a reader who already takes lion's mane; a reader who takes kratom some days), since questions 73 and 74 came from them.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1127a/make_briefs_x1127a.py [KEY ...]
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'x1123a'))
sys.path.insert(0, str(HERE))
import make_briefs_x1123a as M  # noqa: E402
import texts_x1127a as T  # noqa: E402

TOP = 'A Complete Guide to Bio-De-Armoring (the warnings at the top, before the protocol)'
M.SPEC['lma'] = dict(heading=TOP,
                     for_='the reader learns that the protocol can\'t recommend starting lion\'s mane or ashwagandha, the '
                          'rare lasting effects people report from them, and what would make them stop either if they '
                          'take it',
                     moment='you are an adult with trauma about to start this protocol, reading its warnings; you already '
                            'take lion\'s mane for focus')
M.SPEC['prec'] = dict(heading=TOP,
                      for_='the reader learns what not to combine agmatine with, and who should be careful with it',
                      moment='you are an adult with trauma about to start this protocol, reading its warnings; you take '
                             'kratom some days')

if __name__ == '__main__':
    keys = sys.argv[1:] or list(T.ORDER)

    class _T:
        TEXTS = {k: (lambda k=k: T.plain(T.NEW[k])) for k in T.ORDER}
    M.HERE = HERE / 'v1'
    M.T = _T
    M.main(keys)
