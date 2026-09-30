#!/usr/bin/env python3
"""check_owner_edits.py - check that what the records say is in the article is in the article.

Usage:
  python3 check_owner_edits.py [--article FILE] [--ledger FILE] [--json]

Joel, 2026-09-27 21:18: "so how can we prevent that kind of error in future where you say
you will write something and don't write it?" Twice a record said something was in the
article when it wasn't:
  - The orphaned "ask" fix was called "resolved" (2026-09-24) in an audit of a candidate
    that was never installed. The article kept the old sentence until 2026-09-27.
  - The three-jobs paragraph's note said "the three jobs explained where they're first
    named", but the paragraph explained only the Guide.
Both times the claim described a draft or a plan, and nothing compared it with the text.

OWNER-EDITS.json lists each edit Joel gives and each claim about what a paragraph covers.
Each entry has strings the article's visible text must contain, must not contain, or must
have in order. An entry can also list links (must_link: text and url) the article must
have; those are checked on the text with comments removed but link targets kept. This script checks them against HUMANIZED-ARTICLE-SO-FAR.md, reading it
without comments, link targets or emphasis marks, and with curly quotes made straight.
render_article_so_far.py runs it every time. A failure goes in a red box at the top of the
article Joel gets, and the render exits 1.

Entry statuses:
  applied   the edit is in the article; any failed check is an error
  claim     a record says the article covers something; any failed check is an error
  pending   not in yet; listed as waiting, with what it waits for
  superseded  replaced by a later entry; skipped

Exit code: 0 if every applied and claim entry passes, 1 otherwise.
"""
import argparse, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ARTICLE = HERE.parent / 'HUMANIZED-ARTICLE-SO-FAR.md'
LEDGER = HERE.parent / 'OWNER-EDITS.json'

QUOTES = str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"'})


def norm(s):
    s = s.translate(QUOTES)
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)   # [text](url) -> text
    s = s.replace('*', '')
    s = re.sub(r'^#+\s*', '', s, flags=re.M)          # heading marks
    return re.sub(r'\s+', ' ', s).strip()


def visible(md):
    return norm(re.sub(r'<!--.*?-->', ' ', md, flags=re.S))


def check_entry(e, text, raw=''):
    """Return a list of failure strings for one entry."""
    fails = []
    for l in e.get('must_link', []):
        if ('[%s](%s)' % (l['text'], l['url'])).translate(QUOTES) not in raw:
            fails.append('link missing: [%s](%s)' % (l['text'], l['url']))
    for s in e.get('must_contain', []):
        if norm(s) not in text:
            fails.append('missing: "%s"' % s)
    for s in e.get('must_not_contain', []):
        if norm(s) in text:
            fails.append('still there: "%s"' % s)
    order = e.get('order', [])
    if order:
        pos = 0
        for s in order:
            i = text.find(norm(s), pos)
            if i < 0:
                fails.append('out of order or missing: "%s"' % s)
                break
            pos = i + len(norm(s))
    sp = e.get('span')
    if sp:
        a = text.find(norm(sp['from']))
        b = text.find(norm(sp['to']), a + 1) if a >= 0 else -1
        if a < 0 or b < 0:
            fails.append('span not found: "%s" to "%s"' % (sp['from'], sp['to']))
        else:
            chunk = text[a:b]
            for s in sp.get('must_contain', []):
                if norm(s) not in chunk:
                    fails.append('not in the span from "%s": "%s"' % (sp['from'][:40], s))
    return fails


def run(article=ARTICLE, ledger=LEDGER):
    md = pathlib.Path(article).read_text(encoding='utf-8')
    text = visible(md)
    raw = re.sub(r'<!--.*?-->', ' ', md, flags=re.S).translate(QUOTES)
    data = json.loads(pathlib.Path(ledger).read_text(encoding='utf-8'))
    out = {'failed': [], 'waiting': [], 'looks_applied': [], 'passed': 0}
    for e in data['entries']:
        st = e.get('status')
        if st == 'superseded':
            continue
        fails = check_entry(e, text, raw)
        if st in ('applied', 'claim'):
            if fails:
                out['failed'].append({'id': e['id'], 'what': e['what'], 'fails': fails})
            else:
                out['passed'] += 1
        elif st == 'pending':
            out['waiting'].append({'id': e['id'], 'what': e['what'], 'waits_for': e.get('waits_for', '')})
            if not fails and (e.get('must_contain') or e.get('order') or e.get('span') or e.get('must_link')):
                out['looks_applied'].append(e['id'])
        else:
            out['failed'].append({'id': e.get('id', '?'), 'what': e.get('what', ''),
                                  'fails': ['unknown status: %r' % st]})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--article', default=str(ARTICLE))
    ap.add_argument('--ledger', default=str(LEDGER))
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args()
    r = run(a.article, a.ledger)
    if a.json:
        print(json.dumps(r, indent=1, ensure_ascii=False))
    else:
        print('== check_owner_edits: %s' % a.article)
        print('passed: %d   failed: %d   waiting: %d' % (r['passed'], len(r['failed']), len(r['waiting'])))
        for f in r['failed']:
            print('FAIL %s (%s)' % (f['id'], f['what']))
            for x in f['fails']:
                print('   - ' + x)
        for w in r['waiting']:
            print('waiting %s: %s (%s)' % (w['id'], w['what'], w['waits_for']))
        for i in r['looks_applied']:
            print('note: pending entry %s already passes; update its status' % i)
    sys.exit(1 if r['failed'] else 0)


if __name__ == '__main__':
    main()
