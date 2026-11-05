"""tools/humanization/sense_receipt.py: the making-sense read's receipt (gate E363, enforcing E362; Joel, 2026-11-05 15:14 UTC: "READ what
you wrote, it literally is a whole big waste of time to talk about this, there's NO PAYOFF ... fix the way you work
because i'm not telling you the same stuff over and over")."""
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import sense_receipt as R  # noqa: E402

TEXT = ('As for topical CBD, it hasn\'t been well-studied. There was a short 12-week trial done, where they used a CBD '
        'skin gel, and it didn\'t work any better than placebo. Dr. Smith thought the dose was too low.')
READER = 'someone with a person having a seizure from MDMA or a psychedelic overdose, which is generalized'


def filled(text=TEXT, his=''):
    r = R.make(text, 'Active Seizure', READER, his)
    for x in r['sentences']:
        if not x.get('his'):
            x['payoff'] = 'they know not to count on the gel during a seizure'
            x['follows'] = 'continues the CBD paragraph before it'
    r['placement'] = 'after the cannabis paragraphs, because it carries on from CBD taken other ways'
    r['questions'] = {q: 'PASS: checked against this text' for q in R.QUESTIONS}
    return r


class Sentences(unittest.TestCase):
    def test_splits_on_sentence_ends_but_not_abbreviations(self):
        self.assertEqual(R.sentences(TEXT), [
            'As for topical CBD, it hasn\'t been well-studied.',
            'There was a short 12-week trial done, where they used a CBD skin gel, and it didn\'t work any better than '
            'placebo.',
            'Dr. Smith thought the dose was too low.'])

    def test_closing_quotes_stay_with_their_sentence_and_lines_split(self):
        self.assertEqual(R.sentences('He said "stop." Then he left.\nNew line here'),
                         ['He said "stop."', 'Then he left.', 'New line here'])


class Check(unittest.TestCase):
    def test_a_filled_receipt_passes(self):
        self.assertEqual(R.check(TEXT, filled()), [])

    def test_a_sentence_without_its_payoff_fails(self):
        r = filled()
        r['sentences'][1]['payoff'] = 'none'
        self.assertTrue(any('payoff missing' in p for p in R.check(TEXT, r)))

    def test_a_checked_point_that_lost_its_reason_must_be_cut(self):
        r = filled()
        r['checked'] = [{'point': '7-OH-CBD is more active', 'found': 'about as active as CBD in mice',
                         'still_needed': 'no: nothing was missed', 'fate': 'changed'}]
        self.assertTrue(any('7-OH-CBD' in p and 'cut' in p for p in R.check(TEXT, r)))
        r['checked'][0]['fate'] = 'cut'
        self.assertEqual(R.check(TEXT, r), [])

    def test_a_receipt_for_another_text_fails(self):
        self.assertTrue(any('another text' in p for p in R.check(TEXT + ' More.', filled())))

    def test_the_reader_is_the_case_not_the_topic(self):
        r = filled()
        r['reader'] = 'seizure readers'
        self.assertTrue(any(p.startswith('reader') for p in R.check(TEXT, r)))

    def test_a_failed_or_blank_question_fails(self):
        r = filled()
        r['questions']['Q7'] = 'FAIL: a focal-seizure trial for a generalized-seizure reader'
        r['questions']['Q6'] = ''
        probs = R.check(TEXT, r)
        self.assertTrue(any(p.startswith('Q7 fails') for p in probs))
        self.assertTrue(any(p.startswith('Q6:') for p in probs))

    def test_joels_own_sentences_need_no_payoff(self):
        his = 'As for topical CBD, it hasn\'t been well-studied.'
        r = filled(his=his)
        self.assertTrue(r['sentences'][0].get('his'))
        self.assertEqual(R.check(TEXT, r), [])

    def test_check_files_ignores_the_trailing_newline(self):
        with tempfile.TemporaryDirectory() as d:
            t = pathlib.Path(d, 't.txt')
            t.write_text(TEXT + '\n', encoding='utf-8')
            rp = pathlib.Path(d, 'r.json')
            rp.write_text(json.dumps(filled()), encoding='utf-8')
            self.assertEqual(R.check_files(t, rp), [])


if __name__ == '__main__':
    unittest.main()
