"""The registered master of the community article, from the accepted humanized article (Joel's 45 a of 2026-10-17 21:37 UTC:
"Accept it all (sections 1 to 16 and the appendix) once 46 to 51 are settled").
candidate/HUMANIZED-SO-FAR.md stays the working copy, with every section's history in its notes; the master is the same article
without those notes: the version-history comments in front of each section (<!-- CANDIDATE: ... -->, <!-- ACCEPTED: ... -->,
<!-- Section ... -->) come out, and everything else stays as it is, the image notes for images still to be uploaded included.
After any accepted change to the working copy, run this again and record it with a receipt (PROMOTION-RECEIPT-20261017.md says
how). Writes articles/intentional-communities/master.md. Run from candidate/: python3 fix-20261017d/make_master.py"""
import hashlib, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
work = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
NOTE = re.compile(r'^<!-- (CANDIDATE|ACCEPTED|Section)\b.*?-->\n', flags=re.S | re.M)
master = NOTE.sub('', work)
master = re.sub(r'\n{3,}', '\n\n', master).strip() + '\n'
# every heading and paragraph of the working copy is in the master, in order; only the notes are gone
strip = lambda t: [b.strip() for b in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', t, flags=re.S)) if b.strip()]
assert strip(master) == strip(work), 'the master must be the working copy without its notes'
out = C.parent / 'master.md'
out.write_text(master, encoding='utf-8')
print(out, len(master.encode('utf-8')), 'bytes, sha256', hashlib.sha256(master.encode('utf-8')).hexdigest())
print('notes taken out:', len(NOTE.findall(work)), '; other comments kept:', len(re.findall(r'<!--', master)))
