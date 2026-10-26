#!/usr/bin/env python3
"""Turn 113, gate round 2: the items whose words changed after round 1's reviews (change-working, start-stop, escape-trips,
escape-prone: new headings the reviewers asked for) and the items whose section changed around them (start-thoughts,
start-anxiety, change-empty, change-relief, change-stop, hooks-change), each in a new folder (<name>-r2, or its new name)
with its section as it reads now, so every review reads the context Joel will see. Round 1's folders stay as the record.
"Feeling less safe" left the gate: its heading is now the paragraph's own words (cold read B).

  python3 make_gate_files_r2.py"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
ROOT = HERE.parents[3]
GATE = ROOT / 'tools' / 'humanization' / 'owner_delivery_gate.py'
SEC = {r['id']: r for r in json.loads((HERE.parent / 't113-shape' / 'SECTIONS.json').read_text(encoding='utf-8'))['sections']}
R2 = {  # folder: (section, heading words, what the change also does)
    'start-thoughts-r2': ('H-start', 'Which thoughts to talk to', ''),
    'start-anxiety-r2': ('H-start', "If it's anxiety", ''),
    'start-stop': ('H-start', 'When to stop', ''),
    'change-empty-r2': ('H-change', 'When the words sound empty', ''),
    'change-relief-r2': ('H-change', "If the relief doesn't last", ''),
    'change-stop-r2': ('H-change', "If you'd rather stop", ''),
    'change-working': ('H-change', "If you're doing it right and it still isn't working",
                       ' It is made from the condition of the paragraph\'s first sentence, "And if you keep following the reparenting '
                       'steps correctly without getting the expected results,", which leaves the sentence, so the paragraph starts '
                       '"Consider if you have a unique case these steps don\'t match yet." (the round-1 reviewers\' point: the heading names '
                       'the reader\'s situation, and the sentence no longer says it again). Joel decides on the review sheet.'),
    'escape-trips': ('H-escape', 'Coming back from trips confused or spaced out',
                     ' It is made from the paragraph\'s first sentence, "Say you keep coming back from trips confused or spaced out.", '
                     'which leaves the paragraph, so it starts "Maybe nothing worse happens, but after several trips like that I\'d be '
                     'concerned." Joel decides on the review sheet whether his sentence becomes the heading.'),
    'escape-prone': ('H-escape', 'If you might be prone to mania or psychosis', ''),
    'hooks-change-r2': ('H-hooks', 'Can they change?', ''),
}


def context_of(r):
    lines = [r['heading']]
    for x in r['new']:
        lines.append(('#' * int(x['kind'][1]) + ' ' + x['text']) if x['kind'] != 'p' else x['text'])
    return '\n\n'.join(lines)


def under(r, heading):
    new = r['new']
    k = next(n for n, x in enumerate(new) if x['kind'] != 'p' and x['text'] == heading)
    paras = []
    for x in new[k + 1:]:
        if x['kind'] != 'p':
            break
        paras.append(x['text'])
    olds = []
    for p in paras:
        hit = [o for o in r['old'] if p[1:] in o or p in o]
        olds.append(hit[0] if hit else p)
    return paras, list(dict.fromkeys(olds))


for name, (sid, words, extra) in R2.items():
    r = SEC[sid]
    ctx = context_of(r)
    paras, olds = under(r, words)
    src = ('A new heading, proposed for Joel\'s review, to stand over these paragraphs of the section "%s" (Joel\'s idea of '
           '2026-10-25: "give each paragraph a little heading ... they can just skip the parts that don\'t apply very easily, '
           'assuming the headings are very clear"). The paragraphs as they are now:\n\n%s' % (r['heading'].lstrip('# '), '\n\n'.join(olds)))
    change = ('A case heading, "%s", over the paragraph%s that start%s "%s ...", one level below the section\'s heading. It must '
              'say what the part under it is about, in words a reader skimming for their own situation would recognize, and add '
              'no claim the paragraphs don\'t make.%s' % (words, 's' if len(paras) > 1 else '', '' if len(paras) > 1 else 's',
                                                           ' '.join(paras[0].split()[:8]), extra))
    d = HERE / name
    d.mkdir(exist_ok=True)
    assert ctx.count(words) == 1, (name, ctx.count(words))
    (d / 'DRAFT.txt').write_text(words, encoding='utf-8')
    (d / 'CONTEXT.txt').write_text(ctx + '\n', encoding='utf-8')
    (d / 'SOURCE.txt').write_text(src + '\n', encoding='utf-8')
    (d / 'CHANGE.txt').write_text(change + '\n', encoding='utf-8')
    files = ['--draft', str(d / 'DRAFT.txt'), '--context', str(d / 'CONTEXT.txt'), '--source', str(d / 'SOURCE.txt'),
             '--manifest', str(d / 'ADMISSION.json')]
    if not (d / 'ADMISSION.json').exists():
        out = subprocess.run([sys.executable, str(GATE), 'init'] + files, capture_output=True, text=True)
        if out.returncode not in (0, 2):
            sys.exit(out.stdout + out.stderr)
    m = json.loads((d / 'ADMISSION.json').read_text(encoding='utf-8'))
    print('%-18s lint %-6s %s' % (name, m['lint']['verdict_at_init'], [f['label'] for f in m['lint']['findings']]))
