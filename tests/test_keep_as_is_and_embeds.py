"""Tests for tools/humanization/keep_as_is.py (E340), and the embed notes in article_images.py, file_links_check.py and
post_embeds.py (E341)."""
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import article_images  # noqa: E402
import file_links_check as flc  # noqa: E402
import keep_as_is as K  # noqa: E402
import post_embeds  # noqa: E402
import suggestion_review as R  # noqa: E402

ARTICLE = ('# Guide\n\nAs Lao Tsu might have said (if I could ever have read that whole boring Art of War book), a war with no '
           'casualties is best.\n\n“What’s a ‘boundary’?”, I might be asking. That looks like saying no.\n\n'
           '<!-- EMBED https://www.youtube.com/watch?v=JQs2watlFws : a mantra video -->\n\nIf the hook is stuck.\n')
LEDGER = {'format': K.FORMAT, 'article': 'a.md', 'keep': [
    {'id': 'K1', 'kind': 'joke', 'quote': 'As Lao Tsu might have said (if I could ever have read that whole boring Art of War book)',
     'what': 'the joke', 'joel': "that's the joke yeah you forgot", 'when': '2026-11-03', 'where': 'A2', 'basis': 'his answer'},
    {'id': 'K2', 'kind': 'voice', 'quote': '“What’s a ‘boundary’?”, I might be asking.', 'what': 'I, not you', 'joel': '',
     'when': '2026-11-03', 'where': 'A3', 'basis': 'his answer'},
    {'id': 'K3', 'kind': 'placement', 'quote': 'watch?v=JQs2watlFws', 'what': 'his video stays', 'joel': '', 'when': '2026-11-03',
     'where': 'F2', 'basis': 'his answer'}],
    'cuts': [{'id': 'X1', 'quote': 'It’s four pairs, starting with pleasure and pain', 'what': 'cut as redundant', 'joel': '',
              'when': '2026-11-03', 'where': 'P11', 'basis': 'his answer'}]}


class KeepAsIs(unittest.TestCase):
    def setUp(self):
        self.d = pathlib.Path(tempfile.mkdtemp())
        (self.d / 'a.md').write_text(ARTICLE, encoding='utf-8')
        (self.d / K.FILE).write_text(json.dumps(LEDGER, ensure_ascii=False), encoding='utf-8')
        (self.d / 'experiments').mkdir()

    def test_all_there(self):
        led = K.load(self.d / 'a.md')
        self.assertEqual(K.problems(led), [])
        self.assertEqual(K.missing(ARTICLE, led), [])
        self.assertEqual(K.back(ARTICLE, led), [])
        self.assertEqual(K.main(['check', str(self.d / 'a.md')]), 0)

    def test_quote_marks_and_links_dont_count(self):
        """His French quote marks turned English, or a link put on kept words, are still the kept words."""
        md = ARTICLE.replace('“What’s a ‘boundary’?”', '«\xa0What’s a ‘boundary’?\xa0»').replace('Art of War', '[Art of War](https://x.org)')
        self.assertEqual(K.missing(md, K.load(self.d / 'a.md')), [])

    def test_a_kept_quote_gone_or_a_cut_back_fails(self):
        md = ARTICLE.replace('As Lao Tsu', 'As Sun Tzu') + '\nIt’s four pairs, starting with pleasure and pain, and more.\n'
        md = md.replace('<!-- EMBED https://www.youtube.com/watch?v=JQs2watlFws : a mantra video -->', '')
        (self.d / 'a.md').write_text(md, encoding='utf-8')
        led = K.load(self.d / 'a.md')
        self.assertEqual([e['id'] for e in K.missing(md, led)], ['K1', 'K3'])
        self.assertEqual([e['id'] for e in K.back(md, led)], ['X1'])
        self.assertEqual(K.main(['check', str(self.d / 'a.md')]), 1)

    def test_is_kept(self):
        led = K.load(self.d / 'a.md')
        self.assertEqual([e['id'] for e in K.kept('Lao Tsu', led)], ['K1'])
        self.assertEqual(K.kept('saying no', led), [])
        self.assertEqual(K.main(['is-kept', str(self.d / 'a.md'), 'Lao Tsu']), 0)
        self.assertEqual(K.main(['is-kept', str(self.d / 'a.md'), 'saying no']), 1)

    def test_a_file_inside_the_article_folder_uses_its_ledger(self):
        self.assertEqual(K.path_for(self.d / 'experiments' / 'GUIDE-PAGE.md'), self.d / K.FILE)

    def test_ledger_problems(self):
        bad = dict(LEDGER, keep=[dict(LEDGER['keep'][0], kind='nonsense', basis='')])
        self.assertTrue(any('kind' in p for p in K.problems(bad)))
        self.assertTrue(any('basis' in p for p in K.problems(bad)))

    def test_marking_page_refuses_a_card_on_kept_words(self):
        """The turn-116 card A2 asked about the Lao Tsu joke; with the ledger, check() refuses it, and a card that puts a
        meant cut back, and lets one with keep_ack through."""
        md = ARTICLE
        bl = R.blocks(md)
        i = next(k for k, b in enumerate(bl) if 'Lao Tsu' in b['text'])
        t = bl[i]['text']
        s = t.index('Lao Tsu')
        j = next(k for k, b in enumerate(bl) if 'boundary' in b['text'])

        def card(sid, **kw):
            c = {'id': sid, 'type': 'ask', 'title': 't', 'advice': 'ask', 'question': 'q?', 'why': 'w',
                 'spans': [{'block': i, 'start': s, 'end': s + 7}]}
            c.update(kw)
            return c
        review = {'format': R.FORMAT, 'article': {'file': str(self.d / 'a.md')}, 'types': {'ask': {'label': 'Ask'}},
                  'suggestions': [card('A2'), card('A2b', keep_ack='he asked to name Sun Tzu after all'),
                                  {'id': 'P11', 'type': 'ask', 'title': 't', 'advice': 'approve', 'what': 'w', 'why': 'w',
                                   'stays': 's', 'deciding': 'd', 'spans': [{'block': j, 'start': 0, 'end': 4}],
                                   'edits': [{'block': j, 'before': bl[j]['text'],
                                              'after': bl[j]['text'] + ' It’s four pairs, starting with pleasure and pain.'}]}]}
        probs = [p for p in R.check(review, bl) if 'Joel' in p]
        self.assertTrue(any(p.startswith('A2: highlights "Lao Tsu"') for p in probs), probs)
        self.assertFalse(any(p.startswith('A2b') for p in probs))
        self.assertTrue(any(p.startswith('P11: puts back') for p in probs), probs)

    def test_a_highlight_next_to_kept_words_passes(self):
        bl = R.blocks(ARTICLE)
        j = next(k for k, b in enumerate(bl) if 'boundary' in b['text'])
        t = bl[j]['text']
        s = t.index('saying no')
        c = {'id': 'T1', 'spans': [{'block': j, 'start': s, 'end': s + 9}]}
        self.assertEqual(K.card_problems(c, [b['text'] for b in bl], K.load(self.d / 'a.md')), [])


class Embeds(unittest.TestCase):
    MD = ('Before.\n\n<!-- EMBED https://www.youtube.com/watch?v=abc : Rosey Grier, a song -->\n\n'
          '<!-- EMBED substack-audio:bc40 : a meditation -->\n\n<!-- EMBED https://x.substack.com/p/post : Post card: "A post" -->\n\n'
          '<!-- IMAGE odt:Pictures/pic.png : a chart of his -->\n\nAfter.\n')

    def test_prompts_show_what_each_is(self):
        s = article_images.show(self.MD)
        self.assertIn('[a video: Rosey Grier, a song]', s)
        self.assertIn('[an audio: a meditation]', s)
        self.assertIn('[a post card: Post card: "A post"]', s)
        self.assertIn('[an image: a chart of his]', s)
        self.assertEqual([u for u, _ in article_images.embeds(self.MD)], ['https://www.youtube.com/watch?v=abc', 'substack-audio:bc40',
                                                                          'https://x.substack.com/p/post'])

    def test_page_shows_boxes_and_his_picture(self):
        page = article_images.figure_html(self.MD, lambda u: 'data:image/png;base64,AAAA' if u.endswith('pic.png') else None)
        self.assertEqual(page.count('class="art-embed"'), 3)
        self.assertIn('<a href="https://www.youtube.com/watch?v=abc">', page)
        self.assertIn('uploaded to the post (substack-audio:bc40)', page)
        self.assertIn('<img src="data:image/png;base64,AAAA" alt="a chart of his"', page)
        self.assertIn('art-missing', article_images.figure_html(self.MD))   # no folder for his picture: a box naming it

    def test_file_links_check_counts_embeds(self):
        d = pathlib.Path(tempfile.mkdtemp())
        (d / 'a.md').write_text(self.MD, encoding='utf-8')
        (d / 'page.html').write_text(article_images.figure_html(self.MD), encoding='utf-8')
        (d / 'plain.md').write_text('Before.\n\nAfter.\n', encoding='utf-8')
        _, apics, fpics = flc.lost(str(d / 'a.md'), str(d / 'page.html'))
        self.assertEqual((apics, fpics), (4, 4))
        self.assertEqual(flc.main(['--article', str(d / 'a.md'), str(d / 'plain.md')]), 1)


POST = ('<html><link rel="canonical" href="https://x.substack.com/p/this-post"><div class="body markup">'
        '<div data-component-name="Image2ToDOM"><a href="https://substackcdn.com/image/fetch/w_1456/https%3A%2F%2Fsubstack-post-media.s3.'
        'amazonaws.com%2Fpublic%2Fimages%2F40c24f21-070c-4bc5-9333-c838b20d46dd_1122x1402.png"><img src="x"></a></div>'
        '<p>The song I subtitled:</p><div data-component-name="VideoEmbedPlayer" data-media-upload-id="f302980e-0c6a-40c5-b6db-1e89ab887e3d"></div>'
        '<p>Further down:</p><div id="youtube2-4PxC3zZ2Mus" data-attrs="{&quot;videoId&quot;:&quot;4PxC3zZ2Mus&quot;}" data-component-name="Youtube2ToDOM"></div>'
        '<p>Here\'s one example:</p><div data-component-name="DigestPostEmbed"><div class="videoEmbedPlaceholder"></div></div>'
        '<p>Next, a <a href="https://x.substack.com/p/other">link</a>.</p>'
        '<p>The meditation:</p><div data-component-name="AudioEmbedPlayer"><a href="/api/v1/audio/upload/bc40d36b-6d3d-470d-a25d-14eb7eb067fb/src"></a></div>'
        '</div></article><script>{&quot;canonical_url&quot;:&quot;https://x.substack.com/p/this-post&quot;}'
        '{&quot;canonical_url&quot;:&quot;https://x.substack.com/p/treasuring&quot;}</script></html>')


class PostEmbeds(unittest.TestCase):
    """The turn-116 card named seven of the live post's eleven embeds; the list comes from the post's HTML now."""

    def test_every_embed_with_its_id(self):
        found = post_embeds.embeds(POST)
        self.assertEqual([(k, r) for k, r, _ in found], [
            ('picture', '40c24f21-070c-4bc5-9333-c838b20d46dd_1122x1402.png'), ('video', 'f302980e-0c6a-40c5-b6db-1e89ab887e3d'),
            ('video', '4PxC3zZ2Mus'), ('post card', 'https://x.substack.com/p/treasuring'),
            ('audio', 'bc40d36b-6d3d-470d-a25d-14eb7eb067fb')])
        self.assertEqual(found[1][2], 'The song I subtitled:')

    def test_a_video_in_the_editor_html(self):
        # his pasted editor HTML has no data-component-name on a YouTube video, only class="youtube-wrap"
        editor = ('<p>Before it:</p><div class="captioned-image-container"><figure><picture><source srcset="x.png"><img '
                  'src="x.png"></picture></figure></div>'
                  '<div id="youtube2-1aBjoARwlOY" class="youtube-wrap" data-attrs="{&quot;videoId&quot;:'
                  '&quot;1aBjoARwlOY&quot;,&quot;startTime&quot;:null}" contenteditable="false"><div class="youtube-inner">'
                  '<iframe src="https://www.youtube-nocookie.com/embed/1aBjoARwlOY?rel=0"></iframe></div></div><p>After.</p>')
        self.assertEqual(post_embeds.embeds(editor), [('video', '1aBjoARwlOY', 'Before it:')])
        # the published page, which has both markers on one video, still lists it once
        both = editor.replace('class="youtube-wrap"', 'class="youtube-wrap" data-component-name="Youtube2ToDOM"')
        self.assertEqual([(k, r) for k, r, _ in post_embeds.embeds(both)], [('video', '1aBjoARwlOY')])

    def test_the_ones_the_article_has_no_note_for(self):
        md = ('<!-- IMAGE https://substack-post-media.s3.amazonaws.com/public/images/40c24f21-070c-4bc5-9333-c838b20d46dd_1122x1402.png : c -->\n'
              '<!-- EMBED https://www.youtube.com/watch?v=4PxC3zZ2Mus : v -->\n')
        self.assertEqual([r for _, r, _ in post_embeds.missing(post_embeds.embeds(POST), md)],
                         ['f302980e-0c6a-40c5-b6db-1e89ab887e3d', 'https://x.substack.com/p/treasuring', 'bc40d36b-6d3d-470d-a25d-14eb7eb067fb'])


if __name__ == '__main__':
    unittest.main()
