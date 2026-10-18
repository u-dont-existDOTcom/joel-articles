# Turn 72 installs (registered with register(name, old, new); see t72.py). Joel's answers of 2026-10-18 19:06 UTC
# (experiments/t72-answers/JOEL-20261018-1906.md).

SAID72 = 'his answers of 2026-10-18 19:06 UTC (experiments/t72-answers/JOEL-20261018-1906.md)'


def note(text):
    return '<!-- Turn 72 (%s): %s -->\n\n' % (SAID72, text)


# --- His own edits and cuts -------------------------------------------------------------------------------------------

# 49, 6: "remove this nonsense, how did this get in? "Those don't even agree with each other on everything!""
RCW_OLD = "validates it as a package. Those don't even agree with each other on everything!"
register('rcw-cut', RCW_OLD, "validates it as a package.")
register('rcw-cut-note', "\n\nThis framework developed through the teachers and collaborators credited below",
         "\n\n" + note('49, 6: "Those don\'t even agree with each other on everything!" is out ("remove this nonsense, how did this get in?"). It was my rendering of the guide\'s "These approaches do not all make the same claims.", moved to the end of the paragraph in round t71ccc to break an AI window; how it got in is in experiments/t72-guide/REVIEWS.md.').rstrip('\n') + "\n\nThis framework developed through the teachers and collaborators credited below")

# 47 (A, E) and 49, 6: "dedup yeah, so just remove "Several teachers directly influenced this method. ...""
register('teachers-p1-cut',
         "Several teachers directly influenced this method. I can’t fully endorse any of them because none follows my whole approach or has expressed interest in doing so. Daja works with",
         "Daja works with")
register('teachers-p1-note', "\n\nDaja works with inner-child pl/ork intuitively",
         "\n\n" + note('47, A and E, and 49, 6: the two first-person sentences are his words, and they come out as a repeat of Related Clinical Work\'s "I borrow particular distinctions and practices ..." ("dedup yeah, so just remove ..."). The Gemini-thread sentence stays out (47, E).').rstrip('\n') + "\n\nDaja works with inner-child pl/ork intuitively")

# 49, 7: "Insert in p3 as first sentence: ..." (his text, his characters; the Open Path link from the guide's sentence it
# replaces, and the guide's IFS filter sentence out, since his new sentences say which to filter for)
OPEN_PATH = 'https://openpathcollective.org/pricing-and-eligibility-for-affordable-therapy/'
HIS_P3 = ("I don't know of a resource to find a perfect inner child therapist, and there are none which work with my guide yet, (although I can consult, and if you like the guide, you can ask a therapist to check it out and see what they agree with or disagree with as a great way to vet them). "
          "The best I could suggest at the moment is to search [Open Path Collective](" + OPEN_PATH + ") (or a similar resource in your country), which lists thousands of affordable therapists. "
          "Filter for  Schema Therapy, since that's the one with the most similarity to my guide, but you'll find about 10x more Internal Family Systems therapists, which also overlap with reparenting in many ways. "
          "You can often find [even more Schema therapists at the official site](https://schematherapysociety.org/Search?&tab=1): 3x more on that page for NYC than via Open Path search when I checked.")
register('teachers-p3',
         "If you're looking for a therapist, [Open Path Collective](" + OPEN_PATH + ") lists thousands of affordable ones. Filter for Internal Family Systems, since IFS-trained therapists often have the most relevant background for inner-child pl/ork. And for bottom-up support,",
         HIS_P3 + " And for bottom-up support,")

# 49, 2: cut his demon sentence in Non-altered states
register('demon-cut',
         "Even if you’ve never literally been attacked by a demon that looked like the one above, the truth is that in this world, we’re always being manipulated and attacked by whatever evil force sees us as an easy target. Even social media",
         "Even social media")

# 49, 2: his two fixes in Altered States Can Require Reparenting P2 (his words)
register('asr-p2-pro', "That said, professional assessment may be warranted in some situations.",
         "That said, it'd make sense to get a professional to weigh in for some situations.")
register('asr-p2-parents', "and it meant something that my parents took it seriously.",
         "and I really appreciate that my parents took it seriously without catastrophizing.")

# 51, A: "the grown-up relationship has to refer to between inner child and inner adult"
register('speak-p9', "then into the grown-up relationship,", "then into your relationship with the grown-up you,")

# 53, B
register('chicken-stages', "For now, I think of it in five fairly predictable stages.",
         "For now, I think of the whole path in five fairly predictable stages.")

# 54, 12 C: his wording
register('alo-only-support', "starts acting like they should be your only one, that's where I'd want the Protector paying attention.",
         "starts acting like they should be your only support, that's where I'd want the Protector paying attention.")


# 50: his One Intention in the Morning, One Review at Night, word for word (Franklin out: "keep all except for 4")
ONE_INTENTION = '''In the morning, begin the day intentionally, not just because the sun chose to come up once more, since we can't count on that 🫣. Here's one way you might pl/orkfully start off:

“Today I will neither be Peter Pan nor Captain Hook. I will notice a hook or 2 which lead to unconscious behaviors.”

Then at night, pay yourself to be your own therapist so as not to break the bank. Equipoisedly look into how the practice went for you today:

"Where did I notice the hook?" At dinner with the in-laws? Doom scrolling TikTok nonsense? Watching animé?

"Where did it still seem to control me despite noticing it?" (That's the most frustrating part, when you know better, and you still act the same.)

Then get practical so it doesn't become another OCD loop: "What small repair or protective act shall I bring in for a proper response to that?"

And don't forget to appreciate the good! Moments of warm, beneficial connection (whether internally from child to adult, socially, spiritually, or undefined) are all to be celebrated. Were you maybe firm like an elephant today, or courageous like a lion? Adopt the entire spirit animal zoo if need be! Turtles are good if you need impulse control.

Count recognition as progress, regardless whether it came up a bit late, as the goal is to bring the awareness closer and closer to the present. All or nothing from the get go would be cool, but we normally have to learn step by step. If/when you interrupted the pattern, pat yourself on the back, or even kiss yourself on the shoulder. If you made a mistake, you can see how to repair that. You can renew your intention for tomorrow, getting better & better, every day, in every way. And enjoy your well-earned rest tonight.'''


def _oi_old():
    t = ART.read_text(encoding='utf-8')
    h = '## One Intention in the Morning, One Review at Night\n\n'
    i = t.index(h) + len(h)
    j = t.index('\n## Use Childhood Photographs Gently', i)
    body = t[i:j].rstrip('\n')
    return None if body.endswith('And enjoy your well-earned rest tonight.') else h + body


register('one-intention', _oi_old,
         lambda: '## One Intention in the Morning, One Review at Night\n\n' + note('50: his own version of the section, word for word, in place of mine ("keep all except for 4"; Benjamin Franklin, my pointer 4, is out: "he seems tangential to this practice and from what you said it sounds a bit OCD"). He checked it himself: "this is human high conf". The rewrite and what it teaches are in experiments/t72-guide/REVIEWS.md.') + ONE_INTENTION)


# Two section moves (his message: "move "you don't need an inner monologue section" to right after "when healing turns into
# checking" and we should move "when the present-day adult is dangerous" after that, since both of those to me are less
# likely to be important for most people compared to the other sections, and the didn't really fit where they were")
DANGER_START = '<!-- Dangerous-adult H2 installed 2026-09-25'
MONO_H = '## You Don’t Need an Inner Monologue\n'
BODY_C = '<!-- Regulation section (source H2 `Regulation May Come Before Dialogue`)'
BORROW_H = '# Borrow the Adult Before You Can Be the Adult\n'
EMBED_NOTE = '<!-- The original bottom-up-healing embed belongs after readiness; exact native source remains source-recovery pending. -->\n\n'


def _blocks():
    t = ART.read_text(encoding='utf-8')
    i = t.index(DANGER_START)
    j = t.index(MONO_H)
    k = t.index(BODY_C)
    if not (i < j < k < t.index(BORROW_H)):
        return None
    danger = t[i:j]
    assert danger.endswith(EMBED_NOTE), danger[-200:]
    return danger[:-len(EMBED_NOTE)], t[j:k], EMBED_NOTE


def _move_old():
    b = _blocks()
    return None if b is None else b[0] + b[2] + b[1]


def _move_new():
    b = _blocks()
    return None if b is None else b[2]   # None once a move is in (round t72f)


def _move_ins_old():
    return None if _blocks() is None else '\n' + BORROW_H


def _move_ins_new():
    if _blocks() is None:
        return None
    danger, mono, _ = _blocks()
    moved = note('his section move: You Don\'t Need an Inner Monologue goes right after When Healing Turns Into Checking, and When the Present-Day Adult Is Dangerous to the Child after it ("both of those to me are less likely to be important for most people compared to the other sections"). Their text is unchanged.')
    return '\n' + moved + mono + danger + BORROW_H


register('move-out', _move_old, _move_new)
register('move-in', _move_ins_old, _move_ins_new)


# --- My drafts from his notes (each goes in only after it reads Human alone and in its h1) ----------------------------

def dnote(stem, text, key):
    return note(text + ' experiments/t72-guide/drafts/%s.txt. @@%s@@' % (stem, key))


# 49, 3: paranoia isn't automatically on the way to psychosis; practicality is the test (his examples, his words)
register('par', lambda: para('Your own drug history matters too.'),
         lambda: dnote('par-a', '49, 3: "paranoia isn\'t automatically leading to psychosis, since it can be valid, but it does tend to lead to psychosis when it isn\'t balanced by practicality", with his three examples ("so let\'s merge that in somehow"), in place of "Paranoia during a rough trip is a warning sign for psychosis."; "Freemason" for his "free mason".', 'PAR') + draft('par-a'))

# 49, 4: the fear, and his meaning ("the thing to fear is fear itself ... we give them the power")
register('tr', lambda: para('Sleep paralysis is a trance-like state'),
         lambda: dnote('tr-a', '49, 4, B: "the fear" for "it", with his meaning after it ("what i\'m trying to say is that the thing to fear is fear itself as it actually opens us up to being manipulated by demons which feed on it directly. so it\'s not really that they have no power, but we give them the power").', 'TR') + draft('tr-a'))

# 54, 11 B and 8: the guide's list of what to change, in place of "If you're getting worse, though, change several things at once, and get some support." ("sounds too vague to be useful")
register('yb5', lambda: para('So how were the next few days?'),
         lambda: dnote('yb5-b', '54, 11, B ("original list more informative"): the guide\'s "Try shorter duration, less depth or imagery, better timing, more symbolic or indirect representation, eyes open or stronger external anchors, less isolation, and more support."; and 54, 8: "If you\'re getting worse, though, change several things at once, and get some support." is out ("that sounds too vague to be useful"), since coming outward first is in Before You Try to Go Deep now.', 'YB5') + draft('yb5-b'))

# 54, 8 B and 10: coming outward first, in Before You Try to Go Deep after its P2
register('bg-out', lambda: para('And if the grown-up you is there, and it'),
         lambda: para('And if the grown-up you is there, and it') + '\n\n' + dnote('bg-out-b', '54, 8, B ("humanize that in before you try to go deep") and 10 ("that\'s what we are putting back into 8"): the guide\'s "If you cannot reliably stop, return, stay oriented, or inward attention itself is making things worse, stop the inner exercise and come outward first." with its "This is not an endurance test. One breath may be enough." and the eyes-open hello as the gentler way back in.', 'BGOUT') + draft('bg-out-b'))

# 54, 9 B ("keep first one remove 2nd one"): the full pause as a last resort that safety can force
register('bg3', lambda: para('If you ever need a full break from your little one'),
         lambda: dnote('bg3-b', '54, 9, B: the guide\'s "A complete tolerance pause is a last resort, and a safety problem can require a pause whether or not you want one." first; its no-testing-while-paused part stays out ("keep first one remove 2nd one").', 'BG3') + draft('bg3-b'))

# 54, 7 B: the guide's checks on a person, after his test line in Don't Give
register('dg-chk', lambda: para('If you still feel like a kid inside, somebody who seems grown-up'),
         lambda: para('If you still feel like a kid inside, somebody who seems grown-up') + '\n\n' + dnote('dg-chk-b', '54, 7, B: the guide\'s "Keep the feeling and test the conclusion against track record, respect for boundaries, independent evidence and contradictions, and what happens when you disagree or say no." after his test line (52, A).', 'DGCHK') + draft('dg-chk-b'))

# 54, 4 ("keep first instance"): checking that turns into doing, in When Healing Turns Into Checking after P2
register('chk-beh', lambda: para('Going back can still matter, since realizations'),
         lambda: para('Going back can still matter, since realizations') + '\n\n' + dnote('chk-beh-a', '54, 4 ("keep first instance, remove 2nd one in also look outward"; his 19:26 UTC "yes you read me correctly"): the guide\'s "A checking loop can move into behavior." with its examples and "The test may calm uncertainty briefly and then make the next fluctuation matter even more." ("exposure" and the exposure paragraph stay out, 54, 5, A).', 'CHKBEH') + draft('chk-beh-a'))

# 54, 4 ("remove 2nd one in also look outward") and 6 ("merge them"): his dating sentence out, the reassurance machine in
register('alo-date', lambda: para('Then there are people you\'re just getting to know.'),
         lambda: dnote('alo-date-b', '54, 4 and 6: his "If the real reason you\'re asking someone out is to prove you\'re lovable, or that you\'re sure what you want, then they\'ve become part of the test." is out, since When Healing Turns Into Checking has the date among its examples now, and the guide\'s "Another person is not a diagnostic instrument or reassurance machine. Healthy support and mutual co-regulation are part of relationships, and in a crisis getting a safe human involved can be exactly the right move." is merged in, with "if you need them to prove you\'re lovable" keeping the test he named.', 'ALODATE') + draft('alo-date-b'))

# 45: his qualification of the Higher Self line, and the Guide as its analog, from his notes
IFS_NO_USE = " I have no use for another neo-Advaita, [spiritual-bypassing](https://goenka.u-dont-exist.com/) claim that a perfect Higher Self is already waiting underneath everything."
register('ifs', lambda: (lambda p: p if p and IFS_NO_USE in p else None)(para('Can\'t find a calm, compassionate Self in there?')),
         lambda: para('Can\'t find a calm, compassionate Self in there?').replace(IFS_NO_USE, '') + '\n\n'
         + dnote('ifs-hs-b', '45 ("all that is ai paraphrasing me, but i\'d qualify the "no use" part"): his notes, as he asked ("obv that\'s not the prose for the guid exactly but maybe yopu can build from that"), in place of "I have no use for another neo-Advaita, spiritual-bypassing claim that a perfect Higher Self is already waiting underneath everything." (the spiritual-bypassing link kept): his own experience of the Higher Self perspective, a vantage point with no specific wisdom of its own, both ways in the guru types, and Anthony de Mello as his example (Wikipedia\'s page, opened 2026-10-18: Indian Jesuit priest and psychotherapist, stories from Christian, Sufi, Hindu and Buddhist sources).', 'IFSHS') + draft('ifs-hs-b')
         + '\n\n' + dnote('ifs-guide-b', '45: the rest of his notes: the inner Guide as the analog of the Higher Self, after the Nurturer and Protector, never a transcendent dismissive authority; most inner child therapy short on the Guide; IFS as more than one system, with branches and disputes. 45, D: the guide\'s "A trustworthy adult function is built through care, boundaries, action, and direction." stays out.', 'IFSGUIDE') + draft('ifs-guide-b'))

# His pointer to the schema therapy research ("we can mention that before the IFS section"): a short h2 before IFS
register('st', '\n## How This Relates to IFS\n',
         lambda: '\n## How This Relates to Schema Therapy\n\n'
         + dnote('st-a', 'his message ("you were sent info on schema therapy and how it overlaps with my guide in many places, so we can mention that before the IFS section"): the research suggestion of 2026-10-18 (UDA branch chat/guide-schema-therapist-fit-20261018, suggested-fixes/joel-articles/2026-10-18-schema-therapist-fit-and-reparenting-guide.md, from innerSignalGraph\'s research Pass 15), checked against ISST\'s Limited Reparenting page (George Lockwood, opened 2026-10-18: "the heart of the treatment in schema therapy"; warmth, nurturance, firmness, playfulness and limit-setting; the patient internalizes it as a healthy adult mode; the Vulnerable Child; fighting punitive parent modes). His Teachers line says the rest ("Filter for Schema Therapy, since that\'s the one with the most similarity to my guide").', 'ST') + draft('st-a')
         + '\n\n' + dnote('st-b2', 'the research\'s differences, as the ones that depend on the therapist (one adult with three jobs and borrowing one; practical safety now; no images as proof), and its screening questions compressed to the two the article\'s readers need. The guide\'s no to the inner-child frame isn\'t among them: he cut it on 2026-10-08.', 'STB') + draft('st-b2')
         + '\n\n## How This Relates to IFS\n')


# The grounding check of turn 71 had flagged "like ... and so on" for opening the guide's closed list of ten (COLD-READ-t71-appendix.md, passage E)
register('rcw-list',
         "Later revisions also compare notes with other approaches, like schema therapy, compassion-focused therapy, attachment repair, motivational interviewing, mentalizing, metacognitive therapy, behavioral activation, radically open DBT, emotion-focused therapy, spiritually integrated psychotherapy and so on.",
         "Later revisions also compare notes with schema therapy, compassion-focused therapy, attachment repair, motivational interviewing, mentalizing, metacognitive therapy, behavioral activation, radically open DBT, emotion-focused therapy and spiritually integrated psychotherapy.")


# --- Round b: the four drafts that read AI in round a, again, and my own sentences from the filler sweep -------------

register('bg-out-2', lambda: para('And if the grown-up you is there, and it'),
         lambda: para('And if the grown-up you is there, and it') + '\n\n' + dnote('bg-out-c', '54, 8, B ("humanize that in before you try to go deep") and 10 ("that\'s what we are putting back into 8"): the guide\'s "If you cannot reliably stop, return, stay oriented, or inward attention itself is making things worse, stop the inner exercise and come outward first." with "One breath may be enough." and the eyes-open hello as the gentler way back in. Round t72a\'s bg-out-b read AI alone (1.00), https://www.pangram.com/history/1fa68500-e6a9-46e0-b4ed-9f915b19cb94.', 'BGOUT') + draft('bg-out-c'))

register('yb5-2', lambda: para('So how were the next few days?'),
         lambda: dnote('yb5-c', '54, 8: "If you\'re getting worse, though, change several things at once, and get some support." is out ("that sounds too vague to be useful"); the paragraph is otherwise as it was.', 'YB5') + draft('yb5-c')
         + '\n\n' + dnote('yb6-c', '54, 11, B ("original list more informative"): the guide\'s "Try shorter duration, less depth or imagery, better timing, more symbolic or indirect representation, eyes open or stronger external anchors, less isolation, and more support." as a paragraph of its own. Round t72a\'s yb5-b, the list inside the paragraph, read AI alone (0.94), https://www.pangram.com/history/43936887-847b-446e-8094-8d5e4afde4b2.', 'YB6') + draft('yb6-c'))

register('st-2', '\n## How This Relates to IFS\n',
         lambda: '\n## How This Relates to Schema Therapy\n\n'
         + dnote('st-c', 'his message ("you were sent info on schema therapy and how it overlaps with my guide in many places, so we can mention that before the IFS section"): the research suggestion of 2026-10-18 (UDA branch chat/guide-schema-therapist-fit-20261018, suggested-fixes/joel-articles/2026-10-18-schema-therapist-fit-and-reparenting-guide.md, from innerSignalGraph\'s research Pass 15), checked against ISST\'s Limited Reparenting page (George Lockwood, opened 2026-10-18: "the heart of the treatment in schema therapy"; warmth, nurturance, firmness, playfulness and limit-setting; the patient internalizes it as a healthy adult mode; the Vulnerable Child; fighting punitive parent modes). His Teachers line says the rest ("Filter for Schema Therapy, since that\'s the one with the most similarity to my guide"). Round t72a\'s st-a read AI Detected alone (0.43), https://www.pangram.com/history/756f554c-31af-4866-8795-46c5b40cf144.', 'ST') + draft('st-c')
         + '\n\n' + dnote('st-e', 'the research\'s differences that depend on the therapist (one adult with three jobs and borrowing one; practical safety now; images and feelings no evidence about childhood), in his first person; its screening questions are left to his Teachers paragraph. The guide\'s no to the inner-child frame isn\'t among them: he cut it on 2026-10-08. Round t72a\'s st-b2 read AI alone (0.97), https://www.pangram.com/history/b733c68e-eaeb-4254-82f1-14cd899db6b9.', 'STB') + draft('st-e')
         + '\n\n## How This Relates to IFS\n')

register('ifs6', lambda: para('Before choosing a therapist, get to know the strengths'),
         lambda: dnote('ifs6-a', 'the filler sweep (JUNK-SWEEP.md, 24): "Could an IFS therapist help? They may, if they\'re skilled and grounded." is true of any therapist, so the paragraph goes straight to what makes one helpful.', 'IFS6') + draft('ifs6-a'))

register('jl', lambda: para('This one works best on a steadier day'),
         lambda: dnote('jl1-a', 'the filler sweep (JUNK-SWEEP.md, 15): "With that many people feeling the same thing, the theory that you\'re the defective one gets kind of hard to keep up." moves up from P2 to the step it belongs to, after "and wanting it to stop, just like you."', 'JL') + draft('jl1-a'))
register('jl2', lambda: para("If you've tried Pema Chödrön's"), lambda: draft('jl2-a'))

register('som', lambda: para('Rumi says you have to keep breaking your heart'),
         lambda: dnote('som-a', 'the filler sweep (JUNK-SWEEP.md, 17): "That describes what they feel, and it doesn\'t prove how the body produces it." is out: the paragraph never says how the body produces anything, and "doesn\'t prove" is the hedge he named on 2026-10-18 (O43).', 'SOM') + draft('som-a'))

register('cs5', lambda: para('Sometimes the session itself goes really well.'),
         lambda: dnote('cs5-c', 'the filler sweep (JUNK-SWEEP.md, 12): "and once isn\'t proof you\'ve got it all down" is out, a second hedge on a point nobody makes (O43).', 'CS5') + draft('cs5-c'))

register('tf11', lambda: para('Daniel Kahneman and Gary Klein came at intuition'),
         lambda: dnote('tf11-l', 'the filler sweep (JUNK-SWEEP.md, 11): "Yours too, probably." is out (a quip telling the reader what nobody doubts).', 'TF11') + draft('tf11-l'))


# --- Round c -----------------------------------------------------------------------------------------------------------
for _s in ('bg-out-d', 'bg-out-e', 'bg-out-f'):
    register('bg-out-' + _s[-1] + '3', lambda: para('And if the grown-up you is there, and it'),
             (lambda s: lambda: para('And if the grown-up you is there, and it') + '\n\n' + dnote(s, '54, 8, B ("humanize that in before you try to go deep") and 10 ("that\'s what we are putting back into 8"): the guide\'s "If you cannot reliably stop, return, stay oriented, or inward attention itself is making things worse, stop the inner exercise and come outward first." with "One breath may be enough." and the eyes-open hello as the gentler way back in. Rounds t72a and t72b\'s versions read AI alone (1.00, 0.999).', 'BGOUT') + draft(s))(_s))

for _a, _b in (('yb5-d', 'yb6-d'), ('yb5-d', 'yb6-e')):
    register('yb5-3' + _b[-1], lambda: para('So how were the next few days?'),
             (lambda a, b: lambda: dnote(a, '54, 8: "If you\'re getting worse, though, change several things at once, and get some support." is out ("that sounds too vague to be useful"), and the paragraph asks what you\'d change; without any last line it read AI alone (round t72b, 0.83).', 'YB5') + draft(a)
              + '\n\n' + dnote(b, '54, 11, B ("original list more informative"): the guide\'s "Try shorter duration, less depth or imagery, better timing, more symbolic or indirect representation, eyes open or stronger external anchors, less isolation, and more support." as the answer.', 'YB6') + draft(b))(_a, _b))

register('st-3', '\n## How This Relates to IFS\n',
         lambda: '\n## How This Relates to Schema Therapy\n\n'
         + dnote('st-c', 'his message ("you were sent info on schema therapy and how it overlaps with my guide in many places, so we can mention that before the IFS section"): the research suggestion of 2026-10-18 (UDA branch chat/guide-schema-therapist-fit-20261018, suggested-fixes/joel-articles/2026-10-18-schema-therapist-fit-and-reparenting-guide.md, from innerSignalGraph\'s research Pass 15), checked against ISST\'s Limited Reparenting page (George Lockwood, opened 2026-10-18: "the heart of the treatment in schema therapy"; warmth, nurturance, firmness, playfulness and limit-setting; the patient internalizes it as a healthy adult mode; the Vulnerable Child; fighting punitive parent modes). His Teachers line says the rest ("Filter for Schema Therapy, since that\'s the one with the most similarity to my guide").', 'ST') + draft('st-c')
         + '\n\n' + dnote('st-h', 'the research\'s differences that depend on the therapist (one adult with three jobs and borrowing one; practical safety now; images and feelings no evidence about childhood), in his first person. The guide\'s no to the inner-child frame isn\'t among them: he cut it on 2026-10-08.', 'STB') + draft('st-h')
         + '\n\n## How This Relates to IFS\n')
register('st-4', '\n## How This Relates to IFS\n',
         lambda: '\n## How This Relates to Schema Therapy\n\n' + dnote('st-c', 'as st-3, with its first paragraph only.', 'ST') + draft('st-c') + '\n\n## How This Relates to IFS\n')
register('ifs6-2', lambda: para('Before choosing a therapist, get to know the strengths'),
         lambda: dnote('ifs6-b', 'the filler sweep (JUNK-SWEEP.md, 24): "Could an IFS therapist help? They may, if they\'re skilled and grounded." is true of any therapist; the paragraph now asks which kind, and says what makes each the better fit.', 'IFS6') + draft('ifs6-b'))


# --- Round e: in his One Intention voice (E194: "rewrite it in that voice, with the content kept and the steps turned into
# scenes, asides and jokes, before trying another arrangement of the same instructions") ------------------------------
BG2 = 'And if the grown-up you is there, and it'
for _x in 'abc':
    register('bg2' + _x, lambda: para(BG2),
             (lambda s: lambda: dnote(s, '54, 8, B ("humanize that in before you try to go deep") and 10 ("that\'s what we are putting back into 8"): the guide\'s "If you cannot reliably stop, return, stay oriented, or inward attention itself is making things worse, stop the inner exercise and come outward first.", with "could you stop and return" as its question, in P2 right after "I\'d go shallower.", where the guide has it (just before "Do not test another inward technique just to prove you can tolerate something."). As a paragraph of its own it read AI fourteen times (turns 34, 38 and 72).', 'BG2') + draft(s))('bg2-' + _x))

for _a, _b in (('yb5-e', 'yb6-g'), ('yb5-f', 'yb6-h'), ('yb5-g', 'yb6-i')):
    register('yb56' + _a[-1], lambda: para('So how were the next few days?'),
             (lambda a, b: lambda: dnote(a, '54, 8: "If you\'re getting worse, though, change several things at once, and get some support." is out ("that sounds too vague to be useful"; coming out first is in Before You Try to Go Deep P2 now), and the questions get scenes the way his One Intention answers its own (E194).', 'YB5') + draft(a)
              + '\n\n' + dnote(b, '54, 11, B ("original list more informative"): the guide\'s "Try shorter duration, less depth or imagery, better timing, more symbolic or indirect representation, eyes open or stronger external anchors, less isolation, and more support.", packed the way his One Intention packs its list (with a catch-all), and one item played out.', 'YB6') + draft(b))(_a, _b))

HON = "And reaching out doesn't mean telling strangers everything."
for _x in 'ac':
    register('hon' + _x, lambda: para(HON),
             (lambda s: lambda: dnote(s, 'his section moves put a 67-word AI window on this paragraph, my C2 of turn 38 (round t72c, https://www.pangram.com/history/63c1d7da-6554-470e-859a-58b5571b9020), so "how they handle the smaller things you tell them" gets a scene; the rest is as it was.', 'HON') + draft(s))('alo-hon-' + _x))

TY_NOTE = ('the filler sweep (JUNK-SWEEP.md, 2): the Tyler sentence moves from P6, which is on tone of voice, to the end of P5, after the line we came up with, and "it meant a lot to me that he liked" becomes his own words of 2026-09-27 16:29 ("the fact that he really appreciated how I was interpreting Jesus\' message is pretty important to me"), since "it meant something that" is the phrasing he named on 2026-10-18 (E193).')
register('tyler', lambda: para('But Jesus also said to take the log out'), lambda: dnote('wi5-a', TY_NOTE, 'TY') + draft('wi5-a'))
register('tyler', lambda: para("It's also how your voice sounds, though."), lambda: draft('wi6-a'))


# --- Round f -----------------------------------------------------------------------------------------------------------
# Only When the Present-Day Adult Is Dangerous to the Child moves (after When Healing Turns Into Checking): round t72e's
# moved-order checks all had AI windows in Your Body Might Need Some Love First P3 to P5 once it no longer followed
# You Don't Need an Inner Monologue.
def _dmove_old():
    b = _blocks()
    return None if b is None else b[0]


def _dmove_ins_new():
    if _blocks() is None:
        return None
    danger = _blocks()[0]
    moved = note('his section move: When the Present-Day Adult Is Dangerous to the Child goes after When Healing Turns Into Checking ("both of those to me are less likely to be important for most people compared to the other sections"). Its text is unchanged. You Don\'t Need an Inner Monologue stays where it was for now: with it moved too, every version had an AI window in Your Body Might Need Some Love First P3 to P5 (round t72e).')
    return '\n' + moved + danger + BORROW_H


register('dmove-out', _dmove_old, '')
register('dmove-in', _move_ins_old, _dmove_ins_new)

# 45, my wording of his "most inner child therapy does not sufficiently address the Guide": "doesn't do much with the
# Guide at all" said more than he did
register('ifsg', lambda: para('So inner child therapy draws on those higher vantage points'),
         lambda: dnote('ifs-guide-c', '45: his "most inner child therapy does not sufficiently address the Guide ... so it can go in the oppoosite extreme from IFS" was "doesn\'t do much with the Guide at all, which is the opposite problem" in my first wording (installed in round t72c), more than he said; now "doesn\'t do enough with the Guide, which is the opposite extreme".', 'IFSG') + draft('ifs-guide-c'))


# --- Round g: the guide's list inside P5's own sentence, and the vague last sentence out (54, 8 and 11) ---------------
for _x in 'hik':
    register('yb5' + _x, lambda: para('So how were the next few days?'),
             (lambda s: lambda: dnote(s, '54, 8 ("we can remove the "change several things at once" version in the other section since that sounds too vague to be useful"; coming out first is in Before You Try to Go Deep P2 now) and 11, B ("original list more informative"): the guide\'s "Try shorter duration, less depth or imagery, better timing, more symbolic or indirect representation, eyes open or stronger external anchors, less isolation, and more support." inside the paragraph\'s own "a bit easier" sentence, with the rest as it was. As a paragraph of its own, or inside P5 with scenes, it read AI in all eight versions (rounds t72a to t72e).', 'YB5') + draft(s))('yb5-' + _x))


# --- Round h: the checking-into-doing paragraph without its list (it had a 37-word AI window in three h1 contexts) -----
register('chkf', lambda: para('And the checking doesn\'t always stay in your head.'),
         lambda: dnote('chk-beh-f', '54, 4 (as chk-beh-a, round t72d), with its list of five broken up: it had a 37-word AI window in three checks of Before You Try to Go Deep this turn (rounds t72e, t72f and t72g).', 'CHKF') + draft('chk-beh-f'))


# --- Round i: checking-into-doing folded into P2 (folding is what got coming out first in, round t72e) ----------------
def _chk_pair():
    t = ART.read_text(encoding='utf-8')
    a = para('Going back can still matter, since realizations')
    b = para('And the checking doesn\'t always stay in your head.')
    if a is None or b is None:
        return None
    i, j = t.index(a), t.index(b)
    return t[i:j + len(b)]


register('chkm', _chk_pair,
         lambda: dnote('chk-merge-a', '54, 4: the checking-into-doing paragraph (chk-beh-a, round t72d) folded into P2 after "is clearly not what we\'re after here.", word for word: on its own it had a 37-word AI window in three checks of Before You Try to Go Deep (rounds t72e to t72g).', 'CHKM') + draft('chk-merge-a'))
