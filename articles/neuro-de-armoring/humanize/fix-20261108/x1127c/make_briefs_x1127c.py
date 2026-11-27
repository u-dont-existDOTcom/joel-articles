"""The fresh readers' briefs for this turn (texts_x1127c), as make_briefs_x1123a.py makes them, into v1/KIND/KEY: the
three reads of the Gibson paragraph with the split fixed (sw18), Part 1's intro line (p030, checked with the paragraph
after it), and the Metabolic Red Line's two paragraphs (p032, p033), each as the article has
them.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1127c/make_briefs_x1127c.py [KEY ...]
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'x1123a'))
sys.path.insert(0, str(HERE))
import make_briefs_x1123a as M  # noqa: E402
import texts_x1127c as T  # noqa: E402

PSY = 'Psychology is the Software; Biology is the Hardware. (before Part 1, the science)'
SCI = 'Part 1: THE SCIENCE (Why We Do This), then its first subsection, A. The Metabolic Red Line'
WHO = ('you are an adult with trauma who has done years of therapy (CBT, EMDR) and still gets triggered, reading why '
       'this protocol starts with the body')
M.SPEC['sw18'] = dict(heading=PSY + ', under the line "' + T.plain(T.NEW['sub']) + '"',
                      for_='the reader learns why the brain builds its armor: Lindsay Gibson\'s Role-Self, and Bruce '
                           'Perry\'s figures on how few grown-ups a child has today against the band our brains evolved in',
                      moment=WHO + '; you have just read Perry\'s house picture (therapy decorates while the foundation '
                             'crumbles)')
M.SPEC['p030'] = dict(heading='Part 1: THE SCIENCE (Why We Do This)',
                      for_='the reader learns what the science part is for: what goes wrong in the brain under trauma, '
                           'withdrawal or chronic stress, which the protocol\'s tools are meant to fix',
                      moment=WHO + '; you have just read that the protocol works in doses of a few seconds, like 30 '
                             'seconds of slow breathing, and are starting the science behind it')
M.SPEC['p032'] = dict(heading='A. The Metabolic Red Line (in Part 1: THE SCIENCE)',
                      for_='the reader learns why talking yourself out of a trigger fails once the body is in fear: '
                           'Perry\'s red line, where blood flow leaves the reasoning brain for the survival brain',
                      moment=WHO + '; you are starting the science section, which says what goes wrong in the brain '
                             'under trauma')
M.SPEC['p033'] = dict(heading='A. The Metabolic Red Line (in Part 1: THE SCIENCE)',
                      for_='the reader learns what working on trauma above the red line does (it adds armor), and so '
                           'why to stay within what they can handle',
                      moment=WHO + '; you have just read that above a "red line" (a racing resting heart rate) blood '
                             'flow leaves the reasoning brain for the survival brain')
TEXTS = {'sw18': lambda: T.plain(T.NEW['sw18']),
         'p030': lambda: T.plain(T.OLD['p030']),
         'p032': lambda: T.plain(T.OLD['p032']),
         'p033': lambda: T.plain(T.OLD['p033'])}

if __name__ == '__main__':
    keys = sys.argv[1:] or list(TEXTS)

    class _T:
        pass
    _T.TEXTS = TEXTS
    M.HERE = HERE / 'v1'
    M.T = _T
    M.main(keys)
