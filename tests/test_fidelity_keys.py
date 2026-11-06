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

    def test_a_limit_in_words_matches_its_sign_but_no_other_number(self):
        # "under 20g/day" says the post's "<20g/day" (neuro de-armoring, Strategy B, 2026-11-05); "under 25g/day" doesn't
        master = 'Method: You restrict carbs (<20g/day) to force your liver to produce ketones.\n'
        keys = fk.extract(master)
        self.assertTrue(fk.check(keys, 'Carbs stay under 20g/day so the liver makes the ketones itself.\n')['pass'])
        self.assertFalse(fk.check(keys, 'Carbs stay under 25g/day so the liver makes the ketones itself.\n')['pass'])
        # a plain number said with "under" stays as it was: no sign is added where the master had none
        keys90 = fk.extract('Keep it under 90 minutes.\n')
        self.assertTrue(fk.check(keys90, 'Keep it under 90 minutes.\n')['pass'])

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

    def test_what_his_approved_card_changed_is_his_and_nothing_else(self):
        """2026-11-04: he approved cards that cut warnings and changed a dose the studies support; the check reads those
        changes as his once each is recorded with the card that made it, and still fails on anything else."""
        draft = MASTER.replace('Cap at 1 g/day unless clinician-supervised.', 'Cap at 1 g/day.').replace('150–300 mg', '200 mg')
        r = fk.check(self.keys, draft)
        self.assertFalse(r['pass'])
        change = {'by': 'ANSWERS.json, card W-1', 'numbers_lost': r['numbers_lost'], 'numbers_new': r['numbers_new'],
                  'terms_lost': r['terms_lost'], 'keys_lost': {u['id']: u['missing'] for u in r['warnings_lost']}}
        keys = dict(self.keys, owner_changes=[change])
        r2 = fk.check(keys, draft)
        self.assertTrue(r2['pass'], r2)
        self.assertEqual(r2['owner_changes'], ['ANSWERS.json, card W-1'])
        self.assertFalse(fk.check(keys, draft.replace('400mg', '300mg'))['pass'])          # another change still fails
        with self.assertRaises(ValueError):
            fk.check(dict(self.keys, owner_changes=[dict(change, by='')]), draft)

    def test_a_recorded_dont_leaves_its_unit(self):
        """2026-11-06 (bad trips, round 11): his approved card changed "they don't trust" to "they're wary of" and kept
        "bathroom"; the change recorded as "don't" has to take the unit's "do not" out, or the unit's last key is matched
        to another paragraph and reported lost."""
        master = 'Intro.\n\nAre they hot, desperate for the bathroom, or beside somebody they don\'t trust?\n\nDon\'t panic.\n'
        keys = fk.extract(master)
        unit = [u for u in keys['units'] if 'bathroom' in u['what']]
        if not unit:
            self.skipTest('the extractor made no unit of the bathroom line')
        uid = unit[0]['id']
        draft = master.replace("beside somebody they don't trust", "beside someone they're wary of")
        keys = dict(keys, units=[dict(u, keys=[["don't"], ['bathroom']]) if u['id'] == uid else u for u in keys['units']])
        change = {'by': 'ANSWERS.json, card PFA-PLAIN', 'keys_lost': {uid: [["don't"]]}}
        r = fk.check(dict(keys, owner_changes=[change]), draft)
        self.assertEqual([u for u in r['warnings_lost'] if u['id'] == uid], [], r)
        self.assertFalse(fk.check(dict(keys, owner_changes=[change]), draft.replace('the bathroom', 'a break'))['pass'])

    def test_what_his_version_left_out_is_held_open_not_passed_or_lost(self):
        his = MASTER.replace('5-HTP, agmatine or', 'agmatine or')
        self.assertIn('5-HTP', fk.check(self.keys, his)['terms_lost'])
        keys = dict(self.keys, owner_open=[{'term': '5-HTP', 'by': 'his card', 'question': 'question 3'}])
        r = fk.check(keys, his)
        self.assertTrue(r['pass'], r)
        self.assertEqual([o['term'] for o in r['open_with_owner']], ['5-HTP'])
        # anything else lost still fails
        self.assertFalse(fk.check(keys, his.replace('150–300 mg', '150–250 mg'))['pass'])
        with self.assertRaises(ValueError):
            fk.check(dict(self.keys, owner_open=[{'term': '5-HTP', 'by': 'his card'}]), his)

    def test_the_typographic_swap_loses_nothing(self):
        master = MASTER + '\nDo not stay numb—living in your head is the trap.\n'
        keys = fk.extract(master)
        self.assertTrue(fk.check(keys, master.replace('numb—living', 'numb – living'))['pass'])
        self.assertTrue(fk.check(keys, master.replace('numb—living', 'numb--living'))['pass'])   # his two hyphens (E353 (Inner Child))
        fish = fk.extract('Don\'t lean on tuna daily — mercury.\n')
        self.assertTrue(fk.check(fish, 'Don\'t lean on tuna daily--mercury.\n')['pass'])   # a compound after his two hyphens
        self.assertTrue(fk.check(keys, master.replace('“push through”', '"push through"'))['pass'])

    def test_a_heading_in_capitals_is_not_a_compound(self):
        k = fk.extract('# THE SHIELD\n\nNAC: 1.8g – 2.4g (divided doses).\n')
        self.assertIn('NAC', k['terms'])
        self.assertNotIn('SHIELD', k['terms'])

    def test_his_8a_lets_a_warning_be_reworded_but_holds_its_warning_word_compounds_and_numbers(self):
        # Joel, 2026-11-04 18:10 UTC: "8a not sure why you had to ask that, the whole point is rewording stuff here"
        reworded = MASTER.replace('Do not start UMP on the same day you start 5-HTP, agmatine or',
                                  "Don't begin UMP the same day as 5-HTP, agmatine or")
        self.assertFalse(fk.check(self.keys, reworded)['pass'])          # held to the sentence's own words by default
        keys = dict(self.keys, warning_words={'rule': 'meaning', 'by': 'his answer 8a'})
        self.assertTrue(fk.check(keys, reworded)['pass'])
        self.assertFalse(fk.check(keys, reworded.replace("Don't begin UMP", 'Begin UMP'))['pass'])       # the warning word stays
        self.assertFalse(fk.check(keys, reworded.replace('5-HTP, agmatine or', '5-HTP or'))['pass'])     # a compound stays
        # a warning that names no compound and no number keeps its own words: they are what "stop" applies to
        self.assertFalse(fk.check(keys, MASTER.replace('Stop immediately if it causes flatness or increased craving.',
                                                       'Stop if you go flat.'))['pass'])

    def test_his_50mg_is_the_posts_50_mg(self):
        # Joel, 2026-11-04 18:09 UTC, on the 5-HTP trial: "don't think i've seen humans put spaces there"
        self.assertTrue(fk.check(self.keys, MASTER.replace('150–300 mg', '150-300mg'))['pass'])
        self.assertTrue(fk.check(self.keys, MASTER.replace('400mg (Night)', '400 mg (Night)'))['pass'])


if __name__ == '__main__':
    unittest.main()


class CitationsLost(unittest.TestCase):
    """Gate E378. Joel, 2026-11-06 20:17 UTC: "i didn't even see Nestler, so if i took thatout, don't assume that was on
    purpose ... don't assume a citation was removed on purpose unless it makes sense that it owuld be, ask the user if
    unsure"."""
    MASTER = ('DeltaFosB holds the circuit in place for weeks ([Nestler, 2008](https://example.org/n)). It builds up under '
              'stress ([Vialou, et al, 2010](https://example.org/v)).\n')

    def setUp(self):
        self.keys = fk.extract(self.MASTER)
        self.his = self.MASTER.replace(' ([Nestler, 2008](https://example.org/n))', '')
        r = fk.check(self.keys, self.his)
        self.assertIn('2008', r['numbers_lost'])
        self.change = {'by': 'his paragraph', 'numbers_lost': r['numbers_lost'], 'numbers_new': r['numbers_new']}

    def test_a_citation_year_his_change_took_out_needs_its_reason(self):
        r = fk.check(dict(self.keys, owner_changes=[self.change]), self.his)
        self.assertFalse(r['pass'])
        self.assertEqual(r['citations_unexplained'], [{'by': 'his paragraph', 'year': '2008'}])

    def test_a_vague_reason_is_not_one(self):
        c = dict(self.change, citations_lost=[{'cite': 'Nestler 2008', 'why': 'his rewrite dropped it'}])
        self.assertFalse(fk.check(dict(self.keys, owner_changes=[c]), self.his)['pass'])

    def test_his_words_his_card_or_a_claim_that_is_gone_pass(self):
        for why in ('he said: "cut the Nestler cite, it\'s the wrong paper"',
                    'on his card: X-1 proposed the cut and he approved it',
                    'the claim is gone: nothing in the article says it lasts weeks any more'):
            c = dict(self.change, citations_lost=[{'cite': 'Nestler 2008', 'why': why}])
            self.assertTrue(fk.check(dict(self.keys, owner_changes=[c]), self.his)['pass'], why)

    def test_the_citation_put_back_passes_with_no_entry(self):
        self.assertTrue(fk.check(self.keys, self.MASTER)['pass'])
