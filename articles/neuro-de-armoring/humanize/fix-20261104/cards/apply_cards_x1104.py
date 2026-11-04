"""His answers to Neuro De-Armoring Cards, 4 November (all 12 approved; ANSWERS-20261104-1205.json, exported 12:05:54 UTC,
with his message of 12:06 UTC, ../joel-20261104-1206-message.txt), into the article.

Each card's after-text goes in as the card showed it, in the cards' order. The fidelity check (FIDELITY-KEYS.json) runs
before and after every card: what a card took out or put in (a cut warning, the PS dose) is recorded under
"owner_changes" with the card's id, from the check's own difference, so nothing goes in that the card didn't change.
The comparative read (gate E284) of the changed paragraphs beside his post's is the lead session's own (E294), recorded
in read/READ-RECORD.json with its findings and their fates.

  python3 articles/neuro-de-armoring/humanize/fix-20261104/cards/apply_cards_x1104.py [--check]
Writes HUMANIZED-SO-FAR.md, FIDELITY-KEYS.json, APPLIED-CARDS.json and read/READ-RECORD.json.
"""
import argparse
import collections
import copy
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
F = HERE.parent
H = F.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(ROOT / 'articles' / 'inner-signal' / 'humanize' / 'fix-20261025' / 'review'))
import compare_read as cr  # noqa: E402
import fidelity_keys as fk  # noqa: E402
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
KEYS = H / 'FIDELITY-KEYS.json'
REVIEW = HERE / 'REVIEW-X1104.json'
ANSWERS = HERE / 'ANSWERS-20261104-1205.json'
BY = 'fix-20261104/cards/ANSWERS-20261104-1205.json, card %s (approved 2026-11-04)'
# the comparative read, mine (E284, E294): each changed paragraph beside his post's, sentence by sentence
FINDINGS = [
    {'id': 'Y-83.1', 'card': 'Y-83', 'severity': 1, 'kind': 'vaguer',
     'now': 'Scott added a standard dose of UMP, and within a day his ketamine/LSD cravings fell hard.',
     'note': 'his post has the whole response within a day ("he got a striking response within a day: vivid dreams '
             'returned, ..."); here "within a day" sits with the cravings, and the dreams come at the end with "too"'},
    {'id': 'Y-83.2', 'card': 'Y-83', 'severity': 1, 'kind': 'vaguer',
     'now': 'UMP can show you very clearly when the brain\'s system for rebuilding synaptic membranes and recovering '
            'dopamine receptors has been starved of building materials',
     'note': 'his "a very clean signal" (clean: the choline and DHA were already there) is "very clearly" here'},
    {'id': 'Y-82.1', 'card': 'Y-82', 'severity': 1, 'kind': 'vaguer',
     'now': 'which uses them to make the fatty membranes at its synapses',
     'note': 'brain phosphatide synthesis is wider than the synapses\' membranes; the term in brackets keeps it'},
]
DISPOSITIONS = {
    'Y-83.1': ['his', 'shown on card Y-83, which he approved; the next try of the paragraph (his answer 5a) aims at the '
                      'Low window these sentences are in, and puts "within a day" back over the dreams'],
    'Y-83.2': ['his', 'card Y-83, approved; the next try (5a) says "clean" again'],
    'Y-82.1': ['kept', 'severity 1: the bracket keeps his term, and the paragraph is about the synapses'],
}


def counts(xs):
    return collections.Counter(xs)


def delta(before, after):
    """What one card changed, from two fidelity results: the lost and new numbers, lost terms and warning keys that
    weren't so before it."""
    d = {'numbers_lost': sorted((counts(after['numbers_lost']) - counts(before['numbers_lost'])).elements()),
         'numbers_new': sorted((counts(after['numbers_new']) - counts(before['numbers_new'])).elements()),
         'terms_lost': sorted(set(after['terms_lost']) - set(before['terms_lost']))}
    was = {u['id']: [tuple(k) for k in u['missing']] for u in before['warnings_lost']}
    keys = {}
    for u in after['warnings_lost']:
        new = [k for k in u['missing'] if tuple(k) not in was.get(u['id'], [])]
        if new:
            keys[u['id']] = new
    d['keys_lost'] = keys
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    assert (F / 'joel-20261104-1206-message.txt').read_text(encoding='utf-8').rstrip().endswith('medium aren\'t a big issue usually')
    md = ARTICLE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    review = json.loads(REVIEW.read_text(encoding='utf-8'))
    answers = json.loads(ANSWERS.read_text(encoding='utf-8'))
    assert answers['review_id'] == review['review_id'], 'answers to another page'
    assert sha == review['article']['sha256'] == answers['article']['sha256'], 'the article changed since the cards'
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl)
    keys = json.loads(KEYS.read_text(encoding='utf-8'))
    work = copy.deepcopy(keys)
    work.setdefault('owner_changes', [])
    A = {x['id']: x for x in answers['items']}
    first = fk.check(work, md)
    assert first['pass'], first
    applied, prev, lost = [], first, []
    for s in review['suggestions']:
        ans = A[s['id']]
        assert ans['status'] == 'approved' and not ans['your_version'].strip(), (s['id'], ans['status'])
        assert ans['my_version'] == '\n\n'.join(e['after'] for e in s['edits']), s['id']
        for e in s['edits']:
            i = e['block']
            assert bl[i]['text'] == e['before'], (s['id'], i)
            if '](' in e['after'] or raw[i] == bl[i]['text']:
                raw[i] = e['after']                      # the card's text is the block's whole Markdown
            else:
                raw[i] = set_block_text(raw[i], e['after'], lost)   # keeps the block's own emphasis (W-73: *right now*)
        now = '\n\n'.join(raw) + '\n'
        r = fk.check(work, now)
        d = delta(prev, r)
        if any(d.values()):
            work['owner_changes'].append(dict({'by': BY % s['id']}, **{k: v for k, v in d.items() if v}))
            r = fk.check(work, now)
        applied.append({'id': s['id'], 'blocks': [e['block'] for e in s['edits']], 'where': sr.where(bl, s['edits'][0]['block']),
                        'fidelity_change': {k: v for k, v in d.items() if v}})
        prev = r
    out = '\n\n'.join(raw) + '\n'
    final = fk.check(work, out)
    after = hashlib.sha256(out.encode('utf-8')).hexdigest()
    rec = {'about': 'his answers to Neuro De-Armoring Cards, 4 November: all 12 approved', 'answers': ANSWERS.name,
           'before_sha256': sha, 'after_sha256': after, 'cards': applied, 'emphasis_lost': lost,
           'fidelity': {'pass': final['pass'], 'owner_changes': final['owner_changes']}}
    print(json.dumps(rec, ensure_ascii=False, indent=1))
    assert final['pass'], final
    assert not lost, lost
    if a.check:
        return
    ARTICLE.write_text(out, encoding='utf-8')
    KEYS.write_text(json.dumps(work, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'APPLIED-CARDS.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    nb = sr.blocks(out)
    cover = [cr.phash(nb[i]['text']) for c in applied for i in c['blocks']]
    found = []
    for f in FINDINGS:
        (i,) = [i for c in applied if c['id'] == f['card'] for i in c['blocks'] if f['now'] in nb[i]['text']]
        found.append(dict(f, block_hashes=[cr.phash(nb[i]['text'])]))
    d = HERE / 'read'
    d.mkdir(exist_ok=True)
    cr.record(d, findings=found, coverage=cover, dispositions=DISPOSITIONS,
              article='HUMANIZED-SO-FAR.md at %s: the 12 approved cards, each changed paragraph read beside his post\'s by '
                      'the lead session (E284, E294)' % after[:8])


if __name__ == '__main__':
    main()
