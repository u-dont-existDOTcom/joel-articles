"""Batch n4 (Nibbāna) and b477 (the hypnosis guide): Emulate's samples for the red of Nibbāna's fourth recheck and the
guide's recheck B, spliced sentence by sentence (2026-10-23, Joel's message of 18:13 UTC gave the two rechecks' links).

The red (../recheck4/SCORE.md; the guide's ../../../inner-signal/humanize/fix-20261023/recheck/RESULT-B.json):
- Nibbāna window 9 (AI, High): the unification paragraph's first sentence, my batch n1 rewrite, alone in its window once
  his rewrite of the paragraph before (his 14) moved the window's edge (gate E249); window 10 (AI, Low): the paragraph's
  second sentence and Soh's first, with my gloss on "sensory unification";
- window 33 (AI, Low): "It sounds abstract, but the next sections explain what I think the experience was showing.";
- windows 85 and 86 (AI, Low): the suttas' preservation sentences and "That creates a practical problem.";
- the guide's window 17 (AI, Low): "You don’t have to fix this. I’m here now."

Emulate ran on each whole paragraph the red covers (E235, E244), three samples a round: round 1 br, bs, bt (BUNDLE.json),
round 2 bu, bv, bw (BUNDLE2.json), the unification paragraph alone in round 2 with its definition tied to the senses
(NB-unif2). Only the red sentences go back, each from the sample that keeps its meaning best; every change I made to
Emulate's words is in "mine" with its reason (docs/EMULATE-FALLBACK.md, section 4: spelling to the article's own, a
typo, a pronoun). Soh's sentence goes back to his published words, which read Human, Medium, alone in recheck 3: my gloss
read red, and the snag he asked about ("i wasn't clear exactly how you'll fix the sensory unification vs unification
part with soh?") is fixed in the definition instead, which now says unification is what makes "all of the senses work
together", his own sense of it ("the binding that normally holds all my senses together", the percentages paragraph).

"That creates a practical problem." is his and stays: the one sample with a replacement ("There's also a practical
problem.", bv) turns his cause into a second problem, and the recheck reads his sentence in its new neighbours first.

  python3 articles/nibbana/humanize/fix-20261023/n4/emulate_n4.py --prompt   writes REVIEW-PROMPT.txt for a fresh reader
  (install_n1.py calls apply() after batch n3; the guide's edit goes in through apply_edits41.py --add ../../../
  inner-signal/humanize/fix-20261023/b477/EDITS-b477.json, written by --guide)
"""
import argparse, html, json, pathlib, re

N4 = pathlib.Path(__file__).resolve().parent
ROOT = N4.parents[4]
UP = pathlib.Path('/mnt/user-data/uploads/inbox')
GUIDE_B477 = ROOT / 'articles/inner-signal/humanize/fix-20261023/b477'


def sample(run, key):
    return (N4 / run / (key + '.out.txt')).read_text(encoding='utf-8').strip()


# key: (the paragraph's first words, the red text as it is in the working copy, the new text, the sample and its
# sentences used, my changes to Emulate's words with reasons, the windows, the published text the meaning comes from)
UNIF_RED = ('When I say “unification”, I mean whatever pulls everything together so that a person can talk, cross a road, '
            'recognize a friend and answer a text, and it works even when there’s no separate knower in there. Most of my '
            'daily life includes that ordinary unification and feels almost like everybody else’s day (well, if they’re '
            'happy).')
SPLICES = {
    'n4-unification': dict(
        first='When I say “unification”', old=UNIF_RED, run='bu', key='NB-unif2', take=None,
        mine=[('But I am using the term', 'I am using the term',
               'the paragraph before opens on "But" already (his 14: "But when you read AtR’s own accounts"), and nothing '
               'here is set against it'),
              ('which works even without a knower', 'which works even without a separate knower',
               'the reader (REVIEW.md, item 1): "without a knower" is Soh\'s claim, a stronger one; his is "no separate '
               'knower"'),
              ('Most of my day includes that unification', 'Most of my day includes that ordinary unification',
               'the reader (item 1): "ordinary" is what sets this everyday unification apart from the meditative one '
               '(MN 137\'s) the article also calls unification')],
        windows='9 (High) and 10 (Low) in recheck 4 (feed 933f5abe)',
        published='I use “unification” for the functional coordination through which a person speaks, crosses a road, '
                  'recognizes a friend, and answers a message, even with no separate knower. Most of my daily life '
                  'includes that ordinary unification and feels almost like everybody else’s day (well, if they’re happy).'),
    'n4-soh': dict(
        first='I owe Soh a great deal',
        old='he says sensory unification (that pulling-together of the senses) isn’t required for functioning',
        new='he says sensory unification isn’t required for functioning', run=None, key=None, take=None, mine=[],
        windows='10 (Low) in recheck 4; the same sentence without my gloss read Human, Medium, alone in recheck 3',
        published='I owe Soh a great deal, but one key difference remains: he says sensory unification isn’t required '
                  'for functioning, which makes no sense to me.'),
    'n4-abstract': dict(
        first='This article itself is version 2.0',
        old='It sounds abstract, but the next sections explain what I think the experience was showing.',
        run='bv', key='NB-abstract', take=('As you can see this is going to be a little abstract', None),
        mine=[('to explain a bit more on what I think', 'to explain what I think',
               'the reader (item 3): "a bit more" made the sections a partial explanation; his say they explain it')],
        windows='33 (Low) in recheck 4',
        published='It sounds abstract, but the next sections explain what I think the experience was showing.'),
    'n4-preserve-1': dict(
        first='The funny part is that the words',
        old='They were transmitted communally for centuries, and separately preserved early collections agree on a great '
            'deal despite variants, rearrangements, and later additions.',
        run='br', key='NB-preserve', take=('The words were transmitted communally', 'later additions.'),
        mine=[('The words were transmitted', 'They were transmitted',
               'the sentence before ends on "the words may have survived surprisingly well"; his pronoun, as he had it'),
              ('re-arrangements', 'rearrangements', 'O15: the article\'s own spelling (E246)')],
        windows='85 (Low) in recheck 4',
        published='They were transmitted communally for centuries, and separately preserved early collections agree on a '
                  'great deal despite variants, rearrangements, and later additions.'),
    'n4-preserve-2': dict(
        first='The funny part is that the words',
        old='But preserving the puzzle pieces doesn’t preserve the picture on the box.',
        run='bt', key='NB-preserve', take=('But just because the pieces of the puzzle', 'the picture on the box has.'),
        mine=[('come down to use well', 'come down to us well', 'a typo: "use" for "us"')],
        windows='86 (Low) in recheck 4, with "That creates a practical problem.", which stays',
        published='But preserving the puzzle pieces doesn’t preserve the picture on the box.'),
}
GUIDE = dict(
    old='You don’t have to fix this. I’m here now. The adult is listening.”',
    run='br', key='HG-B-love', take=('You don’t have to fix it.', 'to listen to you.”'), mine=[],
    windows='17 (Low) in recheck B (feed 1db9825e): "You don’t have to fix this. I’m here now."; "The adult is listening." '
            'read Human, Medium, after it, and Emulate joined it to "I’m here now", so the three go together',
    published='“Little one, you are not alone. You don’t have to fix this. I’m here now. The adult is listening.”')


def new_text(s):
    if s.get('new') is not None:
        return s['new']
    out = sample(s['run'], s['key'])
    if s['take']:
        a, b = s['take']
        i = out.index(a)
        j = out.index(b, i) + len(b) if b else len(out)
        out = out[i:j]
    for x, y, _why in s['mine']:
        assert out.count(x) == 1, (x, out)
        out = out.replace(x, y)
    return out


def para_bounds(work, first):
    hits = [(m.start(1), m.end(1)) for m in re.finditer(r'<p\b[^>]*>(.*?)</p>', work, re.S)
            if html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).lstrip().startswith(first)]
    assert len(hits) == 1, ('one paragraph must start with', first, len(hits))
    return hits[0]


def apply(work):
    recs = []
    for key, s in SPLICES.items():
        a, b = para_bounds(work, s['first'])
        inner = work[a:b]
        old_h, new = html.escape(s['old'], quote=False), new_text(s)
        assert inner.count(old_h) == 1, (key, s['old'][:60])
        work = work[:a] + inner.replace(old_h, html.escape(new, quote=False)) + work[b:]
        recs.append({'key': key, 'old': s['old'], 'new': new, 'windows': s['windows'],
                     'source': ('Emulate sample %s (%s)' % (s['run'], s['key'])) if s['run'] else 'his published words',
                     'mine': [{'replace': x, 'with': y, 'why': w} for x, y, w in s['mine']],
                     'published': s['published'], 'check': None, 'try': None,
                     'result': 'read in place in the next recheck (recheck 5)',
                     'review': 'fix-20261023/n4/REVIEW.md', 'triage': 'fix-20261023/n4/TRIAGE.json'})
    (N4 / 'EDITS-n4.json').write_text(json.dumps(recs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return work, recs


def guide_edit():
    new = new_text(GUIDE)
    return [{'key': 'b477-HG-B-love', 'section': None, 'batch': '477',
             'source': 'Emulate sample %s (%s), the red of recheck B; windows %s' % (GUIDE['run'], GUIDE['key'], GUIDE['windows']),
             'old': GUIDE['old'], 'new': new, 'published': GUIDE['published'],
             'check': 'read in place in the next recheck B', 'review': 'fix-20261023/b477/REVIEW.md'}]


def context(work_text, s_old):
    """The paragraph holding S_OLD and its neighbours, from a plain text with one paragraph a line."""
    lines = [l for l in work_text.split('\n') if l.strip()]
    k = next(i for i, l in enumerate(lines) if s_old in l)
    return (lines[k - 1] if k else ''), lines[k], (lines[k + 1] if k + 1 < len(lines) else '')


PROMPT = '''You check {n} rewritten passages: {nn} in Joel's long article on nibbāna (Buddhist enlightenment), written for a general Substack audience, in his casual first-person voice with jokes and emoji, and one in his self-hypnosis guide (a script the reader says to their own inner child; "I" in the script is the reader). Each NOW sentence is a detector-passing rewrite of only the sentence(s) marked WAS in its paragraph; PUBLISHED is what he published, the meaning to keep (where a WAS differs from PUBLISHED, an earlier pass of mine changed it, and PUBLISHED is still the meaning).

For each item, say in a few words each:
1. MEANING: does NOW keep every point, claim, condition and image of PUBLISHED, with the same strength (nothing made more or less certain, nothing turned into a different claim, no cause turned into a coincidence)? KEPT, or what CHANGED or was LOST, and anything ADDED that a reader would take as a claim.
2. SENSE: would a reader understand the paragraph with NOW in it, between BEFORE and AFTER? OK, or the words that stop them and why.
End each item with one line, `VERDICT: OK` or `VERDICT: CHANGED`. Judge meaning and sense only, not style or grammar (the casual grammar, the run-on sentences and the "etc." are on purpose), and suggest the smallest possible rewrite only for a problem you report.

Write your report with a single Write call to `{report}`, one "## Item N" part per item, then reply with only the verdicts, one line per item. Don't read any other file, don't run commands, and don't use the web.

{items}'''


def prompt(work_text, guide_text):
    items, n = [], 0
    notes = {'n4-unification': ('the definition of "unification", the term the next paragraph calls "sensory unification" '
                                'in Soh\'s claim; NOW also has to make that link clear without a gloss'),
             'n4-soh': 'his published words back, without my gloss',
             'n4-abstract': 'the last sentence of the paragraph, leading into the article\'s explanation sections',
             'n4-preserve-1': 'the suttas: how well the Buddha\'s words were preserved',
             'n4-preserve-2': 'the same paragraph: his puzzle image (the words are the pieces; what they add up to is the picture)'}
    done = work_text
    for s in SPLICES.values():
        done = done.replace(s['old'], new_text(s))
    for key, s in SPLICES.items():
        n += 1
        before, para, after = context(work_text, s['old'])
        before, after = context(done, new_text(s))[0], context(done, new_text(s))[2]
        now = para.replace(s['old'], new_text(s))
        items.append('## Item %d (%s)\n\nBEFORE:\n%s\n\nPARAGRAPH WITH WAS:\n%s\n\nWAS:\n%s\n\nPUBLISHED:\n%s\n\nNOW:\n%s\n\n'
                     'PARAGRAPH WITH NOW:\n%s\n\nAFTER:\n%s\n' % (n, notes[key], before, para, s['old'], s['published'],
                                                                 new_text(s), now, after))
    n += 1
    before, para, after = context(guide_text, GUIDE['old'])
    items.append('## Item %d (the guide: a few words the reader says to their own scared inner child, hands on heart and '
                 'solar plexus)\n\nBEFORE:\n%s\n\nPARAGRAPH WITH WAS:\n%s\n\nWAS:\n%s\n\nPUBLISHED:\n%s\n\nNOW:\n%s\n\n'
                 'PARAGRAPH WITH NOW:\n%s\n\nAFTER:\n%s\n' % (n, before, para, GUIDE['old'], GUIDE['published'],
                                                             new_text(GUIDE), para.replace(GUIDE['old'], new_text(GUIDE)),
                                                             after))
    return PROMPT.format(n=n, nn=len(SPLICES), report=(N4 / 'REVIEW.md').resolve(), items='\n'.join(items))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--prompt', action='store_true')
    ap.add_argument('--guide', action='store_true')
    a = ap.parse_args(argv)
    if a.prompt:
        wt = (ROOT / 'articles/nibbana/humanize/fix-20261023/recheck4/DRAFT-TEXT.txt').read_text(encoding='utf-8')
        gt = (ROOT / 'articles/inner-signal/humanize/HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
        (N4 / 'REVIEW-PROMPT.txt').write_text(prompt(wt, gt), encoding='utf-8')
        print('REVIEW-PROMPT.txt written')
    if a.guide:
        GUIDE_B477.mkdir(parents=True, exist_ok=True)
        (GUIDE_B477 / 'EDITS-b477.json').write_text(json.dumps(guide_edit(), ensure_ascii=False, indent=1) + '\n',
                                                     encoding='utf-8')
        print('EDITS-b477.json written')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
