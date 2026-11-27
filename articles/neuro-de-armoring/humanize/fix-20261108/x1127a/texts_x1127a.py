#!/usr/bin/env python3
"""His answers of 2026-11-27 15:45 UTC (fix-20261108/joel-20261127-1545-message.txt): "73 a  but i also can't recommend
starting them 74 b". Questions 73 and 74 (OWNER-QUESTIONS.md) came from the fresh readers of his own versions last turn
(x1126c/v1/fit/lma, x1126c/v1/fit/prec).

73a: the herbs warning says what to watch for, the way his agmatine paragraph does ("stop it right away if you notice
you're flatter"), "... so if you take either, stop it if you notice you feel less pleasure or desire than before", and
glosses "anhedonia (little pleasure or desire)". His line "but i also can't recommend starting them" is fitted where it
answers the reader's question: the first sentence, whose "I'm not advising" a reader who already takes lion's mane
couldn't read as "stop" or "don't start". So the paragraph now opens on not starting and ends on when to stop, which
covers both readers (one who takes either already, and one who starts anyway). "If you take either" stays as question
73a had it, without "already", since the stop sign holds for anyone taking them.

74b: "concurrently with" becomes "on the same day as" in his Precautions. The sub-question in 74 (add "and ask your
doctor first" after "Use with extreme caution") had no letter and he didn't pick it, so his "Use with extreme caution"
stays word for word.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
OLD = json.loads((HERE / 'OLD-X1127A.json').read_text(encoding='utf-8'))


def plain(s):
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)
    s = re.sub(r'(?<![\w*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![\w*])', r'\1', s)
    return s.replace('**', '')


def change(k, *pairs):
    t = OLD[k]
    for a, b in pairs:
        assert t.count(a) == 1, (k, a)
        t = t.replace(a, b)
    return t


NEW = {
    'lma': change('lma',
                  ("I'm not advising lion's mane or ashwagandha,", "I can't recommend starting lion's mane or "
                   "ashwagandha,"),
                  ('anhedonia (no desire)', 'anhedonia (little pleasure or desire)'),
                  ("so it's something to keep in mind.", 'so if you take either, stop it if you notice you feel less '
                   'pleasure or desire than before.')),
    'prec': change('prec', ('Do not use agmatine concurrently with', 'Do not use agmatine on the same day as')),
}
# What the first fresh readers read (v1): 73a's words as question 73 gave them.
READ1 = dict(NEW)

# The sense fixes to my words of 73a, from the v1 reads (his own sentences are left as they are; their marks go to him):
#  - "if you take either" came right after "SSRIs and finasteride", so a quick reader could take "either" as those two
#    drugs (his-fixes S2, way 10): "either herb", as his way names the thing;
#  - "if you take either, stop it if you notice" stacked two ifs (his-fixes S2, way 8): one condition, then the act, as
#    his agmatine paragraph has it ("so stop it right away if you notice ...");
#  - "than before" had no before for a reader already on lion's mane (fit S2, CAN'T TELL): "since you started it", the
#    baseline his agmatine paragraph uses ("than before you started");
#  - the stop sign named only pleasure and desire, while his first sentence also names sexual dysfunction (needed S2,
#    his-fixes S2 way 7): "or any sexual problems" added, which widens 73a's stop sign to the second effect his sentence
#    names, so it goes to him as question 75 (my pick: keep it).
LMA_END_73A = 'so if you take either, stop it if you notice you feel less pleasure or desire than before.'
LMA_END_2 = ('so if you take either herb and notice less pleasure or desire, or any sexual problems, since you started '
             'it, stop taking it.')
assert NEW['lma'].count(LMA_END_73A) == 1
NEW['lma'] = NEW['lma'].replace(LMA_END_73A, LMA_END_2)

# The second reads (v2, of the text with LMA_END_2): the fit reader still took his "sexual dysfunction long after they
# stop taking them" as if stopping brings the problems on, which matters more now that the paragraph ends on "stop
# taking it" (v2/fit/lma S1); "that last" says they start while taking them and last after. It is a word in his own
# sentence, so it goes to him with "or any sexual problems" as question 75 (my pick: keep both). The v2 reads' other
# marks are on his own words (his-fixes S1 "they" two ways, S2 "it's the same kind of thing") or can't be fixed with
# words (a reader long on lion's mane has no before to compare with), and are named in the report.
LMA_S1_A = 'and sexual dysfunction long after they stop taking them.'
LMA_S1_B = 'and sexual dysfunction that last long after they stop taking them.'
assert NEW['lma'].count(LMA_S1_A) == 1
NEW['lma'] = NEW['lma'].replace(LMA_S1_A, LMA_S1_B)

# The order the two go in the article: the herbs warning, the agmatine warning, then the Precautions.
ORDER = ['lma', 'prec']

if __name__ == '__main__':
    for k in ORDER:
        print('==', k, len(plain(NEW[k]).split()), 'words')
        print(NEW[k])

# ---- Tries after checks-1127a. The Precautions with 74b read Human Written, one window, High
# (https://www.pangram.com/history/df64f39b-0778-436c-a650-efe5d3bfbda5): it goes in as it is. The herbs warning
# (LMA-73A) read AI Generated, 100%: AI Medium over its first sentence, AI Low over its second
# (https://www.pangram.com/history/666f323c-0200-4f4f-a54e-be84150a350b); the fold before it read Human High in one
# window. Diagnosis: what I added made his rough, spoken paragraph a tidy one. The stop sign was a built conditional
# ("if you take either herb and notice A, or B, since C, stop D"), a checklist in one clause, and "that last" smoothed his
# own "long after they stop taking them". Try 2 keeps his first sentence as his line and 73a made it (no "that last"),
# and says the stop sign the way he says advice: "I'd" (as his agmatine paragraph's "I wouldn't push through that
# signal"), "the moment you notice", and his own baseline "than before you started" (his agmatine paragraph). "Already"
# answers the fit readers' "is this about me" (v1, v2) after "can't recommend starting".
TRY = {}
TRY['lma-2'] = change('lma',
                      ("I'm not advising lion's mane or ashwagandha,", "I can't recommend starting lion's mane or "
                       "ashwagandha,"),
                      ('anhedonia (no desire)', 'anhedonia (little pleasure or desire)'),
                      ("so it's something to keep in mind.", "so if you're already taking either herb, I'd stop the "
                       "moment you notice less pleasure or desire than before you started, or any sexual problems."))

# Try 2 read AI Detected, 76%: AI-Assisted Low over the first sentence, AI-Generated Low over the second
# (https://www.pangram.com/history/f3417de9-5888-4720-adc1-66303c140dab), better than try 1 (100%) but no Human window.
# Its second AI read sent it to the tell panel (panel-lma-t2/PANEL.md, three readers): agreed on both sentences. What
# they agree on that is mine: the stop sign repeats the first sentence's two symptoms in the same order ("less pleasure or
# desire than before you started, or any sexual problems", a closing-the-loop echo), "I can't recommend" reads as an
# assistant declining, and the measured gloss "(little pleasure or desire)". What they agree on that is his ("even though
# they're popular herbs", "some people report", "are rare, but it's the same kind of thing", "Post-ashwa") stays: his
# words go to him first, and they read High in the fold. Try 3: his own opening for his line ("I'm not advising anyone to
# start", the meaning of "i also can't recommend starting them"); the gloss as bluntly as his "(no desire)" was, with
# pleasure in it as 73a asks ("(no pleasure or desire)": an-hedonia, no pleasure); and the stop sign points back at what
# the first sentence names instead of repeating it ("notice any of that starting, I'd quit it"), which also says the
# problems start while taking the herb and covers both of them (question 75).
TRY['lma-3'] = change('lma',
                      ("I'm not advising lion's mane or ashwagandha,", "I'm not advising anyone to start lion's mane or "
                       "ashwagandha,"),
                      ('anhedonia (no desire)', 'anhedonia (no pleasure or desire)'),
                      ("so it's something to keep in mind.", "so if you're already on either herb and notice any of that "
                       "starting, I'd quit it."))

# Try 3 read AI Generated, 100%, one window AI High (https://www.pangram.com/history/a4917d66-e42f-4533-8713-e72d039f379c),
# worse than try 2, though its first sentence differs from the fold (Human High) only by "anyone to start" and the gloss.
# What all three tries share against the fold: a stop sign took the place of his slack ending ("so it's something to
# keep in mind"). His fixes end slack (lesson bad-trips-2026-11-07j); a warning that closes on a crisp instruction reads as
# a label's wrap-up (the panel's "standard cautionary wrap-up"). Try 4 keeps his two sentences as they read High, with
# only his line and 73a's gloss in them, and puts the stop sign after them as its own short sentence, in his first-person
# voice for advice ("I'd", as in "I wouldn't push through that signal"): "If I were already on either herb, I'd quit the
# day I noticed any of that." It points back at what the first sentence names instead of repeating it, and "either herb"
# keeps it from reading as SSRIs or finasteride.
TRY['lma-4'] = change('lma',
                      ("I'm not advising lion's mane or ashwagandha,", "I'm not advising anyone to start lion's mane or "
                       "ashwagandha,"),
                      ('anhedonia (no desire)', 'anhedonia (no pleasure or desire)'),
                      ("so it's something to keep in mind.", "so it's something to keep in mind. If I were already on "
                       "either herb, I'd quit the day I noticed any of that."))

# Try 4 read AI Detected, 96%, in three windows (https://www.pangram.com/history/35b9a7c1-f6cb-4de9-8424-82b918c1b4c9):
# his own second sentence, word for word as in the fold, read AI Low in a window of its own, his first (with his line
# and 73a's gloss) AI Low, my third sentence AI Medium. In the fold, his two sentences were one window, High. Four tries
# of W-LMA-73a each changed several things from the fold at once, so none says which change turns it. From here the
# near-miss rule's path: the fold's own lineage (W-LMA-his, the fold Human High, 1 of 6 tries), one or two words per
# check. Step 1: his line in his opening ("anyone to start") and 73a's gloss with pleasure in it, as bluntly as his "(no
# desire)"; his slack ending stays.
STEP = {}
STEP['lma-s1'] = change('lma',
                        ("I'm not advising lion's mane or ashwagandha,", "I'm not advising anyone to start lion's mane "
                         "or ashwagandha,"),
                        ('anhedonia (no desire)', 'anhedonia (no pleasure or desire)'))

# Step 1 read AI Detected, 39%: Human Low over the first sentence, AI Low over his own second sentence, word for word
# (https://www.pangram.com/history/d2357d72-aa6f-4a8c-9ff1-ab3e53ac084b). Two small changes turned the fold's one High
# window into two. Step 2 takes one of them back: his line alone ("anyone to start"), the gloss as he had it, to see which
# of the two turns it (the one-change-per-check rule, which step 1 stretched to two).
STEP['lma-s2'] = change('lma', ("I'm not advising lion's mane or ashwagandha,", "I'm not advising anyone to start lion's "
                                "mane or ashwagandha,"))

# Step 2 (his line alone) read Mostly Human, 3% AI: Human Medium over the first sentence, Human Low over his second
# (https://www.pangram.com/history/e48fb85c-ea18-48c5-b61a-7066b4069dec), between the fold (one window, High) and step 1
# (Human Low, AI Low). So both small changes weaken his first sentence, and the gloss more: "I'm not advising lion's mane
# or ashwagandha" (advising a thing, not a person) is his own turn of phrase, and "anyone to start" makes it the standard
# sentence. Once his first sentence reads weaker, his second splits off into a window of its own and reads Low or AI.
# What his line asks for, the paragraph can say without touching his opening: "I'm not advising lion's mane or
# ashwagandha" already tells a reader not to take them, and what question 73's reader couldn't tell (whether to stop or
# only not start) is answered by a stop sign addressed to the reader already on one. Step 3: his first sentence as the
# fold had it, and 73a's stop sign in place of his slack ending, addressed to the reader already on either herb, in his
# voice ("I'd quit"), pointing back at what his first sentence names ("any of that").
STEP['lma-s3'] = change('lma', ("so it's something to keep in mind.", "so if you're already on either herb, I'd quit as "
                                "soon as you notice any of that."))

# Step 3 read Human Written, 0.0% AI: High over his first sentence, Medium over the second
# (https://www.pangram.com/history/2cd62104-8545-4d8c-ad06-c468ec2e4786). A near miss: the next steps change a word or
# two. What a reader could take two ways in the second sentence: "I'd quit as soon as you notice" (quit what, and who
# quits?): "I'd quit it", the herb. And 73a's gloss isn't in yet, which his rule asks for (never leave out a fix he
# asked for to get past Pangram): his "(no desire)" read as low sex drive alone (question 73), and the stop sign now
# points back at it ("any of that"), so a reader who takes it that way watches for the wrong thing. "(no pleasure or
# desire)" weakened the first sentence (step 1), so the gloss is said in plainer words, as bluntly as his: "(no joy or
# desire)". Two words, the near-miss rule's step.
STEP['lma-s4'] = change('lma', ('anhedonia (no desire)', 'anhedonia (no joy or desire)'),
                        ("so it's something to keep in mind.", "so if you're already on either herb, I'd quit it as soon "
                         "as you notice any of that."))

# Step 4 read Human Written, 0.0% AI: High over his first sentence, now with 73a's gloss in plain words, and Medium over
# the second (https://www.pangram.com/history/c785d020-2ff6-40d6-9ee7-669c1ca39a46): the gloss holds, and the second
# sentence's window is where it was. What stays the same in steps 3 and 4 is the stop sign's build, two clauses with two
# persons ("if you're already on either herb, I'd quit it as soon as you notice"), a templated advice. His own stop sign,
# in his agmatine paragraph two paragraphs down, which reads High, says it in one clause: "so stop it right away if you
# notice you're flatter". Step 5, the lineage's last try: his idiom, one clause, one "if", and "either herb" kept so it
# can't be read as the two drugs: "so stop either herb right away if you notice any of that."
STEP['lma-s5'] = change('lma', ('anhedonia (no desire)', 'anhedonia (no joy or desire)'),
                        ("so it's something to keep in mind.", 'so stop either herb right away if you notice any of '
                         'that.'))

# Step 5 read Human Written, 0.0% AI, one window, Medium (https://www.pangram.com/history/fef78872-dac8-438a-8377-5f03bfed1bf7):
# the stop sign in his idiom merged the paragraph back into one window, as the fold was, but at Medium. The paragraph has
# had nine checks this turn (W-LMA-73a 4, W-LMA-his 5), past the budget's six, so it goes to him as a teaching card
# (W-LMA-73A) with steps 3 to 5, my best, and the article keeps the fold until his answer.

# ---- His message of 2026-11-27 17:21 UTC (fix-20261108/joel-20261127-1721-message.txt): "76 yes, and that can be
# dangerous with non-kratom opioids where overdose is more of a concern but even with kratom you can get side effects
# when more sensitive." 76a: "(will reduce tolerance)" becomes "(it lowers your tolerance, so your usual dose can hit
# harder)"; his reason says what "harder" means for each: an overdose risk with opioids, side effects even with kratom.
# Fitted, the reason is too long for the bracket inside a sentence that already lists four kinds of drug, so it goes in
# a sentence of its own right after, and the bracket goes. The Precautions read High as 74b left them (#291), so the
# steps go from there, one piece a check (lesson neuro-2026-11-27a): 76a's bracket, then its overdose half, then the
# sentence with both halves.
P74 = NEW['prec']
PREC76 = {
    'a': P74.replace('(will reduce tolerance)', '(it lowers your tolerance, so your usual dose can hit harder)'),
    'b': P74.replace('(will reduce tolerance)', '(it lowers your tolerance, so your usual dose can hit harder, which '
                     'with opioids can mean an overdose)'),
    'c': P74.replace('opioids and/or kratom (will reduce tolerance), ', 'opioids and/or kratom, ').replace(
        " It's not recommended", " Agmatine lowers your tolerance to opioids and kratom, so your usual dose can hit harder, "
        "which with opioids can mean an overdose, and even with kratom you can get side effects once you're more "
        "sensitive. It's not recommended"),
}
for _k, _v in PREC76.items():
    assert _v != P74, _k
