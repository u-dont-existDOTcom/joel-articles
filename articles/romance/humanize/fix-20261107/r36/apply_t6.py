#!/usr/bin/env python3
"""His answers on the sixth page (2026-11-23 19:36 UTC, review/teach-20261123/ANSWERS-T6.json) as a layer over the
fixed version, after r35's: HIS-T6.json, which whole/build.py applies.

- The seven cards he approved (J-B10, J-B84, J-B201, J-B220, J-B379, J-B412, J-B453) go in as the cards had them, each
  with the check that read it (r35/README.md); J-B84 is a cut.
- Q-B442 and Q-B257: his own versions, from his comments, with his checks ("high conf hum", "now human high conf all").
- Q-B480 "makes sense to me as is": no change; the sentence is on the keep-as-is list (whole/KEEP-AS-IS.json).
- 366 and 440: his own sentences, where my r34 layer had swapped his "honestly" for another word. His message of the same
  turn: "you can't just switch honestly for compassionately always that's working sometimes, but like authentically,
  genuinely, those are more real synonyms, and honestly is also ok sometimes just it's overused". His word goes back in
  both, as his checks read them (Human High); the article's other three uses were model text and keep their swaps.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
ANS = json.loads((ROOT / 'articles/romance/review/teach-20261123/ANSWERS-T6.json').read_text(encoding='utf-8'))
CARDS = {c['id']: c for c in json.loads((HERE.parent / 'r35' / 'CARDS.json').read_text(encoding='utf-8'))}
ASKS = {c['id']: c for c in json.loads((HERE.parent / 'r35' / 'ASKS.json').read_text(encoding='utf-8'))}
R34 = {c['live']: c for c in json.loads((HERE.parent / 'r34' / 'MINE-R34.json').read_text(encoding='utf-8'))['changes']}
items = {i['id']: i for i in ANS['items']}

LIVE = {  # each card's live paragraphs, in the order of its "old" texts (found by their exact words in the fixed version)
    'J-B10': [6, 7], 'J-B84': [74], 'J-B201': [192], 'J-B220': [213], 'J-B379': [355], 'J-B412': [390], 'J-B453': [427],
    'Q-B442': [419], 'Q-B257': [250],
}
TESTED = {  # the check that read each approved card's text (r35/README.md); J-B84's cut rests on his own check
    'J-B10': 'https://www.pangram.com/history/46351c02-95e5-41d5-8044-3413fb07cc47',
    'J-B84': 'https://www.pangram.com/history/c12ff059-dc9e-432d-bc7f-bddb2219ebaf',
    'J-B201': 'https://www.pangram.com/history/ef1f216b-1b56-4d93-8744-c471e85a5933',
    'J-B220': 'https://www.pangram.com/history/b7aa8694-67eb-4170-9bb3-3ef562c34919',
    'J-B379': 'https://www.pangram.com/history/2b637949-e160-4da0-a203-c7a0332a367d',
    'J-B412': 'https://www.pangram.com/history/74a3b94f-ed02-4fc4-9fd8-44aeb688bb8c',
    'J-B453': 'https://www.pangram.com/history/ab01adee-1d7d-4259-a060-215bce4186e2',
}
HIS = {  # his own versions: the text after "high conf ..." and its link in his comment
    'Q-B442': 'https://www.pangram.com/history/48952c2b-ff84-4e2c-97f8-c6bff836ceac',
    'Q-B257': 'https://www.pangram.com/history/126e846d-7968-4de2-a5ba-4124a5685dae',
}

out = []
for cid in ('J-B10', 'J-B84', 'J-B201', 'J-B220', 'J-B379', 'J-B412', 'J-B453'):
    it, card = items[cid], CARDS[cid]
    assert it['status'] == 'approved', cid
    for n, old, new in zip(LIVE[cid], card['old'], card['new']):
        out.append({'card': cid, 'kind': 'para', 'live': n, 'before': old, 'after': [new] if new else [],
                    'comment': 'approved', 'his_checks': [TESTED[cid]], 'title': card['title']})
for qid in ('Q-B442', 'Q-B257'):
    it, ask = items[qid], ASKS[qid]
    assert it['status'] == 'answered', qid
    comment = it['comment']
    link = HIS[qid]
    assert link.rsplit('/', 1)[1] in comment, qid
    version = comment.split('\n\n', 1)[1].strip()  # his paragraph comes after the line with his check's link
    assert version.startswith(ask['block'][:40]), qid
    out.append({'card': qid, 'kind': 'para', 'live': LIVE[qid][0], 'before': ask['block'], 'after': [version],
                'comment': comment.split('\n\n', 1)[0].strip(), 'his_checks': [link], 'title': ask['title']})
assert items['Q-B480']['comment'].strip() == 'makes sense to me as is'
HIS_WORD = {  # his checks of his own sentence: 440 exactly as here (r30/HIS-T4.json M-440); 366's first two sentences
    # are his (ANSWERS-T2.json, TEACH-JEALOUSY-POLY: "i re-did all of it, now human high conf"), the paragraph as here
    # read in its section in the section pass (r32-74-jealousy-on-trial-p2: Human, High)
    440: ['https://www.pangram.com/history/42b7f544-83cb-4879-8bf8-ad977962888d',
          'https://www.pangram.com/history/f72e86ef-fd45-4fa2-934d-14e776d8021a'],
    366: ['https://www.pangram.com/history/8f1e5924-1921-4136-8815-d09f45d295e5',
          'https://www.pangram.com/history/5a4b81cd-deb8-48c9-97c2-8d1e0fa089f3'],
}
for n in (366, 440):
    c = R34[n]
    out.append({'card': 'his word back in %d' % n, 'kind': 'para', 'live': n, 'before': c['after'][0],
                'after': [c['before']],
                'comment': 'honestly is also ok sometimes just it\'s overused (his message of 2026-11-23 19:36 UTC); '
                           'his own sentence, as his check read it',
                'his_checks': HIS_WORD[n], 'was': 'r34 ' + c['card']})
data = {'about': __doc__.strip().split('\n\n')[0], 'answers': 'review/teach-20261123/ANSWERS-T6.json',
        'links': [], 'embeds': [], 'changes': out}
(HERE / 'HIS-T6.json').write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('changes', len(out))
