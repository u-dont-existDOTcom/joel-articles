"""Section 2, writers round 1 (2026-10-01): the system's own first drafts for the paragraphs that failed Pangram
after the trace fixes (v2.1) and after a fresh Emulate round.

Prompts come from tools/humanization/reviewer/reviewer.py build_draft (writer_draft.txt plus Joel's fixes
catalogue), with two recorded adaptations: its first sentence describes the Inner Child article, so it's replaced by
one describing this essay; and a unit of two paragraphs gets a two-paragraph instruction. The brief gives Joel's
published paragraph as the meaning to carry, with his distinctive lines to keep word for word.
"""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
UNI = pathlib.Path('/home/claude/universal')
sys.path.insert(0, str(UNI / 'tools/humanization/reviewer')); import reviewer as R
IC = HERE.parent.parent
src = [p.strip() for p in (IC / 'sections/003-original.md').read_text(encoding='utf-8').split('\n\n') if p.strip()]
def para(start):
    return [p for p in src if p.startswith(start)][0]
plain = lambda t: re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', t)
O = {k: plain(para(s)) for k, s in dict(C1='The longing', C2='I’m less interested', C3='Look at Google', C4='I can’t prove',
                                         seba='It’s poppin', C6='Another large', C7='Not everybody', C8='The commune comments',
                                         C9='Although that comment', C10='Communal ownership', C11='The desire', C12='I’m not currently').items()}
V = {k: (HERE / (k + '.txt')).read_text(encoding='utf-8').strip() for k in ('C2', 'C12')}  # v2.1, Pangram Human alone
so_far = re.sub(r'<!--.*?-->', '', (HERE.parent / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'), flags=re.S)
s1 = so_far[:so_far.index('# Communes Are Hot Again')].strip().split('\n\n')
s1_end = plain([p for p in s1 if p.startswith('The secular communities often')][0])

OPEN_OLD = ("You're writing one short paragraph for a friendly self-help article about inner-child therapy, by an author named Joel. "
            "It goes between two paragraphs of his (below), so it has to read as his and follow on from the one before.")
def open_new(n):
    what = 'one short paragraph' if n == 1 else 'two short paragraphs'
    return ("You're writing %s for an essay about intentional communities and communes, by an author named Joel, published on "
            "Substack. It replaces %s of his that an AI detector flagged. It goes between paragraphs of his (below), so it has to read "
            "as his and follow on from the one before." % (what, 'a paragraph' if n == 1 else 'two paragraphs'))
CARRY = ("Carry everything in it: every claim at the same strength, every condition and hedge, the same people doing the same "
         "things, and nothing new about Joel's life or anyone else's. Write it in your own sentences, not his, except the words "
         "marked to keep. Don't add examples, reasons or feelings that aren't in his paragraph.")
UNITS = {
 'U1': dict(n=1, orig=[O['C1']], before=s1_end + '\n\n# Communes Are Hot Again 🔥', after=V['C2'], length='one or two sentences, 35 to 55 words',
            keep=['“U.S. Surgeon General’s advisory” (a link sits on these words; keep them together)', '“roughly half of American adults” (not “50% of Americans”)'],
            note="“My father’s film” is the documentary from section 1, about the communes he visited."),
 'U2': dict(n=2, orig=[O['C3'], O['C4']], before=V['C2'], between='[image: the Google Trends chart for both terms]', after=O['seba'],
            length='the first paragraph one or two sentences, 20 to 40 words; the second three or four sentences, 45 to 75 words',
            keep=['“ecovillage” and “intentional community”, each in quotation marks (each carries a link)',
                  'the second paragraph’s last sentence, word for word: Suddenly “maybe we should form a village” sounded less like a 1972 leftover and more like a backup plan.'],
            note='All four of what AI began reorganizing stay: jobs, feeds, relationships, and expectations of the future.'),
 'U3': dict(n=2, orig=[O['C6'], O['C7']], before=O['seba'], between='### The Freeloader Problem', after='[image: a screenshot of one of the comments]\n\n' + O['C8'],
            length='the first paragraph two or three sentences, 35 to 60 words; the second two sentences, 30 to 50 words',
            keep=['“floated the commune idea” (a link sits on these words)', 'the sofa comparison (“used sofa” or “second-hand sofa”)',
                  '“owned by everyone, cared for by nobody”, in quotation marks, as the commenters’ words inside their objection'],
            note='“It was chaotic, sincere, and revealing” is Joel’s verdict on the comments: keep all three, though not necessarily as a list. The objection stays hedged with “maybe”.'),
 'U4': dict(n=1, orig=[O['C9']], before='[image: a screenshot of one of the comments]\n\n' + O['C8'], after=O['C10'], length='three or four sentences, 50 to 80 words',
            keep=['“the same three people maintain everything while everybody else discusses freedom”'],
            note='“That comment” is the one in the screenshot above; “the objection” is the general one it makes.'),
 'U5': dict(n=1, orig=[O['C10']], before=O['C9'], after=O['C11'], length='two or three sentences, 45 to 80 words',
            keep=['“before resentment becomes the real government”', 'all four needs and all four things that removing bosses doesn’t remove'],
            note='“Therefore”: it follows from the paragraph before.'),
 'U6': dict(n=1, orig=[O['C11']], before=O['C10'], after=V['C12'], length='three sentences, 50 to 80 words',
            keep=['“lonely and exhausted”', '“beautiful land”'],
            note='All three things people usually don’t know stay, and all four things that come in: money, children, jealousy, and ownership.'),
}
OUT = HERE / 'writers-r1'; OUT.mkdir(exist_ok=True)
for u, d in UNITS.items():
    brief = ("Joel's published %s, which the detector flagged:\n%s\n\n%s\n\nKeep word for word:\n%s\n\nAlso: %s" % (
        'paragraph' if d['n'] == 1 else 'two paragraphs', '\n\n'.join('«%s»' % p for p in d['orig']), CARRY,
        '\n'.join('- ' + k for k in d['keep']), d['note']))
    t = dict(brief=brief, before=d['before'], after=d['after'], length=d['length'],
             voice="in Joel's voice, like the paragraphs around it (first person where he speaks for himself)")
    tp = OUT / ('%s-target.json' % u); tp.write_text(json.dumps(t, indent=1, ensure_ascii=False), encoding='utf-8')
    w = R.build_draft(tp)
    assert w.startswith(OPEN_OLD), u
    w = open_new(d['n']) + w[len(OPEN_OLD):]
    if d['n'] == 2:
        w = w.replace('The paragraph before it (final; don\'t change it):', 'The paragraph before them (final; don\'t change it):')
        w = w.replace('The paragraph after it (final; don\'t change it):',
                      'Between your two paragraphs comes this line (fixed; don\'t write it):\n%s\n\nThe paragraph after them (final; don\'t change it):' % d['between'])
        a = w.index('Write the paragraph:'); b = w.index('\n', a)
        w = w[:a] + ('Write the two paragraphs: %s, %s. No heading. Output only the two paragraphs, separated by a blank line.' % (
            d['length'], t['voice'])) + w[b:]
    dd = OUT / u; dd.mkdir(exist_ok=True)
    (dd / 'prompt.txt').write_text(w, encoding='utf-8')
    print(u, len(w.split()), 'words')
