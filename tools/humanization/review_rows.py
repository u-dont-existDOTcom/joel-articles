#!/usr/bin/env python3
"""A turn's review page from a small rows file (turn 76; replaces the per-turn map builders).

  python3 tools/humanization/review_rows.py ROWS.json MAP.json [--render OUT.html --since SHA] [--article-dir DIR]

ROWS.json:
  {"title": "...", "meta": "...", "intro": ["..."],
   "blocks": [{"headings": ["# H1", "## H2"], "rows": [
       {"label": "P4 (changed: ...)", "start": "the article paragraph's first words", "source": ["r4 paragraph start"],
        "beside": {"label": "Your words, ...", "text": "..."}}]}]}
A row's "beside" may give {"label", "file", "start"} instead of "text": the paragraph of FILE (relative to the article
folder; "> " quote marks are taken off) that starts with START. Each row's notes are the HTML comment right above its
paragraph in the article (the install note), as the turn map builders did. With --render it runs render_in_context.py
(the article, the r4 guide, --since SHA) and checks that every row's paragraph start is on the page.
"""
import argparse
import html
import json
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SOURCE = 'source/inner-child-guide-2026-10-04-r4.txt'


def unquote(t):
    return '\n'.join(l[2:] if l.startswith('> ') else (l[1:] if l.startswith('>') else l) for l in t.split('\n'))


def note_for(lines, start):
    for i, l in enumerate(lines):
        if l.startswith(start):
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            c = lines[j].strip() if j >= 0 else ''
            return re.sub(r'^<!--\s*|\s*-->$', '', c) if c.startswith('<!--') and c.endswith('-->') else ''
    raise SystemExit('not in the article: ' + start)


def beside(b, adir):
    if 'text' in b:
        return {'label': b['label'], 'text': b['text']}
    blocks = [x.strip() for x in unquote((adir / b['file']).read_text(encoding='utf-8')).split('\n\n')]
    hit = [x for x in blocks if x.startswith(b['start'])]
    if len(hit) != 1:
        raise SystemExit('%d paragraphs of %s start with %r' % (len(hit), b['file'], b['start']))
    return {'label': b['label'], 'text': hit[0]}


def build(rows_spec, adir):
    lines = (adir / 'HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8').split('\n')
    blocks = []
    for blk in rows_spec['blocks']:
        rows = []
        for r in blk['rows']:
            note = note_for(lines, r['start'])
            row = dict(label=r['label'], article=r['start'], source=r.get('source', []), notes=[note] if note else [])
            if 'beside' in r:
                row['beside'] = beside(r['beside'], adir)
            rows.append(row)
        blocks.append({'headings': blk['headings'], 'rows': rows})
    return {'title': rows_spec['title'], 'meta': rows_spec.get('meta', ''), 'intro': rows_spec.get('intro', []),
            'blocks': blocks}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('rows')
    ap.add_argument('map')
    ap.add_argument('--render')
    ap.add_argument('--since')
    ap.add_argument('--article-dir', default=str(REPO / 'articles/inner-child-therapy'))
    a = ap.parse_args(argv)
    adir = pathlib.Path(a.article_dir)
    m = build(json.loads(pathlib.Path(a.rows).read_text(encoding='utf-8')), adir)
    pathlib.Path(a.map).write_text(json.dumps(m, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    n = sum(len(b['rows']) for b in m['blocks'])
    print('map: %s, %d rows' % (a.map, n))
    if a.render:
        cmd = [sys.executable, str(REPO / 'tools/humanization/render_in_context.py'), a.map, a.render,
               '--article', str(adir / 'HUMANIZED-ARTICLE-SO-FAR.md'), '--source', str(adir / SOURCE)]
        if a.since:
            cmd += ['--since', a.since]
        r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, timeout=600)
        if r.returncode:
            raise SystemExit('render failed:\n' + (r.stdout + r.stderr)[-3000:])
        # struck words are the old text's (the page can't select them either), so a row whose first words changed is
        # still found by its new words (turn 107: two of his paragraphs changed their first words)
        raw = re.sub(r'<del>.*?</del>', ' ', pathlib.Path(a.render).read_text(encoding='utf-8'), flags=re.S)
        page = html.unescape(re.sub(r'<[^>]+>', ' ', raw))
        page = re.sub(r'\s+', ' ', page)
        missing = [r['article'] for b in m['blocks'] for r in b['rows'] if re.sub(r'\s+', ' ', r['article']) not in page]
        if missing:
            raise SystemExit('rows not on the page: %s' % missing)
        print('page: %s, every row on it' % a.render)
    return 0


if __name__ == '__main__':
    sys.exit(main())
