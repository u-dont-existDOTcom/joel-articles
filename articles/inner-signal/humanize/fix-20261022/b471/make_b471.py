"""Batch 471g (2026-10-22): Joel's answers to question 12, 21:41 UTC ("12a A. b.A c Yeah it can be useful in guided hypnosis
to split them into three roles. I'd just clarify that in real life they are all part of the one inner adult, so we could
also imagine them splitting apart if need be and coming together as well.").

- 12 a, A: "When the adult role is not available yet" names forced adulthood, his name for it in the Inner Child article.
- 12 b, A: no umbrella word; nothing changes.
- 12 c: the three roles stay in Appendix B's NLP sequence, with his clarification right after the step, in his words
  ("we", "if need be", "coming together as well"). The invocation's "inner adult(s)" and Appendix K's "three-adult
  arrangement" stay as they are: three roles are fine, and the step says what they are in real life.

The same machinery as batch 470g (make_b470.py): the candidate, the edit list for fix-20261020/apply_edits41.py --add, each
changed paragraph as Pangram reads it with its reading in the recheck of 2026-10-21, the item review (Opus, -> REVIEW.md),
the march (Sonnet, -> march/march-labels.txt) and the stance check (Opus, -> STANCE.md).

  python3 articles/inner-signal/humanize/fix-20261022/b471/make_b471.py [--edits-only]   (from the repo root)
"""
import json, pathlib, subprocess, sys

B = pathlib.Path(__file__).resolve().parent
H = B.parents[1]
REPO = H.parents[2]
sys.path.insert(0, str(H / 'fix-20261022' / 'b470'))
import make_b470 as M   # noqa: E402  (its readings, reading_of, the quick minimal runs, and the helpers it imports)

S, PA, R = M.S, M.PA, M.R
Q12 = ('Joel, 2026-10-22 21:41 UTC, question 12: "12a A. b.A c Yeah it can be useful in guided hypnosis to split them into '
       'three roles. I\'d just clarify that in real life they are all part of the one inner adult, so we could also imagine '
       'them splitting apart if need be and coming together as well."')
Q12A = (Q12 + ' (12 a, option A: name it there, "... or feel like a child part who may be playing at being an adult (what I '
        'call forced adulthood)". In the Inner Child article, his words of 15:33 UTC: asking the child to heal itself is "really '
        'a disguised request for the child to abandon its own nature and turn into an adult. I call that "forced adulthood," '
        'where the child has to deal with situations the evolved inner adult should be handling".)')
Q12C = (Q12 + ' (12 c asked about Appendix B\'s "Put 3 good adults in with the person (Nurturer, Protector, and Guide)", '
        'against his convention "Three functions of that same Inner Adult—not three additional people".)')
E = [
    ('forced-adulthood', 'HG14', Q12A, 'or feel like a child part who may be playing at being an adult.',
     'or feel like a child part who may be playing at being an adult (what I call forced adulthood).'),
    ('three-roles', 'HG31', Q12C, 'Put 3 good adults in with the person (Nurturer, Protector, and Guide).',
     'Put 3 good adults in with the person (Nurturer, Protector, and Guide). In real life they’re all part of the one '
     'inner adult, so we can imagine them splitting apart if need be and coming together as well.'),
]


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    blocks = md.split('\n\n')
    cur = list(blocks)
    edits, items, rw, texts, drafts, mparas, mp = [], [], {}, {}, {}, [], []
    for key, sec, why, old, new in E:
        assert md.count(old) == 1, key
        i = next(k for k, b in enumerate(cur) if old in b)
        cur[i] = cur[i].replace(old, new)
        edits.append({'key': 'b471-' + key, 'section': sec, 'old': old, 'new': new, 'batch': '471g', 'diagnosis': why,
                      'block': i, 'paragraph_check': None,
                      'paragraph_result': 'pending: read in the next whole-guide recheck through Substack (gate E200)',
                      'section_check': None, 'section_result': None, 'reviews': 'fix-20261022/b471/'})
    cand = '\n\n'.join(cur)
    (B / 'CANDIDATE.md').write_text(cand, encoding='utf-8')
    rs = M.readings()
    pp = PA.paragraphs(cand)
    for n, e in enumerate(edits, 1):
        i = e['block']
        was, now = blocks[i], cur[i]
        h1 = next(cur[k] for k in range(i, -1, -1) if cur[k].startswith('# '))
        prev = next(cur[k] for k in range(i - 1, -1, -1) if cur[k].strip())
        nxt = '\n\n'.join(c for c in cur[i + 1:i + 2] if c.strip())
        items.append('## Item %d (%s, section %s)\n\nTHE ANSWER IT CARRIES OUT:\n%s\n\nBEFORE:\n%s\n\nWAS:\n%s\n\nNOW:\n%s\n\nAFTER:\n%s\n'
                     % (n, e['key'][5:], e['section'], e['diagnosis'], prev, was, now, nxt))
        rw.setdefault(h1, []).append(now)
        j = next(k for k, (_, q) in enumerate(pp) if q == now.strip())
        t, tries = PA.tries_for(cand, pp, j)
        text = t if len(t.split()) >= 50 else next(x for x in tries if len(x.split()) >= 50)
        drafts[e['key']] = text
        texts[e['key']] = {'section': e['section'], 'edits': [e['key'][5:]], 'block': i, 'lineage': '%s-B%d' % (e['section'], i),
                           'words': len(text.split()), 'alone': text == t, 'reading_41': M.reading_of(rs, S.plain(was))}
        for ver, p in (('was', was), ('new', now)):
            q = S.plain(p)
            k = len(R.march_paragraphs(q))
            if k:
                mparas.append(q)
                mp.append({'key': e['key'], 'ver': ver, 'n': k, 'start': sum(m['n'] for m in mp)})
    (B / 'EDITS-471g.json').write_text(json.dumps(edits, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (B / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (B / 'meta.json').write_text(json.dumps({'edits': edits, 'texts': texts}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    head = (
        "You check %d changes to a long self-hypnosis guide by Joel. Each carries out an answer he gave about how the guide "
        "names the figures inside a person: the inner child; the guards (childhood protector parts); the inner adult the "
        "reader builds, with its three jobs (the Nurturer, the Protector and the Guide); and the inherited parent script. For "
        "each item you get THE ANSWER IT CARRIES OUT (his words), BEFORE and AFTER (what comes just before and after it in "
        "the guide), WAS (the paragraph as it is now) and NOW (as changed).\n\nFor each item, say in a few words each:\n"
        "1. ANSWER: does NOW do what the answer asks, no more and no less? DONE, or what is missing or overdone.\n"
        "2. MEANING: apart from what the answer asks for, does NOW keep every point of WAS? KEPT, or what CHANGED or was LOST, "
        "and anything ADDED that a reader would act on or believe.\n"
        "3. NAMES: does NOW keep the figures apart (a protective reaction is not the Protector; the adult's jobs are not "
        "guards or parts; the inherited parent script is not the inner adult)? OK, or the words that mix them.\n"
        "4. SENSE: would a reader who has read the guide up to here understand every sentence of NOW in its place, between "
        "BEFORE and AFTER? OK, or the words that stop them and why.\n"
        "End each item with one line, `VERDICT: OK` or `VERDICT: CHANGED`. Judge meaning, names and sense only, not style, and "
        "suggest a rewrite only for a problem you report.\n\nWrite your report with a single Write call to `%s`, one \"## Item "
        "N\" part per item, then reply with only the verdicts, one line per item. Don't read any other file, don't run "
        "commands, and don't use the web.\n\n" % (len(items), B / 'REVIEW.md'))
    (B / 'REVIEW-PROMPT.txt').write_text(head + '\n'.join(items), encoding='utf-8')
    Mf = B / 'march'
    Mf.mkdir(exist_ok=True)
    draft = '\n\n'.join(mparas)
    (Mf / 'march-draft.txt').write_text(draft + '\n', encoding='utf-8')
    (Mf / 'march-map.json').write_text(json.dumps(mp, indent=1) + '\n', encoding='utf-8')
    prompt = R.build_march(draft, M.ABOUT)
    prompt += ('\n\nWrite exactly those lines, one per paragraph from T1 to T%d, with a single Write call to `%s`, then reply '
               'with only "done". Don\'t read any other file, don\'t run commands, and don\'t use the web.\n'
               % (len(mparas), Mf / 'march-labels.txt'))
    (Mf / 'march-prompt.txt').write_text(prompt, encoding='utf-8')
    (B / 'REWRITE.md').write_text('\n\n'.join(h + '\n\n' + '\n\n'.join(ps) for h, ps in rw.items()) + '\n', encoding='utf-8')
    pos = (H / 'fix-20261022' / 'b470' / 'POSITIONS.txt').read_text(encoding='utf-8').rstrip()
    (B / 'POSITIONS.txt').write_text(pos + '\n\n' + Q12 + '\n', encoding='utf-8')
    if '--edits-only' in sys.argv:
        return
    (B / 'stance').mkdir(exist_ok=True)
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'stance_check_prompt.py'),
                        '--essay', M.rel(H / 'source' / 'published-20260928.md'), '--rewrite', M.rel(B / 'REWRITE.md'),
                        '--out', M.rel(B / 'stance' / 'prompt.txt'),
                        '--scope', 'two paragraphs: the one that names forced adulthood where the adult role is not available '
                                   'yet, and the NLP sequence\'s step that brings in the inner adult\'s three roles',
                        '--topic', 'self-hypnosis and listening to the subconscious',
                        '--positions', M.rel(B / 'POSITIONS.txt'), '--report', str(B / 'STANCE.md')],
                       capture_output=True, text=True, cwd=REPO)
    assert r.returncode == 0, r.stderr[-2000:]
    for f in ('REVIEW-PROMPT.txt', 'march/march-prompt.txt', 'stance/prompt.txt'):
        print(f, len((B / f).read_text(encoding='utf-8').split()), 'words')
    for k, v in texts.items():
        print(k, v['words'], 'words;', v.get('reading_41') and '%s %s w%s' % (v['reading_41']['part'], v['reading_41']['shade'], v['reading_41']['windows']))


if __name__ == '__main__':
    main()
