#!/usr/bin/env python3
"""apply_r47.py - his round-47 answers (the headings for Substack's contents sidebar), exported 2026-11-21 14:28 UTC
(ANSWERS-R47-20261121-1428.json), into the guide.

What it does, each from his answer:
  - every heading as his picks resolve it (humanize/h64-20261121/toc/read_answers.py worked them out again from the
    columns he saw and found them the same as the page saved): 11 in his own words, Fable's "The Feel-Good Bypass", the
    rest my pick; "How To Check For SS" in title case, his rule ("How to Check for SS"; tools/humanization/heading_case.py);
  - B65, his "remove this section for now since my app isn't ready": the Inner Signal heading and its paragraph out,
    kept word for word in REMOVED-B65.md beside this file for when the app is ready;
  - the links a heading carried stay: Coffee Cherry's on his "Coffee Cherry"; ZHoly3O's moves to "the ZHoly3O ferment" in
    the section's first line (his new heading names the zeolite ZeoCharge, linked to his post on it); his "Holy Water"
    links his ZHoly3O page, "an ozonated charcoal 'holy water'" in his own words elsewhere; "Sending Love" moves to the
    same words in the section's quote line. No word of the text changes for a link;
  - the two sentences that name a section (gate inner-child-2026-11-20c/d): "(see Mental Stabilizers That Don't Abort the
    Trip)" takes the section's new name, and both get a link to the section's anchor in his post (170920118).

  python3 articles/bad-trips/review/r47/apply_r47.py        (from the repo root)
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
REPO = ART.parents[1]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import section_links as SL  # noqa: E402

BJ, MD = ART / 'GUIDE-SO-FAR-blocks.json', ART / 'GUIDE-SO-FAR.md'
ANS = HERE / 'ANSWERS-R47-20261121-1428.json'
PICKS = ART / 'humanize' / 'h64-20261121' / 'toc' / 'HIS-PICKS.json'
POST = 'https://ibogaqueen.substack.com/i/170920118/'
ZEOCHARGE = 'https://ibogaqueen.substack.com/p/here-is-why-everyone-should-use-zeocharge'
ZHOLY = 'http://zholy3o.u-dont-exist.com/'

CASE = {'How To Check For SS': 'How to Check for SS'}          # his title-case rule (gate inner-child-2026-11-20j)
LINKED = {                                                      # heading words that keep or get a link
    'B152': '[ZeoCharge](%s) & Ferment' % ZEOCHARGE,
    'B166': '([Coffee Cherry](http://coffeecherry.u-dont-exist.com/) for Brain also)',
    'B189': 'Shungite, [Holy Water](%s)' % ZHOLY,
    'B199': '[**DMSO**](http://dmso.u-dont-exist.com/)',
}
BODY = [  # (block id, old, new): links only, no word changes, except the renamed section name in R33-SMELL-L
    ('B153', 'zeolite and the ZHoly3O ferment', 'zeolite and the [ZHoly3O](%s) ferment' % ZHOLY),
    ('B378', '> *Missing hurts. Sending love feels good.*',
     '> *Missing hurts. [Sending love](http://love.u-dont-exist.com/) feels good.*'),
    ('R33-SMELL-L', "(see Mental Stabilizers That Don't Abort the Trip)",
     '(see [Too Intense? Stabilizers](%s%s))' % (POST, SL.slug('Too Intense? Stabilizers'))),
    ('B207', '(more on that in Active Seizure)', '(more on that in [Active Seizure](%s%s))' % (POST, SL.slug('Active Seizure'))),
]


def plain_words(md):
    return re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', md).replace('**', '')


def main():
    B = json.loads(BJ.read_text(encoding='utf-8'))
    assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
    ans = json.loads(ANS.read_text(encoding='utf-8'))
    picks = json.loads(PICKS.read_text(encoding='utf-8'))
    assert {e['id']: e['heading'] for e in picks} == ans['headings'], 'his picks and the saved headings differ'
    ids = {b['id']: i for i, b in enumerate(B)}
    removed = []
    for e in picks:
        b = B[ids[e['id']]]
        m = re.match(r'^(#{1,6})\s+(.*)$', b['md'])
        assert m, (e['id'], b['md'][:60])
        if e['id'] == 'B65':
            continue
        new = LINKED.get(e['id']) or CASE.get(e['heading'], e['heading'])
        assert plain_words(new) == CASE.get(e['heading'], e['heading']), (e['id'], new)
        b['md'] = '#' * e['level'] + ' ' + new
    for bid, old, new in BODY:
        b = B[ids[bid]]
        assert b['md'].count(old) == 1, (bid, old)
        b['md'] = b['md'].replace(old, new)
    # B65, his answer: the section out (its heading and its one paragraph), kept word for word
    i = ids['B65']
    assert B[i + 1]['id'] == 'B66' and B[i + 2]['md'] == '---', [x['id'] for x in B[i:i + 3]]
    removed = B[i:i + 2]
    del B[i:i + 2]
    (HERE / 'REMOVED-B65.md').write_text(
        '# The Inner Signal section, out of the guide for now\n\n'
        'His round-47 answer (2026-11-21 14:28 UTC), for the heading "Inner Signal App to the Rescue!": "remove this section '
        'for now since my app isn\'t ready". The section as it stood, word for word, for when the app is ready (it went '
        'right after the guide\'s opening picture, before When to Get Outside Help):\n\n'
        + '\n\n'.join(b['md'] for b in removed) + '\n', encoding='utf-8')
    MD.write_text('\n\n'.join(x['md'] for x in B) + '\n', encoding='utf-8')
    BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied: %d headings, %d body edits, B65 and B66 out' % (len(picks) - 1, len(BODY)))


if __name__ == '__main__':
    main()
