#!/usr/bin/env python3
"""Turn 102, third round: the Untangling paragraph read 100% AI with my 95.2 sentence (#146) and Human Written with no AI
window without it (#150), so the sentence is the cause. u02 puts it as its own sentence, a plain reason with a
concrete picture ("And sometimes you need the break anyway, because it's hard to hear what you actually want while the old
programming is still playing in your ear."). A second shape (u03, a parenthesis on his sentence) waits: the ledger takes
one open prediction per lineage, so two shapes can't go in one batch. Writes TEXTS-3.json."""
import json
import pathlib

from make_texts import line

HERE = pathlib.Path(__file__).resolve().parent
D = HERE.parent / 't102-tries' / 'drafts'
TEXTS = {'t102c_untangle_u02': [('p', (D / 'u02-untangle.txt').read_text(encoding='utf-8').strip())],
}

if __name__ == '__main__':
    out = {n: '\n'.join(line(k, b) for k, b in blocks) for n, blocks in TEXTS.items()}
    (HERE / 'TEXTS-3.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for n, t in out.items():
        (HERE / 'texts' / (n + '.txt')).write_text(t, encoding='utf-8')
        print('%-20s %4d words | %s' % (n, len(t.split()), t[:90].replace('\n', ' / ')))
