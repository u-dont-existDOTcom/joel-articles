"""Batch f1102: the fixes of fixes_f1102.py (ours, and two cards' suggestions) checked through the API with public links,
each in a stretch of at most six paragraphs (E325: the API takes no more; a stretch is the fix with its neighbours, E319,
and its heading, E327), my predictions written first. Each stretch is a new stretch lineage (HG-f1102-NN, try 1 of 2).

The free whole-guide check of 2 November (Joel's result pages, his message of 21:57 UTC) read these windows AI or Human
(Low) in place; every other window of the guide read Human there. So the question each check answers is whether the fix
reads Human with its neighbours before it goes into the guide (ours) or onto his page (cards); the next whole check,
on the Substack drafts with his extension, reads them all in place.

  python3 articles/inner-signal/humanize/fix-20261102/f1102/make_f1102.py [--ledger]
Writes TEXTS.json and PREDICTIONS.json here; with --ledger, adds the predictions.
"""
import argparse
import hashlib
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
F = HERE.parent
H = F.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import fixes_f1102 as fx  # noqa: E402
import suggestion_review as sr  # noqa: E402
import pangram_api  # noqa: E402

LEDGER = H / 'pangram-ledger.jsonl'
DETECTOR = 'pangram 4.1, the API (Joel\'s key, run on his laptop; E218, E325)'
C92B = ("It’s still one grown-up doing three jobs (nobody new is moving in to help with the rent), and each job keeps the "
        "others in balance.")
# key -> (blocks, edits, my chance of a fully Human result, the tells I see, the human tells)
PLAN = {
    'f1102-61': (range(58, 64), ['F-61', 'F-62'], 0.6, 'the pairs of minds in a row that open the paragraph; the four-way pairing, said twice now',
                 'his "Nobody needs to win!"; "The same goes for"'),
    'f1102-119': (range(115, 120), ['F-119'], 0.7, 'the instructions in a row ("just meet it with love")', 'his loop of love going around, "they don\'t owe it to you"'),
    'f1102-216': (range(210, 217), ['F-216'], 0.55, 'the run of questions (the checklist itself), and the list of manipulative sentences',
                  '"Will they punish me, shame me, laugh at me"; the plain boundary line'),
    'f1102-361': (range(360, 365), ['F-361'], 0.55, 'the five steps in brackets; the 3-2-1 senses list', '"a handy appointment with yourself"'),
    'f1102-527': (range(523, 530), ['F-527', 'F-528'], 0.45, 'the run of short questions; the nominalization list', 'his "A bit more safety can come to me"'),
    'f1102-762': (range(758, 763), ['F-762'], 0.6, 'a citation list', 'his Cochrane medal joke; "don\'t blame them"'),
    'c1102-92a': (range(90, 94), ['C-92'], 0.5, 'his "That\'s X, not Y" line now ends on its "not Y" (O9)', 'his rent and party jokes, 🙈'),
    'c1102-92b': (range(90, 94), ['C-92b'], 0.55, 'a bracket inside his line', 'his rent and party jokes, 🙈'),
    'c1102-480': (range(476, 481), ['C-480'], 0.6, 'three prompts in a row', 'his "I\'d only do it if it\'s loving and leaves you free"'),
}


def texts_for():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    ours = fx.apply(md, ('ours',))
    out = {}
    for key, (blocks, edits, *_r) in PLAN.items():
        new = ours
        if key.startswith('c1102'):
            raw = re.split(r'\n\s*\n', new.rstrip('\n'))
            for eid, b, kind, old, nw, why in fx.EDITS:
                if eid in edits:
                    raw[b] = raw[b].replace(old, nw)
            if 'C-92b' in edits:
                old = [e for e in fx.EDITS if e[0] == 'C-92'][0][3]
                assert raw[92].count(old) == 1
                raw[92] = raw[92].replace(old, C92B)
            new = '\n\n'.join(raw) + '\n'
        bl = sr.blocks(new)
        out[key] = '\n\n'.join(bl[i]['text'] for i in blocks)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ledger', action='store_true')
    a = ap.parse_args()
    texts = texts_for()
    rows = []
    for key, (blocks, edits, chance, tells, human) in PLAN.items():
        t = texts[key]
        big = pangram_api.too_big(t)
        assert not big, (key, big)
        rows.append({'key': key, 'lineage': 'HG-' + key, 'scope': 'stretch', 'blocks': list(blocks), 'edits': edits,
                     'words': len(t.split()), 'call': 'Human' if chance >= 0.5 else 'AI', 'chance': chance, 'tells': tells,
                     'human_tells': human, 'sha256': hashlib.sha256(t.encode('utf-8')).hexdigest()})
    (HERE / 'TEXTS.json').write_text(json.dumps(texts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'PREDICTIONS.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for r in rows:
        print(r['key'], r['words'], 'words', r['call'], r['chance'])
    if not a.ledger:
        return
    td = HERE / 'texts'
    td.mkdir(exist_ok=True)
    for r in rows:
        f = td / (r['key'] + '.txt')
        f.write_text(texts[r['key']], encoding='utf-8')
        cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
               '--lineage', r['lineage'], '--scope', r['scope'], '--text', str(f), '--call', r['call'],
               '--chance', str(r['chance']), '--key', r['key'], '--batch', 'f1102', '--detector', DETECTOR,
               '--tells', r['tells'], '--human-tells', r['human_tells'],
               '--diagnosis', 'the free whole check\'s windows below High in it fixed (%s), read with the paragraphs around '
                              'them and the heading' % ', '.join(r['edits']),
               '--decides', 'whether the fix reads Human in place before it goes into the guide (ours) or onto his page (cards)']
        p = subprocess.run(cmd, capture_output=True, text=True)
        if p.returncode:
            sys.exit('%s: %s%s' % (r['key'], p.stdout, p.stderr))
    print('ledger: %d predictions added' % len(rows))


if __name__ == '__main__':
    main()
