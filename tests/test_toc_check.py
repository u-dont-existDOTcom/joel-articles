import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'tools', 'humanization'))
import toc_check as T  # noqa: E402


SS = [
    {'id': 'A', 'level': 1, 'heading': 'Medical Emergencies'},
    {'id': 'B', 'level': 2, 'heading': 'Serotonin Syndrome (SS)?'},
    {'id': 'C', 'level': 3, 'heading': 'Is It Serotonin Toxicity?'},
    {'id': 'D', 'level': 3, 'heading': 'Do This Immediately'},
    {'id': 'E', 'level': 2, 'heading': 'Chest Pain and Injury'},
]


class TocCheckTest(unittest.TestCase):
    def test_a_child_that_repeats_its_parent_is_listed(self):
        # lesson bad-trips-2026-11-21a: "why would you put 2 serotonin syndrome headings in a row"
        found = T.repeats(SS)
        self.assertIn(('C', 'parent', 'B', ['serotonin']), found)

    def test_headings_that_say_different_things_are_not_listed(self):
        fixed = [dict(e) for e in SS]
        fixed[2]['heading'], fixed[3]['heading'] = 'How to Recognize It', 'What to Do Right Away'
        self.assertEqual(T.repeats(fixed), [])

    def test_a_plural_matches_its_singular(self):
        found = T.repeats([{'id': 'X', 'level': 1, 'heading': 'My Acute Rescue Remedies'},
                           {'id': 'Y', 'level': 2, 'heading': 'Remedy Cautions'}])
        self.assertEqual(found, [('Y', 'parent', 'X', ['remedy'])])

    def test_every_candidate_needs_a_fate(self):
        lines, missing = T.check(SS, {'D': ['names no problem']}, {'repeat:C': 'changed: How to Recognize It'})
        self.assertEqual(missing, ['hard:D'])
        lines, missing = T.check(SS, {'D': ['names no problem']},
                                 {'repeat:C': 'changed: How to Recognize It', 'hard:D': 'kept'})
        self.assertEqual(missing, ['hard:D'])   # "kept" needs its reason
        lines, missing = T.check(SS, {'D': ['names no problem']},
                                 {'repeat:C': 'changed: How to Recognize It',
                                  'hard:D': 'changed: What to Do Right Away'})
        self.assertEqual(missing, [])

    def test_hard_lines_are_read_from_the_reads(self):
        with tempfile.TemporaryDirectory() as d:
            json.dump([{'n': i + 1, 'id': e['id']} for i, e in enumerate(SS)], open(os.path.join(d, 'LINES-X.json'), 'w'))
            with open(os.path.join(d, 'READ-X-1.txt'), 'w') as f:
                f.write('1 | 2 | sure | 3\nHARD: 4 | names no problem\nHARD: 99 | not a line\n')
            self.assertEqual(T.hard(d, 'X'), {'D': ['names no problem']})


if __name__ == '__main__':
    unittest.main()
