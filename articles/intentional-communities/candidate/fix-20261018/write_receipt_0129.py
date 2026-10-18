"""The promotion receipt for Joel's 45 a (PROMOTION-RECEIPT-20261017.md beside IMPORT-RECEIPT-20261013.md), as it stood after
his message of 2026-10-18 01:29 UTC: written after fix-20261017d/make_master.py and before fix-20261017d/promote.py, which
registers it. Fills in the master's, the working copy's and the published text's sizes and hashes.
Run from candidate/: python3 fix-20261018/write_receipt_0129.py"""
import hashlib, pathlib

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
A = C.parent
master, work, orig = A / 'master.md', C / 'HUMANIZED-SO-FAR.md', A / 'original.md'
h = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
n = lambda p: len(p.read_bytes())
text = f'''# Promotion receipt: Intentional Communities

## What Joel decided

Question 45 on the lane's questions page asked whether to accept the humanized article. Joel, 2026-10-17 21:37 UTC: "45a", that
is, "Accept it all (sections 1 to 16 and the appendix) once 46 to 51 are settled" (`candidate/joel-20261017/joel-20261017-2137-message.txt`).
47 to 51 settled with that message and his answers of 23:10 UTC (`candidate/joel-20261017/joel-20261017-2310-message.txt`). His
answers of 2026-10-18 01:29 UTC (`candidate/joel-20261018/joel-20261018-0129-message.txt`) gave section 2 its last text, his first
paragraph (56 a) and his aside (55 b), which he checked in Pangram himself ("i checked the section, it passes as human when first
part is this"), and asked for the merge: "so i guess now we're done? then when done you can merge the final article into the
substack html".

46 a (the anomie paragraph after his second paragraph, with his screenshot and caption moved to section 2) goes in "once section 2
reads 100% Human with it". That check (batch 428g, `candidate/fix-20261018/b428/`) waits on Pangram: after his message the web app
in the desktop app's browser was signed out and the API key had no credits. So the master has section 2 as he checked it, without
the anomie paragraph, and the screenshot note stays in section 12.

## What changed

- `master.md` is the registered master: the humanized article, `candidate/HUMANIZED-SO-FAR.md` without its version notes
  (`candidate/fix-20261017d/make_master.py`; {n(master)} UTF-8 bytes, SHA-256 {h(master)}). The working copy ({n(work)} bytes,
  SHA-256 {h(work)}) keeps every section's history in its notes and stays where the next changes are made.
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
new hash. Open at promotion: my own Pangram checks of section 2 v3.6 and the anomie paragraph (46 a, batch 428g), the article's
image 7 address, and his upload of the PsyPost screenshot to Substack.

## Changes since

(none yet)
'''
(A / 'PROMOTION-RECEIPT-20261017.md').write_text(text, encoding='utf-8')
print('wrote', A / 'PROMOTION-RECEIPT-20261017.md')
