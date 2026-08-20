#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

PART1_SHA = "ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8"
PART2_SHA = "2df878093bc05fefa98ca30e9a97bdd52e212370f432bf0408e90f1b60c54bb0"

PART1_REPLACEMENTS = [
    (
        "talk-before-sex-sex-drive-mismatch",
        """Sex drives are independently alive and always changing. For some stretch, one of you will want more, less, or something different. When the discordance comes, it's one of the saddest sources of quiet resentment. Talk about what you’ll do when that happens before either person is already hurt. It won’t solve it in advance, but at least you’ll have somewhere to begin.""",
        """Sex drives have lives of their own, and they change. For a while one of you may want more, less, or something different. That mismatch can turn into a lot of quiet resentment. Talk about what you’ll do when it happens before either person is already hurt. It won’t solve it in advance, but at least you’ll have somewhere to begin.""",
    ),
]

PART2_REPLACEMENTS = [
    (
        "spiritual-sex-source-progression",
        """She has collected a ton of stories from students who say those practices spilled over into their health, work, money, creativity, and the rest of life.

Her jade-egg practice is part of the same idea. It gives a woman a way to work with pelvic-floor strength, attention, and arousal when there isn’t a partner involved.

Brad and Pam Keene are an example I really like. Pam says her Kundalini process completed while they were making love and opened into a lasting universal-consciousness awakening. She later helped Brad awaken too, so the marriage itself became part of the path.""",
        """She has collected a ton of stories from students who say those practices spilled over into their health, work, money, creativity, and the rest of life. Her jade-egg practice takes the same idea into solo practice: pelvic-floor strength, attention, and arousal when there isn’t a partner involved.

Brad and Pam Keene are the example I really like. Pam says her Kundalini process completed while they were making love and opened into a lasting universal-consciousness awakening. She later helped Brad awaken too, so the marriage itself became part of the path.""",
    ),
    (
        "muses-directors-lived-thought",
        """Of course, some women barely have that poetic quality. Men can go into it too; artistic men often live much closer to it. But it’s one of the things I experience as highly feminine. She may be feeling or seeing something before either of us can explain it, while I’m already trying to turn it into prose: What happened? What does it mean? What are we going to do about it?

I think girls should be encouraged to develop that side without either having it trained out of them or letting it turn into helplessness and chaos. Boys need access to it too.

Toft’s fifty-year-marriage advice is basically the old Men Are from Mars, Women Are from Venus problem in lived form. She may want to talk and be heard while he immediately starts fixing. Men complain just to be heard too, although I think men are more often looking for a solution. The easy question is, “Do you want me to help figure this out, or do you mostly want me to listen?”

I can listen for the feeling without pretending every literal statement is true. If the intensity turns into intimidation, false accusations, or making somebody scared to say no, that’s the safety problem I already talked about in the Crucible.

Poetry still has to survive reality. The muse gives the director his ineffable inspiration. She sees the big picture or feels something that has not become a plan yet. Then I have a chance to be useful by figuring out the details.""",
        """Of course, some women barely have that poetic quality, and men can go there too; artistic men often live much closer to it. I still experience it as highly feminine. She may be feeling or seeing something before either of us can explain it, while I’m already trying to turn it into prose: What happened? What does it mean? What are we going to do about it?

I think girls should be encouraged to develop that side without having it trained out of them, but also without letting intuition turn into helplessness or chaos. Boys need access to it too.

Toft’s fifty-year-marriage advice is the old Men Are from Mars, Women Are from Venus problem in lived form. She may want to talk and be heard while he immediately starts fixing. Men complain just to be heard too, although I think men are more often looking for a solution. The easy question is, “Do you want me to help figure this out, or do you mostly want me to listen?”

I can listen for the feeling without pretending every literal statement is true. If the intensity turns into intimidation, false accusations, or making somebody scared to say no, that’s the safety problem I already talked about in the Crucible.

Poetry still has to survive reality. The muse may see the big picture or feel something before it has become a plan. Then I get to be useful by figuring out the details.""",
    ),
    (
        "primal-roles-remove-economy-analogy",
        """Equality in terms of dignity does not require both people to do every role equally.

Relationships work better when each person develops what they are good at, like specialization in any economy. That can be taken too far, of course. I’m not saying women should never learn to drive, nor that men should never cook. But if the man enjoys driving and the woman enjoys cooking, they can both usually do what makes them happiest.""",
        """Equality in dignity does not mean splitting every role equally.

Relationships usually work better when each person develops what they’re good at. I’m not saying women should never learn to drive, nor that men should never cook. But if the man enjoys driving and the woman enjoys cooking, they can both usually do what makes them happiest.""",
    ),
    (
        "not-a-performance-remove-duplicate-surrender",
        """The same is true for a woman. She should not have to perform softness, helplessness, or cuteness every minute to prove she is feminine. Surrender means so much more when she could take control but prefers not to at that moment.""",
        """The same is true for a woman. She should not have to perform softness, helplessness, or cuteness every minute to prove she is feminine.""",
    ),
    (
        "not-a-performance-gently-recurrence",
        """We can invite these energies out of each other gently.""",
        """We can invite these energies out of each other.""",
    ),
    (
        "after-leaving-direct-thought",
        """Often times the breakup is hard, but the aftermath is worse. Public demonization should be avoided, but that doesn't mean you should hide the truth about the relationship just to save face. Sometimes the truth is abuse, coercion, or serious deception. How much you say, who you say it to, and how public you make it depends on what happened and why you are telling people.

Part of that truth-telling is that a breakup can also expose things you genuinely couldn't see while you were bonded. Make sure to look at yourself as much as you look at them, to see what you honestly contributed to the problems. Try to see your ex's perspective in so far as it may have had some kernels of truth, including their own internal conflicts, rather than one-dimensionalizing them.

Don’t jump straight to the conclusion that they were fake all along merely because that story makes the whole relationship easier to explain. Don’t rule it out either if it is actually the most parsimonious explanation. Seek opinions from people who aren’t heavily invested in seeing your innocence. A therapist, a pastor, or even a stranger can sometimes look at the evidence more clearly than a lifelong friend, and even the curiosity itself can be therapeutic for you.""",
        """Often times the breakup is hard, but the aftermath is worse. Public demonization should be avoided, but I don't think that means hiding the truth about the relationship to save face. Sometimes the truth is abuse, coercion, or serious deception. How much you say, to whom, and how publicly depends on what happened and why you're telling people.

A breakup can expose things you genuinely couldn't see while you were bonded. Look at what you contributed, but also try to understand whatever was true in your ex's perspective, including the conflicts they were carrying inside themselves. Don't flatten them into one character just because the relationship ended.

Sometimes the easiest story is that they were fake all along. Don’t grab that story just because it makes everything easier to explain, and don’t reject it if it really is the most parsimonious explanation. Ask people who aren’t heavily invested in seeing your innocence. A therapist, pastor, or even a stranger may see the evidence more clearly than a lifelong friend. Staying curious about what happened can be therapeutic in itself.""",
    ),
    (
        "after-leaving-spiritual-opening",
        """Spiritual practice during an ending is critical, but it shouldn't be about bypassing your feelings. Pray for your ex's wellbeing. Remember what was real and good, and refuse to use your pain as permission to hate them. Avoid the New Age belief that everyone is simply a mirror of you. No, that isn’t true. We partly mirror one another, but each person is also their own unique person, forged from their own influences apart from you.""",
        """Spiritual practice during an ending is critical, but don't use it to get around the feelings. Pray for your ex's wellbeing. Remember what was real and good, and don't use your pain as permission to hate them. Avoid the New Age belief that everyone is simply a mirror of you. No, that isn’t true. We partly mirror one another, but each person was formed by plenty that had nothing to do with you.""",
    ),
]


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def apply_replacements(text: str, replacements: list[tuple[str, str, str]]) -> tuple[str, list[dict[str, object]]]:
    audit: list[dict[str, object]] = []
    for label, old, new in replacements:
        occurrences = text.count(old)
        if occurrences != 1:
            raise RuntimeError(f"{label}: expected exactly one source occurrence, found {occurrences}")
        before_sha = sha256_text(old)
        after_sha = sha256_text(new)
        text = text.replace(old, new, 1)
        audit.append(
            {
                "label": label,
                "source_occurrences": occurrences,
                "old_sha256": before_sha,
                "new_sha256": after_sha,
            }
        )
    return text, audit


def main() -> int:
    parser = argparse.ArgumentParser(description="Materialize accepted Romance detector-repair pass 1.")
    parser.add_argument("--part1", type=Path, required=True)
    parser.add_argument("--part2", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    part1 = args.part1.read_text(encoding="utf-8")
    part2 = args.part2.read_text(encoding="utf-8")

    observed1 = sha256_text(part1)
    observed2 = sha256_text(part2)
    if observed1 != PART1_SHA:
        raise RuntimeError(f"Part 1 baseline hash mismatch: {observed1}")
    if observed2 != PART2_SHA:
        raise RuntimeError(f"Part 2 baseline hash mismatch: {observed2}")

    candidate1, audit1 = apply_replacements(part1, PART1_REPLACEMENTS)
    candidate2, audit2 = apply_replacements(part2, PART2_REPLACEMENTS)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    out1 = args.output_dir / "candidate-part-1.txt"
    out2 = args.output_dir / "candidate-part-2.txt"
    manifest_path = args.output_dir / "candidate-halves-manifest.json"

    out1.write_text(candidate1, encoding="utf-8")
    out2.write_text(candidate2, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "status": "candidate_not_owner_final",
        "source": {
            "part1_sha256": PART1_SHA,
            "part2_sha256": PART2_SHA,
        },
        "candidate": {
            "part1": {
                "path": out1.name,
                "sha256": sha256_text(candidate1),
                "word_count_whitespace": len(candidate1.split()),
                "operations": audit1,
            },
            "part2": {
                "path": out2.name,
                "sha256": sha256_text(candidate2),
                "word_count_whitespace": len(candidate2.split()),
                "operations": audit2,
            },
        },
        "detector_note": (
            "These are the same fixed historical half boundaries with accepted surgical edits applied in place. "
            "No detector result is implied until each exact candidate file is measured."
        ),
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
