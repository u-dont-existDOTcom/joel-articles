"""Tests for tools/humanization/contents_picks_page.py, Joel's contents picks page."""
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
TOOL = ROOT / 'tools' / 'humanization' / 'contents_picks_page.py'


class PicksPage(unittest.TestCase):
    def build(self, **more):
        d = pathlib.Path(tempfile.mkdtemp())
        now = [{'id': 'S001', 'level': 1, 'heading': 'How to use this very large guide', 'words': 10},
               {'id': 'S002', 'level': 2, 'heading': 'Do you think in words?', 'words': 5}]
        (d / 'CONTENTS-NOW.json').write_text(json.dumps(now), encoding='utf-8')
        (d / 'SECTIONS.json').write_text(json.dumps([{'id': 'S001', 'text': 'one two'}, {'id': 'S002', 'text': 'three'}]),
                                         encoding='utf-8')
        (d / 'P.json').write_text(json.dumps([dict(e, heading=e['heading'].title(), kind='case') for e in now]), encoding='utf-8')
        (d / 'O.json').write_text(json.dumps(dict({'title': 't', 'sub': 's', 'store': 'x', 'primary': 'pick',
                                                   'options': {'pick': {'label': 'Proposed', 'file': 'P.json'}},
                                                   'scores': {'question': 'q', 'table': '', 'git': ''}}, **more)), encoding='utf-8')
        subprocess.run([sys.executable, str(TOOL), str(d), str(d / 'O.json'), str(d / 'page.html')], check=True,
                       capture_output=True)
        return (d / 'page.html').read_text(encoding='utf-8')

    def test_a_pick_updates_its_heading_in_place(self):
        """Lesson toc-2026-11-24a (Joel, 2026-11-24 14:18 UTC: "i got up to s034, but now it won't let me make any
        selection?"): rebuilding every heading on each click threw away the box being typed in. A pick now updates only
        its own heading, and the page says so when its script breaks."""
        page = self.build()
        handler = page[page.index("document.addEventListener('change'"):]
        handler = handler[:handler.index('});') + 3]
        self.assertIn('updateItem(id)', handler)
        self.assertNotIn('redraw()', handler)
        self.assertIn("window.addEventListener('error'", page)

    def test_his_answers_are_merged_never_replaced(self):
        """Lesson toc-2026-11-24c (Joel, 2026-11-24 21:35 UTC: "i don't want to redo all my of selections, is that
        necessary? and i already gave a title at s122 check what i sent you"): the page swapped everything it held for
        the store's copy when the store connected and wrote its whole copy back on every save."""
        page = self.build()
        self.assertNotIn('ans = Object.assign(ans, {picks: v.picks', page)
        flush = page[page.index('function flush()'):page.index('function save()')]
        self.assertLess(flush.index('doc.get()'), flush.index('doc.set(record())'))
        self.assertIn('show(takeIn(v))', flush)
        self.assertIn('waiting = true', flush)
        for handler in ("stamp('p:' + id)", "stamp('o:' + t.dataset.own)", "stamp('q:' + t.dataset.q)", "stamp('c')"):
            self.assertIn(handler, page)
        self.assertIn('Not connected to your saved answers', page)

    def test_a_test_copy_says_so_and_keeps_its_own_answers(self):
        page = self.build(test=True, real='https://claude.ai/artifact/REAL')
        self.assertIn('TEST COPY. This is not your page', page)
        self.assertIn('https://claude.ai/artifact/REAL', page)
        self.assertIn('"store": "x-TEST"', page)
        self.assertIn('<title>TEST COPY, not your page: t</title>', page)
        self.assertNotIn('TEST COPY. This', self.build())

    def test_saving_in_a_browser(self):
        """The same lesson, run in a browser stand-in (jsdom) when node and jsdom are there: an ordinary visit, a title
        typed before the saved answers connect, a second tab, an older change against a newer one, no connection."""
        node = shutil.which('node')
        paths = [p for p in (os.environ.get('JSDOM_NODE_PATH'), '/home/claude/pagetest/node_modules') if p and os.path.isdir(p)]
        if not node or not paths:
            self.skipTest('node or jsdom not here')
        env = dict(os.environ, NODE_PATH=paths[0])
        if subprocess.run([node, '-e', "require('jsdom')"], env=env, capture_output=True).returncode:
            self.skipTest('jsdom not here')
        ids = ['S011', 'S015', 'S040', 'S050', 'S060', 'S122']
        d = pathlib.Path(tempfile.mkdtemp())
        now = [{'id': i, 'level': 2, 'heading': 'heading %s as it is' % i, 'words': 9} for i in ids]
        prop = [dict(e, heading='Breathe Less (Buteyko)' if e['id'] == 'S122' else 'Proposal %s' % e['id'], kind='fable') for e in now]
        (d / 'CONTENTS-NOW.json').write_text(json.dumps(now), encoding='utf-8')
        (d / 'SECTIONS.json').write_text(json.dumps([{'id': i, 'text': 'words'} for i in ids]), encoding='utf-8')
        (d / 'P.json').write_text(json.dumps(prop), encoding='utf-8')
        (d / 'O.json').write_text(json.dumps({'title': 't', 'sub': 's', 'store': 'x', 'primary': 'pick',
                                              'options': {'pick': {'label': 'Proposed', 'file': 'P.json'}},
                                              'pick': {i: 'pick' for i in ids},
                                              'scores': {'question': 'q', 'table': '', 'git': ''}}), encoding='utf-8')
        subprocess.run([sys.executable, str(TOOL), str(d), str(d / 'O.json'), str(d / 'page.html')], check=True, capture_output=True)
        r = subprocess.run([node, str(ROOT / 'tests' / 'js' / 'contents_picks_page_merge.cjs'), str(d / 'page.html')],
                           env=env, capture_output=True, text=True, timeout=120)
        self.assertEqual(r.returncode, 0, r.stdout[-2000:] + r.stderr[-800:])


if __name__ == '__main__':
    unittest.main()
