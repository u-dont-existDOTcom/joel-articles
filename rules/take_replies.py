#!/usr/bin/env python3
"""take_replies.py - his replies on the rule tree's human view, into Git (rule R-replies-read; Joel, 2026-11-28 15:23 UTC:
"make the rule tree something i can reply to.").

The view saves each reply to its artifact's store as replies/<rule id>: {rule, title, mark, text, updated, tree_built}.
At the start of a turn the lane reads them (the artifact tools' db_list of the collection "replies", or the JSON he
copies from the view's "Your replies" tab and pastes in the chat), saves what it read as a file, and runs:

  python3 rules/take_replies.py FILE --read-at "2026-11-29T09:00Z"

FILE is the view's export ({"format": "rule-tree-replies-v1", "replies": [...]}) or a list of reply objects. Each reply
not already taken (same rule and same "updated") is added to rules/replies/replies.jsonl, and rules/replies/README.md is
rewritten: every reply, newest first, with its rule, his mark, his words and its fate. A fate is written in
rules/replies/fates.json ({"<rule id>|<updated>": "what was done"}) the turn the reply is answered; a reply without one
is listed as waiting.
"""
import argparse
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / 'replies'
LOG = OUT / 'replies.jsonl'
FATES = OUT / 'fates.json'
MARKS = {'right': 'Looks right', 'change': 'Change it', 'question': 'A question', '': ''}


def load(path):
    data = json.loads(pathlib.Path(path).read_text(encoding='utf-8'))
    items = data.get('replies') if isinstance(data, dict) else data
    out = []
    for x in items or []:
        if isinstance(x, dict) and isinstance(x.get('data'), dict):   # a db_list line: {id, data, ...}
            x = dict(x['data'], rule=x['data'].get('rule') or x.get('id'))
        if isinstance(x, dict) and x.get('rule'):
            out.append({k: x.get(k) for k in ('rule', 'title', 'mark', 'text', 'updated', 'tree_built')})
    return out


def key(x):
    return '%s|%s' % (x['rule'], x.get('updated') or '')


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('file')
    ap.add_argument('--read-at', required=True, help='when the lane read them (the turn\'s first clock reading)')
    a = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    seen = set()
    old = []
    if LOG.exists():
        for line in LOG.read_text(encoding='utf-8').splitlines():
            if line.strip():
                x = json.loads(line)
                old.append(x)
                seen.add(key(x))
    new = [dict(x, read_at=a.read_at) for x in load(a.file) if key(x) not in seen]
    with LOG.open('a', encoding='utf-8') as f:
        for x in new:
            f.write(json.dumps(x, ensure_ascii=False) + '\n')
    fates = json.loads(FATES.read_text(encoding='utf-8')) if FATES.exists() else {}
    allr = sorted(old + new, key=lambda x: x.get('updated') or '', reverse=True)
    tree = json.loads((HERE / 'tree.json').read_text(encoding='utf-8'))
    titles = {r['id']: r['title'] for b in tree['branches'] for g in b['groups'] for r in g['rules']}
    md = ['# His replies on the rule tree', '',
          'Each reply he wrote under a rule in the tree\'s human view, newest first, with what was done about it (rule '
          'R-replies-read). Written by `rules/take_replies.py`; the fates are in `fates.json`.', '']
    if not allr:
        md.append('None yet.')
    for x in allr:
        md += ['## %s' % titles.get(x['rule'], x.get('title') or x['rule']), '',
               '- **When:** %s UTC (read %s)' % (str(x.get('updated') or '?')[:16].replace('T', ' '), x.get('read_at')),
               '- **His mark:** %s' % (MARKS.get(x.get('mark') or '', x.get('mark')) or 'none'),
               '- **His words:** "%s"' % ' '.join(str(x.get('text') or '').split()),
               '- **Fate:** %s' % fates.get(key(x), 'waiting'), '']
    (OUT / 'README.md').write_text('\n'.join(md).rstrip('\n') + '\n', encoding='utf-8')
    print('%d new, %d in all, %d waiting' % (len(new), len(allr), sum(1 for x in allr if key(x) not in fates)))


if __name__ == '__main__':
    main()
