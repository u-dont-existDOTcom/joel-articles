import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "work"
    / "romance-detector-repair-20260820"
    / "apply_pass1.py"
)
spec = importlib.util.spec_from_file_location("romance_pass1", MODULE_PATH)
assert spec and spec.loader
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class RomancePass1MaterializerTests(unittest.TestCase):
    def test_replacement_counts_are_frozen(self):
        self.assertEqual(len(mod.PART1_REPLACEMENTS), 1)
        self.assertEqual(len(mod.PART2_REPLACEMENTS), 7)
        self.assertEqual(len(mod.MASTER_REPLACEMENTS), 8)

    def test_replacement_fails_closed_on_zero_or_duplicate_source(self):
        label, old, new = mod.PART1_REPLACEMENTS[0]
        with self.assertRaises(RuntimeError):
            mod.apply_replacements("unrelated", [(label, old, new)])
        with self.assertRaises(RuntimeError):
            mod.apply_replacements(old + "\n" + old, [(label, old, new)])
        changed, audit = mod.apply_replacements(old, [(label, old, new)])
        self.assertEqual(changed, new)
        self.assertEqual(audit[0]["source_occurrences"], 1)

    def test_master_muses_variant_preserves_markdown_italics(self):
        triples = {label: (old, new) for label, old, new in mod.MASTER_REPLACEMENTS}
        old, new = triples["muses-directors-lived-thought"]
        self.assertIn("*Men Are from Mars, Women Are from Venus*", old)
        self.assertIn("*Men Are from Mars, Women Are from Venus*", new)

    def test_invariant_helpers_are_not_vacuous(self):
        source = "# A\n\n[x](https://example.com)\n\n[NATIVE IMAGE — x]\n"
        self.assertEqual(mod.headings(source), ["# A"])
        self.assertEqual(mod.native_markers(source), ["[NATIVE IMAGE — x]"])
        self.assertEqual(mod.markdown_link_destinations(source), ["https://example.com"])


if __name__ == "__main__":
    unittest.main()
