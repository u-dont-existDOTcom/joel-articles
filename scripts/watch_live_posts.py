#!/usr/bin/env python3
"""watch_live_posts.py - the daily look at Joel's live posts: did a passage change that another passage depends on?

Joel, 2026-11-25 11:18 UTC: "some way to know when one thing changes that another thing is dependent on in same article
or diff article." The registry (articles/DEPENDS.json, tools/humanization/depends.py) answers that for a lane's own
edits: `depends.py check` looks for every registered passage in each article's saved copy of its live post
(articles/<id>/LIVE-SECTIONS.json). Nothing noticed when he edits a post on Substack himself, because the saved copy
stays as it was. Joel, 2026-11-25 16:14 UTC: "for the registry, yes you can add the github job". This is that job's
script; .github/workflows/depends-watch.yml runs it once a day.

For every article the registry's "texts" names it fetches the live post (Substack's public post API), builds its
sections in memory (tools/humanization/live_sections.py) and compares them with the saved copy: whether the post
changed at all (its HTML's sha256, Substack's updated_at), and which sections have other words, are new, are gone or
have another heading. Then it runs `depends.check` on the fetched text: every registered quote or heading that is no
longer found in a live post is listed with its point, the place that changed, and every other place that depends on it,
so a reader knows what to read again. A quote that was already missing from the saved copy is listed apart: the post
did not change there, the registry is behind.

It writes nothing under articles/: every file there is registered with its hash in articles/INDEX.json, and the lane
refreshes the saved copies itself (`live_sections.py build --article ID --out ...`).

  python3 scripts/watch_live_posts.py                        # the report (Markdown) on the screen
  python3 scripts/watch_live_posts.py --report REPORT.md     # ... and in a file
  python3 scripts/watch_live_posts.py --json > RESULT.json   # the same as JSON, with the report in it
  python3 scripts/watch_live_posts.py --issues-from RESULT.json [--run-url URL]
        # no fetch: open, update or close the GitHub issues for a saved result, with `gh` (the daily job's second step)

Exit: 0 nothing registered changed; 1 at least one registered passage or heading changed in a live post; 2 a post
could not be fetched (the report says which, with the HTTP status; what could be fetched is still compared, and its
changed passages are in the report and the JSON); 3 the script itself failed.

The issues (`--issues-from`). Changed passages: one open issue labelled depends-watch, "Live post changed: N registered
passages to re-read (date)", with the report; while one is open, a new report goes under it as a comment, and only
when the list of changed passages is another one than the last posted (the same change is not posted every day). A
post that could not be fetched: one open issue labelled depends-watch-fetch that says which post and since when; its
text is brought up to date each day without a new issue, and it is closed, with a comment, the first day every post
can be fetched again.
"""
import argparse
import collections
import datetime
import difflib
import hashlib
import json
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import depends as D  # noqa: E402
import live_sections as LS  # noqa: E402
import section_links as SL  # noqa: E402

LABEL = D.WATCH_LABEL
FETCH_LABEL = 'depends-watch-fetch'
LABELS = {LABEL: ('BFD4F2', 'A registered passage changed in a live post (scripts/watch_live_posts.py)'),
          FETCH_LABEL: ('FBCA04', 'The daily job could not fetch a live post (scripts/watch_live_posts.py)')}
MARK = re.compile(r'<!-- depends-watch report ([0-9a-f]{64}) -->')
FETCH_MARK = re.compile(r'<!-- depends-watch-fetch (\{.*?\}) -->', re.S)
BODY_LIMIT = 60000                      # GitHub refuses an issue body or comment over 65536 characters
EXAMPLES = 3                            # changed paragraphs shown for one section


# ---------------------------------------------------------------- what differs between two lists of sections

def _words(section):
    return ' '.join(section.get('paragraphs') or []).split()


def _alike(a, b):
    """How alike two sections' own words are, from 0 to 1."""
    return difflib.SequenceMatcher(None, _words(a), _words(b), autojunk=False).ratio()


def pair_sections(old, new):
    """[(i, j, renamed)]: which saved section is which live one.

    First by heading: a section keeps its heading unless he renamed it (of several with the same heading, the ones
    with the same words first, then in order). Then, among the rest, a section whose words stand under another
    heading is that section renamed: the same words anywhere, or, between the same two neighbours, words that are
    mostly the same or two headings with no words of their own."""
    pairs, left_old, left_new = [], [], list(range(len(new)))
    by_heading = collections.defaultdict(list)
    for j, s in enumerate(new):
        by_heading[s['heading']].append(j)
    for i, s in enumerate(old):
        js = by_heading.get(s['heading'])
        if not js:
            left_old.append(i)
            continue
        j = next((j for j in js if new[j]['paragraphs'] == s['paragraphs']), js[0])
        js.remove(j)
        left_new.remove(j)
        pairs.append((i, j, False))

    to_new = {i: j for i, j, _ in pairs}
    to_old = {j: i for i, j, _ in pairs}

    def take(i, j):
        left_old.remove(i)
        left_new.remove(j)
        pairs.append((i, j, True))
        to_new[i], to_old[j] = j, i

    for i in list(left_old):                                       # the same words under another heading
        j = next((j for j in left_new if old[i]['paragraphs'] and new[j]['paragraphs'] == old[i]['paragraphs']), None)
        if j is not None:
            take(i, j)

    def after_old(i):                 # the live section that the nearest paired saved section before i has become
        return to_new.get(max((x for x in to_new if x < i), default=None), -1)

    def after_new(j):                 # the nearest paired live section before j
        return max((x for x in to_old if x < j), default=-1)

    for i in list(left_old):                                       # between the same neighbours
        scored = [(1.0 if not old[i]['paragraphs'] and not new[j]['paragraphs'] else _alike(old[i], new[j]), -j)
                  for j in left_new if after_new(j) == after_old(i)]
        if scored and max(scored)[0] >= 0.5:
            take(i, -max(scored)[1])
    if len(left_old) * len(left_new) <= 400:                       # mostly the same words, moved elsewhere
        for i in list(left_old):
            scored = [(_alike(old[i], new[j]), -j) for j in left_new if old[i]['paragraphs'] and new[j]['paragraphs']]
            if scored and max(scored)[0] >= 0.6:
                take(i, -max(scored)[1])
    return sorted(pairs)


def _differs(x, y, around=6, most=30):
    """The stretch where two paragraphs differ, each with a few words around it."""
    a, b = x.split(), y.split()
    ops = [o for o in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if o[0] != 'equal']
    if not ops:
        return x, y

    def cut(words, lo, hi):
        start, end = max(0, lo - around), min(len(words), max(hi, lo) + around)
        end = min(end, start + most + 2 * around)
        return ('…' if start else '') + ' '.join(words[start:end]) + ('…' if end < len(words) else '')

    return cut(a, ops[0][1], ops[-1][2]), cut(b, ops[0][3], ops[-1][4])


def paragraph_changes(a, b):
    """None when two sections have the same paragraphs; else how many changed, were added and removed, and the first
    few as {"was", "now"} (a new paragraph has no "was", a removed one no "now")."""
    if a == b:
        return None
    out = {'changed': 0, 'added': 0, 'removed': 0, 'examples': []}
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == 'equal':
            continue
        k = min(i2 - i1, j2 - j1)
        out['changed'] += k
        out['removed'] += (i2 - i1) - k
        out['added'] += (j2 - j1) - k
        for x, y in zip(a[i1:i1 + k], b[j1:j1 + k]):
            was, now = _differs(x, y)
            out['examples'].append({'was': was, 'now': now})
        out['examples'] += [{'was': D.first_words(x, 14), 'now': None} for x in a[i1 + k:i2]]
        out['examples'] += [{'was': None, 'now': D.first_words(y, 14)} for y in b[j1 + k:j2]]
    out['more'] = max(0, len(out['examples']) - EXAMPLES)
    out['examples'] = out['examples'][:EXAMPLES]
    return out


def diff_sections(old, new):
    """What differs between the saved copy's sections and the live post's, by heading: {"changed": sections with
    other words, "renamed", "added", "removed", "level": headings that moved up or down a level}."""
    out = {'changed': [], 'renamed': [], 'added': [], 'removed': [], 'level': []}
    pairs = pair_sections(old, new)
    for i, j, renamed in pairs:
        a, b = old[i], new[j]
        text = paragraph_changes(a['paragraphs'], b['paragraphs'])
        if renamed:
            out['renamed'].append({'was': a['heading'], 'now': b['heading'], 'saved_id': a['id'], 'live_id': b['id'],
                                   'text': text})
        elif text:
            out['changed'].append({'heading': b['heading'], 'saved_id': a['id'], 'live_id': b['id'], 'text': text})
        if a['level'] != b['level']:
            out['level'].append({'heading': b['heading'], 'was': a['level'], 'now': b['level']})
    kept_old, kept_new = {i for i, _, _ in pairs}, {j for _, j, _ in pairs}
    out['removed'] = [{'heading': s['heading'], 'saved_id': s['id'], 'level': s['level'],
                       'paragraphs': len(s['paragraphs'])} for i, s in enumerate(old) if i not in kept_old]
    out['added'] = [{'heading': s['heading'], 'live_id': s['id'], 'level': s['level'],
                     'paragraphs': len(s['paragraphs'])} for j, s in enumerate(new) if j not in kept_new]
    return out


# ---------------------------------------------------------------- the look itself

def live_catalog(saved, body_html, post):
    """The live post's headings with their anchors, in the shape of SECTION-LINKS.json. A heading whose words the
    saved catalog has keeps the anchor recorded there (read on the rendered page); a new or renamed one gets the
    anchor Substack makes from its words (section_links.slug)."""
    cat = SL.build(body_html, LS.publication(post), post.get('id'), 'the live post, as fetched')
    known = collections.defaultdict(list)
    for h in (saved or {}).get('headings', []):
        known[D.plain(h.get('text'))].append(h.get('anchor'))
    for h in cat['headings']:
        anchors = known.get(D.plain(h['text']))
        if anchors:
            h['anchor'] = anchors.pop(0)
    return cat


def _key(f):
    return json.dumps([f['id'], f['side'], f['place']], ensure_ascii=False, sort_keys=True)


def _points_by_section(reg):
    out = collections.defaultdict(list)
    for p in reg.get('points', []):
        for place in [p['home']] + p.get('uses', []):
            name = place.get('section') or place.get('heading')
            if name and p.get('id') not in out[(place.get('article'), D.plain(name))]:
                out[(place.get('article'), D.plain(name))].append(p.get('id'))
    return out


def _default_fetch(timeout):
    return lambda post_id, post: LS.fetch_post(post_id, LS.publication(post), timeout=timeout)


def watch(root=REPO, fetch=None, today=None, timeout=20):
    """Fetch every watched post, compare, check. Returns the result (a dict that goes to JSON as it is); its "exit"
    is the exit code and its "report" the Markdown. fetch(post_id, saved_post) returns the API's answer or raises
    live_sections.FetchError; the tests give their own, so nothing here touches the network."""
    root = pathlib.Path(root)
    reg = D.load(root)
    fetch = fetch or _default_fetch(timeout)
    today = today or datetime.datetime.now(datetime.timezone.utc).date().isoformat()
    by_section = _points_by_section(reg)
    articles, failures, given, catalogs, why = [], [], {}, {}, {}

    for article, row in LS.posts(root, reg).items():
        saved_post = row['post']
        entry = {'article': article, 'post_id': row['id'], 'saved_copy': row['path'], 'api': row['url'],
                 'url': saved_post.get('canonical_url'), 'title': saved_post.get('title'), 'fetched': False}
        articles.append(entry)
        try:
            if not row['id']:
                raise LS.FetchError('no post id: %s' % row.get('why'), None, None)
            post = LS.post_of(fetch(row['id'], saved_post), row['url'])
            if str(post.get('id')) != str(row['id']):
                raise LS.FetchError('the answer is post %s, not post %s' % (post.get('id'), row['id']), None,
                                    row['url'])
            saved = json.loads((root / row['path']).read_text(encoding='utf-8'))
        except LS.FetchError as e:
            entry['error'] = {'status': e.status, 'reason': e.reason}
            failures.append({'article': article, 'post_id': row['id'], 'api': e.url or row['url'],
                             'status': e.status, 'reason': e.reason})
            given[article] = None
            why[article] = 'its live post could not be fetched (%s)' % e.reason
            continue
        live = LS.build(post, fetched=today)
        diff = diff_sections(saved.get('sections') or [], live['sections'])
        for kind, name in (('changed', 'heading'), ('renamed', 'was'), ('removed', 'heading')):
            for item in diff[kind]:
                item['points'] = by_section.get((article, D.plain(item[name])), [])
        words = any(diff[k] for k in ('changed', 'renamed', 'added', 'removed'))
        entry.update({
            'fetched': True, 'url': live['post'].get('canonical_url') or entry['url'],
            'title': live['post'].get('title') or entry['title'],
            'saved': {k: saved_post.get(k) for k in ('body_sha256', 'updated_at', 'fetched')},
            'live': {k: live['post'].get(k) for k in ('body_sha256', 'updated_at', 'wordcount')},
            'html_changed': saved_post.get('body_sha256') != live['post']['body_sha256'],
            'words_changed': words, 'sections': diff, 'section_count': len(live['sections']),
            'fields': [{'field': k, 'was': saved_post.get(k), 'now': live['post'].get(k)}
                       for k in ('title', 'subtitle') if saved_post.get(k) != live['post'].get(k)],
            'audience': post.get('audience')})
        given[article] = D.parse(json.dumps(live), 'live.json')._replace(
            path='the live post (%s)' % (entry['url'] or row['url']))
        try:
            catalog = json.loads((root / 'articles' / article / 'SECTION-LINKS.json').read_text(encoding='utf-8'))
            catalogs[article] = live_catalog(catalog, post['body_html'], post)
        except (OSError, ValueError):
            pass                                   # no catalog for it: `check` reads the heading only, as it does now

    live_texts = D.Texts(reg, root, given=given, catalogs=catalogs, why=why)
    findings, unread, places = D.check(reg, live_texts)
    was = {_key(f) for f in D.check(reg, D.Texts(reg, root))[0]}
    for f in findings:
        f['md'] = D.finding_md(f, live_texts)
    affected = [f for f in findings if _key(f) not in was]
    already = [f for f in findings if _key(f) in was]
    not_checked = collections.defaultdict(list)
    for pid, article, _ in unread:
        if pid not in not_checked[article]:
            not_checked[article].append(pid)
    for failure in failures:
        failure['points_not_checked'] = not_checked.get(failure['article'], [])
    named = {x.get('article') for p in reg.get('points', []) for x in [p['home']] + p.get('uses', [])}
    result = {
        'checked': today, 'exit': 2 if failures else 1 if affected else 0,
        'points': len(reg.get('points', [])), 'places': places, 'watched': len(articles),
        'affected': affected, 'already': already, 'fetch_failures': failures, 'articles': articles,
        'not_watched': sorted(a for a in named if a and a not in given),
        'not_read': sorted({'%s: %s' % (a, w) for _, a, w in unread if a not in given}),
        'fingerprint': hashlib.sha256(json.dumps(sorted(_key(f) for f in affected)).encode('utf-8')).hexdigest(),
        'fetch_fingerprint': hashlib.sha256(json.dumps(sorted(
            [f['article'], f['status'], f['reason']] for f in failures)).encode('utf-8')).hexdigest(),
    }
    result['title'] = 'Live post changed: %s to re-read (%s)' % (D._n(len(affected), 'registered passage'), today)
    result['report'] = report(result)
    return result


# ---------------------------------------------------------------- the report

def _q(s):
    return '“%s”' % re.sub(r'\s+', ' ', str(s or '')).strip()


def _ids(ids, most=12):
    """Point ids in a line; a long list is cut, with how many more there are."""
    return ', '.join(ids) if len(ids) <= most else '%s and %d more' % (', '.join(ids[:most - 2]), len(ids) - most + 2)


def _points(item):
    return ' Registered here: %s.' % _ids(item['points']) if item.get('points') else ''


def _text_lines(text, indent='    '):
    if not text:
        return []
    counts = ', '.join(D._n(text[k], 'paragraph') + ' ' + k for k in ('changed', 'added', 'removed') if text[k])
    out = []
    for e in text['examples']:
        if e['was'] and e['now']:
            out += ['%s- was: %s' % (indent, _q(e['was'])), '%s  now: %s' % (indent, _q(e['now']))]
        elif e['now']:
            out.append('%s- new: %s' % (indent, _q(e['now'])))
        else:
            out.append('%s- gone: %s' % (indent, _q(e['was'])))
    if text.get('more'):
        out.append('%s- and %d more' % (indent, text['more']))
    return [counts] + out


def _article_lines(a):
    name = '%s (%s)' % (a['title'], a['article']) if a.get('title') else a['article']
    out = ['### %s' % name, '']
    copy = '[the saved copy%%s](%s%s)' % (D.GIT, a['saved_copy'])
    if not a['fetched']:
        return out + ['- Could not be fetched: %s. Nothing in it was compared with %s.'
                      % (a['error']['reason'], copy % ''), '']
    saved, live = a['saved'], a['live']
    where = '[the post](%s)' % a['url'] if a.get('url') else 'the post'
    since = copy % (' of %s' % saved['fetched'] if saved.get('fetched') else '')
    updated = (' Substack last updated it %s (the saved copy has %s).' % (live['updated_at'], saved.get('updated_at'))
               if live.get('updated_at') and live['updated_at'] != saved.get('updated_at') else '')
    if not a['html_changed']:
        out.append('- No change: %s is the same as in %s.%s' % (where, since, updated))
        if a['words_changed']:
            out.append('- The saved copy has other sections than this script makes from the same HTML, so that file '
                       'was made another way; the differences below are not changes on Substack.')
    elif not a['words_changed']:
        out.append('- No words changed in %s since %s; its HTML did (links, pictures or formatting).%s'
                   % (where, since, updated))
    else:
        out.append('- **Changed** since %s: %s.%s' % (since, where, updated))
    for f in a['fields']:
        out.append('- Its %s changed: %s, was %s.' % (f['field'], _q(f['now']), _q(f['was'])))
    if a.get('audience') and a['audience'] != 'everyone':
        out.append('- Its audience is "%s", so what the public API gives may be cut short.' % a['audience'])
    d = a['sections']
    if d['changed']:
        out.append('- Sections with other words (%d):' % len(d['changed']))
        for s in d['changed']:
            lines = _text_lines(s['text'])
            out += ['  - %s: %s.%s' % (_q(s['heading']), lines[0], _points(s))] + lines[1:]
    if d['renamed']:
        out.append('- Headings renamed (%d):' % len(d['renamed']))
        for s in d['renamed']:
            lines = _text_lines(s['text'])
            out += ['  - %s is now %s%s.%s' % (_q(s['was']), _q(s['now']),
                                                 '; ' + lines[0] if lines else '', _points(s))] + lines[1:]
    if d['added']:
        out.append('- New sections (%d): %s.' % (len(d['added']), ', '.join(
            '%s (%s)' % (_q(s['heading']), D._n(s['paragraphs'], 'paragraph')) for s in d['added'])))
    if d['removed']:
        out.append('- Sections that are gone (%d):' % len(d['removed']))
        out += ['  - %s (%s).%s' % (_q(s['heading']), D._n(s['paragraphs'], 'paragraph'), _points(s))
                for s in d['removed']]
    if d['level']:
        out.append('- Headings that moved a level (%d): %s.' % (len(d['level']), ', '.join(
            '%s (h%d, was h%d)' % (_q(s['heading']), s['now'], s['was']) for s in d['level'])))
    return out + ['']


def report(result):
    """The Markdown report: what to re-read first, then what could not be fetched, then each post."""
    affected, failures, already = result['affected'], result['fetch_failures'], result['already']
    watched = D._n(result['watched'], 'live post')
    out = ['## Live posts and the shared passages', '']
    if affected:
        out.append('**%s changed in a live post.** Each is listed below with the other places that depend on it, to '
                   'read again.' % D._n(len(affected), 'registered passage'))
    elif failures:
        out.append('No registered passage changed in the posts that could be fetched.')
    elif already:
        one = len(already) == 1
        out.append('No registered passage changed on Substack: the %s say what the saved copies say. %s already '
                   'missing from a saved copy and %s listed below.'
                   % (watched, '1 registered passage was' if one else '%d registered passages were' % len(already),
                      'is' if one else 'are'))
    else:
        out.append('Nothing registered changed: every passage and heading of the registry that was looked for (%s, '
                   '%s) still stands in the %s.' % (D._n(result['points'], 'point'), D._n(result['places'], 'place'),
                                                    watched))
    if failures:
        out.append('')
        out.append('**%d of the %s could not be fetched**, so the passages in %s were not checked.'
                   % (len(failures), watched, 'it' if len(failures) == 1 else 'them'))
    out.append('')
    if affected:
        out += ['### To re-read (%d)' % len(affected), '']
        for f in affected:
            out += f['md'] + ['']
    if failures:
        out += ['### Could not be fetched (%d)' % len(failures), '']
        for f in failures:
            skipped = f.get('points_not_checked') or []
            out.append('- **%s** (post %s): %s. %s%s' % (
                f['article'], f['post_id'] or '?', f['reason'], f['api'] or '',
                ' Not checked: %s (%s).' % (D._n(len(skipped), 'point'), _ids(skipped)) if skipped else ''))
        out.append('')
    if already:
        out += ['### Already missing from the saved copy (%d)' % len(already), '',
                'These were not found in the saved copy of the post either, so they are not a change on Substack: '
                'the registry is behind its own files (`depends.py check` lists them too).', '']
        for f in already:
            out += f['md'] + ['']
    if result['not_read']:
        out += ['### Not looked for', ''] + ['- %s' % line for line in result['not_read']] + ['']
    out += ['## The posts', '']
    for a in result['articles']:
        out += _article_lines(a)
    if not result['articles']:
        out += ['The registry\'s "texts" names no saved live post, so there was nothing to fetch.', '']
    if result['not_watched']:
        out += ['Not fetched, because the registry reads %s in a file of the repository and not in a saved live '
                'post: %s.' % ('it' if len(result['not_watched']) == 1 else 'them', ', '.join(result['not_watched'])),
                '']
    return '\n'.join(out).rstrip('\n') + '\n'


# ---------------------------------------------------------------- the issues

class GhError(Exception):
    pass


def run_gh(args, text=None):
    """Run `gh` with these arguments (text goes to its standard input) and return what it prints."""
    r = subprocess.run(['gh'] + list(args), input=text, capture_output=True, text=True, timeout=120)
    if r.returncode:
        raise GhError('gh %s failed (exit %d): %s' % (' '.join(args[:3]), r.returncode, r.stderr.strip()[-600:]))
    return r.stdout


def _fits(text):
    if len(text) <= BODY_LIMIT:
        return text
    return text[:BODY_LIMIT].rsplit('\n', 1)[0] + '\n\n(The report is longer than an issue can hold. The whole of ' \
                                                  'it is in the summary of the job\'s run.)\n'


def _ensure_label(gh, name):
    have = json.loads(gh(['label', 'list', '--search', name, '--json', 'name', '--limit', '100']) or '[]')
    if name not in [x.get('name') for x in have]:
        gh(['label', 'create', name, '--color', LABELS[name][0], '--description', LABELS[name][1]])
        return True
    return False


def _open_issue(gh, label):
    """The open issue with this label (the oldest, when there are several), or None."""
    rows = json.loads(gh(['issue', 'list', '--state', 'open', '--label', label, '--json', 'number,title,url',
                          '--limit', '50']) or '[]')
    return min(rows, key=lambda r: r['number']) if rows else None


def _foot(run_url):
    made = 'Made by the daily job ([the daily check](%s%s))' % (D.GIT, D.WATCH)
    return made + (', [this run](%s).' % run_url if run_url else '.')


def file_issues(result, gh=None, run_url=None):
    """Open, update or close the issues for a result. Returns the lines that say what was done.

    gh(args, text) runs the GitHub CLI (run_gh); the tests give their own."""
    gh = gh or run_gh
    done, today = [], result['checked']
    affected, failures = result['affected'], result['fetch_failures']

    if affected:
        created = _ensure_label(gh, LABEL)
        mark = '<!-- depends-watch report %s -->' % result['fingerprint']
        issue = None if created else _open_issue(gh, LABEL)
        if issue is None:
            body = '%s\n---\n%s The page of all shared passages is [articles/DEPENDS.md](%s%s). Close this issue ' \
                   'when the passages are in line again; the job opens a new one at the next change.\n%s\n' \
                   % (_fits(result['report']), _foot(run_url), D.GIT, D.PAGE, mark)
            url = gh(['issue', 'create', '--title', result['title'], '--label', LABEL, '--body-file', '-'], body)
            done.append('opened an issue: %s %s' % (result['title'], url.strip()))
        else:
            seen = json.loads(gh(['issue', 'view', str(issue['number']), '--json', 'body,comments']))
            marks = [m for text in [seen.get('body')] + [c.get('body') for c in seen.get('comments') or []]
                     for m in MARK.findall(text or '')]
            if marks and marks[-1] == result['fingerprint']:
                done.append('issue #%d already has this list of changed passages: nothing posted' % issue['number'])
            else:
                body = '**%s: %s to re-read now.** The list is another one than the last posted here.\n\n%s\n---\n' \
                       '%s\n%s\n' % (today, D._n(len(affected), 'registered passage'), _fits(result['report']),
                                     _foot(run_url), mark)
                gh(['issue', 'comment', str(issue['number']), '--body-file', '-'], body)
                done.append('added the new report to issue #%d' % issue['number'])

    if failures:
        created = _ensure_label(gh, FETCH_LABEL)
        issue = None if created else _open_issue(gh, FETCH_LABEL)
        state = {'since': {}, 'fingerprint': None}
        if issue is not None:
            seen = json.loads(gh(['issue', 'view', str(issue['number']), '--json', 'body']))
            found = FETCH_MARK.search(seen.get('body') or '')
            try:
                state.update(json.loads(found.group(1)) if found else {})
            except ValueError:
                pass
        since = {f['article']: (state.get('since') or {}).get(f['article'], today) for f in failures}
        first = min(since.values())
        lines = ['The daily job could not read %s, so the passages in %s were not checked:' % (
            'this live post' if len(failures) == 1 else 'these live posts', 'it' if len(failures) == 1 else 'them'), '']
        for f in failures:
            skipped = f.get('points_not_checked') or []
            lines.append('- **%s** (post %s): %s, since %s. %s%s' % (
                f['article'], f['post_id'] or '?', f['reason'], since[f['article']], f['api'] or '',
                ' Not checked: %s.' % D._n(len(skipped), 'point') if skipped else ''))
        lines += ['', 'Last tried: %s. The job tries again every day and closes this issue itself the first day every '
                      'post can be read. If Substack keeps refusing GitHub\'s servers, the same check runs from a '
                      'laptop: `python3 scripts/watch_live_posts.py`.' % today, '', '---', _foot(run_url),
                  '<!-- depends-watch-fetch %s -->' % json.dumps(
                      {'since': since, 'fingerprint': result['fetch_fingerprint']}, sort_keys=True), '']
        body = '\n'.join(lines)
        if issue is None:
            title = 'Live %s could not be fetched since %s' % ('post' if len(failures) == 1 else 'posts', first)
            url = gh(['issue', 'create', '--title', title, '--label', FETCH_LABEL, '--body-file', '-'], body)
            done.append('opened an issue: %s %s' % (title, url.strip()))
        else:
            gh(['issue', 'edit', str(issue['number']), '--body-file', '-'], body)
            done.append('brought issue #%d up to date (still not fetched)' % issue['number'])
            if state.get('fingerprint') != result['fetch_fingerprint']:
                gh(['issue', 'comment', str(issue['number']), '--body-file', '-'],
                   '%s: what could not be fetched is another list now: %s.\n' % (today, '; '.join(
                       '%s (%s)' % (f['article'], f['reason']) for f in failures)))
                done.append('said in issue #%d that the list changed' % issue['number'])
    else:
        have = json.loads(gh(['label', 'list', '--search', FETCH_LABEL, '--json', 'name', '--limit', '100']) or '[]')
        issue = _open_issue(gh, FETCH_LABEL) if FETCH_LABEL in [x.get('name') for x in have] else None
        if issue is not None:
            gh(['issue', 'close', str(issue['number']), '--comment',
                'Fetching works again: on %s the job read all %s.' % (today, D._n(result['watched'], 'live post'))])
            done.append('closed issue #%d: fetching works again' % issue['number'])

    return done or ['nothing to post']


# ---------------------------------------------------------------- the command

class _Parser(argparse.ArgumentParser):
    def error(self, message):                      # argparse leaves with 2, which here means "a post was not fetched"
        self.print_usage(sys.stderr)
        self.exit(3, '%s: %s\n' % (self.prog, message))


def _inside(path, folder):
    try:
        pathlib.Path(path).resolve().relative_to(pathlib.Path(folder).resolve())
        return True
    except ValueError:
        return False


def main(argv=None):
    ap = _Parser(description=__doc__.split('\n')[0])
    ap.add_argument('--root', default=str(REPO), help='the repository (default: this one)')
    ap.add_argument('--report', metavar='FILE', help='write the Markdown report here too (never under articles/)')
    ap.add_argument('--json', action='store_true', help='print the result as JSON, not the report')
    ap.add_argument('--timeout', type=float, default=20, help='seconds to wait for Substack (default 20)')
    ap.add_argument('--issues-from', metavar='RESULT.json',
                    help='no fetch: open, update or close the GitHub issues for a result saved with --json')
    ap.add_argument('--run-url', help='the address of the job\'s run, for the issue\'s last line')
    args = ap.parse_args(argv)
    try:
        if args.issues_from:
            result = json.loads(pathlib.Path(args.issues_from).read_text(encoding='utf-8'))
            for line in file_issues(result, run_url=args.run_url):
                print(line)
            return 0
        if args.report and _inside(args.report, pathlib.Path(args.root) / 'articles'):
            print('the report cannot go under articles/: every file there is registered in articles/INDEX.json',
                  file=sys.stderr)
            return 3
        result = watch(args.root, timeout=args.timeout)
        if args.report:
            pathlib.Path(args.report).write_text(result['report'], encoding='utf-8')
        sys.stdout.write(json.dumps(result, ensure_ascii=False, indent=1) + '\n' if args.json else result['report'])
        for f in result['fetch_failures']:
            print('not fetched: %s (post %s): %s' % (f['article'], f['post_id'], f['reason']), file=sys.stderr)
        return result['exit']
    except Exception as e:                           # noqa: BLE001 - 1 and 2 have meanings; a failure is 3
        import traceback
        traceback.print_exc()
        print('watch_live_posts.py failed: %s' % e, file=sys.stderr)
        return 3


if __name__ == '__main__':
    sys.exit(main())
