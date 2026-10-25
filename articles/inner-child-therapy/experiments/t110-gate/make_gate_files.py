#!/usr/bin/env python3
"""Turn 110: the owner-delivery gate's files (docs/HUMANIZATION-OWNER-DELIVERY-GATE.md, main's of 2026-10-25 17:44 UTC) for
the new model-written words on the review sheet, each the literal sentence that would be new in the article:

  S1-nurturer    "I'd still keep the Nurturer voice."                     (S1, P8's fix of "I'd still keep it the same.")
  S1-watch       the move-out sentence split in two, with "call it all off" (S1, GPT's readability fix and the cold read's)
  S1-protective  "Blaming yourself can be doing a protective job, too."    (S1, for "a job like that")
  P2             GPT's wording with "I'd" kept: "I'd keep what you feel around them in mind, and look at their track record too."
  P5             "My son did that for me, and I think that's very common for parents." (his 2026-10-02 answer as an article sentence)
  P6             "I'd leave out forgiving them and picturing their childhood here."

Each gets DRAFT.txt (the exact sentence, no newline added, as the sheet shows it), CONTEXT.txt (its section as it would
read, holding the draft once) and SOURCE.txt (the sentence it replaces, and for P5 his answer). What is outside the gate,
with why, is in GATE.md.

  python3 make_gate_files.py"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

review = json.loads((HERE.parent / 't110-review' / 'REVIEW.json').read_text(encoding='utf-8'))
md = (ROOT / review['article']['file']).read_text(encoding='utf-8')
BL = sr.blocks(md)
SUG = {s['id']: s for s in review['suggestions']}


def section_of(i):
    h = max(b['i'] for b in BL[:i + 1] if b['level'])
    paras = []
    for b in BL[h + 1:]:
        if b['level']:
            break
        paras.append(b['i'])
    return h, paras


def write(name, draft, context, source):
    d = HERE / name
    d.mkdir(exist_ok=True)
    assert context.count(draft) == 1, name
    (d / 'DRAFT.txt').write_text(draft, encoding='utf-8')
    (d / 'CONTEXT.txt').write_text(context + '\n', encoding='utf-8')
    (d / 'SOURCE.txt').write_text(source + '\n', encoding='utf-8')
    print('%-14s %3d words | %s' % (name, len(draft.split()), draft[:70]))


s1 = SUG['S1']
blocks = sorted({sp['block'] for sp in s1['spans']})
h, paras = section_of(blocks[0])
s1_context = (BL[h - 1]['text'] + '\n\n' + BL[h]['text'] + '\n\n' + '\n\n'.join(r['text'] for r in s1['reads'])
              + '\n\n' + BL[paras[-1] + 1]['text'])
cur = '\n\n'.join(BL[i]['text'] for i in paras)
write('S1-nurturer', "I'd still keep the Nurturer voice.", s1_context, "I'd still keep it the same.")
write('S1-watch', "It can keep watch while you take one small step toward your little one. I think watching is what it wants anyway, "
      "to find out if there's a grown-up here now who could call it all off if things got to be too much.", s1_context,
      "It can keep watch while you take one small step toward your little one, and I think watching is what it wants anyway, "
      "to find out if there's a grown-up here now who could call it off if things got to be too much.")
write('S1-protective', 'Blaming yourself can be doing a protective job, too.', s1_context,
      'Blaming yourself can be doing a job like that, too.')
assert all(x in cur for x in ("I'd still keep it the same.", 'Blaming yourself can be doing a job like that, too.'))

for sid, draft, old, extra in (
        ('P2', "I'd keep what you feel around them in mind, and look at their track record too.",
         "I'd keep whatever you feel around them, and look at their track record.", ''),
        ('P5', "My son did that for me, and I think that's very common for parents.",
         'A real-life child of yours, or a calm pet, can also act as a companion that brings out the relationship with your own inner child.',
         '\n\nHis answer of 2026-10-02 00:16 UTC: "I actually used my son (i shouldn\'t say "used") to reconnect with my inner child, '
         'and I think that\'s very common for parents."'),
        ('P6', "I'd leave out forgiving them and picturing their childhood here.",
         "I'd leave out forgiving them and picturing their childhood.", '')):
    e = SUG[sid]['edits'][0]
    hh, ps = section_of(e['block'])
    context = '\n\n'.join([BL[hh]['text']] + [e['after'] if i == e['block'] else BL[i]['text'] for i in ps])
    assert old in e['before'] and draft in e['after'], sid
    write(sid, draft, context, old + extra)
