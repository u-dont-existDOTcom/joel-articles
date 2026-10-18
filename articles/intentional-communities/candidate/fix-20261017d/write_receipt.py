"""The promotion receipt for Joel's 45 a (PROMOTION-RECEIPT-20261017.md beside IMPORT-RECEIPT-20261013.md), written after
make_master.py and before promote.py, which registers it. Fills in the master's and the working copy's sizes and hashes.
Run from candidate/: python3 fix-20261017d/write_receipt.py BATCH_KEY  (the section 2 check that settled 46, e.g. S2v35c)"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
A = C.parent
key = sys.argv[1]
R = json.loads((HERE / 'b425' / 'b425-results.json').read_text(encoding='utf-8'))
master, work, orig = A / 'master.md', C / 'HUMANIZED-SO-FAR.md', A / 'original.md'
h = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
n = lambda p: len(p.read_bytes())
text = f'''# Promotion receipt: Intentional Communities, 2026-10-17

## What Joel decided

Question 45 on the lane's questions page asked whether to accept the humanized article. Joel, 2026-10-17 21:37 UTC: "45a", that
is, "Accept it all (sections 1 to 16 and the appendix) once 46 to 51 are settled" (`candidate/joel-20261017/joel-20261017-2137-message.txt`).
The last of 46 to 51 settled with his answers of 23:10 UTC (52 to 54, `candidate/joel-20261017/joel-20261017-2310-message.txt`):
section 2 read 100% Human with his opening, the anomie paragraph and his screenshot (batch 425g, {key}:
https://www.pangram.com/history{R[key][5]}).

## What changed

- `master.md` is the registered master: the humanized article, `candidate/HUMANIZED-SO-FAR.md` without its version notes
  (`candidate/fix-20261017d/make_master.py`; {n(master)} UTF-8 bytes, SHA-256 {h(master)}). The working copy ({n(work)} bytes, SHA-256
  {h(work)}) keeps every section's history in its notes and stays where the next changes are made.
- `original.md`, the published Substack text ({n(orig)} bytes, SHA-256 {h(orig)}), stays as the published source (role
  "published_source"), the text every section was humanized from. It is never edited.
- `OWNER-LOCKS.json`: the owner review is confirmed by his acceptance, and the protected function "working-master-source-identity"
  says which file is which.
- `EDITORIAL-STATUS.json`: "passed", every section accepted with his words.
- `articles/INDEX.json`: the master's path and hash, `original.md` as the published source and this receipt as the promotion
  receipt (`candidate/fix-20261017d/promote.py`).
- The article's status stays "working": the claim-level citation review (`CITATIONS.json`) is still pending, and the validator
  allows "owner_final" only after it.

## After promotion

Any change Joel accepts goes into the working copy first, with its checks, then `make_master.py` again and a line here with the
new hash. Open at promotion: question 55 (the source of his section 2 aside), the article's image 7 address, and his upload of the
PsyPost screenshot to Substack.

## Changes since

(none yet)
'''
(A / 'PROMOTION-RECEIPT-20261017.md').write_text(text, encoding='utf-8')
print('wrote', A / 'PROMOTION-RECEIPT-20261017.md')
