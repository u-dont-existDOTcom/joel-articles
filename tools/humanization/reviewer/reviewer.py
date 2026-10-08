#!/usr/bin/env python3
"""reviewer.py - build the prompts for the reviewer-writer loop (2026-09-28).

Joel, 2026-09-28 00:56: "you can easily notice what looks ai from a prior turn, but not in
this turn. that's why a sub agent should fix the problem ... the sentence by sentence
engineering prompt ... where a subagent would give the instructions for fixing each
sentence and the writer would follow those like an engineering task".

The reviewer learns Pangram's line from our own labeled paragraphs (../calibration/),
not from tell definitions. Validation, the human-prose test and the loop's results are in
../REVIEWER-VALIDATION-20260928.md and
articles/inner-child-therapy/experiments/REVIEWER-WRITER-LOOP-20260928.md.

Each prompt is written to a file of its own. A subagent is told to read that one file and
nothing else (so it can't see the PASS_/FAIL_ file names), and uses model "opus".

Usage (from the repo root):
  python3 tools/humanization/reviewer/reviewer.py [--article ARTICLE.md] [--source SOURCE] COMMAND ...
The commands:
  reviewer.py validation OUTDIR          two fold prompts and their answer keys
  reviewer.py review DRAFT TARGET OUT [--sense NOTES] [--note TEXT]
  reviewer.py writer DRAFT TICKETS TARGET OUT
  reviewer.py draft TARGET OUT              a first draft from the brief (writer_draft.txt)
  reviewer.py sense DRAFT TARGET OUT        reads the article when the target has "earlier": "section"
  reviewer.py grounding DRAFT TARGET OUT [--blind] [--push tight|default|wide]
                                            guide-grounding and logic review (grounding.txt); reads the
                                            source, and the article unless the target has "article_upto"
  reviewer.py human-test OUTDIR          the human-prose test (needs local/human_items.json)
  reviewer.py score KEYS.json ANSWERS.txt [ANSWERS.txt ...]
  reviewer.py march DRAFT OUT               the marching-order check (march.txt): a reader labels each
                                            sentence a step or a break; give it to a "sonnet" subagent
  reviewer.py march-score DRAFT LABELS      reads that reader's answer and flags a paragraph with no break
  reviewer.py dedup OUT TARGET [TARGET ...] [--draft TARGET=FILE ...] [--report PATH]
                                            the whole-article dedup check (dedup.txt, E151): every point of each
                                            target's guide passage against the whole article and against the
                                            other targets, SAID / PARTLY / NEW, and what's left to add. Run it
                                            before drafting, and again with the drafts; give it to an "opus" subagent
  reviewer.py repeats OUT --article A [--focus TEXT] [--report PATH]
                                            the whole-article repeat check (repeats.txt, E151): every point the
                                            article makes twice, and contradictions

TARGET is a JSON file with "before", "after" and "brief". Each article keeps its own targets
(Inner Child: articles/inner-child-therapy/tools/targets/).

The article and its source:
  --article PATH  the humanized article (Markdown).
  --source PATH   what the article is made from ("the guide"): HTML, read with its tags stripped,
                  or Markdown or plain text, read as is.
Without the flag, the target's "article" or "source" key is used: a path from the repo root.
A command that needs one and gets neither stops with a message. The flags can go before or
after the command. The calibration texts, the Joel fixes catalogue and the prompt files are
found from this script's folder. For example (Inner Child's targets carry both keys):
  python3 tools/humanization/reviewer/reviewer.py grounding DRAFT.txt \\
      articles/inner-child-therapy/tools/targets/love-doesnt-wait-p5.json OUT.txt
"""
import argparse, json, pathlib, random, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]  # the repo root (tools/humanization/reviewer/ is three folders down)
CAL = HERE.parent / 'calibration'
LOCAL = HERE / 'local' / 'human_items.json'
PATHS = {'article': None, 'source': None}  # from --article and --source
WHAT = {'article': 'the humanized article (Markdown)', 'source': "the article's source (the guide)"}


def article_or_source(t, key):
    """The article ('article') or its source ('source') for target t: the --article or --source
    flag if given, else the target's own key, a path from the repo root."""
    if PATHS[key]:
        return pathlib.Path(PATHS[key])
    if t.get(key):
        return ROOT / t[key]
    sys.exit('reviewer.py: this command needs %s. Give --%s PATH, or put "%s" in the target '
             '(a path from the repo root).' % (WHAT[key], key, key))


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
    t = (HERE / name).read_text(encoding='utf-8')
    if '{bans}' in t:
        # Joel's bans come from owner_bans.txt, so a ban added there reaches every prompt. Until 2026-10-03 the
        # prompts held copies, and the copies had stopped at five of its lines: no writer was told about feelings
        # as agents, the "enough to" pair or chat acronyms (a turn-19 writer wrote "IMO").
        t = t.replace('{bans}', (HERE / 'owner_bans.txt').read_text(encoding='utf-8').strip())
    return t


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


NORM = str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"', '—': ' ', '–': ' '})


def norm(s):
    return ' '.join(re.sub(r'[^a-z0-9]+', ' ', s.translate(NORM).lower()).split())


def original_text(t):
    """The guide the article was first made from (Inner Child: its folder's master.html), or the target's
    "original": a path from the repo root. None when there isn't one."""
    if t.get('original'):
        p = ROOT / t['original']
    else:
        try:
            p = pathlib.Path(article_or_source(t, 'article')).parent / 'master.html'
        except SystemExit:
            return None
    return guide_text(p) if p.exists() else None


def guide_additions(t):
    """The guide passage's sentences that aren't in the original guide: what a later guide version added."""
    orig, gp = original_text(t), t.get('guide_passage')
    if not orig or not gp:
        return []
    body = re.sub(r'^The [^\n]*\(the passage this carries\):\n', '', gp.strip())
    o = norm(orig)
    return [s for s in split_sentences(body) if len(norm(s).split()) >= 4 and norm(s) not in o]


def require_provenance(t, name):
    """Joel, 2026-10-08 02:23: "maybe we should somehow implement a rule that guide additions can't be suggested by
    other owrkers unless they are explained, what map change caused them, and how they are really needed vs
    superfluous to the guide." A target whose guide passage adds to the original guide needs "provenance" with
    "map_change" (what changed upstream, and where: the pull request, amendment or node) and "why_reader_needs_it"
    (why the article's reader needs it, given what the guide and the article already say). Without both, no
    drafting (E155)."""
    add = guide_additions(t)
    pv = t.get('provenance') or {}
    if add and not (pv.get('map_change') and pv.get('why_reader_needs_it')):
        shown = '\n'.join('  - ' + s[:140] for s in add[:4]) + ('\n  - …' if len(add) > 4 else '')
        sys.exit('%s: this guide passage adds to the original guide (%d sentences, e.g.:\n%s\n), and the target has no '
                 'explanation. Add "provenance": {"map_change": "what changed upstream and where (PR, amendment, node)", '
                 '"why_reader_needs_it": "why the reader needs it, vs superfluous to what the guide and article say"} '
                 'before drafting (Joel, 2026-10-08: guide additions need to be explained; E155).' % (name, len(add), shown))


def build_draft(target):
    t = json.loads(pathlib.Path(target).read_text(encoding='utf-8'))
    require_provenance(t, pathlib.Path(target).name)
    w = read('writer_draft.txt')
    for k in ('brief', 'before', 'after'):
        w = w.replace('{%s}' % k, t[k])
    if t.get('length'):  # a target can set its own length (e.g. two guide paragraphs merged into one)
        w = w.replace('two or three sentences, 50 to 80 words', t['length'])
    if t.get('voice'):  # e.g. Joel's own story, told in his first person
        w = w.replace('in the second person like the paragraphs around it', t['voice'])
    i = w.index('Write the paragraph:')
    return w[:i] + joel_fixes() + '\n\n' + w[i:]


def earlier_section(t):
    # What a reader who got this far has read just before the paragraph before: the whole section before this
    # one, then this section's heading and any of its paragraphs up to the paragraph before. For a paragraph early
    # in a section, the paragraph before is too little: on 2026-09-30 the cold reads called "what you promised
    # them" a claim from nowhere, while the section before says "Keep one small promise to your little one"
    # (target key "earlier": "section").
    art = re.sub(r'<!--.*?-->', '', article_or_source(t, 'article').read_text(encoding='utf-8'), flags=re.S)
    i = art.find(t['before'])
    new_section = False
    if i < 0 and t.get('cut') and art.rfind(t['cut']) >= 0:
        # 'before' carries notes for the writers (a new heading, 2026-10-01): start from the paragraph that
        # ends with 'cut'. When 'append' opens a new section, the section that's ending is all that came before.
        i = art.rfind('\n\n', 0, art.rfind(t['cut'])) + 2
        new_section = bool(t.get('append'))
    if i < 0:
        sys.exit("the target's paragraph before isn't in the article yet, so what comes earlier can't be found")
    heads = [m.start() for m in re.finditer(r'(?m)^#{1,3} ', art[:i])]
    if not heads:
        return ''
    start = heads[-1] if new_section or len(heads) == 1 else heads[-2]
    return re.sub(r'\n{3,}', '\n\n', art[start:i]).strip()


def outline(t):
    # The headings a reader has passed on the way to this paragraph. On 2026-10-02 the cold reads couldn't place
    # "borrowed adulthood", the idea of a whole h1 (Borrow the Adult Before You Can Be the Adult), because they saw
    # only this section and the one before; Joel put it back in P6 himself ("But with the borrowed adulthood trick").
    try:
        art = article_text(article_or_source(t, 'article'))
    except SystemExit:
        return '(not given)'
    i = art.find(t['before'])
    if i < 0 and t.get('cut'):
        i = art.rfind(t['cut'])
    heads = re.findall(r'(?m)^#{1,3} .*$', art[:i] if i >= 0 else art)
    return '\n'.join(heads) or '(none)'


def build_sense(draft, target):
    t = json.loads(pathlib.Path(target).read_text(encoding='utf-8'))
    s = read('sense.txt')
    earlier = ''
    if t.get('earlier') == 'section':
        earlier = ('Earlier in the article (the reader has already read this):\n'
                   + earlier_section(t) + '\n\n')
    return (s.replace('{outline}', outline(t)).replace('{earlier}', earlier).replace('{before}', t['before'])
            .replace('{after}', t['after']).replace('{draft}', numbered(draft)))


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


def guide_text(path):
    """The source as text: HTML with its tags stripped, or Markdown or plain text as is."""
    import html as _html
    s = pathlib.Path(path).read_text(encoding='utf-8')
    if pathlib.Path(path).suffix.lower() not in ('.html', '.htm'):
        return s
    s = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', s, flags=re.S)
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'</(p|h[1-6]|li|blockquote|div)>', '\n\n', s)
    s = _html.unescape(re.sub(r'<[^>]+>', '', s))
    return re.sub(r'\n\s*\n+', '\n\n', s).strip()


def article_text(path):
    """The article as a reader sees it: no comments, no working-notes header (a "> **Working
    review" note, and a "# … humanized article so far" title)."""
    s = re.sub(r'<!--.*?-->', '', pathlib.Path(path).read_text(encoding='utf-8'), flags=re.S)
    paras = [x for x in re.split(r'\n\s*\n', s) if x.strip()]
    paras = [x for x in paras if not x.lstrip().startswith('> **Working review')
             and not re.match(r'# [^\n]*humanized article so far', x)]
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
        # 'cut' is where the article stops, when 'before' carries notes for the writers (e.g. a new heading)
        full, tail = article_text(article_or_source(t, 'article')), re.sub(r'\s+', ' ', (t.get('cut') or t['before']).strip())[-80:]
        flat = re.sub(r'\s+', ' ', full)
        k = flat.rfind(tail)
        if k < 0:
            sys.exit("the target's 'before' isn't in the article; give 'article_upto' in the target")
        art = flat[:k + len(tail)]
        if t.get('append'):  # text that isn't in the article yet but comes before the new text (a new heading)
            art += '\n\n' + t['append']
    d = numbered(re.sub(r'^#+\s*', '', draft, flags=re.M)).replace('(heading) ', '[H] ')
    for k, v in (('{guide}', guide_text(article_or_source(t, 'source'))), ('{article}', art), ('{guide_passage}', t['guide_passage']),
                 ('{next}', t.get('next', '(not given)')), ('{rulings}', t.get('rulings') or '(none)'), ('{push}', PUSH[push]), ('{draft}', d)):
        g = g.replace(k, v)
    return g


EMBED = re.compile(r'<!--\s*Native Substack embed[^"]*"([^"]+)"[^>]*-->')


def numbered_article(path):
    """The whole article as a reader sees it, each block numbered [B#] for the dedup checks (E151). An
    embedded post (a "Native Substack embed" note, or a bare Substack URL on its own line) becomes a
    bracketed note, so the paragraph that introduces it doesn't seem to dangle."""
    s = pathlib.Path(path).read_text(encoding='utf-8')
    s = EMBED.sub(lambda m: '\n\n[Embedded post by the author: "%s"]\n\n' % m.group(1), s)
    s = re.sub(r'<!--.*?-->', '', s, flags=re.S)
    out = []
    for p in (x.strip() for x in re.split(r'\n\s*\n', s) if x.strip()):
        if p.startswith('> **Working review') or re.match(r'# [^\n]*humanized article so far', p):
            continue
        if re.fullmatch(r'https://substack\.com/\S+', p):
            p = '[Embedded Substack note by the author, shown as a preview card]'
        out.append('[B%d] %s' % (len(out), p))
    return '\n\n'.join(out)


def report_line(report):
    return ('Write your findings to %s with the Write tool, in plain English, and reply with one line of counts.' % report
            if report else 'Return your findings as your final message, in plain English.')


def build_dedup(targets, drafts=None, report=None, article=None):
    """The whole-article dedup check for new material (E151): every guide point of every target, against the
    whole article and against each other, before drafting (and again with the drafts). drafts maps a target's
    file name (without .json) to its drafts."""
    drafts, groups, art = drafts or {}, [], None
    for n, tp in enumerate(targets, 1):
        t = json.loads(pathlib.Path(tp).read_text(encoding='utf-8'))
        require_provenance(t, pathlib.Path(tp).name)
        art = art or numbered_article(article or article_or_source(t, 'article'))
        flat, tail = re.sub(r'\s+', ' ', art), re.sub(r'\s+', ' ', (t.get('cut') or t['before']).strip())[-80:]
        k = flat.rfind(tail)
        where = re.findall(r'\[B(\d+)\]', flat[:k])[-1:] if k >= 0 else []
        g = ['GROUP %d (%s): would go right after [B%s]' % (n, pathlib.Path(tp).stem, where[0]) if where
             else 'GROUP %d (%s): its place is given in the brief' % (n, pathlib.Path(tp).stem)]
        g.append('The guide passage:\n\n' + re.sub(r'^The [^\n]*\(the passage this carries\):\n', '', t['guide_passage'].strip()))
        d = drafts.get(pathlib.Path(tp).stem)
        g.append('The drafts:\n\n' + d.strip() if d else '(No drafts yet: list the points and what is left to add.)')
        groups.append('\n\n'.join(g))
    return (read('dedup.txt').replace('{report}', report_line(report)).replace('{article}', art)
            .replace('{groups}', '\n\n---\n\n'.join(groups)))


def build_repeats(article, focus=None, report=None):
    """The whole-article repeat check (E151): every point the article makes more than once."""
    f = ('WHERE TO LOOK HARDEST\n\n%s was put together from several sources at different times, so check every block there '
         'against every other block there, and against the rest of the article. Then check the rest of the article against '
         'itself.' % focus) if focus else ''
    return (read('repeats.txt').replace('{focus}', f).replace('{report}', report_line(report))
            .replace('{article}', numbered_article(article)))


def march_paragraphs(t):
    """The draft's paragraphs that have sentences (headings and quotes-only lines are skipped)."""
    out = []
    for p in [p for p in re.split(r'\n\s*\n', t) if p.strip()]:
        p = re.sub(r'\s+', ' ', p.strip())
        if p.startswith('#') or (len(p.split()) <= 12 and not p.endswith(('.', '?', '!', '"', '”'))):
            continue
        out.append(split_sentences(p))
    return out


def build_march(draft):
    """The marching-order check (E131; Joel, 2026-10-03: "the marching order of code instructions
    translated to english"). A reader labels each sentence a step or a break. Tested blind on 100
    calibration paragraphs (tools/humanization/calibration/MARCH-READER-TEST-20261003.json): two readers
    agreed on 92% of the sentences, and a paragraph with no break failed Pangram 23 times out of 30,
    against 27 out of 70 with a break."""
    ps = march_paragraphs(draft)
    body = '\n\n'.join('T%d: ' % (i + 1) + ' '.join('[%d] %s' % (j + 1, s) for j, s in enumerate(ss))
                       for i, ss in enumerate(ps))
    return read('march.txt').replace('{n}', str(len(ps))).replace('{paragraphs}', body)


def march_score(draft, labels):
    ps = march_paragraphs(draft)
    got = dict(re.findall(r'^\s*T(\d+):\s*([SB ]+)\s*$', labels, re.M))
    worst = 0
    for i, ss in enumerate(ps):
        seq = got.get(str(i + 1), '').split()
        start = ' '.join(ss[0].split()[:8])
        if len(seq) != len(ss):
            print('T%d (%s…): the reader gave %d labels for %d sentences; ask again' % (i + 1, start, len(seq), len(ss)))
            worst = max(worst, 2)
            continue
        breaks = [j + 1 for j, x in enumerate(seq) if x == 'B']
        if not breaks:
            print('T%d (%s…): MARCH, %d steps and no break. In the 2026-10-03 test, 23 of 30 paragraphs like this failed '
                  'Pangram. Break it where a person would react, pause, allow something, or wonder what it feels like '
                  '(E131), rather than rewording the steps.' % (i + 1, start, len(ss)))
            worst = max(worst, 1)
        else:
            # The longest run of steps is where to start if Pangram still fails the paragraph (E134, Joel 2026-10-04:
            # "if they found them, then why couldn't you fix them? are you seeing the march there?"). In the 2026-10-03
            # sequence draft, P2 had breaks at 1-3 and then four steps; his fix went at exactly those four sentences.
            best, cur, end = 0, 0, 0
            for j, x in enumerate(seq):
                cur = cur + 1 if x == 'S' else 0
                if cur > best:
                    best, end = cur, j + 1
            run = ('; longest run of steps: %d-%d (%d sentences), the place to start if Pangram fails it'
                   % (end - best + 1, end, best)) if best >= 3 else ''
            print('T%d (%s…): breaks at %s (%s)%s' % (i + 1, start, ', '.join(map(str, breaks)), ' '.join(seq), run))
    return worst


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    files = argparse.ArgumentParser(add_help=False)  # the same two flags, accepted after the command too
    for p, default in ((ap, None), (files, argparse.SUPPRESS)):
        p.add_argument('--article', default=default, help="the humanized article (Markdown); default: the target's \"article\"")
        p.add_argument('--source', default=default, help="the article's source, HTML or Markdown/plain text; default: the target's \"source\"")
    sub = ap.add_subparsers(dest='cmd', required=True)
    cmd = lambda name: sub.add_parser(name, parents=[files])
    s = cmd('validation'); s.add_argument('outdir')
    s = cmd('review'); s.add_argument('draft'); s.add_argument('target'); s.add_argument('out')
    s.add_argument('--sense', help="a file with a cold reader's notes the tickets must fix")
    s.add_argument('--note', default='', help='extra text placed before the instructions')
    s = cmd('writer'); s.add_argument('draft'); s.add_argument('tickets'); s.add_argument('target'); s.add_argument('out')
    s = cmd('sense'); s.add_argument('draft'); s.add_argument('target'); s.add_argument('out')
    s = cmd('draft'); s.add_argument('target'); s.add_argument('out')
    s = cmd('grounding'); s.add_argument('draft'); s.add_argument('target'); s.add_argument('out')
    s.add_argument('--blind', action='store_true', help='leave out the worked examples (for validation)')
    s.add_argument('--push', choices=sorted(PUSH), help="how hard to push on the reader's open questions (default: the target's 'push', else default)")
    s = cmd('human-test'); s.add_argument('outdir')
    s = cmd('score'); s.add_argument('key'); s.add_argument('answers', nargs='+')
    s = cmd('march'); s.add_argument('draft'); s.add_argument('out')
    s = cmd('march-score'); s.add_argument('draft'); s.add_argument('labels')
    s = cmd('dedup'); s.add_argument('out'); s.add_argument('targets', nargs='+')
    s.add_argument('--draft', action='append', default=[], metavar='TARGET=FILE',
                   help="a target's drafts (TARGET is its file name without .json); repeat for each")
    s.add_argument('--report', help='a path the reader writes its findings to (default: its final message)')
    s = cmd('repeats'); s.add_argument('out')
    s.add_argument('--focus', help='the part of the article to check hardest, e.g. \'"# Before You Try to Go Deep" ([B32] to [B77])\'')
    s.add_argument('--report', help='a path the reader writes its findings to (default: its final message)')
    a = ap.parse_args()
    PATHS['article'], PATHS['source'] = a.article, a.source
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
    elif a.cmd == 'march':
        write(a.out, build_march(rd(a.draft)))
    elif a.cmd == 'march-score':
        sys.exit(march_score(rd(a.draft), rd(a.labels)))
    elif a.cmd == 'dedup':
        drafts = {}
        for d in a.draft:
            k, _, f = d.partition('=')
            drafts[k] = rd(f)
        write(a.out, build_dedup(a.targets, drafts, a.report, PATHS['article']))
    elif a.cmd == 'repeats':
        if not PATHS['article']:
            sys.exit('reviewer.py repeats: give --article PATH')
        write(a.out, build_repeats(PATHS['article'], a.focus, a.report))


if __name__ == '__main__':
    main()
