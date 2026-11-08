#!/usr/bin/env python3
"""fill_receipts.py - the making-sense receipts of the three lines his rule changes (drug-neutral), filled by me; the
fresh reader's needed read is in NEEDED-READ.md (Haiku, given tools/humanization/needed_read_brief.md).

  python3 fill_receipts.py      fills NEW-B330b, NEW-B366a and NEW-B319 .receipt.json in place
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
Q_ALL = {
    'Q1': 'PASS: each sentence opens on its point (the flood; what lies underneath; the memories, mindset and setting; be kind)',
    'Q2': 'PASS: the one instruction says what it is for ("because blaming anyone only makes it heavier")',
    'Q3': 'PASS: "the dose of what drug(s) you took" and "how hard you pushed a practice" name the two cases exactly',
    'Q4': 'PASS: no term a reader wouldn\'t know; "a practice" is the guide\'s word for meditation, breathwork, fasting and the like',
    'Q5': 'PASS: "those interpretations" points to S1\'s meanings; the memories and setting add to S2\'s factors; S4 turns from causes to blame',
    'Q6': 'PASS: what it feels like, then what lies under it, then the reader\'s response',
    'Q7': 'PASS: every cause is one this reader may have had, now including a practice',
    'Q8': 'PASS: the dose, the body and the practice are the physical factors; memories, mindset and setting the rest',
    'Q9': 'PASS: one clause added, said plainly',
}
R = {
 'NEW-B330b.receipt.json': {
  'payoff': [
   'they recognize what the overwhelm felt like, and that the mind keeps making meanings out of it',
   'they see what lies under those meanings, the dose and their body, or how hard they pushed a practice, so a state from meditation or breathwork fits too',
   'they see the other causes, from their past, their mindset and the people or place',
   'they stop blaming themselves or the person they sat with, since blame makes it heavier'],
  'follows': [
   'it opens the paragraph after his line that a bad trip can mean several things: here is the first, the flood',
   '"those interpretations" are S1\'s meanings; this says what is under them',
   'more of the factors S2 began',
   'having named causes, it turns to how to treat the person who had them'],
  'link': [None, 'Underlying those interpretations', 'Old painful memories could have been triggered', 'because blaming anyone only makes it heavier'],
  'placement': 'his (Re)defining "Bad Trip", second paragraph: after "It can refer to various things which may be intertwined", which it begins to list; before his shadow-work paragraph',
  'opens': 'it names the state they would recognize in themselves: too much at once, nothing making sense',
  'same_point': 'the causes are said here and, for the ones it doesn\'t name, in the paragraph after the picture ("may also come from drug interactions, sleep deprivation ..."); the practice case also in Psychological First Aid\'s practice paragraph, which is about what to do, not why: none merged',
  'q': Q_ALL,
 },
 'NEW-B366a.receipt.json': {
  'payoff': [
   'they plan the session\'s start, end and middle before it begins, whether it is a substance or a practice',
   'they rest first and start early, so food, company and sleep fit in afterward'],
  'follows': [
   'it opens the section under its heading and picture: the heading\'s beginning and end, said as what to do',
   'the first of the things to plan: rest and timing'],
  'link': [None, 'Rest and timing come first'],
  'placement': 'the first paragraph of his Give the Session a Beginning and an End, under the heading and the picture',
  'opens': 'it tells someone planning a session what this section is for: thinking the session through before it begins',
  'same_point': 'none: read the section from its heading to the next (The Fear/Panic Loop) for planning ahead and rest: only here',
  'q': {
   'Q1': 'PASS: S1 opens on "If you\'re planning a session", S2 on "Rest and timing come first"',
   'Q2': 'PASS: each instruction says what it is for (so there\'s time afterward for food, company and sleep)',
   'Q3': 'PASS: "ahead of time" fits a substance and a practice alike, which "before you take anything" didn\'t',
   'Q4': 'PASS: no term a reader wouldn\'t know',
   'Q5': 'PASS: S2 is the first thing to think through, as S1 asks',
   'Q6': 'PASS: plan first, then the first step of the plan',
   'Q7': 'PASS: both are for someone planning a session now',
   'Q8': 'N/A: no group of items',
   'Q9': 'PASS: one phrase changed',
  },
 },
 'NEW-B319.receipt.json': {
  'payoff': ['they put a vision\'s command off: write it down, sleep, and talk it over with one grounded person once their head is clear, whether it came from a drug or a practice'],
  'follows': ['it is the section\'s rule in bold, after the heading (Visions Are Not Commands): what to do instead of acting'],
  'link': [None],
  'placement': 'No Rash Actions: Visions Are Not Commands, its bold rule, before the paragraph on treating trip content as experience-content',
  'opens': 'it tells someone who feels a vision is telling them to act what to do instead, right away',
  'same_point': 'the next paragraph ends "it can wait until the state has passed", the reason for this rule, and the list before it says "Until you have slept and eaten, maybe don\'t ...": they make the rule\'s point from two sides, none merged',
  'q': {
   'Q1': 'PASS: it opens on what to do',
   'Q2': 'PASS: each step is something the reader does, and the heading says what they are for',
   'Q3': 'PASS: "once your head is clear" fits a state from a practice, which "sober" didn\'t',
   'Q4': 'PASS: no term a reader wouldn\'t know',
   'Q5': 'N/A: one sentence',
   'Q6': 'PASS: write it down, sleep, then talk it over: the order they happen in',
   'Q7': 'PASS: for someone in that state now',
   'Q8': 'N/A: no group of items',
   'Q9': 'PASS: one phrase changed',
  },
 },
}
for f, v in R.items():
    p = HERE / f
    r = json.loads(p.read_text())
    for k, s in enumerate(r['sentences']):
        s['payoff'], s['follows'] = v['payoff'][k], v['follows'][k]
        if 'link' in s:
            s['link'] = v['link'][k]
    r['placement'] = v['placement']
    r['opens']['why_reading'] = v['opens']
    r['same_point'] = v['same_point']
    r['questions'] = v['q']
    p.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
print('filled', len(R))
