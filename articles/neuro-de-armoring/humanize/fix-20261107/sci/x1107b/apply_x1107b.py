"""Apply his answers to the three rewritten section B cards (ANSWERS-X1107B-20261107-1349.json, 13:49 UTC).

All three approved with no comment: SB-37b (what the storm feels like), SB-38b (the GluD finding, the guess with its
mechanism, the "Low" row out) and SB-40b (the Vacuum becomes the Brake, with the NAC dose line's note).

  python3 articles/neuro-de-armoring/humanize/fix-20261107/sci/x1107b/apply_x1107b.py [--write]
"""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[2]
sys.path.insert(0, str(HERE))
import texts_b as T  # noqa: E402

ANS = HERE / 'ANSWERS-X1107B-20261107-1349.json'
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
CARDS = {'SB-37b': [('B37b', 'The Mechanism: Excess')],
         'SB-38b': [('B38b', 'The Signal Dial')],
         'SB-40b': [('B40b', 'The Fix ("Lock'), ('B119b', 'NAC: 1.8g')]}


def plain(t):
    return re.sub(r'\*([^*]+)\*', r'\1', re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t))


def main(write=False):
    md = ARTICLE.read_text(encoding='utf-8')
    answers = json.loads(ANS.read_text(encoding='utf-8'))
    assert answers['article']['sha256'] == hashlib.sha256(md.encode('utf-8')).hexdigest(), \
        'the article changed since his page'
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    applied = []
    for card in answers['items']:
        sid = card['id']
        assert card['status'] == 'approved', (sid, card['status'])
        shown = [x.strip() for x in card['my_version'].split('\n\n')]
        for n, (key, prefix) in enumerate(CARDS[sid]):
            (i,) = [k for k, b in enumerate(raw) if b.startswith(prefix)]
            after = T.TEXTS[key]
            assert plain(after).strip() == shown[n], (sid, key, 'the card showed another text')
            raw[i] = after
            applied.append({'card': sid, 'key': key, 'block_starts': prefix, 'after': plain(after)})
    out = '\n\n'.join(raw) + '\n'
    for a in applied:
        print('in:', a['card'], a['key'])
    if write:
        ARTICLE.write_text(out, encoding='utf-8')
        (HERE / 'APPLIED-X1107B.json').write_text(json.dumps({
            'review_id': answers['review_id'], 'answered_utc': answers['exported_at'], 'applied': applied,
            'article_sha256_after': hashlib.sha256(ARTICLE.read_bytes()).hexdigest()},
            ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print('written')
    return 0


if __name__ == '__main__':
    sys.exit(main('--write' in sys.argv))
