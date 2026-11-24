"""lane_push.py's two checks from Joel's message of 2026-11-14 22:08 UTC ("i merged, and that should happen automatically
... didn't understand why you gave me no cards and quit working tho"): a refused merge is no reason to hold a pull request
(lesson bad-trips-2026-11-14a), and a turn whose checks still read below Human High ends only at a boundary it names
(lesson bad-trips-2026-11-14b)."""
import json
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import lane_push as P  # noqa: E402


class NoHoldForARefusedMerge(unittest.TestCase):
    def args(self, *extra):
        return P.parser().parse_args(['subject', '--mailbox', '2026-11-14T22:08Z'] + list(extra))

    def test_the_turn_43_reason_is_refused(self):
        a = self.args('--no-merge', "this session's permission check refused merging into main (Merge Without Review)")
        with self.assertRaises(SystemExit) as e:
            P.merge_gate(a, ['tools/humanization/x.py'], robot=True)
        self.assertIn('should happen automatically', str(e.exception))

    def test_a_change_that_must_wait_can_hold(self):
        P.merge_gate(self.args('--no-merge', 'its tests fail until his answer on round 40'), ['tools/x.py'], robot=True)

    def test_neither_flag_leaves_it_to_the_workflow(self):
        P.merge_gate(self.args(), ['tools/x.py'], robot=True)


def ledger(recs):
    f = tempfile.NamedTemporaryFile('w', suffix='.jsonl', delete=False)
    f.write('\n'.join(json.dumps(r) for r in recs) + '\n')
    f.close()
    return f.name


class OpenWork(unittest.TestCase):
    """Turn 43's chest pain paragraph: one try, AI Assisted, and the turn ended on a report."""
    RECS = [
        {'type': 'prediction', 'id': 'cp#1', 'lineage': 'cp', 'at': '2026-11-13T15:45:06Z'},
        {'type': 'result', 'prediction': 'cp#1', 'headline': 'AI Assisted',
         'windows': [{'label': 'AI-Assisted', 'confidence': 'Low'}, {'label': 'AI-Assisted', 'confidence': 'Medium'}]},
        {'type': 'prediction', 'id': 'dmso#1', 'lineage': 'dmso', 'at': '2026-11-13T15:45:07Z'},
        {'type': 'result', 'prediction': 'dmso#1', 'headline': 'Human Written',
         'windows': [{'label': 'Human', 'confidence': 'High'}]},
        {'type': 'prediction', 'id': 'old#1', 'lineage': 'old', 'at': '2026-11-12T10:00:00Z'},
        {'type': 'result', 'prediction': 'old#1', 'headline': 'AI Generated',
         'windows': [{'label': 'AI-Generated', 'confidence': 'High'}]},
    ]

    def test_this_turns_paragraph_below_high_is_open(self):
        left = P.open_work(ledger(self.RECS), '2026-11-13T14:56Z')
        self.assertEqual([(l, n) for l, n, _ in left], [('cp', 1)])

    def test_human_high_and_earlier_turns_are_not(self):
        left = P.open_work(ledger(self.RECS[2:]), '2026-11-13T14:56Z')
        self.assertEqual(left, [])

    def test_the_apis_human_written_label_counts_as_human(self):
        # turn 63 (2026-11-24): both checks read "Human Written, High" through the API, one window each, and the gate
        # counted them open, since it compared the label with "Human" exactly
        recs = [
            {'type': 'prediction', 'id': 'api#1', 'lineage': 'api', 'at': '2026-11-24T01:45:00Z'},
            {'type': 'result', 'prediction': 'api#1', 'headline': 'Human Written',
             'windows': [{'label': 'Human Written', 'confidence': 'High', 'words': 270}]},
            {'type': 'prediction', 'id': 'med#1', 'lineage': 'med', 'at': '2026-11-24T01:45:01Z'},
            {'type': 'result', 'prediction': 'med#1', 'headline': 'Human Written',
             'windows': [{'label': 'Human Written', 'confidence': 'High', 'words': 125},
                         {'label': 'Human Written', 'confidence': 'Medium', 'words': 22}]},
        ]
        left = P.open_work(ledger(recs), '2026-11-24T01:26Z')
        self.assertEqual([(l, n) for l, n, _ in left], [('med', 1)])

    def test_the_push_names_a_boundary(self):
        a = P.parser().parse_args(['subject', '--article', 'none-such', '--mailbox', '2026-11-13T14:56Z'])
        P.boundary_gate(a)   # no ledger for the article: nothing to say


class TrailerNote(unittest.TestCase):
    """Lesson bad-trips-2026-11-24v: four turns' commits went out without their trailer lines; the variable was set in an
    earlier command."""

    def test_a_claude_session_without_trailers_is_told(self):
        self.assertIn('NO TRAILERS', P.trailer_note({'CLAUDE_CODE_SESSION_ID': 'abc'}))

    def test_trailers_set_or_another_runner_say_nothing(self):
        self.assertEqual(P.trailer_note({'CLAUDE_CODE_SESSION_ID': 'abc', 'LANE_COMMIT_TRAILERS': 'Co-Authored-By: x'}), '')
        self.assertEqual(P.trailer_note({}), '')


if __name__ == '__main__':
    unittest.main()
