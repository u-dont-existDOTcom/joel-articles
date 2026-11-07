"""Apply his answers to section B's science cards (ANSWERS-X1107A-20261107-1310.json, 2026-11-07 13:10 UTC).

Approved: SB-37, SB-39, SB-41, SB-42 (which cuts leucine), SB-148. He marked SB-38 and SB-40 revise, so those
paragraphs stay exactly as they are -- block 38 as he wrote it on 7 November, and the two NAC lines as the post has
them -- and their new versions go to him on the next page. SB-37 is approved with a question about its last sentence,
which the next page answers; the approved text goes in now.

  python3 articles/neuro-de-armoring/humanize/fix-20261107/sci/x1107a/apply_x1107a.py [--write]
"""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[2]
ROOT = H.parents[2]
sys.path.insert(0, str(HERE))
import texts as T  # noqa: E402
from receipts import plain  # noqa: E402

ANS = HERE / 'ANSWERS-X1107A-20261107-1310.json'
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
# each card's new text, with the raw-Markdown prefix of the paragraph it replaces
CARDS = {'SB-37': [('B37', 'The Mechanism: Excess')], 'SB-39': [('B39', 'D-serine may support')],
         'SB-41': [('B41', 'The Lock (Zinc')], 'SB-42': [('B42', 'The Repair (Leucine')],
         'SB-148': [('B148', 'Use D-Serine for acute')],
         'SB-40': [('B40', 'The Fix ("Lock'), ('B119', 'NAC: 1.8g')], 'SB-38': [('B38', 'The Signal Dial')]}


def main(write=False):
    md = ARTICLE.read_text(encoding='utf-8')
    answers = json.loads(ANS.read_text(encoding='utf-8'))
    assert answers['article']['sha256'] == hashlib.sha256(md.encode('utf-8')).hexdigest(), \
        'the article changed since his page'
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    applied, held = [], []
    for card in answers['items']:
        sid = card['id']
        if card['status'] != 'approved':
            held.append({'card': sid, 'status': card['status'], 'comment': card.get('comment', '').strip()})
            continue
        for key, prefix in CARDS[sid]:
            (i,) = [k for k, b in enumerate(raw) if b.startswith(prefix)]
            after = T.TEXTS[key]
            assert plain(raw[i]).strip() == card['before'].strip(), (sid, plain(raw[i])[:90])
            assert plain(after).strip() == card['my_version'].strip(), (sid, 'the card showed another text')
            raw[i] = after
            applied.append({'card': sid, 'key': key, 'block_starts': prefix, 'whose_words': 'mine, he approved',
                            'after': plain(after)})
    out = '\n\n'.join(raw) + '\n'
    for a in applied:
        print('in:', a['card'], a['key'])
    for h in held:
        print('held (%s):' % h['status'], h['card'])
    if write:
        ARTICLE.write_text(out, encoding='utf-8')
        (HERE / 'APPLIED-X1107A.json').write_text(json.dumps({
            'review_id': answers['review_id'], 'answered_utc': answers['exported_at'],
            'applied': applied, 'held': held,
            'article_sha256_after': hashlib.sha256(ARTICLE.read_bytes()).hexdigest(),
        }, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print('written')
    return 0


if __name__ == '__main__':
    sys.exit(main('--write' in sys.argv))
