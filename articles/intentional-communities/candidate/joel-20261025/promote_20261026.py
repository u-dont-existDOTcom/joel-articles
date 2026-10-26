"""The community article's registered master, brought up to the version in Joel's post since his message of 2026-10-26
00:54 UTC ("and i made the changes on the community article that's done"): candidate/joel-20261025/answer66/WORKING.html,
which is the last master's version (answer65/WORKING.html) with his answers to question 66 in (IC-E1, IC-E2, IC-E3 and
IC-T1, 2026-10-25 23:05 UTC; apply_66.py, RECORD-66.json), the five changes he made in his post himself from
SUBSTACK-EDITS.md.

His post (https://ibogaqueen.substack.com/p/building-healing-community-escuelitas, "Updated: Oct 25 2026") was read in
the app's browser in the turn of his message: its text, read the way Pangram's check reads it (272 lines), equals
answer66/WORKING.html's checked text line for line except two spaces the post's own rendering drops (a double space
after "starting a commune." made single, and the space before a line break after "labeled as such."), and holds all
five new sentences (PROMOTE-CHECK-20261026.json). The steps after an accepted change are the last promotion's
(promote_20261025.py): the receipt's line, the owner locks' note of which file is which, the editorial status, the
detector evidence (batch 478g's API checks of the changed paragraphs), the current state, and the registry's hashes.
original.md, the text first published, stays as the published source and is never edited.

  python3 articles/intentional-communities/candidate/joel-20261025/promote_20261026.py   (from the repo root)
"""
import hashlib, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
CAND = HERE.parent
A = CAND.parent
REPO = A.parents[1]
INDEX = REPO / 'articles' / 'INDEX.json'
WORK = CAND / 'joel-20261025' / 'answer66' / 'WORKING.html'
FEED = 'https://www.pangram.com/feed/954042b6-e624-4c7f-87d7-db15c547d5c8'   # the last whole-article check (the version before 66)
B478 = 'candidate/joel-20261025/answer66/b478/PREDICTIONS.md'
WHEN = '2026-10-25 23:05 UTC (his answers to 66) and 2026-10-26 00:54 UTC (the changes in his post)'
sha = lambda p: hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
rel = lambda p: pathlib.Path(p).relative_to(REPO).as_posix()
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import clarity_read as C  # noqa: E402


def words(t):
    t = t.translate(str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'", '\xa0': ' '}))
    return re.sub(r'[^\w]+', ' ', t.lower()).split()


def main():
    from markdownify import markdownify
    html = WORK.read_text(encoding='utf-8')
    master = re.sub(r'\n{3,}', '\n\n', markdownify(re.sub(r'<(strong|em|b|i|u|s|a)\b[^>]*>(\s+)</\1>', r'\2', html), heading_style='ATX', bullets='-', strip=['span'])).strip() + '\n'
    # markdownify writes a <br> as two trailing spaces; a backslash is the same line break without trailing whitespace
    # (git diff --check)
    master = re.sub(r' {2,}\n', '\\\n', master)
    master = re.sub(r'[ \t]+\n', '\n', master)
    # every word the check reads is in the master, in order (the master also has headings, captions and links' addresses)
    import substack_check_text as S
    body = words(S.checked_text(html, limit=10 ** 9))   # the text Pangram reads, without the reading text's image markers
    have = words(master)
    k = 0
    for w in body:
        k = have.index(w, k) + 1
    out = A / 'master.md'
    old_sha = sha(out)
    out.write_text(master, encoding='utf-8')
    new_sha = sha(out)

    receipt = A / 'PROMOTION-RECEIPT-20261017.md'
    r = receipt.read_text(encoding='utf-8')
    line = ('- 2026-10-26 (after his message of 00:54 UTC): `master.md` is now `candidate/joel-20261025/answer66/WORKING.html` as '
            'Markdown (`candidate/joel-20261025/promote_20261026.py`; %d UTF-8 bytes, SHA-256 %s; it was %s). That file is the '
            'last master\'s version with his answers to 66 in (IC-E1, IC-E2, IC-E3 and IC-T1, his message of 2026-10-25 23:05 UTC; '
            '`candidate/joel-20261025/answer66/apply_66.py`), which he made in his post himself as five changes ("and i made the '
            'changes on the community article that\'s done"); his post was read in the browser that turn and matches it line for '
            'line (`candidate/joel-20261025/answer66/PROMOTE-CHECK-20261026.json`). Each changed paragraph read Human through the '
            'API (batch 478g, %s).' % (len(master.encode('utf-8')), new_sha, old_sha, B478))
    if '2026-10-26 (after his message of 00:54 UTC)' not in r:
        r = r.replace('## Changes since\n\n(none yet)', '## Changes since\n\n' + line) if '(none yet)' in r else r.rstrip('\n') + '\n' + line + '\n'
        receipt.write_text(r, encoding='utf-8')

    locks = json.loads((A / 'OWNER-LOCKS.json').read_text(encoding='utf-8'))
    for f in locks['protected_functions']:
        if f['id'] == 'working-master-source-identity':
            f['description'] = ('The registered master is master.md: since 2026-10-26, candidate/joel-20261025/answer66/WORKING.html '
                                '(his editor HTML of 2026-10-20 with his answers 57 to 66 and his kibbutz image, each accepted '
                                'by him, the last on %s) as Markdown, made by candidate/joel-20261025/promote_20261026.py; '
                                'PROMOTION-RECEIPT-20261017.md lists each promotion. The published Substack text first imported '
                                'stays as original.md (97920 UTF-8 bytes, SHA-256 '
                                '5d2892335ba53e93147caf5588a11e660d3ff2180d1ab1b23ff9fc5b2eb99aa6); it is never edited.' % WHEN)
    (A / 'OWNER-LOCKS.json').write_text(json.dumps(locks, ensure_ascii=False, indent=2), encoding='utf-8')   # its own format

    ed = json.loads((A / 'EDITORIAL-STATUS.json').read_text(encoding='utf-8'))
    if not any(a.get('section') == 'question 66 (the Emulate check)' for a in ed['accepted']):
        ed['accepted'].append({'section': 'question 66 (the Emulate check)', 'by': 'Joel', 'when': WHEN,
                               'words': '"66a" with his answers file: IC-E1, IC-E2, IC-E3 and IC-T1 approved, IC-Q1 and IC-E4 rejected; '
                                        'then "and i made the changes on the community article that\'s done"',
                               'record': 'joel-20261025/joel-20261025-2305-message.txt, joel-20261025/joel-20261026-0054-message.txt, '
                                         'joel-20261025/answer66/RECORD-66.json'})
    if '2026-10-26' not in ed.get('note', ''):
        ed['note'] = ed.get('note', '') + (' 2026-10-26: his answers to 66 are in his post and in master.md '
                                           '(PROMOTION-RECEIPT-20261017.md, "Changes since").')
    (A / 'EDITORIAL-STATUS.json').write_text(json.dumps(ed, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    det = json.loads((A / 'DETECTOR-EVIDENCE.json').read_text(encoding='utf-8'))
    if not any(B478 in x.get('record', '') for x in det['runs']):
        det['runs'].append({'section': 'the four paragraphs question 66 changed', 'version': 'candidate/joel-20261025/answer66/WORKING.html (2026-10-25)',
                            'passage': 'each changed paragraph where it sits (IC-E1 with the paragraph before it), through the API on his laptop',
                            'service': 'Pangram API (model pangram-4, answered 4.1), his key',
                            'record': 'IC-E2, IC-E3 and IC-T1 Human (High) alone; IC-E1 with the paragraph before it Mixed, its AI window '
                                      '(Low) in the unchanged paragraph before, which reads Human (High) alone: ' + B478,
                            'limitations': 'Paragraph checks, not the whole article; the last whole-article check (%s) read the '
                                           'version before 66, Human Written, 0 of 72 windows AI.' % FEED})
    (A / 'DETECTOR-EVIDENCE.json').write_text(json.dumps(det, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    cs = (A / 'CURRENT-STATE.md').read_text(encoding='utf-8')
    note = ('## Now (2026-10-26)\n\nThe working copy is `candidate/joel-20261025/answer66/WORKING.html`: the 2026-10-25 version with '
            'his answers to 66 in, which he made in his post himself (his message of 2026-10-26 00:54 UTC); his post matches it '
            '(`candidate/joel-20261025/answer66/PROMOTE-CHECK-20261026.json`), and `master.md` is that version '
            '(PROMOTION-RECEIPT-20261017.md). Nothing is waiting on him in this lane. The sections below are the history of how '
            'the article got here.\n\n')
    if '## Now (2026-10-26)' not in cs:
        k2 = cs.index('\n## ')
        cs = cs[:k2 + 1] + note + cs[k2 + 1:]
        (A / 'CURRENT-STATE.md').write_text(cs, encoding='utf-8')

    idx = json.loads(INDEX.read_text(encoding='utf-8'))
    arts = idx['articles'] if isinstance(idx, dict) else idx
    art = next(a for a in arts if a['id'] == 'intentional-communities')
    art['authority']['master']['sha256'] = new_sha
    art['authority']['owner_locks']['sha256'] = sha(A / 'OWNER-LOCKS.json')
    art['authority']['current_state']['sha256'] = sha(A / 'CURRENT-STATE.md')
    art['review']['editorial']['sha256'] = sha(A / 'EDITORIAL-STATUS.json')
    art['review']['detector']['sha256'] = sha(A / 'DETECTOR-EVIDENCE.json')
    e = next(x for x in art['additional_artifacts'] if x['path'] == rel(receipt))
    e['sha256'] = sha(receipt)
    # ARCHITECTURE.md was redrawn by hand in the same change for the essay and How-To Manual (articles/AGENTS.md: update it
    # whenever the section order changes); its role is one the registration script leaves to a person
    e = next(x for x in art['additional_artifacts'] if x['path'] == rel(A / 'ARCHITECTURE.md'))
    e['sha256'] = sha(A / 'ARCHITECTURE.md')
    INDEX.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('master.md', new_sha, len(master.encode('utf-8')), 'bytes (was %s)' % old_sha[:12])


if __name__ == '__main__':
    main()
