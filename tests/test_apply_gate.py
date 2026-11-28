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

    def test_the_api_label_human_written_passes(self):
        # the API's windows say "Human Written" where the web app's reader says "Human" (lesson bad-trips-2026-11-25e)
        ok, lines = G.check(recs(('paragraph', PARA, [('Human Written', 'High', 20)])), PARA)
        self.assertTrue(ok, lines)
        ok, _ = G.check(recs(('paragraph', PARA, [('Human Written', 'High', 10), ('Human Written', 'Medium', 10)])), PARA)
        self.assertFalse(ok)
        ok, _ = G.check(recs(('paragraph', PARA, [('AI-Generated', 'High', 20)])), PARA)
        self.assertFalse(ok)

    def test_a_medium_window_fails(self):
        ok, _ = G.check(recs(('paragraph', PARA, [('Human', 'High', 10), ('Human', 'Medium', 10)])), PARA)
        self.assertFalse(ok)

    def test_a_medium_heading_word_or_phrase_doesnt_hold_it_out(self):
        # Joel, 2026-11-28 15:23 UTC: "unless it's just a heading or a word or phrase, but a whole sentence at least yeah
        # that's more important to fix"
        def rec(win):
            out = recs(('paragraph', PARA, [('Human', 'High', 20)]))
            out[1]['windows'].append(win)
            return out
        ok, lines = G.check(rec({'label': 'Human', 'confidence': 'Medium', 'words': 4, 'text': 'Things get tricky fast'}), PARA)
        self.assertTrue(ok, lines)
        self.assertIn('only a heading, a word or a phrase', lines[0])
        ok, _ = G.check(rec({'label': 'Human', 'confidence': 'Medium', 'words': 1, 'text': 'Why?'}), PARA)
        self.assertTrue(ok)
        ok, _ = G.check(rec({'label': 'Human', 'confidence': 'Medium', 'words': 2}), PARA)
        self.assertTrue(ok)
        # a whole sentence, or a window whose text isn't kept and is longer than a phrase, still holds it out
        ok, _ = G.check(rec({'label': 'Human', 'confidence': 'Medium', 'words': 5, 'text': 'Call medics if they faint.'}), PARA)
        self.assertFalse(ok)
        ok, _ = G.check(rec({'label': 'Human', 'confidence': 'Medium', 'words': 9}), PARA)
        self.assertFalse(ok)
        # Low or AI is never minor
        ok, _ = G.check(rec({'label': 'Human', 'confidence': 'Low', 'words': 2, 'text': 'For H.'}), PARA)
        self.assertFalse(ok)
        # and a paragraph whose only window is Medium has nothing High
        ok, _ = G.check(recs(('paragraph', PARA, [('Human', 'Medium', 3)])), PARA)
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

    def test_a_content_change_he_approved_goes_in_without_the_check(self):
        # rules audit 2026-11-28, card C04 (approved)
        owner = {'card': 'C04', 'words': 'yes, put it in', 'where': 'ANSWERS.json, turn 3'}
        ok, lines = G.check([], PARA, owner_approved=owner)
        self.assertTrue(ok)
        self.assertIn('C04', lines[0])
        self.assertIn('yes, put it in', lines[0])
        self.assertIn('ANSWERS.json, turn 3', lines[0])
        self.assertIn('humanizing follows', lines[0])
        self.assertFalse(G.check([], PARA)[0])                    # without it, nothing changes

    def test_an_owner_claim_needs_the_card_his_words_and_where(self):
        for gone in ('card', 'words', 'where'):
            owner = {'card': 'C04', 'words': 'yes', 'where': 'x'}
            owner[gone] = ''
            with self.assertRaises(ValueError):
                G.check([], PARA, owner_approved=owner)

    def test_require_lets_an_approved_text_through_and_records_it(self):
        with tempfile.TemporaryDirectory() as d:
            led = pathlib.Path(d) / 'ledger.jsonl'
            led.write_text('')
            owner = {'card': 'C04', 'words': 'yes', 'where': 'ANSWERS.json'}
            self.assertTrue(G.require(str(led), [PARA], owner_approved=owner))
            with self.assertRaises(SystemExit):
                G.require(str(led), [PARA])


if __name__ == '__main__':
    unittest.main()
