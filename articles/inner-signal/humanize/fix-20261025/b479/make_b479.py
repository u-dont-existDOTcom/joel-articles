"""Batch 479: candidates for the red windows of the whole guide's recheck of 2026-10-25 (read after Joel's message of 23:50
UTC: ../recheck/RESULT-A.json and RESULT-B.json, SCORE-A.md and SCORE-B.md), for one more recheck in place.

What each red stretch is (../recheck/RESULT-*.json against the cards of his two marking pages, ../review/REVIEW.json and
../emulate-check/REVIEW-EMULATE.json, and his inner child guide on main, articles/inner-child-therapy/):
- S1, part A, Low: IC-A2's "That's one grown-up doing three jobs, and each job keeps the others in balance.", his inner
  child guide's sentence with its middle cut ("not three more people moving in to help with the rent", his own edit there,
  its OWNER-EDITS.json entry joel-upload-20261019). The candidate is his whole sentence, word for word. No Emulate.
- S2, part A, High: the borrowed adulthood paragraph, Emulate's first sentence and EM-2's plainer words for his
  published second one (mine, through the gate, approved by him).
- S3, part A, five Low windows marked humanized: the safe-place paragraph's pointer to "Already open? Contain before you
  deepen" (RR-4.6), and "Deciding to do it." through the end of the next paragraph's stop lines (TY-6, RR-4.1's quote
  marks and "say"; the last two lines unchanged since recheck A4, where all of it read Human).
- S4, part B, Low and High: the last two sentences of the Core prompts' answer paragraph, his own words in his inner
  child guide (its OWNER-EDITS.json entry sws-p3-p5-joel: "I fixed p3-p5 for you"), put in by IC-B12.
- S5, part B, High (and its neighbours Low and Medium, unchanged since recheck B2): IC-B14's "No warmth today? ..." line
  at the end of the Inner child love paragraph, from his inner child guide's two-hand practice (and also in part A's
  two-hand practice, IC-A10, where it read Human).
- S6, part B, High: his published test ("The useful question is whether ..."), put back by EM-16.
- Not sent: part B's hypnosis audit questions (High), which stay a list by his answer 2c, as in recheck B2.

Emulate went first (E237, E235): three samples of each red paragraph with the one before it where it is short
(BUNDLE.json, make_bundle.py; on the laptop, emu-b479-84d0138afe71 and emu-hg-cg, -ch, -ci; their outputs in cg/, ch/,
ci/). Only the red sentences are spliced from a sample, and each fix to a sample's words is listed with its reason
(meaning put back from his published guide or his inner child guide, the guide's spelling, the heading's own words).

  python3 articles/inner-signal/humanize/fix-20261025/b479/make_b479.py   (from the repo root)
Writes CANDIDATES.json, CANDIDATE-MASTER.md (HUMANIZED-SO-FAR.md with every candidate in, for the recheck),
REVIEW-PROMPT-A1, -A2 and -B.txt (the meaning readers' items, two or three each), TEXTS.json and b479-items.json (the API checks).
"""
import hashlib
import json
import pathlib
import re
import sys

B = pathlib.Path(__file__).resolve().parent
ROOT = B.parents[4]
H = ROOT / 'articles/inner-signal/humanize'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(B.parent / 'review'))
import suggestion_review as sr  # noqa: E402
import apply_answers as AA  # noqa: E402

FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})


def sample(run, key):
    return (B / run / (key + '.out.txt')).read_text(encoding='utf-8')


def cut(text, first, last):
    a = text.index(first)
    z = text.index(last, a) + len(last)
    assert text.count(first) == 1, first
    return text[a:z]


IC_JOBS = 'That’s one grown-up doing three jobs, not three more people moving in to help with the rent, and each job keeps the others in balance.'

# key: the spot. 'where' is the paragraph (sr.where); 'old' the words that go (exactly once in it); 'from' the sample run
# and the first and last words of what comes in (None: his own words in 'new'); 'fixes' (old, new, why) on the sample's
# words; 'published' the meaning to keep; 'api' whether the candidate paragraph is checked alone first (High windows only:
# a Low window in place isn't reproduced by the API, E226, E240, and the recheck in place decides).
SPOTS = {
    'S1': {'part': 'A', 'card': 'IC-A2', 'where': 'The inner child, the guards, and the inner adult’s three jobs, P2',
           'old': 'That’s one grown-up doing three jobs, and each job keeps the others in balance.',
           'from': None, 'new': IC_JOBS,
           'source': 'his inner child guide, The Chicken-and-Egg Problem, word for word (the rent is his own edit, its OWNER-EDITS.json entry joel-upload-20261019)',
           'fixes': [],
           'published': ('I organize that adult capacity into three functions: Nurturer, Protector, and Leader/Guru. They aren’t '
                         'three literal beings. They’re three ways the present-day person reparents the inner child.\n'
                         '(His inner child guide: "' + IC_JOBS + '")'),
           'red': 'Low, 16 words', 'api': False},
    'S2': {'part': 'A', 'card': 'EM-2', 'where': 'When the adult role is not available yet, P2',
           'old': None,  # the whole paragraph
           'from': ('ch', 'HG-A-borrowed', 'So, I came up with the idea', 'has been tried before.'),
           'fixes': [('a number of things that I know work', 'a number of familiar practices',
                      'his published "It combines familiar practices": the practices are familiar ones, not ones he says he knows work'),
                     ('modelling', 'modeling', 'the guide\'s spelling'),
                     ('even though I don’t know if the whole sequence has been tried before',
                      'even though I’m not claiming the whole sequence has been proven as one treatment',
                      'his published "without claiming that the complete sequence has been validated as one treatment": a claim he doesn\'t make, '
                      'not something he doesn\'t know, and proven, not tried (the meaning reader, REVIEW-A1.md: "I don\'t know if" is about his '
                      'knowledge, not about what he claims, and "tested" is a lower bar than "validated")')],
           'left': ['two of his four practices, as in EM-2, which he approved ("a list of four reads as AI"); both meaning readers '
                    'named the other two as lost, and the section carries both as its steps: witnessing is the next paragraph '
                    '("Access your witnessing position"), and the gradual handing over is the apprentice adult hat and its return, '
                    '"noticing what you borrowed and what you were able to do on your own (even if it\'s only 5%)"',
                    '"a temporary fix" for "provisional", and "I came up with the idea of constructing" for "I use" (the reader: minor, '
                    'the same interim sense, author-developed kept)'],
           'published': ('For that starting point, I use a provisional, author-developed bridge I call borrowed adulthood. It '
                         'combines familiar practices—witnessing, modeling, supported action, and gradual transfer of '
                         'responsibility—without claiming that the complete sequence has been validated as one treatment.'),
           'red': 'High, 46 words: the whole paragraph', 'api': True, 'lineage': 'HG-adult-unavailable-P2'},
    'S3a': {'part': 'A', 'card': 'RR-4.6', 'where': 'Before you begin, P3',
            'old': '(The part below called "Already open? Contain before you deepen" can be used to help orient you if you\'re already open, but don\'t use it to make yourself deeper if you\'re not stable.)',
            'from': ('ci', 'HG-A-stop', 'If you are already partally or fully opened', 'if you are not in a safe state.'),
            'fixes': [('partally', 'partially', 'spelling'),
                      ('if you are not in a safe state', 'if you are not stable',
                       'his published "an unstable state", and the guide\'s own "if you\'re not stable" there since recheck A4 (the second '
                       'meaning reader, REVIEW-A3.md: "not in a safe state" is a weaker trigger than "unstable")'),
                      ("the 'Already open? Contain yourself before deepening' section", "the later 'Already open? Contain before you deepen' section",
                       'the heading\'s own words, so the reader can find it (RR-4.6\'s reason), and his published "The later Already open? practice"')],
            'left': ['"partially or fully": Emulate\'s, and true of the section ("Use this when ... has already opened the state")'],
            'note': 'sample ci, not cg: the meaning reader (REVIEW-A2.md) failed cg\'s "don\'t deepen if you can\'t be safe" as narrower than '
                    'his "an unstable state" and its "you can use" for losing "is for orientation"; ci keeps "to help orient yourself" '
                    'and "if you are not in a safe state"',
            'published': ('Choose a physically secure place without driving, water, machinery, or anyone needing your '
                          'supervision. When intoxicated, acutely confused, or unable to keep yourself safe, deal with '
                          'immediate support rather than exploratory hypnosis. The later Already open? practice is for '
                          'orientation, not permission to intensify an unstable state.'),
            'red': 'Low, from its second half into "Deciding to do it."', 'api': False},
    'S3b': {'part': 'A', 'card': 'RR-4.1', 'where': 'Before you begin, P4',
            'old': 'Know that you can say "stop" at any time and the induction will end. If you want to change something, say "less" if you want it to be asking for less from you, or say "quiet" and the talking will stop.',
            'from': ('cg', 'HG-A-stop', 'Remind yourself that if you say', 'the talking will stop.'),
            'fixes': [],
            'left': ['the two sentences after these stay as they are ("You can also just open your eyes and stop, and then come all '
                     'the way back anyway." and "You don\'t need to ask any parts for permission to stop, even if a part tells you that '
                     'you do."): unchanged since recheck A4, where they read Human, and red in the last check only beside RR-4.1\'s two; '
                     'both meaning readers failed sample cg\'s versions of them, as a promise of a full return (REVIEW-A2.md, '
                     'REVIEW-A3.md) and for "permission to do this" (REVIEW-A2.md)'],
            'note': 'round 1 also spliced cg\'s last two sentences; round 2 keeps only the two that RR-4.1 changed',
            'published': ('Decide what kind of encouragement is welcome: spacious listening, warm company, or a firmer '
                          'invitation to stay with a feeling. Preview eye closure, any repeated exit and re-entry, and the '
                          'return. For a recording, read the script beforehand when possible. “Stop” ends the exercise; '
                          '“less” reduces the demand; “quiet” stops the words. You can simply open your eyes and finish. No '
                          'inner part has to approve your decision to stop.'),
            'red': 'four Low windows marked humanized, the last four sentences (these two changed since recheck A4)', 'api': False},
    'S4': {'part': 'B', 'card': 'IC-B12', 'where': 'Core prompts, P8',
           'old': "It should make sense, too. Even then, anything big or hard to undo can wait until you're calm and you've checked it against what you actually know.",
           'from': ('ci', 'HG-B-act', 'It should make sense to you and', 'check it out with what you know.'),
           'fixes': [],
           'published': ('His own words in his inner child guide (Start With Whatever Showed Up): "If it tells you to do '
                         'something, I\'d only do it if it\'s loving and leaves you free. It should make sense, too. Even then, '
                         'anything big or hard to undo can wait until you\'re calm and you\'ve checked it against what you '
                         'actually know."'),
           'red': 'Low (5 words) and High (24 words): these two sentences', 'api': True, 'lineage': 'HG-core-prompts-P8'},
    'S5': {'part': 'B', 'card': 'IC-B14', 'where': 'Inner child love, P1',
           'old': 'No warmth today? Then rest your hands there and notice what you find, no faking required.',
           'from': ('ch', 'HG-B-love', 'If you can’t do this in a loving way today', 'You don’t have to fake it!'),
           'fixes': [],
           'published': ('Published: "Start with the hand-on-heart, hand-on-solar-plexus practice. “Little one, you are not '
                         'alone. You do not have to solve this. I am here now. The adult is listening.” Don’t recite the words '
                         'like an incantation you’re hoping the subconscious will grade. Say them the way you’d speak to a '
                         'frightened child you actually love."\n(His inner child guide\'s two-hand practice, where the added '
                         'line comes from: "No warmth today? Then rest your hands there and notice what you find, no faking '
                         'required.")'),
           'red': 'High (16 words), with the quote and the line before it Low and Medium', 'api': True,
           'lineage': 'HG-inner-child-love-P1'},
    'S6': {'part': 'B', 'card': 'EM-16', 'where': 'A response check, not a verdict about what it is, P4',
           'old': 'The useful question is whether this way of responding helps you become clearer, steadier, and less hooked.',
           'from': ('cg', 'HG-B-test', 'Is it helping you', 'less hooked?'),
           'fixes': [('Is it helping you', 'Is this way of responding helping you',
                      'his published "whether this way of responding helps you": the test is of the response, and "it" would read as the presence')],
           'published': ('Neither response establishes its origin. A protective part needn’t reveal its fear quickly; a '
                         'comforting response doesn’t prove an interpretation either. The useful question is whether this way '
                         'of responding helps you become clearer, steadier, and less hooked. Love and boundaries don’t require '
                         'a verdict first.'),
           'red': 'High, 17 words: this sentence', 'api': True, 'lineage': 'HG-response-check-P4', 'with_before': True},
}


def build():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl)
    by = {sr.where(bl, b['i']): b['i'] for b in bl}
    new_text, cands = {}, {}
    for k, s in SPOTS.items():
        i = by[s['where']]
        t = new_text.get(i, bl[i]['text'])
        old = s['old'] if s['old'] is not None else t
        assert t.count(old) == 1, (k, old[:50])
        done = []
        if s['from']:
            run, key, first, last = s['from']
            new = cut(sample(run, key), first, last)
            raw_new = new
            for a, b, why in s['fixes']:
                assert new.count(a) == 1, (k, a)
                new = new.replace(a, b)
                done.append({'replace': a, 'with': b, 'why': why})
        else:
            new = raw_new = s['new']
        new_text[i] = t.replace(old, new)
        cands[k] = {'part': s['part'], 'card': s['card'], 'where': s['where'], 'block': i, 'red': s['red'],
                    'sample': (s['from'][0] + '/' + s['from'][1]) if s['from'] else None,
                    'source': s.get('source') or 'Emulate sample %s/%s (three samples: cg, ch, ci)' % (s['from'][0], s['from'][1]),
                    'old': old, 'sample_words': raw_new, 'new': new, 'fixes': done, 'published': s['published'],
                    'api': s['api'], 'lineage': s.get('lineage'), 'left': s.get('left', []), 'note': s.get('note')}
    out, lost = list(raw), []
    for i, t in new_text.items():
        out[i] = AA.set_block_text(raw[i], t, lost)
    assert not lost, lost
    master = '\n\n'.join(out) + ('\n' if md.endswith('\n') else '')
    bl2 = sr.blocks(master)
    for k, c in cands.items():
        c['paragraph_after'] = bl2[c['block']]['text']
        assert c['new'] in c['paragraph_after'], k
        prev = c['block'] - 1
        c['paragraph_before'] = bl2[prev]['text'] if bl2[prev]['level'] == 0 else '(the heading "%s")' % bl2[prev]['text']
        nxt = c['block'] + 1
        c['paragraph_next'] = bl2[nxt]['text'] if bl2[nxt]['level'] == 0 else '(the heading "%s")' % bl2[nxt]['text']
    (B / 'CANDIDATE-MASTER.md').write_text(master, encoding='utf-8')
    record = {'guide_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(),
              'candidate_master_sha256': hashlib.sha256(master.encode('utf-8')).hexdigest(), 'spots': cands}
    (B / 'CANDIDATES.json').write_text(json.dumps(record, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return cands


NAMES = {
    'S1': 'the guide\'s section on the inner adult: what the grown-up you build up does, in three jobs',
    'S2': 'the guide\'s section on readers who can\'t reach their adult side yet, and the temporary help it offers',
    'S3a': 'the end of the safety paragraph before an induction (where and when not to do it)',
    'S3b': 'the end of the step before an induction where the reader previews it and learns how to stop it',
    'S4': 'what to do with an answer the reader gets from their own subconscious after asking it a question',
    'S5': 'a short practice in the anxiety appendix: hands on heart and solar plexus, and words to the inner child',
    'S6': 'the end of a section on meeting a hostile presence or part in an altered state: how to tell if your response helps',
}


def prompt(cands, keys, path, out_name):
    items = []
    for n, k in enumerate(keys, 1):
        c = cands[k]
        own = c['sample'] is None
        items.append('## Item %d (%s)\n\n%s\n\nBEFORE:\n%s\n\nPUBLISHED:\n%s\n\nNOW:\n%s\n\nCHANGED WORDS IN NOW:\n%s\n\nAFTER:\n%s\n' % (
            n, NAMES[k], ('(NOW puts back the author\'s own sentence from his other guide; check sense only, and say if '
                          'anything in it repeats the paragraph or reads oddly here.)' if own else ''),
            c['paragraph_before'], c['published'], c['paragraph_after'], c['new'], c['paragraph_next']))
    head = (
        "You check %d rewritten passages of Joel's long self-hypnosis guide (how to learn self-hypnosis safely, with inner "
        "child and parts work, and many safety cautions). The guide is self-guided: the reader leads themselves, so \"you\" "
        "is the reader. In each NOW paragraph only the CHANGED WORDS are new (a detector-passing rewrite or the author's own "
        "words); the rest of NOW read human already and stays. PUBLISHED is the meaning to keep: the author's own published "
        "guide, or his own words in his other guide where it says so. Safety cautions and steps matter most.\n\n"
        "For each item, say in a few words each:\n"
        "1. MEANING: do the CHANGED WORDS keep every point, step, caution and claim of PUBLISHED that they replace, with the "
        "same strength (nothing made more or less certain or more optional, no instruction turned into a suggestion, no "
        "safety caution weakened, no step lost)? KEPT, or what CHANGED or was LOST, and anything ADDED that a reader would "
        "take as a claim.\n"
        "2. SENSE: would a reader understand NOW in its place, between BEFORE and AFTER? OK, or the words that stop them "
        "and why.\n"
        "End each item with one line, `VERDICT: OK` or `VERDICT: CHANGED`. Judge meaning and sense only, not style or "
        "grammar (the casual grammar, run-on sentences and comma splices are on purpose), and suggest the smallest "
        "possible rewrite only for a problem you report.\n\n"
        "Write your report with a single Write call to `%s`, one \"## Item N\" part per item, then reply with only the "
        "verdicts, one line per item. Don't read any other file, don't run commands, and don't use the web.\n\n" % (
            len(keys), B / out_name))
    path.write_text(head + '\n'.join(items), encoding='utf-8')


def api_texts(cands):
    texts = {}
    for k, c in cands.items():
        if not c['api']:
            continue
        t = c['paragraph_after']
        name = 'b479-%s-p' % k
        if SPOTS[k].get('with_before'):
            t = c['paragraph_before'] + '\n\n' + t
            name = 'b479-%s-p+prev' % k
        texts[name] = t
    (B / 'TEXTS.json').write_text(json.dumps(texts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    items = [[n, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for n, t in texts.items()]
    (B / 'b479-items.json').write_text(json.dumps(items, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return texts


if __name__ == '__main__':
    cands = build()
    # two or three items a reader (E270). Round 1 read the candidates as first spliced; round 2 (A3) reads the three that
    # changed after round 1's reports (S2's caution, S3a from another sample, S3b's "stop"). A prompt a reader has read is
    # never rewritten.
    for keys, name, report in ((['S1', 'S2'], 'REVIEW-PROMPT-A1.txt', 'REVIEW-A1.md'),
                               (['S3a', 'S3b'], 'REVIEW-PROMPT-A2.txt', 'REVIEW-A2.md'),
                               (['S4', 'S5', 'S6'], 'REVIEW-PROMPT-B.txt', 'REVIEW-B.md'),
                               (['S2', 'S3a', 'S3b'], 'REVIEW-PROMPT-A3.txt', 'REVIEW-A3.md')):
        if not (B / name).exists():
            prompt(cands, keys, B / name, report)
    texts = api_texts(cands)
    for k, c in cands.items():
        print(k, c['card'], '|', c['new'][:110])
    print('API texts:', {n: len(t.split()) for n, t in texts.items()})
