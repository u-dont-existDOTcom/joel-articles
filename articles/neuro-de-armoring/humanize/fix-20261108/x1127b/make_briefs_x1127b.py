"""The fresh readers' briefs for this turn (texts_x1127b), as make_briefs_x1123a.py makes them, into v1/KIND/KEY: the
three reads of the "Underpinning" Principle as the article has it (sw17), and the read against his fixes of my new
practice paragraph (sw23n, the sentence after the Anti-Breakthrough).

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1127b/make_briefs_x1127b.py [KEY ...]
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'x1123a'))
sys.path.insert(0, str(HERE))
import make_briefs_x1123a as M  # noqa: E402
import texts_x1127b as T  # noqa: E402

SEC = 'Psychology is the Software; Biology is the Hardware. (before Part 1, the science)'
WHO = ('you are an adult with trauma who has done years of therapy (CBT, EMDR) and still gets triggered, reading why '
       'this protocol starts with the body')
M.SPEC['sw17'] = dict(heading=SEC,
                      for_='the reader learns why therapy aimed at thoughts can fail while the brain\'s foundation is '
                           'damaged, through Bruce Perry\'s picture of a house',
                      moment=WHO + '; you have just read that therapy rewrites the "code" while the "motherboard" is '
                             'overheating')
M.SPEC['sw23n'] = dict(heading=SEC + ', right after the paragraph that ends "Instead, this protocol works in doses of a '
                                     'few seconds, which is what I mean by micro-dosing here."',
                       for_='the reader learns the daily practice the doses of a few seconds come to, and why often '
                            'beats long',
                       moment=WHO + '; you have just read that this protocol works in doses of a few seconds')
TEXTS = {'sw17': lambda: T.plain(T.OLD['sw17']), 'sw23n': lambda: T.plain(T.NEW['sw23'])}

if __name__ == '__main__':
    keys = sys.argv[1:] or list(TEXTS)

    class _T:
        pass
    _T.TEXTS = TEXTS
    M.HERE = HERE / 'v1'
    M.T = _T
    M.main(keys)
