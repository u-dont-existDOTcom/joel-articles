"""The written tells and the linter agree (2026-10-11). Joel: "you mention that boring and quietly were in the tells list, but
never checked? why is that? can we debug that? any time something is not executing as intended it should be debugged."
tools/humanization/tells_registry.json holds every tell the five documents name; these tests hold it to the documents and
to tells_lint.py (tools/humanization/TELLS-COVERAGE-20261011.md is the audit that found the gaps)."""
import importlib.util
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
# The linter's parsed O6 check loads spaCy, a second or two per run; the word list is enough here.
os.environ['TELLS_LINT_PARSE'] = '0'
TOOLS = ROOT / 'tools' / 'humanization'
sys.path.insert(0, str(TOOLS))

REGISTRY = json.loads((TOOLS / 'tells_registry.json').read_text(encoding='utf-8'))
TELLS = REGISTRY['tells']
IMPORT_NAMES = {'pyspellchecker': 'spellchecker'}   # the "requires" package and the module it installs


def straightened(t):
    """Whitespace collapsed and curly quotes made straight: how a quote is matched against its file."""
    t = t.translate({0x2019: "'", 0x2018: "'", 0x201C: '"', 0x201D: '"'})   # ’ ‘ “ ”
    return re.sub(r'\s+', ' ', t)


def lint(text, source=None):
    with tempfile.TemporaryDirectory() as d:
        f = pathlib.Path(d) / 'draft.txt'
        f.write_text(text + '\n', encoding='utf-8')
        cmd = [sys.executable, str(TOOLS / 'tells_lint.py'), str(f)]
        if source is not None:
            s = pathlib.Path(d) / 'source.txt'
            s.write_text(source + '\n', encoding='utf-8')
            cmd += ['--source', str(s)]
        r = subprocess.run(cmd, capture_output=True, text=True)
        assert 'verdict:' in r.stdout, r.stderr[-600:]   # a crash prints nothing, which no rule check would notice
        return r.stdout


def rule_ids(out):
    """The rule IDs on the report's flag lines ("-- B4/E15 list…") and hard-fail lines ("  HARD: B7/B13 landings…")."""
    ids = set()
    for line in out.split('\n'):
        m = re.match(r'^(?:-- |  HARD: )(\S+)', line)
        if m:
            ids |= set(m.group(1).split('/'))
    return ids


def flag_labels(out):
    return sorted(line for line in out.split('\n') if line.startswith('-- ') or line.startswith('  HARD: '))


class RegistryShape(unittest.TestCase):
    def test_one_entry_per_tell(self):
        ids = [t['id'] for t in TELLS]
        # 131 and 82 from the 2026-10-11 audit; W83 (O38) and J50 from Joel's message of 2026-10-11 18:35; J51 from 23:12;
        # W84 (O39) from 2026-10-12 05:33; W85 (O40) and J52 from 17:23; W86 and W87 (B5's two announcing openers) from
        # Joel's section 4 and 12 texts of 2026-10-13; J53 to J55 from his Rule Scoring Sheet answers of 2026-10-14; W88 (E186,
        # "X can ... without Y") and J57 (formulaic expression) from his message of 2026-10-17 14:01
        self.assertEqual(len(ids), 145)
        self.assertEqual(len(set(ids)), len(ids))
        self.assertEqual(sum(t['kind'] == 'mechanical' for t in TELLS), 88)
        for t in TELLS:
            with self.subTest(id=t['id']):
                self.assertIn(t['kind'], ('mechanical', 'judgment'))
                self.assertTrue(t['tell'] and t['sources'])
                if t['kind'] == 'mechanical':
                    self.assertTrue(t.get('rule') and t.get('example'))
                else:
                    self.assertTrue(t.get('reason'))
                    self.assertNotIn('rule', t)


class RegistryAgreesWithTheDocuments(unittest.TestCase):
    def test_each_quote_is_in_its_file(self):
        cache = {}
        for t in TELLS:
            for src in t['sources']:
                with self.subTest(id=t['id'], file=src['file']):
                    path = ROOT / src['file']
                    self.assertTrue(path.is_file(), src['file'])
                    if src['file'] not in cache:
                        cache[src['file']] = straightened(path.read_text(encoding='utf-8'))
                    self.assertIn(straightened(src['quote']), cache[src['file']])


class RegistryAgreesWithTheLinter(unittest.TestCase):
    def test_each_rule_exists_in_the_linter(self):
        src = (TOOLS / 'tells_lint.py').read_text(encoding='utf-8')
        for t in TELLS:
            if t['kind'] == 'mechanical':
                with self.subTest(id=t['id'], rule=t['rule']):
                    self.assertRegex(src, r'\b' + re.escape(t['rule']) + r'\b')

    def test_each_mechanical_example_gets_its_rule(self):
        for t in TELLS:
            if t['kind'] != 'mechanical':
                continue
            with self.subTest(id=t['id'], rule=t['rule']):
                need = t.get('requires')
                if need and importlib.util.find_spec(IMPORT_NAMES.get(need, need)) is None:
                    self.skipTest(f'{need} is not installed')
                out = lint(t['example'], t.get('source_text'))
                self.assertIn(t['rule'], rule_ids(out), out[-1500:])


class CurlyQuotesMatchLikeStraightOnes(unittest.TestCase):
    """Curly quotes (2026-10-11 audit): B2, B5, E41 and E138 matched only a straight apostrophe, so "That’s where…" came
    back CLEAR. The rules now read straightened text, and a flag still quotes the sentence as written."""
    STRAIGHT = ("That's where the money matters to me, since it pays for the roof. The rest of the budget is small enough "
                "to settle at any meeting in the barn.")

    def test_b5_curly_and_straight_twins_get_the_same_flags(self):
        curly = self.STRAIGHT.replace("'", chr(0x2019))   # ’
        a, b = lint(self.STRAIGHT), lint(curly)
        self.assertIn('B5', rule_ids(a))
        self.assertEqual(flag_labels(a), flag_labels(b))
        self.assertIn('* That’s where the money matters to me', b)   # his characters, not the straightened copy

    def test_the_other_rules_read_curly_quotes_too(self):
        for s, rule in (('The fence isn’t a wall, it’s a promise to share the gate with the neighbors.', 'B2'),
                        ('You’ll want to store the loaves down in the cellar during the summer months.', 'E41'),
                        ('I’d be tempted to fix the pump myself before calling anyone out to the farm.', 'E138')):
            with self.subTest(rule=rule):
                self.assertIn(rule, rule_ids(lint(s)))


class NewChecksStaySpecific(unittest.TestCase):
    """Cases the new checks must leave alone, found by running them on the calibration texts and the community article."""
    def test_cases_that_are_not_the_tell(self):
        for text, rule in (
                ('It was not until 1987 that the mill closed for good. It was a sad day for the whole valley.', 'B11'),
                ('That isn\'t a failure, though checking it off doesn\'t prove it helped. That\'s the question again.', 'B11'),
                ("That's fine. But we still need a second pump before the summer comes around again.", 'O2'),
                ('She said "I care about you" and then left the room without another word to anyone.', 'O22'),
                ('Even the treasurer laughed at the joke, and nobody expected that from him at the meeting.', 'O25'),
                ('A plain arrow → in a sentence is not an emoji, and neither is a check mark ✓ in a list.', 'O26'),
                ('The garden came in strong this year \U0001F970 and the tomatoes kept going into October.', 'O26'),
                ('The council met in the barn after the harvest  \nand the treasurer read the numbers to everyone who came.', 'O27'),
                ('Say you comfort your little one at night. Your little one may cry. Then hold your little one close.', 'O30')):
            with self.subTest(rule=rule, text=text[:50]):
                self.assertNotIn(rule, rule_ids(lint(text)))

    def test_rough_edges_are_mine_only(self):
        """O27 (JOEL-FIXES-CATALOGUE: "Rough edges he leaves ... They aren't something for me to imitate."): never on --owner lines."""
        text = 'The council met in the barn.  The treasurer read the numbers aloud to everyone who came that night'
        self.assertIn('O27', rule_ids(lint(text)))
        with tempfile.TemporaryDirectory() as d:
            f, o = pathlib.Path(d) / 'draft.txt', pathlib.Path(d) / 'owner.txt'
            f.write_text(text + '\n', encoding='utf-8')
            o.write_text(text + '\n', encoding='utf-8')
            r = subprocess.run([sys.executable, str(TOOLS / 'tells_lint.py'), str(f), '--owner', str(o)], capture_output=True, text=True)
        self.assertIn('verdict:', r.stdout, r.stderr[-600:])
        self.assertNotIn('O27', rule_ids(r.stdout))


class RedundantPrerequisite(unittest.TestCase):
    """O38 (Joel, 2026-10-11 18:35): "you can't say "required as pre-reqs" that's redundant, just say "when things are pre-reqs"".
    The family fails in my text; his "are pre-reqs" and a prerequisite that isn't called required again are left alone."""
    def test_the_family_fails(self):
        for s in ('And when things are required as pre-reqs for people to get medicine, it can put power in the hands of the gatekeepers.',
                  'And when pre-reqs are required for people to get medicine, it can put power in the hands of the gatekeepers.',
                  'A necessary prerequisite for joining is a season of visiting the farm and helping out in the kitchen.',
                  'The prerequisites required for membership are written on the board by the barn door every spring.'):
            with self.subTest(s=s[:50]):
                out = lint(s)
                self.assertIn('O38', rule_ids(out))
                self.assertIn('verdict: FAIL', out)

    def test_what_isnt_the_tell(self):
        for s in ('And when communal therapy processes are pre-reqs for people to get medicine, it can feel like gatekeeping.',
                  'Nobody has to take medicine, and the prerequisites for it are a ceremony rule the community holds.',
                  'She said "it\'s required as a pre-req" and then laughed about the paperwork for a while with the others.'):
            with self.subTest(s=s[:50]):
                self.assertNotIn('O38', rule_ids(lint(s)))

    def test_his_lines_arent_flagged(self):
        text = 'And when things are required as pre-reqs for people to get medicine, the circle holds a lot of power.'
        with tempfile.TemporaryDirectory() as d:
            f, o = pathlib.Path(d) / 'draft.txt', pathlib.Path(d) / 'owner.txt'
            f.write_text(text + '\n', encoding='utf-8')
            o.write_text(text + '\n', encoding='utf-8')
            r = subprocess.run([sys.executable, str(TOOLS / 'tells_lint.py'), str(f), '--owner', str(o)], capture_output=True, text=True)
        self.assertIn('verdict:', r.stdout, r.stderr[-600:])
        self.assertNotIn('O38', rule_ids(r.stdout))



class TwoParentheticalsInARow(unittest.TestCase):
    """O39 (Joel, 2026-10-12 05:33): "you can't put p22 into parentheses... that's 2 parentheticals in a row...". A sentence
    wholly in parentheses fails right after another one, across a paragraph break or inside one paragraph."""
    def test_the_tell_fails(self):
        for text in ("You have a need that far outstrips your free resource right now. (This doesn't mean you're bad or doomed, "
                     "it's about timing.)\n\n(Any humane membership process should have ways of not flat-out rejecting people.)",
                     'She told us at the gate. (We had asked her twice.) (Nobody else had asked at all.)\n\nThat was the end of it.'):
            with self.subTest(text=text[:40]):
                out = lint(text)
                self.assertIn('O39', rule_ids(out))
                self.assertIn('verdict: FAIL', out)

    def test_what_isnt_the_tell(self):
        for text in ("You have a need that far outstrips your free resource right now. (This doesn't mean you're bad or doomed.)"
                     "\n\nAny humane membership process should have ways of not flat-out rejecting people who fall into these.",
                     'Mid-sentence parentheses (like these) are fine at the market, and so is one at the end. (Like this one.)'
                     '\n\nThat was the end of it for the season.',
                     '(A founding group shouldn\'t pretend it can give you those.) You want the feeling of village life, though.'):
            with self.subTest(text=text[:40]):
                self.assertNotIn('O39', rule_ids(lint(text)))

    def test_his_lines_arent_flagged(self):
        a = "(We had asked her twice about the well.)"
        b = "(Nobody else had asked her about it at all.)"
        with tempfile.TemporaryDirectory() as d:
            f, o = pathlib.Path(d) / 'draft.txt', pathlib.Path(d) / 'owner.txt'
            f.write_text(a + '\n\n' + b + '\n', encoding='utf-8')
            o.write_text(a + '\n\n' + b + '\n', encoding='utf-8')
            r = subprocess.run([sys.executable, str(TOOLS / 'tells_lint.py'), str(f), '--owner', str(o)], capture_output=True, text=True)
        self.assertIn('verdict:', r.stdout, r.stderr[-600:])
        self.assertNotIn('O39', rule_ids(r.stdout))


if __name__ == '__main__':
    unittest.main()
