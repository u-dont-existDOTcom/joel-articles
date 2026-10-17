"""Put this turn's sections in HUMANIZED-SO-FAR.md (2026-10-17, after Joel's 13:11 message): section 16 v28 in place of the
published section, and section 15 v13, section 4 v11.4, section 12 v14, section 8 v30 and section 1 (the sweep) in place of
their installed versions. It refuses unless every changed paragraph read Human alone or with its neighbor (410g, 411g), every
changed section read 100% Human as a whole (411g, 412g), the key files pass where a section has one, the linter finds no FAIL
in the new text, and the repeated pauses of sections 15 and 16 are answered.
Run from candidate/: python3 fix-20261017/install_20261017.py"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
T = REPO / 'tools' / 'humanization'
py = sys.executable
R = {}
for b in ('b410', 'b411', 'b412'):
    R.update(json.loads((HERE / b / ('%s-results.json' % b)).read_text(encoding='utf-8')))


def human(k):
    r = R[k]
    return r[0].startswith('Human') and all(w.startswith('Human') for w in r[3].split('; '))


PARAS = ['S16v28-H1P3', 'S16v28-H1P3+prev', 'S16v28-H3P7+prev', 'S16v28-H3P7+next', 'S15v13-H1P3', 'S15v13-H1P3+prev',
         'S15v13-H2P2', 'S15v13-H2P2+prev', 'S15v13-H3P3', 'S15v13-H3P5', 'S4v114-container+prev', 'S4v114-container+next',
         'S1sw-EastWind', 'S1sw-EastWind+prev', 'S8v30-safeguards+prev', 'S8v30-safeguards+next']
S12PARAS = [k for k in R if k.startswith('S12v14-')]
WHOLES = ['S16v28', 'S15v13', 'S4v114', 'S1sw', 'S8v30', 'S12v14']
bad = [k for k in PARAS + S12PARAS + WHOLES if k not in R or not human(k)]
assert S12PARAS and not bad, ('not Human, or not checked:', bad, S12PARAS)
for keys, draft in (('s15/preservation-keys.json', 's15/v13.md'), ('s16/preservation-keys.json', 's16/v28.md')):
    r = subprocess.run([py, str(T / 'preservation_keys.py'), str(C / keys), str(C / draft), '--article',
                        str(C / 's16' / 'review-r1' / 'article-with-s15v3.md')], capture_output=True, text=True)
    assert 'verdict: PASS' in r.stdout, r.stdout
for reps, draft in (('s15/review-r*/SENSE*.md', 's15/v13.md'), ('s16/review-r*/SENSE*.md', 's16/v28.md')):
    r = subprocess.run([py, str(T / 'pause_tally.py')] + sorted(str(p) for p in C.glob(reps)) +
                       ['--draft', str(C / draft), '--ledger', str(C / 'OWNER-EDITS.json'), '--dispositions',
                        str(HERE / 'DISPOSITIONS-PAUSES-20261017.md')], capture_output=True, text=True)
    assert 'verdict: PASS' in r.stdout, r.stdout
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
for draft, src in ((C / 's16' / 'v28.md', C / 's16' / 'v0.md'), (C / 's15' / 'v13.md', C / 's15' / 'v0.md')):
    r = subprocess.run([py, str(T / 'tells_lint.py'), str(draft), '--source', str(src), '--installed', str(C / 'HUMANIZED-SO-FAR.md'),
                        '--style', str(C.parent / 'STYLE.json')], capture_output=True, text=True)
    assert 'verdict: FAIL' not in r.stdout, r.stdout[-2500:]


def region(text, start, ends):
    a = text.index(start)
    m = re.search(ends, text[a + 3:])
    return a, a + 3 + m.start()


NOTES = {
 's16': ('CANDIDATE: section 16 v28 (2026-10-17, after Joel\'s 13:11 message): v26 kni, the best faithful version (Mostly Human, '
         '0.32, one 61-word window, 399g), with his lines for that stretch (question 42: "And whether communal showers feel '
         'liberating, or make you start looking at studio apartments! No manifesto is going to tell you any of that! Look before '
         'you leap. It will really save you some time & money.") and "quietly" out of the opening (his correction). Every changed '
         'paragraph Human alone or with its neighbor (410g) and the whole section 100% Human (412g); key words PASS; the repeated '
         'pauses answered (fix-20261017/DISPOSITIONS-PAUSES-20261017.md). Records: s16/make_v28.py, fix-20261017/. Not accepted '
         'until Joel says so.'),
}
# section 16: the published section goes
a, b = art.index('# Practice Comes Before Property'), art.index('<!-- CANDIDATE: the appendix')
assert art[a:b].strip() == (C / 's16' / 'v0.md').read_text(encoding='utf-8').strip(), 'the article does not hold the published section 16'
art = art[:a] + '<!-- ' + NOTES['s16'] + ' -->\n' + (C / 's16' / 'v28.md').read_text(encoding='utf-8').strip() + '\n\n' + art[b:]
# the others: each installed section, from its heading to the next note or section, replaced by this turn's version
SWAPS = [
 ('# What This Looks Like From Sénégal', C / 's15' / 'v13.md', '<!-- CANDIDATE: section 15 v12',
  'CANDIDATE: section 15 v13 (2026-10-17, after Joel\'s 13:11 message): v12 with his three corrections (H2-P2: "public advocacy '
  'for homosexuality", without quotes, for the law\'s French "apologie", and the financing clause he called redundant cut; '
  'H3-P3: "This is also" for "It\'s also"; H3-P5: his "I understand the motivation to negotiate like that, but I think it\'s not '
  'a full solution either." for the "I like that." I had added) and H1-P3\'s "This is the most joking culture" (the sweep of his '
  '"this" rule). Each changed paragraph Human alone (410g), the whole section 100% Human (412g); key words PASS; his 40 a keeps '
  'H1-P4. Records: s15/make_v13.py, fix-20261017/. Before: '),
 ('# The Four Parts That Have to Pl/ork Together', HERE / 's4-v11.4.md', '<!-- CANDIDATE: section 4 v11.3',
  'CANDIDATE: section 4 v11.4 (2026-10-17, after Joel\'s 13:11 message): v11.3 with his answer to question 39 after the container '
  'line ("It\'s the practical logistical foundation that gets built once the architects can work well together."; his "I\'d '
  'say" dropped). Human with either neighbor (410g), the whole section 100% Human (412g). Records: fix-20261017/. Before: '),
 ('# The Math of Absorption, and Who This Isn’t For', HERE / 's12-v14.md', '<!-- CANDIDATE: section 12 v13',
  'CANDIDATE: section 12 v14 (2026-10-17, after Joel\'s 13:11 message): v13 with the PsyPost study he sent at the end of his P2 '
  '(his link, his "no, duh") and his screenshot after it as an image note; question 44 asks him about the placement. P2 Human '
  'alone and with P3 (411g), the whole section 100% Human (411g). Records: fix-20261017/ (march r3, cold reads SENSE-s12*.md, the '
  'study check SOURCE-s12.md, the stance check STANCE-s12.md). Before: '),
 ('# The Grown Children Get the Final Review', HERE / 's8-v30.md', '<!-- CANDIDATE: section 8 v29',
  'CANDIDATE: section 8 v30 (2026-10-17): v29 with "quietly" out of "Older kids can\'t be allowed to quietly boss the younger '
  'ones around there." (the sweep of Joel\'s 13:11 "remove "quietly" that\'s an ai tell"). Human with either neighbor (410g), the '
  'whole section 100% Human (412g). Records: fix-20261017/. Before: '),
]
for head, path, old_note, note in SWAPS:
    i = art.index(old_note)
    j = art.index('-->', i) + 3
    art = art[:i] + '<!-- ' + note + art[i + 5:j - 3].strip() + ' -->' + art[j:]
    a, b = region(art, head, r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )')
    art = art[:a] + path.read_text(encoding='utf-8').strip() + '\n' + art[b:]
# section 1 has no note of its own: it starts the file, before section 2's note
a = art.index('# The New Age May Dawn Suddenly')
b = art.index('<!-- CANDIDATE: section 2')
s1 = (HERE / 's1-swept.md').read_text(encoding='utf-8').strip()
assert s1.startswith('[image 1]')
art = ('<!-- CANDIDATE: section 1 (2026-10-17): "That\'s the sort of thing that doesn\'t make it into the history books." for "It\'s '
       'the sort of thing ..." (the sweep of Joel\'s 13:11 "this is not the same as it"; the published sentence is "These are the '
       'questions history books neglect."). Human alone and with the paragraph before (410g), the whole section 100% Human '
       '(412g). Records: fix-20261017/. -->\n' + s1 + '\n\n' + art[b:])
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
r = subprocess.run([py, str(T / 'check_owner_edits.py'), '--article', str(C / 'HUMANIZED-SO-FAR.md'), '--ledger',
                    str(C / 'OWNER-EDITS.json')], capture_output=True, text=True)
print(r.stdout[-600:])
print('installed: section 16 v28, section 15 v13, section 4 v11.4, section 12 v14, section 8 v30, section 1 (the sweep)')
