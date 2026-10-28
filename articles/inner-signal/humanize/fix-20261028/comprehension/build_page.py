"""The hypnosis guide's comprehension page of 2026-10-28 (REVIEW-28.json, .html, .artifact.html, .md).

Joel, 2026-10-28 15:20 UTC: "i started on it, but the guide itself is now too incomprehensible, we went wrong somewhere".
The comparative read (AUDIT.md) found where the guide reads worse than his published version, I checked every finding,
fresh writers fixed the ones that are real (fix/), I went through every fix (fix/MY-REVIEW.json) and fresh readers read
each fixed paragraph beside his published one (verify/). This page is the guide with his six answers of 15:19 UTC in
(BASE-ANSWERS.md), each fix highlighted on the words it changes, one card per paragraph, in the marking page's form
(tools/humanization/suggestion_review.py, gate E265); passages in his own words that a reader found hard to follow are
cards for him to keep or edit (advice "edit").

  python3 articles/inner-signal/humanize/fix-20261028/comprehension/build_page.py
"""
import collections
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/'
LANE = 'articles/inner-signal/humanize/'
ARTICLE = LANE + 'HUMANIZED-SO-FAR.md'
GIT_FILE = LANE + 'fix-20261028/comprehension/REVIEW-28.html'
MD = (HERE / 'BASE-ANSWERS.md').read_text(encoding='utf-8')
BL = sr.blocks(MD)
PUB = sr.blocks((H / 'source' / 'published-20260928.md').read_text(encoding='utf-8'))

TYPES = {
    'sense': {'label': "Doesn't read",
              'about': "Words a reader can't follow: a sentence that doesn't parse, a word that doesn't fit, an \"it\" or "
                       "\"this\" with nothing to point to, or a list run together."},
    'lost': {'label': 'Lost or changed',
             'about': 'A point, step or contrast your published version made that this one dropped or changed, so the '
                      'passage now says less, or something else.'},
    'snag': {'label': 'Small snag',
             'about': 'A small thing a reader may trip on: a vaguer word, a lost nuance. A few words fix it.'},
    'his': {'label': 'Your own words',
            'about': 'Words of yours that a reader found hard to follow. Keep them as they are, or edit them.'},
}
FOUND_BY = ('The comparative read of 28 October (fresh readers with your published guide beside this one, sentence by '
            'sentence), my check of every finding, a fresh writer\'s fix, my check of the fix, and a fresh reader of the '
            'fixed paragraph beside yours')
DECIDING = 'Approve uses the new wording; Reject keeps it as it is; Revise lets you write your own.'


def quote_start(t, n=7):
    w = t.split()
    return '“%s%s”' % (' '.join(w[:n]), ' …' if len(w) > n else '')


def main():
    F = {r['id']: r for r in json.loads((HERE / 'FINDINGS.json').read_text(encoding='utf-8'))['findings']}
    V = json.loads((HERE / 'CHECKED.json').read_text(encoding='utf-8'))['verdicts']
    ch = json.loads((HERE / 'CHANGES.json').read_text(encoding='utf-8'))
    assert ch['from']['sha256'] == hashlib.sha256(MD.encode('utf-8')).hexdigest(), 'CHANGES.json is not on BASE-ANSWERS.md'
    advice = json.loads((HERE / 'fix' / 'ADVICE.json').read_text(encoding='utf-8')) \
        if (HERE / 'fix' / 'ADVICE.json').exists() else {}
    by_block = collections.defaultdict(list)
    for c in ch['changes']:
        by_block[c['block']].append(c)
    S = []
    for i in sorted(by_block):
        cs = by_block[i]
        fids = [f for c in cs for f in c['findings']]
        verdicts = [V.get(f, ['not']) for f in fids]
        real = [f for f, v in zip(fids, verdicts) if v[0] == 'real']
        kinds = {F[f]['kind'] for f in real}
        listy = any('\n' in c['with'] for c in cs)
        typ = 'sense' if (listy or kinds & {'garbled', 'unclear'}) else 'lost' if real else 'snag'
        before = BL[i]['text']
        after = cs[-1]['after'].replace('\n', '\n\n') if listy else cs[-1]['after']
        spans = []
        for c in cs:
            a = before.index(c['replace'])
            spans.append({'block': i, 'start': a, 'end': a + len(c['replace'])})
        why = []
        for f, v in zip(fids, verdicts):
            r = F[f]
            line = v[-1][:1].upper() + v[-1][1:]
            pub = r['published'] if r['published'].lower() != 'none' else ''
            why.append(line.rstrip('.') + '.' + (' Your published version: “%s”' % pub.strip('“”" ') if pub else ''))
        hows = {c['how'] for c in cs}
        note = advice.get(str(i)) or ('Approve: it puts your published wording back.' if hows == {'published'} else
                                      'Approve.' if typ != 'snag' else 'Approve: a few words, and it reads more clearly.')
        adv = 'leave' if note.lower().startswith('leave') else 'approve'
        S.append({'id': 'C-%d' % (len(S) + 1), 'type': typ, 'title': quote_start(cs[0]['replace']),
                  'where': sr.where(BL, i), 'spans': spans,
                  'edits': [{'block': i, 'before': before, 'after': after}], 'inserts': [], 'moves': [],
                  'what': '; '.join('“%s” becomes “%s”' % (c['replace'], c['with'].replace('\n', ' / ')) for c in cs) + '.',
                  'why': ' '.join(why), 'stays': 'Everything else in the paragraph, word for word.',
                  'advice': adv, 'advice_note': note, 'found_by': FOUND_BY, 'deciding': DECIDING,
                  'findings': fids})
    # his own words that a reader found hard to follow: his to keep or edit. Not the paragraphs his answers of today
    # rewrote (he has just written them), and one card for a line that is in two places (the second names the first).
    answered = {c['block'] for c in json.loads((HERE / 'CHANGES-ANSWERS.json').read_text(encoding='utf-8'))['changes']}
    same_line = {'F3a.5': 'F6a.27'}
    for f, v in sorted(V.items(), key=lambda kv: (F[kv[0]]['now_blocks'] or [0])[0]):
        if v[0] != 'his' or not F[f]['now_blocks'] or f in same_line:
            continue
        r = F[f]
        i = r['now_blocks'][0]
        if i in answered:
            continue
        t = BL[i]['text']
        q = r['now'].strip()
        a = t.find(q)
        if a < 0:
            continue
        pub = r['published'] if r['published'].lower() != 'none' else ''
        S.append({'id': 'C-%d' % (len(S) + 1), 'type': 'his', 'title': quote_start(q), 'where': sr.where(BL, i),
                  'spans': [{'block': i, 'start': a, 'end': a + len(q)}], 'edits': [], 'inserts': [], 'moves': [],
                  'why': v[-1][:1].upper() + v[-1][1:].rstrip('.') + '.' +
                  (' Your published version: “%s”' % pub.strip('“”" ') if pub else ''),
                  'advice': 'edit', 'keep_label': 'keep it as it is',
                  'advice_note': advice.get('his-' + f, 'Your call: keep it if it says what you mean.'),
                  'findings': [f] + [g for g, h in same_line.items() if h == f]})
    S.sort(key=lambda s: (s['spans'][0]['block'], s['spans'][0]['start']))
    for n, s in enumerate(S, 1):
        s['id'] = 'C-%d' % n
    n = collections.Counter(s['type'] for s in S)
    # the fix check (verify/): every fixed paragraph read beside his published one; a paragraph read by two readers had
    # its fix redone after the first one failed it
    vres = json.loads((HERE / 'verify' / 'VERIFY.json').read_text(encoding='utf-8'))
    vparts = json.loads((HERE / 'verify' / 'VERIFY-PARTS.json').read_text(encoding='utf-8'))
    seen = collections.Counter(i for m in vparts for i in m['paragraphs'])
    fixed_blocks = {s['spans'][0]['block'] for s in S if s['advice'] != 'edit'}
    assert not vres['failed'] and not vres['readers_missing'], 'the fix check is not finished or a fix failed it'
    assert fixed_blocks <= {int(i) for i in vres['results']}, 'a fixed paragraph was not read'
    redone = sum(1 for i in fixed_blocks if seen[i] > 1)
    review = {
        'format': sr.FORMAT, 'review_id': 'inner-signal-hypnosis-guide-comprehension-20261028',
        'title': 'Hypnosis Guide Fixes',
        'intro': [
            'This is your hypnosis guide as it is in Git now, with your six answers of today in, and every fix of the '
            'comprehension check highlighted where it is. Fresh readers went through the whole guide beside your '
            'published version, sentence by sentence, and wrote down every place this one reads worse; I checked each '
            '(<a href="%s">the audit</a>).' % (BLOB + LANE + 'fix-20261028/comprehension/AUDIT.md'),
            '<b>%d fixes</b>, one card per paragraph: %d where a sentence doesn\'t read, %d where a point was lost or '
            'changed, %d small snags. Each fix changes only the words highlighted. Click <b>Approve</b>, <b>Reject</b> '
            'or <b>Revise</b>.' % (n['sense'] + n['lost'] + n['snag'], n['sense'], n['lost'], n['snag']),
            'Fresh writers made the fixes, from your published wording where it fit, and I went through every one. '
            'Then a fresh reader read each fixed paragraph beside your published version: does it read clearly, does '
            'it say what yours says, and is it at least as easy to follow as before? All %d passed (%d after a second fix).'
            % (len(fixed_blocks), redone),
            '<b>Your own words</b> (%d cards): places in text you wrote where a reader stumbled. <b>Keep</b> or '
            '<b>Edit it</b>.' % n['his'],
            'None of these has been through Pangram yet: after your answers, the whole guide gets one recheck, and any '
            'fix that reads AI or below High comes back to you with the clearest version that passes.',
            'Your answers save as you click. When you\'re done, click <b>Copy my answers</b> (or <b>Save them as a '
            'file</b>) and send them to me.',
        ],
        'git_file': GIT_FILE, 'article': {'file': ARTICLE, 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'links': {'guide': BLOB + ARTICLE, 'review': BLOB + LANE + 'fix-20261028/comprehension/REVIEW-28.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-28.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-28.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-28.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    (HERE / 'REVIEW-28.md').write_text(cards_md(review), encoding='utf-8')
    print(len(S), 'cards:', dict(n))


def cards_md(review):
    """Every card as a page GitHub renders, in the guide's order (the page's readable copy in Git)."""
    types = review['types']
    out = ['# %s: every card' % review['title'], '',
           'The fix page\'s cards as text, in the order of the guide (`REVIEW-28.json` holds the same, for the scripts). '
           'Built %s from [the guide so far](%s). To answer, use the page; or write your answer under a card\'s number '
           'in a message to me.' % (review['built'], review['links']['guide']), '']
    section = None
    for s in review['suggestions']:
        b = s['spans'][0]['block']
        if BL[b]['section'] != section:
            section = BL[b]['section']
            out += ['## %s' % (section or 'The opening'), '']
        out += ['### %s: %s (%s)' % (s['id'], s['title'], types[s['type']]['label']), '']
        if s['advice'] == 'edit':
            out += ['**As it is now:**', '', '> %s' % BL[b]['text'], '', '**Why it\'s here:** %s' % s['why'], '',
                    '**My advice:** %s' % s['advice_note'], '']
            continue
        for e in s['edits']:
            out += ['**Now:**', '', '> %s' % e['before'], '', '**How it would read:**', '']
            out += ['> %s' % ln if ln.strip() else '>' for ln in e['after'].split('\n')] + ['']
        out += ['**Why:** %s' % s['why'], '', '**My advice:** %s' % s['advice_note'], '']
    return '\n'.join(out).replace('\n\n\n', '\n\n') + '\n'


if __name__ == '__main__':
    main()
