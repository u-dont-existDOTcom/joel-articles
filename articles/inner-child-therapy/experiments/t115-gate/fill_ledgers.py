#!/usr/bin/env python3
"""Turn 115: the writer's half of each gate manifest (docs/HUMANIZATION-OWNER-DELIVERY-GATE.md) for the five reworded
paragraphs of the pass: who wrote it, a literal T/C judgment for every inventory row (docs/HUMANIZATION-TELL-INVENTORY.md),
a reason for each linter REVIEW finding, and where the three reviewers' reports go. The reviews are three fresh
subagents, one per role, each reading only the files and the brief. Run after make_gate_files.py; it refuses a manifest
whose hashes don't match its files. Adapted from experiments/t113-gate/fill_ledgers.py."""
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ME = {'name': 'Claude Opus 5.5, the Inner Child lane writer', 'context_id': 'session_01NbUfhcTaRT8sbjyYV1wEFq'}
REVIEWS = {'preservation': 'REVIEW-preservation.json', 'cold_read_1': 'REVIEW-cold_read_1.json', 'cold_read_2': 'REVIEW-cold_read_2.json'}
A = 'ABSENT'
D9 = 'It is the same paragraph with one tell taken out, so it follows the approved paragraph\'s order by design; each sentence still notices something (T13 and T09 in the ledger).'

ROWS = {
    'F02': {
        'T01': 'no first person in the two sentences; they continue the exercise in his paragraph before',
        'T02': 'an instruction and its example, after his own paragraph; no run of compressed commands',
        'T03': '"whatever you\'d tell them" picks up his "ask what you\'d tell them as a friend" right before it',
        'T04': 'no scene: one example of a small step (teeth before midnight)',
        'T05': 'the example is the approved paragraph\'s own (teeth before midnight instead of at two), not a new prop',
        'T06': 'concrete words: sleep, teeth, midnight, two',
        'T07': 'the filler "then for now just try" is gone; nothing staged',
        'T08': 'the image "hand it to yourself" is gone; "do it yourself" says the step plainly, with nothing explained after',
        'T09': 'the paragraph keeps its scaffolding aside and link after these two sentences; the sentences differ in shape',
        'T10': 'no "you don\'t have to X before Y" packaging',
        'T11': '"Then" moves his exercise to its next step; it carries the step, not a bridge',
        'T12': '"before midnight instead of at two" is the example\'s own pair of times, the size of the step, not a balanced contrast',
        'T13': 'the paragraph names the technique (scaffolding, linked) after the example',
        'T14': 'nothing reordered or moved; a reassuring follow-up ("and it works now, too") is cut where it was',
        'T15': 'the structure changed (the image and the packaged example are gone), not just words swapped',
        'T16': 'no "not X, it\'s Y"',
        'T17': 'no thesis line: an instruction and an example',
        'T18': 'no premise flipped by a short sentence',
        'T19': 'neither sentence announces what comes next',
        'T20': 'the paragraph ends on the scaffolding sentence with its link, as approved, not a new closer',
        'T21': 'one job each: the step, then the example',
        'T22': '"start by" and the reassurance are gone; what stays is the guide\'s step, said once',
        'T23': 'the teeth at two in the morning are the approved example, specific to the sleep advice',
        'T24': 'no question in the sentences',
        'T25': 'no colon in the sentences',
        'T26': '"get more sleep" appears once; "them" is the person from his paragraph',
        'T27': 'none of the tic words',
        'T28': 'not the end of the section (Show Up When Nothing\'s Wrong follows)',
        'T29': 'not the paragraph\'s last sentence (the scaffolding sentence follows)',
        'C01': 'the inner child is not named, and "the kid" appears nowhere',
        'C02': '"them" is "somebody you care about" in his paragraph before; "it" in "If it\'s" is whatever you\'d tell them',
        'C03': 'no fact about Joel\'s life',
        'C04': 'no claim about a study, person or product in the two sentences; the scaffolding link after them is unchanged',
    },
    'F04': {
        'T01': 'the first person of "None of that is me answering" is gone; no preference or care is staged',
        'T02': 'two sentences that finish a safety instruction: when it applies, and what it is for',
        'T03': '"Do the same" points at the instruction two sentences up; "the question of whether life is worth living" is the section\'s subject',
        'T04': 'no scene in the sentences',
        'T05': 'no props in the sentences',
        'T06': 'concrete conditions: can\'t stop yourself, badly disoriented, intoxicated, can\'t tell',
        'T07': 'no filler or staged hesitation',
        'T08': 'no image in the sentences',
        'T09': 'the two sentences have different jobs and shapes (a long condition sentence, a short purpose sentence)',
        'T10': 'no permission packaging',
        'T11': '"Do the same" is the instruction applied to more readers, not a bridge',
        'T12': 'the conditions are his guide\'s own ("can\'t stop yourself, are badly disoriented or intoxicated") and the grounding\'s MUST, in different shapes, not a balanced taxonomy',
        'T13': 'the purpose sentence is his guide\'s stance on the question, the thing the paragraph adds beyond the steps',
        'T14': 'nothing reordered: the safety order stands, and the scope line stays at the end where his guide has it',
        'T15': 'the shape changed: the question and its short answer became one condition, the disclaimer and its reframe one statement',
        'T16': 'the "None of that is me answering ... It just keeps ..." shape is gone; nothing is set up to be denied',
        'T18': 'the short knock-down "Treat it like it is." is gone; "can\'t tell" is a condition of the same instruction',
        'T19': 'nothing announces what comes next',
        'T20': 'the paragraph ends on what the steps are for, plainly, with no antithesis or polish',
        'T21': 'the long sentence has one job, when to do the same, with its conditions',
        'T22': 'no reassurance or anticipated feeling; a plain instruction and its purpose',
        'T23': 'no scenery in the sentences',
        'T24': 'the self-answered question ("Can\'t tell if that\'s you? Treat it like it is.") is gone',
        'T25': 'no colon in the sentences',
        'T26': '"the question" once in the draft; "Do the same" points back without repeating the steps',
        'T27': 'none of the tic words',
        'T28': 'not the end of the section: his paragraph and The Spiritual Side of the Question follow',
        'T29': 'the last sentence adds the guide\'s point (the steps don\'t settle the question, they keep it open), not a restatement of the steps',
        'C01': 'the inner child is not named, and "the kid" appears nowhere',
        'C02': '"any of this" is the paragraph\'s own conditions (about to act, the means close by); "Getting safe first" is the two steps just given',
        'C03': 'no fact about Joel\'s life; the "me" is gone',
        'C04': 'no claim about a study, person or product',
    },
    'F05': {
        'T01': 'the first person is the paragraph\'s own practice ("I\'d read it once as if I were them"); the approved sentence said "when I wrote it"',
        'T02': 'one sentence after one instruction; no run of commands',
        'T03': 'it gives the reason for the reread in the sentence before it',
        'T04': 'no scene beyond the approved "sitting there with my phone" before it',
        'T05': 'no new prop in the sentence',
        'T06': '"scared" and "a threat" are the plain feelings on each side of the message',
        'T07': '"Stuff" is the guide\'s own casual word ("the smaller stuff", "embarrassing stuff"), not a staged hesitation',
        'T08': 'no image followed by explanation',
        'T09': 'one sentence; the section around it is his long, uneven paragraphs',
        'T10': 'no permission packaging',
        'T11': 'a reason, not a bridge',
        'T12': 'the inversion (felt scared here, reads like a threat over there) is gone; it says what the message can sound like to them',
        'T13': 'it notices what fear does to a message on the other end',
        'T14': 'nothing reordered; the sentence is where it was',
        'T15': 'the balanced shape is gone, not only its words',
        'T16': 'no "not X, it\'s Y"',
        'T17': 'it is about the message you\'re about to send, not a general rule',
        'T18': 'no premise flipped',
        'T19': 'nothing announced',
        'T20': 'a plain reason, with no antithesis or polish',
        'T21': 'one job: why to read it as them',
        'T22': 'no reassurance',
        'T23': 'no scenery in the sentences',
        'T24': 'no question in the sentences',
        'T25': 'no colon in the sentences',
        'T26': '"them" twice in the paragraph, both the people you\'re writing to; nothing distinctive repeated',
        'T27': 'none of the tic words',
        'T28': 'the section ends on the reason to reread, practical, not uplift',
        'T29': 'it gives the reason for the reread, which the first sentence doesn\'t say, not a moral or a restatement',
        'C01': 'the inner child is not named, and "the kid" appears nowhere',
        'C02': '"them" is "them" of the sentence before, the people you\'re writing to',
        'C03': 'no new fact about Joel: the approved sentence already had "when I wrote it"',
        'C04': 'no claim about a study, person or product',
    },
    'F06': {
        'T01': 'no first person in the sentences',
        'T02': 'one sentence, the paragraph\'s first; no run of commands',
        'T03': '"how they got there" picks up the paragraphs before (their conditioning, history and pain)',
        'T04': 'no scene in the sentences',
        'T05': 'no props in the sentences',
        'T06': 'plain words about the people: answer for what they did, it hurt',
        'T07': 'no filler in the sentences',
        'T08': 'no image in the sentences',
        'T09': 'the paragraph keeps its fragment ("Or the skills.") and its uneven sentences',
        'T10': 'no permission packaging',
        'T11': 'it carries the claim, not a bridge',
        'T12': 'two facts about them and the harm, said about the people, with the concession as a clause',
        'T13': 'the concession ("even if you see how they got there") is the point the old short sentence made',
        'T14': 'nothing reordered; two sentences became one in place',
        'T15': 'the knock-down sentence is gone, not reworded into another knock-down',
        'T16': 'the "doesn\'t make it okay" negation is gone',
        'T17': 'it is about these people and this harm, not a general rule; the hypnosis guide\'s version of this shape ("They really did hurt us and they still have to answer for it, ...") read Human, high',
        'T18': 'the premise-and-knock-down pair is gone',
        'T19': 'nothing announced',
        'T20': 'not the paragraph\'s end',
        'T21': 'one job: they are still accountable, even understood',
        'T22': 'no reassurance',
        'T23': 'no scenery in the sentences',
        'T24': 'no question in the sentences',
        'T25': 'no colon in the sentences',
        'T26': '"still" twice, the approved sentence\'s own pair; "how they got there" once',
        'T27': 'none of the tic words',
        'T28': 'not the section\'s end',
        'T29': 'not the paragraph\'s last sentence',
        'C01': 'the inner child is not named, and "the kid" appears nowhere',
        'C02': '"They" are the people who hurt you, the section\'s subject; "how they got there" is what the paragraph before pictures',
        'C03': 'no fact about Joel\'s life',
        'C04': 'no claim about a study, person or product',
    },
    'F10': {
        'T01': 'no first person in the sentences',
        'T02': 'one parenthetical pointer at the paragraph\'s end',
        'T03': '"no example" picks up the paragraph\'s request for a real example ("as long as it really happened")',
        'T04': 'no scene in the sentences',
        'T05': 'no props in the sentences',
        'T06': 'concrete: an example of your own, another doorway',
        'T07': 'no filler in the sentences',
        'T08': 'no image followed by explanation',
        'T09': 'one aside in parentheses after his long paragraph',
        'T10': 'no permission packaging',
        'T11': 'a pointer for a reader the paragraph doesn\'t fit, not connective tissue',
        'T12': 'no matched pair',
        'T13': 'it notices the reader with no example',
        'T14': 'nothing moved or reordered',
        'T15': 'the question-and-answer shape is gone, not only its words',
        'T16': 'no "not X, it\'s Y"',
        'T17': 'no principle stated',
        'T18': 'no premise flipped',
        'T19': 'it points elsewhere for a reader who has no example; it does not announce the next section',
        'T20': 'a plain parenthetical pointer, not a clever closer',
        'T21': 'one job: a pointer',
        'T22': 'no reassurance',
        'T23': 'no scenery in the sentences',
        'T24': 'the self-answered question ("No example? Try another doorway.") is gone',
        'T25': 'no colon in the sentences',
        'T26': '"example" is the word the paragraph is about; "doorway" appears once',
        'T27': 'none of the tic words',
        'T28': 'not the h1\'s end (Notice the Part That Came Here follows)',
        'T29': 'it adds a pointer, not a restatement',
        'C01': 'the inner child is not named, and "the kid" appears nowhere',
        'C02': '"another doorway" is another of the ways into borrowing the adult that this part of the guide offers (its other sections), as before',
        'C03': 'no fact about Joel\'s life',
        'C04': 'no claim about a study, person or product',
    },
}
PRESENT = {
    'F04': {'T17': ('"Getting safe first keeps the question of whether life is worth living open long enough to look at." states what the steps are for',
                    'It is his guide\'s own point in this place ("It keeps the question open long enough to investigate it"), which the grounding review marked as a point the paragraph must carry; said once, about these steps, for a reader who may resist being told life is worth living.')},
}
LINT = {
    'F02': {'B2 contrast': '"before midnight instead of at two" is the approved example\'s own pair of times; it sizes the step, it is not a rhetorical contrast.',
            'D9 follows the source order': D9,
            'E36/E41 heavy second person': 'The two sentences are the guide\'s instruction to the reader, as the whole guide is; "you" and "your teeth" are the reader doing the step.'},
    'F04': {'B4/E15 list or packed sentence': 'One action ("Do the same") with its conditions: his guide\'s own ("can\'t stop yourself, are badly disoriented or intoxicated") and the grounding\'s MUST (if you can\'t tell, do the same), in different shapes; the list-of-three rule passes.',
            'D9 follows the source order': D9 + ' A safety instruction keeps its order.',
            'E36/E41 heavy second person': 'A safety instruction to a reader who may be about to act; the second person is its point.'},
    'F05': {'D9 follows the source order': D9},
    'F06': {'B1 finished principle': 'It is about the people who hurt you and this harm, with the concession as a clause: the shape the gate notes read Human, high in the hypnosis guide ("They really did hurt us and they still have to answer for it, ...").',
            'D9 follows the source order': D9},
    'F10': {'B7 short landing at paragraph end': 'A parenthetical pointer for a reader with no example, as the approved paragraph had; plain, with nothing to land.',
            'D9 follows the source order': D9},
}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


for name, rows in ROWS.items():
    d = HERE / name
    m = json.loads((d / 'ADMISSION.json').read_text(encoding='utf-8'))
    assert m['candidate_sha256'] == sha(d / 'DRAFT.txt') and m['context_sha256'] == sha(d / 'CONTEXT.txt'), name
    ids = [r['id'] for r in m['tell_ledger']]
    ledger = []
    for k in ids:
        if k in PRESENT.get(name, {}):
            ev, why = PRESENT[name][k]
            ledger.append({'id': k, 'status': 'PRESENT', 'evidence': ev, 'resolution': 'JUSTIFIED_KEEP', 'reason': why})
        else:
            ev = rows[k]
            assert len(ev) >= 12, (name, k)
            ledger.append({'id': k, 'status': A, 'evidence': ev, 'resolution': ''})
    m['tell_ledger'] = ledger
    m['writer'] = ME
    labels = [f['label'] for f in m['lint']['findings']]
    assert set(labels) == set(LINT[name]), (name, labels)
    for f in m['lint']['findings']:
        f['disposition'] = 'JUSTIFIED_KEEP'
        f['reason'] = LINT[name][f['label']]
    m['review_files'] = dict(REVIEWS)
    m['status'] = 'READY_FOR_CHECK'
    (d / 'ADMISSION.json').write_text(json.dumps(m, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('%s ledger %d rows, present %s, lint %d' % (name, len(ledger), [r['id'] for r in ledger if r['status'] == 'PRESENT'], len(labels)))
