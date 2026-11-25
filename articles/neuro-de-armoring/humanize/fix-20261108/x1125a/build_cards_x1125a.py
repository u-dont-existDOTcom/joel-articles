"""The cards page of 2026-11-25 (review x1125a): three warnings at the top whose texts of mine read AI by themselves in
every try, as teaching cards (lesson bad-trips-2026-11-14b; gate bad-trips-2026-11-07c): the Isolation Trap (W-ISO,
three tries), the Agmatine Warning's first paragraph (W-AGMINTRO, three tries) and the warning for psychedelic users
(W-HTPTOP, three tries; the card shows the closest, try 2). Texts: texts_x1125a.V8 (iso, agm) and V7 (htp).

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1125a/build_cards_x1125a.py
"""
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parent
H = FIX.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import suggestion_review as sr  # noqa: E402
import texts_x1125a as T  # noqa: E402

BRANCH = 'claude/community-joel-1018'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/%s/' % BRANCH
LANE = 'articles/neuro-de-armoring/humanize/'
REL = LANE + 'fix-20261108/x1125a/'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
PG = 'https://www.pangram.com/history/'
ISO = [('2bef0402-3916-4f9c-b1cd-2678afe1b0fd', '100% AI'), ('e4fe5ff4-a18f-4149-9012-602e43efe756', '100% AI'),
       ('11c50d40-e436-4393-be4f-522934cc9c33', '100% AI')]
AGM = [('61e59dc5-7acd-488f-be9d-6277cdbdc2d4', '100% AI'), ('08c6a4d2-9228-4ddd-a038-6988c2a72769', '100% AI'),
       ('2829fcb4-fcf2-4f52-b75d-70268695285b', '100% AI')]
HTP = [('de9dc2c7-5af6-4ab3-8070-fbd0eaf7fc0d', '84.9% AI'), ('1b3bfd01-d122-4085-ad46-3824d7028a01', '67.2% AI'),
       ('b0b8ebed-8061-4fc0-a1b3-f37c57705130', '100% AI')]


def tries(rows):
    return '; '.join('try %d [%s](%s%s)' % (n, r, PG, u) for n, (u, r) in enumerate(rows, 1))


def panel(*names):
    return ' and '.join('[%s](%s%s%s/PANEL.md)' % (lab, BLOB, REL, d) for d, lab in names)


def main():
    bl = sr.blocks(MD, whole=True)

    def blk(start):
        (i,) = [b['i'] for b in bl if b['text'].startswith(start)]
        return i, (sr.block_text(bl, i) if hasattr(sr, 'block_text') else bl[i]['text'])
    iso_i, iso_old = blk('Behavioral Warning (The Isolation Trap):')
    agm_i, agm_old = blk('Agmatine Warning (The Voltage Governor):')
    htp_i, htp_old = blk('Uridine & 5-HTP Warning for Psychedelic Users:')
    common = {'type': 'teach', 'advice': 'approve', 'approve_label': 'use mine anyway',
              'deciding': 'Your version of this paragraph: it goes in as yours.'}
    iso = dict(common, **{
        'id': 'W-ISO', 'title': 'The Isolation Trap: three tries, all AI',
        'spans': [{'block': iso_i, 'start': 0, 'end': len(iso_old)}],
        'edits': [{'block': iso_i, 'before': iso_old, 'after': T.V8['iso']}],
        'what': ('The Isolation Trap warning: what the protocol has you cut, the trap in that (holing up alone), the '
                 'don\'t with its reason, and what to keep (people around you, the calm kind of company).'),
        'why': ('I can\'t find any more AI tells here that are mine, and I see some human tells, like these: "hole up '
                'alone", "But do not isolate completely", "locks the armor in place". Can you help show me the tells '
                'I\'m missing? Three tries by itself, each one window, AI High: %s. Two fresh readers marked the tells '
                'they saw before the third try and again on its draft (%s). What they still agree on is in the post '
                'itself: the label, the bracket after "Phasic" Dopamine, "the chronic stress hormone", and the order '
                '(warning, mechanism, remedy).' % (tries(ISO), panel(('panel-iso', 'the panel'),
                                                                      ('panel-iso8', 'its second read')))),
        'reading': 'No try had a Human window: each read as one window, AI High (the first: [100%% AI](%s%s)).' % (PG, ISO[0][0]),
        'tested': 'This version (try 3) by itself: [AI Generated, 100%% AI](%s%s), one window, High.' % (PG, ISO[2][0]),
        'stays': ('Every term the post has: "Phasic" Dopamine with its bracket, cortisol with its gloss, glutamate, the '
                  '"Oxytocinergic Anchoring", and the don\'t. The Rule after it, as it is.'),
        'advice_note': ('Revise, with your version. One thing mine leaves out, so say if it should stay: "because humans '
                        'are social animals" (the sentence before it already gives the reason, that isolation spikes '
                        'cortisol). One thing it adds: that holing up alone is the easiest way to cut the dopamine, '
                        'which is why the warning is there.'),
        'ask_because': 'downside: three Pangram tries read AI by themselves, so mine can\'t go in',
        'found_by': 'The humanizing pass of 2026-11-25; three checks in his Pangram account',
        'receipt': [REL + 'v8/ISO8.receipt.json']})
    agm = dict(common, **{
        'id': 'W-AGMINTRO', 'title': 'What agmatine is (the Agmatine Warning\'s first paragraph): three tries, all AI',
        'spans': [{'block': agm_i, 'start': 0, 'end': len(agm_old)}],
        'edits': [{'block': agm_i, 'before': agm_old, 'after': T.V8['agm']}],
        'what': ('The first paragraph of the Agmatine Warning: agmatine is optional, it\'s sold as a supplement but is a '
                 'neuromodulator, what it\'s in the protocol for, and why it can interact with far more medications '
                 'than a nutrient would. Your precautions follow it, as they are.'),
        'why': ('I can\'t find any more AI tells here that are mine, and I see some human tells, like these: "although '
                'it\'s sold as a supplement", "a lot more medications than ... would". Can you help show me the tells '
                'I\'m missing? Three tries by itself, each one window, AI High: %s. Two fresh readers marked the tells '
                'they saw before the third try and again on its draft (%s). What they still agree on is in the post '
                'itself: the label, the two nutrients set side by side, and the pathway names with their slashes.'
                % (tries(AGM), panel(('panel-agm', 'the panel'), ('panel-agm8', 'its second read')))),
        'reading': 'No try had a Human window: each read as one window, AI High (the first: [100%% AI](%s%s)).' % (PG, AGM[0][0]),
        'tested': 'This version (try 3) by itself: [AI Generated, 100%% AI](%s%s), one window, High.' % (PG, AGM[2][0]),
        'stays': ('Every name the post has: magnesium, phosphatidylcholine, NMDA/glutamate signaling, imidazoline/alpha-2 '
                  'adrenergic tone, nitric-oxide pathways, opioid reward/tolerance. Your Precautions paragraph after it, '
                  'which read Human High as it stands.'),
        'advice_note': ('Revise, with your version. Three things mine adds, so say if any should go: "optional" and "a '
                        'brake on NMDA/glutamate signaling" (both from your Shield section), "sold as a supplement", '
                        'and the closing point that it can interact with a lot more medications than a nutrient '
                        'would. It leaves out "multi-target".'),
        'ask_because': 'downside: three Pangram tries read AI by themselves, so mine can\'t go in',
        'found_by': 'The humanizing pass of 2026-11-25; three checks in his Pangram account',
        'receipt': [REL + 'v8/AGM8.receipt.json']})
    htp = dict(common, **{
        'id': 'W-HTPTOP', 'title': 'The 5-HTP warning for psychedelic users: three tries, none Human',
        'spans': [{'block': htp_i, 'start': 0, 'end': len(htp_old)}],
        'edits': [{'block': htp_i, 'before': htp_old, 'after': T.V7['htp']}],
        'what': ('The warning for people who use psychedelics: the two supplements aren\'t trip enhancers and can change '
                 'how strongly a trip hits; 5-HTP and serotonin syndrome; the list of what never to take it with; the '
                 'rule for trip days, ayahuasca and iboga, and the reason for those two.'),
        'why': ('I can\'t find any more AI tells here that I know how to fix, and I see some human tells, like these: '
                '"hit you", "is how people end up with serotonin syndrome", "iboga microdoses included". Can you help '
                'show me the tells I\'m missing? Three tries by itself: %s. Try 2, the one shown, had the list at Human '
                'High and the rule at Human Medium. In try 3 I said the danger the way the 5-HTP '
                'section says it and tied ayahuasca to the list ("its harmalas are MAOIs themselves"), and every window went to '
                'AI, the list too, so I don\'t know what carries it. Two fresh readers marked the tells they saw in try '
                '2 (%s).' % (tries(HTP), panel(('panel-htp7', 'the panel')))),
        'reading': ('The closest try is this one (try 2): [AI Detected, 67.2%% AI](%s%s): the first sentence AI Low, the '
                    'next two AI High, the list Human High, the rule Human Medium, the last sentence AI High.' % (PG, HTP[1][0])),
        'tested': ('This version (try 2) by itself: [AI Detected, 67.2%% AI](%s%s). Every try with each window: [the '
                   'checks](%s%schecks-1125d/RESULTS.md) and [the last batch](%s%schecks-1125e/RESULTS.md).'
                   % (PG, HTP[1][0], BLOB, REL, BLOB, REL)),
        'stays': ('Every compound in the list, as the post names it; the rule; the uridine paragraph after it, which read '
                  'Human High.'),
        'advice_note': ('Revise, with your version. What mine adds, so say if any should go: "so don\'t count on your '
                        'usual dose acting the way it used to", "which can be deadly" (from your 5-HTP section), '
                        '"psychedelics act on serotonin too" and "iboga microdoses included" (both from your Weeks 3–7 '
                        'line). It leaves out "or other serotonin-raising stacks" from the end of the list: say if you '
                        'want it back.'),
        'ask_because': 'downside: three Pangram tries read AI by themselves, and it rewords the post\'s warning',
        'found_by': 'The humanizing pass of 2026-11-25; three checks in his Pangram account',
        'receipt': [REL + 'v7/HTP7-MD.receipt.json']})
    cards = [iso, agm, htp]
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261125-x1125a',
        'title': 'Neuro De-Armoring Cards, 25 November: three warnings at the top, for you to teach me',
        'intro': ['The Isolation Trap, what agmatine is, and the 5-HTP warning for psychedelic users: every try of mine '
                  'read AI by itself. It\'s the whole article, so you can read each where it goes.',
                  'Three cards. No compound, dose, unit or timing changes anywhere.'],
        'git_file': REL + 'REVIEW-X1125A.html',
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'whole': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': 'https://ibogaqueen.substack.com/p/trauma-and-addiction-why-neurological',
                  'guide_label': 'your live post', 'review': BLOB + REL + 'REVIEW-X1125A.md'},
        'types': {'teach': {'label': 'For you to teach me',
                            'about': 'A text of mine whose Pangram tries read AI: my best tested version, the tells I see, '
                                     'and room for yours.'}},
        'suggestions': cards,
    }
    bad = ['PROBLEM ' + x for x in sr.check(review, bl)]
    (HERE / 'REVIEW-X1125A.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for x in bad:
        print(x)
    if bad:
        return 1
    page = sr.page(review, MD, bl)
    (HERE / 'REVIEW-X1125A.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1125A.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    out = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    for card, i in ((iso, iso_i), (agm, agm_i), (htp, htp_i)):
        out += ['## %s: %s' % (card['id'], card['title']), '', '*In place of %s*' % sr.where(bl, i), '',
                '**As it would read:**', '', '> %s' % card['edits'][0]['after'], '',
                '**What it says:** %s' % card['what'], '', '**Why I\'m asking:** %s' % card['why'], '',
                '**The closest try:** %s' % card['reading'], '', '**This version:** %s' % card['tested'], '',
                '**What stays:** %s' % card['stays'], '', '**You\'re deciding:** %s' % card['deciding'], '',
                '**My advice:** %s' % card['advice_note'], '']
    (HERE / 'REVIEW-X1125A.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('ok', iso_i, agm_i, htp_i)
    return 0


if __name__ == '__main__':
    sys.exit(main())
