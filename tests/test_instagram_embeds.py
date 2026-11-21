"""Tests for the Instagram embeds in tools/humanization/post_embeds.py and instagram_alive.js (lesson embeds-2026-11-21a)."""
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import post_embeds  # noqa: E402

# The published page: an empty div whose data-attrs hold the id and Substack's saved snapshot image.
PUBLISHED = ('<div class="body markup"><p>Before it:</p><div class="instagram-embed-wrap" data-attrs="{&quot;instagram_id&quot;:'
             '&quot;DQ_V5uZje4f&quot;,&quot;title&quot;:&quot;@cerebral_liberty on Instagram&quot;,&quot;thumbnail_url&quot;:'
             '&quot;https://substack-post-media.s3.amazonaws.com/public/images/__ss-rehost__IG-snapshot-DQ_V5uZje4f.jpg&quot;,'
             '&quot;belowTheFold&quot;:true}" data-component-name="InstagramToDOM"></div><p>After.</p>%s</div></article>')
# His pasted editor HTML (2026-11-21): the node view and Substack's frame, the id only inside its data: address.
EDITOR = ('<p>Before the video:</p><div class="react-renderer node-instagram" contenteditable="false" draggable="true">'
          '<div class="instagram-embed-wrap" data-drag-handle="" data-node-view-wrapper="" style="white-space: normal;">'
          '<iframe class="instagram-embed-frame" src="data:text/html;charset=utf-8,%3C!doctype%20html%3E%0A%3Cblockquote%0A'
          '%20class%3D%22instagram-media%22%0A%20data-instgrm-permalink%3D%22https%3A%2F%2Fwww.instagram.com%2Fp%2F'
          'DfZHKYpRzuG%2F%3Futm_source%3Dig_embed%26utm_campaign%3Dloading%22%3E%3C%2Fblockquote%3E" title="Instagram post">'
          '</iframe></div></div><p>After.</p>')


class InstagramEmbeds(unittest.TestCase):
    """Instagram embeds were missing from post_embeds.py; three of Joel's 18 were dead on 2026-11-21."""

    def test_published_embed_with_its_id(self):
        self.assertEqual(post_embeds.embeds(PUBLISHED % ''), [('instagram', 'DQ_V5uZje4f', 'Before it:')])

    def test_editor_html_lists_the_embed_once(self):
        # the node view and the frame inside it are two markers of one embed
        self.assertEqual(post_embeds.embeds(EDITOR), [('instagram', 'DfZHKYpRzuG', 'Before the video:')])

    def test_the_line_for_the_live_check(self):
        found = post_embeds.embeds(PUBLISHED % EDITOR)
        self.assertEqual(post_embeds.instagram_call(found), 'await instagramAlive(["DQ_V5uZje4f", "DfZHKYpRzuG"])')
        self.assertEqual(post_embeds.instagram_call([('video', '4PxC3zZ2Mus', '')]), 'no Instagram embeds')

    def test_the_live_check_reads_as_a_signed_out_reader(self):
        js = (ROOT / 'tools' / 'humanization' / 'instagram_alive.js').read_text(encoding='utf-8')
        for needed in ("credentials: 'omit'", 'EmbedBrokenMedia', 'EmbeddedMedia', '/embed/captioned/',
                       'async function instagramAlive'):
            self.assertIn(needed, js)


if __name__ == '__main__':
    unittest.main()
