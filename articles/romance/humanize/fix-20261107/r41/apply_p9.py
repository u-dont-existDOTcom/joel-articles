#!/usr/bin/env python3
"""His answers on the ninth page (review/teach-20261124c/ANSWERS-T9.json, exported 2026-11-24 18:12 UTC) as layers over
the fixed version, after r40's: HIS-P9.json (his words) and MINE-R41.json (mine, from his answer), which whole/build.py
applies. Run it with both layers out of whole/build.py's output (it reads REPLACEMENTS.json as r40 left it).

- Q-C7 ("this whole section was messed up ... i fixed it:"): his version of "Muses & Directors" replaces the section,
  live 262 to 275: his first three paragraphs take 262 to 264, before the picture; the other five take 265 to 275. His
  version keeps from 270 to 275 only "If she micromanages, I start feeling useless.", "She might have a better idea, or
  just not want to do it, but she still wants me to take initiative" and "I don't think equality means dividing every role
  50/50."; the rest of them goes with his rewrite (named in the turn's report).
- Q-S5 ("change it"): "in modern years" becomes "in recent years" in his new opening of "Primal attraction".
- Q-S12 ("i meant doing as it's more active than living"): "worth doing" stays (whole/KEEP-AS-IS.json).
- Q-C1 ("right you are correct"): my reading said in the Labels paragraph (MINE-R41.json): a promise on paper is a red
  flag when it has to stand in for the closeness.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parent
ROOT = HERE.parents[4]
A = json.loads((ROOT / 'articles/romance/review/teach-20261124c/ANSWERS-T9.json').read_text(encoding='utf-8'))
items = {i['id']: i for i in A['items']}
POST = {}
for line in (FIX / 'live-check' / 'LIVE-POST-BLOCKS-20261123.jsonl').read_text(encoding='utf-8').splitlines():
    r = json.loads(line)
    if r.get('n') is not None:
        POST[r['n']] = r['text']
REPL = json.loads((FIX / 'whole' / 'REPLACEMENTS.json').read_text(encoding='utf-8'))
his, mine = [], []

c7 = items['Q-C7']
assert c7['status'] == 'answered' and 'i fixed it:' in c7['comment']
paras = [p.strip() for p in c7['comment'].split('i fixed it:', 1)[1].split('\n') if p.strip()]
assert len(paras) == 8 and paras[0].startswith('I don’t think equality') and paras[3].startswith('Key could')
his.append({'card': 'Q-C7', 'kind': 'run', 'live': [262, 263, 264], 'after': paras[:3], 'comment': c7['comment'][:120],
            'his_checks': [], 'title': 'Muses & Directors: his own version, before the picture'})
his.append({'card': 'Q-C7', 'kind': 'run', 'live': list(range(265, 276)), 'after': paras[3:], 'comment': c7['comment'][:120],
            'his_checks': [], 'title': 'Muses & Directors: his own version, after the picture'})

s5 = items['Q-S5']
assert s5['comment'].strip() == 'change it'
p5 = [t for t in REPL['260'] if 'in modern years' in t]
assert len(p5) == 1
his.append({'card': 'Q-S5', 'kind': 'para', 'live': 260, 'before': p5[0],
            'after': [p5[0].replace('in modern years', 'in recent years')], 'comment': 'change it', 'his_checks': []})

c1 = items['Q-C1']
assert c1['comment'].strip() == 'right you are correct'
cur = REPL['39'][0]
old = 'I don’t need to promise that on paper, and if I did, that would be more like a red flag.'
new = 'I don’t need to promise that on paper, and if a promise had to stand in for that closeness, that would be more like a red flag.'
assert cur.count(old) == 1
mine.append({'card': 'Q-C1', 'kind': 'para', 'live': 39, 'before': cur, 'after': [cur.replace(old, new)],
             'comment': 'right you are correct', 'his_checks': []})

# r41's check of the Labels section with Q-C1's words read one Medium window: the short "Which is why almost nobody has
# the full conversation." by itself (9 words; #343). The line runs on into the sentence it belongs to (way 18), in my
# paragraph from the junk pass (R38J-09).
cur41 = REPL['41'][0]
o41 = 'if they took it seriously. Which is why almost nobody has the full conversation.'
assert cur41.count(o41) == 1
mine.append({'card': 'R41-09', 'kind': 'para', 'live': 41, 'before': cur41,
             'after': [cur41.replace(o41, 'if they took it seriously, which is why almost nobody has the full conversation.')],
             'comment': 'a short line run on into its sentence (way 18), after a Medium window', 'his_checks': []})

# With the short line run on, the section's opener stood alone as a 43-word window and read Human Low (#347): it announced
# its point ("Here’s the funny thing about labels:"). Starting on the case instead, the section read Human High in one
# window (#348, https://www.pangram.com/history/48b96e7c-c31f-437b-809a-d16edc5b57e3).
cur38 = REPL['38'][0]
o38 = 'Here’s the funny thing about labels: you can call someone your boyfriend or girlfriend for years and still have one foot out the door, but the word at least shows pretty fast whether you both think you’re in the same relationship.'
assert cur38 == o38, cur38
mine.append({'card': 'R41-09-opener', 'kind': 'para', 'live': 38, 'before': cur38,
             'after': ['You can call someone your boyfriend or girlfriend for years and still have one foot out the door, but at least the word shows pretty fast whether you both think you’re in the same relationship.'],
             'comment': 'the announcing opener cut, after a Low window', 'his_checks': ['https://www.pangram.com/history/48b96e7c-c31f-437b-809a-d16edc5b57e3']})

(HERE / 'HIS-P9.json').write_text(json.dumps({'about': 'His answers on the ninth page (ANSWERS-T9.json, 2026-11-24 18:12 UTC): '
    'Q-C7 his version of Muses & Directors, Q-S5 "in recent years".', 'whose': 'his', 'changes': his},
    ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'MINE-R41.json').write_text(json.dumps({'about': 'Q-C1 of the ninth page ("right you are correct"): my reading said '
    'in the Labels paragraph.', 'whose': 'mine', 'changes': mine}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('HIS-P9:', len(his), 'changes; MINE-R41:', len(mine))
