"""The mailbox merge driver: every lane's records kept once (2026-11-04: three hand merges of state/MAILBOX.json in a day)."""
import json, pathlib, subprocess, sys, tempfile, unittest
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import mailbox_merge as M  # noqa: E402
import lane_push as P  # noqa: E402

H = {'about': 'x', 'places': {'repo': 'y'}}


def rec(turn, at):
    return {'turn': turn, 'lines_of_work': ['l'], 'places': [], 'items': [], 'recorded_utc': at}


class MailboxMerge(unittest.TestCase):
    def test_both_sides_new_records_are_kept_once_in_time_order(self):
        base = dict(H, checks=[rec('a', '01')])
        ours = dict(H, checks=[rec('a', '01'), rec('gut', '03')])
        theirs = dict(H, checks=[rec('a', '01'), rec('ic', '02'), rec('gut', '03')])
        self.assertEqual([c['turn'] for c in M.merge(base, ours, theirs)['checks']], ['a', 'ic', 'gut'])

    def test_a_header_change_is_left_to_a_person(self):
        self.assertIsNone(M.merge(dict(H, checks=[]), dict(H, checks=[]), dict(H, about='changed', checks=[])))

    def test_the_driver_writes_the_merge_into_ours(self):
        with tempfile.TemporaryDirectory() as d:
            p = pathlib.Path(d)
            for n, m in (('o', dict(H, checks=[])), ('a', dict(H, checks=[rec('gut', '2')])), ('b', dict(H, checks=[rec('ic', '1')]))):
                (p / n).write_text(json.dumps(m))
            self.assertEqual(M.main([str(p / 'o'), str(p / 'a'), str(p / 'b')]), 0)
            self.assertEqual([c['turn'] for c in json.loads((p / 'a').read_text())['checks']], ['ic', 'gut'])

    def test_lane_push_sets_the_driver_once(self):
        calls = []

        def run(cmd, check=True, timeout=600):
            calls.append(cmd)
            return subprocess.CompletedProcess(cmd, 0, '', '')
        with mock.patch.object(P, 'run', run):
            self.assertIn('merge driver', P.install_merge_driver())
        self.assertIn(['git', 'config', 'merge.lane-mailbox.driver', P.MAILBOX_DRIVER], calls)

        def run2(cmd, check=True, timeout=600):
            return subprocess.CompletedProcess(cmd, 0, P.MAILBOX_DRIVER + '\n', '')
        with mock.patch.object(P, 'run', run2):
            self.assertEqual(P.install_merge_driver(), '')

    def test_gitattributes_names_the_driver(self):
        ga = (pathlib.Path(__file__).resolve().parents[1] / '.gitattributes').read_text()
        self.assertIn('state/MAILBOX.json merge=lane-mailbox', ga)


if __name__ == '__main__':
    unittest.main()
