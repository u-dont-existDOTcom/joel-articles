"""The receipts for this turn's texts of mine (texts_x1126a.NEW: ethno, rule, uri), each his answer fitted where it goes
and then fixed for sense after the fresh reads of the first draft (v1/needed, v1/his-fixes, v1/fit: Fable, 2026-11-26)
and the comparison reads of the first and second drafts (read-1126a, read-1126b).
Every sentence a read marked is changed here, or kept with why.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1126a/build_receipts_x1126a.py
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'x1123a'))
sys.path.insert(0, str(HERE.parent / 'x1123b'))
sys.path.insert(0, str(HERE))
import build_receipts_x1123b as BB  # noqa: E402  (its fill allows a link of "none: why")
import texts_x1126a as T  # noqa: E402

B = BB.B
S = B.S
OUT = HERE / 'receipts'
OUT.mkdir(exist_ok=True)
B.HERE = OUT
TOP = 'A Complete Guide to Bio-De-Armoring, the warnings at the top'
YOU = ('an adult with trauma or an addiction who has read the short introduction and is reading the warnings before '
       'starting the protocol, ')
MSG = 'his message of 2026-11-26 00:50 UTC (fix-20261108/joel-20261126-0050-message.txt)'

# the first drafts the readers read (v1), as make_briefs_x1126a.py gave them
V1 = {
    'ethno': T.plain(T.OLD['ethno']
                     .replace('dangerous for your heart and nervous system.', 'dangerous for your heart.')
                     .replace('and if you take any medication, check it against my full [iboga guide here](' + T.GUIDE +
                              ') first (the iboga [microdosing protocol is here](' + T.MICRO + ')).',
                              'and if you take any medication, ask an AI first whether it interacts with iboga, since AI '
                              'is pretty good at that (my full [iboga guide here](' + T.GUIDE + ') has more, and the iboga '
                              '[microdosing protocol is here](' + T.MICRO + ')).')),
    'rule': ('The Rule: Seek "Boring Love", meaning parallel play (like reading next to someone) and touch that feels safe. '
             '"Exciting Love" (a new romance, high-stakes drama) spikes Phasic Dopamine and puts the armor right back up, '
             'so this may not be a good time to jump into it.'),
    'uri': T.plain(T.OLD['uri'].replace(
        'and on your first trip after starting it, assume your old psychedelic dose may now be too high and take less.',
        'and on your first trip once you\'re on it, start with a third of your old psychedelic dose, since UMP can boost '
        'the effects a lot in some people, especially "hard heads" who usually need more than an average dose.')),
}


def v1(key, n):
    return S.sentences(V1[key])[n - 1]


def reader(kind, key):
    brief = {'needed': 'needed_read_brief.md', 'his-fixes': 'his_fixes_brief.md', 'fit': 'fit_read_brief.md'}[kind]
    return ('a fresh reader (Fable, 2026-11-26) given tools/humanization/%s and only the text, one sentence a line, of the '
            'first draft (x1126a/v1/%s/%s/READ.md)' % (brief, kind, key))


def ethno():
    return B.build(
        'ETHNO2', T.plain(T.NEW['ethno']), TOP + ': the third item, the plant medicines', YOU + 'who may be on medication '
        'and has never taken iboga',
        {'Ethnobotanicals:': ('they learn which two plant medicines the warnings are about, and what iboga is', 'it is the '
                              'next item of the warnings', None),
         'Both are illegal': ('they learn both are illegal in many places and carry risks, and that iboga can be dangerous '
                              'for the heart', 'it says what the two just named carry', 'Both'),
         'So never combine': ('they don\'t mix iboga with most medications, heart and psych ones above all', 'it follows '
                              'from the heart danger', 'So'),
         'If you take any': ('they ask an AI whether a medication of theirs is one of those, with his guide and the '
                             'microdosing protocol linked for more', 'it says how to know which medications are meant',
                             'If you take any medication'),
         'Ask the AI about the mushrooms': ('they ask about the mushrooms too, and know lithium is one to ask about', 'it '
                                            'takes the same check to the second plant', 'Ask the AI about the mushrooms '
                                            'too')},
        'they learn which plant medicines the protocol uses and the warnings that go with them, before getting either',
        [('iboga can be dangerous for the heart', 'ibogaine prolongs the QT interval, which raises the risk of a dangerous '
          'arrhythmia, and deaths after it have been put down to that (Koenig and Hilber 2015, '
          'https://pmc.ncbi.nlm.nih.gov/articles/PMC4382526)', 'yes: they see why heart meds are named among the medications not to mix', 'kept'),
         ('a nervous-system risk from iboga', 'his 66: "i\'m not aware of it having more neurological risk than shrooms. it '
          'looks like that\'s based on giving rats high doses"', 'no', 'cut'),
         ('AI can check iboga interactions', 'his 67: "i\'d say AI is pretty good for giving iboga interactions in general. '
          'so people can just check AI for that"', 'yes: they know where to check a medication of theirs', 'kept'),
         ('lithium with psychedelics is tied to seizures', 'Nayak et al. 2021, Pharmacopsychiatry: 47% of 62 reports of '
          'lithium with a psychedelic involved seizures (https://pubmed.ncbi.nlm.nih.gov/34348413/)', 'yes: they check '
          'lithium, or any medication, before the mushrooms', 'kept')],
        {'reader': reader('needed', 'ethno'), 'unneeded': [], 'kept': {}},
        {'reader': reader('his-fixes', 'ethno'),
         'marked': [{'s': v1('ethno', 1), 'difference': '4: "psilocybin mushrooms" and "this protocol" lean on what the '
                     'reader knows'},
                    {'s': v1('ethno', 2), 'difference': '4, 1, 10: "carry risks" names none; "iboga\'s are the serious '
                     'ones" ranks without saying what the mushrooms\' are'},
                    {'s': v1('ethno', 3), 'difference': '12, 10, 4, 1, 14, 15, 17, 8: "never ... most" then "ask an AI '
                     'first" reads two ways; "first" before nothing named; one sentence carries all; "Iboga" capitalised'}],
         'kept': {v1('ethno', 1): 'psilocybin mushrooms is the name a reader knows, and the protocol is the article\'s own'}},
        {'reader': reader('fit', 'ethno'),
         'marked': [{'s': v1('ethno', 2), 'found': 'MISREAD: the mushrooms read as the safe choice on psych medication'},
                    {'s': v1('ethno', 3), 'found': 'CAN\'T TELL which medications; MISREAD: never, or fine if the AI says '
                     'so'}],
         'kept': {}},
        'the post\'s item: both are illegal and carry risks, never combine iboga with most medications (especially heart '
        '& psych meds), and the links to his guide and the microdosing protocol; his 66 takes out the nervous-system risk, '
        'his 67 says to check with an AI and keep the links for more',
        'the third item of the warnings, where the post has it')


def rule():
    return B.build(
        'RULE6', T.plain(T.NEW['rule']), TOP + ': The Rule, right after the Isolation Trap', YOU + 'who has just read that '
        'being alone works against the protocol, and may be single, dating or with a partner',
        {'The Rule:': ('they look for calm company: being near someone while each does their own thing, and touch that '
                       'feels safe to them', 'it is the rule the Isolation Trap ends on, the calm kind of company', None),
         'The other kind': ('they know which kind of closeness to hold off on, and that it undoes what the protocol does',
                            'it is the other kind, set against the one just named', 'The other kind'),
         'So this may not': ('they wait on starting a new romance or stepping into drama, and keep the partner they have, '
                             'with the two named so "either one" can\'t be read as the two kinds of love (read-1126c F1.2)',
                             'it says what follows for them now', 'So')},
        'they learn which company and closeness help during the protocol and which may not',
        [('a new romance spikes phasic dopamine and puts the armor back up', 'the post\'s own rule ("Avoid \'Exciting '
          'Love\' (romance, high-stakes drama), as this spikes Phasic Dopamine and resets the armor")', 'yes: they hold off on a new romance because it would undo the protocol', 'kept'),
         ('not a time to jump into a new romance, and no need to leave a partner', 'his 66 on P6: "make sure i\'m not '
          'telling people to break up with their partner to avoid romance lol. just maybe not a good time to jump into it"',
          'yes: they wait on a new romance and keep their partner', 'kept')],
        {'reader': reader('needed', 'rule'), 'unneeded': [], 'kept': {}},
        {'reader': reader('his-fixes', 'rule'),
         'marked': [{'s': v1('rule', 1), 'difference': '5, 13, 1, 4: opens on the label; "touch that feels safe" says not '
                     'to whom'},
                    {'s': v1('rule', 2), 'difference': '2, 12, 4, 10, 21: mirrors the first sentence; not said to be the '
                     'other kind; "it" could be three things'}],
         'kept': {}},
        {'reader': reader('fit', 'rule'),
         'marked': [{'s': v1('rule', 2), 'found': 'CAN\'T TELL what counts, or what to do if already in a new romance'}],
         'kept': {}},
        'the post\'s rule: seek "Boring Love" (parallel play, reading next to someone, safe touch) and hold off on '
        '"Exciting Love" (romance, high-stakes drama), since it spikes Phasic Dopamine and resets the armor; his 66 says a '
        'new romance, and nothing about leaving a partner',
        'right after the Isolation Trap, as in the post; the Isolation Trap before it (his version) says what phasic '
        'dopamine is, with his link')


def uri():
    keep3 = ('they take the dream and craving changes as what UMP is for, not a reason to stop: his 66 kept my additions to this paragraph but the two he named: the changes UMP is taken for, from his UMP '
             'section ("Vivid dreams and increased sensitivity to psychedelics are the hoped-for benefits of UMP"; Scott\'s '
             'cravings fell within a day), so a reader doesn\'t take them as a reason to stop; the article is for trauma '
             'and addiction, its title says so')
    return B.build(
        'URI3', T.plain(T.NEW['uri']), TOP + ': uridine, after the 5-HTP warning for psychedelic users', YOU + 'who uses '
        'psychedelics now and then and knows the usual dose',
        {'Uridine (the UMP': ('they learn what uridine can change about a trip, who it hits hardest, and that this rests on '
                              'reports like Scott\'s, not studies', 'it comes after the 5-HTP warning and says how this '
                              'caution differs', None),
         'So do not take UMP': ('they keep UMP off trip days and start their first trip on it at a third of their old '
                                'dose', 'it follows from how much harder a trip can hit', 'So'),
         'It may also': ('they know the dream and craving changes are what UMP is for, not reasons to stop', 'it names the '
                         'other changes, after the one to be careful with', 'It may also')},
        'they learn the caution that comes with uridine for anyone who uses psychedelics',
        [('UMP can boost psychedelic effects a lot in some people, "hard heads" most, so start with a third of the old dose',
          'his 69 (' + MSG + ')', 'yes: they start their first trip on UMP at a third of their old dose', 'kept'),
         ('within a day of starting uridine', 'Scott\'s report in his UMP section', 'yes: they know to expect the change from the first day', 'kept')],
        {'reader': reader('needed', 'uri'), 'unneeded': [v1('uri', 3)], 'kept': {v1('uri', 3): keep3}},
        {'reader': reader('his-fixes', 'uri'),
         'marked': [{'s': v1('uri', 1), 'difference': '1, 9, 11, 16, 3, 4, 10: five ideas in one sentence; the source '
                     'before the claim'},
                    {'s': v1('uri', 2), 'difference': '12, 17, 16, 1, 14, 4: "since UMP can boost the effects" says S1 again'},
                    {'s': v1('uri', 3), 'difference': '12, 29, 10, 4, 6: "It" and "your cravings" unnamed; a summing-up tag'}],
         'kept': {v1('uri', 3): keep3}},
        {'reader': reader('fit', 'uri'),
         'marked': [{'s': v1('uri', 2), 'found': 'CAN\'T TELL whether a microdose day is a trip'},
                    {'s': v1('uri', 3), 'found': 'FROM: cravings from an addiction text; MISREAD: vivid dreams as nightmares'}],
         'kept': {v1('uri', 3): keep3}},
        'the post\'s uridine caution: not serotonergic, but may change dreams, visuals, craving and psychedelic tolerance; no '
        'UMP on the same day as a trip; and his 69: a third of the old dose to start',
        'after the 5-HTP warning, where the post\'s "Rule:" paragraph had it')


# The small steps (texts_x1126a.STEP), which the near-miss rule asks for before the full versions: each puts in one of his
# answers in the fewest words; what a read marked that a step leaves as it was is fixed in the full version, and the
# receipt says so.
LATER = ('kept for this small step only: the near-miss rule (lesson bad-trips-2026-11-19b) takes at most a fifth of the '
         'words of the passing try changed until two such steps are checked, and the full version fixes it')


def ethno_step(name, text, check_line, s3):
    checked = [('iboga can be dangerous for the heart', 'ibogaine prolongs the QT interval, which raises the risk of a '
                'dangerous arrhythmia (Koenig and Hilber 2015, https://pmc.ncbi.nlm.nih.gov/articles/PMC4382526)',
                'yes: they see why heart meds are named among the medications not to mix', 'kept'),
               ('a nervous-system risk from iboga', 'his 66: "i\'m not aware of it having more neurological risk than '
                'shrooms. it looks like that\'s based on giving rats high doses"', 'no', 'cut')] + check_line
    return B.build(
        name, text, TOP + ': the third item, the plant medicines', YOU + 'who may be on medication and has never taken iboga',
        {'Ethnobotanicals:': ('they learn which two plant medicines the warnings are about, and what iboga is', 'it is the '
                              'next item of the warnings', None),
         'Both are illegal': ('they learn both are illegal in many places and carry risks, and that iboga can be dangerous '
                              'for the heart', 'it says what the two just named carry', 'Both'),
         'So never combine': (s3, 'it follows from the heart danger', 'So')},
        'they learn which plant medicines the protocol uses and the warnings that go with them, before getting either',
        checked,
        {'reader': reader('needed', 'ethno'), 'unneeded': [], 'kept': {}},
        {'reader': reader('his-fixes', 'ethno'),
         'marked': [{'s': v1('ethno', 1), 'difference': '4: "psilocybin mushrooms" and "this protocol" lean on what the '
                     'reader knows'},
                    {'s': v1('ethno', 2), 'difference': '4, 1, 10: "carry risks" names none; "iboga\'s are the serious '
                     'ones" ranks without saying what the mushrooms\' are'},
                    {'s': v1('ethno', 3), 'difference': '12, 10, 4, 1, 14, 15, 17, 8: "never ... most" then "ask an AI '
                     'first" reads two ways; "first" before nothing named; one sentence carries all; "Iboga" capitalised'}],
         'kept': {v1('ethno', 1): 'psilocybin mushrooms is the name a reader knows, and the protocol is the article\'s own'}},
        {'reader': reader('fit', 'ethno'),
         'marked': [{'s': v1('ethno', 2), 'found': 'MISREAD: the mushrooms read as the safe choice on psych medication'},
                    {'s': v1('ethno', 3), 'found': 'CAN\'T TELL which medications; MISREAD: never, or fine if the AI says '
                     'so'}],
         'kept': {}},
        'the post\'s item: both are illegal and carry risks, never combine iboga with most medications (especially heart '
        '& psych meds), and the links to his guide and the microdosing protocol; his 66 takes out the nervous-system risk',
        'the third item of the warnings, where the post has it')


def uri_step(name, text, s1, checked):
    keep3 = ('they take the dream and craving changes as what UMP is for, not a reason to stop: his 66 kept my additions '
             'to this paragraph but the two he named, and his UMP section calls them the hoped-for benefits')
    return B.build(
        name, text, TOP + ': uridine, after the 5-HTP warning for psychedelic users', YOU + 'who uses psychedelics now and '
        'then and knows the usual dose',
        {'Uridine (the UMP': (s1, 'it comes after the 5-HTP warning and says how this caution differs', None),
         'So do not take UMP': ('they keep UMP off trip days and start their first trip on it at a third of their old '
                                'dose', 'it follows from how much harder a trip can hit', 'So'),
         'It may also': ('they know the dream and craving changes are what UMP is for, not reasons to stop', 'it names the '
                         'other changes, after the one to be careful with', 'It may also')},
        'they learn the caution that comes with uridine for anyone who uses psychedelics',
        checked,
        {'reader': reader('needed', 'uri'), 'unneeded': [v1('uri', 3)], 'kept': {v1('uri', 3): keep3}},
        {'reader': reader('his-fixes', 'uri'),
         'marked': [{'s': v1('uri', 1), 'difference': '1, 9, 11, 16, 3, 4, 10: five ideas in one sentence; the source '
                     'before the claim'},
                    {'s': v1('uri', 2), 'difference': '12, 17, 16, 1, 14, 4: "since UMP can boost the effects" says S1 again'},
                    {'s': v1('uri', 3), 'difference': '12, 29, 10, 4, 6: "It" and "your cravings" unnamed; a summing-up tag'}],
         'kept': {v1('uri', 1): LATER, v1('uri', 3): keep3}},
        {'reader': reader('fit', 'uri'),
         'marked': [{'s': v1('uri', 2), 'found': 'CAN\'T TELL whether a microdose day is a trip'},
                    {'s': v1('uri', 3), 'found': 'FROM: cravings from an addiction text; MISREAD: vivid dreams as nightmares'}],
         'kept': {v1('uri', 3): keep3}},
        'the post\'s uridine caution: not serotonergic, but may change dreams, visuals, craving and psychedelic tolerance; no '
        'UMP on the same day as a trip; and his 69: a third of the old dose to start',
        'after the 5-HTP warning, where the post\'s "Rule:" paragraph had it')


def steps():
    third = [('start a first trip on UMP at a third of the old dose', 'his 69 (' + MSG + ')', 'yes: they start their '
              'first trip on UMP at a third of their old dose', 'kept'),
             ('within a day of starting uridine', 'Scott\'s report in his UMP section', 'yes: they know to expect the '
              'change from the first day', 'kept')]
    some = [('it hits some people a lot harder', 'his 69: "it can boost effects a lot in *some* people"', 'yes: they know '
             'the change is large for some and not for all', 'kept')]
    ai = [('AI can check iboga interactions, and the guide lists only some', 'his 67: "iboga guide mentions some '
           'interactions ... i\'d say AI is pretty good for giving iboga interactions in general"', 'yes: they know where '
           'to check a medication of theirs', 'kept')]
    return (ethno_step('ETHNO-E1', T.STEP['e1'], [], 'they don\'t mix iboga with most medications, heart and psych ones '
                       'above all, and check a medication of theirs against his guide first, with the microdosing protocol '
                       'linked')
            + ethno_step('ETHNO-E2', T.STEP['e2'], ai, 'they don\'t mix iboga with most medications, heart and psych ones '
                         'above all, and ask an AI about a medication of theirs first, since his guide lists only some')
            + uri_step('URI-U1', T.STEP['u1'], 'they learn that uridine can make a trip hit harder from the first day, and '
                       'that this rests on reports like Scott\'s, not studies', third)
            + uri_step('URI-U2', T.STEP['u2'], 'they learn that uridine can make a trip hit some people a lot harder from '
                       'the first day, and that this rests on reports like Scott\'s, not studies', third + some))


V1['cog'] = ('Cognitive Warning: As you de-armor, you will feel naked and exposed. You will assume everyone can see your '
             'anxiety. Dr. Nicholas Epley, Mindwise, calls this the "Illusion of Transparency."')


def cog_step(name, text):
    S3KEY = 'Dr. Nicholas Epley' if 'Dr. Nicholas Epley' in text else 'Nicholas Epley'
    """The Cognitive Warning's first paragraph with one change, checked with the paragraph after it (the first is under
    50 words); the fresh reads are of the first paragraph as it stood (V1['cog'])."""
    s1 = ('kept for this step: the near-miss rule takes one change a try from a window that read Human (lesson '
          'bad-trips-2026-11-19b); the label is the post\'s own, as every warning above opens on one, and the join the '
          'read asks for (S1 and S2 in one sentence) is the next step if this one reads below High')
    s3 = ('the term and the book are his credit (his 68a: credit Epley\'s book only); in the article Mindwise is an '
          'italic link to the book, which shows it is a book; with S2 now saying the assumption is wrong, "this" points '
          'at that mistaken assumption')
    return B.build(
        name, text, TOP + ': the Cognitive Warning, its first paragraph with the one after it', YOU + 'who gets anxious '
        'around people',
        {'Cognitive Warning:': ('they expect to feel exposed as the armor comes off', 'the next warning', None),
         'You will assume': ('they know they will think everyone can see their anxiety, and that people see much less of '
                             'it than they think', 'it says the thought that comes with that feeling, and that it is '
                             'mistaken', 'You will assume'),
         S3KEY: ('they learn the mistake has a name and where to read about it', 'it names what the sentence before '
                 'described', 'calls this'),
         'Your armored brain': ('they learn the second way their read goes wrong: they will feel judged by people who are '
                                'mostly thinking about themselves', 'it adds to the paragraph before, which said they '
                                'will feel seen through', 'also'),
         'So during this protocol': ('they distrust their read of a room during the protocol, at least until their heart '
                                     'rate is back down to their usual resting rate and under 90 BPM', 'it gives the rule '
                                     'both paragraphs lead to', 'So during this protocol')},
        'they learn they will feel seen through and judged, and that both feelings are mistaken',
        [('people see much less of your anxiety than you think', 'people overestimate how much others can discern their '
          'internal states (Gilovich, Savitsky and Medvec 1998, https://pubmed.ncbi.nlm.nih.gov/9731312/); Epley\'s book '
          'Mindwise describes it', 'yes: they know the feeling of being seen through is mistaken', 'kept'),
         ('a racing heart means the reasoning brain is offline', 'the article\'s section A and Scenario A ("your '
          'Reasoning Brain is offline")', 'yes: they know why the heart rate is the test', 'kept')],
        {'reader': reader('needed', 'cog'), 'unneeded': [], 'kept': {}},
        {'reader': reader('his-fixes', 'cog'),
         'marked': [{'s': v1('cog', 1), 'difference': '4, 13, 21: a label for the thing; exposed to whom, when'},
                    {'s': v1('cog', 2), 'difference': '2, 8, 12: built like S1, two flat sentences with nothing joining '
                     'them'},
                    {'s': v1('cog', 3), 'difference': '5, 7, 10, 11, 12, 13: opens on the authority; "this" could point at '
                     'three things; the fact the reader needs (they can\'t see it as well as you think) is never said'}],
         'kept': {v1('cog', 1): s1, v1('cog', 3): s3}},
        {'reader': reader('fit', 'cog'),
         'marked': [{'s': v1('cog', 1), 'found': 'ANYWAY; MISREAD: a danger with no reassurance'},
                    {'s': v1('cog', 2), 'found': 'ANYWAY; CAN\'T TELL whether people really see it; MISREAD: read fast, '
                     '"everyone will see your anxiety"'},
                    {'s': v1('cog', 3), 'found': 'CAN\'T TELL what the term means; FROM: a general finding; MISREAD: '
                     'which way the illusion goes'}],
         'kept': {v1('cog', 1): 'the reassurance it asks for is now in S2, right after it: people see much less of the '
                                'anxiety than the reader thinks; ' + s1,
                  v1('cog', 3): s3 + '; the general finding is what the warning applies to the reader, and S2 now says '
                                'which way it goes'}},
        'the post\'s Cognitive Warning: you will feel naked and exposed, you will assume everyone can see your anxiety, '
        'and Epley\'s Mindwise calls this the Illusion of Transparency; his 68a keeps the credit as it is',
        'fifth of the warnings, where the post has it, with its second paragraph after it')


def cog_join(name, text):
    """Step 2 of the Cognitive Warning: his usual fix alone, S1 and S2 joined, from the paragraph as it stands; the
    payoff clause of step 1 read lower (x1126f) and stays out."""
    s3 = ('the term and the book are his credit (his 68a: credit Epley\'s book only); in the article Mindwise is an '
          'italic link to the book, which shows it is a book; "this" now follows one sentence, so it points at that '
          'sentence\'s feeling and assumption')
    left = ('the clause saying people see much less of it read lower in this pair (x1126f, Human Medium and then Low: '
            'https://www.pangram.com/history/3e0b20f3-f755-4192-b4b0-39cc3aa2a03f), so it waits; the paragraph right after '
            'this one gives the reassurance ("when they\'re mostly just thinking about themselves")')
    return B.build(
        name, text, TOP + ': the Cognitive Warning, its first paragraph with the one after it', YOU + 'who gets anxious '
        'around people',
        {'Cognitive Warning:': ('they expect to feel exposed as the armor comes off, and to think everyone can see their '
                                'anxiety', 'the next warning', None),
         'Dr. Nicholas Epley': ('they learn the mistake has a name and where to read about it', 'it names what the '
                                'sentence before described', 'calls this'),
         'Your armored brain': ('they learn the second way their read goes wrong: they will feel judged by people who are '
                                'mostly thinking about themselves', 'it adds to the paragraph before, which said they '
                                'will feel seen through', 'also'),
         'So during this protocol': ('they distrust their read of a room during the protocol, at least until their heart '
                                     'rate is back down to their usual resting rate and under 90 BPM', 'it gives the rule '
                                     'both paragraphs lead to', 'So during this protocol')},
        'they learn they will feel seen through and judged, and that both feelings mislead them',
        [('the feeling of being seen through is a known mistake', 'people overestimate how much others can discern their '
          'internal states (Gilovich, Savitsky and Medvec 1998, https://pubmed.ncbi.nlm.nih.gov/9731312/); Epley\'s book '
          'Mindwise describes it', 'yes: they know the feeling has a name and misleads them', 'kept'),
         ('a racing heart means the reasoning brain is offline', 'the article\'s section A and Scenario A ("your '
          'Reasoning Brain is offline")', 'yes: they know why the heart rate is the test', 'kept')],
        {'reader': reader('needed', 'cog'), 'unneeded': [], 'kept': {}},
        {'reader': reader('his-fixes', 'cog'),
         'marked': [{'s': v1('cog', 1), 'difference': '4, 13, 21: a label for the thing; exposed to whom, when'},
                    {'s': v1('cog', 2), 'difference': '2, 8, 12: built like S1, two flat sentences with nothing joining '
                     'them'},
                    {'s': v1('cog', 3), 'difference': '5, 7, 10, 11, 12, 13: opens on the authority; "this" could point at '
                     'three things; the fact the reader needs (they can\'t see it as well as you think) is never said'}],
         'kept': {v1('cog', 3): s3 + '; ' + left}},
        {'reader': reader('fit', 'cog'),
         'marked': [{'s': v1('cog', 1), 'found': 'ANYWAY; MISREAD: a danger with no reassurance'},
                    {'s': v1('cog', 2), 'found': 'ANYWAY; CAN\'T TELL whether people really see it; MISREAD: read fast, '
                     '"everyone will see your anxiety"'},
                    {'s': v1('cog', 3), 'found': 'CAN\'T TELL what the term means; FROM: a general finding; MISREAD: '
                     'which way the illusion goes'}],
         'kept': {v1('cog', 3): s3 + '; ' + left}},
        'the post\'s Cognitive Warning: you will feel naked and exposed, you will assume everyone can see your anxiety, '
        'and Epley\'s Mindwise calls this the Illusion of Transparency; his 68a keeps the credit as it is',
        'fifth of the warnings, where the post has it, with its second paragraph after it')


def cog_who(name, text):
    """Step 3 of the Cognitive Warning: from the paragraph as it stands, "around people" says exposed to whom; steps 1
    and 2 read lower (x1126f, x1126g)."""
    lower = ('steps 1 and 2 read lower in this pair (the clause saying people see much less of it: '
             'https://www.pangram.com/history/3e0b20f3-f755-4192-b4b0-39cc3aa2a03f; the join: '
             'https://www.pangram.com/history/bc3c7d3f-a85b-4bc1-824a-d57f827a4446), so this step changes only the one '
             'thing in the window that read Medium that a reader could take two ways, exposed to whom; the paragraph right '
             'after this one gives the reassurance ("when they\'re mostly just thinking about themselves")')
    s3 = ('the term and the book are his credit (his 68a: credit Epley\'s book only); in the article Mindwise is an '
          'italic link to the book, which shows it is a book; ' + lower)
    return B.build(
        name, text, TOP + ': the Cognitive Warning, its first paragraph with the one after it', YOU + 'who gets anxious '
        'around people',
        {'Cognitive Warning:': ('they expect to feel exposed around people as the armor comes off', 'the next warning',
                                None),
         'You will assume': ('they know they will think everyone can see their anxiety', 'it says the thought that comes '
                             'with that feeling', 'You will assume'),
         'Dr. Nicholas Epley': ('they learn the thought is a known mistake with a name, and where to read about it', 'it '
                                'names what the sentence before described', 'calls this'),
         'Your armored brain': ('they learn the second way their read goes wrong: they will feel judged by people who are '
                                'mostly thinking about themselves', 'it adds to the paragraph before, which said they '
                                'will feel seen through', 'also'),
         'So during this protocol': ('they distrust their read of a room during the protocol, at least until their heart '
                                     'rate is back down to their usual resting rate and under 90 BPM', 'it gives the rule '
                                     'both paragraphs lead to', 'So during this protocol')},
        'they learn they will feel seen through and judged, and that both feelings mislead them',
        [('the feeling of being seen through is a known mistake', 'people overestimate how much others can discern their '
          'internal states (Gilovich, Savitsky and Medvec 1998, https://pubmed.ncbi.nlm.nih.gov/9731312/); Epley\'s book '
          'Mindwise describes it', 'yes: they know the feeling has a name and misleads them', 'kept'),
         ('a racing heart means the reasoning brain is offline', 'the article\'s section A and Scenario A ("your '
          'Reasoning Brain is offline")', 'yes: they know why the heart rate is the test', 'kept')],
        {'reader': reader('needed', 'cog'), 'unneeded': [], 'kept': {}},
        {'reader': reader('his-fixes', 'cog'),
         'marked': [{'s': v1('cog', 1), 'difference': '4, 13, 21: a label for the thing; exposed to whom, when'},
                    {'s': v1('cog', 2), 'difference': '2, 8, 12: built like S1, two flat sentences with nothing joining '
                     'them'},
                    {'s': v1('cog', 3), 'difference': '5, 7, 10, 11, 12, 13: opens on the authority; "this" could point at '
                     'three things; the fact the reader needs (they can\'t see it as well as you think) is never said'}],
         'kept': {v1('cog', 2): 'the join read lower (step 2); ' + lower, v1('cog', 3): s3}},
        {'reader': reader('fit', 'cog'),
         'marked': [{'s': v1('cog', 1), 'found': 'ANYWAY; MISREAD: a danger with no reassurance'},
                    {'s': v1('cog', 2), 'found': 'ANYWAY; CAN\'T TELL whether people really see it; MISREAD: read fast, '
                     '"everyone will see your anxiety"'},
                    {'s': v1('cog', 3), 'found': 'CAN\'T TELL what the term means; FROM: a general finding; MISREAD: '
                     'which way the illusion goes'}],
         'kept': {v1('cog', 2): '"assume" says it is a thought, and S3 names it a known mistake; ' + lower,
                  v1('cog', 3): s3}},
        'the post\'s Cognitive Warning: you will feel naked and exposed, you will assume everyone can see your anxiety, '
        'and Epley\'s Mindwise calls this the Illusion of Transparency; his 68a keeps the credit as it is',
        'fifth of the warnings, where the post has it, with its second paragraph after it')


import re as _re
_art = T.ARTICLE.read_text(encoding='utf-8').split('\n\n')
_i = next(j for j, p in enumerate(_art) if p.startswith('Cognitive Warning:'))
COG1 = T.plain(T.COG['c1']) + '\n\n' + T.plain(_art[_i + 1])
COG2 = T.plain(T.COG['c2']) + '\n\n' + T.plain(_art[_i + 1])
COG3 = T.plain(T.COG['c3']) + '\n\n' + T.plain(_art[_i + 1])
COG4 = T.plain(T.COG['c4']) + '\n\n' + T.plain(_art[_i + 1])
COG5 = T.plain(T.COG['c5']) + '\n\n' + T.plain(_art[_i + 1])

if __name__ == '__main__':
    bad = ethno() + rule() + uri() + steps() + cog_step('COG-C1', COG1) + cog_join('COG-C2', COG2) + cog_who('COG-C3', COG3) + cog_step('COG-C4', COG4) + cog_step('COG-C5', COG5)
    print('\n'.join(bad) or 'receipts: PASS')
