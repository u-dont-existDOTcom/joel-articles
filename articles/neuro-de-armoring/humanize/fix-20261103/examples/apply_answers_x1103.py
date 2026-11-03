"""Joel's three versions on Neuro De-Armoring Cards, 3 November (REVIEW-X1103.json), into the article.

His answers file, sent at 2026-11-03 17:48 UTC with no other text, word for word in ANSWERS-20261103-1748.json (exported
17:48:26 UTC). All three cards are "revise", each with his version:
- X-26 (Psychology is the Software, the underpinning paragraph), his comment "passes";
- X-84 (the uridine section, the trial paragraph), his comment "passes";
- X-15 (the disclaimers, agmatine's interactions), no comment.
He had asked for them so his versions train the rest of the article: "give me a couple examples i will see how to rewrite
it to train you" (../joel-20261103-1522-answers.txt).

Each version goes in as he wrote it. Only obvious typos are fixed, each listed in TYPOS with its reason; his own
characters stay (straight quotes, "Omega-3's", " - ", "150-300mg"). He tested X-26 and X-84 in Pangram himself ("passes"),
so they aren't checked again; X-15 is checked by itself (../x15/).

  python3 articles/neuro-de-armoring/humanize/fix-20261103/examples/apply_answers_x1103.py [--check]
Writes HUMANIZED-SO-FAR.md, APPLIED-X1103.json (each card's paragraph before and after) and read/READ-RECORD.json.
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
BEFORE = 'a4b4e05ae5b6930519e79708f0d7dbedf5cb4f9c6158bf2efd60121501fdef0f'
REVIEW = HERE / 'REVIEW-X1103.json'
ANSWERS = HERE / 'ANSWERS-20261103-1748.json'
# (card, his words, the fix, why): a letter dropped or swapped in a word he spells right elsewhere or a drug's name
TYPOS = [
    ('X-26', 'HDAC inhibiton', 'HDAC inhibition', 'a dropped letter ("inhibition")'),
    ('X-15', 'clonidine and/or guafacine', 'clonidine and/or guanfacine',
     'a dropped letter in the drug\'s name (guanfacine, as his post spells it)'),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    md = ARTICLE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    review = json.loads(REVIEW.read_text(encoding='utf-8'))
    answers = json.loads(ANSWERS.read_text(encoding='utf-8'))
    assert sha == BEFORE == review['article']['sha256'] == answers['article']['sha256'], 'the article changed'
    assert answers['review_id'] == review['review_id']
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl), (len(raw), len(bl))
    cards = {s['id']: s for s in review['suggestions']}
    fates = {}
    for x in answers['items']:
        assert x['status'] == 'revise' and x['your_version'].strip(), x['id']
        s = cards[x['id']]
        (sp,) = s['spans']
        i = sp['block']
        assert bl[i]['text'] == x['before'] == x['my_version'], x['id']
        assert raw[i] == bl[i]['text'] and not re.search(r'[*_\[\]<>`]', raw[i]), 'marks in block %d' % i
        new = x['your_version'].strip()
        fixed = []
        for cid, old, repl, why in TYPOS:
            if cid == x['id']:
                assert new.count(old) == 1, (cid, old)
                new = new.replace(old, repl)
                fixed.append({'his': old, 'now': repl, 'why': why})
        raw[i] = new
        fates[x['id']] = {'block': i, 'where': sr.where(bl, i), 'his comment': x['comment'], 'before': x['before'],
                          'his version': x['your_version'], 'after': new, 'typos fixed': fixed}
    new_md = '\n\n'.join(raw) + '\n'
    after = hashlib.sha256(new_md.encode('utf-8')).hexdigest()
    nb = sr.blocks(new_md)
    assert len(nb) == len(bl)
    assert [b['text'] for b in nb if b['i'] not in {f['block'] for f in fates.values()}] == \
        [b['text'] for b in bl if b['i'] not in {f['block'] for f in fates.values()}]
    rec = {'about': 'His three versions on Neuro De-Armoring Cards, 3 November, put in by apply_answers_x1103.py',
           'answers_file': ANSWERS.name, 'answers_sha256': hashlib.sha256(ANSWERS.read_bytes()).hexdigest(),
           'before_sha256': sha, 'after_sha256': after, 'cards': fates}
    print(json.dumps(rec, ensure_ascii=False, indent=1))
    if a.check:
        return
    ARTICLE.write_text(new_md, encoding='utf-8')
    (HERE / 'APPLIED-X1103.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    d = HERE / 'read'
    d.mkdir(parents=True, exist_ok=True)
    cr.record(d, findings=[], coverage=sorted({cr.phash(f['after']) for f in fates.values()}), dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: his three versions (X-26, X-84, X-15), each read in place beside the '
                      'paragraph it replaces by the lead session (E284, E331): his words, two typos fixed' % after[:8])


if __name__ == '__main__':
    main()
