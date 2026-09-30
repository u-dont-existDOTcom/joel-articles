#!/usr/bin/env python3
"""reviewer.py - build the prompts for the reviewer-writer loop (2026-09-28).

Joel, 2026-09-28 00:56: "you can easily notice what looks ai from a prior turn, but not in
this turn. that's why a sub agent should fix the problem ... the sentence by sentence
engineering prompt ... where a subagent would give the instructions for fixing each
sentence and the writer would follow those like an engineering task".

The reviewer learns Pangram's line from our own labeled paragraphs (tools/calibration),
not from tell definitions. Validation, the human-prose test and the loop's results are in
tools/REVIEWER-VALIDATION-20260928.md and experiments/REVIEWER-WRITER-LOOP-20260928.md.

Each prompt is written to a file of its own. A subagent is told to read that one file and
nothing else (so it can't see the PASS_/FAIL_ file names), and uses model "opus".

Usage:
  reviewer.py validation OUTDIR          two fold prompts and their answer keys
  reviewer.py review DRAFT TARGET OUT [--sense NOTES] [--note TEXT]
  reviewer.py writer DRAFT TICKETS TARGET OUT
  reviewer.py draft TARGET OUT              a first draft from the brief (writer_draft.txt)
  reviewer.py sense DRAFT TARGET OUT
  reviewer.py grounding DRAFT TARGET OUT [--blind]   guide-grounding and logic review (grounding.txt)
  reviewer.py human-test OUTDIR          the human-prose test (needs local/human_items.json)
  reviewer.py score KEYS.json ANSWERS.txt [ANSWERS.txt ...]

TARGET is a JSON file in targets/ with "before", "after" and "brief".
"""
import argparse, json, pathlib, random, re, sys

HERE = pathlib.Path(__file__).resolve().parent
CAL = HERE.parent / 'calibration'
LOCAL = HERE / 'local' / 'human_items.json'

FAMILIES = {
 'A': {
  'ce_guide': ['FAIL_ce_guide_r1_44pct', 'PASS_ce_guide_r2_joel_words', 'PASS_ce_guide_alone_r2'],
  'ce_jobs': ['FAIL_ce_jobs_r1b_definitions', 'PASS_ce_jobs_r2_scene', 'PASS_ce_jobs_r3_joel_guide'],
  'borrow_p5': ['FAIL_borrow_p5_r10', 'FAIL_borrow_p5_r10b', 'PASS_borrow_p5_joel_fix'],
  'outward': ['FAIL_outward_p1_accepted_20260918', 'FAIL_fix_outward_p1_r1', 'FAIL_outward_p1_rewrite_r1',
              'FAIL_outward_p1a_r2_sense_first', 'FAIL_outward_p1a_r5_dinner_scene', 'FAIL_outward_p1_r7_short_remark'],
  'spirit': ['FAIL_love_spirit_p1_r1', 'FAIL_love_spirit_p1_r2'],
  'threefn_p5': ['FAIL_threefn_p5_r1', 'FAIL_threefn_p5_r2c'],
  'askgod': ['PASS_love_askgod_p1', 'PASS_love_askgod_p2'],
  'tyler': ['PASS_tyler_p4_r1', 'PASS_tyler_p5_r1'],
  'fix': ['PASS_fix_ask_p1', 'PASS_fix_hook_p1'],
  'borrow_p3p4': ['PASS_borrow_p3_joel_fix', 'PASS_borrow_p4_r10'],
 },
 'B': {
  'threefn_p1': ['FAIL_threefn_p1_r1b', 'FAIL_threefn_p1_r2', 'FAIL_threefn_p1_r3b', 'PASS_threefn_p1_cut', 'PASS_threefn_p1_joel_fix'],
  'apprentice': ['FAIL_apprentice_p1_r1', 'PASS_apprentice_p1_r2', 'FAIL_apprentice_section_r1', 'FAIL_apprentice_section_r2', 'FAIL_apprentice_section_r3'],
  'music': ['FAIL_music_r2_mine', 'PASS_music_r4_mine'],
  'goodwill': ['PASS_love_goodwill_p1_r2', 'FAIL_love_goodwill_h3_r3', 'PASS_love_goodwill_p1_r1_fidelity_rejected'],
  'threefn_newp1': ['FAIL_threefn_newp1_r1', 'FAIL_threefn_newp1_r2'],
  'borrow_p6p7': ['PASS_borrow_guide_r8e', 'PASS_borrow_p7_r11', 'FAIL_borrow_p6p7_pair_r12'],
  'threefn_p2p4': ['PASS_threefn_p2_r1', 'PASS_threefn_p3_r1b', 'PASS_threefn_p4_r1'],
  'misc': ['PASS_ce_p2_worth_line', 'PASS_love_p2_r3', 'PASS_noticing', 'PASS_regulation'],
 },
}
# Two paragraphs that each pass alone and fail together: fine to learn from, not a fair single-passage test.
TRAIN_ONLY = {'FAIL_borrow_p6p7_pair_r12'}

NOTES = {
 'ce_guide': "Same paragraph three ways. In the first, the last two sentences are an AI's rewording of the author's two sentences. In the second they're the author's own words, unchanged. The third is the second without its first sentence. Pangram: the reworded one 44% AI, the flagged part in the later sentences; the other two 100% Human.",
 'ce_jobs': "Same paragraph. The first gives the Nurturer and the Protector a sentence each and then the party example. The second keeps only the party example, with both jobs inside it. The third is the second plus the author's own sentence about the Guide.",
 'borrow_p5': "Two AI attempts, then the author's minimal fix of the second attempt: he replaced the examples, merged 'You may still feel completely like the child...' and 'That's ok.' into one sentence, and added the 'Fake it til you make it' sentence and 'If it sounds funny, laugh!'.",
 'outward': "Six AI attempts at the same paragraph, all 100% AI: an early accepted version, a fix of it, a rewrite, a version written for sense first, a version built around a dinner scene, and a three-sentence remark with no instructions in it.",
 'spirit': "Two AI attempts at the same paragraph, both 100% AI.",
 'threefn_p5': "Two AI attempts at the same paragraph, both 100% AI.",
 'askgod': "Two consecutive paragraphs, AI-drafted with the author's feedback, each 100% Human.",
 'tyler': "Two consecutive paragraphs telling the author's friend's story (the story came from the author), AI-drafted with one of the author's lines, each 100% Human.",
 'fix': "Two paragraphs from an earlier accepted version, mostly AI-drafted with the author's edits over several rounds, each 100% Human.",
 'borrow_p3p4': "The first is the author's minimal fix of an AI draft; the second is an AI draft. Both Human.",
 'threefn_p1': "Same paragraph. The first two are earlier AI attempts. The third ends on a 'So...' sentence and is 100% AI. The fourth is the third without its last sentence: Human. The fifth is the third with the author's own last sentence in place of the AI's: Human.",
 'apprentice': "The first is an AI attempt (AI); the second is a rewrite (Human). The three 'section' versions put the passing second paragraph together with one or two more paragraphs, and all three came back 100% AI.",
 'music': "Two versions of the short lines that come after a song in the article.",
 'goodwill': "The first paragraph passed alone (Human). With a heading and a second paragraph added, the passage came back 54% AI, flagged in the later part. The third is an earlier first-person version that also passed.",
 'threefn_newp1': "Two AI attempts at a section opening, both 100% AI.",
 'borrow_p6p7': "Two consecutive paragraphs. Each passed alone. The two together, unchanged, came back 100% AI.",
 'threefn_p2p4': "Three consecutive short paragraphs, AI-drafted, each 100% Human.",
 'misc': "Assorted passages that passed. The first is mostly the author's own paragraph with one AI sentence. The last two are whole short sections with headings.",
}

JOEL = [  # Joel's own paragraphs from the article (Also Look Outward P2; the Celine paragraph)
 "You may not know for certain whether the other person is or could be capable of a healthier response, and neither do they. If they promise to change, that's probably as useful as their prior promises were. Think about how long it has taken you to become more healthy. Could you have done that from one moment to the next based on a promise? Sometimes we can be a better support for someone when we maintain a realistic boundary, so that we can hold high expectations, and still feel prepared for their failure to meet them.",
 "Céline's song is called On ne change pas—\"we don't change.\" I think that's both fortunately and unfortunately true for most of us. Fortunately in the sense that the sweet, innocent, curious, vivacious little one is still inside us, even if hiding. Unfortunate in the sense that we often don't truly develop the adult qualities that we might pretend to have, so we continue burdening that little one inside us with troubles they aren't made for handling. This shows up in how we may feel abandoned, helpless, impulsive, frightened, or desperate to be chosen.",
]
BLOG_EXAMPLES = ['blog2015_noway_cheese', 'blog2015_truelove_p2', 'blog2016_perfect_p1', 'blog2015_noway_algebra', 'owner_heartloop']
PCT = {'FAIL_ce_guide_r1_44pct': '44% AI', 'FAIL_love_goodwill_h3_r3': '54% AI'}


def text(name):
    return (CAL / (name + '.txt')).read_text(encoding='utf-8').strip()


def label(name):
    return 'AI' if name.startswith('FAIL_') else 'HUMAN'


def pct(name):
    return PCT.get(name, '100% AI' if label(name) == 'AI' else '100% Human')


def split_sentences(p):
    """Like tells_lint.sentences, but keeps a closing quote with its sentence."""
    p = re.sub(r'\s+', ' ', p).strip()
    parts = re.split(r'(?<=[.!?]["”)])\s+(?=["“(]?[A-Z0-9])|(?<=[.!?])\s+(?=["“(]?[A-Z0-9])', p)
    out = []
    for s in (x.strip() for x in parts if x and x.strip()):
        if out and out[-1].endswith(('Mr.', 'Mrs.', 'Ms.', 'Dr.', 'St.', 'vs.', 'e.g.', 'i.e.')):
            out[-1] += ' ' + s
        else:
            out.append(s)
    return out


def numbered(t):
    out, n = [], 0
    for p in [p for p in re.split(r'\n\s*\n', t) if p.strip()]:
        if len(p.split()) <= 12 and not p.rstrip().endswith(('.', '?', '!', '"', '”', ':')):
            out.append('(heading) ' + p.strip())
            continue
        ss = []
        for s in split_sentences(p):
            n += 1
            ss.append('[%d] %s' % (n, s))
        out.append(' '.join(ss))
    return '\n\n'.join(out)


def read(name):
    return (HERE / name).read_text(encoding='utf-8')


def local_items():
    if not LOCAL.exists():
        return None
    d = json.loads(LOCAL.read_text(encoding='utf-8'))
    return {n: t for n, s, t in d['human']}, {n: t for n, s, t in d['ai']}


def examples(folds=('A', 'B'), skip='', extra=True):
    """Part 1 of a prompt: Joel's samples, the extra human and AI sets, then the labeled families."""
    same = lambda a, b: re.sub(r'\s+', ' ', a).strip() == re.sub(r'\s+', ' ', b).strip()
    parts = ["\n\nPART 1 — LABELED EXAMPLES (Pangram's verdicts)\n", "\n--- The author's own writing, for his natural voice ---\n"]
    for i, t in enumerate(JOEL, 1):
        parts.append("\nJ%d (the author's own writing (never edited by AI)):\n%s\n" % (i, t))
    li = local_items() if (folds == ('A', 'B') and extra) else None
    if li:
        H, A = li
        parts.append("\n--- More of the author's own writing, from his old blog (2013-2016, before AI tools) and from other articles. All human. ---\n")
        for i, n in enumerate(BLOG_EXAMPLES, 1):
            parts.append('\nJ%d:\n%s\n' % (i + 2, H[n]))
        parts.append("\n--- A set from his somatic-therapy article. The first two are humanized drafts of a short intro that the author accepted (both Pangram Human; not his own unassisted writing). The next three are an AI's attempts to write the same intro after reading those two (all three Pangram AI). ---\n")
        for n in ('owner_somatic_ex1', 'owner_somatic_ex2'):
            parts.append('\nS (humanized, Pangram Human):\n%s\n' % H[n])
        for n in ('somatic_model_A', 'somatic_model_B', 'somatic_model_C'):
            parts.append('\nS (AI attempt, Pangram AI):\n%s\n' % A[n])
        parts.append("\n--- Another pair from his romance article. The first is the author's version (Pangram Human, high confidence). The second is an AI's shorter version of the same material (Pangram about 60% AI). ---\n")
        parts.append('\nR (author, Human):\n%s\n' % H['owner_romance_high'])
        parts.append('\nR (AI, about 60%% AI):\n%s\n' % A['romance_assistant'])
    elif folds == ('A', 'B') and extra:
        print('note: %s is missing, so the blog, somatic and romance examples are left out' % LOCAL, file=sys.stderr)
    k = 0
    for fold in folds:
        for fam, names in FAMILIES[fold].items():
            k += 1
            parts.append('\n--- Group %d. %s ---\n' % (k, NOTES[fam]))
            for j, nm in enumerate(names, 1):
                if skip and same(text(nm), skip):
                    continue   # never show the draft under review as a labeled example
                parts.append('\n%d%s — Pangram: %s\n%s\n' % (k, 'abcdefgh'[j - 1], pct(nm), text(nm)))
    return ''.join(parts)


def build_validation(outdir):
    out = pathlib.Path(outdir)
    for train, test, seed in (('A', 'B', 11), ('B', 'A', 12)):
        tests = [nm for names in FAMILIES[test].values() for nm in names if nm not in TRAIN_ONLY]
        random.Random(seed).shuffle(tests)
        prefix = 'Q' if test == 'A' else 'R'
        key, parts = {}, [read('rubric.txt'), examples((train,))]
        parts.append('\n\nPART 2 — PASSAGES TO JUDGE (%d passages; sentences numbered)\n' % len(tests))
        for i, nm in enumerate(tests, 1):
            pid = '%s%02d' % (prefix, i)
            key[pid] = {'name': nm, 'label': label(nm)}
            parts.append('\n=== %s ===\n%s\n' % (pid, numbered(text(nm))))
        parts.append(read('output_verdicts.txt'))
        d = out / ('train%s_test%s' % (train, test))
        d.mkdir(parents=True, exist_ok=True)
        (d / 'prompt.txt').write_text(''.join(parts), encoding='utf-8')
        (out / ('key_test%s.json' % test)).write_text(json.dumps(key, indent=1), encoding='utf-8')
        print(d / 'prompt.txt', '(keep the key file out of the folder the subagent reads)')


def build_review(draft, target, extra=''):
    t = json.loads(pathlib.Path(target).read_text(encoding='utf-8'))
    p = [read('rubric.txt'), examples(skip=draft), '\n\nPART 2 — THE PARAGRAPH TO REVIEW\n']
    p.append('\nWhat the paragraph has to get across (the meaning, not an outline; any order, any number of sentences):\n%s\n' % t['brief'])
    p.append("\nThe paragraph before it in the article (context only; don't judge it):\n%s\n" % t['before'])
    p.append('\nTHE PARAGRAPH (sentences numbered):\n%s\n' % numbered(draft))
    p.append("\nThe paragraph after it (context only; the author wrote it; don't judge it):\n%s\n" % t['after'])
    if extra:
        p.append(extra)
    p.append(read('tickets.txt'))
    return ''.join(p)


SENSE_EXTRA = """

ONE MORE THING BEFORE YOU WRITE TICKETS

A cold reader, who checked only whether the paragraph makes sense (not whether it sounds like AI), reported this:

%s

The article's owner requires that a paragraph make sense before anything else. So your tickets have to fix these sense problems. Fix them without bringing back the march: whatever keeps this paragraph from reading as an outline, keep it. It's fine for a sentence to stay long or a little rough, as long as a reader can follow it in one read. Judge the paragraph as it is now, then write your tickets in the same format.
"""


def build_writer(draft, tickets, target):
    t = json.loads(pathlib.Path(target).read_text(encoding='utf-8'))
    w = read('writer.txt')
    for k, v in (('{brief}', t['brief']), ('{before}', t['before']), ('{after}', t['after']),
                 ('{draft}', numbered(draft)), ('{tickets}', tickets)):
        w = w.replace(k, v)
    return w


def joel_fixes():
    # Joel's own before/after fixes, from JOEL-FIXES-CATALOGUE (2026-09-28). His rewrites teach more than
    # paraphrased lessons, so the examples go in as he wrote them.
    c = (HERE.parent / 'JOEL-FIXES-CATALOGUE-20260928.md').read_text(encoding='utf-8')
    a, b = c.index('## What he cuts'), c.index('## In his words')
    return ("How the author himself has fixed AI drafts, with his exact before and after wording. "
            "These are examples of what he changes, not a checklist:\n\n" + c[a:b].strip())


def build_draft(target):
    t = json.loads(pathlib.Path(target).read_text(encoding='utf-8'))
    w = read('writer_draft.txt')
    for k in ('brief', 'before', 'after'):
        w = w.replace('{%s}' % k, t[k])
    if t.get('length'):  # a target can set its own length (e.g. two guide paragraphs merged into one)
        w = w.replace('two or three sentences, 50 to 80 words', t['length'])
    i = w.index('Write the paragraph:')
    return w[:i] + joel_fixes() + '\n\n' + w[i:]


def build_sense(draft, target):
    t = json.loads(pathlib.Path(target).read_text(encoding='utf-8'))
    s = read('sense.txt')
    return s.replace('{before}', t['before']).replace('{after}', t['after']).replace('{draft}', numbered(draft))


def build_human_test(outdir):
    li = local_items()
    if not li:
        sys.exit('local/human_items.json is missing; see human_items.manifest.json')
    d = json.loads(LOCAL.read_text(encoding='utf-8'))
    items = [(n, 'HUMAN', t) for n, s, t in d['human']] + [(n, 'AI', t) for n, s, t in d['ai']]
    outv = read('output_verdicts.txt').replace('Q01 AI 80', 'X01 AI 80').replace('Q02 HUMAN 70', 'X02 HUMAN 70')
    for seed, run in ((21, 'h1'), (22, 'h2')):
        order = items[:]
        random.Random(seed).shuffle(order)
        # The human-test items are the extra examples, so they stay out of Part 1 here.
        key, parts = {}, [read('rubric.txt'), examples(extra=False)]
        parts.append('\n\nPART 2 — PASSAGES TO JUDGE (%d passages; sentences numbered)\n' % len(order))
        parts.append("These come from several places: the same author's other writing (old blog posts, other articles, notes) and AI drafts. They're not all about inner-child therapy, and they aren't in the same proportions as Part 1. Judge each one the same way: what would Pangram say?\n")
        for i, (n, lab, t) in enumerate(order, 1):
            pid = 'H%02d' % i
            key[pid] = {'name': n, 'label': lab}
            parts.append('\n=== %s ===\n%s\n' % (pid, numbered(t)))
        parts.append(outv)
        p = pathlib.Path(outdir) / ('human_' + run) / 'prompt.txt'
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(''.join(parts), encoding='utf-8')
        (pathlib.Path(outdir) / ('key_human_%s.json' % run)).write_text(json.dumps(key, indent=1), encoding='utf-8')
        print(p)


def score(keyfile, answerfiles):
    key = json.loads(pathlib.Path(keyfile).read_text(encoding='utf-8'))
    pred = {}
    for f in answerfiles:
        for line in pathlib.Path(f).read_text(encoding='utf-8').splitlines():
            m = re.match(r'\s*([A-Z]\d\d)\s+(AI|HUMAN)\s+(\d+)', line)
            if m:
                pred[m.group(1)] = (m.group(2), int(m.group(3)))
    ok = sum(1 for pid, k in key.items() if pid in pred and pred[pid][0] == k['label'])
    ai = [pid for pid, k in key.items() if k['label'] == 'AI']
    hu = [pid for pid, k in key.items() if k['label'] == 'HUMAN']
    print('right %d/%d; AI caught %d/%d; Human called Human %d/%d' % (
        ok, len(key), sum(pred.get(p, ('',))[0] == 'AI' for p in ai), len(ai),
        sum(pred.get(p, ('',))[0] == 'HUMAN' for p in hu), len(hu)))


# --- Guide-grounding and logic review (Joel, 2026-09-29 19:14: "One role the reviewer instance should have is
# checking whether the sentence not only makes sense based on the guide but whether it goes beyond the guide in a
# way that needs support from the guide." Logic rules from UDA patterns/whole-argument-reconstruction.md and
# docs/requirements/2026-09-13-predicate-alignment-before-correction.owner-requirement.md.) ---

GUIDE_HTML = HERE.parent.parent / 'master.html'
ARTICLE_MD = HERE.parent.parent / 'HUMANIZED-ARTICLE-SO-FAR.md'


def guide_text():
    import html as _html
    s = GUIDE_HTML.read_text(encoding='utf-8')
    s = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', s, flags=re.S)
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'</(p|h[1-6]|li|blockquote|div)>', '\n\n', s)
    s = _html.unescape(re.sub(r'<[^>]+>', '', s))
    return re.sub(r'\n\s*\n+', '\n\n', s).strip()


def article_text():
    """The article as a reader sees it: no comments, no working-notes header."""
    s = re.sub(r'<!--.*?-->', '', ARTICLE_MD.read_text(encoding='utf-8'), flags=re.S)
    paras = [x for x in re.split(r'\n\s*\n', s) if x.strip()]
    paras = [x for x in paras if not x.lstrip().startswith('> **Working review')
             and not x.startswith('# Inner Child Therapy — humanized article so far')]
    return '\n\n'.join(p.strip() for p in paras)


PUSH = {  # how hard the grounding review pushes on the reader's open questions (Joel, 2026-09-30 04:44)
    'tight': ("tight. Raise only MUST questions. A fix stays inside the existing sentences or adds a clause, "
              "and the section shouldn't grow by more than about 5%. Everything else goes on PARKED or is ASK AUTHOR."),
    'default': ("default. Raise MUST and SHOULD questions. A fix can add up to about one short sentence per paragraph, "
                "and the section can grow or shrink by up to about 10%. Anything bigger is ASK AUTHOR. "
                "The author doesn't want the article to grow much; small increases or decreases are fine when they're warranted."),
    'wide': ("wide. Raise MUST, SHOULD and COULD questions. A fix can add a sentence or two per paragraph, or suggest a new "
             "paragraph, but anything that would change what the section is about is still ASK AUTHOR."),
}


def build_grounding(draft, target, blind=False, push=None):
    t = json.loads(pathlib.Path(target).read_text(encoding='utf-8'))
    push = push or t.get('push', 'default')
    g = read('grounding.txt')
    if blind:  # validation: leave out the worked examples, which quote the errors being tested
        a, b = g.index('Why this review exists.'), g.index('THE STEPS')
        g = g[:a] + g[b:]
    art = t.get('article_upto')
    if art is None:
        full, tail = article_text(), re.sub(r'\s+', ' ', t['before'].strip())[-80:]
        flat = re.sub(r'\s+', ' ', full)
        k = flat.rfind(tail)
        if k < 0:
            sys.exit("the target's 'before' isn't in the article; give 'article_upto' in the target")
        art = flat[:k + len(tail)]
    d = numbered(re.sub(r'^#+\s*', '', draft, flags=re.M)).replace('(heading) ', '[H] ')
    for k, v in (('{guide}', guide_text()), ('{article}', art), ('{guide_passage}', t['guide_passage']),
                 ('{next}', t.get('next', '(not given)')), ('{rulings}', t.get('rulings') or '(none)'), ('{push}', PUSH[push]), ('{draft}', d)):
        g = g.replace(k, v)
    return g


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    s = sub.add_parser('validation'); s.add_argument('outdir')
    s = sub.add_parser('review'); s.add_argument('draft'); s.add_argument('target'); s.add_argument('out')
    s.add_argument('--sense', help="a file with a cold reader's notes the tickets must fix")
    s.add_argument('--note', default='', help='extra text placed before the instructions')
    s = sub.add_parser('writer'); s.add_argument('draft'); s.add_argument('tickets'); s.add_argument('target'); s.add_argument('out')
    s = sub.add_parser('sense'); s.add_argument('draft'); s.add_argument('target'); s.add_argument('out')
    s = sub.add_parser('draft'); s.add_argument('target'); s.add_argument('out')
    s = sub.add_parser('grounding'); s.add_argument('draft'); s.add_argument('target'); s.add_argument('out')
    s.add_argument('--blind', action='store_true', help='leave out the worked examples (for validation)')
    s.add_argument('--push', choices=sorted(PUSH), help="how hard to push on the reader's open questions (default: the target's 'push', else default)")
    s = sub.add_parser('human-test'); s.add_argument('outdir')
    s = sub.add_parser('score'); s.add_argument('key'); s.add_argument('answers', nargs='+')
    a = ap.parse_args()
    rd = lambda f: pathlib.Path(f).read_text(encoding='utf-8').strip()
    def write(out, txt):
        p = pathlib.Path(out); p.parent.mkdir(parents=True, exist_ok=True); p.write_text(txt, encoding='utf-8')
        print('%d words -> %s' % (len(txt.split()), p))
    if a.cmd == 'validation':
        build_validation(a.outdir)
    elif a.cmd == 'review':
        extra = (SENSE_EXTRA % rd(a.sense)) if a.sense else ''
        write(a.out, build_review(rd(a.draft), a.target, extra + a.note))
    elif a.cmd == 'writer':
        write(a.out, build_writer(rd(a.draft), rd(a.tickets), a.target))
    elif a.cmd == 'draft':
        write(a.out, build_draft(a.target))
    elif a.cmd == 'sense':
        write(a.out, build_sense(rd(a.draft), a.target))
    elif a.cmd == 'grounding':
        write(a.out, build_grounding(rd(a.draft), a.target, a.blind, a.push))
    elif a.cmd == 'human-test':
        build_human_test(a.outdir)
    elif a.cmd == 'score':
        score(a.key, a.answers)


if __name__ == '__main__':
    main()
