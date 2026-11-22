#!/usr/bin/env python3
"""results_md.py - RESULTS.md for turn 34's fixes: every check of this folder with its link, each window's confidence and
the words of every window that isn't Human High, and what went into the guide.

  python3 results_md.py
"""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
LINK = 'https://www.pangram.com/history%s'
ROWS = [
 ('h43a', 'h42-08-fix1', 'Active Seizure 2, the Low sentence ("So it might help ...")', 'out: AI Low, worse than the guide\'s Human Low'),
 ('h43a', 'h42-17-fix1', 'Nausea Smoothers, the Low sentence', 'in (Low to High)'),
 ('h43a', 'h42-30-fix1', 'Grounding Menu 2, going outside and exercise', 'in (Low to Medium; the Medium one is mine, on the list for him)'),
 ('h43b', 'h42-08-fix2', 'Active Seizure 2, second try ("While a seizure continues ...")', 'out: Human Medium, but it drops "adjunct remedy" (KEEP-AS-IS K12): round 34\'s ADJUNCT card'),
 ('h43b', 'h42-20-p-fix1', 'DMSO\'s contraindications, the seizure item (paragraph check, E343)', 'in with the section'),
 ('h43b', 'h42-22-p-fix1', 'Ocean water\'s touch and effect (paragraph check)', 'in with the section'),
 ('h43b', 'h42-25-p-fix1', 'Niacin\'s B3 forms and the bridge to tripsitting, the list taken apart', 'out: the bridge AI High'),
 ('h43c', 'h42-20-fix1', 'Mental Stabilizers 3 (DMSO\'s interactions and contraindications), the whole section', 'in (AI to Human High throughout)'),
 ('h43c', 'h42-22-fix1', 'Mental Stabilizers 5 (ocean water and the charcoal waters), the whole section', 'in (AI to Human High throughout)'),
 ('h43c', 'h42-25-p-fix2', 'The bridge to tripsitting, without its list', 'out: the bridge AI High; next: the tell panel'),
 ('h43c', 'anchor-a1', 'Get One Human Anchor, its first two paragraphs', 'in (AI to Human; 38 earlier wordings read AI)'),
 ('h43c', 'harm-b1', 'Risk of Harm, its first paragraph, the nine reasons taken apart', 'teaching card (round 34, TEACH-HARM)'),
 ('h43d', 'h42-08-fix3', 'Active Seizure 2, third try, "adjunct remedy" kept', 'out: AI Low'),
 ('h43d', 'h42-41-p-fix1', 'Dealing With Shadow Thoughts, the during-a-trip lines in his list frame', 'out: AI Low and Medium, worse than the guide\'s two AI Low'),
 ('h43d', 'harm-b3', 'Risk of Harm, third wording, from the tell panel\'s notes (panel-harm-b2/PANEL.md)', 'teaching card (round 34, TEACH-HARM)'),
]
R = {}
for b in ('h43a', 'h43b', 'h43c', 'h43d'):
    R.update(json.loads((HERE / ('RESULTS-%s.json' % b)).read_text(encoding='utf-8')))
md = ['# The humanize pass\'s first fixes (2026-11-11, turn 34)', '',
      'Every fix is his five first (SKILL.md, "Writing for Pangram"), checked in his Pangram account after its prediction '
      '(`predict.py`), its making-sense receipt (`make_receipts.py`, with each fresh reader\'s needed read in '
      '`NEEDED-READ.md`) and the linter. The tests are `TEST-*.txt` (`build_tests.py`); what went into the guide is '
      '`apply_h43.py`. A section whose first check read Mixed was checked a paragraph at a time first (E343).', '',
      '| batch | test | what | result | windows (label, confidence, words) | link | fate |', '|---|---|---|---|---|---|---|']
for b, k, what, fate in ROWS:
    r = R[k]
    md.append('| %s | %s | %s | %s, %d%% AI | %s | [%s](%s) | %s |' % (b, k, what, r[0], round(r[1] * 100), r[3],
              r[5].strip('/')[:8], LINK % r[5], fate))
md += ['', '## Every window that isn\'t Human High', '']
for b, k, what, fate in ROWS:
    r = R[k]
    lines = r[6] + r[7]
    if lines:
        md += ['### %s ([result](%s))' % (k, LINK % r[5]), ''] + ['- %s' % x.replace('\n', ' / ') for x in lines] + ['']
md += ['## What I learned', '',
       '- His five fixes carried where his voice was already around the window: the remedies (DMSO, ocean water) went to '
       'Human High throughout, and Get One Human Anchor\'s opening read Human for the first time in 39 wordings once its '
       'point was said as what makes a trip worse and the crowd\'s four acts became two.',
       '- They didn\'t carry in a firm call-for-help list (Risk of Harm: AI 100% in each wording, after a tell panel that '
       'flagged its whole shape), nor in his J69 list frame with my words (Shadow Thoughts), as SKILL.md\'s fifth fix '
       'already says. The call-for-help list is round 34\'s teaching card.',
       '- A word on his keep list can hold a sentence at Low: Active Seizure\'s "adjunct remedy" read Medium without it '
       'and AI with it in my order, so the choice is his (round 34\'s ADJUNCT card).', '']
(HERE / 'RESULTS.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
print('ok', len(ROWS))
