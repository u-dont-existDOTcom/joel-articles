"""tools/humanization/toc_sidebar.py: Substack's contents sidebar, as measured on 2026-11-16 (Joel's laptop, the post's
own menu; widths from the page's canvas with the font the menu used, Inter at 15px)."""
import importlib.util, os, sys, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location('toc_sidebar', os.path.join(ROOT, 'tools', 'humanization', 'toc_sidebar.py'))
ts = importlib.util.module_from_spec(spec); spec.loader.exec_module(ts)

MEASURED = {  # heading: width in px the browser measured
    'Five Stages of Reparenting': 191.0, 'Understanding Reparenting': 194.4, 'My Journey': 84.3,
    'If You Want to Kill Yourself': 187.1, 'Signs of Manipulation': 153.2, 'Write It. Don’t Send It Yet.': 181.8,
    'Talk to the hand!✋🏿': 136.2, 'Ask God for a Loan 🫶🏿': 158.8,
}

class Widths(unittest.TestCase):
    def test_matches_the_browser(self):
        tol = 0.15 if ts._shaper() else 1.5
        for text, px in MEASURED.items():
            self.assertAlmostEqual(ts.width(text), px, delta=tol, msg=text)

    def test_fallback_table_close(self):
        saved = ts._hb
        try:
            ts._hb = False
            for text, px in MEASURED.items():
                self.assertAlmostEqual(ts.width(text), px, delta=1.5, msg=text)
        finally:
            ts._hb = saved

class Shown(unittest.TestCase):
    def test_cut_like_the_sidebar(self):
        # as the menu showed them (h2 = 205px of room, h3 = 193)
        self.assertEqual(ts.shown('The Chicken-and-Egg Problem', 2)[1], 'The Chicken-and-Egg Pro…')
        self.assertEqual(ts.shown('Borrow One Competency at a Time', 3)[1], 'Borrow One Competency…')
        self.assertEqual(ts.shown('If You Want to Kill Yourself', 2)[1], 'If You Want to Kill Yourself')

    def test_status(self):
        self.assertEqual(ts.status('My Journey', 2), 'fits')
        self.assertEqual(ts.status('Write It. Don’t Send It Yet.', 3), 'tight')
        self.assertEqual(ts.status('Use Childhood Photographs Gently', 2), 'cut')

    def test_toc_file(self):
        import tempfile, json, io, contextlib
        with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
            f.write('# Safety and Readiness  (0 words)\n    ## [S007] Dip Your Toes In Before You Go Deep  (202 words)\n##### Not listed\n')
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            ts.main([f.name, '--json'])
        rows = json.loads(out.getvalue())
        self.assertEqual([r['status'] for r in rows], ['fits', 'cut', 'not listed'])
        self.assertEqual(rows[1]['id'], 'S007')

if __name__ == '__main__':
    unittest.main()
