"""The romance post's Medium windows, on a marking page for him to fix (2026-11-08, his message of 17:20 UTC: "ok show me
any more medium sections i will fix those as well, i notice that medium sections usually do point at ai slop
writing"). Every window his whole-article check of 16:47 UTC read Human at Medium (MEDIUM-WINDOWS.json), except where a
later section check reread the paragraph; there that check's Medium windows (r27, r28) are shown instead. Each paragraph
is shown as the fixed version has it now; a window whose words are gone is left out. One card a paragraph, his to edit.

  python3 articles/romance/review/teach-20261108/build_t4.py     (from the repo root)

writes PAGE-T4.md, REVIEW-T4.json, REVIEW-T4.html, REVIEW-T4.artifact.html and REVIEW-T4.md beside this file.
"""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
FIX = REPO / 'articles' / 'romance' / 'humanize' / 'fix-20261107'
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as SR  # noqa: E402

FEED = {'A': 'https://www.pangram.com/feed/87029c8c-313d-436c-b885-e76466096da6',
        'B': 'https://www.pangram.com/feed/5b03d47c-4290-42e5-8693-688418a08a68'}
H = 'https://www.pangram.com/history/'
norm = lambda s: re.sub(r'\s+', ' ', s).strip()  # noqa: E731
q = lambda s: s.replace('‘', "'").replace('’', "'").replace('“', '"').replace('”', '"')  # noqa: E731
fp = lambda s: hashlib.sha256(norm(s).encode('utf-8')).hexdigest()[:12]  # noqa: E731

IDX = {int(l.split()[0]): l.split()[2] for l in (FIX / 'whole' / 'LIVE-INDEX.txt').read_text().splitlines()}
BYFP = {}
for i, h in IDX.items():
    BYFP.setdefault(h, []).append(i)
REPL = json.loads((FIX / 'whole' / 'REPLACEMENTS.json').read_text(encoding='utf-8'))
HEADS = json.loads((HERE / 'HEADINGS.json').read_text(encoding='utf-8'))
WHOLE = json.loads((HERE / 'MEDIUM-WINDOWS.json').read_text(encoding='utf-8'))['whole']


def live_of(para):
    if fp(para) in BYFP:
        return BYFP[fp(para)][0], 'live'
    for k, v in REPL.items():
        if any(q(norm(para)) == q(norm(x)) for x in v):
            return int(k), 'fixed'
    raise SystemExit('unplaced: ' + para[:60])


def current(live, para):
    """The paragraph as the fixed version has it now."""
    v = REPL.get(str(live))
    if not v:
        return para
    hit = [x for x in v if q(norm(x))[:40] == q(norm(para))[:40]]
    return hit[0] if hit else v[0]


def heading(live):
    hs = [h for h in HEADS if h[0] <= live]
    return hs[-1][2] if hs else ''


ITEMS = {}  # live -> {'text', 'wins': [(words, source)]}
for d, _line, para, meds in WHOLE:
    live, _ = live_of(para)
    cur = current(live, para)
    e = ITEMS.setdefault(live, {'text': cur, 'wins': []})
    for m in meds:
        if q(norm(m)) in q(norm(cur)):
            e['wins'].append((m, 'whole-' + d))

# Medium windows of the section checks that reread their paragraphs (r27, r28)
SEC = [('r28/checks/RESULTS-r28.json', ('r28-labels', 'r28-ptsd', 'r28-dam', 'r28-pillars')),
       ('r27/checks/RESULTS-r27.json', ('r27-jeal-b', 'r27-ideal-c'))]
for f, keys in SEC:
    res = json.loads((FIX / f).read_text(encoding='utf-8'))
    for k in keys:
        r = res[k]
        text = (FIX / f.split('/')[0] / 'checks' / ('CHECK-%s.txt' % k)).read_text(encoding='utf-8')
        for w in r['windows']:
            if w['confidence'] != 'Medium':
                continue
            para = next(p for p in text.split('\n\n') if q(norm(w['text'].split('\n')[0]))[:30] in q(norm(p)))
            live, _ = live_of(para)
            cur = current(live, para)
            e = ITEMS.setdefault(live, {'text': cur, 'wins': []})
            if q(norm(w['text'])) in q(norm(cur)) and all(q(norm(w['text'])) != q(norm(x)) for x, _ in e['wins']):
                e['wins'].append((w['text'], k + '|' + r['link']))
ITEMS = {k: v for k, v in ITEMS.items() if v['wins']}

# What I see in each (his rule: name the tells I see, and the human tells, when I ask for his help)
NOTES = {
    4: 'Human tells: "tangled up together", the plain "I want" run. I can’t find an AI tell here.',
    13: 'Short questions in a run; human tells: "Are we ready?" after a long question. I can’t find an AI tell here.',
    14: 'The window is three of the questions. Human tells: "anything kinky you need to be able to say out loud". I can’t find an AI tell here.',
    28: 'Short questions in a run ("Then what? You block her?"), and "Or vice versa." standing alone. Human tells: "she’s gonna call you", your Baptist girlfriend.',
    34: 'Mine. Tell I see: the closing one-liner ("Doomscrolling entertains you too.") lands like a punchline after an abstract sentence ("the existential void another superficial fix creates").',
    35: 'Tell I see: "They may actually mean:" announces the reading before giving it. Human tell: "drainingly superficial".',
    39: 'Mine. Tell I see: "not a label:" (the X-not-Y turn), and "I don’t need to promise that on paper." as a short landing.',
    40: 'Tell I see: "Usually they’re just less aware that it isn’t." is an X-isn’t-Y line. Human tell: your friend’s "No, I’m miserable, dude."',
    51: 'A fragment list ending on "Everything." Human tells: "ALWAYS", "survives contact with another human being". The one-word ending may be what reads.',
    69: 'Tell I see: "It’s philosophical." as a short reveal. Human tell: "(often subconscious)".',
    73: 'Mine. Tells I see: "and I agree" tacked on, and "which can create the opposite pattern" (abstract, unexplained). Human tell: "totally broke and crazy".',
    76: 'Tell I see: "There is a real contradiction here." announces instead of saying it.',
    77: 'Tells I see: two hedges ("I think", "It may be") before the point.',
    97: 'Short line "Other people know them." Human tell: "irritated, bored, jealous". I can’t find an AI tell here.',
    107: 'Mine. Tells I see: a source note opening the paragraph ("comes from my own experience and from reading I’ve done"), an em-dash list of three chemicals, "biases us toward".',
    108: 'Mine. Tell I see: "You might get anxious or suspicious." as one of two parallel "You might" lines.',
    114: 'An imperative as a fragment ("Ask deep questions."). Human tell: "may seem silly". I can’t find an AI tell here.',
    116: 'Mine. Tell I see: "its own little high too" (a cute coinage of mine).',
    117: 'Short question "Is it weird?". Human tells: "hit you up later", "Can you guys be normal together". I can’t find an AI tell here.',
    119: 'Tell I see: "It doesn’t prove anything." (your "doesn’t prove" pattern).',
    124: 'A short question. Human tell: "“I have baggage” tells me almost nothing." I can’t find an AI tell here.',
    125: 'Tells I see: a run of four questions, and "That tells me more than either of us announcing that we’re healed." as a tidy close.',
    126: 'Mine. Tells I see: "The most recent conflicts are the best place to look." (a topic sentence that announces), then a run of questions.',
    135: 'Tell I see: "That was my mistake." as a short confession line. I can’t find more.',
    154: 'Tell I see: two short sentences in a row ("I see the good. I give the benefit of the doubt ...") with a neat turn ("stopped being a benefit"). Human tells: "like Ping Pong", "anti-PTSD".',
    155: 'Short questions; "That’s my question." as a landing. Human tell: "Would my twin flame behave like this?"',
    157: 'Your Bee story; "She would tell you the same." Human tell: "witchcrafted". I can’t find an AI tell here.',
    160: 'Tell I see: "That wasn’t the whole story." as a short turn. Human tell: "enough insanity for several lifetimes".',
    149: 'Mine. Short lines in a run ("We’re twin flames. She knows my motives. I’m Lord Krishna."). Human tell: "Lord Krishna".',
    150: 'Short line "I’m not trying to make her jealous." Human tell: "she isn’t ready for me". I can’t find an AI tell here.',
    151: 'Mine. Tell I see: the "not when ..." tail, a turn shaped like a quip.',
    171: 'Tells I see: "Phone or video first can help. So can ..." (a short parallel pair), "but they noticed something real" (a balancing concession). Human tell: "helicoptering".',
    173: 'Tell I see: "That only deals with pregnancy, though." as a short turn. Human tell: "Gandarussa", "traditonal".',
    175: 'A two-word question ("Based on what?"). I can’t find an AI tell here.',
    206: 'Short questions. Human tell: "suddenly it was weird." I can’t find an AI tell here.',
    214: 'Tell I see: "I like that idea." (approval announced). Human tell: the long list from Toft.',
    215: 'Mine. Tell I see: "So I’d rather ..." (a preference announced).',
    216: 'Tells I see: three short imperatives in a row ("See people together. Go places. Don’t just disappear ...").',
    219: 'Tell I see: "A peer can give another angle." (a generic opener). Human tell: "hopefully does not".',
    223: 'Mine. Tell I see: a balanced either/or ("Sometimes she’s deliberately ..., and other times it’s hard to tell").',
    252: 'Tells I see: an announcing opener with a list of three ("honesty, closeness, and equal dignity"). Human tell: "tear each other’s clothes off".',
    253: 'Tells I see: an aphorism with an X-not-Y turn ("gives the space for desire, even if it doesn’t spark it").',
    264: 'One word ("Woops..."), your joke. I can’t find an AI tell here.',
    277: 'Tell I see: "Women often show wanting directly." (an abstract topic sentence). Human tell: "even when they could do it themselves".',
    285: 'Mine, from your T1 lessons. Tell I see: "The same is true for a woman." (an announcing opener). Human tell: "pretending she can’t open a jar".',
    286: 'Mine. Tell I see: "Women can get pulled in two directions here." (announces).',
    287: 'Mine. Short line "She’s choosing the ride." Human tell: "a woman who drives just fine asking me to drive".',
    327: 'One word ("Anyway."). Human tell: "playing John Legend on loop". I can’t find an AI tell here.',
    332: 'Your Two Pillars paragraph, an owner lock; "I think that’s rare." I can’t find an AI tell here.',
    338: 'One letter ("H."), the start of the paragraph. I can’t find an AI tell here.',
    342: 'Mine. A short question after an ellipsis. Human tell: "the biggie"-style register around it.',
    343: 'Tell I see: "I’d call that a practical partnership." (naming the thing).',
    346: 'Mine. Tell I see: a balanced "What counts as X, and what’s just Y" question.',
    349: 'Tells I see: a parallel pair ("You can’t promise ... You can promise ...").',
    361: 'Tell I see: "was not simply tracking" (an X-not-Y turn).',
    405: 'Two words ("Well, yeah."). I can’t find an AI tell here.',
    409: 'A short line ("That drove me crazy."). Human tell: the door story. I can’t find an AI tell here.',
    437: 'Mine. Tells I see: a list of three ("how much you say, and to whom, and how publicly") and "really depends on".',
    438: 'Mine. Tell I see: "Look at what you contributed." as a bare imperative.',
    440: 'Mine. Tell I see: "No, that isn’t true." then a balanced "partly ..., but ..." correction.',
    441: 'Tell I see: "doesn’t always have to be the last chapter" (a soft metaphor). Human tell: "You’re not a yo-yo."',
    44: 'A short landing ("You’re not ready."). Human tells: "Get a cat or a puppy", "come on". I can’t find an AI tell here.',
}
# The word-for-sense read of PAGE-T4.md (sense-t4/, two fresh readers, every planted error found)
SENSE = {
    173: 'Its one finding: "traditonal" is a typo for "traditional" (I fix that either way), and "health benefits (including libido and for HIV)" mixes a noun with "for".',
    332: 'Its one finding: the capital "If" mid-sentence, which is your owner-final Two Pillars text (2026-08-24), so it stays.',
    338: 'Its one finding: "naturally deepen ... so it was natural for the dependency" says natural twice; "so the dependency grew too" would say it once.',
    441: 'Its one finding: the sentences after it are about cutting contact and letting them back in, not public demonization; "doesn’t always have to be the last chapter" may want the breakup as its subject.',
}
SENSE_NONE = 'A fresh reader read it for sense (sense-t4/) and found nothing wrong.'
ASK = ('You asked to see every Medium window (2026-11-08 17:20 UTC: "i notice that medium sections usually do point at ai '
       'slop writing").')


def main():
    order = sorted(ITEMS)
    md, last_head = [], None
    for live in order:
        h = heading(live)
        if h != last_head:
            md += ['### ' + h, '']
            last_head = h
        md += [ITEMS[live]['text'], '']
    MD = '\n'.join(md).strip() + '\n'
    (HERE / 'PAGE-T4.md').write_text(MD, encoding='utf-8')
    BL = SR.blocks(MD)
    cards = []
    for live in order:
        e = ITEMS[live]
        b = next(i for i, x in enumerate(BL) if x['text'] == e['text'])
        spans = []
        for w, _ in e['wins']:
            t = BL[b]['text']
            a = q(t).find(q(norm(w)))
            if a < 0:
                a = q(norm(t)).find(q(norm(w)))
            spans.append({'block': b, 'start': max(a, 0), 'end': max(a, 0) + len(norm(w))} if a >= 0 else
                         {'block': b, 'start': 0, 'end': len(t)})
        srcs = sorted({s for _, s in e['wins']})
        links = []
        for s in srcs:
            if s.startswith('whole-'):
                links.append('[your whole check, draft %s](%s)' % (s[-1], FEED[s[-1]]))
            else:
                links.append('[its section check](%s)' % s.split('|')[1])
        whose = 'mine' if str(live) in REPL else 'the live post’s'
        cards.append(dict(
            id='M-%d' % live, type='medium', advice='edit', keep_label='leave it',
            whose=('he asked: "ok show me any more medium sections i will fix those as well" (2026-11-08 17:20 UTC); '
                   'the words are ' + whose),
            title='“%s”' % (e['wins'][0][0][:70] + ('…' if len(e['wins'][0][0]) > 70 else '')),
            reading='Human, Medium in %s.' % ', and '.join(links),
            why=ASK, advice_note=NOTES.get(live, 'I can’t find an AI tell here. Can you help show me the tells I’m missing?'),
            sense=SENSE.get(live, SENSE_NONE),
            spans=spans))
    review = {
        'format': 'joel-suggestion-review-v1', 'review_id': 'romance-medium-t4',
        'title': 'Romance Advice I Wish My Parents Taught Me: the Medium windows',
        'intro': ['Every window your whole-article check read Human at Medium, in the paragraphs it read, shown as the fixed '
                  'version has them now (where a section check reread a paragraph since, its Medium windows are shown '
                  'instead). Each highlight is the window; press Edit it to write your version, or leave it.',
                  'Under each I name the tells I see, and where I see none, the human tells I do see. "Mine" means my '
                  'rewrite of the live words.'],
        'git_file': 'articles/romance/review/teach-20261108/REVIEW-T4.html',
        'article': {'file': 'articles/romance/review/teach-20261108/PAGE-T4.md',
                    'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': '2026-11-08',
        'links': {'guide': 'https://ibogaqueen.substack.com/p/romance-advice-i-wish-my-parents', 'guide_label': 'your live post',
                  'review': 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/romance-20261108/articles/romance/review/teach-20261108/REVIEW-T4.md'},
        'types': {'medium': {'label': 'Medium', 'about': 'words Pangram read Human at Medium confidence'}},
        'suggestions': cards,
    }
    probs = SR.check(review, BL)
    if probs:
        raise SystemExit('\n'.join(probs))
    (HERE / 'REVIEW-T4.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    page = SR.page(review, MD, BL)
    (HERE / 'REVIEW-T4.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-T4.artifact.html').write_text(SR.artifact_view(page), encoding='utf-8')
    out = ['# %s: every card' % review['title'], ''] + [x for p in review['intro'] for x in (p, '')]
    for c in cards:
        b = c['spans'][0]['block']
        out += ['## %s: %s' % (c['id'], c['title']), '', '*%s* (the words are %s)' % (SR.where(BL, b), c['whose'].split('the words are ')[-1]), '',
                '> %s' % BL[b]['text'], '', '**Pangram:** %s' % c['reading'], '', '**What I see:** %s' % c['advice_note'], '', '**Sense read:** %s' % c['sense'], '']
    (HERE / 'REVIEW-T4.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print(len(cards), 'cards;', sum(len(v['wins']) for v in ITEMS.values()), 'windows; missing notes:',
          [k for k in order if k not in NOTES])


if __name__ == '__main__':
    main()
