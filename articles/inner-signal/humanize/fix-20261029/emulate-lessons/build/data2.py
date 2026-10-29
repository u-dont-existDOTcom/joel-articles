"""4.1 pairs from the re-runs of 2026-10-23 (the seam re-run, batches 474 and 475) and the screening post of 2026-10-22."""
from ex import T, J
from data1 import L, O

C474 = 'fix-20261023/b474/CANDIDATES.json'
C475 = 'fix-20261023/b475/CANDIDATES.json'
R1022A = 'fix-20261022/recheck/RESULT-A.json'
R1023A = 'fix-20261023/recheck/RESULT-A.json'
RA3 = 'fix-20261023/recheck-a3/RESULT-A.json'
RA4 = 'fix-20261023/recheck-a4/RESULT-A.json'
SEAM_IN = 'fix-20261023/emu-seam/INPUT.json'
BJ = 'fix-20261023/emu-seam/bj/HG-seam-rr.out.txt'
BK = 'fix-20261023/emu-seam/bk/HG-seam-rr.out.txt'
API472 = 'fix-20261023/b472/API-CHECKS.md'
API473 = 'fix-20261023/b473/API-CHECKS.md'
API474 = 'fix-20261023/b474/API-CHECKS.md'
SCR = 'fix-20261022/screen/RESULT-S.json'
PUB17 = 'fix-20261018/emu-bc/HG17-pub2.txt'
FX17 = 'fix-20261018/emu-be/HG17-fx1.txt'
B429 = 'fix-20261018/b429/b429-results.json'
W41R3A = 'fix-20261020/result41/WINDOWS-41r3-a.json'


def pairs():
    P = []
    # ---- the seam: Emulate's earlier text (with meaning fixes) read AI High in 4.1; Joel's re-run trick ----
    seam_read = ('AI (High): the whole stretch read AI (High) through the API as it stood, 245 words (b472_s2_base, %s), and in the recheck of 2026-10-22 part A (AI High, 162 words, %s). The text is Emulate\'s earlier output (samples emu-bf and emu-ax, which had passed) with the lane\'s meaning fixes.' % (API472, R1022A))
    P.append(dict(
        id='seam-bj-help', batch='473 (emu-seam)', detector='Pangram 4.1', kind='pass-alone-ai-in-place',
        input=J(SEAM_IN, 'HG-seam-rr', 'If you are finding that you are responding', 'qualified to help you.'),
        input_reading=seam_read,
        emulate=T(BJ, 'If it’s causing you a problem', 'someone who can help you.'),
        emulate_reading='Human (High, 157 words) alone through the API with "who\'s qualified" put back (b473_seam_bj_p1, %s); in place in the recheck of 2026-10-23 part A this sentence read AI (Low, 0.879, 35 words) (%s)' % (API473, R1023A),
        labels=[L['subj'], O['aside'], O['etc'], L['casual']],
        meaning_error='"qualified" dropped (anyone "who can help you"); put back before the check.',
        note='Shape: a two-part condition in full clauses ("If you are finding that you are ..., or you are having problems with ...") became one plain condition with the examples in brackets ending on "whatever". Passed alone, failed in place: the reading of a 35-word window depended on its neighbours.'))
    P.append(dict(
        id='seam-bj-keep', batch='473 (emu-seam)', detector='Pangram 4.1', kind='pass-alone-ai-in-place',
        input=J(SEAM_IN, 'HG-seam-rr', 'If you want to keep it in, you can', 'when you come out of it.'),
        input_reading=seam_read,
        emulate=T(BJ, 'If you want to keep it around', 'over for today.'),
        emulate_reading='Human (High, 157 words) alone through the API (b473_seam_bj_p1, %s); in place in the recheck of 2026-10-23 part A these two sentences read AI (Medium, 0.958, 45 words) (%s)' % (API473, R1023A),
        labels=[L['casual'], L['order'], O['conn']],
        meaning_error='Dropped condition: "only for the use of starting a session at a later time" became a plain permission ("that\'s fine"); the restriction "only" is gone.',
        note='Shape: a hedged permission with a restriction ("you can, but only for ...") became a casual permission ("If you want to keep it around ..., that\'s fine."), and the closing clause order was swapped. AI (Medium) in place.'))
    P.append(dict(
        id='seam-bk-reverse', batch='473 (emu-seam)', detector='Pangram 4.1', kind='pass',
        input=J(SEAM_IN, 'HG-seam-rr', 'Make sure to reverse anything', 'normal size again.'),
        input_reading='AI (High): these sentences read AI (High, then Medium 25 words) in the recheck of 2026-10-22 part A (%s) and AI (High) through the API (b472_s2_base, %s). Emulate\'s own earlier output (emu-ax), which had read Human in Pangram 4.0 (batch 463, HG18-wb).' % (R1022A, API472),
        emulate=T(BK, 'If you have done anything to alter your state', 'your regular size.'),
        emulate_reading='Human (High, a 286-word window) in the API pair check b473_seam_pair (%s); never installed, so never read in place' % API473,
        labels=[L['order'], O['formal'], O['ifrun']],
        meaning_error='"If you have done anything to alter your state when coming out of a trance" attaches "when coming out" to the altering, not to the reversing.',
        note='A counter-case: Emulate made this run MORE uniform ("If you have X, make sure to Y" three times) and dropped the contractions, and the pair still read Human (High). The structural lessons are tendencies, not switches.'))
    # ---- batch 474 (bl, bm, bn): the three stretches recheck A of 2026-10-23 read red ----
    P.append(dict(
        id='b474-drive', batch='474', detector='Pangram 4.1', kind='pass',
        input=J(C474, 'b474_seam2/old/0'),
        input_reading='Human (Low, 0.67, 18 words) for the first sentence and AI (Low, 0.575, a 98-word window) from the second sentence into the next paragraph, recheck of 2026-10-23 part A (%s)' % R1023A,
        emulate=T('fix-20261023/b474/bn/HG-A-seam2.out.txt', 'There is something you should never do', 'just not safe.'),
        emulate_reading='Human (High, 0.999, in a 1365-word window), recheck A3 (%s); through the API, Human (Medium, 11 words, the first line) and Human (High, 129 words) (b474_seam2, %s)' % (RA3, API474),
        labels=[O['setup'], L['split'], L['casual'], L['uneven'], O['closer_in']],
        meaning_error='"train" and "test" were lost in an earlier step; this sample kept "never" and made "your eyes can be open" a may.',
        note='Shape: a flat prohibition and one long sentence with two trailing "even ..." clauses became a spoken announcement ("There is something you should never do ... And that\'s use it while ..."), the reason as its own sentence, and the "even though ..., even though ..." clauses as a last sentence ending on a repeated "it\'s just not safe". Two tells from the inventory (an announcing set-up, a restating closer) are here, and it read High: in speech-like prose they read as speech.'))
    P.append(dict(
        id='b474-shortcut-steps', batch='474', detector='Pangram 4.1', kind='pass',
        input=J(C474, 'b474_seam2/old/1', 'If you want to turn this one off', 'gone right away.'),
        input_reading='AI (Low, 0.575) for the first sentence (in the 98-word window above) and AI (Medium, 0.933, 34 words) for the second, recheck of 2026-10-23 part A (%s). Emulate\'s bj with the lane\'s fix "You\'ll want to say, while you\'re awake,".' % R1023A,
        emulate=T('fix-20261023/b474/bl/HG-A-seam2.out.txt', 'If you want to turn this one off, simply', 'gone right away.'),
        emulate_reading='Human (High, 0.999, in a 1365-word window), recheck A3 (%s); through the API, Human (High, 129 words) and Human (Medium, 33 words) for "Tell yourself ... right away." (b474_seam2, %s)' % (RA3, API474),
        labels=[L['split'], L['split_list'], L['notxy'], L['casual'], L['uneven'], O['direct']],
        meaning_error='',
        note='Shape: two long sentences, a comma run of four steps and a "..., but saying that it\'s gone doesn\'t mean ..." contrast, became five shorter ones: the first step alone, the other steps together, the instruction ("Tell yourself, when you\'re awake, ..."), and the caution as its own "Just because you say ... doesn\'t mean ..." sentence.'))
    P.append(dict(
        id='b474-shortcut-help', batch='474', detector='Pangram 4.1', kind='pass',
        input=J(C474, 'b474_seam2/old/1', 'If it’s causing you a problem', 'over for today.'),
        input_reading='AI (Low, 0.879, 35 words) and AI (Medium, 0.958, 45 words), recheck of 2026-10-23 part A (%s); Emulate\'s bj (with "who\'s qualified" put back), which had read Human (High) alone' % R1023A,
        emulate=T('fix-20261023/b474/bl/HG-A-seam2.out.txt', 'If it’s causing you a problem, if you’re still', 'over for today.'),
        emulate_reading='Human (High, 0.999, in a 1365-word window), recheck A3 (%s); Human (High, 82 words) and Human (Medium, 16 words) through the API (b474_seam2, %s)' % (RA3, API474),
        labels=[O['ifrun'], O['etc'], O['conn'], L['casual']],
        meaning_error='',
        note='Shape: the bracketed examples ("(you\'re responding to it ..., you\'re having disorientation issues, whatever)") became a run of "if" clauses ("If it\'s causing you a problem, if you\'re still ..., if you\'re having ..., etc,"), and casual connectives ("If, on the other hand, ...", "that\'s fine too", "For now, though,") were added.'))
    P.append(dict(
        id='b474-trouble-show', batch='474', detector='Pangram 4.1', kind='pass',
        input=J(C474, 'b474_trouble/old/1'),
        input_reading='AI (Medium, 0.94, 34 words, marked humanized), with the next line, recheck of 2026-10-23 part A (%s). Emulate\'s own earlier output (emu-as, HG24-ow1), which had read Human (Medium) in the recheck of 2026-10-22.' % R1023A,
        emulate=T('fix-20261023/b474/bn/HG-A-trouble.out.txt', 'Show yourself one sensation', 'need to rest.'),
        emulate_reading='As installed, with "body" put back ("Show yourself one body sensation, ..."), Human (High, 0.999, in a 1797-word window), recheck A3 (%s); the line before it ("Is there a way you could try this on a smaller scale?") read Human (Medium, 0.967, 57 words); Human (High, 132 words) for the stretch through the API (b474_trouble, %s)' % (RA3, API474),
        labels=[O['q2s'], O['direct'], L['people']],
        meaning_error='The requests were made of the inner process ("Show me ...") and are now made to yourself ("Show yourself ..."); "body" is dropped and "what today is for" became what you want or need.',
        note='Shape: a verbless question fragment with a slash list ("Showing yourself just one sensation in your body / one word / whether to listen today or rest?") became an instruction with a comma list and a second verb ("ask yourself if you want to ... or if you need to rest").'))
    P.append(dict(
        id='b474-trouble-fake', batch='474', detector='Pangram 4.1', kind='pass',
        input=J(C474, 'b474_trouble/old/2', 'Do you know what exactly feels fake', 'the role etc?'),
        input_reading='AI (Medium, 0.94, 34 words, marked humanized), recheck of 2026-10-23 part A (%s); Emulate\'s earlier output (emu-as)' % R1023A,
        emulate=T('fix-20261023/b474/bm/HG-A-trouble.out.txt', 'Do you have a sense of what it is that feels fake?', 'have to play etc.'),
        emulate_reading='Human (High, 0.999, in a 1797-word window), recheck A3 (%s)' % RA3,
        labels=[L['colon'], L['split'], L['concrete'], L['casual']],
        meaning_error='"First" (ask first) is gone: a no now has no next step.',
        note='Shape: one question with a dash and a short list tucked into it ("... feels fake - the words, an image, what you are expecting, the role etc?") became a plain question, then the list as its own verbless line with fuller, more particular items ("what you are expecting to get from this, a role you feel you have to play etc.").'))
    P.append(dict(
        id='b474-stand', batch='474', detector='Pangram 4.1', kind='pass-low',
        input=J(C474, 'b474_s3c/old/0', 'Move around a bit, and don’t get up', 'do the whole job).'),
        input_reading='AI (Low, 0.575, 38 words), recheck of 2026-10-23 part A (%s)' % R1023A,
        emulate=J(C474, 'b474_s3c/new/0', 'Move around a bit.', 'but not always).'),
        emulate_reading='Human (Low, 0.503, 4 words) and Human (Low, 0.714, 56 words), recheck A3 (%s): a weak pass; the unchanged lines before it read AI (Low) in the same check, and batch 475 replaced the stretch' % RA3,
        labels=[L['split'], L['concrete'], L['uneven']],
        meaning_error='"stand only when steady" became "until you feel like you can do so without falling over", a lower bar; "the count is supposed to bring you back" became "counting does this, but not always".',
        note='Shape (two samples spliced: bn, then bm): one joined instruction became a four-word sentence and a longer one with a vivid particular ("without falling over").'))
    # ---- batch 475 (bo, bp, bq): the return stretch that read red in recheck A3 ----
    P.append(dict(
        id='b475-script', batch='475', detector='Pangram 4.1', kind='pass',
        input=J(C475, 'script/old'),
        input_reading='AI (Low, 0.503, 23 words) and AI (Low, 0.684, 93 words), recheck A3 (%s). Emulate\'s earlier output (emu-ax) with the lane\'s fixes.' % RA3,
        emulate=J(C475, 'script/new'),
        emulate_raw=T('fix-20261023/b475/bo/HG-A-return.out.txt', 'All the instructions you have given me', 'adult judgement."'),
        emulate_reading='Human (High, 0.999, in a 1587-word window), recheck A4 (%s)' % RA4,
        labels=[L['join'], O['runon'], O['noise']],
        meaning_error='The triage changed the sample\'s "instruction" to "intention" (the reader\'s fix); the raw sample\'s "in to", "every day" and "judgement" were put back to the guide\'s spelling.',
        note='Shape: two sentences, the second with neat paired commas ("The only instruction ..., or the only cue ..., is the one ..., and neither ..."), became one long comma-spliced run with almost no internal commas ("... are now finished, the only intention I will take ... or the only cue ... will be the one I consciously choose to and neither of them will keep me in this state.").'))
    P.append(dict(
        id='b475-count', batch='475', detector='Pangram 4.1', kind='pass',
        input=J(C475, 'count/old'),
        input_reading='AI (Low, 0.684, 93 words), AI (Medium, 0.951, 20 words) and AI (Low, 0.644, 31 words), recheck A3 (%s)' % RA3,
        emulate=J(C475, 'count/new'),
        emulate_raw=T('fix-20261023/b475/bp/HG-A-return.out.txt', 'Then do a count up', 'the session is now over.'),
        emulate_reading='Human (High, 0.999), Human (Medium, 0.988, 39 words) and Human (High, 0.995, 52 words), recheck A4 (%s)' % RA4,
        labels=[O['runon'], L['join'], O['minimal']],
        meaning_error='Raw sample: "you can put your weight here if you like" and "know where you are" for "of your choice" and "name where you are"; the lane put his words back.',
        note='Shape: numbered fragments ("1...feel your body again ... 2...feel your breathing ...") became full sentences with the number as a time ("On 1 start to feel ..."), and the closing line was joined onto step 5 with "and" ("... feeling normal and clear and the session is now over.").'))
    P.append(dict(
        id='b475-reorient', batch='475', detector='Pangram 4.1', kind='pass',
        input=J(C475, 'reorient/old'),
        input_reading='AI (Low, 0.644, 31 words), AI (Low, 0.575, 7 words) and AI (Low, 0.531, 7 words), recheck A3 (%s). Emulate\'s own earlier output (emu-ax), which had split the published "Look left, right, near, and far." into two sentences.' % RA3,
        emulate=J(C475, 'reorient/new'),
        emulate_raw=T('fix-20261023/b475/bo/HG-A-return.out.txt', 'When you come out make sure you remember', 'something further away.'),
        emulate_reading='Human (High, 0.995, 52 words), recheck A4 (%s)' % RA4,
        labels=[L['join'], O['runon'], O['soft']],
        meaning_error='Raw sample: "make sure you remember what day" for "remind yourself" (the lane: "make sure you can name").',
        note='Shape: three short command sentences became one comma-run instruction ("When you come out make sure you can name what day (or date) it is, look to your left and right, look at something near to you and something further away."). The same content split into short commands read AI three times in a row.'))
    P.append(dict(
        id='b475-note', batch='475', detector='Pangram 4.1', kind='pass',
        input=J(C475, 'note/old'),
        input_reading='Human (Medium, 0.974, 43 words) for the first sentence and AI (Medium, 0.977, 36 words) for the second, recheck A3 (%s)' % RA3,
        emulate=J(C475, 'note/new'),
        emulate_raw=T('fix-20261023/b475/bo/HG-A-return.out.txt', 'Note: If you are going to sleep to a recording', 'indefinite length of time.'),
        emulate_reading='Human (High, 0.998, in a 521-word window), recheck A4 (%s)' % RA4,
        labels=[L['join'], O['runon'], O['formal']],
        meaning_error='',
        note='Shape: two sentences joined into one with ", however", then a comma splice into the list ("... an altered state, this includes leaving yourself in a role, ..."), contractions removed, and the last item made a phrase ("for an indefinite length of time").'))
    # ---- the screening post of 2026-10-22: raw samples, two per input, one Human and one not ----
    P.append(dict(
        id='screen-S2-metaphors', batch='screen 2026-10-22 (emu-bd)', detector='Pangram 4.1', kind='pass',
        input=T(PUB17, 'Choose one purpose, one starting anchor', 'stops helping.'),
        input_reading='The published section read AI (High, a 1642-word window) in the 4.0 baseline (batch 429, %s); in 4.1 the installed sample ba of this section read AI with most windows marked humanized (whole-guide check 41r3-a, %s)' % (B429, W41R3A),
        emulate=T('fix-20261018/emu-bd/HG17-pub2.out.txt', 'Have some idea what you want to do', 'if you do so consciously.'),
        emulate_reading='Human (High, 0.999, in a 1847-word window) in the screening post (%s); sample S2 read Human in every window' % SCR,
        labels=[L['people'], L['quip_out'], O['soft'], O['etc']],
        meaning_error='"neutral witnessing" became "neutral"; "a firm boundary" became "protective, forceful"; "when the metaphor stops helping" is gone.',
        note='Shape: noun lists ("one purpose, one starting anchor or image, and a way back"; "Floating, stairs, gardens, ...") became things the reader does ("what you want to do, where you are starting, how you will get back"; "You may want to float, go down stairs, walk in a garden ..., etc."), and the quip ("do not all need to report for duty at once") became a plain reason ("It doesn\'t make sense to do all of these in one session."). Compare screen-S1-metaphors, the same input in sample bc, which read AI.'))
    P.append(dict(
        id='screen-S2-imagery', batch='screen 2026-10-22 (emu-bd)', detector='Pangram 4.1', kind='pass',
        input=T(PUB17, 'Imagery is optional.', 'replacing your identity.'),
        input_reading='As screen-S2-metaphors: the published section read AI (High) in 4.0 (%s); its installed Emulate version read AI (humanized) in 4.1 (%s)' % (B429, W41R3A),
        emulate=T('fix-20261018/emu-bd/HG17-pub2.out.txt', 'You don\'t have to use imagery at all.', 'don\'t change your identity.'),
        emulate_reading='Human (High, 0.999, in a 1847-word window) in the screening post (%s)' % SCR,
        labels=[L['colon'], L['hedge'], O['quote'], O['etc'], O['aside'], L['join']],
        meaning_error='"no response at all" became "nothing"; "let a count mark something meaningful there" became "even as you count, etc." (the instruction about the count is gone).',
        note='Shape: a short definition line ("Imagery is optional."), a noun list and a colon instruction became a "you" sentence, a looser list with a quoted inner phrase ("\\"I know it,\\""), and one joined, hedged instruction ("If you do choose a metaphor, try to stay in that \\"world,\\" even as you count, etc., and come back ..."). Compare screen-S1-imagery (sample bc), which kept the noun list and read AI.'))
    P.append(dict(
        id='screen-S4-active', batch='screen 2026-10-22 (emu-bf)', detector='Pangram 4.1', kind='pass',
        input=T(FX17, 'If your state of being still', 'disappear inward.'),
        input_reading='AI in 4.1: this installed text (sample ba with the lane\'s fixes) read AI with its windows marked humanized in whole-guide check 41r3-a, "Don\'t try to disappear inward." AI (Medium, 6 words) and the script after it AI (High, 56 words) (%s)' % W41R3A,
        emulate=T('fix-20261018/emu-bf/HG17-fx1.out.txt', 'If being still tends to make you sleepy', 'escape inside yourself.'),
        emulate_reading='Human (High, 0.998, 99 words) and Human (High, 0.999, 32 words) in the screening post (%s); sample S4 read Human in every window' % SCR,
        labels=[L['split'], L['uneven'], L['def'], L['people']],
        meaning_error='The step "making a deliberate movement with one hand as you bring yourself into a clearer state" became "Tell yourself that as you move one of your hands, you\'re going to move deliberately": the clearer state is gone from the step (the comprehension pass later restored it).',
        note='Shape: a "since hypnosis can be more alert rather than more relaxed" explanation became an instruction ("Instead of getting more relaxed ..., try getting more alert."); a verbless "For example, keeping ..., and making ..., and then ceasing ..." fragment became a four-word command ("Keep your eyes open.") and a long spoken sentence. Compare screen-S3-active (sample be), which read AI.'))
    return P
