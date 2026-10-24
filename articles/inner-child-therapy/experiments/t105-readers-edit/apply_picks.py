#!/usr/bin/env python3
"""Turn 105: my check of each reader's item (pick and note, from edit-picks.json or caveat-picks.json) into the read's ITEMS.json,
which clarity_read.py collect keeps when the readers' reports are collected again."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent


def norm(s):
    return ' '.join(s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').split())


def main(kind, picks_file):
    items_p = HERE / kind / 'ITEMS.json'
    items = json.loads(items_p.read_text(encoding='utf-8'))
    picks = {norm(k): v for k, v in json.loads((HERE / picks_file).read_text(encoding='utf-8')).items()}
    missing = []
    for x in items:
        v = picks.get(norm(x['quote']))
        if not v:
            missing.append(x['key'])
            continue
        x['my_pick'], x['note'] = v[0], v[1]
        if len(v) > 2:
            x['whose'] = v[2]
        if len(v) > 3:
            x['status'] = v[3]
    items_p.write_text(json.dumps(items, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(kind, len(items), 'items;', 'no pick yet:', ', '.join(missing) or 'none')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
