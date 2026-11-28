#!/usr/bin/env python3
"""sense_receipt.py - the making-sense read's receipt: a short note, sentence by sentence where it helps, of the read for
sense that a paragraph I wrote or changed gets before it goes to Pangram or onto Joel's marking page (gate E365, which
enforced E362; a light note since the rules audit of 2026-11-28, card C02).

Joel, 2026-11-05 15:14 UTC, on round 6 of the bad trips guide, where my card had kept the 7-OH-CBD point after checking it
had taken away its reason for being there, and had brought in a trial of focal seizures for a reader facing a seizure
from MDMA or a psychedelic overdose, which are generalized: "i already told you to stop putting stuff in that is wasting
reader's time ... READ what you wrote, it literally is a whole big waste of time to talk about this, there's NO PAYOFF
... why did i have to tell you this twice? fix the way you work because i'm not telling you the same stuff over and
over." The making-sense read (docs/MAKING-SENSE.md) already asked "does this fact help this reader now?" (E360). Nothing
made me answer it for each sentence before the card went out, so it wasn't answered. UDA's
patterns/task-time-lesson-activation.md: when the owner catches a violation of a rule he already stated, repair the
enforcement, not only the candidate. That enforcement was this receipt: tools/humanization/pangram_ledger.py predict
refused a text of mine without a receipt that passed here, and tools/humanization/suggestion_review.py refused a card that
adds or changes words without one (reviews built from 2026-11-05).

Rules audit 2026-11-28, card C02 (approved; Joel: "something like this already exists maybe merge"): the making-sense read
still comes before every Pangram try, and each sentence shows early how it follows from the one before, judged by reading
it, not by counting words; the receipt is a short note of that read, and no tool refuses a change for lacking one. So a
text of mine without a receipt is no longer refused (pangram_ledger.py notes that the read comes first; a marking-page
card needs none), and the problems a given receipt has here are printed there as notes.

The judging is mine (a model reads meaning; nothing here judges it): the receipt is where I write, for the sentences that
need it, what this section's reader does or understands differently because of it, and why it comes where it does. The
code checks only what is present and wrong: the receipt is for another text (SHA-256) or lists sentences that aren't the
text's; a sentence a fresh read marked is still in the text with no reason in "kept"; a question is answered FAIL; quoted
link words aren't in their sentence; a "his_answer" entry leaves something out with no reason, or quotes a sentence that
isn't in the text; a checked point that lost its reason for being there isn't cut; sentences are marked his without
"his_whose" saying he wrote them himself (E373); a term is explained after the text has already used it (E369). A field
that is missing or empty is not a problem: the per-sentence payoff, follows and link, opens, same_point, placement, the
three fresh reads (needed, his_fixes, fit) and the nine questions.

  python3 tools/humanization/sense_receipt.py make TEXT --section "Active Seizure" --reader "who reads it, facing what
          exactly" [--his HIS.txt] --out RECEIPT.json
  python3 tools/humanization/sense_receipt.py check TEXT RECEIPT.json

make writes every field, empty, as a prompt for the read: every sentence of TEXT with an empty payoff and follows (a
sentence found word for word in HIS.txt, Joel's own text, is marked his and needs neither), the nine questions, placement
and checked. Fill what the read needs by editing the JSON, then check it; a field left empty is not a problem (card C02).
A sentence whose payoff you can't write still goes from the text (E362); make the receipt again.

The fields:
  reader     who reads this section and what exactly they face: the case, not the topic ("someone with a person having
             a seizure from MDMA or a psychedelic overdose, which is generalized", not "someone interested in seizures").
             Every payoff is judged against it.
  sentences  [{"s": the sentence, "his": true for Joel's words, "payoff": what this reader does or understands
             differently because of it, "follows": why it comes after the sentence before (what it continues, answers
             or turns on); for the first sentence, why it follows the paragraph or heading before it}]
  checked    [{"point", "found": what the source says, "still_needed": "yes: ..." or "no: ..." (does the reason this
             point is here survive what the check found?), "fate": "kept", "changed" or "cut"}]   every point I checked
             against a source; "no" must be "cut" (the 7-OH-CBD case: it was there because it might be more active; the
             check found it about as active as CBD, so nothing was missed and the point had no payoff left)
  placement  where the paragraph sits and why there: next to what it continues; same-topic paragraphs together, a
             different topic before or after the group, never inside it; and what its first "also", "this" or "as for"
             now points to (Joel, 2026-11-05: "the problem was simply that you had the ideas out of their natural
             order"; "we should move the non-cannabis para above all the cannabis info ... isn't that obvious?")
  questions  Q1 to Q9, docs/MAKING-SENSE.md's questions: "PASS: the evidence in the text" or "N/A: why it can't apply";
             "FAIL" is a problem, a question left blank is not (card C02).
  late_ok    optional {term: why}: a term a sentence of mine explains after the text has already used it, and why it
             can't be explained where it is first used. Without it such a sentence fails (gate E369: Joel, 2026-11-05,
             "make sure every term is introduced once at first"; "Colostrum is the first milk a cow makes ..." after
             "Liposomal first-milking colostrum" read AI, Medium).
  opens      {"first_sentence": the text's first sentence (make writes it), "why_reading": what that first sentence
             tells this reader about their own case, so they know why they are reading on: the state they would
             recognize in themselves, or what they get from the paragraph}. Asked of the paragraph, whoever wrote its
             first sentence: a payoff for each sentence I add doesn't say whether the paragraph opens on one (gate E374;
             Joel, 2026-11-06 19:40 UTC, on my dynorphin tries, which kept the model's mechanism-first opening and
             added the payoff at the end: "it was not giving the payoff quick enough. i was as usual wondering why am i
             reading this?"; his version opens "If you're feeling apathetic, gray, no desire for anything, you might be
             in a neurochemical "Void" state"). Since the rules audit of 2026-11-28 (card C03, approved), payoff first
             stays his test and an opening on the reader's own case is one way he has met it, to consider, not to
             require: an empty "opens" is not a problem (his note on the card: "this also has to do usually with
             connections between sentences, paragraphs, ideas").
  same_point which paragraphs of the section (heading to next heading) already make a point this paragraph makes, and
             what happens to each: "merged here; block N, the Hardening paragraph, is deleted" or "none: read the
             section from its heading to the next for <the points>". A point said in two places is merged into one, in
             the order the reader needs it, and the other place goes (gate E376; Joel, the same message: "delete the
             "hardening" para since i had to incorporate that into this one, otherwise it was out of order and a bit
             redundant"). Both fields are in every receipt make writes from 2026-11-06 19:40 UTC; left empty, neither is
             a problem (cards C02, C03).
  needed     {"reader": who read it (a fresh reader: a new agent that saw only the paragraph, its heading and
             what the paragraph is for, given tools/humanization/needed_read_brief.md), "unneeded": [each sentence that
             reader said the reader of this paragraph doesn't need for what it is for], "kept": {sentence: "they ...: what
             the reader does with it, so it stays"}}. A sentence the read lists goes, unless "kept" names what the reader
             does with it for the paragraph's job; that it is true, sourced, testable, a hypothesis with a mechanism, or
             already in the text is not a reason (gate neuro-2026-11-08a; Joel, 2026-11-08 00:49 UTC, cutting my GluD
             paragraph to two sentences: "did you even read what you had there? it was making no sense. i removed most of
             it and just put the basic facts. it seems like you're doing anything possible to preserve prose even if it
             doesn't help the reader. fix that durably."). Every point in "checked" marked "yes" says the same:
             "yes: they ..." for what the reader does with it, not why the claim holds. In every receipt make writes from
             2026-11-08.
  his_fixes  {"reader": who read it (a fresh reader given tools/humanization/his_fixes_brief.md and the text, one sentence
             a line), "marked": [{"s": a sentence it marked, "difference": the way it reads unlike his fixes}], "kept":
             {sentence: why it stays}} (gate bad-trips-2026-11-12g). The read is against his fixes wherever they are in
             the repo, not only this article's: his note on card C17 of the rules audit of 2026-11-28, "and not just
             against my own fixes in that article of course but any fixes in the repo that could be useful for that
             context".
  fit        {"reader", "marked": [{"s": a line it marked, "found": what it found}], "kept": {line: why it fits}} (gate
             bad-trips-2026-11-12j; tools/humanization/fit_read_brief.md).
             The three fresh reads (needed, his_fixes, fit) are a help whose marks are each judged, not a gate rerun on
             every version (card C17, revised as his note says): a read not done, or with no "reader", is not a problem;
             a sentence it marked that is still in the text needs its reason in "kept".
  his_answer for a text that carries his answers to a round's cards, written only where something relevant he said is
             dropped: [{"said": his words, quoted from his answer; "in": the sentence (or sentences) of this text that
             carry that claim; "left_out": {what he said there that is relevant and that "in" doesn't say, in his
             words: where it went, why it is out, or "asked: <card id>" when I'm not sure it is relevant}}]. Not every
             word of his reaches the sentence: he often says things beside the point, so what he means is read first.
             Something relevant to his point (a condition, a scope, a reason) stays with it, or has a reason to go, or he
             is asked; the clearest sign that it is relevant is that the sentence doesn't make sense or say what he
             meant without it. Lesson
             bad-trips-2026-11-27m, correcting k (Joel, 2026-11-27 22:48 UTC: "it's not that every word of my answer has
             to reach the sentence that says my point, but clearly if i'm saying something which is relevant and then
             you're removing that, you'd need to have a reason for removing it. if you're unsure, you'd ask. i often do
             say a lot of things which aren't super relevant so you should try to understand. in this case it was pretty
             clear because what you wrote didn't make sense without that"). The case: his "it absorbs almost as well as
             eating it, especially on sensitive skin" went in as "Its juice works through the skin almost as well as
             eating the leaf does", which isn't true of skin in general and left his "under the armpits" unexplained
             (19:54 UTC: "you forgot the most important part, sensitive skin... that's why i said under the armpits").
             The code checks only that each entry is whole and each "left_out" item has a reason; whether something
             bears on the claim is a reader's call, and `candidates` lists the words of his that the sentence doesn't
             have, as candidates for that read, never as a test. A receipt made in turn 74 with "words" is read as
             "left_out". make writes the key, empty; nothing requires an entry (the check of each relevant drop is the
             read, and the 22:48 UTC rules check of lesson m: "record it only where a relevant thing is actually
             dropped").
  link       on every sentence of mine after the first: the words in that sentence that tie it to the one before or to
             the reader's case ("One reason to think about, is that", "So to address that", "because"), quoted from the
             sentence; or "none: why it needs none" (a list item, a new step the reader expects). The code checks only
             that the quoted words are in the sentence; an empty link is not a problem, and where the tie sits is the
             read's to judge (the test that refused a tie after the sentence's first five words, lesson
             bad-trips-2026-11-22a, went with card C02). Gate neuro-2026-11-06b; Joel, 2026-11-06 23:01 UTC, on my third
             try of the section's first paragraph, whose receipt had each sentence's `follows` right while the sentences
             themselves said nothing of it: "as usual, it was not giving the payoff at the start, i told you this a
             million times"; his version turned "Standard therapy is trying to rewrite" into "One reason to think about,
             is that standard therapy is trying to rewrite" and "This protocol goes after" into "So to address that,
             I've designed this protocol to go after". In every receipt make writes from 2026-11-06 23:01 UTC.
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

SCHEMA = 'SENSE_RECEIPT_V1'
# Gate E373 (Joel, 2026-11-06 17:30 UTC: "'my words' for an AI article, are not my words, unless those were human before we
# started humanizing (i.e if i wrote that myself inside an ai article) otherwise it's AI words that i humanized"): from this
# day a sentence is marked his only for what he wrote himself, and the receipt says so ("his_whose": "his own: ...")
PROVENANCE_FROM = '2026-11-06'
# Gates E374 and E376: from this day every receipt answered "opens" and "same_point" (receipts that already carried either
# key were checked for both from the moment make began writing them, 2026-11-06 19:40 UTC). Rules audit 2026-11-28, cards
# C02 and C03 (approved; C03, Joel: "this also has to do usually with connections between sentences, paragraphs, ideas"):
# neither is required now, so this date decides nothing; it stays for the record and for scripts that name it.
PARAGRAPH_FROM = '2026-11-07'
# Gate neuro-2026-11-08a: from this day a receipt for a text of mine carries a fresh reader's "needed" read, and a
# sentence that read says the reader doesn't need is cut unless "kept" says what the reader does with it. Since the rules
# audit of 2026-11-28 (card C17) the read itself is optional; this date still says from when a checked point marked "yes"
# says what the reader does with it.
NEEDED_FROM = '2026-11-08'
# Gate bad-trips-2026-11-12g: from this day a receipt for a text of mine carries a fresh reader's read against his fixes
# (tools/humanization/his_fixes_brief.md, the eight ways his 112 fixes differ from the drafts he fixed), and each sentence
# that read marks is changed before the check, or "kept" says why it stays. Joel, 2026-11-12 14:45 UTC: "have you
# systematically looked at all of the fixes i've shown you and what are the idfferences in how you write vs how i fix?"
HIS_FIXES_FROM = '2026-11-12'
# Gate bad-trips-2026-11-12j: from this day a receipt for a text of mine carries a fresh reader's fit read
# (tools/humanization/fit_read_brief.md: for each line that says what to look for or do, whether it is true anyway of
# someone tripping or overdosing, whether a friend could tell, whether it is a rule from another setting), and each line
# it marks is changed before the check, or "kept" says why it fits. Joel, 2026-11-12 19:44 UTC, after cutting "It's their
# first seizure" and "Check if their vision has changed" from texts every fresh read had passed: "we need to have a
# better sense check in general". The receipts make writes carry the field from that hour; a receipt made before it with
# no field is read as it was.
# Rules audit 2026-11-28, card C17 (revised as his note says: "and not just against my own fixes in that article of course
# but any fixes in the repo that could be useful for that context"): a fresh read is a help whose marks are each judged, not
# a gate, so neither date above requires a read now; a sentence a read marked still needs its reason in "kept".
FIT_FROM = '2026-11-13'
# Lesson bad-trips-2026-11-27k: from this day every receipt maps each claim of his answers to the sentence that carries it
HIS_ANSWER_FROM = '2026-11-28'
HIS_ANSWER_STOP = {'that', 'this', 'with', 'from', 'have', 'when', 'what', 'them', 'they', 'their', 'there', 'then',
                   'than', 'into', 'just', 'would', 'could', 'should', 'about', 'because', 'which', 'while', 'your',
                   'were', 'been', 'being', 'does', "doesn't", "don't", "i'd", "it's", 'also', 'altho', 'although',
                   'though', 'like', 'said', 'example', "that's", "there's", "what's", "i'm", "i've", "can't", "won't",
                   "isn't", "didn't"}
CARD_CITED = re.compile(r'\bcard [A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+\b')
# Lesson bad-trips-2026-11-22a (Joel, 2026-11-22 17:21 UTC, on my sentence after "Serotonin syndrome comes from too much
# serotonin, so I'd stop anything suspected of adding more": "S2 doesn't follow from S1. you really don't see that? what's
# connecting them? even "So" would connect", and on "Even if they take an antidepressant every day ...": "I'm reading like 20
# words before I understand why I'm reading them"): the words that tie a sentence to the one before come early, where the
# reader asks why they are reading it ("So", "It doesn't matter if", "And while you might think", "Although").
# Rules audit 2026-11-28, card C02 (approved): that is judged by reading the sentence, not by counting words, so the test
# that refused a tie after the sentence's first five words (LINK_START_FROM, LINK_START_WORDS) is gone; the read keeps
# his point.
READER_USE = re.compile(r'^\s*(yes\s*:\s*)?they\b\s+\S.{20,}', re.I | re.S)
HIS_OWN = re.compile(r'^\s*his own\s*:\s*\S.{8,}', re.I | re.S)
NOT_HIS = ('--his is only for what Joel wrote himself, before any humanizing: give --whose "his own: what and where". His '
           'version of a model\'s text, and the published text of an article a model drafted, are AI words he humanized: '
           'their sentences are read for sense like mine (gate E373)')
QUESTIONS = {
    'Q1': 'Why am I reading this sentence, and do I know it before I have to work through it? (the point first, in each '
          'sentence and each paragraph; a study after the question it answers; a term explained where it is first used, '
          'never in a sentence after it)',
    'Q2': 'What is each instruction for, said in the reader\'s terms, and is it something the helper does ("have someone '
          'go with them"), not a rule stated as a fact ("someone goes with them")?',
    'Q3': 'Which thing exactly? (pools of water, not water; any substance, not anything)',
    'Q4': 'What does each word act on, or mean here? (adjunct remedy; known-genuine) Is every term a high-school graduate '
          'wouldn\'t know (enterocytes, BPC-157) explained once, where it is first used, and common ones (a vitamin) '
          'left alone? Is each mechanism explained by what it does in the reader\'s experience (dopamine "for '
          'motivation (by showing us what is important to pay attention to)"; DeltaFosB "preventing that learning from '
          'really clicking"), not by where it sits or what it looks like ("a chemical blanket", "the slower one '
          'underneath")? (E375)',
    'Q5': 'Why does each sentence follow from the one before? (every but, so, because and this has what it turns on)',
    'Q6': 'Is this the order the reader is thinking in, and does each idea sit next to what it continues?',
    'Q7': 'Does each fact help this reader now, in their case (the same kind of thing they face, not just the same topic)?',
    'Q8': 'Does each item belong in the group it is put in?',
    'Q9': 'Is anything compressed? (one step a sentence, the small words that carry the relation, no space before mg)',
}
# What an unfilled payoff used to hold. Rules audit 2026-11-28, card C02 (approved): an empty payoff is not a problem, so
# check() no longer reads it; it stays for scripts that name it.
NO_PAYOFF = re.compile(r'^\s*(none|nothing|no payoff|n/?a|-+|\?|tbd|todo)\b', re.I)
# A sentence that says what a term is: "Colostrum is the first milk ...", "liposomal means ...", "SCFAs are a ..."
DEFINES = re.compile(r'^(?:the |a |an )?([A-Za-z][\w\-]*(?:[ \-][\w\-]+){0,3}?)\s+(?:is|are)\s+(?:a|an|the|what)\s'
                     r'|^(?:the |a |an )?([A-Za-z][\w\-]*(?:[ \-][\w\-]+){0,3}?)\s+(?:means|stands for|refers to)\b', re.I)
NOT_TERMS = {'this', 'that', 'it', 'these', 'those', 'there', 'here', 'which', 'what', 'each', 'one', 'he', 'she',
             'they', 'we', 'you', 'i', 'the point', 'the problem', 'the reason', 'the exception', 'the rest', 'the idea'}


def late_definitions(text, receipt):
    """Gate E369 (Joel, 2026-11-05 18:43 UTC: "make sure every term is introduced once at first, like enterocytes my
    readers won't know what those are"): sentences of mine that say what a term is after the text has already used the
    term. Returns [(term, the defining sentence)], less any term the receipt's late_ok excuses with a reason."""
    ok = {k.lower() for k, v in (receipt.get('late_ok') or {}).items() if len((v or '').strip()) >= 20}
    out, before = [], []
    for x in receipt.get('sentences', []):
        s = x.get('s', '')
        m = DEFINES.match(s)
        term = (m.group(1) or m.group(2)).strip() if m else ''
        if term and not x.get('his') and term.lower() not in NOT_TERMS and len(term) > 2 and term.lower() not in ok:
            if any(re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(term), b, re.I) for b in before):
                out.append((term, s))
        before.append(s)
    return out


def sha256(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


ABBREV = {'dr', 'mr', 'mrs', 'ms', 'st', 'vs', 'etc', 'e.g', 'i.e', 'cf', 'al', 'approx', 'no', 'fig'}


def sentences(text):
    """The text's sentences, in order: a break after . ! ? (and any closing quote or bracket) before a space and a
    capital, a digit or an opening quote, but not after an abbreviation such as "Dr." or "e.g."; and at line breaks.
    Exact and repeatable, so a receipt's sentences can be compared with the text's."""
    out = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        start = 0
        for m in re.finditer(r'[.!?]["”’)\]]*(\s+)(?=["“‘(\[]?[A-Z0-9])', line):
            word = re.search(r'([\w.]+)$', line[start:m.start() + 1])
            if word and line[m.start()] == '.' and word.group(1).rstrip('.').lower() in ABBREV:
                continue
            out.append(line[start:m.start(1)].strip())
            start = m.end(1)
        rest = line[start:].strip()
        if rest:
            out.append(rest)
    return [x for x in out if x]


def make(text, section='', reader='', his_text='', whose=''):
    his = his_text or ''
    if his and not HIS_OWN.match(whose or ''):
        raise ValueError(NOT_HIS)
    import datetime
    return dict({
        'schema': SCHEMA,
        'made': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d'),
        'text_sha256': sha256(text),
        'text': text,
        'section': section,
        'reader': reader,
        'sentences': [dict({'s': s}, **({'his': True} if his and s in his else
                                        dict({'payoff': '', 'follows': ''}, **({'link': ''} if n else {}))))
                      for n, s in enumerate(sentences(text))],
        'checked': [],
        'placement': '',
        'opens': {'first_sentence': (sentences(text) or [''])[0], 'why_reading': ''},
        'same_point': '',
        'needed': {'reader': '', 'unneeded': [], 'kept': {}},
        'his_fixes': {'reader': '', 'marked': [], 'kept': {}},
        'fit': {'reader': '', 'marked': [], 'kept': {}},
        'his_answer': [],
        'questions': {q: '' for q in QUESTIONS},
        'question_text': QUESTIONS,
    }, **({'his_whose': whose} if his else {}))


# A link of "none" (on its own or with its why: "none: a new step the reader expects") quotes no words.
LINK_NONE = re.compile(r'^\s*none\s*(?:[:;,.(\u2013\u2014-]|$)', re.I)


def check(text, receipt):
    """Problems with RECEIPT for TEXT: [message]. Empty means nothing in it is wrong.

    Rules audit 2026-11-28, card C02 (approved; Joel: "something like this already exists maybe merge"): the receipt is a
    short note of the making-sense read, so this reports only what is present and wrong. A field that is missing or empty
    is not a problem (make writes them all, empty, as a prompt): the per-sentence payoff, follows and link, the reader,
    opens (card C03), same_point, placement, the three fresh reads (card C17) and the nine questions. Still problems: a
    receipt for another text, or one that lists sentences the text doesn't have; a sentence a fresh read marked that is
    still in the text with no reason in "kept"; a question answered FAIL; quoted link words that aren't in their
    sentence; a "his_answer" entry that leaves something out with no reason; a checked point that lost its reason for
    being here and isn't cut (E362); sentences marked his with no "his_whose" (E373); a term explained late (E369)."""
    p = []
    if receipt.get('schema') != SCHEMA:
        p.append('not a %s receipt' % SCHEMA)
    if receipt.get('text_sha256') != sha256(text):
        p.append('the receipt is for another text (its SHA-256 %s, this text\'s %s): a changed text needs its read again'
                 % ((receipt.get('text_sha256') or '?')[:12], sha256(text)[:12]))
    want = sentences(text)
    # a sentence the receipt leaves out is not a problem (card C02); one that isn't the text's means the receipt (or part
    # of it) is for another text
    extra = [x.get('s', '') for x in receipt.get('sentences', []) if x.get('s', '') not in want]
    if extra:
        p.append('sentences: the receipt lists sentences that are not in this text (make writes the text\'s own): %s'
                 % ' | '.join(e[:60] for e in extra[:3]))
    if any(x.get('his') for x in receipt.get('sentences', [])) and (receipt.get('made') or '') >= PROVENANCE_FROM \
            and not HIS_OWN.match(receipt.get('his_whose') or ''):
        p.append('sentences are marked his, but the receipt doesn\'t say they are what he wrote himself ("his_whose": '
                 '"his own: what and where"). ' + NOT_HIS)
    mine = 0
    for x in receipt.get('sentences', []):
        if x.get('his'):
            continue
        mine += 1
        # Rules audit 2026-11-28, card C02 (approved): an empty payoff, follows or link is not a problem, and where the
        # tie sits in the sentence is the read's to judge (the five-word test of lesson bad-trips-2026-11-22a is gone).
        # Quoted words that aren't in the sentence are still wrong: the note would point at words the reader never sees.
        link = (x.get('link') or '').strip()
        if link and not LINK_NONE.match(link) and link.lower() not in (x.get('s') or '').lower():
            p.append('link for "%s": the quoted words "%s" are not in the sentence; quote the words in it that tie it to '
                     'the one before or to the reader\'s case ("One reason to think about, is that", "So to address '
                     'that"), or say "none: why" (gate neuro-2026-11-06b)' % (x.get('s', '')[:60], link[:40]))
    for c in receipt.get('checked', []):
        if (c.get('still_needed') or '').strip().lower().startswith('no') and c.get('fate') != 'cut':
            p.append('checked: "%s" lost its reason for being here when it was checked, so it goes (fate "cut"); '
                     'a corrected point with no payoff still wastes the reader\'s time (the 7-OH-CBD case, E362)'
                     % (c.get('point') or '?')[:50])
        if c.get('fate') not in (None, '', 'kept', 'changed', 'cut'):
            p.append('checked: fate must be "kept", "changed" or "cut"')
    for term, s in late_definitions(text, receipt):
        p.append('"%s" is explained in "%s", after the text has already used it: explain it where it is first used, in '
                 'that sentence, and keep the point of the sentence first (gate E369; Joel, 2026-11-05: "make sure every '
                 'term is introduced once at first"); or say in late_ok why it can\'t be' % (term, s[:70]))
    # Rules audit 2026-11-28, cards C02 and C03 (approved): "placement", "opens" and "same_point" left empty are not
    # problems (C03, Joel: "this also has to do usually with connections between sentences, paragraphs, ideas"); card C17
    # (revised as his note says): the fresh reads are a help whose marks are each judged, so a read not done is not a
    # problem, and a sentence a read marked that is still in the text needs its reason in "kept".
    if mine:
        p += needed_problems(text, receipt)
        p += his_fixes_problems(text, receipt)
        p += fit_problems(text, receipt)
    if 'his_answer' in receipt or (receipt.get('made') or '') >= HIS_ANSWER_FROM:
        p += his_answer_problems(text, receipt)
    # Rules audit 2026-11-28, card C02 (approved): a question left blank is not a problem; one answered FAIL is
    qs = receipt.get('questions') or {}
    for q in QUESTIONS:
        a = (qs.get(q) or '').strip()
        if a.upper().startswith('FAIL'):
            p.append('%s fails: %s' % (q, a[:120]))
    return p


def needed_problems(text, receipt):
    """Gate neuro-2026-11-08a: every sentence the fresh reader's "needed" read lists is gone or kept for a use the reader
    has, and every checked point marked "yes" says what the reader does with it. A read not done is not a problem (rules
    audit 2026-11-28, card C17: a fresh read is a help whose marks are each judged, not a gate)."""
    p = []
    why = ('a sentence stays because the reader needs it for what the paragraph is for, not because it is true, sourced, '
           'testable or already there (gate neuro-2026-11-08a; Joel, 2026-11-08: "it seems like you\'re doing anything '
           'possible to preserve prose even if it doesn\'t help the reader. fix that durably.")')
    n = receipt.get('needed') or {}
    have = sentences(text)
    kept = n.get('kept') or {}
    for u in n.get('unneeded') or []:
        u = (u or '').strip()
        if not u:
            continue
        if any(u in x or x in u for x in have):
            k = (kept.get(u) or '').strip()
            if not READER_USE.match(k):
                p.append('needed: "%s" is a sentence the fresh reader said this reader doesn\'t need; cut it, or say in '
                         '"kept" what the reader does with it ("they ..."); %s' % (u[:70], why))
    if 'needed' in receipt or (receipt.get('made') or '') >= NEEDED_FROM:
        for c in receipt.get('checked', []):
            a = (c.get('still_needed') or '').strip()
            if a.lower().startswith('yes') and not READER_USE.match(a):
                p.append('checked: "%s" says it is still needed; say what the reader does with it ("yes: they ..."), '
                         'not why the claim holds; %s' % ((c.get('point') or '?')[:50], why))
    return p


def his_fixes_problems(text, receipt):
    """Gate bad-trips-2026-11-12g: every sentence a fresh reader's read against his fixes marks is gone from the text or
    kept with the reason it stays. The read is against any of his fixes in the repo that could help in this context, not
    only one article's (rules audit 2026-11-28, card C17, his note: "and not just against my own fixes in that article of
    course but any fixes in the repo that could be useful for that context"); a read not done is not a problem (C17: the
    marks are each judged, not a gate)."""
    p = []
    why = ('a marked sentence may read the way his fixes change (tools/humanization/his_fixes_brief.md, and his fixes '
           'anywhere in the repo that fit this context); judge the mark: change the sentence, or say in "kept" why it '
           'stays (rules audit 2026-11-28, card C17; Joel, 2026-11-12: "when i look at how you try to implement my fixes, '
           'it\'s laughable")')
    h = receipt.get('his_fixes') or {}
    have = sentences(text)
    kept = h.get('kept') or {}
    for m in h.get('marked') or []:
        u = ((m.get('s') if isinstance(m, dict) else m) or '').strip()
        if not u:
            continue
        if any(u in x or x in u for x in have) and len((kept.get(u) or '').strip()) < 25:
            p.append('his_fixes: "%s" was marked (%s) and is still in the text; %s' % (
                u[:70], (m.get('difference') if isinstance(m, dict) else '') or '?', why))
    return p


def fit_problems(text, receipt):
    """Gate bad-trips-2026-11-12j: every line a fresh reader's fit read marks is gone from the text or kept with the reason
    it fits. A read not done is not a problem (rules audit 2026-11-28, card C17: a fresh read is a help whose marks are
    each judged, not a gate)."""
    p = []
    why = ('a marked line may be true anyway of someone tripping or overdosing, something a friend couldn\'t tell, or a rule '
           'from another setting (tools/humanization/fit_read_brief.md); judge the mark: change the line, or say in "kept" '
           'why it fits (rules audit 2026-11-28, card C17; Joel, 2026-11-12: "we need to have a better sense check in '
           'general")')
    h = receipt.get('fit') or {}
    have = sentences(text)
    kept = h.get('kept') or {}
    for m in h.get('marked') or []:
        u = ((m.get('s') if isinstance(m, dict) else m) or '').strip()
        if not u:
            continue
        if any(u in x or x in u for x in have) and len((kept.get(u) or '').strip()) < 25:
            p.append('fit: "%s" was marked (%s) and is still in the text; %s' % (
                u[:70], (m.get('found') if isinstance(m, dict) else '') or '?', why))
    return p


def his_words(said):
    """The words of SAID worth a look when the sentence carrying his claim doesn't have them: four letters or more,
    lower case, but a few words that carry no claim (HIS_ANSWER_STOP). Candidates for a reader's call, never a test
    (lesson bad-trips-2026-11-27m)."""
    out = []
    for w in re.findall(r"[A-Za-z][A-Za-z'’]+", said or ''):
        w = w.lower().replace('’', "'").strip("'")
        if len(w) >= 4 and w not in HIS_ANSWER_STOP and w not in out:
            out.append(w)
    return out


def candidates(said, into):
    """The words of his (SAID) that the sentence carrying his claim (INTO) doesn't have, for a reader to look at: a word
    of his matches a word there that starts with its first five letters, so "relaxing" finds "relax"."""
    have = [w.lower().replace('’', "'") for w in re.findall(r"[A-Za-z][A-Za-z'’]+", into or '')]
    return [w for w in his_words(said) if not any(x.startswith(w[:5]) for x in have)]


def his_answer_problems(text, receipt):
    """Lesson bad-trips-2026-11-27m (correcting k): where something relevant he said is dropped from the sentence that
    carries his claim, the entry says where it went, why it is out, or the card that asks him. Whether something is
    relevant is a reader's call: the code checks that each entry is whole and each left-out item has a reason, and never
    that his words are all there, nor that there are entries."""
    p = []
    why = ('what he says that bears on his claim stays with it, or the receipt gives the reason it goes, or asks him '
           '(lesson bad-trips-2026-11-27m; Joel, 2026-11-27 22:48 UTC: "if i\'m saying something which is relevant and '
           'then you\'re removing that, you\'d need to have a reason for removing it. if you\'re unsure, you\'d ask")')
    entries = receipt.get('his_answer') or []
    flat = re.sub(r'\s+', ' ', text)
    for e in entries:
        said, into = (e.get('said') or '').strip(), re.sub(r'\s+', ' ', (e.get('in') or '').strip())
        if not said or not into:
            p.append('his_answer: each entry needs "said" (his words) and "in" (the sentence of the text that carries '
                     'them); ' + why)
            continue
        if into not in flat:
            p.append('his_answer: "%s" is not in the text; quote the sentence that carries his "%s"' % (into[:60], said[:40]))
            continue
        out = e.get('left_out', e.get('words')) or {}
        if not isinstance(out, dict):
            p.append('his_answer: "left_out" is {his words: where they went, why they are out, or "asked: CARD"}; ' + why)
            continue
        for k, v in out.items():
            if len((v or '').strip()) < 12:
                p.append('his_answer: his "%s" (in "%s") is left out with no reason; say where it went, why it is out, or '
                         'ask him ("asked: CARD"); %s' % (k[:50], said[:60], why))
    return p


def check_files(text_path, receipt_path):
    text = pathlib.Path(text_path).read_text(encoding='utf-8').rstrip('\n')
    receipt = json.loads(pathlib.Path(receipt_path).read_text(encoding='utf-8'))
    return check(text, receipt)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = ap.add_subparsers(dest='cmd', required=True)
    m = sub.add_parser('make')
    m.add_argument('text')
    m.add_argument('--section', default='')
    m.add_argument('--reader', default='')
    m.add_argument('--his', help='a file of what Joel wrote himself, before any humanizing: its sentences in TEXT are '
                   'marked his (needs --whose; gate E373)')
    m.add_argument('--whose', help='with --his: "his own: what he wrote, and where"')
    m.add_argument('--out', required=True)
    c = sub.add_parser('check')
    c.add_argument('text')
    c.add_argument('receipt')
    w = sub.add_parser('candidates', help='the words of his answer that the sentence carrying it does not have, as '
                       'candidates for the read of what bears on his claim (lesson bad-trips-2026-11-27m); never a test')
    w.add_argument('said')
    w.add_argument('sentence')
    a = ap.parse_args(argv)
    if a.cmd == 'candidates':
        print(', '.join(candidates(a.said, a.sentence)) or '(none)')
        return 0
    if a.cmd == 'make':
        text = pathlib.Path(a.text).read_text(encoding='utf-8').rstrip('\n')
        his = pathlib.Path(a.his).read_text(encoding='utf-8') if a.his else ''
        try:
            r = make(text, a.section, a.reader, his, a.whose or '')
        except ValueError as e:
            print('REFUSED: %s' % e, file=sys.stderr)
            return 2
        pathlib.Path(a.out).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print('receipt to fill: %s (%d sentences)' % (a.out, len(sentences(text))))
        return 0
    probs = check_files(a.text, a.receipt)
    if probs:
        print('FAIL\n  ' + '\n  '.join(probs))
        return 1
    # rules audit 2026-11-28, card C02: a light note, so a pass says nothing is wrong, not that every field is filled
    print('PASS: nothing in the making-sense receipt is wrong for this text (fields left empty are not problems)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
