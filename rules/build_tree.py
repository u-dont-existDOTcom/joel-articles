#!/usr/bin/env python3
"""build_tree.py - the rule tree: one place for every rule, its checks, and the views made from it.

Joel, 2026-11-28 10:25 UTC: "i also feel like there are a lot of rules that are overlapping and there's not very good
organization of the rules like you should have some kind of rule tree ... there should be a human view of the rule tree
where everything makes sense, maybe with graphical links". The shape: rules/BRAINSTORM.md.

  python3 rules/build_tree.py            check rules/TREE.md and write rules/tree.json, rules/README.md, rules/view/index.html
  python3 rules/build_tree.py --check    check only; exit 1 on a problem

rules/TREE.md is the source. A branch is "## N Title", a group "### N.M Title", a rule "#### R-slug | Title" followed by
fields, each a line "- **Label:** text" (a field may run on over indented lines). "<!-- include: his_fixes_ways -->" brings
in the ways of tools/humanization/his_fixes_brief.md as rules of their group. "## Words" holds the glossary, one
"- **term:** meaning" a line.

Problems (exit 1 with --check): two rules with one id; a rule with no "Rule" or no "Why" and no "Record"; a link to an id
that doesn't exist; a "conflicts with" link (two rules that contradict can't both stand: settle it, or mark it "open
question" in Status); a stage that isn't one of STAGES. Notes (printed, written to rules/CHECKS.md): a quote of his in
"Why" that no file of the repository holds word for word (it may come from his saved preferences or a chat, or it may be
misquoted: look).
"""
import argparse
import datetime
import hashlib
import html
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent
TREE = HERE / 'TREE.md'
CHECKED = HERE / 'QUOTES-CHECKED.md'
WAYS = REPO / 'tools' / 'humanization' / 'his_fixes_brief.md'
STAGES = ['start', 'sense', 'humanize', 'check', 'show', 'record']
STAGE_NAMES = {'start': 'Starting an article', 'sense': 'Making it make sense', 'humanize': 'Humanizing',
               'check': 'Checking in Pangram', 'show': 'Showing Joel', 'record': 'Recording'}
RELATIONS = {'builds on': 'builds on', 'goes with': 'goes with', 'comes before': 'comes before',
             'comes after': 'comes after', 'replaces': 'replaces', 'conflicts with': 'conflicts with'}
GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
VIEW_URL = 'https://claude.ai/artifact/'  # the published view's link is filled in README by --view-url

FIELD = re.compile(r'^\s*[-*]\s+\*\*([A-Za-z ]+?):\*\*\s*(.*)$')
RULE_H = re.compile(r'^####\s+(R-[a-z0-9-]+)\s*\|\s*(.+?)\s*$')
GROUP_H = re.compile(r'^###\s+(\d+\.\d+)\s+(.+?)\s*$')
BRANCH_H = re.compile(r'^##\s+(\d+)\s+(.+?)\s*$')
WORDS_H = re.compile(r'^##\s+Words\s*$')
INCLUDE = re.compile(r'^<!--\s*include:\s*his_fixes_ways\s*-->\s*$')
QUOTE = re.compile(r'"([^"]{20,})"')


def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip().lower()


def ways():
    """The ways of the read against his fixes, as rules: "N. **Title.** text"."""
    text = WAYS.read_text(encoding='utf-8')
    out = []
    for m in re.finditer(r'^(\d{1,2})\. \*\*(.+?)\*\*(.*?)(?=^\d{1,2}\. \*\*|^\S|\Z)', text, re.M | re.S):
        n, title, body = int(m.group(1)), m.group(2).strip().rstrip('.'), re.sub(r'\s+', ' ', m.group(3)).strip()
        first = re.split(r'(?<=[.!?])\s+(?=[A-Z])', body)
        rule = ' '.join(first[:2])[:600]
        out.append({'id': 'R-way-%02d' % n, 'title': title, 'fields': {
            'Rule': rule,
            'Why': 'From his fixes: the read against his fixes, way %d, with his words and examples there.' % n,
            'Checked by': 'judgment: a fresh reader with the read against his fixes marks it before a check',
            'Stages': 'sense, humanize',
            'Replaces': 'tools/humanization/his_fixes_brief.md, way %d' % n,
            'Status': 'active',
            'Record': 'way %d of the read against his fixes (the full text, his words and examples: %s%s)' % (
                n, GH, 'tools/humanization/his_fixes_brief.md')}, 'way': n})
    return out


def parse(text):
    branches, words, problems = [], [], []
    cur_b = cur_g = cur_r = None
    last_field = None
    in_words = False
    intro_target = None
    for raw in text.split('\n'):
        line = raw.rstrip()
        if WORDS_H.match(line):
            in_words, cur_b, cur_g, cur_r, intro_target = True, None, None, None, None
            continue
        if in_words:
            m = FIELD.match(line)
            if m:
                words.append({'term': m.group(1).strip(), 'meaning': m.group(2).strip()})
                last_field = ('w', len(words) - 1)
            elif line.startswith('  ') and last_field and line.strip():
                words[last_field[1]]['meaning'] += ' ' + line.strip()
            continue
        m = BRANCH_H.match(line)
        if m:
            cur_b = {'id': 'B' + m.group(1), 'num': m.group(1), 'title': m.group(2), 'intro': '', 'groups': []}
            branches.append(cur_b)
            cur_g = cur_r = None
            intro_target = cur_b
            continue
        m = GROUP_H.match(line)
        if m and cur_b:
            cur_g = {'id': 'G' + m.group(1), 'num': m.group(1), 'title': m.group(2), 'intro': '', 'rules': []}
            cur_b['groups'].append(cur_g)
            cur_r = None
            intro_target = cur_g
            continue
        if INCLUDE.match(line) and cur_g is not None:
            cur_g['rules'] += ways()
            continue
        m = RULE_H.match(line)
        if m and cur_g is not None:
            cur_r = {'id': m.group(1), 'title': m.group(2), 'fields': {}}
            cur_g['rules'].append(cur_r)
            intro_target = None
            last_field = None
            continue
        if cur_r is not None:
            m = FIELD.match(line)
            if m:
                last_field = m.group(1).strip()
                cur_r['fields'][last_field] = m.group(2).strip()
            elif line.startswith((' ', '\t')) and last_field and line.strip():
                cur_r['fields'][last_field] += ' ' + line.strip()
            continue
        if intro_target is not None and line.strip() and not line.startswith('<!--'):
            intro_target['intro'] = (intro_target['intro'] + ' ' + line.strip()).strip()
    return branches, words, problems


def links_of(s):
    """'builds on R-a; goes with R-b, R-c' -> [('builds on', 'R-a'), ('goes with', 'R-b'), ('goes with', 'R-c')]."""
    out = []
    for part in re.split(r';', s or ''):
        part = part.strip()
        rel = next((r for r in RELATIONS if part.lower().startswith(r)), None)
        for rid in re.findall(r'R-[a-z0-9-]+', part):
            out.append((rel or 'goes with', rid))
    return out


def corpus():
    """Lower-cased, whitespace-collapsed text of every file of the repository a quote of his could be in."""
    parts = []
    roots = [REPO / 'docs', REPO / 'tools' / 'humanization', REPO / 'articles']
    for f in [REPO / 'AGENTS.md', REPO / 'SKILL.md']:
        parts.append(f.read_text(encoding='utf-8', errors='replace'))
    for root in roots:
        for f in root.rglob('*'):
            if f.is_file() and f.suffix in ('.md', '.json', '.txt', '.py') and f.stat().st_size < 3_000_000:
                if '/humanize/' in str(f) and f.suffix == '.json' and 'ANSWERS' not in f.name:
                    continue
                try:
                    parts.append(f.read_text(encoding='utf-8', errors='replace'))
                except OSError:
                    pass
    return norm('\n'.join(parts))


def build(check_only=False, view_url=''):
    text = TREE.read_text(encoding='utf-8')
    branches, words, problems = parse(text)
    rules = [r for b in branches for g in b['groups'] for r in g['rules']]
    ids = {}
    for b in branches:
        for g in b['groups']:
            for r in g['rules']:
                if r['id'] in ids:
                    problems.append('two rules with the id %s' % r['id'])
                ids[r['id']] = (b, g, r)
    notes = []
    for r in rules:
        f = r['fields']
        if not f.get('Rule'):
            problems.append('%s has no Rule' % r['id'])
        if not f.get('Why') and not f.get('Record'):
            problems.append('%s has neither Why nor Record' % r['id'])
        for rel, rid in links_of(f.get('Links', '')):
            if rel == 'conflicts with':
                problems.append('%s: "conflicts with %s": two rules that contradict can\'t both stand; settle it, or say the '
                                'open question in Status' % (r['id'], rid))
            elif rid not in ids:
                problems.append('%s links to %s, which no rule has' % (r['id'], rid))
        st = [s.strip().lower() for s in re.split(r'[,;]', f.get('Stages', '')) if s.strip()]
        bad = [s for s in st if s not in STAGES]
        if bad:
            problems.append('%s: stages %s aren\'t among %s' % (r['id'], bad, STAGES))
        r['stages'] = [s for s in st if s in STAGES]
        r['links'] = [{'rel': rel, 'to': rid} for rel, rid in links_of(f.get('Links', '')) if rid in ids]
        status = (f.get('Status') or 'active').strip()
        r['status'] = ('open question' if status.lower().startswith('open question') else
                       'to build' if status.lower().startswith('to build') else
                       'retired' if status.lower().startswith(('retired', 'historical')) else 'active')
    big = corpus()
    checked_text = norm(CHECKED.read_text(encoding='utf-8')) if CHECKED.exists() else ''
    checked = []
    for r in rules:
        if r.get('way'):
            continue
        for q in QUOTE.findall(r['fields'].get('Why', '')):
            if len(q.split()) >= 5 and norm(q) not in big:
                if norm(r['id'] + ': ' + q[:60].strip()) in checked_text:
                    checked.append('%s: "%s"' % (r['id'], q[:90]))
                    continue
                notes.append('%s: his words "%s" are in no file of the repository word for word (a saved preference or a '
                             'chat, or misquoted: look, then list it in QUOTES-CHECKED.md)' % (r['id'], q[:90]))
    counts = {b['id']: sum(len(g['rules']) for g in b['groups']) for b in branches}
    data = {'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
            'source_sha256': hashlib.sha256(text.encode('utf-8')).hexdigest(),
            'stages': [{'id': s, 'name': STAGE_NAMES[s]} for s in STAGES],
            'branches': [{'id': b['id'], 'num': b['num'], 'title': b['title'], 'intro': b['intro'],
                          'groups': [{'id': g['id'], 'num': g['num'], 'title': g['title'], 'intro': g['intro'],
                                      'rules': [{'id': r['id'], 'title': r['title'], 'fields': r['fields'],
                                                 'stages': r['stages'], 'links': r['links'], 'status': r['status'],
                                                 'anchor': gh_anchor('%s | %s' % (r['id'], r['title']))}
                                                for r in g['rules']]} for g in b['groups']]} for b in branches],
            'words': words, 'counts': counts, 'notes': notes, 'checked': checked}
    for p in problems:
        print('PROBLEM: ' + p)
    for n in notes:
        print('note: ' + n)
    print('%d rules in %d branches (%s); %d words; %d problems, %d notes' % (
        len(rules), len(branches), ', '.join('%s %d' % (k, v) for k, v in counts.items()), len(words), len(problems),
        len(notes)))
    if check_only:
        return 1 if problems else 0
    (HERE / 'tree.json').write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'CHECKS.md').write_text(checks_md(problems, notes, data), encoding='utf-8')
    (HERE / 'README.md').write_text(readme(data, view_url), encoding='utf-8')
    (HERE / 'view').mkdir(exist_ok=True)
    (HERE / 'view' / 'index.html').write_text(view(data), encoding='utf-8')
    return 1 if problems else 0


def gh_anchor(heading):
    """GitHub's anchor for a heading: lower case, punctuation but '-' and '_' dropped, spaces to '-'."""
    s = heading.strip().lower()
    s = re.sub(r'[^\w\- ]', '', s)
    return s.replace(' ', '-')


def checks_md(problems, notes, data):
    out = ['# Rule tree: the build\'s checks', '', 'Built %s from `rules/TREE.md` (SHA-256 %s).' % (
        data['built'], data['source_sha256'][:12]), '']
    out += ['## Problems', ''] + (['- ' + p for p in problems] or ['- none']) + ['']
    out += ['## Notes', '', 'Quotes of his in "Why" that no file of the repository holds word for word: from his saved '
            'preferences or a chat, or misquoted. Each is looked at.', ''] + (['- ' + n for n in notes] or ['- none'])
    out += ['', '## Quotes checked by hand', '', 'Quotes no file holds that a lane checked against his saved preferences or '
            'his message, as `rules/QUOTES-CHECKED.md` records.', ''] + (['- ' + c for c in data.get('checked', [])] or
                                                                         ['- none'])
    return '\n'.join(out) + '\n'


def readme(data, view_url):
    out = ['# The rule tree', '',
           'Every rule the editor follows on Joel\'s articles, once, in a branch named for what it protects: the reader '
           'first, his words next, passing Pangram after those (hacks last), then working with Joel and how the lanes '
           'work. Where an older file says otherwise, this tree wins (AGENTS.md). Why this shape: '
           '[BRAINSTORM.md](BRAINSTORM.md).', '']
    if view_url:
        out += ['**The human view** (the tree, a map of the links, and what every term means): %s' % view_url, '']
    out += ['The source is [TREE.md](TREE.md); `python3 rules/build_tree.py` checks it and writes this page, '
            '[tree.json](tree.json) and the view. Built %s; checks: [CHECKS.md](CHECKS.md).' % data['built'], '']
    out += ['```mermaid', 'flowchart LR', '  T(("The rules"))']
    for b in data['branches']:
        out.append('  T --> %s["%s %s (%d)"]' % (b['id'], b['num'], b['title'].replace('"', "'"), data['counts'][b['id']]))
        for g in b['groups']:
            out.append('  %s --> %s["%s %s (%d)"]' % (b['id'], g['id'].replace('.', '_'), g['num'],
                                                      g['title'].replace('"', "'"), len(g['rules'])))
    out += ['```', '']
    for b in data['branches']:
        out += ['## %s %s' % (b['num'], b['title']), '', b['intro'], '']
        for g in b['groups']:
            out += ['### %s %s' % (g['num'], g['title']), '']
            for r in g['rules']:
                tag = '' if r['status'] == 'active' else ' *(%s)*' % r['status']
                out.append('- [%s](TREE.md#%s)%s' % (r['title'], r['anchor'], tag) if not r['id'].startswith('R-way-')
                           else '- %s (the read against his fixes, way %s)' % (r['title'], r['id'][-2:].lstrip('0')))
            out.append('')
    if data['words']:
        out += ['## Words', ''] + ['- **%s:** %s' % (w['term'], w['meaning']) for w in data['words']] + ['']
    return '\n'.join(out)


def view(data):
    page = (HERE / 'view_template.html').read_text(encoding='utf-8')
    blob = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    return page.replace('/*TREE_DATA*/null', blob)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--view-url', default='')
    a = ap.parse_args()
    return build(a.check, a.view_url)


if __name__ == '__main__':
    sys.exit(main())
