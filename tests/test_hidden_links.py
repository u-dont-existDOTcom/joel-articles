"""The newcomer read (gate E345; Joel, 2026-11-04 10:18 UTC: "just explain stuff to someone who doesn't already know the
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
        gaps = [{'id': 'L1', 'sentence': 2, 'quote': 'x', 'gap': 'why?', 'answer': "So that’s why it's faster",
                 'raised': 'skips digestion'},
                {'id': 'L2', 'sentence': 3, 'quote': 'y', 'gap': 'how?'},
                {'id': 'L3', 'sentence': 4, 'quote': 'z', 'gap': 'what?', 'status': 'drop'},
                {'id': 'L4', 'sentence': 5, 'quote': 'w', 'gap': 'who?', 'answer': 'not in it'}]
        probs = H.problems(gaps, "It skips digestion.  So that's why it's faster than food.")
        self.assertEqual([p.split(':')[0] for p in probs], ['L2', 'L3', 'L4'])
        # his glutamine: the "so what?" is answered after the how, three sentences on; order counts, not distance
        two = [{'id': 'L1', 'sentence': 1, 'quote': 'x', 'gap': 'how?', 'raised': 'skips digestion', 'answer': 'turned into α-KG'},
               {'id': 'L2', 'sentence': 1, 'quote': 'x', 'gap': 'so what?', 'raised': 'skips digestion,',
                'answer': "So that's why it's faster"}]
        ok = "It skips digestion, and in the cell it's turned into α-KG. That feeds the cycle. So that's why it's faster."
        self.assertEqual(H.problems(two, ok), [])
        two[1]['raised'] = 'That feeds the cycle'
        two[0]['raised'] = "So that's why"
        self.assertIn('the order a reader thinks', H.problems(two, ok)[0])

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
            links[0]['raised'] = 'skips digestion'
            (p / 'run' / 'LINKS.json').write_text(json.dumps(links), encoding='utf-8')
            H.main(['collect', str(p / 'run')])  # a second collect keeps the answer
            # every link answered, but the draft itself hasn't been read yet (E355)
            self.assertEqual(H.main(['check', str(p / 'run'), str(p / 'draft.txt')]), 1)
            self.assertEqual(H.main(['make', str(p / 'draft.txt'), str(p / 'run' / 'draft')]), 0)
            (p / 'run' / 'draft' / 'READER.md').write_text('none\n', encoding='utf-8')
            H.main(['collect', str(p / 'run' / 'draft')])
            self.assertEqual(H.main(['check', str(p / 'run'), str(p / 'draft.txt')]), 0)

    def test_the_draft_itself_gets_a_fresh_read(self):
        """Joel, 2026-11-04 16:00 UTC, on my kits: "your version, r08, makes no sense by the 6th word. Where is the "but"
        coming from? ... it only follows from "these" kits not "three kits"" (E355)."""
        with tempfile.TemporaryDirectory() as d:
            p = pathlib.Path(d)
            (p / 'in.txt').write_text('Gemini suggested these kits to me, but so far they are the best.', encoding='utf-8')
            H.main(['make', str(p / 'in.txt'), str(p / 'run')])
            (p / 'run' / 'READER.md').write_text('none\n', encoding='utf-8')
            H.main(['collect', str(p / 'run')])
            (p / 'draft.txt').write_text('Gemini suggested three kits to me, but so far they are the best.', encoding='utf-8')
            self.assertIn('no fresh read of its own', ' '.join(H.draft_problems(p / 'run', (p / 'draft.txt').read_text())))
            H.main(['make', str(p / 'draft.txt'), str(p / 'run' / 'draft')])
            self.assertIn('"this", "that", "it"', (p / 'run' / 'draft' / 'BRIEF.txt').read_text(encoding='utf-8'))
            (p / 'run' / 'draft' / 'READER.md').write_text('S1 | "but so far" | Why "but"? What is it answering?\n', encoding='utf-8')
            H.main(['collect', str(p / 'run' / 'draft')])
            self.assertEqual(H.main(['check', str(p / 'run'), str(p / 'draft.txt')]), 1)
            # fixed: a new draft, so the old read is stale until the new one is read
            (p / 'draft.txt').write_text('Gemini suggested these kits to me, but so far they are the best.', encoding='utf-8')
            self.assertIn('changed after its fresh read', ' '.join(H.draft_problems(p / 'run', (p / 'draft.txt').read_text())))
            # a flag the words answer can be dropped with a note instead
            H.main(['make', str(p / 'draft.txt'), str(p / 'run' / 'draft')])
            (p / 'run' / 'draft' / 'READER.md').write_text('S1 | "Gemini" | Who is Gemini?\n', encoding='utf-8')
            H.main(['collect', str(p / 'run' / 'draft')])
            g = json.loads((p / 'run' / 'draft' / 'LINKS.json').read_text(encoding='utf-8'))
            g[0].update(status='drop', note='the article introduces his Gemini Gem earlier')
            (p / 'run' / 'draft' / 'LINKS.json').write_text(json.dumps(g), encoding='utf-8')
            self.assertEqual(H.main(['check', str(p / 'run'), str(p / 'draft.txt')]), 0)


if __name__ == '__main__':
    unittest.main()
