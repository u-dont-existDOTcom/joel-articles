"""The hypnosis guide's cards of 1 November (2): the windows of batch s1101 that read AI or Human (Low) in his own words
(REVIEW-S1101.json, .html, .artifact.html, .md).

Gate E306 (Joel, 2026-11-01 18:57 UTC): every window that reads AI or Human (Low) gets fixed, with its meaning read
again ("often smoothed over and vague"); our words are fixed in place (../FIXES-S1101.json), and his words come to him
here, in the marking page's form (tools/humanization/suggestion_review.py, gate E265): his versions and rewrites, the
lines of his inner child guide that this guide uses (whole or shortened), and the two lines of his inner child guide
that the first round of fixes changed without a card (G-23, now back as he wrote them). Each card says what Pangram read
there, what the suggestion does, and my advice; three of them are stretches I'd keep as they are ("edit" cards: Keep it
as it is, or Edit it).

  python3 articles/inner-signal/humanize/fix-20261101/sections/review/build_page_s1101.py
"""
import collections
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
D = HERE.parent
H = D.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/'
LANE = 'articles/inner-signal/humanize/'
ARTICLE = LANE + 'HUMANIZED-SO-FAR.md'
GIT_FILE = LANE + 'fix-20261101/sections/review/REVIEW-S1101.html'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
BL = sr.blocks(MD)
CONF = json.loads((D / 'CONFIDENCE.json').read_text(encoding='utf-8'))
FOUND = 'Batch s1101: each section checked by itself in Pangram (1 November)'

TYPES = {
    'yours': {'label': 'Your own words',
              'about': 'A paragraph you wrote or rewrote, where Pangram read AI or Human (Low). Approve uses the '
                       'suggestion; Reject keeps your words; Revise lets you write your own.'},
    'stuck': {'label': 'Our words, still AI',
              'about': 'Words of ours (Emulate\'s or mine) that read AI in all three tries, each said plainly from your '
                       'published version. Keep it as it is (a clear version stays in), or Edit it: your own versions '
                       'have read Human.'},
    'icguide': {'label': 'From your inner child guide',
                'about': 'Your inner child guide\'s words in this guide, whole or shortened, where Pangram read AI or '
                         'Human (Low). Approve uses the suggestion; Reject keeps them; Revise lets you write your own.'},
}


def block_with(s, level=None):
    hits = [b['i'] for b in BL if s in b['text'] and (level is None or b['level'] == level)]
    assert len(hits) == 1, (s[:60], hits)
    return hits[0]


def reading(blocks):
    """What Pangram read on these blocks in batch s1101: each window to fix that touches them."""
    out = []
    for w in CONF['fix']:
        if set(w['blocks']) & set(blocks):
            lab = 'Human' if w['label'] == 'Human' else 'AI'
            out.append('%s (%s), %d words' % (lab, w['confidence'], w['words']))
    return '; '.join(out)


def win_blocks(*keys):
    """The guide's blocks of these windows (CONFIDENCE.json's numbering is the guide's at a32e6afe; the fixes since
    change no paragraph count, which build() checks)."""
    out = set()
    for k, n in keys:
        out |= {b for w in CONF['fix'] if w['key'] == k and w['window'] == n for b in w['blocks']}
    return out


def card(cid, typ, title, changes, what, why, stays, deciding, note, label=None, read=None):
    """changes: [(block, old, new)]; old is the words to highlight, new what they become ("" cuts them; old == the
    whole block and new == "" cuts the block)."""
    spans, edits = [], {}
    for i, old, new in changes:
        t = edits.get(i, {}).get('after') if i in edits else BL[i]['text']
        assert BL[i]['text'].count(old) == 1, (cid, old[:60])
        k = BL[i]['text'].find(old)
        spans.append({'block': i, 'start': k, 'end': k + len(old.rstrip())})
        after = t.replace(old, new) if old != BL[i]['text'] or new else ''
        edits[i] = {'block': i, 'before': BL[i]['text'], 'after': after.strip() if after else ''}
    s = {'id': cid, 'type': typ, 'title': title, 'where': sr.where(BL, changes[0][0]), 'spans': spans,
         'edits': [edits[i] for i in sorted(edits)], 'inserts': [], 'moves': [], 'what': what, 'why': why,
         'stays': stays, 'advice': 'approve', 'advice_note': note, 'found_by': FOUND, 'deciding': deciding}
    if read:
        s['reading'] = read
    if label:
        s['approve_label'] = label
    return s


def edit_card(cid, typ, title, block, old, why, note, read):
    t = BL[block]['text']
    assert t.count(old) == 1, (cid, old[:60])
    k = t.find(old)
    return {'id': cid, 'type': typ, 'title': title, 'where': sr.where(BL, block), 'advice': 'edit', 'why': why,
            'reading': read, 'advice_note': note, 'keep_label': 'keep it as it is', 'found_by': FOUND,
            'spans': [{'block': block, 'start': k, 'end': k + len(old)}]}


DECIDE = 'Approve uses the suggestion; Reject keeps your words; Revise lets you write your own.'


def build_cards():
    S = []
    # W-92: his inner child guide's line, shortened when it came into this guide
    i = block_with('That’s one grown-up doing three jobs, and each job keeps the others in balance.')
    S.append(card('W-92', 'icguide', '“That’s one grown-up doing three jobs …”',
                  [(i, 'That’s one grown-up doing three jobs, and each job keeps the others in balance.',
                    'That’s one grown-up doing three jobs, not three more people moving in to help with the rent, and '
                    'each job keeps the others in balance.')],
                  'Your inner child guide’s whole line, with “not three more people moving in to help with the rent” '
                  'back in.',
                  'The line is from your inner child guide, shortened when it came into this guide, and the cut took '
                  'out the part that says what your published version says here: “They aren’t three literal beings. '
                  'They’re three ways the present-day person reparents the inner child.” Without it, “one grown-up '
                  'doing three jobs” reads like a slogan.',
                  'The rest of the paragraph word for word.', DECIDE,
                  'I’d approve: it’s your own line in full, and it says the point your published version makes.',
                  'use your whole line', reading(win_blocks(('s1101-15', 2)))))
    # W-111: his inner child guide's last line in Love doesn't have to wait for trust
    i = block_with('That takes warmth, and if there isn\'t any yet, borrow some.')
    S.append(card('W-111', 'icguide', '“That takes warmth, and if there isn’t any yet, borrow some.”',
                  [(i, 'That takes warmth, and if there isn\'t any yet, borrow some.',
                    'Even that takes some warmth, and if you don\'t have any yet, borrow some from someone who\'s been '
                    'good to you, or from an adult you imagine.')],
                  '“That takes warmth, and if there isn’t any yet, borrow some.” becomes “Even that takes some warmth, '
                  'and if you don’t have any yet, borrow some from someone who’s been good to you, or from an adult '
                  'you imagine.”',
                  '“That” didn’t say what takes warmth (just not hitting back, the sentence before), and “borrow some” '
                  'didn’t say from where. Your published version says where: “Use a remembered person when that helps, '
                  'or an imagined adult whose intention is to take good care of you.”',
                  'The paragraph before it word for word.', DECIDE,
                  'I’d approve: same point, and a reader knows where to borrow from.', None,
                  reading(win_blocks(('s1101-18', 4)))))
    # W-119: his inner child guide's two lines in the two-hand practice
    i = block_with('No warmth today? Then rest your hands there and notice what you find, no faking required.')
    S.append(card('W-119', 'icguide', '“No warmth today? …”',
                  [(i, 'No warmth today? Then rest your hands there and notice what you find, no faking required.',
                    'If you can\'t find any warmth today, just leave your hands where they are and notice what\'s there. '
                    'Don\'t pretend to feel something you don\'t.')],
                  '“No warmth today? Then rest your hands there and notice what you find, no faking required.” becomes '
                  '“If you can’t find any warmth today, just leave your hands where they are and notice what’s there. '
                  'Don’t pretend to feel something you don’t.”',
                  'Your inner child guide’s two lines, word for word. The question-and-answer turn read AI (Low, then '
                  'High), and “no faking required” says it sideways; your published induction says it straight: “I '
                  'will not force it. I will not fake it.”',
                  'The rest of the paragraph, the loop and the rest of the practice word for word.', DECIDE,
                  'I’d approve: the same instruction, said the way you’d say it to someone in the room.', None,
                  reading(win_blocks(('s1101-20', 5), ('s1101-20', 6)))))
    # G-23: Working with your guards, his inner child guide's words; the first round's fix of them undone
    i1 = block_with('But before you decide where it\'s coming from, ask it what it\'s trying to stop, or what it wants.')
    i2 = block_with('Say to the guard, in the same Nurturer voice you meant for your inner child:')
    S.append(card('G-23', 'icguide', '“… ask it what it’s trying to stop, or what it wants.”',
                  [(i1, 'But before you decide where it\'s coming from, ask it what it\'s trying to stop, or what it '
                        'wants. It could also be your inner child, mad that you took so long to come back, or your '
                        'inherited parent script, or something from earlier today, or a bit of each.',
                    'It might not be a guard at all, though. Maybe it\'s your inner child, mad that you took so long to '
                    'come back. Maybe it\'s your inherited parent script, or something from earlier today, or a bit of '
                    'each. So before you decide where it\'s coming from, ask it what it\'s trying to stop, or what it '
                    'wants.'),
                   (i2, 'Say to the guard, in the same Nurturer voice you meant for your inner child:',
                    'Talk to the guard the way your Nurturer talks to your inner child:'),
                   (i2, 'If nothing comes, that\'s fine for now. At some point you can ask,',
                    'If nothing comes back, that\'s okay, you don\'t need to push for an answer. Later on, you can ask '
                    'it,')],
                  'In the first paragraph, the other things it could be come first, each in its own sentence, and then '
                  'what to do; in the second, how to talk to the guard, and that you don’t need to push when nothing '
                  'comes. Your words stay: “mad that you took so long to come back”, “a bit of each”, “I see you. I’m '
                  'not going to force my way past you. What’s going on?”, “Then wait and listen patiently.”',
                  'These two paragraphs read AI in five windows (the section read AI Detected). Most of their words are '
                  'your inner child guide’s. This afternoon’s fixes changed some of them without asking you (“What’s '
                  'going on?” had become “What’s up?”, and “If nothing comes, that’s fine for now.” “If you get nothing '
                  'back, leave it there for today.”), so I’ve put your words back and brought the fix here. As it was, '
                  'the paragraph told you what to do before it said what the thing might be, and the possibilities '
                  'ran on as one list; “in the same Nurturer voice you meant for your inner child” and “that’s fine for '
                  'now” said less than they mean.',
                  'Your inner child guide’s lines named above, and the rest of both paragraphs word for word.', DECIDE,
                  'I’d approve: your words, in an order a reader can follow, and the guard spoken to the way your '
                  'Nurturer would.', None,
                  reading(win_blocks(('s1101-23', 7), ('s1101-23', 8), ('s1101-23', 9), ('s1101-23', 10),
                                     ('s1101-23', 11)))))
    # W-164: his step A of Don't rush the repair
    i = block_with('A. Prepare yourself to tend to them with some privacy')
    S.append(card('W-164', 'yours', '“Can you pause before you act? …”',
                  [(i, 'Check how much grown-up you is really in the room first. Can you pause before you act? Are you '
                       'following through after making decisions? If you can’t do those things because you’re basically '
                       'the frightened kid still, then let’s leave the deeper conversation until later. Do whatever '
                       'helps you come back a bit before you try to talk to little you.',
                    'Check how much grown-up you is really in the room first: can you pause before you act, and do you '
                    'follow through on what you decide? If you can’t, because right now you’re mostly still the '
                    'frightened kid, leave the deeper conversation for later, and do whatever helps you come back to '
                    'yourself a bit before you try to talk to little you.')],
                  'The two questions become one, and the “if … because … then let’s” sentence and the next one become '
                  'one sentence that says what to do.',
                  'Human (Low) twice: two questions in a row, then a long “if … because … then” sentence. Your step '
                  'says to check one thing, whether the adult is there, and what to do if not.',
                  'Your first sentence of step A, and the steps after it, word for word.', DECIDE,
                  'I’d approve: the same check, said once.', None, reading(win_blocks(('s1101-27', 7), ('s1101-27', 8)))))
    # W-270: his heading Already Trancey? (and the line in Before you begin that names it)
    i = block_with('Already Trancey? Stabilize before dipping deeper.', level=2)
    j = block_with('(The part below called "Already Trancey? Stabilize before dipping deeper." can be used')
    S.append(card('W-270', 'yours', '“Already Trancey? Stabilize before dipping deeper.”',
                  [(i, 'Already Trancey? Stabilize before dipping deeper.', 'When you’re already trancey'),
                   (j, '"Already Trancey? Stabilize before dipping deeper."', '"When you\'re already trancey"')],
                  'The heading becomes “When you’re already trancey”, and step 3 of Before you begin names it that way.',
                  'AI (Low): a question and then a command is a heading shape Pangram reads as AI. This one says when '
                  'to use the section, as your paragraph under it does (“This is for when …”).',
                  'Your paragraphs under the heading, and the rest of step 3, word for word.', DECIDE,
                  'I’d approve, unless you like your heading’s ring better; it’s the smallest of these.', None,
                  reading(win_blocks(('s1101-39', 1)))))
    # W-271: his paragraph under it
    i = block_with('This is for when you\'re already open for some reason')
    S.append(card('W-271', 'yours', '“This is for when you’re already open …”',
                  [(i, 'This is for when you\'re already open for some reason (loveyhuasca, meditation, lucid dreaming, '
                       'going through grief, listening to beautiful music, prayer, erotic energy, exhaustion, seeing '
                       'something you love, etc) and want to aim and stabilize it.',
                    'This is for when something has already opened you up before you start: loveyhuasca, meditation, '
                    'lucid dreaming, going through grief, listening to beautiful music, prayer, erotic energy, '
                    'exhaustion, seeing something you love, etc.')],
                  'The list comes out of its brackets, and “and want to aim and stabilize it” comes off the end.',
                  'Human (Low), 38 words. Your next paragraph says “you just need to aim and stabilize it, and keep it '
                  'kind”, so the end of this one said it first; and “already open for some reason” is said plainly as '
                  'something having opened you up before you start.',
                  'Your list word for word, and the next paragraph as it is.', DECIDE,
                  'I’d approve: it says it once, in your next paragraph.', None, reading(win_blocks(('s1101-39', 2)))))
    # W-274: his "Only what I can integrate, please." (keep)
    i = block_with('Say something like, "Only what I can integrate, please.')
    S.append(edit_card('W-274', 'yours', '“Only what I can integrate, please.”', i,
                       'Say something like, "Only what I can integrate, please.',
                       'Pangram read these nine words Human (Low). Short windows rarely get its top label, and this one '
                       'says exactly what it means; “integrate” is the guide’s word for taking in only what you can '
                       'live with, used the same way in Appendix G.',
                       'Keep it as it is, I’d say; the section is checked again after your answers either way.',
                       reading(win_blocks(('s1101-39', 7)))))
    # W-282: his paragraph Make the hypnosis more alert
    i = block_with('If being still tends to make you sleepy, zone out, or wish you were out (escapism)')
    S.append(card('W-282', 'yours', '“If being still tends to make you sleepy …”',
                  [(i, BL[i]['text'],
                    'If sitting still makes you sleepy, or you zone out, or you\'d rather be anywhere else (escapism), '
                    'no worries, there\'s a trick for that: instead of relaxing more, get a bit more alert (relaxed and '
                    'alert, not on edge). Keep your eyes open. Each time you tell yourself you\'re getting clearer, make '
                    'a small movement with your hand. Then stop moving your hand and see where your mind is. The '
                    'movement gives the part of you that wants to escape somewhere to go, into your body. Say something '
                    'like,')],
                  'Each sentence said the plain way: “relaxed and alert, not on edge” for “relaxed-alert, not '
                  'paranoid-alert”; “each time you tell yourself you’re getting clearer” for “each time you make the '
                  'auto-suggestion that you’re gaining increasing clarity”; and what the hand movement is for.',
                  'The whole paragraph read AI: High on its first two sentences, then Medium, High, Medium. “That hand '
                  'movement is the mental escape into the body’s flow” took two reads to follow; I’ve said it as I '
                  'understand it, that the movement gives the urge to escape somewhere to go, into the body. If that '
                  'isn’t what you meant, Revise.',
                  'The script after it, and the heading.', DECIDE,
                  'I’d approve, if I’ve read the hand movement right.', None,
                  reading(win_blocks(('s1101-40', 6), ('s1101-40', 7), ('s1101-40', 8), ('s1101-40', 9)))))
    # W-283: his fingers script
    i = block_with('“Starting with your eyes open, press your thumb to your forefinger.')
    S.append(card('W-283', 'yours', '“Starting with your eyes open, press your thumb …”',
                  [(i, BL[i]['text'],
                    '“Starting with your eyes open, press your thumb to your forefinger, gently, and let go. As you do, '
                    'you begin to bring yourself into a place of clearer awareness… Press and let go again, and you’re '
                    'clearer still. And once more, into the clearest state of awareness yet. Now stop pressing. In the '
                    'first second after you stop, notice if there’s any echo of the pressing in your fingers, in your '
                    'breathing, in your attention, or nowhere at all. Just notice, sit up straight and work from this '
                    'level.”')],
                  'Three presses still, each said once: “press your fingers together and release” isn’t repeated in '
                  'full each time, and “in the first second after you stop pressing your fingers together '
                  'deliberately” becomes “in the first second after you stop”.',
                  'The script read AI (High, Medium, High). A script read aloud repeats on purpose, so this is your '
                  'call; the repeats here are whole clauses said again word for word, which is the part Pangram '
                  'reads.',
                  'Each press, the clearest last (your card of 1 November), the echo, and your last sentence.', DECIDE,
                  'I’d approve, or write your own if you’d rather keep the rhythm of the repeats.', None,
                  reading(win_blocks(('s1101-40', 10), ('s1101-40', 11), ('s1101-40', 12)))))
    # W-289: his fractionation paragraph
    i = block_with('Fractionation means returning toward ordinary awareness')
    S.append(card('W-289', 'yours', '“Fractionation means returning toward ordinary awareness …”',
                  [(i, BL[i]['text'],
                    'Fractionation means coming partway back toward normal awareness, then deciding whether to go back '
                    'into the trance. It gives the trance a revolving door, so you can check how the session is going '
                    'from a few different depths instead of "flying blind." Going in and out a few times also makes '
                    'going in and coming out easier and quicker, until it feels natural. At some point in a session, you '
                    'can do it on purpose, like this:')],
                  '“returning toward ordinary awareness … hypnotic absorption” becomes “coming partway back toward '
                  'normal awareness … the trance”; “so that the approach can be evaluated at different levels” becomes '
                  '“so you can check how the session is going from a few different depths”; and the last sentence '
                  'leads into your script under it.',
                  'AI (Low) on the heading and the first two sentences, Human (Low) on the third. “Hypnotic '
                  'absorption”, “the approach can be evaluated at different levels” and “add this with intention” are '
                  'abstract; said as what you do.',
                  'Your revolving door, “flying blind”, and the script under it word for word.', DECIDE,
                  'I’d approve.', None, reading(win_blocks(('s1101-41', 2), ('s1101-41', 3)))))
    # W-358: his inner child guide's "That's enough for today ..." (keep)
    i = block_with('tell your little one, "That’s enough for today. We’re going back to the life we’re building."')
    S.append(edit_card('W-358', 'icguide', '“We’re going back to the life we’re building.”', i,
                       'We’re going back to the life we’re building."',
                       'Your inner child guide’s line, the one every session ends on (your card F18.1 kept it here). '
                       'Pangram read its last ten words Human (Low); the line is clear and it’s yours, so there’s '
                       'nothing to say more plainly.',
                       'Keep it as it is, I’d say; the section read Human Written overall.',
                       reading(win_blocks(('s1101-51', 3)))))
    # W-509: his bridge-words paragraphs
    i1 = block_with('Bridge words are words like ‘as, whilst, because, when, after, before, which means’ etc.')
    i2 = block_with('Here\'s an example of some of the overly commanding bridge language many hypnotists will use:')
    S.append(card('W-509', 'yours', '“Bridge words are words like …”',
                  [(i1, BL[i1]['text'],
                    'Bridge words, like ‘as’, ‘whilst’, ‘because’, ‘when’, ‘after’, ‘before’ and ‘which means’, link one '
                    'event to the next, so the first can seem to come with the second, or even cause it. That doesn\'t '
                    'mean it does, of course.'),
                   (i2, 'Here\'s an example of some of the overly commanding bridge language many hypnotists will use:',
                    'Lots of hypnotists use them to claim too much, like:')],
                  'The definition in one sentence (“which can make something seem like it goes along with or produces '
                  'the next thing” said as “so the first can seem to come with the second, or even cause it”), and '
                  '“overly commanding bridge language” said as what it does: claims too much.',
                  'These paragraphs are inside one AI (High) window of 402 words over Patterns 3 to 7. Our paragraphs '
                  'in it are fixed already; yours are here.',
                  'Your two examples, “Because I breathe, the trauma leaves.” and the communion version, word for '
                  'word.', DECIDE, 'I’d approve.', None, reading({i1, i2})))
    # W-513: his embedded-invitation paragraph
    i = block_with('An embedded invitation places a small direction inside a larger sentence.')
    S.append(card('W-513', 'yours', '“An embedded invitation places a small direction …”',
                  [(i, 'An embedded invitation places a small direction inside a larger sentence. For our purposes in '
                       'ethical communion-style hypnosis, we don\'t use these to hide commands, but to smooth them into '
                       'nudges without breaking the communion dialog rhythm, for example:',
                    'An embedded invitation tucks a small direction inside a bigger sentence. In ethical, '
                    'communion-style hypnosis we don\'t use them to hide commands. We use them to soften a direction into '
                    'a nudge, so it doesn\'t break the back-and-forth of the conversation, for example:')],
                  '“For our purposes in …” goes, “we don’t use these to hide commands, but to …” becomes two sentences, '
                  'and “the communion dialog rhythm” is said as “the back-and-forth of the conversation”.',
                  'In the same AI (High) window as the bridge words.',
                  'Your example, “And I can allow myself to experience...”, and the rest of Pattern 5.', DECIDE,
                  'I’d approve.', None, reading({i})))
    # W-579: his example in What I will not use NLP for
    i = block_with('As an example, I won’t tell anyone to override their fear without first asking what it’s protecting.')
    S.append(card('W-579', 'yours', '“As an example, I won’t tell anyone to override their fear …”',
                  [(i, BL[i]['text'],
                    'For example, I won’t tell anyone to push past their fear before asking what it’s protecting, and I '
                    'won’t make anyone feel rushed when they want time to take it in.')],
                  'The fragment “Or to make them feel urgency when they want time to process.” joins the sentence before '
                  'it.',
                  'AI (Medium), then AI (Low) on the fragment that stood as its own sentence.',
                  'The rest of the section word for word.', DECIDE, 'I’d approve.', None,
                  reading(win_blocks(('s1101-71', 2), ('s1101-71', 3)))))
    # W-589: his step in Running the whole NLP sequence
    i = block_with('Gently change an aspect of your pattern\'s representation from the prior step.')
    S.append(card('W-589', 'yours', '“Gently change an aspect of your pattern’s representation …”',
                  [(i, BL[i]['text'],
                    'Gently change one thing about how the pattern showed up in the step before, for example move the '
                    'image further away, turn the sound down, or slow it down.')],
                  '“an aspect of your pattern’s representation from the prior step” becomes “one thing about how the '
                  'pattern showed up in the step before”, with your published version’s examples.',
                  'Human (Low). Your published step gave the examples (“Move it back, lower the volume, add space, '
                  'change posture, slow the scene.”); without them, “an aspect of your pattern’s representation” is '
                  'hard to act on.', 'The steps around it word for word.', DECIDE, 'I’d approve.', None,
                  reading(win_blocks(('s1101-72', 5)))))
    # W-596: his Appendix C opening (keep)
    i = block_with('What to do when you feel like you’re being pushed too hard by something')
    S.append(edit_card('W-596', 'yours', '“I don’t even have to attack it.”', i, 'I don’t even have to attack it.',
                       'Pangram read these eight words Human (Low), in your Appendix C opening (the section read Human '
                       'Written overall). The sentence is clear.',
                       'Keep it as it is, I’d say.', reading(win_blocks(('s1101-73', 3)))))
    # W-605: his Hypnosis-specific audit, in his Appendix C way
    first = block_with('Before accepting a hypnotic recording or live suggestion, ask these important questions')
    blocks = list(range(first, first + 11))
    t = {k: BL[k]['text'] for k in blocks}
    assert t[blocks[6]] == 'Continuing with the job interview:', t[blocks[6]]
    new = {
        blocks[0]: 'Before you let a hypnotic recording or a live hypnotist put suggestions into your head, interview '
                   'them a bit, so you don\'t get manipulated.',
        blocks[1]: 'First, what are they going to do to bring you under? And if you react to something, will they '
                   'pause or change the script, or stop and bring you all the way back?',
        blocks[2]: '',
        blocks[3]: 'Then, if you can\'t tell what\'s going on, do they take that as proof the process worked? Are they '
                   'using identity roles, obedience ladders, age regression, or your wish to belong, to get past your '
                   'adult judgment?',
        blocks[4]: '',
        blocks[5]: 'Keep in mind though, you can only answer that last one by reading the script first, or by telling '
                   'them what your adult judgment would accept, since they can\'t be expected to know that.',
        blocks[7]: 'Will they tell you before they use fractionation, cues, or anything else that affects your memory or '
                   'what you do after the session?',
        blocks[8]: 'Are they quietly turning what you feel in your body into evidence for something they\'d already '
                   'decided?',
        blocks[9]: 'And when it\'s time to come out, will they tell you clearly that the session is over, so you get your '
                   'normal waking (and walking) self back and can think critically again?',
        blocks[10]: 'If any answer is unclear, be careful. Ask for the exact script. If they don\'t want to give it, '
                    'change the method, or walk right out that door.',
    }
    S.append(card('W-605', 'yours', 'Hypnosis-specific audit',
                  [(k, t[k], new[k]) for k in sorted(new)],
                  'The audit as you’d say it to the reader, the way you turned Appendix C’s list into questions: its '
                  'eight questions in five paragraphs instead of eight lines, “you” instead of “my”, and the jargon '
                  'said plainly (“induction mechanics … to bring me under the spell”, “implicitly”, “a prior '
                  'assumption”, “my critical judgement abilities”). Your bridge “Continuing with the job interview:” '
                  'stays, and so does your ending.',
                  'The section read AI Generated (1.0): AI (High) on the heading and the first four questions, AI '
                  '(Medium) on “Keep in mind though …”, AI (High) on the next three, and AI (Medium) on the last '
                  'lines. Your Appendix C, rewritten the same way, reads Human Written. This may also be what your '
                  'question 27 comment meant (“apply the fix strategy I used above on the below”).',
                  'Every question, “Continuing with the job interview:”, “walk right out that door”.', DECIDE,
                  'I’d approve: it’s your strategy from Appendix C, which reads Human, on the section that reads AI.',
                  None, reading(set(blocks))))
    # W-685: his inner child guide's forgiving-yourself lines
    i = block_with('Then you\'re allowed to stop holding yourself hostage, and the responsibility stays.')
    S.append(card('W-685', 'icguide', '“Then you’re allowed to stop holding yourself hostage …”',
                  [(i, 'Then you\'re allowed to stop holding yourself hostage, and the responsibility stays. Every so '
                       'often, come back to how you got to be someone who could do that,',
                    'Then you can stop holding yourself hostage, while you keep owning what you did. Now and then, look '
                    'again at how you got to be someone who could do that,')],
                  '“and the responsibility stays” becomes “while you keep owning what you did”, and “Every so often, '
                  'come back to” becomes “Now and then, look again at”.',
                  'Human (Low), 41 words: your inner child guide’s lines, shortened. “The responsibility stays” is '
                  'said as what it means for the person doing it.',
                  'The first sentence and the end, “until you understand it well enough that it changes how you feel.”',
                  DECIDE, 'I’d approve.', None, reading(win_blocks(('s1101-84', 9)))))
    # W-687: his inner child guide's "Borrowed is fine ..."
    i = block_with('Borrowing them is fine, as long as it’s from someone steady who won’t try to run your trip for you.')
    S.append(card('W-687', 'icguide', '“Borrowing them is fine …”',
                  [(i, 'Borrowing them is fine, as long as it’s from someone steady who won’t try to run your trip for '
                       'you.',
                    'If you don’t have them in you yet, it’s fine to borrow them from someone steady, as long as they '
                    'won’t try to run your trip for you.')],
                  'Says when you’d borrow them (when they aren’t in you yet), and keeps “someone steady” and “run your '
                  'trip for you”.',
                  'Human (Low): your inner child guide’s line (“Borrowed is fine, as long as …”), shortened here; “them” '
                  'is the Nurturer and Protector of the sentence before.',
                  'The rest of the paragraph word for word.', DECIDE, 'I’d approve.', None,
                  reading(win_blocks(('s1101-85', 3)))))
    # W-762: his steps of the no-trance inner contact
    i = block_with('Now keep your sense of agency during the answer phase.')
    j = block_with('Don\'t jump to interpreting it as validation of some theory.')
    k = block_with('Hand off the role: have your adult self answer that same question')
    m = block_with('Integration/exit: reality test the signal you noticed.')
    n = block_with('There\'s no elaborate exit protocol here since you didn\'t go into trance.')
    S.append(card('W-762', 'yours', '“Now keep your sense of agency during the answer phase.”',
                  [(i, 'Now keep your sense of agency during the answer phase.',
                    'While you wait for an answer, stay the one who decides.'),
                   (i, 'You can always take a break or rephrase the question. Sometimes you might ask advice from someone '
                       'else.',
                    'You can always take a break or ask the question a different way. Sometimes you might ask someone '
                    'else\'s advice.'),
                   (j, 'Don\'t jump to interpreting it as validation of some theory.',
                    'Don\'t jump to reading it as proof of some theory.'),
                   (k, BL[k]['text'],
                    'Then let your adult self answer the same question, preferably in writing or by doing one practical '
                    'thing.'),
                   (m, BL[m]['text'],
                    'To finish, check the signal against reality. If it seems right, part of that check can be doing one '
                    'simple thing based on it.'),
                   (n, 'There\'s no elaborate exit protocol here since you didn\'t go into trance.',
                    'You didn\'t go into a trance, so there\'s nothing to come back out of.')],
                  'Five of your steps said plainly: “keep your sense of agency during the answer phase”, “interpreting '
                  'it as validation”, “Hand off the role”, “Integration/exit: reality test”, “no elaborate exit '
                  'protocol”.',
                  'Human (Low) on four windows here, each on one of these sentences. Your published version names each '
                  'step the same way (Genuine choice, Handoff, Integration and exit); said as what you do in it.',
                  'Your other sentences in these steps word for word (“Hopefully your name didn’t suddenly change to '
                  'Larry.” is in the step before).', DECIDE, 'I’d approve.', None,
                  reading(win_blocks(('s1101-99', 10), ('s1101-99', 12), ('s1101-99', 13), ('s1101-99', 14)))))
    # the stretches of ours that read AI in three tries (round 1 or 2 in the section checks, round 3 alone: ../recheck/)
    stuck = [
        ('E-107', '“That way you keep the good parts of feeling younger …”', 'That way you keep the good parts of feeling younger',
         'AI (High) in the first section check (the paragraph before my rewrites), AI (High) in the second (one window over '
         'the whole section), and AI (High), 38 words, checked with the quote before it',
         'Your published version: “That distinction lets you recover curiosity, spontaneity, play, sensory freshness, '
         'honest need, and quick emotional movement without pairing those gifts with obedience, helplessness, scolding, or '
         'weakened judgment.” Three versions of ours kept its two lists, and each read AI. The paragraph before it, '
         'rewritten the same evening, reads Human (High) now.'),
        ('E-315', '“If your recording cuts out partway through …”', 'If your recording cuts out partway through',
         'AI (High) on these two paragraphs in both section checks (126 and 134 words), and AI checked alone: AI (High '
         'and Medium) on the first, AI (High) on the second',
         'Your published version: “If a recording stops unexpectedly: say, “The recording stopped and the session is '
         'over.” … Don’t wait for the missing narrator to release you.” and “Sleep is separate. … A waking recording '
         'shouldn’t end by preserving a role, reduced judgment, impaired movement, blankness, an undefined reset word, or '
         'an invitation to remain altered indefinitely.” Three versions of ours, rules first and then rules with reasons, '
         'all read AI.'),
        ('E-368', '“Once or twice a week …”', 'Once or twice a week, when it’s useful, give this practice more time',
         'AI Detected (0.65) in the first section check, AI Generated (1.0) in the second, and AI (High) checked alone and '
         'with the paragraph after it',
         'Your published The weekly deeper practice: two paragraphs, how to give the practice more time once or twice a '
         'week and why to do the normal thing right after. Three versions of ours read AI, the last two more than the '
         'first.'),
        ('E-406', '“If the bliss spreads out into a big warm haze …”', 'If the bliss spreads out into a big warm haze',
         'AI (Medium) and then AI (High) in the section checks, with the headings and your “Don’t pry.” around it, and AI '
         '(High) checked alone with its heading',
         'Your published “Ask the bliss to become specific.” and “What task, boundary, meal, rest, repair, or '
         'conversation does love require next?” Three versions of ours read AI.'),
    ]
    for cid, title, start, read, why in stuck:
        i = block_with(start)
        blocks_ = [i] + ([i + 1] if cid in ('E-315', 'E-368') else [])
        S.append({'id': cid, 'type': 'stuck', 'title': title, 'where': sr.where(BL, i), 'advice': 'edit',
                  'why': why + ' The version that’s in is clear, so it stays until a version reads both clear and Human '
                  '(your rule of 29 October).', 'reading': read,
                  'advice_note': 'Edit it, if you can say it your way; I’m out of versions that keep your meaning and '
                                 'read Human here. Or keep it as it is, and the whole-guide check reads it in place.',
                  'keep_label': 'keep it as it is', 'found_by': FOUND,
                  'spans': [{'block': b, 'start': 0, 'end': len(BL[b]['text'])} for b in blocks_]})
    return S


def build():
    S = build_cards()
    S.sort(key=lambda s: (s['spans'][0]['block'], s['spans'][0]['start']))
    n = collections.Counter(s['type'] for s in S)
    edit = sum(1 for s in S if s['advice'] == 'edit')
    review = {
        'format': sr.FORMAT, 'review_id': 'inner-signal-hypnosis-guide-cards-20261101-s1101',
        'title': 'Hypnosis Guide Cards, 1 November (2)',
        'intro': [
            'Your hypnosis guide as it is in Git, after each section was checked in Pangram by itself. 91 windows '
            'read AI or Human (Low). The ones in our words (Emulate’s or mine) are fixed in the guide already, each '
            'said plainly from your published version. The ones in <b>your own words</b> are here: <b>%d cards</b> on '
            'paragraphs you wrote or rewrote, and <b>%d</b> on lines from your inner child guide that this guide '
            'uses. %d of them I’d keep as they are. And <b>%d stretches of our own words</b> are here too, as stretches to '
            'edit: each read AI in three tries, and you may want to say them your way.' % (n['yours'], n['icguide'],
                                                                                          edit - n['stuck'], n['stuck']),
            'One of them, G-23, puts back two lines of your inner child guide that the first round of fixes this '
            'afternoon changed without asking you (“What’s going on?” and “If nothing comes, that’s fine for now.”).',
            'Each card says what Pangram read there. Once you’ve answered, each section with a card gets its second '
            'and last check by itself, and then the whole guide on the Substack drafts.',
            'Your answers save as you click. When you’re done, click <b>Copy my answers</b> (or <b>Save them as a '
            'file</b>) and send them to me.',
        ],
        'git_file': GIT_FILE, 'article': {'file': ARTICLE, 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'links': {'guide': BLOB + ARTICLE, 'review': BLOB + LANE + 'fix-20261101/sections/review/REVIEW-S1101.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    return review, n


def marked(j, spans):
    t = BL[j]['text']
    for sp in sorted((x for x in spans if x['block'] == j), key=lambda x: -x['start']):
        t = t[:sp['start']] + '**' + t[sp['start']:sp['end']] + '**' + t[sp['end']:]
    return t


def cards_md(review):
    """Every card as a page GitHub renders, in the guide's order (the page's readable copy in Git)."""
    types = review['types']
    out = ['# %s: every card' % review['title'], '',
           'The page\'s cards as text, in the order of the guide. Built %s from [the guide so far](%s). To answer, use '
           'the page; or write your answer under a card\'s number in a message to me.' % (
               review['built'], review['links']['guide']), '']
    section = None
    for s in review['suggestions']:
        b = s['spans'][0]['block']
        if BL[b]['section'] != section:
            section = BL[b]['section']
            out += ['## %s' % (section or 'The opening'), '']
        out += ['### %s: %s (%s)' % (s['id'], s['title'], types[s['type']]['label']), '']
        if s.get('reading'):
            out += ['**Pangram read:** %s' % s['reading'], '']
        if s['advice'] == 'edit':
            blocks_ = sorted({sp['block'] for sp in s['spans']})
            out += ['**As it is now** (the words Pangram read in bold):', '']
            out += ['> %s' % marked(k, s['spans']) for k in blocks_] + ['']
        else:
            for e in s['edits']:
                out += ['**Now** (the words it changes in bold):', '', '> %s' % marked(e['block'], s['spans']), '']
                out += (['**How it would read:**', '', '> %s' % e['after'], ''] if e['after'] else
                        ['**How it would read:** this paragraph goes (its words are in the one above).', ''])
        out += ['**Why:** %s' % s['why'], '', '**My advice:** %s' % s['advice_note'], '']
    return '\n'.join(out).replace('\n\n\n', '\n\n') + '\n'


def main():
    review, n = build()
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-S1101.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-S1101.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-S1101.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    (HERE / 'REVIEW-S1101.md').write_text(cards_md(review), encoding='utf-8')
    print(len(review['suggestions']), 'cards:', dict(n))


if __name__ == '__main__':
    main()
