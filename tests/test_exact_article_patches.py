import importlib.util,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('exact_patch',ROOT/'scripts/apply_exact_article_patches.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class ExactArticlePatches(unittest.TestCase):
 def test_unicode_roundtrip_and_wrong_source(self):
  s='<p>Héllo</p>';n='<p>Bonjour</p>'
  p={'format':'exact-anchor-patches-v1','baseline_sha256':m.sha(s),'candidate_sha256':m.sha(n),'patches':[{'id':'one','before':s,'after':n,'before_sha256':m.sha(s),'after_sha256':m.sha(n),'current_start':0}]}
  self.assertEqual(m.apply(s,p),n)
  with self.assertRaises(ValueError):m.apply(s+' ',p)
  p['patches'][0]['current_start']=1
  with self.assertRaises(ValueError):m.apply(s,p)
 def test_current_r03_reconstructs_exact_registered_master(self):
  import json
  a=ROOT/'articles/inner-signal'
  if not (a/'sync-r03/PATCHES-R03.json').exists():self.skipTest('r03 source family absent')
  self.assertEqual(m.apply((a/'source/owner-editor-20260911.html').read_text(),json.loads((a/'sync-r03/PATCHES-R03.json').read_text())),(a/'master.html').read_text())
if __name__=='__main__':unittest.main()
