"""tools/humanization/sense_receipt.py: the making-sense read's receipt (gate E365, enforcing E362; Joel, 2026-11-05 15:14 UTC: "READ what
you wrote, it literally is a whole big waste of time to talk about this, there's NO PAYOFF ... fix the way you work
because i'm not telling you the same stuff over and over"). Since the rules audit of 2026-11-28 (cards C02, C03 and C17)
it is a light note: check() reports only what is present and wrong."""
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
    r['his_fixes'] = {'reader': 'a fresh reader given his_fixes_brief.md', 'marked': [], 'kept': {}}
    r['fit'] = {'reader': 'a fresh reader given fit_read_brief.md', 'marked': [], 'kept': {}}
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

    def test_a_sentence_without_its_payoff_is_not_a_problem(self):
        # rules audit 2026-11-28, card C02 (approved): the receipt is a light note; an empty field is not a problem
        r = filled()
        r['sentences'][1]['payoff'] = 'none'
        r['sentences'][2]['payoff'] = ''
        r['sentences'][2]['follows'] = ''
        self.assertEqual(R.check(TEXT, r), [])

    def test_a_blank_receipt_from_make_is_a_prompt_not_a_failure(self):
        """Rules audit 2026-11-28, cards C02, C03 and C17: make still writes every field, empty, as a prompt, and check()
        reports only what is present and wrong, so the receipt as make writes it has nothing wrong."""
        r = R.make(TEXT, 'Active Seizure', '')
        self.assertEqual(r['placement'], '')
        self.assertEqual(r['same_point'], '')
        self.assertEqual(r['opens']['why_reading'], '')
        self.assertEqual(r['needed'], {'reader': '', 'unneeded': [], 'kept': {}})
        self.assertEqual(r['his_fixes'], {'reader': '', 'marked': [], 'kept': {}})
        self.assertEqual(r['fit'], {'reader': '', 'marked': [], 'kept': {}})
        self.assertEqual(set(r['questions'].values()), {''})
        self.assertEqual([x.get('payoff') for x in r['sentences']], ['', '', ''])
        self.assertEqual([x.get('link') for x in r['sentences']], [None, '', ''])
        self.assertEqual(R.check(TEXT, r), [])
        import io, contextlib, os
        with tempfile.TemporaryDirectory() as d:
            tp, rp = os.path.join(d, 't.txt'), os.path.join(d, 'r.json')
            pathlib.Path(tp).write_text(TEXT + '\n', encoding='utf-8')
            pathlib.Path(rp).write_text(json.dumps(r), encoding='utf-8')
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                self.assertEqual(R.main(['check', tp, rp]), 0)
            self.assertTrue(out.getvalue().startswith('PASS'))
            r['questions']['Q7'] = 'FAIL: a focal-seizure trial for a generalized-seizure reader'
            pathlib.Path(rp).write_text(json.dumps(r), encoding='utf-8')
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(R.main(['check', tp, rp]), 1)

    def test_a_checked_point_that_lost_its_reason_must_be_cut(self):
        r = filled()
        r['checked'] = [{'point': '7-OH-CBD is more active', 'found': 'about as active as CBD in mice',
                         'still_needed': 'no: nothing was missed', 'fate': 'changed'}]
        self.assertTrue(any('7-OH-CBD' in p and 'cut' in p for p in R.check(TEXT, r)))
        r['checked'][0]['fate'] = 'cut'
        self.assertEqual(R.check(TEXT, r), [])

    def test_a_receipt_for_another_text_fails(self):
        self.assertTrue(any('another text' in p for p in R.check(TEXT + ' More.', filled())))

    def test_a_sentence_left_out_is_not_a_problem_but_one_not_in_the_text_is(self):
        # card C02: what is missing is not a problem; a sentence the text doesn't have means the note is for another text
        r = filled()
        del r['sentences'][2]
        self.assertEqual(R.check(TEXT, r), [])
        r['sentences'].append({'s': 'A sentence from another draft.', 'payoff': 'x', 'follows': 'y'})
        self.assertTrue(any(p.startswith('sentences:') and 'another draft' in p for p in R.check(TEXT, r)))

    def test_a_short_or_empty_reader_is_the_reads_to_judge(self):
        # the case, not the topic, is still what the field asks for; the code no longer counts its letters (card C02)
        r = filled()
        r['reader'] = 'seizure readers'
        self.assertEqual(R.check(TEXT, r), [])
        r['reader'] = ''
        self.assertEqual(R.check(TEXT, r), [])

    def test_a_failed_question_fails_and_a_blank_one_does_not(self):
        r = filled()
        r['questions']['Q7'] = 'FAIL: a focal-seizure trial for a generalized-seizure reader'
        r['questions']['Q6'] = ''
        del r['questions']['Q5']
        probs = R.check(TEXT, r)
        self.assertTrue(any(p.startswith('Q7 fails') for p in probs))
        self.assertFalse(any(p.startswith('Q6') or p.startswith('Q5') for p in probs), probs)
        self.assertEqual(len(probs), 1, probs)

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

    def test_no_needed_read_is_not_a_problem(self):
        # rules audit 2026-11-28, card C17 (revised as his note says): a fresh read is a help whose marks are each judged,
        # not a gate, so a read not done is not a problem; its marks, when there are any, still are
        r = self.receipt()
        r['needed']['reader'] = ''
        self.assertFalse(self.probs(r))
        del r['needed']
        self.assertFalse(self.probs(r))
        u = 'A mutation behind one ataxia leaves them leaking.'
        self.assertTrue(self.probs(self.receipt(needed={'reader': '', 'unneeded': [u]})))

    def test_still_needed_says_what_the_reader_does_not_why_the_claim_holds(self):
        c = {'point': 'the leak', 'found': 'Allen 2023', 'fate': 'changed'}
        self.assertTrue(self.probs(self.receipt(checked=[dict(c, still_needed='yes: the guess has a mechanism')])))
        self.assertFalse(self.probs(self.receipt(checked=[dict(c, still_needed='yes: they take D-serine knowing what '
                                                                            'it opens')])))



class HisFixes(unittest.TestCase):
    """Gate bad-trips-2026-11-12g: a fresh reader's read against his fixes, and a sentence it marks is changed or kept with
    the reason it stays."""
    S = 'Dr. Smith thought the dose was too low.'

    def probs(self, r):
        return [x for x in R.check(TEXT, r) if x.startswith('his_fixes')]

    def test_a_filled_read_passes(self):
        self.assertEqual(self.probs(filled()), [])

    def test_no_read_is_not_a_problem(self):
        # rules audit 2026-11-28, card C17: the read is a help whose marks are each judged, not a gate
        r = filled()
        r['his_fixes']['reader'] = ''
        self.assertFalse(self.probs(r))
        del r['his_fixes']
        self.assertFalse(self.probs(r))

    def test_the_read_is_against_any_of_his_fixes_in_the_repo(self):
        # his note on card C17: "and not just against my own fixes in that article of course but any fixes in the repo
        # that could be useful for that context"
        for doc in (R.his_fixes_problems.__doc__, R.__doc__):
            self.assertIn('any fixes in the repo that could be useful for that context', ' '.join(doc.split()))

    def test_a_marked_sentence_left_in_fails_until_changed_or_kept_with_a_reason(self):
        r = filled()
        r['his_fixes']['marked'] = [{'s': self.S, 'difference': '7'}]
        self.assertTrue(self.probs(r))
        r['his_fixes']['kept'] = {self.S: 'it stays: the reader needs who doubted the dose'}
        self.assertFalse(self.probs(r))
        r['his_fixes']['kept'] = {}
        self.assertFalse(self.probs(dict(r, his_fixes={'reader': 'a fresh reader', 'marked': [{'s': 'Gone from the text.'}]})))

    def test_a_receipt_made_before_the_rule_is_read_as_it_was(self):
        r = filled()
        del r['his_fixes']
        r['made'] = '2026-11-11'
        self.assertFalse(self.probs(r))



class Fit(unittest.TestCase):
    """Gate bad-trips-2026-11-12j: a fresh reader's fit read, and a line it marks is changed or kept with the reason it
    fits."""
    S = 'Dr. Smith thought the dose was too low.'

    def probs(self, r):
        return [x for x in R.check(TEXT, r) if x.startswith('fit')]

    def test_a_filled_read_passes(self):
        self.assertEqual(self.probs(filled()), [])

    def test_no_read_is_not_a_problem(self):
        # rules audit 2026-11-28, card C17: the read is a help whose marks are each judged, not a gate
        r = filled()
        r['fit']['reader'] = ''
        self.assertFalse(self.probs(r))
        del r['fit']
        self.assertFalse(self.probs(r))

    def test_a_marked_line_left_in_fails_until_changed_or_kept_with_a_reason(self):
        r = filled()
        r['fit']['marked'] = [{'s': self.S, 'found': 'ANYWAY'}]
        self.assertTrue(self.probs(r))
        r['fit']['kept'] = {self.S: 'it fits: the dose is the guide\'s own claim, not a sign to look for'}
        self.assertFalse(self.probs(r))

    def test_a_receipt_made_before_the_rule_is_read_as_it_was(self):
        r = filled()
        del r['fit']
        r['made'] = '2026-11-12'
        self.assertFalse(self.probs(r))


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

    def test_the_opening_is_not_refused(self):
        # rules audit 2026-11-28, card C03 (approved): payoff first stays his test, and the reader's-case opening is one
        # way he has met it, to consider, not to require: "the receipt's opens refusal goes"
        r = filled()
        r['opens']['why_reading'] = 'none'
        self.assertEqual(R.check(TEXT, r), [])
        r['opens'] = {}
        self.assertEqual(R.check(TEXT, r), [])

    def test_the_same_point_and_placement_left_empty_are_not_problems(self):
        # card C02: a field that is missing or empty is not a problem
        r = filled()
        r['same_point'] = ''
        r['placement'] = ''
        self.assertEqual(R.check(TEXT, r), [])
        r['same_point'] = 'none, there is nothing like it anywhere else here'
        self.assertEqual(R.check(TEXT, r), [])

    def test_a_receipt_without_the_fields_passes_whenever_it_was_made(self):
        r = filled()
        del r['opens'], r['same_point'], r['placement']
        for made in ('2026-11-05', '2026-11-07', '2026-11-28'):
            r['made'] = made
            self.assertEqual(R.check(TEXT, r), [], made)


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

    def test_quoted_link_words_must_be_in_the_sentence(self):
        self.assertTrue(any(p.startswith('link for') for p in R.check(self.TEXT, self.receipt('One reason to think about'))))
        # card C02: an empty link, or "none" with or without its why, quotes nothing, so nothing in it is wrong
        for empty in ('', 'none', 'none: no', 'None - a new step'):
            self.assertFalse(any(p.startswith('link for') for p in R.check(self.TEXT, self.receipt(empty))), empty)

    def test_his_kind_of_link_passes(self):
        text = self.TEXT.replace('Standard therapy rewrites', 'One reason to think about, is that standard therapy rewrites')
        r = filled(text)
        r['sentences'][1]['link'] = 'One reason to think about, is that'
        self.assertEqual(R.check(text, r), [])


class LinkAtTheStart(unittest.TestCase):
    """Lesson bad-trips-2026-11-22a (Joel, 2026-11-22 17:21 UTC: "S2 doesn't follow from S1. you really don't see that?
    what's connecting them? even "So" would connect"): the tie to the sentence before comes early. Rules audit 2026-11-28,
    card C02 (approved): that is judged by reading the sentence, not by counting words, so the five-word test is gone."""
    S1 = "Serotonin syndrome comes from too much serotonin, so I'd stop anything suspected of adding more."
    LATE = S1 + (" No more MDMA or other stimulants, of course, but also no DXM cough syrup, the painkiller tramadol or the "
                 "antibiotic linezolid.")
    HIS = S1 + (" So no more MDMA or other stimulants, of course, but also no DXM cough syrup, the painkiller tramadol or "
                "the antibiotic linezolid.")

    def receipt(self, text, link, made):
        r = filled(text)
        r['sentences'][1]['link'] = link
        r['made'] = made
        return r

    def test_a_tie_after_five_words_is_not_refused(self):
        for made in ('2026-11-22', '2026-11-28'):
            p = R.check(self.LATE, self.receipt(self.LATE, 'of course, but also', made))
            self.assertEqual(p, [], made)

    def test_his_so_at_the_start_passes(self):
        self.assertEqual(R.check(self.HIS, self.receipt(self.HIS, 'So', '2026-11-22')), [])

    def test_receipts_made_before_the_lesson_are_checked_as_before(self):
        p = R.check(self.LATE, self.receipt(self.LATE, 'of course, but also', '2026-11-21'))
        self.assertFalse(any('come after' in x for x in p), p)

    def test_a_link_address_before_the_tie_is_not_counted(self):
        # turn 61: "[DMSO](https://.../dmso), though" counted the address's words and refused a tie at word two
        s1 = "Niacin is unsafe with serotonin syndrome, since it can drop the blood pressure."
        text = s1 + " [DMSO](https://ibogaqueen.substack.com/i/170920118/dmso), though, seems to help prevent seizures."
        self.assertFalse(any('come after' in x for x in R.check(text, self.receipt(text, 'though', '2026-11-23'))))

    def test_none_with_a_reason_still_passes(self):
        r = self.receipt(self.LATE, 'none: a new step, which the reader expects after the one before', '2026-11-22')
        self.assertFalse(any(x.startswith('link for') for x in R.check(self.LATE, r)))


class HisAnswer(unittest.TestCase):
    """Lesson bad-trips-2026-11-27m, correcting k: his "it absorbs almost as well as eating it, especially on sensitive
    skin" went in as "Its juice works through the skin almost as well as eating the leaf does". What bears on his claim
    needs a place, a reason or a question; not every word of his reaches the sentence (Joel, 2026-11-27 22:48 UTC: "it's
    not that every word of my answer has to reach the sentence that says my point")."""
    TEXT = ('The leaf is strong enough that even picking one can relax me if the juice touches sensitive skin. Its juice '
            'works through the skin almost as well as eating the leaf does.')
    SAID = 'it absorbs almost as well as eating it, especially on sensitive skin'

    def problems(self, text, entries, found='review/r62/ANSWERS-R62.json, card LEAF-JUICE: his words'):
        r = {'made': '2026-11-27', 'checked': [{'found': found}], 'his_answer': entries}
        return R.his_answer_problems(text, r)

    def test_words_of_his_are_not_each_required(self):
        into = 'Its juice works through sensitive skin almost as well as eating the leaf does.'
        text = self.TEXT.replace('through the skin', 'through sensitive skin')
        self.assertEqual(self.problems(text, [{'said': self.SAID, 'in': into}]), [])

    def test_a_left_out_part_needs_a_reason_or_a_question(self):
        into = 'Its juice works through the skin almost as well as eating the leaf does.'
        probs = self.problems(self.TEXT, [{'said': self.SAID, 'in': into, 'left_out': {'especially on sensitive skin': ''}}])
        self.assertTrue(any('no reason' in x for x in probs), probs)
        fine = {'especially on sensitive skin': 'asked: card SKIN-SCOPE, whether the whole leaf works on any skin'}
        self.assertEqual(self.problems(self.TEXT, [{'said': self.SAID, 'in': into, 'left_out': fine}]), [])

    def test_a_turn_74_receipt_with_words_is_read_as_left_out(self):
        into = 'Its juice works through the skin almost as well as eating the leaf does.'
        probs = self.problems(self.TEXT, [{'said': self.SAID, 'in': into, 'words': {'sensitive': ''}}])
        self.assertTrue(any('no reason' in x for x in probs), probs)

    def test_candidates_list_his_words_the_sentence_lacks(self):
        into = 'Its juice works through the skin almost as well as eating the leaf does.'
        self.assertEqual(R.candidates(self.SAID, into), ['absorbs', 'especially', 'sensitive'])

    def test_no_entry_is_required(self):
        self.assertEqual(self.problems(self.TEXT, []), [])
        self.assertEqual(self.problems(self.TEXT, [], found='his post as of 2026-11-03'), [])

    def test_the_sentence_must_be_in_the_text(self):
        probs = self.problems(self.TEXT, [{'said': self.SAID, 'in': 'Nothing like this is in the text.'}])
        self.assertTrue(any('not in the text' in x for x in probs), probs)

