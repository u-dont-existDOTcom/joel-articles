"""Section 3 v1: assemble the picks, then the gate's fresh-context checks (review-v1/): the blind trace in two halves
(one report overran the output limit), the cold read and the grounding review. Adaptations of the shared prompts, as in
section 2: the first line describes this essay instead of the Inner Child article."""
import json, pathlib, re, shutil, sys
HERE = pathlib.Path(__file__).resolve().parent
IC = HERE.parent.parent
sys.path.insert(0, '/home/claude/work'); import mdplain
UNI = pathlib.Path('/home/claude/universal')
sys.path.insert(0, str(UNI / 'tools/humanization/reviewer')); import reviewer as R
T = json.load(open(HERE / 'fixlog-s3.json', encoding='utf-8'))['texts']
O = json.load(open(HERE / 'original-blocks.json', encoding='utf-8'))
PICK = ['P1', 'P2', 'P3', 'P4b', 'P5', 'P6a', 'P7', 'P8a', 'P9b']
def section(p3='P3'):
    return '\n\n'.join([O['H1'], T['P1'], O['H2a'], T['P2'], T[p3], T['P4b'], O['H2b'], T['P5'], T['P6a'], T['P7'], T['P8a'], T['P9b']])
md = section()
(HERE / 'section-v1.md').write_text(md + '\n', encoding='utf-8')
(HERE / 'r1' / 'section-v1.txt').write_text(mdplain.plain(md).strip() + '\n', encoding='utf-8')
(HERE / 'r1' / 'section-v1e.txt').write_text(mdplain.plain(section('P3e')).strip() + '\n', encoding='utf-8')
OUT = HERE / 'review-v1'
for n in ('traceA', 'traceB', 'sense', 'grounding'):
    if (OUT / n).exists(): shutil.rmtree(OUT / n)
brief = (OUT / 'trace' / 'BRIEF.md').read_text(encoding='utf-8')
brief = brief.replace("- `R-section.md`: the rewrite assembled in order (P4b, P6a, P8a and P9a), with the headings in place.",
                      "- `R-section.md`: the rewrite assembled in order (P4b, P6a, P8a and P9b), with the headings in place.")
brief = brief.replace('Keep the whole report under 3,000 words', 'Keep the whole report under 1,500 words')
for half, keys in (('traceA', ['P1', 'P2', 'P3', 'P4b']), ('traceB', ['P5', 'P6a', 'P7', 'P8a', 'P8b', 'P9b'])):
    d = OUT / half; d.mkdir()
    (d / 'original-section.md').write_text((IC / 'sections/004-original.md').read_text(encoding='utf-8').rstrip('\n') + '\n', encoding='utf-8')
    (d / 'R-section.md').write_text(md + '\n', encoding='utf-8')
    for k in keys:
        (d / ('R-%s.md' % k)).write_text(T[k] + '\n', encoding='utf-8')
    b = brief.replace(str(HERE / 'TRACE-v1.md'), str(HERE / ('TRACE-v1-%s.md' % half[-1])))
    b = b.replace("- `R-*.md`: the rewritten paragraphs,", "- `R-*.md`: the rewritten paragraphs you trace (%s; the others are traced separately),\n  " % ', '.join(keys))
    (d / 'BRIEF.md').write_text(b, encoding='utf-8')
# cold read, adapted from reviewer/sense.txt to one whole section (as in section 2)
so_far = re.sub(r'<!--.*?-->', '', (HERE.parent / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'), flags=re.S)
before = so_far[:so_far.index('# Why Communities Keep Dying')].strip()
before = before[before.index('# Communes Are Hot Again'):]  # the section the reader has just read
nxt = (IC / 'sections/005-original.md').read_text(encoding='utf-8')
nxt_start = '\n\n'.join(nxt.strip().split('\n\n')[:3])
last = R.read('sense.txt').split('\n\n')[-1]
body = re.sub(r'(?m)^\[image \d+\]\(.*?\)$', '[an image]', md)
sense = ("Below is one section from an essay about intentional communities and communes, with the section the reader has just read "
         "before it, and the start of the section after it.\n\n"
         "Read it as an ordinary reader who is seeing it for the first time. Your only job is to check whether it makes sense. "
         "Don't judge the style, and don't say whether it sounds like AI.\n\n"
         "For each numbered sentence of THE SECTION, write one line: OK if it makes sense right where it is, or UNCLEAR followed by "
         "exactly what trips you up (a word or pronoun whose meaning you can't pin down, a jump you can't follow, a claim that seems to "
         "come from nowhere, grammar that makes you reread). Then write one line for each paragraph saying whether it makes sense after "
         "the one before it, and one line saying whether the section after it follows on.\n\n"
         "The section before (the reader has just read it):\n" + re.sub(r'(?m)^\[image \d+\]\(.*?\)$', '[an image]', before) + "\n\n"
         "THE SECTION:\n" + R.numbered(re.sub(r'^#+\s*', '', body, flags=re.M)) + "\n\n"
         "The start of the section after:\n" + nxt_start + "\n\n" + last)
(OUT / 'sense').mkdir(); (OUT / 'sense' / 'prompt.txt').write_text(sense, encoding='utf-8')
# grounding, with the shared prompt's first line adapted (as in section 2)
gate = (UNI / 'docs/HUMANIZATION-GATE.md').read_text(encoding='utf-8')
lessons = pathlib.Path('/home/claude/s2lessons/docs/HUMANIZATION-GATE.md').read_text(encoding='utf-8')
rulings = lessons[lessons.index('## Owner rulings on rewriting'):lessons.index('## Every correction teaches the system')].strip()
bans = lessons[lessons.index('## Owner bans'):lessons.index('## What the linter checks')].strip()
target = dict(source=str(IC / 'original.md'), article_upto=so_far[:so_far.index('# Why Communities Keep Dying')].strip(),
              guide_passage=(IC / 'sections/004-original.md').read_text(encoding='utf-8').strip(), next=nxt_start,
              rulings=rulings + '\n\n' + bans, push='tight')
tp = OUT / 'grounding-target.json'; tp.write_text(json.dumps(target, indent=1, ensure_ascii=False), encoding='utf-8')
g = R.build_grounding(md, tp)
old = R.read('grounding.txt').split('\n', 1)[0]; assert g.startswith(old)
new = (HERE.parent / 's2/review-v2/grounding/prompt.txt').read_text(encoding='utf-8').split('\n', 1)[0]
(OUT / 'grounding').mkdir(); (OUT / 'grounding' / 'prompt.txt').write_text(new + g[len(old):], encoding='utf-8')
for n in ('traceA', 'traceB', 'sense', 'grounding'):
    print(n, sum(len(p.read_text(encoding='utf-8').split()) for p in (OUT / n).iterdir()), 'words')
print(len(mdplain.plain(md).split()), 'words in the section')
