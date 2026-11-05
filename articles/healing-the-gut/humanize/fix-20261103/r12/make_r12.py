#!/usr/bin/env python3
"""r12: r11 with Joel's batch-8 answers (2026-11-04 21:01 UTC, experiments/t11-answers/): all 22 approved as they were, no
revisions or comments. Each card's change goes in word for word, and every changed block is checked equal to the card's
"my_version" (the paragraph as it would read, which he approved), in the Markdown and in the HTML. Writes r12.md and
r12.html. No API calls."""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
sys.path.insert(0, str(FIX / 'live'))
import suggestion_review as sr  # noqa: E402
from make_plan import blocks as html_blocks  # noqa: E402

ANS = json.loads((REPO / 'articles' / 'healing-the-gut' / 'experiments' / 't11-answers' /
                  'joel-20261104-2101-b8-answers.json').read_text(encoding='utf-8'))
assert ANS['counts'] == {'approved': 22, 'rejected': 0, 'revise': 0, 'pending': 0}
# the cards' changes (r11/b8/build_review.py), old -> new, each once in its block
PAIRS = {
 'F8-1': [('based one one incompleted clinical trial', 'based on one incomplete clinical trial'),
          ('Glutamine an amino acid', 'Glutamine is an amino acid')],
 'F8-2': [('with regard vitamins', 'with regard to vitamins')],
 'F8-3': [('jungtions', 'junctions')],
 'F8-4': [('For H. Pylori specifically', 'For H. pylori specifically'), ("that's usually H. Pylori", "that's usually H. pylori")],
 'F8-5': [('Endsickness.org', 'EndSickness.org')],
 'F8-6': [("with something that those don't help quickly", "with something that H2O2 and berberine don't clear quickly")],
 'F8-7': [('BIND to the toxins', 'BIND the toxins')],
 'F8-8': [('can cement other stress vectors', 'can cement the stress coming from those other vectors')],
 'F8-9': [('which stays in your intestinal gaps', 'which sticks to your intestinal lining')],
 'F8-10': [('his urine pH testing for anabolic/catabolic state freezes',
            'his urine pH testing for whether your body is frozen in a building-up or a breaking-down state (anabolic or catabolic)')],
 'F8-11': [("don't do that, the barrier loosens up", "don't get that energy, the barrier loosens up")],
 'F8-12': [('preventing the dangerous escape of substances from gut to blood, which then turns down inflammatory signals that '
            'would be needed otherwise to contain the damage',
            "so dangerous substances can't escape from gut to blood, and your body can turn down the inflammatory signals it "
            'would otherwise need to contain the damage')],
 'F8-13': [('But glutamine is still the main thing they need', 'But glutamine is still the main thing your enterocytes need')],
 'F8-14': [("you'll get a herx reaction you can't detoxify",
            "you'll get a herx reaction: the dying microbes release toxins you can't detoxify")],
 'F8-15': [('and take butyrate itself or something that helps short-chain fatty acid production, especially the main one, butyrate.',
            'and take something that helps short-chain fatty acid production, especially the main one, butyrate, or take butyrate itself.')],
 'F8-16': [("Other serious signs to note: If you're losing weight fast, or if you have severe pain, a fever or dehydration.",
            'Other serious signs to note: losing weight fast, severe pain, a fever or dehydration.')],
 'F8-17': [('So the phases below are only what the Gem will tell you, from the nine books.',
            'So the phases below are what the Gem will tell you, from the nine books (apart from my H2O2 swap in Phase 3).')],
 'F8-18': [("Don't skip any, since", "Don't skip ahead, since")],
 'F8-19': [('organ failure, or environmental toxicity or brain plasticity',
            "an organ that isn't working right, or environmental toxicity or your brain's false danger signals")],
 'F8-20': [('(Phase 1):', '(Phase 1 of the recipe below):')],
 'F8-21': [('(closest: Phase 4)', '(not in the phases, but Phase 4 comes closest)')],
 'F8-22': [('see Severe stress above', 'see "Severe stress" above'), ('see Low stomach acid.', 'see "Low stomach acid".'),
           ('see Poor diet now and Plant foods, above', 'see "Poor diet now" and "Plant foods", above'),
           ('see Leaky gut above', 'see "Leaky gut" above'), ('and Sitting above for movement', 'and "Sitting" above for movement')],
}
# F8-20's "(Phase 1):" occurs twice in the article (also "Low stomach acid ... (Phase 1):"); the card is on the first
FIRST_ONLY = {'(Phase 1):'}


def apply(text, what):
    for item in ANS['items']:
        for old, new in PAIRS[item['id']]:
            n = text.count(old)
            if old in FIRST_ONLY:
                assert n >= 1, (what, item['id'], old, n)
                text = text.replace(old, new, 1)
            else:
                assert n == 1, (what, item['id'], old, n)
                text = text.replace(old, new)
    return text


md = apply((FIX / 'r11' / 'r11.md').read_text(encoding='utf-8'), 'md')
html = apply((FIX / 'r11' / 'r11.html').read_text(encoding='utf-8'), 'html')

# every approved paragraph, as he approved it, is now a block of the Markdown and of the HTML
squash = lambda s: re.sub(r'\s+', '', s)
md_blocks = [squash(b['text']) for b in sr.blocks(md)]
hb = ''.join(html_blocks(html))  # an HTML list item can hold two paragraphs where the Markdown has one block
for item in ANS['items']:
    for para in item['my_version'].split('\n\n'):
        assert squash(para) in md_blocks, ('md', item['id'], para[:60])
        assert squash(para) in hb, ('html', item['id'], para[:60])
    for para in item['before'].split('\n\n'):
        assert squash(para) not in md_blocks, ('md still has', item['id'], para[:60])
for name, t in (('r12.md', md), ('r12.html', html)):
    (HERE / name).write_text(t, encoding='utf-8')
    print(name, hashlib.sha256(t.encode('utf-8')).hexdigest())
