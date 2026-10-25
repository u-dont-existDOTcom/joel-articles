"""The community article's marking page for the strict Emulate check (REVIEW-EMULATE.json, REVIEW-EMULATE.html).

Joel, 2026-10-25 19:42 UTC, on the hypnosis guide's page: "it looks like you must have forgotten to fix all kinds of errors
you got from emulate? ... that means we should also check the community article i guess?" and "make sure all the
citations and stuff are not messed up in the emulate-infused articles".

The check (run_audit.sh; tools/humanization/emulate_artifacts.py) compared the article as it is now (answer65/WORKING.html,
the text of his copy helper of 2026-10-25) with his published post (original.md), his own words from his messages and
answers (JOEL-TEXTS.txt, OWNER-RULINGS.txt) and the edits he and GPT made in Substack after my version of 2026-10-18
(JOEL-EDITS-20261020.md). Eight fresh Sonnet readers read each paragraph that isn't his word for word beside his own
(READ-<n>.json, 163 findings). A change he made himself after my version (his Substack edits, his answers 57 to 65, his
caveat cuts), or his own words, stays as it is; so does Emulate's wording where it keeps his meaning. What's left is here.
The page shows the article from answer65/READING-COPY.md, the same text as WORKING.html block for block.

  python3 articles/intentional-communities/candidate/joel-20261025/emulate-check/build_emulate_review.py
"""
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

ARTICLE = 'articles/intentional-communities/candidate/joel-20261024/answer65/READING-COPY.md'
GIT_FILE = 'articles/intentional-communities/candidate/joel-20261025/emulate-check/REVIEW-EMULATE.html'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/'
MD = (ROOT / ARTICLE).read_text(encoding='utf-8')
BL = sr.blocks(MD)
TYPES = {
    'quotes': {'label': 'Quote marks', 'about': 'Quote marks Emulate put around words your text has plain.'},
    'meaning': {'label': 'Emulate changed your meaning', 'about': 'A point, condition or right of yours that Emulate dropped; the suggestion puts it back in the paragraph\'s own words.'},
    'typo': {'label': 'Grammar', 'about': 'A sentence that doesn\'t parse.'},
}
FOUND = 'The strict Emulate check: a fresh reader comparing this paragraph with your published one (READ-%s.json)'
# (id, type, a quote that finds the paragraph, [(old, new)], title, why, stays, note, finding)
CARDS = [
    ('IC-Q1', 'quotes', None, None, 'Quote marks Emulate put around three words',
     'Your published post has these words plain: "full political membership", "designated spiritual spaces", "parity". Emulate put "in", "spiritual" and "even" in quote marks.',
     'Everything else, and the quote marks that are speech or carry a point ("right" to leave, "neutral stranger").',
     'The same kind of quote marks you asked about in the hypnosis guide.', '3.6, 3.25, 7.15'),
    ('IC-E1', 'meaning', 'Whatever answers we find stay fluid and organic.',
     [('Whatever answers we find stay fluid and organic.', 'Whatever answers we find stay fluid and organic, and don’t freeze into doctrine.')],
     'Your "don\'t freeze into doctrine"',
     'Your own version of this paragraph (your answers, in JOEL-TEXTS.txt) ends: "Whatever answers we find stay fluid and organic, and don\'t freeze into doctrine." The clause got lost when it went in, and the next paragraph\'s "When agreements get frozen" picks it up.',
     'Everything else in the paragraph, word for word.', 'Your words, word for word.', '2.6'),
    ('IC-E2', 'meaning', 'A group that practices together weekly for two years may never own land.',
     [('So what? It can still make a difference', 'So what? It’s already a real piece of community, and it can still make a difference')],
     'A practice group already is community',
     'Your published line: "A weekly group that has practiced together for two years already contains a real piece of community. It may never own land." Emulate kept "may never own land" and dropped the point that the group already is community, which is what the section\'s heading promises.',
     'Your "So what?" and everything else.', 'Your point in the paragraph\'s words.', '2.10'),
    ('IC-E3', 'meaning', 'This power to remove people is so easily abused, though.',
     [('What counts as cause for immediate protective action?', 'What counts as cause for immediate protective action? Who has to step aside because they’re too close to it?'),
      ('How will the person be able to reply to the concerns?', 'How will the person be able to reply to the concerns? What review or appeal is possible without endangering others?')],
     'Who steps aside, and the appeal',
     'Your published line: "Decide the process before the name: what conduct triggers immediate protective action, who preserves evidence, who is recused, who decides temporary restrictions, how the person replies, what review or appeal is possible without endangering others, ..." Emulate\'s list kept the others and dropped who is recused and the appeal.',
     'The rest of the list, word for word.', 'Your two points back as questions; the second in your words (the gate\'s reviewers refused my "safely" for losing "others").', '7.23, 7.24'),
    ('IC-E4', 'meaning', 'The key is that it’s not the same people.',
     [('The key is that it’s not the same people.', 'The key is that it’s not the same people. And a community’s autonomy doesn’t let it take away rights a person can’t sign away, or make the law outside disappear.')],
     'Autonomy doesn\'t erase rights',
     'Your published lines: "The Zapatistas are an important correction here: autonomous institutions can review local power without becoming the state. But autonomy is not permission to erase non-waivable individual rights, and it does not make outside jurisdiction disappear." The list already has "autonomous regional institutions"; Emulate dropped the limit.',
     'Everything else in the paragraph, word for word.', 'Your limit, in plain words.', '7.25, 7.26'),
    ('IC-T1', 'typo', 'Just because it’s optional participating in the ceremonies',
     [('Just because it’s optional participating in the ceremonies doesn’t mean they don’t have to work with the other parts.',
       'Just because taking part in the ceremonies is optional doesn’t mean people don’t have to work with the other parts.')],
     'A sentence that doesn\'t parse',
     'You kept this sentence on 2026-10-24 (65.14 B); as it stands it doesn\'t parse ("it\'s optional participating"), and "they" could be the ceremonies.',
     'What it says.', 'Grammar only: "taking part" for "participating", and "people" for "they".', '4.11, 4.12'),
]
QUOTES = [('fully “in” the commune', 'fully in the commune'), ('designated “spiritual” places', 'designated spiritual places'),
          ('“even”', 'even')]


def changed(old, new):
    a = 0
    while a < min(len(old), len(new)) and old[a] == new[a]:
        a += 1
    z = 0
    while z < min(len(old), len(new)) - a and old[len(old) - 1 - z] == new[len(new) - 1 - z]:
        z += 1
    s, e = a, len(old) - z
    while s > 0 and old[s - 1].isalnum():
        s -= 1
    while e < len(old) and old[e].isalnum():
        e += 1
    if e <= s:
        k = max(old.rfind('. ', 0, s), old.rfind('? ', 0, s))
        s, e = (k + 2 if k >= 0 else 0), len(old)
    return s, e


def card(sid, typ, pairs, title, why, stays, note, ids):
    by_block, spans = {}, []
    for old, new in pairs:
        i = sr.find_quote(BL, old)[0]
        before = BL[i]['text']
        cur = by_block.get(i, before)
        assert cur.count(old) == 1, (sid, old)
        by_block[i] = cur.replace(old, new)
        o = before.index(old)
        cs, ce = changed(old, new)
        spans.append({'block': i, 'start': o + cs, 'end': o + ce})
    what = ' '.join('"%s" becomes "%s".' % (o, n) for o, n in pairs) if all(len(o) < 160 for o, _ in pairs) else \
        'Rewrites "%s ...", as shown below.' % pairs[0][0][:60]
    return {'id': sid, 'type': typ, 'title': title, 'advice': 'approve', 'spans': spans,
            'edits': [{'block': i, 'before': BL[i]['text'], 'after': a} for i, a in by_block.items()],
            'inserts': [], 'moves': [], 'why': why, 'stays': stays, 'advice_note': note,
            'found_by': FOUND % ids, 'what': what,
            'deciding': 'Approve uses the new wording; Reject keeps it as it is; Revise lets you write your own.'}


def main():
    cards = []
    for sid, typ, _anchor, pairs, title, why, stays, note, ids in CARDS:
        cards.append(card(sid, typ, QUOTES if pairs is None else pairs, title, why, stays, note, ids))
    cards.sort(key=lambda s: min(sp['block'] for sp in s['spans']))
    review = {
        'format': sr.FORMAT, 'review_id': 'intentional-communities-emulate-check-20261025',
        'title': 'Community Emulate Check',
        'intro': [
            'This is your community article as it is in Git now (the text of the copy I sent you on 2026-10-25), with the strict Emulate check you asked for: every paragraph that isn\'t yours word for word, compared with your published post, your own answers and the edits you and GPT made in Substack.',
            'It found much less than in the hypnosis guide: no spaces before full stops, no typos of that kind, and the references are as you have them. Changes you made yourself (your Substack edits, your answers 57 to 65 and your caveat cuts) stay as they are. What\'s left is these six cards, each with your own version beside it.',
            'Click <b>Approve</b>, <b>Reject</b> or <b>Revise</b> on each card. If your post is already up with the last copy, I\'ll give you the few words to change in Substack, or a new copy, once you\'ve answered.',
        ],
        'git_file': GIT_FILE, 'article': {'file': ARTICLE, 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'links': {'guide': BLOB + 'articles/intentional-communities/master.md', 'guide_label': 'the article so far',
                  'review': BLOB + 'articles/intentional-communities/candidate/joel-20261025/emulate-check/REVIEW-EMULATE.json'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': cards,
    }
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-EMULATE.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-EMULATE.html').write_text(page, encoding='utf-8')
    print(len(cards), 'cards;', HERE / 'REVIEW-EMULATE.html', len(page), 'bytes')


if __name__ == '__main__':
    main()
