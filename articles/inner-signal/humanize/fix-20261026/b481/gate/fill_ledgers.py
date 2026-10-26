#!/usr/bin/env python3
"""The writer's half of each batch 481 gate manifest (docs/HUMANIZATION-OWNER-DELIVERY-GATE.md): who wrote it, a literal
judgment on every inventory row (docs/HUMANIZATION-TELL-INVENTORY.md, T01 to T29 and C01 to C04, the row wording of
../../../fix-20261025/emulate-check/gate/fill_ledgers.py), a reason written for each draft's linter REVIEW findings, and
where the three reviewers' reports go. Run after make_gate_files.py; it refuses a manifest whose hashes don't match.

  python3 articles/inner-signal/humanize/fix-20261026/b481/gate/fill_ledgers.py [NAME ...]
"""
import hashlib
import importlib.util
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location('fill_prev', HERE.parents[2] / 'fix-20261025' / 'emulate-check' / 'gate' / 'fill_ledgers.py')
prev = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(prev)

ME = {'name': 'Claude Opus 5.5, the hypnosis guide lane\'s writer (the splices and their fixes; the words are Emulate\'s)',
      'context_id': 'session_01Mxpoi6tFT3FgKmBvtGjRtS'}
REVIEWS = dict(prev.REVIEWS)
A = 'ABSENT'
# D9 for every draft: Emulate rewrote the passage it replaces, so its points come in that passage's order; the turns named
# are Emulate's own.
TURNS = {
    'G-S11': '"read some of the stuff in"', 'G-S12': '"It\'ll be really helpful", "as it\'s a long one"',
    'G-S14': '"There are a lot of ways", "has a report on", the dash', 'G-S15': 'the dash joining the list to the question',
    'G-S16': '"each can correct the other"', 'G-S17': 'the line without "And"',
    'G-S18': '"One reason might have been", "when I did that", "But I think a bigger reason is"',
    'G-S19': '"I can tell", "twist it around to a yes"', 'G-S20': '"be able to", "the quiet little preferences that you have", "know for sure", "going by"',
    'G-S21': '"make sure to"', 'G-S22': '"And then", "NOT going to help you", "soup to you at that point"',
    'G-S23': '"Think about", "Are there things"', 'G-S24': '"Make sure you\'re in a safe place"',
    'G-S25': '"Decide to do it", "etc." for "Something else?", the questions split', 'G-S26': '"What is one next thing I can do?"',
    'G-S27': '"if it has to do with trauma or memories", "take it as an image", "outside help"',
    'G-S28': '"Could you try"', 'G-S29': '"Maybe ask to be shown just", "Or even just"',
    'G-S30': '"Have you got any sense", "that\'s making it feel fake"', 'G-S31': '"You may have", "in the past"',
    'G-S32': '"gives someone a choice between two genuinely safe things to do", the term for "one"', 'G-S33': '"Here is a little script"',
    'G-S34': '"Let\'s see if I can find"', 'G-S36': '"What’s theirs and what’s mine?" for two questions',
}
LINT_BY = {
    ('G-S14', 'E186 "without ...ing"'): 'The sentence\'s point is influence that bypasses the conscious mind, his published "Influence doesn’t wait for the conscious mind to sign a form."; "without engaging their conscious mind" names exactly that, and the next sentence (his own) says who knows it.',
    ('G-S15', 'B4/E15 list or packed sentence'): 'The four kinds of agreement are his published four ("Conscious agreement is one thing. Unconscious receptivity is another. Emotional compliance is another. Legal and ethical consent is another."), already listed in the paragraph; the change joins them to the question with a dash.',
    ('G-S27', 'B4/E15 list or packed sentence'): 'The list is the middle sentence\'s, which stays word for word (the paragraph he approved in batch 470: "The mind makes it symbolic, squashes things together, distorts, dramatizes, pulls from cultural influences, fears etc."); the change is the sentences around it.',
    ('G-S16', 'B7 short landing'): 'It ends the paragraph as the sentence it replaces did ("So these modes can correct each other."), saying the consequence of the four "Without ..." lines before it: his published "Let the modes correct each other." It sums nothing up that the lines before don\'t lead to.',
    ('G-S17', 'B7 short landing'): 'It is the whole paragraph, as the approved line was ("And it’s got to lead somewhere!"): the practice has to lead to something real, his published "A powerful state matters only if something survives it". Only the "And" is gone.',
    ('G-S22', 'B7 short landing'): 'It ends the paragraph as the approved "It\'s all just soup." did: his own image (published: "long elegant sentences become soup during an induction"), and "at that point" places it in the induction; it doesn\'t sum the paragraph up.',
    ('G-S23', 'B7 short landing'): 'The linter sees the draft alone. In the article it isn\'t the paragraph\'s end: "How long do you want to spend on this?" and the bracket follow (CONTEXT.txt).',
    ('G-S25', 'B7 short landing'): 'The linter sees the draft alone. In the article it isn\'t the paragraph\'s end: the recording line and the stop lines follow (CONTEXT.txt).',
    ('G-S26', 'B7 short landing'): 'The linter sees the draft alone. In the article it is the last request inside the quotation, which closes and goes on "etc."; a request to the subconscious, not a summing-up line.',
    ('G-S28', 'B7 short landing'): 'It is the whole paragraph, as the old question was: the troubleshooting item opens by asking whether a smaller try is possible, and the next paragraph gives the smaller asks.',
    ('G-S31', 'B7 short landing'): 'The linter sees the draft alone. In the article it isn\'t the paragraph\'s end: his "“Tell me what you remember, I’m listening.” works well here." follows (CONTEXT.txt).',
    ('G-S33', 'B7 short landing'): 'It is the whole paragraph, a lead-in ending on a colon, as the old line was; the script follows in the next paragraphs.',
    ('G-S34', 'B7 short landing'): 'The linter sees the draft alone. In the article it is the script\'s first line, and its questions follow in the same paragraph (CONTEXT.txt).',
    ('G-S36', 'B7 short landing'): 'The linter sees the draft alone. In the article it isn\'t the paragraph\'s end: his "What does accountability require?" and the last question follow (CONTEXT.txt).',
    ('G-S25', 'E23 paragraph of instructions'): 'The paragraph prepares the session in steps, as the paragraph it replaces did and as his published one does ("Decide what kind of encouragement is welcome ... Preview eye closure, any repeated exit and re-entry, and the return."); the change rewords the steps, it adds none.',
    ('G-S25', 'O29 a run of three or more questions'): 'The three preview questions are his published preview ("Preview eye closure, any repeated exit and re-entry, and the return") as questions the reader asks himself, as in the paragraph it replaces; the text doesn\'t answer them, the reader does.',
    ('G-S36', 'O29 a run of three or more questions'): 'His published forgiveness questions are a run of questions ("What happened?" "What was the impact?" "What boundaries are still needed?" ...); the change merges his "theirs" and "mine" into one question in place.',
    ('G-S25', 'R1 action "it"'): '"it" is the induction, the subject of the section ("Before you begin") and of the paragraphs before; the paragraph it replaces opened the same way ("Deciding to do it.").',
    ('G-S27', 'O45 a safety line'): 'It is the paragraph\'s own closing caution, which he approved in batch 470 ("So, treat it like an image and get some help outside of yourself!"), reworded in place; no safety line is added or repeated.',
    ('G-S29', 'O25 "even" or "actually"'): 'Emulate\'s "even just" marks the smallest of the asks, which is the item\'s point (his published "Start smaller:"); it is the draft\'s only one.',
}
YOU = 'The guide speaks to the reader as "you" throughout; %s'
YOU_BY = {
    'G-S20': 'here "you" is the reader whose own preferences are to come up, in a paragraph that describes a step, not a run of coaching lines.',
    'G-S21': 'here one "you" gives the step of coming back the way you went, one sentence in a paragraph about the trance\'s world.',
    'G-S22': 'here "you" is the person writing the script and going into the trance, in the paragraph\'s two steps.',
    'G-S23': 'here the two questions are the reader\'s preparation, asked of himself, as the paragraph it replaces asked them.',
    'G-S24': 'here one "you" in one safety step, as the sentence it replaces had.',
    'G-S25': 'here the "you"s are the reader preparing his own session, as in the paragraph it replaces.',
    'G-S28': 'here one "you" in the one question of the paragraph.',
    'G-S30': 'here one "you" in the question the troubleshooting item opens with, as the sentence it replaces had.',
    'G-S31': 'here "you" is the reader who may have fooled himself, one sentence in a paragraph of lines to say to the part.',
    'G-S33': 'here one "you" in the lead-in to the script.',
}
SAID = {
    'G-S11': {'T07': (A, '"some of the stuff" is Emulate\'s casual register for "the daily and weekly sections", not a staged hesitation')},
    'G-S12': {'C02': (A, '"It" is the table of contents of the sentence before ("Substack kinda hides the table of contents ..."); "it\'s a long one" is this guide')},
    'G-S14': {'C02': (A, '"their conscious mind" is the people\'s of the same sentence; "this" in his sentence after it is that influence'),
              'C04': (A, 'the FTC report and what it describes are his published line ("The FTC’s report on dark patterns describes designs that trick or manipulate consumers")')},
    'G-S15': {'T12': (A, 'the four kinds of agreement are his published four, not a list made for balance'),
              'C02': (A, '"their minds" and "their adult self" are the people of the question')},
    'G-S16': {'T17': (A, 'it states the consequence of the four "Without ..." lines before it, his published "Let the modes correct each other"; not a free-standing aphorism'),
              'T20': (A, 'it closes the paragraph as the approved sentence did, with the same point; it isn\'t polished into a quotable line'),
              'C02': (A, '"each" is the modes of the lines before it (love and analysis, intuitive signals and testing)')},
    'G-S17': {'T20': (A, 'the approved line, "And it’s got to lead somewhere!", without its "And"'),
              'T28': (A, 'it ends the section as the approved line did; it adds no lesson the approved line didn\'t have'),
              'C02': (A, '"It" is the state the section is about, as in the approved line')},
    'G-S18': {'T01': (A, 'his own first person from his published paragraph ("I was sober and didn’t feel especially suggestible")'),
              'C02': (A, '"when I did that" is "the very little I managed to do with a professional hypnotist", the sentence before'),
              'C03': (A, 'that he was sober and didn\'t feel suggestible at the session is his published fact; "One reason might have been" keeps his "Maybe part of that"')},
    'G-S19': {'T01': (A, 'his own first person from his published line ("I can catch the body’s no ...")'),
              'C02': (A, '"it" is the body\'s no, the start of the same sentence')},
    'G-S20': {'T06': (A, '"bubble up to the surface" is the approved image the sentence already had')},
    'G-S22': {'T08': (A, '"at that point" places his image (soup) in the induction; nothing explains the image'),
              'T20': (A, 'it closes the paragraph as the approved "It\'s all just soup." did'),
              'C02': (A, '"it" is the script you\'re writing, from the paragraph before; "that point" is the induction of the sentence before')},
    'G-S24': {'C02': (A, '"this" is the induction the section prepares, as in the sentence it replaces')},
    'G-S25': {'T12': (A, '"spacious" and "warm and held" are the approved paragraph\'s two ways to coax yourself, with "etc." for its "Something else?"'),
              'C02': (A, '"it" and "this" are the induction, the section\'s subject')},
    'G-S26': {'T01': (A, '"I" is the reader speaking to the subconscious in the quoted request, as in the line it replaces')},
    'G-S27': {'C02': (A, '"it" is the hypnotic imagery of the paragraph\'s first sentence, as in the approved paragraph')},
    'G-S28': {'T24': (A, 'the question is the suggestion itself (try smaller); the next paragraph gives the smaller asks, so nothing is set up to be answered'),
              'C02': (A, '"this" is the practice that "Nothing happens" in, the heading just before, as in the old sentence')},
    'G-S29': {'T07': (A, 'Emulate\'s "just" marks how small each ask is, the item\'s point (his published "Start smaller:")'),
              'T12': (A, 'his own three asks, the third now its own sentence; not a list made for symmetry')},
    'G-S30': {'C02': (A, '"it" is the practice that feels fake, the heading just before, as in the old sentence')},
    'G-S31': {'C02': (A, '"that part" is the part asked "What are you protecting me from?" in the sentences before, as in his sentence')},
    'G-S34': {'T01': (A, '"I" is the reader saying the script to himself, as in the questions it replaces ("Where are my body parts?")')},
    'G-S36': {'T12': (A, 'his published pair, "What belongs to them?" "What belongs to me?", as one question; not a pair made for balance'),
              'C02': (A, '"theirs" is the other person(s) of the question two before')},
}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def reason(name, label):
    for (n, k), v in LINT_BY.items():
        if n == name and label.startswith(k):
            return v
    if label.startswith('D9'):
        return ('It is Emulate\'s rewrite of the words it replaces (SOURCE.txt), so it follows their points in order by design; '
                'the turns are Emulate\'s own (%s).' % TURNS[name])
    if label.startswith('E36/E41'):
        return YOU % YOU_BY[name]
    raise SystemExit('%s: no reason for %s' % (name, label))


def main(names):
    inputs = json.loads((HERE / 'GATE-INPUTS.json').read_text(encoding='utf-8'))
    for name in names or list(inputs):
        d = pathlib.Path(inputs[name]['folder'])
        m = json.loads((d / 'ADMISSION.json').read_text(encoding='utf-8'))
        assert m['candidate_sha256'] == sha(d / 'DRAFT.txt') and m['context_sha256'] == sha(d / 'CONTEXT.txt'), name
        draft = (d / 'DRAFT.txt').read_text(encoding='utf-8')
        m['writer'] = ME
        m['tell_ledger'] = prev.rows(draft, SAID.get(name, {}))
        # T14's and T15's stock lines (from the gate where each draft put his words back) say the draft "puts back" his point;
        # here most drafts are Emulate's own wording (a reviewer of group d caught it), so they say what these drafts do
        q0 = '"%s"' % (draft if len(draft) < 90 else draft[:87] + '...')
        for r in m['tell_ledger']:
            if r['id'] == 'T14' and 'T14' not in SAID.get(name, {}):
                r['evidence'] = ('no material moved to dodge a detector: %s takes the place of the flagged words in the same '
                                 'paragraph, in their order' % q0)
            if r['id'] == 'T15' and 'T15' not in SAID.get(name, {}):
                r['evidence'] = ('%s is Emulate\'s own wording for the flagged words, not less likely words swapped into the old '
                                 'sentence while its other tells stay; where Emulate shifted his sense, his words are back '
                                 '(the_change says where)' % q0)
        # T28's stock line says the draft is not the end of its section; where it is (the section's last paragraph holds it),
        # say so (a reviewer of group f caught the stock line on G-S27 and G-S29)
        last = (d / 'CONTEXT.txt').read_text(encoding='utf-8').strip().split('\n\n')[-1]
        if draft in last and 'T28' not in SAID.get(name, {}):
            q = '"%s"' % (draft if len(draft) < 90 else draft[:87] + '...')
            for r in m['tell_ledger']:
                if r['id'] == 'T28':
                    r['evidence'] = ('%s is in the section\'s last paragraph, where the words it replaces were; it adds no lesson '
                                     'or uplift they didn\'t have' % q)
        for f in m['lint']['findings']:
            f['disposition'] = 'JUSTIFIED_KEEP'
            f['reason'] = reason(name, f['label'])
        m['review_files'] = dict(REVIEWS)
        m['status'] = 'READY_FOR_CHECK'
        (d / 'ADMISSION.json').write_text(json.dumps(m, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print('%-6s ledger %d rows, lint %s' % (name, len(m['tell_ledger']), [f['label'][:24] for f in m['lint']['findings']]))


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
