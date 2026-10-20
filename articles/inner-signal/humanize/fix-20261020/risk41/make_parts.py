"""The hypnosis guide as it stands (HUMANIZED-SO-FAR.md, 2026-10-20) in parts of at most about 1,800 words, for the Pangram
4.1 risk read (tools/humanization/pangram41_risk_prompt.py). HTML comments and images are dropped, links kept as their words.
Whole h1 sections go together while they fit; a longer section is cut at its h2 headings, or between paragraphs, and each
piece after the first repeats the h1 heading with "(continued)".

The first run (four parts of about 6,800 words, 2026-10-20) failed: each of the four Sonnet readers spent its whole output
on reasoning through the part, hit the output limit, and started over until it was stopped, writing nothing. Parts this
size leave room for the reasoning and the report.

Run from the repo root: python3 articles/inner-signal/humanize/fix-20261020/risk41/make_parts.py"""
import pathlib, re, subprocess, sys

CAP = 1800
H = pathlib.Path(__file__).resolve().parents[2]
REPO = H.parents[2]
OUT = pathlib.Path(__file__).resolve().parent
md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
md = re.sub(r'<!--.*?-->', '', md, flags=re.S)
md = re.sub(r'^>?\s*\[image \d+\]\([^)]*\)\s*$', '', md, flags=re.M)   # image markers
md = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', md)                           # images
md = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', md)                       # links as their words
words = lambda t: len(t.split())


def split_on(text, pattern):
    """Pieces of text, each starting at a line that matches pattern (the first piece is what comes before)."""
    out, cur = [], []
    for line in text.split('\n'):
        if re.match(pattern, line) and cur:
            out.append('\n'.join(cur).strip()); cur = []
        cur.append(line)
    out.append('\n'.join(cur).strip())
    return [p for p in out if p]


def pieces(section):
    """A section in pieces of at most CAP words: at its h2 headings, then between paragraphs."""
    if words(section) <= CAP:
        return [section]
    head = section.split('\n')[0]
    units = []
    for sub in split_on(section, r'^## '):
        if words(sub) <= CAP:
            units.append(sub)
        else:
            units += [p for p in re.split(r'\n\s*\n', sub) if p.strip()]
    out, cur = [], []
    for u in units:
        if cur and words('\n\n'.join(cur + [u])) > CAP:
            out.append('\n\n'.join(cur)); cur = []
        cur.append(u)
    out.append('\n\n'.join(cur))
    return [out[0]] + ['%s (continued)\n\n%s' % (head, p) for p in out[1:]]


secs = [p for s in split_on(md, r'^# ') for p in pieces(s)]
parts, cur = [], []
for s in secs:
    if cur and words('\n\n'.join(cur + [s])) > CAP:
        parts.append(cur); cur = []
    cur.append(s)
parts.append(cur)
for old in list(OUT.glob('part*.md')) + list(OUT.glob('PROMPT-*.txt')):
    old.unlink()
for i, p in enumerate(parts, start=1):
    f = OUT / ('part%02d.md' % i)
    f.write_text('\n\n'.join(p) + '\n', encoding='utf-8')
    subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram41_risk_prompt.py'), str(f),
                    str(OUT / ('PROMPT-%02d.txt' % i)), '--report', str(OUT / ('RISK-%02d.md' % i)),
                    '--what', 'the hypnosis guide ("The Inner Signal" self-hypnosis guide), part %d of %d' % (i, len(parts))],
                   check=True, capture_output=True)
    print(f.name, len(p), 'pieces', words('\n\n'.join(p)), 'words;', p[0].split('\n')[0][:60])
print(sum(words(s) for s in secs), 'words in', len(secs), 'pieces,', len(parts), 'parts')
