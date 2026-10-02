"""Section 4: the gate's fresh-context checks for version N (review-vN/), before any Pangram call: the blind
two-way trace in three parts (a 64k output limit), the cold read, the grounding review and the whole-article
stance check (tools/humanization/stance_check_prompt.py, new 2026-10-02). Adapted from section 3's build_review.py."""
import json, pathlib, re, shutil, sys
HERE = pathlib.Path(__file__).resolve().parent
IC = HERE.parent.parent
sys.path.insert(0, '/home/claude/work'); import mdplain
RULES = pathlib.Path('/home/claude/s3rules')
sys.path.insert(0, str(RULES / 'tools/humanization/reviewer')); import reviewer as R
sys.path.insert(0, str(RULES / 'tools/humanization')); import stance_check_prompt as SC
n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
F = json.load(open(HERE / ('final-v%d.json' % n), encoding='utf-8'))
B, ORDER = F['blocks'], F['order']
O = json.load(open(HERE / 'original-blocks.json', encoding='utf-8'))
md = (HERE / ('section-v%d.md' % n)).read_text(encoding='utf-8').strip()
changed = [k for k in ORDER if k.startswith('P') and B[k] != O[k]]
OUT = HERE / ('review-v%d' % n)
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir()
orig = (IC / 'sections/005-original.md').read_text(encoding='utf-8').strip()
img = lambda t: re.sub(r'(?m)^\[image \d+\]\(.*?\)$', '[an image]', t)
BRIEF = """# Blind two-way preservation trace: one section of an essay on intentional communities

You're checking a rewrite against the published original. Open only the files in this folder. Don't look for notes, other folders or the web.

Files:
- `original-section.md`: the published section, 31 paragraphs under five headings. Number its paragraphs P1 to P31 in order, counting every block of text that isn't a heading or an image (so "Pl/ork means play + work." is P8, and the last paragraph, "Skip one…", is P31).
- `R-*.md`: the rewritten paragraphs you trace ({keys}; the others are traced separately), named by the published paragraph they answer.
- `R-section.md`: the whole rewrite assembled in order, with the headings in place. Paragraphs not listed as changed are the published ones. Use it for the sense check across paragraphs.

The author's rulings for this rewrite: the wording can change freely as long as the meaning stays: the same claims at the same strength, the same people doing the same things, nothing new about anyone. A quip may go if its point stays, when the point matters.

For each rewrite file:
1. Which original paragraph it answers.
2. **Forward.** Split the original paragraph into units of meaning: one per claim, condition, quantity, time, attribution, hedge, example or link. Mark each SAME, SAME-MEANING (reworded, same meaning and strength), SHIFTED (meaning, scope, strength, voice, tense of a claim or attribution changed; say exactly how) or DROPPED.
3. **Reverse.** List everything in the rewrite that isn't in the original (ADDED): facts, claims, judgments, feelings, causes, people, intensifiers, hedges.
4. **Sources.** Links (same URL, doing the same job), quotation marks, who said or did what, numbers.
5. **Sense.** Every word or pronoun whose referent a reader can't find in the visible text (this paragraph, or what comes before it in `R-section.md`), tense slips, grammar that makes you reread.

Put the marks in tables. Don't judge whether the rewrite is better, and don't suggest rewrites. Be exhaustive: a small shift counts.

Keep the whole report under 1,500 words: terse tables, one row per unit, no prose beyond what a row needs. Write it to `{report}` with one Write call. Then return only a summary table: file, the count of SHIFTED, DROPPED and ADDED, and one line for each change that alters what a reader would believe about a fact, a person, or the author's position.
"""
PARTS = {1: {'A': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P11', 'P12'],
             'B': ['P15', 'P16', 'P17', 'P18', 'P19', 'P20', 'P21', 'P23'],
             'C': ['P24', 'P25', 'P26', 'P27', 'P28', 'P29', 'P30', 'P31']},
         # v2: what changed since v1, and P24 to P31, whose v1 trace overran the output limit
         2: {'A': ['P3', 'P4', 'P5', 'P6', 'P7', 'P12'], 'B': ['P16', 'P17', 'P18', 'P19', 'P21'],
             'C': ['P23', 'P24', 'P25', 'P26'], 'D': ['P27', 'P28', 'P29', 'P30', 'P31']},
         # v5: what changed since v3 (v3 was traced; v4 went only to Pangram)
         5: {'A': ['P5', 'P11', 'P12', 'P15', 'P16'], 'B': ['P17', 'P18', 'P19', 'P29', 'P30']},
         # v6: Joel rewrote P5, P7, P11 to P13, P26, P28 and P29 himself; the v5 paragraphs of mine or Emulate's
         # that never had a fresh trace are traced now
         6: {'A': ['P15', 'P16', 'P17', 'P18', 'P19', 'P30']},
         # v7: P16 and P17 fixed, and the run P21 to P24 from one Emulate call
         7: {'A': ['P16', 'P17', 'P21', 'P22', 'P23', 'P24']},
         8: {'A': ['P23', 'P24']}}
parts = {h: [k for k in ks if k in changed] for h, ks in PARTS[n].items()}
if n == 1:
    assert sorted(sum(parts.values(), [])) == sorted(changed), (changed, parts)
BRIEF = BRIEF.replace('Keep the whole report under 1,500 words', 'Keep the whole report under %s words' % ('1,500' if n == 1 else '1,000'))
for half, keys in parts.items():
    d = OUT / ('trace' + half); d.mkdir()
    (d / 'original-section.md').write_text(img(orig) + '\n', encoding='utf-8')
    (d / 'R-section.md').write_text(img(md) + '\n', encoding='utf-8')
    for k in keys:
        (d / ('R-%s.md' % k)).write_text(B[k] + '\n', encoding='utf-8')
    (d / 'BRIEF.md').write_text(BRIEF.format(keys=', '.join(keys), report=str(HERE / ('TRACE-v%d-%s.md' % (n, half)))), encoding='utf-8')
# cold read: the section before (section 3 as installed), this section, the start of the next
so_far = re.sub(r'<!--.*?-->', '', (HERE.parent / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'), flags=re.S)
cut = so_far.index('# The Four Parts That Have to Pl/ork Together')
before = so_far[so_far.index('# Why Communities Keep Dying'):cut].strip()
nxt = (IC / 'sections/006-original.md').read_text(encoding='utf-8')
nxt_start = '\n\n'.join(img(nxt).strip().split('\n\n')[:3])
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
# grounding, the shared prompt with its first line adapted to the essay (as in sections 2 and 3)
gate = (RULES / 'docs/HUMANIZATION-GATE.md').read_text(encoding='utf-8')
rulings = gate[gate.index('## Owner rulings on rewriting'):gate.index('## Every correction teaches the system')].strip()
bans = gate[gate.index('## Owner bans'):gate.index('## What the linter checks')].strip()
target = dict(source=str(IC / 'original.md'), article_upto=so_far[:cut].strip(), guide_passage=orig,
              next=nxt_start, rulings=rulings + '\n\n' + bans, push='tight')
tp = OUT / 'grounding-target.json'; tp.write_text(json.dumps(target, indent=1, ensure_ascii=False), encoding='utf-8')
g = R.build_grounding(md, tp)
old = R.read('grounding.txt').split('\n', 1)[0]; assert g.startswith(old)
new = (HERE.parent / 's2/review-v2/grounding/prompt.txt').read_text(encoding='utf-8').split('\n', 1)[0]
(OUT / 'grounding').mkdir(); (OUT / 'grounding' / 'prompt.txt').write_text(new + g[len(old):], encoding='utf-8')
# the whole-article stance check
st = SC.build((IC / 'original.md').read_text(encoding='utf-8'), md,
              scope='section 4 ("The Four Parts That Have to Pl/ork Together"); sections 1 to 3 were checked before',
              topic='intentional communities', report=str(HERE / ('STANCE-v%d.md' % n)))
(OUT / 'stance').mkdir(); (OUT / 'stance' / 'prompt.txt').write_text(st, encoding='utf-8')
for d in sorted(OUT.iterdir()):
    if d.is_dir(): print(d.name, sum(len(p.read_text(encoding='utf-8').split()) for p in d.iterdir()), 'words')
print('changed:', ' '.join(changed))
