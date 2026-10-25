"""ALLOWED.txt for the guide's Emulate check: the words Joel approved that aren't in his own texts.

  python3 articles/inner-signal/humanize/fix-20261025/emulate-check/make_allowed.py

Each paragraph of ALLOWED.txt is one sentence: the new sentences (under 80% of their words in one sentence before) of every suggestion that went into the guide on
2026-10-25 (his answers, ../review/APPLIED.json: approved, his own versions, and those he left to my advice), with the
follow-on fixes listed there. The inner child guide (../ic-align/IC-GUIDE.txt, his own published guide) is passed to the
check as a second allowed file.
"""
import difflib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import emulate_artifacts as ea  # noqa: E402

review = json.loads((HERE.parent / 'review' / 'REVIEW.json').read_text(encoding='utf-8'))
applied = json.loads((HERE.parent / 'review' / 'APPLIED.json').read_text(encoding='utf-8'))
answers = json.loads((HERE.parent / 'review' / 'ANSWERS-20261025-1940.json').read_text(encoding='utf-8'))
A = {x['id']: x for x in answers['items']}
went_in = {sid for sid, f in applied['fates'].items() if f.startswith(('approved', 'revised', 'accepted'))}


def sents(t):
    return [t[a:z].strip() for a, z in ea.sentences(t)]


def new_ones(after, before):
    """AFTER's sentences that are new: no sentence of BEFORE has 80% of the same words (a typo fixed in a sentence
    doesn't make the rest of it his)."""
    bw = [ea.words(x) for x in sents(before or '')]
    out = []
    for x in sents(after or ''):
        w = ea.words(x)
        if not any(difflib.SequenceMatcher(None, w, y, autojunk=False).ratio() >= 0.8 for y in bw):
            out.append(x)
    return out


out = []
for s in review['suggestions']:
    if s['id'] not in went_in:
        continue
    for e in s['edits']:
        after = A[s['id']]['your_version'] if A[s['id']]['status'] == 'revise' else e['after']
        out += new_ones(after, e['before'])
    for ins in s['inserts']:
        out += sents(ins['text'])
for p in applied['paragraphs']:
    if p['after']:
        out += new_ones(p['after'], p['before'])
seen, lines = set(), []
for x in out:
    if x and ea.low(x) not in seen:
        seen.add(ea.low(x))
        lines.append(x)
(HERE / 'ALLOWED.txt').write_text('\n\n'.join(lines) + '\n', encoding='utf-8')
print(len(lines), 'sentences')
