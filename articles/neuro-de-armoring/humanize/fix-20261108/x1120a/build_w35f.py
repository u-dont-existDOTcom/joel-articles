"""The receipts for the Weeks 3-5 line (texts_x1120a), his answers 16a and 17 of 2026-11-20, before each Pangram check
by itself: W35F (try 1; reads needed/w35e, his-fixes/w35e and fit/w35e, fresh Haiku readers of W35E, every sentence they
marked changed) and W35H (try 2; reads of W35G in w35g, its two-way words changed and the rest waiting on the near-miss
rule) W35J (try 3; the read against his fixes of W35I in his-fixes/w35i) and W35L (try 4; that read of W35K in
his-fixes/w35k) W35N (try 5; that read of W35M in his-fixes/w35m) and W35P (refused before its check; the read of W35O) and W35R
(try 6; the read of W35Q in his-fixes/w35q, after the tell panel, panel-w35p), as texts_x1120a's notes say.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1120a/build_w35f.py [W35F|W35H|W35J|W35L|W35N|W35P|W35R]
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import sense_receipt as S  # noqa: E402
import texts_x1120a as T  # noqa: E402

KEY = sys.argv[1] if len(sys.argv) > 1 else 'W35F'
READS = {'W35F': 'w35e', 'W35H': 'w35g', 'W35J': 'w35g', 'W35L': 'w35g', 'W35N': 'w35g', 'W35P': 'w35g', 'W35R': 'w35g'}[KEY]
READ_OF = {'W35F': 'W35E', 'W35H': 'W35G', 'W35J': 'W35G', 'W35L': 'W35G', 'W35N': 'W35G', 'W35P': 'W35G', 'W35R': 'W35G'}[KEY]
# the read against his fixes is made again before each check (AGENTS.md); the needed and fit reads of W35G stand for
# W35J, whose changes since are the two-way words and the reader as the subject of S5
HIS_READS, HIS_READ_OF = {'W35J': ('w35i', 'W35I'), 'W35L': ('w35k', 'W35K'), 'W35N': ('w35m', 'W35M'), 'W35P': ('w35o', 'W35O'), 'W35R': ('w35q', 'W35Q')}.get(KEY, (READS, READ_OF))
WAIT = ('it waits: from the near miss (W35F, a Human window) only words a reader could take two ways change until two '
        'small tries are checked (lesson bad-trips-2026-11-19b; pangram_ledger.py refuses more)')


def reader_line(kind):
    brief = {'needed': 'needed_read_brief.md', 'his-fixes': 'his_fixes_brief.md', 'fit': 'fit_read_brief.md'}[kind]
    reads, of = (HIS_READS, HIS_READ_OF) if kind == 'his-fixes' else (READS, READ_OF)
    return ('a fresh reader (Haiku, 2026-11-23) given tools/humanization/%s and only the text %s, one sentence a line '
            '(x1120a/%s/%s/READ.md)' % (brief, of, kind, reads))


def main():
    text = getattr(T, KEY)
    s = S.sentences(text)
    e = S.sentences(getattr(T, READ_OF))
    assert len(s) == 6, len(s)
    reader = ('someone with trauma in the numb, gray phase of weeks 3 to 5 (the "Void"), about to start its UMP and 5-HTP '
              'trials, an iboga, elliptica or mushroom microdose and the keto diet, who needs to know in what order, and '
              'whether UMP or 5-HTP can go with a microdose day')
    spec = {
        'So you can tell what each': (
            'they learn to add the phase\'s new things one at a time, in the order the list below gives them, from the UMP '
            'trial to the keto diet, so they can tell which change did what',
            'it opens the plan the heading and its State line set up ("the world turns gray/boring"), before the list '
            'it puts in order', None),
        '5-HTP could help your mood here': (
            'they learn the one pairing that is a firm no, 5-HTP while microdosing iboga or elliptica, and why (iboga '
            'acts on serotonin too), so they leave 5-HTP out for as long as they microdose iboga',
            'once the order is set, the first thing the reader asks is what may go together; the firm no comes first',
            'could help your mood here'),
        'But if you want UMP with any microdose': (
            'they learn that for UMP with a microdose, or 5-HTP with a mushroom microdose, nobody can say yet whether the '
            'psychedelic-day warnings apply, so a microdose day is neither ruled out nor cleared',
            'it turns from the one settled pairing to the ones that are not', 'But if you want'),
        'Until there': (
            'they learn what to do about the unknown: try the supplement on days they microdose and on days they don\'t, '
            'and compare (his answer 17: "people can try each way to see how it feels")',
            'it answers the unknown the sentence before states', 'Until there'),
        'For now': (
            'they learn what to do about the unknown for now: try the supplement on a microdose day and on a day without, '
            'and compare (his answer 17: "people can try each way to see how it feels")',
            'it answers the gap the sentence before states, for as long as it lasts', 'For now'),
        'Mushrooms act on serotonin too': (
            'they learn why 5-HTP with mushrooms needs watching but isn\'t ruled out like iboga, and when to stop it: at '
            'any stop sign the 5-HTP section lists',
            'it closes the mushroom pairing\'s trial with its one hard limit, and says why it differs from the iboga no',
            'Mushrooms act on serotonin too'),
        'So until there': (
            'they learn what to do about the unknown: try the supplement on a microdose day and on a day without, and '
            'compare (his answer 17: "people can try each way to see how it feels")',
            'it answers the unknown the sentence before states, joined by his own "so"', 'So until there'),
        'If ': (
            'they learn what to compare when they can\'t feel much: how they sleep and dream, the first changes the UMP and '
            '5-HTP sections say to expect',
            'it answers what a numb reader can\'t do in the sentence before, "see how each feels"',
            None),
        'Like iboga, mushrooms act on serotonin': (
            'they learn why 5-HTP with mushrooms needs watching and when to stop it: at any stop sign the 5-HTP section '
            'lists',
            'it closes the mushroom pairing\'s trial with its one hard limit, tied back to the reason given for iboga',
            'Like iboga')}
    r = S.make(text, 'Weeks 3–5: The Dynorphin Void (Depression Phase), a new first line', reader)
    for x in r['sentences']:
        (k,) = [k for k in spec if x['s'].startswith(k)]
        x['payoff'], x['follows'] = spec[k][0], spec[k][1]
        if 'link' in x:
            link = spec[k][2] or x['s'].split(',')[0]  # S5: its opening clause, "If ... tell"
            assert link in x['s'], (k, link)
            x['link'] = link
    r['opens'] = {'first_sentence': s[0], 'why_reading': (
        'they learn how to start the phase\'s new things so they can tell which one does what, which they need before '
        'starting any of the trials and microdoses listed below')}
    r['checked'] = [
        {'point': 'iboga acts on serotonin (S2)',
         'found': 'ibogaine and its metabolite noribogaine block the serotonin transporter, the pump SSRIs also block '
                  '(Bulling et al. 2012, J Biol Chem, PMC3365767; Coleman et al. 2019, Nature, PMC6750207)',
         'still_needed': 'yes: they learn why 5-HTP with iboga is a firm no, so they keep the two apart',
         'fate': 'kept'},
        {'point': 'mushrooms act on serotonin (S6)',
         'found': 'psilocybin\'s active form, psilocin, is an agonist at many serotonin receptors, mainly 5-HT2A (Ling et '
                  'al. 2022, CNS Drugs, PMID 34791625)',
         'still_needed': 'yes: they learn why 5-HTP with mushrooms needs watching, so they stop it at its stop signs',
         'fate': 'kept'},
        {'point': 'elliptica with 5-HTP (S2)',
         'found': 'the article calls Tabernanthe elliptica "healer" iboga, "an iboga cousin with many iboga alkaloids" '
                  '(his 32b line); his answer 17 bars iboga with 5-HTP, and S2 reads that as covering elliptica, named in '
                  'the turn\'s report for him to undo',
         'still_needed': 'yes: they learn where 5-HTP stands with the microdose the article says to try first',
         'fate': 'kept'},
        {'point': 'sleep and dreams as what to compare (S5)',
         'found': 'the 5-HTP section: "the first things you\'ll usually notice are your mood or sleep quality improves, '
                  'you have less nighttime rumination, and your dreams become more vivid"; the UMP section: "Vivid dreams '
                  '... are the hoped-for benefits of UMP"',
         'still_needed': 'yes: they learn what to compare when they can\'t feel much',
         'fate': 'kept'}]
    r['needed'] = {'reader': reader_line('needed'), 'unneeded': [], 'kept': {}}
    if KEY == 'W35F':
        r['his_fixes'] = {'reader': reader_line('his-fixes'),
                          'marked': [{'s': e[1], 'difference': '14'}, {'s': e[3], 'difference': '4'},
                                     {'s': e[4], 'difference': '10'}],
                          'kept': {}}
        r['fit'] = {'reader': reader_line('fit'),
                    'marked': [{'s': e[2], 'found': 'can\'t tell: whether the psychedelic-day warning covers their '
                                                    'microdose, since the line says the data can\'t say'},
                               {'s': e[3], 'found': 'can\'t tell: a numb reader judging how a supplement feels; misread: '
                                                    'the try reads as leave the earlier rule forbids'}],
                    'kept': {s[2]: 'the unknown is his answer to question 17 ("there isn\'t enough data to make a '
                                   'suggestion about this"); the line says it so the reader neither assumes the warnings '
                                   'cover a microdose nor that they don\'t, and S4 gives the act',
                             s[3]: 'the try is his answer 17 ("people can try each way to see how it feels"), and S3 says '
                                   'why the warnings don\'t settle it; S5 now gives a numb reader sleep and dreams to '
                                   'compare'}}
    elif KEY == 'W35R':
        h = S.sentences(T.W35Q)
        r['his_fixes'] = {'reader': reader_line('his-fixes'),
                          'marked': [{'s': h[2], 'difference': '1'}, {'s': h[3], 'difference': '12'},
                                     {'s': h[5], 'difference': '17'}],
                          'kept': {h[2]: 'way 1 (the gap, the warnings and the microdose days in one sentence): its window '
                                         'read Human High in tries 3 and 4, and it states his answer 17 whole; ' + WAIT}}
        r['fit'] = {'reader': reader_line('fit'),
                    'marked': [{'s': e[2], 'found': 'misread: "there isn\'t enough data yet to say whether the warnings '
                                                    '... apply" can sound like they don\'t apply, which reassures'}],
                    'kept': {e[2]: 'the unknown is his answer to question 17 ("there isn\'t enough data to make a '
                                   'suggestion about this"), neither a yes nor a no, and S4 gives the act; ' + WAIT}}
    elif KEY == 'W35P':
        h = S.sentences(T.W35O)
        r['his_fixes'] = {'reader': reader_line('his-fixes'),
                          'marked': [{'s': h[1], 'difference': '3'}, {'s': h[2], 'difference': '1'},
                                     {'s': h[3], 'difference': '10'}, {'s': h[4], 'difference': '4'}],
                          'kept': {h[1]: 'way 3 (the help 5-HTP could give set against the risk): the reader would want '
                                         '5-HTP here (way 14 asked for that), and its window read Human High in tries 3 '
                                         'and 4; ' + WAIT,
                                   h[2]: 'way 1 (the two pairings, the gap and the question in one sentence): its window '
                                         'read Human High in tries 3 and 4, and it states his answer 17 whole; ' + WAIT,
                                   h[4]: 'way 4 ("each kind of day"): S4 names the two days again in this try ("a '
                                         'microdose day and a day without"), so the phrase has them to point to'}}
        r['fit'] = {'reader': reader_line('fit'),
                    'marked': [{'s': e[2], 'found': 'misread: "there isn\'t enough data yet to say whether the warnings '
                                                    '... apply" can sound like they don\'t apply, which reassures'}],
                    'kept': {e[2]: 'the unknown is his answer to question 17 ("there isn\'t enough data to make a '
                                   'suggestion about this"), neither a yes nor a no, and S4 gives the act; ' + WAIT}}
    elif KEY == 'W35N':
        h = S.sentences(T.W35M)
        r['his_fixes'] = {'reader': reader_line('his-fixes'),
                          'marked': [{'s': h[2], 'difference': '1'}, {'s': h[3], 'difference': '10'},
                                     {'s': h[5], 'difference': '8'}],
                          'kept': {h[2]: 'way 1 (the two pairings, the gap and the question in one sentence): its window '
                                         'read Human High in tries 3 and 4, and it states his answer 17 whole; ' + WAIT,
                                   h[5]: 'way 8 (", so"): its window read Human High in tries 3 and 4, and "so" is a join '
                                         'his own fixes make (way 8 itself); ' + WAIT}}
        r['fit'] = {'reader': reader_line('fit'),
                    'marked': [{'s': e[2], 'found': 'misread: "there isn\'t enough data yet to say whether the warnings '
                                                    '... apply" can sound like they don\'t apply, which reassures'}],
                    'kept': {e[2]: 'the unknown is his answer to question 17 ("there isn\'t enough data to make a '
                                   'suggestion about this"), neither a yes nor a no, and S4 gives the act; ' + WAIT}}
    elif KEY == 'W35L':
        h = S.sentences(T.W35K)
        r['his_fixes'] = {'reader': reader_line('his-fixes'), 'marked': [{'s': h[3], 'difference': '10'}], 'kept': {}}
        r['fit'] = {'reader': reader_line('fit'),
                    'marked': [{'s': e[2], 'found': 'misread: "there isn\'t enough data yet to say whether the warnings '
                                                    '... apply" can sound like they don\'t apply, which reassures'}],
                    'kept': {e[2]: 'the unknown is his answer to question 17 ("there isn\'t enough data to make a '
                                   'suggestion about this"), neither a yes nor a no, and S4 gives the act; ' + WAIT}}
    elif KEY == 'W35J':
        h = S.sentences(T.W35I)
        r['his_fixes'] = {'reader': reader_line('his-fixes'),
                          'marked': [{'s': h[1], 'difference': '10, 8'}, {'s': h[2], 'difference': '1'},
                                     {'s': h[4], 'difference': '10'}, {'s': h[5], 'difference': '8'}],
                          'kept': {h[1]: 'way 10 ("here"): in the article it follows the Weeks 3-5 heading and the '
                                         'order line, so "here" is this phase, and its window read Human High in W35H; '
                                         'way 8 ("though ... so"): ' + WAIT,
                                   h[2]: 'way 1 (the condition, the gap and the question in one sentence); ' + WAIT,
                                   h[5]: 'way 8 (", so"): ' + WAIT}}
        r['fit'] = {'reader': reader_line('fit'),
                    'marked': [{'s': e[2], 'found': 'misread: "there isn\'t enough data yet to say whether the warnings '
                                                    '... apply" can sound like they don\'t apply, which reassures'}],
                    'kept': {e[2]: 'the unknown is his answer to question 17 ("there isn\'t enough data to make a '
                                   'suggestion about this"), neither a yes nor a no, and S4 gives the act; ' + WAIT}}
    else:
        r['his_fixes'] = {'reader': reader_line('his-fixes'),
                          'marked': [{'s': e[1], 'difference': '8'}, {'s': e[2], 'difference': '1'},
                                     {'s': e[3], 'difference': '10'}, {'s': e[4], 'difference': '10'},
                                     {'s': e[5], 'difference': '8, 13'}],
                          'kept': {e[1]: 'way 8 as the reader gives it (a benefit and a warning joined by "though" and '
                                         '"so"); ' + WAIT + '; it read Human (Low) in W35F, the near miss\'s one Human '
                                         'window',
                                   e[2]: 'way 1 (the condition, the gap and the question in one sentence); ' + WAIT,
                                   e[5]: 'ways 8 and 13 (", so" and the fact before the reader\'s case); ' + WAIT}}
        r['fit'] = {'reader': reader_line('fit'),
                    'marked': [{'s': e[2], 'found': 'misread: "there isn\'t enough data yet to say whether the warnings '
                                                    '... apply" can sound like they don\'t apply, which reassures'}],
                    'kept': {e[2]: 'the unknown is his answer to question 17 ("there isn\'t enough data to make a '
                                   'suggestion about this"), neither a yes nor a no, and S4 gives the act; ' + WAIT}}
    r['same_point'] = (
        'read the section from its heading (Weeks 3–5) to the next (Week 8+) for one-at-a-time and for UMP or 5-HTP with '
        'psychedelics. The 5-HTP line\'s "Do not use with ... iboga" says S2\'s no; S2 keeps it because his answer 17 '
        'gives it as the one microdose exception, and a reader who thinks a microdose doesn\'t count would miss it; that '
        'line stays for its other items. The UMP line\'s "Do not take UMP on psychedelic days" and the 5-HTP line\'s '
        '"same-day psychedelics" are the warnings S3 points to, kept where they are. No other paragraph of the section '
        'gives the order or the microdose rule')
    r['placement'] = (
        'a new first line under the Weeks 3–5 heading and its State line, before "Protocol:Reduce or stop '
        'phosphatidylserine here.": the order it gives and its microdose rules cover the whole list after it (the UMP '
        'trial, the 5-HTP trial, the showers and microdose line, the keto transition), so it comes before that list; its '
        'first "So" points to the plan the heading opens')
    r['questions'] = {
        'Q1': 'PASS: each sentence opens on what the reader gets or the case it answers: the reason for the order (S1), why '
              'they would want 5-HTP (S2), their own pairing (S3), the unknown (S4), their numbness (S5), the mushroom '
              'link (S6)',
        'Q2': 'PASS: each instruction says what it is for in the reader\'s terms: one at a time to tell what each change '
              'does; no 5-HTP with iboga because both act on serotonin; try each way because the data can\'t say; stop '
              '5-HTP at its stop signs because mushrooms act on serotonin too',
        'Q3': 'PASS: the list is named by its ends (the UMP trial, the keto diet), the pairings by what they are (UMP with '
              'any microdose, 5-HTP with a mushroom microdose), the warnings by what they say, the stop signs by the '
              'section that lists them',
        'Q4': 'PASS: UMP, 5-HTP, elliptica and microdosing are explained in their own sections earlier in the article (the '
              'uridine and 5-HTP sections, the iboga list), which this line follows; serotonin is named as what they act on',
        'Q5': 'PASS: "though" turns on the help 5-HTP could give, "so" on the shared serotonin; "But" turns from the firm no '
              'to the unknown; "Until there is" on the missing data; "If ... that" on "see how each feels"; "Like iboga" '
              'and "so" on the reason in S2',
        'Q6': 'PASS: the order of the list first, then what may go together: the firm no, the unknown, what to do about it, '
              'how a numb reader can tell, and the limit',
        'Q7': 'PASS: each fact is about the supplements and microdoses this phase gives them',
        'Q8': 'N/A: no group or list inside this paragraph; the two pairings in S3 are the two his answer leaves open',
        'Q9': 'PASS: one step a clause, with "though", "so", "But", "Until" and "Like" carrying each relation'}
    (HERE / ('%s.receipt.json' % KEY)).write_text(json.dumps(r, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    (HERE / ('%s.txt' % KEY)).write_text(text + '\n', encoding='utf-8')
    probs = S.check(text, r)
    for p in probs:
        print(p)
    print('ok' if not probs else 'PROBLEMS')
    return 1 if probs else 0


if __name__ == '__main__':
    sys.exit(main())
