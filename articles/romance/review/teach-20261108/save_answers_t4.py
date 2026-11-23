#!/usr/bin/env python3
"""Rebuild the Medium page's export (ANSWERS-T4.json) from his fields (ANSWERS-T4-his.json)
and the page's own fields (REVIEW-T4.json, PAGE-T4.md), in the export's key order.

The page's export adds, for each card: type, title, where ("<heading>, P<n>", n counting the
card paragraphs under that heading), advice, my_version and before (both the paragraph as the
page showed it). Run from anywhere: python3 save_answers_t4.py
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent


def blocks(md):
    return [b for b in re.split(r'\n\s*\n', md.strip('\n')) if b.strip()]


def main():
    his = json.loads((HERE / 'ANSWERS-T4-his.json').read_text(encoding='utf-8'))
    review = json.loads((HERE / 'REVIEW-T4.json').read_text(encoding='utf-8'))
    page = blocks((HERE / 'PAGE-T4.md').read_text(encoding='utf-8'))
    # where: heading and the card paragraph's number under it
    heading_of, number_of = {}, {}
    head, n = None, 0
    for i, b in enumerate(page):
        if b.startswith('#'):
            head, n = b.lstrip('#').strip(), 0
            continue
        n += 1
        heading_of[i], number_of[i] = head, n
    cards = {s['id']: s for s in review['suggestions']}
    items = []
    for h in his['items']:
        c = cards[h['id']]
        spans = c['spans'] if isinstance(c['spans'], list) else json.loads(c['spans'].replace("'", '"'))
        bi = spans[0]['block']
        para = page[bi]
        items.append({
            'id': h['id'], 'type': c['type'], 'title': c['title'],
            'where': '%s, P%d' % (heading_of[bi], number_of[bi]),
            'advice': c['advice'], 'status': h['status'], 'your_version': h['your_version'],
            'comment': h['comment'], 'my_version': para, 'before': para,
            'history': h['history'], 'updated': h['updated'],
        })
    counts = {k: sum(1 for i in items if i['status'] == k) for k in ('approved', 'rejected', 'revise', 'pending')}
    if counts != his['counts']:
        sys.exit('counts differ: %s vs %s' % (counts, his['counts']))
    if len(items) != len(cards):
        sys.exit('%d answers for %d cards' % (len(items), len(cards)))
    out = {k: his[k] for k in ('format', 'review_id', 'title', 'git_file', 'article', 'built', 'generator', 'exported_at', 'counts')}
    out['items'] = items
    (HERE / 'ANSWERS-T4.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('ANSWERS-T4.json: %d items, %s' % (len(items), counts))


if __name__ == '__main__':
    main()
