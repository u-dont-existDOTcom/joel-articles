"""tools/humanization/suggestion_review.py: the whole article with every suggestion marked where it applies (Joel,
2026-10-25 14:40 UTC: "why don't you give me the full HTML guide with highlighting where you notice x,y,z type of problems
(color-coded) and your suggestion for that and then my comment box on your suggestion with approve reject reivse buttons")."""
import json
import pathlib
import re
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import clarity_read  # noqa: E402
import suggestion_review as R  # noqa: E402

MD = '''# A heading

[image 1](https://example.com/a.png)

[Subscribe now](%%checkout_url%%)

This is the first paragraph. It has a [link here](https://example.com/x) and “curly quotes”. As I said, it repeats.

## A subheading

- A list item.

Double click to interact with video

The last paragraph says something, then it says it again.
'''


def review(suggestions):
    return {'format': R.FORMAT, 'review_id': 'test-review', 'title': 'Test Review', 'intro': ['Hello.'],
            'article': {'file': 'x.md', 'sha256': 'f' * 64}, 'built': 'now',
            'types': {'caveat': {'label': 'Caveats', 'about': 'a'}, 'structure': {'label': 'Headings', 'about': 'b'}},
            'suggestions': suggestions}


class SuggestionReviewTests(unittest.TestCase):
    def setUp(self):
        self.bl = R.blocks(MD)

    def test_blocks_number_paragraphs_and_mark_native_objects(self):
        kinds = [(b['kind'], b['native'], b['pn']) for b in self.bl]
        self.assertEqual(kinds[0], ('h1', None, None))
        self.assertEqual(kinds[1][1], 'image 1')
        self.assertEqual(kinds[2][1], 'subscribe button')
        para = self.bl[3]
        self.assertEqual(para['pn'], 'P3')
        self.assertIn('link here', para['text'])
        self.assertNotIn('](', para['text'])
        self.assertEqual(self.bl[6]['native'], 'video')
        self.assertEqual(self.bl[7]['section'], 'A subheading')

    def test_a_link_whose_address_holds_brackets_keeps_them(self):
        # 2026-11-04: the guide's "[Anthony de Mello](https://en.wikipedia.org/wiki/Anthony_de_Mello_(Jesuit_priest))"
        segs = R.segments('see [Anthony de Mello](https://en.wikipedia.org/wiki/Anthony_de_Mello_(Jesuit_priest)) is it')
        self.assertEqual(''.join(x['t'] for x in segs), 'see Anthony de Mello is it')
        self.assertEqual(segs[1]['href'], 'https://en.wikipedia.org/wiki/Anthony_de_Mello_(Jesuit_priest)')

    def test_a_link_inside_emphasis_is_a_link(self):
        # 2026-11-04: "*[No Bad Parts](https://ifs-institute.com/store/419).*" showed its markup on the page
        segs = R.segments('his book *[No Bad Parts](https://ifs-institute.com/store/419).* Honor')
        self.assertEqual(''.join(x['t'] for x in segs), 'his book No Bad Parts. Honor')
        link = [x for x in segs if x['href']]
        self.assertEqual([(x['t'], x['href'], x['em']) for x in link], [('No Bad Parts', 'https://ifs-institute.com/store/419', True)])

    def test_a_quote_is_found_with_other_quote_marks_and_spacing(self):
        i, s, e = R.find_quote(self.bl, 'and "curly quotes".')
        self.assertEqual(self.bl[i]['text'][s:e], 'and “curly quotes”.')
        with self.assertRaises(ValueError):
            R.find_quote(self.bl, 'words that are not there')

    def test_a_cut_is_tidied_only_where_it_joins(self):
        line = 'Keep this , untouched. Cut me here. And the rest!'
        s = line.index('Cut me here.')
        self.assertEqual(R.cut_text(line, s, s + len('Cut me here.')), 'Keep this , untouched. And the rest!')
        line2 = 'One thing (a parenthetical) or it may be nothing!'
        s2 = line2.index(' or it may be nothing!')
        self.assertEqual(R.cut_text(line2, s2, len(line2)), 'One thing (a parenthetical)!')

    def test_check_finds_a_before_text_that_is_not_the_articles(self):
        para = self.bl[3]
        good = {'id': 'CV-1.1', 'type': 'caveat', 'title': 'A cut', 'advice': 'approve',
                'spans': [{'block': 3, 'start': para['text'].index('As I said'), 'end': len(para['text'])}],
                'edits': [{'block': 3, 'before': para['text'], 'after': para['text'].replace(' As I said, it repeats.', '')}],
                'inserts': [], 'moves': [], 'what': 'Cuts it.', 'why': 'Said already.', 'stays': 'The rest.',
                'deciding': 'Approve cuts it.'}
        self.assertEqual(R.check(review([good]), self.bl), [])
        bad = dict(good, id='CV-1.2', edits=[{'block': 3, 'before': 'not the text', 'after': 'x'}])
        self.assertTrue(any('before-text' in p for p in R.check(review([bad]), self.bl)))
        vague = dict(good, id='CV-1.3', what='')
        self.assertTrue(any('no what' in p for p in R.check(review([vague]), self.bl)))

    def test_a_teaching_card_is_never_a_hidden_leave_card(self):
        # Lesson neuro-2026-11-27f: "leave" cards are hidden until he ticks a box, so three teaching cards never showed
        # (Joel, 2026-11-27: "your cards have no card in them btw").
        para = self.bl[3]
        r = review([])
        r['types']['teach'] = {'label': 'For you to teach me', 'about': 'c'}
        card = {'id': 'W-1', 'type': 'teach', 'title': 'A paragraph', 'advice': 'leave',
                'spans': [{'block': 3, 'start': 0, 'end': len(para['text'])}], 'inserts': [], 'moves': [],
                'edits': [{'block': 3, 'before': para['text'], 'after': para['text'].replace('first', 'opening')}],
                'what': 'Says it.', 'why': 'Tries spent.', 'stays': 'The rest.', 'deciding': 'Your version.'}
        r['suggestions'] = [card]
        self.assertTrue(any('teaching card' in p for p in R.check(r, self.bl)))
        r['suggestions'] = [dict(card, advice='approve', approve_label='use mine anyway')]
        self.assertFalse(any('teaching card' in p for p in R.check(r, self.bl)))

    def test_the_page_marks_the_words_and_carries_the_cards_and_the_form_controls(self):
        para = self.bl[3]
        s = {'id': 'CV-1.1', 'type': 'caveat', 'title': 'A cut', 'advice': 'approve',
             'spans': [{'block': 3, 'start': para['text'].index('As I said'), 'end': len(para['text'])}],
             'edits': [{'block': 3, 'before': para['text'], 'after': para['text'].replace(' As I said, it repeats.', '')}],
             'inserts': [], 'moves': [], 'what': 'Cuts it.', 'why': 'Said already.', 'stays': 'The rest.',
             'deciding': 'Approve cuts it.', 'approve_label': 'cut it'}
        h = {'id': 'ST-1.1', 'type': 'structure', 'title': 'A heading', 'advice': 'leave', 'spans': [], 'edits': [],
             'inserts': [{'before': 7, 'kind': 'h2', 'text': 'A new heading', 'seq': 0}], 'moves': [],
             'what': 'Adds a heading.', 'why': 'Why.', 'stays': 'All.', 'deciding': 'Approve adds it.'}
        page = R.page(review([s, h]), MD, self.bl)
        self.assertIn('<mark class="hl t-caveat" data-s="CV-1.1">As I said, it repeats.</mark>', page)
        self.assertIn('<del>', page)
        self.assertIn('id="c-CV-1.1"', page)
        self.assertIn('Approve: cut it', page)
        self.assertIn('Approve: make this change anyway', page)   # a leave card says what approving it does
        # the fourth button names what it does and waits, hidden, until there is an answer to undo (1.11; Joel,
        # 2026-11-11 19:54 UTC: "can you durably fix this cards thing because 'not approved yet' doesn't work as a button")
        self.assertIn('<button type="button" class="dec undo" data-dec="pending" hidden>Undo my answer</button>', page)
        self.assertNotIn('data-dec="pending">Not approved yet<', page)
        self.assertIn("$$('.dec.undo', c).forEach(b => { b.hidden = st.status === 'pending'; });", page)
        self.assertIn('class="card t-structure leave"', page)
        self.assertIn('A new heading', page)
        self.assertIn('review-form-controls-v1', page)
        self.assertIn((ROOT / 'project-sources' / 'review-form-controls.css').read_text(encoding='utf-8'), page)
        self.assertIn('<a href="https://example.com/x"', page)
        self.assertIn('[video]', page)
        self.assertNotIn('Double click to interact', page)
        data = json.loads(re.search(r'<script id="review-data" type="application/json">(.*?)</script>', page, re.S).group(1))
        self.assertEqual([x['id'] for x in data['suggestions']], ['CV-1.1', 'ST-1.1'])
        self.assertNotIn('https://fonts', page)
        self.assertIn('claude:viewport-fit-sides', page)
        self.assertIn('prefers-color-scheme: dark', page)

    def test_the_hypnosis_review_builds_and_checks(self):
        """The 2026-10-25 page: every suggestion's before-text is the guide's, so the page can't show another version."""
        rj = ROOT / 'articles/inner-signal/humanize/fix-20261025/review/REVIEW.json'
        rv = json.loads(rj.read_text(encoding='utf-8'))
        md = (ROOT / rv['article']['file']).read_text(encoding='utf-8')
        bl = R.blocks(md)
        import hashlib
        if hashlib.sha256(md.encode('utf-8')).hexdigest() != rv['article']['sha256']:
            self.skipTest('the guide changed after this review was built')
        self.assertEqual(R.check(rv, bl), [])
        ids = [s['id'] for s in rv['suggestions']]
        self.assertEqual(len(ids), len(set(ids)))
        decided = [s for s in rv['suggestions'] if s.get('decided')]
        self.assertEqual([s['id'] for s in decided], ['RR-1.1'])   # his own fix of 14:40


class PasteSafeTests(unittest.TestCase):
    """E266 (Inner Child): each version on the page is clean text, so a page pasted into a chat still reads right (the
    Inner Child sheet of 2026-10-25, pasted for GPT: "I'd keep Keep", "child.child", and a cut that showed no change)."""

    def setUp(self):
        self.bl = R.blocks(MD)

    def test_the_two_sides_are_each_one_version(self):
        now, new = R.sides("I'd keep whatever you feel around them.", 'Keep what you feel around them in mind.')
        strip = lambda h: __import__('html').unescape(re.sub(r'<[^>]+>', '', h))
        self.assertEqual(strip(now), "I'd keep whatever you feel around them.")
        self.assertEqual(strip(new), 'Keep what you feel around them in mind.')
        self.assertIn('<del>', now)
        self.assertNotIn('<del>', new)
        self.assertIn('<ins>', new)
        self.assertNotIn('<ins>', now)
        # a change that only takes words out still shows: the new side is shorter, the old one has them struck
        now, new = R.sides("So I'd ask these:", 'So ask these:')
        self.assertEqual(strip(new), 'So ask these:')
        self.assertIn("I&#x27;d</del>", now)

    def test_a_whole_passage_and_a_question_card(self):
        para = self.bl[3]
        last = self.bl[7]
        whole = {'id': 'S1', 'type': 'structure', 'title': 'A new order', 'advice': 'approve',
                 'spans': [{'block': 3, 'start': 0, 'end': len(para['text'])}, {'block': 7, 'start': 0, 'end': len(last['text'])}],
                 'card_after': 7, 'edits': [{'block': 3, 'before': para['text'], 'after': last['text']},
                                            {'block': 7, 'before': last['text'], 'after': para['text']}],
                 'inserts': [], 'moves': [],
                 'reads': [{'text': last['text'], 'note': 'Moved up.'}, {'text': para['text'], 'new': [['has a ', 'link']]}],
                 'what': 'Swaps them.', 'why': 'Order.', 'stays': 'Every word.', 'deciding': 'Approve swaps them.'}
        ask = {'id': 'Q1', 'type': 'caveat', 'title': 'A question', 'advice': 'ask', 'question': 'What is it based on?',
               'why': 'See https://example.com/why.', 'spans': [{'block': 7, 'start': 0, 'end': 8}]}
        self.assertEqual(R.check(review([whole, ask]), self.bl), [])
        page = R.page(review([whole, ask]), MD, self.bl)
        self.assertIn('class="reads"', page)
        self.assertIn('has a <ins>link</ins>', page)
        self.assertIn('Moved up.', page)
        self.assertLess(page.index('id="b7"'), page.index('id="c-S1"'))   # the card sits after card_after's block
        self.assertIn('data-advice="ask"', page)
        self.assertIn('Your answer', page)
        self.assertIn('<a href="https://example.com/why"', page)
        data = json.loads(re.search(r'<script id="review-data" type="application/json">(.*?)</script>', page, re.S).group(1))
        got = {x['id']: x for x in data['suggestions']}
        self.assertEqual(got['S1']['proposed'], last['text'] + '\n\n' + para['text'])
        self.assertEqual(got['S1']['before'], para['text'] + '\n\n' + last['text'])
        self.assertEqual(got['Q1']['question'], 'What is it based on?')
        bad = dict(ask, id='Q2', edits=[{'block': 7, 'before': last['text'], 'after': 'x'}])
        self.assertTrue(any('a question changes nothing' in p for p in R.check(review([bad]), self.bl)))
        badr = dict(whole, id='S2', reads=[{'text': 'Some words.', 'new': ['not there']}])
        self.assertTrue(any('not in their reads paragraph' in p for p in R.check(review([badr]), self.bl)))

    def test_a_stretch_to_edit_and_type_colours(self):
        # 2026-10-27, Joel: "give me the editor interface so i can see and edit what needs editing": a stretch with no change
        # of mine, Keep / Edit it / Not decided yet, Edit starting from the paragraph as it is; and a type the template
        # has no colours for gets them, so its highlights show (batch 481's page had four such types and showed none)
        last = self.bl[7]
        ed = {'id': 'ED-1', 'type': 'short', 'title': 'A short line', 'advice': 'edit', 'why': 'It read Medium.',
              'reading': 'Human, Medium (0.987): https://www.pangram.com/history/0a1b2c3d-0000-4000-8000-000000000000',
              'advice_note': 'Keep it.', 'keep_label': 'keep it as it is',
              'spans': [{'block': 7, 'start': 0, 'end': 8}], 'edits': [], 'inserts': [], 'moves': []}
        rv = review([ed])
        rv['types'] = dict(rv['types'], short={'label': 'Short line', 'about': 'A short line.'})
        self.assertEqual(R.check(rv, self.bl), [])
        page = R.page(rv, MD, self.bl)
        self.assertIn('data-advice="edit"', page)
        self.assertIn('>Keep it as it is</button>', page)
        self.assertIn('>Edit it</button>', page)
        self.assertIn('.t-short{--c:', page)
        data = json.loads(re.search(r'<script id="review-data" type="application/json">(.*?)</script>', page, re.S).group(1))
        got = {x['id']: x for x in data['suggestions']}
        self.assertEqual(got['ED-1']['proposed'], last['text'])
        bad = dict(ed, id='ED-2', edits=[{'block': 7, 'before': last['text'], 'after': 'x'}])
        self.assertTrue(any('a stretch to edit changes nothing' in p for p in R.check(dict(rv, suggestions=[bad]), self.bl)))
        nospan = dict(ed, id='ED-3', spans=[])
        self.assertTrue(any('needs its spans' in p for p in R.check(dict(rv, suggestions=[nospan]), self.bl)))

    def test_a_stretch_to_edit_is_for_his_own_words_only(self):
        # gate E373, Joel 2026-11-06 17:30 UTC: "don't say 'those are your words so you need to fix it' -- your job is to do
        # the fixing", and "'my words' for an AI article, are not my words, unless those were human before we started
        # humanizing": round 10's one card asked him for his version of the guide's AI text, which he had humanized, as his
        ed = {'id': 'ED-1', 'type': 'caveat', 'title': 'A stretch', 'advice': 'edit', 'why': 'It read AI.',
              'advice_note': 'Keep it.', 'spans': [{'block': 7, 'start': 0, 'end': 8}], 'edits': [], 'inserts': [], 'moves': []}
        rv = dict(review([ed]), built='2026-11-06')
        self.assertTrue(any('only for what he wrote himself' in p for p in R.check(rv, self.bl)))
        for whose in ('his own: the paragraph he wrote into section 3 (2026-10-20)', 'he asked: "let me edit that one" (2026-11-06)'):
            self.assertEqual(R.check(dict(rv, suggestions=[dict(ed, whose=whose)]), self.bl), [])
        self.assertTrue(R.check(dict(rv, suggestions=[dict(ed, whose='his round-8 version')]), self.bl))
        # the words that handed it back: a card, a type or an introduction that calls the model's text his
        ask = {'id': 'Q1', 'type': 'caveat', 'title': 'A line', 'advice': 'ask', 'question': 'Keep it?',
               'why': 'Four of the sentences they agree on are yours.', 'spans': [{'block': 7, 'start': 0, 'end': 8}],
               'edits': [], 'inserts': [], 'moves': []}
        self.assertTrue(any('calls the text his' in p for p in R.check(dict(rv, suggestions=[ask]), self.bl)))
        self.assertEqual(R.check(dict(rv, suggestions=[dict(ask, whose='his own: his line in the intro, 2026-10-20')]), self.bl), [])
        plain = dict(ask, why='It read AI.')
        self.assertEqual(R.check(dict(rv, suggestions=[plain]), self.bl), [])
        self.assertTrue(R.check(dict(rv, suggestions=[plain], intro=['Your words read AI here.']), self.bl))
        # pages built before the rule are left as they were
        self.assertEqual(R.check(dict(rv, built='2026-11-05', suggestions=[ed]), self.bl), [])

    def test_a_pangram_card_carries_its_links(self):
        # 2026-11-02, Joel on the hypnosis guide's cards: "why are you not giving me the pangram link so i can see? always
        # give me the links", and "you didn't check if your changes passed.. they didn't. don't waste my time": a card
        # that says what Pangram read gives the result's link, and a suggestion for that stretch gives its own check's
        # link ("tested"); both show on the card, an approve card's too (1.4 showed an approve card's reading nowhere)
        last = self.bl[7]
        link = 'https://www.pangram.com/history/1050793a-1f08-47d0-aac9-098afd0e5408'
        s = {'id': 'P-1', 'type': 'caveat', 'title': 'A line', 'advice': 'approve',
             'spans': [{'block': 7, 'start': 0, 'end': 8}],
             'edits': [{'block': 7, 'before': last['text'], 'after': 'The last paragraph says something once.'}],
             'inserts': [], 'moves': [], 'what': 'Says it once.', 'why': 'It repeats.', 'stays': 'The rest.',
             'deciding': 'Approve uses it.', 'reading': 'AI (High), 27 words: [the section](%s)' % link,
             'tested': 'Human Written: [the suggestion](https://www.pangram.com/history/5ad82ada-83a8-4c4f-89f2-4f0966465f5f)'}
        self.assertEqual(R.check(review([s]), self.bl), [])
        page = R.page(review([s]), MD, self.bl)
        self.assertIn('Pangram read', page)
        self.assertIn('Pangram on the suggestion', page)
        self.assertIn('<a href="%s" target="_blank" rel="noopener noreferrer">the section</a>' % link, page)
        nolink = dict(s, id='P-2', reading='AI (High), 27 words')
        self.assertTrue(any('has no link' in p for p in R.check(review([nolink]), self.bl)))
        untested = dict(s, id='P-3')
        del untested['tested']
        self.assertTrue(any('its own Pangram check' in p for p in R.check(review([untested]), self.bl)))
        # a card with no Pangram reading (a clarity card, a question) needs neither
        plain = dict(s, id='P-4')
        del plain['reading'], plain['tested']
        self.assertEqual(R.check(review([plain]), self.bl), [])

    def test_a_new_heading_in_a_whole_passage(self):
        # turn 113: a case heading over a paragraph shows as a heading with its Markdown #s, so a paste keeps it a heading,
        # and his Revise box starts from the same text
        para = self.bl[3]
        s = {'id': 'H1', 'type': 'structure', 'title': 'Case headings', 'advice': 'approve',
             'spans': [{'block': 3, 'start': 0, 'end': len(para['text'])}], 'card_after': 3,
             'edits': [], 'inserts': [{'before': 3, 'kind': 'h4', 'text': 'If it calls this stupid', 'seq': 0}], 'moves': [],
             'reads': [{'text': 'If it calls this stupid', 'kind': 'h4', 'new': ['If it calls this stupid']}, {'text': para['text']}],
             'what': 'A heading.', 'why': 'Skimming.', 'stays': 'Every word.', 'deciding': 'Approve puts it in.'}
        self.assertEqual(R.check(review([s]), self.bl), [])
        page = R.page(review([s]), MD, self.bl)
        self.assertIn('<p class="rd rd-h rd-h4"><span class="rd-hm">#### </span><ins>If it calls this stupid</ins></p>', page)
        data = json.loads(re.search(r'<script id="review-data" type="application/json">(.*?)</script>', page, re.S).group(1))
        self.assertEqual(data['suggestions'][0]['proposed'], '#### If it calls this stupid\n\n' + para['text'])
        bad = dict(s, id='H2', reads=[{'text': 'A heading', 'kind': 'h7'}])
        self.assertTrue(any('kind must be' in p for p in R.check(review([bad]), self.bl)))


class ReaderBriefTests(unittest.TestCase):
    def test_previous_goes_to_the_card_before_and_never_wraps_to_the_bottom(self):
        # Joel, 2026-10-30: "your "pevious" button brouught me to the bottom of the page" (with every card above decided,
        # it wrapped round to the last undecided card on the page); the browser check is fix-20261030/previous-button/
        page = R.page(review([]), MD, R.blocks(MD))
        step = page[page.index('function step(dir)'):page.index("$('#nextBtn').addEventListener")]
        prev = step[step.index('// Previous'):]
        self.assertNotIn('list[list.length - 1]', prev)
        self.assertNotIn('filter(undecided)', prev)
        self.assertIn('this is the first card', prev)
        self.assertIn('title="The card before this one"', page)

    def test_card_text_links_by_name_and_keeps_line_breaks(self):
        h = R.linked('Read AI in the check (see [part A](https://www.pangram.com/feed/abc)).\nTry 1, read AI <High> at '
                     'https://example.com/x.')
        self.assertIn('<a href="https://www.pangram.com/feed/abc" target="_blank" rel="noopener noreferrer">part A</a>)', h)
        self.assertIn('<br>Try 1', h)
        self.assertIn('&lt;High&gt;', h)
        self.assertIn('<a href="https://example.com/x" target="_blank" rel="noopener noreferrer">https://example.com/x</a>.', h)
        self.assertNotIn('[part A]', h)

    def test_the_brief_says_a_referent_right_before_is_clear(self):
        """E264: the reader flagged "do that" right after "remove anything from laws of nature"; Joel, 14:40: ""do that" is
        clearly referring to "remove anything from the laws of nature" directly before it"."""
        self.assertIn('whose meaning is in the words right before it', clarity_read.BRIEF)
        self.assertIn('read the sentence before it', clarity_read.BRIEF)

    def test_the_brief_keeps_plain_versions_his_own_words(self):
        """E264: the plain version added two brackets; Joel: "it's actually harder to read now with these 2 parentheticals"."""
        self.assertIn('How to write PLAIN', clarity_read.BRIEF)
        self.assertIn('at most one per passage', clarity_read.BRIEF)
        ex = json.loads((ROOT / 'tools/humanization/clarity_examples.json').read_text(encoding='utf-8'))
        last = ex[-1] if isinstance(ex, list) else ex['examples'][-1]
        self.assertIn('redirecting the thought stream with your conscious, higher intention', json.dumps(last, ensure_ascii=False))


    def test_paragraph_labels_are_never_copied_with_the_text(self):
        """E326: Joel's checks of paragraphs copied from these pages read "P1Here is a list" and "Your inherited parent
        script P1One", and taking the labels out alone turned AI Detected 21% to 46% into Human Written (his second Pangram
        account, 2026-11-02). Every page that numbers paragraphs keeps the labels out of a copy."""
        import re
        for rel in ('tools/humanization/suggestion_review_template.html', 'tools/humanization/render_article_so_far.py',
                    'tools/humanization/render_in_context.py'):
            src = (ROOT / rel).read_text(encoding='utf-8')
            rules = re.findall(r'\.pn\s*\{+([^}]*)\}', src)
            self.assertTrue(rules, rel)
            self.assertTrue(any('user-select:none' in r.replace(' ', '') for r in rules), rel)


class ReceiptTests(unittest.TestCase):
    """Gate E365: from 2026-11-05 a card that adds or changes words carries a making-sense receipt that passes."""

    def test_a_card_with_new_words_needs_its_receipt(self):
        import tempfile, sense_receipt
        text = 'Time the seizure. Keep them on their side.'
        rv = {'built': '2026-11-05'}
        card = {'id': 'C1', 'advice': 'approve', 'edits': [{'block': 0, 'before': 'Time it.', 'after': text}]}
        self.assertTrue(R.receipt_problems(rv, card))
        self.assertEqual(R.receipt_problems(dict(rv, built='2026-11-04'), card), [])
        self.assertEqual(R.receipt_problems(rv, dict(card, owner_text="his round-6 version")), [])
        r = sense_receipt.make(text, 'Active Seizure', 'someone with a person having a seizure from MDMA, which is generalized')
        for x in r['sentences']:
            x['payoff'], x['follows'] = 'tells the helper what to do', 'the next step after the one before'
            if 'link' in x:
                x['link'] = 'none: each step is the next one the helper expects'
        r['placement'] = 'first in the section, which it opens'
        r['opens']['why_reading'] = 'the helper learns the first thing to do while the seizure is on'
        r['same_point'] = 'none: read the Active Seizure section from its heading to the next for timing and the side'
        r['needed'] = {'reader': 'a fresh reader given needed_read_brief.md', 'unneeded': [], 'kept': {}}
        r['his_fixes'] = {'reader': 'a fresh reader given his_fixes_brief.md', 'marked': [], 'kept': {}}
        r['fit'] = {'reader': 'a fresh reader given fit_read_brief.md', 'marked': [], 'kept': {}}
        r['questions'] = {q: 'PASS: said plainly' for q in sense_receipt.QUESTIONS}
        with tempfile.NamedTemporaryFile('w', suffix='.json', dir=str(R.ROOT), delete=False) as f:
            json.dump(r, f)
        try:
            rel = str(pathlib.Path(f.name).relative_to(R.ROOT))
            self.assertEqual(R.receipt_problems(rv, dict(card, receipt=rel)), [])
            other = dict(card, edits=[{'block': 0, 'before': 'x', 'after': 'Another text.'}], receipt=rel)
            self.assertTrue(R.receipt_problems(rv, other))
        finally:
            pathlib.Path(f.name).unlink()



class DoubledPercentTests(unittest.TestCase):
    """Lesson bad-trips-2026-11-24t: round 56's question showed him "(4%%)", a string never %-formatted."""

    def card(self, question):
        return {'id': 'CHLORIDE-CLAIM', 'advice': 'ask', 'type': 'ask', 'question': question, 'spans': []}

    def test_a_doubled_percent_in_a_card_or_the_intro_is_refused(self):
        rv = {'built': R.PERCENT_FROM, 'intro': ['96%% on 2026-11-11'], 'suggestions': [self.card('found magnesium oxide poorly absorbed (4%%)')]}
        probs = R.percent_problems(rv)
        self.assertEqual(len(probs), 2)
        self.assertIn('CHLORIDE-CLAIM: its question', probs[1])

    def test_a_single_percent_and_older_pages_pass(self):
        self.assertEqual(R.percent_problems({'built': R.PERCENT_FROM, 'suggestions': [self.card('poorly absorbed (4%)')]}), [])
        self.assertEqual(R.percent_problems({'built': '2026-11-24', 'suggestions': [self.card('(4%%)')]}), [])


class UnitSpaceTests(unittest.TestCase):
    """Lesson bad-trips-2026-11-23a: "don't put space between the number and the unit i told you that before"."""

    def card(self, question):
        return {'id': 'QUIZ-2', 'advice': 'ask', 'type': 'ask', 'question': question, 'spans': []}

    def test_a_card_from_today_with_12_mg_is_refused(self):
        rv = {'built': R.UNITS_FROM, 'suggestions': [self.card('S1: "I\'d give an adult 12 mg to start."')]}
        probs = R.unit_problems(rv)
        self.assertEqual(len(probs), 1)
        self.assertIn('"12 mg"', probs[0])

    def test_12mg_and_older_pages_pass(self):
        self.assertEqual(R.unit_problems({'built': R.UNITS_FROM, 'suggestions': [self.card('give an adult 12mg, then 2mg every 2 hours')]}), [])
        self.assertEqual(R.unit_problems({'built': '2026-11-22', 'suggestions': [self.card('12 mg')]}), [])

    def test_a_range_and_mcg_are_read_too(self):
        probs = R.unit_problems({'built': R.UNITS_FROM, 'suggestions': [self.card('100-200 mcg a day')]})
        self.assertEqual(len(probs), 1)


if __name__ == '__main__':
    unittest.main()

class WholePageTests(unittest.TestCase):
    """Lesson romance-2026-11-22a (Joel, 2026-11-22 22:24 UTC): "it would have helped if you just had the whole page so i
    could see the whole context, make that a rule from now on" and "make it more clear when you cut parts out (which should
    not happen unless it would take up a lot of space, like don't cut out one paragraph to save space"."""

    def setUp(self):
        import tempfile
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        paras = ['Paragraph number %d says one thing and then another thing, with enough words in it to count as a '
                 'long paragraph for the cut rule, which wants many words before it lets a stretch go. ' % k * 1
                 + 'More words follow here so each one is long. ' * 8 for k in range(12)]
        self.paras = paras
        self.whole = '# Title\n\n' + '\n\n'.join(paras[:2]) + \
            '\n\n<!-- EMBED https://www.youtube-nocookie.com/embed/pvN8QgGatew : a video -->\n\n' + \
            '\n\n'.join(paras[2:]) + '\n'
        (self.tmp / 'whole.md').write_text(self.whole, encoding='utf-8')
        import hashlib
        self.wsha = hashlib.sha256(self.whole.encode('utf-8')).hexdigest()

    def rv(self, whole=True):
        r = review([])
        r['built'] = R.WHOLE_FROM
        if whole:
            r['whole'] = {'file': str(self.tmp / 'whole.md'), 'sha256': self.wsha}
        return r

    def test_a_page_from_today_names_the_whole_article(self):
        bl = R.blocks(self.whole, whole=True)
        self.assertTrue(any('"whole"' in p for p in R.whole_problems(self.rv(whole=False), bl)))
        self.assertEqual(R.whole_problems(self.rv(), bl), [])

    def test_a_page_that_drops_a_paragraph_is_refused(self):
        page_md = self.whole.replace(self.paras[5] + '\n\n', '')
        probs = R.whole_problems(self.rv(), R.blocks(page_md, whole=True))
        self.assertTrue(any('leaves out' in p for p in probs), probs)

    def test_a_short_cut_is_refused_and_a_long_one_shows_as_a_box_that_opens(self):
        short = self.whole.replace(self.paras[5], '<!-- CUT -->\n\n' + self.paras[5] + '\n\n<!-- /CUT -->')
        probs = R.whole_problems(self.rv(), R.blocks(short, whole=True))
        self.assertTrue(any('only a long one may be' in p for p in probs), probs)
        body = '\n\n'.join(self.paras[2:11])
        long_md = self.whole.replace(body, '<!-- CUT -->\n\n' + body + '\n\n<!-- /CUT -->')
        bl = R.blocks(long_md, whole=True)
        self.assertEqual(R.whole_problems(self.rv(), bl), [])
        cut = [b for b in bl if b['kind'] == 'cut']
        self.assertEqual(len(cut), 1)
        h = R.block_html(cut[0], [])
        self.assertIn('Left out here to save space: 9 paragraphs', h)
        self.assertIn('<details', h)
        self.assertIn('Paragraph number 2 says', h)

    def test_a_video_shows_as_a_box_with_its_youtube_link(self):
        bl = R.blocks(self.whole, whole=True)
        emb = [b for b in bl if b['kind'] == 'embed']
        self.assertEqual(len(emb), 1)
        h = R.block_html(emb[0], [])
        self.assertIn('https://www.youtube.com/watch?v=pvN8QgGatew', h)
        self.assertNotIn('<iframe', h)
        # pages built before the rule keep their old blocks, so their spans still point where they did
        self.assertFalse(any(b['kind'] == 'embed' for b in R.blocks(self.whole)))
