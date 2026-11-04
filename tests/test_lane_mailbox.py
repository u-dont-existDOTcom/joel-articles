"""Tests for tools/humanization/lane_mailbox.py and lane_push.py's mailbox gate (Joel, 2026-10-31: "can we make sure you always
check what is addressed to you in each turn? like checking ur mailbox?"; adopted 2026-11-01 from
universal-dev-architecture's suggested-fixes/joel-articles/2026-10-31-mailbox-every-turn.md)."""
import pathlib
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import lane_push as P  # noqa: E402
import lane_mailbox as M  # noqa: E402

READ_ALL = [('uda-lane', 'no new items'), ('repo', 'no new issues, comments or reviews'),
            ('notes', 'no edits by others'), ('runtime', 'no queued messages')]


class Record(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = pathlib.Path(self.tmp.name) / 'MAILBOX.json'

    def tearDown(self):
        self.tmp.cleanup()

    def test_every_place_read_is_complete(self):
        self.assertEqual(M.record('2026-11-01 22:27', ['guide'], READ_ALL, [], [], path=self.path), [])
        self.assertEqual(M.check('2026-11-01T22:27:00Z', path=self.path), [])

    def test_a_place_left_out_is_missing(self):
        probs = M.record('2026-11-01 22:27', [], READ_ALL[:3], [], [], path=self.path)
        self.assertTrue(any(p.startswith('runtime') for p in probs), probs)

    def test_an_unreachable_place_counts_with_what_failed_and_a_retry(self):
        probs = M.record('2026-11-01 22:27', [], READ_ALL[:1] + READ_ALL[2:],
                         [('repo', 'GitHub API 502', 'first thing next turn')], [], path=self.path)
        self.assertEqual(probs, [])
        probs = M.record('2026-11-01 22:27', [], READ_ALL[:1] + READ_ALL[2:], [('repo', 'GitHub API 502', '')], [],
                         path=self.path)
        self.assertTrue(any(p.startswith('repo') for p in probs), probs)

    def test_an_item_needs_an_outcome(self):
        probs = M.record('2026-11-01 22:27', [], READ_ALL, [], [('item.md', '')], path=self.path)
        self.assertTrue(any('item.md' in p for p in probs), probs)

    def test_another_turn_is_not_this_turn(self):
        M.record('2026-11-01 22:27', [], READ_ALL, [], [], path=self.path)
        self.assertTrue(M.check('2026-11-02 09:10', path=self.path))

    def test_a_turn_is_a_clock_reading(self):
        with self.assertRaises(ValueError):
            M.turn_key('this turn')


class PushGate(unittest.TestCase):
    def test_push_without_mailbox_is_refused_before_anything_is_committed(self):
        with mock.patch.object(P, 'commit') as commit, self.assertRaises(SystemExit) as e:
            P.main(['subject', '--article', 'inner-signal'])
        self.assertIn('--mailbox', str(e.exception))
        commit.assert_not_called()

    def test_push_with_an_incomplete_check_is_refused(self):
        with mock.patch.object(M, 'check', return_value=['runtime: not checked']), \
                mock.patch.object(P, 'commit') as commit, self.assertRaises(SystemExit) as e:
            P.main(['subject', '--article', 'inner-signal', '--mailbox', '2026-11-01 22:27'])
        self.assertIn('runtime', str(e.exception))
        commit.assert_not_called()


if __name__ == '__main__':
    unittest.main()


class LaneRecord(unittest.TestCase):
    """2026-11-04 13:53 UTC, Joel: "290 has conflicts". Every lane wrote state/MAILBOX.json each turn, so a lane's open pull
    request conflicted with main whenever another lane's merged first. Each lane now writes its own file."""

    def test_each_branch_has_its_own_record(self):
        import os
        import subprocess
        import tempfile
        env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(M.lane_record(d), M.LEGACY)                       # no git: the shared file
            subprocess.run(['git', 'init', '-q', '-b', 'claude/some-lane', d], check=True, env=env)
            self.assertEqual(M.lane_record(d), M.LANES / 'claude-some-lane.json')

    def test_a_check_in_the_old_shared_file_still_counts(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            old = pathlib.Path(d) / 'MAILBOX.json'
            M.record('2026-11-01 22:27', ['guide'], READ_ALL, [], [], path=old)
            self.assertEqual(M.check('2026-11-01 22:27', path=old), [])
            self.assertTrue(M.check('2026-11-01 22:27', path=pathlib.Path(d) / 'lane.json'))   # not in the lane's own

    def test_settle_gives_the_shared_file_mains_content_and_moves_this_lanes_records(self):
        """2026-11-04 14:28 UTC, Joel: "pr 290 has conflicts" again: the branch still carried its own records in the shared
        file, which another lane's merge had changed too."""
        import json
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            legacy, lane = pathlib.Path(d) / 'MAILBOX.json', pathlib.Path(d) / 'mailbox' / 'lane.json'
            M.record('2026-11-01 22:27', ['other lane'], READ_ALL, [], [], path=legacy)
            main_text = legacy.read_text(encoding='utf-8')
            M.record('2026-11-02 09:10', ['this lane'], READ_ALL, [], [], path=legacy)
            self.assertEqual(M.settle(legacy=legacy, lane=lane, main_text=main_text), ['2026-11-02T09:10Z'])
            self.assertEqual(legacy.read_text(encoding='utf-8'), main_text)
            self.assertEqual([c['turn'] for c in json.loads(lane.read_text(encoding='utf-8'))['checks']], ['2026-11-02T09:10Z'])
            self.assertEqual(M.settle(legacy=legacy, lane=lane, main_text=main_text), [])      # nothing left to do

