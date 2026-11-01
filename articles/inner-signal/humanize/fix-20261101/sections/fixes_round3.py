"""Round 3 of batch s1101's fixes (2026-11-01, after the recheck r1101): the six sections that still read AI or Human
(Low) by themselves on their second and last section check (recheck/RESULTS.md), each with the cause named first
(the budget rule: a new try only with a diagnosis). The section checks are spent, so these are checked paragraph by
paragraph (recheck/para/, scope paragraph or pair, try 1 of 6 per lineage), and then in the whole guide.

The round-2 (or round-1) text that was checked stays in each entry as "checked_r1101", with what Pangram read.

  python3 articles/inner-signal/humanize/fix-20261101/sections/fixes_round3.py
Rewrites the named fixes in FIXES-S1101.json; then apply_s1101_fixes.py rebuilds the guide from a32e6afe.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

# entry id -> (the start of the old text of the pair to change, the old text it should have (None: unchanged),
#              the new text, what Pangram read on 1 November in r1101, the diagnosis)
R3 = [
    ('s1101-17 w1', 'You can choose to let the parts of you', None,
     'Let the parts of you that feel younger have their say. You’re still the one making the adult decisions, though, '
     'and you’re not trying to become a little kid again.',
     'AI Generated (1.0): one AI (High) window over the whole section, 230 words; it read AI Detected (0.23) before '
     'round 1',
     'Round 1 built all three paragraphs from paired negations and lists ("You don’t hand ..., and you don’t try ...", '
     '"No younger part of me, no guide, no recording and no other person", and two lists in a row in the last '
     'paragraph, which also repeated the good things of being young the first paragraph lists). Fewer pairs, and the '
     'last paragraph says only what the first one doesn’t: what you leave behind.'),
    ('s1101-17 w3', 'I am not going to replace my adult judgment', None,
     'I\'m not handing my adult decisions over to a younger part of me, or to a guide or a recording, or to anyone else.',
     'in the same AI (High) window', 'as above'),
    ('s1101-17 w4', 'This way you get the benefits of being young', None,
     'That way you keep the good parts of feeling younger and leave behind what came with really being a kid: having to obey, '
     'not being able to do much for yourself, getting scolded, and not knowing better yet.',
     'in the same AI (High) window', 'as above'),
    ('s1101-42 w5', 'It just might mean that something is listening.',
     'Even if something happens, it doesn’t mean that what comes next will be true. It just might mean that something '
     'is listening.',
     'Even if something happens, it doesn’t mean that what comes next will be true, only that some part of you might be '
     'listening.',
     'Human Written; the closing sentence Human (Low), 12 words, as before',
     'A short closing sentence on its own reads Low however it is worded; joined to the sentence it qualifies, as the '
     'published "None proves truth; at most, something may be listening" is one sentence.'),
    ('s1101-44 w4-6', 'Take mental note of only what actually came up', None,
     'Make a mental note of just what actually came up and anything you need to do about it, then go and do something '
     'normal, like eating or washing up.',
     'Human (Low), 11 words, on "Then go and do something normal, like eating or washing up."',
     'The short last sentence again; joined to the one before.'),
    ('s1101-44 w4-6', 'If your recording cuts out for some reason', None,
     'If your recording cuts out partway through, you could end up lying there waiting for a voice that isn\'t coming '
     'back. So tell yourself, "The recording has stopped and the session is over," and do the count and the checks '
     'above on your own. Once your eyes are open, press your feet or hands into something solid too.',
     'AI (High), 134 words over this paragraph and the next, as on 1 November (126 words)',
     'Both versions were rules in the published order: an instruction, then a list of what a recording mustn’t do. '
     'Each paragraph now says why: what happens if you wait for the missing voice, and what being left in a role or '
     'blank means once you get up.'),
    ('s1101-44 w4-6', 'Note: If you are going to sleep to a recording', None,
     'Sleep recordings are different, since drifting off at the end of one, or just resting, is what they\'re for. A '
     'recording that\'s meant to wake you back up has to finish the job, though. If it leaves you still in a role, with '
     'your judgment or your body slowed down, or blank, you\'d be walking around half under. The same goes for a vague '
     'reset word, or a state it never ends.',
     'in the same AI (High) window', 'as above'),
    ('s1101-53 w1-2', 'It’s good to give this more time once or twice a week', None,
     'Once or twice a week, when it’s useful, give this practice more time, so there’s room to follow whatever shows '
     'up. It doesn’t need to be more intense than usual. Start from your Higher Self, or from simply '
     'noticing what’s there if that’s out of reach. If you need the Protector or another of your adult jobs, bring it '
     'in or borrow it from someone safe, and check you’re not skipping past anything important. Leave enough time at '
     'the end to come all the way back out.',
     'AI Generated (1.0): AI (Medium, High, Medium, High) over the whole section; it read AI Detected (0.65) before',
     'Round 2 cut the repeated "it’s good to" into short commands and short statements ("More time doesn’t have to '
     'mean more intense.", "Then follow whatever shows up."), each read AI on its own. The paragraph now starts from '
     'what the extra time is for, and the steps run together as one person would say them.'),
    ('s1101-53 w1-2', 'If possible, it’s good to do the normal thing immediately', None,
     'Then, if you can, do the normal thing that came up right away. Your subconscious gets to see that the adult in '
     'you heard it and did something, and it doesn’t just become one more beautiful inner meeting with the dishes still '
     'in the sink.',
     'in the same AI window (High, 98 words with the end of the paragraph before)', 'as above'),
    ('s1101-59 w1', 'Bring it down to something specific.', None,
     'If the bliss spreads out into a big warm haze, it can’t do much for you or anyone else yet. Bring it down to one '
     'next step by asking, “What’s the next small thing this love is asking me to do? A task, a boundary, a meal, some '
     'rest, a repair, a conversation?”',
     'AI (High), 50 words over the heading, this paragraph, the next heading and his "Don’t pry." (AI Medium on 1 '
     'November)',
     'A rewrite of the words that kept the shape (the ledger’s explanation of HG1101-59#195): a heading, a one-line '
     'instruction, a quoted question. The paragraph now says what the problem is ("diffuse" in the heading) before '
     'the step, so the window holds more than a heading and an order.'),
    ('s1101-93 w1', 'Presences, shadow forces, or grandiose parts don’t always attack through fear, either.',
     'Presences, shadow forces, or grandiose parts don’t always attack through fear, either. They may also try to give '
     'you a sense',
     'Sometimes a hostile presence, a shadow force or a grandiose part comes at you with flattery instead of fear. It '
     'may try to give you a sense',
     'AI (Low), 19 words: the heading and the first sentence, both times',
     'An opening generalization kept (HG1101-93#197). It now says what happens instead (flattery), in the next '
     'sentence’s terms.'),
]


def main():
    path = HERE / 'FIXES-S1101.json'
    fx = json.loads(path.read_text(encoding='utf-8'))
    byid = {w['id']: w for w in fx['windows']}
    for wid, start, old, new, read, why in R3:
        w = byid[wid]
        pairs = [p for p in w['fix'] if start in p[0]]
        assert len(pairs) == 1, (wid, start, len(pairs))
        p = pairs[0]
        rec = w.setdefault('round3', [])
        if not any(start in r['old'] for r in rec):
            rec.append({'old': p[0], 'checked_r1101': p[1], 'read_r1101': read, 'diagnosis': why})
        r = [r for r in rec if start in r['old']][0]
        if old:
            assert old.startswith(r['old'][:20]) or r['old'] in old, (wid, old[:40])
            p[0] = old
            r['old'] = old
        p[1] = new
    fx['about'] = fx['about'].split(' Round 3:')[0] + (' Round 3: fixes_round3.py (the six sections that still read AI '
                                                        'or Human (Low) on their second and last section check, each '
                                                        'fix with its diagnosis and the text that was checked).')
    path.write_text(json.dumps(fx, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(R3), 'fixes rewritten')


if __name__ == '__main__':
    main()
