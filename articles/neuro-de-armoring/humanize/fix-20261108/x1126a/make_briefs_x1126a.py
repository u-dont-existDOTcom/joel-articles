"""The fresh readers' briefs for this turn's texts of mine (texts_x1126a: the plant medicines, The Rule, uridine), as
make_briefs_x1125a.py makes them: the needed read, the read against his fixes and the fit read, into
v1/needed/KEY, v1/his-fixes/KEY and v1/fit/KEY.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1126a/make_briefs_x1126a.py [KEY ...]
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'x1123a'))
sys.path.insert(0, str(HERE.parent / 'x1125a'))
sys.path.insert(0, str(HERE))
import make_briefs_x1123a as M  # noqa: E402
import make_briefs_x1125a as M5  # noqa: E402,F401  (fills M.SPEC with the x1125a readers)
import texts_x1126a as T  # noqa: E402

M.SPEC['ethno'] = dict(M.SPEC['ethno'], for_='the reader learns that the protocol\'s two plant medicines are illegal in '
                       'many places and risky (iboga for the heart), never to mix iboga with most medications, and how '
                       'to check the ones they take')
M.SPEC['rule'] = dict(M.SPEC['rule'], for_='the reader learns which kind of company and closeness to look for during the '
                      'protocol, and why it may not be the time to start a new romance or anything dramatic')
M.SPEC['uri'] = dict(M.SPEC['uri'], for_='the reader who uses psychedelics learns what uridine (UMP) may change, to keep '
                     'it off trip days, and how much to take on the first trip after starting it')

if __name__ == '__main__':
    keys = sys.argv[1:] or list(T.MINE)

    class _T:
        TEXTS = {k: (lambda k=k: T.plain(T.NEW[k])) for k in T.MINE}
    M.HERE = HERE / 'v1'
    M.T = _T
    M.main(keys)
