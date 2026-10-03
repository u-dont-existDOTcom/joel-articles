"""Section 5: the gate's fresh-context checks for version N (review-vN/), before any Pangram call: the blind
two-way trace in parts (a 64k output limit; about 1,000 words of rewrite a part), the cold read, the grounding
review and the whole-article stance check. Images go to every prompt with what they show (images.json; Joel,
2026-10-02 23:49: "the actual article uses an image"). Adapted from section 4's build_review.py."""
import json, pathlib, re, shutil, sys
HERE = pathlib.Path(__file__).resolve().parent
IC = HERE.parent.parent
sys.path.insert(0, '/home/claude/work'); import mdplain
RULES = pathlib.Path('/home/claude/s3rules')
sys.path.insert(0, str(RULES / 'tools/humanization/reviewer')); import reviewer as R
sys.path.insert(0, str(RULES / 'tools/humanization')); import stance_check_prompt as SC
IMAGES = json.load(open(HERE.parent / 'images.json', encoding='utf-8'))
img = lambda t: SC.describe_images(t, IMAGES)
n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
F = json.load(open(HERE / ('final-v%d.json' % n), encoding='utf-8'))
B, ORDER = F['blocks'], F['order']
O = json.load(open(HERE / 'original-blocks.json', encoding='utf-8'))
md = (HERE / ('section-v%d.md' % n)).read_text(encoding='utf-8').strip()
changed = [k for k in ORDER if k.startswith('P') and B[k] != O[k]]
OUT = HERE / ('review-v%d' % n)
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir()
orig = (IC / 'sections/006-original.md').read_text(encoding='utf-8').strip()
BRIEF = """# Blind two-way preservation trace: one section of an essay on intentional communities

You're checking a rewrite against the published original. Open only the files in this folder. Don't look for notes, other folders or the web.

Files:
- `original-section.md`: the published section, 33 paragraphs under four headings. Number its paragraphs P1 to P33 in order, counting every block of text that isn't a heading or an image (so "Insights need somewhere to land…" is P9, "No special shamans…" is P18, and the last paragraph, "Once the call sobers up…", is P33).
- `R-*.md`: the rewritten paragraphs you trace ({keys}; the others are traced separately), named by the published paragraph they answer.
- `R-section.md`: the whole rewrite assembled in order, with the headings in place. Use it for the sense check across paragraphs.

The author's rulings for this rewrite: the wording can change freely as long as the meaning stays: the same claims at the same strength, the same people doing the same things, nothing new about anyone. A quip may go if its point stays, when the point matters. Specific pairings turned into a general tangle are a changed claim, not lost detail. The author's first person ("I", "my") may say only what the original says he did, knows, felt or thinks.

For each rewrite file:
1. Which original paragraph it answers.
2. **Forward.** Split the original paragraph into units of meaning: one per claim, condition, quantity, time, attribution, hedge, example or link. Mark each SAME, SAME-MEANING (reworded, same meaning and strength), SHIFTED (meaning, scope, strength, voice, tense of a claim or attribution changed; say exactly how) or DROPPED.
3. **Reverse.** List everything in the rewrite that isn't in the original (ADDED): facts, claims, judgments, feelings, causes, people, intensifiers, hedges.
4. **Sources.** Links (same URL, doing the same job), quotation marks, who said or did what, numbers and dates.
5. **Sense.** Every word or pronoun whose referent a reader can't find in the visible text (this paragraph, or what comes before it in `R-section.md`), tense slips, grammar that makes you reread.

Put the marks in tables. Don't judge whether the rewrite is better, and don't suggest rewrites. Be exhaustive: a small shift counts.

Keep the whole report under 1,000 words: terse tables, one row per unit, no prose beyond what a row needs. Write it to `{report}` with one Write call. Then return only a summary table: file, the count of SHIFTED, DROPPED and ADDED, and one line for each change that alters what a reader would believe about a fact, a person, or the author's position.
"""
PARTS = {1: {'A': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],
             'B': ['P9', 'P10', 'P11', 'P12', 'P13', 'P14', 'P15', 'P16', 'P17'],
             'C': ['P18', 'P19', 'P20', 'P21', 'P22', 'P23', 'P24', 'P25'],
             'D': ['P26', 'P27', 'P28', 'P29', 'P30', 'P31', 'P32', 'P33']},
         # v2: every paragraph the v1 gate sent back (all but P5, which it passed)
         2: {'A': ['P1', 'P2', 'P3', 'P4', 'P6', 'P7', 'P8'],
             'B': ['P9', 'P10', 'P11', 'P12', 'P13', 'P14', 'P15', 'P16', 'P17'],
             'C': ['P18', 'P19', 'P20', 'P21', 'P22', 'P23', 'P24', 'P25'],
             'D': ['P26', 'P27', 'P28', 'P29', 'P30', 'P31', 'P32', 'P33']},
         # v3: the paragraphs the v2 gate sent back
         3: {'A': ['P1', 'P3', 'P8', 'P9', 'P10', 'P11', 'P12', 'P13', 'P15'],
             'B': ['P16', 'P17', 'P20', 'P23', 'P24', 'P25', 'P27', 'P28', 'P30']},
         # v4: the paragraphs the v3 gate sent back
         4: {'A': ['P11', 'P17', 'P22', 'P24', 'P27', 'P30']},
         # v5: Emulate round 2 for the paragraphs that read AI, and the v4 gate's findings
         5: {'A': ['P6', 'P7', 'P11', 'P15', 'P18'], 'B': ['P21', 'P29', 'P30', 'P31', 'P33']},
         6: {'A': ['P6', 'P7', 'P18', 'P29', 'P30', 'P33']},
         7: {'A': ['P18', 'P29', 'P30', 'P31', 'P33']}}
parts = {h: [k for k in ks if k in changed] for h, ks in PARTS.get(n, {}).items()}
if n == 1:
    assert sorted(sum(parts.values(), [])) == sorted(changed), (changed, parts)
for half, keys in parts.items():
    if not keys: continue
    d = OUT / ('trace' + half); d.mkdir()
    (d / 'original-section.md').write_text(img(orig) + '\n', encoding='utf-8')
    (d / 'R-section.md').write_text(img(md) + '\n', encoding='utf-8')
    for k in keys:
        (d / ('R-%s.md' % k)).write_text(B[k] + '\n', encoding='utf-8')
    (d / 'BRIEF.md').write_text(BRIEF.format(keys=', '.join(keys), report=str(HERE / ('TRACE-v%d-%s.md' % (n, half)))), encoding='utf-8')
# cold read: section 4 as installed, this section, the start of section 6
so_far = re.sub(r'<!--.*?-->', '', (HERE.parent / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'), flags=re.S)
cut = so_far.index('# The Medicine Part, Without Pretending')
before = so_far[so_far.index('# The Four Parts That Have to Pl/ork Together'):cut].strip()
nxt = (IC / 'sections/007-original.md').read_text(encoding='utf-8')
nxt_start = '\n\n'.join(img(mdplain.strip_widgets(nxt)).strip().split('\n\n')[:3])
last = R.read('sense.txt').split('\n\n')[-1]
sense = ("Below is one section from an essay about intentional communities and communes, with the section the reader has just read "
         "before it, and the start of the section after it.\n\n"
         "Read it as an ordinary reader who is seeing it for the first time. Your only job is to check whether it makes sense. "
         "Don't judge the style, and don't say whether it sounds like AI.\n\n"
         "For each numbered sentence of THE SECTION, write one line: OK if it makes sense right where it is, or UNCLEAR followed by "
         "exactly what trips you up (a word or pronoun whose meaning you can't pin down, a jump you can't follow, a claim that seems to "
         "come from nowhere, grammar that makes you reread). Then write one line for each paragraph saying whether it makes sense after "
         "the one before it, and one line saying whether the section after it follows on.\n\n"
         "The section before (the reader has just read it):\n" + img(before) + "\n\n"
         "THE SECTION:\n" + R.numbered(re.sub(r'^#+\s*', '', img(md), flags=re.M)) + "\n\n"
         "The start of the section after:\n" + nxt_start + "\n\n" + last)
(OUT / 'sense').mkdir(); (OUT / 'sense' / 'prompt.txt').write_text(sense, encoding='utf-8')
# grounding, the shared prompt with its first line adapted to the essay (as in sections 2 to 4)
gate = (RULES / 'docs/HUMANIZATION-GATE.md').read_text(encoding='utf-8')
rulings = gate[gate.index('## Owner rulings on rewriting'):gate.index('## Every correction teaches the system')].strip()
bans = gate[gate.index('## Owner bans'):gate.index('## What the linter checks')].strip()
target = dict(source=str(IC / 'original.md'), article_upto=img(so_far[:cut].strip()), guide_passage=img(orig),
              next=nxt_start, rulings=rulings + '\n\n' + bans, push='tight')
tp = OUT / 'grounding-target.json'; tp.write_text(json.dumps(target, indent=1, ensure_ascii=False), encoding='utf-8')
g = R.build_grounding(img(md), tp)
old = R.read('grounding.txt').split('\n', 1)[0]; assert g.startswith(old)
new = (HERE.parent / 's2/review-v2/grounding/prompt.txt').read_text(encoding='utf-8').split('\n', 1)[0]
(OUT / 'grounding').mkdir(); (OUT / 'grounding' / 'prompt.txt').write_text(new + g[len(old):], encoding='utf-8')
# the whole-article stance check
st = SC.build((IC / 'original.md').read_text(encoding='utf-8'), md,
              scope='section 5 ("The Medicine Part, Without Pretending It Isn’t There"); sections 1 to 4 were checked before',
              topic='intentional communities', report=str(HERE / ('STANCE-v%d.md' % n)), images=IMAGES)
(OUT / 'stance').mkdir(); (OUT / 'stance' / 'prompt.txt').write_text(st, encoding='utf-8')
for d in sorted(OUT.iterdir()):
    if d.is_dir(): print(d.name, sum(len(p.read_text(encoding='utf-8').split()) for p in d.iterdir()), 'words')
print('changed:', ' '.join(changed))
