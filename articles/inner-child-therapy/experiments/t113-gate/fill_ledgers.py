#!/usr/bin/env python3
"""Turn 113: the writer's half of each gate manifest (docs/HUMANIZATION-OWNER-DELIVERY-GATE.md): who wrote it, a literal
T/C judgment for every inventory row (docs/HUMANIZATION-TELL-INVENTORY.md), a reason for each linter REVIEW finding, and
where the three reviewers' reports go. The reviews are three fresh subagents, one per role, each reading only the files
(REVIEW-BRIEF.md). Run after make_gate_files.py; it refuses a manifest whose hashes don't match its files."""
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ME = {'name': 'Claude Opus 5.5, the Inner Child lane writer', 'context_id': 'session_01NbUfhcTaRT8sbjyYV1wEFq'}
REVIEWS = {'preservation': 'REVIEW-preservation.json', 'cold_read_1': 'REVIEW-cold_read_1.json', 'cold_read_2': 'REVIEW-cold_read_2.json'}
A = 'ABSENT'


def heading_rows(draft, said):
    q = '"%s"' % draft
    base = {
        'T01': 'a heading, %s, with no first-person stake of its own; the paragraph under it keeps his "I\'d"s' % q,
        'T02': '%s names one case; it is not a run of compressed commands' % q,
        'T03': '%s names what the paragraph right under it is about; nothing arrives unprepared' % q,
        'T04': 'no scene in %s' % q,
        'T05': 'no concrete prop in %s' % q,
        'T06': 'no vague healing or process language in %s; its words are the paragraph\'s own subject' % q,
        'T07': 'no filler or staged hesitation in %s' % q,
        'T08': 'no image followed by an explanation in %s' % q,
        'T09': 'the headings come only where a paragraph is its own case; the paragraphs keep their uneven lengths and asides',
        'T10': 'no "you don\'t have to X before Y" packaging in %s' % q,
        'T11': '%s labels a case a reader may be in; it is not prose connective tissue between document parts' % q,
        'T12': 'the case headings in the section name cases a reader may or may not be in (an open set of situations), not a closed taxonomy built for coverage',
        'T13': 'the paragraphs under %s keep their reasons, asides and callbacks; the heading removes none' % q,
        'T14': 'no material moved to dodge a detector: the heading is Joel\'s skimming idea, placed only where a paragraph is its own case',
        'T15': 'plain words in %s, chosen for a reader skimming for their situation, not for unlikelihood' % q,
        'T16': 'no "not X, it\'s Y" in %s' % q,
        'T17': 'no thesis or aphorism in %s; it names a situation' % q,
        'T18': 'no premise flipped by a short sentence in %s' % q,
        'T19': '%s is a heading that labels its paragraph, the way the article\'s other headings do; it is not a sentence whose only job is to announce' % q,
        'T20': '%s ends no paragraph' % q,
        'T21': '%s does one job: it names a case' % q,
        'T22': 'no reassurance in %s' % q,
        'T23': 'no generic scenery in %s' % q,
        'T24': 'no faux-insight setup in %s' % q,
        'T25': 'no colon in %s' % q,
        'T26': 'no distinctive word of %s is repeated without a job; a word it shares with the paragraph is how a skimmer finds the paragraph' % q,
        'T27': 'none of the tic words in %s' % q,
        'T28': '%s does not end its section' % q,
        'T29': '%s is not a paragraph\'s last sentence' % q,
        'C01': 'the inner child is not named in %s, and "the kid" appears nowhere in it' % q,
        'C02': 'any pronoun in %s points at the section\'s subject, named in the section heading and the paragraphs above' % q,
        'C03': 'no fact about Joel\'s life in %s' % q,
        'C04': 'no claim about a study, person or product in %s' % q,
    }
    return rows(base, said)


def rows(base, said):
    out = []
    for k, ev in base.items():
        if k in said:
            st, ev2, *why = said[k]
            r = {'id': k, 'status': st, 'evidence': ev2, 'resolution': 'JUSTIFIED_KEEP' if st == 'PRESENT' else ''}
            if st == 'PRESENT':
                r['reason'] = why[0]
            out.append(r)
        else:
            out.append({'id': k, 'status': A, 'evidence': ev, 'resolution': ''})
    return out


def solomon_rows(draft, said):
    q = '"... and the blind spot behind it even has a name, Solomon’s paradox ..."'
    base = {
        'T01': 'no first-person stake; the sentence is Joel\'s, about a named effect',
        'T02': 'one sentence about the trick and its name, not a run of compressed commands',
        'T03': 'the sentence before it is the exercise ("put somebody you care about into your exact life ... ask what you’d tell them as a friend"); "This psychological trick" is that exercise',
        'T04': 'no scene of mine; the king is the study\'s and his ("the biblical king everybody brought their disputes to")',
        'T05': 'no concrete prop in the sentence; the king and his disputes are his own comparison',
        'T06': '"the blind spot behind it" names a specific thing, the self-other asymmetry the study names Solomon\'s paradox',
        'T07': 'no filler or staged hesitation',
        'T08': 'no image followed by its explanation',
        'T09': 'one change in one sentence; the paragraph keeps its two sentences as he wrote them',
        'T10': 'no "you don\'t have to X before Y" packaging',
        'T11': 'it carries a claim (the effect has a name and a story), not a bridge',
        'T12': 'no matched pair or closed list',
        'T13': 'his asides stay ("has a rich history around it", "who then wrecked his own life")',
        'T14': 'no material moved to dodge a detector: the change makes the name accurate (his 109 A)',
        'T15': '"blind spot" is the plain word for what the study measures, chosen for accuracy, not unlikelihood',
        'T16': 'no "not X, it\'s Y"',
        'T17': 'no aphorism: a named effect with its origin',
        'T18': 'no premise flipped by a short sentence',
        'T19': 'it does not announce what comes next',
        'T20': 'the paragraph ends on his "who then wrecked his own life", unchanged',
        'T21': 'one job: the trick has a history, and the gap behind it a name',
        'T22': 'no reassurance',
        'T23': 'no generic scenery',
        'T24': 'no faux-insight setup',
        'T25': 'no colon in the sentence; its commas are his',
        'T26': '"it" twice ("around it", "behind it") both mean the trick; no distinctive word repeated without a job',
        'T27': 'no tic words',
        'T28': 'not the section\'s end (the scaffolding paragraph follows)',
        'T29': 'the last sentence of its paragraph, and it adds a consideration (the name and the king), not a restatement',
        'C01': 'the inner child is not named, and "the kid" appears nowhere',
        'C02': '"it" in "behind it" is "This psychological trick", named just before',
        'C03': 'no fact about Joel\'s life',
        'C04': 'the claim about the study is now what the study says: its title names "Solomon\'s paradox" the self-other asymmetry, which "the blind spot behind it" is',
    }
    return rows(base, said)


ECHO = ('PRESENT', None, 'The heading shares one word with the paragraph\'s first sentence, which is how a reader skimming for this case finds it; the sentence goes on to say something the heading doesn\'t (what the case means, or what to do).')
CANDIDATES = {
    'guard-trust': ({'C02': (A, '"its" is the guard, the section\'s subject ("Hear the Guard First", "that part" above); the paragraph under it says "that guard\'s trust"')}, {}),
    'guard-step-back': ({'C02': (A, '"it" is the guard; "step back" picks up the section\'s own question, "What are you afraid would happen if you stepped back?"')}, {}),
    'guard-fault': ({'T26': (A, '"it\'s all your fault" is the reader\'s own self-talk, which the paragraph quotes as "It\'s all my fault"; the heading names the situation in those words and the paragraph explains it')}, {}),
    'start-thoughts': ({'C02': (A, 'no pronoun; "thoughts" covers the fear, the stray thought and the worry the paragraph under it sorts')}, {}),
    'start-anxiety': ({'T26': ('PRESENT', 'the heading "If it\'s anxiety" and the first sentence "Anxiety is often a part of you that\'s trying to protect you" share "anxiety"', ECHO[2])}, {}),
    'start-says-no': ({'T26': ('PRESENT', 'the heading "If a part says no" and the first sentence "If a part hesitates ... or says no to going deeper" share "a part" and "says no"', ECHO[2])}, {}),
    'change-empty': ({'T15': (A, '"sound empty" says plainly what the paragraph\'s "the words are all there, but the loving grown-up behind them isn\'t" is like from the inside')}, {}),
    'change-relief': ({'T26': (A, 'the paragraph says "Some relief is nice"; the heading names the case, the paragraph its example ("lighter for a few hours")')}, {}),
    'change-stop': ({'T26': (A, 'no word repeated: the first sentence says "Not wanting to do it anymore", the heading "rather stop"')}, {}),
    'change-different': ({'T26': ('PRESENT', 'the heading "If your case is different" and "consider if you have a unique case" share "case"', ECHO[2])}, {}),
    'escape-vulnerable': ({'T26': ('PRESENT', '"vulnerable" in the heading, "a vulnerability in you" in the first sentence', ECHO[2]),
                           'C04': (A, 'no claim: the paragraph\'s own warning signs (mania, paranoia, family history) are what "vulnerable" names')}, {}),
    'escape-confused': ({'T26': (A, 'the heading takes the words of the sentence it replaces ("Say you keep coming back from trips confused or spaced out."), which goes, so nothing is said twice')}, {}),
    'therapist-ifs': ({'T12': (A, 'two named therapies, the two the paragraph names ("Internal Family Systems (IFS), or Schema Therapy"); a real pair, not a balanced contrast')}, {}),
    'hooks-change': ({'T24': (A, 'a reader\'s real question ("Can they change?") answered flatly by the paragraph under it ("You may not know for certain ... and neither do they")'),
                      'C02': (A, '"they" is "the other person" of the section, named in its first paragraph')},
                     {'B7 short landing at paragraph end': 'The linter reads the heading alone as a paragraph. It is a heading over a paragraph of five sentences, so it lands nothing.',
                      'D9 follows the source order': 'A heading over its own paragraph follows that paragraph by design; nothing is reordered.'}),
    'hooks-less-safe': ({'T26': ('PRESENT', 'the heading "Feeling less safe" and the first sentence "If a relationship keeps making you feel less safe" share "less safe"', ECHO[2])}, {}),
    'start-stop': ({'T26': (A, 'the heading shares only "stop" with "I\'d stop there and not test it", and names the action for a reader whose part hesitates or says no; the cases (touch, sex, going deeper, an altered state) are in the sentence, said once'),
                    'C02': (A, 'no pronoun in "When to stop"')}, {}),
    'change-working': ({'T26': (A, 'the heading takes the condition of the sentence under it ("if you keep following the reparenting steps correctly without getting the expected results"), which leaves the sentence, so nothing is said twice'),
                        'C02': (A, '"it" is the practice the section is about ("When to Change the Strategy")')}, {}),
    'escape-trips': ({'T26': (A, 'the heading is the paragraph\'s first sentence ("Say you keep coming back from trips confused or spaced out."), which leaves the paragraph, so nothing is said twice; "trips like that" in the next sentence points at it'),
                      'C02': (A, 'no pronoun; "trips like that" right under it points at the heading\'s "trips"')}, {}),
    'escape-prone': ({'T26': (A, '"mania or psychosis" is the paragraph\'s own pair ("any predisposition toward mania or psychosis"), the words a reader with that history looks for; the paragraph says what to do'),
                      'T06': (A, '"prone to mania or psychosis" names the specific risk the paragraphs warn about, not a generic vulnerability (the round-1 reviewers\' point)'),
                      'C04': (A, 'no claim: the paragraph\'s own warning signs are what the heading names')}, {}),
    'borrow-guiding': ({'T12': (A, 'the three headings "For warmth", "For protecting", "For guiding" are the article\'s own three jobs of the inner adult (Nurturer, Protector, Guide), and the first two are the paragraphs\' own first words; the third completes his structure, not one made for coverage'),
                        'T26': (A, '"guiding" names the Guide\'s job; the paragraph says "The Guide can be you too"')}, {}),
    # round 3 (after the section cold reads): changed words get their own rows; unchanged words keep their base's
    'guard-trust-r3': ({'C02': (A, '"its" is the guard, the section\'s subject ("Hear the Guard First", "that part" above); the paragraph under it says "that guard\'s trust"'),
                        'T15': (A, '"day to day" says plainly where the trust is earned, the paragraph\'s "mostly out in ordinary life", for a reader who expects it in the session')}, {}),
    'guard-fault-r3': ({'T26': (A, 'the heading puts the reader\'s own feeling in plain words; the paragraph quotes the self-talk once, as "It\'s all my fault", and says what it may be doing'),
                        'C02': (A, '"it all" is everything going wrong, the reader\'s own sense of it; no pronoun points at the guard')}, {}),
    'start-noanswer': ({'T26': (A, 'the heading pairs with "If you do get an answer" right after it; the paragraph under it says "Even without the answer", which the heading sets up'),
                        'C02': (A, 'no pronoun; "answer" is the answer to the question just asked ("What\'s going on?") and waited for')}, {}),
    'change-empty-r3': ({'T15': (A, '"sound empty" says plainly what the paragraph\'s "the words are all there, but the loving grown-up behind them isn\'t" is like from the inside'),
                         'C02': (A, '"your kind words" are the words said to your little one, the paragraph\'s "the words" and "sweeter and sweeter things"')}, {}),
    'escape-badtrip': ({'T26': (A, 'no word repeated: the paragraph names the bad reactions (manic, psychotic, paranoid, worse afterward); the heading names the reader\'s case in one plain phrase'),
                        'C04': (A, 'no claim: the paragraph\'s own reactions are what "went badly" names')}, {}),
    'escape-paranoia': ({'T24': (A, 'a real reader\'s question ("Is your paranoia a warning sign?") answered flatly by the sentence under it ("can be a warning sign for psychosis, but it doesn\'t automatically lead there")'),
                         'T26': ('PRESENT', 'the heading and the first sentence share "paranoia" and "warning sign"', 'The heading is the reader\'s question in the paragraph\'s own words, and the sentence answers it with what the heading can\'t say: when it is a warning sign and when it is not.')},
                        {'B7 short landing at paragraph end': 'The linter reads the heading alone as a paragraph. It is a heading over two paragraphs, so it lands nothing.',
                         'D9 follows the source order': 'A heading over its own paragraphs follows them by design; nothing is reordered.',
                         'E36/E41 heavy second person': 'The linter counts one "your" in a six-word heading. It is the heading asking the reader\'s own question, as the guide\'s other headings speak to the reader ("If you do get an answer").'}),
    'escape-prone-r3': ({'T26': (A, '"mania or psychosis" is the paragraph\'s own pair ("any predisposition toward mania or psychosis"), the words a reader with that history looks for; the paragraph says what to do'),
                         'T06': (A, '"prone to mania or psychosis" names the specific risk the paragraph warns about, not a generic vulnerability'),
                         'C04': (A, 'no claim: the paragraph\'s own warning signs are what the heading names')}, {}),
    'escape-trusted': ({'T26': ('PRESENT', 'the heading and the first sentence share "trusted"', 'The heading asks what the paragraph\'s first words answer ("By trusted, I mean"), so the shared word is the question and its answer; "trusted advisors" in the paragraph above is what it picks up.'),
                        'C02': (A, 'no pronoun in "Who counts as trusted"; its "trusted" picks up "trusted advisors" just above')}, {}),
    'escape-trips-r3': ({'T26': (A, 'the heading is the paragraph\'s first sentence ("Say you keep coming back from trips confused or spaced out.") with "If" for "Say"; the sentence leaves the paragraph, so nothing is said twice; "trips like that" in the next sentence points at it'),
                         'C02': (A, 'no pronoun; "trips like that" right under it points at the heading\'s "trips"')}, {}),
    'escape-meds': ({'T26': (A, 'the heading shares "medication" with "Don\'t suddenly stop a medication"; it names the reader\'s case before the advice, which says what to do'),
                     'C04': (A, 'no claim: "quit a medication or alcohol" is the paragraph\'s own two cases ("stop a medication", "quit cold turkey", "Alcohol withdrawal")')}, {}),
    'therapist-licensed': ({'T26': (A, '"licensed" is the paragraph\'s own word ("The best licensed, listed therapists"), the one that sets it apart from the often-unlicensed reparenting therapists above; the sentence goes on to name the two therapies'),
                            'C02': (A, 'no pronoun in "If you want a licensed therapist"')}, {}),
}
SOLOMON_LINT = {
    'B4/E15 list or packed sentence': 'It is Joel\'s sentence, with its appositive and its relative clause, as he wrote it ("this version passes"); the change adds five words inside it and no clause.',
    'D9 follows the source order': 'It is his sentence with one phrase changed, so it follows his order by design.',
    'O25 "even" or "actually", 1 in my text (TELLS-FROM-PANGRAM-DATA-20261007.md: they go with the failing paragraphs; "They\'re words I add to sound casual, and they don\'t help"): keep one only where it says something':
        'The "even" is his ("and even has a name"), kept with his sentence; it says the effect is well enough known to be named.',
    'O6 a candidate, to judge, not a finding: a feeling or idea doing what a person does. A neat, quotable line is the tell ("Grief doesn\'t keep a schedule"); a phrase people say all the time is not (Joel 2026-10-07 23:50: "Modern life trains us" is "so common it\'s almost cliche, it\'s not a witty AI quip"). Judge each with abstract_agents_prompt.py or by his ratings; fix only a quip, giving the action to a person with as few words changed as possible':
        'No quip: "a blind spot ... has a name" is the ordinary way to say an effect is named, and the trick "has a rich history" is his.',
}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


for d in sorted(p for p in HERE.iterdir() if p.is_dir() and (p / 'ADMISSION.json').exists()):
    name = d.name
    m = json.loads((d / 'ADMISSION.json').read_text(encoding='utf-8'))
    assert m['candidate_sha256'] == sha(d / 'DRAFT.txt') and m['context_sha256'] == sha(d / 'CONTEXT.txt'), name
    draft = (d / 'DRAFT.txt').read_text(encoding='utf-8')
    if name == 'solomon':
        m['tell_ledger'] = solomon_rows(draft, {})
        reasons = SOLOMON_LINT
    else:
        said, reasons = CANDIDATES[name] if name in CANDIDATES else CANDIDATES[name[:-3] if name[-3:] in ('-r2', '-r3') else name]
        m['tell_ledger'] = heading_rows(draft, said)
    m['writer'] = ME
    labels = [f['label'] for f in m['lint']['findings']]
    assert set(labels) == set(reasons), (name, labels)
    for f in m['lint']['findings']:
        f['disposition'] = 'JUSTIFIED_KEEP'
        f['reason'] = reasons[f['label']]
    m['review_files'] = dict(REVIEWS)
    m['status'] = 'READY_FOR_CHECK'
    (d / 'ADMISSION.json').write_text(json.dumps(m, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    present = [r['id'] for r in m['tell_ledger'] if r['status'] == 'PRESENT']
    print('%-18s ledger %d rows, present %s, lint %d' % (name, len(m['tell_ledger']), present, len(labels)))
