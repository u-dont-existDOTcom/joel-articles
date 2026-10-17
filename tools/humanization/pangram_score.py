"""pangram_score.py - fill a batch's "(pending)" PREDICTIONS.md rows from what its OUT-read.js returned.

Usage (from the repo root):
  python3 tools/humanization/pangram_score.py READ.json articles/X/tools/PREDICTIONS.md

READ.json is the reader's object ({key: {headline, avg_ai_likelihood, words, windows, utc, link}}); fields it
doesn't use may be left out. A result may also be the short list [headline, avg, words, windows, utc, uuid].
Each row whose "[key]" is in READ.json and still says "(pending)" gets the result, the check's UTC time and
link, and hit or miss against the row's prediction. It prints one line per result.

2026-10-17 (turn 65): Joel asked for twelve hours of work done as fast as I can ("keep optimizing your approach");
until now each batch's rows were scored by typing every result into a script by hand.
"""
import json
import pathlib
import re
import sys


def num(x):
    return '%.3f' % x if x < 0.01 else '%.2g' % x


def result(r):
    """The result cell: the headline, the AI likelihood, the confidence (or the windows that aren't Human) and the
    word count, as the rows are written by hand."""
    wins = [w.split(', ') for w in r.get('windows') or []]
    avg = num(float(r['avg_ai_likelihood']))
    if len(wins) <= 1:
        conf = wins[0][1] if wins and len(wins[0]) > 1 else '?'
        return '%s (%s, %s; %s)' % (r['headline'], avg, conf, r['words'])
    other = [w for w in wins if w[0] != 'Human']
    tail = (': %s' % ', '.join('%s %s words (%s)' % (w[0], w[2], w[1]) for w in other)) if other else ''
    return '%s (%s; %s), %d windows%s' % (r['headline'], avg, r['words'], len(wins), tail)


def hit(prediction, headline):
    p = prediction.strip().split()[0].strip(',').lower() if prediction.strip() else ''
    h = headline.lower()
    if p == 'human':
        return 'hit' if 'human' in h else 'miss'
    if p == 'ai':
        return 'hit' if 'ai' in h.split() or h.startswith('ai') else 'miss'
    return '?'


def expand(v):
    """A result as the reader gives it, or in the short form [headline, avg, words, windows, utc, uuid] that the
    browser call can return so that less has to be copied (turn 65)."""
    if isinstance(v, dict):
        return v
    h, avg, words, wins, utc, uuid = v
    return {'headline': h, 'avg_ai_likelihood': avg, 'words': words, 'windows': wins, 'utc': utc,
            'link': uuid if uuid.startswith('http') else 'https://www.pangram.com/history/' + uuid}


def score(read, lines):
    """READ: the reader's object. LINES: PREDICTIONS.md's lines. Returns (new lines, [(key, cell, hit)])."""
    done = []
    out = list(lines)
    for i, ln in enumerate(out):
        m = re.search(r'\[([A-Za-z0-9_]+)\]', ln)
        if not m or m.group(1) not in read or '(pending) | |' not in ln:
            continue
        k = m.group(1)
        r = read[k]
        cells = ln.split(' | ')
        pred = cells[2] if len(cells) > 2 else ''
        t = (r.get('utc') or '')[11:19]
        cell = result(r)
        h = hit(pred, r['headline'])
        out[i] = ln.replace('(pending) | |', '%s; %s UTC, %s | %s |' % (cell, t, r['link'], h))
        done.append((k, cell, h))
    return out, done


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 2:
        sys.exit(__doc__)
    raw = pathlib.Path(argv[0]).read_text(encoding='utf-8')
    read = json.loads(raw)
    if isinstance(read, str):  # the reader returns JSON text, and the browser tool may wrap it once more
        read = json.loads(read)
    read = {k: expand(v) for k, v in read.items()}
    p = pathlib.Path(argv[1])
    lines, done = score(read, p.read_text(encoding='utf-8').rstrip('\n').split('\n'))
    p.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    for k, cell, h in done:
        print('%-22s %-4s %s' % (k, h, cell))
    missing = sorted(set(read) - {k for k, _, _ in done})
    if missing:
        print('no pending row for: ' + ', '.join(missing), file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main())
