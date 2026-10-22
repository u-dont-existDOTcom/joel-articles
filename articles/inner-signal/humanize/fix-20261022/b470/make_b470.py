"""Batch 470g (2026-10-22): Joel's answers of 18:37 UTC to questions 9, 10 and 11, put into the guide.

- 9: "i would call anxiety a childhood protector part. that's what we have to protect us when the consciously installed
  parental Protector is not functioning, same as when we were children. let's make this more clear in the guide also."
  So the guards get his name, childhood protector parts, where the guide first reads "guard" (the opening's "guard mind"),
  where it explains them (Working with protectors, now Working with childhood protector parts, with his reason in his words)
  and where anxiety or a negative state is put down to one (You get anxious; the synchronicity cue, which question 9 asked
  about; Appendix D's opening, again with his reason; Stabilize before you interpret).
- 10 (one name for the inherited parent?): "check the work in the innerchild article lane regarding the naming conventions
  as they've been updated". The Inner Child lane's names, all his: the table he took at 13:22 UTC
  (articles/inner-child-therapy/experiments/t85-answers/JOEL-20261022-1322.md: "Nurturer, Adult Protector, Guide: Three
  functions of that same Inner Adult—not three additional people"; "Inherited parent script: Learned rules and ways of
  treating yourself—not necessarily a literal voice or only something learned from parents"; "Guards: Protective reactions
  or guarding patterns"), the core names he took at 14:26 UTC, and his nutshell of 16:12 UTC ("comprising a Nurturer, an
  Adult Protector (hereafter just the Protector) and a Guide"), with his three words for them that the Inner Child lane put
  at the first naming on his "81a" ("a loving Nurturer, a safe Adult Protector (hereafter just the Protector) and a wise
  Guide"; his rule, 16:12 UTC: "we should explain everything when it first gets read"). The Inner Child lane's note for
  this lane (NOTE-FROM-INNER-CHILD-LANE-20261022.md, part 2) lists the same. So: the third job is the Guide (Leader and Guru
  stay among the names a reader may give it); the Protector is first named the Adult Protector; the h1 gives the inner adult
  three jobs rather than making three inner adults; the inherited parent is the inherited parent script, explained once
  where the guide introduces it. The note's other two points (forced adulthood; the core names' learned patterns) are not
  names of figures this guide already has, so they go to Joel as question 12.
- 11 b: "If you are overwhelmed by chemicals, acutely confused, or not able to keep yourself safe, then get some immediate
  support instead of doing exploratory hypnosis." (HG17's installed text; the next HG17 version carries it too:
  fix-20261018/make_emu_bc.py.)

  python3 articles/inner-signal/humanize/fix-20261022/b470/make_b470.py   (from the repo root)
Writes CANDIDATE.md; EDITS-470g.json (for fix-20261020/apply_edits41.py --add); drafts.json and meta.json (each changed
paragraph as Pangram reads it, with its reading in the recheck of 2026-10-21); REVIEW-PROMPT.txt (one Opus reader: each
changed paragraph against the answers it carries out, its meaning, the names and its sense in place, -> REVIEW.md);
march/march-prompt.txt (Sonnet, -> march/march-labels.txt); sense/prompt.txt (the cold read of the h1 that holds most of
the changes, Opus, -> SENSE-HG14.md); stance/prompt.txt (Opus, -> STANCE.md), with REWRITE.md and POSITIONS.txt.
"""
import json, pathlib, subprocess, sys

B = pathlib.Path(__file__).resolve().parent
H = B.parents[1]
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
sys.path.insert(0, str(H / 'fix-20261021' / 'b469'))
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
sys.path.insert(0, str(REPO / 'tools' / 'humanization' / 'reviewer'))
import sections as S          # noqa: E402
import paragraphs_alone as PA  # noqa: E402
import reviewer as R          # noqa: E402
import score_b469 as SC       # noqa: E402

X = H / 'fix-20261020' / 'substack41r'
PARTS = [('A', 'https://www.pangram.com/feed/c8001eb5-84a6-41dc-a2c0-0f4733dc3fc7', X / 'RESULT-41r3-a.json'),
         ('B', 'https://www.pangram.com/feed/558d14f6-625d-46aa-8495-adf9141cb3a4', X / 'RESULT-41r2-b.json')]
H1_14 = '# The inner child, the guards, and the inner adult’s three jobs'
ABOUT = ('a long self-help guide to self-hypnosis ("the inner child", "little parts", "guards" or "childhood protector '
         'parts", and the inner adult\'s three jobs, "the Nurturer", "the Protector" and "the Guide", are the guide\'s terms)')

Q9 = ('Joel, 2026-10-22 18:37 UTC, question 9: "i would call anxiety a childhood protector part. that\'s what we have to '
      'protect us when the consciously installed parental Protector is not functioning, same as when we were children. '
      'let\'s make this more clear in the guide also."')
Q9S = Q9 + (' (Question 9 asked about this line: "If I am in a negative state, I check if it is a message from my Inner '
            'Child, my Protector or if I just need to grieve", where "my Protector" could be read as the role or as a guard.)')
Q10 = ('Joel, 2026-10-22 18:37 UTC, question 10 (one name for the inherited parent?): "check the work in the innerchild '
       'article lane regarding the naming conventions as they\'ve been updated". Those conventions, all his: "Nurturer, Adult '
       'Protector, Guide: Three functions of that same Inner Adult—not three additional people"; first named "a loving '
       'Nurturer, a safe Adult Protector (hereafter just the Protector) and a wise Guide"; "Inherited parent script: Learned '
       'rules and ways of treating yourself—not necessarily a literal voice or only something learned from parents"; '
       '"Guards: Protective reactions or guarding patterns"; and his rule "we should explain everything when it first gets '
       'read"')
Q11 = ('Joel, 2026-10-22 18:37 UTC, question 11: "b", that is: "If you are overwhelmed by chemicals, acutely confused, or not '
       'able to keep yourself safe, then get some immediate support instead of doing exploratory hypnosis." (The guide\'s '
       'own line elsewhere is at "feeling overwhelmed by chemicals"; its sessions include ones on loveyhuasca.)')

# (key, section, answer, old, new): each old text is in the working copy once; edits of one paragraph are in reading order
E = [
    ('guard-first-read', 'HG02+03', Q9 + ' And his rule, 2026-10-22 16:12 UTC: "we should explain everything when it first gets read"',
     'child mind, guard mind, body mind,', 'child mind, guard mind (your childhood protector parts), body mind,'),
    ('h1-three-jobs', 'HG14', Q10, '# The inner child, the guards, and the three inner adults', H1_14),
    ('three-jobs-named', 'HG14', Q10, 'your Nurturer, your Protector and your Leader/Guru, but',
     'your loving Nurturer, your safe Adult Protector (hereafter just the Protector) and your wise Guide, but'),
    ('h2-guide', 'HG14', Q10, '## The Leader, Guide, or Guru', '## The Guide'),
    ('guide-label', 'HG14', Q10, 'The Leader/Guide/Guru:', 'The Guide:'),
    ('guide-work', 'HG14', Q10, 'You can also work with your Leader. Call them whatever you want, Guide, Guru,',
     'You can also work with your Guide. Call them whatever you want, Leader, Guru,'),
    ('h2-protector-parts', 'HG14', Q9, '## Working with protectors', '## Working with childhood protector parts'),
    ('protector-parts-label', 'HG14', Q9, 'Working with protectors:', 'Working with childhood protector parts:'),
    ('guard-defined', 'HG14', Q9, 'they are you experiencing what is often a very charming protector or guard.',
     'they are you experiencing what is often a very charming guard, a childhood protector part. It\'s what protects you '
     'when your consciously installed parental Protector isn\'t functioning, the same as when you were a child.'),
    ('parent-script', 'HG14', Q10,
     'One important voice to become aware of when approaching your inner child is your inherited parent. This is the voice of '
     'your parent(s) that you internalized as a child, based on how they treated you. This is not the same as your inner adult '
     '(Nurturer, Protector, Leader/Guru) that you will eventually build up. Often this inherited parent acts as a critic or '
     'warden,',
     'One important thing to become aware of when approaching your inner child is your inherited parent script. This is the '
     'set of rules and ways of treating yourself that you internalized as a child, mostly based on how your parent(s) treated '
     'you, and it doesn’t always sound like a voice. This is not the same as your inner adult (Nurturer, Protector, Guide) '
     'that you will eventually build up. Often this script acts as a critic or warden,'),
    ('parent-script-fake', 'HG14', Q10, 'this voice may jump in to say', 'it may jump in to say'),
    ('to-the-part', 'HG14', Q9, '(To the protector: “I notice you', '(To the protector part: “I notice you'),
    ('talk-to-part', 'HG14', Q9, '(Now talk to the protector. Tell them', '(Now talk to the protector part. Tell them'),
    ('part-wants', 'HG14', Q9, 'Most of the time the protector wants you to do certain things,',
     'Most of the time the protector part wants you to do certain things,'),
    ('script-humiliating', 'HG15', Q10, 'Because often your inherited inner parent tells your inner child',
     'Because often your inherited parent script tells your inner child'),
    ('guide-care', 'HG20', Q10, '“Nurturer”, “Protector” or “Leader” to help you', '“Nurturer”, “Protector” or “Guide” to help you'),
    ('script-fake', 'HG24', Q10, 'It could also be the voice of your inherited inner parent that you are picking up,',
     'It could also be your inherited parent script that you are picking up,'),
    ('anxious-parts', 'HG24', Q9, 'Tell your Little parts and protector parts that you’re there',
     'Tell your Little parts and childhood protector parts that you’re there'),
    ('guide-stuck', 'HG24', Q10, 'What would the Leader choose to do now?', 'What would the Guide choose to do now?'),
    ('guide-proportion', 'HG25', Q10, 'the “Leader” to ignore the needs of the “Child”', 'the “Guide” to ignore the needs of the “Child”'),
    ('synchronicity', 'HG31', Q9S, 'a message from my Inner Child, my Protector or if I just need to grieve.',
     'a message from my Inner Child, a childhood protector part, or if I just need to grieve.'),
    ('guide-cue', 'HG31', Q10, '"What does my Leader think about this?"', '"What does my Guide think about this?"'),
    ('guide-reframe', 'HG31', Q10, 'How might my Leader reframe this?', 'How might my Guide reframe this?'),
    ('guide-nlp', 'HG31', Q10, '(Nurturer, Protector, and Leader)', '(Nurturer, Protector, and Guide)'),
    ('anxiety-part', 'HG33', Q9,
     'Remember that often the anxiety comes from a protector part of you, who is trying to help you, but who believes you are in danger,',
     'Remember that often the anxiety comes from a childhood protector part of you. It’s what protects you when your '
     'consciously installed parental Protector isn’t functioning, the same as when you were a child. It’s trying to help '
     'you, but it believes you are in danger,'),
    ('altered-part', 'HG36', Q9, 'it could be a protector part,', 'it could be a childhood protector part,'),
    ('chemicals', 'HG17', Q11, 'If you are intoxicated, acutely confused,', 'If you are overwhelmed by chemicals, acutely confused,'),
]


def rel(p):
    return str(pathlib.Path(p).resolve().relative_to(REPO))


def near_runs(md, i, span=8):
    """paragraphs_alone.minimal_runs, looking only within SPAN paragraphs of i: the full search is quadratic in the guide's
    700 paragraphs and ran for minutes on "The Guide:" (2 words, its neighbor 23), and a minimal run is near i anyway."""
    seq = PA.reader_blocks(md)
    pidx = [n for n, (k, _) in enumerate(seq) if k == 'p']
    memo = {}

    def w(a, b):
        if a > b:
            return 0
        if (a, b) not in memo:
            memo[(a, b)] = len(PA._run(seq, pidx, a, b).split())
        return memo[(a, b)]
    out = []
    for a in range(i, max(-1, i - span), -1):
        for b in range(i, min(len(pidx), i + span)):
            if w(a, b) >= 50 and (a == i or w(a + 1, b) < 50) and (b == i or w(a, b - 1) < 50):
                out.append((a, b, PA._run(seq, pidx, a, b), PA._run(seq, pidx, a, b, lead=True)))
    return out


PA.minimal_runs = near_runs


def readings():
    out = []
    for name, link, f in PARTS:
        r = json.loads(f.read_text(encoding='utf-8'))
        nt, idx = SC.norm_map(r['text'])
        out.append((name, link, r, nt, idx))
    return out


def reading_of(rs, text):
    """The recheck's reading of TEXT (plain): the part, the shade (red, light, dark) and its windows. A list item's number
    or bullet isn't in the checked text (the post renders it), so it goes."""
    text = S.LIST.sub('', text)
    q, _ = SC.norm_map(text)
    for name, link, r, nt, idx in rs:
        i = nt.find(q[:160])
        if i < 0:
            continue
        tail, _ = SC.norm_map(text[-120:])
        j = nt.find(tail, i)
        a = idx[i]
        b = idx[j + len(tail) - 1] + 1 if j >= 0 else a + len(text)
        shade, hit = SC.reading(r['windows'], a, b)
        ws = [k + 1 for k, w in enumerate(r['windows']) if w in hit]
        return {'part': name, 'link': link, 'shade': shade, 'windows': ws,
                'labels': ['%s %s' % (w['label'], w['confidence']) for w in hit]}
    return None


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    blocks = md.split('\n\n')
    cur = list(blocks)
    groups, edits = {}, []
    for key, sec, why, old, new in E:
        assert '\n\n' not in old and sum(b.count(old) for b in cur) == 1 and md.count(old) == 1, key
        i = next(k for k, b in enumerate(cur) if old in b)
        cur[i] = cur[i].replace(old, new)
        groups.setdefault(i, []).append(key)
        edits.append({'key': 'b470-' + key, 'section': sec, 'old': old, 'new': new, 'batch': '470g', 'diagnosis': why,
                      'block': i, 'paragraph_check': None,
                      'paragraph_result': 'pending: read in the next whole-guide recheck through Substack (gate E200)',
                      'section_check': None, 'section_result': None, 'reviews': 'fix-20261022/b470/'})
    cand = '\n\n'.join(cur)
    (B / 'CANDIDATE.md').write_text(cand, encoding='utf-8')
    byk = {e['key'][5:]: e for e in edits}
    rs = readings()
    pp = PA.paragraphs(cand)
    drafts, texts, items, rw, mparas, mp = {}, {}, [], {}, [], []
    for n, (i, keys) in enumerate(sorted(groups.items()), 1):
        was, now = blocks[i], cur[i]
        sec = byk[keys[0]]['section']
        h1 = next(cur[k] for k in range(i, -1, -1) if cur[k].startswith('# '))
        answers = list(dict.fromkeys(byk[k]['diagnosis'] for k in keys))
        pk = 'b470-' + keys[0]
        heading = was.startswith('#')
        prev = next(cur[k] for k in range(i - 1, -1, -1) if cur[k].strip())
        nxt = '\n\n'.join(c for c in cur[i + 1:i + (4 if heading else 2)] if c.strip())
        items.append('## Item %d (%s, section %s%s)\n\nTHE ANSWER%s IT CARRIES OUT:\n%s\n\nBEFORE:\n%s\n\nWAS:\n%s\n\nNOW:\n%s\n\n'
                     'AFTER:\n%s\n' % (n, ', '.join(keys), sec, ', a heading' if heading else '', 'S' if len(answers) > 1 else '',
                                       '\n'.join(answers), prev, was, now, nxt))
        rw.setdefault(h1, []).append(now)
        if heading:
            texts[pk] = {'section': sec, 'edits': keys, 'block': i, 'heading': True,
                         'note': 'a heading: Pangram\'s check of a Substack post doesn\'t read headings'}
            continue
        j = next(k for k, (_, q) in enumerate(pp) if q == now.strip())
        t, tries = PA.tries_for(cand, pp, j)
        text = t if len(t.split()) >= 50 else next(x for x in tries if len(x.split()) >= 50)
        drafts[pk] = text
        texts[pk] = {'section': sec, 'edits': keys, 'block': i, 'lineage': '%s-B%d' % (sec, i), 'words': len(text.split()),
                     'alone': text == t, 'reading_41': reading_of(rs, S.plain(was))}
        for ver, p in (('was', was), ('new', now)):
            q = S.plain(p)
            k = len(R.march_paragraphs(q))
            if k:
                mparas.append(q)
                mp.append({'key': pk, 'ver': ver, 'n': k, 'start': sum(m['n'] for m in mp)})
    (B / 'EDITS-470g.json').write_text(json.dumps(edits, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (B / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (B / 'meta.json').write_text(json.dumps({'edits': edits, 'texts': texts}, ensure_ascii=False, indent=1) + '\n',
                                 encoding='utf-8')

    head = (
        "You check %d changes to a long self-hypnosis guide by Joel. Each carries out answers he gave about how the guide "
        "names the figures inside a person: the inner child (\"little parts\"); the guards, which he now calls childhood "
        "protector parts (protective reactions learned in childhood); the inner adult the reader builds, with its three jobs "
        "(the Nurturer, the Adult Protector or just the Protector, and the Guide, formerly the Leader or Guru); and the "
        "inherited parent script (rules and ways of treating yourself learned growing up). For each item you get THE "
        "ANSWER(S) IT CARRIES OUT (his words), BEFORE and AFTER (what comes just before and after it in the guide), WAS (the "
        "paragraph or heading as it is now) and NOW (as changed).\n\nFor each item, say in a few words each:\n"
        "1. ANSWER: does NOW do what the answer asks, no more and no less? DONE, or what is missing or overdone.\n"
        "2. MEANING: apart from what the answer asks for, does NOW keep every point of WAS? KEPT, or what CHANGED or was LOST, "
        "and anything ADDED that a reader would act on or believe.\n"
        "3. NAMES: does NOW keep the figures apart? A protective reaction must not be called the Protector (the adult's job), "
        "the adult's jobs must not be called guards or parts, and the inherited parent script must not be mixed up with the "
        "inner adult. OK, or the words that mix them.\n"
        "4. SENSE: would a reader who has read the guide up to here understand every sentence of NOW in its place, between "
        "BEFORE and AFTER? OK, or the words that stop them and why.\n"
        "End each item with one line, `VERDICT: OK` or `VERDICT: CHANGED`. Judge meaning, names and sense only, not style, and "
        "suggest a rewrite only for a problem you report.\n\nWrite your report with a single Write call to `%s`, one \"## Item "
        "N\" part per item, then reply with only the verdicts, one line per item. Don't read any other file, don't run "
        "commands, and don't use the web.\n\n" % (len(items), B / 'REVIEW.md'))
    (B / 'REVIEW-PROMPT.txt').write_text(head + '\n'.join(items), encoding='utf-8')

    M = B / 'march'
    M.mkdir(exist_ok=True)
    draft = '\n\n'.join(mparas)
    (M / 'march-draft.txt').write_text(draft + '\n', encoding='utf-8')
    (M / 'march-map.json').write_text(json.dumps(mp, indent=1) + '\n', encoding='utf-8')
    prompt = R.build_march(draft, ABOUT)
    prompt += ('\n\nWrite exactly those lines, one per paragraph from T1 to T%d, with a single Write call to `%s`, then reply '
               'with only "done". Don\'t read any other file, don\'t run commands, and don\'t use the web.\n'
               % (len(mparas), M / 'march-labels.txt'))
    (M / 'march-prompt.txt').write_text(prompt, encoding='utf-8')

    (B / 'REWRITE.md').write_text('\n\n'.join(h + '\n\n' + '\n\n'.join(ps) for h, ps in rw.items()) + '\n', encoding='utf-8')
    pos = (H / 'fix-20261021' / 'b469' / 'POSITIONS.txt').read_text(encoding='utf-8').rstrip()
    (B / 'POSITIONS.txt').write_text(pos + '\n\n' + '\n\n'.join([Q9, Q10, Q11]) + '\n', encoding='utf-8')

    (B / 'sense').mkdir(exist_ok=True)
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'reviewer' / 'reviewer.py'), '--article',
                        rel(B / 'CANDIDATE.md'), 'sense-section', rel(B / 'sense' / 'prompt.txt'), '--section',
                        H1_14[2:], '--report', str(B / 'SENSE-HG14.md')], capture_output=True, text=True, cwd=REPO)
    assert r.returncode == 0, r.stderr[-2000:]
    (B / 'stance').mkdir(exist_ok=True)
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'stance_check_prompt.py'),
                        '--essay', rel(H / 'source' / 'published-20260928.md'), '--rewrite', rel(B / 'REWRITE.md'),
                        '--out', rel(B / 'stance' / 'prompt.txt'),
                        '--scope', 'the paragraphs and headings where the guide names the guards (now childhood protector '
                                   'parts), the inner adult\'s three jobs (now Nurturer, Protector and Guide) and the inherited '
                                   'parent script, and one line of its safety advice before an induction',
                        '--topic', 'self-hypnosis and listening to the subconscious',
                        '--positions', rel(B / 'POSITIONS.txt'), '--report', str(B / 'STANCE.md')],
                       capture_output=True, text=True, cwd=REPO)
    assert r.returncode == 0, r.stderr[-2000:]
    for f in ('REVIEW-PROMPT.txt', 'march/march-prompt.txt', 'sense/prompt.txt', 'stance/prompt.txt'):
        print(f, len((B / f).read_text(encoding='utf-8').split()), 'words')
    print(len(edits), 'edits in', len(groups), 'paragraphs or headings;', len(drafts), 'texts;', len(mparas), 'march paragraphs')
    for k, v in texts.items():
        print(k, v.get('reading_41') and '%s %s w%s' % (v['reading_41']['part'], v['reading_41']['shade'], v['reading_41']['windows']))


if __name__ == '__main__':
    main()
