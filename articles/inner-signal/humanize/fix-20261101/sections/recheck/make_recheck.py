"""The second and last check of each section of batch s1101 whose windows are all fixed or decided (gate E307; Joel,
2026-11-01 18:57 UTC), with my predictions written before the run.

A section is ready when every window CONFIDENCE.md lists for it is fixed in our words (../FIXES-S1101.json) or isn't
prose, and none of its windows is in his words waiting on his cards page (../review/REVIEW-S1101.json): eleven sections
on 1 November. The rest wait for his answers. Each text is the section as it stands, cut at the same blocks as the first
check (../SECTIONS.json), so the two results compare window by window.

My chance of a 100% Human result per section starts from the first check: a section that read Human Written with a few
Low windows, 0.7; Mostly Human, 0.6; AI Detected, 0.45; less where much of it is new words Pangram hasn't read (each fix
is new words), more where the fixes changed little. One prediction per section in the ledger (lineage HG1101-NN, try 2
of 2; pangram_ledger.py refuses a third).

  python3 articles/inner-signal/humanize/fix-20261101/sections/recheck/make_recheck.py [--ledger]
Writes r1101-items.json ([key, text, sha256]), SECTIONS-R1101.json and PREDICTIONS.md / .json; with --ledger, adds each
prediction to ../../../pangram-ledger.jsonl.
"""
import argparse
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
D = HERE.parent
H = D.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

LEDGER = H / 'pangram-ledger.jsonl'
TEXTS = HERE / 'texts'
BATCH = 'r1101'

# section: (chance, what the chance rests on)
CHANCE = {
    's1101-14': (0.6, 'Mostly Human Written (0.05) on 1 November; its two Low windows rewritten (round 1)'),
    's1101-17': (0.45, 'AI Detected (0.23); its three windows rewritten (round 1), the AI (High) one a list made into '
                       'sentences'),
    's1101-28': (0.65, 'Mostly Human Written (0.01); one Human (Low) sentence said plainly'),
    's1101-42': (0.7, 'Human Written; one Human (Low) closer said with the published "at most"'),
    's1101-44': (0.4, 'AI Detected (0.24); its last two paragraphs (AI High, 126 words) rewritten, with the published '
                      'point about the recording that cuts out'),
    's1101-46': (0.55, 'Mostly Human Written (0.08); its AI (High) opening rewritten'),
    's1101-53': (0.4, 'AI Detected (0.65) on 126 words, nearly all rewritten now'),
    's1101-59': (0.55, 'AI Detected (0.19) on one AI (Medium) window; that paragraph rewritten'),
    's1101-92': (0.65, 'Human Written with two Human (Low) windows, both rewritten (the warning signs kept whole)'),
    's1101-93': (0.55, 'AI Detected (0.11) on one AI (Low) sentence, rewritten'),
    's1101-96': (0.7, 'Human Written; one Human (Low) closing line rewritten'),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ledger', action='store_true')
    a = ap.parse_args()
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    bl = sr.blocks(md)
    first = {s['key']: s for s in json.loads((D / 'SECTIONS.json').read_text(encoding='utf-8'))['sections']}
    res = json.loads((D / 'RESULTS.json').read_text(encoding='utf-8'))
    fx = json.loads((D / 'FIXES-S1101.json').read_text(encoding='utf-8'))
    cards = json.loads((D / 'review' / 'REVIEW-S1101.json').read_text(encoding='utf-8'))['suggestions']
    conf = json.loads((D / 'CONFIDENCE.json').read_text(encoding='utf-8'))['fix']
    waiting = {s for c in cards for sp in c['spans'] for s, f in first.items() if sp['block'] in f['blocks']}
    waiting |= {w['section'] for w in fx['windows'] if w['fate'] == 'card'}
    keys = sorted({w['key'] for w in conf} - waiting)
    handled = {w['section'] for w in fx['windows'] if w['fate'] in ('fixed', 'not prose')}
    assert set(keys) <= handled, set(keys) - handled
    ready = [k for k in keys if k in CHANCE]
    assert set(ready) == set(CHANCE), (sorted(set(keys) - set(CHANCE)), sorted(set(CHANCE) - set(keys)))
    secs, rows = [], []
    for k in ready:
        f = first[k]
        text = '\n\n'.join(bl[i]['text'] for i in f['blocks'])
        nk = '%s-%s' % (BATCH, k.split('-')[1])
        secs.append({'key': nk, 'first': k, 'name': f['name'], 'blocks': f['blocks'], 'words': len(text.split()),
                     'sha256': hashlib.sha256(text.encode('utf-8')).hexdigest(), 'text': text})
        chance, why = CHANCE[k]
        r1 = res[k]
        rows.append({'key': nk, 'first': k, 'lineage': 'HG1101-%s' % k.split('-')[1], 'name': f['name'],
                     'words': len(text.split()), 'call': 'Human' if chance >= 0.5 else 'AI', 'chance': chance,
                     'why': why, 'first_result': '%s (%.3f), %s' % (r1['headline'], r1['likelihood'], r1['link'])})
    (HERE / 'SECTIONS-R1101.json').write_text(json.dumps({'guide_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(),
                                                          'sections': secs}, ensure_ascii=False, indent=1) + '\n',
                                              encoding='utf-8')
    (HERE / ('%s-items.json' % BATCH)).write_text(json.dumps([[s['key'], s['text'], s['sha256']] for s in secs],
                                                            ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    out = ['# Batch r1101: the second and last check of eleven sections by themselves (predictions, before the run)', '',
           'Gate E307. Each section\'s windows that read AI or Human (Low) on 1 November are fixed in our words '
           '(../FIXES-S1101.json); none waits on his cards. Chance = my chance of a 100% Human result. The Pangram column '
           'is filled after the run.', '', '| text | mine | chance | why | first check | Pangram |', '|---|---|---|---|---|---|']
    for r in rows:
        out.append('| %s: %s (%d words) | %s | %.2f | %s | %s | |' % (
            r['key'], r['name'].replace('|', '/'), r['words'], r['call'], r['chance'], r['why'], r['first_result']))
    (HERE / 'PREDICTIONS.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    (HERE / 'PREDICTIONS.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(rows), 'sections,', sum(r['words'] for r in rows), 'words; waiting on his cards:', len(waiting))
    if not a.ledger:
        return
    TEXTS.mkdir(exist_ok=True)
    for s, r in zip(secs, rows):
        f = TEXTS / (s['key'] + '.txt')
        f.write_text(s['text'], encoding='utf-8')
        cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
               '--lineage', r['lineage'], '--scope', 'section', '--text', str(f), '--call', r['call'],
               '--chance', str(r['chance']), '--key', s['key'], '--batch', BATCH,
               '--tells', 'first check: ' + r['first_result'].split(',')[0],
               '--human-tells', 'its AI and Human (Low) windows fixed in our words, read beside the published version',
               '--diagnosis', r['why'],
               '--decides', 'whether this section reads Human by itself after its fixes (E306, E307): try 2 of 2']
        p = subprocess.run(cmd, capture_output=True, text=True)
        if p.returncode:
            sys.exit('%s: %s%s' % (s['key'], p.stdout, p.stderr))
    print('ledger: %d predictions added' % len(rows))


if __name__ == '__main__':
    main()
