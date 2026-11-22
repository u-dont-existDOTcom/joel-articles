"""apply_gate.py: a paragraph of mine goes in only when a check of it by itself read Human High in every window."""
import json, pathlib, sys, tempfile, unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import apply_gate as G  # noqa: E402


def recs(*checks):
    out = []
    for n, (scope, text, wins) in enumerate(checks):
        pid = 'lin#%d' % (n + 1)
        out.append({'type': 'prediction', 'id': pid, 'lineage': 'lin', 'scope': scope, 'text': text, 'call': 'Human'})
        out.append({'type': 'result', 'prediction': pid, 'link': 'https://www.pangram.com/history/x%d' % n,
                    'windows': [{'label': l, 'confidence': c, 'words': w} for l, c, w in wins]})
    return out


PARA = "After giving it, keep a close eye on their breathing, since a benzodiazepine adds to the risk."


class Gate(unittest.TestCase):
    def test_alone_all_high_passes(self):
        ok, lines = G.check(recs(('paragraph', PARA, [('Human', 'High', 20)])), PARA)
        self.assertTrue(ok, lines)

    def test_a_medium_window_fails(self):
        ok, _ = G.check(recs(('paragraph', PARA, [('Human', 'High', 10), ('Human', 'Medium', 10)])), PARA)
        self.assertFalse(ok)

    def test_ai_alone_fails_even_when_the_section_reads_high(self):
        r = recs(('paragraph', PARA, [('AI-Generated', 'High', 20)]),
                 ('section', 'Active Seizure\n\nTime it.\n\n' + PARA, [('Human', 'High', 30)]))
        self.assertFalse(G.check(r, PARA)[0])

    def test_section_counts_only_with_a_reason(self):
        r = recs(('section', 'Active Seizure\n\n' + PARA, [('Human', 'High', 30)]))
        self.assertFalse(G.check(r, PARA)[0])
        self.assertTrue(G.check(r, PARA, section_ok='it points to the list above it')[0])

    def test_markdown_in_the_guide_matches_the_typed_text(self):
        md = ("After giving it, keep a close eye on their breathing, since a [benzodiazepine](https://x.org/1) adds to "
              "the **risk**.")
        ok, lines = G.check(recs(('paragraph', PARA, [('Human', 'High', 20)])), md)
        self.assertTrue(ok, lines)

    def test_words_not_checked_fail(self):
        ok, lines = G.check(recs(('paragraph', 'Something else entirely.', [('Human', 'High', 20)])), PARA)
        self.assertFalse(ok)
        self.assertIn('no check', lines[0])

    def test_require_exits_with_the_reasons(self):
        with tempfile.TemporaryDirectory() as d:
            led = pathlib.Path(d) / 'ledger.jsonl'
            led.write_text('\n'.join(json.dumps(r) for r in recs(('paragraph', PARA, [('Human', 'Low', 20)]))) + '\n')
            with self.assertRaises(SystemExit) as e:
                G.require(str(led), [PARA])
            self.assertIn('not Human High', str(e.exception))


if __name__ == '__main__':
    unittest.main()
