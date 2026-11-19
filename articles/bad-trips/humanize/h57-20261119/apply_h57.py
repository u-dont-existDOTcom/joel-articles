#!/usr/bin/env python3
"""apply_h57.py - turn 49's tries into the guide, each change of mine only once its check by itself read Human High in
every window (tools/humanization/apply_gate.py; RESULTS.md has the links). The edits are build_tries.py's, so the words
that go in are the words that were checked.

- B203, DMSO's side effects (b06-dmso-side, Human High 179): "Sensitivity varies." cut (every read: it gives the reader
  nothing to do); "lighter" said as the study has it ("less deep"); "crenate" explained ("shrivel"); the two "it"s of the
  itch line named; the mouth line said as what to do ("so wet your mouth first").
- B214, niacin's side effects (b07-niacin-side, Human High 57): "real risk" said as the risk it is ("a real risk of liver
  damage"), "sensitive physiology", which no reader can check, out; "This" named ("The flush").
- B255, Get One Human Anchor (b10-anchor-lead, Human High 70): "them" said as the anchor, "safe" said as "from getting
  hurt", "do it" said as "get that help".
- B312, the Grounding Menu's ordinary-world list (b12-move-list, Human High 83): "The same goes" said as what to skip
  ("Skip exercise too"), "after a stimulant" as having taken one, "with any medical concern" as theirs.
- B433, the Appendix's list (b19-appendix, Human High 52): "U.C." spelt UC, which Pangram read as a sentence of its own.
- B215, niacin's other forms (c08-niacin-forms, with B214 before it, Human High 97): less reliable "than niacin";
  niacinamide's "sometimes ... and sometimes" built two ways, "their state" said as "the state the person is in"; the
  non-flush form named the way a label has it ("no-flush", inositol hexanicotinate).
- B344, Shadow Work's opening (c13-shadow-def, Human High 74): "is central" said as "is central to shadow work"; the
  link's stray space put back outside it.

Each edit's old words, so it can be undone, are in build_tries.py's TRIES (block, old, new).

  python3 articles/bad-trips/humanize/h57-20261119/apply_h57.py      (from the repo root)
"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
REPO = ART.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
LEDGER = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
sys.path.insert(0, str(HERE))
import build_tries as BT  # noqa: E402

PASSED = ['b06-dmso-side', 'b07-niacin-side', 'b10-anchor-lead', 'b12-move-list', 'b19-appendix',
          'c08-niacin-forms', 'c13-shadow-def']


def gate(key):
    test = HERE / ('TEST-%s.txt' % key)
    r = subprocess.run([sys.executable, 'tools/humanization/apply_gate.py', LEDGER, '--file', str(test.relative_to(REPO))],
                       cwd=REPO, capture_output=True, text=True)
    if r.returncode:
        sys.exit('refused by apply_gate.py for %s:\n%s' % (key, (r.stdout + r.stderr)[-800:]))


def main():
    B = json.loads(BJ.read_text(encoding='utf-8'))
    assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
    ids = [b['id'] for b in B]
    for key in PASSED:
        gate(key)
        for blk, old, new in (BT.TRIES.get(key) or BT.TRIES_C[key])[1]:
            md = B[ids.index(blk)]['md']
            if old not in md:
                continue                                   # already in
            assert md.count(old) == 1, (key, blk, old)
            B[ids.index(blk)]['md'] = md.replace(old, new)
    MD.write_text('\n\n'.join(b['md'] for b in B) + '\n', encoding='utf-8')
    BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    # two records that check the anchor paragraph's backup line word for word (turn 34 updated them the same way when
    # anchor-a1 changed it): the line still names the two people once, bold as before; only "do it" is now "get that help"
    OE = ART / 'OWNER-EDITS.json'
    oe = json.loads(OE.read_text(encoding='utf-8'))
    OLD_L = ("bring in **one more calm adult or a crisis professional** to back them up, and do it right away if there's any "
             "risk of violence or self-harm.")
    NEW_L = ("bring in **one more calm adult or a crisis professional** to back them up, and get that help right away if "
             "there's any risk of violence or self-harm.")
    NOTE = (' | the sentence it checks changed in turn 49\'s fix b10-anchor-lead (2026-11-19; humanize/h57-20261119/'
            'apply_h57.py; https://www.pangram.com/history/36cf33c5-55a8-4a4f-942f-4f9bea7d145d, Human High 70): "them" '
            'said as the anchor, "safe" as "from getting hurt", "do it" as "get that help"; the two people it names still '
            'the one place backup is said, bold as before')
    for e in oe['entries']:
        if e['id'] in ('t19-anchor-committee-cut', 't19-recruit-once'):
            m = e.get('must_contain_exact') or []
            if OLD_L in m:
                e['must_contain_exact'] = [NEW_L if x == OLD_L else x for x in m]
                if NOTE not in e['what']:
                    e['what'] += NOTE
    OE.write_text(json.dumps(oe, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('in:', ', '.join(PASSED))


if __name__ == '__main__':
    main()
