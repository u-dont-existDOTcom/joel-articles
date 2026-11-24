"""The fresh readers' briefs for x1124a's texts (texts_x1124a), as make_briefs_x1123a.py makes them.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1124a/make_briefs_x1124a.py KEY ...
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'x1123a'))
sys.path.insert(0, str(HERE))
import make_briefs_x1123a as M  # noqa: E402
import texts_x1124a as T  # noqa: E402

M.HERE = HERE
M.T = T
M.SPEC['l61'] = dict(heading='Part 5: The Timeline, Weeks 3-7: The Void (Depression Phase), the line at its top',
                     for_='the reader learns to add the Void phase\'s new things one at a time, what not to combine with '
                          'iboga or mushroom microdoses, and how to tell what helps when they feel too numb to tell',
                     moment='you are an adult with trauma in the gray, numb weeks after the anxiety phase, about to add '
                            'UMP, 5-HTP or a microdose and wanting to know what is safe together and how to tell what works')
M.SPEC['n58'] = dict(heading='Part 5: The Timeline, Weeks 1-2, right after the daily supplement list',
                     for_='the reader learns which zinc to take and how much, the copper to take with it, and how much '
                          'L-serine, for the daily list just above',
                     moment='you are an adult with trauma setting up the first two weeks\' daily supplements from the list '
                            'just above, which names zinc and L-serine without amounts')

if __name__ == '__main__':
    M.main(sys.argv[1:])
