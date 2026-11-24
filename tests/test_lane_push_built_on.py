"""Tests for the built-on reminder in tools/humanization/lane_push.py (lesson toc-2026-11-24b; Joel, 2026-11-24 21:05 UTC:
"whenever i change those you should also think to merge the changes into this one (and i shouldn't have to tell you this
either, right?)")."""
import json
import pathlib
import sys
import tempfile
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import lane_push as P  # noqa: E402


EDGES = {'edges': [
    {'source': 'inner-child-therapy', 'built_on_it': 'inner-signal', 'sections': {'ids': 'S017-S034'},
     'last_brought_in_line': {'what': 'r03, 2026-09-11'}},
    {'source': 'inner-child-therapy', 'built_on_it': 'hearthwork', 'registered': False, 'last_brought_in_line': None},
    {'source': 'somatic-therapies', 'built_on_it': 'inner-signal', 'last_brought_in_line': None},
]}


class BuiltOn(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = pathlib.Path(self.tmp.name) / 'BUILT-ON.json'
        self.path.write_text(json.dumps(EDGES), encoding='utf-8')

    def tearDown(self):
        self.tmp.cleanup()

    def test_a_source_lane_is_told_what_is_built_on_it(self):
        lines = P.built_on_lines('inner-child-therapy', self.path)
        self.assertEqual(len(lines), 2)
        self.assertIn('inner-signal is built on inner-child-therapy', lines[0])
        self.assertIn('carry this turn\'s changes', lines[0])
        self.assertIn('not registered here yet', lines[1])

    def test_a_built_on_lane_is_told_its_sources_and_the_last_catch_up(self):
        lines = P.built_on_lines('inner-signal', self.path)
        self.assertEqual(len(lines), 2)
        self.assertIn('S017-S034', lines[0])
        self.assertIn('r03, 2026-09-11', lines[0])
        self.assertIn('somatic-therapies', lines[1])
        self.assertIn('never recorded', lines[1])

    def test_an_article_with_no_edges_gets_nothing(self):
        self.assertEqual(P.built_on_lines('romance', self.path), [])

    def test_a_missing_or_broken_file_gets_nothing(self):
        self.assertEqual(P.built_on_lines('inner-signal', pathlib.Path(self.tmp.name) / 'none.json'), [])
        self.path.write_text('{not json', encoding='utf-8')
        self.assertEqual(P.built_on_lines('inner-signal', self.path), [])


class TheRealFile(unittest.TestCase):
    def test_every_registered_edge_names_registered_articles(self):
        edges = json.loads((REPO / 'articles' / 'BUILT-ON.json').read_text(encoding='utf-8'))['edges']
        index = json.loads((REPO / 'articles' / 'INDEX.json').read_text(encoding='utf-8'))
        ids = set(index['articles'].keys()) if isinstance(index.get('articles'), dict) else \
            {a.get('id') or a.get('article_id') for a in index['articles']}
        self.assertTrue(edges)
        for e in edges:
            self.assertIn(e['source'], ids)
            if e.get('registered', True):
                self.assertIn(e['built_on_it'], ids)
            self.assertTrue(e.get('next'), e)

    def test_the_file_and_the_map_are_shared_files(self):
        self.assertEqual(P.shared(['articles/BUILT-ON.json', 'ARTICLE-META-MAP.md', 'articles/AGENTS.md']),
                         ['ARTICLE-META-MAP.md', 'articles/AGENTS.md', 'articles/BUILT-ON.json'])


if __name__ == '__main__':
    unittest.main()
