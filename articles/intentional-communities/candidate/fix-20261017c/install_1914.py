"""Install section 13 v35 into HUMANIZED-SO-FAR.md (Joel's message of 2026-10-17 19:14 UTC, "i agree with your excl 13 14
ideas"; make_s13_v35.py), in place of v34, with a new ACCEPTED note in front of the old one: the section stays accepted, and the
change is his decision. It goes in only if 420g read the whole section and every check of its changed paragraphs (the exact final
text) Human, with no AI window. Idempotent. Run from candidate/: python3 fix-20261017c/install_1914.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
ART = C / 'HUMANIZED-SO-FAR.md'
R = json.loads((HERE / 'b420' / 'b420-results.json').read_text(encoding='utf-8'))
for k, v in json.loads((HERE / 'b420' / 'aliases.json').read_text(encoding='utf-8')).items():
    R.setdefault(k, R[v])
G = json.loads((HERE / 'b420' / 'GATE.json').read_text(encoding='utf-8'))
H13 = '# Your Little Forming Group Already Is the Community'
KEY = 'S13v35'
parts = [p for p in G[KEY]['parts'] if p != 'installed']
bad = [k for k in [KEY] + parts if k not in R or not R[k][0].startswith('Human') or '; AI' in R[k][3] or R[k][3].startswith('AI')]
assert not bad, bad
new = (C / 's13' / 'v35.md').read_text(encoding='utf-8').strip()
md = ART.read_text(encoding='utf-8')
if new in md:
    print(KEY, 'already in')
else:
    a = md.index(H13)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', md[a + 3:])
    b = a + 3 + m.start()
    md = md[:a] + new + '\n' + md[b:]
    old_note = '<!-- ACCEPTED: section 13 v34'
    i = md.index(old_note)
    note = ('<!-- ACCEPTED: section 13 v35 (2026-10-17): Joel\'s decision of 19:14 UTC on its exclamations ("i agree with your excl '
            '13 14 ideas", the list sent with question 48, fix-20261017b/excl-13-14.md): 15 marks made periods (one, inside a bracket, '
            'simply dropped), one filler phrase out ("There\'s lots you can do!"), four kept, the quoted visitor\'s own kept; one the '
            'list missed ("Not exactly a high bar! 😅", an emoji after its mark) the same way (fix-20261017c/make_s13_v35.py). Held '
            'back after the march reads, each its paragraph\'s only break: the cuts of "Very important!" and "Lots of decisions to '
            'make!" (question 48); the hint\'s mark stays. Pangram web app (420g): every changed paragraph Human alone or with its neighbor, '
            'the whole section %s (%s). Section 14 unchanged. Before: -->\n'
            % (R[KEY][0].replace(' Written', ''), 'https://www.pangram.com/history' + R[KEY][5]))
    md = md[:i] + note + md[i:]
    ART.write_text(md, encoding='utf-8')
    print(KEY, 'installed')
