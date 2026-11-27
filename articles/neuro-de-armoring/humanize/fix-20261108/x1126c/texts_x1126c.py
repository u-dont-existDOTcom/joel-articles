#!/usr/bin/env python3
"""His answer of 2026-11-26 23:30 UTC (fix-20261108/joel-20261126-2330-message.txt): "72a". Question 72 asked how the
labels in the warnings at the top should appear, after the section read Mostly Human (6% AI) and its five middle
warnings read AI together (90%), 28% with their labels off (x1126b, #253, #255, #256). 72a: fold each label into its
warning's first sentence, opening on the subject, with his nicknames kept in the sentence, for all of them so they
match; then fix The Rule's and agmatine's openings, and run the section's last check.

FOLD is step 1 for each warning: the label folded in, the fewest words changed. The disclaimer line ("CRITICAL MEDICAL
DISCLAIMER:") stays as the list's title; the uridine paragraph and the paragraph after the Cognitive Warning have no
label.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
OLD = json.loads((HERE / 'OLD-X1126C.json').read_text(encoding='utf-8'))


def plain(s):
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)
    s = re.sub(r'(?<![\w*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![\w*])', r'\1', s)
    return s.replace('**', '')


def fold(k, *pairs):
    t = OLD[k]
    for a, b in pairs:
        assert t.count(a) == 1, (k, a)
        t = t.replace(a, b)
    return t


FOLD = {
    'dmso': fold('dmso', ('DMSO Safety: This protocol has you smell DMSO', 'This protocol has you smell DMSO')),
    # not "This protocol has you" twice in a row, as the DMSO paragraph now opens that way
    'elec': fold('elec', ('Electrolytes: This protocol has you eating', 'You\'ll also be eating')),
    'ethno': fold('ethno', ('Ethnobotanicals: The plant medicines', 'The plant medicines')),
    'iso': fold('iso', ('Behavioral Warning (The Isolation Trap): This neural', 'This neural'),
                ('But don\'t isolate completely, because', 'But don\'t fall into the isolation trap of cutting yourself '
                 'off completely, because')),
    'rule': fold('rule', ('The Rule: Seek "Boring Love"', 'My rule for now is to seek "Boring Love"')),
    'cog': fold('cog', ('Cognitive Warning: As you de-armor', 'As you de-armor')),
    'lma': fold('lma', ('Lion\'s Mane & Ashwagandha: I\'m not advising either of these, even though',
                        'I\'m not advising lion\'s mane or ashwagandha, even though')),
    'agm': fold('agm', ('Agmatine Warning (The "Voltage Regulator"): Agmatine acts like a brake',
                        'Agmatine, the "voltage regulator", acts like a brake')),
    'prec': fold('prec', ('Precautions/Side Effects: Do not use concurrently with',
                          'Do not use agmatine concurrently with')),
    # and "it" named in the last sentence: a fresh reader of the fold took it as the list's drugs (v1/fit/htp)
    'htp': fold('htp', ('Uridine & 5-HTP Warning for Psychedelic Users: These two supplements are in this protocol',
                        'Uridine and 5-HTP are in this protocol'),
                ('Do not use it anywhere near iboga', 'Do not use 5-HTP anywhere near iboga')),
}

# What the fresh readers read (v1): the folds before the 5-HTP "it" was named.
READ = dict(FOLD)
READ['htp'] = fold('htp', ('Uridine & 5-HTP Warning for Psychedelic Users: These two supplements are in this protocol',
                           'Uridine and 5-HTP are in this protocol'))

# The paragraph after the Cognitive Warning (no label, unchanged): the Cognitive Warning is under 50 words, so it is
# checked with it, as PAIR-COG-FACES.
# (a snapshot as it stood before this turn, OLD-FACES-X1126C.txt, since the fourth run changed its first sentence)
FACES = (HERE / 'OLD-FACES-X1126C.txt').read_text(encoding='utf-8')

# Try 2 where the fold read below High by itself (checks-1126r): the Behavioral Warning (Human Medium over its third
# sentence, where the fold put his nickname, and over its last) and the Precautions (Human Low over its last two
# sentences, his, which have no subject once the label is gone).
FIRST = {'iso': ('Behavioral Warning (The Isolation Trap): This neural', 'This neural'),
         'prec': ('Precautions/Side Effects: Do not use concurrently with', 'Do not use agmatine concurrently with')}
TRY2 = {
    'iso-a': fold('iso', FIRST['iso'], ('But don\'t isolate completely, because',
                                        'But don\'t isolate completely (the isolation trap), because')),
    'iso-b': fold('iso', FIRST['iso'], ('But don\'t isolate completely, because that actually spikes',
                                        'But the isolation trap is cutting yourself off completely, which actually '
                                        'spikes')),
    'prec-a': fold('prec', FIRST['prec'], ('Not recommended for use', 'It\'s not recommended for use'),
                   ('Use with extreme caution', 'Use it with extreme caution')),
    'prec-b': fold('prec', FIRST['prec'], ('interactions. Not recommended for use in pregnancy or breast-feeding. Use '
                                           'with extreme caution in those',
                                           'interactions. It\'s not recommended for use in pregnancy or breast-feeding, '
                                           'and calls for extreme caution in those')),
}

# The openings 72a asks me to fix after the folds: in the stretch with the labels off (x1126n), The Rule's second
# sentence read AI High ('The other kind, "Exciting Love", is ...', a definition built like the one before it) and the
# agmatine opening AI Medium (a new topic straight after the herbs the protocol leaves out).
TRY2['rule-a'] = fold('rule', ('The Rule: Seek "Boring Love"', 'My rule for now is to seek "Boring Love"'),
                      ('The other kind, "Exciting Love", is the rush of a new romance or high-stakes drama, which spikes',
                       'A new romance or high-stakes drama gives you the rush of "Exciting Love", which spikes'))
TRY2['agm-a'] = fold('agm', ('Agmatine Warning (The "Voltage Regulator"): Agmatine acts like a brake on NMDA/glutamate '
                             'signaling, which is why we use it in this protocol.',
                             'Agmatine, the "voltage regulator", acts like a brake on NMDA/glutamate signaling, which is '
                             'why we do use it in this protocol.'))
# (a first try, "is a supplement we do use in this protocol, because it acts like a brake ...", changed 27% of the words
# of the best try, his version; the near-miss rule takes one word: "do", the tie to the herbs the protocol leaves out)
# Try 3 of the Precautions: try 2 (prec-a) read Human High, but its "Use it with extreme caution" no longer holds his
# words "use with extreme caution", which the fidelity keys keep for warning W009 (his card X-15); this try names the
# subject in the first of the two sentences only.
TRY2['prec-c'] = fold('prec', FIRST['prec'], ('Not recommended for use', 'It\'s not recommended for use'))

# After the section's last check (checks-1126u: Human Written, 0.0% AI, two Medium windows): the Ethnobotanicals
# paragraph's second sentence alone ("Both are illegal ... dangerous for your heart") and The Rule's second sentence. His
# usual fix first: each short sentence joined to the one its point leads to ("So never combine iboga ...", "So this may
# not be a good time ..."). The Rule keeps "a new romance or drama" named: "one" there could be read as one of the two
# kinds of love, which an earlier comparison read found in "either one" (read-1126c F1.2).
TRY2['ethno-a'] = fold('ethno', ('Ethnobotanicals: The plant medicines', 'The plant medicines'),
                       ('can be dangerous for your heart. So never combine', 'can be dangerous for your heart, so never '
                        'combine'))
TRY2['rule-b'] = fold('rule', ('The Rule: Seek "Boring Love"', 'My rule for now is to seek "Boring Love"'),
                      ('The other kind, "Exciting Love", is the rush of a new romance or high-stakes drama, which spikes',
                       'A new romance or high-stakes drama gives you the rush of "Exciting Love", which spikes'),
                      ('puts the armor right back up. So this may not be a good time',
                       'puts the armor right back up, so this may not be a good time'))

# After the section's check after the joins (checks-1126w: Human Written, 0.0% AI, one Medium window): the window moved to
# the first sentence of the paragraph after the Cognitive Warning. The point-first reorder changed 25% of the pair's
# words, past the near-miss rule; his usual fix that fits in a word or two: my paraphrase back to his post's plain words
# ("The armored brain projects its own internal threat level onto neutral faces").
FACES_S1 = ('Your armored brain also reads the threat it feels into neutral faces, so you will think people are judging you '
            'when they\'re mostly just thinking about themselves.')
FACES_S1B = ('Your armored brain also projects the threat it feels onto neutral faces, so you will think people are judging '
             'you when they\'re mostly just thinking about themselves.')
assert FACES.count(FACES_S1) == 1
FACES2 = FACES.replace(FACES_S1, FACES_S1B)

# After the section's check after the faces fix (checks-1126y: Human Written, 0.0% AI, two Medium windows): the Cognitive
# Warning's short sentences split into windows of 13 and 9 words, its second Medium, and the faces sentence stayed Medium
# with his verb back. The fixes the reads and the near-miss rule left for this step, now that two small tries from the
# pair's best are checked (#273, #288): the Cognitive Warning's first two sentences joined (the join its read asked for,
# x1126a/v1/his-fixes/cog), and the faces sentence's point first, in his post's words ("You will think people are judging
# you").
COG_S12 = ('As you de-armor, you will feel naked and exposed. You will assume everyone can see your anxiety, which they '
           'mostly can\'t.')
COG_S12B = ('As you de-armor, you will feel naked and exposed, and you will assume everyone can see your anxiety, which '
            'they mostly can\'t.')
assert FOLD['cog'].count(COG_S12) == 1
COG2 = FOLD['cog'].replace(COG_S12, COG_S12B)
FACES_S1C = ('You will also think people are judging you when they\'re mostly just thinking about themselves, because your '
             'armored brain projects the threat it feels onto neutral faces.')
FACES3 = FACES2.replace(FACES_S1B, FACES_S1C)
# The faces sentence point first read Human Medium over the whole second paragraph (checks-1126z), worse than with his
# verb alone (High, checks-1126x); the Cognitive Warning's join read High in its own window. The last try of the pair:
# the join, with the faces sentence as it read High.
FACES4 = FACES2
