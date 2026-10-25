"""tools/humanization/clarity_read.py: the whole-article clarity read (Joel, 2026-10-23 16:55 UTC: "let's make sure this
kind of check is standard for articles as we write them and as we finalize before publishing in future")."""
import json
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import clarity_read as C  # noqa: E402

ARTICLE_HTML = ('<div class="body markup"><h1>One</h1><p>First paragraph about “unification” here.</p>'
                '<div class="captioned-image-container"><figure><img src="x.png"><figcaption>A caption</figcaption></figure></div>'
                '<p>https://example.substack.com/p/a-card</p><h2>Two</h2><p>' + 'Second section text. ' * 30 + '</p>'
                '<ul><li><p>An item.</p></li></ul><h2>Three</h2><p>' + 'Third section text. ' * 30 + '</p></div>')

READER = '''## 1
QUOTE: First paragraph about “unification” here.
HARD: "unification" is never explained.
SCORE: 3
PLAIN: First paragraph about "unification" (gathering the mind into one) here.

## 2
QUOTE: A sentence the reader made up.
HARD: something
SCORE: 2
PLAIN: something plainer
'''


class ClarityReadTests(unittest.TestCase):
    def test_markdown_reading_text_leaves_out_the_editors_notes(self):
        # 2026-10-24: the Inner Child guide's Markdown keeps its turn notes in HTML comments, some of them many lines long
        md = '# One\n\n<!-- Turn 9: a note\nthat runs on -->\n\nThe paragraph.\n<!-- another -->\n'
        t = C.reading_text(md, 'md')
        self.assertEqual(t.split('\n'), ['## One', 'The paragraph.'])

    def test_reading_text_keeps_headings_and_paragraphs_and_skips_images_and_cards(self):
        t = C.reading_text(ARTICLE_HTML, 'html')
        lines = t.split('\n')
        self.assertEqual(lines[0], '## One')
        self.assertIn('First paragraph about “unification” here.', lines)
        self.assertNotIn('A caption', t)
        self.assertIn('[an image]', lines)  # the reader sees that an image is there, not its caption
        self.assertNotIn('https://example.substack.com', t)
        self.assertIn('- An item.', lines)

    def test_a_line_break_inside_a_paragraph_is_a_break_for_the_reader(self):
        """2026-10-23: Nibbāna's greeting paragraph ends "it also!<br><br>But first, ..." and the reading text joined the
        two, so a reader proposed a paragraph break the post already has."""
        t = C.reading_text('<div class="body markup"><p>One, it also!<br><br>But first, two.</p><ul><li>a<br>b</li></ul></div>', 'html')
        self.assertEqual(t.split('\n'), ['One, it also!', 'But first, two.', '- a b'])

    def test_parts_start_at_headings_and_cover_everything(self):
        t = C.reading_text(ARTICLE_HTML, 'html')
        ps = C.split_parts(t, 3)
        self.assertEqual('\n'.join(ps), t)
        for p in ps[1:]:
            self.assertTrue(p.startswith('## '), p[:30])

    def test_make_collect_and_page(self):
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            art = d / 'a.html'
            art.write_text(ARTICLE_HTML, encoding='utf-8')
            out = d / 'clarity'
            C.make(art, out, parts=2, about='a test article', question='Is anything unclear?')
            brief = (out / 'BRIEF-1.txt').read_text(encoding='utf-8')
            self.assertIn('part 1 of 2 of a test article', brief)
            self.assertIn('Compression.', brief)  # Joel's examples are in every brief
            self.assertIn('no summing-up line', brief)
            (out / 'READER-1.md').write_text(READER, encoding='utf-8')
            (out / 'READER-2.md').write_text('NOTHING\n', encoding='utf-8')
            items = C.collect(out)
            self.assertEqual(len(items), 2)
            self.assertTrue(items[0]['found'])
            self.assertEqual(items[0]['heading'], 'One')
            self.assertFalse(items[1]['found'])
            # the worker's whole-article check is kept when the readers' reports are collected again
            items[1]['status'] = 'drop'
            items[1]['note'] = 'not in the article'
            (out / 'ITEMS.json').write_text(json.dumps(items), encoding='utf-8')
            items = C.collect(out)
            self.assertEqual(items[1]['status'], 'drop')
            md, n = C.page(out, title='T')
            self.assertEqual(n, 1)
            self.assertIn('### 1. One', md)
            self.assertIn('## Flagged but not counted', md)

    def test_the_readers_edit_brief_proposals_and_page(self):
        """Joel, 2026-10-23 18:13 UTC: "the clarity check for articles should also include the readability check from GPT
        that i started doing in the inner child article" (docs/CLARITY-READ.md, part 2)."""
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            art = d / 'a.html'
            art.write_text(ARTICLE_HTML, encoding='utf-8')
            out = d / 'edit'
            C.make(art, out, parts=2, about='a test article', read='edit')
            self.assertEqual(C.read_kind(out), 'edit')
            brief = (out / 'BRIEF-1.txt').read_text(encoding='utf-8')
            self.assertIn("the reader's edit", brief)
            self.assertIn('does it change what the reader should do here', brief)
            self.assertIn('What would an attentive reader still genuinely need here?', brief)
            self.assertIn('If the Love Isn', brief)  # his 91.1 answer is an example
            self.assertIn('He chose: no label', brief)  # and his 91.3
            self.assertIn('new jokes, examples, metaphors or teaching', brief)
            self.assertNotIn('PLAIN:', brief)
            (out / 'READER-1.md').write_text('''## 1
SECTION: One
QUOTE: First paragraph about “unification” here.
MOVE: heading
CHANGE: a heading, "Where It Starts", before this paragraph
WHY: a second subject starts here (question 2)
KEEPS: every sentence
''', encoding='utf-8')
            (out / 'READER-2.md').write_text('NOTHING\n', encoding='utf-8')
            items = C.collect(out)
            self.assertEqual(len(items), 1)
            self.assertEqual(items[0]['move'], 'HEADING')
            self.assertTrue(items[0]['found'])
            items[0]['my_pick'] = 'A'
            items[0]['note'] = 'checked against the whole article'
            (out / 'ITEMS.json').write_text(json.dumps(items), encoding='utf-8')
            items = C.collect(out)  # the worker's pick and note survive a second collect
            self.assertEqual(items[0]['my_pick'], 'A')
            md, n = C.page(out)
            self.assertEqual(n, 1)
            self.assertIn('### 1. One: a heading', md)
            self.assertIn('**A (my pick):** put it in.', md)
            self.assertIn('**My check:** checked against the whole article', md)

    def test_the_caveat_read_brief_cuts_and_page(self):
        """Part 3 (Joel, 2026-10-23 22:29 UTC: "obnoxious safety language and caveats"): the brief carries his examples
        and what to keep; the page strikes each cut through in its paragraph and shows the paragraph after it."""
        art = ('<div class="body markup"><h1>One</h1><p>Do the practice lying down. If nobody is in danger, take a breath '
               'or three. That might not be how it goes for everyone.</p><h2>Two</h2><p>' + 'Text. ' * 40 + '</p></div>')
        with tempfile.TemporaryDirectory() as d:
            src = pathlib.Path(d) / 'a.html'
            src.write_text(art, encoding='utf-8')
            out = pathlib.Path(d) / 'cav'
            C.make(src, out, parts=1, read='caveats')
            brief = (out / 'BRIEF-1.txt').read_text(encoding='utf-8')
            self.assertIn('extra extra ridiculous safety language', brief)
            self.assertIn('NOBODY-SUGGESTED', brief)
            self.assertIn('Getting in touch is a separate decision', brief)  # an example from his guide
            self.assertIn('a caution that changes what you do at that step', brief)  # what to keep
            self.assertIn('one front note', brief)  # how public books place safety
            self.assertEqual((out / 'KIND').read_text().strip(), 'caveats')
            (out / 'READER-1.md').write_text(
                '## 1\nSECTION: One\nQUOTE: If nobody is in danger, take a breath or three.\nKIND: BLANKET\n'
                'WHY: nobody stops to breathe while someone is in danger\nLOSES: nothing\n\n'
                '## 2\nSECTION: One\nQUOTE: That might not be how it goes for everyone.\nKIND: hedge\n'
                'WHY: his own experience\nLOSES: nothing\n', encoding='utf-8')
            items = C.collect(out)
            self.assertEqual([x['kind'] for x in items], ['BLANKET', 'HEDGE'])
            self.assertTrue(all(x['found'] for x in items))
            md, n = C.page(out)
            self.assertEqual(n, 2)
            self.assertIn('~~If nobody is in danger, take a breath or three.~~', md)
            self.assertIn('> Do the practice lying down. That might not be how it goes for everyone.', md)
            self.assertIn('> Do the practice lying down. If nobody is in danger, take a breath or three.', md)
            self.assertIn('**A (my pick):** cut it.', md)

    def test_the_repeats_read_gives_the_whole_article_and_lists_cuts_with_the_kept_place(self):
        """Part 4 (Joel, 2026-10-23 22:29 UTC: "as much as possible we should be deduplicating"): each reader reads the whole
        article and owns one part's points; each cut shows where the point is kept."""
        art = ('<div class="body markup"><h1>One</h1><p>Founders hold too much power. That is the core problem.</p>'
               '<h1>Two</h1><p>' + 'Text. ' * 40 + 'As I said, founders hold too much power.</p></div>')
        with tempfile.TemporaryDirectory() as d:
            src = pathlib.Path(d) / 'a.html'
            src.write_text(art, encoding='utf-8')
            out = pathlib.Path(d) / 'rep'
            C.make(src, out, parts=2, read='repeats')
            brief = (out / 'BRIEF-1.txt').read_text(encoding='utf-8')
            self.assertIn(str((out / 'ARTICLE.txt').resolve()), brief)  # the whole article
            self.assertIn('You own part 1 of 2', brief)
            self.assertIn('too redundant', brief)
            (out / 'READER-2.md').write_text(
                '## 1\nSECTION: Two\nQUOTE: As I said, founders hold too much power.\n'
                'KEPT: Founders hold too much power. [One]\nWHY: the same point\nLOSES: nothing\n', encoding='utf-8')
            items = C.collect(out)
            self.assertEqual(items[0]['kind'], 'REPEAT')
            self.assertEqual(items[0]['said_already'], 'Founders hold too much power. [One]')
            md, n = C.page(out)
            self.assertEqual(n, 1)
            self.assertIn('What the article says more than once', md)
            self.assertIn('~~As I said, founders hold too much power.~~', md)
            self.assertIn('**Said already:** Founders hold too much power. [One]', md)

    def test_the_pov_read_runs_the_omission_test_first_and_lists_cuts_and_points_of_view(self):
        """Part 5 (Joel, 2026-10-25 14:20 UTC: "marking wherever it looks like there's a lack of a real POV and just some
        generic portable prose/advice that should be replaced or cut"): the brief has the rule's omission test and labels and
        his examples; collect reads a reader's points of view one a line; the page strikes a cut and lists the options."""
        art = ('<div class="body markup"><h1>One</h1><p>Take a breath. Sometimes human beings need to be being, not always doing. '
               'Then go on.</p><h2>Two</h2><p>Some people find that grief gives way to warmth. ' + 'Text. ' * 40 + '</p></div>')
        with tempfile.TemporaryDirectory() as d:
            src = pathlib.Path(d) / 'a.html'
            src.write_text(art, encoding='utf-8')
            out = pathlib.Path(d) / 'pov'
            C.make(src, out, parts=1, read='pov')
            brief = (out / 'BRIEF-1.txt').read_text(encoding='utf-8')
            for want in ('omission test', 'Who cares what I want?', 'SOURCE-SUPPORTED', 'ARTICLE-HINTED', 'NEW OWNER CHOICE',
                         'You can figure that out later.', 'it\'s an objection that so many people have raised to me'):
                self.assertIn(want, brief)
            self.assertEqual((out / 'KIND').read_text().strip(), 'pov')
            (out / 'READER-1.md').write_text(
                '## 1\nSECTION: One\nQUOTE: Sometimes human beings need to be being, not always doing.\nLABEL: CUT\n'
                'MISSING: "Take a breath." already says to pause\nPOVS: none\nPICK: delete\nQUESTION: none\n\n'
                '## 2\nSECTION: Two\nQUOTE: Some people find that grief gives way to warmth.\nLABEL: ACTUAL POV REQUIRED\n'
                "MISSING: nobody's case behind it\nPOVS:\n- ARTICLE-HINTED: the warmth line hints at a moment\n"
                '- NEW OWNER CHOICE: has grief turned into warmth for you,\n  and when?\nPICK: his moment\n'
                'QUESTION: Has grief turned into warmth for you?\n', encoding='utf-8')
            items = C.collect(out)
            self.assertEqual([x['label'] for x in items], ['CUT', 'POV'])
            self.assertEqual(items[0]['povs'], [])
            self.assertEqual(items[0]['question'], '')
            self.assertEqual(len(items[1]['povs']), 2)
            self.assertTrue(items[1]['povs'][1].startswith('NEW OWNER CHOICE') and items[1]['povs'][1].endswith('and when?'))
            md, n = C.page(out)
            self.assertEqual(n, 2)
            self.assertIn('OVERCLOSURE / CUT CANDIDATE', md)
            self.assertIn('~~Sometimes human beings need to be being, not always doing.~~', md)
            self.assertIn('> Take a breath. Then go on.', md)
            self.assertIn('ACTUAL POV REQUIRED', md)
            self.assertIn('- ARTICLE-HINTED: the warmth line hints at a moment', md)
            self.assertIn('**Question for you:** Has grief turned into warmth for you?', md)

    def test_every_brief_says_to_work_quickly(self):
        """E262: the reader of the hypnosis guide's first part ran out of output deliberating; every kind of brief now says
        to work quickly, as the edit and repeats briefs did."""
        with tempfile.TemporaryDirectory() as d:
            src = pathlib.Path(d) / 'a.html'
            src.write_text(ARTICLE_HTML, encoding='utf-8')
            for kind in ('clarity', 'edit', 'caveats', 'repeats', 'pov'):
                out = pathlib.Path(d) / kind
                C.make(src, out, parts=1, read=kind)
                self.assertIn('Work quickly', (out / 'BRIEF-1.txt').read_text(encoding='utf-8'), kind)

    def test_a_cut_flagged_twice_is_listed_once_and_numbers_follow_the_page(self):
        """2026-10-25: 48 of the hypnosis guide's 295 items were the same words twice, or on two lists. "status": "dup" lists
        one at the end with where it is offered, and numbers() gives each offered item its number on the page."""
        art = ('<div class="body markup"><h1>One</h1><p>Founders hold too much power. That is the core problem.</p>'
               '<h1>Two</h1><p>' + 'Text. ' * 40 + 'As I said, founders hold too much power.</p></div>')
        with tempfile.TemporaryDirectory() as d:
            src = pathlib.Path(d) / 'a.html'
            src.write_text(art, encoding='utf-8')
            out = pathlib.Path(d) / 'rep'
            C.make(src, out, parts=2, read='repeats')
            report = ('## 1\nSECTION: Two\nQUOTE: As I said, founders hold too much power.\n'
                      'KEPT: Founders hold too much power. [One]\nWHY: the same point\nLOSES: nothing\n\n'
                      '## 2\nSECTION: One\nQUOTE: That is the core problem.\n'
                      'KEPT: Founders hold too much power. [One]\nWHY: says it again\nLOSES: nothing\n')
            (out / 'READER-1.md').write_text(report, encoding='utf-8')
            (out / 'READER-2.md').write_text(report.split('\n\n')[0] + '\n', encoding='utf-8')
            items = C.collect(out)
            self.assertEqual([x['key'] for x in items], ['1.1', '1.2', '2.1'])
            items[2]['status'], items[2]['note'] = 'dup', 'Same cut as 18.2.'
            (out / 'ITEMS.json').write_text(json.dumps(items), encoding='utf-8')
            self.assertEqual(C.numbers(items), {'1.2': 1, '1.1': 2})  # in the article's order
            md, n = C.page(out)
            self.assertEqual(n, 2)
            self.assertIn('## Flagged twice, or offered on another list', md)
            self.assertIn('(Same cut as 18.2.)', md)
            self.assertEqual(md.count('~~As I said, founders hold too much power.~~'), 1)

    def test_the_after_shows_the_cut_made(self):
        """Joel, 2026-10-24 19:52 UTC (64.14): "instead of telling me "the sentence then starts with.." you actually make
        that change in the "after" version". A cut that takes a sentence's first words leaves its capital; a dash or comma
        left before the end goes with the cut."""
        line = ('Most of them almost never discuss the suttas – though the suttas can also be read with bias. The map '
                'helped. Community’s not a panacea, but community can make a difference.')
        self.assertEqual(C.cut_text(line, 'though the suttas can also be read with bias'),
                         'Most of them almost never discuss the suttas. The map helped. Community’s not a panacea, but '
                         'community can make a difference.')
        self.assertEqual(C.cut_text(line, 'Community’s not a panacea, but '),
                         'Most of them almost never discuss the suttas – though the suttas can also be read with bias. The '
                         'map helped. Community can make a difference.')
        self.assertEqual(C.cut_text('It matters, but that’s something which varies a lot in every society also.',
                                    'but that’s something which varies a lot in every society also'), 'It matters.')
        self.assertEqual(C.cut_text('Whether you call it that or not, “loneliness” is real.', 'Whether you call it that or not, '),
                         '“Loneliness” is real.')
        self.assertEqual(C.cut_text('One (an aside) two.', '(an aside)'), 'One two.')
        self.assertEqual(C.cut_text('All of it.', 'All of it.'), '')
        struck, after = C.cut_paragraph('## H\nWhy not? This doesn’t mean you’re doomed, it just means you need a step.',
                                        'This doesn’t mean you’re doomed, it just means ')
        self.assertEqual(after, 'Why not? You need a step.')

    def test_a_clarity_read_dir_without_kind_is_a_clarity_read(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(C.read_kind(d), 'clarity')

    def test_a_quote_is_found_when_only_its_quote_marks_differ(self):
        self.assertEqual(C.locate('## H\nHe said "yes" there.', 'He said “yes” there.'), (2, 'H'))
        self.assertIsNone(C.locate('## H\nx\nx', 'x'))


if __name__ == '__main__':
    unittest.main()
