"""His answers to Neuro De-Armoring Cards, 4 November (3) (ANSWERS-20261104-1809.json, exported 18:09:56 UTC; his message of
18:10 UTC, ../joel-20261104-1810-message.txt: "8a not sure why you had to ask that, the whole point is rewording stuff
here"), into the article. All six are his versions ("revise").

- Y-85, Y-88, Y-89, Y-90 and Y-91: each read Human Written by itself in his checks, and the text he checked is the text he
  sent (the lane read each of his results from his history: same SHA-256). Y-91 goes in with the full stop it lacked,
  checked by the lane first (Human Written, every window High: https://www.pangram.com/history/d2b0d600-d1fe-4187-94e7-4bb0851a1b54).
- Y-86 (39 words, under the web app's 50-word minimum) read Human (High) after his Y-85, checked by the lane as a pair:
  https://www.pangram.com/history/365e4cec-67ac-4cd8-a5be-15dc24697387. His version replaces the post's "safety signal"
  ("idk where this safety warning came from, doesn't make much sense at all"); the same-day rule his version leaves out
  here ("Do not take UMP on psychedelic days") stays in the article twice, in the uridine and 5-HTP warning near the top
  (W017) and in the summary (W082).
- Y-89: his note, "i'd cut this whole paragraph or merge anything important from it into the last one, looks very
  redundant". Its points the other paragraphs don't make go into the paragraph before it, his "Who this is for", in one
  sentence after Scott's, where a reader asks why 5-HTP would help a bottleneck: it skips that bottleneck because the
  body uses it to make serotonin directly; responders feel it quickly; it's weaker for sleep or mood than the hype; the
  review linked. The merged paragraph read Human Written, one window High, by itself (batch x1104o:
  https://www.pangram.com/history/f645d894-6c91-41b3-841d-26ec0d79b093). His tool paragraph comes out. What stays out:
  the review's list of other uses (anxiety, myoclonus, obesity) and his "if levels go too high too fast, because it skips
  over the tryptophan conversion bottleneck"; the risk itself stays in his serotonin syndrome sentence, the stop signs and
  the hard interaction rule.
- 8a: FIDELITY-KEYS.json's "warning_words" is "meaning" now (fidelity_keys.py: a warning keeps its warning word, its
  compounds and terms, and its numbers; its other words may change).

The fidelity check runs before and after each card. What his versions change in the protocol goes into "owner_changes",
each entry naming his card: Y-86's W037 (its "caution", the safety signal he replaced), Y-91's second "50mg" and its "if"
for "only if" (W041), and what the merge takes out of W040.

The comparative read of the merged sentence beside his Y-89 (E284, E294) is mine; his own versions are the protocol.

  python3 articles/neuro-de-armoring/humanize/fix-20261104/cards/apply_cards_x1104d.py [--check]
Writes HUMANIZED-SO-FAR.md, FIDELITY-KEYS.json, APPLIED-CARDS-D.json and read-d/READ-RECORD.json.
"""
import argparse
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
sys.path.insert(0, str(HERE))
import compare_read as cr  # noqa: E402
import fidelity_keys as fk  # noqa: E402
import suggestion_review as sr  # noqa: E402
from apply_cards_x1104 import delta  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
KEYS = H / 'FIDELITY-KEYS.json'
ANSWERS = HERE / 'ANSWERS-20261104-1809.json'
MERGED = HERE / 'merge-b088-b089.md'
BY = 'fix-20261104/cards/ANSWERS-20261104-1809.json, card %s (his version, 2026-11-04)'
LINK = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7796270/'
HIS_CHECKS = {
    'Y-85': 'https://www.pangram.com/history/ed3c43bd-63c0-4802-8bfd-8ee01afd2f1f',
    'Y-86': 'https://www.pangram.com/history/365e4cec-67ac-4cd8-a5be-15dc24697387 (the lane\'s, after his Y-85)',
    'Y-88': 'https://www.pangram.com/history/d4e2622f-359a-4b2e-85ad-e3aee9d053ab',
    'Y-89': 'https://www.pangram.com/history/a72831f6-6bba-4f3f-a0f9-c9221286437e',
    'Y-90': 'https://www.pangram.com/history/9829b9d7-ca66-42ca-8226-218a0dcbc92d',
    'Y-91': 'https://www.pangram.com/history/66a972f2-4286-494d-96b7-179670418738 (his, without the full stop); '
            'https://www.pangram.com/history/d2b0d600-d1fe-4187-94e7-4bb0851a1b54 (the lane\'s, with it)',
}


def plain(t):
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    msg = (F / 'joel-20261104-1810-message.txt').read_text(encoding='utf-8')
    assert '8a not sure why you had to ask that, the whole point is rewording stuff here' in msg
    md = ARTICLE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    answers = json.loads(ANSWERS.read_text(encoding='utf-8'))
    assert answers['review_id'] == 'neuro-de-armoring-cards-20261104-x1104d' and answers['article']['sha256'] == sha
    A = {x['id']: x for x in answers['items']}
    assert all(x['status'] == 'revise' and x['your_version'].strip() for x in A.values())
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    at = {}
    for k in A:
        hits = [i for i, b in enumerate(raw) if plain(b) == A[k]['before']]
        assert len(hits) == 1, (k, hits)
        at[k] = hits[0]
    keys = json.loads(KEYS.read_text(encoding='utf-8'))
    work = copy.deepcopy(keys)
    work['warning_words'] = {'rule': 'meaning', 'by': 'fix-20261104/joel-20261104-1810-message.txt: "8a not sure why you had '
                             'to ask that, the whole point is rewording stuff here" (his answer to question 8, 2026-11-04 18:10 UTC)'}
    prev = fk.check(copy.deepcopy(work), md)
    assert prev['pass'], prev
    applied = []

    def put(card, how, override=None):
        nonlocal prev
        now = '\n\n'.join(x for x in raw if x is not None) + '\n'
        r = fk.check(copy.deepcopy(work), now)
        d = delta(prev, r)
        if override is not None:
            d = override
        if any(d.values()):
            work.setdefault('owner_changes', []).append(dict({'by': BY % card + ('; ' + how if how else '')},
                                                             **{k: v for k, v in d.items() if v}))
            r = fk.check(copy.deepcopy(work), now)
        assert r['pass'], (card, r)
        applied.append({'id': card, 'how': how, 'his_check': HIS_CHECKS.get(card), 'fidelity_change': {k: v for k, v in d.items() if v}})
        prev = r

    raw[at['Y-85']] = A['Y-85']['your_version'].strip()
    put('Y-85', 'his version as he checked it; his last line cut ("you were overcompleting, repeating yourself on the last line")')
    raw[at['Y-86']] = A['Y-86']['your_version'].strip()
    put('Y-86', 'his version; the same-day rule stays in W017 and W082',
        override={'numbers_lost': [], 'numbers_new': [], 'terms_lost': [], 'keys_lost': {'W037': [['caution']]}})
    merged = MERGED.read_text(encoding='utf-8').strip()
    his88 = A['Y-88']['your_version'].strip()
    assert merged.startswith(his88[:his88.index('and 5-HTP helped his sleep and mood.')]) and merged.endswith(
        his88[his88.index('I\'d avoid casually'):])
    raw[at['Y-88']] = merged
    raw[at['Y-89']] = None
    put('Y-89', 'his note: "i\'d cut this whole paragraph or merge anything important from it into the last one"; merged into '
                'his Y-88 (batch x1104o, Human Written: https://www.pangram.com/history/f645d894-6c91-41b3-841d-26ec0d79b093)')
    raw[at['Y-90']] = A['Y-90']['your_version'].strip()
    put('Y-90', 'his version; "so the low dose matters. More is not better." cut as overcompletion (his comment)')
    raw[at['Y-91']] = A['Y-91']['your_version'].strip() + '.'
    put('Y-91', 'his version, with its full stop (the lane\'s check: https://www.pangram.com/history/d2b0d600-d1fe-4187-94e7-4bb0851a1b54)')
    out = '\n\n'.join(x for x in raw if x is not None) + '\n'
    final = fk.check(copy.deepcopy(work), out)
    after = hashlib.sha256(out.encode('utf-8')).hexdigest()
    rec = {'about': 'his six versions on Neuro De-Armoring Cards, 4 November (3), and the merge of the tool paragraph he suggested',
           'answers': ANSWERS.name, 'before_sha256': sha, 'after_sha256': after, 'cards': applied, 'fidelity_pass': final['pass'],
           'warning_words': work['warning_words']}
    print(json.dumps(rec, ensure_ascii=False, indent=1))
    assert final['pass'], final
    if a.check:
        return
    ARTICLE.write_text(out, encoding='utf-8')
    KEYS.write_text(json.dumps(work, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'APPLIED-CARDS-D.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    nb = sr.blocks(out)
    (i88,) = [b['i'] for b in nb if b['text'].startswith('Who this is for: 5-HTP is not for every depressed person either.')]
    d = HERE / 'read-d'
    d.mkdir(exist_ok=True)
    cr.record(d, findings=[], coverage=[cr.phash(nb[i88]['text'])], dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: the merged sentence in block %d read beside his Y-89 by the lead session (E284, '
                      'E294): his "is a serotonin precursor, meaning your body uses it to make serotonin" and "skips over the '
                      'tryptophan conversion bottleneck" as "skips over that bottleneck, because your body uses it to make '
                      'serotonin directly"; his responders and hype as they were; his review linked; the review\'s other uses and '
                      'his "if levels go too high too fast" left out with his note (the risk stays in his serotonin syndrome '
                      'sentence and the stop signs). No finding.' % (after[:8], i88))


if __name__ == '__main__':
    main()
