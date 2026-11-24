"""Regression: owner-feedback research pages must remain commentable."""
import importlib.util,importlib.machinery,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(name,path):
    loader=importlib.machinery.SourceFileLoader(name,str(path))
    spec=importlib.util.spec_from_loader(name,loader);mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;loader.exec_module(mod);return mod
guard=load("review_delivery_guard",ROOT/"tools/humanization/review_delivery_check.py")
gen=load("review_delivery_generator",ROOT/"project-sources/interactive_review.py.txt")
class ReviewFeedbackDeliveryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        old=gen.extract_blocks("<h2>Example</h2><p>Old wording.</p>")
        new=gen.extract_blocks("<h2>Example</h2><p>New wording.</p>")
        cls.page=gen.build_document((ROOT/"project-sources/review_interface_template.html.txt").read_text(),title="Feedback",artifact_id="test",baseline_type="original-vs-current",row_scope="all-passages",source_label="Old",new_label="New",source_filename="old.html",revised_filename="new.html",source_version="r1",new_version="r2",source_sha="a"*64,revised_sha="b"*64,rows=gen.align_blocks(old,new),export_basename="comments")
    def test_canonical_generator_passes(self):
        self.assertTrue(guard.check_review_html(self.page,2)["ok"])
    def test_static_report_rejected(self):
        self.assertFalse(guard.check_review_html("<h1>Research comparison</h1><p>A</p><p>B</p>")["ok"])
    def test_missing_comment_button_rejected(self):
        changed=self.page.replace('class="comment-btn"','class="missing-comment-btn"',1)
        self.assertNotEqual(changed,self.page)
        self.assertFalse(guard.check_review_html(changed)["ok"])
    def test_missing_textarea_rejected(self):
        self.assertFalse(guard.check_review_html(self.page.replace('id="commentText"','id="not-comment"'))["ok"])
    def test_readability_guard_required(self):
        self.assertFalse(guard.check_review_html(self.page.replace('review-form-controls-v1','missing-color-contract'))["ok"])
if __name__=="__main__":unittest.main()
