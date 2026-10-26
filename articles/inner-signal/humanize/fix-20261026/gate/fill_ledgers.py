#!/usr/bin/env python3
"""The writer's half of each gate manifest (docs/HUMANIZATION-OWNER-DELIVERY-GATE.md): who wrote it, a literal judgment on
every inventory row (docs/HUMANIZATION-TELL-INVENTORY.md, T01 to T29 and C01 to C04; the row wording is the Emulate check
gate's, ../../fix-20261025/emulate-check/gate/fill_ledgers.py), a reason for each linter REVIEW finding, and where the
three reviewers' reports go. Run after make_gate_files.py; it refuses a manifest whose hashes don't match its files.

  python3 articles/inner-signal/humanize/fix-20261026/gate/fill_ledgers.py [NAME ...]
"""
import hashlib
import importlib.util
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location('fill_prev', HERE.parents[1] / 'fix-20261025' / 'emulate-check' / 'gate' / 'fill_ledgers.py')
prev = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(prev)

ME = {'name': 'Claude Opus 5.5, the hypnosis guide lane\'s writer (the splices and their fixes; the words are Emulate\'s)',
      'context_id': 'session_01Mxpoi6tFT3FgKmBvtGjRtS'}
REVIEWS = dict(prev.REVIEWS)
A = 'ABSENT'
LINT = {
    'B1 finished principle': 'The sentence is his own caveat about his method, from his published line ("without claiming that the complete sequence has been validated as one treatment"): a disclaimer, not a closing aphorism.',
    'D9 follows the source order': 'It is Emulate\'s rewrite of the passage it replaces, so it follows that passage\'s points in order by design, with Emulate\'s own asides and turns ("if I can put it that way", "of course", "just", "!").',
    'E36/E41 heavy second person': 'The guide speaks to the reader as "you" throughout; these lines give the reader one step or one check inside a paragraph that is not a run of coaching lines.',
    'B7 short landing at paragraph end': 'The linter sees the draft alone. In the article the short line is either not the paragraph\'s end (the stop lines go on after "quiet") or is the fallback\'s own point ("Don\'t fake it.", his inner child guide\'s "no faking required"), not a summing-up line.',
    'O30 a phrase said three or more times': '"you say" names each word the reader can say, one per sentence: \'stop\', \'less\', \'quiet\', as his published "“Stop” ends the exercise; “less” reduces the demand; “quiet” stops the words." The repeat is the instruction.',
    'B4/E15 list or packed sentence': 'Emulate\'s run-on of his two sentences: two steps joined by "and if", the casual join that is the human register here; nothing is listed.',
    'O14 two repeated': 'His three outcomes (clearer, steadier, less hooked) asked as a spoken question to the reader; the "and ... and" is the question\'s spoken register, not a written list.',
}
# A reason for one NAME's finding, where the label's general reason above doesn't describe that draft.
LINT_BY = {
    ('G-S5', 'D9 follows the source order'): 'It is Emulate\'s rewrite of the line it replaces, so it follows that line\'s points in order by design (no warmth today, hands there, notice, no faking); the turns are Emulate\'s ("If you can\'t do this in a loving way today", "just", "see what you feel"), the last three words his.',
    ('G-S5', 'E36/E41 heavy second person'): 'The "you"s are the reader doing the practice the paragraph gives ("If you can\'t do this", "your hands", "what you feel"): one fallback step inside the practice, not a run of coaching lines.',
    ('G-S7', 'B2 contrast'): 'The contrast is his own joke from his inner child guide ("one grown-up doing three jobs, not three more people moving in to help with the rent"), as Emulate put it; it is the point of the sentence, not a framing device.',
    ('G-S7', 'B7 short landing at paragraph end'): 'The linter sees the draft alone. In the article it is not the paragraph\'s end (his "It’s you that needs to develop these qualities." follows), and its words are his own, from his inner child guide: "each job keeps the others in balance".',
    ('G-S7', 'D9 follows the source order'): 'It is Emulate\'s rewrite of his sentence, so it follows his points in order by design (one person, three jobs, not three more people for the rent, the balance); the turns are Emulate\'s own ("rather than getting", "move in with you", "!").',
    ('G-S8', 'D9 follows the source order'): 'It is Emulate\'s rewrite of the two sentences it replaces, so it follows their points in order by design; the turns are Emulate\'s own ("what/where it is", "make sure to", "of course", "it may be").',
    ('G-S8', 'B4/E15 list or packed sentence'): 'The possibilities are the card he approved (IC-A14): the inner child, the parent script, something from earlier in the day, or a bit of each. They have different shapes (the child with why it is mad, "it may be" for the script) and end on his catch-all.',
    ('G-S8', 'E125 list of three'): 'The linter\'s own exception: the list ends on a casual catch-all, his "or a bit of each" from IC-A14, the card he approved (so a REVIEW, not a FAIL); the possibilities are that card\'s meaning, the things the reaction may be.',
    ('G-S9', 'D9 follows the source order'): 'It is Emulate\'s rewrite (samples cj and ck) of the two sentences it replaces, so it follows their points in order by design; the turns are Emulate\'s own ("is made up of a collection of", "take the form of", "consciously build").',
    ('G-S9', 'E36/E41 heavy second person'): 'The "you"s are the reader\'s own history and the inner adult the reader builds ("rules ... that you adopted as a child", "how you were treated", "that you consciously build"): it says what the parent script is; it does not coach.',
    ('G-S10', 'D9 follows the source order'): 'It is Emulate\'s rewrite of the sentence it replaces, so it follows its points in order by design; the turns are Emulate\'s own ("Borrow some from someone else if you need to", "make sure they\'re stable", "direct your trip").',
    ('G-S10', 'E36/E41 heavy second person'): 'Two "you"s in one caution ("if you need to", "your trip"), inside a paragraph of cautions, not a run of coaching lines.',
}
SAID = {
    'G-S2': {'T01': (A, '"I came up with the idea" and "I’m not claiming" are his first person about his own method, from his published "author-developed bridge" and "without claiming"'),
             'C03': (A, 'that he developed the bridge and doesn\'t claim it as a proven treatment are both his published words'),
             'T17': (A, 'the second sentence is his caveat about the method, not a compressed thesis')},
    'G-S3a': {'C02': (A, '"the later \'Already open? Contain before you deepen\' section" names the section by its heading; "yourself" is the reader')},
    'G-S3b': {'T12': (A, 'the three words to say are his three ("stop", "less", "quiet"), each with what it does, not a symmetry built for balance')},
    'G-S4': {'C02': (A, '"It" is the answer\'s instruction, from the sentence before: "If it tells you to do something, I\'d only do it if it\'s loving and leaves you free."')},
    'G-S5': {'C02': (A, '"this" is saying the words to the little one "in a loving way"; "there" is the heart and solar plexus, both named before'),
             'T22': (A, 'it gives the fallback for a day without warmth, and its last words are his own release from his inner child guide ("no faking required"), not reassurance alone')},
    'G-S6': {'T12': (A, 'the three outcomes are his published three, "clearer, steadier, and less hooked"'),
             'C02': (A, '"this way of responding" is the response of the paragraphs before it: warmth or arm\'s length, the Nurturer, stopping')},
    'G-S7': {'C01': (A, 'the inner child isn\'t named in it, and "the kid" appears nowhere in it'),
             'T12': (A, 'one person against three people is his own joke from his inner child guide ("not three more people moving in to help with the rent")')},
    'G-S8': {'C01': (A, 'the inner child is "your inner child" in it; "the kid" appears nowhere in it'),
             'C02': (A, '"it" is the reaction of the paragraph\'s first sentences (numbness, cynicism, urges); "it" is the same in the next sentence')},
    'G-S9': {'C01': (A, 'the draft names the parent script and the inner adult; the inner child isn\'t named in it, and "the kid" appears nowhere in it'),
             'C02': (A, '"Your parent script" picks up "your inherited parent script" of the sentence before; "It" and "This" are that script')},
    'G-S10': {'C02': (A, '"some" is the Nurturer and Protector of the sentence before ("enough Nurturer and Protector in the room"); "they" is the someone else')},
}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main(names):
    inputs = json.loads((HERE / 'GATE-INPUTS.json').read_text(encoding='utf-8'))
    for name in names or list(inputs):
        d = pathlib.Path(inputs[name]['folder'])
        m = json.loads((d / 'ADMISSION.json').read_text(encoding='utf-8'))
        assert m['candidate_sha256'] == sha(d / 'DRAFT.txt') and m['context_sha256'] == sha(d / 'CONTEXT.txt'), name
        draft = (d / 'DRAFT.txt').read_text(encoding='utf-8')
        m['writer'] = ME
        m['tell_ledger'] = prev.rows(draft, SAID.get(name, {}))
        for f in m['lint']['findings']:
            by = next((v for (n, k), v in LINT_BY.items() if n == name and f['label'].startswith(k)), None)
            f['disposition'] = 'JUSTIFIED_KEEP'
            f['reason'] = by or LINT[next(k for k in LINT if f['label'].startswith(k))]
        m['review_files'] = dict(REVIEWS)
        m['status'] = 'READY_FOR_CHECK'
        (d / 'ADMISSION.json').write_text(json.dumps(m, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print('%-6s ledger %d rows, lint %s' % (name, len(m['tell_ledger']), [f['label'][:30] for f in m['lint']['findings']]))


if __name__ == '__main__':
    main(sys.argv[1:])
