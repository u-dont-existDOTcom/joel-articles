#!/usr/bin/env python3
"""fill_aft1.py - TEST-AFT1's receipt: the base's sentences from earlier receipts (as make_receipts.py does), the
aftermath carry's below. The needed read is in NEEDED-READ.md.

  python3 fill_aft1.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
EARLIER = {}
for f in sorted(HERE.parent.glob('h*/TEST-*.receipt.json')):
    try:
        for s in json.loads(f.read_text())['sentences']:
            if s.get('payoff') and s.get('follows'):
                EARLIER.setdefault(s['s'], s)
    except (ValueError, KeyError):
        continue
NEW = {
 'What Kind of Aftermath Is This?': ('they know this part sorts the aftermath into kinds', "the section's heading, after the base", None),
 'When symptoms linger, try to name the pattern.': ('they start by naming which kind of aftermath theirs is', 'it opens the section on what its heading asks', None),
 '"I\'m broken" lumps everything together, and different patterns need different support.': ('they see why naming it helps: each kind needs its own support', 'the reason for the instruction before it', '"I\'m broken" lumps everything together'),
 "If it's mostly anxiety and fear that stayed with you, grounding helps, and so does a steady routine with less going on around you.": ('if theirs is anxiety and fear, they ground themselves and keep a quiet, steady routine', 'the first kind', "If it's mostly anxiety and fear"),
 "You can also check the scary thoughts against what's happening, the way CBT does it.": ('they test the scary thoughts against what is happening', 'one more thing for the same kind', 'You can also'),
 'If you can\'t sleep or keep having nightmares, look after your sleep first, and stay away from more substances or intense practice for now.': ('if theirs is sleep, they protect it and take nothing more and push no practice', 'the second kind', "If you can't sleep"),
 'If either one is severe or drags on, get professional help.': ('they know when these two need a professional', 'the limit for both kinds just named', 'If either one'),
}
p = HERE / 'TEST-AFT1.receipt.json'
r = json.loads(p.read_text())
for s in r['sentences']:
    e = NEW.get(s['s'])
    if e:
        pay, fol, link = e
    else:
        old = EARLIER[s['s']]
        pay, fol, link = old['payoff'], old['follows'], old.get('link')
    s['payoff'], s['follows'] = pay, fol
    if 'link' in s:
        s['link'] = link or "none: the first sentence after its heading"
r['placement'] = 'a test text: the Human base (the first five minutes to his reminder), then the section heading and the first part of the aftermath list as sentences'
r['opens']['why_reading'] = 'it names what to do first when someone could get hurt in the next five minutes'
r['same_point'] = 'none: read What Kind of Aftermath Is This? to the next heading for anxiety, sleep and professional help: the other kinds follow in the list, each with its own help'
r['needed'] = {'reader': 'a fresh Haiku agent given tools/humanization/needed_read_brief.md with the paragraph (NEEDED-READ.md, AFT1)', 'unneeded': [], 'kept': {}}
r['questions'] = {
 'Q1': 'PASS: each sentence opens on its point; each kind opens on "If it\'s ..." in the reader\'s own terms',
 'Q2': 'PASS: each instruction is something the reader does, with what it is for',
 'Q3': 'PASS: "more substances or intense practice" names both cases',
 'Q4': 'PASS: "CBT" and "grounding" are explained earlier in the guide (the thinking traps, the Grounding Menu)',
 'Q5': 'PASS: the reason follows the instruction; "also" adds to the same kind; "either one" points back to both',
 'Q6': 'PASS: name it, then each kind, then the limit',
 'Q7': 'PASS: for someone whose symptoms linger now',
 'Q8': 'PASS: each remedy sits with its kind',
 'Q9': 'PASS: the list\'s labels said as conditions, one kind a sentence or two',
}
p.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
print('filled')
