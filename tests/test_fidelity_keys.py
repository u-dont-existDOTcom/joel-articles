"""fidelity_keys.py holds a protocol article's doses, units, timings, compounds and warnings to the master (the queue's rule
for neuro de-armoring: "Every compound, dose, unit, timing and warning must come out exactly as it went in")."""
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import fidelity_keys as fk  # noqa: E402

MASTER = """# Part 2

Trial: UMP 150–300 mg in the morning with food for 3–7 days. Do not start UMP on the same day you start 5-HTP, agmatine or
ketamine.

Stop immediately if it causes flatness or increased craving. Do not “push through” numbness. If agmatine makes the world
more gray, it is the wrong tool.

Magnesium Glycinate: 400mg (Night). Cap at 1 g/day unless clinician-supervised. Weeks 1–2: the storm.
"""


class FidelityKeys(unittest.TestCase):
    def setUp(self):
        self.keys = fk.extract(MASTER)

    def test_the_master_passes_and_dashes_are_one_kind(self):
        self.assertTrue(fk.check(self.keys, MASTER)['pass'])
        self.assertTrue(fk.check(self.keys, MASTER.replace('150–300 mg', '150-300 mg'))['pass'])

    def test_a_changed_dose_fails(self):
        r = fk.check(self.keys, MASTER.replace('150–300 mg', '150–250 mg'))
        self.assertEqual(r['numbers_lost'], ['150-300mg'])
        self.assertEqual(r['numbers_new'], ['150-250mg'])
        self.assertFalse(r['pass'])

    def test_a_dose_said_another_way_fails(self):
        self.assertFalse(fk.check(self.keys, MASTER.replace('150–300 mg', '150 to 300 mg'))['pass'])

    def test_a_lost_warning_fails_even_when_another_do_not_stays(self):
        r = fk.check(self.keys, MASTER.replace('Do not “push through” numbness. ', ''))
        self.assertTrue(any('numbness' in u['what'] for u in r['warnings_lost']))
        self.assertFalse(r['pass'])

    def test_a_lost_compound_fails(self):
        r = fk.check(self.keys, MASTER.replace('5-HTP, agmatine or', 'agmatine or'))
        self.assertIn('5-HTP', r['terms_lost'])
        self.assertFalse(r['pass'])

    def test_a_timing_word_kept_with_its_number(self):
        self.assertIn('Weeks1-2', self.keys['numbers'])
        self.assertFalse(fk.check(self.keys, MASTER.replace('Weeks 1–2', 'Weeks 1–3'))['pass'])

    def test_a_heading_in_capitals_is_not_a_compound(self):
        k = fk.extract('# THE SHIELD\n\nNAC: 1.8g – 2.4g (divided doses).\n')
        self.assertIn('NAC', k['terms'])
        self.assertNotIn('SHIELD', k['terms'])


if __name__ == '__main__':
    unittest.main()
