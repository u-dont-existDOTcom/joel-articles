"""Tests for tools/humanization/contents_picks_page.py, Joel's contents picks page."""
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
TOOL = ROOT / 'tools' / 'humanization' / 'contents_picks_page.py'


class PicksPage(unittest.TestCase):
    def build(self):
        d = pathlib.Path(tempfile.mkdtemp())
        now = [{'id': 'S001', 'level': 1, 'heading': 'How to use this very large guide', 'words': 10},
               {'id': 'S002', 'level': 2, 'heading': 'Do you think in words?', 'words': 5}]
        (d / 'CONTENTS-NOW.json').write_text(json.dumps(now), encoding='utf-8')
        (d / 'SECTIONS.json').write_text(json.dumps([{'id': 'S001', 'text': 'one two'}, {'id': 'S002', 'text': 'three'}]),
                                         encoding='utf-8')
        (d / 'P.json').write_text(json.dumps([dict(e, heading=e['heading'].title(), kind='case') for e in now]), encoding='utf-8')
        (d / 'O.json').write_text(json.dumps({'title': 't', 'sub': 's', 'store': 'x', 'primary': 'pick',
                                              'options': {'pick': {'label': 'Proposed', 'file': 'P.json'}},
                                              'scores': {'question': 'q', 'table': '', 'git': ''}}), encoding='utf-8')
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


if __name__ == '__main__':
    unittest.main()
