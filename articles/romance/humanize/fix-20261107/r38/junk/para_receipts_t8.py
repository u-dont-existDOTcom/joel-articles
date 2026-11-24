#!/usr/bin/env python3
"""A paragraph's making-sense receipt for each new paragraph on the eighth marking page (CARDS-T8.json), made from the
receipt of the section try that read Human High in every window: the paragraph's sentences with their fills (fresh
readers' and my verdicts, carried by their words), and the section's reads (placement, same point, needed, his fixes,
fit, the nine questions), which were read on the whole section with this paragraph in it.

  python3 para_receipts_t8.py   ->  para/R-<card>-<live>.json, each checked (sense_receipt.py check)
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import sense_receipt  # noqa: E402

M = HERE
OUT = M / 'para'
OUT.mkdir(exist_ok=True)
CARDS = json.loads((HERE / 'CARDS-T8.json').read_text(encoding='utf-8'))
FOLDERS = ('t2', 'receipts')
made = {}
for cid, changes in CARDS.items():
    for ch in changes:
        if not ch['after']:
            continue
        para = ch['after'][0]
        key = ch['section_key']
        src = None
        for f in FOLDERS:
            p = M / f / ('R-%s.json' % key)
            if p.exists():
                r = json.loads(p.read_text(encoding='utf-8'))
                if para in r.get('text', '').split('\n\n'):
                    src = (p, r)
                    break
        assert src, (cid, key)
        p, S = src
        have = {s['s']: s for s in S['sentences']}
        R = sense_receipt.make(para, S['section'], S['reader'])
        for s in R['sentences']:
            for f in ('payoff', 'follows', 'link'):
                s[f] = have[s['s']][f]
        R['made'] = S['made']
        R['derived_from'] = ('%s: the receipt of the section try that read Human High in every window (%s); this '
                             'paragraph\'s sentences with their fills, and the section\'s reads, made on the whole section'
                             % (p.relative_to(ROOT), ch['his_checks'][0]))
        R['placement'] = 'The paragraph is number %d of the section "%s". In the section: %s' % (
            ch['paragraph'], S['section'], S['placement'])
        first = R['sentences'][0]
        R['opens']['why_reading'] = 'Its first sentence gives them what this paragraph is for: %s' % first['payoff']
        R['same_point'] = S['same_point']
        keep = {s['s'] for s in R['sentences']}
        R['needed'] = dict(S['needed'], unneeded=[u for u in S['needed']['unneeded'] if u in keep],
                           kept={u: v for u, v in S['needed'].get('kept', {}).items() if u in keep})
        for read in ('his_fixes', 'fit'):
            R[read] = dict(S[read], marked=[m for m in S[read]['marked'] if m['s'] in keep],
                           kept={u: v for u, v in S[read].get('kept', {}).items() if u in keep})
        R['questions'] = S['questions']
        R['question_text'] = S.get('question_text')
        out = OUT / ('R-%s-%d.json' % (cid, ch['live']))
        out.write_text(json.dumps(R, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        probs = sense_receipt.check(para, R)
        print(out.name, 'PASS' if not probs else 'FAIL: ' + ' | '.join(probs)[:500])
        made.setdefault(cid, []).append(str(out.relative_to(ROOT)))
(OUT / 'INDEX.json').write_text(json.dumps(made, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
