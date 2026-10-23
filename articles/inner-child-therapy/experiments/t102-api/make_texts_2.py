#!/usr/bin/env python3
"""Turn 102, second round. The pain and sharing paragraphs read 100% Human alone (round 1), so their h3s, each whole:
Physical Pain Makes It Harder (heading and four paragraphs, before its h4) and Opening up honestly to the right people at
the right pace (heading and three paragraphs). The Untangling paragraph read 100% AI alone with my 95.2 sentence, in one
window over all of it, and it had never been checked alone before, so: (a) the paragraph as it was before this turn,
alone, to see whether my sentence is the cause. A new wording of my sentence waits for that result (draft u01 FAILed the
linter's coach register, with "you can tell what you actually want"). Writes TEXTS-2.json."""
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import reader_blocks  # noqa: E402
from make_texts import line, seq, find  # noqa: E402

old_md = subprocess.run(['git', 'show', 'f40adcc2:articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'], cwd=ROOT,
                        capture_output=True, text=True, check=True).stdout
old_seq = reader_blocks(re.sub(r'<!--.*?-->', '', old_md, flags=re.S))
old_u = [b for k, b in old_seq if k == 'p' and b.startswith('Differentiation is slow')]
assert len(old_u) == 1
D = HERE.parent / 't102-tries' / 'drafts'
pain = find('### Physical Pain Makes It Harder')
assert seq[pain + 5][1].startswith('#### Listen To Your Body')
share = find('### Opening up honestly to the right people')
assert seq[share + 4][1].startswith('## Other Folks Also Have Hooks')
TEXTS = {
    't102b_pain_h3': seq[pain:pain + 5],
    't102b_sharing_h3': seq[share:share + 4],
    't102b_untangle_old': [('p', old_u[0])],
}

if __name__ == '__main__':
    out = {n: '\n'.join(line(k, b) for k, b in blocks) for n, blocks in TEXTS.items()}
    (HERE / 'TEXTS-2.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for n, t in out.items():
        (HERE / 'texts' / (n + '.txt')).write_text(t, encoding='utf-8')
        print('%-20s %4d words | %s' % (n, len(t.split()), t[:90].replace('\n', ' / ')))
