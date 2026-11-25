#!/usr/bin/env python3
"""build_review.py - the marking page of 2026-11-25 for the Self-Hypnosis guide: what the guide would gain from the two
guides it is built on (inner child, somatic), four places where it and the inner child guide now differ, his answer 7 b
(breathing the somatic guide's way) as a whole paragraph, and the section Joel wrote that day, each as a card in the whole
guide.

  python3 articles/inner-signal/experiments/toc-20261123/review/build_review.py

Reads (never writes) from the folder above this one:
  AFTER.md                                the guide as it reads after the contents edit: the whole article the page shows
  catchup/CARRYOVERS-DRAFT.json           the drafted additions (C14 and C15 are left out: the guide already says them;
                                          C11 is a question, not an addition: Pangram read its sentence as AI in its
                                          section twice, see ASK_INSTEAD)
  catchup/CATCHUP-INNER-CHILD.json        the comparison items (C03, C06, C08 and C18 become questions)
  catchup/SECTIONS-*-20261125.json, LIVE-POST-META-*-20261125.json   the two other guides as they are live, and their posts
  PROPOSAL-FINAL.json                     this guide's section ids and their headings as they are in AFTER.md
  pangram/SEC-N001-his.txt                his new section, word for word
  pangram/SEC-S122-7b-after.txt           "Breathe, Relax & Flow" as it would read with his answer 7 b (the somatic guide's
                                          way of breathing), and pangram/receipts/R-S122-7b-b.json, its making-sense receipt
  review/READINGS.json (optional)         {"<card id>": {"read": "Human Written, 1 window, High", "link": "https://www.pangram.com/history/...",
                                          "note" (optional): what was read}}: each goes on its card as "tested" (a card
                                          with a change only; one reading for two cards is given under both ids); run this
                                          script again when the file appears. Q7b and N001 carry their readings already;
                                          an entry for either replaces it. C11's question needs its entry

Writes, all in this folder:
  ARTICLE.md              AFTER.md with only <!-- CUT --> / <!-- /CUT --> lines added, around the long stretches that hold
                          no card (the page folds them into a box that opens); it is the page's Markdown ("article"), and
                          AFTER.md is "whole". Not written when nothing is long enough to fold.
  REVIEW.json             the review (joel-suggestion-review-v1)
  REVIEW.html, REVIEW-artifact.html   the page, from `suggestion_review.py page ... --artifact ...` after `check` passes
  CARDS.md                the same cards as a Markdown page GitHub renders

Every place is found by its words (the draft's anchor sentence, the comparison's quote), never by a block number, so the
script can run again after AFTER.md changes. What a card says this guide already has elsewhere is checked against the
article (SAID below), and the card texts are tied to the drafts they were written from (WRITTEN_FOR): if a draft changes,
the script stops and names the card whose wording needs reading again.
"""
import datetime
import difflib
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
T = HERE.parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import section_links as sl  # noqa: E402
import suggestion_review as sr  # noqa: E402

REL = 'articles/inner-signal/experiments/toc-20261123/'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
SUBSTACK = 'https://ibogaqueen.substack.com'
LIVE_DAY = '2026-11-25'
SKIPPED = ('C14', 'C15')
NIBBANA = 'https://ibogaqueen.substack.com/i/209400477/who-gets-reborn'
NIBBANA_WORDS = 'more info about rebirth in my nibbana guide'
N001_HEADING = 'Past Life & Ancestral Trauma'
N001_AFTER = 'Stabilize, Then Interpret'
N001_BEFORE = 'H: Demons, Jinn & Presences'
# the text Pangram read (pangram-ledger.jsonl, IS-toc-N001): his five paragraphs, no heading, the file's text stripped
N001_SHA = '95aa99e956f499822d34a81debd8cbf858f97f6b11a270bedf751e773df3f2d5'
N001_READ = ('Human Written, 1 window, High (453 words)', 'https://www.pangram.com/history/7c92d0c3-fd89-4f35-b3db-0672bbcb36f9')
CLINIC = 'Do These With a Clinician'
EDITORS_SENTENCE = ('If what you\'re going back for is trauma from this life, though, that is the regression I\'d do with a '
                    'clinician (see “Do These With a Clinician”).')
EDITORS_AFTER = 'In fact, they might be more confused than you, or confuse you.'
GUIDES = {'C': ('ic', 'the inner child guide', 'inner child'), 'M': ('so', 'the somatic guide', 'somatic')}
# His answer "7 b" (2026-11-25): the somatic guide's way of breathing in "Breathe, Relax & Flow" too. The paragraph as it
# would read is pangram/SEC-S122-7b-after.txt; these are the pieces it is checked against.
Q7B_SECTION = 'Breathe, Relax & Flow'
Q7B_STARTS = 'Try breathing less.'
Q7B_CAUTION = 'However, please don’t hold your breath until you are air hungry, which can make you more anxious in the short term.'
Q7B_NOSE = 'Breathe in small amounts through your nose and let it out quietly, through your nose too.'
Q7B_PAUSE = 'Only pause if that\'s comfortable.'
Q7B_IN = ['By simply pursing your lips together on exhale, you can slow down your exhale.',
          'Slower exhales, combined with not breathing more on inhales, lead to overall reduction in breathing.',
          'That slight oxygen hunger feels a bit anxiogenic for the first 20 seconds or so, but after that, you’ll feel much '
          'calmer.']
Q7B_IN_FROM = 'S008'      # the somatic guide's "Breathwork"
Q7B_MINE = ['Try the continuous breathing from Systema (a Russian martial art) too: it helps not just with relaxing, but with '
            'getting into trance and flow states more deeply.',
            'You can learn it from the best video on it I\'ve seen so far, and my somatic guide explains it more.']
Q7B_RECEIPT = 'pangram/receipts/R-S122-7b-b.json'
Q7B_READ = ('Human Written, 1 window, High (144 words)', 'https://www.pangram.com/history/4a0969c3-c90f-49f6-a720-1aa1770f21d3')

# The drafts and comparison items these card texts were written from (the first 12 hex digits of the SHA-256 of each item as
# JSON, keys sorted). A changed item stops the build: read the item again and bring the card's text below in line with it.
WRITTEN_FOR = {'C02': 'f1156160d7b9', 'C04': '5e31420539fb', 'C05': 'b20e3cdd6dfa', 'C09': '436806007a0e',
               'C10': '8c67cded1d75', 'C11': 'c2f25c335911', 'C12': '25c1bcfb6908', 'C13': 'ec252414955c',
               'C14': 'e8da978a705f', 'C15': 'a51d4ef1b4ee', 'C16': 'd71cf07774db', 'C17': '0cff86f999db',
               'M05': 'b323cd15012d', 'M06': '154fd0a765ee'}
WRITTEN_FOR_Q = {'C03': 'd91ea109f1e0', 'C06': '80495ddb3e88', 'C08': '7741a96680cb', 'C18': '4252d58e2035'}

TYPES = {
    'otherguide': {'label': 'From your other guides',
                   'about': 'A point your inner child guide or somatic guide makes that this guide lacks, added here in '
                            'that guide’s sentences.'},
    'differs': {'label': 'Said differently in your other guide',
                'about': 'A place where this guide and the inner child guide now say different things. A question: '
                         'nothing changes unless you say so.'},
    'youranswer': {'label': 'Your answer 7 b',
                   'about': 'Your answer to question 7 of 25 November (the somatic guide’s way of breathing here too), as '
                            'the whole paragraph it changes.'},
    'newsection': {'label': 'Your new section',
                   'about': 'The section you wrote on 25 November, shown where it would go.'},
}

# ---------------------------------------------------------------- the cards' own words
# In these texts {s:Heading} is a section of this guide (checked to be a heading of AFTER.md, kept unfolded on the page, shown
# in curly quotes) and {o:Sxxx} a section of the card's other guide (shown as a link to it in the live post).
# "said": [(heading, words)] what the card says this guide already has there; each is checked against AFTER.md.
# "absent": words the card says this guide doesn't have; checked too.
# "source": [(section id in the other guide, which part)] where the new words come from.
ADDS = {
    'C02': {
        'title': 'If it goes badly: the signs not to try the same thing again',
        'what': 'A new paragraph after the first paragraph of Appendix G, two sentences: the signs to reconsider trying the '
                'same thing again (going manic or psychotic, getting super paranoid, ending up worse afterward than '
                'before), and “Don’t try again until you understand what would make it safe.”',
        'stays': 'The first paragraph as it is, and the rest of the appendix.',
        'deciding': 'Whether the paragraph adds enough. {s:Getting Anxious?}, {s:When to Get Outside Help} and {s:Could It Be '
                    'Psychosis?} already name mania, psychosis and paranoia as reasons to stop going deeper and get help, so '
                    'the new part is its last sentence. “If you go manic” and “the same thing” lean on the paragraph '
                    'before for what was taken. Left out, to keep it to two sentences: what the inner child guide says '
                    'next (to look at the drug and the dosage, mindset and setting) and its link to your bad trips guide, '
                    'which this guide doesn’t mention. Whether to link from here to {o:S101} in the inner child guide, as '
                    'the comparison suggested, is yours to say.',
        'changed': 'nothing.',
        'source': [('S102', '')],
        'said': [('Getting Anxious?', 'mania-like symptoms'), ('When to Get Outside Help', 'manic or psychotic symptoms'),
                 ('Could It Be Psychosis?', 'more paranoid')],
        'absent': ['bad trip'],
    },
    'C04': {
        'title': '“Just meet it with love” becomes “listen to it and be patient”',
        'what': 'One sentence changes. Now: “If you feel resistance, just meet it with love.” It would read: “If you feel '
                'resistance, listen to it and be patient.”',
        'stays': 'The rest of the paragraph, word for word, with the sentence after it: “If you feel or see something, just '
                 'meet that with love as well.”',
        'deciding': 'Mostly whether that next sentence keeps “as well”: it used to point back to this sentence, and now it '
                    'points back to the sending of love, so “as well” could go. The caution itself is already in this '
                    'guide: {s:Stuck in Spiritual Bypass?} has the inner child guide’s sentence nearly whole (“they might '
                    'just need to see if you’re actually humble enough, and grateful enough for them, to listen to their '
                    'rejection and be patient”). This change stops the two-hand practice from telling the reader the '
                    'opposite. The inner child guide’s third point, that the view from above may be missing something, '
                    'isn’t brought into this practice: {s:Start From the Whole} already says it of the Higher Self '
                    '(“problems can also look like they were never problems at all from up there”).',
        'changed': 'this guide’s own opening (“If you feel resistance”) stays, and “listen to their rejection, be patient” '
                   'takes the place of “just meet it with love”, with “it” for “their rejection” because this sentence '
                   'speaks of resistance. Left out: “call BS” and “humble enough, and grateful enough”, which this guide '
                   'already has in {s:Stuck in Spiritual Bypass?}, and “your Higher View is missing the trees for the '
                   'forest”, because this guide has no “Higher View”.',
        'source': [('S059', '')],
        'said': [('Stuck in Spiritual Bypass?', 'they might just need to see if you’re actually humble enough, and grateful '
                                                'enough for them, to listen to their rejection and be patient'),
                 ('Stuck in Spiritual Bypass?', 'call BS')],
        'absent': ['Higher View'],
    },
    'C05': {
        'title': 'The Higher Self’s wisdom, “that can be followed mechanically”',
        'what': 'One sentence gains five words at its end. Now: “And I don’t think the Higher Self has any specific wisdom.” '
                'It would read: “And I don’t think the Higher Self has any specific wisdom that can be followed '
                'mechanically.”',
        'stays': 'The rest of the paragraph, word for word.',
        'deciding': 'Only whether you want the inner child guide’s fuller sentence here; the writer had no doubt about it. '
                    'Left out: that guide’s next point, that leaving all decisions to the Higher Self is spiritual '
                    'bypassing, because {s:The Guide} already calls overruling your inner child in the name of something '
                    'higher spiritual bypassing, and {s:An Oracle Isn’t an Order} says an inner answer isn’t an order.',
        'changed': 'this guide’s “And” stays where the inner child guide has “But where I part ways with IFS is”, since this '
                   'passage isn’t about IFS (Internal Family Systems). The rest is word for word.',
        'source': [('S151', '')],
        'said': [('The Guide', 'in the name of something higher (spiritual bypassing'),
                 ('An Oracle Isn’t an Order', 'that doesn\'t mean you need to treat it like an order')],
        'absent': [],
    },
    'C09': {
        'title': 'A critical voice may be trying to protect you',
        'what': 'A new paragraph after the section’s one paragraph, three sentences: a critical voice might be the inherited '
                'parent script or an outside influence, or it could be trying to protect you from rejection or failure; it '
                'may be pointing to a real problem in a cruel way; stay curious about its motivations and open to any '
                'kernels of truth, without accepting its insults and cruelty.',
        'stays': 'The section’s paragraph as it is.',
        'deciding': 'Whether the third sentence (“Stay curious ...”) stays, or only the caution of the first two. This guide '
                    'says something close about other parts, though not about the critic: {s:Love First, Trust Later} '
                    '(“there will likely be something true in what they are saying”), {s:"It Feels Fake"} (“there could be '
                    'something to it”) and {s:D: Anxiety, Body First}, on the anxious guard (“It can be right!”). The '
                    'parent-script paragraph in {s:"It Feels Fake"}, which the comparison also named, is left as it is.',
        'changed': 'the first two sentences are word for word. The third drops its opening, “We want to use the Mr. Rogers '
                   'reframing trick to”, because this guide doesn’t tell the Mr. Rogers story, and starts at “Stay curious”.',
        'source': [('S027', 'the first two sentences'), ('S028', 'the third')],
        'said': [('Love First, Trust Later', 'there will likely be something true in what they are saying'),
                 ('"It Feels Fake"', 'there could be something to it'), ('D: Anxiety, Body First', 'It can be right!'),
                 ('"It Feels Fake"', 'inherited parent script')],
        'absent': ['Rogers'],
    },
    'C10': {
        'title': 'Let a stray thought go',
        'what': 'Two sentences added at the end of the paragraph: let a stray thought go as just thinking, and a worry that '
                'just keeps asking to be reassured can go the same way, unless it’s your inner child asking.',
        'stays': 'The paragraph before them, word for word.',
        'deciding': 'Whether the two sentences sit right after “Still, notice it, and then look at what might be going on.” '
                    'They narrow that sentence; if the two read to you as pulling against each other, that sentence would '
                    'have to change too, and it is left as it is. The half about reassurance is partly in this guide '
                    'already: {s:Endless Processing?} says to allow a checking thought to be there without engaging with it '
                    'and get on with what you have chosen to do.',
        'changed': '“and come back to the room you’re in” is dropped: in this guide coming back to the room is the return '
                   'from hypnosis (the script in {s:Come All the Way Back} says “coming back to the room I am in now”), so '
                   'here it could read as ending the session. “your little one” became “your inner child”, the name this '
                   'section uses.',
        'source': [('S070', '')],
        'said': [('Endless Processing?', 'allow the thought to be there without engaging with it and get on with what you '
                                         'have chosen to do'),
                 ('Come All the Way Back', 'coming back to the room I am in now'),
                 ('Working With Your Guards', 'your inner child')],
        'absent': [],
    },
    'C12': {
        'title': 'If being alone was the hurt, call someone first',
        'what': 'Two sentences added in step A, after its first sentence: if being alone was a big part of what hurt during '
                'your childhood, call somebody now; and if you have no one who wants to listen, there are warmlines.',
        'stays': 'The rest of step A, word for word.',
        'deciding': 'Two things. “Warmlines” is explained only by the contrast with hotlines; the inner child guide says no '
                    'more about them, so nothing was added, and you may want to say what one is. And the place. A fresh '
                    'reader marked it: right after these two sentences, “Check how much grown-up you is really in the '
                    'room first.” reads as “before you call”, and “now, mess and all” comes before step A has said you '
                    'may be stuck as the frightened little boo. In the inner child guide the two sentences come after '
                    'the grown-up check. The other place here is the end of step A, after “Do what makes you feel adult '
                    'before you try to talk to little you.” I checked step A by itself with them there and it read '
                    '[AI Detected, 0.51 (144 words)](https://www.pangram.com/history/76e3b83c-f9a7-47af-8efe-ec73dd31bb2a), '
                    'but your own “If you answered "No," ...” sentence read AI in that check too, so it mostly shows '
                    'what a lettered step does when it is checked alone. The whole section has had its two tries. Say '
                    '“end of step A” in the comment if you want them there, and I check the section again with them '
                    'there. Nothing else in this guide says this.',
        'changed': 'nothing.',
        'source': [('S007', '')],
        'said': [],
        'absent': ['warmline'],
    },
    'C13': {
        'title': 'Don’t invent a child’s voice',
        'what': 'One sentence added after the second sentence of the paragraph: if you don’t hear a little kid talking in '
                'your head, don’t invent one.',
        'stays': 'The rest of the paragraph, word for word.',
        'deciding': 'Whether this guide needs the sentence, since two sections come close to it: {s:Do You Think in Words?} '
                    'says “ask” and “listen” don’t mean full sentences will come, and {s:Working With Your Guards} says '
                    'there’s no need to answer for a part. They also cover the rest of the inner child guide’s passage '
                    '(that “ask” can sound like waiting for a second voice to answer), so only this one sentence is '
                    'brought over.',
        'changed': 'nothing.',
        'source': [('S067', '')],
        'said': [('Do You Think in Words?', 'it doesn\'t mean they\'ll be saying full sentences to you'),
                 ('Working With Your Guards', 'No need to answer for that part')],
        'absent': [],
    },
    'C16': {
        'title': 'A test for counsel that turns into handing your power over',
        'what': 'Two sentences added at the end of the paragraph: they can know things you don’t and still be wrong for you '
                'to follow too much, and the test is whether the relationship makes you more grounded, truthful, and free.',
        'stays': 'The paragraph’s two sentences, and the Hearthwork paragraph after it.',
        'deciding': 'Whether the test goes here, or a pointer does the job. This guide already has ways to notice: {s:Keep '
                    'Your Adult in Charge} (“it can take a no and wait”) and the questions in {s:Are You Being Influenced?} '
                    '(“If I say no, what will the consequences be?”, “do I come away from them more present and grown up, '
                    'or less?”). So this says again, in other words, a test this guide has, and a pointer from here to '
                    '{s:Are You Being Influenced?} would do the same. That is why the inner child guide’s follow-up '
                    'questions (do they respect a no) and its signs of manipulation are left out. The “safe adult” '
                    'sentence in {s:No Adult Yet? Borrow One}, which the comparison also named, is left as it is.',
        'changed': 'the opening “But” is dropped. The rest is word for word.',
        'source': [('S019', '')],
        'said': [('Keep Your Adult in Charge', 'it can take a no and wait'),
                 ('Are You Being Influenced?', 'If I say no, what will the consequences be?'),
                 ('Are You Being Influenced?', 'do I come away from them more present and grown up, or less?'),
                 ('No Adult Yet? Borrow One', 'safe adult'), ('Take It to the Council', 'In Hearthwork')],
        'absent': [],
    },
    'C17': {
        'title': 'You don’t have to forgive first',
        'what': 'One sentence added after the second sentence of the paragraph: we don’t have to forgive first to get safe, '
                'set boundaries, hold someone accountable, get justice or get better.',
        'stays': 'The rest of the paragraph, word for word.',
        'deciding': 'Only whether you want it said here; the writer had no other doubt. The paragraph already says the '
                    'boundary stays and that they still have to answer for it. What it doesn’t say is that none of this '
                    'waits on forgiving.',
        'changed': '“you” became “we”, because this paragraph is written in “we”.',
        'source': [('S038', '')],
        'said': [('Forgiving Without Bypass', 'they still have to answer for it'),
                 ('Forgiving Without Bypass', 'Our boundary with them is crucial to maintain')],
        'absent': [],
    },
    'M05': {
        'title': 'Titration, pendulation and orientation',
        'what': 'One sentence added at the end of the paragraph, naming Peter Levine’s three concepts with the pool '
                'picture: titration, pendulation, and orientation (coming out of the pool, drying off, noticing you’re '
                'safe).',
        'stays': 'The paragraph before it, word for word.',
        'deciding': 'Whether one sentence on the closing step alone would be better. That is what the comparison asked for; '
                    'this sentence brings titration and pendulation with it, and the pool arrives with no lead-in, as it '
                    'does in the somatic guide. It names the closing step without telling the reader to do it, and no '
                    'instruction was written that the somatic guide doesn’t have. This guide has its own ways to finish: '
                    '{s:Come All the Way Back} is its return, and {s:When to Stop Scanning} and {s:Already Trancey?} say to '
                    'orient yourself by looking around. Titration and pendulation are already named and explained in '
                    '{s:Feels Like Too Much?} (“This is called pendulation, and approaching in smaller amounts is '
                    'titration.”), so only orientation and the pool picture are new here, and the sources appendix '
                    '({s:Body Awareness & Contact}) already credits Levine for both.',
        'changed': '“He” became “SE’s founder, Peter Levine,” because this section hasn’t named him; the name is from '
                   '“it’s founder, Peter Levine,” earlier in the same section there, without its apostrophe slip. The '
                   'rest is word for word.',
        'source': [('S009', '')],
        'said': [('When to Stop Scanning', 'orient yourself (look around'), ('Already Trancey?', 'Orient yourself by looking '
                                                                                               'around'),
                 ('Body Awareness & Contact', 'titration, pendulation'), ('Come All the Way Back', 'Then do a count up'),
                 ('Feels Like Too Much?', 'This is called pendulation, and approaching in smaller amounts is titration')],
        'absent': [],
    },
    'M06': {
        'title': 'Massage styles, from forceful to gentle',
        'what': 'Two sentences added after the bracketed cautions: massage styles run from super aggressive (Rolfing) to '
                'quite gentle (Swedish), and choose the level that feels right for you.',
        'stays': 'The rest of the paragraph, word for word.',
        'deciding': 'Where it goes, and the length. It sits after the bracketed cautions and before “You’ve got lots of '
                    'other options”, so the cautions stay next to the body parts they are about; straight after “Maybe get '
                    'a massage” is the other place for it. The paragraph was already long, and this adds two sentences. '
                    'The somatic guide doesn’t say to pick a gentle style for anxiety, only to choose the level that feels '
                    'right, so this doesn’t either. In the somatic guide “Rolfing” is a link, which would come over with '
                    'the word.',
        'changed': '“in that domain” is dropped: there it points back to a sentence about unravelling stored tension that '
                   'isn’t in this guide. The rest is word for word.',
        'source': [('S017', '')],
        'said': [('Calm the Body Directly', 'You’ve got lots of other options'),
                 ('Calm the Body Directly', 'Maybe get a massage')],
        'absent': [],
    },
}

# The four questions. {here} is the comparison's quote of this guide and {there} its quote of the inner child guide, both
# word for word; {o:Sxxx} links a section of the inner child guide. "there_also": (section id, words) quoted besides.
ASKS = {
    'C03': {
        'title': 'What takes warmth: not hitting back, or their trust?',
        'question': 'Here: “{here}” So here even not hitting back takes warmth. In the inner child guide ({o:S033}) you can '
                    'stop judging with no love coming yet: “{there}” There it is their trust that takes warmth. Bring this '
                    'guide in line with that, or do you mean it its own way here?',
        'why': 'A reader with no warmth yet gets a higher bar for the first step here than the inner child guide sets.',
        'there_also': [('S033', 'If the love still isn’t coming, you can at least stop judging your little one.')],
        'said': [],
    },
    'C06': {
        'title': 'Sort out which part it is, or not spend long on naming?',
        'question': 'This section is for a reader who already splits into too many parts, and it ends by giving them seven '
                    'questions for sorting: “{here}” The inner child guide now says ({o:S070}): “{there}” And in {o:S064}: '
                    '“Before you decide where it’s coming from, ask it what it’s trying to stop, or what it wants.” Bring '
                    'this paragraph in line with that, or is the sorting how you mean it in this guide?',
        'why': 'The two guides now give a reader who splits into too many parts opposite advice: sort each thing out, or '
               'don’t spend long naming it.',
        'there_also': [('S064', 'Before you decide where it’s coming from, ask it what it’s trying to stop, or what it '
                                'wants.')],
        'said': [('Start From the Whole', 'Some people make themselves too fragmented by starting to work with parts.')],
    },
    'C08': {
        'title': 'The Guide: someone you ask, or a job you do?',
        'question': 'Here the reader asks the Guide for direction, as if it were someone else: “{here}” In the inner child '
                    'guide ({o:S044}) the Guide is a job you do: “{there}” Make the Guide a job the reader does here too, or '
                    'is asking an inner figure how you mean it for hypnosis?',
        'why': 'This guide treats the Nurturer and the Protector as jobs the reader does, and in trance an inner figure’s '
               'answers are easier to take as orders.',
        'there_also': [],
        'said': [('When to Stop Scanning', 'Do you want to embody your Protector?')],
    },
    'C18': {
        'title': 'Who the three jobs come from',
        'question': 'The sources note says who the three jobs are not from, and stops there: “{here}” The inner child guide '
                    'now credits them ({o:S152}): “{there}” Under {o:S153} it names Daja’s work for the Nurturer and '
                    'Protector, and Key for adding the Guide. Credit them here too, or leave this note as it is?',
        'why': 'A reader of this guide’s sources learns only who the arrangement isn’t from.',
        'there_also': [('S153', 'Daja works with inner-child'), ('S153', 'the three grown-up jobs draw a lot from it'),
                       ('S153', 'she added The Guide')],
        'said': [],
    },
}
ASK_STAYS = 'The paragraph as it is, unless you say otherwise.'

# A drafted addition that goes to him as a question instead of an "add it" card: Pangram read its sentence as AI where it
# would go, in both places tried in the section, and the section's tries are spent (2026-11-25). The readings and their
# links are READINGS.json's entry for the card, which the question needs: {reading} below. {text} is the drafted sentence.
ASK_INSTEAD = {
    'C11': {
        'title': 'The ritual sentence reads AI here, twice',
        'question': 'The sentence from your inner child guide ({o:S089}, its last sentence) that would go here, after step '
                    'G: “{text}” I can’t find AI tells in this sentence, and “allowed to live” reads like you, but it '
                    'doesn’t pass in this section. Leave it out, since step G says something close, or tell me how '
                    'you’d say it here?',
        'why': 'What Pangram read: {reading} Everything else in the section reads Human in both tries, most of it at High '
               'confidence. This guide has a point close to it there: step G opens “Stop and rest before the caring '
               'turns into another performance”. What step G doesn’t say is the other half, that the exercises can '
               'become something you have to finish before you’re allowed to live; the writer who drafted this card '
               'called that the part this guide lacks.',
        'stays': 'The section as it is, without the sentence.',
        'advice': 'I’d leave it out for now rather than put in a sentence that reads AI. If you want the point here, write '
                  'it your way in the answer box and I’ll check that.',
        'source': [('S089', 'its last sentence')],
        'said': [('Don\'t Rush the Repair', 'G. Stop and rest before the caring turns into another performance')],
    },
}
ASK_ADVICE = '“In line” or “its own way” is answer enough.'


# ---------------------------------------------------------------- helpers

def fail(msg):
    raise SystemExit('build_review.py: ' + msg)


def load(rel):
    return json.loads((T / rel).read_text(encoding='utf-8'))


def item_sha(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest()[:12]


def sha256(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def shown(heading):
    """A heading in curly quotes, as the cards name it (a heading that is itself in straight quotes loses them)."""
    return '“%s”' % heading.strip('"')


def locate(bl, quote):
    """sr.find_quote, and once more with the space before a comma or full stop taken out: the comparison quoted the live
    post, where a link leaves that space ("adulthood , etc"), and AFTER.md has none."""
    try:
        return sr.find_quote(bl, quote)
    except ValueError:
        return sr.find_quote(bl, re.sub(r'\s+([,.;:])', r'\1', quote))


def md_esc(t):
    """T safe inside a Markdown paragraph."""
    return re.sub(r'([\\`*_\[\]<>~|])', r'\\\1', t)


def md_para(t):
    """An escaped paragraph that can't start a list, a heading or a quote of its own."""
    return re.sub(r'^(\d+)([.)])', r'\1\\\2', re.sub(r'^([-+#>])', r'\\\1', t))


def md_mark(t, mark):
    core = t.strip()
    if not core:
        return t
    return t[:len(t) - len(t.lstrip())] + mark + md_esc(core) + mark + t[len(t.rstrip()):]


def md_sides(old, s, e, kind, text):
    """(the paragraph OLD with the words that go struck through, the paragraph as it would read with the new words in
    bold), as Markdown. An addition goes in after old[s:e], whole; a change replaces old[s:e] with TEXT, and what the two
    sentences share at their start and end is left unmarked."""
    if kind != 'change':
        return md_para(md_esc(old)), md_para(md_esc(old[:e]) + ' ' + md_mark(text, '**') + md_esc(old[e:]))
    a, b = sr.tokens(old[s:e]), sr.tokens(text)
    p = 0
    while p < min(len(a), len(b)) and a[p] == b[p]:
        p += 1
    q = 0
    while q < min(len(a), len(b)) - p and a[len(a) - 1 - q] == b[len(b) - 1 - q]:
        q += 1
    head, tail = md_esc(old[:s] + ''.join(a[:p])), md_esc(''.join(a[len(a) - q:]) + old[e:])
    return (md_para(head + md_mark(''.join(a[p:len(a) - q]), '~~') + tail),
            md_para(head + md_mark(''.join(b[p:len(b) - q]), '**') + tail))


def md_ops(old, ops):
    """(the paragraph OLD with the words that go struck through, the paragraph as it would read with the new words in
    bold), as Markdown, for OPS: [(words of OLD, in its order, what takes their place or "")]."""
    now, new, pos = [], [], 0
    for gone, comes in ops:
        k = old.index(gone, pos)
        now += [md_esc(old[pos:k]), md_mark(gone, '~~')]
        new += [md_esc(old[pos:k]), md_mark(comes, '**')]
        pos = k + len(gone)
    now.append(md_esc(old[pos:]))
    new.append(md_esc(old[pos:]))
    return md_para(''.join(now)), md_para(''.join(new))


def md_linked(t):
    """Insert text for CARDS.md: its Markdown links kept as links, the rest escaped."""
    out, pos = [], 0
    for m in sr.LINK.finditer(t):
        out.append(md_esc(t[pos:m.start()]))
        out.append('[%s](%s)' % (md_esc(m.group(1)), m.group(2)))
        pos = m.end()
    out.append(md_esc(t[pos:]))
    return md_para(''.join(out))


def quote_block(paras):
    return '\n>\n'.join('> ' + p for p in paras)


# ---------------------------------------------------------------- build

def main():
    after_md = (T / 'AFTER.md').read_text(encoding='utf-8')
    flat = sr.blocks(after_md, whole=True)
    if any(b['kind'] == 'cut' for b in flat):
        fail('AFTER.md has CUT lines of its own')
    drafts = {d['id']: d for d in load('catchup/CARRYOVERS-DRAFT.json')}
    comp = {x['id']: x for x in load('catchup/CATCHUP-INNER-CHILD.json')}
    prop = {x['id']: x for x in load('PROPOSAL-FINAL.json')}
    other = {'ic': {x['id']: x for x in load('catchup/SECTIONS-inner-child-%s.json' % LIVE_DAY.replace('-', ''))},
             'so': {x['id']: x for x in load('catchup/SECTIONS-somatic-%s.json' % LIVE_DAY.replace('-', ''))}}
    post = {'ic': load('catchup/LIVE-POST-META-inner-child-%s.json' % LIVE_DAY.replace('-', '')),
            'so': load('catchup/LIVE-POST-META-somatic-%s.json' % LIVE_DAY.replace('-', ''))}

    # the drafts are the ones the card texts were written from
    if set(drafts) != set(WRITTEN_FOR):
        fail('the drafts are no longer %s: %s' % (', '.join(sorted(WRITTEN_FOR)), ', '.join(sorted(drafts))))
    for cid, d in drafts.items():
        if item_sha(d) != WRITTEN_FOR[cid]:
            fail('the draft of %s changed since its card was written (now %s): read it again, bring ADDS[%r] in line, '
                 'then put the new value in WRITTEN_FOR' % (cid, item_sha(d), cid))
    for cid, want in WRITTEN_FOR_Q.items():
        if item_sha(comp[cid]) != want:
            fail('the comparison item %s changed since its question was written (now %s): read it again, bring ASKS[%r] '
                 'in line, then put the new value in WRITTEN_FOR_Q' % (cid, item_sha(comp[cid]), cid))
    for cid in SKIPPED:
        if not drafts[cid]['doubt'].startswith('skip:'):
            fail('%s is left out because its writer marked it "skip:", and it no longer is' % cid)
    add_ids = [cid for cid in drafts if cid not in SKIPPED]
    if set(add_ids) != set(ADDS) | set(ASK_INSTEAD) or set(ADDS) & set(ASK_INSTEAD):
        fail('ADDS and ASK_INSTEAD have cards for %s, the drafts to show are %s'
             % (sorted(set(ADDS) | set(ASK_INSTEAD)), sorted(add_ids)))

    heads = {}
    for b in flat:
        if b['level']:
            heads.setdefault(b['text'], []).append(b['i'])
    named = set()            # the headings of this guide the cards name: each stays unfolded
    folded_already = []      # set once the folds are chosen: no card may name a new heading after that

    def here(heading):
        if len(heads.get(heading, [])) != 1:
            fail('“%s” is a heading of AFTER.md %d times, not once' % (heading, len(heads.get(heading, []))))
        if folded_already and heading not in named:
            fail('“%s” is named on a card after the folds were chosen' % heading)
        named.add(heading)
        return shown(heading)

    def there(guide, sid):
        """A link to a section of the other guide in its live post."""
        h = other[guide][sid]['heading']
        if not h or sl.unchecked(h):
            fail('no checked anchor for the %s guide\'s section %s (“%s”)' % (guide, sid, h))
        return '[%s](%s)' % (shown(h), sl.url(SUBSTACK, post[guide]['id'], h))

    def fill(text, guide):
        text = re.sub(r'\{s:([^{}]+)\}', lambda m: here(m.group(1)), text)
        return re.sub(r'\{o:(S\d+)\}', lambda m: there(guide, m.group(1)), text)

    def check_said(cid, pairs, absent=()):
        for heading, words in pairs:
            here(heading)
            if not any(words in b['text'] for b in flat if b['section'] == heading and not b['level']):
                fail('%s says “%s” has “%s”, and AFTER.md doesn\'t have it there' % (cid, heading, words))
        for words in absent:
            if words.lower() in after_md.lower():
                fail('%s says this guide doesn\'t have “%s”, and AFTER.md does' % (cid, words))

    # ---- where each card sits, in AFTER.md's own blocks
    touched = set()
    place = {}
    notes = []
    for cid in add_ids:
        d = drafts[cid]
        i, s, e = locate(flat, d['anchor'])
        b = flat[i]
        if prop[d['section']]['heading'] != b['section']:
            fail('%s: its anchor is under “%s”, and the draft says section %s (“%s”)'
                 % (cid, b['section'], d['section'], prop[d['section']]['heading']))
        old = b['text']
        if d['kind'] == 'change':
            new = old[:s] + d['text'] + old[e:]
        elif d.get('new_paragraph'):
            if e != len(old):
                fail('%s: a new paragraph after a sentence that doesn\'t end its paragraph' % cid)
            new = old + '\n\n' + d['text']
        elif d['kind'] == 'add':
            new = old[:e] + ' ' + d['text'] + old[e:]
        else:
            fail('%s: kind %r' % (cid, d['kind']))
        if new != d['paragraph_after']:
            # the draft was written on the live post; AFTER.md may differ from it outside the new words
            if d.get('new_paragraph'):
                fail('%s: the draft\'s paragraph before the new one is not AFTER.md\'s' % cid)
            a, c = sr.tokens(new), sr.tokens(d['paragraph_after'])
            diffs = [(''.join(a[i1:i2]), ''.join(c[j1:j2])) for op, i1, i2, j1, j2 in
                     difflib.SequenceMatcher(None, a, c, autojunk=False).get_opcodes() if op != 'equal']
            notes.append('%s: AFTER.md\'s paragraph differs from the draft\'s outside the new words (%s); the card shows '
                         'AFTER.md\'s paragraph with the new words in place'
                         % (cid, '; '.join('%r for %r' % (x, y) for x, y in diffs)))
        if d['text'] not in new:
            fail('%s: the new words are not whole in the paragraph as it would read' % cid)
        place[cid] = {'flat': i, 'span': (s, e), 'old': old, 'new': new}
        touched.add(i)
        if d.get('new_paragraph') and i + 1 < len(flat):
            touched.add(i + 1)
    for cid in ASKS:
        x = comp[cid]
        i, s, e = locate(flat, x['hypnosis_quote'])
        if prop[x['hypnosis_section']]['heading'] != flat[i]['section']:
            fail('%s: its quote is under “%s”, and the comparison says section %s' % (cid, flat[i]['section'],
                                                                                    x['hypnosis_section']))
        place[cid] = {'flat': i, 'span': (s, e), 'here': flat[i]['text'][s:e]}
        touched.add(i)
    here(N001_AFTER), here(N001_BEFORE), here(CLINIC)
    n_before = heads[N001_BEFORE][0]
    if flat[n_before - 1]['section'] != N001_AFTER or flat[n_before - 1]['level']:
        fail('“%s” no longer comes right after the section “%s”' % (N001_BEFORE, N001_AFTER))
    touched.update((n_before - 1, n_before))
    clinic = [b for b in flat if b['section'] == CLINIC and not b['level']]
    cq_start = 'If you want to deliberately do trauma-focused regression'
    cq_end = 'then you should do this with a trauma-informed clinician present.'
    if not clinic or not clinic[0]['text'].startswith(cq_start) or cq_end not in clinic[0]['text']:
        fail('the first paragraph of “%s” no longer holds the regression sentence' % CLINIC)
    place['N001-Q'] = {'flat': clinic[0]['i'], 'span': (0, clinic[0]['text'].index(cq_end) + len(cq_end))}
    touched.add(clinic[0]['i'])

    # ---- his answer 7 b: the paragraph as it is, and as the tested file has it
    here(Q7B_SECTION)
    q7 = [b for b in flat if b['section'] == Q7B_SECTION and not b['level'] and b['text'].startswith(Q7B_STARTS)]
    if len(q7) != 1:
        fail('“%s” no longer has one paragraph that starts “%s”' % (Q7B_SECTION, Q7B_STARTS))
    q7_old = q7[0]['text']
    q7_new = (T / 'pangram' / 'SEC-S122-7b-after.txt').read_text(encoding='utf-8').strip()
    q7_ops = [(' ' + Q7B_CAUTION, ''), (Q7B_NOSE + ' ' + Q7B_PAUSE, ' '.join(Q7B_IN))]
    built7 = q7_old
    for gone, comes in q7_ops:
        if built7.count(gone) != 1:
            fail('Q7b: “%s” is not in the paragraph of AFTER.md once' % gone.strip())
        built7 = built7.replace(gone, comes)
    if built7 != q7_new:
        fail('Q7b: pangram/SEC-S122-7b-after.txt is not AFTER.md\'s paragraph with the caution and the pause sentence out '
             'and the somatic guide\'s three sentences for the nose sentence: the card\'s account of it no longer holds')
    for s_ in Q7B_IN:
        if not any(s_ in p for p in other['so'][Q7B_IN_FROM]['paragraphs']):
            fail('Q7b: “%s” is not in the somatic guide\'s section %s' % (s_, Q7B_IN_FROM))
    for s_ in Q7B_MINE:
        if s_ not in q7_old or s_ not in q7_new:
            fail('Q7b: the Systema sentence “%s...” is not in the paragraph before and after' % s_[:40])
    if json.loads((T / Q7B_RECEIPT).read_text(encoding='utf-8')).get('text', '').strip() != q7_new:
        fail('Q7b: %s is not the receipt of the paragraph as it would read' % Q7B_RECEIPT)
    place['Q7b'] = {'flat': q7[0]['i'], 'old': q7_old, 'new': q7_new, 'ops': q7_ops}
    touched.add(q7[0]['i'])

    # ---- the cards' texts, with what they say checked against the article
    text = {}
    for cid in add_ids:
        spec, d = ADDS.get(cid) or ASK_INSTEAD[cid], drafts[cid]
        guide, guide_name, _ = GUIDES[cid[0]]
        check_said(cid, spec['said'], spec.get('absent', ()))
        for q in d['from_source']:
            if not any(q in p for sid, _ in spec['source'] for p in other[guide][sid]['paragraphs']):
                fail('%s: “%s...” is not in the %s section the card names' % (cid, q[:50], guide_name))
        if cid in ASK_INSTEAD:
            if d['kind'] != 'add' or d.get('new_paragraph'):
                fail('%s: its question is written for a sentence added inside a paragraph' % cid)
            text[cid] = {'question': fill(spec['question'], guide).replace('{text}', d['text'])}
            continue
        text[cid] = {k: fill(spec[k], guide) for k in ('what', 'stays', 'deciding', 'changed')}
    for cid, spec in ASKS.items():
        x = comp[cid]
        check_said(cid, spec['said'])
        if not any(x['source_quote'] in p for p in other['ic'][x['source_section']]['paragraphs']):
            fail('%s: the comparison\'s quote is not in the inner child guide\'s section %s' % (cid, x['source_section']))
        for sid, words in spec['there_also']:
            if not any(words in p for p in other['ic'][sid]['paragraphs']):
                fail('%s: “%s” is not in the inner child guide\'s section %s' % (cid, words, sid))
        q = fill(spec['question'], 'ic')
        text[cid] = {'question': q.replace('{here}', place[cid]['here']).replace('{there}', x['source_quote']),
                     'why': fill(spec['why'], 'ic')}
    if flat[place['C06']['flat']]['text'].count('?') != 7:
        fail('C06 says seven questions, and the paragraph no longer has seven')

    # ---- his new section
    n_text = (T / 'pangram' / 'SEC-N001-his.txt').read_text(encoding='utf-8')
    if sha256(n_text.strip()) != N001_SHA:
        fail('pangram/SEC-N001-his.txt is no longer the text Pangram read (%s): its reading and link don\'t apply; check '
             'it again and update N001_SHA and N001_READ' % N001_READ[1])
    n_paras = [p.strip() for p in re.split(r'\n\s*\n', n_text.strip())]
    if len(n_paras) != 5 or n_paras[-1].count(NIBBANA_WORDS) != 1 or n_paras[3].count(EDITORS_AFTER) != 1:
        fail('the new section is no longer five paragraphs with its link words and “%s”' % EDITORS_AFTER)
    one_doorway = 'One doorway into either of these would be to do an age regression hypnosis'
    no_pro = 'And you don\'t necessarily need to have a professional do this either.'
    if not n_paras[2].startswith(one_doorway) or not n_paras[3].startswith(no_pro):
        fail('the new section no longer says what the card quotes from it')
    n_inserts = [N001_HEADING] + n_paras[:-1] + [n_paras[-1].replace(NIBBANA_WORDS, '[%s](%s)' % (NIBBANA_WORDS, NIBBANA))]
    # the heading is his, as he typed it in his message of 11:18 UTC, with its one slip set right ("Past LIfe")
    msg = T / 'answers' / 'JOEL-20261125-1118-message.txt'
    typed = N001_HEADING.replace('Life', 'LIfe')
    if msg.exists() and re.search(r'^%s\s*$' % re.escape(typed), msg.read_text(encoding='utf-8'), re.M):
        n_heading_said = 'your heading, “%s” (you typed “%s”),' % (N001_HEADING, typed.split(' &')[0])
    else:
        n_heading_said = 'the heading “%s”' % N001_HEADING

    # ---- fold the long stretches that hold no card and that no card names
    sec, k, parent, stack = [], -1, {}, []       # a section: a heading and what follows it up to the next heading
    for b in flat:
        if b['level'] or k < 0:
            k += 1
            if b['level']:
                while stack and stack[-1][0] >= b['level']:
                    stack.pop()
                parent[k] = stack[-1][1] if stack else None
                stack.append((b['level'], k))
        sec.append(k)
    keep = {0, sec[min(1, len(flat) - 1)]}       # the opening, and the first headed section
    for i in touched:                            # a card's section, and the one before and after it
        keep.update((sec[i] - 1, sec[i], sec[i] + 1))
    for h in named:                              # each section a card names, so "Go to a section" finds it
        keep.add(sec[heads[h][0]])
    for s_ in sorted(keep):                      # and the headings each of those sits under, so none shows under the
        p = parent.get(s_)                       # wrong chapter
        while p is not None:
            keep.add(p)
            p = parent.get(p)
    folded_already.append(True)
    folds, i = [], 0
    while i < len(flat):
        if sec[i] in keep:
            i += 1
            continue
        j = i
        while j < len(flat) and sec[j] not in keep:
            j += 1
        run = flat[i:j]
        if (sum(1 for b in run if b['kind'] != 'embed') >= sr.CUT_MIN_BLOCKS
                and sum(len(b['text'].split()) for b in run) >= sr.CUT_MIN_WORDS):
            folds.append((i, j - 1))
        i = j
    raw = re.split(r'\n\s*\n', sr.join_split_links(after_md))
    raw_of = []                                   # the raw block each of AFTER.md's page blocks comes from
    for r, rb in enumerate(raw):
        if sr.para_numbers.visible(rb):
            raw_of.append(r)
        else:
            raw_of += [r] * len(sr.NOTE_RE.findall(rb))
    if len(raw_of) != len(flat):
        fail('AFTER.md\'s blocks don\'t line up with its paragraphs (%d, %d)' % (len(raw_of), len(flat)))
    starts = {raw_of[a]: True for a, _ in folds}
    ends = {raw_of[z]: True for _, z in folds}
    if folds:
        out = []
        for r, rb in enumerate(raw):
            if r in starts:
                out.append('<!-- CUT -->')
            out.append(rb.strip('\n'))
            if r in ends:
                out.append('<!-- /CUT -->')
        page_md = '\n\n'.join(out).rstrip('\n') + '\n'
        (HERE / 'ARTICLE.md').write_text(page_md, encoding='utf-8')
        art_file = REL + 'review/ARTICLE.md'
    else:
        page_md, art_file = after_md, REL + 'AFTER.md'
        if (HERE / 'ARTICLE.md').exists():
            (HERE / 'ARTICLE.md').unlink()
    bl = sr.blocks(page_md, whole=True)
    page_of, n = {}, 0
    for b in bl:
        if b['kind'] == 'cut':
            n += len(b['inner'])
        else:
            page_of[n] = b['i']
            n += 1
    if n != len(flat):
        fail('the page\'s blocks are not AFTER.md\'s (%d, %d)' % (n, len(flat)))

    def at(cid):
        i = page_of[place[cid]['flat']]
        s, e = place[cid]['span']
        if bl[i]['text'] != flat[place[cid]['flat']]['text']:
            fail('%s: its paragraph moved' % cid)
        return i, {'block': i, 'start': s, 'end': e}

    # ---- optional Pangram readings
    readings = {}
    rf = HERE / 'READINGS.json'
    if rf.exists():
        readings = json.loads(rf.read_text(encoding='utf-8'))
        for cid, r in readings.items():
            if not isinstance(r, dict) or not (r.get('read') or '').strip() or not sr.PANGRAM_LINK.search(r.get('link') or ''):
                fail('READINGS.json: %s needs "read" and a Pangram "link"' % cid)

    def tested(cid, default=None):
        r = readings.get(cid)
        if r:
            note = (r.get('note') or '').strip()
            if note and note[-1] not in '.!?':
                note += '.'
            return '[%s](%s)' % (r['read'].strip(), r['link'].strip()) + ('. ' + note if note else '')
        return default

    # ---- the cards
    cards = []
    for cid in add_ids:
        i, span = at(cid)
        if cid in ASK_INSTEAD:
            spec, reading = ASK_INSTEAD[cid], tested(cid)
            if not reading:
                fail('%s is a question because Pangram read its sentence as AI where it would go: READINGS.json must hold '
                     'its reading, with the links' % cid)
            cards.append({
                'id': cid, 'type': 'otherguide', 'advice': 'ask', 'title': spec['title'], 'spans': [span],
                'question': text[cid]['question'],
                'why': spec['why'].replace('{reading}', reading if reading[-1] in '.!?' else reading + '.'),
                'stays': spec['stays'], 'advice_note': spec['advice'], '_md': {'where': i}})
            continue
        spec, d = ADDS[cid], drafts[cid]
        guide, guide_name, guide_short = GUIDES[cid[0]]
        srcs = [(other[guide][sid]['heading'], part) for sid, part in spec['source']]
        src_plain = ' and '.join(shown(h) for h, _ in srcs)
        src_links = ' and '.join(there(guide, sid) + (' (%s)' % part if part else '') for sid, part in spec['source'])
        owner = ('his own: his %s guide, section%s %s, as it is live on %s'
                 % (guide_short, 's' if len(srcs) > 1 else '', src_plain, LIVE_DAY))
        if d['kind'] == 'change':
            lead, read = 'the new words are from %s, %s, as it is live on 25 November, put into this sentence', 'they read'
        elif len(re.findall(r'[.!?][)”"’]*(?=\s|$)', d['text'])) > 1:
            lead, read = 'your sentences from %s, %s, as it is live on 25 November, placed here', 'they read'
        else:
            lead, read = 'your sentence from %s, %s, as it is live on 25 November, placed here', 'it reads'
        card = {
            'id': cid, 'type': 'otherguide', 'advice': 'approve', 'title': spec['title'],
            'approve_label': 'use this wording' if d['kind'] == 'change' else 'add it',
            'spans': [span],
            'what': text[cid]['what'], 'why': d['why'], 'stays': text[cid]['stays'], 'deciding': text[cid]['deciding'],
            'owner_text': owner, 'whose': owner,
            'ask_because': 'his own: %s. Changed from how %s there: %s'
                           % (lead % (guide_name, src_links), read, text[cid]['changed']),
            'found_by': 'The comparison of this guide with %s as it is live on 25 November (item %s); a writer drafted the '
                        '%s from that guide’s sentences.' % (guide_name, cid,
                                                            'change' if d['kind'] == 'change' else 'addition'),
        }
        if d.get('new_paragraph'):
            card['inserts'] = [{'before': i + 1, 'kind': 'p', 'text': d['text'], 'seq': 1}]
            # shown as the paragraph before it and the new one, in the guide's own type (the tool's view of a lone insert
            # sets a whole paragraph in heading type)
            card['reads'] = [{'text': place[cid]['old']}, {'text': d['text'], 'new': [d['text']]}]
            card['reads_label'] = 'How it would read (the new paragraph is marked)'
        else:
            card['edits'] = [{'block': i, 'before': sr.block_text(bl, i), 'after': place[cid]['new']}]
        t = tested(cid)
        if t:
            card['tested'] = t
        card['_md'] = {'where': i, 'old': place[cid]['old'], 'span': place[cid]['span'], 'kind': d['kind'],
                       'text': d['text'], 'new_paragraph': bool(d.get('new_paragraph')), 'from': src_links,
                       'guide': guide_name, 'changed': text[cid]['changed'], 'read': read}
        cards.append(card)
    for cid, spec in ASKS.items():
        i, span = at(cid)
        x = comp[cid]
        cards.append({
            'id': cid, 'type': 'differs', 'advice': 'ask', 'title': spec['title'], 'spans': [span],
            'question': text[cid]['question'], 'why': text[cid]['why'], 'stays': ASK_STAYS, 'advice_note': ASK_ADVICE,
            '_md': {'where': i}})
    q7i = page_of[place['Q7b']['flat']]
    if bl[q7i]['text'] != q7_old:
        fail('Q7b: its paragraph moved')
    q7_spans = []
    for words in (Q7B_CAUTION, Q7B_NOSE + ' ' + Q7B_PAUSE):
        k = q7_old.index(words)
        q7_spans.append({'block': q7i, 'start': k, 'end': k + len(words)})
    q7_whose = ('his own: the paragraph is his (“%s” of the live post) and the three sentences that come in are from his '
                'somatic guide’s “%s”; the two Systema sentences in it are the editor’s, from the edit of %s'
                % (Q7B_SECTION, other['so'][Q7B_IN_FROM]['heading'], LIVE_DAY))
    cards.append({
        'id': 'Q7b', 'type': 'youranswer', 'advice': 'approve', 'approve_label': 'use this paragraph',
        'title': 'Breathing the somatic guide’s way: the whole paragraph',
        'spans': q7_spans,
        'edits': [{'block': q7i, 'before': sr.block_text(bl, q7i), 'after': q7_new}],
        # shown whole, with the sentences that come in marked: the tool's word-by-word view of three sentences swapped for
        # three others strikes and marks single words all through both
        'reads': [{'text': q7_new, 'new': [' '.join(Q7B_IN)]}],
        'reads_label': 'How it would read (the three sentences that come in are marked; the words that go are the ones '
                       'highlighted in the paragraph above)',
        'what': 'You answered “7 b”: the somatic guide’s way of breathing here too. Its three sentences, from %s, come in '
                'where the nose sentence was (“%s”): “%s” Two more sentences of yours, which belonged to breathing out '
                'through the nose, leave: “%s” and “%s”'
                % (there('so', Q7B_IN_FROM), Q7B_NOSE, ' '.join(Q7B_IN), Q7B_CAUTION, Q7B_PAUSE),
        'tested': tested('Q7b', 'The paragraph as it would read: [%s](%s).' % Q7B_READ),
        'why': 'Swapping only the nose sentence left two things wrong, which a fresh reader of the result found. “%s” was '
               'left hanging: it was the pause after breathing out through the nose, and with that sentence gone nothing '
               'says what is paused. And the two sentences about air hunger read opposite ways: the bracket says not to '
               'hold your breath until you are air hungry because it can make you more anxious, and three sentences later '
               'the somatic guide’s sentence says a slight oxygen hunger feels a bit anxiogenic for 20 seconds and then '
               'you feel much calmer. So the swap is offered as the whole paragraph.' % Q7B_PAUSE,
        'stays': 'The rest of the paragraph: “Try breathing less.”, the first sentence in the bracket, “Can you make your '
                 'breathing very quiet?”, the two Systema sentences, and the stop line at the end. The two Systema '
                 'sentences (“Try the continuous breathing from Systema ...” and “You can learn it from the best video '
                 '...”) are mine, from today’s edit; every other sentence in the paragraph is yours.',
        'deciding': 'This paragraph, or your own wording of it (Revise opens it for you). Two things a fresh reader '
                    'marked in it, both in your own lines. The stop line (“If you feel bad, dizzy, or panicky, or have '
                    'medical issues, stop.”) now follows a sentence that says to expect a bit of anxiety for the first 20 '
                    'seconds, and the paragraph is for someone who is panicked, so they can’t tell whether those 20 '
                    'seconds are a reason to stop. And “anxiogenic” (anxiety-causing) comes in unexplained, while the '
                    'sentence that said it in plain words (“can make you more anxious in the short term”) leaves.',
        'whose': q7_whose,
        'receipt': REL + Q7B_RECEIPT,
        'ask_because': 'downside: two sentences of yours leave with the nose-out way, and one of them is the caution not '
                       'to hold your breath until you are air hungry.',
        'found_by': 'Your answer “7 b” to the questions of 25 November, and a fresh reader’s read of the paragraph with '
                    'only the one sentence swapped.',
        '_md': {'where': q7i, 'old': q7_old, 'ops': q7_ops},
    })
    nb = page_of[n_before]
    conflict = ('%s says: “If you want to deliberately do trauma-focused regression (going backwards in your memory or '
                'imagination to times when you were younger) ... then you should do this with a trauma-informed clinician '
                'present”. This section says: “%s ... %s” A reader of both can’t tell which holds for going back after '
                'trauma.' % (here(CLINIC), one_doorway, no_pro))
    choices = ('Three ways to settle it:\n'
               '1. Approve: the section goes in as it is.\n'
               '2. Revise: add a sentence of your own (the box opens with the section).\n'
               '3. Say “use yours” in the comment, and this sentence of mine goes in after “%s”:\n“%s”\n'
               'It isn’t checked in Pangram yet; if you pick it, I check the section with it before it goes in.'
               % (EDITORS_AFTER, EDITORS_SENTENCE))
    n_owner = 'his own: typed in the chat on 2026-11-25 11:18 UTC'
    n001 = {
        'id': 'N001', 'type': 'newsection', 'advice': 'approve', 'title': '%s: your new section, in Appendix G' % N001_HEADING,
        'approve_label': 'it goes in as it is', 'card_after': nb - 1,
        'inserts': [{'before': nb, 'kind': 'h2' if k == 0 else 'p', 'text': t, 'seq': k + 1} for k, t in enumerate(n_inserts)],
        'reads': [dict({'text': t}, **({'kind': 'h2'} if k == 0 else {})) for k, t in enumerate(n_inserts)],
        'reads_label': 'The new section, as it would read',
        'what': 'A new section in Appendix G, after %s and before %s: %s and your five paragraphs, word for '
                'word. In the last sentence “%s” is a link to [this part of your nibbana guide](%s); the page shows it '
                'the way Markdown writes a link, in square brackets with its address after it.'
                % (here(N001_AFTER), here(N001_BEFORE), n_heading_said, NIBBANA_WORDS, NIBBANA),
        'tested': tested('N001', 'Your five paragraphs by themselves, without the heading: [%s](%s).' % N001_READ),
        'why': 'You wrote this section on 25 November. The place is the one I proposed in that day’s questions: Appendix G, '
               'after %s.' % here(N001_AFTER),
        'stays': 'Everything else in Appendix G, and %s as it is.' % here(CLINIC),
        'owner_text': n_owner, 'whose': n_owner,
        'ask_because': 'his own: you typed this section in the chat on 25 November; it goes in word for word, and it '
                       'says something different from %s about who can do a regression.' % here(CLINIC),
        'deciding': conflict + '\n' + choices,
        'warning': 'As it stands, this section and %s tell a reader two different things about going back after trauma. '
                   'The question card N001-Q marks the sentence there.' % here(CLINIC),
        'advice_note': 'Your call: the first way leaves both passages as they are, and the second and third tell the '
                       'reader which one holds.',
        '_md': {'where': nb, 'paras': n_inserts},
    }
    cards.append(n001)
    qi, qspan = at('N001-Q')
    cards.append({
        'id': 'N001-Q', 'type': 'newsection', 'advice': 'ask', 'title': 'Your new section says something different',
        'spans': [qspan],
        'question': 'Does this sentence stay as it is once your new section is in? The new section (card N001, in '
                    'Appendix G after %s) says of age regression: “%s” The choices are on that card; if you answer '
                    'there, leave this one empty.' % (here(N001_AFTER), no_pro),
        'why': 'This is the sentence a reader of both would set beside the new section.',
        'stays': 'This paragraph as it is.',
        '_md': {'where': qi}})

    # in the page's order: the block each card sits under, then where its highlight starts (as the page sorts them)
    cards.sort(key=lambda c: (c.get('card_after', c['spans'][0]['block'] if c.get('spans') else c['_md']['where']),
                              c['spans'][0]['start'] if c.get('spans') else 0, c['id']))
    for cid in readings:
        if cid not in {c['id'] for c in cards if c['advice'] == 'approve'} | set(ASK_INSTEAD):
            notes.append('READINGS.json names %s, which is not a card with a change on this page: not shown' % cid)

    n_add = len(ADDS)
    n_q = len(ASKS)
    intro = [
        'This is the whole Self-Hypnosis guide as it reads after today’s contents edit (25 November), with a card under '
        'each paragraph where something would be added or changed, or where I have a question: %d additions made of '
        'sentences from your inner child and somatic guides, one more that comes to you as a question (%s), %d places '
        'where this guide and the inner child guide now differ, your answer 7 b on breathing as a whole paragraph, and '
        'the section you wrote today.' % (n_add, ', '.join(ASK_INSTEAD), n_q),
        'Nothing on these cards is in the post yet. Approve, Reject or Revise on each card is your answer; when you’re '
        'done, open “Save / send”, press “Copy my answers (JSON)” and send them back to me.',
        'Two drafted additions are not here, %s and %s: the writer found this guide already says both.' % SKIPPED,
    ]
    after_sha = sha256(after_md)
    review = {
        'format': sr.FORMAT,
        'review_id': 'inner-signal-catchup-20261125',
        'title': 'Self-Hypnosis Guide, 25 November: from your other guides, and your new section',
        'intro': intro,
        'git_file': REL + 'review/REVIEW.html',
        'article': {'file': art_file, 'sha256': sha256(page_md)},
        'whole': {'file': REL + 'AFTER.md', 'sha256': after_sha},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': BLOB + REL + 'AFTER.md', 'guide_label': 'this guide as it reads after the contents edit',
                  'review': BLOB + REL + 'review/CARDS.md'},
        'types': TYPES,
        'suggestions': [{k: v for k, v in c.items() if not k.startswith('_')} for c in cards],
    }
    (HERE / 'REVIEW.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')

    # ---- the cards as a Markdown page
    type_of = {k: v['label'] for k, v in TYPES.items()}

    def where_md(i):
        b = bl[i]
        return 'the heading %s' % shown(b['text']) if b['level'] else '%s, %s' % (shown(b['section']), b['pn'])

    def lines_md(t):
        return t.replace('\n', '\n\n')

    md = ['# %s' % review['title'], '', intro[0], '',
          'Nothing on these cards is in the post yet. This page is the same cards for reading on GitHub; the Approve, '
          'Reject and Revise buttons are on the marking page, which shows each card inside the whole guide.', '',
          intro[2], '',
          '[The guide the page shows](%s) · [the comparison with the inner child guide](%s) · [the comparison with the '
          'somatic guide](%s)' % (BLOB + REL + 'AFTER.md', BLOB + REL + 'catchup/CATCHUP-INNER-CHILD.md',
                                  BLOB + REL + 'catchup/CATCHUP-SOMATIC.md'), '',
          'The cards are in the guide’s order.', '']
    for c in cards:
        m = c['_md']
        md += ['## %s · %s' % (c['id'], md_esc(c['title'])), '']
        if c['id'] == 'N001':
            md += ['*%s · in Appendix G, after %s and before %s*' % (type_of[c['type']], shown(N001_AFTER),
                                                                    shown(N001_BEFORE)), '',
                   '**The new section**', '',
                   quote_block(['**%s** (the heading)' % md_esc(m['paras'][0])] + [md_linked(p) for p in m['paras'][1:]]), '',
                   '**What goes in:** %s' % c['what'], '', '**Pangram:** %s' % c['tested'], '', '**Why:** %s' % c['why'], '',
                   '**What stays:** %s' % c['stays'], '',
                   '**Why I’m asking:** %s' % (c['ask_because'][len('his own: '):][:1].upper()
                                               + c['ask_because'][len('his own: ') + 1:]), '',
                   '**You’re deciding:** %s' % lines_md(c['deciding']), '', '**My advice:** %s' % c['advice_note'], '']
            continue
        md += ['*%s · %s*' % (type_of[c['type']], where_md(m['where'])), '']
        if c['advice'] == 'ask':
            t = bl[m['where']]['text']
            sp = c['spans'][0]
            para = md_para(md_esc(t[:sp['start']]) + md_mark(t[sp['start']:sp['end']], '**') + md_esc(t[sp['end']:]))
            md += ['**The paragraph now** (the words in question in bold)', '', '> ' + para, '',
                   '**My question:** %s' % c['question'], '', '**Why I ask:** %s' % c['why'], '',
                   '**Until you answer:** %s' % c['stays'], '']
            if c.get('advice_note'):
                md += ['**My advice:** %s' % c['advice_note'], '']
            continue
        if 'ops' in m:                            # several changes in one paragraph
            a, b2 = md_ops(m['old'], m['ops'])
            now, new = [a], [b2]
        elif m['new_paragraph']:                  # a new paragraph after the anchor's
            now = [md_para(md_esc(m['old']))]
            new = now + [md_para(md_mark(m['text'], '**'))]
        else:
            a, b2 = md_sides(m['old'], m['span'][0], m['span'][1], m['kind'], m['text'])
            now, new = [a], [b2]
        md += ['**The paragraph now**' + (' (the words that go struck through)' if '~~' in now[0] else ''), '',
               quote_block(now), '', '**As it would read** (the new words in bold)', '', quote_block(new), '',
               '**What %s:** %s' % ('changes' if 'ops' in m or m['kind'] == 'change' else 'it adds', c['what']), '',
               '**Why:** %s' % c['why'], '']
        if 'from' in m:
            md += ['**Where the words are from:** %s, %s, as it is live on 25 November. Changed from how %s there: %s'
                   % (m['guide'], m['from'], m['read'], m['changed']), '']
        if c.get('tested'):
            md += ['**Pangram:** %s' % c['tested'], '']
        md += ['**What stays:** %s' % c['stays'], '']
        if 'from' not in m:
            k = c['ask_because'].index(':') + 2
            md += ['**Why I’m asking:** %s' % (c['ask_because'][k:k + 1].upper() + c['ask_because'][k + 1:]), '']
        md += ['**You’re deciding:** %s' % c['deciding'], '']
    (HERE / 'CARDS.md').write_text('\n'.join(md).rstrip('\n') + '\n', encoding='utf-8')

    # ---- the tool's own check, then the page
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    tool = 'tools/humanization/suggestion_review.py'
    rj = REL + 'review/REVIEW.json'
    for n_ in notes:
        print('NOTE', n_)
    r = subprocess.run([sys.executable, tool, 'check', rj], cwd=str(ROOT), env=env, capture_output=True, text=True)
    print((r.stdout + r.stderr).rstrip())
    if r.returncode:
        print('check did not pass: no page written')
        return 1
    r = subprocess.run([sys.executable, tool, 'page', rj, REL + 'review/REVIEW.html', '--artifact',
                        REL + 'review/REVIEW-artifact.html'], cwd=str(ROOT), env=env, capture_output=True, text=True)
    print((r.stdout + r.stderr).rstrip())
    if r.returncode:
        return 1
    words = sum(len(b['text'].split()) for b in flat)
    folded = sum(len(b['text'].split()) for a, z in folds for b in flat[a:z + 1])
    print('%d blocks in AFTER.md (%d words); %d stretches folded (%d words): %s'
          % (len(flat), words, len(folds), folded,
             '; '.join('“%s” to “%s”' % (flat[a]['text'][:40], flat[z]['section']) for a, z in folds) or 'none'))
    print('%d cards: %d additions from the other guides, %d drafted addition as a question (%s), %d questions on '
          'differences, his answer 7 b, his new section and its pointer; %d to decide, %d questions; %d with a Pangram '
          'reading' % (len(cards), n_add, len(ASK_INSTEAD), ', '.join(ASK_INSTEAD), n_q,
                       sum(1 for c in cards if c['advice'] != 'ask'), sum(1 for c in cards if c['advice'] == 'ask'),
                       sum(1 for c in cards if c.get('tested')) + len(ASK_INSTEAD)))
    print('in page order: ' + ', '.join(c['id'] for c in cards))
    return 0


if __name__ == '__main__':
    sys.exit(main())
