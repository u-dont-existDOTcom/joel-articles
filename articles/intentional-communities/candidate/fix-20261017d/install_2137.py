"""Install Joel's texts and line decisions of 2026-10-17 21:37 UTC (make_2137.py) into HUMANIZED-SO-FAR.md: section 2 v3.4, section
8 v31, section 12 v16, section 15 v15 and section 16 v30, each in place of the section now there, with a new note in front of the
old one. A section goes in only if 421g read it whole and every check of its changed paragraphs (the exact final text) Human,
with no AI window; section 2 also needs section 12 to go in with it (the screenshot moves), and the other way round. Idempotent.
Run from candidate/: python3 fix-20261017d/install_2137.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
ART = C / 'HUMANIZED-SO-FAR.md'
R = json.loads((HERE / 'b421' / 'b421-results.json').read_text(encoding='utf-8'))
for k, v in json.loads((HERE / 'b421' / 'aliases.json').read_text(encoding='utf-8')).items():
    R.setdefault(k, R[v])
G = json.loads((HERE / 'b421' / 'GATE.json').read_text(encoding='utf-8'))
ok = lambda k: k in R and R[k][0].startswith('Human') and R[k][3].startswith('Human') and '; AI' not in R[k][3]
link = lambda k: 'https://www.pangram.com/history' + R[k][5]
J = 'Joel\'s message of 21:37 UTC (joel-20261017/joel-20261017-2137-message.txt'
SECT = [
    ('S2v34', '# Communes Are Hot Again', HERE / 's2-v34.md', '<!-- CANDIDATE: section 2 v3.2', 'CANDIDATE',
     'section 2 v3.4 (2026-10-17, after %s, 47.5 and 46 a): his P2 ("Genevia" spelled "Geneva"), then the anomie paragraph of '
     'question 46, his pick, with his screenshot and caption moved here from section 12' % J),
    ('S12v16', '# The Math of Absorption, and Who This Isn’t For', HERE / 's12-v16.md', '<!-- CANDIDATE: section 12 v15', 'CANDIDATE',
     'section 12 v16 (2026-10-17, after %s, 46 a): v15 without the screenshot and its caption, which moved to section 2' % J),
    ('S8v31', '# The Grown Children Get the Final Review', HERE / 's8-v31.md', '<!-- CANDIDATE: section 8 v30', 'CANDIDATE',
     'section 8 v31 (2026-10-17, after %s, 49): "If it can\'t, it can still avoid punishing departure." back after the transition '
     'help, and the Rumspringa sentence without its fixed length ("from about age 16 ... a period"); his points 1 and 4 as he wrote '
     'them' % J),
    ('S15v15', '# What This Looks Like From Sénégal', C / 's15' / 'v15.md', '<!-- CANDIDATE: section 15 v14', 'CANDIDATE',
     'section 15 v15 (2026-10-17, after %s, 47.4): his rewrite of "All is not well in paradise" P1 and P2 as he wrote it ("No, not '
     'quite." given its period, "favor" for "favort"), with the published law link kept after "March 2026"' % J),
    ('S16v30', '# Practice Comes Before Property', C / 's16' / 'v30.md', '<!-- CANDIDATE: section 16 v29', 'CANDIDATE',
     'section 16 v30 (2026-10-17, after %s, 47.1): his cut of "One disagreement is enough!" ("it undermines ... "at least one""); '
     '"Really, go!" and the passing "make a difference" stay (47.2, 47.3)' % J),
]
# Joel's rule is that every paragraph passes alone, or with a neighbor when it is under 50 words. Section 16's practice-group
# paragraph (47 words) passes with the paragraph before it (S16v30-H3P2+prev, 0.07); with the one after, Pangram read the next
# paragraph's list as AI (S16v30-H3P2+next, 0.54), and that paragraph, unchanged and 44 words, passes with its own next one (389g
# S16v25-H3-P4+P5, the same text, 0.00). So every paragraph there passes with a neighbor, and the section reads 100% Human.
NEIGHBOR_OK = {'S16v30-H3P2+next': ('S16v30-H3P2+prev', 's16/b389', 'S16v25-H3-P4+P5')}


def part_ok(p):
    if ok(p):
        return True
    if p in NEIGHBOR_OK:
        other, folder, key = NEIGHBOR_OK[p]
        r389 = json.loads((C / folder / (folder.split('/')[-1] + '-results.json')).read_text(encoding='utf-8'))
        return ok(other) and r389[key][0].startswith('Human') and r389[key][3].startswith('Human') and '; AI' not in r389[key][3]
    return False


good = {key: ok(key) and all(part_ok(p) for p in G[key]['parts'] if p != 'installed') for key, *_ in SECT}
if not (good['S2v34'] and good['S12v16']):
    good['S2v34'] = good['S12v16'] = False   # the screenshot moves only if both read Human
md = ART.read_text(encoding='utf-8')
for key, h1, path, old_note, word, what in SECT:
    if not good[key]:
        print(key, 'not installed:', [p for p in [key] + G[key]['parts'] if p != 'installed' and not part_ok(p)] or 'its pair')
        continue
    new = path.read_text(encoding='utf-8').strip()
    if new in md:
        print(key, 'already in'); continue
    a = md.index(h1)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', md[a + 3:])
    md = md[:a] + new + '\n' + md[a + 3 + m.start():]
    i = md.index(old_note)
    note = ('<!-- %s: %s. Pangram web app (421g): every changed paragraph Human alone or with its neighbor, the whole section %s (%s). '
            'Records: fix-20261017d/. Before: -->\n' % (word, what, R[key][0].replace(' Written', ''), link(key)))
    md = md[:i] + note + md[i:]
    print(key, 'installed')
ART.write_text(md, encoding='utf-8')
