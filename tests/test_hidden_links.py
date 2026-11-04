"""The newcomer read (gate E343; Joel, 2026-11-04 10:18 UTC: "just explain stuff to someone who doesn't already know the
hidden links in your prose's thinking")."""
import json, pathlib, sys, tempfile, unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import hidden_links as H  # noqa: E402


class HiddenLinks(unittest.TestCase):
    def test_sentences_keep_dr_and_brackets_together(self):
        t = 'L-Glutamine (watch Dr. Rhonda vid) is the main fuel. It skips digestion. (Called α-KG.) Done.'
        self.assertEqual(H.sentences(t), ['L-Glutamine (watch Dr. Rhonda vid) is the main fuel.', 'It skips digestion.',
                                          '(Called α-KG.)', 'Done.'])

    def test_the_reader_lines_parse_and_anything_else_is_ignored(self):
        reply = ('Here you go:\nS2 | "skips the complicated digestive steps" | Why does that matter?\n'
                 '- S4 | “lock down the barrier” | How does that turn down inflammation?\nnone of the rest\n')
        self.assertEqual(H.parse(reply), [
            {'sentence': 2, 'quote': 'skips the complicated digestive steps', 'gap': 'Why does that matter?'},
            {'sentence': 4, 'quote': 'lock down the barrier', 'gap': 'How does that turn down inflammation?'}])

    def test_the_draft_must_state_every_link_or_say_why_not(self):
        gaps = [{'id': 'L1', 'sentence': 2, 'quote': 'x', 'gap': 'why?', 'answer': "So that’s why it's faster"},
                {'id': 'L2', 'sentence': 3, 'quote': 'y', 'gap': 'how?'},
                {'id': 'L3', 'sentence': 4, 'quote': 'z', 'gap': 'what?', 'status': 'drop'},
                {'id': 'L4', 'sentence': 5, 'quote': 'w', 'gap': 'who?', 'answer': 'not in it'}]
        probs = H.problems(gaps, "It skips digestion.  So that's why it's faster than food.")
        self.assertEqual([p.split(':')[0] for p in probs], ['L2', 'L3', 'L4'])

    def test_make_collect_check_round_trip(self):
        with tempfile.TemporaryDirectory() as d:
            p = pathlib.Path(d)
            (p / 'in.txt').write_text('It skips digestion. So the cells heal.', encoding='utf-8')
            H.main(['make', str(p / 'in.txt'), str(p / 'run')])
            self.assertIn('S1 It skips digestion.', (p / 'run' / 'TEXT.txt').read_text(encoding='utf-8'))
            self.assertIn('His fix', (p / 'run' / 'BRIEF.txt').read_text(encoding='utf-8'))
            (p / 'run' / 'READER.md').write_text('S1 | "skips digestion" | Why does that matter?\n', encoding='utf-8')
            H.main(['collect', str(p / 'run')])
            (p / 'draft.txt').write_text('It skips digestion, so it gets to the cells faster than food.', encoding='utf-8')
            self.assertEqual(H.main(['check', str(p / 'run'), str(p / 'draft.txt')]), 1)
            links = json.loads((p / 'run' / 'LINKS.json').read_text(encoding='utf-8'))
            links[0]['answer'] = 'so it gets to the cells faster than food'
            (p / 'run' / 'LINKS.json').write_text(json.dumps(links), encoding='utf-8')
            H.main(['collect', str(p / 'run')])  # a second collect keeps the answer
            self.assertEqual(H.main(['check', str(p / 'run'), str(p / 'draft.txt')]), 0)


if __name__ == '__main__':
    unittest.main()
