#!/usr/bin/env python3
"""fill_start.py - the making-sense receipt of TEST-DRUG-START.txt: his Give the Session (round 24, as he checked it) with
"before you take anything" said drug-neutrally ("think through beforehand how ...") and "themself" fixed. His sentences are
his humanized version of the model's list, so each gets its payoff and follows like mine (gate E373).

  python3 fill_start.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
P = HERE / 'TEST-DRUG-START.receipt.json'
r = json.loads(P.read_text())
rows = [
 ('they know the section is about planning a session\'s start and end', 'the section\'s heading', None),
 ('they plan the start, the end and the middle before the session, whatever kind it is', 'it opens the section on what its heading promises', None),
 ('they rest first and start early, so food, company and sleep fit in afterward', 'the first thing to plan', 'Rest and timing come first'),
 ('they set up the room and decide in advance what would make them call for help', 'the next thing to plan, the place and the limit', 'Set up the space you\'ll be in'),
 ('they go in curious, without demanding a particular revelation or breakthrough', 'from the room to the mind they bring into it', 'Go in curious'),
 ('they see that preparing with love can be enough on its own', 'it turns the gentle intention into what it can do', 'Sometimes people find that'),
 ('they hear it said plainly: the preparation can be the whole work', 'it finishes the thought of the sentence before', 'The work is already done'),
 ('they get an example of preparation doing the work', 'his story, after the claim it shows', 'One woman I met in Kenya'),
 ('they see what she understood before the trip', 'the story\'s turn', 'Before she took the shrooms'),
 ('they see what she did with the anxiety instead', 'what she did once she understood it', 'So instead'),
 ('they see the outcome, with no trip needed', 'the end of the story', 'Her addictions vanished'),
 ('if they are taking a drug, they know what and how much, and check its interactions and medical concerns', 'it turns back from the case that needed no trip to the reader who is taking something', 'though'),
 ('they use a dose they know as a starting point, and expect their sensitivity to vary', 'from what to check to what a known dose tells them', 'If you\'ve taken this amount before'),
 ('they don\'t jump in at a new dose or a new intensity of practice', 'the other case: a dose or practice they haven\'t done before', 'If you\'ve never taken this dose'),
 ('they know what the sitter does during it, and who the sitter is', 'from before the session to during it', 'During the experience'),
 ('they close the session as it winds down', 'from during to the end', 'As the experience winds down'),
 ('they stop adding stimulation, and why he dislikes redosing', 'the first step of the closure', 'Stop adding stimulation'),
 ('they check where they are and what day it is', 'the next step of the closure', 'Check where you are'),
 ('they eat and drink to replenish their electrolytes', 'the next step of the closure', 'Eat and drink a bit'),
 ('they note what they want to remember, and tell the body it\'s over with a massage', 'the next step of the closure', 'Jot down anything'),
 ('they keep the rest of the day and the next morning free, and why', 'after the session: the time after it', 'Keep the rest of the day free'),
]
assert len(rows) == len(r['sentences']), (len(rows), len(r['sentences']))
for s, (pay, fol, link) in zip(r['sentences'], rows):
    s['payoff'], s['follows'] = pay, fol
    if 'link' in s:
        s['link'] = link if link else "none: the section's first sentence after its heading"
r['placement'] = 'Give the Session a Beginning and an End, after The Other Bypass and Hang up the phone, before The Fear/Panic Loop: the planned session, before anyone is in trouble (its last line sends a reader already in trouble to the triage app)'
r['opens']['why_reading'] = 'it tells someone planning a session that this section is for thinking it through before it begins'
r['same_point'] = 'none merged: read from the heading to The Fear/Panic Loop; food and sleep afterward come up in P1 and P7 (rest first so there\'s time for them; the day kept free), which he wrote that way'
r['needed'] = {'reader': 'a fresh Haiku agent that saw the first paragraph, its heading and what it is for (NEEDED-READ.md, paragraph B); the other paragraphs are his as he checked them', 'unneeded': [], 'kept': {}}
r['questions'] = {
 'Q1': 'PASS: each paragraph opens on its point (planning, the space, the story, the drug case, the sitter, closure, the day after)',
 'Q2': 'PASS: the instructions say what they are for (time for food and sleep; not jumping in; not cementing worse patterns)',
 'Q3': 'PASS: "beforehand" fits a substance and a practice, which "before you take anything" didn\'t',
 'Q4': 'PASS: "sitter" is glossed where it is first used; "plastic" glossed as "vulnerable, flexible"',
 'Q5': 'PASS: each step follows the session\'s order: before, during, the end, after',
 'Q6': 'PASS: the order of a session',
 'Q7': 'PASS: every step is for someone planning a session',
 'Q8': 'PASS: the closure steps are all for the end of a session',
 'Q9': 'PASS: one step a sentence in the closure',
}
P.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
print('filled')
