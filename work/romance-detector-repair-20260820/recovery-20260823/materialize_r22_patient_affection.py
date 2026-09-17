from __future__ import annotations

import base64
import hashlib
import json
import re
import urllib.request
from pathlib import Path


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def words(text: str) -> int:
    return len(text.split())


MASTER_PATH = Path(
    "work/romance-detector-repair-20260820/"
    "materialized-preservation-r20-casual-two-deletions/candidate-master.md"
)
EXPECTED_MASTER_SHA = "8b60f2916a4c050c6295b858889c3a7e3e80c87e18307a2c3e2cf9e276e8637d"
PART1_BLOB_SHA = "7982862512ad6dae2b3573af23b410442eb047b5"
EXPECTED_PART1_SHA = "04ea13442d4044ee56733b75771cb62c5cd44ba1b5da1bbb57d637c4f2ec4316"

PATIENT_OLD = '''All three women told me at some point that they felt like my patient. Which is true, I really was the one they asked about almost every medical, mental-health, and practical problem:

“I’m sick. What should I take?”

“I’m sad. What should I do?”

Of course I helped. Saying, “I’m not your doctor or therapist,” every time would have been cold. But enough moments become a pattern.'''

PATIENT_NEW = '''All three women told me at some point that they felt like my patient, and I couldn't exactly argue with them. They asked me about almost every medical, mental-health, and practical problem:

“I’m sick. What should I take?”

“I’m sad. What should I do?”

I usually had some idea, so of course I answered. But enough moments become a pattern.'''

AFFECTION_OLD_MD = '''## Affection and the simmer

Doug Toft, who has been married for fifty years, has a useful list called [*50 Things I Learned from 50 Years of Marriage*](https://dougtoft.substack.com/p/50-things-i-learned-from-50-years). One of his points is to touch his wife without an agenda. A hug, cuddle, kiss, or back rub should sometimes be allowed to end right there. If every affectionate touch becomes a bid for sex, affection itself can start feeling like pressure.

The opposite failure is letting the erotic current disappear except when somebody officially initiates sex. Kim Anami calls the current between encounters [“the simmer”](https://kimanami.com/meet-another-well-fked-man/). Maybe she texts from work, “I can’t wait to touch you.” Maybe he tells her what he wants to do later. It shouldn’t become relationship homework. But if two people who supposedly want each other barely flirt, tease, or show desire through the day, I would take that as a warning light rather than expect great sex to materialize from zero at bedtime.

You need both. Affection has to be safe from escalation, and the erotic current has to stay alive.

Sex can also be a barometer for whatever else is happening between you. If the sex changes, ask what else changed: resentment, closeness, stress, health, medication, or how wanted each person feels.

Each person has some responsibility for staying sexually alive too. My partner matters enormously, but she shouldn’t have to manufacture all my desire for me. And if sex is one of the main things separating this relationship from friendship, it probably deserves more than whatever exhausted time is left after everything else.'''

AFFECTION_NEW_MD = '''## Affection and the simmer

Doug Toft, who has been married for fifty years, has a useful list called [*50 Things I Learned from 50 Years of Marriage*](https://dougtoft.substack.com/p/50-things-i-learned-from-50-years). One of his points is to touch his wife without an agenda. A hug, cuddle, kiss, or back rub should sometimes be allowed to end right there. If every affectionate touch becomes a bid for sex, affection itself can start feeling like pressure.

Kim Anami calls the sexual current between encounters [“the simmer”](https://kimanami.com/meet-another-well-fked-man/). Maybe she texts from work, “I can’t wait to touch you.” Maybe he tells her what he wants to do later. If we supposedly want each other but hardly ever flirt or let each other know it, I think something is already wrong. Great sex probably isn't going to materialize out of nowhere at bedtime.

And if our sex life suddenly changes, I want to know what changed. Maybe we're pissed off at each other. Maybe somebody's sick, stressed, on a new medication, whatever.

I also don't want my partner to have to manufacture my desire for me. And if sex is one of the main things separating our relationship from friendship, giving it whatever exhausted scraps are left after everything else seems pretty dumb.'''

AFFECTION_OLD_PLAIN = '''Affection and the simmer

Doug Toft, who has been married for fifty years, has a useful list called 50 Things I Learned from 50 Years of Marriage. One of his points is to touch his wife without an agenda. A hug, cuddle, kiss, or back rub should sometimes be allowed to end right there. If every affectionate touch becomes a bid for sex, affection itself can start feeling like pressure.

The opposite failure is letting the erotic current disappear except when somebody officially initiates sex. Kim Anami calls the current between encounters “the simmer”. Maybe she texts from work, “I can’t wait to touch you.” Maybe he tells her what he wants to do later. It shouldn’t become relationship homework. But if two people who supposedly want each other barely flirt, tease, or show desire through the day, I would take that as a warning light rather than expect great sex to materialize from zero at bedtime.

You need both. Affection has to be safe from escalation, and the erotic current has to stay alive.

Sex can also be a barometer for whatever else is happening between you. If the sex changes, ask what else changed: resentment, closeness, stress, health, medication, or how wanted each person feels.

Each person has some responsibility for staying sexually alive too. My partner matters enormously, but she shouldn’t have to manufacture all my desire for me. And if sex is one of the main things separating this relationship from friendship, it probably deserves more than whatever exhausted time is left after everything else.'''

AFFECTION_NEW_PLAIN = '''Affection and the simmer

Doug Toft, who has been married for fifty years, has a useful list called 50 Things I Learned from 50 Years of Marriage. One of his points is to touch his wife without an agenda. A hug, cuddle, kiss, or back rub should sometimes be allowed to end right there. If every affectionate touch becomes a bid for sex, affection itself can start feeling like pressure.

Kim Anami calls the sexual current between encounters “the simmer”. Maybe she texts from work, “I can’t wait to touch you.” Maybe he tells her what he wants to do later. If we supposedly want each other but hardly ever flirt or let each other know it, I think something is already wrong. Great sex probably isn't going to materialize out of nowhere at bedtime.

And if our sex life suddenly changes, I want to know what changed. Maybe we're pissed off at each other. Maybe somebody's sick, stressed, on a new medication, whatever.

I also don't want my partner to have to manufacture my desire for me. And if sex is one of the main things separating our relationship from friendship, giving it whatever exhausted scraps are left after everything else seems pretty dumb.'''


def fetch_part1() -> str:
    url = (
        "https://api.github.com/repos/u-dont-existDOTcom/pangram-humanization-lab/"
        f"git/blobs/{PART1_BLOB_SHA}"
    )
    with urllib.request.urlopen(url, timeout=60) as response:
        blob = json.load(response)
    text = base64.b64decode(blob["content"]).decode("utf-8")
    actual = sha(text)
    if actual != EXPECTED_PART1_SHA:
        raise SystemExit(f"r20 Part1 SHA mismatch: {actual}")
    return text


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"expected {label} exactly once, found {count}")
    return text.replace(old, new, 1)


def main() -> None:
    master = MASTER_PATH.read_text(encoding="utf-8")
    actual_master_sha = sha(master)
    if actual_master_sha != EXPECTED_MASTER_SHA:
        raise SystemExit(f"r20 Markdown SHA mismatch: {actual_master_sha}")

    candidate = replace_once(master, PATIENT_OLD, PATIENT_NEW, "patient source in Markdown")
    candidate = replace_once(candidate, AFFECTION_OLD_MD, AFFECTION_NEW_MD, "Affection source in Markdown")

    protected_anchors = [
        "Sex is what you do when you are older and you find a friend you want to have children with.",
        "It's important to talk about sexual compatibility before getting undressed, even if that kills the vibe.",
        "Your body doesn’t know that you picked someone up at a bar and agreed it was only for fun.",
        "If you’re both really numb or robotic about sex, maybe not.",
        "[Gandarussa](https://thediplomat.com/2013/09/a-male-contraceptive-pill-for-indonesia/)",
        'Key at first asked me innocently, "Can you be my guru?"',
        "I know what can happen on my side. Helping feels good. Being needed can feel good too.",
        "## Can Casual Sex or a Situationship Actually Be Honest?",
        "## Different levels in different domains can be complementary",
    ]
    missing = [anchor for anchor in protected_anchors if anchor not in candidate]
    if missing:
        raise SystemExit(f"protected Markdown anchors missing: {missing}")

    forbidden = [
        "The opposite failure is letting the erotic current disappear except when somebody officially initiates sex.",
        "It shouldn’t become relationship homework.",
        "You need both. Affection has to be safe from escalation, and the erotic current has to stay alive.",
        "Saying, “I’m not your doctor or therapist,” every time would have been cold.",
    ]
    surviving = [item for item in forbidden if item in candidate]
    if surviving:
        raise SystemExit(f"superseded prose survived: {surviving}")

    native_source = master.count("[NATIVE ")
    native_candidate = candidate.count("[NATIVE ")
    if native_source != native_candidate:
        raise SystemExit(f"native object count changed {native_source}->{native_candidate}")
    link_re = re.compile(r"\[[^\]]+\]\([^\)]+\)")
    links_source = len(link_re.findall(master))
    links_candidate = len(link_re.findall(candidate))
    if links_source != links_candidate:
        raise SystemExit(f"Markdown link count changed {links_source}->{links_candidate}")

    part1 = fetch_part1()
    part1_candidate = replace_once(part1, PATIENT_OLD, PATIENT_NEW, "patient source in Part1")
    part1_candidate = replace_once(
        part1_candidate,
        AFFECTION_OLD_PLAIN,
        AFFECTION_NEW_PLAIN,
        "Affection source in Part1",
    )

    output_dir = Path(
        "work/romance-detector-repair-20260820/"
        "materialized-preservation-r22-patient-affection"
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    candidate_path = output_dir / "candidate-master.md"
    part1_path = output_dir / "part1.txt"
    candidate_path.write_text(candidate, encoding="utf-8")
    part1_path.write_text(part1_candidate, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "candidate_id": "romance-detector-repair-20260820-r22-patient-affection",
        "base_master": {
            "path": str(MASTER_PATH),
            "sha256": EXPECTED_MASTER_SHA,
            "word_count_whitespace": words(master),
        },
        "candidate_master": {
            "path": str(candidate_path),
            "sha256": sha(candidate),
            "word_count_whitespace": words(candidate),
        },
        "base_part1": {
            "git_blob_sha": PART1_BLOB_SHA,
            "sha256": EXPECTED_PART1_SHA,
            "word_count_whitespace": words(part1),
        },
        "candidate_part1": {
            "path": str(part1_path),
            "sha256": sha(part1_candidate),
            "word_count_whitespace": words(part1_candidate),
        },
        "operations": [
            {
                "id": "CH-R22-01",
                "type": "owner-accepted-patient-replacement",
                "old_sha256": sha(PATIENT_OLD),
                "new_sha256": sha(PATIENT_NEW),
            },
            {
                "id": "CH-R22-02",
                "type": "owner-accepted-holistic-Affection-repair",
                "old_markdown_sha256": sha(AFFECTION_OLD_MD),
                "new_markdown_sha256": sha(AFFECTION_NEW_MD),
                "old_plain_sha256": sha(AFFECTION_OLD_PLAIN),
                "new_plain_sha256": sha(AFFECTION_NEW_PLAIN),
            },
        ],
        "native_object_count_source": native_source,
        "native_object_count_candidate": native_candidate,
        "markdown_link_count_source": links_source,
        "markdown_link_count_candidate": links_candidate,
        "section_order_changed": False,
        "unexplained_deltas": 0,
        "part2_sha256": "9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85",
        "part2_exact_prior_human": 1.0,
        "canonical_main_changed": False,
        "status": "task candidate only; final preservation receipt required before detector submission",
    }
    (output_dir / "candidate-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
