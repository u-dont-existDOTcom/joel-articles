"""Batch 482's writers' targets: the sentences the recheck of 2026-10-29 read AI that aren't his words, one item a paragraph.

Emulate's balance was 0 words on 2026-10-29 at 18:28 UTC (`emulate_humanize.py balance` on the laptop), so fresh writers make
the new versions this time (docs/EMULATE-FALLBACK.md: Emulate first when it can run), clear first: Joel, 2026-10-29 17:21
UTC, "we never publish nonsense because it passes pangram. we come back and we try again if clarity loses on pangram."
(E291). Each item gives the paragraph as it stands, its flagged sentences, the paragraphs around it, and his published
passage for what it has to say. Only the flagged sentences change.

  python3 articles/inner-signal/humanize/fix-20261029/b482/make_targets.py   -> TARGETS.json, writers/BRIEF-W<k>.md
"""
import difflib
import json
import pathlib
import sys

B = pathlib.Path(__file__).resolve().parent
H = B.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

MASTER = H / 'HUMANIZED-SO-FAR.md'
PUB = sr.blocks((H / 'source' / 'published-20260928.md').read_text(encoding='utf-8'))
# a link line next to a red window, not a sentence to rewrite (the window's red is the fractionation lines after it)
SKIP = {'Check out Nimja’s sleep playlist to go to sleep listening to hypnosis',
        # his inner child guide's sentence with its middle cut (batch 479's S1): his words, so it goes to him
        'That’s one grown-up doing three jobs, and each job keeps the others in balance.'}
GROUPS = 3
HIS_PLACE = {'No warmth today?': 630, 'Then rest your hands there and notice what you find, no faking required.': 630}
HIS_WAIT = {'Quick start: do this first, P3', 'Protecting Yourself from Hypnotists, P3'}
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})

BRIEF = '''# Batch 482: new versions of sentences that read AI (writer W{k})

You are writing for Joel, a Substack writer, in his self-hypnosis guide ("The Inner Signal"). The guide was rewritten so
that Pangram, an AI-text detector, reads it as human-written. In its newest check (version 4.1) the sentences below read
AI. Your job: for each item, write **two new versions of only the flagged sentences**, so that they say exactly what they
say now, just as clearly, in Joel's voice, without the patterns that read AI.

Joel's rule, which outranks the detector: "we never publish nonsense because it passes pangram." A version a reader can't
follow on a first read, or that drops or changes a point, is worthless however human it sounds.

## What each new version must do
- Say everything the flagged sentences say now: every point, step, condition, contrast and example, with the same
  strength. The current wording already passed a careful read beside Joel's published version (shown as PUBLISHED, which
  is the meaning reference: it says what the passage is for, but its wording is the AI-written original, so don't copy
  its phrasing).
- Be clear on a first read to someone who only sees the new paragraph.
- Fit the paragraph: the sentences before and after stay as they are, so no repeating them, and no "it"/"this" without
  something to point to.
- Keep his terms exactly: the inner adult's three jobs are the Nurturer, the Protector and the Guide; a protective part
  from childhood is a guard; the inner child is also "your little one"; "borrowed adulthood" is his term. American
  spelling.
- Add nothing: no new claim, example, warning, safety line or reassurance.

## What reads AI to Pangram 4.1 (avoid it)
- Wry quips, joke similes and punchlines ("a tiny wellness trade show"); aphorisms and balanced closers that wrap a
  thought up ("trance has a door in both directions"); tidy follow-ups that restate, sum up or reassure.
- Definitions and explanations in a textbook shape ("X means A and then B", "X places A inside B"); parallel pairs and
  "not X, but Y" contrasts; colon reveals and signposting ("one advantage ...: immediate dialogue").
- Lists of abstract nouns, especially in threes ("kinder behavior, more humility, better judgment"); say it about people
  and what they do instead.
- Generic "you"/"imagine" scenarios; stock words (journey, profound, navigate, delve, crucial, genuinely, truly).

What reads human: plain sentences of uneven length, his particulars, a reason or a doubt in his own words, casual
first-person asides ("I", "honestly", "for me") where the paragraph already speaks that way, concrete actions. The
document's own voice is casual and direct (see the paragraphs around each item).

## What to return
Write your answer with a single Write call to `{out}`, as JSON:

{{"<item id>": {{"v1": "<the replacement for all the flagged sentences of the item, in order>",
                 "v2": "<a second, different replacement>",
                 "keeps": "<one line: the points of the flagged sentences, and where each is in v1 and v2>"}}, ...}}

Each replacement replaces the flagged sentences as one stretch (they are next to each other in the paragraph, in the
order given), so it can be one sentence or several. Read only `{targets}` (your items are listed under
"W{k}"); don't run commands or use the web. Reply with only "DONE: <number of items>".
'''


HIS_NOTE = """**These sentences are Joel's own words** (from his inner child guide, or lines he wrote himself). Nothing goes in
without him: your versions are suggestions he will see beside his own words on his marking page. So stay as close to his
words as the job allows: keep his phrases, his rhythm and his particulars, and change only what most likely reads AI. One
of your two versions may be his own sentence with the smallest change you can find.
"""


def main():
    bl = sr.blocks(MASTER.read_text(encoding='utf-8'))
    sorted_ = json.loads((B / 'SORTED.json').read_text(encoding='utf-8'))
    items = {}
    for s in sorted_:
        if not s['reading'].startswith('AI') or s['fate'] != 'Emulate' or s['sentence'] in SKIP:
            continue
        i = s['block']
        it = items.setdefault(i, {'block': i, 'where': s['where'], 'flagged': [], 'readings': []})
        if s['sentence'] not in it['flagged']:
            it['flagged'].append(s['sentence'])
            it['readings'].append('%s, window %d of part %s' % (s['reading'], s['window'], s['part']))
    out = []
    for n, (i, it) in enumerate(sorted(items.items()), 1):
        text = bl[i]['text']
        # the flagged sentences as the paragraph has them (the checked text curls the guide's straight quotes, one
        # character for one), in the paragraph's order, and the stretch from the first to the last
        ft = text.translate(FLAT)
        spans = []
        for f in it['flagged']:
            k = ft.find(f.translate(FLAT))
            assert k >= 0, (it['where'], f)
            spans.append((k, k + len(f)))
        spans.sort()
        it['flagged'] = [text[x:y] for x, y in spans]
        a, z = spans[0][0], spans[-1][1]
        pubs = sorted(range(len(PUB)), key=lambda j: -difflib.SequenceMatcher(
            a=text.lower(), b=PUB[j]['text'].lower(), autojunk=False).ratio())[:2]
        out.append({'id': 'T%d' % n, 'block': i, 'where': it['where'], 'readings': it['readings'],
                    'paragraph': text, 'flagged_stretch': text[a:z], 'flagged': it['flagged'],
                    'before': bl[i - 1]['text'] if i > 0 else '', 'after': bl[i + 1]['text'] if i + 1 < len(bl) else '',
                    'published': [PUB[j]['text'] for j in sorted(pubs)]})
    groups = {'W%d' % (k + 1): [t['id'] for t in out[k::GROUPS]] for k in range(GROUPS)}
    for t in out:
        t['writer'] = next(w for w, ids in groups.items() if t['id'] in ids)
    # his own words that read AI: a suggestion each for his card (W4), never put in without him. His HG-S15 list and the
    # Quick start line of his 28 October version sit in windows that start in our sentences before them, so they wait.
    his = {}
    for s in sorted_:
        if not s['reading'].startswith('AI') or not s['fate'].startswith('his') or s['where'] in HIS_WAIT:
            continue
        # a line that stands in two places is placed where the window is: "No warmth today? ..." read red at the end of
        # part B's Inner child love paragraph, not in part A's two-hand practice (the sorting took the first place)
        blk = HIS_PLACE.get(s['sentence'], s['block'])
        his.setdefault(blk, {'where': sr.where(bl, blk), 'flagged': [], 'readings': [], 'whose': s['fate']})
        if s['sentence'] not in his[blk]['flagged']:
            his[blk]['flagged'].append(s['sentence'])
            his[blk]['readings'].append('%s, window %d of part %s' % (s['reading'], s['window'], s['part']))
    for i, it in sorted(his.items()):
        text = bl[i]['text']
        ft = text.translate(FLAT)
        spans = sorted((ft.find(f.translate(FLAT)), ft.find(f.translate(FLAT)) + len(f)) for f in it['flagged'])
        assert all(x >= 0 for x, _ in spans), it['where']
        a, z = spans[0][0], spans[-1][1]
        pubs = sorted(range(len(PUB)), key=lambda j: -difflib.SequenceMatcher(
            a=text.lower(), b=PUB[j]['text'].lower(), autojunk=False).ratio())[:2]
        out.append({'id': 'J%d' % (len([x for x in out if x['id'].startswith('J')]) + 1), 'block': i, 'where': it['where'],
                    'readings': it['readings'], 'whose': it['whose'], 'paragraph': text, 'flagged_stretch': text[a:z],
                    'flagged': [text[x:y] for x, y in spans],
                    'before': bl[i - 1]['text'] if i > 0 else '', 'after': bl[i + 1]['text'] if i + 1 < len(bl) else '',
                    'published': [PUB[j]['text'] for j in sorted(pubs)], 'writer': 'W4'})
    groups['W4'] = [t['id'] for t in out if t['writer'] == 'W4']
    (B / 'TARGETS.json').write_text(json.dumps({'groups': groups, 'items': out}, ensure_ascii=False, indent=1) + '\n',
                                    encoding='utf-8')
    (B / 'writers').mkdir(exist_ok=True)
    for w in groups:
        brief = BRIEF.format(k=w[1:], out=B / 'writers' / ('VERSIONS-%s.json' % w), targets=B / 'TARGETS.json')
        if w == 'W4':
            brief = brief.replace('## What each new version must do', HIS_NOTE + '\n## What each new version must do')
        (B / 'writers' / ('BRIEF-%s.md' % w)).write_text(brief, encoding='utf-8')
    for t in out:
        print(t['id'], t['writer'], t['where'], '|', t['flagged_stretch'][:90])


if __name__ == '__main__':
    main()
