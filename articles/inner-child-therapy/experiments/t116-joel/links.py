#!/usr/bin/env python3
"""Turn 116: the links in his reorganized guide against the last guide I gave him (LINKS.md, LINKS.json).

His file (his ODT of 2026-11-03 21:00 UTC) has six real hyperlinks (read from its content.xml, <text:a>). Every other
"[text](url)" in JOEL-GUIDE-20261103.md is text he typed in that form, which Substack shows as typed. For each link of
the base (HUMANIZED-ARTICLE-SO-FAR.md at 8c7068d4, outside HTML comments) this finds what his version did with it:
REAL (a real hyperlink in his file), TYPED (he typed it as [text](url)), UNLINKED (the words are there with no link),
or GONE (the words aren't there). Then it lists his typed links that the base didn't have.

  python3 links.py [path/to/his.odt]"""
import json
import pathlib
import re
import subprocess
import sys
import zipfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BASE_SHA = '8c7068d4c572590c93145deee3bafee72d55f608'
base = subprocess.run(['git', 'show', BASE_SHA + ':articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'], cwd=ROOT,
                      capture_output=True, text=True, check=True).stdout
base = re.sub(r'<!--.*?-->', '', base, flags=re.S)
joel = (HERE / 'JOEL-GUIDE-20261103.md').read_text(encoding='utf-8')
LINK = re.compile(r'\[([^\[\]]+)\]\s?\(<?([^()\s<>]+(?:\([^()\s]*\))?[^()\s<>]*)>?\)')


def straight(s):
    return s.translate(str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"'})).replace('*', '').strip().lower()


def real_links(odt):
    if not odt or not pathlib.Path(odt).exists():
        return None
    x = zipfile.ZipFile(odt).read('content.xml').decode('utf-8')
    out = []
    for h, t in re.findall(r'<text:a [^>]*xlink:href="([^"]*)"[^>]*>(.*?)</text:a>', x, flags=re.S):
        out.append((re.sub(r'<[^>]+>', '', t), h.replace('&amp;', '&')))
    return out


def main():
    odt = sys.argv[1] if len(sys.argv) > 1 else None
    real = real_links(odt)
    real_texts = {straight(t) for t, _ in real} if real else set()
    base_links = [(m.group(1), m.group(2)) for m in LINK.finditer(base)]
    joel_links = [(m.group(1), m.group(2), m.start()) for m in LINK.finditer(joel)]
    joel_plain = straight(LINK.sub(lambda m: m.group(1), joel))
    joel_link_texts = {straight(t): u for t, u, _ in joel_links}
    rows = []
    for t, u in base_links:
        k = straight(t)
        if k in real_texts:
            fate = 'REAL'
        elif k in joel_link_texts:
            fate = 'TYPED'
        elif k in joel_plain:
            fate = 'UNLINKED'
        else:
            fate = 'GONE'
        rows.append({'text': t, 'url': u, 'fate': fate, 'his_url': joel_link_texts.get(k)})
    base_texts = {straight(t) for t, _ in base_links}
    new_typed = [{'text': t, 'url': u} for t, u, _ in joel_links if straight(t) not in base_texts and straight(t) not in real_texts]
    out = {'base_commit': BASE_SHA, 'real_hyperlinks_in_his_file': real, 'base_links': rows, 'his_new_typed_links': new_typed,
           'counts': {f: sum(r['fate'] == f for r in rows) for f in ('REAL', 'TYPED', 'UNLINKED', 'GONE')}}
    (HERE / 'LINKS.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    lines = ['# The links in his reorganized guide (turn 116)', '',
             'Base: the guide as I last gave it (commit %s). His file: six real hyperlinks; every other "[text](url)" in it is text '
             'he typed that way. Counts of the base\'s %d links: %s.' % (BASE_SHA[:8], len(rows), json.dumps(out['counts'])), '',
             '| Base link text | Base URL | In his version | His URL |', '|---|---|---|---|']
    for r in rows:
        lines.append('| %s | %s | %s | %s |' % (r['text'].replace('|', '/'), r['url'], r['fate'], r['his_url'] or ''))
    lines += ['', '## Links he typed that the base did not have', '']
    for r in new_typed:
        lines.append('- "%s" → `%s`' % (r['text'], r['url']))
    (HERE / 'LINKS.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps(out['counts']), 'new typed', len(new_typed))


if __name__ == '__main__':
    main()
