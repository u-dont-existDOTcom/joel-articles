"""Promote the accepted humanized article to the registered master (Joel's 45 a of 2026-10-17 21:37 UTC, "Accept it all (sections 1
to 16 and the appendix) once 46 to 51 are settled"; joel-20261017/joel-20261017-2137-message.txt).
- articles/intentional-communities/master.md (make_master.py: the working copy without its version notes) becomes the registered
  master in articles/INDEX.json; original.md, the published Substack text, stays as the published source (role "published_source").
- OWNER-LOCKS.json: the protected function "working-master-source-identity" now says which is which; the owner review is confirmed by
  his acceptance.
- EDITORIAL-STATUS.json: "passed", every section accepted, with his words.
- the receipt is PROMOTION-RECEIPT-20261017.md beside IMPORT-RECEIPT-20261013.md (written by hand, registered here).
The article's status stays "working": the citation review is still pending (the validator allows "owner_final" only after it).
Idempotent. Run from the repo root: python3 articles/intentional-communities/candidate/fix-20261017d/promote.py"""
import hashlib, json, pathlib

REPO = pathlib.Path(__file__).resolve().parents[4]
A = REPO / 'articles' / 'intentional-communities'
INDEX = REPO / 'articles' / 'INDEX.json'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
rel = lambda p: p.relative_to(REPO).as_posix()
WHEN = '2026-10-17 21:37 UTC'
WORDS = '45a'
RECORD = 'articles/intentional-communities/candidate/joel-20261017/joel-20261017-2137-message.txt'
master, original, receipt = A / 'master.md', A / 'original.md', A / 'PROMOTION-RECEIPT-20261017.md'
assert master.exists() and receipt.exists()

locks = json.loads((A / 'OWNER-LOCKS.json').read_text(encoding='utf-8'))
locks['owner_review'] = {'status': 'confirmed',
                         'evidence': '%s: Joel accepted the humanized article ("%s": "Accept it all (sections 1 to 16 and the appendix) once 46 '
                                     'to 51 are settled"), %s; earlier, question 20 and his answer of 2026-10-13 21:00 UTC registered the '
                                     'article without forking the rules.' % (WHEN, WORDS, RECORD)}
for f in locks['protected_functions']:
    if f['id'] == 'working-master-source-identity':
        f['description'] = ('The registered master is master.md, the humanized article Joel accepted on %s ("%s"; PROMOTION-RECEIPT-20261017.md), '
                            'built from candidate/HUMANIZED-SO-FAR.md by candidate/fix-20261017d/make_master.py (the same text without its '
                            'version notes). The published Substack text stays as original.md (97920 UTF-8 bytes, SHA-256 '
                            '5d2892335ba53e93147caf5588a11e660d3ff2180d1ab1b23ff9fc5b2eb99aa6), the published source every section was '
                            'humanized from; it is never edited.' % (WHEN, WORDS))
(A / 'OWNER-LOCKS.json').write_text(json.dumps(locks, ensure_ascii=False, indent=2), encoding='utf-8')   # its own format: no final newline

ed = json.loads((A / 'EDITORIAL-STATUS.json').read_text(encoding='utf-8'))
ed['status'] = 'passed'
ed['note'] = ('Editorial status of the humanized article. Joel accepted all of it on %s ("%s"), so master.md, the article without its '
              'version notes, is the registered master (PROMOTION-RECEIPT-20261017.md). The gate in docs/HUMANIZATION-GATE.md ran on '
              'every section; its records are in candidate/. Sections 13 and 14 were accepted first, on 2026-10-17 02:07 UTC.' % (WHEN, WORDS))
have = {(a['section']) for a in ed['accepted']}
for n in list(range(1, 17)) + ['appendix']:
    if n not in have:
        ed['accepted'].append({'section': n, 'by': 'Joel', 'when': WHEN, 'words': WORDS + ' ("Accept it all (sections 1 to 16 and the '
                               'appendix) once 46 to 51 are settled")', 'record': 'joel-20261017/joel-20261017-2137-message.txt'})
(A / 'EDITORIAL-STATUS.json').write_text(json.dumps(ed, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

idx = json.loads(INDEX.read_text(encoding='utf-8'))
arts = idx['articles'] if isinstance(idx, dict) else idx
art = next(a for a in arts if a['id'] == 'intentional-communities')
art['authority']['master'] = {'path': rel(master), 'sha256': sha(master)}
art['authority']['owner_locks']['sha256'] = sha(A / 'OWNER-LOCKS.json')
art['review']['editorial'].update(sha256=sha(A / 'EDITORIAL-STATUS.json'), status='passed')
extra = art['additional_artifacts']
for path, role in ((original, 'published_source'), (receipt, 'promotion_receipt')):
    e = next((x for x in extra if x['path'] == rel(path)), None)
    if e is None:
        extra.append({'path': rel(path), 'sha256': sha(path), 'role': role})
    else:
        e.update(sha256=sha(path), role=role)
INDEX.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('master', rel(master), sha(master))
