"""heading_case.py: AP title case for headings (lesson inner-child-2026-11-20j)."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import heading_case as hc  # noqa: E402


class HeadingCase(unittest.TestCase):
    def test_his_rule_examples(self):
        cases = {
            'Earning trust, day to day': 'Earning Trust, Day to Day',
            'Which thoughts to talk to': 'Which Thoughts to Talk To',      # last word capitalized
            'How To Let People In': 'How to Let People In',                # infinitive "to" lower case
            'AI therapy': 'AI Therapy',                                    # capitals inside a word stay
            'Goodwill: a Smaller Door': 'Goodwill: A Smaller Door',        # after a colon
            'Journal With Each Hand': 'Journal With Each Hand',            # four letters or more
            'Ask God for a Loan 🫶🏿': 'Ask God for a Loan 🫶🏿',
            'Re-do Trauma Memories': 'Re-do Trauma Memories',              # after a hyphen, as written
            'Shame Says “Unlovable”': 'Shame Says “Unlovable”',
            'Life’s a trip also': 'Life’s a Trip Also',
        }
        for before, after in cases.items():
            self.assertEqual(hc.title_case(before)[0], after, before)

    def test_particles_are_left_for_a_reader(self):
        new, amb = hc.title_case('Dip Your Toes In First')
        self.assertEqual((new, amb), ('Dip Your Toes In First', ['In']))
        self.assertEqual(hc.title_case('Show Up Just for Joy')[1], ['Up'])
        self.assertEqual(hc.title_case('“And So That’s the Way It Happened!”')[1], ['So'])
        self.assertEqual(hc.title_case('Dip your toes in first')[0], 'Dip Your Toes in First')   # lower case stays a preposition


if __name__ == '__main__':
    unittest.main()
