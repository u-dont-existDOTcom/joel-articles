"""Question 67, answered: Joel's own fix of the anomie sentence, in his post and in master.md.

His message of 2026-11-02 17:40 UTC (joel-20261102-1740-message.txt here, word for word): "67 i fixed it by removing the
obvious ai part which i didn't write", with his Pangram check of the whole section (Human Written, one window Human
(High), 412 words: https://www.pangram.com/history/7813bbfe-30db-4f31-a17f-2937f4e465bf) and the section as he checked
it. His section differs from his post in one place only: "the shared norms and close ties that held those groups
together fall apart, and" is gone (words of ours from an earlier round, not his).

The edit went into his post through its editor, as on 1 and 2 November: the Find string once, in one run of text with no
marks; one transaction (the editor's document 421a7902 before, fcd20edb after); the draft saved; Update, then "Update now"
(Substack's publish call answered 200; the public post showed the change about three minutes later). The public post,
read through Substack's API from the laptop without signing in (POST.json), has the change and the working copy's words.

  python3 .../sections/review/q67/apply_q67.py POST.json
Writes WORKING-20261102b.md and LIVE-CHECK-Q67.json here, and promotes master.md as promote_20261102.py does.
"""
import difflib
import hashlib
import html
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
A = HERE.parents[6]
REPO = A.parents[1]
INDEX = REPO / 'articles' / 'INDEX.json'
FIND = ('In a large society, the shared norms and close ties that held those groups together fall apart, and nobody knows '
        'anybody')
REPLACE = 'In a large society, nobody knows anybody'
NEW = ('In a large society, nobody knows anybody well enough or for long enough to tell who can be trusted—even your '
       'next-door neighbor is often a total stranger.')
HIS_CHECK = 'https://www.pangram.com/history/7813bbfe-30db-4f31-a17f-2937f4e465bf'
WHEN = '2026-11-02 17:40 UTC (his answer to question 67, with his Pangram check of the section)'


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def rel(p):
    return pathlib.Path(p).relative_to(REPO).as_posix()


def words(s):
    s = re.sub(r'!\[[^\]]*\]\([^)]*\)', ' ', s)
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)
    s = re.sub(r'[*_#>`|]', ' ', s)
    return re.findall(r"[\w’'-]+", s)


def main():
    post = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))
    master = A / 'master.md'
    old = master.read_text(encoding='utf-8')
    old_sha = sha(master)
    work_f = HERE / 'WORKING-20261102b.md'
    if NEW in old:
        work = old
    else:
        assert old.count(FIND) == 1, 'the Find string is not in master.md once'
        work = old.replace(FIND, REPLACE)
    assert work.count(NEW) == 1
    work_f.write_text(work, encoding='utf-8')
    body = post['body_html']
    text = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', body)))
    assert text.count(NEW) == 1 and 'the shared norms and close ties' not in text, 'the change is not live'
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
    wd = [d for d in diffs if d['kind'] == 'WORDS']
    assert not wd, wd[:3]
    live = {'about': __doc__.split('\n\n')[2].replace('\n', ' '),
            'his_message': 'joel-20261102-1740-message.txt', 'his_check': HIS_CHECK,
            'find': FIND, 'replace': REPLACE,
            'editor_doc_sha256': {'before': '421a7902762364aa636c7624af6376616732aeb1ba43e7c31fc5b4cc7ddb3033',
                                  'after': 'fcd20edb21eed6ecfaeee43368521b41304856dc2cc9730f363d98e3b3b28d8d'},
            'post': {'title': post['title'], 'audience': post['audience'], 'post_date': post['post_date'],
                     'body_html_sha256': hashlib.sha256(body.encode('utf-8')).hexdigest()},
            'live_against_working': {'working': 'WORKING-20261102b.md, SHA-256 ' + hashlib.sha256(work.encode('utf-8')).hexdigest(),
                                     'differences': len(diffs), 'word_differences': 0, 'list': diffs}}
    (HERE / 'LIVE-CHECK-Q67.json').write_text(json.dumps(live, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if old == work:
        print('master.md has it already')
        return
    master.write_text(work, encoding='utf-8')
    new_sha = sha(master)
    receipt = A / 'PROMOTION-RECEIPT-20261017.md'
    r = receipt.read_text(encoding='utf-8')
    if '2026-11-02 (after his message of 17:40 UTC)' not in r:
        r = r.rstrip('\n') + '\n' + ('- 2026-11-02 (after his message of 17:40 UTC): `master.md` is now `%s` (`%s`; %d UTF-8 '
                                     'bytes, SHA-256 %s; it was %s): his own fix of the anomie sentence (question 67), made '
                                     'in his post through its editor and read back from the public post (`%s`).'
                                     % (rel(work_f), rel(pathlib.Path(__file__)), len(work.encode('utf-8')), new_sha,
                                        old_sha, rel(HERE / 'LIVE-CHECK-Q67.json'))) + '\n'
        receipt.write_text(r, encoding='utf-8')
    locks = json.loads((A / 'OWNER-LOCKS.json').read_text(encoding='utf-8'))
    for f in locks['protected_functions']:
        if f['id'] == 'working-master-source-identity':
            f['description'] = ('The registered master is master.md: since 2026-11-02 17:40 UTC, %s (the master of the same '
                                'day with his own fix of question 67, %s), put in place by %s; PROMOTION-RECEIPT-20261017.md '
                                'lists each promotion. The published Substack text first imported stays as original.md '
                                '(97920 UTF-8 bytes, SHA-256 5d2892335ba53e93147caf5588a11e660d3ff2180d1ab1b23ff9fc5b2eb99aa6); '
                                'it is never edited.' % (rel(work_f), WHEN, rel(pathlib.Path(__file__))))
    (A / 'OWNER-LOCKS.json').write_text(json.dumps(locks, ensure_ascii=False, indent=2), encoding='utf-8')
    ed = json.loads((A / 'EDITORIAL-STATUS.json').read_text(encoding='utf-8'))
    if not any(x.get('section') == 'question 67 (2 November)' for x in ed['accepted']):
        ed['accepted'].append({'section': 'question 67 (2 November)', 'by': 'Joel', 'when': WHEN,
                               'words': '67 i fixed it by removing the obvious ai part which i didn\'t write',
                               'record': '%s, %s' % (rel(HERE / 'joel-20261102-1740-message.txt'),
                                                     rel(HERE / 'LIVE-CHECK-Q67.json'))})
    (A / 'EDITORIAL-STATUS.json').write_text(json.dumps(ed, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    cs = (A / 'CURRENT-STATE.md').read_text(encoding='utf-8')
    old_now = cs[cs.index('## Now (2026-11-02)'):cs.index('\n## ', cs.index('## Now (2026-11-02)') + 5) + 1]
    new_now = ('## Now (2026-11-02)\n\n`master.md` is his post as of 2 November: the master of 1 November with the six '
               'edits of his answers to Community Article Cards, 1 November, and his own fix of the anomie sentence '
               '(question 67, his message of 17:40 UTC), each made in his post through its editor and read back from the '
               'public post (`%s`, `%s`). Both sections those edits touched read Human Written by themselves; his check of '
               'Communes Are Hot Again with his fix reads Human (High) throughout (%s). Nothing is waiting in this lane. The '
               'sections below are the history of how the article got here.\n\n'
               % (rel(HERE.parent / 'LIVE-CHECK-20261102.json'), rel(HERE / 'LIVE-CHECK-Q67.json'), HIS_CHECK))
    cs = cs.replace(old_now, new_now)
    (A / 'CURRENT-STATE.md').write_text(cs, encoding='utf-8')
    idx = json.loads(INDEX.read_text(encoding='utf-8'))
    arts = idx['articles'] if isinstance(idx, dict) else idx
    art = next(x for x in arts if x['id'] == 'intentional-communities')
    art['authority']['master']['sha256'] = new_sha
    art['authority']['owner_locks']['sha256'] = sha(A / 'OWNER-LOCKS.json')
    art['authority']['current_state']['sha256'] = sha(A / 'CURRENT-STATE.md')
    art['review']['editorial']['sha256'] = sha(A / 'EDITORIAL-STATUS.json')
    art['review']['detector']['sha256'] = sha(A / 'DETECTOR-EVIDENCE.json')
    e = next(x for x in art['additional_artifacts'] if x['path'] == rel(receipt))
    e['sha256'] = sha(receipt)
    INDEX.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('master.md', new_sha[:12], '(was %s); differences %d, word differences 0' % (old_sha[:12], len(diffs)))


if __name__ == '__main__':
    main()
