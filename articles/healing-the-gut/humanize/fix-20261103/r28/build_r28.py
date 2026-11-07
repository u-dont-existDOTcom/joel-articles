#!/usr/bin/env python3
"""r28 = r27 with Phase 4's one numbered step joined to the paragraph its "So" points to.

The organ step by itself read AI Generated, 100%, in three wordings (#196, #199, #203), two of them after the tell panel,
while every check that read it after Phase 4's first paragraph read it High (#194: one 143-word window with that
paragraph; #195, the whole protocol section). By itself the step has no reason in it: why the reader checks their organs
is the last sentence of the paragraph before it ("The problem is likely an organ that isn't working right, ..."), which
its "So" points to; the second panel's whole-paragraph note (a summarizer relaying claims, nothing at stake) is read as
that sense problem first (E360). And Phase 4's numbered list has only this one item. So the step goes into that
paragraph, right after the sentence it answers, and its "(Brown)" goes, since the paragraph's first sentence names Brown
as the phase's only source. The step's words are r27's otherwise. Writes r28.md and CHANGES.json."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
md = (HERE.parent / 'r27' / 'r27.md').read_text(encoding='utf-8')
lead = ('(those two are Phase 6, below).')
step_old = ('\n\n  1. So check your organs (Brown). Do your stools look oily or greasy?')
assert md.count(lead + step_old) == 1, 'the step must follow the lead paragraph directly'
md = md.replace(lead + step_old, lead + ' So check your organs. Do your stools look oily or greasy?')
CHANGES = [{'old': lead + step_old.replace('\n', '\\n'), 'new': lead + ' So check your organs. Do your stools look oily or greasy?',
            'kind': 'structure',
            'why': 'the organ step by itself read AI in three wordings (#196, #199, #203) and High with the paragraph before '
                   'it (#194, #195): its reason is that paragraph\'s last sentence, which its "So" points to, and the '
                   'numbered list had only this item; it joins that paragraph, and "(Brown)" goes since the paragraph '
                   'names Brown as the phase\'s only source'}]
(HERE / 'r28.md').write_text(md, encoding='utf-8')
(HERE / 'CHANGES.json').write_text(json.dumps(CHANGES, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(CHANGES), 'change;', len(md.split()), 'words')
