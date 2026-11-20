#!/usr/bin/env python3
"""apply_c.py - his answers to the contradictions check's four questions into the guide (chat, 2026-11-20 22:40 UTC:
"C1 a C2a C3 a C4 a"), and the Systema video he sent in the same message ("best systema breathing vid i have seen so far:
https://www.youtube.com/shorts/Nar2-nvomAk").

- C1 (a): step 3 of the serotonin steps (B136) says it his way: "Call emergency help and arrange transport." ("for moderate
  or severe signs" out), so it agrees with his "So if you see any of these patterns, call medics." Words out, none added.
- C2 (a): No Rash Actions' lock line (B317), two clocks, each where it belongs: his list after it already says what waits
  until they've slept and eaten, so the line says the longer one, "Put yourself on an action lock: nothing life-changing
  for 24–72 hours." (his answer's words, less the clause his list says; the read against his fixes marked the two limits
  packed in one line, and his list restating the first). Goes in only when its pair check reads Human High in every
  window (apply_gate.py).
- C3 (a): the ozone story (B197): "The mistake suggested that ..." for "showed me", so it agrees with his DMSO lines ("I
  don't yet know why").
- C4 (a): My Brain Feels Damaged's first step (B144): "Smell humic acid; if that doesn't help, take a 5mg lick of it."
  ("first" out, so humic acid can't read as coming before DMSO; the smell still comes before the lick, his round-6 rule,
  "smell it first for sure, that's like an allergy test").
- SYSTEMA: "a video" in his Systema breathing line (B302) links the video he sent ("Linear & Circular Breathing", Systema
  Vasiliev); a link only, the words as he wrote them.

  python3 articles/bad-trips/humanize/h62-20261120/apply_c.py C1 C3 C4 SYSTEMA [C2]      (from the repo root)
"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
REPO = ART.parents[1]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import apply_gate  # noqa: E402

BJ, MD = ART / 'GUIDE-SO-FAR-blocks.json', ART / 'GUIDE-SO-FAR.md'
LEDGER = ART / 'humanize' / 'pangram-ledger.jsonl'
VIDEO = 'https://www.youtube.com/shorts/Nar2-nvomAk'
ANSWER = '2026-11-20 22:40 UTC: "C1 a C2a C3 a C4 a"'
BY = 'humanize/h62-20261120/apply_c.py'

CHANGES = {
    'C1': ('B136', '3. **Call emergency help and arrange transport for moderate or severe signs.**',
           '3. **Call emergency help and arrange transport.**'),
    'C2': ('B317', '**Put yourself on a 24–72 hour action lock.**',
           '**Put yourself on an action lock: nothing life-changing for 24–72 hours.**'),
    'C3': ('B197', 'The mistake showed me that DMSO and aged ozonated-charcoal water address different kinds of overload.',
           'The mistake suggested that DMSO and aged ozonated-charcoal water address different kinds of overload.'),
    'C4': ('B144', "1. **DMSO immediately. Smell humic acid first; if that doesn't help, take a 5mg lick of it.**",
           "1. **DMSO immediately. Smell humic acid; if that doesn't help, take a 5mg lick of it.**"),
    'SYSTEMA': ('B302', 'It helps to watch a video on how to do it prior though',
                'It helps to watch [a video](%s) on how to do it prior though' % VIDEO),
}

EDITS = {
    'C1': {'id': 'c1-ss-call-any', 'status': 'applied',
           'what': ('C1 (a), the contradictions check\'s item 6: the serotonin steps\' step 3 says his rule, "Call emergency '
                    'help and arrange transport." ("for moderate or severe signs" out), agreeing with his "So if you see any '
                    'of these patterns, call medics."'),
           'joel': ANSWER, 'applied_by': BY,
           'must_contain_exact': ['3. **Call emergency help and arrange transport.** Don\'t drive yourself.'],
           'must_not_contain': ['arrange transport for moderate or severe signs']},
    'C2': {'id': 'c2-lock-two-clocks', 'status': 'applied',
           'what': ('C2 (a), item 12: No Rash Actions\' lock line gives the longer clock, his list after it the shorter '
                    '("Until you have slept and eaten"); the night\'s lines elsewhere keep tomorrow or morning'),
           'joel': ANSWER, 'applied_by': BY,
           'must_contain_exact': ['**Put yourself on an action lock: nothing life-changing for 24–72 hours.**'],
           'must_not_contain': ['Put yourself on a 24–72 hour action lock.']},
    'C3': {'id': 'c3-ozone-suggested', 'status': 'applied',
           'what': ('C3 (a), item 9: the ozone story says the mistake "suggested" what DMSO and the charcoal water each '
                    'address, agreeing with his DMSO lines ("I don\'t yet know why")'),
           'joel': ANSWER, 'applied_by': BY,
           'must_contain_exact': ['The mistake suggested that DMSO and aged ozonated-charcoal water address different kinds '
                                  'of overload.'],
           'must_not_contain': ['The mistake showed me']},
    'C4': {'id': 'c4-humic-no-first', 'status': 'applied',
           'what': ('C4 (a), item 4: "first" out of My Brain Feels Damaged\'s first step, so humic acid can\'t read as coming '
                    'before DMSO; the smell still comes before the lick ("if that doesn\'t help")'),
           'joel': ANSWER, 'applied_by': BY,
           'must_contain_exact': ["Smell humic acid; if that doesn't help, take a 5mg lick of it."],
           'must_not_contain': ['Smell humic acid first', 'Smell humic acid, take a 5mg lick of it.']},
    'SYSTEMA': {'id': 'systema-video', 'status': 'applied',
                'what': ('his Systema breathing line links the video he sent, on "a video" (the words as he wrote them)'),
                'joel': ('2026-11-20 22:40 UTC: "best systema breathing vid i have seen so far: '
                         'https://www.youtube.com/shorts/Nar2-nvomAk"'),
                'applied_by': BY, 'must_contain_exact': ['[a video](%s)' % VIDEO]},
}
SUPERSEDES = {'C2': ('r16-nra-lock', '2026-11-20: his C2 answer a (c2-lock-two-clocks)'),
              'C4': ('q1-smell-first', '2026-11-20: his C4 answer a (c4-humic-no-first); the smell still comes before '
                                       'the lick, as his "smell it first for sure" asked')}


def main(keys):
    B = json.loads(BJ.read_text(encoding='utf-8'))
    assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
    by = {b['id']: b for b in B}
    if 'C2' in keys:  # a paragraph of mine: its check by itself (the pair) must read Human High in every window
        apply_gate.require(str(LEDGER), [CHANGES['C2'][2]])
    done = []
    for k in keys:
        bid, old, new = CHANGES[k]
        md = by[bid]['md']
        if new in md and old not in md:
            continue
        assert md.count(old) == 1, (k, bid, md[:120])
        by[bid]['md'] = md.replace(old, new)
        done.append(k)
    MD.write_text('\n\n'.join(b['md'] for b in B) + '\n', encoding='utf-8')
    BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

    OE = ART / 'OWNER-EDITS.json'
    oe = json.loads(OE.read_text(encoding='utf-8'))
    have = {e['id']: e for e in oe['entries']}
    for k in keys:
        if EDITS[k]['id'] not in have:
            oe['entries'].append(EDITS[k])
        if k in SUPERSEDES:
            old_id, why = SUPERSEDES[k]
            e = have[old_id]
            e['status'] = 'superseded'
            if why not in e.setdefault('superseded', []):
                e['superseded'].append(why)
    OE.write_text(json.dumps(oe, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied', done, '|', len(MD.read_text(encoding='utf-8').split()), 'words')


if __name__ == '__main__':
    ks = sys.argv[1:]
    assert ks and all(k in CHANGES for k in ks), 'give some of %s' % ', '.join(CHANGES)
    main(ks)
