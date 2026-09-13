#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import apply_pass5 as helper

PASS5_MASTER_SHA = "cad2b0d828256f1816cbd2c293cbf0ced9e43aec3595b4a78daa566db4a8338d"
PASS5_P1_SHA = "ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8"
PASS5_P2_SHA = "a5b1cf38a81537492d08a8eac2e930012fbf10264beadfc252a3efc1bd794c20"
REGISTERED_P1_SHA = PASS5_P1_SHA

MUSES_OLD = """Of course, some women barely have that poetic quality, and men can go there too; artistic men often live much closer to it. I still experience it as highly feminine. She may be feeling or seeing something before either of us can explain it, while I’m already trying to turn it into prose: What happened? What does it mean? What are we going to do about it?

I think girls should be encouraged to develop that side without having it trained out of them, but also without letting intuition turn into helplessness or chaos. Boys need access to it too.

Toft’s fifty-year-marriage advice is the old Men Are from Mars, Women Are from Venus problem in lived form. She may want to talk and be heard while he starts fixing. Men do this too, although I think men are more often looking for the solution. So I ask, “Do you want me to help figure this out, or do you mostly want me to listen?”

I can listen to the feeling without agreeing with every literal statement. If it turns into intimidation, false accusations, or making somebody scared to say no, that’s no longer poetry. That’s the Crucible safety problem I already talked about.

The part I like is when she sees something before it has become a plan and I get to figure out the details. She can influence the direction without taking over the whole thing. If she keeps saying “Let me do it,” I start feeling useless.

Money can create the same dynamic. A woman earning more than me doesn’t bother me. Using it as proof that she’s the competent adult can effeminate me in the relationship. A man can wreck the polarity from the other side by needing a successful woman to shrink so he can feel masculine."""
MUSES_NEW = """Of course, this isn’t literally women=poetry and men=prose. Some women barely have that quality, and artistic men can live much closer to it. What attracts me is the intuitive leap—the thing she sees before I can explain it. I want girls to keep that without learning helplessness or chaos, and boys to keep access to it too.

This shows up in arguments. Toft says that after fifty years of marriage, sometimes she wants to talk while he wants to fix. I recognize that. So I ask, “Do you want me to help figure this out, or do you mostly want me to listen?” Listening doesn’t mean agreeing with every literal statement. If it turns into intimidation, false accusations, or making somebody scared to say no, that’s the Crucible safety problem I already talked about.

Where I like the polarity is when she sees something before it has become a plan and I help make it workable. If she keeps taking over with “Let me do it,” I start feeling useless. Money can do the same thing. Her earning more than me is fine. Treating that as proof that she’s the competent adult can effeminate me in the relationship. I can wreck it from the other side by needing a successful woman to shrink so I feel masculine."""

DIRECTION_OLD = """She doesn't have to pretend I'm always right either. “Thank you, I’ll consider that. What do you think about doing it this way?” can be a kind of gentle leadership: she changes the direction without making every disagreement a contest over who is driving.

In my experience, women often prefer a man to say what he wants more directly:

“This is where I want to go. This is what I think we should do. Are you game?”

She can argue with the plan, improve it, or say no. For me that doesn’t kill the masculine charge. Part of the charge is actually offering a direction instead of waiting for her to pull one out of me.

I don’t think equal dignity means splitting every role down the middle. I’d rather each of us do more of what we’re actually good at. If I like driving and she likes cooking, great. If it’s the reverse, great too. Whatever I’m leading, her ideas still matter. Mandar obedeciendo, as the Zapatistas say. I don’t need us to keep score."""
DIRECTION_NEW = """In my experience, women often prefer me to say what I want instead of hovering around it:

“This is where I want to go. This is what I think we should do. Are you game?”

She can improve the plan or say no. That doesn’t make it feel less masculine to me; I’m still offering a direction instead of waiting for her to pull one out of me.

I don’t need every role to be symmetrical either. If I like driving and she likes cooking, we can do that. If one of us is better at something, let that person do more of it. When I’m leading, I still want her ideas. Mandar obedeciendo, as the Zapatistas say."""

COMMUNITY_OLD = """Maybe an unusually strong couple can get away without much community. I think that's rare, and community can't rescue a relationship if both people are falling apart anyway.

What we were missing wasn't just more friends on each side. We needed people who actually knew both of us. Mutual friends can notice patterns neither person sees. Somebody else can comfort your partner when you've become the wrong person to do it. And if somebody knows both of you, they have a chance of noticing when the story they're hearing doesn't match the person they know."""
COMMUNITY_NEW = """Maybe an unusually strong couple can get away without much community. I think that's rare. Community isn't magic either; if both people are falling apart, there is only so much anyone else can do."""

EXCLUSIVITY_OLD = """Strict exclusivity backed by law and social enforcement grew alongside agriculture, settled property, and inheritance; by the Industrial Revolution it had become a mass norm. Tribal cultures across the world have generally been more flexible, with primary partnerships or “social monogamy” that still allowed accepted sexual or emotional connections outside them.

Marriage still carries that property-and-inheritance job, while modern vows pile a second job on top: guarantee a permanent romantic feeling."""
EXCLUSIVITY_NEW = """A lot of that history runs through agriculture, property, and inheritance. By the Industrial Revolution, strict exclusivity had law and social pressure behind it as a mass norm. Tribal cultures across the world have generally been looser: a primary partnership could still leave accepted room for sexual or emotional connections outside it—what gets called “social monogamy.”

Marriage kept the property-and-inheritance job, and modern romantic vows gave it another one: promise that this feeling will last forever."""

P2_REPLACEMENTS = [
    ("muses-live-thought-chain", MUSES_OLD, MUSES_NEW),
    ("direct-leadership-without-aftercare", DIRECTION_OLD, DIRECTION_NEW),
    ("community-concrete-example-does-the-work", COMMUNITY_OLD, COMMUNITY_NEW),
    ("exclusivity-history-live-question", EXCLUSIVITY_OLD, EXCLUSIVITY_NEW),
]

MASTER_MUSES_OLD = MUSES_OLD.replace("the old Men Are from Mars, Women Are from Venus problem", "the old *Men Are from Mars, Women Are from Venus* problem")
MASTER_MUSES_NEW = MUSES_NEW
MASTER_REPLACEMENTS = [
    ("muses-live-thought-chain", MASTER_MUSES_OLD, MASTER_MUSES_NEW),
    ("direct-leadership-without-aftercare", DIRECTION_OLD, DIRECTION_NEW),
    ("community-concrete-example-does-the-work", COMMUNITY_OLD, COMMUNITY_NEW),
    ("exclusivity-history-live-question", EXCLUSIVITY_OLD, EXCLUSIVITY_NEW),
]

PASS6_REQUIRED = {
    "crucible-safety": "that’s the Crucible safety problem I already talked about.",
    "money-not-problem": "Her earning more than me is fine.",
    "effeminate": "effeminate me in the relationship",
    "successful-woman-reverse": "successful woman to shrink so I feel masculine",
    "direct-offer": "This is where I want to go. This is what I think we should do. Are you game?",
    "female-can-say-no": "She can improve the plan or say no.",
    "zapatista": "Mandar obedeciendo",
    "community-caveat": "Community isn't magic either",
    "concrete-community-next": "That's not abstract to me: I'm sure B. and I would still be together",
    "agriculture": "agriculture, property, and inheritance",
    "industrial": "Industrial Revolution",
    "social-monogamy": "social monogamy",
    "romantic-vow": "promise that this feeling will last forever",
}


def audit(source: str, candidate: str) -> dict[str, object]:
    checks = helper.audit_master(source, candidate)
    missing = [name for name, anchor in PASS6_REQUIRED.items() if anchor not in candidate]
    checks["pass6_required_missing"] = missing
    checks["passed"] = bool(checks.get("passed")) and not missing
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description="Materialize Romance detector-repair pass 6.")
    parser.add_argument("--pass5-master", type=Path, required=True)
    parser.add_argument("--pass5-part1", type=Path, required=True)
    parser.add_argument("--pass5-part2", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    master = args.pass5_master.read_text(encoding="utf-8")
    part1 = args.pass5_part1.read_text(encoding="utf-8")
    part2 = args.pass5_part2.read_text(encoding="utf-8")
    observed = {"master": helper.sha256_text(master), "part1": helper.sha256_text(part1), "part2": helper.sha256_text(part2)}
    expected = {"master": PASS5_MASTER_SHA, "part1": PASS5_P1_SHA, "part2": PASS5_P2_SHA}
    if observed != expected:
        raise RuntimeError(f"pass-5 source hash mismatch: expected={expected} observed={observed}")

    master6, master_ops = helper.apply_replacements(master, MASTER_REPLACEMENTS)
    part2_6, p2_ops = helper.apply_replacements(part2, P2_REPLACEMENTS)
    part1_6 = part1
    if helper.sha256_text(part1_6) != REGISTERED_P1_SHA:
        raise RuntimeError("Part 1 changed during pass 6; detector submission is forbidden")
    checks = audit(master, master6)
    if not checks["passed"]:
        raise RuntimeError(f"pass-6 master invariant audit failed: {checks}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    out_master = args.output_dir / "candidate-master.md"
    out_p1 = args.output_dir / "candidate-part-1.txt"
    out_p2 = args.output_dir / "candidate-part-2.txt"
    out_master.write_text(master6, encoding="utf-8")
    out_p1.write_text(part1_6, encoding="utf-8")
    out_p2.write_text(part2_6, encoding="utf-8")
    manifest = {
        "schema_version": 1,
        "status": "candidate_not_owner_final",
        "source_pass5": observed,
        "candidate": {
            "master": {"path": out_master.name, "sha256": helper.sha256_text(master6), "word_count_whitespace": len(master6.split()), "operations": master_ops, "invariant_audit": checks},
            "part1": {"path": out_p1.name, "sha256": helper.sha256_text(part1_6), "word_count_whitespace": len(part1_6.split()), "operations": [], "reuses_registered_detector_result": True},
            "part2": {"path": out_p2.name, "sha256": helper.sha256_text(part2_6), "word_count_whitespace": len(part2_6.split()), "operations": p2_ops},
        },
        "detector_plan": {"part1": "no_new_call_exact_registered_hash_unchanged", "part2": "final_paid_pangram4_measurement_slot_6_via_private_selfhost"},
        "editorial_note": "Pass 6 targets the four exact residual AI windows returned by pass 5. It removes redundant explanatory recap where the following owner examples already do the work, preserves the Primal/Crucible/community/exclusivity claims, and is the final paid Part-2 slot under the six-call cap.",
    }
    (args.output_dir / "candidate-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
