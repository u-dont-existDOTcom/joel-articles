#!/usr/bin/env python3
"""section_refs.py - after a reorganization, every mention of a section by name: is it before or after, and is it still there?

Lesson E338 (Inner Child). Joel reorganized the whole Inner Child guide himself (2026-11-03) and fixed most of the
pointers his moves broke: he cut "the way you did in Hear the Guard First" with the section, took "further down" off
Timing Is Individual once it came earlier, and wrote "further on" for the ones pointing ahead. A few slipped through,
among them "(as described in Noticing Counts)" in a section that now comes before Noticing Counts, and "my section, “meet
the protector first,”" after the section it meant was cut. A model reading 28,000 words misses these; exact strings
don't. This lists every place a paragraph names a section (a heading's words, two words or more), with which way the
section is and the pointer word next to the name, and flags:
  - a back pointer ("as described in", "back in", "earlier", "above", "we discussed", "remember") to a section that comes
    later, and a forward pointer ("further on", "further down", "below", "later", "coming up") to one that came before;
  - a section name from --previous (the version before the reorganization) that is no longer a heading.
The "that X" and "this X" whose X was in a paragraph that moved or went still need a reader: this only does the names.

  python3 tools/humanization/section_refs.py ARTICLE.md [--previous OLD.md] [--all]

Exit 0 when nothing is flagged, 1 when something is."""
import argparse
import pathlib
import re
import sys

BACK = re.compile(r'(as (?:we )?(?:described|discussed|mentioned) in|back in|as in|the same test as in|we discussed|earlier|above|remember)', re.I)
FORWARD = re.compile(r'(further on|further down|below|later on|later|coming up|ahead)', re.I)
HEAD = re.compile(r'^(#{1,6})\s+(.*\S)\s*$')


def plain(s):
    s = re.sub(r'\[([^\]]+)\]\s?\([^)]*\)', r'\1', s)
    s = re.sub(r'[*_`]', '', s)
    s = s.translate(str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"', ' ': ' ', '«': '"', '»': '"'}))
    return re.sub(r'\s+', ' ', s).strip()


def blocks(md):
    md = re.sub(r'<!--.*?-->', '', md, flags=re.S)
    out = []
    for b in re.split(r'\n\s*\n', md):
        b = b.strip()
        if not b:
            continue
        m = HEAD.match(b.split('\n')[0])
        if m and len(b.split('\n')) == 1:
            t = plain(m.group(2))
            if t:
                out.append(('h', t))
        else:
            out.append(('p', plain(b)))
    return out


def headings(md):
    return [t for k, t in blocks(md) if k == 'h']


def refs(md, previous=None):
    """[{'para': i, 'title', 'where': 'before'|'after'|'gone', 'pointer', 'flag', 'text'}] for each mention of a section."""
    bl = blocks(md)
    pos = {}
    for i, (k, t) in enumerate(bl):
        if k == 'h' and len(t.split()) >= 2:
            pos.setdefault(t.lower().rstrip(' !?.'), i)
    gone = []
    if previous:
        now = set(pos)
        cur = ' | '.join(now)
        # a title of three words or more that is no longer a heading, nor inside one (a renamed "The Parent You Inherited"
        # is now "Protecting from the Parent You Inherited"; "6. The Love Has to Move" kept its words)
        gone = sorted({t.lower().rstrip(' !?.') for t in headings(previous) if len(t.split()) >= 3} - now, key=len, reverse=True)
        gone = [g for g in gone if g not in cur]
    out = []
    for i, (k, t) in enumerate(bl):
        if k != 'p':
            continue
        low = t.lower()
        for title, j in sorted(pos.items(), key=lambda kv: -len(kv[0])):
            for m in re.finditer(re.escape(title), low):
                around = low[max(0, m.start() - 30):m.end() + 20]
                back, fwd = BACK.search(around), FORWARD.search(around)
                where = 'after' if j > i else 'before'
                flag = ''
                if back and where == 'after':
                    flag = 'points back ("%s") to a section that comes later' % back.group(1)
                elif fwd and where == 'before' and not back:
                    flag = 'points ahead ("%s") to a section that came before' % fwd.group(1)
                out.append({'para': i, 'title': title, 'where': where, 'pointer': (back or fwd).group(1) if (back or fwd) else '',
                            'flag': flag, 'text': t[max(0, m.start() - 60):m.end() + 40]})
        for title in gone:
            for m in re.finditer(re.escape(title), low):
                out.append({'para': i, 'title': title, 'where': 'gone', 'pointer': '', 'flag': 'names a section that is no longer a heading',
                            'text': t[max(0, m.start() - 60):m.end() + 40]})
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('article')
    ap.add_argument('--previous', help='the version before the reorganization')
    ap.add_argument('--all', action='store_true', help='list every mention, not only the flagged ones')
    a = ap.parse_args(argv)
    md = pathlib.Path(a.article).read_text(encoding='utf-8')
    prev = pathlib.Path(a.previous).read_text(encoding='utf-8') if a.previous else None
    rows = refs(md, prev)
    flagged = [r for r in rows if r['flag']]
    for r in (rows if a.all else flagged):
        print('%s paragraph %d, "%s" (%s%s): ...%s...' % ('FLAG' if r['flag'] else 'ok  ', r['para'], r['title'], r['where'],
              '; ' + r['flag'] if r['flag'] else '', r['text']))
    print('%d mentions of sections, %d flagged' % (len(rows), len(flagged)))
    return 1 if flagged else 0


if __name__ == '__main__':
    sys.exit(main())
