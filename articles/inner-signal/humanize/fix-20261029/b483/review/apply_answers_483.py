"""Put Joel's answers to the cards page (Hypnosis Guide Cards, REVIEW-483) into the hypnosis guide, with every card's fate.

Joel, 2026-10-30 14:35 UTC, sent the page's export (ANSWERS-20261030-1435.json, word for word in this folder): 9 cards
approved, 19 revised (his own versions; nine of them he reports as passing Pangram on his side: "passes pangram alone").

- An approved card goes in as the card showed it (its edit's "after").
- A revised card goes in as his version, word for word, except: obvious typos (TYPOS, each listed); the text he put
  around his version that isn't the guide's words (a heading the guide already has, "this passes:", the three labelled
  versions of R-755, of which the one he marked 100% High goes in); and where his version covers fewer paragraphs than
  the card (N-243: he wrote only the first of its two, so the second stays as it is, and he is asked).
- His comment on R-96 asks for one more change: the next paragraph starts "First, access your...".

  python3 articles/inner-signal/humanize/fix-20261029/b483/review/apply_answers_483.py [--check]

Writes HUMANIZED-SO-FAR.md and APPLIED-483.json (each card's fate, the typo fixes, the notes for him).
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[2]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text  # noqa: E402

GUIDE = H / 'HUMANIZED-SO-FAR.md'
ANSWERS = HERE / 'ANSWERS-20261030-1435.json'

# obvious typos in his versions: (card, wrong, right, why)
TYPOS = [
    ('T1', 'reading from a telecaster like', 'reading from a teleprompter like',
     'a slip of the word: a news anchor reads from a teleprompter'),
    ('T8', 'can make help smooth', 'can help smooth', 'a leftover word'),
    ('T16', 'that experience  you had', 'that experience you had', 'a double space'),
    ('T16', 'with strings  or get revoked', 'with strings or get revoked', 'a double space'),
    ('R-237', 'out of the subsconscious', 'out of the subconscious', 'a typo'),
    ('R-audit', 'the script,  or stopping', 'the script, or stopping', 'a double space'),
    ('R-audit', 'my lack of awarenes of', 'my lack of awareness of', 'a typo'),
    ('R-755', 'aware of the sutble inner signal', 'aware of the subtle inner signal', 'a typo'),
]


def his_paragraphs(cid, text):
    """His version as the guide's paragraphs, with what isn't the guide's words taken off (each step recorded)."""
    notes = []
    t = text
    if cid == 'R-237':
        head = 'Please don’t put six metaphors in one trance\n\n'
        assert t.startswith(head)
        t = t[len(head):]
        notes.append('his version began with the section\'s heading, which the guide already has: left out')
    if cid == 'N-757':
        head = 'Appendix K: Sources and further reading\n'
        assert t.startswith(head)
        t = t[len(head):]
        notes.append('his version began with the appendix\'s heading, which the guide already has: left out')
    if cid == 'R-630':
        pre = 'this passes: "'
        assert t.startswith(pre) and t.endswith('"')
        t = t[len(pre):-1]
        notes.append('his version came as: this passes: "…"; the words inside the quotation marks went in')
    if cid == 'R-755':
        a = t.index('this one 100% high conf human:\n\n') + len('this one 100% high conf human:\n\n')
        b = t.index('\n\n\nthis one was ai:')
        t = t[a:b]
        notes.append('he sent three versions (one Human at about 70% High and the rest Medium, one 100% High Human, one '
                     'AI); the 100% High one went in')
    for c, wrong, right, why in TYPOS:
        if c == cid:
            assert t.count(wrong) == 1, (cid, wrong)
            t = t.replace(wrong, right)
            notes.append('typo fixed (%s): "%s" -> "%s"' % (why, wrong.strip(), right.strip()))
    paras = [p.strip() for p in re.split(r'\n\s*\n', t.strip()) if p.strip()]
    if cid == 'N-276':
        # his first paragraph ends "Say something like," and the script follows on the next line, as in the guide's two
        assert len(paras) == 1 and paras[0].count('Say something like,\n') == 1
        first, second = paras[0].split('Say something like,\n')
        paras = [first + 'Say something like,', second.strip()]
        notes.append('his first paragraph ends "Say something like," and the script follows on the next line: two '
                     'paragraphs, as in the guide')
    if cid == 'R-audit':
        # each question on a line of its own, as the guide had them (a paragraph each)
        paras = [ln.strip() for p in paras for ln in p.split('\n') if ln.strip()]
        notes.append('each line of his lists is a paragraph of its own in the guide, as the audit\'s lines were')
    return paras, notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    review = json.loads((HERE / 'REVIEW-483.json').read_text(encoding='utf-8'))
    answers = json.loads(ANSWERS.read_text(encoding='utf-8'))
    md = GUIDE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert sha == review['article']['sha256'] == answers['article']['sha256'], 'the guide changed since the cards page'
    assert answers['review_id'] == review['review_id']
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl)
    A = {x['id']: x for x in answers['items']}
    new_raw, fates, lost, notes_all = {}, {}, [], {}
    for s in review['suggestions']:
        x = A[s['id']]
        blocks = sorted({sp['block'] for sp in s['spans']}) if s['advice'] == 'edit' else [s['edits'][0]['block']]
        if x['status'] == 'approved':
            assert s['advice'] == 'approve'
            i = s['edits'][0]['block']
            assert s['edits'][0]['before'] == bl[i]['text']
            new_raw[i] = [set_block_text(raw[i], s['edits'][0]['after'], lost)]
            fates[s['id']] = 'approved: the card\'s version went in'
            continue
        assert x['status'] == 'revise' and x['your_version'].strip(), s['id']
        paras, notes = his_paragraphs(s['id'], x['your_version'])
        if s['id'] == 'J5':
            notes.append('his version replaces the whole paragraph, so its four factors (conscious agreement, unconscious '
                         'receptivity, emotional compliance, legal and ethical consent) and "People have their minds '
                         'influenced without the conscious agreement of their adult self." are gone: told him once')
        if s['id'] == 'N-243':
            assert len(paras) == 1 and blocks == [243, 244]
            blocks = [243]
            notes.append('his version had one paragraph for the card\'s two; it replaced the first ("Put yourself in a '
                         'place …"), and the second ("Deciding to do it: …", with how to stop the induction) stays as it '
                         'is until he says to cut it')
        if s['id'] == 'N-282':
            assert len(paras) == 4 and blocks == [282, 283, 285, 286]
            for k in (1, 2, 3):
                assert paras[k] == bl[blocks[k]]['text'], (s['id'], k)
            notes.append('his four paragraphs go in the card\'s four places (the heading "Sleep induction" stays between '
                         'the second and the third); only the first changed')
        for i in blocks:
            assert i not in new_raw, (s['id'], i)
        if len(paras) == len(blocks):
            for i, p in zip(blocks, paras):
                new_raw[i] = [set_block_text(raw[i], p, lost)]
        else:
            # fewer or more paragraphs than the card's places: all of them go where the card's first place was (the
            # card's places are next to each other here)
            assert blocks == list(range(blocks[0], blocks[-1] + 1)), (s['id'], blocks)
            new_raw[blocks[0]] = [set_block_text(raw[blocks[0]], p, lost) for p in paras]
            for i in blocks[1:]:
                new_raw[i] = []
        fates[s['id']] = 'his version'
        notes_all[s['id']] = notes
    # his comment on R-96: "next sentence should start with, "First, access your...""
    j = 97
    assert bl[j]['text'].startswith('Access your witnessing position')
    assert j not in new_raw
    new_raw[j] = [set_block_text(raw[j], 'First, a' + bl[j]['text'][1:], lost)]
    notes_all['R-96'].append('his comment: the next paragraph now starts "First, access your witnessing position"')
    out = []
    for i, r in enumerate(raw):
        out += new_raw.get(i, [r])
    new = '\n\n'.join(out) + '\n'
    rec = {'answers': ANSWERS.name, 'answers_sha256': hashlib.sha256(ANSWERS.read_bytes()).hexdigest(),
           'before_sha256': sha, 'after_sha256': hashlib.sha256(new.encode('utf-8')).hexdigest(),
           'fates': fates, 'notes': notes_all, 'typos': [{'card': c, 'was': w, 'now': r, 'why': y} for c, w, r, y in TYPOS],
           'links_dropped': lost, 'changed_blocks': sorted(new_raw)}
    print(json.dumps({k: v for k, v in rec.items() if k not in ('fates', 'notes', 'typos')}, indent=1))
    from collections import Counter
    print(Counter(fates.values()))
    for k, v in notes_all.items():
        for n in v:
            print(k, '|', n)
    if not a.check:
        GUIDE.write_text(new, encoding='utf-8')
        (HERE / 'APPLIED-483.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
