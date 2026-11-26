"""The texts of the turn of his message of 2026-11-26 00:50 UTC (../joel-20261126-0050-message.txt), with why each one
changed. His three versions come from the cards page's export (../x1125a/ANSWERS-X1125A-20261126-0050.json); the rest
are his answers 66, 67 and 69 fitted where they go (68 is "a": the credit to Epley's book stays as it is).

  HIS[key]   his version as the article takes it (obvious typos fixed, the link he asked for, a link the card's plain
             text could not carry put back)
  OLD[key]   the paragraph as HUMANIZED-SO-FAR.md has it now (raw Markdown)
  NEW[key]   what replaces it
  WHY[key]   one line on why
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parent
H = FIX.parent
ROOT = H.parents[2]
sys.path.insert(0, str(FIX / 'x1125a'))
import texts_x1125a as T  # noqa: E402

plain = T.plain
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
CARDS = {i['id']: i for i in json.loads((FIX / 'x1125a' / 'ANSWERS-X1125A-20261126-0050.json')
                                        .read_text(encoding='utf-8'))['items']}
HTP_SECTION = 'https://ibogaqueen.substack.com/i/181671197/serotonin-bottleneck-pattern-5-htp-low-dose-p5p'
PHASIC = 'https://www.sciencedirect.com/science/article/pii/S0959438825001059'
GUIDE = 'http://iboga.u-dont-exist.com/'
MICRO = 'http://ibogamicroprotocol.u-dont-exist.com/'
HARMALA = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7678905/'
SCOTT = 'https://ibogaqueen.substack.com/i/181671197/dopamine-receptor-burnout-daws-pattern-uridine-monophosphate'

# his versions exactly as he checked them (the share pages' text, read back this turn: each Human Written, one window,
# High): https://www.pangram.com/history/364ba0a6-ea20-4584-85e8-5d8ca2c733d0 (W-ISO, 108 words),
# .../75d40a7b-25a9-4eb1-9ab6-6635b66eff58 (W-AGMINTRO, 81 words), .../bc1f203e-34da-44e7-99db-6e4140130364 (W-HTPTOP,
# 125 words)
CHECKED = {k: CARDS[k]['your_version'].strip() for k in CARDS}

HIS = {
    # his link for "Phasic" Dopamine (his comment: "link phasic dopamine to https://www.sciencedirect.com/...")
    'iso': CHECKED['W-ISO'].replace('"Phasic" Dopamine', '["Phasic" Dopamine](' + PHASIC + ')', 1),
    # two double spaces and "etc" without its point are typos (fixed, no recheck needed: his rule of 2026-11-0x); and
    # "tone" -> "receptors", his own fix: '"tone" was unclear. when i changed tone to receptors it flipped that section
    # human. but i flipped it back to tone, because i wanted to show the main triggers for pangram'. This text is
    # checked by itself this turn before it goes in.
    'agm': (CHECKED['W-AGMINTRO'].replace('  ', ' ').replace('etc)', 'etc.)')
            .replace('adrenergic tone,', 'adrenergic receptors,')),
    # the card's plain text can't carry links, and my version linked "the 5-HTP section" to the section; nothing says
    # he took it out (his rule: never assume a citation absent from his version was removed on purpose)
    'htp': CHECKED['W-HTPTOP'].replace('(see the 5-HTP section)', '(see [the 5-HTP section](' + HTP_SECTION + '))', 1),
}
assert HIS['iso'] != CHECKED['W-ISO'] and HIS['htp'] != CHECKED['W-HTPTOP'] and 'receptors' in HIS['agm']


def _before():
    """The article as this turn found it (a65eaa1b), so the old paragraphs can still be read once they are replaced:
    APPLIED-X1126A.json keeps every old paragraph, and before it exists the article itself still has them."""
    f = pathlib.Path(__file__).resolve().parent / 'APPLIED-X1126A.json'
    if f.exists():
        import json
        return '\n\n'.join(a['old'] for a in json.loads(f.read_text(encoding='utf-8'))['runs'][0]['applied'])
    return ARTICLE.read_text(encoding='utf-8')


def para(start):
    hits = [p for p in _before().split('\n\n') if p.startswith(start)]
    assert len(hits) == 1, (start, len(hits))
    return hits[0]


OLD = {
    'ethno': para('Ethnobotanicals: The plant medicines in this protocol'),
    'iso': para('Behavioral Warning (The Isolation Trap):'),
    'rule': para('The Rule: Seek "Boring Love"'),
    'agm': para('Agmatine Warning (The Voltage Governor):'),
    'htp': para('Uridine & 5-HTP Warning for Psychedelic Users:'),
    'uri': para('Uridine (the UMP in this protocol)'),
    'ss': para('[Serotonin syndrome](https://medlineplus.gov/ency/article/007272.htm) usually comes from mixing'),
    'void5htp': para('5-HTP: Not a dopamine tool.'),
    'shield5htp': para('5-HTP trial if the bottleneck looks serotonergic:'),
}

NEW = dict(HIS)
WHY = {
    'iso': 'his version (W-ISO), with his link for "Phasic" Dopamine',
    'agm': 'his version (W-AGMINTRO) with his "receptors" for "tone"; typos fixed',
    'htp': 'his version (W-HTPTOP), with the link to the 5-HTP section carried over',
}

# 66 (P4): "remove this thing about iboga carrying neurological risk ... it looks like that's based on giving rats high
# doses". 67: "people can just check AI for that, they don't need to read my big iboga guide just for that, but they
# should still have the links to the guide for more info". The heart stays: it is why heart meds are named.
NEW['ethno'] = (OLD['ethno']
                .replace('and iboga\'s are the serious ones, since it can be dangerous for your heart and nervous system.',
                         'and iboga can be dangerous for your heart.')
                .replace('So never combine Iboga with', 'So never combine iboga with')
                .replace('& psych meds), and if you take any medication, check it against my full [iboga guide here](' + GUIDE + ') first '
                         '(the iboga [microdosing protocol is here](' + MICRO + ')).',
                         '& psych meds). If you take any medication, ask an AI whether it\'s one of them, since AI is pretty good at '
                         'that (my full [iboga guide here](' + GUIDE + ') lists some of them, and the iboga [microdosing '
                         'protocol is here](' + MICRO + ')). Ask the AI about the mushrooms too, since lithium, for one, has '
                         'been tied to seizures when taken with psychedelics.'))
# (after the fresh reads of the first draft, v1, and the comparison read of the second, read-1126b: "never ... most" then
# "ask an AI first" read two ways, never or fine if the AI says so, and "first" came before nothing named, so the check asks
# whether the medication is one of the "most"; the mushrooms had no word for a reader on medication, and lithium with
# psychedelics is tied to seizures, Nayak et al. 2021, https://pubmed.ncbi.nlm.nih.gov/34348413/, my addition for him to
# approve; my ranking "iboga's are the serious ones" then said the mushrooms' risks weren't serious, against that sentence,
# so it goes; "lists some of them" is his 67, "iboga guide mentions some interactions"; "Iboga" was capitalised here only)
WHY['ethno'] = 'his 66 (no nervous-system risk) and 67 (ask an AI about interactions; the guide stays linked for more)'

# 66 (P6): "make sure i'm not telling people to break up with their partner to avoid romance lol. just maybe not a good
# time to jump into it". The post's "Avoid 'Exciting Love' (romance, ...)" can read as avoiding the romance you have.
NEW['rule'] = ('The Rule: Seek "Boring Love", meaning parallel play (like reading next to someone) and touch that feels '
               'safe to you. The other kind, "Exciting Love", is the rush of a new romance or high-stakes drama, which '
               'spikes Phasic Dopamine and puts the armor right back up. So this may not be a good time to jump into '
               'a new romance or drama, though there\'s no need to leave the partner you have.')
# (read-1126c F1.2: "either one" could be read as Boring Love or Exciting Love, the two kinds just named, so the
# sentence names what to hold off on)
# (the fresh reads, v1: "it" in "jump into it" could be the romance, the drama or "Exciting Love"; the second sentence
# mirrored the first's quoted label and brackets; a reader in a new romance or with a partner couldn't tell what to do,
# which is his worry: "make sure i'm not telling people to break up with their partner". The comparison read of the
# second draft, read-1126b F1.3: "jump into one" read as the romance only, so the drama dropped out of the advice)
WHY['rule'] = 'his 66 on P6: a new romance, and "maybe not a good time to jump into it", in place of "avoid romance"'

# 69: "i'd start with 1/3 the psychedelic dose after UMP because it can boost effects a lot in *some* people
# (especially "hard heads" who usually need more than avg doses)"
NEW['uri'] = OLD['uri'].replace(
    'and it comes from experience like [Scott\'s below](' + SCOTT + '), since I don\'t have studies on it: within a day of '
    'starting uridine, psychedelics can hit harder, visuals included. So do not take UMP on the same day as a psychedelic '
    'trip, and on your first trip after starting it, assume your old psychedelic dose may now be too high and take less.',
    'within a day of starting it, psychedelics can hit some people a lot harder, visuals included, especially "hard heads" '
    'who usually need more than an average dose (I don\'t have studies on this, only experience like [Scott\'s](' + SCOTT +
    '), whose story is further down). So do not take UMP on the same day as a psychedelic trip, and on your first trip '
    'once you\'re on it, start with a third of your old psychedelic dose.').replace(
    'so its caution is a different one, within a day', 'so its caution is a different one: within a day')
# (the his-fixes read, v1: a reason for the third that said "UMP can boost the effects a lot" again after "psychedelics can
# hit harder" was the same point twice, so who it hits hardest goes where the effect is said; the comparison reads,
# read-1126a F1.12 and read-1126b F1.7: the caution came after four clauses, two "it"s pointed at different things, and
# Scott was named before the reader meets him, so the caution comes first and the source goes in brackets after it)
WHY['uri'] = 'his 69: start with a third of the old dose, and why (a lot, in some people, hard heads most)'

# 69: "5htp is ok a day before iboga or aya, or day after aya, or a few days after iboga usually (well, 1 day after low
# dose iboga is fine, they often say wait weeks after a flood dose to use anything that is at all psychoactive but
# mainly to ensure you don't block iboga's after-effects)"; and his comment on W-HTPTOP: "we should change the 5-HTP
# warning with psychedelics, it's not likely to be dangerous with them" (his version has no same-day rule). His
# W-HTPTOP and his Weeks 3-7 line keep 5-HTP out while microdosing iboga.
NEW['ss'] = OLD['ss'].replace(
    'If you\'re doing psychedelics, avoid 5-HTP on the same day as a trip, and be especially strict around ayahuasca\'s '
    '[harmala MAOI chemistry](' + HARMALA + ') and around iboga or ibogaine.',
    'If you\'re doing psychedelics, be especially strict around ayahuasca\'s [harmala MAOI chemistry](' + HARMALA + ') '
    'and around iboga or ibogaine: never take 5-HTP on the same day as either one, though it\'s fine the day before, or '
    'the day after ayahuasca. After a low dose of iboga, wait a day, and after a bigger dose usually a few days. After a '
    'flood dose (one big dose), people often wait weeks before taking anything psychoactive, mainly so they don\'t block '
    'the after-effects they took iboga for. While you\'re microdosing iboga, leave 5-HTP out altogether.')
# (read-1126c F1.7: with the general same-day rule gone, as he asked, "be especially strict" no longer said strict about
# what, and the paragraph said when 5-HTP is fine without saying when it isn't; F1.8: "a few days otherwise" then
# "weeks" made the reader reread to find three cases)
# (his own paragraph from card E of 2026-11-04, fix-20261104/cards/ANSWERS-20261104-2234.json, kept word for word but the
# same-day rule; the comparison read of the first draft, read-1126a F1.17: "wait a few days" then "a day is enough" then
# "weeks" left the wait unclear, "flood dose" wasn't explained, and "iboga's after-effects" sounded like something to
# block, so the waits go from the shortest up and the after-effects are the ones they took iboga for)
WHY['ss'] = 'his 69 (how near ayahuasca and iboga) and his comment on W-HTPTOP (no same-day rule for psychedelics)'
NEW['void5htp'] = OLD['void5htp'].replace('iboga, MDMA, DXM, tramadol, or a same-day psychedelic trip.',
                                          'iboga, MDMA, DXM, or tramadol.')
WHY['void5htp'] = 'his comment on W-HTPTOP: no same-day rule for 5-HTP with psychedelics'
NEW['shield5htp'] = OLD['shield5htp'].replace('iboga, MDMA, DXM, tramadol, or a same-day psychedelic trip.',
                                              'iboga, MDMA, DXM, or tramadol.')
WHY['shield5htp'] = WHY['void5htp']

for _k in OLD:
    assert NEW[_k] != OLD[_k], _k

# which of these are mine and go in only at Human High by themselves (or in a pair under 50 words), which are his
MINE = ['ethno', 'rule', 'uri']
HIS_KEYS = ['iso', 'agm', 'htp']
OWNER_EDITS = ['ss', 'void5htp', 'shield5htp']   # his answers in paragraphs not yet humanized ("never checked")


# Small steps (the near-miss rule, lesson bad-trips-2026-11-19b): the last tries of W-ETHNO and W-URITOP read Human High,
# so the ledger takes a try that changes more than a fifth of their words only after two tries of at most a fifth have been
# checked from them. Each step puts in one of his answers in the fewest words, and each makes sense by itself; the full
# versions above (NEW) are the rewrites that follow.
E232 = ('Ethnobotanicals: The plant medicines in this protocol are iboga (an African root bark) and psilocybin mushrooms. '
        'Both are illegal in many jurisdictions and carry risks, and iboga\'s are the serious ones, since it can be dangerous '
        'for your heart and nervous system. So never combine Iboga with most medications (especially heart & psych meds), '
        'and if you take any medication, check it against my full iboga guide here first (the iboga microdosing protocol is '
        'here).')
U233 = ('Uridine (the UMP in this protocol) doesn\'t raise serotonin, so its caution is a different one, and it comes from '
        'experience like Scott\'s below, since I don\'t have studies on it: within a day of starting uridine, psychedelics '
        'can hit harder, visuals included. So do not take UMP on the same day as a psychedelic trip, and on your first trip '
        'after starting it, assume your old psychedelic dose may now be too high and take less. It may also make your dreams '
        'more vivid and your cravings weaker, which are the benefits you\'re hoping for.')
STEP = {
    # his 66: no nervous-system risk, and with it my ranking, which made the mushrooms read as the safe choice (fit read)
    'e1': E232.replace('and iboga\'s are the serious ones, since it can be dangerous for your heart and nervous system.',
                       'and iboga can be dangerous for your heart.').replace('combine Iboga', 'combine iboga'),
    # his 69: a third of the old dose to start
    'u1': U233.replace('on your first trip after starting it, assume your old psychedelic dose may now be too high and take '
                       'less.', 'on your first trip once you\'re on it, start with a third of your old psychedelic dose.'),
}
# his 67: an AI first, since the guide lists only some interactions, and the guide still linked
STEP['e2'] = STEP['e1'].replace('check it against my full iboga guide here first (the iboga microdosing protocol is here).',
                                'ask an AI about it first, since my full iboga guide here only lists some (the iboga '
                                'microdosing protocol is here).')
# his 69: it hits some people a lot harder
STEP['u2'] = STEP['u1'].replace('psychedelics can hit harder, visuals included.',
                                'psychedelics can hit some people a lot harder, visuals included.')


# The Cognitive Warning's first paragraph (P8, the post's own, 29 words; his 68a keeps Epley's book as the credit), checked
# with the paragraph after it. As it stands it read Human, its first 21 words at Medium (x1126e). The three fresh reads
# (v1/needed/cog, v1/his-fixes/cog, v1/fit/cog) all found the same gap: nothing says plainly that other people see much
# less of the anxiety than the reader thinks, which is what the warning is for. One change a try (the near-miss rule):
# first that sentence, then, if needed, the join the his-fixes read asks for.
COG_OLD = next(p for p in ARTICLE.read_text(encoding='utf-8').split('\n\n') if p.startswith('Cognitive Warning:'))
COG = {'c1': COG_OLD.replace('You will assume everyone can see your anxiety.',
                             'You will assume everyone can see your anxiety, but people see much less of it than you '
                             'think.')}
# c1 read lower (Human Medium, then Low over the paragraph after it, which had read High): the payoff clause stays out,
# and the next step, from the check of the paragraph as it stands, is his usual fix alone, joining S1 and S2.
COG['c2'] = COG_OLD.replace('you will feel naked and exposed. You will assume everyone',
                            'you will feel naked and exposed, and you\'ll assume everyone')
# c2 read lower too (Medium, Low, Medium). Step 3, from the paragraph as it stands: one thing a reader could take two ways
# in the window that read Medium, exposed to whom (the his-fixes read: "exposed to whom and in what moments"), two words.
COG['c3'] = COG_OLD.replace('you will feel naked and exposed.', 'you will feel naked and exposed around people.')
# c3 read the same as the paragraph as it stands (Medium, then High). Step 4: the payoff in the words that lifted my
# version last turn (x1125a: "when really they notice far less of it than you think" read lower, "which they mostly
# can't" lifted every window to Human), four words; c1's longer clause read lower.
COG['c4'] = COG_OLD.replace('You will assume everyone can see your anxiety.',
                            'You will assume everyone can see your anxiety, which they mostly can\'t.')
# c4 read Human High over 25 and 87 words, with one window of one word at Medium: "Dr.", where Pangram splits a sentence
# at the abbreviation's point (the splits at "Dr." the lane has seen before, lessons gut-2026-11-07). The apply gate
# takes every window High, so step 5 takes the title off, a deletion, and nothing else.
COG['c5'] = COG['c4'].replace('Dr. Nicholas Epley,', 'Nicholas Epley,')
