"""An audio upload's shared media id must not imply video transfer behavior."""
import importlib.util
import importlib.machinery
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
loader=importlib.machinery.SourceFileLoader("audio_islands",str(ROOT/"project-sources/html_islands.py.txt"))
spec=importlib.util.spec_from_loader(loader.name,loader)
mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;loader.exec_module(mod)
class NativeAudioClassification(unittest.TestCase):
 def test_audio_id_is_not_video(self):
  raw='<div class="native-audio-embed" data-attrs="{&quot;mediaUploadId&quot;:&quot;123&quot;}"><audio src="/api/v1/audio/upload/123/src"></audio></div>'
  self.assertEqual(mod.classify_object(raw),("native_audio","unverified"))
 def test_native_video_unchanged(self):
  self.assertEqual(mod.classify_object('<div class="native-video-embed" data-attrs="mediaUploadId"><video></video></div>'),("native_video","split_payload_manual_native_video_insertion"))
 def test_video_post_still_preview(self):
  self.assertEqual(mod.classify_object('<div class="digest-post-embed" data-attrs="video_upload_id"><video></video></div>'),("substack_video_post_embed","canonical_url_in_payload"))
 def test_null_video_identity_is_an_ordinary_story_card(self):
  raw='<div class="digest-post-embed" data-attrs="{&quot;video_upload_id&quot;:null,&quot;type&quot;:&quot;newsletter&quot;}"></div>'
  self.assertEqual(mod.classify_object(raw),("digest_post_embed","rich_html"))
 def test_nonempty_video_identity_without_player(self):
  raw='<div class="digest-post-embed" data-attrs="{&quot;video_upload_id&quot;:&quot;abc-123&quot;}"></div>'
  self.assertEqual(mod.classify_object(raw),("substack_video_post_embed","canonical_url_in_payload"))
 def test_image_not_reclassified(self):
  self.assertEqual(mod.classify_object('<div class="captioned-image-container"><img src="x"></div>'),("image","rich_html"))
if __name__=='__main__':unittest.main()
