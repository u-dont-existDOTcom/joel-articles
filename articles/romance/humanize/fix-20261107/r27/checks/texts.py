"""r27's check texts (2026-11-08): his T2 answer for Jealousy 366 to 370 in its section, and S17's section with the
doubled "example" he caught taken out. Built from r26's and r21's check texts; the edits are listed in EDITS."""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parents[1]

# His version of 366 to 370 (ANSWERS-T2.json, TEACH-JEALOUSY-POLY), as the post will render it (the link's words only),
# with the three slips the word-for-sense read found (EDITS).
HIS = [
    'I do believe two people can choose sexual exclusivity honestly. They can admit that attraction to other people '
    'exists and decide not to act on it each day. And even better than simply suppressing it, I agree with Esther Perel, '
    'who writes that this sexual energy felt outside the relationship can be used and redirected into the relationship '
    'to make it more alive.',
    'Imagine if you and your partner both saw those outside attractions as beneficial energy sources rather than a threat '
    'to your relationship. It sure would beat beating around the bush because of fear and jealousy. You can start '
    'playing around with opening up about the minor, momentary attractions, rather than wait in hiding until a serious '
    'crush is dramatically confessed.',
    'Lots of couples promise forever to each other and nobody else. Look around at how many actually live that way. On '
    'the other hand, in a polyamorous relationship, the boundaries might be more negotiable, but then somebody has to sit '
    "down and negotiate them, down to who gets to stay the night. That can end up sometimes creating more drama than it's "
    'worth.',
    'Polyamory can also be a way of escaping deeper intimacy, like my one poly college friend who boasted about having 4 '
    'girlfriends, but admitted to me that he felt deeply unhappy. Or it can be a way of escaping guilt, like when someone '
    'keeps cheating until they finally "come out of the closet" as poly, as if that solves their prior dishonesty. But '
    'they are right to finally come clean and hopefully avoid that dishonesty in future.',
    "I learned most of this by screwing it up. Some of it I just thought through, and I'm still not sure about all of it.",
]
EDITS = [
    ('366', '"And even better simply suppressing it" -> "And even better than simply suppressing it"', 'a word missing'),
    ('369', '"Polyamory can also be a way of escaping deeper intimacy, too," -> "... deeper intimacy,"',
     '"also" and "too" both said, the same slip as "example" said twice'),
    ('370', 'curly apostrophe in "I’m" straightened', 'his standing swap (curly quote marks read as AI to him)'),
    ('S17 (#118 section)', '"the example couple I really liked as an example" -> "the couple I really liked as an example"',
     'his correction, 2026-11-08 15:07 UTC'),
    ('S17 (#118 section)', '"strengthens the pelvic-floor" -> "strengthens the pelvic floor"', 'a noun, not a modifier'),
]

jeal = (FIX / 'r26' / 'checks' / 'CHECK-r26-jeal.txt').read_text(encoding='utf-8').split('\n\n')
cut = next(i for i, p in enumerate(jeal) if p.startswith('I do believe two people'))
spir = (FIX / 'r21' / 'checks' / 'CHECK-r21-spir.txt').read_text(encoding='utf-8')
assert spir.count('the example couple I really liked as an example') == 1 and spir.count('the pelvic-floor') == 1
spir = spir.replace('the example couple I really liked as an example', 'the couple I really liked as an example')
spir = spir.replace('the pelvic-floor', 'the pelvic floor')

TEXTS = {
    'r27-jeal': '\n\n'.join(jeal[:cut] + HIS).strip(),
    'r27-spir': spir.strip(),
}

# The fresh sense read (whole/sense-r27) found 366's comparison with nothing to attach to ("even better than simply
# suppressing it, I agree with ..."). The fix put to him, tested here as r27-jeal-b; the fixed version keeps his words
# until he says yes.
FIX_366 = ('And even better than simply suppressing it, I agree with Esther Perel, who writes',
           'And even better than simply suppressing it, they can put it to work. I agree with Esther Perel, who writes')
assert TEXTS['r27-jeal'].count(FIX_366[0]) == 1
TEXTS['r27-jeal-b'] = TEXTS['r27-jeal'].replace(*FIX_366)


# The fresh reader's needed read (2026-11-08) asked for 145's "It" to name what it points at (the exaggerated
# director/muse dynamic) and found 147's bracketed "(although it's not one)" said nothing "almost like" didn't: cut.
# Idealization (143 to 151): #132 read it Human with five Low windows, on 145's two short sentences, 147's second
# sentence, 148's first two and 151's last two. Fixed his way (gate E368): 145's two sentences joined with a reason
# ("since"); 147's two sentences joined and its aside put in brackets, the way he does ("(to me, anyway)"); 148's hedges
# ("can go", "can find") said as what happens, its term ("splitting") shown by the flip it names, "evidence" said
# plainly; 151's "Sure." (an owner ban as a sentence) said as what he'd do, with its reason ("since"), and "still matter
# to me" (a tell, O50) said as "still care about them".
IDEAL = (FIX / 'r24' / 'checks' / 'CHECK-r24-ideal.txt').read_text(encoding='utf-8').strip()
IDEAL_EDITS = [
    ('It shouldn’t have to happen that way, though. It’s a bad shortcut to the divine archetypes.',
     'That exaggerated version shouldn’t have to happen, though, since it’s a bad shortcut to the divine archetypes.'),
    ('The degree of idealization also predicts the degree of demonization for me. I don’t mean it as a clinical '
     'diagnosis, but I do use it almost like one in my own life.',
     'The degree of idealization also predicts the degree of demonization for me, so much that I use it almost like a '
     'clinical diagnosis in my own life.'),
    ('When the BPD splitting happens, she can go from worshipping me to hating me, first in private and then in front of '
     'everybody. Suddenly she can find plenty of flaws, and all of them become evidence I was faking it all along.',
     'When the BPD splitting happens, she flips from worshipping me to hating me, first in private and then in front of '
     'everybody. Suddenly she finds plenty of flaws, and to her, each one means I was faking it all along.'),
    ('“Can you talk less about your exes?” Sure. Maybe I do talk about them too much sometimes, but they still matter to '
     'me. If I’m supposed to listen to everything on her mind, I don’t want to have to pretend they aren’t on mine.',
     '“Can you talk less about your exes?” I’m happy to, since maybe I do talk about them too much sometimes. But I still '
     'care about them, and if I’m supposed to listen to everything on her mind, I don’t want to pretend they aren’t on '
     'mine.'),
]
t = IDEAL
for a, b in IDEAL_EDITS:
    assert t.count(a) == 1, a[:40]
    t = t.replace(a, b)
TEXTS['r27-ideal'] = t

# r27-ideal (#138) read 14% AI: 147 now High, but AI Low on 148's first two sentences and on 151's last, Human Low on
# 145 with 146's opener and on 148's last. Diagnosis: what's left is mine said in neat, mirrored shapes ("first in private
# and then in front of everybody", "on her mind ... on mine") and abstract claims ("a bad shortcut to the divine
# archetypes"), the S2 pattern his versions fixed with particular things and his register (romance-2026-11-07a, d). So:
# 145 says who needs what (she, a knight, that beauty); 148 says what she says, in quotes, as 147 does; 151 ends slack and
# casual ("gonna", "sometimes too"). Checked as the section and each paragraph alone (E343).
IDEAL_B = [
    ('That exaggerated version shouldn’t have to happen, though, since it’s a bad shortcut to the divine archetypes.',
     'She shouldn’t need a knight in shining armor to bring that beauty out, though, because it’s a bad shortcut to the '
     'divine archetypes.'),
    ('When the BPD splitting happens, she flips from worshipping me to hating me, first in private and then in front of '
     'everybody. Suddenly she finds plenty of flaws, and to her, each one means I was faking it all along.',
     'When the BPD splitting kicks in, she goes from “you’re perfect” to “you’re a fraud,” first in private and then in '
     'front of everybody. Suddenly she can see every flaw I have, and decides I was faking it all along.'),
    ('But I still care about them, and if I’m supposed to listen to everything on her mind, I don’t want to pretend they '
     'aren’t on mine.',
     'But I still care about them, and if I’m gonna listen to everything on her mind, she’s gonna have to hear about '
     'mine sometimes too.'),
]
t = TEXTS['r27-ideal']
for a, b in IDEAL_B:
    assert t.count(a) == 1, a[:40]
    t = t.replace(a, b)
TEXTS['r27-ideal-b'] = t
_p = t.split('\n\n')
TEXTS['r27-p145'] = next(p for p in _p if p.startswith('She shouldn’t need a knight'))
TEXTS['r27-p148'] = next(p for p in _p if p.startswith('When the BPD splitting'))
TEXTS['r27-p151'] = next(p for p in _p if p.startswith('If she says, “Can you talk less'))

# The compare read of r27-ideal-b beside the live words (whole/compare-r27, F1.4, severity 2): 151's ending turned his
# boundary ("I don't want to have to pretend that isn't on mine") into a demand ("she's gonna have to hear about mine"),
# and "mine" could be read as his exes. Said as his boundary, first, with its reason trailing: r27-ideal-c.
OLD151C = ('But I still care about them, and if I’m gonna listen to everything on her mind, she’s gonna have to hear about '
           'mine sometimes too.')
NEW151C = ('But I still care about them, and I’m not gonna act like they never cross my mind, not when I’m listening to '
           'everything on hers.')
assert TEXTS['r27-ideal-b'].count(OLD151C) == 1
TEXTS['r27-ideal-c'] = TEXTS['r27-ideal-b'].replace(OLD151C, NEW151C)
