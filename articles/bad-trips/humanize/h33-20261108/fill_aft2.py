#!/usr/bin/env python3
"""fill_aft2.py - TEST-AFT2's receipt (the second try at What Kind of Aftermath Is This?'s first two kinds, after the
panel on AFT1 agreed on four of its six sentences: panel-AFT1/PANEL.md). The base's sentences come from earlier receipts.

  python3 fill_aft2.py
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
 'When symptoms linger, it\'s worth figuring out what kind they are, since "I\'m broken" covers everything at once and each kind is helped by something different.':
  ('they start by working out which kind theirs is, and why', 'it opens the section on what its heading asks', None),
 'Leftover anxiety and fear tend to settle with grounding and a quiet, steady routine, with fewer people and less noise.':
  ('if theirs is anxiety and fear, they ground themselves and keep things quiet and steady', 'the first kind', 'Leftover anxiety and fear'),
 "It also helps to check the scary thoughts against what's going on around you, the way CBT does it.":
  ('they test the scary thoughts against what is happening', 'one more thing for the same kind', 'It also helps'),
 'Sleep problems are their own thing.': ('they see the next kind is separate', 'it turns from the first kind to the second', 'Sleep problems'),
 'With nightmares or bad nights, sleep comes first, which means no more substances and no pushing a practice for a while.':
  ('if theirs is sleep, they protect it and take nothing more and push no practice', 'what to do for the kind just named', 'With nightmares or bad nights'),
 'Bring in a professional if the fear or the bad nights hang on, or get really bad.':
  ('they know when these two need a professional', 'the limit for both kinds just named', 'the fear or the bad nights'),
}
p = HERE / 'TEST-AFT2.receipt.json'
r = json.loads(p.read_text())
for s in r['sentences']:
    pay, fol, link = NEW.get(s['s']) or (EARLIER[s['s']]['payoff'], EARLIER[s['s']]['follows'], EARLIER[s['s']].get('link'))
    s['payoff'], s['follows'] = pay, fol
    if 'link' in s:
        s['link'] = link or "none: the first sentence after its heading"
r['placement'] = 'a test text: the Human base (the first five minutes to his reminder), then the section heading and the first part of the aftermath list as sentences'
r['opens']['why_reading'] = 'it names what to do first when someone could get hurt in the next five minutes'
r['same_point'] = 'none: read What Kind of Aftermath Is This? to the next heading for anxiety, sleep and professional help: the other kinds follow, each with its own help'
r['needed'] = {'reader': 'a fresh Haiku agent given tools/humanization/needed_read_brief.md with the paragraph (NEEDED-READ.md, AFT2)', 'unneeded': [], 'kept': {}}
r['questions'] = {
 'Q1': 'PASS: each sentence opens on its point ("Leftover anxiety and fear", "Sleep problems", "Bring in a professional")',
 'Q2': 'PASS: each instruction is the reader\'s, with what it is for',
 'Q3': 'PASS: "no more substances and no pushing a practice" names both cases',
 'Q4': 'PASS: "CBT" and "grounding" are explained earlier in the guide',
 'Q5': 'PASS: "since" gives the reason; "also" adds to the same kind; the turn to sleep is said',
 'Q6': 'PASS: name it, then each kind, then the limit',
 'Q7': 'PASS: for someone whose symptoms linger now',
 'Q8': 'PASS: each remedy sits with its kind',
 'Q9': 'PASS: the kinds said as their own sentences, not labels',
}
p.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
print('filled')
