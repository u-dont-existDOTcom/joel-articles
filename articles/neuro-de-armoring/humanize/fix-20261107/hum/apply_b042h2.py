"""Block 42's humanized version in: it read Human (High) in his account's web app.

https://www.pangram.com/history/67dd2887-06b0-4c66-8ff2-dbf0bf389e24 (Human Written, 0% AI, one window Human at High,
75 words). A tested change that keeps what the paragraph says goes into the article without a card
(gates gut-2026-11-07b, bad-trips-2026-11-07a); its reason and link are in this turn's report and in RESULTS.md.

  python3 articles/neuro-de-armoring/humanize/fix-20261107/hum/apply_b042h2.py [--write]
"""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
sys.path.insert(0, str(HERE))
import drafts_hum2 as D2  # noqa: E402
import drafts_hum as H1  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
LINK = 'https://www.pangram.com/history/67dd2887-06b0-4c66-8ff2-dbf0bf389e24'


def main(write=False):
    md = ARTICLE.read_text(encoding='utf-8')
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    (d,) = [x for x in D2.D if x['name'] == 'B042h2']
    (i,) = [k for k, b in enumerate(raw) if b.startswith(d['starts'])]
    before, after = raw[i], d['text']
    assert H1.plain(after) != H1.plain(before)
    raw[i] = after
    print('block 42 before:', H1.plain(before)[:80])
    print('block 42 after :', H1.plain(after)[:80])
    if write:
        ARTICLE.write_text('\n\n'.join(raw) + '\n', encoding='utf-8')
        (HERE / 'APPLIED-B042H2.json').write_text(json.dumps({
            'key': 'B042h2', 'result': 'Human Written, one window Human at High, 75 words', 'link': LINK,
            'before': H1.plain(before), 'after': H1.plain(after),
            'article_sha256_after': hashlib.sha256(ARTICLE.read_bytes()).hexdigest()},
            ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print('written')
    return 0


if __name__ == '__main__':
    sys.exit(main('--write' in sys.argv))
