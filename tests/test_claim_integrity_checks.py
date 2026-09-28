"""Pins the claim checks in SKILL.md.

SKILL.md's section "Claims about sources and reviews of Joel's writing" and its
independent final-reader audit carry checks on what reviews, replies, and drafts
say about sources and about Joel's writing. These are text-presence tests: they
show that the rules are in the skill file and that the section's quotations of
other project files are exact. They do not show that a model follows the rules.

Lineage, development side only: the checks are adapted from the claim-integrity
pack v1 in u-dont-existDOTcom/universal-dev-architecture, and ANCHORS uses that
pack's check IDs. Nothing here or in SKILL.md reads that repository at runtime.
"""

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
HEADING = "## Claims about sources and reviews of Joel's writing"

# One exact anchor phrase per check.
ANCHORS = {
    "CI-01": (
        "Every sentence about what a text, author, or person says, writes, "
        "describes, presents, defines, or did must rest on a specific passage."
    ),
    "CI-02": (
        "Do not join words from separate sentences inside one quotation, and do "
        "not put a paraphrase in quotation marks."
    ),
    "CI-03": (
        "search all of it for counterexamples. The claim covers only what was "
        "searched; say so when that was less than all of it."
    ),
    "CI-04": (
        "When Joel has stated expertise in the area, find a source before "
        "contradicting his usage."
    ),
    "CI-05": (
        "trace it to the source it cites, and use that source when the two "
        "differ; two figures that trace to one source are one finding."
    ),
    "CI-06": (
        "must name what was compared against which source or version; when only "
        "part was checked, name the part."
    ),
    "CI-07": (
        "When Joel disputes a claim about a source or a fact, check the source "
        "before agreeing, just as before defending."
    ),
    "CI-08": (
        "or changing the content of an existing one, check it against its source "
        "at that point, even if it was checked earlier"
    ),
    "CI-09": (
        "state the strongest reading under which it is not a problem, and drop "
        "the flag if that reading is plausible."
    ),
    "CI-10": (
        "Label estimates as estimates, and report a derived number at the "
        "resolution of its inputs"
    ),
    "CI-11": (
        "If no genuinely separate model or context is available, check every "
        "listed claim against its source immediately before delivery and "
        "describe it only as rechecked, not independently checked."
    ),
}

CI_11_CLAUSES = (
    "Before delivering a review or critique of Joel's article or a text he is answering",
    "a draft that says what a source says, a fact added to text Joel will publish, or a claim that something was verified",
    "It never applies to companion or therapeutic replies.",
    "Give the list, the draft, and the sources—but not the drafting reasoning—to a genuinely separate model or context.",
    "Ask it to pass or fail each claim with a reason and add any claim the list missed.",
)

# Clauses that keep the checks inside Joel's editorial rules.
SCOPE_CLAUSES = (
    "They do not turn an editing or humanization pass into a fact-check of Joel's own claims",
    "find out which before calling one a misquote",
    "Joel's corrections of his own meaning, memories, voice, and editorial choices remain owner authority",
    "Rewording one of Joel's own claims needs no new source check",
    "This rule covers Joel's own writing only",
    "Once Joel rejects a flag of any kind, drop it.",
)

# Rules from other project files that the section quotes word for word.
QUOTED_RULES = {
    "project-sources/FACTS-HEALTH-FORMATTING.md": (
        "Follow citation chains; do not trust a secondary characterization "
        "without checking the cited source."
    ),
    "project-sources/ARGUMENT-AND-EVIDENCE-ARCHITECTURE.md": (
        "Ten repetitions of one dependent allegation are not ten independent facts."
    ),
    "project-sources/MASTER-INSTRUCTIONS.md": (
        "Once I've heard a concern, don't repeat it in new framings."
    ),
}

# Headings the section points readers to.
POINTED_HEADINGS = {
    "SKILL.md": (
        "## Authority and recovery",
        "## Cold audit",
        "## Independent final-reader audit",
    ),
    "project-sources/FACTS-HEALTH-FORMATTING.md": ("## Verification workflow",),
    "project-sources/ARGUMENT-AND-EVIDENCE-ARCHITECTURE.md": (
        "## 7. Evaluate evidence separately and cumulatively",
        "## 7F. Source-language and negative-claim discipline",
    ),
    "project-sources/EDIT-CONTRACT-AND-LEDGERS.md": ("## Substantive change report",),
}


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def claims_section() -> str:
    text = SKILL.read_text(encoding="utf-8")
    start = text.index(HEADING)
    end = text.find("\n## ", start + len(HEADING))
    return text[start:] if end == -1 else text[start:end]


class ClaimIntegrityChecksTests(unittest.TestCase):
    def setUp(self) -> None:
        self.skill = SKILL.read_text(encoding="utf-8")
        self.skill_normalized = normalize(self.skill)
        self.section = claims_section()
        self.normalized = normalize(self.section)

    def test_skill_carries_each_check(self) -> None:
        for check_id, anchor in ANCHORS.items():
            with self.subTest(check=check_id):
                self.assertIn(normalize(anchor), self.skill_normalized)

    def test_ci_11_keeps_its_scope_and_independent_path(self) -> None:
        for clause in CI_11_CLAUSES:
            with self.subTest(clause=clause):
                self.assertIn(normalize(clause), self.skill_normalized)

    def test_section_keeps_joel_specific_scope(self) -> None:
        for clause in SCOPE_CLAUSES:
            with self.subTest(clause=clause):
                self.assertIn(normalize(clause), self.normalized)

    def test_section_is_self_contained(self) -> None:
        self.assertNotIn("universal-dev-architecture", self.section)
        self.assertIsNone(re.search(r"\bUDA\b", self.section))
        self.assertIsNone(re.search(r"\bCI-(?:\d{2}|X1)\b", self.section))
        for relative in re.findall(r"`([\w./-]+\.md)`", self.section):
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).is_file(), f"missing {relative}")

    def test_quoted_rules_are_exact(self) -> None:
        for relative, quote in QUOTED_RULES.items():
            with self.subTest(path=relative):
                self.assertIn(normalize(f"`{quote}`"), self.normalized)
                source = normalize((ROOT / relative).read_text(encoding="utf-8"))
                self.assertIn(normalize(quote), source)

    def test_pointed_headings_exist(self) -> None:
        for relative, headings in POINTED_HEADINGS.items():
            text = (ROOT / relative).read_text(encoding="utf-8")
            for heading in headings:
                with self.subTest(path=relative, heading=heading):
                    self.assertIn(heading, text)


if __name__ == "__main__":
    unittest.main()
