#!/usr/bin/env python3
"""coverage.py - which of the article's paragraphs, as they stand now, have a Pangram check of their exact words, and
what it read: what is left is computed, not remembered (lesson bad-trips-2026-11-24m; the bad trips lane's
h73-20261124/coverage.py, for this lane's ledger and check folders).

A paragraph is "alone" when the latest recorded check of exactly its words (links read as their words) has every window
Human High; "inside" when its words sit inside a larger checked text whose every window read Human High (enough for a
paragraph under 50 words, which Pangram can't read alone; for a longer one it still needs its own check: a paragraph
can't hide inside a section that passes); "below" when its latest check has a window below Human High; "never" when no
check has its present words. His own checks count too (fix-*/**/HIS-CHECKS-*.json).

  python3 articles/neuro-de-armoring/humanize/coverage.py [--md LEFT.md]
"""
import argparse
import ast
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402

ARTICLE = HERE / 'HUMANIZED-SO-FAR.md'
LEDGER = HERE / 'pangram-ledger.jsonl'
GIT = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/neuro-de-armoring/humanize/'


def norm(s):
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s or '')
    s = s.replace('**', '').replace('’', "'").replace('“', '"').replace('”', '"')
    # italics as typed into Pangram: the words without their marks (the Cognitive Warning's *Mindwise*, 2026-11-26)
    s = re.sub(r'(?<![\w*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![\w*])', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def windows(r):
    """[(label, confidence)] of a result record, whichever way the lane wrote them; None when it recorded none."""
    ws = r.get('windows')
    if isinstance(ws, str):
        try:
            ws = ast.literal_eval(ws)
        except (ValueError, SyntaxError):
            ws = None
    out = []
    for w in ws or []:
        if isinstance(w, dict):
            out.append((str(w.get('label') or ''), str(w.get('confidence') or '')))
        elif isinstance(w, (list, tuple)) and len(w) >= 2:
            out.append((str(w[0]), str(w[1])))
        elif isinstance(w, str):
            parts = [x.strip() for x in w.split(',')]
            if len(parts) >= 2:
                out.append((parts[0], parts[1]))
    if out:
        return out
    shade = str(r.get('shading') or '')
    if shade:
        confs = re.findall(r'High|Medium|Low', shade)
        label = 'Human' if str(r.get('verdict')) == 'Human' else 'AI'
        return [(label, c) for c in confs] or None
    return None


def all_high(ws):
    return bool(ws) and all(lab.startswith('Human') and conf == 'High' for lab, conf in ws)


def shown(ws, r):
    if not ws:
        return str(r.get('headline') or r.get('verdict') or '?') + ' (windows not recorded)'
    parts = ['%s %s' % (lab.replace('AI-Generated', 'AI'), conf) for lab, conf in ws]
    return ', '.join(parts[:8]) + (' … (%d windows)' % len(parts) if len(parts) > 8 else '')


def checks():
    """Every recorded check, oldest first: (at, sha256 of the checked text, its normalized text or '', windows, link,
    lineage, result)."""
    recs = [json.loads(l) for l in LEDGER.read_text(encoding='utf-8').splitlines() if l.strip()]
    preds = {r['id']: r for r in recs if r.get('type') == 'prediction'}
    voided = {r.get('prediction') for r in recs if r.get('type') == 'void'}
    texts = {}
    for p in preds.values():
        if p.get('text'):
            texts[sha(p['text'])] = norm(p['text'])
    for f in HERE.glob('fix-*/**/TEXTS.json'):
        try:
            for t in json.loads(f.read_text(encoding='utf-8')).values():
                if isinstance(t, str):
                    texts[sha(t)] = norm(t)
        except (ValueError, OSError):
            pass
    for f in HERE.glob('fix-*/**/*.txt'):
        try:
            t = f.read_text(encoding='utf-8')
        except (OSError, UnicodeDecodeError):
            continue
        for v in (t, t.rstrip('\n'), t.strip()):
            texts.setdefault(sha(v), norm(v))
    latest = {}
    for r in recs:  # a later result line for the same prediction corrects the earlier one
        if r.get('type') == 'result' and r.get('prediction') in preds and r.get('prediction') not in voided:
            latest[r['prediction']] = r
    out = []
    for pid, r in latest.items():
        p = preds[pid]
        h = p.get('sha256') or r.get('sha256') or ''
        out.append((str(r.get('at') or p.get('at') or ''), h, texts.get(h, ''), windows(r), r.get('link') or '',
                    p.get('lineage') or pid, r))
    for f in HERE.glob('fix-*/**/HIS-CHECKS-*.json'):
        for c in json.loads(f.read_text(encoding='utf-8')).get('checks', []):
            ws = [(str(w[0]), str(w[1])) for w in c.get('windows', [])]
            out.append((str(c.get('at') or '2026-11-24T18:40:00Z'), c.get('text_sha256') or '', '', ws,
                        'https://www.pangram.com/history/' + c['uuid'], 'his own check, card ' + str(c.get('card')),
                        {'headline': c.get('headline')}))
    out.sort(key=lambda x: x[0])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--md', default='')
    a = ap.parse_args()
    done = checks()
    heading, rows, counts = '', [], {'alone': 0, 'inside': 0, 'inside-long': 0, 'below': 0, 'never': 0}
    n = 0
    for b in cr.sr.blocks(ARTICLE.read_text(encoding='utf-8')):
        text = b['text']
        if b.get('kind', '').startswith('h') or re.match(r'^#{1,6} ', b.get('md', '') or ''):
            heading = norm(text)
            continue
        t = norm(text)
        if len(t.split()) < 8 or t.startswith('[image') or t.startswith('image '):
            continue
        n += 1
        own = {sha(v) for v in (text, text + ' ', text + '\n', text.strip())}
        exact = inside = None
        for c in done:
            if c[1] in own:
                exact = c
            elif c[2] and t in c[2] and c[2] != t:
                inside = c
            elif c[2] == t:
                exact = c
        words = len(t.split())
        hit = exact or inside
        if exact and all_high(exact[3]):
            counts['alone'] += 1
            continue
        if not exact and inside and all_high(inside[3]):
            if words < 50:
                counts['inside'] += 1
                continue
            counts['inside-long'] += 1
            rows.append((1, n, heading, words, t[:70], 'only inside a larger text that read Human High', inside[4]))
            continue
        if not hit:
            counts['never'] += 1
            rows.append((2, n, heading, words, t[:70], 'never checked as it stands', ''))
            continue
        counts['below'] += 1
        ai = any(lab.startswith('AI') for lab, _ in hit[3] or []) or str(hit[6].get('verdict')) in ('AI', 'Mixed')
        rows.append((4 if ai else 3, n, heading, words, t[:70],
                     ('by itself: ' if hit is exact else 'inside a larger text: ') + shown(hit[3], hit[6]), hit[4]))
    total = sum(counts.values())
    head = ('%d paragraphs of 8 words or more. Human High by itself: %d; under 50 words and inside a text that read Human '
            'High: %d; 50 words or more and only checked inside a larger text: %d; latest check below Human High: %d; '
            'never checked as they stand: %d.' % (total, counts['alone'], counts['inside'], counts['inside-long'],
                                                   counts['below'], counts['never']))
    print(head)
    if a.md:
        by = {}
        for r in rows:
            by.setdefault(r[2], []).append(r)
        md = ['# Neuro de-armoring: what is left to humanize', '',
              'Computed by [coverage.py](%scoverage.py) from the article as it stands ([HUMANIZED-SO-FAR.md](%sHUMANIZED-SO-FAR.md), %s) '
              'and every recorded Pangram check ([the ledger](%spangram-ledger.jsonl) and his own checks).'
              % (GIT, GIT, sha(ARTICLE.read_text(encoding='utf-8'))[:8], GIT), '', head, '',
              'A paragraph listed here has no check of its present words that read Human High in every window. Paragraph '
              'numbers count the paragraphs of 8 words or more, from the top.', '']
        for h, rs in by.items():
            md += ['## %s (%d left)' % (h or 'Before the first heading', len(rs)), '']
            for worst, num, _, words, start, state, link in rs:
                md.append('- P%d (%d words) "%s…": %s%s' % (num, words, start, state,
                                                             (' ([the check](%s))' % link) if link else ''))
            md.append('')
        pathlib.Path(a.md).write_text('\n'.join(md), encoding='utf-8')
        print('wrote', a.md)


if __name__ == '__main__':
    main()
