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

    def test_each_group_says_where_it_goes_and_carries_its_passage(self):
        p = self.run_cmd('dedup', 'OUT', 'T1', '--report', '/tmp/r.md')
        self.assertIn('GROUP 1 (t_one): would go right after [B1]', p)
        self.assertIn('Wait until you are calm. Keep a friend near.', p)
        self.assertNotIn('(the passage this carries)', p)
        self.assertIn('(No drafts yet', p)
        self.assertIn('/tmp/r.md', p)
        self.assertLess(p.index('THE ARTICLE'), p.index('GROUP 1'))


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
