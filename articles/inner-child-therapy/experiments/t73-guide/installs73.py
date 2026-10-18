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
