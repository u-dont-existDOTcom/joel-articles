#!/usr/bin/env python3
"""Turn 109: every stretch round 6 read below Human with high confidence, saved, by section (Joel, 2026-10-25 14:20 UTC:
"make sure you save all the sections that pangram marked as less than human high confidence.  we can try to fix those
as well").

Round 6 was the whole-article check of turn 107's two Substack drafts (experiments/t107-substack/PAYLOAD-A.html and -B.html),
read in turn 108 (experiments/t108-results/RESULT-A.json and -B.json: the page's windows and the checked text, whose
SHA-256 matched the page's). The checked text has no headings, so each of its lines is matched to its paragraph in the
payload, in order, for the headings above it.

For each window that isn't Human with High confidence it gives: its label, confidence and words; its section (the
headings above it); its paragraph with the window marked; whether its words are still in the article as it is now
(turn 109); and whether they are in a text recorded as his own in OWNER-EDITS.json (an entry whose id has "joel" in it).
That last field is an aid: some of his older text isn't recorded that way.

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
from paragraphs_alone import reader_blocks  # noqa: E402
from ptext import plain  # noqa: E402
from substack_check_text import smart  # noqa: E402

BRANCH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/'
HALVES = {'A': 'https://www.pangram.com/feed/41dfb451-494d-4a13-a76c-335d372dbd4a',
          'B': 'https://www.pangram.com/feed/64c71597-3987-48a7-8431-c8bdc70fddcc'}
STRAIGHT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'", '‍': None, '️': None})


def norm(s):
    return re.sub(r'\s+', ' ', s.translate(STRAIGHT)).strip()


def payload_seq(half):
    """[(heading path, paragraph text)] in the payload's order."""
    raw = (ART / ('experiments/t107-substack/PAYLOAD-%s.html' % half)).read_text(encoding='utf-8')
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
    """For each line of the checked text, the heading path of its paragraph in the payload (matched in order)."""
    lines = text.split('\n')
    out, k = [], 0
    for line in lines:
        n = norm(line)
        hit = next((j for j in range(k, min(k + 6, len(seq))) if norm(seq[j][1]) == n), None)
        if hit is None and n:
            hit = next((j for j in range(k, min(k + 6, len(seq))) if norm(seq[j][1])[:50] == n[:50]), None)
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


def current_text():
    md = re.sub(r'<!--.*?-->', '', (ART / 'HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8'), flags=re.S)
    return norm(' '.join(smart(plain(re.sub(r'^#+\s*', '', b))) for _, b in reader_blocks(md)))


def main():
    his, now = his_texts(), current_text()
    items = []
    for half in 'AB':
        r = json.loads((ART / ('experiments/t108-results/RESULT-%s.json' % half)).read_text(encoding='utf-8'))
        text = r['text']
        lines, secs = line_sections(text, payload_seq(half))
        starts, pos = [], 0
        for l in lines:
            starts.append(pos)
            pos += len(l) + 1
        for w in r['windows']:
            if w['label'] == 'Human' and w['confidence'] == 'High':
                continue
            a, b = w['start'], w['end']
            span = text[a:b]
            core = span.strip()
            # the lines the window's words are on (a window can start on the line break before its first word)
            a2 = a + (len(span) - len(span.lstrip())) if core else a
            b2 = b - (len(span) - len(span.rstrip())) if core else b
            first = max(i for i, s in enumerate(starts) if s <= a2)
            last = max(i for i, s in enumerate(starts) if s < max(b2, a2 + 1))
            paras = []
            for i in range(first, last + 1):
                s, e = starts[i], starts[i] + len(lines[i])
                lo, hi = max(a, s) - s, min(b, e) - s
                paras.append({'before': lines[i][:lo], 'window': lines[i][lo:hi], 'after': lines[i][hi:]})
            items.append({
                'half': half, 'label': 'AI' if w['label'].startswith('AI') else 'Human', 'confidence': w['confidence'],
                'words': w['words'], 'ai_likelihood': w['ai_likelihood'], 'calibrated_confidence': w.get('calibrated_confidence'),
                'start': a, 'end': b, 'text': core, 'section': list(secs[first]),
                'paragraphs': paras, 'still_in_article': bool(core) and norm(core) in now,
                'whose': whose(core, his) if len(core.split()) >= 3 else 'too short to say',
                'kind': 'seam' if w['words'] <= 3 else 'stretch'})
    order = {'AI': 0, 'Low': 1, 'Medium': 2}
    for n, x in enumerate(items, 1):
        x['id'] = 'w%03d' % n
    (HERE / 'WINDOWS.json').write_text(json.dumps({
        'about': __doc__.split('\n\n')[0], 'halves': HALVES, 'items': items}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

    def rank(x):
        return order['AI'] if x['label'] == 'AI' else order[x['confidence']]

    cnt = {}
    for x in items:
        k = ('AI, ' if x['label'] == 'AI' else 'Human, ') + x['confidence']
        cnt[k] = cnt.get(k, 0) + 1
    out = ['# Round 6\'s stretches below Human with high confidence (saved in turn 109)', '',
           'You asked to save every place the last whole-article check, round 6, marked as less than Human with high confidence, '
           'so we can fix those too. Both halves read Human Written with High confidence overall ([half A](%s), [half B](%s)); '
           'these are the %d windows inside them that didn\'t. Every one is in [WINDOWS.json](%s) as well.' % (
               HALVES['A'], HALVES['B'], len(items), BRANCH + 'experiments/t109-windows/WINDOWS.json'), '',
           '| | windows | words |', '|---|---|---|']
    for k in ('AI, Medium', 'AI, Low', 'Human, Low', 'Human, Medium'):
        if k in cnt:
            out.append('| %s | %d | %d |' % (k, cnt[k], sum(x['words'] for x in items if ('AI, ' if x['label'] == 'AI' else 'Human, ') + x['confidence'] == k)))
    seams = [x for x in items if x['kind'] == 'seam']
    out += ['', 'A window of three words or fewer is a seam between two stretches, where the detector changed its mind: '
            'it marks the place more than the words, so the %d seams are listed by section at the end.' % len(seams), '',
            '**Whose words:** "his" means every sentence of the window is in one of your texts recorded in the owner-edits file; '
            '"partly his" means some are; "not recorded as his" means none are, though some of your older text isn\'t recorded '
            'there. **Still in the article** says whether the window\'s words are still there as they were; where they changed '
            'since round 6 (your turn-109 rewrites, say), the next whole-article check reads the new words.', '']
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
                    '**%s, %s confidence**, %d words, half %s. %s. Whose words: %s.' % (
                        x['label'], x['confidence'], x['words'], x['half'],
                        'Still in the article' if x['still_in_article'] else 'Changed since round 6', x['whose']), '']
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
    print('%d windows: %s; %d seams; %d no longer in the article as they were' % (
        len(items), ', '.join('%s %d' % kv for kv in sorted(cnt.items())), len(seams), sum(not x['still_in_article'] for x in items)))
    unmatched = [x['id'] for x in items if not x['section']]
    if unmatched:
        print('no section found for', unmatched)


if __name__ == '__main__':
    main()
