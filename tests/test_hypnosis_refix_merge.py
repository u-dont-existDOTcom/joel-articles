"""refix_runs._merge (the hypnosis guide lane, 2026-10-18): a refix run's output split one paragraph per block must replace
every block of the stretch it came from, never only the first (HG36 lost B10-B12 that way, HG24 B43-B48)."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'articles' / 'inner-signal' / 'humanize' / 'tools'))
import refix_runs as R  # noqa: E402


def seg(blocks, paras):
    return (blocks, paras, 'run', 'file')


class MergeTest(unittest.TestCase):
    def setUp(self):
        self.d = {'key': 'K', 'units': [
            {'kind': 'published', 'blocks': [0], 'paras': ['Heading']},
            {'kind': 'emulate', 'blocks': [1, 2, 3], 'paras': ['one', 'two', 'three']},
            {'kind': 'emulate', 'blocks': [4, 5], 'paras': ['four and five together']},
            {'kind': 'published', 'blocks': [6], 'paras': ['six']}]}

    def text(self, segs):
        out = []
        for kind, u in R._merge(self.d, segs):
            out += u['paras'] if kind == 'base' else u[1]
        return out

    def test_one_segment_per_block_replaces_the_whole_unit(self):
        segs = {('K', b): seg([b], ['new %d' % b]) for b in (1, 2, 3)}
        self.assertEqual(self.text(segs), ['Heading', 'new 1', 'new 2', 'new 3', 'four and five together', 'six'])

    def test_a_segment_over_the_whole_unit(self):
        self.assertEqual(self.text({('K', 1): seg([1, 2, 3], ['all new'])}), ['Heading', 'all new', 'four and five together', 'six'])

    def test_partial_cover_keeps_the_other_paragraphs_when_they_line_up(self):
        self.assertEqual(self.text({('K', 2): seg([2], ['new 2'])}), ['Heading', 'one', 'new 2', 'three', 'four and five together', 'six'])

    def test_partial_cover_that_cannot_line_up_raises(self):
        with self.assertRaises(ValueError):
            self.text({('K', 4): seg([4], ['new 4'])})

    def test_no_segments_keeps_everything(self):
        self.assertEqual(self.text({}), ['Heading', 'one', 'two', 'three', 'four and five together', 'six'])


if __name__ == '__main__':
    unittest.main()
