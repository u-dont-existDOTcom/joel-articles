import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.compile_blind_reader_packet import compile_packet


class BlindReaderPacketCompilerTests(unittest.TestCase):
    def test_exact_contiguous_windows_reconstruct_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "article.md"
            source_bytes = b"".join(f"line {i}\n".encode() for i in range(1, 8))
            source.write_bytes(source_bytes)
            expected = hashlib.sha256(source_bytes).hexdigest()
            out = root / "packet"

            manifest = compile_packet(
                source, out, expected_sha256=expected, lines_per_window=3
            )

            self.assertEqual(manifest["windowing"]["window_count"], 3)
            self.assertEqual(
                [(w["start_line"], w["end_line"]) for w in manifest["windows"]],
                [(1, 3), (4, 6), (7, 7)],
            )
            reconstructed = b"".join(
                (out / w["filename"]).read_bytes() for w in manifest["windows"]
            )
            self.assertEqual(reconstructed, source_bytes)
            self.assertEqual(
                manifest["windowing"]["reconstructed_sha256"], expected
            )

    def test_each_window_hash_matches_written_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "article.md"
            source.write_text("a\nb\nc\nd\n", encoding="utf-8")
            expected = hashlib.sha256(source.read_bytes()).hexdigest()
            out = root / "packet"
            manifest = compile_packet(
                source, out, expected_sha256=expected, lines_per_window=2
            )

            for window in manifest["windows"]:
                data = (out / window["filename"]).read_bytes()
                self.assertEqual(hashlib.sha256(data).hexdigest(), window["sha256"])
                self.assertEqual(len(data), window["byte_count"])

    def test_sha_mismatch_fails_before_creating_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "article.md"
            source.write_text("hello\n", encoding="utf-8")
            out = root / "packet"

            with self.assertRaisesRegex(ValueError, "SHA-256 mismatch"):
                compile_packet(source, out, expected_sha256="0" * 64)
            self.assertFalse(out.exists())

    def test_invalid_window_size_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "article.md"
            source.write_text("hello\n", encoding="utf-8")
            expected = hashlib.sha256(source.read_bytes()).hexdigest()

            with self.assertRaisesRegex(ValueError, "lines_per_window"):
                compile_packet(
                    source,
                    root / "packet",
                    expected_sha256=expected,
                    lines_per_window=0,
                )

    def test_manifest_is_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "article.md"
            source.write_text("α\nβ\nγ\n", encoding="utf-8")
            expected = hashlib.sha256(source.read_bytes()).hexdigest()
            out_a = root / "a"
            out_b = root / "b"

            compile_packet(source, out_a, expected_sha256=expected, lines_per_window=2)
            compile_packet(source, out_b, expected_sha256=expected, lines_per_window=2)

            # Paths differ, so normalize only the source path field before comparison.
            a = json.loads((out_a / "manifest.json").read_text(encoding="utf-8"))
            b = json.loads((out_b / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
