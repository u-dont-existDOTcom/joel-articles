"""Joel's answers to Community Article Cards, 1 November (REVIEW-IC1101), as edits for his post, with every card's fate.

His export (ANSWERS-20261102-0029.json here, word for word), sent with his message of 2026-11-02 16:43 UTC (the hypnosis
lane's fix-20261102/joel-20261102-1643-message.txt: no text, two answers files): 4 approved, 2 revised.

- W-1 (approved) and W-2 (his version) are the same paragraph: his version has W-1's change and his own ending, so his
  version goes in.
- W-3 and W-4 (both approved) change different sentences of one paragraph: both go in.
- W-5 (his version) and W-6 (approved) are the same paragraph: his version has W-6's change ("to tell who can be
  trusted") and more of his own, so his version goes in.
- Typography in his versions follows the post's (TYPOGRAPHY, each listed): his straight apostrophe becomes the post's
  curly one, and "--" between two words becomes an em dash, as the post writes "Seba—my favorite".

Each edit is a Find string (the words that change, inside one run of text with no marks, checked to occur once in
master.md) and its replacement, for his post's editor (one transaction, as on 1 November), and WORKING-20261102.md is
master.md with them.

  python3 articles/intentional-communities/candidate/fullread-20261030/review/joel-20261101-2026/sections/review/apply_ic1101.py
Writes SUBSTACK-EDITS-IC1101.json and WORKING-20261102.md here.
"""
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
A = HERE.parents[5]
MASTER = A / 'master.md'
ANSWERS = HERE / 'ANSWERS-20261102-0029.json'

TYPOGRAPHY = [
    ('W-2', "we're doing even less", 'we’re doing even less', 'the post\'s curly apostrophe'),
    ('W-5', 'be trusted--even your', 'be trusted—even your', 'an em dash for "--", as the post writes "Seba—my favorite"'),
]
# (cards, find, replace): find is in master.md once; replace is his words (or the card's, where he approved it)
EDITS = [
    (['W-1', 'W-2'], 'brought outsiders into their communities for a while to learn autonomy by living it',
     'had outsiders stay with Zapatista families for a while and learn self-government by taking part in everyday life'),
    (['W-2'], 'Otherwise, we’ve built a lovely refuge for whoever got there first.',
     'Otherwise, we might have a lovely refuge for a few lucky souls, but we’re doing even less than a retreat center to '
     'heal the planet.'),
    (['W-3'], 'I was usually just a visitor’s kid, close enough to see how people lived but never quite part of the tribe.',
     'I was usually just a visitor’s kid. I could see how people lived, but I was never really part of the tribe.'),
    (['W-4'], 'At the time, that meant a lot of boredom, with some adventures mixed in, but those years gave me a great '
              'sample to compare against.',
     'At the time it was mostly boring, with some adventures mixed in, but it means I’ve seen a lot of communities to '
     'compare against.'),
    (['W-5'], 'We evolved to live in small groups where everybody knows everybody.',
     'We evolved to live in small groups where everybody knows, loves, and trusts everybody.'),
    (['W-5', 'W-6'], 'and nobody knows anybody well enough to see what they’re really like.',
     'and nobody knows anybody well enough or for long enough to tell who can be trusted—even your next-door neighbor is '
     'often a total stranger.'),
]
FATES = {
    'W-1': 'approved; in his W-2 version, which has the same change',
    'W-2': 'his version',
    'W-3': 'approved: the card\'s version went in',
    'W-4': 'approved: the card\'s version went in',
    'W-5': 'his version',
    'W-6': 'approved; in his W-5 version, which has the same change',
}


def flat(s):
    return ' '.join(s.replace('*', '').split())


def main():
    ans = json.loads(ANSWERS.read_text(encoding='utf-8'))
    items = {x['id']: x for x in ans['items']}
    assert set(items) == set(FATES)
    md = MASTER.read_text(encoding='utf-8')
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == ans['article']['sha256'], 'master.md changed since the cards'
    # his versions, with the post's typography, are what the edits make of his paragraphs
    for cid in ('W-2', 'W-5'):
        v = items[cid]['your_version']
        for c, wrong, right, _ in TYPOGRAPHY:
            if c == cid:
                assert v.count(wrong) == 1, (cid, wrong)
                v = v.replace(wrong, right)
        items[cid]['_his'] = v
    new = md
    for cards, find, repl in EDITS:
        assert new.count(find) == 1, find
        new = new.replace(find, repl)
    paras = [flat(re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', p)) for p in new.split('\n\n')]
    for cid in ('W-2', 'W-5'):
        assert flat(items[cid]['_his']) in paras, cid
    for cid in ('W-3', 'W-4'):
        mv = flat(items[cid]['my_version'])
        assert any(mv.split('kid')[0] in p for p in paras)
    w34 = flat('I spent much of my childhood being carried through Twin Oaks, Acorn, East Wind, Padanaram, Zendik, and '
               'many other communities. I was usually just a visitor’s kid. I could see how people lived, but I was never '
               'really part of the tribe. At the time it was mostly boring, with some adventures mixed in, but it means '
               'I’ve seen a lot of communities to compare against.')
    assert w34 in paras, 'W-3 and W-4 together'
    rec = {'answers': ANSWERS.name, 'answers_sha256': hashlib.sha256(ANSWERS.read_bytes()).hexdigest(),
           'master_before_sha256': ans['article']['sha256'],
           'working_sha256': hashlib.sha256(new.encode('utf-8')).hexdigest(), 'fates': FATES,
           'typography': [{'card': c, 'was': w, 'now': r, 'why': y} for c, w, r, y in TYPOGRAPHY],
           'edits': [{'cards': c, 'find': f, 'replace': r} for c, f, r in EDITS]}
    (HERE / 'SUBSTACK-EDITS-IC1101.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'WORKING-20261102.md').write_text(new, encoding='utf-8')
    print(len(EDITS), 'edits; working', rec['working_sha256'][:12])


if __name__ == '__main__':
    main()
