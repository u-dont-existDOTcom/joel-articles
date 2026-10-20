import sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools/editorial'))
from test_editorial_gate import EditorialGateTests
class QuoteOracleRegression(unittest.TestCase):
 def test_exact_quote_uses_text_content(self):
  s=(ROOT/'project-sources/review_interface_browser_test.py.txt').read_text()
  self.assertIn('quote_shown = page.locator("#commentQuote").text_content() or ""',s)
  self.assertNotIn('quote_shown = page.locator("#commentQuote").inner_text()',s)

class WholePassageOffsetOracle(unittest.TestCase):
    def test_nested_text_uses_whole_passage_offsets(self):
        source=(Path(__file__).resolve().parents[1]/"project-sources/review_interface_browser_test.py.txt").read_text()
        self.assertIn("prefix.selectNodeContents(passage)",source)
        self.assertIn("prefix.setEnd(node, start)",source)
        self.assertIn("return {quote, start: passageStart, end: passageEnd}",source)
        self.assertNotIn("return {quote, start, end};",source)
