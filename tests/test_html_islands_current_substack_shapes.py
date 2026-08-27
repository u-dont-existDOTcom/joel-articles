#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from importlib.machinery import SourceFileLoader
from pathlib import Path
import sys
import unittest

SOURCE_DIR = Path(__file__).resolve().parents[1] / "project-sources"
MODULE_PATH = SOURCE_DIR / "html_islands.py"
if not MODULE_PATH.is_file():
    MODULE_PATH = SOURCE_DIR / "html_islands.py.txt"
loader = SourceFileLoader("html_islands_current_substack", str(MODULE_PATH))
spec = importlib.util.spec_from_loader(loader.name, loader)
assert spec and spec.loader
html_islands = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = html_islands
spec.loader.exec_module(html_islands)


class CurrentSubstackNativeShapeTests(unittest.TestCase):
    def test_youtube_nocookie_wrapper_is_youtube(self) -> None:
        raw = (
            '<div id="youtube2-PgoN0k0_0bg" class="youtube-wrap" '
            'data-attrs="{&quot;videoId&quot;:&quot;PgoN0k0_0bg&quot;}" contenteditable="false" draggable="true">'
            '<div class="youtube-inner"><iframe src="https://www.youtube-nocookie.com/embed/PgoN0k0_0bg?rel=0"></iframe></div></div>'
        )
        self.assertEqual(html_islands.classify_object(raw), ("youtube", "rich_html"))

    def test_checkout_button_is_subscribe_before_generic_button(self) -> None:
        raw = (
            '<p class="button-wrapper" data-attrs="{&quot;url&quot;:&quot;%%checkout_url%%&quot;}" '
            'data-component-name="ButtonCreateButton" contenteditable="false" draggable="true">'
            '<a class="button primary button-wrapper" href="%%checkout_url%%"><span>Subscribe now</span></a></p>'
        )
        self.assertEqual(html_islands.classify_object(raw), ("subscribe", "rich_html_candidate"))

    def test_share_button_remains_share(self) -> None:
        raw = (
            '<p class="button-wrapper" data-attrs="{&quot;url&quot;:&quot;%%share_url%%&quot;}" '
            'data-component-name="ButtonCreateButton" contenteditable="false" draggable="true">'
            '<a class="button primary button-wrapper" href="%%share_url%%"><span>Share</span></a></p>'
        )
        self.assertEqual(html_islands.classify_object(raw), ("share", "rich_html"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
