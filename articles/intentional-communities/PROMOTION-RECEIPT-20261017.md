# Promotion receipt: Intentional Communities

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
  (`candidate/fix-20261017d/make_master.py`; 123954 UTF-8 bytes, SHA-256 2dcfdb297923ceb1352f81adeed1218278d28a168e78846aebcf63d92205fbe2). The working copy (149465 bytes,
  SHA-256 f1add2759a4ced7e53159b1b71cc2cae99f244c7d864ba380d84bd96e49ee884) keeps every section's history in its notes and stays where the next changes are made.
- `original.md`, the published Substack text (97920 bytes, SHA-256 5d2892335ba53e93147caf5588a11e660d3ff2180d1ab1b23ff9fc5b2eb99aa6), stays as the published source (role
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
