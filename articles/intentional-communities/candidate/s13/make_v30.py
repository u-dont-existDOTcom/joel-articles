"""Section 13 draft v30 (2026-10-16): v29 (100% Human as a whole, 309g) with the fixes of its meaning reviews, round r19
(review-r19/trace-T1.md to trace-T6.md, STANCE-sofar.md; dispositions in review-r19/DISPOSITIONS-r19.md). Each fix is the
fewest words inside the sentence that's there, Emulate's where it is Emulate's, so the reading the whole section has doesn't
come back to the published sentences (the lesson of 307g to 309g). H3-P1 goes back to v28's text whole (T4: the scare quotes
and "despite" were round i's; v28's wording passed its traces in rounds r16 and r17 and read Human in 309g's variant v29b).
Writes v30.md and v30-fixes.json. Run from this folder: python3 make_v30.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
blocks = lambda md: [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]
V29 = dict(zip(IDS, blocks((HERE / 'v29.md').read_text(encoding='utf-8'))))
V28 = dict(zip(IDS, blocks((HERE / 'v28.md').read_text(encoding='utf-8'))))
FIX = [  # (paragraph, old, new, reviewer, reason)
 ('H1-P4', 'How long will your cash reserves last?', 'How long will your cash reserves last, if you have any?', 'T1-1',
  'the published "outside debts or cash runway if the community uses them": not every group holds cash'),
 ('H1-P4', 'gets too exhausted to keep going', 'gets exhausted', 'T1-3',
  'the published "one exhausted person": exhausted, not a coming breakdown'),
 ('H2-P3', 'whether or not LGBTQ+ people should be able to live openly', 'whether or not LGBTQ+ people would be able to live openly',
  'T2-2', 'the published "Could an LGBTQ+ member live openly": whether the community would, not what the reader thinks ought to be'),
 ('H2-P3', 'and be fully protected by the community', 'and stay fully protected by the community', 'T2-3',
  'the published "remain fully protected"'),
 ('H2-P3', 'and what should happen if one of', 'and what happens if one of', 'T2-2', 'the published "What happens if"'),
 ('H2-P3', 'You don’t have your community’s values on freedom and raising children complete until you answer these questions. Both of them!',
  'Until you answer these questions, you don’t have your community’s values on freedom and raising children complete. Both of them!',
  'T2-6', '"Both of them!" now follows the pair it means (freedom and raising children), not "these questions"; two cold reads '
  'paused at it'),
 ('H2-P3b', 'whether or not you are willing to experiment. The people next to you may feel that all experimenting ended in 1978,',
  'whether or not you are willing to experiment, because the people next to you may feel that the experiment ended in 1978,',
  'T3-3, T3-5', 'the published "It has to be declared, because the person beside you may believe the experiment ended in 1978"'),
 ('H2-P4', 'It may be an uncomfortable conversation', 'It’ll be an uncomfortable conversation', 'T3-4',
  'the published "the uncomfortable conversation": uncomfortable, not maybe'),
 ('H3-P5', "It's the first book I'd hand to any group starting out.", "Honestly, it's where I'd start for getting that order right!",
  'STANCE-sofar 1', 'the article\'s first step for a new group is the inner pl/ork ("What to Do This Month"); its appendix '
  'recommends this book "for sequencing, membership, money, land, and agreements". "Honestly" and the "!" keep it the '
  'paragraph\'s break: march r19 read 5a found none in "It\'s where I\'d start for getting that order right."'),
 ('H5-P1', 'There’s going to be times when someone has to go.', 'There may be times when someone has to go.', 'T4-1',
  'the published "cannot promise to keep everyone": it can happen, not it will'),
 ('H5-P1', 'just makes living together impossible for everyone else', 'just makes everyday life together impossible for everyone else',
  'T4-2', 'the published "makes ordinary shared life impossible"'),
 ('H5-P2', 'while the separation is being worked out', 'during the separation', 'T5-1', 'the published "during separation"'),
 ('H5-P2', 'and have the decision reviewed or appealed, without anyone being put in danger?',
  'and have the decision reviewed or appealed without putting others in danger?', 'T5-2',
  'the published "what review or appeal is possible without endangering others": the limit is on the review, and it protects others'),
 ('H5-P3', 'But when power started creeping upward in their own system, they pushed it back down again.',
  'But when power had crept up in their own system over the years, it took them a long review to push it back down.',
  'STANCE-sofar 2, T6-4', 'the article\'s Zapatista section: power "had crept up and consolidated itself at higher levels over '
  'time", reversed "After a long internal review, in 2023"; T6 asked for a cut, and the clause stays (round r9\'s disposition: it '
  'answers two cold reads and a stance check, from section 9) with its timing right'),
 ('H5-P4', 'This does not obviate the need for evidence, safeguarding, rulings, etc.',
  "A mediator doesn't obviate the need for evidence, safeguarding, rulings, etc.", 'T6-2',
  '"This" could be read as the advance choice or the distrust; a mediator is what doesn\'t replace them'),
 ('H5-P4', "it's time for a separation.", 'they still need a final separation.', 'T6-4',
  'the published "not a substitute for ... a final separation when consent is gone": "still" says mediation doesn\'t replace it, '
  'and it is final'),
]
text = dict(V29)
log = []
for pid, old, new, who, why in FIX:
    assert text[pid].count(old) == 1, (pid, old)
    text[pid] = text[pid].replace(old, new)
    log.append({'id': pid, 'old': old, 'new': new, 'review': who, 'why': why})
text['H3-P1'] = V28['H3-P1']
log.append({'id': 'H3-P1', 'old': V29['H3-P1'], 'new': V28['H3-P1'], 'review': 'T4-1, T4-2',
            'why': 'v28\'s text back whole: "whether or not your literature says everyone is equal" (round i\'s "despite" presumed the '
                   'literature claims equality) and no scare quotes on "founder"'})
bl = blocks((HERE / 'v29.md').read_text(encoding='utf-8'))
out = [bl[i] if pid is None else text[pid] for i, pid in enumerate(IDS)]
(HERE / 'v30.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v30-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(log), 'changes; paragraphs changed:', sorted({x['id'] for x in log}))
