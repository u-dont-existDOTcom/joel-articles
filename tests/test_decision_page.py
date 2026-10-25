"""tools/humanization/decision_page.py: the interactive review page for many independently actionable proposals (UDA
patterns/owner-questions-page.md; Joel's turn-109 request for the point-of-view read, 2026-10-25)."""
import json
import pathlib
import re
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import decision_page as D  # noqa: E402

SPEC = {
    'review_id': 'test-review', 'title': 'Test Review Sheet', 'source_sha256': 'a' * 64, 'source_name': 'an article',
    'repo_file': 'https://github.com/example/repo/blob/main/page.html', 'intro': ['One [link](https://example.com/x).'],
    'groups': [{'id': 'cut', 'title': 'Cuts', 'approve': 'make the cut.', 'reject': 'keep the line.'},
               {'id': 'pov', 'title': 'Points of view'}],
    'items': [{'id': 'C1', 'group': 'cut', 'title': 'A closer that repeats', 'section': 'One',
               'blocks': [{'label': 'Before', 'paras': [[['Keep this. ', ''], ['Cut this.', 'del']]]},
                          {'label': 'After', 'paras': [[['Keep this.', '']]]}],
               'fields': [{'label': 'Why', 'text': 'It says it again. </script> stays text.'}]},
              {'id': 'P1', 'group': 'pov', 'title': 'A general critique', 'section': 'Two',
               'fields': [{'label': 'Points of view', 'list': ['SOURCE-SUPPORTED: he says it.', 'NEW OWNER CHOICE: a question?']}],
               'links': [{'text': 'the check', 'url': 'https://www.pangram.com/history/x'}]}],
}


class DecisionPage(unittest.TestCase):
    def test_the_page_embeds_the_tested_field_colors_and_the_four_decisions(self):
        page = D.build(SPEC)
        self.assertTrue(page.startswith('<!doctype html>'))
        self.assertIn((ROOT / 'project-sources/review-form-controls.css').read_text(encoding='utf-8'), page)
        for word in ('Approve', 'Revise', 'Reject', 'Pending', 'Copy JSON', 'Download JSON', 'Load the pasted JSON', 'Clear all'):
            self.assertIn(word, page)
        self.assertIn('prefers-color-scheme: dark', page)
        self.assertIn(':root[data-theme="dark"]', page)

    def test_the_data_parses_and_cannot_close_its_script(self):
        page = D.build(SPEC)
        m = re.search(r'<script type="application/json" id="review-data">(.*?)</script>', page, re.S)
        data = json.loads(m.group(1).replace('<\\/', '</'))
        self.assertEqual(data['format'], D.FORMAT)
        self.assertEqual([x['id'] for x in data['items']], ['C1', 'P1'])
        self.assertNotIn('</script> stays', m.group(1))

    def test_the_artifact_version_has_no_document_tags(self):
        page = D.build(SPEC, full=False)
        self.assertTrue(page.startswith('<title>Test Review Sheet</title>'))
        for tag in ('<!doctype', '<html', '<head>', '<body>'):
            self.assertNotIn(tag, page)
        self.assertNotIn('id="downloadJson"', page)  # the artifact viewer blocks downloads a page starts
        self.assertNotIn('createObjectURL', page)
        self.assertIn('id="copyJson"', page)

    def test_a_bad_spec_is_refused(self):
        for bad in (dict(SPEC, source_sha256='nope'),
                    dict(SPEC, items=SPEC['items'] + [dict(SPEC['items'][0])]),
                    dict(SPEC, items=[dict(SPEC['items'][0], group='other')]),
                    dict(SPEC, items=[dict(SPEC['items'][1], links=[{'text': 'x', 'url': 'http://example.com'}])]),
                    dict(SPEC, items=[dict(SPEC['items'][0], blocks=[{'label': 'x', 'paras': [[['t', 'bold']]]}])])):
            with self.assertRaises(SystemExit):
                D.build(bad)

    def test_intro_links_are_links_and_text_is_escaped(self):
        page = D.build(dict(SPEC, intro=['A <b>tag</b> and [a link](https://example.com/y).']))
        self.assertIn('A &lt;b&gt;tag&lt;/b&gt; and <a href="https://example.com/y" target="_blank" rel="noopener">a link</a>.', page)


if __name__ == '__main__':
    unittest.main()
