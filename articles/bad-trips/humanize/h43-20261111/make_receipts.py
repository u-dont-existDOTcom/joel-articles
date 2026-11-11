#!/usr/bin/env python3
"""make_receipts.py - the making-sense receipts for this folder's tests (gate E365): every sentence's payoff, what it
follows and the words that link it, the nine questions, placement, opening and same point, and the fresh reader's needed
read (NEEDED-READ.md).

  python3 make_receipts.py KEY...      make TEST-KEY.receipt.json from TEST-KEY.txt, fill it and check it
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
SR = REPO / 'tools/humanization/sense_receipt.py'
NEEDED = json.loads((HERE / 'NEEDED.json').read_text(encoding='utf-8')) if (HERE / 'NEEDED.json').exists() else {}

R = {
 'h42-08': {
  'section': 'Active Seizure: What Else May Help: At the Aura, and Alongside Rescue Medicine (2 of 2)',
  'reader': 'someone with a person having a seizure, often from MDMA or a psychedelic overdose (generalized), deciding '
            'whether cannabis, topical CBD or DMSO is worth using alongside rescue medicine, and whether to wait on any',
  'sentences': [
   ('they hear the case for cannabis from people who use it: some say it stops a seizure, one EEG showed fewer discharges',
    "it continues the part before on THC, the forum reports after the ones it began with", 'I also read on forums'),
   ('they hear the other side: for some, vapes and concentrates brought seizures on, so the form matters',
    'the counter-reports from the same forums', 'But a few people on the same forums'),
   ('they know the animal evidence leans the same way as the warning, for high-THC smoke',
    'more on the same side', 'And'),
   ("they know topical CBD's evidence is thin before they hear the one trial", 'the next remedy, after cannabis',
    'As for topical CBD'),
   ("they know the one trial found the gel absorbed but no better than placebo", "what the thin evidence is",
    'There was a short 12-week trial done'),
   ('they know why it may have failed: a low dose, or focal epilepsy responding less', "the trial's own explanation",
    'The study authors suggested'),
   ("they know the syndromes oral CBD is approved for have generalized seizures", "it picks up \"the syndromes oral CBD is approved for\"",
    'The seizures in Dravet and Lennox-Gastaut syndrome'),
   ("they know their case (MDMA or psychedelic overdose) is the generalized kind, so the gel might do better for them",
    'what that means for their case', 'so topical CBD might do better for those'),
   ("they know DMSO's evidence is mixed: fewer seizures in one rat model, the opposite at some doses in another",
    'the next remedy, after CBD', 'As for DMSO'),
   ("they use DMSO, if at all, alongside rescue medicine, and never wait on it while the seizure goes on",
    'what the mixed evidence means for them', 'So'),
  ],
  'late_ok': {'Generalized': "not mine and not a definition: the guide's sentence (read Human High in h42a) tells the "
                             "reader their seizures are the generalized kind, after the sentence before says the "
                             "syndromes' seizures are; it names their case, and rewording words that read High is left "
                             "alone (gut-2026-11-06c)"},
  'placement': "the end of What Else May Help, after cannabis's forum reports and topical CBD: DMSO comes last as the "
               "remedy with the weakest seizure evidence, and its last sentence says what to do with it",
  'why_reading': 'it tells someone deciding about cannabis that people who use it report it can stop a seizure, so they '
                 'read on to hear the other side and the other remedies',
  'same_point': 'none: read What Else May Help from its heading to the next for cannabis, topical CBD and DMSO; each '
                'remedy is said once, here',
  'questions': {
   'Q1': 'PASS: each sentence opens on its remedy or the report ("As for topical CBD", "As for DMSO", "So it might help")',
   'Q2': "PASS: the one instruction is the reader's: use it alongside rescue medicine, don't wait on it",
   'Q3': 'PASS: "THC vapes and concentrates", "a CBD skin gel", "rats with temporal-lobe epilepsy" name the exact thing',
   'Q4': 'PASS: "rescue medicine" is the section\'s own term from its first part; "adjunct" is now said as "alongside '
         'rescue medicine"; generalized is explained by what the reader faces',
   'Q5': 'PASS: "But" turns to the counter-reports, "so" draws each conclusion, the last "So" draws it from the mixed evidence',
   'Q6': 'PASS: the reports, then the trial, then what it means for this reader, for each remedy in turn',
   'Q7': "PASS: each fact bears on whether the reader uses that remedy during a seizure",
   'Q8': 'PASS: all three are remedies people try alongside rescue medicine',
   'Q9': 'PASS: one step a sentence, the relations said ("so", "but", "As for")',
  },
 },
 'h42-17': {
  'section': 'Nausea Smoothers When the Person Wants to Preserve the Trip',
  'reader': 'someone nauseous on a psychedelic who wants to keep the trip going, choosing what to take for the nausea, and '
            'when not to',
  'sentences': [
   ('they know this part is for nausea when they want to keep the trip', 'the heading', 'none: the section heading itself'),
   ('they know when to reach for these: when ozonated zeolite and ferment did not help, the nausea is likely the dose acting '
    'on serotonin receptors in the gut', 'it opens the section under its heading', 'When ozonated zeolite and ferment don\'t help'),
   ('they know the first remedy and what else it does', 'the remedy, as its own heading', 'none: a heading, naming the next remedy'),
   ('they know coffee cherries helped his nausea', 'it opens the remedy under its heading', 'Eating a couple of coffee cherries'),
   ('they know what it does to the trip: blissful and sleepy, then clarity and energy', 'what else it does, after the nausea',
    'It'),
   ('they know it may lengthen the trip', 'one more effect', 'also'),
   ("they don't give it first to someone already getting manic, and know a longer trip is fine when planned",
    'what the longer, energized trip means for who should take it', 'I wouldn\'t reach for coffee cherries first'),
  ],
  'placement': 'Nausea Smoothers, after the gut remedies (ozonated zeolite and ferment) that it follows when they did not help',
  'why_reading': 'it tells someone whose nausea didn\'t settle with zeolite and ferment what is likely causing it, so they '
                 'read on for what helps that kind',
  'same_point': 'none: read Nausea Smoothers from its heading to the next for coffee cherry; the gut remedies are their own section before it',
  'questions': {
   'Q1': 'PASS: the section says when to use it first; the last sentence opens on the instruction, the nuance after',
   'Q2': "PASS: the one instruction (not first for someone becoming manic) is the reader's, with what it is for",
   'Q3': 'PASS: "a couple of coffee cherries", "somebody already becoming manic" say exactly which',
   'Q4': 'PASS: ozonated zeolite and ferment are the remedies of the section before; serotonin receptors in the gut is said as what they act on',
   'Q5': 'PASS: "also" adds the longer trip; the last sentence draws on it with "though"',
   'Q6': 'PASS: when to use, what it does, then who should not take it first',
   'Q7': 'PASS: each effect bears on whether to take it now',
   'Q8': 'PASS: coffee cherry is a nausea smoother that keeps the trip',
   'Q9': 'PASS: one step a sentence',
  },
 },
 'h42-30': {
  'section': 'Grounding Menu: Choose One or Two Things (2 of 2: Music, Human, Time, Ordinary world)',
  'reader': 'someone in a hard trip, or the person with them, picking one or two things to ground with, and which to skip and when',
  'sentences': [
   ('they know the next choice is music', "the menu's next part", 'none: a label in the menu'),
   ('they pick music they already know', 'the first thing to do with music', 'none: the first item under its label'),
   ("they don't push a planned arc or a strange playlist on someone who dislikes it", 'the other side of familiar music',
    'none: a list item, the next choice under its label'),
   ('they pick a drum rhythm to ground, or gentle music when that is wanted', 'which music for which need', 'none: a list item, the next choice under its label'),
   ("they know where to find music he finds soothing", 'one source of the gentle kind', 'none: a list item, the next choice under its label'),
   ('they know the next choice is a person', "the menu's next part", 'none: a label in the menu'),
   ("they don't work through it with the most reactive person they know", 'the one thing to know about people here', 'none: the first item under its label'),
   ('they know the next choice is time', "the menu's next part", 'none: a label in the menu'),
   ('they remember the state will rise, peak and change', 'what time does', 'none: the first item under its label'),
   ('they put big decisions off until tomorrow', 'what follows from the state changing', 'none: a list item, the next choice under its label'),
   ('they know the last choice is the ordinary world', "the menu's last part", 'none: a label in the menu'),
   ('they eat something simple, like fruit', 'the first ordinary thing', 'none: the first item under its label'),
   ('they walk slowly with someone clear-headed somewhere safe', 'the next ordinary thing', 'none: a list item, the next choice under its label'),
   ('they go outside if it helps, somewhere quiet, away from roads, water and heights', 'the next ordinary thing, with its limits',
    'too'),
   ("they don't exercise hard when overheating, with chest pain, faint or badly confused", 'the limit on moving, after walking and going out',
    'none: a list item, the next choice under its label'),
   ('they don\'t exercise hard after a stimulant or an unknown mixture, or with any medical concern', 'more of the same limit',
    'The same goes'),
  ],
  'placement': "the Grounding Menu's second half, after Body and Smell and the breathing lines: music, a person, time and the "
               "ordinary world, each a choice the reader can pick",
  'why_reading': 'it gives someone choosing how to ground the next option, music, with which kind to use',
  'same_point': "none: read the Grounding Menu from its heading to the next for music, people, time and the ordinary world; "
                "the human anchor is its own section after it",
  'questions': {
   'Q1': 'PASS: each item opens on what to do or what helps ("Use familiar music", "Going outside can help too", "Avoid strenuous exercise")',
   'Q2': "PASS: each instruction is the reader's own act",
   'Q3': 'PASS: "roads and water", "nothing high to fall from", "a stimulant or an unknown mixture" name the exact things',
   'Q4': 'PASS: no term needs explaining',
   'Q5': 'PASS: "too" adds going out to the ordinary things; "The same goes" extends the limit',
   'Q6': 'PASS: the menu order the guide gives, each limit next to the act it limits',
   'Q7': 'PASS: each item is a choice or a limit for grounding now',
   'Q8': 'PASS: music, a person, time and ordinary things are each grounding choices',
   'Q9': 'PASS: the long list of conditions taken apart into two sentences',
  },
 },
}
R['h42-20'] = {
  'section': "Mental Stabilizers That Don't Abort the Trip (3 of 6): DMSO's interactions and contraindications",
  'reader': 'someone about to use DMSO to steady a hard trip, checking what not to combine it with and who should be careful with it',
  'sentences': [
   ('they know the interactions come next', "the part after DMSO's side effects", 'none: a label in the remedy'),
   ("they clean the skin first, since DMSO carries what's on it inward", 'the first interaction', 'none: the first item under its label'),
   ("they don't take it with drugs that shouldn't absorb fast, since it strengthens them", 'the next interaction', 'none: a list item, the next one under its label'),
   ('they take harmalas and DMSO a little apart, and use DMSO when the ayahuasca is too strong', 'the case of the drug most readers here take with it', 'none: a list item, the next one under its label'),
   ("they avoid cholinergic drugs with it, knowing he hasn't seen it cause a real problem", 'the last interaction', 'none: a list item, the next one under its label'),
   ('they know the contraindications come next', 'after the interactions', 'none: a label in the remedy'),
   ('if they have seizures, they know DMSO can help or hurt depending on the kind and dose, and where the guide says more',
    'the first contraindication', 'none: the first item under its label'),
   ('if they get cluster headaches, they know it may worsen them, though it can ease tension headaches', 'the next contraindication', 'none: a list item, the next one under its label'),
   ('they know it may release histamine', 'the next contraindication', 'none: a list item, the next one under its label'),
   ('if they have MCAS, they go carefully', 'who the histamine matters to', 'Use caution with MCAS'),
  ],
  'placement': "DMSO's entry in Mental Stabilizers, after its side effects: what not to combine it with, then who should be careful",
  'why_reading': 'it tells someone about to use DMSO that what follows is what not to combine it with',
  'same_point': "the seizure item's second sentence repeated Active Seizure's DMSO paragraph (the two animal models, 'a plausible "
                "experimental adjunct remedy') and is cut there (gate E378); what stays here is the contraindication itself, "
                "with a pointer to Active Seizure",
  'questions': {
   'Q1': 'PASS: each item opens on what to avoid or who should be careful ("Don\'t put it on dirty skin", "With seizures")',
   'Q2': "PASS: each instruction is the reader's own act, with its reason",
   'Q3': 'PASS: "drugs that should not absorb rapidly", "cholinergic drugs", "a cluster headache" say which',
   'Q4': 'PASS: harmalas and MCAS are the guide\'s terms from earlier; "cholinergic" is said as what DMSO also is',
   'Q5': 'PASS: each item follows its label; the seizure item says both sides with "either way"',
   'Q6': 'PASS: interactions, then contraindications',
   'Q7': 'PASS: each item bears on whether they take DMSO now, with what',
   'Q8': 'PASS: the seizure item is a reason for some people to be careful with DMSO',
   'Q9': 'PASS: one point an item',
  },
}
R['h42-22'] = {
  'section': 'Ocean Water to calm & protect the energetic field; Shungite, Aged Ozonated-Charcoal Water, or Boiled Charcoal Water',
  'reader': 'someone whose trip is too strong, deciding whether touching ocean water or a charcoal water could steady it, and how each differs',
  'sentences': [
   ('they know this remedy is ocean water', 'the heading', 'none: the section heading itself'),
   ('they know ocean water is simple and works oddly well for him', 'it opens the remedy under its heading', 'none: the first sentence under its heading'),
   ('they know where he noticed it', 'where it comes from', 'I noticed it'),
   ('they know rain water may work too, tested only near the ocean', 'one more water like it', 'also works'),
   ('they know they can buy seawater if there is no ocean', 'how to get it without an ocean', 'You can also buy'),
   ('they touch ocean water when the trip is too strong', 'how to use it', 'When a trip is too strong'),
   ("they know touching the bottle doesn't do it", 'what does not work', 'Touching the outside of a bottle'),
   ('they put their hands in the water itself, bottled or not', 'what does', 'Direct contact with the water'),
   ('they know what it feels like and that it is not the same as his other remedies', 'what the touch does', 'It feels'),
   ("they know he can't say why, only that it has worked again and again for a trip that's too intense", 'what he knows of it', "I don't understand the mechanism"),
   ('they know the next remedies are shungite and the charcoal waters', 'the next heading', 'none: a heading, naming the next remedies'),
   ('they know he is less sure how these differ from ocean water', 'it opens the remedy under its heading', 'I honestly can\'t say'),
   ('they know ocean water lowers the intensity more, charcoal water is more peaceful, ocean water more reliable', 'how they differ, as far as he knows', 'Ocean water seems'),
   ('they know charcoal water is not zeolite or swallowed charcoal', 'what it is not', 'Aged ozonated-charcoal water is different'),
   ('they know which water he means: ozonated with charcoal and left to settle', 'what exactly he uses', 'What I usually use'),
   ('they know it is the water after the ozone is gone', 'which moment exactly', 'I mean'),
   ("they know it won't fix the gut the way zeolite does", 'what it does not do', 'That water'),
  ],
  'placement': "Mental Stabilizers, after the essential oils and DMSO: the waters, ocean water first and the charcoal waters compared with it",
  'why_reading': 'it tells someone in a trip that is too strong that a simple thing, ocean water, steadies it',
  'same_point': 'none: read the section from Ocean Water to the next heading for the waters; zeolite is its own section before',
  'questions': {
   'Q1': 'PASS: each sentence opens on its point ("Ocean water is", "When a trip is too strong", "It feels")',
   'Q2': "PASS: the instruction (touch the water itself) is the reader's own act",
   'Q3': 'PASS: "Quinton Medical Seawater", "the outside of a bottle", "water ozonated with ordinary rock charcoal" say which',
   'Q4': 'PASS: the remedies named are the guide\'s own from the sections before',
   'Q5': 'PASS: "also", "even when", "because" and "while" say each relation',
   'Q6': 'PASS: what it is, how to use it, what it does, then the waters like it',
   'Q7': 'PASS: each fact bears on whether and how they use it now',
   'Q8': 'PASS: the waters are all stabilizers that keep the trip',
   'Q9': 'PASS: one step a sentence',
  },
}
R['h42-25'] = {
  'section': 'When the Goal Is to Stop a Psychedelic Trip (2 of 2): A Final Trip Killer: Niacin (a Form of Vitamin B3)',
  'reader': 'someone who wants a trip to end, without beach morning glory to hand, deciding whether to use flushing niacin, what it feels like and what to avoid',
  'sentences': [
   ('they know beach morning glory is not shown to end MDMA', 'it ends the part on beach morning glory', 'none: it closes the part before'),
   ('they know MDMA has its own branch, with what it centers on', 'where MDMA goes instead', 'MDMA remains'),
   ('they know the last trip killer is niacin', 'the next heading', 'none: a heading, naming the next remedy'),
   ('they know flushing niacin has ended trips for him and friends, though he prefers beach morning glory', 'it opens the remedy under its heading', 'none: the first sentence under its heading'),
   ('they know why it is here: most people lack beach morning glory', 'why it is included', 'I include it because'),
   ('they know doctors have used it for psychosis and how it seems to act', 'what is behind it', 'Niacin has been used'),
   ('they know where to read the clinical literature', 'where the evidence is', 'The clinical literature'),
   ('they know the side effects come next', 'after what it does', 'none: a label in the remedy'),
   ('they know the flush feels like an itchy sunburn heat', 'the first side effect', 'none: the first item under its label'),
   ('they know the flush is normal and some hate it', 'what to make of it', 'This is normal'),
   ('they know it can cause heartburn', 'the next side effect', 'none: a list item, the next one under its label'),
   ('they know it brings drowsiness with poor sleep', 'the next side effect', 'none: a list item, the next one under its label'),
   ('they keep to small single doses, especially with liver problems, alcohol or medicines', 'the risk', 'none: a list item, the next one under its label'),
   ('they know other forms of B3 relax less reliably', 'which form to use', 'Other forms of vitamin B3'),
   ('they know niacinamide can relax or focus depending on the state', 'one of those forms', 'Niacinamide'),
   ('they avoid sustained-release and non-flush niacin', 'which forms to avoid', 'Avoid'),
   ('they know that once the body is settled, someone still needs to sit with what the trip opened up, which is where tripsitting begins',
    'the end of the remedies, handing on to tripsitting', 'Even once the body is stable'),
  ],
  'placement': 'the end of When the Goal Is to Stop a Psychedelic Trip, and of the remedies: niacin last, then the bridge to tripsitting',
  'why_reading': 'it tells someone who wanted beach morning glory for MDMA that it is not shown to work there',
  'same_point': 'none: read the section from its niacin heading to the next for niacin; the bridge is said once, here',
  'questions': {
   'Q1': 'PASS: each sentence opens on its point; the bridge opens on when it applies',
   'Q2': "PASS: the instructions (avoid sustained-release and non-flush forms) are the reader's own acts",
   'Q3': 'PASS: "flushing niacin", "sustained-release niacin", "non-flush hexanicotinate" say which',
   'Q4': 'PASS: niacin is explained in its heading (a form of vitamin B3); niacinamide as another form',
   'Q5': 'PASS: "because", "although" and "Even once" say each relation',
   'Q6': 'PASS: what it does, why it is here, side effects, forms, then the hand-off',
   'Q7': 'PASS: each fact bears on whether and how they use niacin now',
   'Q8': 'PASS: niacin is a trip killer; the bridge belongs at the end of the remedies',
   'Q9': 'PASS: one step a sentence',
  },
}

R['anchor-a1'] = {
  'section': 'Get One Human Anchor',
  'reader': 'someone tripsitting, or about to, deciding who should be with the person in a hard trip, and when to bring in more help',
  'sentences': [
   ('they know this part is about having one person as the anchor', 'the heading', 'none: the section heading itself'),
   ('they know being alone with a frightened or over-certain mind can make it worse', 'it opens the section under its heading',
    'none: the first sentence under its heading'),
   ('they know a crowd explaining it to them, or panicking, makes it worse too', 'the other way it goes wrong', 'So can a crowd'),
   ('they have one calm person stay and take the lead', 'what follows from both ways it goes wrong', 'So have one calm person'),
   ('they know one person has limits', 'the limit on the answer just given', 'though'),
   ('they bring in another calm adult or a crisis professional when it gets too much, at once if there is any risk of violence or self-harm',
    'what to do when the limit is reached', 'If fatigue or logistics'),
  ],
  'placement': "Get One Human Anchor's opening, before the script for the person in the altered state and the 3 a.m. plan",
  'why_reading': 'it tells someone deciding who should be there that being alone can make a bad trip worse',
  'same_point': "none: read Get One Human Anchor to the next heading for who is there; For the Person Helping is how the anchor acts",
  'questions': {
   'Q1': 'PASS: the reason first (alone or a crowd makes it worse), then what to do',
   'Q2': "PASS: each instruction is the helper's act (have one person lead, bring in another)",
   'Q3': 'PASS: "one more calm adult or a crisis professional" says who',
   'Q4': 'PASS: no term needs explaining',
   'Q5': 'PASS: "So can", "So have", "though" and "If" say each relation',
   'Q6': 'PASS: the two ways it goes wrong, the answer, its limit, then what to do at the limit',
   'Q7': 'PASS: each sentence bears on who is with them now',
   'Q8': 'PASS: all of it is about who is there',
   'Q9': 'PASS: the crowd\'s four acts said as two; the conditions as one sentence with the firm one last',
  },
}
R['harm-b1'] = {
  'section': "Risk of Harm: When Peer Support Isn't Enough",
  'reader': 'someone sitting with a person in a hard trip, deciding whether it has gone past what they can handle and they need urgent help now',
  'sentences': [
   ('they know this part is when to get urgent help', 'the heading', 'none: the section heading itself'),
   ("they get urgent help at once if someone might hurt anyone, or can't be kept physically safe, like heading for roads, high places or water",
    'it opens the section under its heading', 'none: the first sentence under its heading'),
   ('they get help too for voices telling the person what to do, or a fixed terrifying belief they are acting on', 'more reasons of the same kind',
    'are a reason too'),
   ('they get help as fast for violence, or confusion so severe the person is unreachable', 'more reasons', 'Get help just as fast'),
   ('they get help for dangerous physical symptoms or sleep loss that has broken judgment', 'the body\'s reasons', 'count, and so does'),
   ("they get help whenever it's more than they can safely handle", 'the last reason, which needs no other', 'And if it'),
  ],
  'placement': "Risk of Harm's first paragraph, before which services to call",
  'why_reading': 'it tells a sitter the first reasons to get urgent help right away',
  'same_point': "When to Bring In Outside Help lists the medical reasons; this part is the reasons of harm, said here once",
  'questions': {
   'Q1': 'PASS: the instruction first (get urgent help), then each reason',
   'Q2': "PASS: each instruction is the sitter's act",
   'Q3': 'PASS: "roads and high places, or water", "voices telling them what to do" say which',
   'Q4': 'PASS: "command voices" said as voices telling them what to do',
   'Q5': 'PASS: "too", "just as fast", "and so does", "And if" say each relation',
   'Q6': 'PASS: harm and safety first, then the mind, violence and confusion, the body, then the sitter\'s limit',
   'Q7': 'PASS: each reason bears on calling now',
   'Q8': 'PASS: every item is a reason to get urgent help',
   'Q9': 'PASS: the nine conditions in five sentences, two at most a sentence',
  },
}
FORMS3 = R['h42-25']['sentences'][13:16]
for _k, _bridge in (('h42-25-p2', ("they know that once the body is settled, someone still needs to sit with what the trip stirred up, which is where tripsitting begins",
                                   'the end of the remedies, handing on to tripsitting', 'Once the body has settled')),
                    ('h42-25-p3', ("they know that even once the body is calm, someone still needs to sit with what the trip stirred up, which is where tripsitting begins",
                                   'the end of the remedies, handing on to tripsitting', 'Even when the body')),):
    R[_k] = dict(R['h42-25'])
    R[_k]['sentences'] = FORMS3 + [_bridge]
    R[_k]['why_reading'] = 'it tells someone reaching for vitamin B3 which forms relax less reliably'
    R[_k]['placement'] = R['h42-25']['placement'] + ' (the forms paragraph and the bridge checked together, E343, E349)'
    NEEDED[_k] = {'reader': NEEDED['h42-25']['reader'] + "; the bridge's job (handing on to tripsitting) is the same in this wording, which only drops the list",
                  'unneeded': ['Other forms of vitamin B3 seem less reliable for relaxation.'],
                  'kept': {'Other forms of vitamin B3 seem less reliable for relaxation.': NEEDED['h42-25']['kept']['Other forms of vitamin B3 seem less reliable for relaxation.']}}

R['harm-b2'] = {
  'section': "Risk of Harm: When Peer Support Isn't Enough",
  'reader': 'someone sitting with a person in a hard trip, deciding whether it has gone past what they can handle and they need urgent help now',
  'sentences': [
   ('they know this part is when to get urgent help', 'the heading', 'none: the section heading itself'),
   ('they know there is a limit to what peer support can carry', 'it opens the section under its heading', 'none: the first sentence under its heading'),
   ("they get urgent help at once if someone might hurt anyone, or can't be kept physically safe, like heading for the road, the water or somewhere high",
    'the first reasons past that limit', 'If it looks like'),
   ('they call for voices telling the person what to do, or a fixed terrifying belief they are acting on', 'more reasons of the same kind', 'are a reason to call'),
   ('they call right away if it turns violent', 'the most urgent reason, said alone', 'If it turns violent'),
   ('they call for confusion so severe the person is unreachable, broken judgment from no sleep, or the dangerous physical symptoms listed above',
    'the reasons of the mind and body', 'that\'s past what a sitter can carry too'),
   ("they call whenever it's more than they can safely handle", 'the last reason, which needs no other', 'And if it'),
  ],
  'placement': "Risk of Harm's first paragraph, after the Call medics list it points back to and before which services to call",
  'why_reading': 'it tells a sitter there is a point where peer support is not enough, which the next sentence names',
  'same_point': "the dangerous physical symptoms are the Call medics list just above: said there in full, pointed to here (lesson 06a)",
  'questions': {
   'Q1': 'PASS: the limit first, then the moment to call, each reason after it',
   'Q2': "PASS: each instruction is the sitter's act (get urgent help, call)",
   'Q3': 'PASS: "the road or the water, or climbing somewhere high", "voices telling them what to do" say which',
   'Q4': 'PASS: "command voices" said as voices telling them what to do',
   'Q5': 'PASS: "If", "and so is", "too" and "And if" say each relation',
   'Q6': 'PASS: harm and safety, the mind, violence, then confusion, sleep and the body, then the sitter\'s limit',
   'Q7': 'PASS: each reason bears on calling now',
   'Q8': 'PASS: every item is a reason to get urgent help',
   'Q9': 'PASS: one or two reasons a sentence, violence alone',
  },
}
R['h42-41-p'] = {
  'section': 'Dealing With Shadow Thoughts',
  'reader': 'someone mid-trip, flooded with frightening shadow thoughts, deciding what to do with them right now',
  'sentences': [
   ('they know he is not saying opposites are needed to understand anything', 'it continues the point before, on shadows co-arising',
    'none: it opens the paragraph by setting his view apart'),
   ('they see why: a baby feels love or hate, not both', 'the example', 'A hated baby'),
   ('they know the mind still pairs two sides in its concepts, which is why shadows come up', 'what he does say', 'however'),
   ("they don't take a shadow thought as the truth about them, or push it down", 'what to do with them during a trip', 'While you\'re still tripping'),
   ("they don't confess it to everyone or make it a permanent diagnosis yet", 'more of what can wait', 'can wait, and so can'),
   ("they notice it as a thought and a feeling, intense but not all of them", 'what to do instead', 'instead'),
   ('they come back to the room, the body, a person, time and love', 'where to go from noticing', 'Then'),
  ],
  'placement': 'Dealing With Shadow Thoughts, its last paragraph before the Joker Poem: what to do with shadow thoughts during a trip',
  'why_reading': 'it tells someone with shadow thoughts that he is not saying they need their opposite to understand anything',
  'same_point': 'none: read Dealing With Shadow Thoughts to the next heading for what to do with them; the menu named in the last sentence is the Grounding Menu',
  'questions': {
   'Q1': 'PASS: each sentence opens on its point; the during-a-trip lines on when they apply',
   'Q2': "PASS: each instruction is the reader's own act",
   'Q3': 'PASS: "everyone in the room", "some permanent diagnosis" say which',
   'Q4': 'PASS: "Hermetic claim" is said by what it claims',
   'Q5': 'PASS: "however", "either", "can wait, and so can", "instead" and "Then" say each relation',
   'Q6': 'PASS: his view, what not to do yet, what to do instead, where to go next',
   'Q7': 'PASS: each line bears on what they do with a shadow thought now',
   'Q8': 'PASS: all of it is about shadow thoughts',
   'Q9': 'PASS: the four don\'ts in two sentences',
  },
}
R['h42-08-fix3'] = dict(R['h42-08'])
R['h42-08-fix3']['sentences'] = R['h42-08']['sentences'][:-1] + [
    ("they keep the rescue medicine first while the seizure goes on, and use DMSO, if at all, as an adjunct remedy alongside it, knowing it's experimental",
     'what the mixed evidence means for them', 'While a seizure continues')]
R['h42-08-fix3']['questions'] = dict(R['h42-08']['questions'],
    Q4='PASS: "rescue medicine" is the section\'s own term from its first part; "adjunct remedy" is his (KEEP-AS-IS K12), what it is an adjunct to said in the same sentence')
NEEDED['h42-08-fix3'] = dict(NEEDED['h42-08-fix2'], reader=NEEDED['h42-08-fix2']['reader'] + "; fix3 differs only in the last sentence's wording ('treat DMSO as a plausible adjunct remedy', his words), the same job")

R['harm-b3'] = dict(R['harm-b2'])
R['harm-b3']['sentences'] = [
   ('they know this part is when to get urgent help', 'the heading', 'none: the section heading itself'),
   ('they know a sitter can carry a lot, but not everything', 'it opens the section under its heading', 'none: the first sentence under its heading'),
   ('they get urgent help the moment they think someone might hurt anyone, without waiting to be sure', 'the first reason past that limit', 'The moment you think'),
   ("they get help if they can't keep the person physically safe, like heading for the road, the water or somewhere high", 'the next reason', 'too'),
   ('they get help for voices telling the person what to do or a terrifying belief they act on, and call at once for violence', 'the reasons of the mind, and violence', 'It\'s time as well'),
   ('they get help when the person is so severely confused they are unreachable', 'confusion', 'Someone so severely confused'),
   ('they get help for dangerous body signs like trouble breathing or overheating, or sleep loss that has broken judgment', 'the body', 'So does'),
   ("they call when they catch themselves wondering whether it's too much", 'the sitter\'s own doubt, the last reason', 'If you find yourself wondering'),
]
R['harm-b3']['why_reading'] = 'it tells a sitter there is a limit to what they can carry, which the next sentences name'
R['harm-b3']['same_point'] = "the Call medics list just above has the body's signs in full; two of them are named here so the reader needn't look back (lesson 06a)"
R['harm-b3']['questions'] = dict(R['harm-b2']['questions'],
    Q5='PASS: "too", "as well", "So does" and "If you find yourself" say each relation',
    Q9='PASS: one or two reasons a sentence, said in different shapes')


# The second try of Active Seizure 2: the same sentences, its last one new
R['h42-08-fix2'] = dict(R['h42-08'])
R['h42-08-fix2']['sentences'] = R['h42-08']['sentences'][:-1] + [
    ("they keep the rescue medicine first while the seizure goes on, and use DMSO, if at all, alongside it, knowing it's experimental",
     'what the mixed evidence means for them', 'While a seizure continues')]
R['h42-08-fix2']['questions'] = dict(R['h42-08']['questions'],
    Q2="PASS: the one instruction is the reader's: the rescue medicine first while a seizure continues, DMSO alongside it if at all",
    Q5='PASS: "But" turns to the counter-reports, "so" draws each conclusion; the last sentence draws on the mixed evidence and says what it means while a seizure goes on')

# Round 34's ADJUNCT card: the DMSO paragraph as it would read with fix2's last sentence (the page's form of N-CBD-3)
R['ADJUNCT'] = dict(R['h42-08-fix2'])
R['ADJUNCT']['sentences'] = R['h42-08-fix2']['sentences'][-2:]
R['ADJUNCT']['why_reading'] = "it tells someone deciding about DMSO during a seizure what the animal evidence found, both ways"
R['ADJUNCT']['placement'] = "What Else May Help's last paragraph, after cannabis and topical CBD (round 34's ADJUNCT card)"
NEEDED['ADJUNCT'] = {'reader': NEEDED['h42-08-fix2']['reader'] + '; this is that unit\'s DMSO paragraph, read there in place',
                     'unneeded': [], 'kept': {}}


def test_path(key):
    base, _, fix = key.partition('-fix')
    return HERE / ('TEST-%s.txt' % key if fix else 'TEST-%s.txt' % key)


def fill(key):
    text = HERE / ('TEST-%s.txt' % key)
    out = HERE / ('TEST-%s.receipt.json' % key)
    d = R[key]
    subprocess.run([sys.executable, str(SR), 'make', str(text), '--section', d['section'], '--reader', d['reader'],
                    '--out', str(out)], check=True, capture_output=True)
    r = json.loads(out.read_text(encoding='utf-8'))
    assert len(r['sentences']) == len(d['sentences']), (key, len(r['sentences']), len(d['sentences']))
    for i, (s, (payoff, follows, link)) in enumerate(zip(r['sentences'], d['sentences'])):
        s['payoff'], s['follows'] = payoff, follows
        if i:
            s['link'] = link
    r['placement'] = d['placement']
    r['opens']['why_reading'] = d['why_reading']
    r['same_point'] = d['same_point']
    r['questions'] = d['questions']
    if key in NEEDED:
        r['needed'] = NEEDED[key]
    if d.get('late_ok'):
        r['late_ok'] = d['late_ok']
    out.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    print(key, (c.stdout + c.stderr).strip().splitlines()[-1] if (c.stdout + c.stderr).strip() else c.returncode)
    if c.returncode:
        print((c.stdout + c.stderr).strip())



def para_entry(key):
    """A paragraph test (KEY-p, E343) takes its unit's entries for the same sentences, in the same order; the paragraph's
    first sentence is said to follow the paragraph before it in the unit. The needed read is the unit's, which read these
    sentences in place, restricted to them."""
    unit = key[:-2]
    d = R[unit]
    sk = HERE / ('TEST-%s.receipt.json' % unit)
    unit_sents = [x['s'] for x in json.loads(sk.read_text(encoding='utf-8'))['sentences']]
    entries = dict(zip(unit_sents, d['sentences']))
    import subprocess as sp
    tmp = HERE / ('.%s.skeleton.json' % key)
    sp.run([sys.executable, str(SR), 'make', str(HERE / ('TEST-%s.txt' % key)), '--section', d['section'], '--reader',
            d['reader'], '--out', str(tmp)], check=True, capture_output=True)
    sents = [x['s'] for x in json.loads(tmp.read_text(encoding='utf-8'))['sentences']]
    tmp.unlink()
    e = dict(d)
    e['sentences'] = [entries[x] for x in sents]
    e['why_reading'] = PARA_WHY[key]
    e['placement'] = d['placement'] + ' (checked here by itself with the paragraph it leans on, E343, E349)'
    if unit in NEEDED:
        n = NEEDED[unit]
        NEEDED[key] = {'reader': n['reader'] + '; this paragraph test is part of that unit, read there in place',
                       'unneeded': [x for x in n['unneeded'] if x in sents],
                       'kept': {k: v for k, v in n['kept'].items() if k in sents}}
    return e


PARA_WHY = {
 'h42-20-p': 'it tells someone checking DMSO that what follows is who should be careful with it',
 'h42-22-p': 'it tells someone whose trip is too strong that touching ocean water can soothe it',
 'h42-25-p': 'it tells someone reaching for vitamin B3 which forms relax less reliably',
}
for _k in PARA_WHY:
    if (HERE / ('TEST-%s.txt' % _k)).exists() and (HERE / ('TEST-%s.receipt.json' % _k[:-2])).exists():
        R[_k] = para_entry(_k)


if __name__ == '__main__':
    for k in sys.argv[1:] or list(R):
        fill(k)
