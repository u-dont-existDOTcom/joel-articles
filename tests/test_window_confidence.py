"""tools/humanization/window_confidence.py: every window that isn't High-confidence Human is listed, with its confidence
and whose words it holds (Joel, 2026-10-26: "always we should be marking down the confidence"; gate E278)."""
import json, pathlib, sys, tempfile, unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import window_confidence as W  # noqa: E402

TEXT = 'His own sentence stays here. A model sentence reads light. Yes.\nThe list reads AI here.'


def result():
    spans = [('Human', 'High', 29), ('Human', 'Low', 59), ('Human', 'Medium', 64), ('AI-Generated', 'High', len(TEXT))]
    ws, a = [], 0
    for label, conf, b in spans:
        ws.append({'label': label, 'confidence': conf, 'start_index': a, 'end_index': b,
                   'word_count': len(TEXT[a:b].split()), 'calibrated_confidence': 0.9 if conf != 'High' else 0.999})
        a = b
    return {'text': TEXT, 'windows': ws, 'headline': 'Mostly Human Written', 'link': 'https://www.pangram.com/feed/x'}


class WindowConfidenceTest(unittest.TestCase):
    def test_rows_skip_only_high_confidence_human(self):
        rows = W.rows(result(), his=W.norm('His own sentence stays here. The list reads AI here.'))
        self.assertEqual([(r['label'], r['confidence']) for r in rows], [('Human', 'Low'), ('Human', 'Medium'), ('AI', 'High')])
        self.assertEqual(rows[0]['sentences'][0]['whose'], 'approved wording')
        self.assertEqual(rows[2]['sentences'][0]['whose'], 'his')

    def test_counts_name_every_confidence(self):
        self.assertEqual(W.counts(result()['windows']), ['Human High 1', 'Human Medium 1', 'Human Low 1', 'AI High 1'])

    def test_page_and_json(self):
        with tempfile.TemporaryDirectory() as d:
            src = pathlib.Path(d, 'RESULT.json')
            src.write_text(json.dumps(result()), encoding='utf-8')
            his = pathlib.Path(d, 'his.md')
            his.write_text('His own sentence stays here.', encoding='utf-8')
            W.main([str(src), '--out', str(pathlib.Path(d, 'C.md')), '--json', str(pathlib.Path(d, 'C.json')), '--his', str(his)])
            page = pathlib.Path(d, 'C.md').read_text(encoding='utf-8')
            self.assertIn('Windows: Human High 1, Human Medium 1, Human Low 1, AI High 1.', page)
            self.assertIn('| Human Low | 0.900 |', page)
            data = json.loads(pathlib.Path(d, 'C.json').read_text(encoding='utf-8'))
            self.assertEqual(len(data['RESULT.json']['rows']), 3)


if __name__ == '__main__':
    unittest.main()
