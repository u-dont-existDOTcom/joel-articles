"""Put his version of SC-48b into HUMANIZED-SO-FAR.md (his answers on x1111c, exported 2026-11-12 18:23 UTC:
ANSWERS-X1111C-20261112-1823.json, SC-48b to revise with his version).

His version is the card's paragraph with a clause added to its last sentence: the forum reviews of BHB salts (his link to a
Reddit thread on brain injury repair), the salts working for rats with trauma, and the salts not nearly as proven in people
as the keto diet (Engelhardt, et al 2026, the integrative review). It goes in as he wrote it, with only these fixes, each
recorded:

- the page shows his version as plain text, so the citations' links are put back where they were;
- "[brain injury repai]r (https://...)": the link's bracket closed a letter early and a space split it from its address;
- "the salts works": "the salts work";
- "[(Engelhardt, et al 2026](https://...))": the bracket put after the parenthesis, with the comma the article's citations
  have ("Engelhardt, et al, 2026");
- the full stop his sentence ends without.

Reddit is blocked to this session's tools as content, so the thread wasn't read; the link is his. Two of the clause's
points are checked against the review he cites in KETO-PTSD.md, and what the review says differently goes to him on
card SC-48c, not into this script.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/keto/apply_x1111c.py [--write]
"""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
sys.path.insert(0, str(HERE))
import texts_x1111c as T  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
ANSWERS = HERE / 'ANSWERS-X1111C-20261112-1823.json'
REDDIT = 'https://www.reddit.com/r/keto/comments/1fmu0po/ketone_supplements_insanely_good/'
ENGELHARDT = 'https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2026.1854499/full'
YOUSSEF_MD = '([Youssef, et al, 2022](%s)).' % T.YOUSSEF
ADDED = (', although we can see some astounding BHB salt reviews on forums, like for [brain injury repair](%s), and the '
         'salts work for rats with trauma, although not nearly as proven for humans as the keto diet is ([Engelhardt, et '
         'al, 2026](%s)).' % (REDDIT, ENGELHARDT))
FIXES = [
    {'was': '[brain injury repai]r (%s)' % REDDIT, 'now': '[brain injury repair](%s)' % REDDIT,
     'why': 'the link\'s bracket closed a letter early and a space split it from its address'},
    {'was': 'the salts works', 'now': 'the salts work', 'why': 'a typo'},
    {'was': '[(Engelhardt, et al 2026](%s))' % ENGELHARDT, 'now': '([Engelhardt, et al, 2026](%s))' % ENGELHARDT,
     'why': 'the bracket after the parenthesis, with the comma the article\'s citations have'},
    {'was': '(the sentence ends without a full stop)', 'now': '.', 'why': 'the full stop'},
    {'was': '(Shimazu, et al, 2013) ... (Youssef, et al, 2022), as plain text', 'now': 'each with its link',
     'why': 'the page shows his version as plain text; the citations\' links put back where they were'},
]


def plain(md):
    return re.sub(r'\[([^\]]+)\]\(((?:[^()\s]|\([^()\s]*\))+)\)', r'\1', md)


def main(write=False):
    md = ARTICLE.read_text(encoding='utf-8')
    a = json.loads(ANSWERS.read_text(encoding='utf-8'))
    (item,) = [x for x in a['items'] if x['id'] == 'SC-48b']
    assert a['article']['sha256'] == hashlib.sha256(md.encode('utf-8')).hexdigest(), 'the article changed since the card'
    assert item['status'] == 'revise' and item['your_version'].startswith(T.plain(T.HIS))
    lines = md.split('\n')
    hits = [i for i, l in enumerate(lines) if l.startswith(T.START)]
    assert len(hits) == 1
    i = hits[0]
    new = lines[i].replace(T.OLD, T.NEW)
    assert new.count(YOUSSEF_MD) == 1 and new.endswith(YOUSSEF_MD)
    new = new[:-len(YOUSSEF_MD)] + YOUSSEF_MD[:-1] + ADDED
    # his version, with the fixes above, word for word: what goes in is his text and nothing else
    his = item['your_version']
    for f in FIXES[:3]:
        assert his.count(f['was']) == 1, f['was']
        his = his.replace(f['was'], f['now'])
    his = plain(his) + '.'
    assert plain(new) == his, (plain(new)[-300:], his[-300:])
    out = '\n'.join(lines[:i] + [new] + lines[i + 1:])
    rec = {'about': 'SC-48b as he revised it (his version), with the fixes listed; answers exported 2026-11-12 18:23 UTC',
           'answers': ANSWERS.name, 'card': 'SC-48b', 'status': 'revise', 'line': i + 1,
           'old': lines[i], 'new': new, 'fixes': FIXES, 'reddit_read': False,
           'why_not_read': 'Reddit is blocked to the web tools as content; the restriction covers every tool, the browser too',
           'checked_after': 'KETO-PTSD.md, "His clause, checked"; what the review says differently is on card SC-48c',
           'before_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(),
           'after_sha256': hashlib.sha256(out.encode('utf-8')).hexdigest()}
    print(new[-420:])
    print('after', rec['after_sha256'][:8])
    if write:
        ARTICLE.write_text(out, encoding='utf-8')
        (HERE / 'APPLIED-X1111C.json').write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main('--write' in sys.argv)
