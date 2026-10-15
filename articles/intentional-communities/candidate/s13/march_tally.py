"""march_tally.py - how often each sentence was a break across march readings (2026-10-15).

Reads MARCH-PROMPT.txt (lines "T7: [1] ... [2] ...") and MARCH-labels-a.txt / -b.txt ("T7: S B S") from each review
folder named, and prints every sentence that was a break (B) at least once: breaks/readings, the sentence, and each
reading's label. A sentence that was a break in every reading it appeared in holds; one that flips is noise.

  python3 march_tally.py review-r5 review-r6 review-r7 review-r8 review-r9      # from s13/
"""
import collections, pathlib, re, sys


def tally(dirs):
    rows = collections.defaultdict(list)
    for d in dirs:
        p = pathlib.Path(d)
        prompt = p / 'MARCH-PROMPT.txt'
        if not prompt.exists():
            continue
        sents = {}
        for line in prompt.read_text(encoding='utf-8').splitlines():
            m = re.match(r'^(T\d+): (\[1\].*)$', line)
            if m:
                parts = re.split(r'\[(\d+)\] ', m.group(2))[1:]
                sents[m.group(1)] = [parts[i + 1].strip() for i in range(0, len(parts), 2)]
        for lab in 'ab':
            f = p / ('MARCH-labels-%s.txt' % lab)
            if not f.exists():
                continue
            for line in f.read_text(encoding='utf-8').splitlines():
                m = re.match(r'^(T\d+): (.*)$', line.strip())
                if not m or m.group(1) not in sents:
                    continue
                labs, ss = m.group(2).split(), sents[m.group(1)]
                if len(labs) != len(ss):
                    continue
                for s, l in zip(ss, labs):
                    rows[s].append((p.name.replace('review-', '') + lab, l))
    return rows


if __name__ == '__main__':
    rows = tally(sys.argv[1:])
    out = [(sum(l == 'B' for _, l in v), len(v), s, v) for s, v in rows.items()]
    for nb, n, s, v in sorted((x for x in out if x[0]), key=lambda x: (x[0] / x[1], x[1])):
        print('%d/%d | %s | %s' % (nb, n, s[:100], ' '.join('%s:%s' % x for x in v)))
