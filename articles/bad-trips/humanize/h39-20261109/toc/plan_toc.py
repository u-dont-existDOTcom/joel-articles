#!/usr/bin/env python3
"""plan_toc.py - the bad trips guide's table of contents as option A or B of round 30's TOC card would make it.

His answer on round 28's helper card (2026-11-09 17:22 UTC): "maybe it would hlep if you look only at the ToC first ...
make sure the ToC is optimized then we can make sure the stuff in each section is what belongs there rather than merging
or moving?" Two fresh readers read the contents alone (reads/READ-NOW-1.md, READ-NOW-2.md); RESULTS.md says what each
found and which of their changes each option takes.

Option A, as he chose it on 2026-11-09 18:43 UTC (A, with the brain section first and three headings renamed),
moves whole sections, changes heading levels and renames those headings; it changes no paragraph. Its headings are his, but for "of
Remedies" (both readers' words), "A Final Trip Killer: Niacin (...)" (his two headings joined) and the split of his part
heading into "Tripsitting Yourself or Others" and "Shadow Work" (his own words, from that heading). Option B is only the
remedies part's levels and order and "Who to Contact, and When" moved up, which both readers found broken.

  python3 plan_toc.py A|B [--write-guide OUT.md]   print the contents (with word counts); with --write-guide, the guide
                                                   in that order, for the page that shows it (nothing in the guide changes)
  python3 plan_toc.py A --apply                    rewrite GUIDE-SO-FAR.md and its blocks in that order (only after he
                                                   approves the option)
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[2]
BJ, MD = ART / 'GUIDE-SO-FAR-blocks.json', ART / 'GUIDE-SO-FAR.md'


def level(b):
    m = re.match(r'^(#{1,6}) ', b['md'] or '')
    return len(m.group(1)) if m else 0


def plan(option):
    blocks = json.loads(BJ.read_text(encoding='utf-8'))
    unit = {b['id']: b for b in blocks}
    ids = [b['id'] for b in blocks]

    def sec(bid, stop_before=None):
        """bid's heading and everything up to the next heading of its level or higher (a divider before that heading
        stays with the section it ends); stop_before cuts it short at that block."""
        i = ids.index(bid)
        lv = level(unit[bid])
        j = i + 1
        while j < len(ids) and not (0 < level(unit[ids[j]]) <= lv) and ids[j] != stop_before:
            j += 1
        return ids[i:j]

    def take(seq):
        for x in seq:
            assert x in order, x
            order.remove(x)
        return list(seq)

    def put_before(seq, anchor):
        k = order.index(anchor)
        order[k:k] = seq

    def put_after(seq, anchor):
        k = order.index(anchor) + 1
        order[k:k] = seq

    order = list(ids)
    relevel, rename, new = {}, {}, {}

    # both options: the remedies part, and who to contact with when
    who = take(sec('B261'))
    put_before(who, 'B98')
    relevel['B261'] = 2
    rename['B138'] = '# My Acute Rescue Hierarchy of Remedies'
    caution = take(sec('B217'))                           # Some Remedies Require More Caution, with its divider
    put_before(caution, 'B150')
    stop = take(sec('B169'))                              # stop the trip: beach morning glory, its divider
    final = take(sec('B209'))                             # A Final Trip Killer + niacin + divider
    final.remove('B209')
    rename['B210'] = '#### A Final Trip Killer: Niacin (a Form of Vitamin B3)'
    put_after(stop + final, 'B208')                       # after the stabilizers' divider
    for g in ('B150', 'B164', 'B169', 'B180'):
        relevel[g] = 2
    for e in ('B152', 'B159', 'B166', 'B170', 'B181', 'B183', 'B185', 'B189', 'B199', 'B210', 'R30-OILS1', 'R30-RUE1'):
        if e in unit:
            relevel[e] = 3
    if option == 'B':
        return blocks, unit, order, relevel, rename, new

    # A as he chose it (round 30, 2026-11-09 18:43 UTC: "a sure rename them so readers can find them, and brain should
    # be at top yeah that's kind of one of the most common things people say"): the brain section stays first, and the
    # three headings fresh readers had to guess at are renamed, his words kept with a lead a reader would look for
    rename['N-SF-1'] = "## Risk of Harm: When Peer Support Isn't Enough"
    rename['B285'] = '### When What They Say Turns Toward Harm'
    rename['B347'] = '## Trip After Trip? Hang up the phone, get off the Healing Treadmill'
    rename['B364'] = '# Planning a Trip or Ceremony? Give It a Beginning and an End'
    # DMSO next to humic acid, as the brain section names them
    dmso = sec('B199', stop_before='B208')
    k = ids.index(dmso[-1]) + 1
    while k < len(ids) and ids[k].startswith('R30-RUE'):   # his Syrian rue oil entry (round 30) goes with DMSO
        dmso.append(ids[k])
        k += 1
    dmso = take(dmso)
    put_before(dmso, 'B185')
    # the psychological part split in two, in his words
    rename['B227'] = '# Tripsitting Yourself or Others'
    grounding = take(sec('B294'))
    put_before(grounding, 'B253')
    reflective = take(sec('B329') + sec('B332') + sec('B338'))
    treadmill = take(sec('B347'))
    session = take(sec('B364'))
    content = take(sec('B376') + sec('B385') + sec('B394') + sec('B405') + sec('B410'))
    new['R30-SHADOW'] = {'id': 'R30-SHADOW', 'kind': 'h1', 'md': '# Shadow Work', 'text': None}
    put_before(['R30-SHADOW'] + content + reflective, 'B419')
    # After the Storm a part of its own: the aftermath, then when to bring in support, then the treadmill
    relevel['B419'] = 1
    relevel['B424'] = 2
    support = take(['B96', 'B97'])
    put_before(support + treadmill, 'B431')
    # for next time, its own part at the end
    relevel['B364'] = 1
    put_before(session, 'B431')
    return blocks, unit, order, relevel, rename, new


def realized(option):
    blocks, unit, order, relevel, rename, new = plan(option)
    unit = dict(unit, **new)
    out = []
    for bid in order:
        b = dict(unit[bid])
        if bid in rename:
            b['md'] = rename[bid]
        if bid in relevel:
            b['md'] = '#' * relevel[bid] + ' ' + re.sub(r'^#{1,6} ', '', b['md'])
            b['kind'] = 'h%d' % relevel[bid]
        out.append(b)
    before = sorted(x['id'] for x in blocks if x['id'] != 'B209')
    after = sorted(x['id'] for x in out if x['id'] not in new)
    assert before == after, 'a block was lost or doubled'
    return out


def contents(blocks):
    rows = []
    for b in blocks:
        lv = level(b)
        if lv:
            t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', re.sub(r'^#{1,6} ', '', b['md']))
            rows.append([lv, t.replace('**', ''), 0])
        elif rows:
            rows[-1][2] += len(re.sub(r'\]\([^)]*\)', '', b['md'] or '').split())
    return rows


def main(argv):
    option = argv[0]
    out = realized(option)
    for lv, t, w in contents(out):
        print('%s%s %s  (%d words)' % ('    ' * (lv - 1), '#' * lv, t, w))
    if '--write-guide' in argv:
        p = pathlib.Path(argv[argv.index('--write-guide') + 1])
        p.write_text('\n\n'.join(b['md'] for b in out) + '\n', encoding='utf-8')
    if '--apply' in argv:
        MD.write_text('\n\n'.join(b['md'] for b in out) + '\n', encoding='utf-8')
        BJ.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main(sys.argv[1:])
