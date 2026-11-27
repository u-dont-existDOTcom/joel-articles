#!/usr/bin/env python3
"""build_h81.py - turn 73's texts for Pangram: his round-62 answers (review/r62/ANSWERS-R62-20261127-1716.json) carried into
Beach Morning Glory's handling line (B174) and amounts paragraph (B173), each as steps from the version that read High
(lesson neuro-2026-11-27a: his answer goes in one piece a check, in the paragraph's own lineage). The guide's blocks are
read from the guide as it stands; only the words I change are written here.

  python3 build_h81.py            the try texts (TEST-KEY.txt)
  python3 build_h81.py section    the section as the guide has it now, for its check (TEST-sec2-bmg.txt)

The whole section as first drafted with both answers in, which the three fresh reads saw, is in
reads/prompt-*-final-bmg-sec.txt; the steps below are what those reads changed (his fixes: the draft packed the juice, the
skin and the absorbing into one sentence and said "absorbs" twice; it packed the nibble, both amounts and the effect into
one, and "give more" didn't say more than what).

Steps are kept small enough for the near-miss rule (pangram_ledger.py, lesson bad-trips-2026-11-19b): each lineage's best
try read Human High in every window (B171 with B174, bb2893ad; B173 by itself, 6bc70ed9), so a step changes at most 20% of
its words until two such steps have been checked.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
B = {x['id']: x['md'] for x in json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))}
# the blocks as turn 73 found them (commit 3066fd8d0, the merge at its start), so the steps stay what they were once applied
import subprocess  # noqa: E402
T0 = {x['id']: x['md'] for x in json.loads(subprocess.run(
    ['git', 'show', '3066fd8d0:articles/bad-trips/GUIDE-SO-FAR-blocks.json'], cwd=ART, capture_output=True, text=True,
    check=True).stdout)}


def swap(text, old, new):
    assert text.count(old) == 1, (old, text)
    return text.replace(old, new)


# LEAF-JUICE, his comment: "touching the juice is relaxing, especially on sensitive skin, it absorbs almost as well as
# eating it. can put it under armpits for example to absorb well". Step 1, his word for what the juice does; step 2, that
# it works through the skin almost as well as eating it, in a sentence of its own; step 3, his armpits, "for example" kept.
B174_S1 = swap(T0['B174'], 'even picking one can affect me if', 'even picking one can relax me if')
B174_S2 = swap(B174_S1, 'so I keep my skin away from the broken end.',
               'so I keep my skin away from the broken end. Its juice works through the skin almost as well as eating it does.')
# step 2 read High but for its own sentence, Medium 13 in a window of its own (5884722d); "eating it" could be eating the
# juice or the leaf, so the next try says which (the near-miss rule: one or two words a reader could take two ways)
B174_S2B = swap(B174_S2, 'as well as eating it does.', 'as well as eating the leaf does.')
B174_S3 = swap(B174_S2B, 'almost as well as eating the leaf does.',
               'almost as well as eating the leaf does, so to give it on purpose, you can put the juice under the armpits, '
               'for example.')

# NIBBLE-SIZE, his comment: "i'd try 10mg at a time for nausea of the extract paste, or 200mg leaf at a time (more if they
# don't mind reducing trip intensity)". Step 1, his two amounts in a sentence of their own after the nibble, his verb
# ("try"); step 2, his "more", saying more than what.
B173_S1 = swap(T0['B173'], 'even improve the trip without ending it. But',
               'even improve the trip without ending it. For nausea I\'d try 200mg of leaf at a time, or 10mg of the extract '
               'paste. But')
B173_S2 = swap(B173_S1, 'or 10mg of the extract paste. But',
               'or 10mg of the extract paste. I\'d give more than that only if the person doesn\'t mind their trip getting '
               'less intense. But')
# both steps read High but for the nibble sentence, Medium 16 in a window of its own (ddea8d92, 10d2a2a5), as it was in try
# 1; it is built like the sentence before it ("A whole leaf can easily end", "A tiny nibble can sometimes smooth"; his fixes,
# way 2), so the next try builds it differently, one word: "though" after its subject
B173_S3 = swap(B173_S2, 'A tiny nibble can sometimes smooth', 'A tiny nibble, though, can sometimes smooth')
# "though" joined the two into one window that read Low 37 (b771d740), so it goes; the fresh his-fixes read of the draft
# said the whole-leaf sentence "gives no amount" and his way "would say how the leaf is taken": one word, "Eating", which
# also builds it differently from the nibble sentence after it
B173_S4 = swap(B173_S2, 'A whole leaf can easily end', 'Eating a whole leaf can easily end')

TEXTS = {
    'c2-bmg-p1p3': T0['B171'] + '\n\n' + B174_S1,
    'c3-bmg-p1p3': T0['B171'] + '\n\n' + B174_S2,
    'c4-bmg-p1p3': T0['B171'] + '\n\n' + B174_S2B,
    'c5-bmg-p1p3': T0['B171'] + '\n\n' + B174_S3,
    'a3-bmg-p2': B173_S1,
    'a4-bmg-p2': B173_S2,
    'a5-bmg-p2': B173_S3,
    'a6-bmg-p2': B173_S4,
}

if __name__ == '__main__':
    if sys.argv[1:] == ['section']:
        ids = ['B171', 'B174', 'B173', 'B176', 'B178']
        t = '\n\n'.join(B[k] for k in ids)
        (HERE / 'TEST-sec2-bmg.txt').write_text(t.strip() + '\n', encoding='utf-8')
        print('sec2-bmg', len(t.split()), 'words')
        sys.exit(0)
    for k, t in TEXTS.items():
        (HERE / ('TEST-%s.txt' % k)).write_text(t.strip() + '\n', encoding='utf-8')
        print(k, len(t.split()), 'words')
