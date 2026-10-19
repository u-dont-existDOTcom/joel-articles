# Turn 73 installs (registered with register(name, old, new); see t73.py). Joel's answers of 2026-10-18 21:58 UTC
# (experiments/t73-answers/JOEL-20261018-2158.md).

SAID73 = 'his answers of 2026-10-18 21:58 UTC (experiments/t73-answers/JOEL-20261018-2158.md)'


def note(text):
    return '<!-- Turn 73 (%s): %s -->\n\n' % (SAID73, text)


def dnote(stem, text, key):
    return note(text + ' experiments/t73-guide/drafts/%s.txt. @@%s@@' % (stem, key))


# --- 55: his picks for the filler sweep (turn 72's JUNK-SWEEP.md) ------------------------------------------------------
register('s2', lambda: para('Going back can still matter, since realizations'),
         lambda: dnote('c55-2', '55, 2, A: "since realizations are a real part of life" was a truism; the guide\'s own reason is "Meaningful grief and practice can revisit familiar ground; novelty is not required every time."', 'S2') + draft('c55-2'))
register('s4', lambda: para("In one of the Buddha's own accounts"),
         lambda: dnote('c55-4', '55, 4, A: "Of course not." is out, so the question is left for the reader to check.', 'S4') + draft('c55-4'))
for _x in 'ab':
    register('s9' + _x, lambda: para('After the day, look at what actually happened.'),
             (lambda s: lambda: dnote(s, '55, 9, his meaning: "your fix doesn\'t make sense, since the acts were already supposed to be done (look at what actually happened). What i meant to say there was "healing is nonlinear, and sometimes standing up for yourself might make you feel worse at first."", in place of "because the process is dynamic".', 'S9') + draft(s))('c55-9' + _x))
register('s12', lambda: para('Differentiation can happen right inside a family'),
         lambda: dnote('c55-12', '55, 12, A: "You\'d still belong, just selectively." for "You\'d be belonging selectively, which still leaves room to belong."', 'S12') + draft('c55-12'))
register('s13', lambda: para('My father often suggested folks remember'),
         lambda: dnote('c55-13', '55, 13, A: "as dramatic as a car crash" for "as dramatic as that", since his sister\'s line sits between them now.', 'S13') + draft('c55-13'))
register('s14', lambda: para('They still have to answer for what they did'),
         lambda: dnote('c55-14', '55, 14, A ("remove that clause it is just confusing"): "and in theory they could have done something else" is out.', 'S14') + draft('c55-14'))
register('s17', lambda: para("It's not so hard to understand that words have power."),
         lambda: dnote('c55-17', '55, 17, A: "the original problem" for "the original question", since there\'s no question before it.', 'S17') + draft('c55-17'))

# --- 57, 1: his own ending for How This Relates to IFS P4 ---------------------------------------------------------------
register('ifs4', lambda: para('Is a perfect Higher Self already waiting'),
         lambda: dnote('c57-1', '57, 1 ("confusing with the "both"... replace last part with"): his words from "It\'s a vantage point" on, with the Anthony de Mello link kept on his name.', 'IFS4') + draft('c57-1'))

# --- 57, 3: the schema section's differences and how to choose a therapist -------------------------------------------
ST_SRC = ('his 57, 3 ("i felt like the schema therapy part was a bit short. i\'d like to include how it differs from my guide. including the spirituality part which schema lacks and which IFS goes overboard on IMO... . and gpt gave some suggestions for how to select a therapist, i thought we should have some of those also, bc not just any schema or IFS therapist will be good right."), from the research suggestion of 2026-10-18 (UDA cd9bf74e, suggested-fixes/joel-articles/2026-10-18-schema-therapist-fit-and-reparenting-guide.md: the differences "depend on the particular schema therapist"; its consult questions 1, 2, 3 and 6; "Directory listing/certification is a useful search starting point, not a guarantee of technique, ethics or fit"). '
          'Jeffrey Young\'s postdoctoral work with Aaron Beck: Wikipedia\'s Jeffrey Young (psychologist), opened 2026-10-18; schema therapy "Building on cognitive therapy": Guilford\'s page for Schema Therapy: A Practitioner\'s Guide.')
for _a in 'abc':
    for _b in 'abc':
        register('st%s%s' % (_a, _b), lambda: para('Of the clinical approaches I know'),
                 (lambda a, b: lambda: para('Of the clinical approaches I know') + '\n\n' + dnote(a, ST_SRC + ' The differences, with spirituality first, as he asked.', 'ST2') + draft(a)
                  + '\n\n' + dnote(b, 'choosing a therapist, from the same research and his words "not just any schema or IFS therapist will be good". The guide\'s no to the inner-child frame, in the research\'s question 2, isn\'t asked: he cut it on 2026-10-08.', 'ST3') + draft(b))('st2-' + _a, 'st3-' + _b))


# --- His Inner Monologue move (turn 72's move-monologue-pending-20261018): the section goes right after When Healing
# Turns Into Checking, before When the Present-Day Adult Is Dangerous to the Child, which moved in round t72f ----------
MONO_H = '## You Don’t Need an Inner Monologue\n'
BODY_C = '<!-- Regulation section (source H2 `Regulation May Come Before Dialogue`)'
DMOVE_KEY = 'his section move: When the Present-Day Adult Is Dangerous to the Child goes after'


def _mono():
    t = ART.read_text(encoding='utf-8')
    j, k = t.find(MONO_H), t.find(BODY_C)
    return t[j:k] if 0 <= j < k else None


def _dmove_line():
    return next((l for l in ART.read_text(encoding='utf-8').split('\n') if DMOVE_KEY in l), None)


register('mono-out', _mono, '')
register('mono-in', lambda: _dmove_line() if _mono() else None,
         lambda: (note('his section move, the other half (2026-10-18 19:06 UTC: "i think we should move "you don\'t need an inner monologue section" to right after "when healing turns into checking" and we should move "when the present-day adult is dangerous" after that"): You Don\'t Need an Inner Monologue is here now, its text unchanged. @@MONO@@') + _mono() + _dmove_line()) if _mono() else None)


# --- Round b ------------------------------------------------------------------------------------------------------------
register('s2b', lambda: para('Going back can still matter, since realizations'),
         lambda: dnote('c55-2b', '55, 2, A, in fewer words: "since realizations are a real part of life" was a truism; the guide\'s own reason is "Meaningful grief and practice can revisit familiar ground; novelty is not required every time."', 'S2') + draft('c55-2b'))
for _a in 'abc':
    register('st2only' + _a, lambda: para('Of the clinical approaches I know'),
             (lambda a: lambda: para('Of the clinical approaches I know') + '\n\n' + dnote(a, ST_SRC + ' The differences, with spirituality first, as he asked.', 'ST2') + draft(a))('st2-' + _a))


# --- Round c ------------------------------------------------------------------------------------------------------------
register('s4i', lambda: para("In one of the Buddha's own accounts"),
         lambda: dnote('c55-4', '55, 4, A: "Of course not." is out, so the question is left for the reader to check.', 'S4') + draft('c55-4'))
for _x in 'ac':
    register('yb4' + _x, lambda: para('Whatever you try from that map'),
             (lambda s: lambda: dnote(s, 'his Inner Monologue move (2026-10-18 19:06 UTC) put a 66-word AI window on this paragraph, my T-point paragraph of turn 34 (rounds t72e and t73b, https://www.pangram.com/history/cbcd178f-8fa5-47a2-8f0a-40cfde2db384), so its last three sentences are said again: the guide\'s "Learning often includes grief, fear, frustration, difficult dreams, or material you would rather not meet." and "But "I stayed oriented" is not enough by itself either.", with the gym as it was.', 'YB4') + draft(s))('yb4-' + _x))
for _x in 'bc':
    register('ifs5' + _x, lambda: para('And the parts just keep coming'),
             (lambda s: lambda: dnote(s, 'his 57, 3 (the longer schema section) put a 34- to 43-word AI window on this paragraph\'s last two sentences, mine of turn 71, in four of five checks (rounds t73a and t73b); its last sentence is the guide\'s "Institutionalization doesn\'t automatically make a framework clearer, safer, or more true." said again, without "by itself" (O43).', 'IFS5') + draft(s))('ifs5-' + _x))
register('chkm2', lambda: (lambda a, b: ART.read_text(encoding='utf-8')[ART.read_text(encoding='utf-8').index(a):ART.read_text(encoding='utf-8').index(b) + len(b)] if a and b else None)(para('Going back can still matter, since realizations'), para("And the checking doesn't always stay in your head.")),
         lambda: dnote('chkm2', '55, 2, A (in fewer words), with the checking-into-doing paragraph (54, 4, round t72d) folded into P2 word for word: with 55, 2 alone, that paragraph had a 37-word AI window in Before You Try to Go Deep (rounds t73a and t73b).', 'CHKM2') + draft('chkm2'))


# --- Round d: Your Body P4 with only its middle sentence said again (yb4-a and yb4-c read AI alone, round t73c) ---------
for _x in 'jl':
    register('yb4' + _x, lambda: para('Whatever you try from that map'),
             (lambda s: lambda: dnote(s, 'his Inner Monologue move (2026-10-18 19:06 UTC) put a 66-word AI window on this paragraph, my T-point paragraph of turn 34 (rounds t72e and t73b, https://www.pangram.com/history/cbcd178f-8fa5-47a2-8f0a-40cfde2db384), so its middle sentence, the guide\'s "But "I stayed oriented" is not enough by itself either.", is said without "by itself" (O43); the rest is as it was.', 'YB4') + draft(s))('yb4-' + _x))


# --- Round e: Also Look Outward's honesty paragraph, which the moved order exposes once P4 holds (round t73d) ----------
HON = "And reaching out doesn't mean telling strangers everything."
for _x in 'cd':
    register('hon' + _x, lambda: para(HON),
             (lambda s: lambda: dnote(s, 'his Inner Monologue move put a 38-word AI window on this paragraph, my C2 of turn 38 that he said yes to (rounds t72b, t72c and t73d, https://www.pangram.com/history/48c365a1-adca-4f29-a4c9-ad21ee98aaeb), so "how they handle the smaller things you tell them" gets a scene; the rest is as it was.', 'HON') + draft(s))('alo-hon-' + _x))


# --- Round f: 55, 2 and turn 72's P5 h (54, 11 and the rest of 8) in the new order ------------------------------------
register('yb5h', lambda: para('So how were the next few days?'),
         lambda: dnote('yb5-h', '54, 8 ("we can remove the "change several things at once" version in the other section since that sounds too vague to be useful"; coming out first is in Before You Try to Go Deep P2) and 11, B ("original list more informative"): the guide\'s "Try shorter duration, less depth or imagery, better timing, more symbolic or indirect representation, eyes open or stronger external anchors, less isolation, and more support." inside the paragraph\'s own "a bit easier" sentence (turn 72\'s draft, alone Human Written 0.38, https://www.pangram.com/history/2b7c63fe-e265-4de7-81a3-45ac0c97b555).', 'YB5') + draft('yb5-h'))


# --- Round g: "IMO" in words (O37: Joel 2026-10-01, "for other articles where they aren't used, you wouldn't put them in") --
for _x in ('2', '3'):
    register('st2b' + _x, lambda: para('Where it really differs is spirituality'),
             (lambda s: lambda: dnote(s, 'his "IMO" (57, 3) in words, since this article doesn\'t use chat acronyms (O37; Joel 2026-10-01: "for articles where the acronyms are used, you\'d use those, but for other articles where they aren\'t used, you wouldn\'t put them in").', 'ST2B') + draft(s))('st2-b' + _x))
