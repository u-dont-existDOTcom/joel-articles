from __future__ import annotations

import hashlib
import re
import unittest
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "articles/somatic-therapies/master.html"
FRAGMENT = ROOT / "articles/somatic-therapies/experiments/R07-PROMOTION-HTML-FRAGMENT-20260824.html"
BOUNDARY = ROOT / "articles/somatic-therapies/experiments/R07-JOB2-TO-END-PANGRAM-BOUNDARY-20260824.txt"
RAW_BOUNDARY_SHA256 = "91dd31d6519e76f30831780789d9a13c2761378978d153f2cc3f602c4b5b0b87"
WITHOUT_TERMINAL_NEWLINE_SHA256 = "06d068603b3a9c0d26bd9537240550ab18ae589ea795aa6bc2f443bffb96451b"
STALE_PREFLIGHT_SHA256 = "6091db45d7ddf80f027cc591396abd75ab7b144c206e28befee86b2f5d3589ec"


class _HeadingParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._active: str | None = None
        self._parts: list[str] = []
        self.headings: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in {"h1", "h2"}:
            self._active = tag
            self._parts = []

    def handle_data(self, data: str) -> None:
        if self._active is not None:
            self._parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self._active == tag:
            text = " ".join("".join(self._parts).split())
            self.headings.append(text)
            self._active = None
            self._parts = []


def _headings(html: str) -> list[str]:
    parser = _HeadingParser()
    parser.feed(html)
    return parser.headings


def _youtube_object(html: str, video_id: str) -> str:
    start_marker = f'<div id="youtube2-{video_id}"'
    start = html.index(start_marker)
    # Current Substack YouTube island has four nested div closures after iframe.
    match = re.search(
        rf'(<div id="youtube2-{re.escape(video_id)}".*?</iframe>'
        rf'<div class="youtube-overlay"><div class="youtube-instructions">'
        rf'Double click to interact with video</div></div></div></div>)',
        html[start:],
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError(f"could not extract YouTube island {video_id}")
    return match.group(1)


def _master_scope(master: str) -> str:
    start = master.index('<h1>Job 2: Keep the Pressure Low Between Deeper Sessions</h1>')
    sky_title = master.index('Try this 10-Second Sky Hypnosis Body/Mind Hack!')
    end = master.rfind('<div class="digest-post-embed"', start, sky_title)
    if end < 0:
        raise AssertionError("could not locate Sky Hypnosis digest boundary")
    return master[start:end]


def _hrefs(html: str) -> Counter[str]:
    return Counter(re.findall(r'href="([^"]+)"', html))


class SomaticR07PromotionFragmentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.master = MASTER.read_text(encoding="utf-8")
        cls.fragment = FRAGMENT.read_text(encoding="utf-8")
        cls.master_scope = _master_scope(cls.master)

    def test_fragment_keeps_registered_heading_identity(self) -> None:
        self.assertEqual(_headings(self.fragment), _headings(self.master_scope))

    def test_brainspotting_youtube_is_byte_identical(self) -> None:
        video_id = "3lFVu4nb5oo"
        self.assertEqual(
            _youtube_object(self.fragment, video_id),
            _youtube_object(self.master_scope, video_id),
        )

    def test_emdr_youtube_is_byte_identical(self) -> None:
        video_id = "AAjkdkHlzYY"
        self.assertEqual(
            _youtube_object(self.fragment, video_id),
            _youtube_object(self.master_scope, video_id),
        )

    def test_job2_to_pre_sky_link_multiset_is_unchanged(self) -> None:
        self.assertEqual(_hrefs(self.fragment), _hrefs(self.master_scope))

    def test_fragment_stops_before_sky_native_embed(self) -> None:
        self.assertNotIn('31fbfc4c-49b6-45de-8ead-3533fbbf20e5', self.fragment)
        self.assertNotIn('b6d5d245-6ba6-4687-b835-77b289167981', self.fragment)
        self.assertNotIn('[EXISTING ', self.fragment)

    def test_r07_boundary_raw_file_sha256(self) -> None:
        raw = BOUNDARY.read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(), RAW_BOUNDARY_SHA256)

    def test_r07_boundary_without_one_terminal_newline_sha256(self) -> None:
        raw = BOUNDARY.read_bytes()
        self.assertTrue(raw.endswith(b"\n"))
        self.assertEqual(hashlib.sha256(raw[:-1]).hexdigest(), WITHOUT_TERMINAL_NEWLINE_SHA256)

    def test_stale_preflight_sha_matches_neither_frozen_byte_identity(self) -> None:
        self.assertNotEqual(STALE_PREFLIGHT_SHA256, RAW_BOUNDARY_SHA256)
        self.assertNotEqual(STALE_PREFLIGHT_SHA256, WITHOUT_TERMINAL_NEWLINE_SHA256)


if __name__ == "__main__":
    unittest.main()
