"""Pairs from the 4.1 batches whose splices are recorded in CANDIDATES.json (479, 480, 481)."""
from ex import T, J

C479 = 'fix-20261025/b479/CANDIDATES.json'
C480 = 'fix-20261026/b480/CANDIDATES.json'
C481 = 'fix-20261026/b481/CANDIDATES.json'
R1025A = 'fix-20261025/recheck/RESULT-A.json'
R1025B = 'fix-20261025/recheck/RESULT-B.json'
R479A = 'fix-20261025/b479/recheck/RESULT-A.json'
R479B = 'fix-20261025/b479/recheck/RESULT-B.json'
R480A = 'fix-20261026/b480/recheck/read/RESULT-A.json'
R480B = 'fix-20261026/b480/recheck/read/RESULT-B.json'
R481A = 'fix-20261026/b481/recheck/read/RESULT-A.json'
R481B = 'fix-20261026/b481/recheck/read/RESULT-B.json'
R1029A = 'fix-20261029/recheck/read/RESULT-A.json'
R1029B = 'fix-20261029/recheck/read/RESULT-B.json'

L = {
    'split_list': 'list split into sentences',
    'short_list': 'list shortened',
    'colon': 'colon or dash removed',
    'closer': 'summing-up or closing line dropped',
    'def': 'definition turned into an action or instruction',
    'people': 'abstract nouns turned into people doing things',
    'notxy': '"not X but Y" or parallel pair broken',
    'uneven': 'sentence lengths made uneven',
    'split': 'a long sentence split',
    'join': 'short sentences joined',
    'q': 'a question added',
    'first': 'first person or a personal aside added',
    'hedge': 'hedge or doubt added',
    'casual': 'casual register (contractions, "kind of", "pretty") added',
    'concrete': 'a concrete particular added',
    'order': 'order changed',
    'subj': 'subject changed',
    'quip_out': 'quip or metaphor removed',
    'quip_in': 'quip or metaphor added',
}
# "other" labels used across the file, kept to a fixed set so they can be counted
O = {
    'etc': 'other: catch-all list ending added (etc., whatever, or anything like that)',
    'excl': 'other: exclamation added',
    'aside': 'other: list or gloss moved into brackets or dashes as an aside',
    'soft': 'other: bare statement or command turned into a softened instruction (make sure, you may want to, it is a good idea to)',
    'direct': 'other: statement or softened line turned into a direct instruction to the reader',
    'note': 'other: label added in front ("Note:", "REMEMBER:", "Invoking:")',
    'caps': 'other: capitals for emphasis added',
    'runon': 'other: run-on or comma splice made (clauses chained with and/then/however or a bare comma)',
    'ifrun': 'other: run of parallel "if" clauses or "If you X, Y" sentences made or kept',
    'reason': 'other: reason or cause clause added (because, since, as, so that)',
    'poly': 'other: "and ... and" or "or ... or" chain instead of a comma list',
    'q2s': 'other: question turned into a statement or instruction',
    'signpost_out': 'other: signposting or framing words dropped ("The useful question is whether", "That distinction matters here")',
    'formal': 'other: register made more formal or more abstract (contractions removed, abstract subject)',
    'quote': 'other: quoted inner speech or a direct request added',
    'minimal': 'other: only a word or two changed',
    'setup': 'other: announcing set-up added ("There is something you should never do ... And that\'s ...")',
    'closer_in': 'other: restating closer added',
    'anaphora': 'other: anaphora or fragment run made or kept (By X? By Y?; If it is really X ...)',
    'conn': 'other: casual connective added (on the other hand, though, also, of course)',
    'noise': 'other: typos, slashes or nonstandard spelling',
    'loose': 'other: looser, wordier phrasing (filler and repetition such as "all you have to do is", "a number of", "when you want to")',
    'tight': 'other: wording tightened (fewer words, every clause doing a job)',
}


def pairs():
    P = []
    # ---- batch 479 (Emulate samples cg, ch, ci of the red stretches of the 2026-10-25 recheck) ----
    P.append(dict(
        id='b479-S2', batch='479', detector='Pangram 4.1', kind='pass',
        input=J(C479, 'spots/S2/old'),
        input_reading='AI (High, calibrated 0.995), its own 46-word window, whole-guide recheck of 2026-10-25 part A (%s); the same words read AI (High, 46 words) again on 2026-10-29 after the splice was taken out (%s)' % (R1025A, R1029A),
        emulate=J(C479, 'spots/S2/new'),
        emulate_raw=T('fix-20261025/b479/ch/HG-A-borrowed.out.txt', 'So, I came up with', 'tried before.'),
        emulate_reading='Human (High, 0.999, 85-word window) with Human (Medium, 0.961, 31 words) in batch 479\'s recheck part A (%s); Human (High) alone through the API (b479-S2-p, README.md); Human (High) in batch 480\'s recheck (%s)' % (R479A, R480A),
        labels=[L['first'], L['hedge'], L['casual'], O['aside'], O['conn']],
        meaning_error='Raw sample: "a number of things that I know work" (a stronger claim than "familiar practices") and "even though I don\'t know if the whole sequence has been tried before" (his not knowing, where he says he makes no claim; "tried" is a lower bar than "formally tested and proven"). Both were put back before the check. Kept: "a temporary fix" for "provisional", "I came up with the idea of constructing" for "I have developed".',
        note='Shape: the noun-heavy claim ("a kind of provisional bridge that I call ...", "built from familiar practices like ...") became a spoken first-person account with an aside in dashes and a self-conscious hedge ("if I can put it that way"); the disclaimer moved from "but I\'m not suggesting" to a trailing "even though".'))
    P.append(dict(
        id='b479-S3a', batch='479', detector='Pangram 4.1', kind='pass',
        input=J(C479, 'spots/S3a/old'),
        input_reading='AI (Low, 0.531, 34-word window, marked humanized) with a Human (Low) window before it, recheck of 2026-10-25 part A (%s)' % R1025A,
        emulate=J(C479, 'spots/S3a/new'),
        emulate_raw=T('fix-20261025/b479/ci/HG-A-stop.out.txt', 'If you are already partally', 'not in a safe state.'),
        emulate_reading='Human (High, 0.996, 83 words), batch 479\'s recheck part A (%s); Human (High) again in batch 481\'s recheck after the linter fix S3a2 (%s)' % (R479A, R481A),
        labels=[L['order'], L['subj'], O['formal']],
        meaning_error='Raw sample narrowed "if you\'re not stable" to "if you are not in a safe state", added "partially or fully", misnamed the section ("Contain yourself before deepening") and misspelled "partally"; the lane put back "not stable" and the heading\'s words.',
        note='Shape: a bracketed passive aside about a section ("The part below called ... can be used to help orient you if ...") became a plain sentence that starts with the reader\'s condition ("If you are already ... opened, you can use ...").'))
    P.append(dict(
        id='b479-S3b', batch='479', detector='Pangram 4.1', kind='pass',
        input=J(C479, 'spots/S3b/old'),
        input_reading='AI (Low, 0.503, 14 words) and AI (Low, 0.855, 27 words), both marked humanized, recheck of 2026-10-25 part A (%s)' % R1025A,
        emulate=J(C479, 'spots/S3b/new'),
        emulate_raw=T('fix-20261025/b479/cg/HG-A-stop.out.txt', "Remind yourself that if you say 'stop'", "the talking will stop."),
        emulate_reading='Human (Medium, 0.969, 71 words), batch 479\'s recheck part A (%s); in batch 480\'s recheck its three sentences read Human Medium (0.944), Low (0.879) and Medium (0.972) (%s): a weak pass' % (R479A, R480A),
        labels=[L['split'], O['ifrun']],
        meaning_error='"If you want to change something" (why you would say less or quiet) is gone.',
        note='Shape: one long mixed sentence ("If you want to change something, say \'less\' if ..., or say \'quiet\' and ...") became three short parallel "If you say X, ..." sentences. Emulate made a parallel run here, and it never read better than Medium.'))
    P.append(dict(
        id='b479-S4', batch='479', detector='Pangram 4.1', kind='pass',
        input=J(C479, 'spots/S4/old'),
        input_reading='AI (Low, 0.754, 5 words) and AI (High, 0.997, 24 words), recheck of 2026-10-25 part B (%s); again AI (Low, 5 words) and AI (High, 24 words) on 2026-10-29 with these words back (%s). His own words (his inner child guide).' % (R1025B, R1029B),
        emulate=J(C479, 'spots/S4/new'),
        emulate_raw=T('fix-20261025/b479/ci/HG-B-act.out.txt', 'It should make sense to you and', 'with what you know.'),
        emulate_reading='Human (High, 0.999, in a 1724-word window), batch 479\'s recheck part B (%s), and again in batch 480\'s (%s); Human (High, one window) alone through the API with its paragraph (b479-S4-p)' % (R479B, R480B),
        labels=[L['join'], L['casual'], O['runon'], O['direct']],
        meaning_error='"Even then" is gone (that a big step waits even when the answer makes sense), and "what you actually know" became "what you know".',
        note='Shape: a short add-on sentence ("It should make sense, too.") and a hedged rule ("Even then, anything big ... can wait until ...") became one run-on instruction joined with "and if", "wait till ... and then check it out".'))
    P.append(dict(
        id='b479-S5', batch='479', detector='Pangram 4.1', kind='pass',
        input=J(C479, 'spots/S5/old'),
        input_reading='AI (High, 0.994, 16 words), recheck of 2026-10-25 part B (%s); again AI (Medium, 3 words) and AI (High, 13 words) on 2026-10-29 with these words back (%s). His inner child guide\'s line.' % (R1025B, R1029B),
        emulate=J(C479, 'spots/S5/new'),
        emulate_raw=T('fix-20261025/b479/ch/HG-B-love.out.txt', 'If you can’t do this in a loving way today', 'You don’t have to fake it!'),
        emulate_reading='Human (High, 0.997, 50 words) and Human (Medium, 0.989, 7 words), batch 479\'s recheck part B (%s); Human (five windows, two High, three Medium) alone through the API (b479-S5-p)' % R479B,
        labels=[O['q2s'], L['quip_out'], L['casual'], O['excl']],
        meaning_error='',
        note='Shape: a fragment question and a clipped tag ("No warmth today? ... no faking required.") became a plain condition and a plain permission ("If you can\'t do this in a loving way today, just ... You don\'t have to fake it!"). The lane later put his "no faking required" back for the linter (S5b), which read Human High in batch 480\'s recheck and Human Medium in batch 481\'s.'))
    P.append(dict(
        id='b479-S6', batch='479', detector='Pangram 4.1', kind='pass',
        input=J(C479, 'spots/S6/old'),
        input_reading='AI (High, 0.996, 17 words), recheck of 2026-10-25 part B (%s); again AI (High, 17 words) on 2026-10-29 with these words back (%s). The published sentence, word for word.' % (R1025B, R1029B),
        emulate=J(C479, 'spots/S6/new'),
        emulate_raw=T('fix-20261025/b479/cg/HG-B-test.out.txt', 'Is it helping you to be clearer', 'less hooked?'),
        emulate_reading='Human (High, 0.999, in a 1772-word window), batch 479\'s recheck part B (%s) and batch 480\'s (%s); Human (High, one window) through the API with the paragraph before it (b479-S6-p+prev)' % (R479B, R480B),
        labels=[L['q'], O['signpost_out'], O['poly']],
        meaning_error='Raw sample: "Is it helping you" had no clear "it"; the lane put back "this way of responding".',
        note='Shape: a framed criterion ("The useful question is whether X helps you become A, B, and C") became the direct question itself, with the three-item list as "A and B and C".'))
    # ---- batch 480 (cj, ck, cl) ----
    P.append(dict(
        id='b480-S7', batch='480', detector='Pangram 4.1', kind='pass',
        input=J(C480, 'spots/S7/old'),
        input_reading='AI (High, 0.996, 27 words), its own window, batch 479\'s recheck part A (%s). His own sentence, from his inner child guide.' % R479A,
        emulate=J(C480, 'spots/S7/new'),
        emulate_raw=T('fix-20261026/b480/cl/HG-A-jobs2.out.txt', 'It’s one person doing three jobs', 'keep the others in balance'),
        emulate_reading='Human (High, 0.998, in a 1766-word window), batch 480\'s recheck part A (%s), and batch 481\'s (%s); Human (High, one 84-word window) alone through the API (b480-S7-p)' % (R480A, R481A),
        labels=[L['split'], L['notxy'], O['excl'], L['casual']],
        meaning_error='Raw sample softened "keeps the others in balance" to "helps to keep" (and lost the full stop); the lane put "keeps" back.',
        note='Shape: one sentence with a "not X" contrast slotted in the middle ("three jobs, not three more people moving in ..., and each job ...") became two sentences: the joke as its own line with "rather than" and an exclamation, then the balance as a plain sentence. Note that his sentence without the rent clause read AI (Low, 16 words) in the 2026-10-25 recheck, and with it AI (High).'))
    P.append(dict(
        id='b480-S8', batch='480', detector='Pangram 4.1', kind='pass',
        input=J(C480, 'spots/S8/old'),
        input_reading='AI (Medium, 0.967, 21 words) and AI (High, 0.996, 48 words), batch 479\'s recheck part A (%s)' % R479A,
        emulate=J(C480, 'spots/S8/new'),
        emulate_raw=T('fix-20261026/b480/ck/HG-A-guards.out.txt', 'Before figuring out what/where it is', 'or a combination.'),
        emulate_reading='Human (High, 0.998, 108 words), batch 480\'s recheck part A (%s); the same in batch 481\'s (%s); Human (five windows, three High, two Medium) through the API with the next paragraph (b480-S8-p+next)' % (R480A, R481A),
        labels=[O['soft'], L['hedge'], O['formal'], O['noise']],
        meaning_error='"of course" adds an assurance he doesn\'t give; "decide where it\'s coming from" became "figuring out what/where it is"; the raw sample ended the list on the model word "a combination", which the lane changed back to his "a bit of each".',
        note='Shape: Emulate kept the long "or ... or ... or" list but changed its frame: "make sure to ask", "It may, of course, be ..., or it may be ...", and dropped the contractions and the opening "But". Here the change is mostly in register and hedging, not structure.'))
    P.append(dict(
        id='b480-S9', batch='480', detector='Pangram 4.1', kind='pass',
        input=J(C480, 'spots/S9/old'),
        input_reading='AI (Low, 0.851, 35 words) and AI (Medium, 0.944, 18 words), both marked humanized, batch 479\'s recheck part A (%s). Words written by Claude in batch 470.' % R479A,
        emulate=J(C480, 'spots/S9/new'),
        emulate_raw=T('fix-20261026/b480/cj/HG-A-script.out.txt', 'Your parent script is made up of', 'that you consciously build.'),
        emulate_reading='Human (High, 0.998, in a 568-word window), batch 480\'s recheck part A (%s), and batch 481\'s (%s). Alone through the API (b480-S9-p), Emulate\'s sentences read Human (High, 73 words) and the paragraph\'s two unchanged last sentences read AI (Low 30, Medium 27).' % (R480A, R481A),
        labels=[L['split'], L['subj'], O['aside']],
        meaning_error='"internalized" became "adopted"; the raw sample lost a full stop ("a voice It is not"), fixed.',
        note='Shape: a definition that opened on "This is the set of rules ..., mostly based on ..., and it doesn\'t always ..." became a sentence with the term as its subject ("Your parent script is made up of ...") with the qualifier in brackets, and the "doesn\'t always sound like a voice" clause split off as its own short sentence.'))
    P.append(dict(
        id='b480-S10', batch='480', detector='Pangram 4.1', kind='pass',
        input=J(C480, 'spots/S10/old'),
        input_reading='AI (Low, 0.754, 21 words), its own window, batch 479\'s recheck part B (%s). His inner child guide\'s sentence.' % R479B,
        emulate=J(C480, 'spots/S10/new'),
        emulate_raw=T('fix-20261026/b480/cl/HG-B-altered.out.txt', 'Borrow some from someone else', 'direct your trip.'),
        emulate_reading='Human (High, 0.999, in a 348-word window), batch 480\'s recheck part B (%s), and batch 481\'s (%s)' % (R480B, R481B),
        labels=[O['direct'], O['soft'], L['quip_out']],
        meaning_error='A permission ("Borrowed is fine, as long as ...") became an instruction with a condition ("Borrow some ... if you need to, but make sure ..."); "run your trip for you" flattened to "direct your trip".',
        note='Shape: a clipped verdict with a condition ("X is fine, as long as ...") became an instruction to the reader with "if you need to" and "make sure".'))
    # ---- batch 481 (cm, cn, co): windows that read Human below High, rewritten to reach High ----
    def b481(sid, sample, labels, meaning, note, in_read, out_read, kind='weak-to-high', start=None, end=None):
        d = dict(id='b481-' + sid, batch='481', detector='Pangram 4.1', kind=kind,
                 input=J(C481, 'spots/%s/old' % sid), input_reading=in_read,
                 emulate=J(C481, 'spots/%s/new' % sid), emulate_reading=out_read,
                 labels=labels, meaning_error=meaning, note=note)
        if start:
            d['emulate_raw'] = T(sample, start, end)
        return d
    P.append(b481('S12', 'fix-20261026/b481/cm/HG-The-table-of-contents-is-hid-6.out.txt',
        [L['quip_out'], L['casual'], O['reason']],
        'The warm personification ("that little hidden menu is your friend") is gone; "It" now has to point back to the table of contents in the sentence before.',
        'Shape: a wry personification of the menu became a plain helpful remark with a reason ("as it\'s a long one").',
        'Human (Low, 0.649, 12 words), batch 480\'s recheck part A (%s). His own sentence.' % R480A,
        'Human (High, 0.999, 399 words), batch 481\'s recheck part A (%s); still Human (High) on 2026-10-29 (%s)' % (R481A, R1029A),
        start='It\'ll be really helpful', end='a long one.'))
    P.append(b481('S15', 'fix-20261026/b481/co/HG-Protecting-Yourself-from-Hyp-30.out.txt',
        [L['join'], O['minimal']],
        '',
        'Shape: a verbless list sentence followed by a question became one sentence: the list, a dash, and the question ("... legal and ethical consent - can people ...?"). Joel\'s own revision of 28 October (his card HG-S15: "All of these are separate factors to consider: conscious agreement, ...", a colon list) read AI (Low, 18 words) on 2026-10-29.',
        'Human (Low, 0.848, 10 words), batch 480\'s recheck part A (%s)' % R480A,
        'Human (High, 0.998, 147 words), batch 481\'s recheck part A (%s)' % R481A,
        start='Conscious agreement, unconscious receptivity', end='of their adult self?'))
    P.append(b481('S16', 'fix-20261026/b481/cm/HG-Forget-the-left-brain-right-62.out.txt',
        [L['subj'], O['minimal']],
        '',
        'Shape: "these modes" (an abstract label) became "each ... the other". A two-word change; with the old words back it read Human (Low, 0.531, 7 words) on 2026-10-29 (%s), so the old line read below High twice and the new one High once.' % R1029A,
        'Human (Medium, 0.989, 14 words, with the next line), batch 480\'s recheck part A (%s)' % R480A,
        'Human (High, 0.998, in a 1746-word window), batch 481\'s recheck part A (%s)' % R481A,
        start='So each can correct the other.', end=None))
    P.append(b481('S18', 'fix-20261026/b481/cm/HG-Why-doing-it-myself-worked-b-65.out.txt',
        [L['notxy'], L['hedge'], L['order'], L['join']],
        'Raw sample stated sobriety as a reason ("One reason was that I was sober") and as a fact about him ("wasn\'t that susceptible"); he only suspected the first and felt the second. The lane changed both ("might have been", "didn\'t feel").',
        'Shape (the splice joins Emulate\'s "But I think a bigger reason is that" to his "trust and precision"): the knock-down ("..., but I suspect that\'s not even the main reason ... The bigger issue was trust and precision.") became a ranked pair in his voice ("One reason might have been ... But I think a bigger reason is ..."), and the short verdict line was folded into the second sentence. With the old words back it read Human (High, 53 words) and Human (Low, 0.503, 7 words: "The bigger issue was trust and precision.") on 2026-10-29 (%s).' % R1029A,
        'Human (Medium, 0.944, 31 words) and Human (Low, 0.531, 7 words), batch 480\'s recheck part A (%s)' % R480A,
        'Human (High, 0.998, in a 1746-word window), batch 481\'s recheck part A (%s)' % R481A,
        start='One reason was that I was sober', end='a bigger reason is that'))
    P.append(b481('S19', 'fix-20261026/b481/co/HG-Why-doing-it-myself-worked-b-65.out.txt',
        [L['casual'], O['minimal']],
        '',
        'Shape: almost none: the opening "And" dropped and "talks me into a yes" became "can twist it around to a yes". With the old words back it read Human (Medium, 0.944) on 2026-10-29 (%s). Counts as evidence that a window this short moves with context more than with wording.' % R1029A,
        'Human (Low, 0.829, 17 words), batch 480\'s recheck part A (%s)' % R480A,
        'Human (High, 0.998, in a 1746-word window), batch 481\'s recheck part A (%s)' % R481A,
        start='I can tell when my body is saying no', end='to a yes.'))
    P.append(b481('S20', 'fix-20261026/b481/cm/HG-When-your-voice-is-everybody-186.out.txt',
        [L['casual'], L['quip_out'], O['runon']],
        '',
        'Shape: a compact purpose sentence ("so you can be sure you\'re not just echoing your social group") became a looser, wordier one ("be able to let the quiet little preferences that you have ... and know for sure that you\'re not going by what your social group would want you to do"): the metaphor "echoing" became a plain action.',
        'Human (Low, 0.722, 64 words, with the two sentences before it, which are his inner child guide\'s), batch 480\'s recheck part A (%s)' % R480A,
        'Human (High, 0.999, in a 1624-word window), batch 481\'s recheck part A (%s); the old words back read Human (High) on 2026-10-29 (%s)' % (R481A, R1029A),
        start='You want to be able to let the quiet little preferences', end='would want you to do.'))
    P.append(b481('S21', 'fix-20261026/b481/cm/HG-Please-don-t-put-six-metapho-238.out.txt',
        [O['soft'], O['minimal']],
        '',
        'Shape: "And when you\'re done, come back" became "When you\'re done, make sure to come back". With the old words back it read Human (Low, 0.754, 10 words) on 2026-10-29 (%s).' % R1029A,
        'Human (Medium, 0.987, 21 words, with the bracket after it), batch 480\'s recheck part A (%s)' % R480A,
        'Human (High, 0.997, 326 words), batch 481\'s recheck part A (%s)' % R481A,
        start="When you're done, make sure to come back the other way.", end=None))
    P.append(b481('S22', 'fix-20261026/b481/cn/HG-Please-don-t-put-six-metapho-238.out.txt',
        [L['casual'], O['caps'], L['people']],
        '"when you\'re being induced" became "when you\'re trying to induce": the reader is now the one inducing, not the one in trance.',
        'Shape: three short tidy lines ending on a clipped image ("It\'s all just soup.") became the same three with a spoken frame ("And then", "are NOT going to help you", "It\'s all soup to you at that point"): the image is tied to the reader and a moment instead of standing as an aphorism. With the old words back they read Human (Low, 0.719) and Human (Medium) on 2026-10-29 (%s).' % R1029A,
        'Human (Medium, 0.974, 26 words), batch 480\'s recheck part A (%s)' % R480A,
        'Human (High, 0.997, 326 words), batch 481\'s recheck part A (%s)' % R481A,
        start='And then read it out loud as you write it.', end='at that point.'))
    P.append(b481('S23', 'fix-20261026/b481/cn/HG-Before-you-begin-242.out.txt',
        [L['casual'], O['minimal']],
        '"during the induction" is gone, and "Get clear on" became the weaker "Think about".',
        'Shape: shorter and plainer words ("Think about what you want to do. Are there things you don\'t want to do today?"); the awkward "What do you want not to do today?" became an ordinary question. With the old words back they read Human (Medium) on 2026-10-29 (%s).' % R1029A,
        'Human (Medium, 0.982, 58 words, with the rest of the paragraph), batch 480\'s recheck part A (%s)' % R480A,
        'Human (High, 0.997, 326 words), batch 481\'s recheck part A (%s)' % R481A,
        start='Think about what you want to do.', end='want to do today?'))
    P.append(b481('S26', 'fix-20261026/b481/co/HG-Capacity-before-content-377.out.txt',
        [L['q'], L['people'], O['minimal']],
        'A demand to the subconscious ("Give me one next action!") became a question ("What is one next thing I can do?"), which is softer.',
        'Shape: the fourth exclamation of a run of commands became a question, and "action" became "thing I can do". With the old words back it read Human (Low, 0.727, 6 words) again on 2026-10-29 (%s).' % R1029A,
        'Human (Low, 0.727, 6 words), batch 480\'s recheck part A (%s)' % R480A,
        'Human (High, 0.999, in an 842-word window), batch 481\'s recheck part A (%s)' % R481A,
        start='What is one next thing I can do?', end=None))
    P.append(b481('S30', 'fix-20261026/b481/co/HG-It-feels-fake-384.out.txt',
        [L['casual'], O['minimal']],
        '',
        'Shape: "Do you have a sense of what it is that feels fake?" became "Have you got any sense of what it is that\'s making it feel fake?": more spoken. With the old words back it read Human (Medium, 0.951) on 2026-10-29 (%s).' % R1029A,
        'Human (Low, 0.575, 31 words, with the requests before the heading), batch 480\'s recheck part A (%s)' % R480A,
        'Human (High, 0.998, 149 words), batch 481\'s recheck part A (%s)' % R481A,
        start='Have you got any sense', end='feel fake?'))
    P.append(b481('S32', 'fix-20261026/b481/cn/HG-Pattern-6-Ethical-double-bin-514.out.txt',
        [L['people'], L['subj'], L['quip_out']],
        'Raw sample dropped his "genuinely" (put back by the gate).',
        'Shape: a compressed line with a pronoun subject and a metaphor ("An ethical one offers two genuinely safe routes.") became the full term doing something to a person ("An Ethical Double Bind Question gives someone a choice between two genuinely safe things to do."). With the old words back it read AI (Medium, 0.951, 8 words) on 2026-10-29 (%s).' % R1029B,
        'Human (Low, 0.640, 8 words), batch 480\'s recheck part B (%s). His own sentence.' % R480B,
        'Human (High, 0.999, 329 words), batch 481\'s recheck part B (%s)' % R481B,
        start='An Ethical Double Bind Question gives someone', end='safe things to do.'))
    P.append(b481('S36', 'fix-20261026/b481/cm/HG-Forgiveness-without-bypass-665.out.txt',
        [L['join'], L['notxy'], L['casual']],
        '',
        'Shape: two parallel short questions ("What is theirs? What is mine?") became one question with contractions ("What\'s theirs and what\'s mine?"). With the old words back they read Human (Medium, 0.972) on 2026-10-29 (%s).' % R1029B,
        'Human (Medium, 0.963, 10 words, with his "What does accountability require?"), batch 480\'s recheck part B (%s)' % R480B,
        'Human (High, 0.997, 66 words), batch 481\'s recheck part B (%s)' % R481B,
        start='What’s theirs and what’s mine?', end=None))
    P.append(b481('S11', 'fix-20261026/b481/co/HG-How-to-use-this-very-large-g-4.out.txt',
        [L['casual']],
        'Raw sample dropped "to make the practice your own" (put back), and its "You can also" was cut for the linter.',
        'Shape: "look at" became "read some of the stuff in": a vaguer, spoken phrase.',
        'Human (Medium, 0.989, 16 words), batch 480\'s recheck part A (%s)' % R480A,
        'Human (High, 0.999, 399 words), batch 481\'s recheck part A (%s); still High on 2026-10-29 (%s)' % (R481A, R1029A),
        start='You can also read some of the stuff', end='weekly sections'))
    P.append(b481('S14', 'fix-20261026/b481/co/HG-Protecting-Yourself-from-Hyp-30.out.txt',
        [L['order'], L['casual'], O['aside']],
        'Raw sample: "their" dark patterns and "used to trick and manipulate" for his "designs that trick or manipulate consumers"; the gate put his words back.',
        'Shape: the dangling opening clause ("Even when not actively engaging the conscious mind, there are many ways ...") became a plain sentence with the condition last ("There are a lot of ways ... without engaging their conscious mind"); the FTC sentence became a short statement with a dash gloss.',
        'Human (Medium, 0.982, 77 words, with the paragraph before), batch 480\'s recheck part A (%s)' % R480A,
        'Human (High, 0.997, 274 words) and Human (Medium, 0.976, 24 words), batch 481\'s recheck part A (%s): only partly High' % R481A,
        kind='weak-to-high', start='There are a lot of ways to influence people', end='manipulate consumers.'))
    P.append(b481('S29', 'fix-20261026/b481/co/HG-Nothing-happens-378.out.txt',
        [L['colon'], L['notxy'], L['hedge'], O['q2s']],
        '"Ask" (an instruction) became "Maybe ask"; the three requests to the inner process became a reported request ("ask to be shown").',
        'Shape: a colon and three parallel quoted requests became one hedged sentence and an "Or even just ..." fragment. It still read Human (Low, 0.813, 23 words): this change did not reach High.',
        'Human (Low, 0.575, 31 words), batch 480\'s recheck part A (%s)' % R480A,
        'Human (Low, 0.813, 23 words), batch 481\'s recheck part A (%s)' % R481A,
        kind='weak-stays-weak', start='Maybe ask to', end='or resting today.'))
    P.append(b481('S31', 'fix-20261026/b481/co/HG-It-feels-fake-384.out.txt',
        [L['hedge'], O['minimal']],
        'Raw sample: "this part knows it" for his "that part remembers" (put back).',
        'Shape: "Maybe you\'ve fooled yourself before" became "You may have fooled yourself in the past". It reached only Medium; the old words back read AI (Low, 0.503, 10 words) on 2026-10-29 (%s).' % R1029A,
        'Human (Low, 0.531, 10 words), batch 480\'s recheck part A (%s). His inner child guide\'s sentence.' % R480A,
        'Human (Medium, 0.989, 12 words), batch 481\'s recheck part A (%s)' % R481A,
        kind='weak-stays-weak', start='You may have fooled yourself in the past', end='knows it.'))
    return P
