"""The receipt for N58B, his answer 58 fitted after the Weeks 1-2 daily list (revise_n58b.py), from the three fresh reads
of the first fit (needed/n58, his-fixes/n58, fit/n58: Fable readers given needed_read_brief.md, his_fixes_brief.md and
fit_read_brief.md, 2026-11-24). Every sentence they marked is changed in N58B; the two clauses the needed read called
extras are his points (his answer 58), kept with that reason.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1124a/build_receipts_x1124a.py
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'x1123a'))
sys.path.insert(0, str(HERE))
import build_receipts_x1123a as B  # noqa: E402
import texts_x1124a as T  # noqa: E402

B.HERE = HERE
S = B.S


def reader(kind):
    brief = {'needed': 'needed_read_brief.md', 'his-fixes': 'his_fixes_brief.md', 'fit': 'fit_read_brief.md'}[kind]
    return ('a fresh reader (Fable, 2026-11-24) given tools/humanization/%s and only the text, one sentence a line, of the '
            'first fit of his answer 58 (x1124a/%s/n58/READ.md)' % (brief, kind))


def main():
    old = S.sentences((HERE / 'needed' / 'n58' / 'TEXT.txt').read_text(encoding='utf-8').strip())
    assert len(old) == 5, len(old)
    bad = B.build(
        'N58B', T.N58(), 'Part 5: The Timeline, Weeks 1-2: the note right after the daily supplement list (his answer 58)',
        'an adult with trauma setting up the first two weeks\' daily supplements from the list just above, which names zinc '
        'and L-serine without amounts',
        {"For the zinc, I'd use": ('they learn which zinc to buy for the list above and why this form: easier on the '
                                   'stomach than other zinc, and good for a leaky gut', 'it picks up the list\'s "with zinc '
                                   'at night" right above it', None),
         'A standard dose is': ('they learn how much to take a day, what that holds in elemental zinc (the number a label '
                                'may give), and what to do if it makes them queasy', 'it gives the amount for the form '
                                'just chosen', 'A standard dose'),
         'Zinc can lower your': ('they learn to take copper too, why, how much a day, and which form to buy and which to '
                                 'skip', 'it adds what the zinc calls for', 'Zinc can lower your copper'),
         'For L-serine,': ('they learn the L-serine range for the list above, a day, adjusted by how it feels', 'it turns '
                           'to the list\'s other item without an amount', 'For L-serine'),
         'Higher doses bring': ('they learn why to stay in that range (more stomach trouble higher up) and how far trials '
                                'have gone, so the 30 g isn\'t a target', 'it gives the limit on the range before it',
                                'Higher doses')},
        'they learn at once which zinc to take for the list just above, and why that one',
        [('zinc carnosine helps repair leaky gut', 'Mahmood 2007 (Gut): 37.5 mg twice daily kept healthy volunteers\' gut '
          'permeability from rising on indomethacin; Davison 2016 (AJCN): it cut the rise in gut permeability after heavy '
          'exercise by 70%', 'yes: they pick zinc carnosine over a cheaper zinc, knowing what it does for their gut too (his reason, his answer 58)', 'kept'),
         ('L-serine up to 30 g a day in trials for neurodegenerative conditions, more stomach trouble higher',
          'Levine 2017 (phase I trial in ALS): up to 15 g twice daily, generally well tolerated, two of 20 left with '
          'stomach problems', 'yes: they keep to 5-15 g and don\'t chase higher doses, knowing trials went to 30 g and the stomach suffers above the range (his point, his answer 58)',
          'kept')],
        {'reader': reader('needed'), 'unneeded': [old[1], old[4]],
         'kept': {old[1]: 'only its first clause was called an extra (leaky gut): it is his point in his answer 58 and his '
                          'reason for this form, so it stays, now beside the choice in the first sentence',
                  old[4]: 'only its first clause was called an extra (the trials\' 30 g): it is his point in his answer 58, '
                          'now after the stomach limit, so it reads as how far trials went'}},
        {'reader': reader('his-fixes'),
         'marked': [{'s': old[0], 'difference': '10'}, {'s': old[1], 'difference': '1, 13, 15'},
                    {'s': old[2], 'difference': '5, 13, 27, 4'}, {'s': old[3], 'difference': '10, 4'},
                    {'s': old[4], 'difference': '9, 3, 10'}], 'kept': {}},
        {'reader': reader('fit'),
         'marked': [{'s': old[0], 'found': 'can\'t tell: one capsule or the day\'s total; misread: 75 mg read as zinc'},
                    {'s': old[1], 'found': 'can\'t tell: split the dose or lower the total'},
                    {'s': old[2], 'found': 'can\'t tell: why copper, per day, at the same moment; misread: swallow together'},
                    {'s': old[3], 'found': 'can\'t tell: what to feel for, per day or per dose'},
                    {'s': old[4], 'found': 'from: trials in other conditions; misread: permission to go to 30 g'}],
         'kept': {}},
        'read the article for zinc, copper and L-serine amounts: the daily list right above names zinc and L-serine without '
        'amounts (his 41a), section B\'s "The Lock" and "The Repair" say what they do, and no other place gives an amount',
        'right after the Weeks 1-2 daily list it gives the amounts for, before the agmatine add-on')
    print('\n'.join(bad) or 'N58B receipt: PASS')


if __name__ == '__main__':
    main()
