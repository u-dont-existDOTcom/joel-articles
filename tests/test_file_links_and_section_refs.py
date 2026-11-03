"""Tests for tools/humanization/file_links_check.py (E337 (Inner Child)) and section_refs.py (E338 (Inner Child))."""
import pathlib
import sys
import tempfile
import unittest
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import file_links_check as flc  # noqa: E402
import section_refs as srf  # noqa: E402

ARTICLE = ('# Guide\n\nRead my [shame guide](https://example.org/shame) and [the post](example.org/post/).\n\n'
           '<!-- IMAGE https://cdn.example.org/chart.png : the chart -->\n\nText.\n')


def docx(path, links, images=0):
    rels = ''.join('<Relationship Id="rId%d" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink" '
                   'Target="%s" TargetMode="External"/>' % (n, u) for n, u in enumerate(links, 1))
    body = ''.join('<w:hyperlink r:id="rId%d"><w:r><w:t>x</w:t></w:r></w:hyperlink>' % n for n in range(1, len(links) + 1))
    with zipfile.ZipFile(path, 'w') as z:
        z.writestr('word/_rels/document.xml.rels', '<Relationships>%s</Relationships>' % rels)
        z.writestr('word/document.xml', '<w:document><w:body>%s</w:body></w:document>' % body)
        for n in range(images):
            z.writestr('word/media/image%d.png' % n, b'png')


class FileLinks(unittest.TestCase):
    def setUp(self):
        self.d = pathlib.Path(tempfile.mkdtemp())
        (self.d / 'a.md').write_text(ARTICLE, encoding='utf-8')

    def test_plain_text_file_fails(self):
        """The turn-115 case: a Word file with no links and no pictures."""
        docx(self.d / 'f.docx', [])
        missing, apics, fpics = flc.lost(str(self.d / 'a.md'), str(self.d / 'f.docx'))
        self.assertEqual(len(missing), 2)
        self.assertEqual((apics, fpics), (1, 0))
        self.assertEqual(flc.main(['--article', str(self.d / 'a.md'), str(self.d / 'f.docx')]), 1)

    def test_file_with_links_and_picture_passes(self):
        docx(self.d / 'f.docx', ['https://example.org/shame', 'http://example.org/post'], images=1)
        self.assertEqual(flc.main(['--article', str(self.d / 'a.md'), str(self.d / 'f.docx')]), 0)

    def test_markdown_file(self):
        (self.d / 'f.md').write_text('[shame](https://example.org/shame)\n\n[image 1](Pictures/x.png)\n', encoding='utf-8')
        missing, _, fpics = flc.lost(str(self.d / 'a.md'), str(self.d / 'f.md'))
        self.assertEqual([u for u, _ in missing], ['https://example.org/post'])
        self.assertEqual(fpics, 1)


class SectionRefs(unittest.TestCase):
    OLD = '# A\n\n## Hear the Guard First\n\nGuard text.\n\n## Noticing Counts\n\nNotice.\n'
    NEW = ('# A\n\n## If You Want to Kill Yourself\n\nNotice who is noticing (as described in Noticing Counts).\n\n'
           '## Noticing Counts\n\nNotice.\n\n## Later Things\n\nHear it out, the way you did in Hear the Guard First. '
           'More in Noticing Counts, further on.\n')

    def test_back_pointer_to_a_later_section(self):
        rows = srf.refs(self.NEW)
        f = [r for r in rows if r['flag'] and r['title'] == 'noticing counts']
        self.assertEqual(len(f), 2)   # "as described in" pointing ahead, and "further on" pointing back
        self.assertIn('comes later', f[0]['flag'])
        self.assertIn('came before', f[1]['flag'])

    def test_gone_section(self):
        rows = srf.refs(self.NEW, self.OLD)
        self.assertTrue(any(r['where'] == 'gone' and r['title'] == 'hear the guard first' for r in rows))

    def test_clean(self):
        md = '# A\n\n## Noticing Counts\n\nNotice.\n\n## B Section\n\nAs described in Noticing Counts, notice.\n'
        self.assertEqual([r for r in srf.refs(md) if r['flag']], [])


if __name__ == '__main__':
    unittest.main()
