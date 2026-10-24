import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class ReviewControlsRegression(unittest.TestCase):
    def test_template_embeds_paired_control_colors(self):
        p=ROOT/"project-sources"
        css=(p/"review-form-controls.css").read_text()
        self.assertIn(css,(p/"review_interface_template.html.txt").read_text())
        for required in ("textarea,select,option,optgroup", "color-scheme:only light", "color:#1f2937", "-webkit-text-fill-color:#1f2937", "background-color:#ffffff", "caret-color:#1f2937", "input::placeholder", "select option:checked", "forced-color-adjust:auto"):
            self.assertIn(required,css)
    def test_rendered_guard_is_in_existing_browser_test(self):
        s=(ROOT/"project-sources/review_interface_browser_test.py.txt").read_text()
        self.assertIn("typed text and native control contrast",s)
        self.assertIn("check_review_control_contrast(page)",s)
        self.assertIn("color-scheme:dark !important",s)
if __name__=="__main__":unittest.main()
