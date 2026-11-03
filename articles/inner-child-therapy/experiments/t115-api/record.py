#!/usr/bin/env python3
"""Turn 115: record an API results file in the ledger (one result per check, the ledger's own verdict rule, as turns 104 to
113 did), and read each check the way E276 (Inner Child) asks: every window below Human with High confidence, not only the
AI ones. For each fix of the pass, it finds the fixed paragraph in its block and lists the windows over it.

A fix goes in when its gate is passed (the three reviews, and for new words the owner-delivery gate) and its block's check
reads no AI and no Low window over the fixed paragraph; a Medium window there is shaded in the docx for the next
whole-guide check to read in context. A fix that doesn't meet that gets a diagnosed second try or stays out.

  python3 record.py API-RESULTS-N.jsonl [--ledger]      updates BLOCK-RESULTS.json; --ledger also records the results"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from pangram_ledger import verdict_of  # noqa: E402
from paragraphs_alone import plain  # noqa: E402
from substack_check_text import smart  # noqa: E402

FIXES = {f['id']: f for f in json.loads((HERE.parent / 't115-pass' / 'FIXES.json').read_text(encoding='utf-8'))['fixes']}
STRAIGHT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})
OUT = HERE / 'BLOCK-RESULTS.json'


def paragraph_span(text, fix):
    """[start, end) of the fixed paragraph (a line of the block) in the submitted text."""
    key = smart(plain(fix['new'])).translate(STRAIGHT)
    pos = 0
    for line in text.split('\n'):
        if key[:60] in line.translate(STRAIGHT) or key[-60:] in line.translate(STRAIGHT):
            return pos, pos + len(line)
        pos += len(line) + 1
    raise SystemExit('fixed paragraph of %s not found in its block' % fix['id'])


def main(path, ledger):
    names = json.loads((HERE / 'NAMES.json').read_text(encoding='utf-8'))
    texts = json.loads(next(HERE.glob('TEXTS-*.json')).read_text(encoding='utf-8'))
    for p in sorted(HERE.glob('TEXTS-*.json')):
        texts.update(json.loads(p.read_text(encoding='utf-8')))
    res = json.loads(OUT.read_text(encoding='utf-8')) if OUT.exists() else {'fixes': {}, 'checks': {}}
    for line in open(path, encoding='utf-8'):
        r = json.loads(line)
        n, text = r['name'], texts[r['name']]
        ws = r.get('windows', [])
        below = [w for w in ws if not (w[0].startswith('Human') and w[1] == 'High')]
        ai = [w for w in ws if w[0].startswith('AI')]
        v = verdict_of(r['headline'], None, r['fraction_ai'])
        res['checks'][n] = {'link': r['dashboard_link'], 'headline': r['headline'], 'fraction_ai': r['fraction_ai'],
                            'words': r['words'], 'windows': len(ws), 'ai_windows': len(ai), 'below_high': len(below),
                            'verdict': v, 'utc': r['utc'],
                            'below_high_windows': [{'label': w[0], 'confidence': w[1], 'words': w[2], 'text': w[5].strip()} for w in below]}
        for fid in names['fixes'][n]:
            a, e = paragraph_span(text, FIXES[fid])
            over = [w for w in below if w[3] < e and w[4] > a]
            para = [[max(w[3], a) - a, min(w[4], e) - a, 'AI' if w[0].startswith('AI') else 'Human', w[1], None, w[2]] for w in over]
            bad = [w for w in over if w[0].startswith('AI') or w[1] == 'Low']
            shown = ('every window over it Human, High' if not over else '; '.join('%s, %s (%d words) on "%s"' % (
                'AI' if w[0].startswith('AI') else 'Human', w[1], w[2], w[5].strip()[:90]) for w in over))
            res['fixes'][fid] = {
                'check': n, 'link': r['dashboard_link'], 'para_windows': para, 'meets': not bad,
                'summary': 'Checked with its block after the change (%s): %s, %.2f%% AI. In this paragraph: %s.' % (
                    r['dashboard_link'], r['headline'], 100 * r['fraction_ai'], shown)}
        if ledger:
            cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'result', str(LEDGER), '--key', n,
                   '--verdict', v, '--link', r['dashboard_link'], '--headline', '%s; %d of %d windows below High (%d AI)' % (
                       r['headline'], len(below), len(ws), len(ai)),
                   '--ai-fraction', '%.6f' % r['fraction_ai'], '--words', str(r['words']), '--detector', 'pangram-4.1-api',
                   '--at', r['utc']]
            out = subprocess.run(cmd, capture_output=True, text=True)
            if out.returncode:
                sys.exit('%s: %s%s' % (n, out.stdout[-600:], out.stderr[-600:]))
            print(out.stdout.strip().split('\n')[-1])
        print('%-18s %-6s %.4f%% AI, %d windows, %d below High (%d AI) | %s' % (n, v, 100 * r['fraction_ai'], len(ws), len(below), len(ai), r['dashboard_link']))
        for w in below:
            print('      %s %s %dw: %s' % (w[0][:5], w[1], w[2], w[5].strip()[:110]))
    res['installed'] = sorted(k for k, x in res['fixes'].items() if x['meets'])
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('fixes meeting the bar:', res['installed'])


if __name__ == '__main__':
    main(sys.argv[1], '--ledger' in sys.argv)
