"""Regression tests for the shared humanization tools' 2026-10-02 additions: the exact-character ledger check,
the linter's abstract-agent flag (O6) and the whole-article stance-check prompt."""
import json
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
# The linter's parsed O6 check loads spaCy, a second or two per run; these tests run it only where they test it.
os.environ['TELLS_LINT_PARSE'] = '0'
TOOLS = ROOT / 'tools' / 'humanization'
sys.path.insert(0, str(TOOLS))

import check_owner_edits  # noqa: E402
import stance_check_prompt  # noqa: E402
import abstract_agents_prompt  # noqa: E402
import preservation_keys  # noqa: E402
import meaning_sweep  # noqa: E402

JOEL_P9 = ("I dream of a way to work in depth that isn’t run by a guru. A place where people who've done the "
           "healing first can join without pretending they're fully finished.")


class OwnerEditsExactCharacters(unittest.TestCase):
    def run_ledger(self, article_text):
        with tempfile.TemporaryDirectory() as d:
            art = pathlib.Path(d) / 'a.md'
            led = pathlib.Path(d) / 'l.json'
            art.write_text('# Title\n\n' + article_text + '\n', encoding='utf-8')
            led.write_text(json.dumps({'entries': [{
                'id': 'p9', 'what': "Joel's P9", 'status': 'applied',
                'must_contain': ["people who’ve done the healing first"],
                'must_contain_exact': ["people who've done the healing first can join without pretending they're fully finished"],
            }]}), encoding='utf-8')
            return check_owner_edits.run(str(art), str(led))

    def test_his_characters_pass(self):
        r = self.run_ledger(JOEL_P9)
        self.assertEqual(r['failed'], [])
        self.assertEqual(r['passed'], 1)

    def test_curled_apostrophes_fail_only_the_exact_check(self):
        r = self.run_ledger(JOEL_P9.replace("who've", "who’ve").replace("they're", "they’re"))
        self.assertEqual(len(r['failed']), 1)
        fails = r['failed'][0]['fails']
        self.assertEqual(len(fails), 1)
        self.assertIn('exact characters', fails[0])


class LinterAbstractAgents(unittest.TestCase):
    def lint(self, text):
        with tempfile.TemporaryDirectory() as d:
            f = pathlib.Path(d) / 'draft.txt'
            f.write_text(text, encoding='utf-8')
            r = subprocess.run([sys.executable, str(TOOLS / 'tells_lint.py'), str(f)], capture_output=True, text=True)
            return r.stdout

    def test_feeling_doing_a_persons_job_is_flagged(self):
        out = self.lint('There is no shared way to talk about the hurt, so the anger goes there, trying to get some justice.\n')
        self.assertIn('O6', out)

    def test_polished_enough_pair_is_flagged(self):
        out = self.lint('A living community should relate to its teachings the same way: devoted enough to practice them and secure enough to disagree.\n')
        self.assertIn('O7', out)
        self.assertNotIn('O7', self.lint('She was old enough to vote, and she did.\n'))

    def test_smuggling_talk_fails(self):
        """O8 (Joel, 2026-10-03 20:51): "ai is always saying something like 'not smuggle in'"."""
        out = self.lint('That includes some uses of ketamine and MDMA and bufo. My reasons are in those articles, not smuggled into one sentence here.\n')
        self.assertIn('O8 owner ban', out)
        self.assertIn('verdict: FAIL', out)
        out = self.lint('That includes some uses of ketamine and MDMA and bufo. My reasons are given in those articles, respectively, since they need more space.\n')
        self.assertNotIn('O8', out)
        out = self.lint('In 1971 two of the members were caught smuggling hashish across the border from Mexico.\n')
        self.assertIn('O8 "smuggle"', out)
        self.assertNotIn('O8 owner ban', out)

    def test_not_y_tail_is_flagged(self):
        """O9 (Joel, same message): "it always wants to add a 'not Y' part"."""
        out = self.lint('If people are training there so they can help others build communities of their own, they are building a genuine alternative, not just escaping society.\n')
        self.assertIn('O9', out)
        self.assertNotIn('O9', self.lint('No, not today. We will talk about the money when everyone is back from the market.\n'))
        self.assertNotIn('O9', self.lint('She did not want to leave, and she said so at the meeting on Sunday.\n'))

    def test_x_not_y_heading_fails(self):
        """H1 (Joel, 2026-10-06): "that heading looks way ai for sure. always trying to do an x not y statement"."""
        body = '\n\nMost of the writing on communities has not caught up with psychedelics, which went from taboo toward regulated use fast.\n'
        out = self.lint('# The Medicine Part, Without Pretending It Isn\u2019t There' + body)
        self.assertIn('H1 x-not-y heading', out)
        self.assertIn('verdict: FAIL', out)
        self.assertNotIn('H1', self.lint("# The Medicine Part - Yes, I'm Naming It" + body))
        self.assertIn('H1 a negation in a heading', self.lint('# The Math of Absorption, and Who This Isn\u2019t For' + body))

    def test_opener_pointing_at_nothing_fails(self):
        """O10 (Joel, 2026-10-06): "'Key here' can't be how you open a section. that's referring to something. Key where? what?"."""
        out = self.lint("# The Medicine Part - Yes, I'm Naming It\n\nKey here is that most of the writing on communities hasn't caught up with psychedelics. They moved fast.\n")
        self.assertIn('O10 an opener that points at nothing', out)
        self.assertIn('verdict: FAIL', out)
        out = self.lint("# The Medicine Part - Yes, I'm Naming It\n\nMost of the writing on communities hasn't caught up with psychedelics. They moved fast.\n")
        self.assertNotIn('O10', out)
        out = self.lint('# Integration\n\nThis is where most groups give up on it, after the first few months of trying hard.\n')
        self.assertIn('O10 the first sentence under a heading opens with a pointer', out)

    def test_person_doing_it_is_not_flagged(self):
        out = self.lint('There is no shared way to talk about the hurt, so the angry communard goes there, trying to get some justice. Money will not fix it.\n')
        self.assertNotIn('O6', out)

    def test_parsed_check_finds_nouns_no_list_has(self):
        """Joel, 2026-10-07 23:22: "abstract nouns are a real vast open-ended list in my mind". With spaCy and WordNet,
        O6 reads the grammar: the subject's kind of thing and the verb's kind of subject."""
        sys.path.insert(0, str(TOOLS))
        import tells_lint
        os.environ['TELLS_LINT_PARSE'] = '1'
        self.addCleanup(os.environ.__setitem__, 'TELLS_LINT_PARSE', '0')
        tells_lint._PARSER = None
        if not tells_lint.parser():
            self.skipTest('spaCy (en_core_web_sm) or NLTK WordNet is not installed')
        for s in ('Modern life trains us to perform competence while hiding whatever might complicate the performance.',
                  'The vaccination policy arrives two years later carrying documents.',
                  'Guilt may keep shouting at you.',
                  'Fear makes the decision before you\u2019ve even noticed it.',
                  "Once a kid is already living inside the disagreement, goodwill doesn't answer those questions.",
                  'There is no shared way to talk about the hurt, so the anger goes there, trying to get some justice.'):
            self.assertTrue(tells_lint.abstract_agents(s), s)
        for s in ('If anger comes up, you can stay with it for a minute.',
                  'The rule says nobody leaves before dawn.',
                  'Fear like that can destroy that gift, and it might not even prevent abuse.',
                  'The adults still have to pay attention to what goes on in a children’s territory.',
                  'There is no shared way to talk about the hurt, so the angry communard goes there, trying to get some justice.',
                  'Money will not fix it.'):
            self.assertEqual(tells_lint.abstract_agents(s), [], s)
        out = self.lint('Modern life trains us to perform competence. If anger comes up, you can stay with it for a minute.\n')
        self.assertIn('O6 a candidate, to judge', out)
        self.assertIn('Modern life trains us', out)
        self.assertNotIn('If anger comes up', out.split('O6 a candidate')[1])

    def test_negated_abstract_agent_is_flagged(self):
        """Joel, 2026-10-07 20:21, on "goodwill doesn't answer those questions": "that AI tell again ... abstracts doing things"."""
        self.assertIn('O6', self.lint("Once a kid is already living inside the disagreement, goodwill doesn't answer those questions.\n"))
        self.assertIn('O6', self.lint('Good intentions alone won’t settle any of that once the kids are in the middle of it.\n'))
        self.assertNotIn('O6', self.lint('The community has to share enough principles about raising kids to offer them coherence.\n'))


class LinterJoelRulings20261007(unittest.TestCase):
    """O14, O15 and O16 (Joel, 2026-10-07 01:43): Emulate's "and and and" list, unusual spellings, overcompleting."""
    def lint(self, text):
        with tempfile.TemporaryDirectory() as d:
            f = pathlib.Path(d) / 'draft.txt'
            f.write_text(text, encoding='utf-8')
            r = subprocess.run([sys.executable, str(TOOLS / 'tells_lint.py'), str(f)], capture_output=True, text=True)
            return r.stdout

    def test_emulates_and_list_fails_and_his_commas_pass(self):
        emu = ("It's not like calling something by a certain name dissolves the childhood panic and the comparison and the "
               "terror of abandonment and the desire to control another person.\n")
        out = self.lint(emu)
        self.assertIn('O14 owner ban', out)
        self.assertIn('verdict: FAIL', out)
        his = ("It's not like calling something by a certain name dissolves the childhood panic, the comparison, the terror "
               "of abandonment, or the desire to control another person.\n")
        self.assertNotIn('O14', self.lint(his))
        self.assertIn('O14 two repeated', self.lint('We had bread and butter and jam on the porch every morning that summer.\n'))

    def test_unusual_spellings_are_flagged_even_in_his_lines(self):
        try:
            import spellchecker  # noqa: F401
        except ImportError:
            self.skipTest('pyspellchecker is not installed')
        out = self.lint('It gets double dipped with the objection that psychedelics are also priveleged escape pods.\n')
        self.assertIn('O15', out)
        self.assertIn('priveleged', out)
        out = self.lint('They told them they are the re-incarnation of King David and Elvis, more or less.\n')
        self.assertIn('re-incarnation', out)
        out = self.lint('It gets double dipped with the objection that psychedelics are also privileged escape pods.\n')
        self.assertNotIn('O15', out)
        self.assertNotIn('O15', self.lint('If people are doing free love, but aren\'t doing the inner pl/ork, they end up with more fear.\n'))

    def test_a_closing_summary_is_flagged(self):
        para = ("Medical care is one of the toughest dependencies to work out. The community should think through how members "
                "are going to have access to care. What things might require outside dollars or some form of insurance? "
                "These are all questions that a community should consider in advance.\n")
        self.assertIn('O16', self.lint(para))
        his = para.replace(' These are all questions that a community should consider in advance.', '')
        self.assertNotIn('O16', self.lint(his))

    def test_may_be_x_and_still_y_is_flagged(self):
        """O17 (Joel, 2026-10-07 15:05): "Another AI tell is 'may be X and still Y'"."""
        for s in ("A scared or confused kid may get mixed up telling it and still need protection.\n",
                  "Fear like that can destroy that gift and still not prevent abuse.\n"):
            self.assertIn('O17', self.lint(s), s)
        for s in ("A scared or confused kid may get mixed up telling what happened, and that's to be expected.\n",
                  "Fear like that can destroy that gift, and it might not even prevent abuse.\n",
                  "We waited an hour and still nobody came, so we went home.\n"):
            self.assertNotIn('O17', self.lint(s), s)


class LinterOwnerScopes(unittest.TestCase):
    """Joel, 2026-10-07 15:44: the "gets to" ban is about subjects that aren't people; "Not x, but still y" is in the
    x-not-y family; "lists in general are overused by AI"."""
    def lint(self, text):
        with tempfile.TemporaryDirectory() as d:
            f = pathlib.Path(d) / 'draft.txt'
            f.write_text(text, encoding='utf-8')
            r = subprocess.run([sys.executable, str(TOOLS / 'tells_lint.py'), str(f)], capture_output=True, text=True)
            self.assertIn('verdict:', r.stdout, r.stderr[-600:])
            return r.stdout

    def test_gets_to_with_a_thing_fails(self):
        for t in ("The urge doesn't get to decide what you do tonight.\n", "That part of you doesn't get a vote here.\n",
                  "The weather doesn't get to decide whether we go.\n"):
            self.assertIn('O1 owner ban', self.lint(t), t)

    def test_gets_to_with_a_person_is_not_flagged(self):
        for t in ("Your dad doesn't get to decide where you live.\n", "Nobody gets to decide that for you.\n",
                  "A real parent doesn't get to do that, which is one reason nobody manages to be a perfect one.\n"):
            self.assertNotRegex(self.lint(t), r'\bO1\b', t)  # \b: main's O15 note ("O15 (spelling) skipped") contains "O1"

    def test_gets_to_with_an_unclear_subject_is_a_review(self):
        out = self.lint("Your little one gets to decide how close to come.\n")
        self.assertIn('O1 "gets to" with an unclear subject', out)
        self.assertNotIn('O1 owner ban', out)

    def test_not_x_but_still_y(self):
        self.assertIn('O18', self.lint("It isn't proof, but it still counts as a good evening.\n"))
        self.assertIn('O18', self.lint("It isn't proof. It still counts as a good evening.\n"))
        self.assertNotIn('O18', self.lint("She still lives in the house by the river with her two dogs.\n"))

    def test_may_x_and_still_y(self):
        """Joel, 2026-10-07 16:46: "it makes no sense AND it sounds ai with "may have X and still Y""."""
        self.assertIn('O17', self.lint("Somebody may really have crossed a boundary and still have hit something old in you.\n"))
        self.assertNotIn('O17', self.lint("Somebody may really have crossed a boundary. Notice what it hit in you.\n"))

    def test_a_list_is_a_review(self):
        out = self.lint("A few people you might call when it gets heavy:\n\n- a friend who listens\n- your sister\n")
        self.assertIn('O19 a list', out)
        self.assertEqual(out.count('O19 a list'), 1)
        self.assertNotIn('O19', self.lint("You could call a friend who listens, or your sister.\n"))

    def test_o12_quietly_o20_o21_joel_20261010(self):
        """Joel, 2026-10-10 12:22 UTC, on community section 10: "quietly" is an AI-frequency word (O12), "I don't want ..."
        opening a stance is in the tells list (O20), and "one super-commune with a nicer logo" is "an AI-tell quip" (O21)."""
        self.assertIn('O12', self.lint("Cooperation also shouldn't quietly turn into assimilation, and that matters.\n"))
        self.assertIn('O20', self.lint("I don't want one big federation for every community in the region.\n"))
        self.assertIn('O20', self.lint("It has to be solved. I want communities that can help one another.\n"))
        self.assertNotIn('O20', self.lint("The members want communities that can help one another.\n"))
        self.assertIn('O21', self.lint("Nobody needs one super-commune with a nicer logo in the end.\n"))
        self.assertIn('O21', self.lint("That would just be another state with extra steps, in the end.\n"))
        self.assertNotIn('O21', self.lint("The new school opened with a nicer playground than the old one.\n"))


class LinterListsOfThree(unittest.TestCase):
    """E125 (Joel, 2026-10-03): "P! failed b ecause it has 2 lists of 3"; "lists of 3 in general are an ai pattern"."""
    FAILED_P1 = ("You might go looking for your little one and get mad instead, or realize you've been staring at the rug. "
                 "I count that as pl/ork too, even if it feels like it's in the way. Before you decide where it's coming from, "
                 "ask it what it's trying to stop, or what it wants, or if it just has something to say. It could be your little "
                 "one, mad that you took so long to come back, or a part of you that's trying to protect you, or the parent you "
                 "inherited, or something from earlier today, or a bit of each.\n")
    JOEL_P1 = ("You might go looking for your little one and get mad instead, or realize you've been staring at the rug. "
               "I count that as pl/ork too, even if it feels like it's in the way. Before you decide where it's coming from, "
               "ask it what it's trying to stop, or what it wants. Maybe it just has something to say. It could be your little "
               "one, mad that you took so long to come back, or a part of you that's trying to protect you. Maybe it's that "
               "parent you inherited, or something from earlier today, or a bit of each.\n")

    def lint(self, text, installed=None):
        with tempfile.TemporaryDirectory() as d:
            f = pathlib.Path(d) / 'draft.txt'
            f.write_text(text, encoding='utf-8')
            cmd = [sys.executable, str(TOOLS / 'tells_lint.py'), str(f)]
            if installed is not None:
                g = pathlib.Path(d) / 'article.md'
                g.write_text(installed, encoding='utf-8')
                cmd += ['--installed', str(g)]
            r = subprocess.run(cmd, capture_output=True, text=True)
            # a crash prints nothing, which would pass every assertNotIn below (2026-10-03)
            self.assertIn('verdict:', r.stdout, r.stderr[-600:])
            return r.returncode, r.stdout

    def test_two_lists_in_one_paragraph_fail(self):
        rc, out = self.lint(self.FAILED_P1)
        self.assertIn('E125 two lists', out)
        self.assertEqual(rc, 2)

    def test_his_fix_leaves_one_list_to_review(self):
        rc, out = self.lint(self.JOEL_P1)
        self.assertIn('E125 list of three', out)
        self.assertNotIn('E125 two lists', out)

    def test_pairs_and_quotes_are_not_lists(self):
        for s in ('If words are there, speak or write them.\n',
                  'Or you tell a therapist, \u201cNo, that\'s not right for me,\u201d and they call it resistance.\n',
                  'If the room itself triggers your spidey sense, leave, or lock the door and get help.\n',
                  'Or something does come, a voice or a hunch, and you listen without putting it in charge.\n'):
            self.assertNotIn('E125', self.lint(s)[1], s)

    def test_installed_text_gets_no_flags(self):
        rc, out = self.lint(self.FAILED_P1, installed='# Section\n\n' + self.FAILED_P1)
        self.assertNotIn('E125', out)


class InContextPageShowsContext(unittest.TestCase):
    """Joel, 2026-10-07 15:44: "whenever you give me the in-context side by side, you need to actually give me the context
    in that page so i can understand what's coming from what"."""
    ARTICLE = ('# Title\n\n## Section\n\nThe paragraph before, which ends the thought.\n\n'
               'An installed paragraph in the middle.\n\n## Next Section\n\nThe next section starts here.\n')

    def render(self, rows):
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / 'a.md').write_text(self.ARTICLE, encoding='utf-8')
            (d / 's.md').write_text('Source paragraph.\n', encoding='utf-8')
            (d / 'm.json').write_text(json.dumps({'title': 'T', 'blocks': [{'headings': ['## Section'], 'rows': rows}]}), encoding='utf-8')
            r = subprocess.run([sys.executable, str(TOOLS / 'render_in_context.py'), str(d / 'm.json'), str(d / 'o.html'),
                                '--article', str(d / 'a.md'), '--source', str(d / 's.md'), '--against-source'],
                               capture_output=True, text=True)
            return r.returncode, (d / 'o.html').read_text(encoding='utf-8') if (d / 'o.html').exists() else r.stderr

    def test_a_candidate_without_a_place_stops_the_page(self):
        rc, out = self.render([{'label': 'B2', 'text': 'Still, a new paragraph.', 'source': []}])
        self.assertNotEqual(rc, 0)
        self.assertIn('needs a place', out)

    def test_his_words_from_chat_show_beside_the_row(self):
        """2026-10-12: an answer he gave in chat, fitted into the article, is shown in the left card (Joel, 2026-10-11
        18:35: "you can't just take what i say to you and publish it. it has to make sense in context")."""
        rc, out = self.render([{'label': 'P2 · your answer, my wording', 'article': 'An installed paragraph',
                                'source': [], 'beside': {'label': 'Your words, 23:12 UTC', 'text': 'well this can be tricky'}}])
        self.assertEqual(rc, 0, out)
        left = out.split('<div class="grid"><div class="card">')[1].split('</div>')[0]
        self.assertIn('Your words, 23:12 UTC', left)
        self.assertIn('well this can be tricky', left)
        self.assertNotIn('No ', left)
        rc, out = self.render([{'label': 'P2', 'article': 'An installed paragraph', 'source': ['Source paragraph.'],
                                'beside': {'label': 'Your words', 'text': 'his answer'}}])
        self.assertEqual(rc, 0, out)
        left = out.split('<div class="grid"><div class="card">')[1].split('</div>')[0]
        self.assertLess(left.index('Source paragraph.'), left.index('his answer'))

    def test_the_paragraphs_around_a_chain_of_candidates_are_shown(self):
        rc, out = self.render([{'label': 'B1', 'text': 'First new paragraph.', 'source': [], 'after': 'An installed paragraph'},
                               {'label': 'B2', 'text': 'Still, a second new one.', 'source': [], 'after_row': 'B1'}])
        self.assertEqual(rc, 0, out)
        self.assertIn('Right before it in the article', out)
        self.assertIn('An installed paragraph in the middle.', out)
        self.assertIn('Right after it in the article', out)
        self.assertIn('## Next Section', out)
        self.assertEqual(out.count('Right before it in the article'), 1)   # B2 follows B1 directly: no context between them
        self.assertIn('Where it goes: Title › Section', out)


class InContextPageShowsRepeats(unittest.TestCase):
    """Joel, 2026-10-07 23:18: "some of that looked like it was duplicating other stuff from before ... did you make the
    dedup pass before trying to humanize?" A dedup note names where the article already says it, with its words."""
    ARTICLE = InContextPageShowsContext.ARTICLE
    render = InContextPageShowsContext.render

    def row(self, **repeat):
        return {'label': 'B1', 'text': 'A new paragraph that ends the thought again.', 'source': [],
                'after': 'An installed paragraph', 'repeats': [repeat]}

    def test_a_repeat_is_marked_and_says_where(self):
        rc, out = self.render([self.row(span='ends the thought again', says='ends the thought', how='same point',
                                        **{'in': 'The paragraph before'})])
        self.assertEqual(rc, 0, out)
        self.assertIn('<span class="dup">ends the thought again</span>', out)
        self.assertIn('Already in the article, in Title › Section: “ends the thought” (same point)', out)

    def test_a_quote_that_isnt_there_stops_the_page(self):
        rc, out = self.render([self.row(span='ends the thought again', says='starts the thought', **{'in': 'The paragraph before'})])
        self.assertNotEqual(rc, 0)
        self.assertIn('not in that paragraph', out)

    def test_a_span_that_isnt_in_the_row_stops_the_page(self):
        rc, out = self.render([self.row(span='begins the thought', says='ends the thought', **{'in': 'The paragraph before'})])
        self.assertNotEqual(rc, 0)
        self.assertIn('not in the row', out)

    def test_a_repeat_between_two_drafts(self):
        rc, out = self.render([{'label': 'B1', 'text': 'First new paragraph about the thought.', 'source': [], 'after': 'An installed paragraph'},
                               {'label': 'B2', 'text': 'Again, about the thought.', 'source': [], 'after_row': 'B1',
                                'repeats': [{'span': 'about the thought', 'in_row': 'B1', 'says': 'about the thought'}]}])
        self.assertEqual(rc, 0, out)
        self.assertIn('Also in B1, on this page: “about the thought”', out)


class StanceCheckPrompt(unittest.TestCase):
    def test_prompt_holds_both_texts_and_the_job(self):
        essay = '# Essay\n\n[image 1](https://example.com/x.png)\n\nI want people to arrive largely healed.\n'
        rewrite = '<!-- CANDIDATE: note -->\n# Section\n\nPeople do not come in pre-healed.\n'
        p = stance_check_prompt.build(essay, rewrite, scope='section 3', topic='communities', report='/tmp/report.md')
        self.assertIn('THE WHOLE PUBLISHED ESSAY:', p)
        self.assertIn('I want people to arrive largely healed.', p)
        self.assertIn('THE REWRITE (section 3):', p)
        self.assertIn('People do not come in pre-healed.', p)
        self.assertIn('[an image]', p)
        self.assertNotIn('CANDIDATE', p)
        self.assertNotIn('example.com', p)
        self.assertIn('/tmp/report.md', p)
        self.assertLess(p.index('THE WHOLE PUBLISHED ESSAY:'), p.index('THE REWRITE (section 3):'))
        self.assertIn('vaguer general one', p)
        # Joel, 2026-10-11 23:12, on "can't be voted away" beside "even by a majority vote": "fix the reviewers"
        self.assertIn("Read the way people talk.", p)
        # Joel, 2026-10-15 13:10, on section 13's visitor rule flagged against his land before critical mass: "it's quite
        # clear already without needing to add anything"
        self.assertIn("Read each rule within the situation its section is about", p)

    def test_images_that_carry_content_are_described(self):
        essay = '# Essay\n\n[image 7](https://example.com/parts.svg)\n\nThese four parts leak.\n\n[image 8](https://example.com/x.png)\n'
        p = stance_check_prompt.build(essay, 'Rewrite.', images={'image 7': 'a diagram naming the four parts'})
        self.assertIn('[an image: a diagram naming the four parts]', p)
        self.assertIn('[an image]', p)
        self.assertNotIn('example.com', p)

    def test_without_a_report_path_the_agent_returns_it(self):
        p = stance_check_prompt.build('Essay.', 'Rewrite.')
        self.assertIn('Return the report as your final message.', p)
        self.assertNotIn('Write call', p)

    def test_published_contradictions_and_stated_positions(self):
        """Joel, 2026-10-07 15:05: the published text contradicted itself and no reviewer said so; his newer positions win."""
        p = stance_check_prompt.build('Essay.', 'Rewrite.', positions='2026-10-07: the home community controls its outside interactions.')
        self.assertIn('Contradictions in the published text', p)
        self.assertIn("THE AUTHOR'S STATED POSITIONS (newer than the essay):", p)
        self.assertLess(p.index('THE REWRITE ('), p.index("THE AUTHOR'S STATED POSITIONS (newer"))
        q = stance_check_prompt.build('Essay.', 'Rewrite.')
        self.assertIn('Contradictions in the published text', q)
        self.assertNotIn("STATED POSITIONS", q)

    def test_the_authors_own_paragraphs_are_his_position(self):
        """Joel, 2026-10-07 20:21, on the check calling his P10 narrower: "you're wrong, it says more than the published version"."""
        mine = 'If the father is unknown, the whole community can do the fathering.'
        p = stance_check_prompt.build('Essay.', 'Rewrite. ' + mine, owner=mine)
        self.assertIn("THE AUTHOR'S OWN REWRITES", p)
        self.assertIn('Questions on the author', p)
        self.assertIn(mine, p[p.index("THE AUTHOR'S OWN REWRITES (his words"):])
        self.assertNotIn("OWN REWRITES", stance_check_prompt.build('Essay.', 'Rewrite.'))


class AbstractAgentsJudgment(unittest.TestCase):
    """Joel, 2026-10-07 23:50: "you don't understand just intuitively which abstractions are normally used and which are
    not? ... isn't that what LLMs are great at?" The linter collects candidates; a fresh agent judges them."""
    def test_prompt_carries_his_ratings_the_candidates_and_his_lines(self):
        text = ('So the anger goes there, trying to get some justice.\n\n'
                'We cooked dinner together on the porch every night that summer.\n\n'
                'Your shame wants you to hide.\n')
        p = abstract_agents_prompt.build(text, owner=['Your shame wants you to hide.'], report='/tmp/r.md')
        self.assertIn("Grief doesn't keep a schedule", p)
        self.assertIn('Modern life trains us to perform competence', p)
        self.assertIn('so common it\'s almost cliche', p)
        cands = p[p.index('CANDIDATES:'):p.index('THE TEXT:')]
        self.assertIn('So the anger goes there, trying to get some justice.', cands)
        self.assertNotIn('We cooked dinner', cands)
        self.assertIn("[JOEL'S] Your shame wants you to hide.", cands)
        self.assertIn('MISSED:', p)
        self.assertIn('/tmp/r.md', p)
        self.assertLess(p.index('CANDIDATES:'), p.index('THE TEXT:'))


class RenderInContextHeadings(unittest.TestCase):
    """Joel, 2026-10-07 15:05: "P7 is in the wrong section. You moved it ... why?" The article was right; the page's map
    had grouped P7 with the rows of the heading before it."""
    ART = '# Title\n\nFirst paragraph here.\n\n## Second Heading\n\nSeventh paragraph here.\n\nEighth paragraph here.\n'

    def render(self, blocks):
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / 'a.md').write_text(self.ART, encoding='utf-8')
            (d / 'm.json').write_text(json.dumps({'title': 'T', 'blocks': blocks}), encoding='utf-8')
            r = subprocess.run([sys.executable, str(TOOLS / 'render_in_context.py'), str(d / 'm.json'), str(d / 'o.html'),
                                '--article', str(d / 'a.md'), '--source', str(d / 'a.md'), '--against-source'],
                               capture_output=True, text=True)
            return r.returncode, r.stdout + r.stderr, (d / 'o.html').exists()

    @staticmethod
    def row(label, start):
        return {'label': label, 'article': start, 'source': [start]}

    def test_a_row_under_the_wrong_heading_stops_the_page(self):
        rc, out, made = self.render([{'headings': ['# Title'], 'rows': [self.row('P1', 'First'), self.row('P7', 'Seventh')]},
                                     {'headings': ['## Second Heading'], 'rows': [self.row('P8', 'Eighth')]}])
        self.assertNotEqual(rc, 0)
        self.assertIn('P7 is under "second heading" in the article but under "title" on the page', out)
        self.assertFalse(made)

    def test_rows_out_of_order_stop_the_page(self):
        rc, out, made = self.render([{'headings': ['# Title'], 'rows': [self.row('P1', 'First')]},
                                     {'headings': ['## Second Heading'], 'rows': [self.row('P8', 'Eighth'), self.row('P7', 'Seventh')]}])
        self.assertIn('P7 comes before the row above it in the article', out)
        self.assertFalse(made)

    def test_a_dropped_paragraph_gets_its_own_row(self):
        """Joel, 2026-10-07 20:21: "idk where p26 is now, are you talking about something you didn't show me?"."""
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / 'a.md').write_text(self.ART, encoding='utf-8')
            (d / 's.md').write_text(self.ART + '\nNinth paragraph, cut since.\n', encoding='utf-8')
            m = {'title': 'T', 'blocks': [{'headings': ['# Title'], 'rows': [self.row('P1', 'First')]},
                                         {'headings': ['## Second Heading'], 'rows': [self.row('P7', 'Seventh'), self.row('P8', 'Eighth'),
                                                                                     {'label': 'P9 · cut', 'dropped': 'Ninth'}]}]}
            (d / 'm.json').write_text(json.dumps(m), encoding='utf-8')
            r = subprocess.run([sys.executable, str(TOOLS / 'render_in_context.py'), str(d / 'm.json'), str(d / 'o.html'),
                                '--article', str(d / 'a.md'), '--source', str(d / 's.md'), '--against-source'],
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            page = (d / 'o.html').read_text(encoding='utf-8')
        self.assertIn('<del>Ninth paragraph, cut since.</del>', page)
        self.assertIn('not in the article', page)

    def test_rows_under_their_own_headings_render(self):
        rc, out, made = self.render([{'headings': ['# Title'], 'rows': [self.row('P1', 'First')]},
                                     {'headings': ['## Second Heading'], 'rows': [self.row('P7', 'Seventh'), self.row('P8', 'Eighth')]}])
        self.assertEqual(rc, 0, out)
        self.assertTrue(made)

    def test_a_label_number_that_disagrees_with_the_page_is_dropped(self):
        """Joel, 2026-10-13: "not sure why you numbered it p1-p4? it's just p1 right?". A map from before para_numbers
        numbered rows across the section, and the page showed both numbers ("P1 · P4 · the principle")."""
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / 'a.md').write_text(self.ART, encoding='utf-8')
            m = {'title': 'T', 'blocks': [{'headings': ['# Title'], 'rows': [self.row('P1 · first', 'First')]},
                                         {'headings': ['## Second Heading'], 'rows': [self.row('P7 · seventh', 'Seventh'),
                                                                                     self.row('eighth', 'Eighth')]}]}
            (d / 'm.json').write_text(json.dumps(m), encoding='utf-8')
            r = subprocess.run([sys.executable, str(TOOLS / 'render_in_context.py'), str(d / 'm.json'), str(d / 'o.html'),
                                '--article', str(d / 'a.md'), '--source', str(d / 'a.md'), '--against-source'],
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            page = (d / 'o.html').read_text(encoding='utf-8')
        self.assertIn('P1 · first', page)
        self.assertIn('P1 · seventh', page)
        self.assertNotIn('P7', page)
        self.assertIn('P2 · eighth', page)
        self.assertIn('the label number was dropped', r.stderr)
        self.assertIn('user-select:none', page)   # struck words don't come along in a copy (2026-10-13)


class PreservationKeys(unittest.TestCase):
    """Joel, 2026-10-12 05:33, on community section 12: "then you broke p7 by reducing it to "but it's not infinite" ?
    what?" Two or three traces had called each break EQUIVALENT. The key words of each preservation unit are now checked
    mechanically, per paragraph, before any trace."""
    UNITS = {'section': 'test', 'units': [
        {'id': 'U8', 'what': 'not infinitely absorbent', 'keys': [['the community'], ['infinitely absorbent']]},
        {'id': 'U7', 'what': 'good enough for community', 'keys': [['good enough'], ['for community']]},
        {'id': 'U26', 'what': 'available resource, early members', 'keys': [['available resource', 'free resource'], ['acute need']]},
        {'id': 'U40', 'what': 'a claim across two paragraphs', 'keys': [['first half'], ['second half']], 'span': 2}]}
    GOOD = ('So the question isn’t whether a person is “good enough” for community.\n\n'
            'That does not make the community *infinitely absorbent*.\n\n'
            'Members need more [available resource](https://www.rc.org/) than acute need.\n\n'
            'The first half is here.\n\nThe second half is here.')

    def test_his_breaks_are_caught(self):
        self.assertEqual(preservation_keys.check(self.UNITS, self.GOOD), [])
        bad = self.GOOD.replace('That does not make the community *infinitely absorbent*.', 'But it’s not infinite.')
        bad = bad.replace('“good enough” for community.', '“good enough.”')
        missing = {m['id']: m['missing'] for m in preservation_keys.check(self.UNITS, bad)}
        self.assertEqual(sorted(missing), ['U7', 'U8'])
        self.assertEqual(missing['U7'], [['for community']])

    def test_a_key_in_another_paragraph_doesnt_count(self):
        # A whole-draft match passed U26 on community section 12: "free resource" is all through the section.
        text = self.GOOD.replace('more [available resource](https://www.rc.org/) than acute need',
                                 'more resource than acute need') + '\n\nGive what free resource you have.'
        self.assertEqual([m['id'] for m in preservation_keys.check(self.UNITS, text)], ['U26'])

    def test_a_spanning_unit_and_the_command(self):
        split = self.GOOD.replace('The first half is here.\n\nThe second half is here.',
                                  'The first half is here.\n\nSomething else.\n\nThe second half is here.')
        self.assertEqual([m['id'] for m in preservation_keys.check(self.UNITS, split)], ['U40'])
        with tempfile.TemporaryDirectory() as d:
            k, f = pathlib.Path(d) / 'keys.json', pathlib.Path(d) / 'draft.md'
            k.write_text(json.dumps(self.UNITS), encoding='utf-8')
            f.write_text(self.GOOD, encoding='utf-8')
            ok = subprocess.run([sys.executable, str(TOOLS / 'preservation_keys.py'), str(k), str(f)], capture_output=True, text=True)
            f.write_text(split, encoding='utf-8')
            bad = subprocess.run([sys.executable, str(TOOLS / 'preservation_keys.py'), str(k), str(f)], capture_output=True, text=True)
        self.assertEqual((ok.returncode, bad.returncode), (0, 1), ok.stderr + bad.stderr)
        self.assertIn('verdict: PASS', ok.stdout)
        self.assertIn('MISSING U40', bad.stdout)


class PreservationKeysSectionTerms(unittest.TestCase):
    """Trace r6, 2026-10-12: "tolerate the disruption" for the published "absorb disruption", in a section called "The Math
    of Absorption"; the unit had never listed "absorb", so the key-word check passed it."""
    def test_a_unit_without_its_section_term_fails_the_key_file(self):
        doc = {'section_terms': ['absorb'], 'units': [
            {'id': 'U23', 'what': 'small communities can absorb disruption least', 'keys': [['paradox'], ['disruption']]}]}
        self.assertEqual([g['id'] for g in preservation_keys.incomplete_units(doc)], ['U23'])
        doc['units'][0]['keys'].append(['absorb'])
        self.assertEqual(preservation_keys.incomplete_units(doc), [])


class MeaningSweepAuthorMarks(unittest.TestCase):
    """Joel, 2026-10-12 17:23: "rather than just ignoring rules that fail my prose, we should fix the rules so they don't fail
    my prose". His sentences are marked so the sweep's reader leaves them alone; mine stay open to it."""
    HIS = 'Make sure kids understand what they say will be taken seriously if they are known to be honest.'

    def test_his_sentences_are_marked_and_mine_are_not(self):
        owners = [meaning_sweep.norm(self.HIS), meaning_sweep.norm('No, taking away the idea of a boss does not make everyone less passive,')]
        text = ('The community has to share enough principles about raising kids. ' + self.HIS +
                ' And that’s just two people.\n\nNo, taking away the idea of a boss does not make everyone less passive, selfish, or helpless.')
        out = meaning_sweep.mark_author(text, owners)
        self.assertIn(meaning_sweep.MARK_OPEN + self.HIS + meaning_sweep.MARK_CLOSE, out)
        self.assertTrue(out.startswith('The community has to share'))
        self.assertIn(meaning_sweep.MARK_OPEN + 'No, taking away the idea', out)

    def test_wording_he_approved_stays_mine(self):
        """2026-10-14: two of the three sweep flags he sent back (F4, F6) were in my wording he had approved ("agree fix
        it"), which the ledger records; an entry marked "words": "proposed" gives no author marks."""
        with tempfile.TemporaryDirectory() as d:
            led = pathlib.Path(d) / 'led.json'
            led.write_text(json.dumps({'entries': [
                {'id': 'a', 'status': 'applied', 'must_contain': [self.HIS]},
                {'id': 'b', 'status': 'applied', 'words': 'proposed',
                 'must_contain': ['or stop trying to act helpless, which I proposed and he approved']}]}), encoding='utf-8')
            owners = meaning_sweep.owner_strings(str(led), [])
        self.assertIn(meaning_sweep.norm(self.HIS), owners)
        self.assertFalse(any('stop trying to act helpless' in o for o in owners))

    def test_the_prompt_and_input(self):
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / 'pub.md').write_text('# One\n\nKids should know adults will listen seriously.\n', encoding='utf-8')
            (d / 'art.md').write_text('# One\n\n<!-- a note -->\n' + self.HIS + '\n', encoding='utf-8')
            (d / 'his.txt').write_text(self.HIS + '\n', encoding='utf-8')
            meaning_sweep.main(['--article', str(d / 'art.md'), '--source', str(d / 'pub.md'), '--section', '1', '--input', str(d / 'in.md'),
                                '--report', str(d / 'r.md'), '--out', str(d / 'p.txt'), '--owner-text', str(d / 'his.txt')])
            inp = (d / 'in.md').read_text(encoding='utf-8')
            prompt = (d / 'p.txt').read_text(encoding='utf-8')
        self.assertIn(meaning_sweep.MARK_OPEN + self.HIS + meaning_sweep.MARK_CLOSE, inp)
        self.assertNotIn('a note', inp)
        self.assertIn('Report nothing inside those marks', prompt)
        self.assertIn('An "it" that is clear in its place is fine', prompt)


class LinterCapacity(unittest.TestCase):
    """O40 (Joel, 2026-10-12 17:23): "capacity is an AI tell"; "capacity is ok when explained as free resource"."""
    def lint(self, text):
        with tempfile.TemporaryDirectory() as d:
            f = pathlib.Path(d) / 'draft.txt'
            f.write_text(text + '\n', encoding='utf-8')
            return subprocess.run([sys.executable, str(TOOLS / 'tells_lint.py'), str(f)], capture_output=True, text=True).stdout

    def test_capacity_alone_is_flagged_and_free_resource_capacity_is_not(self):
        self.assertIn('O40', self.lint('Look at whether the group has enough capacity to support them without becoming a full-time caretaker operation.'))
        self.assertNotIn('O40', self.lint('Look at whether the group has enough free resource/capacity to support them without becoming a full-time caretaker operation.'))


if __name__ == '__main__':
    unittest.main()


class DedupPrompts(unittest.TestCase):
    """E151 (2026-10-08): new material is checked against the whole article, not just its neighbors (Joel, 2026-10-07 01:09:
    "just make sure it's not duplicating stuff"; 23:18: "did you make the dedup pass before trying to humanize?")."""
    ARTICLE = ('# Title — humanized article so far\n\n# Part One\n\nThe first paragraph says to wait until you are calm.\n\n'
               "Here's a map:\n\n<!-- Native Substack embed from source, unchanged: \"The Map\" (https://example.com/map). -->\n\n"
               '## Later\n\n<!-- a working note -->\n\nA later paragraph.\n\nhttps://substack.com/profile/1-x/note/c-2\n')

    def run_cmd(self, *args, target=None):
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / 'a.md').write_text(self.ARTICLE, encoding='utf-8')
            (d / 't_one.json').write_text(json.dumps({
                'before': 'The first paragraph says to wait until you are calm.',
                'guide_passage': 'The 2026-10-04 r4 guide (the passage this carries):\nWait until you are calm. Keep a friend near.'}), encoding='utf-8')
            r = subprocess.run([sys.executable, str(TOOLS / 'reviewer' / 'reviewer.py'), '--article', str(d / 'a.md')] +
                               [x.replace('T1', str(d / 't_one.json')).replace('OUT', str(d / 'o.txt')) for x in args],
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            return (d / 'o.txt').read_text(encoding='utf-8')

    def test_the_whole_article_is_numbered_with_its_embeds(self):
        p = self.run_cmd('repeats', 'OUT', '--focus', '"# Part One"')
        self.assertIn('[B0] # Part One', p)
        self.assertIn('[Embedded post by the author: "The Map"]', p)
        self.assertIn('[Embedded Substack note by the author, shown as a preview card]', p)
        self.assertNotIn('working note', p)
        self.assertNotIn('humanized article so far', p)
        self.assertIn('"# Part One" was put together from several sources', p)
        self.assertIn('Return your findings as your final message', p)

    def test_only_keeps_the_scope_sentence_whole(self):
        """2026-10-14: a "report only" line written inside --focus garbled the scope sentence; --only says it instead."""
        p = self.run_cmd('repeats', 'OUT', '--focus', '"# Part One"', '--only')
        self.assertIn('"# Part One" was put together from several sources', p)
        self.assertIn('Report only repeats and contradictions that involve at least one block there', p)
        self.assertNotIn('Then check the rest of the article against itself', p)

    def test_each_group_says_where_it_goes_and_carries_its_passage(self):
        p = self.run_cmd('dedup', 'OUT', 'T1', '--report', '/tmp/r.md')
        self.assertIn('GROUP 1 (t_one): would go right after [B1]', p)
        self.assertIn('Wait until you are calm. Keep a friend near.', p)
        self.assertNotIn('(the passage this carries)', p)
        self.assertIn('(No drafts yet', p)
        self.assertIn('/tmp/r.md', p)
        self.assertLess(p.index('THE ARTICLE'), p.index('GROUP 1'))


class PangramLinksInMessages(unittest.TestCase):
    """pangram_links_check.py (2026-10-15). Joel, 09:33 UTC: "for future reference, give me the pangram check links when
    you tell me to check something on pangram" (the questions page had told him a pair read AI, with no link)."""

    def test_an_ai_result_needs_its_link_and_a_pass_does_not(self):
        import pangram_links_check as plc
        msg = ('Your paragraph reads AI beside the reparenting paragraph (278g, a control).\n\n'
               '- The pair read AI: [check](https://www.pangram.com/history/4bb0032c-a069-447c-8add-1f975a1c1125).\n'
               '- The section reads 100% Human (284g).\n'
               '- "Mostly Human Written": a window on P4\'s questions (281g).\n'
               '- I used two of your three terms, since a list of three reads AI.\n')   # a rule, not a result
        found = plc.missing(msg)
        self.assertEqual(len(found), 2)
        self.assertTrue(found[0].startswith('Your paragraph reads AI'))
        self.assertIn('Mostly Human', found[1])


class SectionColdReadPrompt(unittest.TestCase):
    """reviewer.py sense-section (2026-10-11). Joel, 18:35 UTC: ""as I'm describing may happen in my case" is obvious so you
    should debug why the cold reader can't understand it." The community lane's section reads were written by hand, with a
    summary in place of the article, and asked for anything that "stops you"; the builder gives the whole article before the
    section and the shared rules, with the best-reading rule from the debugging."""
    ARTICLE = ('# Title — humanized article so far\n\n[image 1](https://example.com/a.jpg)\n\n# First Part\n\n'
               'My father made a [film](https://example.com/film) in 1988.\n\n[caption] The banner my mom painted.\n\n'
               '[Share](%%share_url%%)\n\n<!-- a working note -->\n\n# Second Part\n\nThe second part opens here.\n\n'
               '## A Subsection\n\n[image 2](https://example.com/b.jpg)\n\n[caption] A cult, maybe.\n\n'
               'The subsection goes on.\n\n# Third Part\n\nThe third part.\n')

    def run_cmd(self, *args, ok=True):
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / 'a.md').write_text(self.ARTICLE, encoding='utf-8')
            (d / 'draft.md').write_text('# Second Part\n\nA new opening paragraph.\n\nAnd a second one.\n', encoding='utf-8')
            r = subprocess.run([sys.executable, str(TOOLS / 'reviewer' / 'reviewer.py'), '--article', str(d / 'a.md'), 'sense-section',
                                str(d / 'o.txt')] + [x.replace('DRAFT', str(d / 'draft.md')) for x in args], capture_output=True, text=True)
            if not ok:
                self.assertNotEqual(r.returncode, 0)
                return r.stderr + r.stdout
            self.assertEqual(r.returncode, 0, r.stderr)
            return (d / 'o.txt').read_text(encoding='utf-8')

    def test_the_reader_gets_the_article_before_and_the_section_numbered(self):
        p = self.run_cmd('--section', 'Second Part', '--report', '/tmp/r.md')
        earlier = p[p.index('THE ARTICLE BEFORE'):p.index('THE SECTION:')]
        # a link reads as its words, marked as a link, with where it goes (2026-10-14: "reviewer doesn't know about links")
        self.assertIn('My father made a film [a link to example.com/film] in 1988.', earlier)
        self.assertIn('[an image]', earlier)
        self.assertIn('[caption] The banner my mom painted.', earlier)
        for gone in ('Share', 'working note', 'humanized article so far', 'https://'):
            self.assertNotIn(gone, earlier)
        section = p[p.index('THE SECTION:'):]
        self.assertIn('# Second Part\n\n[P1] The second part opens here.', section)
        self.assertIn('## A Subsection\n\n[an image]\n\n[caption] A cult, maybe.\n\n[P2] The subsection goes on.', section)
        self.assertNotIn('[P3]', section)
        self.assertIn('After it, the next section starts: "# Third Part".', section)
        self.assertNotIn('The third part.', section)
        self.assertIn('/tmp/r.md', p)

    def test_a_linked_phrase_is_marked_and_the_reader_is_told_what_that_means(self):
        # Joel, 2026-10-14 21:19 UTC, on two cold reads asking "which corpus?" of a phrase that is a link to it: "the
        # research corpus is linked in the article... should be linked right there. reviewer doesn't know about links or
        # something?" The reader had been given the link's words only.
        sys.path.insert(0, str(TOOLS / 'reviewer'))
        import reviewer
        view = reviewer.reader_view('I looked through [the research corpus](https://www.example.org/blog/research/?s=1#top) for '
                                    'a case, and [https://example.org](https://example.org) has the rest.')
        self.assertEqual(view, ['I looked through the research corpus [a link to example.org/blog/research] for a case, and '
                                'https://example.org has the rest.'])
        p = self.run_cmd('--section', 'Second Part')
        self.assertIn('Words followed by "[a link to ...]" are a link on the page', p)
        self.assertIn('the research corpus is linked in the article', p)

    def test_the_shared_rules_are_in_it(self):
        p = self.run_cmd('--section', 'Second Part')
        self.assertIn('put your best reading of it after the quote', p)
        self.assertIn('This is only about following the words.', p)
        self.assertIn('"that call" is the one that\'s ringing', p)
        # 2026-10-12, Joel: "you can't do that to me!" doesn't mean "you can not" ... fix the reviewers"; "it was said"
        self.assertIn('Read the way people talk.', p)
        self.assertIn('only where a reasonable reader would see one', p)
        self.assertIn('look for the reason in its other sentences', p)
        self.assertIn("leave it out entirely, and don't report it as garbled", p)
        self.assertIn("Don't suggest rewrites", p)
        self.assertIn('Return the lines as your final message', p)

    def test_a_draft_replaces_the_section(self):
        p = self.run_cmd('--section', 'Second Part', '--draft', 'DRAFT')
        section = p[p.index('THE SECTION:'):]
        self.assertIn('[P1] A new opening paragraph.', section)
        self.assertIn('[P2] And a second one.', section)
        self.assertNotIn('The second part opens here.', p)
        self.assertIn('"# Third Part"', section)

    def test_a_heading_that_isnt_there_stops_it(self):
        self.assertIn('no heading "Fourth Part"', self.run_cmd('--section', 'Fourth Part', ok=False))


class InContextPageShowsWhatADraftCarries(unittest.TestCase):
    """Joel, 2026-10-08 02:23: "i also don't understand how you got depth draft 1 from the r4 guide? doesn't look like a good
    rewrite of that one sentence". The source cell showed one sentence of the guide paragraph; the draft carried all of it."""
    ARTICLE = InContextPageShowsContext.ARTICLE

    def render(self, rows, source='First guide sentence. Second guide sentence.\n'):
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / 'a.md').write_text(self.ARTICLE, encoding='utf-8')
            (d / 's.md').write_text(source, encoding='utf-8')
            (d / 'm.json').write_text(json.dumps({'title': 'T', 'blocks': [{'headings': ['## Section'], 'rows': rows}]}), encoding='utf-8')
            r = subprocess.run([sys.executable, str(TOOLS / 'render_in_context.py'), str(d / 'm.json'), str(d / 'o.html'),
                                '--article', str(d / 'a.md'), '--source', str(d / 's.md'), '--against-source'],
                               capture_output=True, text=True)
            return r.returncode, (d / 'o.html').read_text(encoding='utf-8') if (d / 'o.html').exists() else r.stderr

    def row(self, **kw):
        r = {'label': 'D1', 'text': 'One new sentence. Another one of mine.', 'after': 'An installed paragraph',
             'source': [{'quote': 'First guide sentence.', 'from': 'the guide'}]}
        r.update(kw)
        return r

    def test_a_quote_is_shown_inside_its_whole_paragraph(self):
        rc, out = self.render([self.row()])
        self.assertEqual(rc, 0, out)
        self.assertIn('<span class="mark">First guide sentence.</span> Second guide sentence.', out)
        self.assertIn('the marked part, in its paragraph', out)

    def test_each_sentence_beside_what_it_carries(self):
        rc, out = self.render([self.row(carries=[{'draft': 'One new sentence.', 'guide': 'Second guide sentence.'},
                                                 {'draft': 'Another one of mine.', 'guide': None}])])
        self.assertEqual(rc, 0, out)
        self.assertIn('<td>One new sentence.</td><td>Second guide sentence.</td>', out)
        self.assertIn('added by the writer', out)

    def test_a_guide_quote_that_isnt_in_the_source_stops_the_page(self):
        rc, out = self.render([self.row(carries=[{'draft': 'One new sentence.', 'guide': 'A sentence the guide never had.'}])])
        self.assertNotEqual(rc, 0)
        self.assertIn('not in the source', out)


class GuideAdditionsNeedProvenance(unittest.TestCase):
    """Joel, 2026-10-08 02:23: "maybe we should somehow implement a rule that guide additions can't be suggested by other
    owrkers unless they are explained, what map change caused them, and how they are really needed vs superfluous to the
    guide." (E155)"""

    def run_draft(self, provenance=None):
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / 'a.md').write_text('# Title\n\nThe paragraph before.\n', encoding='utf-8')
            (d / 'master.html').write_text('<p>Keep one small promise to your little one.</p>', encoding='utf-8')
            t = {'before': 'The paragraph before.', 'after': '', 'brief': '- the point',
                 'guide_passage': 'The 2026-10-04 r4 guide (the passage this carries):\nKeep one small promise to your little one. '
                                  'Do not keep trying to sneak it back in through gentler exercises.'}
            if provenance:
                t['provenance'] = provenance
            (d / 't.json').write_text(json.dumps(t), encoding='utf-8')
            r = subprocess.run([sys.executable, str(TOOLS / 'reviewer' / 'reviewer.py'), '--article', str(d / 'a.md'),
                                'draft', str(d / 't.json'), str(d / 'o.txt')], capture_output=True, text=True)
            return r.returncode, r.stderr

    def test_an_unexplained_addition_stops_the_draft(self):
        rc, err = self.run_draft()
        self.assertNotEqual(rc, 0)
        self.assertIn('sneak it back in', err)
        self.assertNotIn('Keep one small promise', err)   # the original guide's sentence isn't an addition

    def test_an_explained_addition_drafts(self):
        rc, err = self.run_draft({'map_change': 'innerSignalGraph PR #126 (2026-10-04): decline handling',
                                  'why_reader_needs_it': 'a reader who said no to the frame needs to hear it is respected'})
        self.assertEqual(rc, 0, err)


class PrePushHookReadsCISteps(unittest.TestCase):
    """E158 (2026-10-09): the pre-push hook runs CI's own content-integrity steps, read from the workflow."""

    def load_hook(self):
        import importlib.machinery
        import importlib.util
        path = str(TOOLS / 'git-hooks' / 'pre-push')
        loader = importlib.machinery.SourceFileLoader('pre_push_hook', path)
        spec = importlib.util.spec_from_loader('pre_push_hook', loader)
        module = importlib.util.module_from_spec(spec)
        loader.exec_module(module)
        return module

    def test_it_runs_every_workflow_step(self):
        hook = self.load_hook()
        cmds = hook.steps(str(ROOT / '.github' / 'workflows' / 'content-integrity.yml'))
        joined = '\n'.join(cmds)
        for script in ('unittest discover -s tests', 'validate_content_repository.py',
                       'validate_article_architecture_maps.py', 'audit_codex_github.py'):
            self.assertIn(script, joined)
        self.assertFalse([c for c in cmds if c.startswith('python ')], cmds)  # this interpreter, not `python`

    def test_a_multi_line_step_is_skipped_with_a_note(self):
        hook = self.load_hook()
        with tempfile.TemporaryDirectory() as tmp:
            wf = pathlib.Path(tmp) / 'wf.yml'
            wf.write_text('steps:\n  - run: |\n      echo a\n  - run: python3 x.py\n', encoding='utf-8')
            self.assertEqual(hook.steps(str(wf)), ['python3 x.py'])


class ParagraphNumbers(unittest.TestCase):
    """Joel, 2026-10-11 03:47 UTC: "Why are there no numbers on many of these paragraphs? how do i identify them?"
    Both pages number paragraphs the same way: P1, P2, ... under each heading."""

    def test_numbers_restart_at_every_heading_and_skip_comments_and_list_bodies(self):
        sys.path.insert(0, str(TOOLS))
        import para_numbers
        blocks = ['# Title', 'One.', '<!-- a note -->', 'Two:', '1. first\n2. second', '## Sub', '<!-- note -->\nThree.', '> A quote.']
        labels = [pn for _, pn in para_numbers.number_blocks(blocks)]
        self.assertEqual(labels, [None, 'P1', None, 'P2', None, None, 'P1', 'P2'])


class ImageNotes(unittest.TestCase):
    """Joel, 2026-10-11 21:10 UTC: "the reviewer didn't see the image." An image note in the article shows as
    "[an image: …]" in the review prompts, as the image on the article page, and nowhere in the numbering or the
    text Pangram reads (it's a comment)."""

    NOTE = '<!-- IMAGE https://example.com/chart.png : A chart of the\n  method, in five steps. -->'

    def test_prompts_show_the_description_and_the_page_shows_the_image(self):
        import article_images
        md = 'Before.\n\n' + self.NOTE + '\n\nAfter.'
        self.assertIn('[an image: A chart of the method, in five steps.]', article_images.show(md))
        page = article_images.figure_html(md)
        self.assertIn('<img src="https://example.com/chart.png" alt="A chart of the method, in five steps."', page)
        self.assertEqual(article_images.notes(md), [('https://example.com/chart.png', 'A chart of the method, in five steps.')])

    def test_the_note_gets_no_paragraph_number(self):
        import para_numbers
        blocks = ['# Title', 'The image below maps it out:', self.NOTE, 'Next.']
        self.assertEqual([pn for _, pn in para_numbers.number_blocks(blocks)], [None, 'P1', None, 'P2'])

    def test_reviewer_and_stance_prompts_show_it(self):
        sys.path.insert(0, str(TOOLS / 'reviewer'))
        import reviewer
        with tempfile.TemporaryDirectory() as d:
            art = pathlib.Path(d) / 'a.md'
            art.write_text('# Title\n\nThe image below maps it out:\n\n' + self.NOTE + '\n\nNext.\n', encoding='utf-8')
            self.assertIn('[an image: A chart of the method, in five steps.]', reviewer.article_text(art))
            self.assertIn('[an image: A chart of the method, in five steps.]', reviewer.numbered_article(art))
        self.assertIn('[an image: A chart of the method, in five steps.]', stance_check_prompt.clean(self.NOTE))
        self.assertIn('[an image: A chart of the method, in five steps.]', '\n'.join(reviewer.reader_view('Before.\n\n' + self.NOTE + '\n\nAfter.')))


class OwnerEditsSpanBan(unittest.TestCase):
    """A ban that holds in one passage only: Joel's 2026-10-11 21:10 answer rules out "get checked" for
    predispositions, while another section rightly says "get checked" about a medical warning sign."""

    def test_span_must_not_contain(self):
        e = {'id': 'x', 'status': 'applied', 'span': {'from': 'And any predisposition', 'to': 'Milder reactions',
                                                       'must_not_contain': ['get checked']}}
        ok = check_owner_edits.norm('A medical warning sign: get checked first. And any predisposition is a caution sign. Milder reactions count too.')
        bad = check_owner_edits.norm('And any predisposition means you should get checked. Milder reactions count too.')
        self.assertEqual(check_owner_edits.check_entry(e, ok), [])
        self.assertTrue(check_owner_edits.check_entry(e, bad))


class GroundingSeesTheRestOfTheSection(unittest.TestCase):
    """2026-10-12: a grounding review of a paragraph in a section already in the article saw the article only up
    to the new text and the next paragraph, so in turns 45 and 46 it reported the acacia confusa warning, which a
    later paragraph carries, as MISSING. The prompt now carries the rest of the section, up to the next heading."""

    ART = ('## A\n\nBefore paragraph, about what came first.\n\nThe new paragraph goes here, old version.\n\n'
           'Next paragraph starts here and goes on.\n\nLater paragraph with the acacia confusa warning.\n\n'
           '## B\n\nNot this section.\n')

    def test_rest_of_section(self):
        sys.path.insert(0, str(TOOLS / 'reviewer'))
        import reviewer
        self.assertEqual(reviewer.rest_of_section(self.ART, 'Next paragraph starts here and goes on.'),
                         'Later paragraph with the acacia confusa warning.')
        self.assertEqual(reviewer.rest_of_section(self.ART, '(then the practices, not drafted yet)'), '')

    def test_grounding_prompt_carries_it(self):
        sys.path.insert(0, str(TOOLS / 'reviewer'))
        import reviewer
        with tempfile.TemporaryDirectory() as d:
            art, src, tgt = (pathlib.Path(d) / n for n in ('a.md', 'g.txt', 't.json'))
            art.write_text(self.ART, encoding='utf-8')
            src.write_text('The guide.\n', encoding='utf-8')
            tgt.write_text(json.dumps({'before': 'Before paragraph, about what came first.', 'next': 'Next paragraph starts here and goes on.',
                                       'guide_passage': 'The guide passage.'}), encoding='utf-8')
            reviewer.PATHS.update({'article': str(art), 'source': str(src)})
            try:
                p = reviewer.build_grounding('The new paragraph, new version.', str(tgt))
            finally:
                reviewer.PATHS.update({'article': None, 'source': None})
        self.assertIn('Later paragraph with the acacia confusa warning.', p)
        self.assertNotIn('Not this section.', p)


class PangramBatchNeedsTheGate(unittest.TestCase):
    """2026-10-12 (turn 48, E167): in the web app the Pangram batch was a script written by hand each time, so
    nothing stopped a call. A draft that marched S S S went to Pangram and read 100% AI, and later drafts went
    before their stance checks and march reads. pangram_gate.py writes the batch only for texts whose gate
    record passes."""

    CLEAN = {'kind': 'draft', 'march': ['S S B S'], 'cold': 'OK', 'grounding': 'OK', 'stance': 0, 'lint': 'REVIEW',
             'missing': []}

    def run_gate(self, drafts, gate, keys):
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / 'drafts.json').write_text(json.dumps(drafts), encoding='utf-8')
            (d / 'gate.json').write_text(json.dumps(gate), encoding='utf-8')
            r = subprocess.run([sys.executable, str(TOOLS / 'pangram_gate.py'), str(d / 'drafts.json'), str(d / 'gate.json'),
                                str(d / 'b.js'), '--name', 'tx'] + keys, capture_output=True, text=True)
            js = (d / 'b.js').read_text(encoding='utf-8') if (d / 'b.js').exists() else None
            read = (d / 'b-read.js').read_text(encoding='utf-8') if (d / 'b-read.js').exists() else None
        return r, js, read

    def test_the_reader_gives_each_result_its_link_and_flagged_words(self):
        # 2026-10-13 (E171): Joel couldn't see what had been checked when a flag was reported.
        _, _, read = self.run_gate({'p': 'One. Two.'}, {'p': self.CLEAN}, ['p'])
        self.assertIn("'https://www.pangram.com/history/' + it.uuid", read)
        self.assertIn('start_index', read)
        self.assertIn("flagged:", read)

    def test_a_march_without_a_break_blocks_the_call(self):
        r, js, _ = self.run_gate({'p': 'One. Two. Three.'}, {'p': dict(self.CLEAN, march=['S S S'])}, ['p'])
        self.assertEqual(r.returncode, 2)
        self.assertIn('the march blocks the call', r.stderr)
        self.assertIsNone(js)

    def test_an_edit_keeps_the_installed_versions_march(self):
        """E173 (2026-10-14): a fix of a few words in a paragraph that passed Pangram without a break is checked
        in Pangram; an edit that takes out the installed version's break is blocked."""
        e = dict(self.CLEAN, kind='edit', march=['S S S'], march_was=['S S S'], was='batch 267g, alone 100% Human')
        r, js, _ = self.run_gate({'p': 'One. Two. Three.'}, {'p': e}, ['p'])
        self.assertEqual(r.returncode, 0, r.stderr)
        r, js, _ = self.run_gate({'p': 'One. Two. Three.'}, {'p': dict(e, march_was=['S B S'])}, ['p'])
        self.assertEqual(r.returncode, 2)
        self.assertIn('the fix made the march', r.stderr.lower())
        g = dict(e); del g['was']
        r, js, _ = self.run_gate({'p': 'One. Two. Three.'}, {'p': g}, ['p'])
        self.assertEqual(r.returncode, 2)
        self.assertIn("needs 'was'", r.stderr)
        r, js, _ = self.run_gate({'p': 'One. Two. Three.'}, {'p': dict(e, cold='[2] UNCLEAR')}, ['p'])
        self.assertEqual(r.returncode, 2)

    def test_no_stance_check_blocks_the_call(self):
        g = dict(self.CLEAN); del g['stance']
        r, js, _ = self.run_gate({'p': 'One. Two.'}, {'p': g}, ['p'])
        self.assertEqual(r.returncode, 2)
        self.assertIn('stance', r.stderr)
        self.assertIsNone(js)

    def test_a_clean_draft_and_its_section_get_a_batch(self):
        import hashlib
        text = 'One. Two, maybe. Three.'
        section = {'text': '# H\n\nBefore.\n\n' + text, 'prefix': '# H\n\nBefore.', 'prefix_from_storage': 'h_old'}
        gate = {'p': self.CLEAN, 'q': dict(self.CLEAN, grounding='same claims as p', stance='same claims as p'),
                'h': {'kind': 'section', 'parts': ['installed', 'p'], 'repeats': 0}}
        r, js, read = self.run_gate({'p': text, 'q': text + ' Four.', 'h': section}, gate, ['p', 'q', 'h'])
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn(hashlib.sha256(text.encode()).hexdigest(), js)
        self.assertIn('sessionStorage.getItem("h_old") + "\\n\\n' + text, js)
        self.assertIn('window.__tx', js)
        self.assertIn(hashlib.sha256(section['text'].encode()).hexdigest(), read)

    def test_a_section_with_a_part_that_fails(self):
        gate = {'p': dict(self.CLEAN, cold='[2] UNCLEAR'), 'h': {'kind': 'section', 'parts': ['p']}}
        r, _, _ = self.run_gate({'p': 'One. Two.', 'h': '# H\n\nOne. Two.'}, gate, ['h'])
        self.assertEqual(r.returncode, 2)
        self.assertIn('part p: cold read', r.stderr)

    def test_same_claims_needs_the_other_record(self):
        g = dict(self.CLEAN, stance='same claims as gone')
        r, _, _ = self.run_gate({'p': 'One. Two.'}, {'p': g}, ['p'])
        self.assertEqual(r.returncode, 2)
        self.assertIn("but gone has None", r.stderr)

    def test_a_screen_needs_only_the_cheap_checks_and_never_joins_a_section(self):
        """E175 (Joel, 2026-10-15 16:39 UTC: "why did that take you 4 hours 22 minutes to humanize 1 paragraph?"):
        candidates are screened in Pangram after the linter and the march, before the long meaning reviews."""
        screen = {'kind': 'screen', 'march': ['S S B S', 'S B S S'], 'lint': 'REVIEW'}
        r, js, _ = self.run_gate({'p': 'One. Two, maybe. Three.'}, {'p': screen}, ['p'])
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIsNotNone(js)
        r, js, _ = self.run_gate({'p': 'One. Two. Three.'}, {'p': dict(screen, march=['S S S', 'S B S'])}, ['p'])
        self.assertEqual(r.returncode, 2)
        self.assertIn('the march blocks the call', r.stderr)
        r, js, _ = self.run_gate({'p': 'One. Two. Three.'}, {'p': dict(screen, lint='FAIL')}, ['p'])
        self.assertEqual(r.returncode, 2)
        gate = {'p': screen, 'h': {'kind': 'section', 'parts': ['p'], 'repeats': 0}}
        r, js, _ = self.run_gate({'p': 'One. Two, maybe.', 'h': '# H\n\nOne. Two, maybe.'}, gate, ['h'])
        self.assertEqual(r.returncode, 2)
        self.assertIn('is a screen', r.stderr)

    def test_a_draft_that_leaves_a_point_out_goes_only_as_a_probe(self):
        """E168 (Joel, 2026-10-12 17:36 UTC): "never take out something important in order to pass pangram"."""
        g = dict(self.CLEAN, missing=["political tribes' consistent positions and predictable reactions"])
        r, js, _ = self.run_gate({'p': 'One. Two, maybe. Three.'}, {'p': g}, ['p'])
        self.assertEqual(r.returncode, 2)
        self.assertIn('goes to Pangram only as a probe', r.stderr)
        self.assertIsNone(js)
        r, js, _ = self.run_gate({'p': 'One. Two, maybe. Three.'}, {'p': dict(g, probe=True)}, ['p'])
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_a_draft_needs_its_missing_list(self):
        g = dict(self.CLEAN); del g['missing']
        r, _, _ = self.run_gate({'p': 'One. Two.'}, {'p': g}, ['p'])
        self.assertEqual(r.returncode, 2)
        self.assertIn("no 'missing' list", r.stderr)

    def test_a_section_can_be_joined_from_earlier_items(self):
        para = 'One. Two, maybe. Three.'
        sec = '# H\n\n' + para
        gate = {'p': self.CLEAN, 'h': {'kind': 'section', 'parts': ['p'], 'repeats': 0}}
        r, js, _ = self.run_gate({'p': para, 'h': {'text': sec, 'concat': [{'lit': '# H\n\n'}, {'key': 'p'}]}}, gate, ['p', 'h'])
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('() => "# H\\n\\n" + sessionStorage.getItem("p")', js)
        r, _, _ = self.run_gate({'p': para, 'h': {'text': sec + '!', 'concat': [{'lit': '# H\n\n'}, {'key': 'p'}]}}, gate, ['p', 'h'])
        self.assertNotEqual(r.returncode, 0)


    def test_a_section_needs_a_repeats_check(self):
        """E172 (Joel, 2026-10-13 20:41 UTC): "duplication is very AI we already knew that but you're not checking
        that well enough". Untangling the Belonging Bargains read 100% Human only after its repeats came out."""
        para = 'One. Two, maybe. Three.'
        gate = {'p': self.CLEAN, 'h': {'kind': 'section', 'parts': ['p']}}
        r, js, _ = self.run_gate({'p': para, 'h': '# H\n\n' + para}, gate, ['p', 'h'])
        self.assertEqual(r.returncode, 2)
        self.assertIn('no repeats check of the assembled section', r.stderr)
        self.assertIsNone(js)
        for ok in (0, 'joel: 2026-10-13, keeps the second "belonging"'):
            gate['h']['repeats'] = ok
            r, js, _ = self.run_gate({'p': para, 'h': '# H\n\n' + para}, gate, ['p', 'h'])
            self.assertEqual(r.returncode, 0, r.stderr)
        gate['h']['repeats'] = 2
        r, _, _ = self.run_gate({'p': para, 'h': '# H\n\n' + para}, gate, ['p', 'h'])
        self.assertEqual(r.returncode, 2)

class MarchSplitsLists(unittest.TestCase):
    """2026-10-12 (turn 49): the march reader got a list's lead-in and its items run together, so a lead-in and
    four questions read as one sentence. Each item is its own sentence now."""

    def test_list_items_are_sentences(self):
        sys.path.insert(0, str(TOOLS / 'reviewer'))
        import reviewer
        ps = reviewer.march_paragraphs('While you\'re hooked, ask yourself these:\n- What am I about to lose?\n- Whose approval feels like survival?\n'
                                       '- Caring about somebody without losing your ground\n\nA plain paragraph. It has two sentences.')
        self.assertEqual(ps[0], ["While you're hooked, ask yourself these:", 'What am I about to lose?',
                                 'Whose approval feels like survival?', 'Caring about somebody without losing your ground'])
        self.assertEqual(ps[1], ['A plain paragraph.', 'It has two sentences.'])
