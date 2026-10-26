#!/usr/bin/env python3
"""Turn 115: every window round 8 read below Human with High confidence, by section, beside what round 6 read for the same
words (Joel, 2026-10-26 12:24 UTC: "let's start prioritizing working now on spots that are not high confidence human ...
it's important data to see in a large pangram test what's not high conf human, for learning").

Round 8 is the whole-guide check of turn 114's two Substack drafts (experiments/t114-substack/PAYLOAD-A.html and -B.html),
read in this turn (RESULT-A.json and RESULT-B.json beside this file: the page's windows and the checked text, whose SHA-256
matched the page's). Round 6 is turn 107's (experiments/t108-results/). Adapted from experiments/t109-windows/windows_list.py.

For each window that isn't Human with High confidence it gives: its label, confidence and words; its section (the headings
above it, from the payload); its paragraph with the window marked; whose words (an aid: "his" when every sentence is in a
text recorded as his in OWNER-EDITS.json, in an entry whose id has "joel" in it); and round 6's reading of the same words
(the windows of round 6 that covered them, when the words were there then).

  python3 windows_list.py      writes WINDOWS.json and WINDOWS.md beside this file"""
import html
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import plain  # noqa: E402  (its ptext.plain)
from substack_check_text import smart  # noqa: E402

BRANCH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/'
HALVES = {'A': 'https://www.pangram.com/feed/909d378e-11d2-4722-b988-a508256c78b4',
          'B': 'https://www.pangram.com/feed/bd483bd6-edab-4f39-834c-3d959b0abb72'}
R6 = {'A': 'https://www.pangram.com/feed/41dfb451-494d-4a13-a76c-335d372dbd4a',
      'B': 'https://www.pangram.com/feed/64c71597-3987-48a7-8431-c8bdc70fddcc'}
STRAIGHT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'", '‍': None, '️': None})


def norm(s):
    return re.sub(r'\s+', ' ', s.translate(STRAIGHT)).strip()


def payload_seq(half):
    raw = (ART / ('experiments/t114-substack/PAYLOAD-%s.html' % half)).read_text(encoding='utf-8')
    path, out = [], []
    for m in re.finditer(r'<(h[1-6]|p)\b[^>]*>(.*?)</\1>', raw, re.S):
        tag, text = m.group(1), html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
        if tag[0] == 'h':
            lvl = int(tag[1])
            path = [p for p in path if p[0] < lvl] + [(lvl, text)]
        else:
            out.append((tuple(t for _, t in path), text))
    return out


def line_sections(text, seq):
    lines = text.split('\n')
    out, k = [], 0
    for line in lines:
        n = norm(line)
        hit = next((j for j in range(k, min(k + 8, len(seq))) if norm(seq[j][1]) == n), None)
        if hit is None and n:
            hit = next((j for j in range(k, min(k + 8, len(seq))) if norm(seq[j][1])[:50] == n[:50]), None)
        if hit is not None:
            out.append(seq[hit][0])
            k = hit + 1
        else:
            out.append(out[-1] if out else ())
    return lines, out


def his_texts():
    d = json.loads((ART / 'OWNER-EDITS.json').read_text(encoding='utf-8'))
    out = []
    for e in d['entries']:
        if 'joel' in e['id']:
            out += [norm(smart(plain(s))) for s in e.get('must_contain_exact', []) + e.get('must_contain', []) if len(s) > 20]
    return out


def sentences(s):
    return [x for x in re.split(r'(?<=[.!?…])\s+', s) if len(x.split()) >= 3]


def whose(window_text, his):
    ss = sentences(norm(window_text)) or [norm(window_text)]
    inside = [s for s in ss if any(s in h for h in his)]
    if len(inside) == len(ss):
        return 'his'
    return 'partly his' if inside else 'not recorded as his'


def round6(core):
    """Round 6's windows over the same words, when they were in round 6's text: [(label, confidence, words)]."""
    n = norm(core)
    if len(n) < 12:
        return None
    for half in 'AB':
        r = json.loads((ART / ('experiments/t108-results/RESULT-%s.json' % half)).read_text(encoding='utf-8'))
        t = r['text']
        flat = t.translate(STRAIGHT)
        i = flat.find(core.translate(STRAIGHT).strip())
        if i < 0:
            continue
        j = i + len(core.strip())
        return {'half': half, 'windows': [('AI' if w['label'].startswith('AI') else 'Human', w['confidence'], w['words'])
                                          for w in r['windows'] if w['start'] < j and w['end'] > i]}
    return None


def r6_text(x):
    if x is None:
        return 'not in round 6 as it is now'
    ws = x['windows']
    worst = sorted(ws, key=lambda w: (w[0] != 'AI', {'Low': 0, 'Medium': 1, 'High': 2}[w[1]]))[0]
    if len(ws) == 1:
        return '%s, %s' % worst[:2]
    return '%s, %s (the lowest of %d windows over these words)' % (worst[0], worst[1], len(ws))


def main():
    his = his_texts()
    items = []
    for half in 'AB':
        r = json.loads((HERE / ('RESULT-%s.json' % half)).read_text(encoding='utf-8'))
        text = r['text']
        lines, secs = line_sections(text, payload_seq(half))
        starts, pos = [], 0
        for l in lines:
            starts.append(pos)
            pos += len(l) + 1
        for k, w in enumerate(r['windows']):
            if w['label'] == 'Human' and w['confidence'] == 'High':
                continue
            a, b = w['start'], w['end']
            span = text[a:b]
            core = span.strip()
            a2 = a + (len(span) - len(span.lstrip())) if core else a
            b2 = b - (len(span) - len(span.rstrip())) if core else b
            first = max(i for i, s in enumerate(starts) if s <= a2)
            last = max(i for i, s in enumerate(starts) if s < max(b2, a2 + 1))
            paras = []
            for i in range(first, last + 1):
                s, e = starts[i], starts[i] + len(lines[i])
                lo, hi = max(a, s) - s, min(b, e) - s
                paras.append({'line': i, 'before': lines[i][:lo], 'window': lines[i][lo:hi], 'after': lines[i][hi:]})
            items.append({
                'half': half, 'i': k, 'label': 'AI' if w['label'].startswith('AI') else 'Human', 'confidence': w['confidence'],
                'words': w['words'], 'ai_likelihood': w['ai_likelihood'], 'calibrated_confidence': w.get('calibrated_confidence'),
                'highlighted': w.get('uncertainty_highlighting'),
                'start': a, 'end': b, 'text': core, 'section': list(secs[first]), 'paragraphs': paras,
                'whose': whose(core, his) if len(core.split()) >= 3 else 'too short to say',
                'round6': round6(core), 'kind': 'seam' if w['words'] <= 3 else 'stretch'})
    for n, x in enumerate(items, 1):
        x['id'] = 'r8w%03d' % n
        x['round6_text'] = r6_text(x['round6'])
    (HERE / 'WINDOWS.json').write_text(json.dumps({
        'about': __doc__.split('\n\n')[0], 'halves': HALVES, 'round6': R6, 'items': items}, ensure_ascii=False, indent=1) + '\n',
        encoding='utf-8')
    cnt = {}
    for x in items:
        k = ('AI, ' if x['label'] == 'AI' else 'Human, ') + x['confidence']
        cnt[k] = cnt.get(k, 0) + 1
    out = ['# Round 8\'s stretches below Human with high confidence (turn 115)', '',
           'Round 8 is the whole guide as installed in turn 114, in the two temporary Substack drafts. Both halves read Human '
           'Written with High confidence overall ([half A](%s), [half B](%s)); these are the %d windows inside them that '
           'didn\'t, each beside what round 6 ([A](%s), [B](%s)) read for the same words. Every one is in [WINDOWS.json](%s) as '
           'well.' % (HALVES['A'], HALVES['B'], len(items), R6['A'], R6['B'], BRANCH + 'experiments/t115-results/WINDOWS.json'), '',
           '| | windows | words |', '|---|---|---|']
    for k in ('AI, Medium', 'AI, Low', 'Human, Low', 'Human, Medium'):
        if k in cnt:
            out.append('| %s | %d | %d |' % (k, cnt[k], sum(x['words'] for x in items if ('AI, ' if x['label'] == 'AI' else 'Human, ') + x['confidence'] == k)))
    seams = [x for x in items if x['kind'] == 'seam']
    out += ['', 'A window of three words or fewer is a seam between two stretches, where the detector changed its mind: '
            'it marks the place more than the words, so the %d seams are listed by section at the end.' % len(seams), '',
            '**Whose words:** "his" means every sentence of the window is in one of your texts recorded in the owner-edits file; '
            '"partly his" means some are; "not recorded as his" means none are, though some of your older text isn\'t recorded '
            'there. **Round 6** is what round 6 read for the same words.', '']
    groups = [('The AI windows', [x for x in items if x['label'] == 'AI']),
              ('Human, Low confidence', [x for x in items if x['label'] == 'Human' and x['confidence'] == 'Low']),
              ('Human, Medium confidence, more than three words', [x for x in items if x['label'] == 'Human' and x['confidence'] == 'Medium' and x['kind'] == 'stretch'])]
    for head, group in groups:
        if not group:
            continue
        out += ['## %s (%d)' % (head, len(group)), '']
        for x in group:
            sec = ' › '.join(x['section']) or '(the article\'s opening)'
            out += ['### %s. %s' % (x['id'], sec), '',
                    '**%s, %s confidence**, %d words, half %s. Round 6: %s. Whose words: %s.' % (
                        x['label'], x['confidence'], x['words'], x['half'], x['round6_text'], x['whose']), '']
            for p in x['paragraphs']:
                w = p['window'].strip()
                lead = p['window'][:len(p['window']) - len(p['window'].lstrip())]
                out += ['> ' + p['before'] + lead + ('**%s**' % w if w else '') + p['window'][len(lead) + len(w):] + p['after'], '']
    if seams:
        out += ['## The seams (%d)' % len(seams), '', '| id | section | label | words | the seam |', '|---|---|---|---|---|']
        for x in seams:
            out.append('| %s | %s | %s, %s | %d | %s |' % (x['id'], ' › '.join(x['section']) or '(opening)', x['label'], x['confidence'],
                                                         x['words'], (x['text'] or '(a line break)').replace('|', '/')))
        out.append('')
    (HERE / 'WINDOWS.md').write_text('\n'.join(out), encoding='utf-8')
    flips = [x['id'] for x in items if x['round6'] and x['label'] == 'AI']
    print('%d windows: %s; %d seams; no section for %s' % (len(items), ', '.join('%s %d' % kv for kv in sorted(cnt.items())),
                                                          len(seams), [x['id'] for x in items if not x['section']]))
    from collections import Counter
    print('round 6 for the same words:', Counter(x['round6_text'].split(' (')[0] for x in items))
    print('AI now, there in round 6:', flips)


if __name__ == '__main__':
    main()
