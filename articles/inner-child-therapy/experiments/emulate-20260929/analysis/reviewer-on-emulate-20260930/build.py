import json, re, random, sys, pathlib
sys.path.insert(0, '/home/claude/ho/articles/inner-child-therapy/tools/reviewer')
import reviewer as R
X = pathlib.Path('/home/claude/lessons/articles/inner-child-therapy/experiments/emulate-20260929')
PAIRS = [  # (id, Claude draft, Emulate version); drafts are Pangram 100% AI, Emulate versions 100% Human
 ('A08', 'inputs/learning/A_joelfixes/A08_before.txt', 'runs/emulate/gpt_A08_api_r1.txt'),
 ('A10', 'inputs/learning/A_joelfixes/A10_before.txt', 'runs/emulate/gpt_A10_api_r1.txt'),
 ('A18', 'inputs/learning/A_joelfixes/A18_before.txt', 'runs/emulate/gpt_A18_api_r1.txt'),
 ('B07', 'inputs/learning/B_protector/B07_out_b.txt', 'runs/emulate/gpt_B07_api_r1.txt'),
 ('B09', 'inputs/learning/B_protector/B09_in_b.txt', 'runs/emulate/gpt_B09_api_r1.txt'),
 ('B10', 'inputs/learning/B_protector/B10_between_a.txt', 'runs/emulate/gpt_B10_api_r1.txt'),
 ('B12', 'inputs/learning/B_protector/B12_first_a.txt', 'runs/emulate/gpt_B12_api_r1.txt'),
 ('B15', 'inputs/learning/B_protector/B15_pick_b.txt', 'runs/emulate/gpt_B15_api_r1.txt'),
 ('B21', 'inputs/learning/B_protector/B21_r2_out3A.txt', 'runs/emulate/gpt_B21_api_r1.txt'),
 ('B23', 'inputs/learning/B_protector/B23_r2_in1A.txt', 'runs/emulate/gpt_B23_api_r1.txt'),
]
CONTROLS = {'r1': ['PASS_mpv_p2_can_show', 'PASS_mpv_p4a_x1b', 'FAIL_mpv_p3_d1', 'FAIL_mpv_p4b_y1b'],
            'r2': ['PASS_mpv_p2c', 'PASS_mpv_p1_joel_underlying_no_bread', 'FAIL_mpv_p3_d2', 'FAIL_mpv_p4b_y2f']}
def clean(t):  # Emulate's tokenizer noise only: "do n't" -> "don't", ``x'' -> "x"
    t = re.sub(r"\s+n't\b", "n't", t); t = t.replace('``', '"').replace("''", '"')
    return t.strip()
ex = R.examples(extra=False)
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
exn = norm(ex)
def item(kind, pid, path=None, cal=None):
    t = clean((X / path).read_text(encoding='utf-8')) if path else R.text(cal)
    assert norm(t)[:120] not in exn, ('already a labeled example', pid, kind)
    return t
for run, seed in (('r1', 31), ('r2', 32)):
    items = []
    for k, (pid, d, e) in enumerate(PAIRS):
        first_half = k < 5
        use_draft = first_half if run == 'r1' else not first_half
        items.append((pid + (' draft' if use_draft else ' emulate'), 'AI' if use_draft else 'HUMAN',
                      item('d' if use_draft else 'e', pid, d if use_draft else e)))
    for c in CONTROLS[run]:
        items.append(('control ' + c, R.label(c), item('c', c, cal=c)))
    random.Random(seed).shuffle(items)
    pre = 'P' if run == 'r1' else 'S'
    outv = R.read('output_verdicts.txt').replace('Q01 AI 80', pre + '01 AI 80').replace('Q02 HUMAN 70', pre + '02 HUMAN 70')
    key, parts = {}, [R.read('rubric.txt'), ex]
    parts.append('\n\nPART 2 — PASSAGES TO JUDGE (%d passages; sentences numbered)\n' % len(items))
    parts.append("These come from the same author's inner-child article project. Judge each one on its own: what would Pangram say?\n")
    for i, (name, lab, t) in enumerate(items, 1):
        pid = '%s%02d' % (pre, i)
        key[pid] = {'name': name, 'label': lab}
        parts.append('\n=== %s ===\n%s\n' % (pid, R.numbered(t)))
    parts.append(outv)
    d = pathlib.Path(run); d.mkdir(exist_ok=True)
    (d / 'prompt.txt').write_text(''.join(parts), encoding='utf-8')
    pathlib.Path('key_%s.json' % run).write_text(json.dumps(key, indent=1), encoding='utf-8')
    print(run, len(items), 'items;', len(''.join(parts).split()), 'words')
