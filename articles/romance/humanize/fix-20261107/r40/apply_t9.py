#!/usr/bin/env python3
"""His message of 2026-11-24 16:23 UTC as a layer over the fixed version, after r39's: HIS-T9.json, which whole/build.py
applies and whole/fixed_md.py reads for its links and its embed.

- "approved j-b54": card J-B54 of the eighth page (r38/junk/CARDS-T8.json) goes in as the card had it (live 43 and 46),
  with the check that read its section Human High.
- "senegal should be corrected": his "Sênêgal" in the Twin Flames paragraph (live 314) is the English spelling now.
- "double full stop is ok": "joke (LOL).." stays (whole/KEEP-AS-IS.json).
- The contradictions read's item 5: "This goes back to what I said in “doing Idealization right:”" names the section
  "Seeing idealization right" by a name it doesn't have; the pointer takes the heading's name (an obvious correction).
- "i'm replacing the primal attraction section with the following": his-primal.txt, his paste kept byte for byte. It
  replaces the section's opening, live 252 to 260 (the paragraphs before "Muses & Directors"): his first four paragraphs
  take 252 to 259, the YouTube video he put after them sits after them, and his six paragraphs on Cooper take 260. Only
  obvious corrections go in ("no need to ask me for obvious corrections"): "descendents" is spelled "descendants", the
  trailing spaces go, and his three broken links are made whole (a space between "]" and "(", two addresses without
  https://, one ")" too many). His characters stay as he typed them; the typography swap is the live update's.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parent
POST = {}
for line in (FIX / 'live-check' / 'LIVE-POST-BLOCKS-20261123.jsonl').read_text(encoding='utf-8').splitlines():
    r = json.loads(line)
    if r.get('n') is not None:
        POST[r['n']] = r['text']
REPL = json.loads((FIX / 'whole' / 'REPLACEMENTS.json').read_text(encoding='utf-8'))
CARDS = json.loads((FIX / 'r38' / 'junk' / 'CARDS-T8.json').read_text(encoding='utf-8'))
out, links, embeds = [], [], []

# J-B54, approved in chat
for c in CARDS['J-B54']:
    assert POST[c['live']] == c['before'], c['live']
    assert str(c['live']) not in REPL, c['live']
    out.append({'card': 'J-B54', 'kind': 'para', 'live': c['live'], 'before': c['before'], 'after': list(c['after']),
                'comment': 'approved j-b54 (in chat, 2026-11-24 16:23 UTC)', 'his_checks': list(c['his_checks']),
                'section_key': c['section_key']})

# Senegal
cur = REPL['314']
assert len(cur) == 1 and cur[0].count('Sênêgal') == 1
out.append({'card': 'S-314', 'kind': 'para', 'live': 314, 'before': cur[0], 'after': [cur[0].replace('Sênêgal', 'Senegal')],
            'comment': 'senegal should be corrected', 'his_checks': []})

# the contradictions read (r40/contradictions, item 5): his pointer names the section by a name it doesn't have
P329 = REPL['329'][0] if '329' in REPL else POST[329]
assert P329.count('“doing Idealization right:”') == 1
out.append({'card': 'P-329', 'kind': 'para', 'live': 329, 'before': P329,
            'after': [P329.replace('“doing Idealization right:”', '“Seeing idealization right:”')],
            'comment': 'an obvious correction: the section it points back to is "Seeing idealization right"',
            'his_checks': []})

# his Primal attraction opening
raw = (HERE / 'his-primal.txt').read_text(encoding='utf-8')
lines = [l.strip() for l in raw.split('\n') if l.strip()]
assert len(lines) == 11, len(lines)
video = lines[4]
assert re.fullmatch(r'https://www\.youtube\.com/watch\?v=ZsFKlxVUYG8&lc=\S+', video)
paras = lines[:4] + lines[5:]
FIXES = [('descendents', 'descendants', 'a typo'),
         ('[maybe most exemplified in South Korea] (https://', '[maybe most exemplified in South Korea](https://',
          'a space between "]" and "(" left the link broken'),
         ('](nibbana.u-dont-exist.com)', '](https://nibbana.u-dont-exist.com)', 'the address had no https://'),
         ('](systema.innerself.love))', '](https://systema.innerself.love)', 'the address had no https://, and one ")" too many')]
fixed = []
for p in paras:
    for a, b, _ in FIXES:
        p = p.replace(a, b)
    fixed.append(p)
assert sum(p.count(b) for p in fixed for _, b, _ in FIXES) == len(FIXES)
LINK = re.compile(r'\[([^\]]+)\]\((https://[^()\s]+(?:\([^()\s]*\))?[^()\s]*)\)')
plain = []
for p in fixed:
    for m in LINK.finditer(p):
        links.append({'card': 'PRIMAL-1' if len(plain) < 4 else 'PRIMAL-2', 'words': m.group(1), 'href': m.group(2),
                      'why': 'his link, in his paste'})
    t = LINK.sub(lambda m: m.group(1), p)
    assert '](' not in t and '[' not in t, t
    plain.append(t)
assert len(links) == 5, links
run_a, run_b = plain[:4], plain[4:]
out.append({'card': 'PRIMAL-1', 'kind': 'run', 'live': list(range(252, 260)), 'after': run_a,
            'comment': "i'm replacing the primal attraction section with the following", 'his_checks': [],
            'title': 'Primal attraction, the opening: his own new version, part 1'})
out.append({'card': 'PRIMAL-2', 'kind': 'run', 'live': [260], 'after': run_b,
            'comment': "i'm replacing the primal attraction section with the following", 'his_checks': [],
            'title': 'Primal attraction, the opening: his own new version, part 2 (Cooper)'})
embeds.append({'card': 'PRIMAL-1', 'after_live': 252, 'url': video, 'kind': 'youtube',
               'note': 'the YouTube video he put here (2026-11-24), Cooper\'s; his link opens a comment under it',
               'why': 'his paste has it on its own line between his fourth and fifth paragraphs'})
for p in plain:
    assert '  ' not in p and p == p.strip(), p
(HERE / 'HIS-T9.json').write_text(json.dumps({
    'about': 'His message of 2026-11-24 16:23 UTC: J-B54 approved, Senegal corrected, and his new opening of "Primal '
             'attraction" (his-primal.txt) in place of live 252 to 260, with his video and links. Obvious corrections '
             'only: ' + '; '.join('%s (%s)' % (a, w) for a, _, w in FIXES) + '.',
    'whose': 'his', 'changes': out, 'links': links, 'embeds': embeds,
    'his_paste_sha256': __import__('hashlib').sha256(raw.encode('utf-8')).hexdigest()},
    ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('HIS-T9:', len(out), 'changes,', len(links), 'links,', len(embeds), 'embed;', sum(len(p.split()) for p in plain),
      'words of his new text in', len(plain), 'paragraphs')
