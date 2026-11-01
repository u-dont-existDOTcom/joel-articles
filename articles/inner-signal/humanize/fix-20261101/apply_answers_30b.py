"""Put Joel's answers to Hypnosis Guide Cards, 30 October (REVIEW-30b) into the hypnosis guide, with every card's fate.

His export of 2026-11-01 18:50 UTC (../fix-20261030/tries/review/ANSWERS-20261101-1850.json, word for word), sent with his
message of 18:57 UTC (joel-20261101-1857-message.txt here): 10 approved, 1 rejected (S-24: "this is that ai slop
creeping back in with the over careful wording"), 10 revised, his own versions; most of them he checked in Pangram as
sections ("it's all human now on its own", "passes high conf human").

- An approved card goes in as the card showed it (its edit's "after").
- A revised card goes in as his version, word for word, one paragraph a line, except the obvious typos (TYPOS, each
  listed). Where his version takes in more of the section than the card did (a heading renamed, paragraphs around the
  card rewritten), it replaces the paragraphs PLANS names, and every paragraph of the guide it doesn't name stays.
- S-24 stays as it is.

  python3 articles/inner-signal/humanize/fix-20261101/apply_answers_30b.py [--check]

Writes HUMANIZED-SO-FAR.md and APPLIED-30b.json (each card's fate, the typo fixes, what each plan replaced).
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text  # noqa: E402

GUIDE = H / 'HUMANIZED-SO-FAR.md'
REVIEW = H / 'fix-20261030' / 'tries' / 'review' / 'REVIEW-30b.json'
ANSWERS = H / 'fix-20261030' / 'tries' / 'review' / 'ANSWERS-20261101-1850.json'

# obvious typos in his versions: (card, wrong, right, why)
TYPOS = [
    ('N-145', 'Don\'t embarass us!', 'Don\'t embarrass us!', 'a spelling slip'),
    ('R-162', 'really int he room', 'really in the room', 'a slip of the space'),
    ('R-162', 'Can you can pause', 'Can you pause', 'a doubled word'),
    ('N-238', 'to hear.  Call me', 'to hear. Call me', 'a double space'),
    ('N-238', 'as they go.  The nice thing', 'as they go. The nice thing', 'a double space'),
    ('N-238', 'like Jim Carey saying', 'like Jim Carrey saying', 'the actor\'s name is spelled Carrey'),
    ('N-269', 'Already Trancey?  Stabilize', 'Already Trancey? Stabilize', 'a double space'),
    ('N-580', 'For example,  I don\'t use', 'For example, I don\'t use', 'a double space'),
    ('N-580', 'resistance we need overcome', 'resistance we need to overcome', 'a missing "to"'),
    ('N-587', 'a red cloth,  then', 'a red cloth, then', 'a double space'),
]

# Each revised card: the guide's paragraphs his version replaces, in order, as (block, [his line numbers]); a block
# with no lines is taken out (its words are in his version); a block given as 'same' is his first line unchanged (a
# heading the guide has) and stays. Every block's text is checked before it changes.
PLANS = {
    'N-145': [(144, 'same'), (145, [1])],
    'R-162': [(162, [0])],
    'N-238': [(231, [0]), (232, [1, 2, 3, 4]), (233, []), (234, []), (235, []), (236, []), (237, [5]),
              (238, [6, 7, 8]), (239, [9, 10, 11]), (240, [12, 13])],
    'T-495': [(247, [0])],
    'N-269': [(265, [0]), (266, [1]), (267, [2]), (268, [3]), (269, [4])],
    'T-339': [(338, [0]), (339, [1, 2])],
    'R-381': [(381, [0]), (382, [1])],
    'R-508': [(508, [0, 1, 2])],
    'N-580': [(573, 'same'), (574, [1]), (575, [2, 3, 4, 5, 6, 7])] + [(i, []) for i in range(576, 586)],
    'N-587': [(587, [0]), (588, [1]), (589, [2]), (590, [3]), (591, [4]), (592, [5]), (593, [6]), (595, [7]),
              (596, [8])],
}
# the first words of each planned block as it is now (so a plan can't land on the wrong paragraph)
STARTS = {144: 'Your inherited parent script', 145: 'One important thing to become aware', 162: 'A. Prepare yourself',
          231: 'Induction: gathering attention', 232: 'Inductions serve to gather you up', 233: 'Get trancey enough',
          234: 'What an induction is actually doing', 235: 'Getting yourself ready', 236: 'Test: For a simple',
          237: 'Please don’t put six metaphors', 238: '"Keep it simple, stupid!"', 239: 'Using metaphors and imagery',
          240: 'When you\'re writing the script', 247: 'Let your response guide you', 265: 'Already open? Contain',
          266: 'This is for when you\'re already open', 267: 'Know that you\'re already open', 268: 'Orient yourself',
          269: 'Say something like, "Only what I can integrate', 338: '"I notice the tightness',
          339: 'Sometimes the invitation just isn\'t right', 381: 'Is there a way you could try this',
          382: 'Ask: “Show me one body sensation', 508: 'Bridge words are words like', 573: 'What I will not use NLP for',
          574: 'Here is a list of things I do not do', 575: 'I do not use NLP to talk myself out',
          585: 'I do not use NLP to get compliance', 587: 'Here is a rough outline', 588: 'Induce or contain yourself',
          593: 'Bring in your 3 good adults', 594: 'Anchor your good state', 595: 'Future pace a scenario',
          596: 'Check in with your body', 597: 'Get yourself out of the altered state'}


def his_lines(cid, text):
    """His version: obvious typos fixed (each recorded), then one paragraph (or heading) a line, spaces trimmed."""
    notes = []
    t = text
    for c, wrong, right, why in TYPOS:
        if c == cid:
            assert t.count(wrong) == 1, (cid, wrong)
            t = t.replace(wrong, right)
            notes.append('typo fixed (%s): "%s" -> "%s"' % (why, wrong, right))
    lines = [ln.strip() for ln in t.split('\n') if ln.strip()]
    return lines, notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    review = json.loads(REVIEW.read_text(encoding='utf-8'))
    answers = json.loads(ANSWERS.read_text(encoding='utf-8'))
    md = GUIDE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert sha == review['article']['sha256'] == answers['article']['sha256'], 'the guide changed since the cards page'
    assert answers['review_id'] == review['review_id']
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl)
    for i, s in STARTS.items():
        assert bl[i]['text'].startswith(s), (i, bl[i]['text'][:60])
    A = {x['id']: x for x in answers['items']}
    new_raw, fates, lost, notes_all, replaced = {}, {}, [], {}, {}
    for s in review['suggestions']:
        x = A[s['id']]
        sid = s['id']
        if x['status'] == 'approved':
            assert s['advice'] == 'approve'
            i = s['edits'][0]['block']
            assert s['edits'][0]['before'] == bl[i]['text'] and i not in new_raw, sid
            new_raw[i] = [set_block_text(raw[i], s['edits'][0]['after'], lost)]
            fates[sid] = 'approved: the card\'s version went in'
            if x['comment']:
                notes_all[sid] = ['his comment: ' + x['comment']]
            continue
        if x['status'] == 'rejected':
            fates[sid] = 'rejected: stays as it is'
            notes_all[sid] = ['his comment: ' + x['comment']]
            continue
        assert x['status'] == 'revise' and x['your_version'].strip(), sid
        lines, notes = his_lines(sid, x['your_version'])
        plan = PLANS[sid]
        used = []
        for i, part in plan:
            assert i not in new_raw, (sid, i)
            if part == 'same':
                assert lines[0] == bl[i]['text'], (sid, i)
                used.append(0)
                continue
            new_raw[i] = [set_block_text(raw[i], lines[k], lost) for k in part]
            used += part
        assert sorted(used) == list(range(len(lines))), (sid, sorted(used), len(lines))
        replaced[sid] = [{'block': i, 'was': bl[i]['text'], 'now': [lines[k] for k in part] if part != 'same' else 'same'}
                         for i, part in plan]
        fates[sid] = 'his version'
        notes_all[sid] = notes + (['his comment: ' + x['comment']] if x['comment'] else [])
    out = []
    for i, r in enumerate(raw):
        out += new_raw.get(i, [r])
    new = '\n\n'.join(out) + '\n'
    rec = {'answers': str(ANSWERS.relative_to(H)), 'answers_sha256': hashlib.sha256(ANSWERS.read_bytes()).hexdigest(),
           'before_sha256': sha, 'after_sha256': hashlib.sha256(new.encode('utf-8')).hexdigest(),
           'fates': fates, 'notes': notes_all, 'replaced': replaced,
           'typos': [{'card': c, 'was': w, 'now': r, 'why': y} for c, w, r, y in TYPOS], 'links_dropped': lost,
           'changed_blocks': sorted(new_raw)}
    print(json.dumps({k: v for k, v in rec.items() if k in ('before_sha256', 'after_sha256', 'links_dropped')},
                     indent=1))
    from collections import Counter
    print(Counter(v.split(':')[0] for v in fates.values()), len(new_raw), 'blocks changed')
    if not a.check:
        GUIDE.write_text(new, encoding='utf-8')
        (HERE / 'APPLIED-30b.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
