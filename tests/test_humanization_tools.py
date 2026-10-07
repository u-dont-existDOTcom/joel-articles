"""Regression tests for the shared humanization tools' 2026-10-02 additions: the exact-character ledger check,
the linter's abstract-agent flag (O6) and the whole-article stance-check prompt."""
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
TOOLS = ROOT / 'tools' / 'humanization'
sys.path.insert(0, str(TOOLS))

import check_owner_edits  # noqa: E402
import stance_check_prompt  # noqa: E402

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
            self.assertNotIn('O1', self.lint(t), t)

    def test_gets_to_with_an_unclear_subject_is_a_review(self):
        out = self.lint("Your little one gets to decide how close to come.\n")
        self.assertIn('O1 "gets to" with an unclear subject', out)
        self.assertNotIn('O1 owner ban', out)

    def test_not_x_but_still_y(self):
        self.assertIn('O14', self.lint("It isn't proof, but it still counts as a good evening.\n"))
        self.assertIn('O14', self.lint("It isn't proof. It still counts as a good evening.\n"))
        self.assertNotIn('O14', self.lint("She still lives in the house by the river with her two dogs.\n"))

    def test_may_x_and_still_y(self):
        """Joel, 2026-10-07 16:46: "it makes no sense AND it sounds ai with "may have X and still Y""."""
        self.assertIn('O14 "may X and still Y"', self.lint("Somebody may really have crossed a boundary and still have hit something old in you.\n"))
        self.assertNotIn('O14', self.lint("Somebody may really have crossed a boundary. Notice what it hit in you.\n"))

    def test_a_list_is_a_review(self):
        out = self.lint("A few people you might call when it gets heavy:\n\n- a friend who listens\n- your sister\n")
        self.assertIn('O15 a list', out)
        self.assertEqual(out.count('O15 a list'), 1)
        self.assertNotIn('O15', self.lint("You could call a friend who listens, or your sister.\n"))


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


if __name__ == '__main__':
    unittest.main()
