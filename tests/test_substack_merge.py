"""tools/humanization/substack_merge.py on a small editor body (2026-10-20, after the hypnosis guide's first merge).

The guide's editor HTML has blockquotes of several paragraphs, line-broken paragraphs and an image inside a blockquote,
and its master has Markdown list items the published text didn't have. The merge failed on all four; these cases keep
them working.
"""
import json, pathlib, subprocess, sys, tempfile, unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
TOOL = REPO / 'tools' / 'humanization' / 'substack_merge.py'

EDITOR = ('<div contenteditable="true" role="textbox" data-testid="editor" dir="auto" class="tiptap ProseMirror mousetrap" '
          'tabindex="0"><h1>One</h1><p>Plain para here.</p><blockquote><p>Line a<br>line b</p><p>Second quoted.</p>'
          '</blockquote><p>Last <strong>bold</strong> para.</p><h1>Two</h1><p>Steps:</p><ol><li><p>Do this first.</p></li>'
          '<li><p>Then this.</p></li></ol></div>')
PUBLISHED = ('# One\n\nPlain para here.\n\nLine a line b\n\nSecond quoted.\n\nLast **bold** para.\n\n# Two\n\nSteps:\n\n'
             'Do this first.\n\nThen this.\n')
MASTER = ('# One\n\nPlain para, rewritten here.\n\nLine a line b\n\nSecond quoted, rewritten.\n\n1. first step\n\n'
          '2. second step\n\nLast **bold** para.\n\n# Two\n\nSteps:\n\nDo this first.\n\nThen this.\n\n- And one more.\n')


class MergeShapes(unittest.TestCase):
    def merge(self):
        d = pathlib.Path(tempfile.mkdtemp())
        for name, text in (('editor.html', EDITOR), ('published.md', PUBLISHED), ('master.md', MASTER)):
            (d / name).write_text(text, encoding='utf-8')
        r = subprocess.run([sys.executable, str(TOOL), '--editor', str(d / 'editor.html'), '--master', str(d / 'master.md'),
                            '--published', str(d / 'published.md'), '--out', str(d / 'out.html'), '--report',
                            str(d / 'report.json')], capture_output=True, text=True, cwd=REPO)
        rep = json.loads((d / 'report.json').read_text(encoding='utf-8'))
        self.assertEqual(rep['verdict'], 'PASS', rep['failures'] or r.stdout + r.stderr)
        return (d / 'out.html').read_text(encoding='utf-8'), rep

    def test_blockquote_unchanged_markup_and_master_lists(self):
        out, rep = self.merge()
        # an unchanged paragraph keeps the editor's markup, line breaks and all, inside its blockquote
        self.assertIn('<blockquote><p>Line a<br>line b</p><p>Second quoted, rewritten.</p></blockquote>', out)
        self.assertIn('<p>Last <strong>bold</strong> para.</p>', out)
        # the master's own numbered items are one list, after the blockquote and before the next paragraph
        self.assertIn('</blockquote><ol><li><p>first step</p></li><li><p>second step</p></li></ol><p>Last', out)
        # a marked item that continues an editor list stays in it
        self.assertIn('<ol><li><p>Do this first.</p></li><li><p>Then this.</p></li><li><p>And one more.</p></li></ol>', out)
        hows = {c['how'] for c in rep['carried_formatting']}
        self.assertTrue({"unchanged: the editor's markup", 'blockquote', "the master's own list (ol)"} <= hows, hows)


if __name__ == '__main__':
    unittest.main()
