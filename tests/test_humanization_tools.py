"""Regression tests for the shared humanization tools' 2026-10-02 additions: the exact-character ledger check,
the linter's abstract-agent flag (O6) and the whole-article stance-check prompt."""
import importlib.util
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
        self.assertIn('verdict: FAIL', out)   # E190 (Joel, 2026-10-17 22:59: "that's X, not Y")
        out = self.lint('If your little one says "he hurt me," that\'s harm, and it gets called harm, not "a learning experience." The rest can wait.\n')
        self.assertIn('O9', out)
        self.assertNotIn('O9', self.lint('If your little one says "he hurt me," that\'s harm, and it gets called harm, even if it was also a learning experience. The rest can wait.\n'))
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
        # "quietly" moved from O12 (a REVIEW) to O42 (a FAIL) at Joel's third flag of it, 2026-10-17 13:11
        self.assertIn('O42', self.lint("Cooperation also shouldn't quietly turn into assimilation, and that matters.\n"))
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

    def test_repeated_openers_fail_only_when_one_is_mine(self):
        # B13 (2026-10-18, turn 71): three installed paragraphs opening "I" don't block a check of their section; a
        # paragraph of mine that makes it a repeat does.
        his = ["I went down to the river every morning that spring, mostly to think, and sometimes just to watch the herons.",
               "I kept a notebook of what I saw there, the birds, the weather and whatever was on my mind that day.",
               "I still have it somewhere in a box in the attic, along with the letters my grandmother sent me back then."]
        installed = "# Notes\n\n" + "\n\n".join(his) + "\n"
        mine_ok = "Somebody new to the river might notice different things, of course, like the old mill or the boats going by."
        rc, out = self.lint("\n\n".join(his + [mine_ok]) + "\n", installed)
        self.assertNotIn('HARD: B13', out)
        self.assertIn('B13 repeated paragraph openers, all in installed', out)
        mine_bad = "I would go back there tomorrow if I could, just to sit by the water for an hour and listen to it go by."
        rc, out = self.lint("\n\n".join(his[:2] + [mine_bad]) + "\n", "# Notes\n\n" + "\n\n".join(his[:2]) + "\n")
        self.assertIn('HARD: B13', out)

    def test_two_lists_in_one_paragraph_fail(self):
        rc, out = self.lint(self.FAILED_P1)
        self.assertIn('E125 two lists', out)
        self.assertEqual(rc, 2)

    def test_his_fix_leaves_one_list_to_review(self):
        rc, out = self.lint(self.JOEL_P1)
        self.assertIn('E125 list of three', out)
        self.assertNotIn('E125 two lists', out)

    def test_one_list_in_my_sentence_fails(self):
        # E186 (Joel, 2026-10-17 14:01: "we got that list of 3 going on again. how is that not detected?")
        rc, out = self.lint("Any part of you that can watch, or wants to keep your body safe, or would rather wait on a decision "
                            "you can't undo, is welcome. And if none of them shows up yet? Then the questions wait.\n")
        self.assertIn('E125 list of three', out)
        self.assertIn('A FAIL in my sentences since 2026-10-17', out)
        self.assertEqual(rc, 2)

    def test_can_without_fails_and_other_without_ing_reviews(self):
        # E186 (Joel, 2026-10-17 14:01: "here we got that X can without Y ai tell")
        rc, out = self.lint("A meal can help, and so can a boundary or a kind sentence, without touching the question underneath. "
                            "Then the evening goes on as it was.\n")
        self.assertIn('E186 "X can ... without Y"', out)
        self.assertEqual(rc, 2)
        rc, out = self.lint("He left the farm without saying goodbye to anyone. The dog waited by the gate until dark.\n")
        self.assertIn('E186 "without ...ing"', out)
        self.assertNotIn('E186 "X can', out)
        self.assertNotIn('E186', self.lint("You can do it without anything special. The barn has room for all of it.\n")[1])

    def test_pairs_and_quotes_are_not_lists(self):
        for s in ('If words are there, speak or write them.\n',
                  'Or you tell a therapist, \u201cNo, that\'s not right for me,\u201d and they call it resistance.\n',
                  'If the room itself triggers your spidey sense, leave, or lock the door and get help.\n',
                  'Or something does come, a voice or a hunch, and you listen without putting it in charge.\n',
                  # E186 (2026-10-17): an opening phrase, a speaker aside, a doubled word and a quote the sentence splitter
                  # cut short aren't items, now that one list is a FAIL
                  'In that view, repeated thought and intention shape the mind, and that keeps going through death.\n',
                  'Repeated thought and intention shape the mind, it says, and that keeps going through death.\n',
                  'Whatever you keep thinking and intending, over and over, bends the mind that way.\n',
                  'If it makes you unreal, so it\'s hard to get back to your life, make it simpler: "I miss you, and I care."\n'):
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


class PreservationKeysElsewhere(unittest.TestCase):
    """Joel, 2026-10-17 02:07 UTC: "you can only cut if it isn't losing important meaning or there's no good way to merge".
    Section 16 repeats section 14's list of what the Bruderhof shaped in his father; the dedup leaves it to section 14, and
    the key check passes the unit only when section 14 of the article carries its words."""
    UNITS = {'units': [{'id': 'U44', 'what': 'the father made a film and founded a research organization',
                        'keys': [['film'], ['research']],
                        'elsewhere': {'section': '# Dissolution and Exit', 'words': ['foundation he started', 'film he made'],
                                      'why': 'the dedup'}}]}
    DRAFT = 'Decades after the Bruderhof shaped my father, I am publishing his film.'
    ART = ('# Dissolution and Exit\n\nIt shaped the foundation he started and the film he made.\n\n'
           '# What This Looks Like\n\nSomething else.\n')

    def test_the_other_section_has_to_carry_it(self):
        moved = []
        self.assertEqual(preservation_keys.check(self.UNITS, self.DRAFT, self.ART, moved), [])
        self.assertEqual([m['id'] for m in moved], ['U44'])
        # without the article, or with the words gone from that section (or only in another one), it is missing
        self.assertEqual([m['id'] for m in preservation_keys.check(self.UNITS, self.DRAFT)], ['U44'])
        gone = self.ART.replace('the foundation he started and ', '') + '\nthe foundation he started\n'
        self.assertEqual([m['id'] for m in preservation_keys.check(self.UNITS, self.DRAFT, gone)], ['U44'])


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


class LinkFlags(unittest.TestCase):
    """link_flags.py (2026-10-15). Joel, 18:28 UTC, question 32: four cold reads asked "why is this here?" of a sentence
    about his linked research report, and I proposed a cut without looking at the link: "you forgot to notice that
    "research" is a link to my research report, so it's about that"."""
    DRAFT = ('# Part\n\n"Outside" does not always mean the nation-state. [My research](https://example.org/research/) '
             'initially leaned too far that way. The important thing is a competent layer.\n\n'
             'Also choose a mediator before the crisis.\n')

    def run_tool(self, report, disp=None):
        import link_flags
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / 'draft.md').write_text(self.DRAFT, encoding='utf-8')
            (d / 'r.md').write_text(report, encoding='utf-8')
            args = [str(d / 'draft.md'), str(d / 'r.md')]
            if disp is not None:
                (d / 'disp.md').write_text(disp, encoding='utf-8')
                args += ['--dispositions', str(d / 'disp.md')]
            found = link_flags.flags(self.DRAFT, [str(d / 'r.md')])
            return found, link_flags.main(args)

    def test_a_flag_on_a_linked_sentence_is_listed_with_its_address(self):
        found, code = self.run_tool('[P1] Why is this here: "My research [a link to example.org/research] initially '
                                    'leaned too far that way." Nothing earlier shows it.\n[P2] "choose a mediator before the '
                                    'crisis": OK really.\n')
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]['links'], [('My research', 'https://example.org/research/')])
        self.assertEqual(code, 0)

    def test_an_equivalent_line_is_not_a_flag(self):
        found, code = self.run_tool('1. "My research initially leaned too far that way": EQUIVALENT. Word for word.\n'
                                    '[P1] OK\n2. ADDED: "initially leaned too far that way" is new.\n')
        self.assertEqual(len(found), 1)
        self.assertTrue(found[0]['line'].startswith('2. ADDED'))

    def test_with_dispositions_the_flag_needs_a_line_on_its_link(self):
        rep = '[P1] "initially leaned too far that way" ... why is this here?\n'
        _, code = self.run_tool(rep, disp='- Kept: "initially leaned too far that way" (one reader).\n')
        self.assertEqual(code, 1)
        _, code = self.run_tool(rep, disp='- Kept: "initially leaned too far that way": the link goes to his report, '
                                          'and the sentence tells its readers which way it leans.\n')
        self.assertEqual(code, 0)


class MarchPrompt(unittest.TestCase):
    """reviewer.py march --about (2026-10-15): the march prompt told every reader it was reading the inner-child article,
    the community lane's paragraphs included."""

    def test_about_names_the_article_and_drops_the_inner_child_line(self):
        sys.path.insert(0, str(TOOLS / 'reviewer'))
        import reviewer
        p = reviewer.build_march('One step. Then another!\n\nA second paragraph.', 'a blog article about building '
                                 'intentional communities')
        self.assertTrue(p.startswith('Below are 2 paragraphs from a blog article about building intentional communities,'))
        self.assertNotIn('inner child', p.split('\n', 1)[0])
        self.assertIn('T1: [1] One step. [2] Then another!', p)
        self.assertIn('inner-child work', reviewer.build_march('One. Two.'))   # the default is unchanged

    def test_a_sentence_that_opens_with_a_link_or_a_single_quote_is_its_own_sentence(self):
        # 2026-10-16: section 13's "‘Outside’ doesn’t always mean the nation-state. [My research](...) initially leaned too
        # far that way." reached both march readers as one sentence with one label.
        sys.path.insert(0, str(TOOLS / 'reviewer'))
        import reviewer
        self.assertEqual(reviewer.split_sentences('Then this. ‘Outside’ isn’t the state. [My research](https://x.example/r) '
                                                  'leaned that way. *Very* important! Dr. Who stays.'),
                         ['Then this.', '‘Outside’ isn’t the state.', '[My research](https://x.example/r) leaned that way.',
                          '*Very* important!', 'Dr. Who stays.'])

    def test_an_emoji_between_sentences_ends_the_first_one(self):
        # 2026-10-17: "...charming for two weeks! 😅 So that's about all you'll find out." reached the march readers as one
        # sentence, so they gave it one label (S), and the paragraph's break went unseen.
        sys.path.insert(0, str(TOOLS / 'reviewer'))
        import reviewer
        self.assertEqual(reviewer.split_sentences("Charming for two weeks! 😅 So that's about all. Fine 😜 then."),
                         ['Charming for two weeks! 😅', "So that's about all.", 'Fine 😜 then.'])
        self.assertEqual(reviewer.split_sentences('Who decides? (Hint: not the recruiter! 😜) What rights will they have?'),
                         ['Who decides?', '(Hint: not the recruiter! 😜)', 'What rights will they have?'])


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

    def test_a_sentence_about_a_linked_report_is_for_whoever_opens_it(self):
        # Joel, 2026-10-15 18:28 UTC, question 32: four cold reads had asked "why is this here?" of "My research initially
        # leaned too far that way", where "My research" links to his research report: "this is the same problem we had
        # before where you forgot to notice that "research" is a link to my research report, so it's about that."
        p = self.run_cmd('--section', 'Second Part')
        self.assertIn('A sentence about a linked thing can be there for the reader who opens the link.', p)
        self.assertIn('so it\'s about that', p)
        self.assertIn('only when it would tell a reader who clicked through nothing', p)

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

    def test_the_linter_decides_lint_when_given_the_article(self):
        # 2026-10-16 (E179): a draft the linter FAILs went into a batch as REVIEW, typed by hand.
        fail = ('You can try this. You can also try that. You might want to start small. It helps to breathe. '
                'You can keep going. You might notice a change. It helps to rest. You can stop anytime.')
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / 'art.md').write_text('# A\n\nSome installed text here.\n', encoding='utf-8')
            (d / 'drafts.json').write_text(json.dumps({'p': fail}), encoding='utf-8')
            (d / 'gate.json').write_text(json.dumps({'p': {'kind': 'screen', 'march': ['S B S'], 'lint': 'REVIEW'}}), encoding='utf-8')
            r = subprocess.run([sys.executable, str(TOOLS / 'pangram_gate.py'), str(d / 'drafts.json'), str(d / 'gate.json'),
                                str(d / 'b.js'), '--name', 'tx', '--lint-article', str(d / 'art.md'), 'p'], capture_output=True, text=True)
        self.assertIn('the linter says', r.stderr)

    def test_the_reader_gives_each_result_its_link_and_flagged_words(self):
        # 2026-10-13 (E171): Joel couldn't see what had been checked when a flag was reported.
        _, _, read = self.run_gate({'p': 'One. Two.'}, {'p': self.CLEAN}, ['p'])
        self.assertIn("'https://www.pangram.com/history/' + it.uuid", read)
        self.assertIn('start_index', read)
        self.assertIn("flagged:", read)

    def test_a_note_cannot_waive_a_dropped_point(self):
        """2026-10-16: section 13 v31 passed with "missing": [] and the dropped "if the community uses them" written in a
        note. Joel, 23:38 UTC: "yes i want "if the community uses them" back"."""
        note = dict(self.CLEAN, missing_note='keeps the questions without the published "if the community uses them"')
        r, js, _ = self.run_gate({'p': 'One. Two.'}, {'p': note}, ['p'])
        self.assertEqual(r.returncode, 2)
        self.assertIn("a note can't waive a dropped point", r.stderr)
        r, js, _ = self.run_gate({'p': 'One. Two.'}, {'p': dict(note, owner_ok='Joel, 2026-10-17: "fine without it"')}, ['p'])
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_every_paragraph_needs_a_human_result_alone(self):
        """Joel, 2026-10-16 23:38 UTC: "no ai tells you see, and it has human tells? isn't that part of the rules?" Section
        13 went in checked only in groups; alone, its short visit read AI (312g)."""
        import paragraphs_alone
        long1 = ' '.join(['word%d' % i for i in range(60)]) + '.'
        short = 'A short one, under fifty words.'
        md = '# S\n\n' + long1 + '\n\n' + short + '\n'
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / 'drafts.json').write_text(json.dumps({'a': long1, 'ab': long1 + '\n\n' + short}), encoding='utf-8')
            (d / 'b1-results.json').write_text(json.dumps({'a': ['Human Written'], 'ab': ['AI Detected']}), encoding='utf-8')
            ok, report = paragraphs_alone.check(md, [d])
            self.assertFalse(ok)
            self.assertTrue(report[1].startswith('MISS A short one'), report)
            (d / 'b1-results.json').write_text(json.dumps({'a': ['Human Written'], 'ab': ['Human Written']}), encoding='utf-8')
            ok, report = paragraphs_alone.check(md, [d])
            self.assertTrue(ok, report)
            # the page's embed lines (section 15's post card and video) are not paragraphs; a prose line that only starts
            # with a link still is
            emb = md + '\n[Professor Baby Sheep Taught Me](https://x.substack.com/p/y)Copy link\n\nDouble click to interact with video\n'
            ok, report = paragraphs_alone.check(emb, [d])
            self.assertTrue(ok, report)
            prose = md + '\n[A link](https://x.example/) and then a sentence of mine.\n'
            ok, report = paragraphs_alone.check(prose, [d])
            self.assertFalse(ok, report)

    def test_a_short_list_entry_counts_in_the_shortest_run_pangram_can_read(self):
        """2026-10-17, the community article's appendix: two or three entries of 8 to 40 words under each heading, so no
        pair under one heading reaches Pangram's 50 words. Such an entry counts inside the shortest run around it (headings
        between included) that reaches 50 words; a longer run doesn't count for it."""
        import paragraphs_alone
        e = lambda n, k: ' '.join('%s%d' % (k, j) for j in range(n)) + '.'
        a, b, c, d_ = e(20, 'a'), e(20, 'b'), e(20, 'c'), e(20, 'd')
        md = '# Top\n\n## One\n\n' + a + '\n\n' + b + '\n\n## Two\n\n' + c + '\n\n' + d_ + '\n'
        abc = a + '\n\n' + b + '\n\nTwo\n\n' + c   # 61 words: a and b with c (b, Two and c alone: 41)
        bcd = b + '\n\nTwo\n\n' + c + '\n\n' + d_  # 61 words
        runs = {(x, y) for x, y, _, _ in paragraphs_alone.minimal_runs(md, 1)}
        self.assertEqual(runs, {(0, 2), (1, 3)})
        abcd = abc + '\n\n' + d_                   # 81 words: d can go and it still reaches 50, so it isn't the shortest
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / 'drafts.json').write_text(json.dumps({'abcd': abcd}), encoding='utf-8')
            (d / 'b1-results.json').write_text(json.dumps({'abcd': ['Human Written']}), encoding='utf-8')
            ok, report = paragraphs_alone.check(md, [d])
            self.assertFalse(ok, report)
            (d / 'drafts.json').write_text(json.dumps({'abc': abc, 'bcd': bcd}), encoding='utf-8')
            (d / 'b1-results.json').write_text(json.dumps({'abc': ['Human Written'], 'bcd': ['Human Written']}),
                                               encoding='utf-8')
            ok, report = paragraphs_alone.check(md, [d])
            self.assertTrue(ok, report)
            (d / 'b1-results.json').write_text(json.dumps({'abc': ['Human Written'], 'bcd': ['AI Detected']}),
                                               encoding='utf-8')
            ok, report = paragraphs_alone.check(md, [d])
            self.assertFalse(ok, report)                # d is only in bcd
            self.assertTrue(report[3].startswith('MISS d0'), report)

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

    def test_a_cut_goes_to_pangram_whatever_the_march_says(self):
        """2026-10-17: a cut that took out the installed version's only break goes to Pangram when the record gives
        the installed text and the text is that text with words taken out (Joel, 21:37 UTC: "it made no difference
        taking those exclamation phrases out for pangram"); a rewording, or a "cut" that adds a word, is still held."""
        e = dict(self.CLEAN, kind='edit', march=['S S'], march_was=['S B S'], was='batch 420g, alone 100% Human',
                 cut_of='One. Very important! Three.')
        r, js, _ = self.run_gate({'p': 'One. Three.'}, {'p': e}, ['p'])
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIsNotNone(js)
        r, js, _ = self.run_gate({'p': 'One. Four.'}, {'p': e}, ['p'])
        self.assertEqual(r.returncode, 2)
        self.assertIn('not that text with words taken out', r.stderr)
        g = dict(e); del g['cut_of']
        r, js, _ = self.run_gate({'p': 'One. Three.'}, {'p': g}, ['p'])
        self.assertEqual(r.returncode, 2)
        self.assertIn('the fix made the march', r.stderr.lower())

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


class PauseTally(unittest.TestCase):
    """pause_tally.py (2026-10-16). Joel, 18:22 UTC, on section 13's "How do you know?": "why did the reviewer not cut that,
    what's that? know what? doesn't seem to follow...". Four cold reads in three rounds had paused there and settled it from
    the next sentence; nothing counted the pauses."""
    DRAFT = ('# Part\n\nWrite down your answers to these questions.\n\nHow do you know? Judge people by their conduct.\n\n'
             'My research initially leaned too far that way.\n')

    def reports(self, d, texts):
        out = []
        for i, t in enumerate(texts):
            p = pathlib.Path(d) / ('SENSE-%d.md' % i)
            p.write_text(t, encoding='utf-8')
            out.append(str(p))
        return out

    def test_old_prose_pauses_and_new_paused_lines_both_count(self):
        import pause_tally
        with tempfile.TemporaryDirectory() as d:
            reps = self.reports(d, [
                'No breaks found. Places where I paused and then got it (so not reported): P20 "How do you know?" read as '
                'how to judge a newcomer; P26 "that way" read as toward the nation-state.',
                'No breaks. Every phrase that made me pause (for example P20 "How do you know?", P14 "the full sequence") '
                'is settled by the next one.',
                '[P1] OK\nPaused: P20 “How do you know?”; P3 "promising strangers"',
                'Paused: none'])
            found = pause_tally.repeated(reps)
        self.assertEqual([(f['quote'], f['count']) for f in found], [('How do you know?', 3)])

    def test_a_reading_in_quotes_after_the_phrase_is_not_a_pause(self):
        import pause_tally
        self.assertEqual(pause_tally.pauses('Paused: P3 "promising strangers" read as "untested", per P1'),
                         [(3, 'promising strangers')])

    def test_the_draft_and_the_authors_own_sentences_filter_the_list(self):
        import pause_tally
        with tempfile.TemporaryDirectory() as d:
            reps = self.reports(d, ['Paused: P20 "How do you know?"; P26 "that way"; P9 "gone phrase"'] * 2)
            (pathlib.Path(d) / 'draft.md').write_text(self.DRAFT, encoding='utf-8')
            (pathlib.Path(d) / 'his.txt').write_text('My research initially leaned too far that way.', encoding='utf-8')
            found = pause_tally.repeated(reps, str(pathlib.Path(d) / 'draft.md'), None, [str(pathlib.Path(d) / 'his.txt')])
        self.assertEqual([f['quote'] for f in found], ['How do you know?'])

    def test_with_dispositions_each_repeated_pause_needs_an_answer(self):
        import pause_tally
        with tempfile.TemporaryDirectory() as d:
            reps = self.reports(d, ['Paused: P20 "How do you know?"'] * 2)
            disp = pathlib.Path(d) / 'D.md'
            disp.write_text('- Kept: nothing about it.\n', encoding='utf-8')
            self.assertEqual(pause_tally.main(reps + ['--dispositions', str(disp)]), 1)
            disp.write_text('- Cut: "How do you know?" (Joel, 18:22).\n', encoding='utf-8')
            self.assertEqual(pause_tally.main(reps + ['--dispositions', str(disp)]), 0)

    def test_a_list_of_paused_phrases_answers_nothing(self):
        """2026-10-17: section 15's "apology" (the law's French "apologie"; Joel at 13:11: "should have been translated as
        "advocacy"") was paused at in rounds r4 and r8, and both dispositions only listed it "for the cross-round count",
        with "(published)". The tally took the list for an answer."""
        import pause_tally
        with tempfile.TemporaryDirectory() as d:
            reps = self.reports(d, ['Paused: P7 "apology"; P8 "So which is it?"'] * 2)
            disp = pathlib.Path(d) / 'D.md'
            disp.write_text('- Phrases paused at, for the cross-round count: "apology" (published), "So which is it?".\n',
                            encoding='utf-8')
            self.assertEqual(pause_tally.main(reps + ['--dispositions', str(disp)]), 1)
            disp.write_text('- Others: "apology" (published), "So which is it?" (published).\n', encoding='utf-8')
            self.assertEqual(pause_tally.main(reps + ['--dispositions', str(disp)]), 1)
            disp.write_text('- "apology": fixed by Joel, now "advocacy".\n- "So which is it?": kept because the next sentence '
                            'answers it.\n', encoding='utf-8')
            self.assertEqual(pause_tally.main(reps + ['--dispositions', str(disp)]), 0)


class AuthorMarksReadExactLocksAndLinks(unittest.TestCase):
    """meaning_sweep.owner_strings (2026-10-16): his published "[My research](...) initially leaned too far that way.", kept by
    his 32 b as a must_contain_exact lock with its link, was in no owner string, so the pause tally listed "that way" as mine."""

    def test_closing_quotes_and_line_breaks_survive_the_marks(self):
        """2026-10-17: the splitter swallowed a closing quote after a sentence end ("keep clean.” Again" came out "keep
        clean. Again"), so the faithfulness readers reported nine quotes missing that the article has."""
        text = ('We sang: “Pick up your toys, keep clean.” Again and again. He said “little school.” I went.\n'
                'A list line? (Not everyone does!) Then "First let\'s get land!" "Then a vision!" Done.')
        self.assertEqual(meaning_sweep.mark_author(text, []), text)
        out = meaning_sweep.mark_author(text, [meaning_sweep.norm('He said “little school.”')])
        self.assertIn(meaning_sweep.MARK_OPEN + 'He said “little school.”' + meaning_sweep.MARK_CLOSE + ' I went.\nA list', out)
        self.assertEqual(out.replace(meaning_sweep.MARK_OPEN, '').replace(meaning_sweep.MARK_CLOSE, ''), text)

    def test_an_exact_lock_with_a_link_marks_the_visible_sentence(self):
        with tempfile.TemporaryDirectory() as d:
            led = pathlib.Path(d) / 'OWNER-EDITS.json'
            led.write_text(json.dumps({'entries': [{'id': 'x', 'status': 'applied', 'words': 'his',
                                                     'must_contain_exact': ['[My research](https://example.org/r/) initially '
                                                                            'leaned too far that way.']}]}), encoding='utf-8')
            owners = meaning_sweep.owner_strings(str(led), [])
        out = meaning_sweep.mark_author('Outside is not the state. My research initially leaned too far that way.', owners)
        self.assertIn(meaning_sweep.MARK_OPEN + 'My research initially leaned too far that way.' + meaning_sweep.MARK_CLOSE, out)


class ColdReadOpenerRule(unittest.TestCase):
    """sense_section.txt (2026-10-16): a paragraph's first sentence has to follow from what comes before it, and every cold
    read ends with a "Paused:" line. Joel, 18:22 UTC: "what's that? know what? doesn't seem to follow...". Narrowed after
    the control read of his section 11 flagged two of his openers that pick up an earlier paragraph or turn with "though"."""

    def test_the_prompt_carries_the_rule_its_limit_and_the_paused_line(self):
        t = (TOOLS / 'reviewer' / 'sense_section.txt').read_text(encoding='utf-8')
        self.assertIn("A paragraph's first sentence has to follow from what comes before it.", t)
        self.assertIn('know what? doesn\'t seem to follow', t)
        self.assertIn('picks up something from a paragraph or two back', t)
        self.assertIn('So does a first sentence that says in full what it\'s about', t)
        self.assertIn('add one line that starts "Paused:"', t)

    def test_the_prompt_names_a_joke_that_takes_back_a_limit_and_a_dangling_either(self):
        """Joel, 2026-10-17 21:37 UTC: "saying "one is enough" actually undermines the prior sentence "at least one"", and
        ""not that either" doesn't make sense" (a cold reader had paused there, and the pause was kept as his published word)."""
        t = (TOOLS / 'reviewer' / 'sense_section.txt').read_text(encoding='utf-8')
        self.assertIn('turns a minimum into a maximum', t)
        self.assertIn('a word like "either", "too", "also" or "again" with nothing before it to refer to', t)

    def test_the_prompt_names_a_sentence_that_only_takes_back_the_one_before_it(self):
        """Joel, 2026-10-17 23:10 UTC, rewrote section 2's opening: my "an advisory about it. Or about the loneliness under it,
        at least." only patched my own first clause, and his names the loneliness there ("the longing to escape loneliness
        which inspired my father's movie"), so nothing needs taking back."""
        t = (TOOLS / 'reviewer' / 'sense_section.txt').read_text(encoding='utf-8')
        self.assertIn('a sentence that only takes back the one before it', t)


class PangramRoundBuildsEveryCheckAtOnce(unittest.TestCase):
    """2026-10-17 (turn 64, E181): turn 63 split each candidate's checks over separate rounds (alone first, then
    the pair and the section) and wrote each round's files by hand; Joel: "idk why that had to take 38 mins tho".
    pangram_round.py builds the paragraph alone, the pair with the paragraph before and the section, for every
    candidate, in one batch."""

    def test_each_candidate_is_checked_alone_after_its_neighbor_and_in_its_section(self):
        import pangram_round
        with tempfile.TemporaryDirectory() as d:
            art = pathlib.Path(d) / 'a.md'
            art.write_text('# Earlier\n\nOld text.\n\n# The Section\n\n<!-- a note -->\n\nFirst one.\n\nSecond one.\n', encoding='utf-8')
            c = pathlib.Path(d) / 'p3-x.txt'
            c.write_text('A new one.\n', encoding='utf-8')
            drafts, gate, n = pangram_round.build(str(art), 'The Section', 'r1', [(str(c), 'S B')], 'P1 S | P2 S', 'note')
        self.assertEqual(n, 3)
        self.assertEqual(drafts['r1_p3x'], 'A new one.')
        self.assertEqual(drafts['r1_pairp3x'], 'Second one.\n\nA new one.')
        self.assertEqual(drafts['r1_secp3x'], '# The Section\n\nFirst one.\n\nSecond one.\n\nA new one.')
        self.assertEqual(list(drafts), ['r1_p3x', 'r1_pairp3x', 'r1_secp3x'])
        self.assertTrue(all(g['kind'] == 'screen' for g in gate.values()))
        self.assertEqual(gate['r1_secp3x']['march'], ['P1 S | P2 S | P3 S B'])

    def test_a_spec_puts_several_sections_in_one_batch_each_linted_against_its_own_article(self):
        """2026-10-17 (turn 65): one batch for paragraphs of several sections, one wait in the browser."""
        import pangram_round
        from unittest import mock
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / 'a1.md').write_text('# One\n\nFirst.\n', encoding='utf-8')
            (d / 'a2.md').write_text('# Two\n\nSecond.\n', encoding='utf-8')
            (d / 'x-a.txt').write_text('New for one.\n', encoding='utf-8')
            (d / 'y-a.txt').write_text('New for two.\n', encoding='utf-8')
            (d / 'P.md').write_text('| date | what | prediction | result | hit |\n', encoding='utf-8')
            groups = [{'article': str(d / 'a1.md'), 'heading': 'One', 'section_march': 'P1 S B', 'cands': [[str(d / 'x-a.txt'), 'S B']]},
                      {'article': str(d / 'a2.md'), 'heading': 'Two', 'section_march': 'P1 S B', 'cands': [[str(d / 'y-a.txt'), 'S B']]}]
            with mock.patch.object(pangram_round.subprocess, 'run', return_value=mock.Mock(returncode=0)) as ran:
                rc = pangram_round.run(groups, 'r9', str(d / 'out'), str(d / 'P.md'), 'today')
            self.assertEqual(rc, 0)
            drafts = json.loads((d / 'out-drafts.json').read_text(encoding='utf-8'))
            gate = json.loads((d / 'out-gate.json').read_text(encoding='utf-8'))
            # after a section's only paragraph the pair would be the section again, so it isn't built
            self.assertEqual(set(drafts), {'r9_xa', 'r9_secxa', 'r9_ya', 'r9_secya'})
            self.assertEqual(gate['r9_secxa']['lint_article'], str(d / 'a1.md'))
            self.assertEqual(gate['r9_ya']['lint_article'], str(d / 'a2.md'))
            self.assertEqual(ran.call_count, 1)  # one gate run, one batch
            self.assertEqual((d / 'P.md').read_text(encoding='utf-8').count('(pending)'), 4)
            groups[1]['checks'] = 'alone'
            with mock.patch.object(pangram_round.subprocess, 'run', return_value=mock.Mock(returncode=0)):
                pangram_round.run(groups, 'r10', str(d / 'out2'), str(d / 'P.md'), 'today')
            self.assertEqual(set(json.loads((d / 'out2-drafts.json').read_text(encoding='utf-8'))), {'r10_xa', 'r10_secxa', 'r10_ya'})


class PangramBatchRunsInTwoTabs(unittest.TestCase):
    """2026-10-17 (turn 65): a 69-check batch took about 20 minutes in one tab. The batch can run in two tabs at
    once, one from each end, meeting in the middle through localStorage."""

    def test_the_batch_has_a_reverse_lane_that_stops_where_the_other_tab_is(self):
        import pangram_gate
        js = pangram_gate.batch_js('t9', [('t9_a', 'One text.'), ('t9_b', 'Two text.')])
        self.assertIn('const rev = !!window.__reverse;', js)
        self.assertIn('items0.slice().reverse()', js)
        self.assertIn("localStorage.setItem(lane(rev ? 'rev' : 'fwd')", js)
        self.assertIn('the other tab has the rest', js)
        self.assertIn("log(k + ': taking')", js)
        self.assertIn('"t9_a"', js)


class PangramScoreFillsThePendingRows(unittest.TestCase):
    """2026-10-17 (turn 65): each batch's PREDICTIONS.md rows were scored by typing every result by hand."""

    def test_a_pending_row_gets_its_result_time_link_and_hit(self):
        import pangram_score
        lines = ['| d | P2 alone [t9_pa], a screen | Human, low (my call) | (pending) | |',
                 '| d | the h1 with pa [t9_sec2pa], a screen | Human, low (my call) | (pending) | |',
                 '| d | done before [t8_x], a screen | Human, low (my call) | Human Written (0.01, low; 70) | hit |']
        read = {'t9_pa': {'headline': 'Human Written', 'avg_ai_likelihood': 0.0041, 'words': 72,
                          'windows': ['Human, low, 72'], 'utc': '2026-10-17T04:00:52Z', 'link': 'https://www.pangram.com/history/u1'},
                't9_sec2pa': {'headline': 'AI Detected', 'avg_ai_likelihood': 0.64, 'words': 226,
                              'windows': ['Human, high, 54', 'AI, high, 88', 'AI, medium, 84'], 'utc': '2026-10-17T04:01:00Z',
                              'link': 'https://www.pangram.com/history/u2'}}
        out, done = pangram_score.score(read, lines)
        self.assertEqual(out[0], '| d | P2 alone [t9_pa], a screen | Human, low (my call) | Human Written (0.004, low; 72); '
                                 '04:00:52 UTC, https://www.pangram.com/history/u1 | hit |')
        self.assertIn('AI Detected (0.64; 226), 3 windows: AI 88 words (high), AI 84 words (medium); 04:01:00 UTC', out[1])
        self.assertTrue(out[1].endswith('| miss |'))
        self.assertEqual(out[2], lines[2])
        self.assertEqual([k for k, _, _ in done], ['t9_pa', 't9_sec2pa'])
        short = pangram_score.expand(['Human Written', 0.0041, 72, ['Human, low, 72'], '2026-10-17T04:00:52Z', 'u1'])
        self.assertEqual(short, dict(read['t9_pa']))


class ClickableLinks(unittest.TestCase):
    """html_links.py and pangram_links_check.py --chat (2026-10-16). Joel, 21:05 UTC: "(your links are not clickable btw)":
    my final message gave each Pangram check as a bare address, and the pages escaped their notes, so no address was a link."""

    def test_linkify_makes_each_address_a_link_and_keeps_the_punctuation_after_it(self):
        import html_links
        out = html_links.linkify('Human, high (https://www.pangram.com/history/abc-1). Next: <b>')
        self.assertIn('<a href="https://www.pangram.com/history/abc-1">https://www.pangram.com/history/abc-1</a>). Next: &lt;b&gt;', out)

    def test_autolink_markdown_leaves_written_links_and_code_alone(self):
        import html_links
        md = 'See https://a.example/x, [the page](https://b.example/y) and `gh pr view https://c.example/z`.'
        self.assertEqual(html_links.autolink_markdown(md),
                         'See <https://a.example/x>, [the page](https://b.example/y) and `gh pr view https://c.example/z`.')
        self.assertEqual(html_links.bare_urls(md), ['https://a.example/x'])
        # the resume line, written [url](url) as Joel asked (2026-10-16), is a link
        self.assertEqual(html_links.bare_urls('read [https://g.example/h.md](https://g.example/h.md) and go on'), [])

    @unittest.skipUnless(importlib.util.find_spec('markdown'), 'python-markdown is not installed (CI has no pip step)')
    def test_the_questions_renderer_links_bare_addresses(self):
        sys.path.insert(0, str(ROOT / 'articles' / 'intentional-communities' / 'candidate' / 'tools'))
        import render_questions
        out = render_questions.render('# Q\n\nLast updated today.\n\n## Open questions\n\n- 🟢 It reads Human: https://www.pangram.com/history/abc-2\n')
        self.assertIn('<a href="https://www.pangram.com/history/abc-2">', out)

    @unittest.skipUnless(importlib.util.find_spec('markdown'), 'python-markdown is not installed (CI has no pip step)')
    def test_two_blank_lines_between_items_keep_the_text_column(self):
        """Joel's screenshot, 2026-10-16 23:38 UTC: an item after two blank lines showed one word per line, because
        python-markdown wrapped it in <p> and the grid put the <p> in the dot's .7rem column."""
        sys.path.insert(0, str(ROOT / 'articles' / 'intentional-communities' / 'candidate' / 'tools'))
        import render_questions
        md = ('# Q\n\nLast updated today.\n\n## Decided\n\n> [!TIP]\n> Answered.\n\n- 🟢 one\n- 🟢 two\n\n\n'
              '- 🟢 three, after two blank lines\n- 🟢 four\n')
        out = render_questions.render(md)
        self.assertNotIn('<li>\n<p>', out)
        self.assertIn('<div>three, after two blank lines</div>', out)
        self.assertEqual(out.count('<li class="gap"'), 1)
        self.assertEqual(render_questions.misplaced_items(
            '<ul class="items"><li>\n<p><span class="dot done"></span>squeezed</p>\n</li></ul>'), ['squeezed'])

    @unittest.skipUnless(importlib.util.find_spec('markdown'), 'python-markdown is not installed (CI has no pip step)')
    def test_sub_bullets_stay_inside_their_item(self):
        """2026-10-17: a decided item with sub-bullets (indented two spaces, as GitHub nests them) came out as top-level
        items without a dot, which the grid squeezes into the dot column; misplaced_items stopped the page from being
        built. Now two-space sub-bullets nest under their item, as an ordinary list in its text column."""
        sys.path.insert(0, str(ROOT / 'articles' / 'intentional-communities' / 'candidate' / 'tools'))
        import render_questions
        md = ('# Q\n\nLast updated today.\n\n## Decided\n\n> [!TIP]\n> Answered.\n\n- 🟢 Done now, cutting:\n'
              '  - the failing well;\n  - scarcity without money;\n- 🟢 the next item\n')
        out = render_questions.render(md)
        self.assertEqual(render_questions.misplaced_items(out), [])
        self.assertEqual(out.count('<span class="dot done"'), 3)  # the heading's dot and one per item, none for sub-bullets
        self.assertRegex(out, r'<div>(<p>)?Done now, cutting:(</p>)?\s*<ul>\s*<li>the failing well;</li>')
        self.assertRegex(out, r'<div>(<p>)?the next item')

    def test_the_questions_lint_finds_questions_hidden_under_coming_up(self):
        """Joel, 2026-10-16 23:38 UTC: "those coming up questions also not numbered with options for some reason so harder to
        asnwser. why are questions about the sections that are now finished still "coming up"..." """
        sys.path.insert(0, str(ROOT / 'articles' / 'intentional-communities' / 'candidate' / 'tools'))
        import questions_lint
        head = '# Q\n\nLast updated today. **Open questions: 1.**\n\n'
        good = (head + '## Open questions\n\n**🟣 35. A title.** What it is.\n- a) one. **My pick**\n- b) two\n\n'
                '## Decided\n\n- 🟢 done\n\n## Coming up (not a question yet)\n\n- 🔵 Section 15 next ("Who would?" is his).\n')
        self.assertEqual(questions_lint.problems(good), [])
        hidden = good.replace('- 🔵 Section 15 next', '- 🔵 Section 13, kept unless you say otherwise: the budget line')
        self.assertTrue(any('asks for an answer' in p for p in questions_lint.problems(hidden)))
        asked = good.replace('- 🔵 Section 15 next ("Who would?" is his).', '- 🔵 Should the chart change?')
        self.assertTrue(any('question mark' in p for p in questions_lint.problems(asked)))
        no_options = good.replace('- b) two\n', '')
        self.assertTrue(any('lettered options' in p for p in questions_lint.problems(no_options)))
        miscount = good.replace('Open questions: 1.', 'Open questions: 0.')
        self.assertTrue(any('header says 0' in p for p in questions_lint.problems(miscount)))

    def test_the_questions_lint_finds_a_decision_under_for_you_to_do(self):
        """Joel, 2026-10-17 02:07 UTC: "now you say for me to do (no decision needed) then ask me to make 2 decisions, emrging
        and accepting changes, funny." """
        sys.path.insert(0, str(ROOT / 'articles' / 'intentional-communities' / 'candidate' / 'tools'))
        import questions_lint
        head = '# Q\n\nLast updated today. **Open questions: 0.**\n\n## Open questions\n\nNone right now.\n\n'
        todo = '## For you to do\n\n- 🟠 Merge this turn\'s work: `gh pr merge 1`.\n\n## Decided\n\n- 🟢 done\n'
        self.assertEqual(questions_lint.problems(head + todo), [])
        claim = todo.replace('## For you to do', '## For you to do (no decision needed)')
        self.assertTrue(any('says no decision is needed' in p for p in questions_lint.problems(head + claim)))
        accept = todo.replace("- 🟠 Merge this turn's work", '- 🟠 Look over sections 13 and 14 and say "accept 13 and 14", or what to change')
        self.assertTrue(any('asks for a decision' in p for p in questions_lint.problems(head + accept)))

    def test_the_chat_check_fails_a_bare_address_and_passes_a_written_link(self):
        script = str(TOOLS / 'pangram_links_check.py')
        with tempfile.TemporaryDirectory() as d:
            bad = pathlib.Path(d) / 'bad.md'
            bad.write_text('The section reads Human: https://www.pangram.com/history/abc-3\n', encoding='utf-8')
            good = pathlib.Path(d) / 'good.md'
            good.write_text('The section reads Human: [check](https://www.pangram.com/history/abc-3). Merge: `gh pr merge 1`.\n',
                            encoding='utf-8')
            r = subprocess.run([sys.executable, script, '--chat', str(bad)], capture_output=True, text=True)
            self.assertEqual(r.returncode, 1)
            self.assertIn("can't click", r.stdout)
            r = subprocess.run([sys.executable, script, '--chat', str(good)], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stdout)
            r = subprocess.run([sys.executable, script, str(bad)], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, 'without --chat a page source may hold bare addresses; its renderer links them')

    @unittest.skipUnless(importlib.util.find_spec('markdown'), 'python-markdown is not installed (CI has no pip step)')
    def test_a_pasted_post_card_link_becomes_its_heading_with_the_link(self):
        import html_links
        md = ('I wrote separately:\n\n[Spirit and Mind Health](https://a.example/p)[\n\n## Facing the Polycrisis\n\n'
              '](https://a.example/p)[u-dont-exist.com](https://b.example/u)·15 novembre 2025\n\nNext paragraph.')
        out = html_links.join_split_links(md)
        self.assertIn('[Spirit and Mind Health](https://a.example/p)\n\n## [Facing the Polycrisis](https://a.example/p)\n\n'
                      '[u-dont-exist.com](https://b.example/u)·15 novembre 2025', out)
        import markdown
        self.assertEqual(html_links.bare_urls_in_html(markdown.markdown(out)), [])
        self.assertTrue(html_links.bare_urls_in_html(markdown.markdown(md)), 'the card as pasted shows its address as text')

    def test_the_page_check_finds_an_address_shown_as_text(self):
        import html_links
        page = ('<style>a{color:red} /* https://x.example/css */</style><p>Human (<a href="https://www.pangram.com/history/a1">'
                'https://www.pangram.com/history/a1</a>), and https://www.pangram.com/history/a2.</p>')
        self.assertEqual(html_links.bare_urls_in_html(page), ['https://www.pangram.com/history/a2'])


def test_render_in_context_link_keeps_balanced_parentheses():
    """2026-10-18 (turn 73): a Wikipedia URL like .../Jeffrey_Young_(psychologist) used to end at its first ")",
    which left a stray ")" after the link text on the review page."""
    import importlib.util
    import pathlib
    import sys
    root = pathlib.Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(root / 'tools/humanization'))
    src = (root / 'tools/humanization/render_in_context.py').read_text(encoding='utf-8')
    line = next(l for l in src.split('\n') if l.startswith('LINK = re.compile('))
    ns = {}
    exec('import re\n' + line, ns)
    text = 'therapy ([Jeffrey Young](https://en.wikipedia.org/wiki/Jeffrey_Young_(psychologist)), who developed it'
    assert ns['LINK'].findall(text) == [('Jeffrey Young', 'https://en.wikipedia.org/wiki/Jeffrey_Young_(psychologist)')]
    assert ns['LINK'].sub(r'\1', text) == 'therapy (Jeffrey Young, who developed it'


def test_owner_edit_lines_keep_heading_marks_and_links_keep_parentheses():
    """2026-10-19 (turn 74): a heading's level is checked as a whole line, and a Wikipedia URL with
    parentheses doesn't leave a stray ")" in the visible text."""
    import pathlib
    import sys
    root = pathlib.Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(root / 'tools/humanization'))
    import check_owner_edits as coe
    md = '# A\n\n## Related Clinical Work\n\nSee [Jeffrey Young](https://en.wikipedia.org/wiki/Jeffrey_Young_(psychologist)), who did it.\n'
    raw = md
    text = coe.visible(md)
    assert 'See Jeffrey Young, who did it.' in text
    ok = {'id': 'x', 'status': 'applied', 'must_have_line': ['## Related Clinical Work'], 'must_not_have_line': ['### Related Clinical Work']}
    assert coe.check_entry(ok, text, raw, coe.visible(md, quotes=False)) == []
    bad = {'id': 'y', 'status': 'applied', 'must_have_line': ['### Related Clinical Work']}
    assert coe.check_entry(bad, text, raw, coe.visible(md, quotes=False))


def test_handoff_note_applies_a_turn_and_refuses_a_miss():
    """2026-10-19 (turn 76): the handoff note's update is one step, and a step that doesn't match writes nothing."""
    import handoff_note
    note = ('# Handoff\n\nWritten (turns 59 to 75 by X); this version is from the end of turn 75 (old; #195).\n\n'
            '## START HERE\n\n- TURN 75 (old entry)\n\n## Waiting on Joel\n1. old\n\n## Next step\n1. old next\n')
    upd = {'turn': 76,
           'replace': [[r'turns 59 to \d+ by', 'turns 59 to 76 by'],
                       [r'this version is from the end of turn \d+ \([^)]*\)\.', 'this version is from the end of turn 76 (new).']],
           'insert_before': [['- TURN ', '- TURN 76 (new entry)\n  - detail']],
           'sections': {'## Waiting on Joel': '1. new'}}
    out, done = handoff_note.apply(note, upd)
    assert 'turns 59 to 76 by' in out and 'end of turn 76 (new).' in out
    assert out.index('- TURN 76') < out.index('- TURN 75')
    assert '## Waiting on Joel\n1. new\n\n## Next step\n1. old next' in out
    again, done2 = handoff_note.apply(out, {'insert_before': upd['insert_before']})
    assert again == out and done2[0].startswith('already there')
    try:
        handoff_note.apply(note, {'replace': [['no such text', 'x']]})
    except SystemExit as e:
        assert '0 matches' in str(e)
    else:
        raise AssertionError('a miss must stop the update')


def test_lane_state_sets_the_turn_date_and_fields():
    """2026-10-19 (turn 76): the checkpoint's date comes from the turn (the scratch helper kept writing 2026-10-18)."""
    import lane_state
    t = ('Updated: 2026-10-18 (turn 75). x\n\n## Current checkpoint (2026-10-18, turn 75)\n\n- **In progress:** a\n'
         '- **Next step (updated on every push, so another account can pick up here):** b\n- **Waiting on Joel:** c\n')
    out = lane_state.set_state(t, '76', '2026-10-19', ('A', 'B', 'C'))
    assert 'Updated: 2026-10-19 (turn 76).' in out and '## Current checkpoint (2026-10-19, turn 76)' in out
    assert '- **In progress:** A\n' in out and 'pick up here):** B\n' in out and '- **Waiting on Joel:** C\n' in out


def test_review_rows_takes_the_install_note_and_his_paragraph():
    """2026-10-19 (turn 76): one rows file makes the review map; a row's note is the comment above its paragraph."""
    import review_rows
    with tempfile.TemporaryDirectory() as d:
        adir = pathlib.Path(d)
        (adir / 'HUMANIZED-ARTICLE-SO-FAR.md').write_text(
            '# H\n\n<!-- Turn 76: one sentence added. -->\n\nBefore choosing a therapist, ask.\n', encoding='utf-8')
        (adir / 'his.md').write_text('# Joel\n\n> Before choosing a therapist, get to know them.\n>\n> Other.\n', encoding='utf-8')
        m = review_rows.build({'title': 'T', 'blocks': [{'headings': ['# H'], 'rows': [
            {'label': 'P1', 'start': 'Before choosing a therapist',
             'beside': {'label': 'Yours', 'file': 'his.md', 'start': 'Before choosing'}}]}]}, adir)
        row = m['blocks'][0]['rows'][0]
        assert row['notes'] == ['Turn 76: one sentence added.']
        assert row['beside']['text'] == 'Before choosing a therapist, get to know them.'


def test_pangram_js_reverse_tab_waits_for_every_result():
    """2026-10-19 (turn 76): tab-6 runs the batch in reverse and returns the results when all N are in."""
    import pangram_js
    fwd, rev = pangram_js.calls('2026-10-19-turn76-a', 3, 'abc123')
    base = 'https://raw.githubusercontent.com/u-dont-existDOTcom/joel-articles/abc123/articles/inner-child-therapy/tools/pangram-runs/2026-10-19-turn76-a'
    assert "window.__reverse = false" in fwd and base + ".js'" in fwd
    assert "window.__reverse = true" in rev and base + "-read.js'" in rev and '.length >= 3) break' in rev
