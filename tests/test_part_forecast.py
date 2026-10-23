"""tools/humanization/part_forecast.py: a forecast names the parts that will read red, and is scored part by part."""
import json, pathlib, sys, tempfile, unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import part_forecast as F  # noqa: E402


def result(text, spans):
    """A RESULT-like dict: SPANS is [(label, confidence, end)], tiling TEXT from 0."""
    ws, a = [], 0
    for label, conf, b in spans:
        ws.append({'label': label, 'confidence': conf, 'start_index': a, 'end_index': b,
                   'word_count': len(text[a:b].split())})
        a = b
    return {'text': text, 'windows': ws, 'headline': 'Mostly Human Written', 'version': '4.1', 'fraction_ai': 0.1}


LAST = 'Alpha paragraph stays the same here.\nBeta was light green last time, sadly.\nGamma is the old version.'
NEW = 'Alpha paragraph stays the same here.\nBeta was light green last time, sadly.\nGamma is the new version now.'


class PartForecastTest(unittest.TestCase):
    def test_make_adds_the_last_checks_light_green_windows(self):
        last = result(LAST, [('Human', 'High', 36), ('Human', 'Low', 75), ('AI-Generated', 'High', len(LAST))])
        fc = F.make(last, NEW, [{'name': 'gamma', 'text': 'Gamma is the new version now.', 'chance_red': 0.3, 'why': 'w'}],
                    with_neighbours=False)
        kinds = [p['kind'] for p in fc['parts']]
        self.assertEqual(kinds, ['changed', 'risk'])
        self.assertIn('Beta was light green', fc['parts'][1]['text'])
        self.assertEqual(fc['parts'][1]['chance_red'], F.LOW_CHANCE)

    def test_make_adds_each_changed_parts_neighbours_itself(self):
        """Gate E249 (2026-10-23 18:13 UTC): the neighbour rule (E244) ran by hand in one lane's forecast and not the
        other's, where the High red was the paragraph after a changed one."""
        text = ('Alpha paragraph stays the same here.\nBeta paragraph, with a changed gloss (like this one) inside it.\n'
                'Gamma paragraph after it, unchanged.\nDelta paragraph far away, unchanged.')
        last = result(text, [('Human', 'High', len(text))])
        fc = F.make(last, text, [{'name': 'gloss', 'text': 'a changed gloss (like this one)', 'chance_red': 0.05, 'why': 'w'}])
        got = {p['name'].split(': ', 1)[1]: p['text'] for p in fc['parts'] if p['kind'] == 'neighbour'}
        self.assertEqual(got['the paragraph before it'], 'Alpha paragraph stays the same here.')
        self.assertEqual(got['the paragraph after it'], 'Gamma paragraph after it, unchanged.')
        self.assertEqual(got['the rest of its paragraph, before it'], 'Beta paragraph, with')
        self.assertNotIn('the rest of its paragraph, after it', got)  # "inside it." is too short to place
        self.assertTrue(all(p['chance_red'] == F.NEIGHBOUR_CHANCE for p in fc['parts'] if p['kind'] == 'neighbour'))
        self.assertNotIn('Delta', ' '.join(got.values()))
        # a neighbour CHANGED.json names itself keeps its own chance and isn't added twice
        fc = F.make(last, text, [{'name': 'gloss', 'text': 'a changed gloss (like this one)', 'chance_red': 0.05, 'why': 'w'},
                                 {'name': 'mine', 'text': 'Gamma paragraph after it, unchanged.', 'chance_red': 0.2, 'why': 'w'}])
        self.assertEqual([p['chance_red'] for p in fc['parts'] if 'Gamma' in p['text']], [0.2])

    def test_a_changed_part_must_be_in_the_new_text_once(self):
        last = result(LAST, [('Human', 'High', len(LAST))])
        with self.assertRaises(SystemExit):
            F.make(last, NEW, [{'name': 'g', 'text': 'not there', 'chance_red': 0.3, 'why': 'w'}])

    def test_score_counts_hits_misses_and_red_outside_the_parts(self):
        res = result(NEW, [('Human', 'High', 36), ('AI-Generated', 'Low', 75), ('Human', 'High', len(NEW))])
        fc = {'parts': [{'name': 'gamma', 'text': 'Gamma is the new version now.', 'chance_red': 0.6, 'why': 'w', 'kind': 'changed'},
                        {'name': 'alpha', 'text': 'Alpha paragraph stays the same here.', 'chance_red': 0.1, 'why': 'w', 'kind': 'risk'}],
              'rest': {'chance_red': 0.2, 'why': 'w'}}
        rows, loose, rest_red, b = F.score(fc, res)
        self.assertEqual([(r[1], r[2]) for r in rows], [('dark', False), ('dark', True)])
        self.assertEqual(loose, [1])
        self.assertTrue(rest_red)
        self.assertAlmostEqual(b, ((0.6 - 0) ** 2 + (0.1 - 0) ** 2 + (0.2 - 1) ** 2) / 3)
        md = F.page(fc, res)
        self.assertIn('**miss**', md)
        self.assertIn('window 1, Low', md)

    def test_the_command_line_writes_both_files(self):
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / 'last.json').write_text(json.dumps(result(LAST, [('Human', 'Low', len(LAST))])), encoding='utf-8')
            (d / 'new.txt').write_text(NEW, encoding='utf-8')
            (d / 'changed.json').write_text(json.dumps([{'name': 'g', 'text': 'Gamma is the new version now.',
                                                         'chance_red': 0.2, 'why': 'w'}]), encoding='utf-8')
            self.assertEqual(F.main(['make', '--last', str(d / 'last.json'), '--text', str(d / 'new.txt'),
                                     '--changed', str(d / 'changed.json'), '--out', str(d / 'fc.json')]), 0)
            (d / 'res.json').write_text(json.dumps(result(NEW, [('Human', 'High', len(NEW))])), encoding='utf-8')
            self.assertEqual(F.main(['score', str(d / 'fc.json'), str(d / 'res.json'), '--out', str(d / 'score.md')]), 0)
            self.assertIn('parts called right', (d / 'score.md').read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
