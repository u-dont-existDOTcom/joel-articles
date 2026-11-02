"""LIVE-CHECK-20261102.json: his post after the six edits of his answers to Community Article Cards, 1 November.

The edits (SUBSTACK-EDITS-IC1101.json, apply_ic1101.py) went into his post through its editor in the app's browser, the
way the community handoff says (his Substack, signed in): each Find string occurred once, inside one run of text with no
marks; the six replacements went in as one editor transaction (each old string then 0 times, each new one once); the
draft saved (Substack's draft record had all six); Update, then "Update now" in Substack's dialog, with the audience and
settings untouched. The title still reads "Updated: Nov 1 2026", as he set it.

The public post was then read through Substack's API without signing in, from the laptop
(inbox/ic-live-20261102/post.json, its body_html the same SHA-256 the browser read). This script compares its words with
WORKING-20261102.md in order and records every difference.

  python3 .../sections/review/record_live_ic1101.py POST.json
"""
import difflib
import hashlib
import html
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
URL = 'https://ibogaqueen.substack.com/p/building-healing-community-escuelitas'
EDITOR = 'https://ibogaqueen.substack.com/publish/post/198340475'


def words(s):
    s = re.sub(r'!\[[^\]]*\]\([^)]*\)', ' ', s)
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)
    s = re.sub(r'[*_#>`|]', ' ', s)
    return re.findall(r"[\w’'-]+", s)


def main():
    post = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))
    body = post['body_html']
    text = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', body)))
    edits = json.loads((HERE / 'SUBSTACK-EDITS-IC1101.json').read_text(encoding='utf-8'))
    work = (HERE / 'WORKING-20261102.md').read_text(encoding='utf-8')
    a, b = words(work), words(text)
    diffs = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes():
        if op == 'equal':
            continue
        w, l_ = ' '.join(a[i1:i2]), ' '.join(b[j1:j2])
        if re.fullmatch(r'[-\d\s]*', w) and not l_:
            kind = 'a horizontal rule or list number (Markdown only)'
        elif not l_ and re.search(r'Copy link|Double click to interact with video|Read full story', w):
            kind = 'an embed\'s own text in the working Markdown (the editor\'s chrome, not the article\'s words)'
        else:
            kind = 'WORDS'
        diffs.append({'working': w, 'live': l_, 'kind': kind})
    word_diffs = [d for d in diffs if d['kind'] == 'WORDS']
    rec = {
        'about': __doc__.split('\n\n')[1].replace('\n', ' '),
        'post': {'url': URL, 'editor': EDITOR, 'title': post['title'], 'audience': post['audience'],
                 'post_date': post['post_date'],
                 'body_html_sha256': hashlib.sha256(body.encode('utf-8')).hexdigest()},
        'editor_doc_sha256': {'before': 'd3e578587c336cd4af6cb6bbecb14e5917ebbe1198d5ab459a3d4087da21a339',
                              'after': '421a7902762364aa636c7624af6376616732aeb1ba43e7c31fc5b4cc7ddb3033'},
        'the_six_edits_live': [{'cards': e['cards'], 'find_left': text.count(e['find']),
                                'replace_live': text.count(e['replace'])} for e in edits['edits']],
        'all_six': all(text.count(e['find']) == 0 and text.count(e['replace']) == 1 for e in edits['edits']),
        'live_against_working': {
            'working': 'WORKING-20261102.md, SHA-256 ' + hashlib.sha256(work.encode('utf-8')).hexdigest(),
            'working_words': len(a), 'live_words': len(b),
            'method': 'the words of the live body_html (tags stripped) against the words of the working Markdown with its '
                      'links, images and emphasis marks stripped, in order (difflib)',
            'differences': len(diffs), 'word_differences': len(word_diffs), 'list': diffs}}
    assert rec['all_six'], rec['the_six_edits_live']
    (HERE / 'LIVE-CHECK-20261102.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('all six live:', rec['all_six'], '| differences', len(diffs), '| word differences', len(word_diffs))


if __name__ == '__main__':
    main()
