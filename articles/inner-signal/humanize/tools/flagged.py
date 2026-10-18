"""flagged.py - which paragraphs of a checked text fall inside the windows Pangram didn't read as Human (2026-10-18).

The in-page reader (tools/humanization/pangram_page_helpers.js, __readC) gives, for every window that isn't Human, its label,
its word count and its words, cut from the checked text after a blank line became one newline (Pangram's window indexes
count it that way). This finds each window's words in the checked text and names the blocks (paragraphs, list items,
quotes: whatever the text joined with a blank line) it covers.

  python3 tools/flagged.py DRAFTS.json RESULTS.json [--out FLAGS.json]

A block is flagged when a window covers at least 12 of its words or a third of them. A window whose words can't be found
(the reader cut it short with "…") is matched on its first 30 characters and its word count.
"""
import argparse, json, re, sys


def norm(t):
    return re.sub(r'\n{2,}', '\n', t)


def spans(text):
    """[(start, end, block_text)] of each blank-line block in norm(text)."""
    out, pos = [], 0
    n = norm(text)
    for b in re.split(r'\n\s*\n', text):
        b = b.strip('\n')
        if not b:
            continue
        i = n.index(b, pos)
        out.append((i, i + len(b), b))
        pos = i + len(b)
    return out


def window_span(n, w):
    """(start, end) of a flagged window's words in the normalized text, or None."""
    m = re.match(r'^(.*?) \((\d+) words\): (.*)$', w, flags=re.S)
    if not m:
        return None
    words, body = int(m.group(2)), m.group(3)
    if body.endswith('…'):
        head = body[:-1].strip()[:30]
        i = n.find(head)
        if i < 0:
            return None
        # walk forward the window's word count
        j, k = i, 0
        for mm in re.finditer(r'\S+', n[i:]):
            k += 1
            j = i + mm.end()
            if k >= words:
                break
        return i, j
    body = body.strip()
    i = n.find(body)
    return (i, i + len(body)) if i >= 0 else None


def flags(text, flagged):
    n = norm(text)
    sp = spans(text)
    out = []
    for w in flagged:
        ws = window_span(n, w)
        if ws is None:
            out.append({'window': w[:80], 'blocks': None})
            continue
        a, b = ws
        hit = []
        for k, (s, e, blk) in enumerate(sp):
            lo, hi = max(a, s), min(b, e)
            if hi <= lo:
                continue
            inside = len(n[lo:hi].split())
            total = len(blk.split())
            if inside >= 12 or inside * 3 >= total:
                hit.append(k)
        out.append({'window': w.split(':')[0], 'blocks': hit})
    return sp, out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('drafts')
    ap.add_argument('results')
    ap.add_argument('--out')
    a = ap.parse_args()
    drafts = json.load(open(a.drafts, encoding='utf-8'))
    res = json.load(open(a.results, encoding='utf-8'))
    report = {}
    for k, text in drafts.items():
        if k not in res:
            continue
        head, ai, words, windows, t, tail, flagged = res[k]
        if flagged and flagged[0].startswith('(every window AI'):
            sp, fl = spans(text), []
            blocks = list(range(len(sp)))
        else:
            sp, fl = flags(text, flagged)
            blocks = sorted({b for f in fl for b in (f['blocks'] or [])})
        report[k] = {'headline': head, 'ai': ai, 'words': words, 'windows': windows, 'link': 'https://www.pangram.com/history' + tail,
                     'n_blocks': len(sp), 'flagged_blocks': blocks, 'unmatched': [f['window'] for f in fl if f['blocks'] is None],
                     'flagged_words': sum(len(sp[b][2].split()) for b in blocks)}
        print('%-9s %-22s ai %.2f  %4d words  flagged blocks %d/%d (%d words)%s' % (
            k, head, ai, words, len(blocks), len(sp), report[k]['flagged_words'],
            '  UNMATCHED %d' % len(report[k]['unmatched']) if report[k]['unmatched'] else ''))
    if a.out:
        json.dump(report, open(a.out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    sys.exit(main())
