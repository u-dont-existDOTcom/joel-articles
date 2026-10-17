"""Put a section 16 draft in HUMANIZED-SO-FAR.md in place of the published section (2026-10-17), after every paragraph read
Human alone or in its pair under the same heading (tools/humanization/paragraphs_alone.py must pass over the section's batches)
and the whole section read 100% Human in the web app (the result named on the command line), with the key words PASS. Joel,
2026-10-17 02:07 UTC: "continue, and don't stop because this is overnight run"; 10:47 UTC: "continue".
Run from candidate/: python3 s16/install/install_s16.py DRAFT BATCH KEY NOTE
  DRAFT: the draft's file name in s16/ (for example v25.md); BATCH, KEY: the whole-section result (for example b389 S16v25);
  NOTE: the text of the CANDIDATE note."""
import json, pathlib, subprocess, sys
C = pathlib.Path(__file__).resolve().parents[2]
REPO = C.parents[2]
S16 = C / 's16'
DRAFT, BATCH, KEY, NOTE = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
BATCHES = sorted(str(p) for p in S16.glob('b3*') if (p / 'drafts.json').exists())
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'paragraphs_alone.py'), str(S16 / DRAFT)] + BATCHES,
                   capture_output=True, text=True)
assert r.returncode == 0, 'every paragraph has to read Human alone first:\n' + r.stdout
res = json.loads((S16 / BATCH / ('%s-results.json' % BATCH)).read_text(encoding='utf-8'))[KEY]
assert res[0].startswith('Human') and all(w.startswith('Human') for w in res[3].split('; ')), ('the whole section', res)
drafts = json.loads((S16 / BATCH / 'drafts.json').read_text(encoding='utf-8'))
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402
import re  # noqa: E402
md = (S16 / DRAFT).read_text(encoding='utf-8')
reader = [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip() and not re.match(r'^\[image \d+\]', b.strip())]
whole = '\n\n'.join(plain(re.sub(r'^\[caption\]\s*', '', b).lstrip('#').strip()) if b.startswith('#') or b.startswith('[caption]')
                    else plain(b) for b in reader)
assert drafts[KEY] == whole, 'the checked text is not this draft'
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'preservation_keys.py'), str(S16 / 'preservation-keys.json'),
                    str(S16 / DRAFT), '--article', str(S16 / 'review-r1' / 'article-with-s15v3.md')], capture_output=True, text=True)
assert 'verdict: PASS' in r.stdout, r.stdout
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
H, NEXT = '# Practice Comes Before Property', '<!-- CANDIDATE: the appendix'
a = art.index(H); b = art.index(NEXT, a)
v0 = (S16 / 'v0.md').read_text(encoding='utf-8').strip()
assert art[a:b].strip() == v0, 'the article does not hold the published section 16; stop'
art = art[:a] + '<!-- CANDIDATE: ' + NOTE + ' -->\n' + md.strip() + '\n\n' + art[b:]
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
print('installed section 16', DRAFT)
