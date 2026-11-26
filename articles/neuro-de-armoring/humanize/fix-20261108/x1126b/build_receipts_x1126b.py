"""The receipt for this turn's text of mine (texts_x1126b.NEW['who']): the 5-HTP section's "Who this is for" with its
last sentence changed by his message of 2026-11-26 15:26 UTC and then fixed for sense after the three fresh reads of the
version with his change alone (v1/needed, v1/his-fixes, v1/fit: Fable, 2026-11-26).

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1126b/build_receipts_x1126b.py
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'x1123a'))
sys.path.insert(0, str(HERE.parent / 'x1123b'))
sys.path.insert(0, str(HERE))
import build_receipts_x1123b as BB  # noqa: E402
import texts_x1126b as T  # noqa: E402

B = BB.B
S = B.S
OUT = HERE / 'receipts'
OUT.mkdir(exist_ok=True)
B.HERE = OUT
MSG = 'his message of 2026-11-26 15:26 UTC (fix-20261108/joel-20261126-1526-message.txt)'
LATER = ('unchanged in this step, which carries his answer and the sense fix the reads asked for in the sentence it '
         'changes (S7); the paragraph read Human High as it stood (fix-20261104/checks/x1104o, b088m), and this mark is '
         'the first work of the 5-HTP section\'s next pass (HANDOFF), one change a try from a High read')


def v1(n):
    return S.sentences(T.plain(T.READ['who']))[n - 1]


def reader(kind):
    brief = {'needed': 'needed_read_brief.md', 'his-fixes': 'his_fixes_brief.md', 'fit': 'fit_read_brief.md'}[kind]
    return ('a fresh reader (Fable, 2026-11-26) given tools/humanization/%s and only the text, one sentence a line '
            '(x1126b/v1/%s/who/READ.md)' % (brief, kind))


def who():
    return B.build(
        'WHO1', T.plain(T.NEW['who']), 'Serotonin Bottleneck Pattern: 5-HTP + Low-Dose P5P, "Who this is for"',
        'an adult with trauma following this protocol, reading the 5-HTP section to decide whether to try it, who sleeps '
        'badly and sometimes takes mushrooms or MDMA',
        {'Who this is for:': ('they learn 5-HTP is not for every depressed person, before the pattern it fits', 'the '
                              'section\'s first paragraph', None),
         'It could help': ('they learn the first part of the pattern: trouble falling asleep and low mood with little '
                           'warmth', 'it turns from who it isn\'t for to who it could help', 'though'),
         'At night you': ('they learn the second part: anxiety at night and going over the same things', 'it adds to '
                          'the pattern', 'At night'),
         'It makes more sense': ('they learn a genetic or clinical reason makes it more likely to fit, with Scott as the '
                                 'case', 'it adds a second test of fit', 'more sense'),
         '5-HTP skips over': ('they learn why a responder feels it quickly, and not to expect too much', 'it explains why '
                              'the bottleneck matters', 'that bottleneck'),
         'I\'d avoid casually': ('they hold off if they are agitated or manic', 'it turns to who should not try it '
                                 'casually', 'none: it starts the second part of the paragraph, who should not try it, after the pattern and the case'),
         'And don\'t take it': ('they don\'t take 5-HTP with antidepressants, MDMA or anything else that raises '
                               'serotonin, and know why, with the full list at the top', 'it adds the second group who '
                               'should not take it', 'And')},
        'they decide whether 5-HTP fits their pattern, and what not to take it with',
        [('5-HTP with anything else that raises serotonin can cause serotonin syndrome', 'his warning at the top (card '
          'W-HTPTOP) and MedlinePlus (https://medlineplus.gov/ency/article/007272.htm)', 'yes: they don\'t take 5-HTP with those drugs',
          'kept'),
         ('serotonergic psychedelics as a reason to watch for serotonin syndrome', 'his comment on card W-HTPTOP ("it\'s '
          'not likely to be dangerous with them") and ' + MSG + ' ("that\'s up to them")', 'no', 'cut')],
        {'reader': reader('needed'), 'unneeded': [], 'kept': {}},
        {'reader': reader('his-fixes'),
         'marked': [{'s': v1(1), 'difference': '27, 10: who it is not for before who it is for; "either"'},
                    {'s': v1(2), 'difference': '21, 10, 3: a label for the pattern; "warmth" unclear; "though"'},
                    {'s': v1(3), 'difference': '12, 4: stands alone, not tied to the pattern; "the same things"'},
                    {'s': v1(4), 'difference': '10, 1, 4: "It makes more sense"; three ideas; TPH2 unexplained'},
                    {'s': v1(5), 'difference': '1, 9, 11, 4: four ideas; the limit in an "although" clause'},
                    {'s': v1(6), 'difference': '15, 4, 10: a don\'t with nothing to do instead; "casually"'},
                    {'s': v1(7), 'difference': '4, 7, 21: "watch out for ... risk" says no act; category words'}],
         'kept': {v1(n): LATER for n in range(1, 7)}},
        {'reader': reader('fit'),
         'marked': [{'s': v1(2), 'found': 'ANYWAY; CAN\'T TELL low-serotonin from trauma sleep and numbness'},
                    {'s': v1(3), 'found': 'ANYWAY; MISREAD: what 5-HTP does at night'},
                    {'s': v1(4), 'found': 'CAN\'T TELL without genetic data; FROM: a clinic\'s words'},
                    {'s': v1(6), 'found': 'ANYWAY; CAN\'T TELL night anxiety from agitation; MISREAD with S3'},
                    {'s': v1(7), 'found': 'CAN\'T TELL what to watch for or whether mushrooms count; FROM: pharmacology '
                     'words; MISREAD: "combine them, just keep an eye out"'}],
         'kept': {v1(n): LATER for n in (2, 3, 4, 6)}},
        'his post\'s "Who this is for": the pattern, Scott\'s TPH2 case, and not a casual experiment for the agitated, '
        'the manic, or anyone on serotonergic meds; his comment on W-HTPTOP and ' + MSG + ' take the psychedelics out',
        'the first paragraph of the 5-HTP section, where the post has it')


if __name__ == '__main__' and 'sw' not in sys.argv:
    bad = who()
    print('receipts:', 'FAIL' if bad else 'PASS')
    sys.exit(1 if bad else 0)


# The Software/Hardware paragraphs that read AI as they stood (x1126p), fixed for sense from their fresh reads.
def v1sw(key, n):
    return S.sentences(T.plain(T.OLD[key]))[n - 1]


def rsw(kind, key):
    brief = {'needed': 'needed_read_brief.md', 'his-fixes': 'his_fixes_brief.md', 'fit': 'fit_read_brief.md'}[kind]
    return ('a fresh reader (Fable, 2026-11-26) given tools/humanization/%s and only the paragraph as it stood, one sentence '
            'a line (x1126b/v1/%s/%s/READ.md)' % (brief, kind, key))


SEC = 'Psychology is the Software; Biology is the Hardware.'
WHO = 'an adult with trauma who has done years of therapy and still gets triggered, reading why the protocol starts with the body'


def sw19():
    return B.build(
        'SW19-1', T.plain(T.NEW['sw19']), SEC + ', after Perry\'s ratio of grown-ups to children', WHO + ', who lives '
        'mostly alone',
        {'That works out': ('they learn how far short of the grown-ups per child our brains evolved with we fall, about a '
                            'sixteenth, from Perry\'s ratio just before', 'it works out the ratio the paragraph before gives',
                            'That works out'),
         'So the empty feeling': ('they learn the emptiness they feel is that missing company, and that the guide calls it '
                                  'the Void', 'it says what that shortfall feels like', 'So'),
         'Once you\'ve de-armored': ('they learn a lonely life will feel worse once the armor is off', 'it says what the '
                                     'shortfall means after the protocol', 'none: it turns from now to after '
                                     'de-armoring, which the next sentence answers'),
         'Gather a tribe': ('they gather people they\'re close to and see most days, and know the armor comes back '
                            'without them', 'it gives the act the sentence before calls for', 'Gather')},
        'they learn how little company modern life gives us, and what to do about it once they de-armor',
        [('about one-sixteenth of the grown-ups per child', 'Perry\'s ratio in the paragraph before (4 mature adults per '
          'child then, 1 immature adult per 4 children now) and his approved card SC-24 (Perry, 2023)', 'yes: they see '
          'the size of the shortfall', 'kept'),
         ('the Void', 'the guide\'s own term for the gray, empty state (Scenario C, Weeks 3 to 7)', 'yes: they know the '
          'emptiness has a name they will meet again', 'kept')],
        {'reader': rsw('needed', 'sw19'), 'unneeded': [v1sw('sw19', 2), v1sw('sw19', 4)], 'kept': {}},
        {'reader': rsw('his-fixes', 'sw19'),
         'marked': [{'s': v1sw('sw19', n), 'difference': d} for n, d in (
             (1, '4, 21, 11: "relational density" counts nothing; opens on the measure'),
             (2, '18, 12, 10: a short line tied to nothing; "Void" and "real" unexplained'),
             (3, '3, 14, 10, 27: "cannot simply return" corrects nobody; reads two ways'),
             (4, '5, 13, 21, 4, 15, 1, 10, 6: a rule with no act; labels; a wise-sounding end'))],
         'kept': {}},
        {'reader': rsw('fit', 'sw19'),
         'marked': [{'s': v1sw('sw19', 1), 'found': 'CAN\'T TELL what it counts; FROM: a number with no source said'},
                    {'s': v1sw('sw19', 3), 'found': 'CAN\'T TELL when it applies; MISREAD: life will be unbearable'},
                    {'s': v1sw('sw19', 4), 'found': 'CAN\'T TELL how many or how often; MISREAD: don\'t bother alone'}],
         'kept': {}},
        'his post\'s line, with his approved card SC-24\'s figure and source: we live on far less of the company our '
        'biology expects, the Void is real, a de-armored person can\'t go back to a lonely life, and without a tribe the '
        'brain reaches for the armor again "just to survive the cold"',
        'after the Gibson and Perry paragraph, where the post has it')


def sw22(name, text, both):
    spec = {'The Anti-Breakthrough': ('they learn an alarmed brain can take in healing work for only seconds at a time, '
                                      'from Perry', 'the next idea of the section', None),
            'So for now we': ('they set aside the hour-long breakthrough for now, knowing why', 'it follows from the '
                              'seconds-long window', 'So'),
            'Instead, this protocol': ('they learn the protocol works in doses of seconds, and what micro-dosing means '
                                       'here', 'it gives the act the two before call for', 'Instead')}
    marked_h = [{'s': v1sw('sw22', n), 'difference': d} for n, d in (
        (1, '11, 5, 13, 4, 21, 7: the source before the point; labels; no act'),
        (2, '3, 6, 18, 21, 8, 10, 4: "a flood, not a fix"; "metabolize ... processing"'),
        (3, '5, 9, 12, 8, 28, 4, 21, 10, 6, 7: the authority first; "therapeutic window" unexplained'))]
    marked_f = [{'s': v1sw('sw22', 1), 'found': 'MISREAD: "Micro-Dosing" as the drug doses; "abandon therapy"'},
                {'s': v1sw('sw22', 2), 'found': 'CAN\'T TELL if it is me; MISREAD: my therapy hours harmed me'},
                {'s': v1sw('sw22', 3), 'found': 'CAN\'T TELL what to do with seconds; FROM; MISREAD: a dose range'}]
    unneeded = [v1sw('sw22', 2)]
    checked = [('the window is often only seconds long', 'his post, from Dr. Perry', 'yes: they work in doses of '
                'seconds', 'kept'),
               ('an hour of trauma work overwhelms an armored nervous system', 'his post ("that is a flood, not a fix")',
                'yes: they set the hour-long session aside for now', 'kept')]
    if both:
        spec.update({'Your goal is': ('they do 30 seconds of slow, steady breathing twenty times a day', 'it gives the '
                                      'practice the paragraph before leads to', 'Your goal'),
                     'It works the way': ('they keep sessions short and many, as physical therapy does with a knee',
                                          'it says why short and often', 'It works')})
        marked_h += [{'s': v1sw('sw23', n), 'difference': d} for n, d in (
            (1, '21, 13, 4: "Micro-Dosing Safety" a label; "regulated breathing" unexplained'),
            (2, '3, 2, 21: "not a marathon; physical therapy" the not-X-Y turn'),
            (3, '18, 6, 16: a three-word slogan at the end'))]
        marked_f += [{'s': v1sw('sw23', 1), 'found': 'CAN\'T TELL the breathing pattern; MISREAD: microdosing drugs'}]
        unneeded += [v1sw('sw23', 2)]
        checked += [('30 seconds of breathing, twenty times a day', 'his post', 'yes: they breathe that way for 30 seconds, twenty '
                    'times a day', 'kept')]
    return B.build(
        name, text, SEC + ', the Anti-Breakthrough', WHO + ', used to hour-long therapy sessions', spec,
        'they learn why the protocol works in seconds-long doses' + (', and the daily practice' if both else ''),
        checked,
        {'reader': rsw('needed', 'sw22') + (' and x1126b/v1/needed/sw23/READ.md' if both else ''), 'unneeded': unneeded,
         'kept': {}},
        {'reader': rsw('his-fixes', 'sw22') + (' and x1126b/v1/his-fixes/sw23/READ.md' if both else ''),
         'marked': marked_h, 'kept': {}},
        {'reader': rsw('fit', 'sw22') + (' and x1126b/v1/fit/sw23/READ.md' if both else ''), 'marked': marked_f,
         'kept': {}},
        'his post\'s Anti-Breakthrough: give up the hour-long breakthrough for now; an armored nervous system can\'t take '
        'an hour of trauma work; Perry finds the window is often seconds long' + ('; and the goal, 30 seconds of breathing '
        'twenty times a day, frequency over intensity' if both else ''),
        'where the post has it, before Part 1')


if __name__ == '__main__' and 'sw' in sys.argv:
    bad = sw19() + sw22('SW22-1', T.plain(T.NEW['sw22']), False) + sw22(
        'SW22-23-1', T.plain(T.NEW['sw22']) + '\n\n' + T.plain(T.NEW['sw23']), True)
    print('receipts:', 'FAIL' if bad else 'PASS')
