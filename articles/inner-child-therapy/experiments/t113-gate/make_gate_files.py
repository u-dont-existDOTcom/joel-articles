#!/usr/bin/env python3
"""Turn 113: the owner-delivery gate's files (docs/HUMANIZATION-OWNER-DELIVERY-GATE.md) for every proposal on the review
sheet that has new words in it (experiments/t113-shape/proposals.py, SECTIONS.json): sixteen case headings and the 109 A
sentence. Each gets a folder with DRAFT.txt (the exact words, no newline added), CONTEXT.txt (its section as it would
read, plain text, headings marked with their #s, holding the draft once) and SOURCE.txt (what the words must be true to:
for a heading, the paragraphs it stands over as they are now; for the sentence, Joel's own sentence and the study title).
Lifted headings (the paragraph's own words), lead drops (words taken away) and paragraph splits add no words, so they
are outside the gate (GATE.md says so), and the cold reads read them in their sections.

  python3 make_gate_files.py      # writes the folders and runs init for each"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
GATE = ROOT / 'tools' / 'humanization' / 'owner_delivery_gate.py'
SEC = json.loads((HERE.parent / 't113-shape' / 'SECTIONS.json').read_text(encoding='utf-8'))['sections']

NAMES = {  # (section id, the new words) -> folder name
    ('H-guard', 'Earning its trust'): 'guard-trust',
    ('H-guard', "If it won't step back"): 'guard-step-back',
    ('H-guard', "If it feels like it's all your fault"): 'guard-fault',
    ('H-start', 'Which thoughts to talk to'): 'start-thoughts',
    ('H-start', "If it's anxiety"): 'start-anxiety',
    ('H-start', 'If a part says no'): 'start-says-no',
    ('H-change', 'When the words sound empty'): 'change-empty',
    ('H-change', "If the relief doesn't last"): 'change-relief',
    ('H-change', "If you'd rather stop"): 'change-stop',
    ('H-change', 'If your case is different'): 'change-different',
    ('H-escape', 'If you might be vulnerable'): 'escape-vulnerable',
    ('H-escape', 'Coming back confused or spaced out'): 'escape-confused',
    ('H-therapist', 'IFS and Schema Therapy'): 'therapist-ifs',
    ('H-hooks', 'Can they change?'): 'hooks-change',
    ('H-hooks', 'Feeling less safe'): 'hooks-less-safe',
    ('H-borrow', 'For guiding'): 'borrow-guiding',
}
SOLOMON_OLD = ('This psychological trick has a rich history around it, and even has a name, Solomon’s paradox, after the '
               'biblical king everybody brought their disputes to, who then wrecked his own life.')
SOLOMON_NEW = ('This psychological trick has a rich history around it, and the blind spot behind it even has a name, '
               'Solomon’s paradox, after the biblical king everybody brought their disputes to, who then wrecked his own life.')


def context_of(r):
    lines = [r['heading']]
    for x in r['new']:
        lines.append(('#' * int(x['kind'][1]) + ' ' + x['text']) if x['kind'] != 'p' else x['text'])
    return '\n\n'.join(lines)


def under(r, heading):
    """The paragraphs the heading would stand over, as they are now (old text), up to the next heading."""
    new = r['new']
    k = next(n for n, x in enumerate(new) if x['kind'] != 'p' and x['text'] == heading)
    paras = []
    for x in new[k + 1:]:
        if x['kind'] != 'p':
            break
        paras.append(x['text'])
    # the old text of those paragraphs: each new paragraph is an old one, or part of one, with a lead dropped
    olds = []
    for p in paras:
        hit = [o for o in r['old'] if p[1:] in o or p in o]
        olds.append(hit[0] if hit else p)
    return paras, olds


def write(name, draft, context, source, change):
    d = HERE / name
    d.mkdir(exist_ok=True)
    assert context.count(draft) == 1, (name, context.count(draft))
    (d / 'DRAFT.txt').write_text(draft, encoding='utf-8')
    (d / 'CONTEXT.txt').write_text(context + '\n', encoding='utf-8')
    (d / 'SOURCE.txt').write_text(source + '\n', encoding='utf-8')
    (d / 'CHANGE.txt').write_text(change + '\n', encoding='utf-8')
    files = ['--draft', str(d / 'DRAFT.txt'), '--context', str(d / 'CONTEXT.txt'), '--source', str(d / 'SOURCE.txt'),
             '--manifest', str(d / 'ADMISSION.json')]
    if not (d / 'ADMISSION.json').exists():
        out = subprocess.run([sys.executable, str(GATE), 'init'] + files, capture_output=True, text=True)
        if out.returncode not in (0, 2):
            sys.exit(out.stdout + out.stderr)
    m = json.loads((d / 'ADMISSION.json').read_text(encoding='utf-8'))
    print('%-18s lint %-6s %s' % (name, m['lint']['verdict_at_init'], [f['label'] for f in m['lint']['findings']]))


for r in SEC:
    ctx = context_of(r)
    for w in r['new_words']:
        if w['kind'] == 'heading':
            name = NAMES[(r['id'], w['new'])]
            paras, olds = under(r, w['new'])
            src = ('A new heading, proposed for Joel\'s review, to stand over these paragraphs of the section "%s" (Joel\'s '
                   'idea of 2026-10-25: "give each paragraph a little heading ... they can just skip the parts that don\'t '
                   'apply very easily, assuming the headings are very clear"). The paragraphs as they are now:\n\n%s'
                   % (r['heading'].lstrip('# '), '\n\n'.join(olds)))
            change = ('A case heading, "%s", over the paragraph%s that start%s "%s ...", one level below the section\'s heading. '
                      'It must say what the part under it is about, in words a reader skimming for their own situation '
                      'would recognize, and add no claim the paragraphs don\'t make.'
                      % (w['new'], 's' if len(paras) > 1 else '', '' if len(paras) > 1 else 's', ' '.join(paras[0].split()[:8])))
            write(name, w['new'], ctx, src, change)
        else:
            assert r['id'] == 'W-solomon'
            ctx_plain = ctx
            assert SOLOMON_NEW in ctx_plain
            src = ('Joel\'s own sentence (his message of 2026-10-25 21:40 UTC, 108.1), in the article now:\n\n%s\n\n'
                   'His answer to question 109, "109a": "the name goes on the gap, and the rest of your sentence stays." '
                   'The study the sentence links on "Solomon’s paradox" is Grossmann and Kross, 2014, Psychological Science, '
                   'titled "Exploring Solomon\'s paradox: self-distancing eliminates the self-other asymmetry in wise reasoning '
                   'about close relationships in younger and older adults": Solomon\'s paradox is the asymmetry, that people '
                   'reason more wisely about other people\'s problems than about their own. "This psychological trick" links '
                   'Kross and Grossmann, 2012, "Boosting wisdom: distance from the self enhances wise reasoning, attitudes, and '
                   'behavior".' % SOLOMON_OLD)
            change = ('In Joel\'s sentence, "and even has a name" becomes "and the blind spot behind it even has a name", so the '
                      'name Solomon\'s paradox goes on the gap the trick gets around (as the study names it), not on the trick. '
                      'Every other word of his sentence stays, his curly apostrophes too.')
            write('solomon', SOLOMON_NEW, ctx_plain, src, change)
