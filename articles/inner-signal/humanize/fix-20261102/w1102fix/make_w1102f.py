"""Batch w1102f: the fixes of fixes_w1102.py (ours, and the cards' suggestions) checked through the API with public links,
my predictions written first: each section they change, by itself (one more check after the fix where a section has used
its two: Joel's answer 28a, 2026-11-02 19:11 UTC, "one more check of the whole section after each fix, each with my
prediction written first"), and the whole guide again in the same two halves as batch w1102 (try 2 of 2), since the
windows fixed here read AI or Human (Low) only in the whole (E319: a verdict belongs to the text it was given).

The halves carry the cards' suggestions too, so each card can show how its suggestion reads in place; the guide itself takes
only our fixes until he answers.

Every section here read Human by itself in its last check (the ledger), so my chance of a fully Human result for each is
high; the halves are the real test, and Pangram moves windows between checks of the same words (E304), so less.

  python3 articles/inner-signal/humanize/fix-20261102/w1102fix/make_w1102f.py [--ledger]
Writes TEXTS.json, PREDICTIONS.json and SECTIONS-W1102F.json here; with --ledger, adds the predictions.
"""
import argparse
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
F = HERE.parent
H = F.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(F / 'whole'))
import fixes_w1102 as fx  # noqa: E402
import read_w1102 as rw  # noqa: E402
import suggestion_review as sr  # noqa: E402

LEDGER = H / 'pangram-ledger.jsonl'
DETECTOR = 'pangram 4.1, the API (Joel\'s key, run on his laptop; E218)'
CUT = 'The 15-minute daily practice'
# section key -> (edits in it, my chance of a fully Human result, the tells I see, the human tells, after-fix?)
PLAN = {
    's1101-02': (['F-11', 'F-16'], 0.7, 'one list of minds left in his sentence before', 'his "Hello Lovey Bunny!", the fantasy mind applying for a job'),
    's1101-03': (['F-20'], 0.7, 'the numbered steps of the quick start', 'his teleprompter line; "even if it\'s an objection or a long silence"'),
    's1101-07': (['F-42'], 0.65, 'the list of four authorities in the first sentence', 'his V. story; "all your annoying questions"'),
    's1101-23': (['F-140', 'C-141'], 0.7, 'the long list of feelings that open the paragraph', 'his inner child guide\'s lines as he wrote them'),
    's1101-33': (['F-216'], 0.6, 'a run of questions (the checklist itself)', 'the seatbelt on the highway'),
    's1101-34': (['F-218'], 0.6, 'the numbered list of eight ways soft language takes away choice', 'his "Just so you know, if you say no"'),
    's1101-37': (['F-251'], 0.65, 'instructions in a row', 'his dad\'s "Be prepared to take what you get", the fire exit sign'),
    's1101-38': (['F-253', 'F-255', 'F-265'], 0.55, 'script language ("Allow yourself some time to do this")', 'the phone\'s voice recorder, the doorknob'),
    's1101-55': (['C-384'], 0.7, 'three questions in a row in the first sentence', 'his inner child guide\'s lines as he wrote them'),
    's1101-69': (['F-527', 'F-528'], 0.6, 'nine patterns in a row, each with its example', 'his McHappyness joke; the workshop leader and your ex'),
    's1101-79': (['C-626'], 0.7, 'the script in quotes', 'his "No warmth today? ... no faking required"'),
    's1101-84': (['C-672'], 0.6, 'the matched pair it fixes, if it still reads so', 'his Jesus on the Cross, his mumbo jumbo, "moving into this wound"'),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ledger', action='store_true')
    a = ap.parse_args()
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    new = fx.apply(md)
    nb = sr.blocks(new)
    dropped = sorted(e[1] for e in fx.EDITS if e[4] is None)
    def now(i):
        return None if i in dropped else i - sum(1 for d in dropped if d < i)
    m = rw.current_index_maps()
    secs = {s['key']: s for s in json.loads((F.parent / 'fix-20261101' / 'sections' / 'SECTIONS.json').read_text(encoding='utf-8'))['sections']}
    texts, rows, smap = {}, [], []
    eids = {e[0] for e in fx.EDITS}
    for key, (edits, chance, tells, human, ) in ((k, v[:4]) for k, v in PLAN.items()):
        assert set(edits) <= eids
        idx = [now(i) for old in secs[key]['blocks'] for i in m.get(old, [])]
        idx = sorted({i for i in idx if i is not None})
        t = '\n\n'.join(nb[i]['text'] for i in idx)
        name = 'w1102f-' + key.split('-')[1]
        texts[name] = t
        smap.append({'key': name, 'section': key, 'name': secs[key]['name'], 'blocks': idx, 'edits': edits,
                     'words': len(t.split()), 'sha256': hashlib.sha256(t.encode('utf-8')).hexdigest()})
        rows.append({'key': name, 'name': secs[key]['name'], 'lineage': 'HG1101-' + key.split('-')[1], 'scope': 'section',
                     'words': len(t.split()), 'call': 'Human', 'chance': chance, 'tells': tells, 'human_tells': human,
                     'why': 'read Human by itself in its last check; the fixes %s read in place' % ', '.join(edits),
                     'sha256': hashlib.sha256(t.encode('utf-8')).hexdigest(), 'edits': edits})
    [k] = [b['i'] for b in nb if b['level'] == 1 and b['text'] == CUT]
    for half, ids, chance, tells in (('A', range(0, k), 0.4, 'his "Then put the screen away." and the countdown numbers, Low in w1102'),
                                     ('B', range(k, len(nb)), 0.45, 'his Reframing paragraph, Low in w1102')):
        t = '\n\n'.join(nb[i]['text'] for i in ids)
        assert len(t) < 99999
        name = 'w1102f-' + half
        texts[name] = t
        rows.append({'key': name, 'name': 'the whole guide, half ' + half, 'lineage': 'HG1102-whole-' + half, 'scope': 'stretch',
                     'words': len(t.split()), 'call': 'AI', 'chance': chance, 'tells': tells,
                     'human_tells': 'every window of w1102 below High in our words fixed, and the cards\' suggestions in place',
                     'why': 'try 2 of 2: the fixes in the whole, where the windows read AI or Low; windows move between checks (E304)',
                     'sha256': hashlib.sha256(t.encode('utf-8')).hexdigest(), 'edits': [e[0] for e in fx.EDITS]})
    (HERE / 'TEXTS.json').write_text(json.dumps(texts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'PREDICTIONS.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'SECTIONS-W1102F.json').write_text(json.dumps({'guide_with_edits_sha256': hashlib.sha256(new.encode('utf-8')).hexdigest(),
                                                           'sections': smap}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for r in rows:
        print(r['key'], r['lineage'], r['words'], r['call'], r['chance'])
    if not a.ledger:
        return
    td = HERE / 'texts'
    td.mkdir(exist_ok=True)
    after = {k for k, v in PLAN.items() if k in ('s1101-23', 's1101-37', 's1101-69', 's1101-84')}
    for r in rows:
        f = td / (r['key'] + '.txt')
        f.write_text(texts[r['key']], encoding='utf-8')
        cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
               '--lineage', r['lineage'], '--scope', r['scope'], '--text', str(f), '--call', r['call'],
               '--chance', str(r['chance']), '--key', r['key'], '--batch', 'w1102f', '--detector', DETECTOR,
               '--tells', r['tells'], '--human-tells', r['human_tells'],
               '--diagnosis', 'the w1102 windows below High in it fixed (%s): %s' % (', '.join(r['edits'][:6]), r['why']),
               '--decides', 'whether the fixes read Human in place before they go into the guide or onto his cards']
        sec = 's1101-' + r['key'].split('-')[1]
        if sec in after:
            cmd += ['--after-fix', 'the fixes %s (his answer 28a: one more check of the whole section after each fix)' % ', '.join(r['edits'])]
        p = subprocess.run(cmd, capture_output=True, text=True)
        if p.returncode:
            sys.exit('%s: %s%s' % (r['key'], p.stdout, p.stderr))
    print('ledger: %d predictions added' % len(rows))


if __name__ == '__main__':
    main()
