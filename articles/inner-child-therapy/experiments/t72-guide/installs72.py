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
    return b[2]


def _move_ins_old():
    return None if _blocks() is None else '\n' + BORROW_H


def _move_ins_new():
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
