#!/usr/bin/env python3
"""Split joel-articles' rule documents into units and pack them into batches for the rules audit (2026-11-27).

  python3 -I extract_rules.py REPO_DIR COMMIT OUT_DIR [--memory FILE]

Reads every rule document at COMMIT (git show), strips link targets (keeps link text), splits each file at headings and
top-level bullets or numbered items, and packs whole units, in file order, into batches of about LIMIT characters.
Writes OUT_DIR/batches/Bnn.md and OUT_DIR/units.json (unit id, file, batch, first line).
"""
import json
import pathlib
import re
import subprocess
import sys

LIMIT = 52000

ORDER = [
    'AGENTS.md',
    'SKILL.md',
    'tools/humanization/his_fixes_brief.md',
    'tools/humanization/fit_read_brief.md',
    'tools/humanization/needed_read_brief.md',
    'tools/humanization/human_tells.md',
    'tools/humanization/meaning_check_brief.md',
    'tools/humanization/reader_moment_brief.md',
    'tools/humanization/sense_read_brief.md',
    'tools/humanization/headings_brief.md',
    'tools/humanization/contents_order_brief.md',
    'docs/FIXING-AN-ARTICLE.md',
    'docs/MAKING-SENSE.md',
    'docs/CLARITY-READ.md',
    'docs/PANGRAM-PRODUCTION-BUDGET-20261020.md',
    'docs/EDITORIAL-SCOPE-AND-PLACEMENT.md',
    'docs/HUMANIZATION-PRESERVATION-GATE.md',
    'docs/HUMANIZATION-ARCHITECTURE-GATE.md',
    'docs/HUMANIZATION-OWNER-DELIVERY-GATE.md',
    'docs/HUMANIZATION-FRESH-CRITIC-GATE.md',
    'docs/HUMANIZATION-COLD-AUDIT-GATE.md',
    'docs/HUMANIZATION-KNOWN-GREEN-CALIBRATION.md',
    'docs/HUMANIZATION-SOURCE-INTEGRITY-GATE.md',
    'docs/HUMANIZATION-TELL-INVENTORY.md',
    'docs/REVIEW-MOVE-INLINE-DIFF-GATE.md',
    'docs/SUBSTACK-HELPER-DELIVERY-GATE.md',
    'docs/READER-QUESTION-AUDIT.md',
    'docs/SUPERVISED-WRITING-ARCHITECTURE.md',
    'docs/EMULATE-FALLBACK.md',
    'docs/INDEX.md',
]


def git_show(repo, commit, path):
    return subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (commit, path)], capture_output=True, text=True,
                          check=True).stdout


def git_ls(repo, commit, prefix):
    out = subprocess.run(['git', '-C', repo, 'ls-tree', '--name-only', commit, prefix], capture_output=True, text=True,
                         check=True).stdout.split()
    return sorted(out)


def strip_links(t):
    t = re.sub(r'\[([^\]]+)\]\((?:[^()]|\([^)]*\))*\)', r'\1', t)
    t = re.sub(r'https?://\S+', '<link>', t)
    return t


START = re.compile(r'^(#{1,4} |- \*\*|\d{1,3}\. \*\*|\*\*[A-Z])')


def split_units(path, text):
    """Units: a heading's own lines up to its first bullet, then each top-level bullet or numbered item with the lines
    that continue it (indented, or not starting a new unit)."""
    units, cur, heading = [], [], ''
    for line in text.split('\n'):
        if START.match(line) and cur:
            units.append((heading, '\n'.join(cur).strip()))
            cur = []
        if line.startswith('#'):
            heading = line.lstrip('#').strip()
        cur.append(line)
    if cur:
        units.append((heading, '\n'.join(cur).strip()))
    out = []
    for n, (h, u) in enumerate(units, 1):
        if not u:
            continue
        m = re.match(r'^(?:- |\d{1,3}\. )?\*\*([a-z-]+-20\d\d-\d\d-\d\d[a-z]+|E\d{1,3}(?: \([a-z-]+\))?)\b', u)
        if m:
            uid = m.group(1)
        else:
            m2 = re.match(r'^(\d{1,3})\. \*\*', u)
            if m2 and path.endswith('his_fixes_brief.md'):
                uid = 'his_fixes_brief way %s' % m2.group(1)
            else:
                uid = '%s unit %d' % (path, n)
        out.append({'id': uid, 'file': path, 'heading': h, 'text': strip_links(u)})
    return out


def tells_units(repo, commit):
    d = json.loads(git_show(repo, commit, 'tools/humanization/tells_registry.json'))
    out = []
    for t in d['tells']:
        src = '; '.join('%s: "%s"' % (s.get('file', ''), s.get('quote', '')) for s in t.get('sources', []))
        line = '%s (%s): %s | sources: %s' % (t['id'], t.get('kind', ''), t.get('tell', ''), src)
        if t.get('rule'):
            line += ' | linter rule: %s' % t['rule']
        if t.get('reason'):
            line += ' | why a reader: %s' % t['reason']
        out.append({'id': 'tell ' + t['id'], 'file': 'tools/humanization/tells_registry.json', 'heading': 'tells',
                    'text': strip_links(line)})
    return out


def main():
    repo, commit, outdir = sys.argv[1], sys.argv[2], pathlib.Path(sys.argv[3])
    memory = sys.argv[sys.argv.index('--memory') + 1] if '--memory' in sys.argv else None
    units = []
    if memory:
        for n, line in enumerate(pathlib.Path(memory).read_text(encoding='utf-8').split('\n'), 1):
            if line.startswith('- [stated]'):
                units.append({'id': 'memory preferences line %d' % n, 'file': 'memory: /preferences.md (project)',
                              'heading': 'his saved preferences', 'text': line})
    for p in ORDER:
        units += split_units(p, git_show(repo, commit, p))
    for p in git_ls(repo, commit, 'docs/lessons/'):
        if p.endswith('README.md'):
            continue
        units += split_units(p, git_show(repo, commit, p))
    units += split_units('docs/HUMANIZATION-GATE.md', git_show(repo, commit, 'docs/HUMANIZATION-GATE.md'))
    units += tells_units(repo, commit)
    # pack, never splitting a unit and never mixing files mid-unit
    batches, cur, size = [], [], 0
    for u in units:
        block = '\n[%s | %s]\n%s\n' % (u['id'], u['file'], u['text'])
        if cur and size + len(block) > LIMIT:
            batches.append(cur)
            cur, size = [], 0
        cur.append((u, block))
        size += len(block)
    if cur:
        batches.append(cur)
    (outdir / 'batches').mkdir(parents=True, exist_ok=True)
    index = []
    for i, b in enumerate(batches, 1):
        name = 'B%02d' % i
        files = []
        for u, _ in b:
            if u['file'] not in files:
                files.append(u['file'])
        head = '# Rules audit batch %s (joel-articles at %s)\n\nFiles: %s\n' % (name, commit[:8], ', '.join(files))
        (outdir / 'batches' / (name + '.md')).write_text(head + ''.join(bl for _, bl in b), encoding='utf-8')
        for u, _ in b:
            index.append({'id': u['id'], 'file': u['file'], 'batch': name, 'first': u['text'][:160]})
    (outdir / 'units.json').write_text(json.dumps(index, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(units), 'units in', len(batches), 'batches')
    for i, b in enumerate(batches, 1):
        print('B%02d' % i, sum(len(bl) for _, bl in b), 'chars', len(b), 'units', b[0][0]['id'][:50], '...',
              b[-1][0]['id'][:50])


if __name__ == '__main__':
    main()
