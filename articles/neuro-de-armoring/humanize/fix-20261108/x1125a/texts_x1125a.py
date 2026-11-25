"""x1125a's texts: the warnings at the top ("A Complete Guide to Bio-De-Armoring"), the first section of the humanizing
pass over LEFT.md (2026-11-25). Each paragraph of model text is fixed for sense first (terms explained where first
used, the reason before the act, one idea in one place), read by fresh readers, and then checked by itself in Pangram.

NOW_* are the paragraphs as the article has them (HUMANIZED-SO-FAR.md 386bad86); V1, V2 ... are my versions, in
Markdown as they would go into the article. plain() gives the words as Pangram reads them (links as their words).
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402

ARTICLE = HERE.parents[1] / 'HUMANIZED-SO-FAR.md'
POST = 'https://ibogaqueen.substack.com/i/181671197/'
HTP = POST + 'serotonin-bottleneck-pattern-5-htp-low-dose-p5p'
UMP = POST + 'dopamine-receptor-burnout-daws-pattern-uridine-monophosphate'
REDLINE = POST + 'a-the-metabolic-red-line'
ELEC = POST + '1-electrolytes-choose-your-path'
DMSO = 'http://dmso.u-dont-exist.com/'
IBOGA = 'http://iboga.u-dont-exist.com/'
MICRO = 'http://ibogamicroprotocol.u-dont-exist.com/'
MINDWISE = 'https://www.amazon.com/Mindwise-Misunderstand-Others-Think-Believe/dp/030774356X'


def plain(md):
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', md)
    s = re.sub(r'(?<![\w*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![\w*])', r'\1', s)
    return s.replace('**', '')


def block(start):
    (b,) = [b for b in cr.sr.blocks(ARTICLE.read_text(encoding='utf-8')) if b['text'].startswith(start)]
    return b['text']


STARTS = {
    'dmso': '⚠️ CRITICAL MEDICAL DISCLAIMER:DMSO Safety:',
    'elec': 'Electrolytes: Consult a doctor',
    'ethno': 'Ethnobotanicals:',
    'iso': 'Behavioral Warning (The Isolation Trap):',
    'rule': 'The Rule: Seek',
    'cog': 'Cognitive Warning:',
    'proj': 'The armored brain projects',
    'agm': 'Agmatine Warning (The Voltage Governor):',
    'prec': 'Precautions/Side Effects:',
    'htp': 'Uridine & 5-HTP Warning for Psychedelic Users:',
    'uri': 'Rule: do not take 5-HTP on the same day',
}

# ---- version 1: fixed for sense first (2026-11-25), before any fresh read
V1 = {
    # DMSO is first named here, so it is said what it is and how the protocol uses it; the two instructions get their
    # reason before them (it carries other chemicals in); "lungs clean", which nobody can do on the spot, is said as
    # the act his DMSO reference gives for smokers (project-sources/cancer-and-research-samples.txt: "don't nebulize
    # too much DMSO if you're a smoker and your lungs are full of tar, it brings all that into your blood").
    'dmso': ('⚠️ CRITICAL MEDICAL DISCLAIMER:DMSO Safety: DMSO is a solvent you\'ll be smelling in this protocol, and since '
             'it goes straight through your skin and lungs into your blood, it can carry other chemicals in with it. So '
             'you should use 99.9% Pharmaceutical Grade DMSO, ideally in a glass bottle. It\'s sold on Amazon and other '
             'sites (I\'ve never had a bad batch). Also make sure your hands, lungs, and nose are clean before '
             'using it, and if you smoke, your lungs aren\'t, so don\'t inhale much of it, since it can pull the tar from '
             'your lungs into your blood. See my [full DMSO reference](' + DMSO + ') here.'),
    # the reason before the act, from the article's own Electrolytes section (the potassium target, and "potassium can
    # build up in your blood" with kidney disease or a blood pressure drug that holds on to it: NIH, 2022, there)
    'elec': ('Electrolytes: [Part 3](' + ELEC + ') has you eating a lot more potassium than most people get, so consult '
             'a doctor first if you have kidney disease or heart conditions, since potassium can build up in your blood '
             'when your kidneys, or some blood pressure drugs, hold on to it.'),
    # the two plants said as what they are, once; "carry risks" said as the risk the article itself names for iboga
    # (the 5-HTP warning: "serious cardiac and neurological risk")
    'ethno': ('Ethnobotanicals: The plant medicines in this protocol are iboga (an African root bark) and psilocybin '
              'mushrooms. Both are illegal in many jurisdictions and carry risks, and iboga\'s are the serious ones, to '
              'the heart and nervous system, so never combine Iboga with most medications (especially heart & psych '
              'meds). See full '
              '[iboga guide here](' + IBOGA + '), and [microdosing protocol here](' + MICRO + ').'),
    # each term said where it is first used; "even without any addiction" said for the reader; the anchoring said as
    # what it is (oxytocin from relationships) with the post's label after it
    'iso': ('Behavioral Warning (The Isolation Trap): This protocol demands starving the brain of "Phasic" Dopamine, the '
            'bursts you get from excitement, novelty and the chase, but do not isolate completely while you\'re doing '
            'that. Total social isolation spikes cortisol, the chronic stress hormone, which makes the brain more '
            'sensitive to glutamate (its main excitatory neurotransmitter) and effectively locks the armor in place, even '
            'if you\'ve never had an addiction. Humans are social animals, so you still need healthy social relationships '
            'to anchor you with oxytocin, the bonding hormone ("Oxytocinergic Anchoring").'),
    'rule': ('The Rule: Seek "Boring Love" (parallel play, reading next to someone, safe touch), and avoid "Exciting '
             'Love" (romance, high-stakes drama), as that kind spikes Phasic Dopamine and resets the armor.'),
    # three short sentences joined; the book named as a book
    'cog': ('Cognitive Warning: As you de-armor, you will feel naked and exposed, and you\'ll assume everyone can see your '
            'anxiety, which Dr. Nicholas Epley calls the "Illusion of Transparency" in his book [*Mindwise*](' + MINDWISE
            + ').'),
    # the projection tied to the paragraph before ("also"); the slogan joined to the rule it explains; the heart-rate
    # test (his 62a, word for word) given its reason from section A and Scenario A (the reasoning brain is offline)
    'proj': ('The armored brain also projects its own internal threat level onto neutral faces, so you will think people '
             'are judging you when really they\'re just thinking about themselves. Rule: During this protocol, do not '
             'trust your social intuition, since it\'s calibrated to find threats right now, whether or not they\'re there. Assume you are misreading '
             'every room until your heart rate is back down to your usual resting rate, and under 90 BPM, which is when '
             'your reasoning brain is back online (see the ["Metabolic Red Line"](' + REDLINE + ') in Part 1).'),
    # what agmatine is for the reader (sold as a supplement, acts on several systems at once), the plain meaning
    # first and the four systems after it in brackets, and what follows from it: the precautions below
    'agm': ('Agmatine Warning (The Voltage Governor): Agmatine is sold as a supplement, but it is not a basic nutrient '
            'like magnesium or a membrane nutrient like phosphatidylcholine. It\'s a neuromodulator, which means it '
            'changes how several of the brain\'s signaling systems work at once (NMDA/glutamate signaling, '
            'imidazoline/alpha-2 adrenergic tone, nitric-oxide pathways, and opioid reward/tolerance), and that\'s where '
            'the precautions below come from.'),
    # everything about 5-HTP in one paragraph (its rule moved up from the next one), the reason for the don't before
    # the don't (serotonin syndrome, which the 5-HTP section explains), each mechanism said plainly
    'htp': ('Uridine & 5-HTP Warning for Psychedelic Users: These two supplements are in this protocol for repair, so don\'t '
            'use them as "trip enhancers," especially since in practice they can change your brain\'s sensitivity '
            'quickly. 5-HTP is what your body '
            'makes serotonin from, and stacking it on anything else that raises serotonin is how people end up with '
            'serotonin syndrome (see [the 5-HTP section](' + HTP + ')). So do not combine it with SSRIs, SNRIs, MAOIs, '
            'linezolid, lithium, tramadol, methadone, fentanyl, DXM, MDMA, St. John\'s wort, SAM-e, L-tryptophan, or '
            'other serotonin-raising stacks. Be especially conservative around ayahuasca, because its harmalas inhibit '
            'MAO-A, the enzyme that breaks serotonin down, which can amplify the serotonin load, and around iboga, '
            'because ibogaine and noribogaine (what your body turns ibogaine into) interact with serotonin transport and '
            'already carry serious cardiac and neurological risk. Rule: do not take 5-HTP on the same day as a '
            'psychedelic trip, and do not use it anywhere near ayahuasca/harmalas or iboga.'),
    # uridine by itself: its two names said as one thing, Scott's story pointed to, the rule tied on with "So"
    'uri': ('Uridine (the UMP in this protocol) doesn\'t raise serotonin, but it may still change how vivid your dreams '
            'are, how much you crave things, and how sensitive you are to psychedelics and their visuals; that\'s from '
            'experience, like [Scott\'s below](' + UMP
            + '), not from studies. So do not take UMP on the same day as a psychedelic trip either, and if your '
            'sensitivity changes, assume your old psychedelic dose may now be too high.'),
}

VERSIONS = {'v1': V1}


def now(key):
    """The paragraph as the article has it, in its Markdown (links and all)."""
    (b,) = [x for x in re.split(r'\n\s*\n', ARTICLE.read_text(encoding='utf-8')) if x.startswith(STARTS[key])]
    return b


TEXTS = {}
for _k in V1:
    TEXTS[_k] = (lambda k=_k: plain(V1[k]))
TEXTS['prec'] = lambda: plain(now('prec'))


# ---- version 2: after the first fresh reads (v1/needed, v1/his-fixes, v1/fit: one Fable reader per text, 2026-11-25).
# What each read found, and what this version does about it, is in READS-V1.md. Nothing is added that the article or
# his own DMSO reference doesn't say, except three plain facts checked against sources (SOURCES below).
SOURCES = {
    'glass': 'https://www.sigmaaldrich.com/product/sigma/D2650 (its questions: "DMSO is not compatible with many types '
             'of plastics, so it is advisable to store it in appropriate amber glass vials"); '
             'https://www.mtc-usa.com/kb-article/aa-02498 (neat DMSO can extract trace compounds from plastics)',
    'ace': 'the article\'s own Electrolytes paragraph: "a blood pressure drug that holds on to potassium, like an ACE '
           'inhibitor or an ARB ... potassium can build up in your blood (NIH, 2022)"',
    'mao-a': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9121195 (serotonin is the preferred substrate of MAO-A; the '
             'harmala alkaloids of ayahuasca\'s vine inhibit it)',
    'noribogaine': 'https://www.ebi.ac.uk/chebi/CHEBI:146264 (the primary, long-lived metabolite of ibogaine; a '
                   'serotonin uptake inhibitor); https://pubmed.ncbi.nlm.nih.gov/11303040/',
    'dmso-smoker': 'his DMSO article (project-sources/cancer-and-research-samples.txt): "Clean your skin first: What you '
                   'need to worry about with DMSO on the skin is mainly that it can bring in chemicals, like beauty '
                   'products"; "don\'t nebulize too much DMSO if you\'re a smoker and your lungs are full of tar, it '
                   'brings all that into your blood (you\'ll start feeling weak as a first symptom)"',
}
V2 = {
    'dmso': ('⚠️ CRITICAL MEDICAL DISCLAIMER:DMSO Safety: This protocol has you smell DMSO for anxiety and brain fog. '
             'It\'s a solvent that goes straight through your skin and lungs into your blood, and the thing to watch is '
             'what it carries in with it, whether that\'s something in the bottle or something on you. So you should use '
             '99.9% Pharmaceutical Grade DMSO, ideally in a glass bottle, since it can leach chemicals out of some '
             'plastics. It\'s sold on Amazon and other sites (I\'ve never had a bad batch). Before using it, wash any '
             'lotions or other products off your hands and nose. Your lungs count too, so if you\'re a smoker, don\'t '
             'breathe in much of it, since it can pull the tar from your lungs into your blood, and feeling weak is the '
             'first sign of that. My [full DMSO reference](' + DMSO + ') has more on all of '
             'this.'),
    'elec': ('Electrolytes: This protocol has you eating [a lot more potassium](' + ELEC + ') than most people get, so '
             'consult a doctor first if you have kidney disease or heart conditions. Weak kidneys can let potassium build '
             'up in your blood, and so can the blood pressure drugs a lot of heart patients are on, like ACE inhibitors '
             'and ARBs.'),
    'ethno': ('Ethnobotanicals: The plant medicines in this protocol are iboga (an African root bark) and psilocybin '
              'mushrooms. Both are illegal in many jurisdictions, and both carry risks, with iboga\'s being the serious '
              'ones, since it can affect your heart and nervous system. Never combine Iboga with most medications '
              '(especially heart & psych meds). See my full [iboga guide here](' + IBOGA + '), and the iboga '
              '[microdosing protocol here](' + MICRO + ').'),
    'iso': ('Behavioral Warning (The Isolation Trap): This protocol has you starve your brain of "Phasic" Dopamine, the '
            'bursts you get from excitement, novelty and the chase. The easiest way to do that is to hole up alone, but '
            'do not isolate completely, because total social isolation locks the armor in place, even if you\'ve never '
            'had an addiction. It raises your stress hormone, cortisol, which sensitizes your brain to glutamate (the '
            'brain\'s main excitatory signal, explained below). Humans are social animals, so what you need is the calm '
            'kind of company that anchors you with the bonding hormone oxytocin ("Oxytocinergic Anchoring").'),
    'rule': ('The Rule: Seek "Boring Love", meaning parallel play (like reading next to someone) and safe touch. Avoid '
             '"Exciting Love" (romance, high-stakes drama), tempting as it is, since it spikes Phasic Dopamine and puts '
             'the armor right back up.'),
    'cog': ('Cognitive Warning: As you de-armor, you will feel more naked and exposed than you\'re used to, and you\'ll '
            'assume everyone can see your anxiety, when really they notice far less of it than you think. Dr. Nicholas '
            'Epley calls that assumption the "Illusion of Transparency" in his book [*Mindwise*](' + MINDWISE + ').'),
    'proj': ('The armored brain also projects its own internal threat level onto neutral faces, so you will think people '
             'are judging you when they\'re mostly just thinking about themselves. Rule: During this protocol, do not '
             'trust your social intuition, least of all when your heart is pounding. Assume you are misreading every '
             'room until your heart rate is back down to your usual resting rate, and under 90 BPM, since a racing heart '
             'means your reasoning brain is offline (see the ["Metabolic Red Line"](' + REDLINE + ') below).'),
    'agm': ('Agmatine Warning (The Voltage Governor): Agmatine is an optional add-on in this protocol, and although '
            'it\'s sold as a supplement, it isn\'t a basic nutrient like magnesium or a membrane nutrient like '
            'phosphatidylcholine, but a neuromodulator that acts on several of the brain\'s signaling systems at once '
            '(NMDA/glutamate signaling, imidazoline/alpha-2 adrenergic tone, nitric-oxide pathways, and the reward and '
            'tolerance you get from opioids). That means it can clash with any drug that works on the same systems, so '
            'if you take it, go by the precautions below, which name those drugs.'),
    'htp': ('Uridine & 5-HTP Warning for Psychedelic Users: These two supplements are in this protocol for repair, so '
            'don\'t use them as "trip enhancers." In practice they can quickly change how sensitive you are to '
            'psychedelics, and one of them brings a second danger. 5-HTP is what your body makes serotonin out of, so '
            'taking it on top of anything else that raises serotonin is how people end up with serotonin syndrome, an '
            'overload that can be deadly if untreated (see [the 5-HTP section](' + HTP + ')). So do not take it if '
            'you\'re on any of these: antidepressants (SSRIs, SNRIs, MAOIs), the antibiotic linezolid, lithium, the '
            'opioids tramadol, methadone and fentanyl, the cough suppressant DXM, MDMA, or the supplements St. John\'s '
            'wort, SAM-e and L-tryptophan. Rule: do not take 5-HTP on the same day as a psychedelic trip, and do not '
            'use it anywhere near ayahuasca/harmalas or iboga, iboga microdoses included. Ayahuasca\'s harmalas inhibit '
            'MAO-A, the enzyme that breaks serotonin down, which amplifies the serotonin load, and ibogaine and '
            'noribogaine (what your body turns ibogaine into) interact with serotonin transport as well, on top of the '
            'serious cardiac and neurological risk iboga already carries.'),
    'uri': ('Uridine (the UMP in this protocol) doesn\'t raise serotonin, but it can make psychedelics hit harder, '
            'visuals included, along with bringing more vivid dreams and fewer cravings, and it can do all that within '
            'a day. I don\'t have studies for this, just experience like [Scott\'s below](' + UMP + '). So do not take '
            'UMP on the same day as a psychedelic trip, and the first time you trip after starting it, assume your old '
            'psychedelic dose may now be too high and take less.'),
}
VERSIONS['v2'] = V2


# ---- version 3: after the second fresh reads (v2/needed, v2/his-fixes, v2/fit: Fable readers, two texts each,
# 2026-11-25). Each sentence a read marked is changed here, or the receipt says why it stays (what only Joel can
# say goes to him as a question: which medications, how many days, which heart-rate bar, how much less).
V3 = {
    # v2's reads marked only the smoker sentence: no amount, and a sign with nothing to do
    'dmso': ('⚠️ CRITICAL MEDICAL DISCLAIMER:DMSO Safety: This protocol has you smell DMSO for anxiety and brain fog. '
             'It\'s a solvent that goes straight through your skin and lungs into your blood, and the thing to watch is '
             'what it carries in with it, whether that\'s something in the bottle or something on you. So you should use '
             '99.9% Pharmaceutical Grade DMSO, ideally in a glass bottle, since it can leach chemicals out of some '
             'plastics. It\'s sold on Amazon and other sites (I\'ve never had a bad batch). Before using it, wash any '
             'lotions or other products off your hands and nose. Your lungs count too, so if you\'re a smoker, breathe in '
             'only a little at a time, since it can pull the tar from your lungs into your blood, and stop if you feel '
             'weak right afterwards, which is the first sign of that. My [full DMSO reference](' + DMSO + ') has more on '
             'all of this.'),
    # the people on those drugs are in the "if" now, and the drugs are said so a reader can match their own pill
    'elec': ('Electrolytes: This protocol has you eating [a lot more potassium](' + ELEC + ') than most people get, so '
             'consult a doctor first if you have kidney disease or heart conditions, or take a blood pressure drug that '
             'holds on to potassium. Those are the ACE inhibitors and ARBs (names ending in -pril or -sartan), and with '
             'them or with weak kidneys, potassium can build up in your blood.'),
    'ethno': ('Ethnobotanicals: The plant medicines in this protocol are iboga (an African root bark) and psilocybin '
              'mushrooms. Both are illegal in many jurisdictions and carry risks, and iboga\'s are the serious ones, since '
              'it can be dangerous for your heart and nervous system. So never combine Iboga with most medications '
              '(especially heart & psych meds), and if you take any, check it against my full [iboga guide here]('
              + IBOGA + ') first. The iboga [microdosing protocol is here](' + MICRO + ').'),
    # the why joined to the don't in one sentence (nothing named twice, no "It"), the addiction clause where it says
    # who this applies to, and the last sentence handing over to the rule below for what counts
    'iso': ('Behavioral Warning (The Isolation Trap): This protocol has you starve your brain of "Phasic" Dopamine, the '
            'bursts you get from excitement, novelty and the chase. The easiest way to do that is to hole up alone, but '
            'do not isolate completely, because total isolation raises your stress hormone, cortisol, which makes your '
            'brain over-react to glutamate (its main excitatory signal, explained below), and that locks the armor in '
            'place whether or not you\'ve ever had an addiction. Since we\'re social animals, what you need instead is '
            'the "Oxytocinergic Anchoring" of healthy relationships, meaning company that calms you with the bonding '
            'hormone oxytocin, and the rule below says which kind.'),
    'rule': ('The Rule: Seek "Boring Love", meaning parallel play (like reading next to someone) and touch that feels '
             'safe. As tempting as "Exciting Love" is (romance, high-stakes drama), avoid it, since it spikes Phasic '
             'Dopamine and puts the armor right back up.'),
    # the source after the reader's point, in brackets, in one sentence (the needed read: the name alone gave the
    # reader nothing; the citation stays)
    'cog': ('Cognitive Warning: As you de-armor, you will feel more naked and exposed than you\'re used to, and you\'ll '
            'assume everyone can see your anxiety, when really they notice far less of it than you think (Dr. Nicholas '
            'Epley calls this the "Illusion of Transparency" in his book [*Mindwise*](' + MINDWISE + ')).'),
    # the rule once, with its test; "at least until" keeps both of the post's statements (don't trust it during the
    # protocol; assume you're misreading until the heart rate is down) without one cancelling the other
    'proj': ('Your armored brain also reads its own threat level into neutral faces, so you will think people are '
             'judging you when they\'re mostly just thinking about themselves. So the rule during this protocol is, do '
             'not trust your social intuition: assume you are misreading every room, at least until your heart rate is '
             'back down to your usual resting rate, and under 90 BPM, since a racing heart means your reasoning brain is '
             'offline (see the ["Metabolic Red Line"](' + REDLINE + ') below).'),
    'agm': ('Agmatine Warning (The Voltage Governor): Agmatine is an optional add-on in this protocol, and although '
            'it\'s sold as a supplement, it isn\'t a basic nutrient like magnesium or a membrane nutrient like '
            'phosphatidylcholine, but a neuromodulator that acts on several of the brain\'s signaling systems at once '
            '(NMDA/glutamate signaling, imidazoline/alpha-2 adrenergic tone, nitric-oxide pathways, and the reward and '
            'tolerance you get from opioids). That means it can clash with any drug that works on the same systems, so '
            'if you take agmatine, go by the precautions below, which name those drugs.'),
    # the shared caution said with its act; no lead line for 5-HTP; one "never" and one rule, the rule's reason
    # before it; ayahuasca and iboga each with what happens
    'htp': ('Uridine & 5-HTP Warning for Psychedelic Users: These two supplements are in this protocol for repair, so '
            'don\'t use them as "trip enhancers." In practice they can quickly change how strongly psychedelics hit you, '
            'so don\'t count on your usual dose acting the way it used to. 5-HTP is also what your body makes serotonin '
            'out of, so taking it on top of anything else that raises serotonin is how people end up with serotonin '
            'syndrome, an overload that can be deadly if untreated (see [the 5-HTP section](' + HTP + ')). So never take '
            'it with any of these: antidepressants (SSRIs, SNRIs, MAOIs), the antibiotic linezolid, lithium, the opioids '
            'tramadol, methadone and fentanyl, the cough suppressant DXM, MDMA, or the supplements St. John\'s wort, '
            'SAM-e and L-tryptophan. Rule: psychedelics act on serotonin too, so do not take 5-HTP on the same day as a '
            'psychedelic trip, and do not use it anywhere near ayahuasca/harmalas or iboga, iboga microdoses included. '
            'That\'s because ayahuasca\'s harmalas inhibit MAO-A, the enzyme that breaks serotonin down, which amplifies the '
            'serotonin load, while ibogaine and noribogaine (what your body turns ibogaine into) interact with serotonin transport '
            'themselves, on top of the serious cardiac and neurological risk iboga already carries.'),
    # what bears on a trip first, with where it comes from before the claim; the rule right after it; the dreams and
    # cravings last, said as the benefits they are (his uridine section: "the hoped-for benefits of UMP")
    'uri': ('Uridine (the UMP in this protocol) doesn\'t raise serotonin, so its caution is a different one, and it '
            'comes from experience like [Scott\'s below](' + UMP + '), since I don\'t have studies on it: within a day '
            'of starting it, psychedelics can hit harder, visuals included. So do not take UMP on the same day as a '
            'psychedelic trip, and on your first trip after starting it, assume your old psychedelic dose may now be '
            'too high and take less. It may also make your dreams more vivid and your cravings weaker, which are the '
            'benefits you\'re hoping for.'),
}
VERSIONS['v3'] = V3


# ---- version 4 (after the DMSO paragraph's first check, x1125b: Human Written, 135 of 161 words High, with two Medium
# windows: its first sentence run together with the section's label, and its last, the short pointer to his
# reference). What that showed: the sentences that carry a reason read High; a line that only labels or points
# reads Medium. So the label, which the post has as a bold line of its own above its list of warnings, is a block of
# its own (LABEL), and a closing pointer says what the reader goes there for, or joins the sentence before it.
LABEL = '⚠️ CRITICAL MEDICAL DISCLAIMER:'
V4 = dict(V3)
V4['dmso'] = (V3['dmso'].replace(LABEL, '', 1)
              .replace('My [full DMSO reference](' + DMSO + ') has more on all of this.',
                       'My [full DMSO reference](' + DMSO + ') goes into the other ways to use it and what else to '
                       'watch for.'))
V4['ethno'] = V3['ethno'].replace(
    'check it against my full [iboga guide here](' + IBOGA + ') first. The iboga [microdosing protocol is here]('
    + MICRO + ').',
    'check it against my full [iboga guide here](' + IBOGA + ') first (the iboga [microdosing protocol is here]('
    + MICRO + ')).')
assert V4['dmso'] != V3['dmso'] and V4['dmso'].startswith('DMSO Safety:') and V4['ethno'] != V3['ethno']
VERSIONS['v4'] = V4
LATEST = V4


# ---- version 5 (after batch x1125c, 2026-11-25): what read Human High by itself stays (ethno, uri; his Precautions
# paragraph as it stands). What read AI or below High is tried once more with a named diagnosis. The common one: in
# answering the fresh reads I glossed every term (a stress hormone, an excitatory signal, a bonding hormone, an
# antibiotic, a cough suppressant, an enzyme), and a gloss in every sentence is the explainer register his lesson
# neuro-2026-11-24f warned of ("one word, once"). These keep the article's own glosses and drop mine, say the reader's
# experience before the mechanism, and fold a closing pointer into the sentence before it.
V5 = dict(V4)
V5['dmso'] = (V4['dmso']
              .replace('and the thing to watch is what it carries in with it, whether that\'s something in the bottle or '
                       'something on you.', 'and it can carry in whatever else is in the bottle or on your skin.')
              .replace('which is the first sign of that. My [full DMSO reference](' + DMSO + ') goes into the other ways '
                       'to use it and what else to watch for.',
                       'which is the first sign of that (there\'s more on all this in my [full DMSO reference](' + DMSO
                       + ')).'))
V5['elec'] = ('Electrolytes: This protocol has you eating [a lot more potassium](' + ELEC + ') than most people get '
              '(potatoes and greens every single day), so consult a doctor first if you have kidney disease or heart '
              'conditions, or you\'re on a blood pressure drug that holds on to potassium, like an ACE inhibitor or an '
              'ARB, since then the potassium can build up in your blood.')
V5['iso'] = ('Behavioral Warning (The Isolation Trap): This protocol demands starving your brain of "Phasic" Dopamine '
             '(excitement, novelty, the chase), and the easiest way to do that is to hole up alone, but do not isolate '
             'completely. Total social isolation spikes cortisol, the chronic stress hormone, which makes your brain more '
             'sensitive to glutamate, and that locks the armor in place whether or not you\'ve ever had an addiction. '
             'We\'re social animals, so you still need people, just the calm kind, whose company gives you oxytocin '
             'instead of a dopamine spike (the "Oxytocinergic Anchoring" the rule below is about).')
V5['proj'] = ('You\'ll also feel like people are judging you, when they\'re mostly just thinking about themselves, because '
              'an armored brain reads its own threat level into neutral faces. So during this protocol, do not trust '
              'your social intuition: assume you are misreading every room, at least until your heart rate is back down '
              'to your usual resting rate, and under 90 BPM, since a racing heart means your reasoning brain is offline '
              '(see the ["Metabolic Red Line"](' + REDLINE + ') below).')
V5['agm'] = ('Agmatine Warning (The Voltage Governor): Agmatine is optional in this protocol, and it\'s sold as a '
             'supplement, but don\'t think of it as a basic nutrient like magnesium or a membrane nutrient like '
             'phosphatidylcholine. It\'s a neuromodulator, and it works on a lot at once: NMDA/glutamate signaling, '
             'imidazoline/alpha-2 adrenergic tone, nitric-oxide pathways, and opioid reward/tolerance. So it can clash '
             'with the drugs that work on those same systems, which is what the precautions below are for.')
V5['htp'] = ('Uridine & 5-HTP Warning for Psychedelic Users: These are not "trip enhancers," they\'re in this protocol '
             'for repair, and in practice they can change your brain\'s sensitivity quickly, so your usual dose might not '
             'act the way you expect. 5-HTP is the one to be careful with, because your body makes serotonin out of it, '
             'and serotonin syndrome (which can be deadly, see [the 5-HTP section](' + HTP + ')) usually comes from '
             'mixing it with something else that raises serotonin. So do not combine it with SSRIs, SNRIs, MAOIs, '
             'linezolid, lithium, tramadol, methadone, fentanyl, DXM, MDMA, St. John\'s wort, SAM-e, L-tryptophan, or '
             'other serotonin-raising stacks. Rule: do not take 5-HTP on the same day as a psychedelic trip, and do not '
             'use it anywhere near ayahuasca/harmalas or iboga (microdoses of iboga included), since ayahuasca\'s MAO-A '
             'inhibition can amplify the serotonin load, and ibogaine and noribogaine interact with serotonin transport '
             'on top of iboga\'s already serious cardiac and neurological risk.')
for _k in ('dmso', 'elec', 'iso', 'proj', 'agm', 'htp'):
    assert V5[_k] != V4[_k], _k
VERSIONS['v5'] = V5
LATEST = V5


# ---- version 6: version 5 after its fresh reads (v5/needed, v5/his-fixes, v5/fit, for the four rewritten ones). What
# a read marked and the article or his answers already settle is kept with why in the receipt; the rest is changed here.
V6 = dict(V5)
V6['iso'] = V5['iso'].replace(
    'We\'re social animals, so you still need people, just the calm kind, whose company gives you oxytocin instead of a '
    'dopamine spike (the "Oxytocinergic Anchoring" the rule below is about).',
    'We\'re social animals, so what you need is the calm kind of company, the kind that gives you oxytocin instead of a '
    'dopamine spike (the "Oxytocinergic Anchoring" the rule below is about).')
V6['proj'] = ('You\'ll also feel like people are judging you, when they\'re mostly just thinking about themselves, because '
              'an armored brain reads its own threat level into neutral faces. So during this protocol, do not trust '
              'your social intuition. A racing heart means your reasoning brain is offline (see the ["Metabolic Red '
              'Line"](' + REDLINE + ') below), so assume you are misreading every room, at least until your heart rate is '
              'back down to your usual resting rate, and under 90 BPM.')
V6['agm'] = V5['agm'].replace('nitric-oxide pathways, and opioid reward/tolerance.',
                              'nitric-oxide pathways, and the reward and tolerance you get from opioids.')
V6['htp'] = ('Uridine & 5-HTP Warning for Psychedelic Users: These are not "trip enhancers," they\'re in this protocol '
             'for repair, and in practice they can quickly change how sensitive you are to psychedelics, so go lower '
             'than your usual dose until you see how it hits now. 5-HTP is the one to be careful with, because your body '
             'makes serotonin out of it, and serotonin syndrome usually comes from mixing 5-HTP with something else that '
             'raises serotonin, which can be deadly (see [the 5-HTP section](' + HTP + ')). So do not combine it with '
             'SSRIs, SNRIs, MAOIs, linezolid, lithium, tramadol, methadone, fentanyl, DXM, MDMA, St. John\'s wort, SAM-e, '
             'L-tryptophan, or other serotonin-raising stacks. Rule: psychedelics act on serotonin too, so do not take '
             '5-HTP on the same day as a psychedelic trip, and do not use it anywhere near ayahuasca/harmalas or iboga '
             '(microdoses of iboga included). Ayahuasca\'s MAO-A inhibition can amplify the serotonin load, and ibogaine '
             'and noribogaine interact with serotonin transport on top of iboga\'s already serious cardiac and '
             'neurological risk.')
for _k in ('iso', 'proj', 'agm', 'htp'):
    assert V6[_k] != V5[_k], _k
VERSIONS['v6'] = V6
LATEST = V6


# ---- version 7: the small steps the ledger's near-miss rule asks for (lesson bad-trips-2026-11-19b). Electrolytes,
# the Cognitive Warning's second paragraph and the 5-HTP warning each had a Human window in their first try (version
# 4), so their next try starts from that try and changes at most a fifth of its words, taking out only my own
# glosses (the diagnosis of x1125c) and what could be read two ways. Version 6's rewrites of those three wait.
V7 = dict(V6)
V7['elec'] = V4['elec'].replace(
    'Those are the ACE inhibitors and ARBs (names ending in -pril or -sartan), and with them or with weak kidneys,',
    'Those are the ACE inhibitors and ARBs, and with either kind, or with weak kidneys,')
V7['proj'] = (V4['proj'].replace('reads its own threat level into neutral faces', 'reads the threat it feels into '
                                 'neutral faces')
              .replace('So the rule during this protocol is, do not trust', 'So during this protocol, do not trust'))
V7['htp'] = (V4['htp']
             .replace('an overload that can be deadly if untreated (see', 'which can be deadly (see')
             .replace('antidepressants (SSRIs, SNRIs, MAOIs), the antibiotic linezolid, lithium, the opioids tramadol, '
                      'methadone and fentanyl, the cough suppressant DXM, MDMA, or the supplements St. John\'s wort, '
                      'SAM-e and L-tryptophan.',
                      'SSRIs, SNRIs, MAOIs, linezolid, lithium, tramadol, methadone, fentanyl, DXM, MDMA, St. John\'s '
                      'wort, SAM-e or L-tryptophan.')
             .replace('inhibit MAO-A, the enzyme that breaks serotonin down, which amplifies', 'inhibit MAO-A, which '
                      'amplifies')
             .replace('ibogaine and noribogaine (what your body turns ibogaine into) interact', 'ibogaine and '
                      'noribogaine interact'))
for _k in ('elec', 'proj', 'htp'):
    assert V7[_k] != V4[_k], _k
VERSIONS['v7'] = V7
LATEST = V7


# ---- version 8 (third tries, after the tell panels, and the next small steps). The panels on version 6 (panel-iso,
# panel-agm) named the same build (label, rule, mechanism, remedy, a pointer to close) and, sentence by sentence, the
# words that were mine and not the post's: "the calm kind of company, the kind that gives you oxytocin instead of a
# dopamine spike", "We're social animals, so what you need is", "whether or not you've ever had an addiction"; "It's a
# neuromodulator, and it works on a lot at once", "which is what the precautions below are for". A first version 8 went
# through the panel again (panel-iso8, panel-agm8), and both readers still marked its last clause in each: the truism
# and the pointer ("since we're social animals, just in the calm ways the rule below describes"; "it can interact with
# the drugs listed below"). Here the Isolation Trap ends on the post's own construction (You need the "Oxytocinergic
# Anchoring" of ...) with the kind of company said plainly, without the truism (the reason is already the sentence
# before: isolation spikes cortisol) and without a pointer (the rule is the next paragraph); agmatine ends on what
# follows from the sentence's own point (it isn't a nutrient, so it interacts with far more than one would).
V8 = dict(V7)
V8['iso'] = ('Behavioral Warning (The Isolation Trap): This protocol demands starving your brain of "Phasic" Dopamine '
             '(excitement, novelty, the chase), and the easiest way to do that is to hole up alone. But do not isolate '
             'completely, because total social isolation spikes cortisol, the chronic stress hormone, and that sensitizes '
             'your brain to glutamate and locks the armor in place even if you\'ve never had an addiction. You still need '
             'the "Oxytocinergic Anchoring" of having people around you, as long as it\'s the calm kind of company.')
V8['agm'] = ('Agmatine Warning (The Voltage Governor): Agmatine is optional in this protocol, and although it\'s sold as '
             'a supplement, it\'s a neuromodulator, here as a brake on NMDA/glutamate signaling. It can interact with a lot '
             'more medications than a basic nutrient like magnesium or a membrane nutrient like phosphatidylcholine '
             'would, since it also acts on imidazoline/alpha-2 adrenergic tone, nitric-oxide pathways, and opioid '
             'reward/tolerance.')
# (the linter's B11 caught the first version 8 of it, "it isn't a basic nutrient ... . It's a neuromodulator": the
# post's own "is not X. It is Y" across two sentences, one of his Claude tics. Here it says what agmatine is, and the
# two nutrients are what its interactions are measured against, which is what the comparison was for, with the
# point before its reason (the linter's O65).)
# the 5-HTP warning: the next small step from version 7 (67.2% AI, the list Human High, the rule Human Medium). Three
# sentences read AI: the two "so" explainers after the first, and the closing "That's because A, while B". The second
# starts with "But" in place of the post's "In practice"; the third says the danger in his own words from the 5-HTP
# section ("Serotonin syndrome usually comes from mixing 5-HTP casually with anything else that raises serotonin");
# the last says what ties ayahuasca to the list above it (its harmalas are MAOIs themselves, his "harmala MAOI
# chemistry") in place of the mirrored "while".
V8['htp'] = (V7['htp']
             .replace('In practice they can quickly', 'But they can quickly')
             .replace('so taking it on top of anything else that raises serotonin is how people end up with serotonin '
                      'syndrome, which can be deadly (see', 'and serotonin syndrome, which can be deadly, usually comes '
                      'from mixing it casually with anything else that raises serotonin (see')
             .replace('That\'s because ayahuasca\'s harmalas inhibit MAO-A, which amplifies the serotonin load, while '
                      'ibogaine and noribogaine interact with serotonin transport themselves, on top',
                      'Ayahuasca\'s harmalas are MAOIs themselves (they inhibit MAO-A, which amplifies the serotonin '
                      'load), and ibogaine and noribogaine interact with serotonin transport, on top'))
# the Cognitive Warning's first paragraph, for its pair: the correction both panel readers marked ("when really they
# notice far less of it than you think", a stock pivot, and mine) said in four plain words
V8['cog'] = V4['cog'].replace('when really they notice far less of it than you think', 'which they mostly can\'t')
for _k in ('htp',):
    assert V8[_k] != V7[_k], _k
assert V8['cog'] != V4['cog']
VERSIONS['v8'] = V8
LATEST = V8


# ---- version 9 (after batch x1125e): the Cognitive Warning's pair went from AI Detected, 61.5%, to Human Written with
# every window Human on one change (the stock correction said in four words), so it is the near miss, and the next
# step is one of the kind he makes: a word that could point at two things. In "(Dr. Nicholas Epley calls this the
# "Illusion of Transparency" ...)", the window that read Medium, "this" could be the assuming or the fact that people
# mostly can't see it. It is the assuming.
V9 = dict(V8)
V9['cog'] = V8['cog'].replace('calls this the', 'calls that assumption the')
assert V9['cog'] != V8['cog']
VERSIONS['v9'] = V9
LATEST = V9


# ---- version 10 (after the comparison read, read-1125a/READER-1.md): three small snags a fresh reader found in
# paragraphs that are in the article at Human High, each a word that could point at two things, the kind he fixes one
# at a time (lesson bad-trips-2026-11-19b). F1.2: "if you take any, check it" (any medication, or any iboga?); F1.17:
# "starting it" after two "it"s that were the caution; F1.1: "Your lungs count too" (count as what?). Each goes in only
# if its check by itself reads Human High again; until then the article keeps the version it has.
V10 = dict(V9)
V10['ethno'] = V4['ethno'].replace('and if you take any, check it against', 'and if you take any medication, check it against')
V10['uri'] = V4['uri'].replace('within a day of starting it, psychedelics', 'within a day of starting uridine, psychedelics')
V10['dmso'] = V6['dmso'].replace('Your lungs count too, so if', 'Your lungs need to be clean too, so if')
for _k, _v in (('ethno', V4), ('uri', V4), ('dmso', V6)):
    assert V10[_k] != _v[_k], _k
VERSIONS['v10'] = V10
LATEST = V10
