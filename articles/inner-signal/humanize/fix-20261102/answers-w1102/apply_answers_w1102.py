"""Put Joel's answers to Hypnosis Guide Cards, 2 November (2) (REVIEW-W1102) into the hypnosis guide, and record the read.

His export of 2026-11-02 20:37 UTC (ANSWERS-20261102-2038.json here, word for word), sent with his message of 20:38 UTC
(joel-20261102-2038-message.txt):
- C-141, approved: his inner child guide's lines in Working with your guards, as the card showed them.
- C-384, revise, with his own version of the Troubleshooting section up to and through the card's paragraph ("Nothing
  happens" and "It feels fake"), and his comment: "this section so far with that has it as human low
  https://www.pangram.com/history/fe024a3a-3338-43a2-a8cc-f5d4579e6fe4 ... here's the fully human high conf section til now
  (text pasted as my version): https://www.pangram.com/history/b7fc49b6-e142-4456-a1a5-9d0bc6c646e1". His version goes in as
  he checked it: the two headings stay; "Check if there's a way you could try this on a smaller scale." and the line of
  requests after it become his one paragraph; the next two paragraphs are his; his "But seriously..." paragraph follows
  them; the two paragraphs after (the parent script, the fake feeling) stay as they were, since his text stops before them
  ("til now"). Only his double space inside the Bush quote and the space after "!!!" go (obvious typos, his rule).

  python3 articles/inner-signal/humanize/fix-20261102/answers-w1102/apply_answers_w1102.py [--check]
Writes HUMANIZED-SO-FAR.md, APPLIED-W1102-ANSWERS.json and read/READ-RECORD.json.
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
F = HERE.parent
H = F.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text  # noqa: E402

GUIDE = H / 'HUMANIZED-SO-FAR.md'
REVIEW = F / 'w1102fix' / 'REVIEW-W1102.json'
ANSWERS = HERE / 'ANSWERS-20261102-2038.json'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    review = json.loads(REVIEW.read_text(encoding='utf-8'))
    answers = json.loads(ANSWERS.read_text(encoding='utf-8'))
    md = GUIDE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert sha == review['article']['sha256'] == answers['article']['sha256'], 'the guide changed since the cards page'
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl)
    A = {x['id']: x for x in answers['items']}
    S = {s['id']: s for s in review['suggestions']}
    new_raw, lost, fates = {}, [], {}
    # C-141, approved: the card's edit
    assert A['C-141']['status'] == 'approved' and not A['C-141']['comment']
    for e in S['C-141']['edits']:
        assert e['before'] == bl[e['block']]['text']
        new_raw[e['block']] = [set_block_text(raw[e['block']], e['after'], lost)]
    fates['C-141'] = 'approved: the card\'s version went in'
    # C-384, revise: his version of the section through the card's paragraph
    x = A['C-384']
    assert x['status'] == 'revise' and x['your_version'].strip()
    parts = [p.strip() for p in re.split(r'\n\s*\n', x['your_version'].strip())]
    p1, p2, p3, p4 = parts
    l1 = p1.split('\n')
    assert l1[0] == 'Troubleshooting' and l1[1] == 'Nothing happens' and len(l1) == 3
    l2 = p2.split('\n')
    assert l2[0] == 'It feels fake' and len(l2) == 2
    fix = lambda s: re.sub(r' {2,}', ' ', s).rstrip()
    i = [b['i'] for b in bl if b['level'] == 1 and b['text'] == 'Troubleshooting'][0]
    assert bl[i + 1]['text'] == 'Nothing happens' and bl[i + 4]['text'] == 'It feels fake'
    assert bl[i + 2]['text'].startswith('Check if there\'s a way') and bl[i + 3]['text'].startswith('Try out these requests')
    assert bl[i + 6]['text'] == S['C-384']['edits'][0]['before'] or bl[i + 6]['text'].startswith('You could say something like')
    new_raw[i + 2] = [set_block_text(raw[i + 2], fix(l1[2]), lost)]
    new_raw[i + 3] = []
    new_raw[i + 5] = [set_block_text(raw[i + 5], fix(l2[1]), lost)]
    new_raw[i + 6] = [set_block_text(raw[i + 6], fix(p3), lost), fix(p4)]
    fates['C-384'] = ('revise: his version of Nothing happens and It feels fake through the card\'s paragraph went in, '
                      'with his "But seriously..." paragraph after it; his check of it: Human Written, every window High '
                      '(https://www.pangram.com/history/b7fc49b6-e142-4456-a1a5-9d0bc6c646e1)')
    assert not lost, lost
    out = []
    for j, r in enumerate(raw):
        out += new_raw.get(j, [r])
    new = '\n\n'.join(out) + '\n'
    after = hashlib.sha256(new.encode('utf-8')).hexdigest()
    rec = {'answers': ANSWERS.name, 'answers_sha256': hashlib.sha256(ANSWERS.read_bytes()).hexdigest(),
           'before_sha256': sha, 'after_sha256': after, 'fates': fates, 'changed_blocks': sorted(new_raw),
           'blocks': [len(bl), len(out)], 'his_checks': {
               'with the card in, his section so far': 'https://www.pangram.com/history/fe024a3a-3338-43a2-a8cc-f5d4579e6fe4',
               'his version, the section so far': 'https://www.pangram.com/history/b7fc49b6-e142-4456-a1a5-9d0bc6c646e1'},
           'typos_fixed': ['the double space inside the Bush quote', 'the space after "!!!"']}
    print(json.dumps(rec, indent=1))
    if a.check:
        return
    GUIDE.write_text(new, encoding='utf-8')
    (HERE / 'APPLIED-W1102-ANSWERS.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    olds = {b['text'] for b in bl}
    changed = [b['text'] for b in sr.blocks(new) if b['text'] not in olds]
    d = HERE / 'read'
    d.mkdir(parents=True, exist_ok=True)
    cr.record(d, findings=[], coverage=sorted({cr.phash(t) for t in changed}), dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: the %d paragraphs his answers to the cards of 2 November (2) changed '
                      '(C-141 approved, C-384 his own version), read by the lead session in place (E284, E294)'
                      % (after[:8], len(changed)))


if __name__ == '__main__':
    main()
