"""Section 2, writers round 2 (2026-10-01).

Round 1 gave the writers Joel's published paragraph and said to carry everything and add nothing; 19 of 20 drafts
came back 100% AI, most of them his paragraph reworded in his order. Round 2 follows HUMANIZATION-GATE step 3
instead ("The human part is what gets noticed while each piece is being said: the reader's obvious counterexample;
why the thing is true, or hard; an irony inside the article's own frame; a callback"), at the gate's default push
(about one short sentence per paragraph):
- the brief is the meaning as bare points, with the words a link sits on and Joel's distinctive lines to keep;
- the writer sees the article so far, so a callback is possible;
- one small noticing is allowed, never a new fact about Joel's life or anyone else's, a new example, or a feeling;
- what round 1 showed is added to the detector notes.
Same recorded adaptations of reviewer.py build_draft as round 1.
"""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
UNI = pathlib.Path('/home/claude/universal')
sys.path.insert(0, str(UNI / 'tools/humanization/reviewer')); import reviewer as R
spec_globals = {'__file__': str(HERE / 'build_writers.py')}
exec(compile(open(HERE / 'build_writers.py', encoding='utf-8').read().split("OUT = HERE / 'writers-r1'")[0], 'bw', 'exec'), spec_globals)
G = spec_globals
O, V, s1_end, OPEN_OLD, open_new = G['O'], G['V'], G['s1_end'], G['OPEN_OLD'], G['open_new']
so_far = re.sub(r'<!--.*?-->', '', (HERE.parent / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'), flags=re.S)
sec1 = G['plain'](so_far[:so_far.index('# Communes Are Hot Again')].strip())
sec1 = sec1.replace('[Subscribe now](%%checkout_url%%)', '').strip()
C2 = V['C2']
U3 = (HERE / 'r1/U3w3.txt').read_text(encoding='utf-8').strip().split('\n\n')  # passed in round 1 (pair)

NOTICE = ("You may add one small thing Joel would notice while saying this, at most one short sentence or clause: the reader's "
          "obvious objection, why the point is true or hard, an irony inside the article's own frame, or a callback to something "
          "earlier in the article. Not a new fact about Joel's life or anyone else's, not a new example, no numbers, no feelings "
          "he didn't state, and nothing that the article's next section is about (why communities die, inner and relational work).")
ROUND1 = ("- On this section, drafts that kept the published paragraph's sentences in its order, reworded, failed: 19 of 20. "
          "The one that passed put its sentences in an order where each reacted to the one before; it stated the commenters' "
          "objection first and only then said it was the oldest one, and that it showed up almost immediately.\n")
UNITS = {
 'U1': dict(n=1, before=s1_end + '\n\n# Communes Are Hot Again 🔥', after=C2, length='one or two sentences, 35 to 60 words', points=[
     "The longing that shaped Joel's father's film (the documentary from the start of the article) is suddenly everywhere again.",
     "The U.S. Surgeon General's 2023 advisory reported that roughly half of American adults experience loneliness (not \"50% of Americans\").",
     "It treated social connection as a public-health issue rather than a sentimental extra."],
     keep=["“U.S. Surgeon General’s advisory”, together (a link sits on these words)"]),
 'U2': dict(n=2, before=C2, between='[image: the Google Trends chart for both terms]', after=O['seba'],
     length='the first paragraph one or two sentences, 20 to 45 words; the second three to five sentences, 50 to 90 words', points=[
     "First paragraph: on Google Trends, interest in “ecovillage” and “intentional community” (each word carries a link, so keep both in quotation marks) drifted downward for years, then turned sharply upward in the mid-2020s.",
     "Second paragraph: Joel can't prove AI caused that turn, but the timing is hard to ignore.",
     "Around the same period, AI stopped being a tech-news curiosity and began reorganizing people's jobs, feeds, relationships, and expectations of the future (all four).",
     "Joel's line, word for word, anywhere in the paragraph (it needn't be the last sentence): Suddenly “maybe we should form a village” sounded less like a 1972 leftover and more like a backup plan."],
     keep=[]),
 'U4': dict(n=1, before='[image: one of the comments]\n\n' + O['C8'], after=O['C10'], length='three to five sentences, 55 to 90 words', points=[
     "That comment (the one in the image above) applies more to large socialism experiments than to small communes.",
     "The objection still deserves a serious answer: some people really would rather let somebody else take responsibility.",
     "Shared ownership can blur responsibility until the same three people maintain everything while everybody else discusses freedom (Joel's words; keep them).",
     "Informal leaders then gain power, partly because everyone keeps handing it to them."],
     keep=[]),
 'U5': dict(n=1, before=O['C9'], after=O['C11'], length='three to five sentences, 50 to 90 words', points=[
     "So (it follows from the paragraph before) communal ownership needs four things: named stewardship; visible duties; consequences for chronic freeloading; and enough relational capacity to confront the problem before resentment becomes the real government (Joel's words from “before”; keep them).",
     "A community can't run on the assumption that removing bosses removes passivity, selfishness, theft, or learned helplessness (all four)."],
     keep=[]),
 'U6': dict(n=1, before=O['C10'], after=V['C12'], length='three to five sentences, 55 to 90 words', points=[
     "The desire to return to a natural way of living together has outrun the knowledge of how.",
     "People know they're lonely and exhausted (Joel's words).",
     "They usually don't know three things: why so many earlier communities failed; why the same conflicts keep returning; and how quickly beautiful land stops mattering once money, children, jealousy, and ownership enter the picture."],
     keep=[]),
}
OUT = HERE / 'writers-r2'; OUT.mkdir(exist_ok=True)
for u, d in UNITS.items():
    brief = '\n'.join('- ' + p for p in d['points'])
    if d['keep']:
        brief += '\n\nKeep word for word:\n' + '\n'.join('- ' + k for k in d['keep'])
    brief += ("\n\nThat's what Joel's published version says, and all of it has to be there, at the same strength, with the same "
              "people doing the same things. The wording is yours, except the words marked as his.\n\n" + NOTICE)
    t = dict(brief=brief, before=d['before'], after=d['after'], length=d['length'],
             voice="in Joel's voice, like the paragraphs around it (first person where he speaks for himself)")
    tp = OUT / ('%s-target.json' % u); tp.write_text(json.dumps(t, indent=1, ensure_ascii=False), encoding='utf-8')
    w = R.build_draft(tp)
    assert w.startswith(OPEN_OLD), u
    w = open_new(d['n']).replace('It replaces', 'It carries') + w[len(OPEN_OLD):]
    w = w.replace('What it has to get across:', 'The article so far, which the reader has already read (for context and callbacks; don\'t repeat it):\n'
                  + sec1 + '\n\n# Communes Are Hot Again 🔥\n[this section starts here]\n\nWhat it has to get across:', 1)
    a = w.index('- The paragraphs that failed marched.')
    w = w[:a] + ROUND1 + w[a:]
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
