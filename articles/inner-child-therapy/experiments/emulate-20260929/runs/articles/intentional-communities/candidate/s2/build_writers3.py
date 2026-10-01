"""Section 2, writers round 3 (2026-10-01, after Joel's answers of 14:49): C1, C4 and C9.

What's new against round 2:
- Joel rewrote C10 and C11 himself this afternoon. His before and after go into the prompt word for word, as the
  model of his voice in this section (the way reviewer.py's draft prompt carries his fixes catalogue).
- His rulings: wording can flex as long as the meaning stays; in C4 keep jobs, relationships and future outlook, feeds
  can go; the 1972 line is optional ("witty altho it's kind of an obvious ai quip").
- The round notes say what failed: 34 of 35 drafts, every one keeping the published paragraph's shape.
Same recorded adaptations of reviewer.py build_draft as rounds 1 and 2.
"""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
UNI = pathlib.Path('/home/claude/universal')
sys.path.insert(0, str(UNI / 'tools/humanization/reviewer')); import reviewer as R
G = {'__file__': str(HERE / 'build_writers.py')}
exec(compile(open(HERE / 'build_writers.py', encoding='utf-8').read().split("OUT = HERE / 'writers-r1'")[0], 'bw', 'exec'), G)
O, V, s1_end, OPEN_OLD, open_new, plain = G['O'], G['V'], G['s1_end'], G['OPEN_OLD'], G['open_new'], G['plain']
so_far = re.sub(r'<!--.*?-->', '', (HERE.parent / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'), flags=re.S)
sec1 = plain(so_far[:so_far.index('# Communes Are Hot Again')].strip()).replace('[Subscribe now](%%checkout_url%%)', '').strip()
V3 = json.load(open(HERE / 'fixlog-v3.json', encoding='utf-8'))['texts']
C3 = (HERE / 'trace-C3.txt').read_text(encoding='utf-8').strip()
C8o = 'The commune comments became a miniature political-philosophy seminar, as Instagram comments sometimes do.'
JOEL = ("How Joel himself rewrote the two paragraphs that come later in this section, this afternoon. The published version "
        "first, then his, word for word. It's the best guide to his voice here: plain, a bit rough, concrete happenings in "
        "place of abstractions, a repeated \"It requires\", a spoken \"No,\", and the polished lines dropped.\n\n"
        "Published: «%s»\nJoel's: «%s»\n\nPublished: «%s»\nJoel's: «%s»" % (O['C10'], V3['C10j'], O['C11'], V3['C11j']))
ROUND = ("- On this section, 34 of 35 drafts by other writers failed. They kept the published paragraph's shape: its points "
         "in its order, a polished line at the end, every claim in its own tidy sentence. Joel's own rewrite of two paragraphs "
         "passed.\n")
RULE = ("Joel's rulings for this section: the wording can change freely as long as the meaning stays. Nothing new about his "
        "life or anyone else's, no new examples, no numbers that aren't in the points, no feelings he didn't state.")
UNITS = {
 'C1': dict(before=s1_end + '\n\n# Communes Are Hot Again 🔥', after=V['C2'], length='two or three sentences, 35 to 60 words', points=[
     "The longing that shaped Joel's father's film (the documentary from the start of the article) is suddenly everywhere again.",
     "The U.S. Surgeon General's advisory, from 2023, reported that roughly half of American adults experience loneliness (adults, and roughly half: not \"50% of Americans\"). The words \"U.S. Surgeon General\" carry a link, so keep them together.",
     "It treated social connection as a public-health issue."]),
 'C4': dict(before=C3 + '\n\n[image: the Google Trends chart for both terms]', after=O['seba'], length='three to five sentences, 45 to 80 words', points=[
     "Joel can't prove AI caused that turn in interest, but the timing is hard to ignore.",
     "Around then, AI stopped being a tech-news curiosity and began changing people's jobs, their relationships and their outlook on the future (those three; Joel says \"feeds\" can go).",
     "So forming a village started to sound like a backup plan. The published line is: Suddenly “maybe we should form a village” sounded less like a 1972 leftover and more like a backup plan. Joel calls it \"witty altho it's kind of an obvious ai quip\": keep it word for word, or say its point your own way."]),
 'C9': dict(before='[image: one of the comments]\n\n' + C8o, after=V3['C10j'], length='three to five sentences, 50 to 85 words', points=[
     "That comment (the one in the image above) applies more to large socialism experiments than to small communes.",
     "The objection still deserves a serious answer: some people really would rather let somebody else take responsibility.",
     "Shared ownership can blur responsibility until the same few people maintain everything while everybody else talks about freedom. (The published words are \"the same three people maintain everything while everybody else discusses freedom\"; keep that image, in its words or yours.)",
     "Informal leaders then gain power, partly because everyone keeps handing it to them."]),
}
OUT = HERE / 'writers-r3'; OUT.mkdir(exist_ok=True)
for u, d in UNITS.items():
    brief = '\n'.join('- ' + p for p in d['points']) + '\n\n' + RULE + '\n\n' + JOEL
    t = dict(brief=brief, before=d['before'], after=d['after'], length=d['length'],
             voice="in Joel's voice, like his rewrites above (first person where he speaks for himself)")
    tp = OUT / ('%s-target.json' % u); tp.write_text(json.dumps(t, indent=1, ensure_ascii=False), encoding='utf-8')
    w = R.build_draft(tp)
    assert w.startswith(OPEN_OLD), u
    w = open_new(1).replace('It replaces', 'It carries') + w[len(OPEN_OLD):]
    w = w.replace('What it has to get across:', "The article so far, which the reader has already read (for context; don't repeat it):\n"
                  + sec1 + '\n\n# Communes Are Hot Again 🔥\n[this section starts here]\n\nWhat it has to get across:', 1)
    a = w.index('- The paragraphs that failed marched.')
    w = w[:a] + ROUND + w[a:]
    dd = OUT / u; dd.mkdir(exist_ok=True)
    (dd / 'prompt.txt').write_text(w, encoding='utf-8')
    print(u, len(w.split()), 'words')
