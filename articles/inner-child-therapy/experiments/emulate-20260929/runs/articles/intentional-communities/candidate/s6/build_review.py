"""Section 6: the gate's fresh-context checks for drafts version N (review-dN/): the blind two-way trace, two logic
audits, the cold read and the whole-article stance check. Adapted from section 5's build_review.py.

The embedded post card and the image are shown to every reviewer the way a reader sees them: the card's title and
date, then its excerpt (Joel's own post, P2) as a quotation; the image as "[an image]" with its caption.
Also writes section-dN.md (the section as it would be installed, links and embed intact)."""
import json, pathlib, re, shutil, sys
HERE = pathlib.Path(__file__).resolve().parent
IC = HERE.parent.parent
RULES = pathlib.Path('/home/claude/s3rules')
sys.path.insert(0, str(RULES / 'tools/humanization/reviewer')); import reviewer as R
sys.path.insert(0, str(RULES / 'tools/humanization')); import stance_check_prompt as SC
n = int(sys.argv[1])
O = json.load(open(HERE / 'original-blocks.json', encoding='utf-8'))
D = json.load(open(HERE / ('drafts-v%d.json' % n), encoding='utf-8'))
orig_md = (IC / 'sections/007-original.md').read_text(encoding='utf-8').strip()
md = orig_md
for k, v in D.items():
    assert md.count(O[k]) == 1, k
    md = md.replace(O[k], v)
(HERE / ('section-d%d.md' % n)).write_text(md + '\n', encoding='utf-8')
changed = [k for k in O if k in D and D[k] != O[k]]

CARD = re.compile(r'\[Spirit and Mind Health\]\(.*?\[image 10\]\([^)]*\)', re.S)
def reader_view(t):
    t = CARD.sub('[An embedded post card: "Facing the Polycrisis: Is There Hope For Humanity?", by u-dont-exist.com '
                 '(the author), 15 November 2025. The card shows the opening of that post:]', t)
    t = t.replace(O['P2'], '> ' + O['P2'])
    t = re.sub(r'(?m)^\[Read full story\]\([^)]*\)[ \t]*$', '[the card ends with a link: Read full story]', t)
    t = re.sub(r'(?m)^\[image 11\]\([^)]*\)[ \t]*$', '[an image]', t)
    t = re.sub(r'(?m)^\[caption\] ', "[the image's caption:] ", t)
    return t
ov, rv = reader_view(orig_md), reader_view(md)
OUT = HERE / ('review-d%d' % n)
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir()
NUMBERING = ('Number its paragraphs P1 to P10 in order: P1 "Loneliness is only one reason…", P2 the excerpt quoted in the embedded '
             'post card ("I just read this post from Jamie Wheal…", the author\'s own earlier post; it is not rewritten), P3 "I don’t know '
             'exactly…", P4 "I’d rather build…", P5 "The useful design question…", then the image and its caption (not numbered), P6 '
             '"Medical care, banking…", P7 "The Amish…", P8 "Medicine is…", P9 "No member…", P10 "At the same time…".')
BRIEF = """# Blind two-way preservation trace: one section of an essay on intentional communities

You're checking a rewrite against the published original. Open only the files in this folder. Don't look for notes, other folders or the web.

Files:
- `original-section.md`: the published section, under one heading. {numbering}
- `R-*.md`: the rewritten paragraphs you trace ({keys}), named by the published paragraph they answer.
- `R-section.md`: the whole rewrite assembled in order, with the heading, the card and the image in place. Use it for the sense check across paragraphs.

The author's rulings for this rewrite: the wording can change freely as long as the meaning stays: the same claims at the same strength, the same people doing the same things, nothing new about anyone. A quip may go if its point stays, when the point matters. Specific pairings turned into a general tangle are a changed claim, not lost detail. The author's first person ("I", "my") may say only what the original says he did, knows, felt or thinks. Advice must stay advice: a recommendation turned into an observation (or the reverse) is SHIFTED.

For each rewrite file:
1. Which original paragraph it answers.
2. **Forward.** Split the original paragraph into units of meaning: one per claim, condition, quantity, time, attribution, hedge, example or link, and one per logical relation between items or clauses (or, and/also, but, because/so, if/unless, rather than, only, even). A changed relation is SHIFTED unless it says exactly the same thing: "may be wise, or may be unvetted" (one of these) became "may be wise. They may also be someone who…" (both at once) in an earlier rewrite, and a trace called it the same meaning; the author: "OR is not ALSO". Mark each SAME, SAME-MEANING (reworded, same meaning and strength), SHIFTED (meaning, scope, strength, voice, tense of a claim or attribution changed; say exactly how) or DROPPED.
3. **Reverse.** List everything in the rewrite that isn't in the original (ADDED): facts, claims, judgments, feelings, causes, people, intensifiers, hedges, scare quotes, rhetorical tags.
4. **Sources.** Links (same URL, doing the same job), quotation marks, who said or did what, numbers and dates.
5. **Sense.** Every word or pronoun whose referent a reader can't find in the visible text (this paragraph, or what comes before it in `R-section.md`), tense slips, grammar that makes you reread.

Put the marks in tables. Don't judge whether the rewrite is better, and don't suggest rewrites. Be exhaustive: a small shift counts.

Keep the whole report under 1,200 words: terse tables, one row per unit, no prose beyond what a row needs. Write it to `{report}` with one Write call. Then return only a summary table: file, the count of SHIFTED, DROPPED and ADDED, and one line for each change that alters what a reader would believe about a fact, a person, or the author's position.
"""
PARTS = {2: {"A": ["P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10"]}, 11: {"A": ["P1", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10"]}, 13: {"A": ["P3", "P5", "P7", "P8", "P9", "P10"]}, 17: {"A": ["P3", "P4", "P5", "P7", "P8", "P9", "P10"]}, 19: {"A": ["P3", "P8"]}, 20: {"A": ["P4", "P5", "P8", "P9"]}}
parts = {h: [k for k in ks if k in changed] for h, ks in PARTS.get(n, {'A': changed}).items()}
for half, keys in parts.items():
    if not keys: continue
    d = OUT / ('trace' + half); d.mkdir()
    (d / 'original-section.md').write_text(ov + '\n', encoding='utf-8')
    (d / 'R-section.md').write_text(rv + '\n', encoding='utf-8')
    for k in keys:
        (d / ('R-%s.md' % k)).write_text(D[k] + '\n', encoding='utf-8')
    (d / 'BRIEF.md').write_text(BRIEF.format(numbering=NUMBERING, keys=', '.join(keys), report=str(HERE / ('TRACE-d%d-%s.md' % (n, half)))), encoding='utf-8')
# cold read: section 5 as installed (Joel's own text), this section, the start of section 7
so_far = re.sub(r'<!--.*?-->', '', (HERE.parent / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'), flags=re.S)
a = so_far.index("# The Medicine Part - Yes, I'm Naming It"); b = so_far.index('# Which Connections to the Technosphere Do You Keep?')
before = so_far[a:b].strip()
before = re.sub(r'(?m)^\[(image \d+)\]\([^)]*\)\s*$', '[an image]', before)
before = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', before)
nxt = (IC / 'sections/008-original.md').read_text(encoding='utf-8')
nxt_start = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', '\n\n'.join(nxt.strip().split('\n\n')[:3]))
last = R.read('sense.txt').split('\n\n')[-1]
plain_rv = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', re.sub(r'^#+\s*', '', rv, flags=re.M))
sense = ("Below is one section from an essay about intentional communities and communes, with the section the reader has just read "
         "before it, and the start of the section after it. Earlier in the essay (not shown) the author wrote about the U.S. Surgeon "
         "General's 2023 advisory on loneliness, and about Chantress Seba, an Instagram influencer who posted an application for people "
         "interested in starting a commune.\n\n"
         "Read it as an ordinary reader who is seeing it for the first time. Your only job is to check whether it makes sense. "
         "Don't judge the style, and don't say whether it sounds like AI.\n\n"
         "For each numbered sentence of THE SECTION, write one line: OK if it makes sense right where it is, or UNCLEAR followed by "
         "exactly what trips you up (a word or pronoun whose meaning you can't pin down, a jump you can't follow, a claim that seems to "
         "come from nowhere, grammar that makes you reread). Then write one line for each paragraph saying whether it makes sense after "
         "the one before it, one line saying whether the heading's promise is met by the paragraph under it, and one line saying whether "
         "the section after it follows on. Keep each line short; don't repeat the sentences back.\n\n"
         "The section before (the reader has just read it):\n" + before + "\n\n"
         "THE SECTION:\n" + R.numbered(plain_rv) + "\n\n"
         "The start of the section after:\n" + nxt_start + "\n\n" + last)
(OUT / 'sense').mkdir(); (OUT / 'sense' / 'prompt.txt').write_text(sense, encoding='utf-8')
st = SC.build((IC / 'original.md').read_text(encoding='utf-8'), rv,
              scope='section 6 ("Which Connections to the Technosphere Do You Keep?"); sections 1 to 5 were checked before',
              topic='intentional communities', report=str(HERE / ('STANCE-d%d.md' % n)))
(OUT / 'stance').mkdir(); (OUT / 'stance' / 'prompt.txt').write_text(st, encoding='utf-8')
LOGIC = """# Logic audit: one section of an essay on intentional communities, rewrite against the published original

Open only the files in this folder. Don't look for notes, other folders or the web.

- `original-section.md`: the published section. {numbering}
- `R-section.md`: the rewrite, the same paragraphs in the same order under the same heading.

Your one job is the logic of each paragraph: whether the rewrite keeps the published paragraph's logical relations. Not style, not wording, not what was dropped as such. Compare every paragraph, P1 to P10, and look at:
- connectives between items and clauses: or (one of these), and / also / too (all of these, or both at once), but / though (contrast), because / since / so (cause and effect, and which way it runs), if / unless / when (a condition), rather than / instead of, only, even, still;
- negation and its scope (not, never, no, neither … nor, without);
- quantifiers (all, every, any, most, many, some, a few, none) and the set they range over (members, anyone, people in general);
- modality (can, may, might, will, would, must, should, has to): a possibility made a certainty, a rule made a suggestion, advice made an observation, or the reverse;
- degree and comparison (more, less, especially, even more, full, completely);
- evidence and causation: "links X with Y" (an association) against "the impact of X on Y" (a cause);
- who does what to whom (who decides, who acts, who pays, who is affected);
- sequence and time (first, before, in advance, after, until, eventually).

Be skeptical. An earlier review called this pair the same meaning: published "A retreat-circuit facilitator may be wise, or may be unvetted, unaccountable, sexually predatory, … or simply wrong", rewrite "The facilitator on the retreat circuit may be wise. They may also be someone who hasn't been vetted…". It isn't: "or" says the facilitator is one of these and you don't know which (the next sentence depends on it), "also" says they may be wise and a predator at once. The author: "OR is not ALSO". Look for every change of that kind.

For each paragraph, a table: the relation, the published wording, the rewrite's wording, and a verdict: SAME, CHANGED (say what a reader would now believe that the original doesn't say), or AMBIGUOUS (the rewrite can be read either way; give both readings). List only relations that differ in wording; one line saying "no changed relations" is enough for a paragraph where none do.

Keep the report under 1,500 words. Write it to `{report}` with one Write call. Then return only the list of CHANGED and AMBIGUOUS findings, one line each: paragraph, the two wordings, what a reader would wrongly believe.
"""
for half in ('A', 'B'):
    d = OUT / ('logic' + half); d.mkdir()
    (d / 'original-section.md').write_text(ov + '\n', encoding='utf-8')
    (d / 'R-section.md').write_text(rv + '\n', encoding='utf-8')
    (d / 'BRIEF.md').write_text(LOGIC.format(numbering=NUMBERING, report=str(HERE / ('LOGIC-d%d-%s.md' % (n, half)))), encoding='utf-8')
for d in sorted(OUT.iterdir()):
    if d.is_dir(): print(d.name, sum(len(p.read_text(encoding='utf-8').split()) for p in d.iterdir()), 'words')
print('changed:', ' '.join(changed))
