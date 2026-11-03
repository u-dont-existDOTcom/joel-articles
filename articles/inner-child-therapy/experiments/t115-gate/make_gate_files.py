#!/usr/bin/env python3
"""Turn 115: the owner-delivery gate's files (docs/HUMANIZATION-OWNER-DELIVERY-GATE.md) for each reworded paragraph of the
pass (experiments/t115-pass/fixes.py, kind "reword"), and the cuts' sheet for the same three reviewers.

Each reworded paragraph gets a folder with DRAFT.txt (its changed sentences as they would read, from the first changed one
to the last, plain reader text, no newline added), CONTEXT.txt (its block as it would read: the heading above it, with its #s, and the block's paragraphs, holding the
draft once), SOURCE.txt (the paragraph as it is now, what the change must keep, and for the safety paragraph the grounding's
MUSTs and the guide's own lines) and CHANGE.txt. A cut adds no words, so it is outside the gate; CUTS.json gives each cut's
paragraph before and after, its block after, and what it keeps and drops, for the reviewers to judge in one file per role.

  python3 make_gate_files.py      # writes the folders and CUTS.json, and runs init for each folder"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
EXP = HERE.parent
GATE = ROOT / 'tools' / 'humanization' / 'owner_delivery_gate.py'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(EXP / 't115-pass'))
from paragraphs_alone import reader_blocks, plain  # noqa: E402
from substack_check_text import smart  # noqa: E402
from fixes import FIXES  # noqa: E402

ART = (EXP.parent / 'HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8')
CAND = (EXP / 't115-pass' / 'CANDIDATE-ARTICLE.md').read_text(encoding='utf-8')
CRISIS_SOURCE = (
    'The grounding review of this paragraph\'s first draft (experiments/t65-guide/GROUNDING-ks01.md) set its MUSTs: "a crisis '
    'line or emergency number counts as another human being; a clause" and, for "How do I know I\'m about to act?", "if unsure, '
    'treat it as if you are; a clause". Joel\'s turn-79 answer made it "A crisis line counts". His published guide says, in this '
    'place: "If you’re about to act, can’t stop yourself, are badly disoriented or intoxicated, or have the means in front of you, '
    'first get another human being involved and put distance between yourself and the means. That isn’t my answer to whether '
    'life is worth living. It keeps the question open long enough to investigate it." The grounding marked "That isn\'t my '
    'answer" and "keeps the question open" as points the paragraph must carry. Every safety instruction, its conditions and '
    'their order must stay.')


def line(kind, b):
    t = plain(re.sub(r'^#+\s*', '', b) if kind == 'h' else b)
    t = smart(t).replace('‍', '').replace('️', '')
    return ('#' * len(re.match(r'^#+', b).group(0)) + ' ' + t) if kind == 'h' else t


def seq(md):
    return [(k, b) for k, b in reader_blocks(re.sub(r'<!--.*?-->', '', md, flags=re.S))]


def block_of(md, heading):
    s = seq(md)
    hits = [i for i, (k, b) in enumerate(s) if k == 'h' and re.sub(r'^#+\s*', '', b) == heading]
    assert len(hits) == 1, (heading, len(hits))
    i = hits[0]
    out = [line(*s[i])]
    for k, b in s[i + 1:]:
        if k == 'h':
            break
        if k == 'p':
            out.append(line(k, b))
    return out


def para_of(md, f):
    """The paragraph of md that holds the fix's text (old in the article, new in the candidate)."""
    key = f['new'] if md is CAND else f['old']
    hits = [b for k, b in seq(md) if k == 'p' and key in b]
    assert len(hits) == 1, (f['id'], len(hits))
    return line('p', hits[0])


def changed_span(old_p, new_p):
    """The new paragraph's sentences from the first one that isn't in the old paragraph to the last one, as one span."""
    ss = re.split(r'(?<=[.!?”)])\s+(?=[A-Z“(])', new_p)
    olds = set(re.split(r'(?<=[.!?”)])\s+(?=[A-Z“(])', old_p))
    idx = [i for i, x in enumerate(ss) if x not in olds]
    span = ' '.join(ss[idx[0]:idx[-1] + 1])
    assert span in new_p, span
    return span


def init(d):
    files = ['--draft', str(d / 'DRAFT.txt'), '--context', str(d / 'CONTEXT.txt'), '--source', str(d / 'SOURCE.txt'),
             '--manifest', str(d / 'ADMISSION.json')]
    if not (d / 'ADMISSION.json').exists():
        out = subprocess.run([sys.executable, str(GATE), 'init'] + files, capture_output=True, text=True)
        if out.returncode not in (0, 2):
            sys.exit(out.stdout + out.stderr)
    m = json.loads((d / 'ADMISSION.json').read_text(encoding='utf-8'))
    return m['lint']['verdict_at_init'], [x['label'] for x in m['lint']['findings']]


def main():
    cuts = {}
    for f in FIXES:
        old_p, new_p = para_of(ART, f), para_of(CAND, f)
        ctx = block_of(CAND, f['block'])
        assert new_p in ctx, f['id']
        if f['kind'] == 'cut':
            cuts[f['id']] = {'where': f['where'], 'before': old_p, 'after': new_p, 'block_after': '\n\n'.join(ctx),
                             'tells': f['tells'], 'keeps': f['keeps'], 'drops': f['loses'], 'windows': f['windows']}
            continue
        d = HERE / f['id']
        d.mkdir(exist_ok=True)
        context = '\n\n'.join(ctx)
        assert context.count(new_p) == 1, f['id']
        draft = changed_span(old_p, new_p)
        assert context.count(draft) == 1, (f['id'], 'draft')
        (d / 'DRAFT.txt').write_text(draft, encoding='utf-8')
        (d / 'CONTEXT.txt').write_text(context + '\n', encoding='utf-8')
        src = ('The paragraph as it is now, in Joel\'s guide (his byline; written by an AI writer and approved by him):\n\n%s\n\n'
               'What the change must keep: %s.' % (old_p, f['keeps']))
        if f['id'] == 'F04':
            src += '\n\n' + CRISIS_SOURCE
        (d / 'SOURCE.txt').write_text(src + '\n', encoding='utf-8')
        change = ('In "%s", a whole-guide Pangram check (round 8) read %s. The tell: %s. The change: "%s" becomes "%s". It '
                  'must keep %s, and add no claim, tone or promise the paragraph as it is doesn\'t make; what it drops: %s.'
                  % (f['where'], f['windows'], f['tells'], smart(plain(f['old'])), smart(plain(f['new'])), f['keeps'], f['loses']))
        (d / 'CHANGE.txt').write_text(change + '\n', encoding='utf-8')
        v, labels = init(d)
        print('%s lint %-6s %s' % (f['id'], v, labels))
    (HERE / 'CUTS.json').write_text(json.dumps(cuts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('cuts:', ', '.join(cuts))


if __name__ == '__main__':
    main()
