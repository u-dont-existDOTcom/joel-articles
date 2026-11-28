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
        # Joel's section 4 and 12 texts of 2026-10-13; J53 to J55 from his Rule Scoring Sheet answers of 2026-10-14; W88 to
        # W92 (O41, S1, S2, R2, A2) from his message of 2026-10-17 13:11, which also moved W02 ("quietly") to O42; W93 (E186,
        # "X can ... without Y") and J57 (formulaic expression) from his message of 2026-10-17 14:01 (inner child lane); J58
        # (a generic "you" or "imagine" scenario) from his community edits for Pangram 4.1, message of 2026-10-20 22:01; W94
        # (O44, "one honest action"), J59 (a saying in a form people don't say) and J60 (a vague stock phrase) from his hypnosis
        # J66 and J67 (turn 105: his notes on 97.8's d4, E256); J62 to J65 (turn 104: the tells Joel's three readers found in 97.8, which the tell panel now checks, E253);
        # message of 2026-10-21 17:56; W95 (O45, a blanket or repeated safety line) and J61 (a tidy metaphor counted as a human
        # tell) from his inner child messages of 2026-10-23 17:53 and 21:52; W96 (O43, "isn't proof of / doesn't prove") from
        # his community answers of 2026-10-24 19:52; W97 to W100 (O46 "one" for "a", O43 "proof", O47 "secretly/silently", O48
        # passive voice) and J68 (one long flow in one sound) from his hypnosis guide cards of 2026-10-30 14:35; W101 to W104
        # (O49 "the next small thing", O50 "still matters", O51 portable phrases, O52 a list asked as one question) from his
        # hypnosis guide cards of 2026-11-02; W105 to W110 (O53 to O58, phrases he cut in his Pangram history) from his history,
        # read at his invitation on 2026-11-02 18:16 UTC; W111 and W112 (O59 "the same principle extends to", O60 "not a
        # recipe") from his second account's history, read at his invitation on 2026-11-02 21:59 UTC; W113 (O61, a dose as a
        # label and its spec) from his three neuro de-armoring examples of 2026-11-03 17:48 UTC (E335); W114 and W115 (O62 a
        # curly quote mark, O63 an em dash) from his message of 2026-11-03 22:02 UTC (E337 (gut), the standard swap); W118 (O64, a
        # negation and its contrast as two sentences) from his neuro de-armoring answer of 2026-11-04 13:53 UTC (E352); W119 to
        # W121 (O65 the point waiting for the sentence's end, O66 "matters", O67 a space before "mg") from his neuro de-armoring
        # answers of 2026-11-04 18:09 UTC (E357); W116 (O46 "one ordinary") and W117 (X1 "X does not Y") from his bad trips
        # guide answers of 2026-11-03 18:59 UTC; W122 (O68, a study opened bare) from his bad trips guide answers of 2026-11-04
        # 22:14 UTC (E360); W123 (O46 again, "one" before any word and a noun: "one intense night") from his bad trips guide
        # answers of 2026-11-07 15:38 UTC; J69 (a compressed list of category words) from his bad trips guide's round-23
        # answer of 2026-11-07 22:38 UTC; W124 (O69, correction or contrast frames, two in a paragraph failing), W125 (O70,
        # "different from" twice) and J70 (a sentence that reads the way his fixes change, the read against his fixes) from his
        # bad trips guide's round-36 answer of 2026-11-12 14:45 UTC (bad-trips-2026-11-12g); W126 (O71, the action said after
        # the list or questions it serves) from his round-37 message of 2026-11-12 16:48 UTC (bad-trips-2026-11-12h); W127
        # (O72, "safe" with no how) and W128 (O73, a sign of health in a list of warning signs) from his round-38 answer of
        # 2026-11-12 18:19 UTC (bad-trips-2026-11-12i); W129 (O74, a list item that finishes its lead-in ending with a period)
        # from his message of 2026-11-13 14:15 UTC (bad-trips-2026-11-12m); W130 (O75, a past perfect where the simple past
        # does) and W131 (O76, the same abbreviation in three sentences in a row) from his round-40 tries of 2026-11-19
        # (bad-trips-2026-11-19a); J71 (a word or a pointer a reader could take two ways) from his round-41 answer of
        # 2026-11-19 15:15 UTC (bad-trips-2026-11-19b); J72 (a sentence not connected to the one before: the other
        # alternative, the next case) from his round-45 answer of 2026-11-20 18:20 UTC (bad-trips-2026-11-20h); J73 to J77
        # (a step that leaves the reader wondering why, a flat rule against a natural impulse, a don't with nothing to do,
        # said twice, advice that isn't right here) from his round-48 answer of 2026-11-21 15:57 UTC (bad-trips-2026-11-21e);
        # J78 to J81 (a short line standing alone, three of a kind or a question inside another, a sentence about the text
        # that isn't true where it stands, a label for the thing) from his romance Medium-page answers of 2026-11-22 22:24
        # UTC (romance-2026-11-22d); J82 and J83 (a pivot that points back without naming what, a run of questions) from the
        # blind test's rounds 2 and 3 and his fix of the romance flaws section, 2026-11-23 (romance-2026-11-23a to d); W132
        # (O77, "honestly") from his message of 2026-11-23 17:27 UTC (romance-2026-11-23f); J84 (a point after the story
        # that interrupts it) from his sixth-page versions of 2026-11-23 19:36 UTC (romance-2026-11-23h); W133 (O78, two
        # sentences in a row opening on "And") from his round-50 answer of 2026-11-23 19:13 UTC (bad-trips-2026-11-23d); J85
        # and J86 (the state an act needs, one brand for a medicine) from the same answer (bad-trips-2026-11-23c and e), and
        # J87 (what not to do before what to do) from his round-51 answer of 23:35 UTC (bad-trips-2026-11-23h); J88 (points
        # out of their natural order, lines the section doesn't need) from his Two Pillars fix, his seventh-page answer of
        # 2026-11-24 02:06 UTC (romance-2026-11-24a); W134 (O79, a count spelled out) and J91 to J93 (a clause a reader
        # has to reread to see what its verbs hang from, a word used in a sense readers don't bring, an exact figure for a
        # practice nobody could keep exactly) from his neuro de-armoring cards of 2026-11-27 22:59 UTC (neuro-2026-11-27s to v);
        # W135 (O80, "one" where a person writes "a") and W136 (O81, "for the thing") from his rules-audit answers of 2026-11-28
        # (cards C11 and C14); W137 (O82, "straight into") from his message of 2026-11-28 15:23 UTC
        self.assertEqual(len(ids), 230)   # W137, O82 "straight into" (Joel, 2026-11-28 15:23 UTC)
        self.assertEqual(len(set(ids)), len(ids))
        self.assertEqual(sum(t['kind'] == 'mechanical' for t in TELLS), 137)
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
                # the entry's level (rules audit 2026-11-28): a FAIL tell fails its example, a REVIEW tell never does
                if t['level'] == 'FAIL':
                    self.assertIn('verdict: FAIL', out, out[-1500:])
                elif not re.search('[\u2018\u2019\u201c\u201d\u2014]', t['example']):   # O62 and O63 fail a curly mark or a dash
                    self.assertNotIn('verdict: FAIL', out, out[-1500:])


class CurlyQuotesMatchLikeStraightOnes(unittest.TestCase):
    """Curly quotes (2026-10-11 audit): B2, B5, E41 and E138 matched only a straight apostrophe, so "That’s where…" came
    back CLEAR. The rules now read straightened text, and a flag still quotes the sentence as written."""
    STRAIGHT = ("That's where the money matters to me, since it pays for the roof. The rest of the budget is small enough "
                "to settle at any meeting in the barn.")

    def test_b5_curly_and_straight_twins_get_the_same_flags(self):
        curly = self.STRAIGHT.replace("'", chr(0x2019))   # ’
        a, b = lint(self.STRAIGHT), lint(curly)
        self.assertIn('B5', rule_ids(a))
        # the curly twin also gets O62 (E337 (gut): a curly mark is itself flagged now); every other flag is the same
        self.assertIn('O62', rule_ids(b))
        self.assertEqual(flag_labels(a), [x for x in flag_labels(b) if not x.startswith('-- O62')])
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
                ('The adult in you can answer that the class is only for finding out what the painting feels like.', 'E41'),
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


class RulesAudit20261128(unittest.TestCase):
    """Rules audit 2026-11-28 (cards C11, C14, C22, C23, C24, approved): a word or shape Joel called overused is a REVIEW for a
    reader; no count fails a draft by itself; a string tell with no words of his is a REVIEW; glosses in brackets are never
    failed; his own removals ("one ordinary", "one honest action", "if it's safe", em dashes, curly quotes, "quietly") still fail."""

    def verdict(self, text):
        return re.search(r'verdict: (\w+)', lint(text)).group(1)

    def assert_review_not_fail(self, text, rule):
        out = lint(text)
        self.assertIn(rule, rule_ids(out), out[-800:])
        self.assertIn('verdict: REVIEW', out, out[-800:])
        self.assertNotIn('verdict: FAIL', out)

    def test_proof_and_prove_are_a_review(self):
        # C11: "i think this is another high freq AI pattern to be aware of: "isn't proof of/doesn't prove""
        for s in ("Presence of one of these alone isn't proof of abuse, but if several are present, they are worth a closer look.",
                  'A bad trip does not prove that you are broken, and the barn roof is still leaking after the storm.',
                  'The feeling is not proof that the plan was wrong, and the garden needs watering in the morning.',
                  'It\'s not proof of anything, and the soup is on the stove for whoever comes by tonight.'):
            with self.subTest(s=s[:40]):
                self.assert_review_not_fail(s, 'O43')

    def test_not_y_tail_and_it_meant_something_are_a_review(self):
        self.assert_review_not_fail('The guide gives new members practical steps for their first month on the land, not just theory. '
                                    'The steps came from the founders\' own mistakes in the early years.', 'O9')
        self.assert_review_not_fail('He called it a long week, and it meant something to the whole group when the roof held up.', 'O43')

    def test_one_small_thing_is_a_review_but_one_ordinary_and_one_honest_action_still_fail(self):
        self.assert_review_not_fail('Do one small thing before the council meets, and let the rest of the list wait until spring.', 'O46')
        for s, rule in (('When the body wants to move, do one ordinary task you can clearly finish. The kettle takes four minutes.', 'O46'),
                        ('Choose one honest action for the rest of the day and leave the rest for later in the week.', 'O44')):
            with self.subTest(rule=rule):
                out = lint(s)
                self.assertIn(rule, rule_ids(out))
                self.assertIn('verdict: FAIL', out)

    def test_x_does_not_y_says_change_it_by_default(self):
        out = lint('The barn roof was patched in May. Urgency does not make a ladder safe, so we waited for the dry week.')
        self.assertIn('X1', rule_ids(out))
        self.assertIn('change it by default (Joel: "super ai"), keep it only where it is the clearest way to say it', out)
        self.assertIn('verdict: REVIEW', out)

    def test_history_cut_string_tells_are_a_review(self):
        # C23: W105 to W112 have no words of his naming a phrase and no result behind them
        for rule, s in (('O53', 'Ask them about it at the start. A good therapist or helpline won\'t mind.'),
                        ('O54', 'One more thing about telling whether it helped. Say you slept better that week.'),
                        ('O60', 'Take what helps from his retreat, not a recipe you have to follow.')):
            with self.subTest(rule=rule):
                self.assert_review_not_fail(s, rule)

    def test_no_count_fails_a_draft_by_itself(self):
        # C22: two contrast frames in a paragraph, "different" twice, three exclamations in a row, a list of three, coach phrases
        # per 100 words, a run of short paragraph endings, two instruction paragraphs
        self.assert_review_not_fail('A bad trip does not mean you are broken. It is a sign of overload rather than a verdict on you.', 'O69')
        self.assert_review_not_fail('Grief is different from guilt, and fear is different from both, so the garden takes its time.', 'O70')
        self.assert_review_not_fail('The council met in the barn. Wow! What a night! The soup was great! Then everyone went home.', 'S1')
        self.assert_review_not_fail('The council handles the budget, the water rota, and the guest rooms for visitors. It meets in the barn.', 'E125')
        coach = ('You can try this. You can also try that. You might want to start small. It helps to breathe. '
                 'You can keep going. You might notice a change. It helps to rest. You can stop anytime.')
        out = lint(coach)
        self.assertIn('E41 coach register', out)
        self.assertNotIn('HARD:', out)
        self.assertNotIn('verdict: FAIL', out)
        shorts = '\n\n'.join(['The council met in the barn after the harvest to sort out the guest policy. Midnight came and went.',
                              'Our treasurer brought the numbers from the last three years of visitors. Grim reading.',
                              'Afterward the cook made soup for everyone who stayed to finish the vote. Lentil, mostly.'])
        out = lint(shorts)
        self.assertIn('B7/B13 landings', out)
        self.assertNotIn('verdict: FAIL', out)

    def test_nothing_in_the_linter_still_prints_a_hard_line(self):
        out = lint('The council met in the barn. Midnight came and went.\n\nOur treasurer read the numbers. Grim reading.\n\nThe cook made soup. Lentil, mostly.')
        self.assertNotIn('HARD:', out)

    def test_a_gloss_in_brackets_is_never_a_failure(self):
        # C24: no bracket rule, no bracket count
        s = ('Dopamine is the neurotransmitter for motivation (by showing us what is important to pay attention to). '
             'Serotonin (the mood chemical) and cortisol (the stress hormone) get their own paragraphs further down the page.')
        self.assertEqual(self.verdict(s).strip(), 'CLEAR', lint(s)[-600:])

    def test_what_still_fails_on_his_own_words(self):
        for s, rule in (('If it\'s safe, have them stand and walk a few steps to see if they keep their balance.', 'O72'),
                        ('Somebody else is quietly paying the tax bill for the whole group every single spring.', 'O42'),
                        ('The council met in the barn \u2014 and the soup ran out before the vote.', 'O63'),
                        ('The fence isn\u2019t a wall, the barn is a promise to share the gate.', 'O62')):
            with self.subTest(rule=rule):
                out = lint(s)
                self.assertIn(rule, rule_ids(out))
                self.assertIn('verdict: FAIL', out)

    def test_one_where_a_person_writes_a_is_a_review(self):
        # C11, his note: "i often find AI using "one" where a human would use "a" ... "one time is too many" would still be "one time is too many""
        for s in ('We painted one wall that spring and the roof held up fine through the whole winter.',
                  'Pick one intense night to talk it through with the group before the harvest begins.'):
            with self.subTest(s=s[:30]):
                self.assertIn('O80', rule_ids(lint(s)))
        out = lint('We painted one wall that spring and the roof held up fine through the whole winter.')
        self.assertIn('use "a" if it reads better', out)
        self.assertIn('verdict: REVIEW', out)

    def test_one_stays_where_the_count_is_the_point(self):
        for s in ('One time is too many, and we all know it by now in this house.',
                  'Do one thing at a time and keep the water running while you work in the garden.',
                  'Take it one by one with the group over the winter months, as the council agreed.',
                  'It was the one place we all agreed to meet again after the harvest was in.',
                  'There was no one idea behind the roof, and every house had its own opinion about it.',
                  'The council asked for one more week to fix the pump before the guests arrive.',
                  'She asked for one of the loaves, or two if the baker could spare them that morning.',
                  'Each of us took one or two jars, which was more than any one house could carry home.',
                  'He waited one time, then a second time, and then he went home at last.',
                  'She said "one wall at a time" and left, so the quote is hers and not mine to change.',
                  'Pay at least one rent and more than one deposit, said the notice on the barn door.'):
            with self.subTest(s=s[:40]):
                self.assertNotIn('O80', rule_ids(lint(s)))

    def test_for_the_thing_is_a_review(self):
        # C14, his note: "and btw "for the thing" is an ai tell"
        for s in ('Nobody had the money for the thing we planned in spring, so the roof waited.',
                  'The council kept a jar on the shelf, the thing for the guests who arrive after dark.'):
            with self.subTest(s=s[:40]):
                out = lint(s)
                self.assertIn('O81', rule_ids(out))
                self.assertIn('say what the thing is', out)
                self.assertNotIn('verdict: FAIL', out)
        self.assertNotIn('O81', rule_ids(lint('The thing is that the roof leaks, and nobody wants to pay for it this year.')))
        self.assertNotIn('O81', rule_ids(lint('She said "for the thing" twice and then stopped talking at the meeting in the barn.')))

    def test_every_mechanical_entry_names_its_level(self):
        for t in TELLS:
            if t['kind'] == 'mechanical':
                with self.subTest(id=t['id']):
                    self.assertIn(t.get('level'), ('FAIL', 'REVIEW'))


if __name__ == '__main__':
    unittest.main()


class ChecksFromJoelsCorrectionsOf20261017(unittest.TestCase):
    """Joel, 2026-10-17 13:11 UTC (community sections 15 and 16): "quietly" (O42), "Do those three things" (O41), three
    exclamations in a row (S1, with S2 for the rate), "this is not the same as it" (R2), and an added "I like that." (A2).
    Each check must leave alone the cases that aren't the tell."""
    def lint_with(self, text, source=None, owner=None):
        with tempfile.TemporaryDirectory() as d:
            f = pathlib.Path(d) / 'draft.txt'
            f.write_text(text + '\n', encoding='utf-8')
            cmd = [sys.executable, str(TOOLS / 'tells_lint.py'), str(f)]
            if source is not None:
                (pathlib.Path(d) / 'source.txt').write_text(source + '\n', encoding='utf-8')
                cmd += ['--source', str(pathlib.Path(d) / 'source.txt')]
            if owner is not None:
                (pathlib.Path(d) / 'owner.txt').write_text(owner + '\n', encoding='utf-8')
                cmd += ['--owner', str(pathlib.Path(d) / 'owner.txt')]
            r = subprocess.run(cmd, capture_output=True, text=True)
            self.assertIn('verdict:', r.stdout, r.stderr[-600:])
            return r.stdout

    def test_quietly_fails_but_not_for_a_sound_or_a_movement(self):
        self.assertIn('verdict: FAIL', lint('Somebody else is quietly paying the tax bill for the whole group every single spring.'))
        for s in ('She spoke quietly so the children could sleep through the meeting in the next room.',
                  'He left quietly before the meeting ended, and nobody noticed until the soup was served.'):
            with self.subTest(s=s[:40]):
                self.assertNotIn('O42', rule_ids(lint(s)))

    def test_a_count_that_names_a_models_parts_is_content(self):
        for s in ("I've broken the model I propose down into the 4 parts shown in the diagram above, with a page for each.",
                  'The three of us took turns cooking for the whole group every night during the harvest that year.'):
            with self.subTest(s=s[:40]):
                self.assertNotIn('O41', rule_ids(lint(s)))

    def test_exclamations_inside_quotes_and_captions_are_not_the_writers(self):
        text = ('Even in Dakar, I found this graffiti on a wall: "Tolerance! Openness! Union! Happiness! Love!" And elsewhere there '
                'are murals of Sufi leaders.\n\n[caption] Graffiti in Dakar: Tolerance! Openness! Union! Happiness! Love!\n\nThe '
                'murals are everywhere, and most of them are hand painted by people from the neighborhood.')
        self.assertNotIn('S1', rule_ids(lint(text)))

    def test_two_in_a_row_is_in_range(self):
        text = ('And whether communal showers feel liberating, or make you start looking at studio apartments! No manifesto is '
                'going to tell you any of that! Look before you leap. It will really save you some time and money.')
        self.assertNotIn('S1', rule_ids(lint(text)))

    def test_a_dummy_it_and_a_kept_this_are_fine(self):
        src = 'I did not find one. That may be because records are private or cases were routed elsewhere, so I cannot claim it.'
        self.assertNotIn('R2', rule_ids(self.lint_with(
            "I couldn't find one. It's possible that records are private, or that cases were referred elsewhere, so I can't claim it.",
            source=src)))
        src2 = 'This is also the boundary problem a money-free commune has to solve, with taxes and hospital bills in money.'
        self.assertNotIn('R2', rule_ids(self.lint_with(
            'This is also the thorny boundary issue of living without money, with taxes and hospital bills still paid in money.',
            source=src2)))

    def test_an_opinion_the_published_text_holds_is_fine(self):
        src = 'Now the young people can work in the city as long as they come back for the harvest. I like that arrangement.'
        self.assertNotIn('A2', rule_ids(self.lint_with(
            'Now the young people can work in the city as long as they come back for the harvest. I like that.', source=src)))

    def test_his_own_lines_are_his(self):
        s = 'Now the young people can work in the city as long as they come back for the harvest. I like that.'
        src = 'Now the young people can work in the city as long as they come back for the harvest every year.'
        self.assertNotIn('A2', rule_ids(self.lint_with(s, source=src, owner=s)))
