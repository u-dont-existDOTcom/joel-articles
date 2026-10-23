#!/usr/bin/env python3
"""Turn 103, fourth round: The Inner Guide's new h2 A Belonging Deeper Than Any Group, as it would be with GPT's move
(question 100): P9 after 98.9's cut (100% Human alone, #169) and P10 without the naming aside, its middle sentence
rewritten (draft s05: P10 without the aside read 76% AI, a High window on the long "keeps watching ... and keeps
reminding" sentence, #196). P10 is under 50 words now, so the h2 is its check. Writes TEXTS-4.json."""
import json
import pathlib

from make_texts import line, seq
from make_texts_2 import at

HERE = pathlib.Path(__file__).resolve().parent
D = HERE.parent / 't103-tries' / 'drafts'
i = at('## A Belonging Deeper Than Any Group', 'h')
assert seq[i + 1][1].startswith('The Guide also points beyond itself') and seq[i + 2][1].startswith('With that under you')
TEXTS = {'t103d_ig_belonging_s05': [seq[i], seq[i + 1], ('p', (D / 's05-97_12-p10.txt').read_text(encoding='utf-8').strip())]}
NAMES = {'t103d_ig_belonging_s05': 'The Inner Guide\'s new h2 A Belonging Deeper Than Any Group, with the naming aside moved to after P1 and P10\'s middle sentence rewritten (draft s05)'}

if __name__ == '__main__':
    out = {n: '\n'.join(line(k, b) for k, b in blocks) for n, blocks in TEXTS.items()}
    (HERE / 'TEXTS-4.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    names = json.loads((HERE / 'NAMES.json').read_text(encoding='utf-8'))
    names.update(NAMES)
    (HERE / 'NAMES.json').write_text(json.dumps(names, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for n, t in out.items():
        (HERE / 'texts' / (n + '.txt')).write_text(t, encoding='utf-8')
        print(n, len(t.split()), 'words'); print(t)
