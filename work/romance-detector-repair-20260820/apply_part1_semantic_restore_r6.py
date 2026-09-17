#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import apply_pass5 as helper
import apply_part1_repair_r1 as r1
import apply_part1_repair_r2 as r2

SOURCE_MASTER_SHA = "d205393b1724256416291050fdeb41c18afb9669fddc45cf713559e9ecd9e406"
SOURCE_P1_SHA = "e6b9e546bb2f07af8e18fc65fb6883d27bf0106d93f5f02d6674a88e034d572d"
SOURCE_P2_SHA = "20301b1bfb0052de694657411f231f82d9a45ae62ff9c4839015befce5c57dc2"

TALK_MASTER = """# Talk about making love before you do it

From here on, when I say making love, I'm talking about two people who care about each other deeply and feel super connected, using their bodies as part of that connection. If you’ve never experienced this, it may be like trying to explain the taste of an orange. If you don’t know what love is, you don’t know. That’s another conversation, and I'd suggest reading my inner child reparenting guide.

Having sex is just the physical act, whether that connection is there or not. But sometimes it can create the connection also.

My dad gave me one piece of advice about sex: before you do it, ask each other whether you would want to raise children together and whether you're ready. That question started this whole article. I still think it's the best advice in it for people living in permissive cultures, where sex has been separated from the assumption that a baby and a life together may follow. In more traditional cultures, that part may already be assumed, which is why the rest of this article can't just be my dad's advice.

If you can really talk about raising children together, most of the other important questions come up on their own. What kind of life do I want? What kind of life do you want? What would we want for a child? What would sex mean between us?

Most couples don’t talk honestly about sex until they’re already having it. Bad timing. Now saying what you actually want might interrupt the whole thing, disappoint somebody, or turn a moment of passion into a negotiation. Talk before you’re naked. That conversation is already part of making love.

What do you actually want? You may know some of it and not the rest. What makes your body relax and open? Is there anything kinky you need to be able to say out loud? What has your past made you want, or made you avoid? What just doesn't work?

You may not know all the answers yet. “I don’t know, but I’m willing to find out honestly with you” is a perfectly good answer.

And what is sex for each of you? One person may mainly think of bonding while the other thinks of play. Sometimes it may feel sacred; another time it may just be how you come down from a bad day. It doesn’t have to mean the same thing every time.

Sex drives are independently alive and always changing. For some stretch, one of you will want more, less, or something different. When the discordance comes, it's one of the saddest sources of quiet resentment. Talk about what you’ll do when that happens before either person is already hurt. It won’t solve it in advance, but at least you’ll have somewhere to begin.

And can you actually say all that once you're naked? Even if you think she'll be disappointed? If not, then you're both just hoping sex will somehow sort out what neither of you wanted to say.

Bodies fitting is not enough. Can you stay honest while you’re completely exposed? Talking before your clothes come off already practices some of the trust, attention, and willingness to be seen that making love needs.

This will naturally prevent sex from happening too soon if we can talk about it with each other. If we can't, that's a red flag for the relationship's chances of success.
"""
TALK_P1 = TALK_MASTER.replace("# Talk about making love before you do it", "Talk about making love before you do it", 1)

AFFECTION_MASTER = """## Affection and the simmer

Doug Toft, who has been married for fifty years, has a useful list called [*50 Things I Learned from 50 Years of Marriage*](https://dougtoft.substack.com/p/50-things-i-learned-from-50-years). One of his points is to touch his wife without an agenda. A hug, cuddle, kiss, or back rub should sometimes be allowed to end right there. If every time I touch her it turns into me asking for sex, sooner or later even affection can start feeling like a setup.

Kim Anami has a term for something that happens at a different time: [“the simmer”](https://kimanami.com/meet-another-well-fked-man/), the sexual current between encounters. I don't mean every hug needs to become sexual. More like, do we still show each other that we want each other when we're not actually having sex? Maybe she texts from work, “I can’t wait to touch you.” Maybe he tells her what he wants to do later. It shouldn't become relationship homework. But if we barely flirt or show desire for months, I'd start wondering what happened before I assumed bedtime was the whole problem.

For me both things matter: affection has to be allowed to stop at affection, and I still want to feel an erotic current between us.

Sex is a pretty sensitive barometer for everything else anyway. If it suddenly changes, I want to look around. Are we resentful? Stressed? Is somebody sick or taking a medication that changed things? Do I still feel wanted? Does she?

And I can't put all of that on my partner. She matters enormously to my desire, but keeping some sexual life in me is partly my job too. If sex is one of the main things separating this relationship from friendship, I don't want to give it whatever exhausted scraps of time happen to be left after everything else.
"""
AFFECTION_P1 = """Affection and the simmer

Doug Toft, who has been married for fifty years, has a useful list called 50 Things I Learned from 50 Years of Marriage. One of his points is to touch his wife without an agenda. A hug, cuddle, kiss, or back rub should sometimes be allowed to end right there. If every time I touch her it turns into me asking for sex, sooner or later even affection can start feeling like a setup.

Kim Anami has a term for something that happens at a different time: “the simmer,” the sexual current between encounters. I don't mean every hug needs to become sexual. More like, do we still show each other that we want each other when we're not actually having sex? Maybe she texts from work, “I can’t wait to touch you.” Maybe he tells her what he wants to do later. It shouldn't become relationship homework. But if we barely flirt or show desire for months, I'd start wondering what happened before I assumed bedtime was the whole problem.

For me both things matter: affection has to be allowed to stop at affection, and I still want to feel an erotic current between us.

Sex is a pretty sensitive barometer for everything else anyway. If it suddenly changes, I want to look around. Are we resentful? Stressed? Is somebody sick or taking a medication that changed things? Do I still feel wanted? Does she?

And I can't put all of that on my partner. She matters enormously to my desire, but keeping some sexual life in me is partly my job too. If sex is one of the main things separating this relationship from friendship, I don't want to give it whatever exhausted scraps of time happen to be left after everything else.
"""

CASUAL_EXAMPLE_CURRENT = """In college I had a friend with four girlfriends who boasted about it to girls while trying to get a fifth. If anybody was supposed to be winning that arrangement, it was him. I asked him, “But are you really happy?” He said, “No, I’m miserable, dude. I feel empty inside.”"""
CASUAL_EXAMPLE_RESTORED = """The person getting more of what they want may think the arrangement is fulfilling. Usually they’re just less aware that it isn’t. In college I had a friend with four girlfriends who boasted about it to girls while trying to get a fifth. If anybody was supposed to be winning that arrangement, it was him. I asked him, “But are you really happy?” He said, “No, I’m miserable, dude. I feel empty inside.”"""

CASUAL_CLOSE_CURRENT = """The full conversation is so big that almost nobody would have casual sex if they took it seriously. Which is why almost nobody has the full conversation. I can’t decide what is okay for anybody else. I can say that most people who defend casual sex are not being very honest with themselves about pregnancy, attachment, or what they might owe the person afterward."""
CASUAL_CLOSE_RESTORED = CASUAL_CLOSE_CURRENT + """

If you want something closer to “casual love-making” without quite so many ways to damage each other, you probably need to find a free-love community where the people aren’t disposable, the bonds can be acknowledged, and any children have a village."""

PATIENT_CURRENT = r2.PATIENT_NEW
PATIENT_RESTORED = r2.PATIENT_OLD

SEMANTIC_REQUIREMENTS = {
    "father-readiness": "ask each other whether you would want to raise children together and whether you're ready",
    "talk-before-naked": "Talk before you’re naked.",
    "talk-body": "What makes your body relax and open?",
    "talk-kink": "anything kinky you need to be able to say out loud",
    "talk-history": "What has your past made you want, or made you avoid?",
    "talk-unknown": "I don’t know, but I’m willing to find out honestly with you",
    "talk-sex-meanings": "One person may mainly think of bonding while the other thinks of play.",
    "talk-drive-mismatch": "Sex drives are independently alive and always changing.",
    "talk-naked-honesty": "And can you actually say all that once you're naked?",
    "talk-trust": "trust, attention, and willingness to be seen",
    "talk-red-flag": "If we can't, that's a red flag for the relationship's chances of success.",
    "affection-no-agenda": "touch his wife without an agenda",
    "affection-simmer": "the sexual current between encounters",
    "affection-examples": "I can’t wait to touch you.",
    "affection-no-homework": "It shouldn't become relationship homework.",
    "affection-both": "For me both things matter",
    "affection-barometer": "Sex is a pretty sensitive barometer for everything else anyway.",
    "affection-responsibility": "keeping some sexual life in me is partly my job too",
    "affection-time": "whatever exhausted scraps of time happen to be left after everything else",
    "casual-awareness": "The person getting more of what they want may think the arrangement is fulfilling.",
    "casual-village": "any children have a village",
    "patient-cold": "would have been cold",
    "patient-pattern": "enough moments become a pattern",
}


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def replace_exact(text: str, label: str, old: str, new: str) -> tuple[str, dict[str, object]]:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one occurrence, found {count}")
    return text.replace(old, new, 1), {
        "label": label,
        "old_sha256": sha256_text(old),
        "new_sha256": sha256_text(new),
    }


def semantic_audit(source: str, candidate: str) -> dict[str, object]:
    missing_protected = [
        name
        for name, anchor in helper.PROTECTED_ANCHORS.items()
        if name not in r1.PROTECTED_EXACT_EXEMPT and anchor not in candidate
    ]
    missing_base = [name for name, anchor in r1.REQUIRED.items() if anchor not in candidate]
    missing_semantic = [name for name, anchor in SEMANTIC_REQUIREMENTS.items() if anchor not in candidate]
    checks = {
        "headings_identical": helper.headings(source) == helper.headings(candidate),
        "native_markers_identical": helper.native_markers(source) == helper.native_markers(candidate),
        "markdown_link_destinations_identical": helper.markdown_links(source) == helper.markdown_links(candidate),
        "protected_anchors_missing": missing_protected,
        "protected_exact_exemptions": sorted(r1.PROTECTED_EXACT_EXEMPT),
        "base_required_missing": missing_base,
        "semantic_required_missing": missing_semantic,
    }
    checks["passed"] = (
        checks["headings_identical"]
        and checks["native_markers_identical"]
        and checks["markdown_link_destinations_identical"]
        and not missing_protected
        and not missing_base
        and not missing_semantic
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
    observed = {
        "master": sha256_text(master),
        "part1": sha256_text(part1),
        "part2": sha256_text(part2),
    }
    expected = {
        "master": SOURCE_MASTER_SHA,
        "part1": SOURCE_P1_SHA,
        "part2": SOURCE_P2_SHA,
    }
    if observed != expected:
        raise RuntimeError(f"source hash mismatch: expected={expected} observed={observed}")

    master2 = master
    part1_2 = part1
    mops: list[dict[str, object]] = []
    pops: list[dict[str, object]] = []

    master2, op = r1.replace_section(
        master2,
        "# Talk about making love before you do it\n",
        "## Affection and the simmer\n",
        TALK_MASTER,
        "talk-semantic-restore-r6",
    )
    mops.append(op)
    part1_2, op = r1.replace_section(
        part1_2,
        "Talk about making love before you do it\n",
        "Affection and the simmer\n",
        TALK_P1,
        "talk-semantic-restore-r6",
    )
    pops.append(op)

    master2, op = r1.replace_section(
        master2,
        "## Affection and the simmer\n",
        "## Can Casual Sex or a Situationship Actually Be Honest?\n",
        AFFECTION_MASTER,
        "affection-semantic-restore-r6",
    )
    mops.append(op)
    part1_2, op = r1.replace_section(
        part1_2,
        "Affection and the simmer\n",
        "Can Casual Sex or a Situationship Actually Be Honest?\n",
        AFFECTION_P1,
        "affection-semantic-restore-r6",
    )
    pops.append(op)

    for label, old, new in [
        ("casual-awareness-restore-r6", CASUAL_EXAMPLE_CURRENT, CASUAL_EXAMPLE_RESTORED),
        ("casual-village-restore-r6", CASUAL_CLOSE_CURRENT, CASUAL_CLOSE_RESTORED),
        ("patient-pattern-restore-r6", PATIENT_CURRENT, PATIENT_RESTORED),
    ]:
        master2, op = replace_exact(master2, label, old, new)
        mops.append(op)
        part1_2, op = replace_exact(part1_2, label, old, new)
        pops.append(op)

    if sha256_text(part2) != SOURCE_P2_SHA:
        raise RuntimeError("Part 2 changed during Part 1 semantic restoration")

    checks = semantic_audit(master, master2)
    if not checks["passed"]:
        raise RuntimeError(f"Part 1 r6 semantic invariant audit failed: {checks}")

    a.output_dir.mkdir(parents=True, exist_ok=True)
    (a.output_dir / "candidate-master.md").write_text(master2, encoding="utf-8")
    (a.output_dir / "candidate-part-1.txt").write_text(part1_2, encoding="utf-8")
    (a.output_dir / "candidate-part-2.txt").write_text(part2, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "status": "part1_semantic_restoration_candidate_not_owner_final_article",
        "source": observed,
        "candidate": {
            "master": {
                "sha256": sha256_text(master2),
                "word_count_whitespace": len(master2.split()),
                "operations": mops,
                "semantic_invariant_audit": checks,
            },
            "part1": {
                "sha256": sha256_text(part1_2),
                "word_count_whitespace": len(part1_2.split()),
                "operations": pops,
            },
            "part2": {
                "sha256": sha256_text(part2),
                "word_count_whitespace": len(part2.split()),
                "operations": [],
                "unchanged": True,
            },
        },
        "source_detector_result": {
            "part1_sha256": SOURCE_P1_SHA,
            "pangram4_fraction_human": 0.9838229417800903,
            "rejected_for_semantic_loss": True,
        },
        "traceability": {
            "method": "requirements-traceability plus atomic-content-unit adaptation",
            "audit": "SEMANTIC-FIDELITY-AUDIT-20260821.md",
            "decision": "restore all unsuperseded canonical argumentative functions before further detector optimization",
        },
        "detector_plan": {
            "status": "do not dispatch aggregate yet",
            "reason": "first inspect exact r6 materialization and freeze the final semantic-function ledger; preserve remaining local-section calls for decision-changing final variants",
        },
    }
    (a.output_dir / "candidate-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
