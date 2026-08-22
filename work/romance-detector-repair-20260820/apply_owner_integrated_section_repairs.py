#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import apply_pass5 as helper

SOURCE_MASTER_SHA = "dee776ada0db4dc2940d3815b9512ad5034e3224b0c569a9d29f6a69d9bb75a9"
SOURCE_P1_SHA = "ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8"
SOURCE_P2_SHA = "9dc539ca99f8c747ecd5a551f2c72ad476c87671919863d2ad469acf6c6e696f"

NOT_PERFORMANCE_OLD = """## Not A Performance

The moment I have to prove that I’m the man, something has already become fake.

I don’t actually walk around thinking I’m some super-masculine guy. I cry, I need help, I get things wrong. Bee once called me her “wife.” I don’t recommend that as a polarity exercise, by the way.

When a woman appreciates that masculine side of me, it tends to come out by itself.

A woman shouldn’t have to act soft, helpless, or cute every minute either. She can get pushed in the opposite direction too: if she’s spent years worrying that she isn’t beautiful enough, or that she’s too emotional, too difficult, not logical enough, or too needy, she may overcorrect into needing nobody. Then receiving care or letting a man lead starts to feel like weakness.

Toft’s advice after fifty years is simple: tell her she’s beautiful, and keep noticing new kinds of beauty as she ages. Anami emphasizes learning to receive. Letting a man help, lead, or give her pleasure doesn’t make a strong woman helpless. A man receiving care doesn’t make him a child either.

We can invite these energies out of each other:
“Honey, how do you see this intuitively?”
or, “Can you help me think through the practical side for a minute?”

When a strong woman surrenders, she is choosing to. She knows she could drive; she asks me to drive because she likes how it feels when I do. That’s sexy.

That's called invitational: Would you rather go to a party where you were invited or a war you got drafted into?

When a woman doesn't know how to gently invite a man to lead, she may manufacture a crisis until the man is forced to take charge to get the same outward result.

Unfortunately, I've seen a lot of the latter."""

NOT_PERFORMANCE_NEW = """## Not A Performance

The moment I have to prove that I’m the man, something has already become fake.

I don’t actually walk around thinking I’m some super-masculine guy. I cry, I need help, I get things wrong. Bee once called me her “wife.” I don’t recommend that as a polarity exercise, by the way.

When a woman appreciates that masculine side of me, it tends to come out by itself.

Toft says that after fifty years he still tells his wife she’s beautiful, including finding new kinds of beauty as she ages. Anami talks a lot about women learning to receive. Sometimes that’s as ordinary as a woman who knows perfectly well how to drive asking me to drive because she likes how it feels when I do; she’s choosing the experience. I might ask, “Honey, how do you see this intuitively?” because I actually want her to go there, and she might ask me to help think through the practical side because she wants that from me.

That's called invitational: Would you rather go to a party where you were invited or a war you got drafted into?

When a woman doesn't know how to gently invite a man to lead, she may manufacture a crisis until the man is forced to take charge to get the same outward result.

Unfortunately, I've seen a lot of the latter."""

TWO_PILLARS_OLD = """Let me show you how this looked for me. I’ve noticed in my own relationships that whenever a serious issue arises, both of us tend to turn to our separate circles of friends for support. Then I resent the one-sided story she’s telling, she resents the one-sided story I’m telling, and eventually neither of us wants to talk to the other’s friends. Some of the friends may even be exes who want us to break up. By then, the outside support isn’t really shared support anymore.

There's a practical side too. Two people covering housing, money, children, health, emotional crises, everything—there's no backup when one of them goes down. Who even has time for the relationship itself at that point?"""

TWO_PILLARS_NEW = """Let me show you how this looked for me. I’ve noticed in my own relationships that whenever a serious issue arises, both of us tend to turn to our separate circles of friends for support. Then I resent the one-sided story she’s telling, she resents the one-sided story I’m telling. Some of the friends may even be exes who want us to break up, and eventually neither of us wants to talk to the other's friends anymore. That's a pretty terrible time to be trying to run the rest of life with two people. Housing, money, children, health, emotional crises—if one person goes down, the other becomes the whole backup system. Who even has time for the relationship itself at that point?"""

PSYCHEDELIC_OLD = """I’ve also had friends get together at MDMA parties and stuff. It’s rarely a good idea. The intimacy can be completely real. You may feel that this person understands you more deeply than anyone ever has. There is still a lot you don’t know: what happens when you’re sober, irritated, jealous, broke, bored, or trying to make a difficult decision together? Or you might even sometimes have the opposite problem, like I had with H.D., where the connection continues to deepen while sober, and it becomes something that one person might cling to desperately, never imagining they could find that again."""

PSYCHEDELIC_NEW = """I’ve also had friends get together at MDMA parties and stuff. It’s rarely a good idea. The intimacy can be completely real without telling you whether the two of you actually work together sober. Or you might even sometimes have the opposite problem, like I had with H.D., where the connection continues to deepen while sober, and it becomes something that one person might cling to desperately, never imagining they could find that again."""

MASTER_REPLACEMENTS = [
    ("not-a-performance-r3", NOT_PERFORMANCE_OLD, NOT_PERFORMANCE_NEW),
    ("two-pillars-r2", TWO_PILLARS_OLD, TWO_PILLARS_NEW),
    ("psychedelic-discernment-r2", PSYCHEDELIC_OLD, PSYCHEDELIC_NEW),
]

P2_REPLACEMENTS = [
    ("not-a-performance-r3", NOT_PERFORMANCE_OLD.replace("## Not A Performance", "Not A Performance"), NOT_PERFORMANCE_NEW.replace("## Not A Performance", "Not A Performance")),
    ("two-pillars-r2", TWO_PILLARS_OLD, TWO_PILLARS_NEW),
    ("psychedelic-discernment-r2", PSYCHEDELIC_OLD, PSYCHEDELIC_NEW),
]

REQUIRED = {
    "not-performance-owner": "Bee once called me her “wife.”",
    "not-performance-r3": "Sometimes that’s as ordinary as a woman who knows perfectly well how to drive asking me to drive",
    "invitation": "Would you rather go to a party where you were invited or a war you got drafted into?",
    "two-pillars": "the other becomes the whole backup system",
    "community-claim": "I'm sure B. and I would still be together if we'd had a real community around us",
    "psychedelic": "The intimacy can be completely real without telling you whether the two of you actually work together sober.",
    "gandarussa": "Gandarussa",
    "bear": "Bear, sex can be what you do when you’re older",
}


def audit(source: str, candidate: str) -> dict[str, object]:
    missing = [name for name, anchor in REQUIRED.items() if anchor not in candidate]
    checks = {
        "headings_identical": helper.headings(source) == helper.headings(candidate),
        "native_markers_identical": helper.native_markers(source) == helper.native_markers(candidate),
        "markdown_link_destinations_identical": helper.markdown_links(source) == helper.markdown_links(candidate),
        "required_missing": missing,
    }
    checks["passed"] = bool(checks["headings_identical"]) and bool(checks["native_markers_identical"]) and bool(checks["markdown_link_destinations_identical"]) and not missing
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
    observed = {"master": helper.sha256_text(master), "part1": helper.sha256_text(part1), "part2": helper.sha256_text(part2)}
    expected = {"master": SOURCE_MASTER_SHA, "part1": SOURCE_P1_SHA, "part2": SOURCE_P2_SHA}
    if observed != expected:
        raise RuntimeError(f"source hash mismatch: expected={expected} observed={observed}")

    master2, master_ops = helper.apply_replacements(master, MASTER_REPLACEMENTS)
    part2_2, p2_ops = helper.apply_replacements(part2, P2_REPLACEMENTS)
    part1_2 = part1
    if helper.sha256_text(part1_2) != SOURCE_P1_SHA:
        raise RuntimeError("Part 1 changed")
    checks = audit(master, master2)
    if not checks["passed"]:
        raise RuntimeError(f"invariant audit failed: {checks}")

    a.output_dir.mkdir(parents=True, exist_ok=True)
    (a.output_dir / "candidate-master.md").write_text(master2, encoding="utf-8")
    (a.output_dir / "candidate-part-1.txt").write_text(part1_2, encoding="utf-8")
    (a.output_dir / "candidate-part-2.txt").write_text(part2_2, encoding="utf-8")
    manifest = {
        "schema_version": 1,
        "status": "owner_integrated_section_repaired_candidate_not_owner_final_article",
        "source": observed,
        "candidate": {
            "master": {"sha256": helper.sha256_text(master2), "word_count_whitespace": len(master2.split()), "operations": master_ops, "invariant_audit": checks},
            "part1": {"sha256": helper.sha256_text(part1_2), "word_count_whitespace": len(part1_2.split()), "operations": [], "reuses_registered_detector_result": True},
            "part2": {"sha256": helper.sha256_text(part2_2), "word_count_whitespace": len(part2_2.split()), "operations": p2_ops},
        },
        "local_section_evidence": {
            "primal-not-a-performance": {"calls": 3, "pangram4_fraction_human": 1.0, "result": "state/experiments/romance-detector-repair-20260820-owner-integrated-r3-local-sections-results.json"},
            "community-two-pillars": {"calls": 2, "pangram4_fraction_human": 1.0, "result": "state/experiments/romance-detector-repair-20260820-owner-integrated-r4-local-sections-results.json"},
            "psychedelic-relationship-discernment": {"calls": 2, "pangram4_fraction_human": 1.0, "result": "state/experiments/romance-detector-repair-20260820-owner-integrated-r2-local-sections-results.json"},
        },
        "detector_plan": {"part2": "aggregate certification boundary; six-call local-section cap does not apply; exact cache/recovery/decision-value gates still apply"},
    }
    (a.output_dir / "candidate-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
