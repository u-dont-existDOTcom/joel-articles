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
            if 'link' in x:
                x['link'] = 'none: each sentence is a new fact the reader expects after the first'
    r['placement'] = 'after the cannabis paragraphs, because it carries on from CBD taken other ways'
    r['opens']['why_reading'] = 'they learn up front that the gel is not something to count on for them'
    r['same_point'] = 'none: read the Active Seizure section from its heading to the next for topical CBD'
    r['needed'] = {'reader': 'a fresh reader given needed_read_brief.md', 'unneeded': [], 'kept': {}}
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


class Needed(unittest.TestCase):
    """Gate neuro-2026-11-08a: a fresh reader's needed read, and a sentence it lists is cut or kept for a reader's use."""
    T = 'D-serine opens the GluD channels. A mutation behind one ataxia leaves them leaking.'

    def receipt(self, **kw):
        r = R.make(self.T, 'B. Section', 'someone deciding whether to take D-serine')
        for i, x in enumerate(r['sentences']):
            x['payoff'] = 'they learn what the tool does at the receptor, which is why it is here'
            x['follows'] = 'it follows the heading, or the sentence before it, on the same receptor'
            if 'link' in x:
                x['link'] = 'none: it opens on its own subject, the same receptor named again'
        r['placement'] = 'the GluD paragraph, after the NMDA one, before the D-serine one'
        r['opens']['why_reading'] = 'it tells the reader what D-serine does, the tool they are about to take'
        r['same_point'] = 'none: read the section from its heading to the next for the receptor points'
        r['questions'] = {q: 'PASS: the evidence is in the text, sentence by sentence' for q in R.QUESTIONS}
        r['needed'] = dict({'reader': 'a fresh reader with needed_read_brief.md', 'unneeded': [], 'kept': {}},
                           **kw.get('needed', {}))
        r['checked'] = kw.get('checked', [])
        return r

    def probs(self, r):
        return [x for x in R.check(self.T, r) if x.startswith('needed') or x.startswith('checked')]

    def test_a_listed_sentence_left_in_fails_until_cut_or_kept_for_a_use(self):
        u = 'A mutation behind one ataxia leaves them leaking.'
        self.assertTrue(self.probs(self.receipt(needed={'unneeded': [u]})))
        self.assertTrue(self.probs(self.receipt(needed={'unneeded': [u], 'kept': {u: 'it is sourced and true'}})))
        self.assertFalse(self.probs(self.receipt(needed={'unneeded': [u], 'kept': {
            u: 'they know the leak is what goes wrong, so they stop if their own balance worsens'}})))

    def test_no_needed_read_fails(self):
        r = self.receipt()
        r['needed']['reader'] = ''
        self.assertTrue(self.probs(r))

    def test_still_needed_says_what_the_reader_does_not_why_the_claim_holds(self):
        c = {'point': 'the leak', 'found': 'Allen 2023', 'fate': 'changed'}
        self.assertTrue(self.probs(self.receipt(checked=[dict(c, still_needed='yes: the guess has a mechanism')])))
        self.assertFalse(self.probs(self.receipt(checked=[dict(c, still_needed='yes: they take D-serine knowing what '
                                                                            'it opens')])))


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


class Link(unittest.TestCase):
    """Gate neuro-2026-11-06b (Joel, 2026-11-06 23:01 UTC: "it was not giving the payoff at the start, i told you this a
    million times"; his "One reason to think about, is that ..." and "So to address that, I've designed ...")."""
    TEXT = ('Have you done years of CBT and still freeze up at the same triggers? Standard therapy rewrites the code while '
            'the motherboard is damaged.')

    def receipt(self, link):
        r = filled(self.TEXT)
        r['sentences'][1]['link'] = link
        return r

    def test_make_asks_for_a_link_after_the_first_sentence(self):
        r = R.make(self.TEXT, 'S', READER)
        self.assertNotIn('link', r['sentences'][0])
        self.assertEqual(r['sentences'][1]['link'], '')

    def test_the_link_must_be_words_in_the_sentence(self):
        self.assertTrue(any(p.startswith('link for') for p in R.check(self.TEXT, self.receipt('One reason to think about'))))
        self.assertTrue(any(p.startswith('link for') for p in R.check(self.TEXT, self.receipt(''))))
        self.assertTrue(any(p.startswith('link for') for p in R.check(self.TEXT, self.receipt('none: no'))))

    def test_his_kind_of_link_passes(self):
        text = self.TEXT.replace('Standard therapy rewrites', 'One reason to think about, is that standard therapy rewrites')
        r = filled(text)
        r['sentences'][1]['link'] = 'One reason to think about, is that'
        self.assertEqual(R.check(text, r), [])
