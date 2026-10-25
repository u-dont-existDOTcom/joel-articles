"""The community article's registered master, brought up to the version Joel accepted and Pangram read as one text
(2026-10-25, after his message of 00:27 UTC: the new version's first whole-article check, Human Written, 0 of 72 windows
AI, https://www.pangram.com/feed/954042b6-e624-4c7f-87d7-db15c547d5c8).

The master (../../master.md) was last made on 2026-10-18 from candidate/HUMANIZED-SO-FAR.md. Since then the article has
lived as his Substack editor HTML: the merge he pasted on 2026-10-18, his own edits in the post (his final paste of
2026-10-20, candidate/joel-20261020/community-final-substack-20261020.html), and then his answers 57 to 63 (2026-10-23 22:29
UTC), 64 (2026-10-24 19:52 UTC), 65 and his kibbutz image (23:40 UTC), all in ../joel-20261024/answer65/WORKING.html. So
the master is now that file as Markdown (the reading copy's conversion without its header), and the steps
PROMOTION-RECEIPT-20261017.md asks for after an accepted change follow: a line in the receipt, the owner locks' note of
which file is which, the editorial status, the detector evidence (the whole-article check), the current state, and the
registry's hashes. original.md, the text first published, stays as the published source and is never edited.

  python3 articles/intentional-communities/candidate/joel-20261025/promote_20261025.py   (from the repo root)
"""
import hashlib, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
CAND = HERE.parent
A = CAND.parent
REPO = A.parents[1]
INDEX = REPO / 'articles' / 'INDEX.json'
WORK = CAND / 'joel-20261024' / 'answer65' / 'WORKING.html'
FEED = 'https://www.pangram.com/feed/954042b6-e624-4c7f-87d7-db15c547d5c8'
WHEN = '2026-10-23 22:29 UTC to 2026-10-24 23:40 UTC'
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
    line = ('- 2026-10-25 (after his message of 00:27 UTC): `master.md` is now `candidate/joel-20261024/answer65/WORKING.html` as '
            'Markdown (`candidate/joel-20261025/promote_20261025.py`; %d UTF-8 bytes, SHA-256 %s; it was %s). That file is his '
            'editor HTML of 2026-10-20, his final paste, with his own edits in the post since this receipt, and his answers '
            '57 to 63 (2026-10-23 22:29 UTC), 64 (2026-10-24 19:52 UTC), and 65 and his kibbutz image (23:40 UTC), each recorded '
            'beside its script. The whole article read Human Written in one Pangram check, 0 of 72 windows AI (%s). The working '
            'copy is that HTML now; `candidate/HUMANIZED-SO-FAR.md` is history.' % (len(master.encode('utf-8')), new_sha, old_sha, FEED))
    if '2026-10-25 (after his message of 00:27 UTC)' not in r:
        r = r.replace('## Changes since\n\n(none yet)', '## Changes since\n\n' + line) if '(none yet)' in r else r.rstrip('\n') + '\n' + line + '\n'
        receipt.write_text(r, encoding='utf-8')

    locks = json.loads((A / 'OWNER-LOCKS.json').read_text(encoding='utf-8'))
    for f in locks['protected_functions']:
        if f['id'] == 'working-master-source-identity':
            f['description'] = ('The registered master is master.md: since 2026-10-25, candidate/joel-20261024/answer65/WORKING.html '
                                '(his editor HTML of 2026-10-20 with his answers 57 to 65 and his kibbutz image, each accepted '
                                'by him, %s) as Markdown, made by candidate/joel-20261025/promote_20261025.py; '
                                'PROMOTION-RECEIPT-20261017.md lists each promotion. The published Substack text first imported '
                                'stays as original.md (97920 UTF-8 bytes, SHA-256 '
                                '5d2892335ba53e93147caf5588a11e660d3ff2180d1ab1b23ff9fc5b2eb99aa6); it is never edited.' % WHEN)
    (A / 'OWNER-LOCKS.json').write_text(json.dumps(locks, ensure_ascii=False, indent=2), encoding='utf-8')   # its own format

    ed = json.loads((A / 'EDITORIAL-STATUS.json').read_text(encoding='utf-8'))
    if not any(a.get('section') == 'the new version (57 to 65)' for a in ed['accepted']):
        ed['accepted'].append({'section': 'the new version (57 to 65)', 'by': 'Joel', 'when': WHEN,
                               'words': '57 a, 58 a, 59 a, 60 a, 61 b, 62 (the essay, then a How-To Manual), 63 a; 64 (22 cuts, 9 '
                                        'kept); 65 (20 cuts, 11 kept) and "after the "preferences and social change" i want to '
                                        'add this image"',
                               'record': 'joel-20261023/joel-20261023-2229-message.txt, joel-20261024/joel-20261024-1952-message.txt, '
                                         'joel-20261024/joel-20261024-2340-message.txt'})
    ed['note'] = (ed.get('note', '') + ' 2026-10-25: his answers 57 to 65 made a new version, the essay then a How-To Manual; '
                  'master.md is that version (PROMOTION-RECEIPT-20261017.md, "Changes since").') if '2026-10-25' not in ed.get('note', '') else ed['note']
    (A / 'EDITORIAL-STATUS.json').write_text(json.dumps(ed, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    det = json.loads((A / 'DETECTOR-EVIDENCE.json').read_text(encoding='utf-8'))
    if not any(x.get('record', '').endswith(FEED) or FEED in x.get('record', '') for x in det['runs']):
        det['runs'].append({'section': 'the whole article', 'version': 'candidate/joel-20261024/answer65/WORKING.html (2026-10-24)',
                            'passage': 'the whole new version, pasted into a temporary Substack draft; the text checked is '
                                       'candidate/joel-20261024/recheck/DRAFT-TEXT.txt (SHA-256 e2ad3e21...)',
                            'service': 'Pangram 4.1, the browser extension\'s check of the draft\'s secret link (free, his account)',
                            'record': 'Human Written, AI fraction 0.0000016%%, document confidence High, 0 of 72 windows AI (37 '
                                      'High, 32 Medium, 3 Low): %s' % FEED,
                            'limitations': 'One run; the check reads the post\'s paragraphs and list items, not headings, '
                                           'captions or alt text.'})
    (A / 'DETECTOR-EVIDENCE.json').write_text(json.dumps(det, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    cs = (A / 'CURRENT-STATE.md').read_text(encoding='utf-8')
    note = ('## Now (2026-10-25)\n\nThe working copy is `candidate/joel-20261024/answer65/WORKING.html`: his editor HTML of '
            '2026-10-20 with his answers 57 to 65 and his kibbutz image, as an essay and then a How-To Manual. It read Human '
            'Written as one text (0 of 72 windows AI, %s), and `master.md` is that version (PROMOTION-RECEIPT-20261017.md). His '
            'post gets it through `exports/COPY-TO-SUBSTACK.html` (receipt `exports/HELPER-RECEIPT-20261025.json`). The '
            'sections below are the history of how the article got here.\n\n' % FEED)
    if '## Now (2026-10-25)' not in cs:
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
