"""The fresh readers' briefs for x1125a's texts (texts_x1125a), as make_briefs_x1123a.py makes them: the needed read,
the read against his fixes and the fit read, into needed/KEY, his-fixes/KEY and fit/KEY.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1125a/make_briefs_x1125a.py VERSION [KEY ...]
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'x1123a'))
sys.path.insert(0, str(HERE))
import make_briefs_x1123a as M  # noqa: E402
import texts_x1125a as T  # noqa: E402

TOP = 'A Complete Guide to Bio-De-Armoring (the warnings at the top, before the protocol starts)'
YOU = ('you are an adult with trauma who has read the short introduction (this guide is for the "hardened neural '
       'pathways", the armor, and comes after fixing general health) and is reading the warnings before starting; ')
M.SPEC.update({
    'dmso': dict(heading=TOP, for_='the reader learns what DMSO is, which kind to buy and how to handle it before the '
                                   'protocol has them smell it',
                 moment=YOU + 'you have never used DMSO'),
    'elec': dict(heading=TOP, for_='the reader with kidney disease or a heart condition learns to see a doctor before the '
                                   'protocol\'s potassium, and why',
                 moment=YOU + 'you may have a kidney or heart condition, or take blood pressure pills'),
    'ethno': dict(heading=TOP, for_='the reader learns that the protocol\'s two plant medicines are illegal in many places '
                                    'and risky, and never to mix iboga with most medications',
                  moment=YOU + 'you may be on medication and have never taken iboga'),
    'iso': dict(heading=TOP, for_='the reader learns to cut back on excitement without cutting themselves off from '
                                  'people, and why being alone works against the protocol',
                moment=YOU + 'you tend to withdraw from people when you are working on yourself'),
    'rule': dict(heading=TOP + ', right after the Isolation Trap paragraph',
                 for_='the reader learns which kind of company to look for and which to avoid during the protocol',
                 moment=YOU + 'you have just read that the protocol starves the brain of excitement but you shouldn\'t '
                              'isolate'),
    'cog': dict(heading=TOP, for_='the reader learns they will feel exposed as the armor comes off and that others '
                                  'can\'t actually see their anxiety',
                moment=YOU + 'you get anxious around people'),
    'proj': dict(heading=TOP + ', the second paragraph of the Cognitive Warning (the first says you will feel exposed '
                               'and assume everyone can see your anxiety)',
                 for_='the reader learns not to trust their read of other people during the protocol, and how to tell '
                      'when they can',
                 moment=YOU + 'you often feel judged in a room and can check your own pulse'),
    'agm': dict(heading=TOP + ', the Agmatine Warning; a list of precautions (what not to combine it with) follows it',
                for_='the reader learns that agmatine, an optional supplement in the protocol, acts on several brain '
                     'systems at once, which is why the precautions that follow apply',
                moment=YOU + 'you take some medication and are deciding whether agmatine is worth trying'),
    'htp': dict(heading=TOP + ', the warning for people who use psychedelics',
                for_='the reader who uses psychedelics learns what not to combine 5-HTP with, and to keep it away from '
                     'trips, ayahuasca and iboga',
                moment=YOU + 'you use psychedelics now and then and may take an antidepressant or other medication'),
    'uri': dict(heading=TOP + ', the warning for people who use psychedelics; the paragraph before it covers 5-HTP',
                for_='the reader who uses psychedelics learns what uridine (UMP) may change and to keep it off trip days',
                moment=YOU + 'you use psychedelics now and then and know your usual dose'),
})

if __name__ == '__main__':
    ver, keys = sys.argv[1], sys.argv[2:]
    V = T.VERSIONS[ver]
    T.TEXTS = {k: (lambda k=k: T.plain(V[k])) for k in V}
    M.HERE = HERE / ver
    M.T = T
    M.main(keys or list(V))
