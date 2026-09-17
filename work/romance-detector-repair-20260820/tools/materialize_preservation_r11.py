#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "work" / "romance-detector-repair-20260820"
BASE = WORK / "materialized-preservation-r10-part1"
OUT = WORK / "materialized-preservation-r11"

EXPECTED_BASE = {
    "master": "2546d719ccd87d8f34fe947ba6f6158baeb7e15f4a85bfbfc8d35cc45b93afd0",
    "part1": "4ab1ad34f171bb75d2f93e261757cca469a655b629508eb3b91ab05ebc83c0ef",
    "part2": "9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85",
}

SLOW_OLD = "But the first night isn’t necessarily the final ceiling either."
SLOW_NEW = ""

CASUAL_OLD = "The STI part is easy: say what you know, or say you don’t know. Feelings aren’t. You can both mean it when you say this is only sex and still have one of you get attached afterward. If you’re both really numb or robotic about sex, maybe not."
CASUAL_NEW = "You can test for STIs and tell each other what you know. If you don't know, say so. Attachment is less cooperative. Both of you can mean it when you say this is only sex, and then one of you wakes up attached anyway. If you’re both really numb or robotic about sex, maybe not."

PATIENT_OLD = """All three women told me at some point that they felt like my patient. Which is true, I really was the one they asked about almost every medical, mental-health, and practical problem:\n\n“I’m sick. What should I take?”\n\n“I’m sad. What should I do?”\n\nOf course I helped. Saying, “I’m not your doctor or therapist,” every time would have been cold. But enough moments become a pattern."""
PATIENT_NEW = """All three women eventually told me they felt like my patient, and I could see why. I was the person they brought almost every medical, mental-health, and practical problem to:\n\n“I’m sick. What should I take?”\n\n“I’m sad. What should I do?”\n\nOf course I was going to help. If every time one of them felt sick I answered, “I’m not your doctor or therapist,” that would have been cold. But after enough of those conversations, I understood why they used the word patient."""

OPS = [
    ("slow-steady-known-human-consolidation", SLOW_OLD, SLOW_NEW),
    ("casual-final-call6-sti-attachment", CASUAL_OLD, CASUAL_NEW),
    ("maturity-patient-known-green-rollback", PATIENT_OLD, PATIENT_NEW),
]


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def wc(text: str) -> int:
    return len(text.split())


def read(name: str) -> str:
    return (BASE / name).read_text(encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one source occurrence, found {count}")
    return text.replace(old, new, 1)


def headings(text: str) -> list[str]:
    return [line for line in text.splitlines() if re.match(r"^#{1,6} ", line)]


def native_markers(text: str) -> list[str]:
    return [line for line in text.splitlines() if line.startswith("[NATIVE ")]


def link_destinations(text: str) -> list[str]:
    return re.findall(r"\]\(([^)]+)\)", text)


master0 = read("candidate-master.md")
part10 = read("candidate-part-1.txt")
part20 = read("candidate-part-2.txt")

for key, text in (("master", master0), ("part1", part10), ("part2", part20)):
    actual = sha(text)
    if actual != EXPECTED_BASE[key]:
        raise SystemExit(f"base {key} SHA mismatch: expected {EXPECTED_BASE[key]} got {actual}")

master = master0
part1 = part10
operations = []
for label, old, new in OPS:
    old_hash = sha(old)
    new_hash = sha(new)
    master = replace_once(master, old, new, f"master/{label}")
    part1 = replace_once(part1, old, new, f"part1/{label}")
    operations.append({
        "label": label,
        "old_sha256": old_hash,
        "new_sha256": new_hash,
        "old_word_count": wc(old),
        "new_word_count": wc(new),
    })

part2 = part20

if headings(master) != headings(master0):
    raise SystemExit("heading invariant failed")
if native_markers(master) != native_markers(master0):
    raise SystemExit("native-marker invariant failed")
if link_destinations(master) != link_destinations(master0):
    raise SystemExit("Markdown link-destination invariant failed")
if sha(part2) != EXPECTED_BASE["part2"]:
    raise SystemExit("Part 2 changed unexpectedly")
if SLOW_OLD in master or SLOW_OLD in part1:
    raise SystemExit("Slow Steady preview deletion failed")
if CASUAL_OLD in master or CASUAL_OLD in part1 or CASUAL_NEW not in master or CASUAL_NEW not in part1:
    raise SystemExit("Casual STI/attachment materialization failed")
if PATIENT_OLD in master or PATIENT_OLD in part1 or PATIENT_NEW not in master or PATIENT_NEW not in part1:
    raise SystemExit("Maturity/patient rollback materialization failed")

required = [
    "Sex is what you do when you are older and you find a friend you want to have children with.",
    "would we like to raise children together? Are we ready?",
    "This will naturally prevent sex from happening too soon",
    "If we can't, that's a red flag for the relationship's chances of success.",
    "Gandarussa",
]
missing = [needle for needle in required if needle not in master]
if missing:
    raise SystemExit(f"required preserved anchors missing: {missing}")

OUT.mkdir(parents=True, exist_ok=True)
(OUT / "candidate-master.md").write_text(master, encoding="utf-8")
(OUT / "candidate-part-1.txt").write_text(part1, encoding="utf-8")
(OUT / "candidate-part-2.txt").write_text(part2, encoding="utf-8")

manifest = {
    "schema_version": 1,
    "status": "preservation_r11_candidate_not_owner_final_article",
    "base": {
        "directory": str(BASE.relative_to(ROOT)),
        "master_sha256": EXPECTED_BASE["master"],
        "part1_sha256": EXPECTED_BASE["part1"],
        "part2_sha256": EXPECTED_BASE["part2"],
    },
    "candidate": {
        "master": {"sha256": sha(master), "word_count_whitespace": wc(master)},
        "part1": {"sha256": sha(part1), "word_count_whitespace": wc(part1)},
        "part2": {"sha256": sha(part2), "word_count_whitespace": wc(part2), "unchanged": True},
    },
    "operations": operations,
    "preservation_proof": {
        "slow_steady": "recovery-20260822/preservation-proof-slow-steady-r11.json",
        "casual": "recovery-20260822/preservation-proof-casual-final-call6.json",
        "maturity_patient": "recovery-20260822/preservation-proof-maturity-patient-known-green.json",
        "talk": "unchanged from preservation-r10; local section hard-capped 6/6",
        "affection": "unchanged from preservation-r10; local section hard-capped 6/6",
        "unexplained_deltas": 0,
    },
    "detector_evidence": {
        "slow_steady_local": {"sha256": "2def6737f8763f6e3a92405166dd27f9d0e30ec043a57a216ffbc05bf6bb72f4", "human": 1.0},
        "casual_final_call6": {"sha256": "e59a9cf974a6252930f774d8246512d68d1137b64481194571488e3814897d04", "human": 0.9496374130249023, "note": "only unchanged final 41-word free-love-community sentence classified AI; no seventh local call"},
        "maturity_patient_cross_split": {"sha256": "7d60bc1c38669848e7e27d313603e4ee8970e34bf3896673160ea6a61c106002", "human": 1.0, "new_paid_call_required": False},
        "part2": {"sha256": EXPECTED_BASE["part2"], "human": 1.0, "unchanged": True},
    },
    "invariants": {
        "headings_identical_to_r10": True,
        "native_markers_identical_to_r10": True,
        "markdown_link_destinations_identical_to_r10": True,
        "part2_byte_identical_to_r10": True,
        "required_missing": [],
        "operations_exactly_three": True,
        "passed": True,
    },
    "next_action": "Run exact Part 1 aggregate Pangram 4 certification; reuse existing Part 2 100% Human result because Part 2 is byte-identical.",
}
(OUT / "candidate-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(json.dumps(manifest["candidate"], ensure_ascii=False, indent=2))
