#!/usr/bin/env python3
"""toc_check.py - before a contents goes to Joel: every heading that repeats the one before it or its parent, and every
heading a contents reader marked as hard, has a fate.

Lesson bad-trips-2026-11-21a. Joel, 2026-11-21 13:04 UTC, after round 47's headings page for the bad trips guide: "learn
lessons. why would you put 2 serotonin syndrome headings in a row". The pick had "Serotonin Syndrome (SS)?" with "Is It
Serotonin Toxicity?" right under it, then "Do This Immediately"; in the sidebar the parent's own text doesn't show, so a
reader sees the same question twice. Both readers of the pick had said so ("It also sits next to line 14, 'Is It
Serotonin Toxicity?', which sounds like the same thing"), and the page went out anyway: their notes came back only in
the chat, and nothing made each one get a fate.

So the readers' hard headings are written into their read files ("HARD: <line number> | <why>", the brief in
docs/FIXING-AN-ARTICLE.md, section 3), and this lists, for one contents:
  - repeat: a heading that shares a content word with its parent or with the heading just before it in the sidebar
    (code finds the candidates; whether it really says the same thing is a reader's call, so each gets a fate);
  - hard: a heading a reader of this contents marked HARD.
With --fates, it fails until every one of them has a fate: "changed: ..." or "kept: why it stays" (a child naming its
own part of the parent's topic, "Active Seizure" > "What Else Helps", is a kept with that reason).

  python3 tools/humanization/toc_check.py CONTENTS.json [--reads DIR --name NAME] [--fates FATES.json]
CONTENTS.json is [{"id", "level", "heading"}, ...] in order; DIR holds READ-<NAME>-<k>.txt (or HARD-<NAME>-<k>.txt) and
LINES-<NAME>.json ([{"n", "id"}]) maps a read's line numbers to section ids.
"""
import argparse, glob, json, os, re, sys

STOP = set('''a an the and or but nor of to in on at by for from with as into onto about over under after before
your you my me i we our it its it's this that these those is are was be been being do does did done if when what how
why who whom which where while than then so not no yes get got some any all one two up off out more most less very
too just only also can could would should will may might must let lets here there their them they he she his her
vs versus & + = ≠'''.split())


def words(heading):
    t = re.sub(r"[“”\"'’()\[\]:;,.!?…/]", ' ', heading.lower())
    out = set()
    for w in t.split():
        w = w.strip('-')
        if len(w) < 3 or w in STOP:
            continue
        if w.endswith('ies') and len(w) > 5:
            w = w[:-3] + 'y'
        elif w.endswith('s') and not w.endswith('ss') and len(w) > 4:
            w = w[:-1]
        out.add(w)
    return out


def repeats(entries):
    """[(id, kind, other_id, shared words)]: kind is 'parent' or 'previous'."""
    found, stack, prev = [], [], None
    for e in entries:
        while stack and stack[-1]['level'] >= e['level']:
            stack.pop()
        parent = stack[-1] if stack else None
        w = words(e['heading'])
        seen = set()
        for kind, other in (('parent', parent), ('previous', prev)):
            if other is None or other['id'] in seen:
                continue
            shared = w & words(other['heading'])
            if shared:
                found.append((e['id'], kind, other['id'], sorted(shared)))
                seen.add(other['id'])
        stack.append(e)
        prev = e
    return found


def hard(reads_dir, name):
    """{section id: [why, ...]} from the HARD lines of every read of contents NAME."""
    path = os.path.join(reads_dir, 'LINES-%s.json' % name)
    if not os.path.exists(path):   # beside the reads, or one folder up beside the contents files
        path = os.path.join(os.path.dirname(os.path.abspath(reads_dir)), 'LINES-%s.json' % name)
    lines = {x['n']: x['id'] for x in json.load(open(path, encoding='utf-8'))}
    out = {}
    files = glob.glob(os.path.join(reads_dir, 'READ-%s-*.txt' % name)) + glob.glob(os.path.join(reads_dir, 'HARD-%s-*.txt' % name))
    for f in sorted(files):
        for line in open(f, encoding='utf-8'):
            m = re.match(r'\s*HARD:\s*(\d+)\s*\|\s*(.*)$', line)
            if m and int(m.group(1)) in lines:
                out.setdefault(lines[int(m.group(1))], []).append(m.group(2).strip())
    return out


def check(entries, hard_ids=None, fates=None):
    """(lines, missing): every candidate, and the keys ("repeat:<id>", "hard:<id>") with no fate."""
    by = {e['id']: e for e in entries}
    lines, keys = [], []
    for i, kind, other, shared in repeats(entries):
        k = 'repeat:%s' % i
        keys.append(k)
        lines.append('%s  "%s" shares %s with its %s "%s"' % (k, by[i]['heading'], ', '.join(shared), kind, by[other]['heading']))
    for i, whys in sorted((hard_ids or {}).items()):
        k = 'hard:%s' % i
        keys.append(k)
        lines.append('%s  "%s": %s' % (k, by[i]['heading'] if i in by else i, ' / '.join(whys)))
    missing = []
    if fates is not None:
        for k in dict.fromkeys(keys):
            f = (fates.get(k) or '').strip()
            if not re.match(r'^(changed|kept)\s*:\s*\S.{8,}', f, re.I):
                missing.append(k)
    return lines, missing


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('contents')
    ap.add_argument('--reads')
    ap.add_argument('--name')
    ap.add_argument('--fates')
    a = ap.parse_args(argv)
    entries = json.load(open(a.contents, encoding='utf-8'))
    h = hard(a.reads, a.name) if a.reads and a.name else {}
    fates = json.load(open(a.fates, encoding='utf-8')) if a.fates else None
    lines, missing = check(entries, h, fates)
    for l in lines:
        print(l)
    if fates is None:
        print('%d to give a fate (repeats and hard headings)' % len(lines))
        return 0
    for k in missing:
        print('NO FATE: %s ("changed: ..." or "kept: why it stays")' % k)
    print('verdict: %s' % ('PASS' if not missing else 'FAIL'))
    return 0 if not missing else 1


if __name__ == '__main__':
    sys.exit(main())
