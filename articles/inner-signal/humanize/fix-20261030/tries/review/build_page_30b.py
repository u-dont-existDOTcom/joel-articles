"""The hypnosis guide's cards of 2026-10-30, after the second recheck of the day (REVIEW-30b.json, .html, .artifact.html,
.md).

Joel's results of 21:40 UTC (part A https://www.pangram.com/feed/a123b9a4-de86-462a-aa45-4f46b122ab4e, part B
https://www.pangram.com/feed/a485abe9-057b-4209-a9be-11ad81a90b90) read the tries of ../TRIES.json in place
(../read/SPOTS.md). One page, his guide as it is in Git (HUMANIZED-SO-FAR.md), in the marking page's form
(tools/humanization/suggestion_review.py, gate E265):
- the tries that read Human in place, ours to approve (a card says "reads Human" only at High, E295);
- T-339, which reads better but not Human yet;
- the suggestions for his own words: S-14, S-20, S-24 and S-782 (read in place in both rechecks of the day) and S-636
  (the exercise named instead of taught again; not checked in place);
- the stretches that still read AI after a try (T-508 with his R-509, the "Nothing happens" asks, the "Don't rush the
  repair" check), for him to keep or rewrite; S-162 is withdrawn (it read worse than his words);
- the words that read AI this time with nothing changed in them, for him to keep or rewrite.

  python3 articles/inner-signal/humanize/fix-20261030/tries/review/build_page_30b.py
"""
import collections
import datetime
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
T = HERE.parent
H = T.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/'
LANE = 'articles/inner-signal/humanize/'
ARTICLE = LANE + 'HUMANIZED-SO-FAR.md'
GIT_FILE = LANE + 'fix-20261030/tries/review/REVIEW-30b.html'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
BL = sr.blocks(MD)
FEED = {'20A': 'https://www.pangram.com/feed/fc1d8dae-ed2b-4050-9c0b-5c1571dc3548',
        '20B': 'https://www.pangram.com/feed/48eed31c-7ff5-4392-887c-92663cd6aea8',
        '21A': 'https://www.pangram.com/feed/a123b9a4-de86-462a-aa45-4f46b122ab4e',
        '21B': 'https://www.pangram.com/feed/a485abe9-057b-4209-a9be-11ad81a90b90'}
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})

TYPES = {
    'passes': {'label': 'Reads Human now',
               'about': 'A new version that read Human where it stands in the latest recheck, in place of words that '
                        'read AI or below High. Approve, Reject or Revise.'},
    'better': {'label': 'Reads better, not Human yet',
               'about': 'A new version that read better than the words it replaces, but still reads AI in one '
                        'place. Approve, Reject or Revise.'},
    'yours': {'label': 'Your own words',
              'about': 'A suggestion for a paragraph you wrote yourself. Approve uses the suggestion; Reject keeps '
                       'your words; Revise lets you write your own.'},
    'rewrite': {'label': 'For you to rewrite',
                'about': 'Words that still read AI after a try (the try and how it read are on the card). Keep them, '
                         'or edit them in your own words.'},
    'red': {'label': 'Reads AI this time only',
            'about': 'Words that read AI in the latest recheck with nothing changed in them or near them. Keep them, '
                     'or edit them in your own words.'},
}
FOUND = 'The two rechecks of 30 October (20:15 and 21:40 UTC)'

# what each try does, said for the card
WHAT = {
    'T-35': 'Cuts “Ads, screens, fear and cravings are already training your mind, and so are your tribe, the people in '
            'authority, loneliness and plain old repetition.”',
    'T-337': 'Cuts “A tightening won\'t tell you what it\'s about by itself, so ask what happened and whether the '
             'invitation fits.” and joins the two sentences around it again, as they were: “..., is a signal to '
             'investigate further, but \'No! That is Not Right!\' is a signal to stop ...”',
    'T-374': 'Cuts “If your subconscious won’t answer, it may be protecting you until your adult is steady enough to take '
             'in what it has.”',
}
TITLES = {'T-35': '“Ads, screens, fear and cravings …”', 'T-337': '“A tightening won\'t tell you …”',
          'T-374': '“If your subconscious won’t answer …”', 'S-14': '“since it\'s not "achieving something", but …”',
          'T-495': '“If nothing changes, notice that too …”', 'T-249': '“Don\'t read the directions out loud …”',
          'T-339': '“Sometimes the invitation just isn\'t right …”', 'T-503': '“Notice how the answer comes to you …”',
          'S-20': '“You\'ll follow whatever you notice …”', 'S-24': '“And "not sure" is a perfectly good answer …”'}
# my read of each beside his published version, short (../read/READ.md has it in full)
READ = {
    'T-35': 'It says what yours says without the list you cut on 25 October.',
    'T-337': 'It keeps every point the guide makes here; the response check just above already says a tightness is a '
             'notice to find out about.',
    'T-374': 'The section\'s first paragraph already says that silence may be protecting you.',
    'T-339': 'It keeps all four of your points (the wrong invitation, the new possibility with a feeling worth meeting, '
             'making room to find out which, doubt that isn\'t a guard and silence that isn\'t a hidden process), with '
             'both "it"s named.',
    'T-495': 'It says what "no change doesn\'t mean secret success" says, as one plain instruction.',
    'T-249': 'It keeps all three points: the same anchor, the directions not read out loud, the pause.',
    'T-503': 'All six ways an answer can come are there, said the way a script is spoken.',
    'T-505': 'What a presupposition is, why it\'s powerful, what to presume and what never to (obedience), and your '
             'example, all there. New: the quoted line a hypnotist might use to presume obedience.',
}


def quote_start(t, n=7):
    w = t.strip('“”"').split()
    return '“%s%s”' % (' '.join(w[:n]), ' …' if len(w) > n else '')


def say(xs):
    return (', '.join(xs[:-1]) + ' and ' + xs[-1]) if len(xs) > 1 else xs[0]


def changed_span(before, after):
    """Where BEFORE and AFTER differ, in BEFORE's offsets, widened to whole words."""
    a = 0
    while a < min(len(before), len(after)) and before[a] == after[a]:
        a += 1
    z = 0
    while z < min(len(before), len(after)) - a and before[-1 - z] == after[-1 - z]:
        z += 1
    k, e = a, len(before) - z
    while k > 0 and before[k - 1] not in ' ':
        k -= 1
    while e < len(before) and before[e] not in ' .,;:!?':
        e += 1
    return k, e


def span_of(i, stretch):
    t = BL[i]['text']
    k = t.find(stretch)
    assert k >= 0 and t.count(stretch) == 1, (i, stretch[:60])
    return {'block': i, 'start': k, 'end': k + len(stretch)}


def locate(text):
    """Each line of TEXT (a window's words) in the guide's blocks: [{'block', 'start', 'end', 'text'}]."""
    out = []
    for ln in [x.strip() for x in text.split('\n') if x.strip()]:
        hits = [b['i'] for b in BL if ln.translate(FLAT) in b['text'].translate(FLAT) and not b['level']]
        assert hits, ln[:60]
        i = hits[0]
        k = BL[i]['text'].translate(FLAT).find(ln.translate(FLAT))
        out.append({'block': i, 'start': k, 'end': k + len(ln), 'text': BL[i]['text'][k:k + len(ln)]})
    return out


def merged(spans):
    out = []
    for sp in sorted(spans, key=lambda x: (x['block'], x['start'])):
        if out and out[-1]['block'] == sp['block'] and sp['start'] <= out[-1]['end'] + 1:
            out[-1]['end'] = max(out[-1]['end'], sp['end'])
        else:
            out.append(dict(sp))
    return out


def last_reading(text):
    """How TEXT's words read in the recheck of 20:15 UTC: (part, 'AI (Low)' or 'Human (High)' ...)."""
    sys.path.insert(0, str(T / 'read'))
    from spots_tries import find, reading
    for p in 'AB':
        r = json.loads((T.parent / 'recheck' / 'read' / ('RESULT-%s.json' % p)).read_text(encoding='utf-8'))
        loc = find(r['text'], text)
        if loc:
            return p, reading(r, *loc)[0]
    return None, 'not found'


def main():
    tries = {t['id']: t for t in json.loads((T / 'TRIES.json').read_text(encoding='utf-8'))['tries']}
    spots_doc = json.loads((T / 'read' / 'SPOTS.json').read_text(encoding='utf-8'))
    spots = {s['id']: s for s in spots_doc['spots']}
    S = []
    # the tries that read Human, and T-339
    for tid in ('T-35', 'T-337', 'T-374', 'T-495', 'T-249', 'T-503', 'T-505', 'T-339'):
        t, sp = tries[tid], spots[tid]
        i = t['block']
        assert BL[i]['text'] == t['before'], tid
        part = sp['part']
        k, e = changed_span(t['before'], t['after'])
        take = t['kind'] == 'take back'
        now, before = sp['reading'], sp['reading_before']
        why = ('%s read %s in the recheck of 20:15 UTC ([part %s](%s)). %s read %s where it stands in the recheck of 21:40 '
               'UTC ([part %s](%s)). %s I read it beside your published version. %s' % (
                   'The paragraph' if take else 'The words it replaces', before, part, FEED['20' + part],
                   'Without the sentence, the paragraph' if take else 'This version', now, part, FEED['21' + part],
                   t['why'], READ[tid]))
        if tid == 'T-339':
            typ = 'better'
            note = ('Approve: it is clearer than what\'s there and it read better (AI at High before, AI at Low now). The '
                    'part that still reads AI (Low, at 0.50, a coin toss) is its last sentence, "Either way, ...", which '
                    'is the guide\'s sentence as it was; if it reads AI again next time, it gets its own try.')
        else:
            typ = 'passes'
            note = ('Approve: it reads Human where it stands and keeps every point.' if not take else
                    'Approve: the paragraph reads Human without it, and the point is said already.')
            if now != 'Human (High)':
                note += (' It read Human at %s confidence in place, so it may still read AI on its own or in a later '
                         'check.' % now[7:-1])
                if now == before:
                    note += ' It reads no worse than now and says it more plainly.'
        k2 = k
        title = TITLES.get(tid) or quote_start(t['after'][k2:])
        S.append({'id': tid, 'spot': tid, 'type': typ, 'title': title,
                  'where': sr.where(BL, i), 'spans': [{'block': i, 'start': k, 'end': e}],
                  'edits': [{'block': i, 'before': t['before'], 'after': t['after']}], 'inserts': [], 'moves': [],
                  'what': WHAT.get(tid) or '“%s” becomes “%s”' % (t['before'][k:e].strip(), t['after'][k:len(t['after']) - (len(t['before']) - e)].strip()),
                  'why': why, 'stays': 'The rest of the paragraph, word for word.', 'advice': 'approve',
                  'advice_note': note, 'found_by': FOUND,
                  'deciding': ('Approve cuts it; Reject keeps it as it is; Revise lets you write your own.' if take else
                               'Approve uses the new wording; Reject keeps it as it is; Revise lets you write your own.'),
                  'approve_label': 'cut it' if take else None})
    # the standing suggestions for his own words (the recheck of 20:15 UTC) and S-636
    for s in json.loads((T.parent / 'recheck' / 'SUGGESTIONS.json').read_text(encoding='utf-8'))['suggestions']:
        i = s['block']
        assert BL[i]['text'] == s['his'], s['id']
        k, e = changed_span(s['his'], s['suggestion'])
        if s['in_recheck']:
            p, r20 = last_reading(s['suggestion'])
            sys.path.insert(0, str(T / 'read'))
            from spots_tries import find, reading
            r21 = None
            for q in 'AB':
                res = json.loads((T / 'read' / ('RESULT-%s.json' % q)).read_text(encoding='utf-8'))
                loc = find(res['text'], s['suggestion'])
                if loc:
                    r21 = reading(res, *loc)[0]
                    break
            read = ('It read %s where it stands in the recheck of 20:15 UTC ([part %s](%s)) and %s in the recheck of 21:40 '
                    'UTC ([part %s](%s)).' % (r20, p, FEED['20' + p], r21, p, FEED['21' + p]))
            note = 'Your call. I\'d use it: it keeps your words where it can.'
            if r20 != 'Human (High)' or r21 != 'Human (High)':
                note += (' It read Human at Medium confidence in both checks, so it may want another light pass '
                         'later.' if r20 == r21 == 'Human (Medium)' else '')
        else:
            read = 'It names the exercise and keeps your words for the inner child; it hasn\'t been checked in place yet.'
            note = 'Your call. I\'d use it: the exercise is taught once, as you asked.'
        S.append({'id': s['id'], 'spot': s['id'], 'type': 'yours', 'title': TITLES.get(s['id']) or quote_start(s['suggestion'][k:]),
                  'where': s['where'], 'spans': [{'block': i, 'start': k, 'end': e}],
                  'edits': [{'block': i, 'before': s['his'], 'after': s['suggestion']}], 'inserts': [], 'moves': [],
                  'what': '“%s” becomes “%s”' % (s['his'][k:e].strip(), s['suggestion'][k:len(s['suggestion']) - (len(s['his']) - e)].strip()),
                  'why': '%s %s (%s.)' % (s['why'], read, s['whose'][:1].upper() + s['whose'][1:]),
                  'stays': 'The rest of your paragraph, word for word.', 'advice': 'approve', 'advice_note': note,
                  'found_by': 'My read of the whole guide beside your published version (30 October)',
                  'deciding': 'Approve uses this wording; Reject keeps yours; Revise lets you write your own.',
                  'approve_label': 'use this wording'})
    # what still reads AI after a try: for him to keep or rewrite
    reds = spots_doc['red_elsewhere']
    w7 = 'So an honest bridge might sound more like'
    i508, i510 = tries['T-508']['block'], 510
    assert BL[i510]['text'].startswith('An embedded invitation places')
    k508 = BL[i508]['text'].find('A better bridge claims')
    S.append({'id': 'R-508', 'spot': 'T-508,R-509', 'type': 'rewrite', 'title': '“A better bridge claims a lot less …”',
              'where': sr.where(BL, i508),
              'spans': [{'block': i508, 'start': k508, 'end': len(BL[i508]['text'])},
                        span_of(i510, 'An embedded invitation places a small direction inside a larger sentence.')],
              'edits': [], 'inserts': [], 'moves': [],
              'why': ('These read AI (High) together, in one window, in both rechecks of 30 October: the better-bridge line '
                      'that ends Pattern 4 and your embedded-invitations paragraph after it (20:15 UTC: [part B](%s), '
                      'window 15, 140 words; 21:40 UTC: [part B](%s), window 7, 67 words). My try led into the better '
                      'bridge the way your reframing paragraph does: "%s, ‘As I breathe, my adult self may become present '
                      'enough to hear a little of what the wound needs.’" It read AI (High) with your paragraph again. '
                      'The likeliest part is the textbook definition your paragraph opens with ("An embedded invitation '
                      'places a small direction inside a larger sentence."): a free-standing definition is the one shape '
                      'that has read AI everywhere in this guide, and this same sentence read AI (High) on 29 October '
                      'too, when the comprehension fix brought it back; the version without it had read Human (the '
                      'Emulate study\'s case reverse-X8.4).' % (FEED['20B'], FEED['21B'], w7)),
              'reading': 'AI (High), in both rechecks of 30 October', 'advice': 'edit', 'keep_label': 'keep it as it is',
              'advice_note': ('Rewrite either or both in your own words if you want them to read Human. Your fix strategy '
                              'fits here: say what an embedded invitation is for before or instead of defining it, and '
                              'lead into the better bridge the way you led into the honest reframe. Keep every point.'),
              'found_by': FOUND})
    i381, i382 = 381, 382
    S.append({'id': 'R-381', 'spot': 'S-382', 'type': 'rewrite', 'title': '“Is there a way you could try this …”',
              'where': sr.where(BL, i381),
              'spans': [{'block': i381, 'start': 0, 'end': len(BL[i381]['text'])},
                        {'block': i382, 'start': 0, 'end': len(BL[i382]['text'])}],
              'edits': [], 'inserts': [], 'moves': [],
              'why': ('The smaller-scale line read AI (Low) in both rechecks of 30 October ([part A](%s), [part A](%s)); '
                      'it had read Human (High) on 29 October. Your three "Show me" asks read AI (High) at 20:15 UTC. My suggestion '
                      'for your asks, "Ask for something small, like “Show me one body sensation,” or “Show me one '
                      'word.” If even that gets you nothing, try “Show me whether today is for listening or resting.”", '
                      'read AI (Medium) at 21:40 UTC, with the next line.' % (FEED['20A'], FEED['21A'])),
              'reading': 'AI (Low) and AI (High); my suggestion AI (Medium)', 'advice': 'edit',
              'keep_label': 'keep it as it is',
              'advice_note': ('Rewrite them in your own words if you want them to read Human: three asks in a row of the '
                              'same shape is what reads AI. Keep the three asks and what "smaller" means.'),
              'found_by': FOUND})
    i162 = tries['S-162']['block']
    k162 = BL[i162]['text'].find('How much of the grown-up you')
    S.append({'id': 'R-162', 'spot': 'S-162', 'type': 'rewrite', 'title': '“How much of the grown-up you …”',
              'where': sr.where(BL, i162), 'spans': [{'block': i162, 'start': k162, 'end': len(BL[i162]['text'])}],
              'edits': [], 'inserts': [], 'moves': [],
              'why': ('Your words (from your inner child guide) read AI (Low, 0.53, a coin toss) at 20:15 UTC ([part A](%s)), '
                      'where they had read High on 29 October. My suggestion, "To find out, try looking around the room, '
                      'pausing before you act, making a choice and following through on it, since those are all things '
                      'your adult self can do.", read AI (High) at 21:40 UTC ([part A](%s)), worse than yours, so I\'ve '
                      'withdrawn it.' % (FEED['20A'], FEED['21A'])),
              'reading': 'AI (Low); my suggestion AI (High)', 'advice': 'edit', 'keep_label': 'keep it as it is',
              'advice_note': ('Your call. Yours read AI only at Low, which moves between checks; mine read worse. Keep it, '
                              'or rewrite it if you want to be sure.'),
              'found_by': FOUND})
    # the words that read AI this time only: one card a stretch (lines two paragraphs or fewer apart)
    lines = []
    for r in reds:
        for ln in locate(r['text']):
            ln.update({'part': r['part'], 'window': r['window'], 'reading': 'AI (%s)' % r['confidence']})
            lines.append(ln)
    taken = {(sp['block']) for s in S for sp in s['spans']}
    lines = [ln for ln in lines if ln['block'] not in taken]
    groups, last = [], None
    for ln in sorted(lines, key=lambda x: (x['block'], x['start'])):
        if last is None or ln['block'] > last + 2 or BL[ln['block']]['section'] != BL[last]['section']:
            groups.append([])
        groups[-1].append(ln)
        last = ln['block']
    for g in groups:
        part = g[0]['part']
        befores = sorted({last_reading(ln['text'])[1] for ln in g},
                         key=lambda r: ['AI (Low)', 'Human (Low)', 'Human (Medium)', 'Human (High)'].index(r)
                         if r in ['AI (Low)', 'Human (Low)', 'Human (Medium)', 'Human (High)'] else 9)
        reads = sorted({ln['reading'] for ln in g}, key=['AI (Low)', 'AI (Medium)', 'AI (High)'].index)
        his = any(BL[ln['block']]['text'].startswith(('"Keep it simple', 'Using metaphors and imagery is your call'))
                  for ln in g)
        S.append({'id': 'N-%d' % g[0]['block'], 'spot': 'red', 'type': 'red', 'title': quote_start(g[0]['text']),
                  'where': sr.where(BL, g[0]['block']),
                  'spans': merged([{'block': ln['block'], 'start': ln['start'], 'end': ln['end']} for ln in g]),
                  'edits': [], 'inserts': [], 'moves': [],
                  'why': ('%s read %s in the recheck of 21:40 UTC ([part %s](%s)). In the recheck of 20:15 UTC they read '
                          '%s ([part %s](%s)), with the same words, and nothing near them changed in between.' % (
                              'Your words' if his else 'These words', say(reads), part, FEED['21' + part], say(befores),
                              part, FEED['20' + part])),
                  'reading': '%s, in the latest recheck only' % say(reads), 'advice': 'edit',
                  'keep_label': 'keep it as it is',
                  'advice_note': ('Your call. They read Human last time with the same words, so they may read Human again '
                                  'next time (last time\'s two AI windows on unchanged words read High this time). If they '
                                  'read AI twice in a row, they get a try or your version.'),
                  'found_by': 'The recheck of 21:40 UTC'})
    for s in S:
        if s.get('approve_label') is None:
            s.pop('approve_label', None)
    S.sort(key=lambda s: (s['spans'][0]['block'], s['spans'][0]['start']))
    n = collections.Counter(s['type'] for s in S)
    review = {
        'format': sr.FORMAT, 'review_id': 'inner-signal-hypnosis-guide-cards-20261030b',
        'title': 'Hypnosis Guide Cards, 30 October',
        'intro': [
            'Your hypnosis guide as it is in Git, with every card from the two rechecks of 30 October (<a href="%s">part '
            'A</a> and <a href="%s">part B</a> of 21:40 UTC).' % (FEED['21A'], FEED['21B']),
            '<b>%d of my tries read Human</b> where they stand, three of them sentences I take back out (one you had cut '
            'yourself on 25 October). Approve, Reject or Revise. <b>One more reads better</b> but not Human yet.'
            % n['passes'],
            '<b>%d suggestions for your own words</b>: four from the last recheck, read in place twice, and the two-hand '
            'exercise named instead of taught again.' % n['yours'],
            '<b>%d places for you to rewrite</b>: words that still read AI after a try. Each card shows the try and how it '
            'read.' % n['rewrite'],
            '<b>%d places that read AI this time only</b>, with nothing changed in or near them. They read Human last time, '
            'so I\'d keep them for now; question 28 on your questions page asks how we call the guide done.' % n['red'],
            'Your answers save as you click. When you\'re done, click <b>Copy my answers</b> (or <b>Save them as a '
            'file</b>) and send them to me.',
        ],
        'git_file': GIT_FILE, 'article': {'file': ARTICLE, 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'links': {'guide': BLOB + ARTICLE, 'review': BLOB + LANE + 'fix-20261030/tries/review/REVIEW-30b.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-30b.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-30b.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-30b.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    (HERE / 'REVIEW-30b.md').write_text(cards_md(review), encoding='utf-8')
    print(len(S), 'cards:', dict(n))


def marked(j, spans):
    t = BL[j]['text']
    for sp in sorted((x for x in spans if x['block'] == j), key=lambda x: -x['start']):
        t = t[:sp['start']] + '**' + t[sp['start']:sp['end']] + '**' + t[sp['end']:]
    return t


def cards_md(review):
    """Every card as a page GitHub renders, in the guide's order (the page's readable copy in Git)."""
    types = review['types']

    def plain(h):
        out = []
        for chunk in h.split('\n\n'):
            first, *rest = chunk.split('\n')
            out.append('\n\n'.join([first] + ['> ' + r for r in rest]))
        return '\n\n'.join(out)
    out = ['# %s: every card' % review['title'], '',
           'The page\'s cards as text, in the order of the guide. Built %s from [the guide so far](%s). To answer, use '
           'the page; or write your answer under a card\'s number in a message to me.' % (
               review['built'], review['links']['guide']), '']
    section = None
    for s in review['suggestions']:
        b = s['spans'][0]['block']
        if BL[b]['section'] != section:
            section = BL[b]['section']
            out += ['## %s' % (section or 'The opening'), '']
        out += ['### %s: %s (%s)' % (s['id'], s['title'], types[s['type']]['label']), '']
        if s['advice'] == 'edit':
            blocks = sorted({sp['block'] for sp in s['spans']})
            out += ['**As it is now** (the words that read AI in bold):', '',
                    '\n>\n'.join('> %s' % marked(j, s['spans']) for j in blocks), '',
                    '**Why it\'s here:** %s' % plain(s['why']), '', '**My advice:** %s' % s['advice_note'], '']
            continue
        for e in s['edits']:
            out += ['**Now** (the words it changes in bold):', '', '> %s' % marked(e['block'], s['spans']), '',
                    '**How it would read:**', '', '> %s' % e['after'], '']
        out += ['**Why:** %s' % plain(s['why']), '', '**My advice:** %s' % s['advice_note'], '']
    return '\n'.join(out).replace('\n\n\n', '\n\n') + '\n'


if __name__ == '__main__':
    main()
