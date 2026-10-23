"""Tests for tools/humanization/lane_push.py's arguments (2026-10-23: "--add TOOL --add TEST" committed only the test, so
the tool change it tests stayed out of the commit, and the checks, which run on the working tree, passed anyway)."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import lane_push as P  # noqa: E402


class Arguments(unittest.TestCase):
    def test_each_add_adds_to_the_list(self):
        a = P.parser().parse_args(['subject', '--add', 'tools/x.py', '--add', 'tests/test_x.py', 'docs/y.md'])
        self.assertEqual(a.add, ['tools/x.py', 'tests/test_x.py', 'docs/y.md'])

    def test_no_add_is_an_empty_list(self):
        self.assertEqual(P.parser().parse_args(['subject']).add, [])


if __name__ == '__main__':
    unittest.main()
