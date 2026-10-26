#!/usr/bin/env python3
"""Turn 113, gate round 3, the last: after the section cold reads (../t113-shape/COLD-READ-A1.md, -A2.md, -A3.md), every
case heading is a #### (the guide's own small-heading size), and some headings and splits changed. Each heading with new
words in a section that changed gets a new folder with its section as it reads now, so every review reads the context
Joel will see: the changed and new headings, and the unchanged ones whose section moved around them. A FAIL here is not
redrafted: its item falls back to the version already admitted, or to the paragraph's own words, or to no heading
(GATE.md). Round 1's and round 2's folders stay as the record. After this, fill_ledgers.py and make_inputs_r3.py.

  python3 make_gate_files_r3.py"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
GATE = ROOT / 'tools' / 'humanization' / 'owner_delivery_gate.py'
SEC = {r['id']: r for r in json.loads((HERE.parent / 't113-shape' / 'SECTIONS.json').read_text(encoding='utf-8'))['sections']}
CUT = ' It replaces the paragraph\'s first words, %s, which leave the paragraph, so it starts %s. Joel decides on the review sheet.'
R3 = {  # folder: (section, heading words, what the change also does)
    'guard-trust-r3': ('H-guard', 'Earning its trust, day to day', ''),
    'guard-step-back-r3': ('H-guard', "If it won't step back", ''),
    'guard-fault-r3': ('H-guard', 'If it all feels like your fault', ''),
    'start-noanswer': ('H-start', 'If no answer comes', CUT % ('"If nothing comes,"', '"That\'s fine for now."')),
    'start-thoughts-r3': ('H-start', 'Which thoughts to talk to', ''),
    'start-anxiety-r3': ('H-start', "If it's anxiety", ''),
    'start-stop-r3': ('H-start', 'When to stop', ''),
    'change-empty-r3': ('H-change', 'When your kind words sound empty', ''),
    'change-relief-r3': ('H-change', "If the relief doesn't last", ''),
    'change-stop-r3': ('H-change', "If you'd rather stop", ''),
    'escape-badtrip': ('H-escape', 'If a past trip went badly', CUT % ('the sentence "Your own drug history matters too."', '"If you go manic, psychotic ..."')),
    'escape-paranoia': ('H-escape', 'Is your paranoia a warning sign?',
                        ' Joel\'s paragraph splits before "If you can’t clearly understand what happened yourself", every sentence kept, and the heading stands over both parts.'),
    'escape-prone-r3': ('H-escape', 'If you might be prone to mania or psychosis',
                        ' The paragraph after it, "By trusted, I mean ...", now has its own heading (escape-trusted), so this one stands over one paragraph.'),
    'escape-trusted': ('H-escape', 'Who counts as trusted', ''),
    'escape-trips-r3': ('H-escape', 'If you keep coming back from trips confused or spaced out',
                        ' It is the paragraph\'s first sentence, "Say you keep coming back from trips confused or spaced out.", with "If" for "Say"; '
                        'the sentence leaves the paragraph, so it starts "Maybe nothing worse happens, but after several trips like that I\'d be '
                        'concerned." The paragraph also splits before "And don\'t suddenly stop a medication", which gets its own heading '
                        '(escape-meds), so this heading stands over its first part only. Joel decides on the review sheet.'),
    'escape-meds': ('H-escape', 'Before you quit a medication or alcohol',
                    ' It stands over the second part of a paragraph that splits before "And don\'t suddenly stop a medication"; the "And" '
                    'leaves, so it starts "Don\'t suddenly stop a medication just because you suspect it\'s involved." Joel decides on the review sheet.'),
    'therapist-licensed': ('H-therapist', 'If you want a licensed therapist', ''),
    'hooks-change-r3': ('H-hooks', 'Can they change?', ''),
    'borrow-guiding-r3': ('H-borrow', 'For guiding', ''),
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


if __name__ == '__main__':
    for name, (sid, words, extra) in R3.items():
        r = SEC[sid]
        ctx = context_of(r)
        paras, olds = under(r, words)
        src = ('A new heading, proposed for Joel\'s review, to stand over these paragraphs of the section "%s" (Joel\'s idea of '
               '2026-10-25: "give each paragraph a little heading ... they can just skip the parts that don\'t apply very easily, '
               'assuming the headings are very clear"). The paragraphs as they are now:\n\n%s' % (r['heading'].lstrip('# '), '\n\n'.join(olds)))
        change = ('A case heading, "%s", over the paragraph%s that start%s "%s ...", a small (####) heading inside the section, '
                  'the size of the guide\'s own small headings. It must say what the part under it is about, in words a reader '
                  'skimming for their own situation would recognize, and add no claim the paragraphs don\'t make.%s' %
                  (words, 's' if len(paras) > 1 else '', '' if len(paras) > 1 else 's', ' '.join(paras[0].split()[:8]), extra))
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
        print('%-20s lint %-6s %s' % (name, m['lint']['verdict_at_init'], [f['label'] for f in m['lint']['findings']]))
