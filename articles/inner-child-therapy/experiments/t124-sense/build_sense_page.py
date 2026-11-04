#!/usr/bin/env python3
"""Turn 124: the marking page for the word-for-sense read (gate E331; SKILL.md, "Word-for-sense read before publication").

Fresh readers read his whole guide, one part each, for words that aren't the ones meant (sense_read.py; READS.md here has
the scores). Every finding was read in place and traced to whose words it is (trace_findings.py, TRACE.json). All of them
are in his own words (his reorganized guide of 2026-11-03), so none is changed without him (Joel's rule: an obvious typo in
his text is fixed only with his OK): each real one is a card here with the smallest fix and my advice, the ones I'd leave
are quiet "leave" cards he can open and overrule, and one is a question only he can answer. The findings that aren't real
(a picture the read leaves out, a link address the parts showed wrong) are in READS.md, not here.

The page is the guide as it stands (GUIDE-PAGE.md: make_page_copy's changes of turn 121, bold marks out and each list item a
block of its own, never his words), built with tools/humanization/suggestion_review.py. Each card names the reader that found
it and the fix in its "after" text, follow-on changes made (his rule: the "after" shows the result).
  python3 articles/inner-child-therapy/experiments/t124-sense/build_sense_page.py"""
import datetime
import hashlib
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

SRC = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
PAGE = HERE / 'GUIDE-PAGE.md'
ARTICLE = 'articles/inner-child-therapy/experiments/t124-sense/GUIDE-PAGE.md'
BRANCH = 'handoff/claude-dangerous-adult-20260924-1631'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/%s/articles/inner-child-therapy/' % BRANCH

md = SRC.read_text(encoding='utf-8')
out = md.replace('**', '')
out = re.sub(r'[ \t]*\n(?=(?:\d+\.|-)\s)', '\n\n', out)
out = re.sub(r'\[\*([^\]*]+)\*\]\(', r'[\1](', out)
PAGE.write_text(out, encoding='utf-8')
BL = sr.blocks(out)

TYPES = {
    'slip': {'label': 'Typo or slip', 'about': 'A word, a letter or a mark that is clearly off: a typo, a missing word, a quote mark in the wrong place.'},
    'meaning': {'label': 'Maybe not the word you meant', 'about': 'A real word where, read closely, another seems meant. Only you know which word you meant, so Revise if mine is not it.'},
    'form': {'label': 'Spelling and dashes', 'about': 'Your own spelling and dash, made the same everywhere.'},
    'ask': {'label': 'A question for you', 'about': 'Something only you know.'},
    'leave': {'label': 'A reader flagged it; I would leave it', 'about': 'A reader found these; I would leave them as they are. Open one to overrule me.'},
}
S = []
READER = {1: 'the reader of part 1', 2: 'the reader of part 2', 3: 'the first reader of part 3', 4: 'the second reader of part 3'}


def fix(cid, typ, title, old, new, why, note, readers, near_words=None, extra=()):
    """An approve card: OLD becomes NEW in the one block holding OLD (and each (old, new) of EXTRA likewise)."""
    spans, edits = [], []
    for o, n in ((old, new),) + tuple(extra):
        b, s, e = sr.find_quote(BL, o)
        t = sr.block_text(BL, b)
        assert t.count(o) == 1, (cid, o)
        spans.append({'block': b, 'start': s, 'end': e})
        edits.append({'block': b, 'before': t, 'after': t.replace(o, n)})
    S.append({'id': cid, 'type': typ, 'title': title, 'advice': 'approve', 'spans': spans, 'edits': edits,
              'what': 'You wrote "%s"; it would read "%s".' % (old, new) if not extra else
                      'Both become your spaced dash: ' + '; '.join('"%s" to "%s"' % (o, n) for o, n in ((old, new),) + tuple(extra)) + '.',
              'why': why, 'stays': 'Everything else in the paragraph.', 'advice_note': note,
              'deciding': 'Whether to make this change, or your own (Revise).',
              'found_by': ', '.join(READER[r] for r in readers)})


def leave(cid, title, quote, reader_said, why_leave, readers, reader_old, reader_new):
    """A reader's change I'd leave out: the card shows it as the reader's, so he can overrule me."""
    b, s, e = sr.find_quote(BL, quote)
    t = sr.block_text(BL, b)
    assert t.count(reader_old) == 1, (cid, reader_old)
    S.append({'id': cid, 'type': 'leave', 'title': title, 'advice': 'leave', 'spans': [{'block': b, 'start': s, 'end': e}],
              'edits': [{'block': b, 'before': t, 'after': t.replace(reader_old, reader_new)}],
              'what': 'The reader would make "%s" into "%s".' % (reader_old, reader_new),
              'why': 'The reader said: %s' % reader_said, 'stays': 'All of it, unless you overrule me.',
              'deciding': 'Whether to overrule me and make the reader\'s change.',
              'advice_note': why_leave, 'found_by': ', '.join(READER[r] for r in readers)})


def ask(cid, title, quote, question, why, note, readers):
    b, s, e = sr.find_quote(BL, quote)
    S.append({'id': cid, 'type': 'ask', 'title': title, 'advice': 'ask', 'question': question, 'why': why,
              'deciding': question,
              'stays': 'The paragraph as it is, until you answer.', 'advice_note': note,
              'spans': [{'block': b, 'start': s, 'end': e}], 'found_by': ', '.join(READER[r] for r in readers)})


CARDS = json.loads((HERE / 'CARDS.json').read_text(encoding='utf-8'))
for c in CARDS:
    kind = c.pop('kind')
    if kind == 'fix':
        c['extra'] = tuple(tuple(x) for x in c.get('extra', []))
        fix(**c)
    elif kind == 'leave':
        leave(**c)
    else:
        ask(**c)

S.sort(key=lambda x: (x['spans'][0]['block'], x['spans'][0]['start']))
counts = {k: sum(1 for x in S if x['type'] == k) for k in TYPES}
review = {
    'format': sr.FORMAT, 'review_id': 'inner-child-t124-sense-read', 'title': 'Inner Child Sense Read',
    'intro': [json.loads((HERE / 'CARDS-INTRO.json').read_text(encoding='utf-8'))['intro'] % counts]
             + json.loads((HERE / 'CARDS-INTRO.json').read_text(encoding='utf-8'))['more'],
    'git_file': 'articles/inner-child-therapy/experiments/t124-sense/REVIEW.html',
    'article': {'file': ARTICLE, 'sha256': hashlib.sha256(out.encode('utf-8')).hexdigest()},
    'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
    'links': {'guide': BLOB + 'experiments/t124-sense/GUIDE-PAGE.md', 'review': BLOB + 'experiments/t124-sense/READS.md'},
    'types': TYPES, 'suggestions': S,
}
probs = sr.check(review, BL)
if probs:
    sys.exit('\n'.join(probs))
(HERE / 'REVIEW.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/suggestion_review.py'), 'page', str(HERE / 'REVIEW.json'),
                    str(HERE / 'REVIEW.html'), '--artifact', str(HERE / 'REVIEW-artifact.html')], cwd=ROOT,
                   capture_output=True, text=True)
print((r.stdout + r.stderr).strip()[-600:])
if r.returncode:
    sys.exit(r.returncode)
print('REVIEW.json', len(S), 'cards:', counts)
