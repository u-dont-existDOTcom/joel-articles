"""Section 13 draft v10 (2026-10-15): v9 with round r7's findings fixed (review-r7/DISPOSITIONS-r7.md), and H1-P2, which
read AI in batch 289g, rebuilt from Emulate round e (emu-e/out/h01-emuA.txt, second paragraph) with the published meaning
put back word by word. Writes v10.md and v10-fixes.json. Run from this folder: python3 make_v10.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


v9 = blocks((HERE / 'v9.md').read_text(encoding='utf-8'))
IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
assert len(IDS) == len(v9) and all((i is None) == b.startswith('#') for i, b in zip(IDS, v9))
text = {i: b for i, b in zip(IDS, v9) if i}

# H1-P2 from round e: Emulate's second paragraph, as returned, then the word fixes below
emu = (HERE / 'emu-e' / 'out' / 'h01-emuA.txt').read_text(encoding='utf-8').split('\n\n')[1]
text['H1-P2'] = emu
FIX = {
 'H1-P2': [('Third, don\'t even think', 'Don\'t even think', 'the numbering ("First", "Second", "Third") was Emulate\'s'),
           ('or by saying "Let\'s all just agree to leave each other alone".',
            'or by calling a truce nobody believes, like "Let\'s all just agree to leave each other alone".',
            'the published "a truce nobody believes"'),
           ('But really, truly dealt with it. Do the real relational pl/ork', 'But really, truly dealt with it. That\'s the real relational pl/ork',
            'not a second imperative: the linter counts two in a paragraph as instructions (E23), and with the trial-run paragraph that failed it'),
           ('allowing whatever is there (jealousy, humiliation, fear, past material, whatever) to come up,',
            'finding whatever is there (jealousy, humiliation, fear, old material, whatever),',
            'the published "Find the jealousy, humiliation, fear, or old material involved"'),
           ('until the emotional pressure is such that an agreement to do something differently actually means something.',
            'until the emotional pressure has changed enough that an agreement actually means something.',
            'the published "has changed enough"; "to do something differently" was Emulate\'s')],
 'H2-P3': [('Date and/or be in a relationship with whomever they choose?', 'Date and/or be in a relationship?',
            'traces T2 of r6 and T1 of r7: "whomever they choose" set a standard the published doesn\'t')],
 'H2-P4': [('(not just how they talk about functioning)', '(not just how they talk about it in public)',
            'trace T2 of r7: the published "public language"'),
           ('Who can block decisions, and how?', 'Who can block decisions?', 'traces T2 of r5 and r7: "and how?" added')],
 'H3-P1': [('People tend to not take this into account enough, but it matters so much!', 'It matters so much!',
            'traces T2 of r5 and r7: a new claim about people; the reaction stays as the break')],
 'H3-P3': [("Transfers of major resources (land, equipment, stores, outside cash, etc.) need to be recorded",
            "Large transfers (land, equipment, stores or outside cash) need to be recorded",
            'trace T3 of r7: large transfers, a closed list'),
           ('provide people with resources when they leave (cash if it uses money, plus tools, transportation, temporary housing, '
            'stored goods, the right to keep using something, etc).',
            'provide people with resources when they leave, in whatever form makes sense (cash if it uses money, or tools, '
            'transportation, temporary housing, stored goods, the right to keep using something).',
            'trace T3 of r7: "in whatever unit makes sense", alternatives, not a bundle'),
           ('can only be exercised if there is money around.', 'can only be exercised if the community has spare money.',
            'trace T3 of r7: the community\'s spare money')],
 'H4-P7': [('that has serious consequences, for example with kids,', 'that has serious consequences, involving kids,',
            'trace T4 of r7: the published list is closed'),
           ('ensure there’s always some way for someone to appeal that decision to a separate authority if needed.',
            'ensure there’s always some way to appeal decisions about these roles to a separate authority if needed.',
            'both cold reads of r7: which decision'),],
 'H4-P8': [("Sorry, hanging out doesn't count!", "(Sorry, hanging out doesn't count!)",
            'march: no break in reading a; asides in parentheses were breaks in every reading of r6 and r7')],
 'H5-P1': [('Even in a safe community it’s ok to kick people out if they’re a serious or general danger. If someone '
            'won’t respect essential boundaries, and won’t stop, and/or is just impossible to live with, it can be okay to '
            'eject them.',
            'Even a safe community can’t promise to keep everyone. If someone is a serious or general danger, won’t '
            'respect essential boundaries and won’t stop, or is just impossible to live with, ejecting them can be the '
            'right call.',
            'both stance checks of r7, from opposite sides; the published "cannot promise to keep everyone" and "can be the '
            'right answer"')],
 'H5-P2': [('What constitutes a reason for immediate protective action', 'What conduct constitutes a reason for immediate '
            'protective action', 'trace T5 and the published-essay stance check of r7: conduct')],
 'H5-P3': [("But autonomy doesn't mean that these institutions can violate non-waivable individual rights, or that outside "
            "jurisdiction stops applying to them.",
            "But autonomy doesn't mean that anyone can erase non-waivable individual rights, or that outside jurisdiction "
            "disappears.",
            'trace T6 and both stance checks of r7: the limit is on autonomy, the community\'s own included')],
 'H5-P4': [('it does not replace the need for evidence and safeguarding and, if necessary, a ruling.',
            'it does not replace the need for evidence, safeguarding or a ruling.',
            'traces T6 of r6 and r7: the ruling isn\'t conditional'),
           ('once consent is gone.', 'once someone no longer consents to the shared life.',
            'both cold reads of r7: whose consent, to what; "the shared life" is the section\'s "ordinary shared life"')],
}
log = []
for pid, fixes in FIX.items():
    t = text[pid]
    for old, new, why in fixes:
        assert t.count(old) == 1, (pid, old)
        t = t.replace(old, new)
        log.append({'id': pid, 'old': old, 'new': new, 'why': why})
    text[pid] = t
out = [b if i is None else text[i] for i, b in zip(IDS, v9)]
(HERE / 'v10.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v10-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('v10.md:', len([b for b in out if not b.startswith('#')]), 'paragraphs;', len(log), 'fixes; changed:', sorted(FIX))
print(text['H1-P2'])
