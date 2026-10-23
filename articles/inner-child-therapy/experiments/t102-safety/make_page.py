#!/usr/bin/env python3
"""Turn 102: SAFETY-CUTS.md, the proposed cuts of repeated and blanket safety lines (question 97), from CUTS.json.

CUTS.json: {"intro": [...], "groups": [{"title": "...", "intro": "...", "items": [
    {"id": "97.1", "title": "...", "start": "the paragraph's first words", "edits": [["old", "new"], ...],
     "who": "...", "kind": "...", "why": "...", "loses": "...", "also": "(optional)", "pick": "A" or "B"}]}],
 "outro": [...]}
Each item's paragraph must start with "start" in the article (comments stripped) and each old text must occur in it
exactly once, so a stale item fails instead of showing the wrong text. The page shows the paragraph as it is, with
each old text struck through and its replacement after it, then the paragraph after the edit. CUTS-AFTER.json keeps
every paragraph's after-text, for the install and the Pangram texts once Joel picks."""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import reader_blocks  # noqa: E402

md = re.sub(r'<!--.*?-->', '', (ROOT / 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8'), flags=re.S)
seq = reader_blocks(md)


def path_to(i):
    heads, level = [], 9
    for k in range(i, -1, -1):
        t, b = seq[k]
        if t == 'h':
            n = len(b) - len(b.lstrip('#'))
            if n < level:
                heads.append(b.lstrip('#').strip())
                level = n
            if n == 1:
                break
    return ' > '.join(reversed(heads))


def main():
    spec = json.loads((HERE / 'CUTS.json').read_text(encoding='utf-8'))
    out = list(spec['intro']) + ['']
    after_all = {}
    for g in spec['groups']:
        out += ['## ' + g['title'], '', g['intro'], '']
        for it in g['items']:
            hits = [i for i, (t, b) in enumerate(seq) if t == 'p' and b.startswith(it['start'])]
            assert len(hits) == 1, (it['id'], it['start'], hits)
            i = hits[0]
            para = seq[i][1]
            shown, after = para, para
            for old, new in it['edits']:
                assert para.count(old) == 1, (it['id'], old)
                core = old.strip()
                lead = old[:len(old) - len(old.lstrip())]
                trail = old[len(old.rstrip()):]
                shown = shown.replace(old, lead + '~~' + core + '~~' + ((' ' + new.strip()) if new.strip() else '') + trail, 1)
                after = after.replace(old, new, 1)
            after_all[it['id']] = {'start': it['start'], 'before': para, 'after': after}
            out += ['### %s %s' % (it['id'], it['title']), '',
                    '*%s* · %s · %s' % (path_to(i), it['who'], it['kind']), '',
                    '> ' + shown.replace('\n', '\n> '), '',
                    '**Why:** ' + it['why'], '']
            if it.get('also'):
                out += ['**Said already:** ' + it['also'], '']
            out += ['**What a reader loses:** ' + it['loses'], '',
                    '**After:**', '', '> ' + after.replace('\n', '\n> '), '',
                    '- **A%s:** cut it.' % (' (my pick)' if it['pick'] == 'A' else ''),
                    '- **B%s:** keep it.' % (' (my pick)' if it['pick'] == 'B' else ''), '']
    out += spec.get('outro', [])
    (HERE / 'SAFETY-CUTS.md').write_text('\n'.join(out).rstrip('\n') + '\n', encoding='utf-8')
    (HERE / 'CUTS-AFTER.json').write_text(json.dumps(after_all, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print('wrote SAFETY-CUTS.md,', sum(len(g['items']) for g in spec['groups']), 'items')


if __name__ == '__main__':
    main()
