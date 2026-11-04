"""Tests for tools/humanization/lane_push.py's arguments (2026-10-23: "--add TOOL --add TEST" committed only the test, so
the tool change it tests stayed out of the commit, and the checks, which run on the working tree, passed anyway)."""
import pathlib
import sys
import subprocess
import unittest
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import lane_push as P  # noqa: E402


class Arguments(unittest.TestCase):
    def test_each_add_adds_to_the_list(self):
        a = P.parser().parse_args(['subject', '--add', 'tools/x.py', '--add', 'tests/test_x.py', 'docs/y.md'])
        self.assertEqual(a.add, ['tools/x.py', 'tests/test_x.py', 'docs/y.md'])

    def test_no_add_is_an_empty_list(self):
        self.assertEqual(P.parser().parse_args(['subject']).add, [])


class LaneIntegration(unittest.TestCase):
    """Gate E339 (Joel, 2026-11-04 00:37 UTC: "make sure no other lane can make the same mistake you made next time"):
    the gut lane never merged main, opened no pull request and changed a shared test another open pull request changed."""

    def test_shared_files_are_the_rules_and_tools_not_an_articles_folder(self):
        self.assertEqual(P.shared(['tools/humanization/x.py', 'docs/GATE.md', 'articles/gut/a.md', 'AGENTS.md',
                                   'state/MAILBOX.json', 'articles/INDEX.json', 'tests/test_x.py']),
                         ['AGENTS.md', 'docs/GATE.md', 'tests/test_x.py', 'tools/humanization/x.py'])

    def test_overlaps_name_each_other_pull_request_and_the_files(self):
        mine = ['tools/humanization/suggestion_review_browser_test.py', 'articles/gut/a.md', 'state/MAILBOX.json']
        others = {280: ('claude/bad-trips-20261103', ['tools/humanization/suggestion_review_browser_test.py',
                                                      'state/MAILBOX.json']),
                  278: ('chat/inner-child', ['state/tasks/x.md'])}
        self.assertEqual(P.overlaps(mine, others), {280: ['tools/humanization/suggestion_review_browser_test.py']})

    def fake(self, behind):
        def run(cmd, check=True, timeout=600):
            rc, out = 0, ''
            if cmd[:3] == ['git', 'merge-base', '--is-ancestor']:
                rc = 1 if behind else 0
            elif cmd[:2] == ['git', 'log']:
                out = 'abc one\ndef two\n'
            elif cmd[:2] == ['git', 'diff']:
                out = 'docs/HUMANIZATION-GATE.md\narticles/x/a.md\n'
            elif cmd[:3] == ['git', 'rev-parse', '--abbrev-ref']:
                out = 'claude/lane\n'
            return subprocess.CompletedProcess(cmd, rc, out, '')
        return run

    def test_main_not_merged_refuses_and_names_the_shared_files(self):
        with mock.patch.object(P, 'run', self.fake(behind=True)):
            with self.assertRaises(SystemExit) as e:
                P.main_gate()
        self.assertIn('git merge origin/main', str(e.exception))
        self.assertIn('docs/HUMANIZATION-GATE.md', str(e.exception))

    def test_main_merged_passes(self):
        with mock.patch.object(P, 'run', self.fake(behind=False)):
            self.assertEqual(P.main_gate(), '')

    def test_no_pull_request_and_no_pr_option_refuses(self):
        a = P.parser().parse_args(['subject'])
        with mock.patch.object(P, 'run', self.fake(behind=False)), \
                mock.patch.object(P, 'open_pulls', return_value={280: ('claude/other', ['docs/x.md'])}):
            with self.assertRaises(SystemExit) as e:
                P.integration_gate(a)
        self.assertIn('no open pull request', str(e.exception))

    def test_an_overlap_refuses_until_it_says_how_it_builds_on_theirs(self):
        pulls = {280: ('claude/other', ['docs/HUMANIZATION-GATE.md']), 282: ('claude/lane', ['articles/x/a.md'])}
        with mock.patch.object(P, 'run', self.fake(behind=False)), mock.patch.object(P, 'open_pulls', return_value=pulls):
            with self.assertRaises(SystemExit) as e:
                P.integration_gate(P.parser().parse_args(['subject']))
            self.assertIn('#280', str(e.exception))
            notes = P.integration_gate(P.parser().parse_args(['subject', '--overlap-ok', 'adds a line after theirs']))
        self.assertTrue(any('#280' in n for n in notes))

    def test_github_unreachable_warns_and_does_not_stop(self):
        with mock.patch.object(P, 'run', self.fake(behind=False)), mock.patch.object(P, 'open_pulls', return_value=None):
            notes = P.integration_gate(P.parser().parse_args(['subject']))
        self.assertTrue(any('could not be read' in n for n in notes))


if __name__ == '__main__':
    unittest.main()
