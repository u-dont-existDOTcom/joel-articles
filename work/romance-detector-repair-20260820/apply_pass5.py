#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

PASS4_MASTER_SHA = "b1541c6b6aee5cf289bc50d00ae6422b681fc6f64327729cd2f03a00bef3c779"
PASS4_P1_SHA = "ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8"
PASS4_P2_SHA = "a21b9670bc0cc61b4fc850761ca57ffa5dc5d1a02bdd5df90b820d6f9d437a0e"
REGISTERED_P1_SHA = PASS4_P1_SHA

ANAMI_OLD = """She has collected a ton of stories from students who say those practices spilled over into their health, work, money, creativity, and the rest of life. Her jade-egg practice takes the same idea into solo practice: pelvic-floor strength, attention, and arousal when there isn’t a partner involved."""
ANAMI_NEW = """She also has a ton of student stories where the effects spill out of sex into health, work, money, creativity, the rest of life. Her jade-egg practice is basically the solo version: pelvic-floor strength, attention, and arousal without needing a partner."""

MUSES_OLD = """Toft’s fifty-year-marriage advice is the old Men Are from Mars, Women Are from Venus problem in lived form. She may want to talk and be heard while he immediately starts fixing. Men complain just to be heard too, although I think men are more often looking for a solution. The easy question is, “Do you want me to help figure this out, or do you mostly want me to listen?”

I can listen for the feeling without pretending every literal statement is true. If the intensity turns into intimidation, false accusations, or making somebody scared to say no, that’s the safety problem I already talked about in the Crucible.

Poetry still has to survive reality. The muse may see the big picture or feel something before it has become a plan. Then I get to be useful by figuring out the details.

The muse can influence any decision where I ask for help, and also the decisions where she suddenly intuits that she has something important to add.

If she keeps taking over with “Let me do it,” I start feeling useless. Money can make the same thing worse. A woman earning more than me isn’t the problem; turning it into “I make more, so I’m the competent adult here” can effeminate me in the relationship. A man can wreck it from the other side by needing a successful woman to shrink so he can feel masculine."""
MUSES_NEW = """Toft’s fifty-year-marriage advice is the old Men Are from Mars, Women Are from Venus problem in lived form. She may want to talk and be heard while he starts fixing. Men do this too, although I think men are more often looking for the solution. So I ask, “Do you want me to help figure this out, or do you mostly want me to listen?”

I can listen to the feeling without agreeing with every literal statement. If it turns into intimidation, false accusations, or making somebody scared to say no, that’s no longer poetry. That’s the Crucible safety problem I already talked about.

The part I like is when she sees something before it has become a plan and I get to figure out the details. She can influence the direction without taking over the whole thing. If she keeps saying “Let me do it,” I start feeling useless.

Money can create the same dynamic. A woman earning more than me doesn’t bother me. Using it as proof that she’s the competent adult can effeminate me in the relationship. A man can wreck the polarity from the other side by needing a successful woman to shrink so he can feel masculine."""

PRIMAL_PERFORMANCE_OLD = """She may argue with the plan, change it, improve it, or refuse it. The masculine charge comes partly from directly offering a direction.

Equality in dignity does not mean splitting every role equally.

Relationships usually work better when each person develops what they’re good at. I’m not saying women should never learn to drive, nor that men should never cook. But if the man enjoys driving and the woman enjoys cooking, they can both usually do what makes them happiest.

Every respectful leader makes sure to take the other person’s ideas as serious input. Mandar obedeciendo, as the Zapatistas say.

The point is not to tally every act and force the totals to match.
Not A Performance

I also don’t want masculinity or femininity to become an identity performance.

The moment I have to prove that I’m the man, something has already become fake. Then I have to defend the identity every time I hesitate, cry, need help, or get something wrong.

I don’t actually think of myself as especially masculine. I step into that energy when I see that a woman would appreciate it, and then it comes naturally. Bee once called me her “wife.” I don’t recommend that as a polarity exercise, by the way.

The same is true for a woman. She should not have to perform softness, helplessness, or cuteness every minute to prove she is feminine.

Women can get pulled in two directions here. She may worry that I don’t find her beautiful enough, or that she’s too emotional, too difficult, not logical enough, or too needy. Then she can overcorrect into needing nobody and make receiving care or letting a man lead feel like weakness.

Toft’s advice after fifty years is simple: tell her she’s beautiful, and keep noticing new kinds of beauty as she ages. Anami makes the other half explicit: receiving is a skill. Letting a man help, lead, or give her pleasure doesn’t make a strong woman helpless. A man receiving care doesn’t make him a child either.

We can invite these energies out of each other.

“Honey, how do you see this intuitively?”

or, “Can you help me think through the practical side for a minute?”

That feels much better than, “Do your female/male thing now.”

When a strong woman surrenders, she is choosing to, which is sexy. She knows she could drive, but she asks you to drive, because she likes how it feels when you do."""
PRIMAL_PERFORMANCE_NEW = """She can argue with the plan, improve it, or say no. For me that doesn’t kill the masculine charge. Part of the charge is actually offering a direction instead of waiting for her to pull one out of me.

I don’t think equal dignity means splitting every role down the middle. I’d rather each of us do more of what we’re actually good at. If I like driving and she likes cooking, great. If it’s the reverse, great too. Whatever I’m leading, her ideas still matter. Mandar obedeciendo, as the Zapatistas say. I don’t need us to keep score.
Not A Performance

The moment I have to prove that I’m the man, something has already become fake. Then every time I hesitate, cry, need help, or get something wrong, I have to defend the identity.

I don’t actually think of myself as especially masculine. I step into that energy when I see that a woman would appreciate it, and then it comes naturally. Bee once called me her “wife.” I don’t recommend that as a polarity exercise, by the way.

A woman shouldn’t have to act soft, helpless, or cute every minute either. She can get pushed in the opposite direction too: if she’s spent years worrying that she isn’t beautiful enough, or that she’s too emotional, too difficult, not logical enough, or too needy, she may overcorrect into needing nobody. Then receiving care or letting a man lead starts to feel like weakness.

Toft’s advice after fifty years is simple: tell her she’s beautiful, and keep noticing new kinds of beauty as she ages. Anami emphasizes learning to receive. Letting a man help, lead, or give her pleasure doesn’t make a strong woman helpless. A man receiving care doesn’t make him a child either.

We can invite these energies out of each other:
“Honey, how do you see this intuitively?”
or, “Can you help me think through the practical side for a minute?”

When a strong woman surrenders, she is choosing to. She knows she could drive; she asks me to drive because she likes how it feels when I do. That’s sexy."""

CHOOSING_OLD = """“We’re together” ... what does that mean exactly? I can hear a whole future in those two words—sex, exclusivity, living together, money, children, caregiving—while she may only mean that we really like each other and want to see what happens. Sometimes I like letting a relationship flow without naming every part.
The problem is when we’re both flowing along and imagining different things."""
CHOOSING_NEW = """“We’re together” ... what does that mean exactly? I might hear sex, exclusivity, living together, money, children, caregiving in those two words. She might mean, “We really like each other; let’s see what happens.” I actually like letting a relationship flow without naming every part. The problem is when we’re using the same words for two different futures."""

EXCLUSIVITY_HISTORY_OLD = """Sexual exclusivity has a different history. Strict sexual exclusivity backed by law and social enforcement grew alongside agriculture, settled property, and inheritance, and became a mass norm during the Industrial Revolution. Tribal cultures across the world have generally had more flexible forms of primary partnership, or 'social monogamy,' with accepted ways for sexual or emotional connection to exist outside it.

Marriage still carries the property-and-inheritance structure while modern vows also ask it to guarantee a permanent romantic feeling."""
EXCLUSIVITY_HISTORY_NEW = """Sexual exclusivity has a different history. Strict exclusivity backed by law and social enforcement grew alongside agriculture, settled property, and inheritance; by the Industrial Revolution it had become a mass norm. Tribal cultures across the world have generally been more flexible, with primary partnerships or “social monogamy” that still allowed accepted sexual or emotional connections outside them.

Marriage still carries that property-and-inheritance job, while modern vows pile a second job on top: guarantee a permanent romantic feeling."""

P2_REPLACEMENTS = [
    ("anami-stories-solo-progression", ANAMI_OLD, ANAMI_NEW),
    ("muses-listening-safety-competence-chain", MUSES_OLD, MUSES_NEW),
    ("primal-performance-lived-chain", PRIMAL_PERFORMANCE_OLD, PRIMAL_PERFORMANCE_NEW),
    ("choosing-same-words-different-futures", CHOOSING_OLD, CHOOSING_NEW),
    ("exclusivity-history-conversational", EXCLUSIVITY_HISTORY_OLD, EXCLUSIVITY_HISTORY_NEW),
]

PROTECTED_ANCHORS = {
    "opening-father-question": "I asked my dad about sex when I was five",
    "bear-terminal-callback": "Bear, sex can be what you do when you’re older",
    "agape-eros-distinction": "Agape or divine love does two jobs at once to rescue the erotic love.",
    "coercion-exits-mutual-crucible": "If you're scared to say no, scared to tell the truth, or scared of what happens if you leave",
    "children-survive-romance": "Never recruit children into the adult war.",
    "community-around-dyad": "Two Pillars Don't Hold The Roof Up",
    "primal-owner-argument": "Primal attraction: channeling the Divine Masculine & Feminine",
    "gandarussa-preserved": "Gandarussa",
    "identity-hale-not-heidi": "A friend of mine was talking about PTSD recently",
}

PASS5_REQUIRED = {
    "anami-source": "She also has a ton of student stories",
    "jade-egg": "Her jade-egg practice is basically the solo version",
    "crucible-local-safety": "That’s the Crucible safety problem I already talked about.",
    "money-polarity": "effeminate me in the relationship",
    "successful-woman-reverse": "successful woman to shrink so he can feel masculine",
    "direct-direction": "This is where I want to go. This is what I think we should do. Are you game?",
    "zapatista-leadership": "Mandar obedeciendo",
    "bee-wife": "Bee once called me her “wife.”",
    "toft-beauty": "Toft’s advice after fifty years is simple",
    "anami-receiving": "Anami emphasizes learning to receive.",
    "chosen-surrender": "When a strong woman surrenders, she is choosing to.",
    "agreement-ambiguity": "same words for two different futures",
    "exclusivity-agriculture": "agriculture, settled property, and inheritance",
    "exclusivity-industrial": "Industrial Revolution",
    "social-monogamy": "social monogamy",
    "permanent-feeling": "guarantee a permanent romantic feeling",
}


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def apply_replacements(text: str, replacements: list[tuple[str, str, str]]) -> tuple[str, list[dict[str, object]]]:
    audit: list[dict[str, object]] = []
    for label, old, new in replacements:
        count = text.count(old)
        if count != 1:
            raise RuntimeError(f"{label}: expected exactly one occurrence, found {count}")
        text = text.replace(old, new, 1)
        audit.append({
            "label": label,
            "source_occurrences": count,
            "old_sha256": sha256_text(old),
            "new_sha256": sha256_text(new),
        })
    return text, audit


def headings(text: str) -> list[str]:
    return [line for line in text.splitlines() if re.match(r"^#{1,6}\s", line)]


def native_markers(text: str) -> list[str]:
    return [line for line in text.splitlines() if line.startswith("[NATIVE ")]


def markdown_links(text: str) -> list[str]:
    return re.findall(r"\]\(([^)]+)\)", text)


def audit_master(source: str, candidate: str) -> dict[str, object]:
    missing = [name for name, anchor in PROTECTED_ANCHORS.items() if anchor not in candidate]
    pass5_missing = [name for name, anchor in PASS5_REQUIRED.items() if anchor not in candidate]
    checks = {
        "headings_identical": headings(source) == headings(candidate),
        "native_markers_identical": native_markers(source) == native_markers(candidate),
        "markdown_link_destinations_identical": markdown_links(source) == markdown_links(candidate),
        "protected_anchors_missing": missing,
        "pass5_required_missing": pass5_missing,
    }
    checks["passed"] = (
        checks["headings_identical"]
        and checks["native_markers_identical"]
        and checks["markdown_link_destinations_identical"]
        and not missing
        and not pass5_missing
    )
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description="Materialize Romance detector-repair pass 5.")
    parser.add_argument("--pass4-master", type=Path, required=True)
    parser.add_argument("--pass4-part1", type=Path, required=True)
    parser.add_argument("--pass4-part2", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    master = args.pass4_master.read_text(encoding="utf-8")
    part1 = args.pass4_part1.read_text(encoding="utf-8")
    part2 = args.pass4_part2.read_text(encoding="utf-8")

    observed = {
        "master": sha256_text(master),
        "part1": sha256_text(part1),
        "part2": sha256_text(part2),
    }
    expected = {
        "master": PASS4_MASTER_SHA,
        "part1": PASS4_P1_SHA,
        "part2": PASS4_P2_SHA,
    }
    if observed != expected:
        raise RuntimeError(f"pass-4 source hash mismatch: expected={expected} observed={observed}")

    master5, master_ops = apply_replacements(master, P2_REPLACEMENTS)
    part2_5, p2_ops = apply_replacements(part2, P2_REPLACEMENTS)
    part1_5 = part1

    if sha256_text(part1_5) != REGISTERED_P1_SHA:
        raise RuntimeError("Part 1 changed during pass 5; detector submission is forbidden")

    checks = audit_master(master, master5)
    if not checks["passed"]:
        raise RuntimeError(f"pass-5 master invariant audit failed: {checks}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    out_master = args.output_dir / "candidate-master.md"
    out_p1 = args.output_dir / "candidate-part-1.txt"
    out_p2 = args.output_dir / "candidate-part-2.txt"
    manifest_path = args.output_dir / "candidate-manifest.json"

    out_master.write_text(master5, encoding="utf-8")
    out_p1.write_text(part1_5, encoding="utf-8")
    out_p2.write_text(part2_5, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "status": "candidate_not_owner_final",
        "source_pass4": observed,
        "candidate": {
            "master": {
                "path": out_master.name,
                "sha256": sha256_text(master5),
                "word_count_whitespace": len(master5.split()),
                "operations": master_ops,
                "invariant_audit": checks,
            },
            "part1": {
                "path": out_p1.name,
                "sha256": sha256_text(part1_5),
                "word_count_whitespace": len(part1_5.split()),
                "operations": [],
                "reuses_registered_detector_result": True,
            },
            "part2": {
                "path": out_p2.name,
                "sha256": sha256_text(part2_5),
                "word_count_whitespace": len(part2_5.split()),
                "operations": p2_ops,
            },
        },
        "detector_plan": {
            "part1": "no_new_call_exact_registered_hash_unchanged",
            "part2": "one_new_pangram4_measurement_via_private_selfhost",
        },
        "editorial_note": (
            "Pass 5 is routed from the five exact AI windows returned by the successful self-hosted pass-4 Pangram-4 result. "
            "It removes source-inventory/explanatory packaging, repairs the Muses-to-competence thought chain, keeps the owner's "
            "masculine/feminine polarity and chosen-surrender claims, turns relationship-label ambiguity into two concrete imagined "
            "meanings, and preserves the historical exclusivity argument while making its movement less textbook-like."
        ),
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
