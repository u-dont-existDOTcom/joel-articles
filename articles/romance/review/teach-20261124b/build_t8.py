#!/usr/bin/env python3
"""The eighth marking page (2026-11-24): the whole fixed article (whole/FIXED.md) with the junk pass's fixes that might
change the meaning (r38/junk/CARDS-T8.json), each tested in its section, and two passages whose meaning is his to say.
The fixes that keep the meaning went in without a card (r38/junk/MINE-R38J.json).

  python3 build_t8.py   ->  REVIEW-T8.json, REVIEW-T8.html, REVIEW-T8.artifact.html, REVIEW-T8.md
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as R  # noqa: E402

FIX = 'articles/romance/humanize/fix-20261107'
ART = FIX + '/whole/FIXED.md'
md = (ROOT / ART).read_text(encoding='utf-8')
sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
bl = R.blocks(md, whole=True)
CHANGES = json.loads((ROOT / FIX / 'r38' / 'junk' / 'CARDS-T8.json').read_text(encoding='utf-8'))
RECEIPTS = json.loads((ROOT / FIX / 'r38' / 'junk' / 'para' / 'INDEX.json').read_text(encoding='utf-8'))
H = 'https://www.pangram.com/history/'


def find_block(text):
    hits = [b['i'] for b in bl if b['kind'] not in ('embed', 'cut') and R.block_text(bl, b['i']) == text]
    if len(hits) != 1:
        import re
        plain = lambda t: re.sub(r'\[([^\]]+)\]\((?:[^()\s]|\([^()\s]*\))+\)', r'\1', t)
        hits = [b['i'] for b in bl if b['kind'] not in ('embed', 'cut') and plain(b['text']) == text]
    assert len(hits) == 1, (text[:60], hits)
    return hits[0]


def find_words(words):
    hits = [(b['i'], b['text'].find(words)) for b in bl if b['kind'] not in ('embed', 'cut') and words in b['text']]
    assert len(hits) == 1, (words[:60], hits)
    i, s = hits[0]
    return {'block': i, 'start': s, 'end': s + len(words)}


FOUND = 'the junk read of 2026-11-22 (four fresh readers) and its vetting by a fifth (r30/junk/VETTED.md, %s)'
CARDS = {
    'J-B54': dict(
        title='What “It depends” on', items='B50, B54',
        highlight=['People don’t only trigger each other and learn lessons. Sometimes they terrorize or kill each other.',
                   'It depends what each of you are ready for and have the resources for.'],
        what='“It depends what each of you are ready for” says what depends on it: “Whether you should be in one depends on '
             'what you and the other person are ready for and have the resources for.” And the two short lines before, '
             '“People don’t only trigger each other and learn lessons. Sometimes they terrorize or kill each other.”, '
             'become one sentence: “People trigger each other and learn lessons, and sometimes they terrorize or kill each '
             'other.”',
        why='A reader couldn’t tell what “It” was, and “each of you” came from nowhere (B54); the two short lines read as a '
            'model’s punch close (B50).',
        stays='The catch-22, your advice to friends, the self-love problem and the video.',
        deciding='whether “It” was the heading’s question, whether you should be in a relationship at all',
        ask_because='meaning: I read “It” as the heading’s question; if you meant whether a relationship can teach you '
                    'self-love, the new sentence says something else',
        advice_note='My pick: use it, if “It” is the heading’s question.',
        reading='The section as it is: Human High in every window (%sef127915-359a-42b1-a576-06217eef8f79).' % H,
        tested='The section with these changes: Human High in every window (%s14dd222c-80ab-4081-8c71-22c7f7b8ef8a).' % H),
    'J-B217': dict(
        title='“The seed of its own destruction”', items='B217',
        highlight=['That little paradise is wonderful, but it contains the seed of its own destruction. Part of why it feels'],
        what='The line “That little paradise is wonderful, but it contains the seed of its own destruction.” goes, and the '
             'next sentence names the paradise: “Part of why that little paradise feels like a magical wonderland is ...”.',
        why='A reader read the line as a model’s aphorism (B217); the paragraph after it shows how the paradise undoes '
            'itself (you stop parenting yourself, go soft, and end up blaming them).',
        stays='The heroin joke, the practices, and “Otherwise, you’ll end up blaming them when you feel bad.”',
        deciding='whether the paragraph still says the paradise undoes itself without the line that says so',
        ask_because='meaning: the paragraph loses the line that says the paradise undoes itself; the rest shows how',
        advice_note='My pick: use it. The section reads Human High with it.',
        reading='The section as it is: Human High in every window (%sb0e21840-e26e-47d0-b7e5-3a021edebaa6).' % H,
        tested='The section with this change: Human High in every window (%s48f4f1be-52c4-4b12-bfcc-fd3a822766a4).' % H),
    'J-B255': dict(
        title='“Where I wasn’t seeing people”', items='B255',
        highlight=['show me where I was missing people'],
        what='“show me where I was missing people” becomes “show me where I wasn’t seeing people”.',
        why='A reader could take “missing people” as longing for them, next to “missing their hidden motives” in the same '
            'sentence (B255).',
        stays='Everything else in the paragraph.',
        deciding='whether “missing people” meant not seeing them clearly',
        ask_because='meaning: “missing people” could mean longing for them; I read it as not seeing them',
        advice_note='My pick: use it, if that is what you meant.',
        reading='The section as it is: Human High in every window (%s8d39d55d-de90-469c-8300-7ab12604de33).' % H,
        tested='The section with this change: Human High in every window (%sd76c7885-a0df-4467-ab2e-66c7100182cc).' % H),
}
ASKS = [
    {'id': 'Q-B476', 'title': 'A relationship like what?', 'words': 'A relationship like this is rare',
     'question': '“Tough Love” opens its second paragraph: “A relationship like this is rare, and that’s probably why romantic '
                 'love has been seen with suspicion as a destabilizing force throughout history.” A reader couldn’t tell what '
                 '“like this” points back to, since the paragraph before is about love not being marketable. What kind of '
                 'relationship do you mean? My guess: a romance that actually works. If that is it, it could say “A romance '
                 'that actually works is rare”, and I’ll test it in its section.',
     'why': 'The vetted junk read, B476: “A relationship like this” has nothing before it to point to.',
     'advice_note': 'A line on what “like this” means is enough.'},
    {'id': 'Q-B478', 'title': 'Reminiscent of Somé how?', 'words': 'Also reminiscent of Somé, they also wore rose-colored glasses',
     'question': '“Also reminiscent of Somé, they also wore rose-colored glasses and taught me that everybody was basically '
                 'good.” A reader couldn’t see what in Somé this recalls: the section says her people distrust romance and '
                 'that the relationship is bigger than the egos in it, not that she saw everybody as good. What is the link? '
                 'If you don’t need it, it could say “They also wore rose-colored glasses and taught me that everybody was '
                 'basically good.”',
     'why': 'The vetted junk read, B478: the Somé link isn’t explained, and “also” comes twice.',
     'advice_note': 'A line on the link is enough; I’ll fix it from your answer and test it.'},
]
review = {
    'format': R.FORMAT, 'review_id': 'romance-t8', 'built': '2026-11-24',
    'title': 'Romance Advice I Wish My Parents Taught Me: the passages that didn’t quite make sense',
    'intro': ['The whole article as it reads now. Of the passages the readers found partly real, 21 still stood, and I fixed '
              'them the way your sixth-page versions did: only the flagged words, with words the passage already has, and '
              'nothing added. Every section with a fix read Human High in every window, each checked by itself. 14 fixes '
              'keep the meaning and are in; three might change it and are the cards below; two need a line from you on '
              'what they mean. Every section of the article now reads Human High in every window. Every paragraph, picture '
              'and video is here in order: nothing is left out.'],
    'git_file': 'articles/romance/review/teach-20261124b/REVIEW-T8.html',
    'article': {'file': ART, 'sha256': sha}, 'whole': {'file': ART, 'sha256': sha},
    'links': {'guide': 'https://ibogaqueen.substack.com/p/romance-advice-i-wish-my-parents', 'guide_label': 'your live post',
              'review': 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/romance-20261108/articles/romance/review/teach-20261124b/REVIEW-T8.md'},
    'types': {'sense': {'label': 'Didn’t make sense or follow', 'about': 'a reader flagged it; my fix, tested in its section'},
              'meaning': {'label': 'What do you mean?', 'about': 'a reader couldn’t tell what it points to; a line from you is enough'}},
    'suggestions': [],
}
order = []
for cid, spec in CARDS.items():
    chs = CHANGES[cid]
    blocks = [find_block(ch['before']) for ch in chs]
    order.append((min(blocks), cid, spec, chs, blocks))
for _, cid, spec, chs, blocks in sorted(order):
    edits = [{'block': i, 'before': R.block_text(bl, i), 'after': ch['after'][0]} for i, ch in zip(blocks, chs)]
    spans = []
    for w in spec['highlight']:
        hit = [i for i in blocks if w in bl[i]['text']]
        assert len(hit) == 1, (cid, w)
        t = bl[hit[0]]['text']
        s = t.find(w)
        spans.append({'block': hit[0], 'start': s, 'end': s + len(w)})
    review['suggestions'].append({
        'id': cid, 'type': 'sense', 'title': spec['title'], 'advice': 'approve', 'spans': spans, 'edits': edits,
        'what': spec['what'], 'why': spec['why'], 'stays': spec['stays'], 'deciding': spec['deciding'],
        'advice_note': spec['advice_note'], 'found_by': FOUND % spec['items'], 'reading': spec['reading'],
        'tested': spec['tested'], 'ask_because': spec['ask_because'], 'receipt': RECEIPTS[cid]})
for a in ASKS:
    review['suggestions'].append({'id': a['id'], 'type': 'meaning', 'title': a['title'], 'advice': 'ask',
                                  'question': a['question'], 'why': a['why'], 'stays': 'The sentence as it is, until your answer.',
                                  'advice_note': a['advice_note'], 'spans': [find_words(a['words'])]})
probs = R.check(review, bl)
if probs:
    sys.exit('\n'.join(probs))
(HERE / 'REVIEW-T8.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
html = R.page(review, md, bl)
(HERE / 'REVIEW-T8.html').write_text(html, encoding='utf-8')
(HERE / 'REVIEW-T8.artifact.html').write_text(R.artifact_view(html), encoding='utf-8')
out = ['# The passages that didn’t quite make sense: the cards (2026-11-24)', '',
       'The page shows the whole article ([FIXED.md](../../humanize/fix-20261107/whole/FIXED.md)); these are its cards.', '']
for s in review['suggestions']:
    out += ['## %s. %s' % (s['id'], s['title']), '']
    if s['advice'] == 'ask':
        out += [s['question'], '', s['why'], '', '**' + s['advice_note'] + '**', '']
        continue
    out += ['**Now:**', ''] + ['> ' + e['before'] for e in s['edits']] + ['']
    out += ['**Would read:**', ''] + ['> ' + (e['after'] or '(cut)') for e in s['edits']] + ['']
    out += [s['why'], '', 'Pangram: ' + s['reading'] + ' ' + s['tested'], '', '**' + s['advice_note'] + '**', '']
(HERE / 'REVIEW-T8.md').write_text('\n'.join(out).rstrip('\n') + '\n', encoding='utf-8')
print('REVIEW-T8: %d blocks, %d cards, %d bytes' % (len(bl), len(review['suggestions']), len(html)))
