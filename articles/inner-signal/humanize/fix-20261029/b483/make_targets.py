"""Batch 483: the next try at the 10 stretches whose batch 482 version still read AI in place (the candidate recheck of
2026-10-29 19:21 UTC, `../b482/recheck/read/SPOTS.md`), by fresh writers given what read AI last time and the shape rules
from Emulate's passing rewrites (`../emulate-lessons/LESSONS.md`, checked by me into LESSONS-FOR-BRIEF.md).

Joel, 2026-10-29 17:21 UTC: "we never publish nonsense because it passes pangram. we come back and we try again if clarity
loses on pangram." (E291); 19:22 UTC: "not sure why you are asking before even checking if you can learn the lessons"
(E293: the lessons from what we have come before any purchase). Each item starts from the working copy's clear version
(HUMANIZED-SO-FAR.md, unchanged: batch 482's versions were never in it). Only the flagged stretch changes.

  python3 articles/inner-signal/humanize/fix-20261029/b483/make_targets.py   -> TARGETS.json, writers/BRIEF-W<k>.md
"""
import json
import pathlib
import sys

B = pathlib.Path(__file__).resolve().parent
H = B.parents[1]
ROOT = H.parents[2]
P482 = B.parent / 'b482'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

MASTER = H / 'HUMANIZED-SO-FAR.md'
CAND = P482 / 'CANDIDATE-MASTER.md'
FAILED = ['T2', 'T4', 'T5', 'T6', 'T7', 'T9', 'T12', 'T15', 'J3', 'T17']
# his HG-S15 sentence (his version of 28 October): batch 482 held it back because its window started in our sentence
# before it; in batch 482's recheck it read AI (Low, 18 words) in a window of its own, the second check in a row, so it gets
# a suggestion for his card now
HIS_EXTRA = {'J5': {'starts': 'All of these are separate factors to consider:',
                    'flagged': 'All of these are separate factors to consider: conscious agreement, unconscious receptivity, '
                               'emotional compliance, legal and ethical consent.',
                    'readings': ['AI (Low), window 5 of part A (2026-10-29 18:18 check)',
                                 'AI (Low), window 5 of part A (2026-10-29 19:22 check)']}}
# one writer per stretch of the guide, so neighbours that turned red together are rewritten together
GROUPS = {'W1': ['J5', 'T2', 'T4', 'T7'], 'W2': ['T5', 'T6', 'T9'], 'W3': ['T12', 'T15', 'J3', 'T17']}
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})

BRIEF = '''# Batch 483: the next try at sentences that read AI (writer W{k})

You are writing for Joel, a Substack writer, in his self-hypnosis guide ("The Inner Signal"). The guide was rewritten so
that Pangram, an AI-text detector (version 4.1), reads it as human-written. The flagged sentences below read AI in its
check, and so did the new version another writer made of each in the last round: that version is shown, with how it
read. Your job: for each item, write **two new versions of only the flagged sentences**, saying exactly what they say now,
just as clearly, in Joel's voice, in shapes that don't read AI.

Joel's rule, which outranks the detector: "we never publish nonsense because it passes pangram." A version a reader can't
follow on a first read, or that drops or changes a point, is worthless however human it sounds.

{his_note}## What each new version must do
- Say everything the flagged sentences say now: every point, step, condition, contrast and example, with the same
  strength. The current wording is clear and was read beside Joel's published version (shown as PUBLISHED, the meaning
  reference; its wording is the AI-written original, so don't copy its phrasing).
- Be clear on a first read to someone who only sees the new paragraph.
- Fit the paragraph: the sentences around it stay as they are, so no repeating them, and no "it"/"this" without
  something to point to.
- Keep his terms exactly: the inner adult's three jobs are the Nurturer, the Protector and the Guide; a protective part
  from childhood is a guard; the inner child is also "your little one"; "borrowed adulthood" is his term. American
  spelling.
- Add nothing: no new claim, example, warning, safety line or reassurance.

## What read AI last time (don't repeat these shapes)
Each item shows the last round's version (LAST TRY) and how it read in place. Several were casual rewrites of the same
length and order as the sentence they replaced: "Stick to the one thing you're doing, with one anchor or image to get
started and one way to come back. You can also set yourself a tone if you want one, maybe warm or bounded or directed or
neutral witnessing, or whatever else." read AI at High, and so did the untouched sentences around it. A casual word or
"maybe ... or whatever" on top of the same shape doesn't change how it reads. Change the shape.

## Shape rules from the rewrites that passed
{lessons}
## What else reads AI to Pangram 4.1 (avoid it)
- Wry quips, joke similes and punchlines; aphorisms and balanced closers that wrap a thought up; tidy follow-ups that
  restate, sum up or reassure.
- Definitions and explanations in a textbook shape ("X means A and then B"); parallel pairs and "not X, but Y"
  contrasts; colon reveals and signposting.
- Lists of abstract nouns, especially in threes; lists of options strung with "or" in one breath.
- Generic "you"/"imagine" scenarios; stock words (journey, profound, navigate, delve, crucial, genuinely, truly).

## What to return
Write your answer with a single Write call to `{out}`, as JSON:

{{"<item id>": {{"v1": "<the replacement for all the flagged sentences of the item, in order>",
                 "v2": "<a second replacement, different in shape from v1>",
                 "keeps": "<one line: the points of the flagged sentences, and where each is in v1 and v2>"}}, ...}}

Each replacement replaces the flagged sentences as one stretch (they are next to each other in the paragraph, in the
order given), so it can be one sentence or several. Read only `{targets}` (your items are listed under "W{k}"); don't run
commands or use the web. Reply with only "DONE: <number of items>".
'''

HIS_NOTE = {'J3': """**Item J3 is Joel's own line** (from his inner child guide). Nothing goes in without him: your versions are suggestions
he will see beside his own words. Stay as close to his words as the job allows, and change only what most likely reads
AI. It ends the same paragraph as item T15, right after it; write the two so they read well together.

""", 'J5': """**Item J5 is Joel's own sentence** (he wrote it on 28 October). Nothing goes in without him: your versions are
suggestions he will see beside his own words. Stay as close to his words as the job allows (keep his four factors, in his
words), and change only what most likely reads AI: here, most likely the colon and the list in one breath. Item J5 has no
last try: his sentence itself read AI (Low) twice.

"""}


def main():
    md = MASTER.read_text(encoding='utf-8')
    bl = sr.blocks(md)
    old = {t['id']: t for t in json.loads((P482 / 'TARGETS.json').read_text(encoding='utf-8'))['items']}
    versions = {}
    for f in sorted((P482 / 'writers').glob('VERSIONS-W*.json')):
        versions.update(json.loads(f.read_text(encoding='utf-8')))
    choices = json.loads((P482 / 'CHOICES.json').read_text(encoding='utf-8'))
    spots = {s['id']: s for s in json.loads((P482 / 'recheck' / 'read' / 'SPOTS.json').read_text(encoding='utf-8'))['spots']}
    red = json.loads((P482 / 'recheck' / 'read' / 'SPOTS.json').read_text(encoding='utf-8'))['red_elsewhere']
    cand = sr.blocks(CAND.read_text(encoding='utf-8'))
    items = []
    for tid in FAILED:
        t = old[tid]
        i = t['block']
        assert bl[i]['text'] == t['paragraph'], (tid, 'the working copy changed under the target')
        pick = choices[tid]['pick']
        # the windows that turned red on unchanged words within two paragraphs of this one (in batch 482's candidate text)
        near = []
        for r in red:
            if r['red_last_time']:
                continue
            first = r['text'].split('\n')[0][:60].translate(FLAT)
            for j in range(max(0, i - 2), min(len(cand), i + 3)):
                if first and first in cand[j]['text'].translate(FLAT):
                    near.append('%s (%s, %d words)' % (r['text'].replace('\n', ' / '), r['reading'], r['words']))
                    break
        items.append({'id': tid, 'block': i, 'where': t['where'], 'whose': 'his' if tid.startswith('J') else 'ours',
                      'readings_before': t['readings'], 'paragraph': t['paragraph'], 'flagged_stretch': t['flagged_stretch'],
                      'before': t['before'], 'after': t['after'], 'published': t['published'],
                      'last_try': {'version': versions[tid][pick], 'read_in_place': spots[tid]['now'],
                                   'windows': spots[tid]['windows'],
                                   'other_version_not_checked': versions[tid]['v2' if pick == 'v1' else 'v1']},
                      'turned_red_nearby': near,
                      'writer': next(w for w, ids in GROUPS.items() if tid in ids)})
    for tid, x in HIS_EXTRA.items():
        i = next(b['i'] for b in bl if b['text'].startswith(x['starts']))
        text = bl[i]['text']
        assert text.count(x['flagged']) == 1, tid
        pub = old['T2']['published'][:0]
        import difflib
        pubs = sr.blocks((H / 'source' / 'published-20260928.md').read_text(encoding='utf-8'))
        best = sorted(range(len(pubs)), key=lambda j: -difflib.SequenceMatcher(
            a=text.lower(), b=pubs[j]['text'].lower(), autojunk=False).ratio())[:2]
        items.append({'id': tid, 'block': i, 'where': sr.where(bl, i), 'whose': 'his', 'readings_before': x['readings'],
                      'paragraph': text, 'flagged_stretch': x['flagged'], 'before': bl[i - 1]['text'],
                      'after': bl[i + 1]['text'], 'published': [pubs[j]['text'] for j in sorted(best)] + pub,
                      'last_try': None, 'turned_red_nearby': [],
                      'writer': next(w for w, ids in GROUPS.items() if tid in ids)})
    (B / 'TARGETS.json').write_text(json.dumps({'groups': GROUPS, 'items': items}, ensure_ascii=False, indent=1) + '\n',
                                    encoding='utf-8')
    lessons_file = B / 'LESSONS-FOR-BRIEF.md'
    lessons = lessons_file.read_text(encoding='utf-8') if lessons_file.exists() else '(none yet)\n'
    for w in GROUPS:
        brief = BRIEF.format(k=w[1:], out=B / 'writers' / ('VERSIONS-%s.json' % w), targets=B / 'TARGETS.json',
                             lessons=lessons, his_note=''.join(HIS_NOTE[j] for j in GROUPS[w] if j in HIS_NOTE))
        (B / 'writers' / ('BRIEF-%s.md' % w)).write_text(brief, encoding='utf-8')
    for it in items:
        print(it['id'], it['writer'], it['where'], '| near red:', len(it['turned_red_nearby']), '|',
              it['last_try']['read_in_place'] if it['last_try'] else 'his own sentence, no last try')
    print('lessons in the brief:', 'yes' if lessons_file.exists() else 'NOT YET')


if __name__ == '__main__':
    main()
