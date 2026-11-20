"""section_links.py: Substack's heading anchors, checked against anchors read from his rendered posts (lesson
inner-child-2026-11-20c). Add a pair here whenever an UNCHECKED heading's real anchor is read."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import section_links as sl  # noqa: E402

# heading words -> the anchor on the rendered page
SEEN = {
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
        self.assertEqual(sl.unchecked('Life’s a trip also'), ['’'])
        self.assertEqual(sl.unchecked('Céline on the Inner Child'), ['é'])
        self.assertEqual(sl.unchecked('Ill Will & Loving-Kindness'), ['&'])

    def test_check_flags_repeats_and_unchecked(self):
        rows = sl.check('# Safety\n\n## Noticing Counts\n\ntext\n\n### Noticing counts!\n\n## Life’s a trip also\n')
        probs = {text: p for _, text, _, p in rows}
        self.assertEqual(probs['Noticing Counts'], [])
        self.assertTrue(any('same slug' in p for p in probs['Noticing counts!']))
        self.assertTrue(any('UNCHECKED' in p for p in probs["Life's a trip also"]))  # plain() straightens quotes


if __name__ == '__main__':
    unittest.main()
