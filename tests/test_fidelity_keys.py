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

    def test_his_own_wording_passes_only_once_recorded(self):
        # his version of the trial paragraph (Neuro De-Armoring Cards, 3 November, X-84); UMP is still named elsewhere
        master = MASTER + '\nThe tool: uridine monophosphate (UMP).\n'
        keys = fk.extract(master)
        his = master.replace('Trial: UMP 150–300 mg in the morning with food for 3–7 days. Do not start UMP',
                             'Do a trial with 150-300mg Uridine, in the morning with food, 3 to 7 days. Don\'t start the uridine')
        self.assertFalse(fk.check(keys, his)['pass'])
        unit = next(u['id'] for u in keys['units'] if u['what'].startswith('Do not start UMP'))
        keys['owner_wording'] = [
            {'his': '3 to 7 days', 'for': '3–7 days', 'by': 'X-84'},
            {'his': "Don't", 'for': 'do not', 'unit': unit, 'by': 'X-84'},
            {'his': 'uridine', 'for': 'UMP', 'unit': unit, 'by': 'X-84'}]
        r = fk.check(keys, his)
        self.assertTrue(r['pass'], r)
        self.assertTrue(fk.check(keys, master)['pass'])   # the master's own words still pass
        # his words stand for that warning's key only: recorded for the UMP warning, "never" doesn't stand for another
        # warning's "do not"
        keys['owner_wording'].append({'his': 'never', 'for': 'do not', 'unit': unit, 'by': 'X-84'})
        other = his.replace('Do not “push through” numbness.', 'Never “push through” numbness.')
        self.assertFalse(fk.check(keys, other)['pass'])

    def test_a_contraction_is_the_same_warning_word(self):
        self.assertTrue(fk.check(self.keys, MASTER.replace('Do not “push through”', 'Don’t “push through”'))['pass'])
        self.assertTrue(fk.check(self.keys, MASTER.replace('Do not “push through”', "Don't “push through”"))['pass'])

    def test_an_owner_wording_entry_with_no_source_or_no_key_is_an_error(self):
        unit = self.keys['units'][0]['id']
        with self.assertRaises(ValueError):
            fk.check(dict(self.keys, owner_wording=[{'his': '3 to 7 days', 'for': '3–7 days'}]), MASTER)
        with self.assertRaises(ValueError):
            fk.check(dict(self.keys, owner_wording=[{'his': 'x', 'for': 'not a key', 'unit': unit, 'by': 'X-84'}]), MASTER)

    def test_a_heading_in_capitals_is_not_a_compound(self):
        k = fk.extract('# THE SHIELD\n\nNAC: 1.8g – 2.4g (divided doses).\n')
        self.assertIn('NAC', k['terms'])
        self.assertNotIn('SHIELD', k['terms'])


if __name__ == '__main__':
    unittest.main()
