"""Install what batch 423g read Human (the cuts make_tighten.py held on the march, run in Pangram after Joel's 21:37 UTC
observation "it made no difference taking those exclamation phrases out for pangram"): section 13 v37b (three cuts) and section
15 v17 (one cut), each only if 423g read it whole Human with no AI window and every check of its changed paragraphs Human.
Section 13 with all five cuts (S13v37) and with the opening's two (S13v37a) read AI windows, so "It may sound cheesy, but it's
true all the same." and "Until then, what's it worth?" stay. Idempotent. Run from candidate/: python3 fix-20261017d/install_423.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
ART = C / 'HUMANIZED-SO-FAR.md'
R = json.loads((HERE / 'b423' / 'b423-results.json').read_text(encoding='utf-8'))
G = json.loads((HERE / 'b423' / 'GATE.json').read_text(encoding='utf-8'))
ok = lambda k: k in R and R[k][0].startswith('Human') and R[k][3].startswith('Human') and '; AI' not in R[k][3]
link = lambda k: 'https://www.pangram.com/history' + R[k][5]
J = 'Joel\'s message of 21:37 UTC (joel-20261017/joel-20261017-2137-message.txt'
SECT = [
    ('S13v37b', '# Your Little Forming Group Already Is the Community', C / 's13' / 'v37b.md', '<!-- ACCEPTED: section 13 v36',
     'ACCEPTED',
     'section 13 v37b (2026-10-17, after %s, 48 a and 51 a): three cuts the march had held, run in Pangram after his test of two '
     'held cuts ("it made no difference taking those exclamation phrases out for pangram"): "Honestly?" before the book line, "Why '
     'wouldn\'t they be?" and "Yeah, it\'s tough. It\'s also true."; the opening\'s two ("It may sound cheesy, but it\'s true all the '
     'same.", "Until then, what\'s it worth?") stay, since the section read AI windows with them out (423g, S13v37 and S13v37a)' % J),
    ('S15v17', '# What This Looks Like From Sénégal', C / 's15' / 'v17.md', '<!-- CANDIDATE: section 15 v16', 'CANDIDATE',
     'section 15 v17 (2026-10-17, after %s, 51 a): "Can you believe it?" out after his "they won\'t let me pay rent!", a cut the '
     'march had held, run in Pangram after his test of two held cuts' % J),
]
md = ART.read_text(encoding='utf-8')
for key, h1, path, old_note, word, what in SECT:
    parts = [p for p in G[key]['parts'] if p != 'installed']
    bad = [p for p in [key] + parts if not ok(p)]
    if bad:
        print(key, 'not installed:', bad)
        continue
    new = path.read_text(encoding='utf-8').strip()
    if new in md:
        print(key, 'already in'); continue
    a = md.index(h1)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', md[a + 3:])
    md = md[:a] + new + '\n' + md[a + 3 + m.start():]
    i = md.index(old_note)
    note = ('<!-- %s: %s. Pangram web app (423g): every changed paragraph Human alone or with its short neighbor, the whole section '
            '%s (%s). Records: fix-20261017d/. Before: -->\n' % (word, what, R[key][0].replace(' Written', ''), link(key)))
    md = md[:i] + note + md[i:]
    print(key, 'installed')
ART.write_text(md, encoding='utf-8')
for k in ('S13v37', 'S13v37a'):
    print(k, 'stays out:', R[k][0], R[k][1], link(k))
