"""tools/humanization/sense_receipt.py: the making-sense read's receipt (gate E365, enforcing E362; Joel, 2026-11-05 15:14 UTC: "READ what
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


def filled(text=TEXT, his='', whose='his own: a test line he wrote into the guide'):
    r = R.make(text, 'Active Seizure', READER, his, whose if his else '')
    for x in r['sentences']:
        if not x.get('his'):
            x['payoff'] = 'they know not to count on the gel during a seizure'
            x['follows'] = 'continues the CBD paragraph before it'
    r['placement'] = 'after the cannabis paragraphs, because it carries on from CBD taken other ways'
    r['opens']['why_reading'] = 'they learn up front that the gel is not something to count on for them'
    r['same_point'] = 'none: read the Active Seizure section from its heading to the next for topical CBD'
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

    def test_only_what_he_wrote_himself_is_marked_his(self):
        """Gate E373, Joel 2026-11-06 17:30 UTC: "'my words' for an AI article, are not my words, unless those were human
        before we started humanizing ... otherwise it's AI words that i humanized". The room stretch's receipt had marked
        his round-8 version of the guide's AI text his, so its sentences skipped the payoff and follows."""
        his = 'As for topical CBD, it hasn\'t been well-studied.'
        with self.assertRaises(ValueError):
            R.make(TEXT, 'Active Seizure', READER, his, 'his round-8 version')
        r = filled(his=his)
        r['his_whose'] = 'his round-8 version'
        self.assertTrue(any('marked his' in p and 'E373' in p for p in R.check(TEXT, r)))
        r['made'] = '2026-11-05'   # a receipt made before the rule is read as it was
        self.assertEqual(R.check(TEXT, r), [])
        import io, contextlib, tempfile, os
        with tempfile.TemporaryDirectory() as d:
            tp, hp = os.path.join(d, 't.txt'), os.path.join(d, 'h.txt')
            pathlib.Path(tp).write_text(TEXT, encoding='utf-8')
            pathlib.Path(hp).write_text(his, encoding='utf-8')
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(R.main(['make', tp, '--his', hp, '--out', os.path.join(d, 'r.json')]), 2)
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(R.main(['make', tp, '--his', hp, '--whose', 'his own: his line of 2026-11-04, t04 answers',
                                         '--out', os.path.join(d, 'r.json')]), 0)

    def test_a_term_is_explained_where_it_is_first_used(self):
        """Gate E369 (Joel, 2026-11-05 18:43 UTC: "make sure every term is introduced once at first, like enterocytes my
        readers won't know what those are"). The colostrum note after the item read AI, Medium."""
        late = ('Liposomal first-milking colostrum, fermented with SIBO yogurt bacteria. Colostrum is the first milk a '
                'cow makes after giving birth, and liposomal means it comes in tiny fat bubbles.')
        probs = R.check(late, filled(late))
        self.assertTrue(any('"Colostrum" is explained' in p and 'E369' in p for p in probs))
        first = ('Liposomal first-milking colostrum, the first milk a cow makes after giving birth, wrapped in tiny fat '
                 'bubbles that help you absorb it.')
        self.assertEqual(R.check(first, filled(first)), [])
        r = filled(late)
        r['late_ok'] = {'Colostrum': 'the item is a product name he copies from the label, and it must lead'}
        self.assertEqual(R.check(late, r), [])

    def test_a_pronoun_or_his_own_definition_is_not_a_late_term(self):
        text = 'Glutamine feeds the gut lining. That is the main point. Glutamine is the fuel the enterocytes prefer.'
        self.assertEqual(R.check(text, filled(text, his='Glutamine is the fuel the enterocytes prefer.')), [])
        self.assertEqual([t for t, s in R.late_definitions(text, filled(text))], ['Glutamine'])

    def test_check_files_ignores_the_trailing_newline(self):
        with tempfile.TemporaryDirectory() as d:
            t = pathlib.Path(d, 't.txt')
            t.write_text(TEXT + '\n', encoding='utf-8')
            rp = pathlib.Path(d, 'r.json')
            rp.write_text(json.dumps(filled()), encoding='utf-8')
            self.assertEqual(R.check_files(t, rp), [])


if __name__ == '__main__':
    unittest.main()


class Paragraph(unittest.TestCase):
    """Gates E374 and E376 (Joel, 2026-11-06 19:40 UTC, on my dynorphin tries: "it was not giving the payoff quick
    enough. i was as usual wondering why am i reading this?"; "delete the "hardening" para since i had to incorporate
    that into this one, otherwise it was out of order and a bit redundant")."""

    def test_make_writes_the_first_sentence_and_both_fields(self):
        r = R.make(TEXT, 'Active Seizure', READER)
        self.assertEqual(r['opens'], {'first_sentence': 'As for topical CBD, it hasn\'t been well-studied.',
                                      'why_reading': ''})
        self.assertEqual(r['same_point'], '')

    def test_the_paragraph_must_say_why_its_first_sentence_is_read(self):
        r = filled()
        r['opens']['why_reading'] = 'none'
        self.assertTrue(any(p.startswith('opens:') for p in R.check(TEXT, r)))
        r = filled()
        r['opens']['first_sentence'] = 'Some other opening.'
        self.assertTrue(any('first_sentence' in p for p in R.check(TEXT, r)))

    def test_the_same_point_elsewhere_must_be_answered(self):
        r = filled()
        r['same_point'] = ''
        self.assertTrue(any(p.startswith('same_point:') for p in R.check(TEXT, r)))
        r['same_point'] = 'none, there is nothing like it anywhere else here'
        self.assertTrue(any(p.startswith('same_point:') for p in R.check(TEXT, r)))

    def test_an_older_receipt_without_the_fields_is_checked_as_before(self):
        r = filled()
        del r['opens'], r['same_point']
        r['made'] = '2026-11-05'
        self.assertEqual(R.check(TEXT, r), [])
        r['made'] = '2026-11-07'
        self.assertTrue(any(p.startswith('opens:') for p in R.check(TEXT, r)))
