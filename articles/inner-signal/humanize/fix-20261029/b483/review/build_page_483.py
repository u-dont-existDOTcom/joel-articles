"""The hypnosis guide's cards of 2026-10-29 22:30 UTC (REVIEW-483.json, .html, .artifact.html, .md).

Joel, 2026-10-29 22:23 UTC, with batch 483's recheck links: "ok give me the cards i'll fix everything and then you can
learn". So one page, his guide as it is in Git (HUMANIZED-SO-FAR.md), in the marking page's form
(tools/humanization/suggestion_review.py, gate E265):
- every new version that read Human in place in batch 483's recheck, in place of words that read AI: ours to approve,
  and suggestions for lines of his own beside his words ("use this wording");
- every stretch that still reads AI after the writers' two tries (batch 482 without Emulate, batch 483 with the shape rules
  from Emulate's fixes), and his audit, as a stretch to edit (advice "edit"): the card shows what was tried and how it
  read. His versions are what the next lessons come from (his "then you can learn").

  python3 articles/inner-signal/humanize/fix-20261029/b483/review/build_page_483.py
"""
import collections
import datetime
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
B = HERE.parent
H = B.parents[1]
ROOT = H.parents[2]
P482 = B.parent / 'b482'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/'
LANE = 'articles/inner-signal/humanize/'
ARTICLE = LANE + 'HUMANIZED-SO-FAR.md'
GIT_FILE = LANE + 'fix-20261029/b483/review/REVIEW-483.html'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
BL = sr.blocks(MD)
FEED = {'483A': 'https://www.pangram.com/feed/d7900092-2691-46bd-b76a-d2043526509c',
        '483B': 'https://www.pangram.com/feed/845b60a9-9b58-4824-bc34-29cb1e395efa',
        '482A': 'https://www.pangram.com/feed/19fba559-fe64-46a3-92a1-ab87f728b4ba',
        '482B': 'https://www.pangram.com/feed/82470746-1d28-4ddc-ac19-276ca31c19f2',
        '29A': 'https://www.pangram.com/feed/d1e283a5-efcf-4fc4-ad6f-d535e12951b2',
        '29B': 'https://www.pangram.com/feed/f9b45a7b-402c-412c-af68-a5f9ca44f6e6'}
AUDIT = (605, 613)   # "Before accepting a recording or live suggestion, ask:" to "... change the method, or leave."

TYPES = {
    'passes': {'label': 'Reads Human now',
               'about': 'A new version that read Human where it stands in the latest recheck, in place of words that '
                        'read AI. Approve, Reject or Revise.'},
    'yours': {'label': 'Your own words',
              'about': 'A line of yours that read AI, and a suggestion that read Human in its place. Approve uses the '
                       'suggestion; Reject keeps your words; Revise lets you write your own.'},
    'rewrite': {'label': 'For you to rewrite',
                'about': 'Words that still read AI after the writers tried twice (both tries are on the card). Keep '
                         'them, or edit them in your own words.'},
    'red': {'label': 'Reads AI, not tried yet',
            'about': 'Words that read AI in the latest recheck that nobody has tried a new version of yet. Keep them, or '
                     'edit them in your own words.'},
}
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})
FOUND = ('The recheck of 29 October 18:18 UTC read these words AI; fresh writers made new versions (batch 482, then batch '
         '483 with the lessons from Emulate\'s fixes), each read beside your published version, then rechecked in place')


def quote_start(t, n=7):
    w = t.strip('“”"').split()
    return '“%s%s”' % (' '.join(w[:n]), ' …' if len(w) > n else '')


def windows_read(rs):
    """'AI (Low), window 56 of part B', 'AI (High), window 57 of part B' -> 'AI (Low) in window 56 and AI (High) in window
    57'; 'AI (Low)' in windows 86, 87 and 88 -> 'AI (Low) in windows 86, 87 and 88' (the part is in the link beside it)."""
    by = collections.OrderedDict()
    for r in rs:
        m = re.match(r'(AI \(\w+\)), window (\d+) of part [AB]', r)
        if m.group(2) not in by.setdefault(m.group(1), []):
            by[m.group(1)].append(m.group(2))
    say = lambda ws: ('window ' + ws[0]) if len(ws) == 1 else 'windows %s and %s' % (', '.join(ws[:-1]), ws[-1])
    parts = ['%s in %s' % (k, say(v)) for k, v in by.items()]
    return ('; ' if len(parts) > 2 else ' and ').join(parts)


def say(xs):
    return (', '.join(xs[:-1]) + ' and ' + xs[-1]) if len(xs) > 1 else xs[0]


def cap(t):
    return t[:1].upper() + t[1:]


def red_elsewhere():
    """Each line of a window that read AI in the latest recheck on words nobody has tried a new version of (SPOTS.json
    "red_elsewhere", less the audit, which has its own card), placed on the working copy: block, start, end, its window's
    number and reading (CONFIDENCE.json), and whether it read AI in batch 482's recheck too."""
    rd = B / 'recheck' / 'read'
    rows = {k[-6]: v['rows'] for k, v in json.loads((rd / 'CONFIDENCE.json').read_text(encoding='utf-8')).items()}
    out = []
    for r in json.loads((rd / 'SPOTS.json').read_text(encoding='utf-8'))['red_elsewhere']:
        if r['text'].startswith('Before accepting a recording'):
            continue
        w = [x for x in rows[r['part']] if x['text'].strip() == r['text'].strip()]
        assert len(w) == 1, r['text'][:60]
        lines = [x.strip() for x in r['text'].split('\n') if x.strip()]
        hits = [[b['i'] for b in BL if ln.translate(FLAT) in b['text'].translate(FLAT)] for ln in lines]
        anchors = [h[0] for h in hits if len(h) == 1]
        assert all(hits) and anchors, r['text'][:60]
        for ln, h in zip(lines, hits):
            i = min(h, key=lambda j: min(abs(j - a) for a in anchors))
            k = BL[i]['text'].translate(FLAT).find(ln.translate(FLAT))
            z = k + len(ln)
            # a window that starts inside a quotation: the highlight starts where the sentence holding the quotation does
            t, ft = BL[i]['text'], BL[i]['text'].translate(FLAT)
            if ft.count('"', 0, k) % 2:
                q = ft.rfind('"', 0, k)
                k = max([ft.rfind(e, 0, q) + 2 for e in ('. ', '? ', '! ')] + [0])
            ln = t[k:z]
            out.append({'block': i, 'start': k, 'end': z, 'text': ln,
                        'part': r['part'], 'window': w[0]['window'], 'reading': r['reading'],
                        'last': bool(r['red_last_time'])})
    return out


def merged(spans):
    """A card's highlights in the guide's order, with those that overlap or touch (a space apart) made one."""
    out = []
    for sp in sorted(spans, key=lambda x: (x['block'], x['start'])):
        if out and out[-1]['block'] == sp['block'] and sp['start'] <= out[-1]['end'] + 1:
            out[-1]['end'] = max(out[-1]['end'], sp['end'])
        else:
            out.append(dict(sp))
    return out


def first_check(part):
    return 'the check of 29 October 18:18 UTC ([part %s](%s))' % (part, FEED['29' + part])


def span_of(i, stretch):
    t = BL[i]['text']
    k = t.find(stretch)
    assert k >= 0 and t.count(stretch) == 1, (i, stretch[:60])
    return {'block': i, 'start': k, 'end': k + len(stretch)}


def main():
    cands = {s['id']: s for s in json.loads((B / 'CANDIDATES.json').read_text(encoding='utf-8'))['spots']}
    spots = {s['id']: s for s in json.loads((B / 'recheck' / 'read' / 'SPOTS.json').read_text(encoding='utf-8'))['spots']}
    t483 = {t['id']: t for t in json.loads((B / 'TARGETS.json').read_text(encoding='utf-8'))['items']}
    t482 = {t['id']: t for t in json.loads((P482 / 'TARGETS.json').read_text(encoding='utf-8'))['items']}
    last482 = {x['id']: x['now'] for x in
               json.loads((P482 / 'recheck' / 'read' / 'SPOTS.json').read_text(encoding='utf-8'))['spots']}
    S = []
    # the versions that read Human: ours to approve, his lines with a suggestion
    for sid, sp in spots.items():
        if not sp.get('human'):
            continue
        c = cands[sid]
        i = c['block']
        assert BL[i]['text'] == c['paragraph_before'], sid
        his = sid.startswith('J')
        part = sp['part']
        if sid == 'J5':
            before = ('Your line read AI (Low) in window 5 in %s, and again in batch 482\'s recheck (19:22 UTC, [part '
                      'A](%s)).' % (first_check('A'), FEED['482A']))
        else:
            before = '%s read %s in %s.' % ('Your line' if his else 'The words it replaces',
                                            windows_read(c['readings']), first_check(part))
        if c['batch'] == 482:
            now = ('read %s where it stands in batch 482\'s recheck (19:22 UTC, [part %s](%s)) and %s in the latest '
                   '(22:23 UTC, [part %s](%s))' % (last482[sid], part, FEED['482' + part], sp['now'], part,
                                                   FEED['483' + part]))
        else:
            now = ('read %s where it stands in the latest recheck (22:23 UTC, [part %s](%s))'
                   % (sp['now'], part, FEED['483' + part]))
        why = ('%s This %s %s. A fresh reader read it beside %s and your published version: it reads clearly and keeps '
               'every point.' % (before, 'suggestion' if his else 'version', now,
                                 'your line' if his else 'the words it replaces'))
        low = sp['now'] in ('Human (Low)', 'Human (Medium)')
        note = ('Your call. I\'d use it: it keeps your words where it can and reads Human.' if his else
                'Approve: it reads Human where it stands and keeps every point.')
        if low:
            note += ' It read Human at %s confidence, so it may want another light pass later.' % sp['now'][7:-1]
        S.append({'id': sid, 'spot': sid, 'type': 'yours' if his else 'passes', 'title': quote_start(c['new']),
                  'where': sr.where(BL, i), 'spans': [span_of(i, c['old'])],
                  'edits': [{'block': i, 'before': BL[i]['text'], 'after': c['paragraph_after']}], 'inserts': [],
                  'moves': [], 'what': '“%s” becomes “%s”' % (c['old'].rstrip(), c['new'].rstrip()),
                  'why': why, 'stays': 'The rest of the paragraph, word for word.', 'advice': 'approve',
                  'advice_note': note, 'found_by': FOUND,
                  'deciding': ('Approve uses this wording; Reject keeps yours; Revise lets you write your own.' if his
                               else 'Approve uses the new wording; Reject keeps it as it is; Revise lets you write your own.'),
                  'approve_label': 'use this wording' if his else None})
    # what still reads AI: one card a paragraph, for him to keep or rewrite
    groups = collections.OrderedDict()
    for sid, sp in spots.items():
        if sp.get('human'):
            continue
        groups.setdefault(cands[sid]['block'], []).append(sid)
    red_lines = red_elsewhere()
    for i, ids in sorted(groups.items()):
        spans, readings, part, said = [], [], None, []
        order = sorted(ids, key=lambda x: BL[i]['text'].find(t483[x]['flagged_stretch']))
        try1, try2, read1, read2 = BL[i]['text'], BL[i]['text'], [], []
        for sid in order:
            t3 = t483[sid]
            part = spots[sid]['part']
            whose_ = 'your line' if sid.startswith('J') else 'our words'
            spans.append(span_of(i, t3['flagged_stretch']))
            readings += t3['readings_before']
            said.append('%s %s' % (whose_ + ' read' if not said else whose_, windows_read(t3['readings_before'])))
            assert cands[sid]['old'] == t3['flagged_stretch'], sid
            try1 = try1.replace(t3['flagged_stretch'], t3['last_try']['version'], 1)
            try2 = try2.replace(t3['flagged_stretch'], cands[sid]['new'], 1)
            read1.append('%s %s' % (whose_, t3['last_try']['read_in_place']))
            read2.append('%s %s' % (whose_, spots[sid]['now']))
        both = len(order) > 1
        why = ('%s in %s.\n\nTry 1 (fresh writers, without Emulate) read AI where it stood in batch 482\'s recheck (19:22 '
               'UTC, [part %s](%s)): %s. The paragraph as it read then:\n%s\n\nTry 2 (fresh writers with the lessons '
               'from Emulate\'s fixes) read AI too, in the latest recheck (22:23 UTC, [part %s](%s)): %s. The paragraph '
               'as it read then:\n%s' % (
                   cap(', and '.join(said)) + (',' if both else ''), first_check(part), part, FEED['482' + part],
                   say(read1) if both else read1[0].split(' ', 2)[-1], try1,
                   part, FEED['483' + part], say(read2) if both else read2[0].split(' ', 2)[-1], try2))
        confs = sorted({re.match(r'AI \((\w+)\)', r).group(1) for r in readings}, key=['Low', 'Medium', 'High'].index)
        reading = 'AI (%s), in the check of 29 October 18:18 UTC' % say(confs)
        also = [ln for ln in red_lines if ln['block'] == i]
        if also:
            red_lines = [ln for ln in red_lines if ln['block'] != i]
            spans += [{'block': i, 'start': ln['start'], 'end': ln['end']} for ln in also]
            why += ('\n\nAlso AI in the latest recheck (22:23 UTC, [part %s](%s)), on words of this paragraph nobody has '
                    'tried a new version of: %s.' % (part, FEED['483' + part], '; '.join(
                        '“%s” (%s in window %d%s)' % (ln['text'], ln['reading'], ln['window'],
                                                      ', and in batch 482\'s recheck too' if ln['last'] else '')
                        for ln in also)))
            reading += '; the other highlighted words %s in the latest recheck' % say(sorted(
                {ln['reading'] for ln in also}, key=['AI (Low)', 'AI (Medium)', 'AI (High)'].index))
        spans = merged(spans)
        S.append({'id': 'R-%d' % i, 'spot': ','.join(ids), 'type': 'rewrite', 'title': quote_start(BL[i]['text']),
                  'where': sr.where(BL, i), 'spans': spans, 'edits': [], 'inserts': [], 'moves': [], 'why': why,
                  'reading': reading, 'advice': 'edit', 'keep_label': 'keep it as it is',
                  'advice_note': ('Rewrite it in your own words if you want it to read Human. Keep every point the '
                                  'highlighted words make. Your version is what I learn from: I\'ll set it beside both '
                                  'tries and write down what yours does that theirs didn\'t.'),
                  'found_by': FOUND})
    # the rest of what read AI in the latest recheck on words nobody has tried a new version of: a card for each stretch of
    # the guide (lines two or fewer paragraphs apart go together), for him to keep or rewrite ("i'll fix everything")
    groups_, last_block = [], None
    for ln in sorted(red_lines, key=lambda x: (x['block'], x['start'])):
        if last_block is None or ln['block'] > last_block + 2:
            groups_.append([])
        groups_[-1].append(ln)
        last_block = ln['block']
    for g in groups_:
        part = g[0]['part']
        old = [ln for ln in g if ln['last']]
        reads = windows_read(['%s, window %d of part %s' % (ln['reading'], ln['window'], part) for ln in g])
        if len(old) == len(g):
            since = 'They read AI in batch 482\'s recheck too (19:22 UTC, [part %s](%s)).' % (part, FEED['482' + part])
            note = ('Rewrite them in your own words if you want them to read Human. Keep every point the highlighted '
                    'words make. Your version is what I learn from.')
        elif not old:
            since = ('They read Human in batch 482\'s recheck (19:22 UTC, [part %s](%s)), and they haven\'t changed: the '
                     'only change since was the writers\' new versions elsewhere in the guide.' % (part, FEED['482' + part]))
            note = ('Your call. They read Human the time before with the same words, so they may read Human again once '
                    'the cards near them are settled. Rewrite them if you want to be sure; your version is what I learn '
                    'from.')
        else:
            since = ('%s read AI in batch 482\'s recheck too (19:22 UTC, [part %s](%s)). The rest read Human there, and '
                     'they haven\'t changed: the only change since was the writers\' new versions elsewhere in the guide.'
                     % (' and '.join('“%s”' % ln['text'] for ln in old), part, FEED['482' + part]))
            note = ('Rewrite them in your own words if you want them to read Human. Keep every point the highlighted '
                    'words make. Your version is what I learn from.')
        confs = sorted({ln['reading'] for ln in g}, key=['AI (Low)', 'AI (Medium)', 'AI (High)'].index)
        S.append({'id': 'N-%d' % g[0]['block'], 'spot': 'red', 'type': 'red', 'title': quote_start(g[0]['text']),
                  'where': sr.where(BL, g[0]['block']),
                  'spans': merged([{'block': ln['block'], 'start': ln['start'], 'end': ln['end']} for ln in g]),
                  'edits': [], 'inserts': [], 'moves': [],
                  'why': ('These words read %s in the latest recheck (22:23 UTC, [part %s](%s)). %s Nobody has tried a new '
                          'version of them yet.' % (reads, part, FEED['483' + part], since)),
                  'reading': 'AI (%s), in the latest recheck' % say([c[4:-1] for c in confs]),
                  'advice': 'edit', 'keep_label': 'keep it as it is', 'advice_note': note,
                  'found_by': 'The latest recheck (22:23 UTC)'})
    # his audit, kept as a list by his answer 2c
    a, z = AUDIT
    assert BL[a]['text'].startswith('Before accepting a recording') and BL[z]['text'].endswith('change the method, or leave.')
    S.append({'id': 'R-audit', 'spot': 'audit', 'type': 'rewrite', 'title': '“Before accepting a recording or live suggestion …”',
              'where': sr.where(BL, a), 'spans': [{'block': j, 'start': 0, 'end': len(BL[j]['text'])} for j in range(a, z + 1)],
              'edits': [], 'inserts': [], 'moves': [],
              'why': ('Your list, kept as a list by your answer 2c. It has read AI (High, 120 words) in every check since '
                      'recheck B2, the latest ([part B](%s)) too. Nobody has tried a version of it since your '
                      'answer.' % FEED['483B']),
              'reading': 'AI (High), 120 words', 'advice': 'edit', 'keep_label': 'keep it as it is',
              'advice_note': ('Your call: keep it as your list, or rewrite it if you want it to read Human. The one '
                              'list-like passage that has read Human is your own rewrite of Appendix C (parallel tests with '
                              'different verbs and lengths, the last long and personal).'),
              'found_by': 'Every whole-guide recheck since recheck B2'})
    for s in S:
        if s.get('approve_label') is None:
            s.pop('approve_label', None)
    S.sort(key=lambda s: (s['spans'][0]['block'], s['spans'][0]['start']))
    n = collections.Counter(s['type'] for s in S)
    review = {
        'format': sr.FORMAT, 'review_id': 'inner-signal-hypnosis-guide-cards-20261029',
        'title': 'Hypnosis Guide Cards',
        'intro': [
            'Your hypnosis guide as it is in Git, with every card from the last two rechecks, as you asked at 22:23 UTC '
            '("give me the cards i\'ll fix everything and then you can learn").',
            '<b>%d new versions that read Human</b> where they stand in the latest recheck (<a href="%s">part A</a>, <a '
            'href="%s">part B</a>), in place of words that read AI: %d of ours, and %d suggestions for lines of yours. '
            'Approve, Reject or Revise.' % (n['passes'] + n['yours'], FEED['483A'], FEED['483B'], n['passes'], n['yours']),
            '<b>%d places for you to rewrite</b>: words that still read AI after the writers tried twice, once without '
            'Emulate and once with the lessons from Emulate\'s fixes. Each card shows both tries and how they read. Keep '
            'it, or Edit it in your own words. One of them is your audit list.' % n['rewrite'],
            '<b>%d more places that read AI</b> in the latest recheck, on words nobody has tried a new version of yet: '
            'some read AI the time before too, some only this time. Keep them, or Edit them in your own words.' % n['red'],
            'Every new version here was read beside your published version first: each reads clearly and says what '
            'yours says. Your own versions get the same read, then the recheck; after that I set each one beside what '
            'the writers tried and write down what yours does that theirs didn\'t.',
            'Your answers save as you click. When you\'re done, click <b>Copy my answers</b> (or <b>Save them as a '
            'file</b>) and send them to me.',
        ],
        'git_file': GIT_FILE, 'article': {'file': ARTICLE, 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'links': {'guide': BLOB + ARTICLE, 'review': BLOB + LANE + 'fix-20261029/b483/review/REVIEW-483.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-483.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-483.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-483.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    (HERE / 'REVIEW-483.md').write_text(cards_md(review), encoding='utf-8')
    print(len(S), 'cards:', dict(n))


def marked(j, spans):
    """Block J's text with the card's highlights in bold (the page's highlights, on GitHub)."""
    t = BL[j]['text']
    for sp in sorted((x for x in spans if x['block'] == j), key=lambda x: -x['start']):
        t = t[:sp['start']] + '**' + t[sp['start']:sp['end']] + '**' + t[sp['end']:]
    return t


def cards_md(review):
    """Every card as a page GitHub renders, in the guide's order (the page's readable copy in Git)."""
    import re
    types = review['types']
    def plain(h):
        # a card's text: paragraphs split by a blank line; a line after a paragraph's first is the guide's paragraph as
        # a try read, quoted
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
            out += ['**Now** (the words it replaces in bold):', '', '> %s' % marked(e['block'], s['spans']), '',
                    '**How it would read:**', '', '> %s' % e['after'], '']
        out += ['**Why:** %s' % plain(s['why']), '', '**My advice:** %s' % s['advice_note'], '']
    return '\n'.join(out).replace('\n\n\n', '\n\n') + '\n'


if __name__ == '__main__':
    main()
