"""The receipt for L61B: his Weeks 3-7 line (his version on card W35, which he checked himself: Human Written, one
window, High) with 61a's words in and, for his 65a, his last sentence moved up to right after the permission it limits,
so the numbness test ends the line and names what the numb reader can't tell. The reads are the three fresh reads of the
line before the move (x1124a/needed/l61, his-fixes/l61, fit/l61: Fable readers, 2026-11-24); what all three found is
what the move fixes, and the marks on his own sentences are kept with the reason each stays.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1124b/build_receipts_x1124b.py
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'x1123a'))
sys.path.insert(0, str(HERE.parent / 'x1123b'))
sys.path.insert(0, str(HERE.parent / 'x1124a'))
import build_receipts_x1123b as BB  # noqa: E402  (its fill allows a link of "none: why")
import texts_x1124a as T  # noqa: E402

B = BB.B
B.HERE = HERE
S = B.S
OLD = HERE.parent / 'x1124a'


def reader(kind):
    brief = {'needed': 'needed_read_brief.md', 'his-fixes': 'his_fixes_brief.md', 'fit': 'fit_read_brief.md'}[kind]
    return ('a fresh reader (Fable, 2026-11-24) given tools/humanization/%s and only the text, one sentence a line, of his '
            'line before his 65a moved its last sentence up (x1124a/%s/l61/READ.md)' % (brief, kind))


def main():
    old = S.sentences((OLD / 'needed' / 'l61' / 'TEXT.txt').read_text(encoding='utf-8').strip())
    assert len(old) == 5, len(old)
    his = 'his own sentence, from his version on card W35, which he checked himself (Human Written, one window, High); '
    bad = B.build(
        'L61B', T.L61(), 'Part 5: The Timeline, Weeks 3-7: The Void (Depression Phase), the line at its top (card W35)',
        'an adult with trauma in the gray, numb weeks after the anxiety phase, about to add UMP, 5-HTP or a microdose and '
        'wanting to know what is safe together and how to tell what works',
        {'So you can tell': ('they add the phase\'s new things one at a time, in the list\'s order, so they can tell what '
                             'each one does', 'it opens the phase, right after its State line', None),
         '5-HTP could help': ('they learn 5-HTP may lift their mood in this phase and the one firm don\'t: none at all '
                              'while microdosing iboga or elliptica', 'it takes one of the new things the first sentence '
                              'says to add, the one with a hard limit', '5-HTP'),
         "There isn't enough data": ('they learn the two combos nobody has data on and that they may try them and judge '
                                     'for themselves', 'it goes from the one combo that is ruled out to the ones that '
                                     'aren\'t', 'none: it turns from the one firm don\'t to the combos nobody has data on'),
         'Mushrooms act on serotonin': ('they learn the limit on the combo just allowed: stop the 5-HTP at any of its '
                                        'stop signs, since mushrooms act on serotonin too', 'it limits the permission '
                                        'the sentence before gives (his 65a put it here)', 'Mushrooms act on serotonin too'),
         "If you're too numb": ('they get a way to tell how a combo feels when numbness hides it: compare sleep and dreams '
                                'after a microdose day and after a day without', 'it answers "see how it feels" for the '
                                'reader this phase leaves too numb to feel it', 'too numb to tell how a combo feels')},
        'they learn at once to add the phase\'s new things one at a time, in the list\'s order, so they can tell what each '
        'one does',
        [],
        {'reader': reader('needed'), 'unneeded': [], 'kept': {}},
        {'reader': reader('his-fixes'),
         'marked': [{'s': old[1], 'difference': '10, 4, 12'}, {'s': old[2], 'difference': '16, 28, 11, 8, 10'},
                    {'s': old[3], 'difference': '10, 4, 13'}, {'s': old[4], 'difference': '28, 12, 3, 7'}],
         'kept': {old[1]: his + '"here" is the Void phase the line opens, named in the State line right above it, and the '
                          '5-HTP section has already said 5-HTP raises serotonin; his words stay his',
                  old[2]: his + 'what the readers found in it, a caution arriving two sentences late, is fixed by moving '
                          'his next sentence up (his 65a), and the last sentence now names what "how it feels" is about; '
                          'the order inside it (the gap in the data, then what to do) is his',
                  old[4]: his + 'it now sits right after the permission it limits (his 65a), which is what the readers '
                          'asked for; the stop signs stay a link away in the 5-HTP section, the one place the article '
                          'lists them'}},
        {'reader': reader('fit'),
         'marked': [{'s': old[2], 'found': 'can\'t tell: what feeling counts; misread: an all-clear, the caution comes late'},
                    {'s': old[3], 'found': 'anyway: sleep and dreams vary; can\'t tell: which difference means it works'},
                    {'s': old[4], 'found': 'can\'t tell: the stop signs aren\'t named here'}],
         'kept': {old[2]: his + 'the misreading (an all-clear) came from the caution standing two sentences later, and '
                          'his 65a moves it to right after this sentence',
                  old[4]: his + 'the stop signs are linked, in the 5-HTP section, where the article lists them once'}},
        'read Weeks 3-7 from its heading to Week 8+ for adding things one at a time and for 5-HTP or UMP with microdoses: '
        'the UMP and 5-HTP trials below give each trial\'s own rules (which name a trip since his 64a), and this line is '
        'the only place that covers microdoses with them',
        'at the top of the Void phase (Weeks 3-7), right after its State line and before its Protocol, where his card W35 '
        'put it: it tells the reader how to take the list that follows')
    print('\n'.join(bad) or 'L61B receipt: PASS')


if __name__ == '__main__':
    main()
