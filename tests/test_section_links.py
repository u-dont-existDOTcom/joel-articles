"""section_links.py: Substack's heading anchors, checked against anchors read from his rendered posts (lesson
inner-child-2026-11-20c). Add a pair here whenever an UNCHECKED heading's real anchor is read."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import section_links as sl  # noqa: E402

# heading words -> the anchor on the rendered page
SEEN = {
    # Self-Hypnosis guide, post 202810155, read on the rendered page on 2026-11-25 after the contents edit: an apostrophe,
    # curly quotes, a colon, an en dash and a comma are dropped; "&" becomes "and"
    "You're Better Than the Pros": 'youre-better-than-the-pros',
    'Is “Your Voice” Really Yours?': 'is-your-voice-really-yours',
    'Sober Induction: 3–5 Min': 'sober-induction-35-min',
    'Play & Rest, Adult Present': 'play-and-rest-adult-present',
    'H: Demons, Jinn & Presences': 'h-demons-jinn-and-presences',
    'B: Ethical NLP': 'b-ethical-nlp',
    # inner child guide, post 189761959 (turn 132, every link opened on the rendered page)
    'Noticing Counts': 'noticing-counts',
    'Chicken-and-Egg Problem': 'chicken-and-egg-problem',
    'Reframe the Critic': 'reframe-the-critic',
    'Toward Divine Love': 'toward-divine-love',
    'Re-do Trauma Memories': 're-do-trauma-memories',
    'Keeping Your Own Ground': 'keeping-your-own-ground',
    'Borrow Hindsight': 'borrow-hindsight',
    'Belonging Bargains': 'belonging-bargains',
    'If You Want to Kill Yourself': 'if-you-want-to-kill-yourself',
    'Therapy or Escapism?': 'therapy-or-escapism',
    'Ask God for a Loan 🫶🏿': 'ask-god-for-a-loan',
    'Borrowed Adulthood': 'borrowed-adulthood',
    'Similar Therapies': 'similar-therapies',
    'Internal Family Systems': 'internal-family-systems',
    'Schema Therapy': 'schema-therapy',
    # inner child guide, its 149 anchored headings as rendered on 2026-11-21 (turn 140; the rest of them in
    # articles/inner-child-therapy/experiments/t140-moves/live_anchors.txt, checked in test_live_inner_child)
    'Céline on the Inner Child': 'celine-on-the-inner-child',
    'Ill Will & Loving-Kindness': 'ill-will-and-loving-kindness',
    'Morning & Night Practice': 'morning-and-night-practice',
    'Altered States & Meditating Intensely': 'altered-states-and-meditating-intensely',
    'Between Old & New Lives': 'between-old-and-new-lives',
    'When You’re the Danger': 'when-youre-the-danger',
    'Talk to the hand!✋🏿': 'talk-to-the-hand',
    '“And So That’s the Way It Happened!”': 'and-so-thats-the-way-it-happened',
    'Write It. Don’t Send It Yet.': 'write-it-dont-send-it-yet',
    'Love Before Trust ❤️': 'love-before-trust',
    'Life’s a trip also': 'lifes-a-trip-also',
    # bad trips guide, post 170920118
    'Alone at 3 a.m.': 'alone-at-3-am',
    'Who to Contact, and When': 'who-to-contact-and-when',
    'Stillness or Movement?': 'stillness-or-movement',
    'Get One Human Anchor': 'get-one-human-anchor',
    'When the Trip Feels Amazing: Euphoric Certainty': 'when-the-trip-feels-amazing-euphoric-certainty',
    'If Someone Says "My Brain Feels Damaged": DMSO + Humic Acid First':
        'if-someone-says-my-brain-feels-damaged-dmso-humic-acid-first',
    'If Someone Says “My Brain Feels Damaged”: DMSO + Humic Acid First':
        'if-someone-says-my-brain-feels-damaged-dmso-humic-acid-first',
    'Nausea Smoothers When the Person Wants to Preserve the Trip':
        'nausea-smoothers-when-the-person-wants-to-preserve-the-trip',
    'When the Goal Is to Stop a Psychedelic Trip': 'when-the-goal-is-to-stop-a-psychedelic-trip',
    'Shadow Work and Tripsitting Yourself or Others': 'shadow-work-and-tripsitting-yourself-or-others',
}


class SectionLinks(unittest.TestCase):
    def test_seen_anchors(self):
        for heading, anchor in SEEN.items():
            self.assertEqual(sl.slug(heading), anchor, heading)
            self.assertEqual(sl.unchecked(heading), [], heading)

    def test_url(self):
        self.assertEqual(sl.url('https://ibogaqueen.substack.com/', 189761959, 'Therapy or Escapism?'),
                         'https://ibogaqueen.substack.com/i/189761959/therapy-or-escapism')

    def test_unchecked_characters_are_flagged(self):
        self.assertEqual(sl.unchecked('Pain (and Joy)'), ['(', ')'])
        self.assertEqual(sl.unchecked('Either/Or'), ['/'])
        self.assertEqual(sl.unchecked('Wait — Really'), ['—'])

    def test_live_inner_child(self):
        root = pathlib.Path(__file__).resolve().parents[1]
        rows = [l.split('\t') for l in (root / 'articles/inner-child-therapy/experiments/t140-moves/live_anchors.txt')
                .read_text(encoding='utf-8').splitlines() if l]
        self.assertEqual(len(rows), 149)
        for heading, anchor in rows:
            self.assertEqual(sl.slug(heading), anchor, heading)

    def test_check_flags_repeats_and_unchecked(self):
        rows = sl.check('# Safety\n\n## Noticing Counts\n\ntext\n\n### Noticing counts!\n\n## Either/Or\n')
        probs = {text: p for _, text, _, p in rows}
        self.assertEqual(probs['Noticing Counts'], [])
        self.assertTrue(any('same slug' in p for p in probs['Noticing counts!']))
        self.assertTrue(any('UNCHECKED' in p for p in probs['Either/Or']))


class Catalog(unittest.TestCase):
    """The catalog (lesson inner-child-2026-11-20g): a renamed heading lists every link to fix, and a stale link is caught."""

    def cat(self):
        base, post = 'https://x.substack.com', '1'
        return {'post': {'base': base, 'id': post, 'not_sent_yet': True},   # a new post keeps the /i/ form until it is sent
                'headings': [{'id': 'S1', 'level': 2, 'text': 'Attacked by a Demon?', 'anchor': 'attacked-by-a-demon'},
                             {'id': 'S2', 'level': 2, 'text': 'Noticing Counts', 'anchor': 'noticing-counts'}],
                'links': [{'in': 'S2', 'text': 'the demon section', 'target': 'S1',
                           'href': base + '/i/1/attacked-by-a-demon'},
                          {'in': 'S1', 'text': 'Noticing Counts', 'href': base + '/i/1/noticing-counts'}],
                'unlinked_on_purpose': []}

    def test_rename_lists_and_fixes_links(self):
        cat = self.cat()
        changes = sl.rename(cat, 'S1', 'Prepare for Altered States Now')
        self.assertEqual([(old, new) for _, old, new in changes],
                         [('https://x.substack.com/i/1/attacked-by-a-demon',
                           'https://x.substack.com/i/1/prepare-for-altered-states-now')])
        self.assertEqual(sl.links_check(cat), [])

    def test_a_heading_changed_outside_the_catalog_is_caught(self):
        cat = self.cat()
        cat['headings'][0].update(text='Prepare for Altered States Now', anchor='prepare-for-altered-states-now')
        probs = sl.links_check(cat)
        self.assertEqual(len(probs), 1)
        self.assertIn('is now #prepare-for-altered-states-now', probs[0][1])

    def test_rename_by_words_without_ids(self):
        cat = self.cat()
        for h in cat['headings']:
            h.pop('id')
        cat['links'][0].pop('target')
        changes = sl.rename(cat, 'Attacked by a Demon?', 'Prepare for Altered States Now')
        self.assertEqual(len(changes), 1)

    def test_inside_its_own_post_a_link_is_the_hash_form(self):
        # lesson toc-2026-11-25c: an /i/ link to the same post loads the page again; "#§slug" scrolls
        self.assertEqual(sl.anchor('Attacked by a Demon?'), '#§attacked-by-a-demon')
        self.assertEqual(sl.anchor('Introduction & Navigation'), '#§introduction-and-navigation')   # read on the Nirvāna post
        for href in ('#§my-nibbana-taxonomy', '#%C2%A7my-nibbana-taxonomy',
                     'https://x.substack.com/p/a-post?open=false#%C2%A7my-nibbana-taxonomy',
                     'https://x.substack.com/i/1/my-nibbana-taxonomy'):
            self.assertEqual(sl.anchor_of(href), 'my-nibbana-taxonomy')
        self.assertTrue(sl.same_post('#%C2%A7x') and sl.same_post('#§x') and not sl.same_post('https://x.substack.com/i/1/x'))

    def test_a_sent_posts_own_i_links_are_listed(self):
        cat = self.cat()
        cat['post'].pop('not_sent_yet')
        probs = sl.links_check(cat)
        self.assertEqual(len(probs), 2)
        self.assertIn('loads the whole page again', probs[0][1])
        for ln in cat['links']:
            ln['href'] = '#§' + sl.anchor_of(ln['href'])
        self.assertEqual(sl.links_check(cat), [])
        changes = sl.rename(cat, 'S1', 'Prepare for Altered States Now')      # a rename keeps the form the link has
        self.assertEqual([(old, new) for _, old, new in changes],
                         [('#§attacked-by-a-demon', '#§prepare-for-altered-states-now')])

    def test_build_reads_both_forms(self):
        html = ('<h2>Noticing Counts</h2><p><a href="#§therapy-or-escapism">here</a> and '
                '<a href="#%C2%A7noticing-counts">up</a> and <a href="#footnote-1">1</a>.</p><h3>Therapy or Escapism?</h3>')
        cat = sl.build(html, 'https://x.substack.com/', 1)
        self.assertEqual([ln['href'] for ln in cat['links']], ['#§therapy-or-escapism', '#%C2%A7noticing-counts'])
        self.assertEqual(sl.links_check(cat), [])

    def test_build_from_post_html(self):
        html = ('<h2>Noticing Counts</h2><p>Look <a href="https://x.substack.com/i/1/therapy-or-escapism">here</a> and '
                '<a href="https://elsewhere.com/a">there</a>.</p><h3>Therapy or Escapism?</h3><p>text</p>')
        cat = sl.build(html, 'https://x.substack.com/', 1, source='test')
        cat['post']['not_sent_yet'] = True
        self.assertEqual([h['anchor'] for h in cat['headings']], ['noticing-counts', 'therapy-or-escapism'])
        self.assertEqual(cat['links'], [{'in': 'Noticing Counts', 'text': 'here',
                                         'href': 'https://x.substack.com/i/1/therapy-or-escapism'}])
        self.assertEqual(sl.links_check(cat), [])

    def test_every_push_names_the_posts_with_links_that_reload(self):
        # lane_push.py prints these lines, so the lane that owns a post sees them (Joel, 2026-11-25 16:14 UTC: "on
        # there would be fixing the anchor links for the other guides")
        import json, pathlib, tempfile
        post = {'base': 'https://x.substack.com', 'id': '1'}
        heads = [{'level': 2, 'text': 'Noticing Counts', 'anchor': 'noticing-counts'}]
        old = {'post': post, 'headings': heads, 'links': [{'in': 'A', 'text': 'here',
                                                           'href': 'https://x.substack.com/i/1/noticing-counts'}]}
        new = {'post': post, 'headings': heads, 'links': [{'in': 'A', 'text': 'here', 'href': '#§noticing-counts'}]}
        with tempfile.TemporaryDirectory() as d:
            for name, cat in (('old-form', old), ('fixed', new)):
                f = pathlib.Path(d, 'articles', name)
                f.mkdir(parents=True)
                (f / 'SECTION-LINKS.json').write_text(json.dumps(cat), encoding='utf-8')
            (pathlib.Path(d, 'articles', 'broken')).mkdir()
            pathlib.Path(d, 'articles', 'broken', 'SECTION-LINKS.json').write_text('{not json', encoding='utf-8')
            lines = sl.notice_lines(d)
        self.assertEqual(len(lines), 2)
        self.assertTrue(lines[0].startswith('broken: not read'))
        self.assertTrue(lines[1].startswith('old-form: 1 links to sections of the same post'))


if __name__ == '__main__':
    unittest.main()
