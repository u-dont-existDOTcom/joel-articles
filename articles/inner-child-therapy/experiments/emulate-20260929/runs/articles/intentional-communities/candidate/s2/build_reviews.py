"""Section 2 v2: the gate's fresh-context checks before any Pangram call (2026-10-01).

Builds one folder per check under review-v2/, each holding only what that agent may read:
  trace/      the blind two-way preservation trace (EMULATE-FALLBACK 4.5.1)
  grounding/  grounding, logic and MISFIRES (HUMANIZATION-GATE S6), tools/humanization/reviewer/reviewer.py grounding
  sense/      the cold read (S3), adapted from reviewer/sense.txt to a whole section
  sweep/      the row-by-row tell sweep (step 6), tools/humanization/build_sweep_prompt.py
  reviewer/   the reviewer's blind verdicts (EMULATE-FALLBACK 4.5.3 and 6), logged before Pangram; key in review-v2/
Adaptations, recorded: the grounding and sense prompts open by describing the Inner Child article, so their first
paragraph is replaced by one describing this essay. Nothing else in them is changed.
"""
import json, pathlib, re, shutil, subprocess, sys, random
HERE = pathlib.Path(__file__).resolve().parent
UNI = pathlib.Path('/home/claude/universal')
sys.path.insert(0, str(UNI / 'tools/humanization/reviewer')); import reviewer as R
sys.path.insert(0, str(HERE)); sys.argv = ['x']
import importlib.util
spec = importlib.util.spec_from_file_location('b', HERE / 'build_s2.py'); B = importlib.util.module_from_spec(spec)
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    import os; cwd = os.getcwd(); os.chdir(HERE); spec.loader.exec_module(B); os.chdir(cwd)
IC = HERE.parent.parent  # runs/articles/intentional-communities
V3 = HERE.parent / 'v3'
OUT = HERE / 'review-v2'
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()
orig = (IC / 'sections/003-original.md').read_text(encoding='utf-8')
nxt = (IC / 'sections/004-original.md').read_text(encoding='utf-8')
nxt_start = '\n\n'.join(nxt.strip().split('\n\n')[:3])
so_far = (HERE.parent / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
so_far = re.sub(r'<!--.*?-->', '', so_far, flags=re.S)
sec1 = so_far[:so_far.index('# Communes Are Hot Again')].strip()
cand = (HERE / (B.CHOSEN + '.md')).read_text(encoding='utf-8')

def folder(name):
    d = OUT / name; d.mkdir(); return d

# 1. trace
d = folder('trace')
(d / 'original-section.md').write_text(orig, encoding='utf-8')
(d / 'R-section.md').write_text(cand, encoding='utf-8')
for k in ('C1a', 'C1b', 'C2', 'C3', 'C4a', 'C4b', 'C6', 'C7a', 'C7b', 'C8', 'C9a', 'C9b', 'C10a', 'C10b', 'C11a', 'C11b', 'C12'):
    (d / ('R-%s.md' % k)).write_text(B.P[k] + '\n', encoding='utf-8')
(d / 'BRIEF.md').write_text('''# Blind two-way preservation trace: one section of an essay on intentional communities

You're checking a rewrite against the published original. Open only the files in this folder. Don't look for notes, other folders or the web.

Files:
- `original-section.md`: the published section. The paragraph that starts "It's poppin' on Instagram" isn't rewritten and has no rewrite file. The image lines aren't text.
- `R-*.md`: the rewritten paragraphs. Where there's an a and a b, they're alternatives for the same paragraph: trace each.
- `R-section.md`: the rewrite assembled in order (the a versions), with the headings, images and the unchanged paragraph in place. Use it for the sense check across paragraphs.

For each rewrite file:
1. Which original paragraph it answers.
2. **Forward.** Split the original paragraph into units of meaning: one per claim, condition, quantity, time, attribution, hedge, example or link. Mark each SAME, SAME-MEANING (reworded, same meaning and strength), SHIFTED (meaning, scope, strength, voice, tense of a claim or attribution changed; say exactly how) or DROPPED.
3. **Reverse.** List everything in the rewrite that isn't in the original (ADDED): facts, claims, judgments, feelings, causes, people, intensifiers, hedges.
4. **Sources.** Links (same URL, doing the same job), quotation marks (whose words they are), who said or did what.
5. **Sense.** Every word or pronoun whose referent a reader can't find in the visible text (this paragraph, or what comes before it in `R-section.md`), tense slips, grammar that makes you reread.

Put the marks in tables. Don't judge whether the rewrite is better, and don't suggest rewrites. Be exhaustive: a small shift counts ("roughly eighty" to "maybe eighty").

Write the whole report to `%s`. Then return only a summary table: file, the count of SHIFTED, DROPPED and ADDED, and one line for each change that alters what a reader would believe about a fact, a person, or the author's position.
''' % (HERE / 'TRACE-v2.md'), encoding='utf-8')

# 2. grounding
d = folder('grounding')
ABOUT_OLD = R.read('grounding.txt').split('\n', 1)[0]
ABOUT_NEW = ("You're reviewing new text for an essay about intentional communities and communes, by Joel, published on Substack. "
             "The essay is being humanized section by section. The guide below is the published essay, which Joel wrote with AI help; "
             "the new text is a rewrite of one of its sections, and it should say what the guide says: the same claims at the same strength, "
             "the same people doing the same things, and nothing new about Joel's life or anyone else's. Below are the whole guide, the article "
             "up to the new text, the guide passage the new text is meant to carry, what comes next, and the author's rulings on this material. "
             "Where the author has ruled on what something means, his ruling is the reference, not the guide's wording.")
gate = (UNI / 'docs/HUMANIZATION-GATE.md').read_text(encoding='utf-8')
rulings = gate[gate.index('## Owner rulings on rewriting'):gate.index('\n---\n')].strip()
bans = gate[gate.index('## Owner bans'):gate.index('## What the linter checks')].strip()
target = dict(source=str(IC / 'original.md'), article_upto=sec1, guide_passage=orig.strip(), next=nxt_start,
              rulings=rulings + '\n\n' + bans, push='tight')
tp = HERE / 'review-v2' / 'grounding-target.json'
tp.write_text(json.dumps(target, indent=1, ensure_ascii=False), encoding='utf-8')
g = R.build_grounding(cand, tp)
assert g.startswith(ABOUT_OLD)
(d / 'prompt.txt').write_text(ABOUT_NEW + g[len(ABOUT_OLD):], encoding='utf-8')

# 3. sense (cold read), adapted from reviewer/sense.txt to one whole section
d = folder('sense')
s = R.read('sense.txt')
s_lines = s.split('\n\n')
assert s_lines[0].startswith('Below is one paragraph from a friendly self-help article about inner-child therapy')
body = cand
body = re.sub(r'(?m)^\[image \d+\]\(.*?\)$', '[an image]', body)
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
         "The start of the section after:\n" + nxt_start + "\n\n" + s_lines[-1])
(d / 'prompt.txt').write_text(sense, encoding='utf-8')

# 4. tell sweep
d = folder('sweep')
(OUT / 'sweep-prev.md').write_text(sec1, encoding='utf-8'); (OUT / 'sweep-next.md').write_text(nxt_start, encoding='utf-8')
sw = subprocess.run([sys.executable, str(UNI / 'tools/humanization/build_sweep_prompt.py'), str(HERE / (B.CHOSEN + '.md')),
                     '--previous', str(OUT / 'sweep-prev.md'), '--next', str(OUT / 'sweep-next.md')], capture_output=True, text=True, check=True)
(d / 'prompt.txt').write_text(sw.stdout, encoding='utf-8')

# 5. reviewer, blind, with controls; the key stays outside the folder
d = folder('reviewer')
ITEMS = ['C2', 'C4a', 'C9a', 'C10a', 'C11a', 'C12', 'C1a-C2', 'C3-C4a', 'C6-C7a', 'C8-C9a', 'C8o-C9a']
ex = R.examples(extra=False); norm = lambda t: re.sub(r'\s+', ' ', t).strip(); exn = norm(ex)
items = [('s2 ' + k, '?', (HERE / (k + '.txt')).read_text(encoding='utf-8').strip()) for k in ITEMS]
for f, lab in (('P4D', 'AI'), ('P4C', 'AI'), ('P10', 'HUMAN'), ('P12', 'HUMAN')):  # community section 1, Pangram-checked
    items.append(('control community-s1 ' + f, lab, (V3 / (f + '.txt')).read_text(encoding='utf-8').strip()))
for c in ('PASS_mpv_p2_can_show', 'FAIL_mpv_p3_d1'):  # Inner Child calibration
    items.append(('control ' + c, R.label(c), R.text(c).strip()))
for name, lab, t in items:
    assert norm(t)[:120] not in exn, name
random.Random(41).shuffle(items)
outv = R.read('output_verdicts.txt').replace('Q01 AI 80', 'V01 AI 80').replace('Q02 HUMAN 70', 'V02 HUMAN 70')
key, parts = {}, [R.read('rubric.txt'), ex, '\n\nPART 2 — PASSAGES TO JUDGE (%d passages; sentences numbered)\n' % len(items),
                  "These come from the same author's essays. Judge each one on its own: what would Pangram say?\n"]
for i, (name, lab, t) in enumerate(items, 1):
    pid = 'V%02d' % i; key[pid] = dict(name=name, label=lab)
    parts.append('\n=== %s ===\n%s\n' % (pid, R.numbered(t)))
parts.append(outv)
(d / 'prompt.txt').write_text(''.join(parts), encoding='utf-8')
(OUT / 'reviewer-key.json').write_text(json.dumps(key, indent=1), encoding='utf-8')
for n in ('trace', 'grounding', 'sense', 'sweep', 'reviewer'):
    print(n, sum(len(p.read_text(encoding='utf-8').split()) for p in (OUT / n).iterdir()), 'words')
