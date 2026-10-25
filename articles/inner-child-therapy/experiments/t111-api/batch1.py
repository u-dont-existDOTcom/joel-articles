#!/usr/bin/env python3
"""Turn 111, API batch 1, predictions first: every paragraph of 50 words or more that his answers of 2026-10-25 20:08 UTC
changed (experiments/t111-installs/apply_t111.py), alone. Hear the Guard First is the text checked as t110_sec_guard_b, so
it isn't checked again; the sections come in round 7, the whole-article check.

  python3 batch1.py [--dry]"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_texts as M  # noqa: E402

ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
BATCH = 't111-api-1'
I = M.Texts(M.ART.read_text(encoding='utf-8'))
texts, names, preds = {}, {}, {}


def add(name, start, desc, chance, diagnosis, human='his words'):
    texts[name], names[name] = I.para(start), desc
    preds[name] = ('t111-' + name.split('_', 2)[2], 'paragraph', chance, diagnosis, human)


CUT = 'try 1: his approved cut of %s; the rest of the paragraph is as it read before'
add('t111_c3_illwill', "In one of the Buddha's own accounts", 'Ill Will and Loving-Kindness P1 after his approved cut (C3), alone', 0.75,
    CUT % '"So it\'s worth noticing what it\'s doing to you." (round 6 read it with the question as Human, Low)', human='the Human Torch; his question')
add('t111_c4_borrowlove', 'Or put somebody you care about', 'Borrow Love P3 after his approved cut (C4), alone', 0.75,
    CUT % 'the life\'s-journey line', human='"a cheap trick for becoming the outsider to your own mess"; Solomon')
add('t111_c5_rogers', 'You can see the same move', 'Love Doesn\'t Have to Wait P8 after his approved cut (C5), alone', 0.75,
    CUT % 'the moral after the Mr. Rogers scene; it ends on the film\'s line', human='the film\'s own lines')
add('t111_c6_hook', 'When you catch it, look around', 'Catch the Hook P2 after his approved cut (C6), alone', 0.75,
    CUT % '"Sometimes human beings need to be being, not always doing. 🙃"', human='"Oh! I\'m hooked again!"; "little boo"')
add('t111_c8_belonging', 'Part of building who you are', 'Untangling the Belonging Bargains P1 after his approved cut (C8), alone', 0.8,
    CUT % '", which is ordinary" (round 6\'s w068 was Human, Medium, on it)', human='"Boys don\'t cry"; the roles')
add('t111_c9_beginner', 'Give a new interest enough tries', 'Let the Child Be Bad at Things P3 after his approved cut (C9), alone', 0.65,
    CUT % 'the "Either way, that\'s pl/ork" summary (round 2 read the stretch AI, Low)', human='"Sorry, I\'m new."')
add('t111_c10_people', 'Reparenting is usually talked about', 'Borrowed Adulthood in Relationship P1 with his added sentence (C10), alone', 0.7,
    'try 1: his new sentence after the blessing line he kept ("If it\'s more distributed ... monumental.")', human='his new sentence')
add('t111_c10_calendar', 'Over time, reparenting can help you', 'Borrowed Adulthood in Relationship P2 after his cut of its first sentence, alone', 0.75,
    'try 1: his own P2 (question 33, A) without its first sentence, his cut', human='"even that calendar bit"; "inner & outer reliance"')
add('t111_c11_forgive', 'For many people, healing does get around', 'How to Forgive Without Forgetting P1 after his approved cut (C11), alone', 0.75,
    CUT % '"(nobody gets a gold star for forgiving fastest)"', human='"an enlightened-looking act"')
add('t111_c12_missing', 'All of this happens in you', 'Missing Someone P2 after his approved cut (C12), alone', 0.75,
    CUT % '"(nobody\'s checking their inbox)"', human='"I miss you, and I care."')
add('t111_p2_trackrecord', 'How do you check that?', 'Don\'t Give the Inner Adult Away P2 with the approved wording (P2), alone', 0.65,
    'try 1: GPT\'s wording with his "I\'d" kept, admitted by the owner-delivery gate; the questions after it unchanged',
    human='"Do they respect a no, or keep pushing on it"')
add('t111_p5_son', 'A real-life child of yours', 'Remind Yourself P2 with his son line (P5), alone', 0.7,
    'try 1: his 2026-10-02 answer as an article sentence, admitted by the gate; the paragraph was his and read Human',
    human='"My son did that for me"')
add('t111_jl1_steadier', 'On a steadier day', 'Just Like Me P1 after his cut of the stray line, alone', 0.7,
    'try 1: his cut of "Some of them make it worse ... Just like you, sometimes. 😅"; the rest as it read Human (round t72b)',
    human='"the theory that you\'re the defective one gets kind of hard to keep up"')
add('t111_q1_truce', 'Taking the hostility out', 'If the Love Isn\'t Coming Yet P3 with his sentence for Q1, alone', 0.7,
    'try 1: his "Once a truce is made, we can begin to let down our defenses." for "What people most often say helped ..."',
    human='his sentence; "rigid security guard"')

(HERE / 'TEXTS-1.json').write_text(json.dumps(texts, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
(HERE / 'texts').mkdir(exist_ok=True)
for n, x in texts.items():
    (HERE / 'texts' / (n + '.txt')).write_text(x, encoding='utf-8')
(HERE / 'NAMES.json').write_text(json.dumps(names, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
for n, x in texts.items():
    print('%-22s %4d words | %s' % (n, len(x.split()), x[:70]))
if '--dry' in sys.argv:
    sys.exit(0)
for n, (lin, scope, chance, diag, human) in preds.items():
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER), '--lineage', lin, '--scope', scope,
           '--text', str(HERE / 'texts' / (n + '.txt')), '--call', 'Human', '--chance', str(chance), '--tells', 'none named',
           '--human-tells', human, '--diagnosis', diag, '--decides', 'whether his turn-111 change stays as installed', '--key', n,
           '--batch', BATCH]
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode:
        sys.exit(out.stdout + out.stderr)
    print(out.stdout.strip().split('\n')[-1])
