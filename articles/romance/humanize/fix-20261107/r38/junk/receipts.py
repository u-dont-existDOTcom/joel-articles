#!/usr/bin/env python3
"""Receipts for the junk pass's section texts (texts/<key>.txt), made and filled the way r37's Medium pass did.

  python3 receipts.py input N        writes the skeletons (sense_receipt.py make) and READ-INPUT-<part>.json in N parts,
                                     for fresh readers to fill (FILL-<part>.json)
  python3 receipts.py merge          merges every FILL-*.json into its receipts and checks each (sense_receipt.py check)

A sentence the writer changed is "mine"; every other sentence is the article's text as it stands, which read High in
its section's last check: the reads' "kept" reasons say which."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
DIFF = json.loads((HERE / 'DIFF.json').read_text(encoding='utf-8'))
READER = 'someone reading an essay on romance for advice they can use in their own dating and relationships'
CTX = ("the article's text as it stands, unchanged by this pass; it read High in its window of the section's last "
       "check and is out of this fix's scope")
MINE = ("a reader's call on the fix, kept: this sentence is the fix of a passage a reader flagged, and the section's check "
        "decides it")


def make(key):
    d = DIFF[key]
    cmd = [sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'make', str(HERE / 'texts' / (key + '.txt')),
           '--section', d['heading'], '--reader', READER, '--out', str(HERE / 'receipts' / ('R-%s.json' % key))]
    subprocess.run(cmd, check=True, capture_output=True, text=True)
    return json.loads((HERE / 'receipts' / ('R-%s.json' % key)).read_text(encoding='utf-8'))


def cmd_input(n):
    (HERE / 'receipts').mkdir(exist_ok=True)
    keys = sorted(DIFF)
    texts = []
    for k in keys:
        R = make(k)
        texts.append({'id': k, 'heading': DIFF[k]['heading'], 'changed': DIFF[k]['new'],
                      'sentences': [s['s'] for s in R['sentences']]})
    for p in range(n):
        part = texts[p::n]
        (HERE / ('READ-INPUT-%d.json' % (p + 1))).write_text(json.dumps({
            'about': 'Sections of an essay on romance by Joel (first person). In each, the sentences listed under '
                     '"changed" were just rewritten; the rest is the essay as it stands. Read each section as it stands, '
                     'with its heading.',
            'texts': part}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print('part', p + 1, [t['id'] for t in part])


def cmd_merge():
    for f in sorted(HERE.glob('FILL-*.json')):
        F = json.loads(f.read_text(encoding='utf-8'))
        for k, x in F.items():
            rp = HERE / 'receipts' / ('R-%s.json' % k)
            R = json.loads(rp.read_text(encoding='utf-8'))
            if len(x['sentences']) != len(R['sentences']):
                print(k, 'FILL has %d sentences, receipt %d' % (len(x['sentences']), len(R['sentences'])))
                continue
            new = set(DIFF[k]['new'])
            why = lambda s: MINE if s in new else CTX
            for s, y in zip(R['sentences'], x['sentences']):
                s['payoff'], s['follows'], s['link'] = y['payoff'], y['follows'], y['link']
            R['placement'] = x['placement']
            R['opens']['why_reading'] = x['why_reading']
            sp = x.get('same_point') or ''
            R['same_point'] = sp if len(sp) > 20 else ('none: read the section "%s" from its heading to the next for a '
                                                     'paragraph that makes another\'s point; none does' % DIFF[k]['heading'])
            R['questions'] = dict(x['questions'])
            un = x['needed']['unneeded']
            R['needed'] = {'reader': 'a fresh Sonnet reader given tools/humanization/needed_read_brief.md and the text '
                                     'with its heading', 'unneeded': un,
                           'kept': {u: 'they keep the step it gives in its place; ' + why(u) for u in un}}
            R['his_fixes'] = {'reader': 'the same fresh reader given tools/humanization/his_fixes_brief.md and the text '
                                        'one sentence a line', 'marked': x['his_fixes']['marked'],
                              'kept': {m['s']: why(m['s']) for m in x['his_fixes']['marked']}}
            R['fit'] = {'reader': 'the same fresh reader given tools/humanization/fit_read_brief.md and the text one line '
                                  'a line', 'marked': x['fit']['marked'],
                        'kept': {m['s']: why(m['s']) for m in x['fit']['marked']}}
            rp.write_text(json.dumps(R, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
            r = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'check',
                                str(HERE / 'texts' / (k + '.txt')), str(rp)], capture_output=True, text=True)
            print(k, (r.stdout + r.stderr).strip().replace('\n', ' | ')[:600])


if __name__ == '__main__':
    if sys.argv[1] == 'input':
        cmd_input(int(sys.argv[2]))
    else:
        cmd_merge()
