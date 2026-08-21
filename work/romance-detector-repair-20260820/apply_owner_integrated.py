#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import apply_pass6 as base

PASS6_MASTER_SHA = "e09cb2309653d3ba9fc14526e7a49b1bef6f27a7494783489895a9c32fba93c5"
PASS6_P1_SHA = "ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8"
PASS6_P2_SHA = "6166fb2c17022e978de1019210067429f749071e53581bbe184adb721dbe8215"
REGISTERED_P1_SHA = PASS6_P1_SHA

# Direct owner rewrite. Two previously authorized D1 typo normalizations are applied:
# `as the grow` -> `as they grow`; `she see sees` -> `she sees`.
MUSES_OWNER = """Some women barely have that poetic quality, and artistic men can live much closer to it. I'm referring more to feminine vs masculine archetypes. What attracts me is the feminine intuitive leap, because it's hard for me to understand, seems often absurd, yet many times more accurate than what I could have figured. I hope this feminine quality can be treasured by all girls as they grow, without falling into helplessness or chaos that over-relying on it without calibration could create. Boys should also maintain their access to this, even if it's not primary.

This polarity is attracting, but it also shows up in arguments. Toft says that after fifty years of marriage, sometimes his wife wants to talk while he wants to fix, a la Men are From Mars, Women are from Venus. I recognize that as well. So I ask, “Do you want me to help figure this out, or do you mostly want me to listen?” Listening doesn't mean I'm gonna be a doormat tho. If I start listening to her demonize me, that’s the Crucible safety problem I already talked about.

Where I like the polarity is when she sees the Big Picture, and I help fill in the details to make our plan workable. If she micromanages, I start feeling useless. If she earns more than me, although that's not inherently problematic, it often becomes so, because she will naturally start to feel like she is the one who should make the decisions ("My house, my rules")."""

LEADERSHIP_MASTER_OLD = """She may know more than I do about any particular field, including a traditionally non-feminine one. Then I want her help. “Honey, let me help you with this,” is still sexy. Pushing me out of the way isn’t.

In my experience, women often prefer me to say what I want instead of hovering around it:

“This is where I want to go. This is what I think we should do. Are you game?”

She can improve the plan or say no. That doesn’t make it feel less masculine to me; I’m still offering a direction instead of waiting for her to pull one out of me.

I don’t need every role to be symmetrical either. If I like driving and she likes cooking, we can do that. If one of us is better at something, let that person do more of it. When I’m leading, I still want her ideas. Mandar obedeciendo, as the Zapatistas say.

## Not A Performance

The moment I have to prove that I’m the man, something has already become fake. Then every time I hesitate, cry, need help, or get something wrong, I have to defend the identity.

I don’t actually think of myself as especially masculine. I step into that energy when I see that a woman would appreciate it, and then it comes naturally. Bee once called me her “wife.” I don’t recommend that as a polarity exercise, by the way."""

LEADERSHIP_MASTER_NEW = """She may know much more than I do about some particular field, including a traditionally non-feminine one, and in that case I want her help. “Honey, let me help you with this,” can be very sexy, until helping turns into doing everything for me and I start feeling useless.

In my experience, women often prefer me to say directly where I want to go:

“This is where I want to go. This is what I think we should do. Are you game?”

She might have a better idea, or just not want to do it. Fine. I still like being the one who puts a direction out there.

I don't think equality means dividing every role 50/50. If I like driving and she likes cooking, great. If she's way better at something, she'll probably do more of it. When I'm leading, I still want to know what she sees. Mandar obedeciendo, as the Zapatistas say.

## Not A Performance

The moment I have to prove that I’m the man, something has already become fake.

I don’t actually walk around thinking I’m some super-masculine guy. I cry, I need help, I get things wrong. Bee once called me her “wife.” I don’t recommend that as a polarity exercise, by the way.

When a woman appreciates that masculine side of me, it tends to come out by itself."""

# The reader-visible Part 2 representation strips Markdown heading syntax and also
# removes the blank line immediately before this heading. Bind to that exact form.
LEADERSHIP_P2_OLD = LEADERSHIP_MASTER_OLD.replace("\n\n## Not A Performance\n\n", "\nNot A Performance\n\n")
LEADERSHIP_P2_NEW = LEADERSHIP_MASTER_NEW.replace("\n\n## Not A Performance\n\n", "\nNot A Performance\n\n")

EXCLUSIVITY_OLD = """Sexual exclusivity has a different history. A lot of that history runs through agriculture, property, and inheritance. By the Industrial Revolution, strict exclusivity had law and social pressure behind it as a mass norm. Tribal cultures across the world have generally been looser: a primary partnership could still leave accepted room for sexual or emotional connections outside it—what gets called “social monogamy.”

Marriage kept the property-and-inheritance job, and modern romantic vows gave it another one: promise that this feeling will last forever.

At one point I tried a more literal solution: stop being attracted to anyone else. B. wanted to marry me, but I was still attracted to other women. I told her, “It’s not fair of me to commit to you if I’m still attracted to other women, so before I do, let me see if I can fix that.”"""

EXCLUSIVITY_OWNER = '''It's hard to find sexually monogamous animals, have you ever looked? And as it turns out, we humans aren't a natural exception to the rule, either.  Plenty of tribal cultures were (and some still are) much looser about this, while still generally retaining the primary-partner "social monogamy."  Sexclusivity started gaining sway around the time we started planting carrots and peas, and owning land. That's when it made sense to keep track of how to keep our land in the family bloodline. By the Industrial Revolution, this ironically bureaucratic basis of romance became the only definition of marriage, by law.  I'm not trying to say we're just like bonobos, but the academic consensus is that humans  tend toward flexible pair-bonding, with a propensity for occasional infidelity. And now we've gone one step further, so that even the brief inkling of attraction to another person becomes almost a sure sign that sexual infidelity is next. That's why I felt I had no choice but to address the issue head on  when B. wanted to marry me. I told her, “I can't fully commit to you if I’m still attracted to other women, so before I do, let's see if I can fix that."'''

PINKEST_OLD = """Start with the pinkest elephants in the room:

“I don’t think we really trust each other.”

“I’m resentful about this.”

“I’m attracted to somebody else.”

“I don’t know whether I still want the same kind of relationship.”

See whether the other person will stay in the conversation. If they won’t, that tells you something another perfectly worded speech probably won’t fix."""

PINKEST_OWNER = """When did you two last dance? And not the “we dance around our problems” joke (LOL).. if that’s where things are at, the trust is out the window. Ouch. I know that one from experience with my first 2 wives and K, too. That generally marks the point of no return, so try not to wait for that. Because once you're there, as my dad explained a thousand times whenever we had a visitor, unconscious resentment begins to snowball, and we feel colder together than alone. Pretty soon, old Romeo & Juliette might get wandering eye syndrome."""

MASTER_REPLACEMENTS = [
    ("owner-muses-archetypes-and-polarity", base.MUSES_NEW, MUSES_OWNER),
    ("owner-accepted-leadership-rhythm", LEADERSHIP_MASTER_OLD, LEADERSHIP_MASTER_NEW),
    ("owner-exclusivity-history-and-B", EXCLUSIVITY_OLD, EXCLUSIVITY_OWNER),
    ("owner-pinkest-replacement", PINKEST_OLD, PINKEST_OWNER),
]

P2_REPLACEMENTS = [
    ("owner-muses-archetypes-and-polarity", base.MUSES_NEW, MUSES_OWNER),
    ("owner-accepted-leadership-rhythm", LEADERSHIP_P2_OLD, LEADERSHIP_P2_NEW),
    ("owner-exclusivity-history-and-B", EXCLUSIVITY_OLD, EXCLUSIVITY_OWNER),
    ("owner-pinkest-replacement", PINKEST_OLD, PINKEST_OWNER),
]

OWNER_REQUIRED = {
    "muses-archetypes": "I'm referring more to feminine vs masculine archetypes.",
    "muses-epistemic-friction": "seems often absurd, yet many times more accurate than what I could have figured",
    "muses-crucible": "that’s the Crucible safety problem I already talked about.",
    "muses-money-authority": "My house, my rules",
    "leadership-direct-offer": "This is where I want to go. This is what I think we should do. Are you game?",
    "leadership-equality": "I don't think equality means dividing every role 50/50.",
    "leadership-zapatista": "Mandar obedeciendo",
    "leadership-bee-wife": "Bee once called me her “wife.”",
    "leadership-natural-energy": "When a woman appreciates that masculine side of me, it tends to come out by itself.",
    "community-pass6": "Community isn't magic either",
    "exclusivity-live-opening": "It's hard to find sexually monogamous animals, have you ever looked?",
    "exclusivity-sexclusivity": "Sexclusivity started gaining sway",
    "exclusivity-industrial": "Industrial Revolution",
    "exclusivity-bonobo": "we're just like bonobos",
    "exclusivity-pair-bonding": "flexible pair-bonding",
    "exclusivity-B": "I can't fully commit to you if I’m still attracted to other women",
    "pinkest-dance": "When did you two last dance?",
    "pinkest-resentment": "unconscious resentment begins to snowball",
    "pinkest-wandering-eye": "wandering eye syndrome",
    "outside-help-heading": "Outside help can sometimes break the loop fast",
}


def audit(source: str, candidate: str) -> dict[str, object]:
    missing_protected = [
        name for name, anchor in base.helper.PROTECTED_ANCHORS.items() if anchor not in candidate
    ]
    missing_owner = [name for name, anchor in OWNER_REQUIRED.items() if anchor not in candidate]
    checks: dict[str, object] = {
        "headings_identical": base.helper.headings(source) == base.helper.headings(candidate),
        "native_markers_identical": base.helper.native_markers(source) == base.helper.native_markers(candidate),
        "markdown_link_destinations_identical": base.helper.markdown_links(source) == base.helper.markdown_links(candidate),
        "protected_anchors_missing": missing_protected,
        "owner_required_missing": missing_owner,
    }
    checks["passed"] = (
        bool(checks["headings_identical"])
        and bool(checks["native_markers_identical"])
        and bool(checks["markdown_link_destinations_identical"])
        and not missing_protected
        and not missing_owner
    )
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description="Materialize the Romance owner-integrated candidate from exact pass 6.")
    parser.add_argument("--pass6-master", type=Path, required=True)
    parser.add_argument("--pass6-part1", type=Path, required=True)
    parser.add_argument("--pass6-part2", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    master = args.pass6_master.read_text(encoding="utf-8")
    part1 = args.pass6_part1.read_text(encoding="utf-8")
    part2 = args.pass6_part2.read_text(encoding="utf-8")
    observed = {
        "master": base.helper.sha256_text(master),
        "part1": base.helper.sha256_text(part1),
        "part2": base.helper.sha256_text(part2),
    }
    expected = {
        "master": PASS6_MASTER_SHA,
        "part1": PASS6_P1_SHA,
        "part2": PASS6_P2_SHA,
    }
    if observed != expected:
        raise RuntimeError(f"pass-6 source hash mismatch: expected={expected} observed={observed}")

    candidate_master, master_ops = base.helper.apply_replacements(master, MASTER_REPLACEMENTS)
    candidate_part2, p2_ops = base.helper.apply_replacements(part2, P2_REPLACEMENTS)
    candidate_part1 = part1

    if base.helper.sha256_text(candidate_part1) != REGISTERED_P1_SHA:
        raise RuntimeError("Part 1 changed during owner integration; detector reuse is forbidden")

    checks = audit(master, candidate_master)
    if not checks["passed"]:
        raise RuntimeError(f"owner-integrated master invariant audit failed: {checks}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    out_master = args.output_dir / "candidate-master.md"
    out_p1 = args.output_dir / "candidate-part-1.txt"
    out_p2 = args.output_dir / "candidate-part-2.txt"
    out_master.write_text(candidate_master, encoding="utf-8")
    out_p1.write_text(candidate_part1, encoding="utf-8")
    out_p2.write_text(candidate_part2, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "status": "owner_integrated_candidate_not_owner_final_article",
        "source_pass6": observed,
        "candidate": {
            "master": {
                "path": out_master.name,
                "sha256": base.helper.sha256_text(candidate_master),
                "word_count_whitespace": len(candidate_master.split()),
                "operations": master_ops,
                "invariant_audit": checks,
            },
            "part1": {
                "path": out_p1.name,
                "sha256": base.helper.sha256_text(candidate_part1),
                "word_count_whitespace": len(candidate_part1.split()),
                "operations": [],
                "reuses_registered_detector_result": True,
            },
            "part2": {
                "path": out_p2.name,
                "sha256": base.helper.sha256_text(candidate_part2),
                "word_count_whitespace": len(candidate_part2.split()),
                "operations": p2_ops,
            },
        },
        "provenance": [
            {
                "label": "owner-muses-archetypes-and-polarity",
                "kind": "direct_owner_rewrite",
                "source": "OWNER-MUSES-REWRITE-LESSON-20260821.md",
                "normalization": ["as the grow -> as they grow", "she see sees -> she sees"],
            },
            {
                "label": "owner-accepted-leadership-rhythm",
                "kind": "assistant_produced_owner_accepted_provisional",
                "source": "OWNER-ACCEPTED-LEADERSHIP-REWRITE-20260821.md",
                "owner_reported_detector": "Pangram 4 100% high-confidence Human; residual AI feel still perceived by owner",
            },
            {
                "label": "owner-exclusivity-history-and-B",
                "kind": "direct_owner_rewrite",
                "source": "OWNER-EXCLUSIVITY-REWRITE-20260821.md",
                "owner_reported_detector": "Pangram 4 high-confidence Human on short local boundary",
            },
            {
                "label": "owner-pinkest-replacement",
                "kind": "owner_final_local_span",
                "source": "OWNER-PINKEST-REWRITE-20260821.md",
                "owner_reported_detector": "Pangram 4 Human / low confidence on 97-word natural-owner boundary",
            },
        ],
        "detector_plan": {
            "part1": "no_new_call_exact_registered_hash_unchanged",
            "part2": "no_automatic_paid_call_audit_cap_exhausted_6_of_6; use wider contiguous context for diagnostics; any seventh full-Part2 call requires explicit owner authorization",
        },
        "editorial_note": "This candidate deterministically integrates the owner-selected residual repairs into exact pass 6. It does not merge to canonical main, does not claim a new full-Part2 Pangram result, and preserves owner-final/natural-owner/owner-accepted provenance distinctions.",
    }
    (args.output_dir / "candidate-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
