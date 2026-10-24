#!/usr/bin/env python3
"""Turn 106, API batch 1: every paragraph of 50 words or more that my installs changed (his picks' cuts and his merge),
alone, and each smallest section around them; his Speak Toward split by E30's heading; and E5, his Inner Monologue as
he checked it beside the same text with one paragraph break (his "if it would read better with diff para break you can
try"). His own five places are his checks and aren't sent again. A heading-only change waits for round 6.
Writes TEXTS-1.json, texts/, NAMES.json, and one prediction per check in the ledger (batch t106-api-1)."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.argv = [sys.argv[0]]
import make_texts as M  # noqa: E402

ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'

P = [  # name, paragraph start, description, which pick
    ('t106_h2_nutshell', 'Reparenting means consciously evolving', 'the nutshell without "You can always slow down and look closer when it helps."', 'H2'),
    ('t106_h3_journey', 'I think most people who chase spiritual freedom', 'My Journey\'s bypassing paragraph without "It doesn\'t mean you\'re stupid or crazy."', 'H3'),
    ('t106_h12_intentional', 'Intentional, meaning you pick one of those acts', 'Not Every Hero\'s P4 without "Some of them are only one step anyway."', 'H12'),
    ('t106_h14_hook', 'Pema Chödrön calls the tightening', 'Catch the Hook\'s P2 without "You can figure that out later."', 'H14'),
    ('t106_h17_photos', 'While you look, notice what your body does', 'his photos P3 without ", which is also completely OK"', 'H17'),
    ('t106_h18_photos', "We don't need to ask it leading questions", 'his photos P4 without ", so we gotta be careful about that"', 'H18'),
    ('t106_h22_escape', 'Any of those reactions, from mania to paranoia', 'his disclaimer out and "These are just caution signs"', 'H22'),
    ('t106_h23_escape', 'Be careful what you mix, too', 'his merged acacia sentence', 'H23'),
    ('t106_h32_timing', 'Most of us need enough Nurturer and Protector first.', 'his P14 without "Timing is different for everyone, but"', 'H32'),
    ('t106_h38_schema', 'Where it really differs is spirituality.', 'the schema paragraph without the Jeffrey Young parenthetical, "(no belief in God required)" and its last line', 'H38, H39'),
    ('t106_e10_blame', 'Whichever age it picks on, saving everybody', 'his P11 without "Hindsight being 20/20 doesn\'t change that."', 'E10'),
    ('t106_e13_intention', 'Count recognition as progress', 'his One Intention\'s last paragraph without "If you made a mistake, you can see how to repair that."', 'E13'),
    ('t106_e34a_ifs', 'Is a perfect Higher Self already waiting', 'the IFS Higher Self paragraph, ending at "more foolish indifference."', 'E34'),
    ('t106_e34b_ifs', 'You can see both sides of this see-saw', 'the de Mello example as its own paragraph', 'E34'),
]
S = [  # name, heading, description, picks
    ('t106_sec_journey', 'My Journey', 'My Journey, its h1 part, with H3', 'H3'),
    ('t106_sec_lovenotyet', "If the Love Isn't Coming Yet", 'If the Love Isn\'t Coming Yet with H7 ("It\'s scaffolding.")', 'H7'),
    ('t106_sec_hero', 'Not Every Hero Wears A Cape', 'Not Every Hero Wears A Cape, P1 to P3 above the new heading', 'E9'),
    ('t106_sec_intentional', 'Make It Intentional', 'Make It Intentional (E9): P4 with H12, and d3', 'E9, H12, 102.2'),
    ('t106_sec_blame', 'Instead of Blame', 'Instead of Blame with E10', 'E10'),
    ('t106_sec_hook', 'Catch the Hook Before the Story Takes Over', 'Catch the Hook, its two paragraphs above the new heading, with H14', 'H14, E12'),
    ('t106_sec_passing', 'What to Make of a Passing Feeling', 'What to Make of a Passing Feeling (E12)', 'E12'),
    ('t106_sec_intention', 'One Intention in the Morning, One Review at Night', 'his One Intention with E13', 'E13'),
    ('t106_sec_photos', 'Use Childhood Photographs Gently', 'his Use Childhood Photographs Gently with H17 and H18', 'H17, H18'),
    ('t106_sec_escape', 'When Escape Leaves Reality Behind', 'When Escape Leaves Reality Behind above the new heading, with H22, H23 and GPT\'s 97.8', 'H22, H23, E21'),
    ('t106_sec_mantra', 'Gentle Meditation and Mantra', 'Gentle Meditation and Mantra (E21)', 'E21'),
    ('t106_sec_listen', 'Listen To Your Body, Or Else!', 'Listen To Your Body, Or Else! without the two-sentence paragraph (H26)', 'H26'),
    ('t106_sec_belong', 'You Belong Everywhere and Nowhere', 'his You Belong Everywhere and Nowhere with H31', 'H31'),
    ('t106_sec_timing', 'Timing Is Individual', 'Timing Is Individual with H32', 'H32'),
    ('t106_sec_schema', 'How This Relates to Schema Therapy', 'How This Relates to Schema Therapy with H38, H39 and the Jeffrey Young cut', 'H38, H39'),
    ('t106_sec_ifs', 'How This Relates to IFS', 'How This Relates to IFS with E34\'s break', 'E34'),
    ('t106_sec_speak', 'Speak Toward What You Are Building', 'his Speak Toward, P1 and P2 above the new heading (E30)', 'E30'),
    ('t106_sec_company', 'Ask What Kind of Company They Want', 'his Speak Toward\'s P3 under the new heading (E30)', 'E30'),
    ('t106_e5_his', 'You Don’t Need an Inner Monologue', 'his You Don\'t Need an Inner Monologue as he checked it', 'E5'),
]
texts, names, meta = {}, {}, {}
for name, start, desc, pick in P:
    texts[name], names[name], meta[name] = M.para(start), desc + ', alone', ('paragraph', pick)
for name, head, desc, pick in S:
    texts[name], names[name], meta[name] = M.h2(head), desc, ('section', pick)
his = texts['t106_e5_his']
cut = 'Then again, maybe what’s actually requiring your attention now is a knot in your stomach.'
assert his.count(' ' + cut) == 1
texts['t106_e5_split'] = his.replace(' ' + cut, '\n' + cut)
names['t106_e5_split'] = "his You Don't Need an Inner Monologue with one paragraph break, before \"Then again\" (E5)"
meta['t106_e5_split'] = ('section', 'E5')
(HERE / 'TEXTS-1.json').write_text(json.dumps(texts, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
(HERE / 'texts').mkdir(exist_ok=True)
for n, t in texts.items():
    (HERE / 'texts' / (n + '.txt')).write_text(t, encoding='utf-8')
allnames = json.loads((HERE / 'NAMES.json').read_text(encoding='utf-8'))
allnames.update(names)
(HERE / 'NAMES.json').write_text(json.dumps(allnames, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')

for n, t in texts.items():
    scope, pick = meta[n]
    if n.startswith('t106_e5'):
        call, chance = 'Human', (0.8 if n == 't106_e5_his' else 0.65)
        diag = ('his web-app check read it all dark green; the API is 4.1, so this is the baseline for E5' if n == 't106_e5_his'
                else 'the same words as his checked version, with the invitation and its alternatives in two paragraphs')
    elif scope == 'paragraph':
        call, chance = 'Human', 0.7
        diag = 'his pick %s takes out a line the readers flagged; the paragraph read Human before, in his check or ours' % pick
    else:
        call, chance = 'Human', 0.6
        diag = 'the section with his pick(s) %s; a cut or a new heading can move a window onto a neighbor (E197)' % pick
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', 't106-' + n.replace('t106_', '').replace('_', '-'), '--scope', scope, '--text', str(HERE / 'texts' / (n + '.txt')),
           '--call', call, '--chance', str(chance), '--tells', 'none named', '--human-tells', 'his words where the pick is in his text',
           '--diagnosis', diag, '--decides', 'whether %s stays in as it is' % pick, '--key', n, '--batch', 't106-api-1']
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode:
        sys.exit(out.stdout + out.stderr)
    print(out.stdout.strip().split('\n')[-1])
print(len(texts), 'texts,', sum(len(t.split()) for t in texts.values()), 'words')
