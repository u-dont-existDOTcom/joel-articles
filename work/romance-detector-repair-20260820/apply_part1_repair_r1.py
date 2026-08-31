#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import apply_pass5 as helper

SOURCE_MASTER_SHA = "7ff7a4c20ed879b6b9ff4c5d41cac406db5c5b3a726dc99f5bb4591b11368b48"
SOURCE_P1_SHA = "ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8"
SOURCE_P2_SHA = "20301b1bfb0052de694657411f231f82d9a45ae62ff9c4839015befce5c57dc2"

TALK_MASTER = """# Talk about making love before you do it

From here on, when I say making love, I'm talking about two people who care about each other deeply and feel super connected, using their bodies as part of that connection. If you’ve never experienced this, it may be like trying to explain the taste of an orange. If you don’t know what love is, you don’t know. That’s another conversation, and I'd suggest reading my inner child reparenting guide.

Having sex is just the physical act, whether that connection is there or not. But sometimes it can create the connection also.

My dad gave me one piece of advice about sex: before you do it, ask each other whether you would want to raise children together and whether you're ready. That question started this whole article. I still think it's the best advice in it for people living in permissive cultures, where sex has been separated from the assumption that a baby and a life together may follow. In more traditional cultures, that part may already be assumed, which is why the rest of this article can't just be my dad's advice.

If you can really talk about raising children together, most of the other important questions come up on their own. What kind of life do I want? What kind of life do you want? What would we want for a child? What would sex mean between us?

This will naturally prevent sex from happening too soon if we can talk about it with each other. If we can't, that's a red flag for the relationship's chances of success.
"""
TALK_P1 = TALK_MASTER.replace("# Talk about making love before you do it", "Talk about making love before you do it", 1)

AFFECTION_MASTER = """## Affection and the simmer

Doug Toft, who has been married for fifty years, has a useful list called [*50 Things I Learned from 50 Years of Marriage*](https://dougtoft.substack.com/p/50-things-i-learned-from-50-years). One of his points is to touch his wife without an agenda. A hug, cuddle, kiss, or back rub should sometimes be allowed to end right there. If every time I touch her it turns into me asking for sex, sooner or later even affection can start feeling like a setup.

Kim Anami has a term for something that happens at a different time: [“the simmer”](https://kimanami.com/meet-another-well-fked-man/), the sexual current between encounters. I don't mean every hug needs to become sexual. More like, do we still show each other that we want each other when we're not actually having sex? Maybe she texts from work, “I can’t wait to touch you.” Maybe he tells her what he wants to do later. If we barely flirt or show desire for months, I'd start wondering what happened before I assumed bedtime was the whole problem.

Sex is a pretty sensitive barometer for everything else anyway. If it suddenly changes, I want to look around. Are we resentful? Stressed? Is somebody sick or taking a medication that changed things? Do I still feel wanted? Does she?

And I can't put all of that on my partner. She matters enormously to my desire, but keeping some sexual life in me is partly my job too. If sex is one of the main things separating this relationship from friendship, I don't want to give it whatever exhausted scraps of time happen to be left after everything else.
"""
AFFECTION_P1 = """Affection and the simmer

Doug Toft, who has been married for fifty years, has a useful list called 50 Things I Learned from 50 Years of Marriage. One of his points is to touch his wife without an agenda. A hug, cuddle, kiss, or back rub should sometimes be allowed to end right there. If every time I touch her it turns into me asking for sex, sooner or later even affection can start feeling like a setup.

Kim Anami has a term for something that happens at a different time: “the simmer,” the sexual current between encounters. I don't mean every hug needs to become sexual. More like, do we still show each other that we want each other when we're not actually having sex? Maybe she texts from work, “I can’t wait to touch you.” Maybe he tells her what he wants to do later. If we barely flirt or show desire for months, I'd start wondering what happened before I assumed bedtime was the whole problem.

Sex is a pretty sensitive barometer for everything else anyway. If it suddenly changes, I want to look around. Are we resentful? Stressed? Is somebody sick or taking a medication that changed things? Do I still feel wanted? Does she?

And I can't put all of that on my partner. She matters enormously to my desire, but keeping some sexual life in me is partly my job too. If sex is one of the main things separating this relationship from friendship, I don't want to give it whatever exhausted scraps of time happen to be left after everything else.
"""

CASUAL_OLD = """True commitment grows out of relational depth, not a label. If we spend hours telling each other our deepest longings, fears, and problems, I’ll naturally be ready to help when you need me. I don’t need to promise that on paper. If someone says “I love you, I feel you, I’m here for you,” yet they hardly ever talk to you about what matters, that's a red flag.

The person getting more of what they want may think the arrangement is fulfilling. Usually they’re just less aware that it isn’t. In college I had a friend with four girlfriends who boasted about it to girls while trying to get a fifth."""
CASUAL_NEW = """True commitment grows out of relational depth, not a label. If we spend hours telling each other our deepest longings, fears, and problems, I’ll naturally be ready to help when you need me; I don't need a promise on paper to make me want to. If someone says “I love you, I feel you, I’m here for you,” yet they hardly ever talk to you about what matters, that's a red flag.

In college I had a friend with four girlfriends who boasted about it to girls while trying to get a fifth. If anybody was supposed to be winning that arrangement, it was him."""
CASUAL_TAIL = """

If you want something closer to “casual love-making” without quite so many ways to damage each other, you probably need to find a free-love community where the people aren’t disposable, the bonds can be acknowledged, and any children have a village."""

CRUCIBLE_OLD = """One warning before I romanticize the crucible too much: sometimes this isn't two wounded people triggering each other. Sometimes one person is terrorizing or controlling the other. If you're scared to say no, scared to tell the truth, or scared of what happens if you leave, don't turn that into a mutual communication exercise. Get other people involved and think about safety first."""
CRUCIBLE_NEW = """One warning before I romanticize the crucible too much: sometimes this isn't two wounded people triggering each other but one person terrorizing or controlling the other. If you're scared to say no or tell the truth, or scared of what happens if you leave, don't treat that as a mutual communication exercise—get other people involved and think about safety first."""


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def replace_section(text: str, start: str, end: str, replacement: str, label: str) -> tuple[str, dict[str, object]]:
    if text.count(start) != 1:
        raise RuntimeError(f"{label}: expected one start marker, found {text.count(start)}")
    a = text.index(start)
    b = text.index(end, a + len(start))
    old = text[a:b]
    new = replacement.rstrip() + "\n\n"
    return text[:a] + new + text[b:], {
        "label": label,
        "old_sha256": sha256_text(old),
        "new_sha256": sha256_text(new),
        "old_word_count": len(old.split()),
        "new_word_count": len(new.split()),
    }


def replace_exact(text: str, old: str, new: str, label: str) -> tuple[str, dict[str, object]]:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one occurrence, found {count}")
    return text.replace(old, new, 1), {
        "label": label,
        "old_sha256": sha256_text(old),
        "new_sha256": sha256_text(new),
    }


def build(master: str, part1: str) -> tuple[str, str, list[dict[str, object]], list[dict[str, object]]]:
    mops: list[dict[str, object]] = []
    pops: list[dict[str, object]] = []

    master, op = replace_section(master, "# Talk about making love before you do it\n", "## Affection and the simmer\n", TALK_MASTER, "talk-r27-concise-spine")
    mops.append(op)
    part1, op = replace_section(part1, "Talk about making love before you do it\n", "Affection and the simmer\n", TALK_P1, "talk-r27-concise-spine")
    pops.append(op)

    master, op = replace_section(master, "## Affection and the simmer\n", "## Can Casual Sex or a Situationship Actually Be Honest?\n", AFFECTION_MASTER, "affection-r3-deframeworked")
    mops.append(op)
    part1, op = replace_section(part1, "Affection and the simmer\n", "Can Casual Sex or a Situationship Actually Be Honest?\n", AFFECTION_P1, "affection-r3-deframeworked")
    pops.append(op)

    for label, old, new in [
        ("casual-example-performs-conclusion", CASUAL_OLD, CASUAL_NEW),
        ("casual-delete-duplicate-community-tail", CASUAL_TAIL, ""),
        ("crucible-safety-direct-boundary", CRUCIBLE_OLD, CRUCIBLE_NEW),
    ]:
        master, op = replace_exact(master, old, new, label)
        mops.append(op)
        part1, op = replace_exact(part1, old, new, label)
        pops.append(op)

    return master, part1, mops, pops


REQUIRED = {
    "father-opening": "I asked my dad about sex when I was five",
    "talk-readiness": "ask each other whether you would want to raise children together and whether you're ready",
    "talk-red-flag": "If we can't, that's a red flag for the relationship's chances of success.",
    "affection-toft": "touch his wife without an agenda",
    "affection-simmer": "the sexual current between encounters",
    "casual-community-unique": "Outside a loving poly community or tribe, I think honest casual sex is almost impossible.",
    "casual-friend": "No, I’m miserable, dude. I feel empty inside.",
    "crucible-terror": "one person terrorizing or controlling the other",
    "crucible-fear": "scared to say no or tell the truth",
    "crucible-leave": "scared of what happens if you leave",
    "crucible-safety": "get other people involved and think about safety first",
    "gandarussa": "Gandarussa",
    "community": "Two Pillars Don't Hold The Roof Up",
    "children": "Never recruit children into the adult war.",
    "bear": "Bear, sex can be what you do when you’re older",
}

# The generic older invariant records the old literal Crucible sentence. This
# repair deliberately changes that sentence while preserving the protected
# function; REQUIRED supplies the stricter semantic/function gate for it.
PROTECTED_EXACT_EXEMPT = {"coercion-exits-mutual-crucible"}


def audit(source: str, candidate: str) -> dict[str, object]:
    missing_protected = [
        name
        for name, anchor in helper.PROTECTED_ANCHORS.items()
        if name not in PROTECTED_EXACT_EXEMPT and anchor not in candidate
    ]
    missing = [name for name, anchor in REQUIRED.items() if anchor not in candidate]
    checks = {
        "headings_identical": helper.headings(source) == helper.headings(candidate),
        "native_markers_identical": helper.native_markers(source) == helper.native_markers(candidate),
        "markdown_link_destinations_identical": helper.markdown_links(source) == helper.markdown_links(candidate),
        "protected_anchors_missing": missing_protected,
        "protected_exact_exemptions": sorted(PROTECTED_EXACT_EXEMPT),
        "required_missing": missing,
        "deleted_duplicate_casual_tail_absent": "If you want something closer to “casual love-making” without quite so many ways to damage each other" not in candidate,
    }
    checks["passed"] = (
        checks["headings_identical"]
        and checks["native_markers_identical"]
        and checks["markdown_link_destinations_identical"]
        and not missing_protected
        and not missing
        and checks["deleted_duplicate_casual_tail_absent"]
    )
    return checks


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--source-master", type=Path, required=True)
    p.add_argument("--source-part1", type=Path, required=True)
    p.add_argument("--source-part2", type=Path, required=True)
    p.add_argument("--output-dir", type=Path, required=True)
    a = p.parse_args()

    master = a.source_master.read_text(encoding="utf-8")
    part1 = a.source_part1.read_text(encoding="utf-8")
    part2 = a.source_part2.read_text(encoding="utf-8")
    observed = {"master": sha256_text(master), "part1": sha256_text(part1), "part2": sha256_text(part2)}
    expected = {"master": SOURCE_MASTER_SHA, "part1": SOURCE_P1_SHA, "part2": SOURCE_P2_SHA}
    if observed != expected:
        raise RuntimeError(f"source hash mismatch: expected={expected} observed={observed}")

    master2, part1_2, mops, pops = build(master, part1)
    if part2 != a.source_part2.read_text(encoding="utf-8") or sha256_text(part2) != SOURCE_P2_SHA:
        raise RuntimeError("Part 2 changed during Part 1 repair")
    checks = audit(master, master2)
    if not checks["passed"]:
        raise RuntimeError(f"Part 1 repair invariant audit failed: {checks}")

    a.output_dir.mkdir(parents=True, exist_ok=True)
    (a.output_dir / "candidate-master.md").write_text(master2, encoding="utf-8")
    (a.output_dir / "candidate-part-1.txt").write_text(part1_2, encoding="utf-8")
    (a.output_dir / "candidate-part-2.txt").write_text(part2, encoding="utf-8")
    manifest = {
        "schema_version": 1,
        "status": "part1_repair_candidate_not_owner_final_article",
        "source": observed,
        "candidate": {
            "master": {"sha256": sha256_text(master2), "word_count_whitespace": len(master2.split()), "operations": mops, "invariant_audit": checks},
            "part1": {"sha256": sha256_text(part1_2), "word_count_whitespace": len(part1_2.split()), "operations": pops},
            "part2": {"sha256": sha256_text(part2), "word_count_whitespace": len(part2.split()), "operations": [], "unchanged": True},
        },
        "local_evidence": {
            "talk": "standalone 0% Human on three materially different realizations; concise selected spine comes from exact historical 879-word Talk+Slow control that was 100% Human; aggregate Part1 is the next decision-changing boundary",
            "affection": "r3 de-frameworked local realization Human 0.19545766711235046; selected on editorial architecture grounds pending aggregate interaction",
            "casual": "full natural section r3 100% Human",
            "crucible": "full natural section r3 100% Human with protected safety function intact",
        },
        "detector_plan": {"part1": "aggregate certification boundary; measure exact changed Part1 next"},
    }
    (a.output_dir / "candidate-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
