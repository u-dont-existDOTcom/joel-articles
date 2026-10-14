"""Section 2 v3: assemble the lead candidate and build the blind trace and the cold read for it (2026-10-01).

Lead picks, each Pangram Human alone or in its pair (r4/pangram-s2.jsonl, pangram-s2.jsonl, r1/pangram-s2.jsonl):
C1 writers round 3 w3; C2 v2.1; C3 C3e2 (pair check pending); C4 C4e1p (the 1972 quip said plainly; C4e1q keeps it,
Joel to choose); Joel's Instagram paragraph with his edit; C6 and C7 writers round 1 U3w3; Joel's C8 line; C9 writers
round 3 w1 (C9e1 the alternative); Joel's C10 and C11; C12 v2.1.
"""
import json, pathlib, re, shutil, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, '/home/claude/work'); import mdplain
UNI = pathlib.Path('/home/claude/universal')
sys.path.insert(0, str(UNI / 'tools/humanization/reviewer')); import reviewer as R
IC = HERE.parent.parent
V3 = json.load(open(HERE / 'fixlog-v3.json', encoding='utf-8'))['texts']
U_SG = 'https://www.hhs.gov/sites/default/files/surgeon-general-social-connection-advisory.pdf'
U_IG2 = 'https://instagram.com/p/DaLvZV2qIk2/'
src = [p.strip() for p in (IC / 'sections/003-original.md').read_text(encoding='utf-8').split('\n\n') if p.strip()]
img = {k: [p for p in src if p.startswith('[image %d]' % k)][0] for k in (4, 5, 6)}
def w(path):
    return (HERE / path).read_text(encoding='utf-8').strip()
C1 = w('writers-r3/C1/w3.txt').replace('the U.S. Surgeon General', '[the U.S. Surgeon General](%s)' % U_SG, 1)
assert U_SG in C1
u3 = w('writers-r1/U3/w3.txt').split('\n\n')
C6 = u3[0].replace('floated the commune idea', '[floated the commune idea](%s)' % U_IG2, 1); C7 = u3[1]
# the cold read (SENSE-v3.md [20]) had to reread C7's second sentence: the objection sat between "The oldest objection" and "showed up", and
# "the responsibility anarchism requires" first read as "responsibility anarchism". Split, with "that" added (not the published sentence back).
C7_OLD = 'The oldest objection, that maybe most people don’t want to take on the responsibility anarchism requires and communal property becomes “owned by everyone, cared for by nobody,” showed up almost right away.'
assert C7_OLD in C7
C7 = C7.replace(C7_OLD, 'The oldest objection showed up almost right away. It was that maybe most people don’t want to take on the responsibility that anarchism requires, and communal property becomes “owned by everyone, cared for by nobody.”')
assert U_IG2 in C6
C8o = 'The commune comments became a miniature political-philosophy seminar, as Instagram comments sometimes do.'
B = {}
exec(compile(open(HERE / 'build_s2.py', encoding='utf-8').read().split('WHY = {')[0], 'b', 'exec'), B)  # v2.1 texts (P)
PICK = dict(C1=C1, C2=B['P']['C2'], C3=V3['C3e2'], C4=V3['C4e1p'], SEBA=V3['SEBAj'], C6=C6, C7=C7, C8=C8o,
            C9=w('writers-r3/C9/w1.txt'), C10=V3['C10j'], C11=V3['C11j'], C12=B['P']['C12'])
ALT = dict(C3=V3['C3e3'], C4=V3['C4e1q'], C9=V3['C9e1'])
def section(p):
    return '\n\n'.join(['# Communes Are Hot Again 🔥', p['C1'], p['C2'], p['C3'], img[4], p['C4'], p['SEBA'], p['C6'],
                        '### The Freeloader Problem', p['C7'], img[5], p['C8'], p['C9'], p['C10'], p['C11'], p['C12'], img[6]])
md = section(PICK)
(HERE / 'section-v3.md').write_text(md + '\n', encoding='utf-8')
(HERE / 'section-v3.txt').write_text(mdplain.plain(md).strip() + '\n', encoding='utf-8')
json.dump(dict(pick=PICK, alt=ALT), open(HERE / 'v3-picks.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
OUT = HERE / 'review-v3'
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()
# blind trace: only the rewritten paragraphs; Joel's own paragraphs (C10, C11, his Instagram one, his C8 line) aren't traced
d = OUT / 'trace'; d.mkdir()
(d / 'original-section.md').write_text((IC / 'sections/003-original.md').read_text(encoding='utf-8').rstrip('\n') + '\n', encoding='utf-8')
(d / 'R-section.md').write_text(md + '\n', encoding='utf-8')
files = dict(C1=PICK['C1'], C2=PICK['C2'], C3a=PICK['C3'], C3b=ALT['C3'], C4a=PICK['C4'], C4b=ALT['C4'], C6=PICK['C6'], C7=PICK['C7'],
             C9a=PICK['C9'], C9b=ALT['C9'], C12=PICK['C12'])
for k, t in files.items():
    (d / ('R-%s.md' % k)).write_text(t + '\n', encoding='utf-8')
(d / 'BRIEF.md').write_text('''# Blind two-way preservation trace: one section of an essay on intentional communities

You're checking a rewrite against the published original. Open only the files in this folder. Don't look for notes, other folders or the web.

Files:
- `original-section.md`: the published section. The image lines aren't text.
- `R-*.md`: the rewritten paragraphs. Where there's an a and a b, they're alternatives for the same paragraph: trace each.
- `R-section.md`: the rewrite assembled in order (the a versions). Four paragraphs in it are the author's own rewrites and have no R- file: the Instagram paragraph that starts "It's poppin'", the line that starts "The commune comments became", and the two paragraphs that start "Communal ownership entails" and "People want to go back". Don't trace those; use them only as context for the sense check.

The author's rulings for this rewrite: the wording can change freely as long as the meaning stays. In the AI paragraph, "feeds" can go. The 1972 line ("Suddenly 'maybe we should form a village' sounded less like a 1972 leftover and more like a backup plan.") may be kept or said plainly.

For each rewrite file:
1. Which original paragraph it answers.
2. **Forward.** Split the original paragraph into units of meaning: one per claim, condition, quantity, time, attribution, hedge, example or link. Mark each SAME, SAME-MEANING (reworded, same meaning and strength), SHIFTED (meaning, scope, strength, voice, tense of a claim or attribution changed; say exactly how) or DROPPED.
3. **Reverse.** List everything in the rewrite that isn't in the original (ADDED): facts, claims, judgments, feelings, causes, people, intensifiers, hedges.
4. **Sources.** Links (same URL, doing the same job), quotation marks (whose words they are), who said or did what.
5. **Sense.** Every word or pronoun whose referent a reader can't find in the visible text (this paragraph, or what comes before it in `R-section.md`), tense slips, grammar that makes you reread.

Put the marks in tables. Don't judge whether the rewrite is better, and don't suggest rewrites. Be exhaustive: a small shift counts.

Keep the whole report under 2,500 words: terse tables, one row per unit, no prose beyond what a row needs. Write it to `%s` with one Write call. Then return only a summary table: file, the count of SHIFTED, DROPPED and ADDED, and one line for each change that alters what a reader would believe about a fact, a person, or the author's position.
''' % (HERE / 'TRACE-v3.md'), encoding='utf-8')
# cold read of the whole section in place (as review-v2/sense)
so_far = re.sub(r'<!--.*?-->', '', (HERE.parent / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'), flags=re.S)
sec1 = so_far[:so_far.index('# Communes Are Hot Again')].strip()
nxt = (IC / 'sections/004-original.md').read_text(encoding='utf-8')
nxt_start = '\n\n'.join(nxt.strip().split('\n\n')[:3])
body = re.sub(r'(?m)^\[image \d+\]\(.*?\)$', '[an image]', md)
last = R.read('sense.txt').split('\n\n')[-1]
sense = ("Below is one section from an essay about intentional communities and communes, with the part of the article the reader has "
         "already read before it, and the start of the section after it.\n\n"
         "Read it as an ordinary reader who is seeing it for the first time. Your only job is to check whether it makes sense. "
         "Don't judge the style, and don't say whether it sounds like AI.\n\n"
         "For each numbered sentence of THE SECTION, write one line: OK if it makes sense right where it is, or UNCLEAR followed by "
         "exactly what trips you up (a word or pronoun whose meaning you can't pin down, a jump you can't follow, a claim that seems to "
         "come from nowhere, grammar that makes you reread). Then write one line for each paragraph saying whether it makes sense after "
         "the one before it, and one line saying whether the section after it follows on.\n\n"
         "Earlier in the article (the reader has already read this):\n" + sec1 + "\n\n"
         "THE SECTION:\n" + R.numbered(re.sub(r'^#+\s*', '', body, flags=re.M)) + "\n\n"
         "The start of the section after:\n" + nxt_start + "\n\n" + last)
(OUT / 'sense').mkdir(); (OUT / 'sense' / 'prompt.txt').write_text(sense, encoding='utf-8')
(HERE / 'r4' / 'C6-C7fix.txt').write_text(mdplain.plain(C6 + '\n\n' + C7).strip() + '\n', encoding='utf-8')
print(len(mdplain.plain(md).split()), 'words in the section')
