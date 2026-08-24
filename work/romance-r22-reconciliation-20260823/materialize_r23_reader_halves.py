#!/usr/bin/env python3
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / "work/romance-r22-reconciliation-20260823"
OUT = WORK / "materialized-r23-five-owner-edits"
BASE_REF = "origin/task/romance-detector-repair-20260820"
P1_PATH = "work/romance-detector-repair-20260820/materialized-preservation-r22-patient-affection/part1.txt"
P2_PATH = "work/romance-detector-repair-20260820/materialized-semantic-r9/candidate-part-2.txt"
EXPECTED_P1_SHA = "5ed333800b9ae7b402f26aa03e751ef8296c7e27ab70e39bc39bb9896b23e62d"
EXPECTED_P2_SHA = "9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85"
EXPECTED_P1_WORDS = 10239
EXPECTED_P2_WORDS = 9892
EXPECTED_R23_P1_WORDS = 10296
EXPECTED_R23_P2_WORDS = 9917

OPS = [
    {
        "id": "R23-01",
        "half": 1,
        "old": "Of course everyone does change over time as well, so communication should remain open beyond a simple interview.",
        "new": "Of course everyone does change over time as well. If our libidos later diverge, it's better to talk about what we'd do before either person is already hurt.",
        "old_sha256": "f0edab39d411ff5d5461a424d29ba7b643e7c6a39e3376d55539c18a3fb97b53",
        "new_sha256": "ce91727a3827b99dcef1233b7c6bb3bab7ad5ffec19bbd0eebd8763909af822c",
    },
    {
        "id": "R23-02A",
        "half": 1,
        "old": "Kim Anami calls the sexual current between encounters “the simmer”. Maybe she texts from work, “I can’t wait to touch you.” Maybe he tells her what he wants to do later. If we supposedly want each other but hardly ever flirt or let each other know it, I think something is already wrong. Great sex probably isn't going to materialize out of nowhere at bedtime.",
        "new": "Kim Anami calls the sexual current between encounters “the simmer”. Maybe she texts from work, “I can’t wait to touch you.” Maybe he tells her what he wants to do later. If we supposedly want each other but hardly ever flirt or let each other know it, that’s called taking each other for granted. Great sex probably isn't going to materialize out of nowhere at bedtime just based on the flirting you did 5 years ago.\n\nIt shouldn't become relationship homework, either: “Hey babe, Kim Anami told me to flirt with you more.”",
        "old_sha256": "edd35bb4e3eb76873753b42f94da01cc1275bf2044ab2abb6c92f3fa4648fd08",
        "new_sha256": "d32955c635ee71ab64c8a9689c5f204cae33a4b42bf3eac530c0867d0e7904b8",
    },
    {
        "id": "R23-02B",
        "half": 1,
        "old": "And if our sex life suddenly changes, I want to know what changed. Maybe we're pissed off at each other. Maybe somebody's sick, stressed, on a new medication, whatever.",
        "new": "And if our sex life suddenly changes, keep some curiosity about why rather than automatically going with the flow and creating a potential “new normal.” Maybe we're pissed off at each other. Maybe one of us doesn't feel wanted. Maybe somebody's sick, stressed, on a new medication, whatever.",
        "old_sha256": "97a2d85b1a4368a7b26881da4d3a7c03c248d9aabbb8b88276a02526c33051b7",
        "new_sha256": "7bac3aa6fa65ce9da5d68b31168935d9db5d9811adc0879c578b645397658588",
    },
    {
        "id": "R23-03",
        "half": 2,
        "old": "She also has a ton of student stories where the effects spill out of sex into health, work, money, creativity, the rest of life. Her jade-egg practice is basically the solo version: pelvic-floor strength, attention, and arousal without needing a partner.",
        "new": "She has also collected a ton of stories from students who say the effects spill out of sex into health, work, money, creativity, the rest of life. Her jade-egg practice is a preliminary training for the cervical O: pelvic-floor strength, attention, and arousal without needing a partner.",
        "old_sha256": "27830111ad636ecd0cfc0ea03d4c5a168a98485b04271bf4f7e30e286685e21e",
        "new_sha256": "8e60f9c4fe77f625cb2ed3af8c023e8cf7b29440b2605d94afd8e58b3b9a18ca",
    },
    {
        "id": "R23-04",
        "half": 2,
        "old": "Maybe an unusually strong couple can get away without much community. I think that's rare. Community isn't magic either; if both people are falling apart, there is only so much anyone else can do.",
        "new": "Maybe an unusually strong couple can get away without much community. I think that's rare. Community isn't magic either; if both people are falling apart, there is only so much anyone else can do.\n\nBut sometimes a friend who actually knows us both sees the pattern before either of us does.",
        "old_sha256": "6b718e49f1e9e6452f695daa41e08928a4aad9315187737436d4afcaf0bc7e58",
        "new_sha256": "bfbf11b694bd71a9e3f311c7d3635939a9880dc1705acc0d269327642936ea96",
    },
    {
        "id": "R23-05",
        "half": 2,
        "old": "“We’re together” ... what does that mean exactly? I might hear sex, exclusivity, living together, money, children, caregiving in those two words. She might mean, “We really like each other; let’s see what happens.” I actually like letting a relationship flow without naming every part. The problem is when we’re using the same words for two different futures.",
        "new": "“We’re together” ... what does that mean exactly? I can hear a whole future in those two words—sex, exclusivity, living together, money, children, caregiving. She might mean, “We really like each other; let’s see what happens.” I actually like letting a relationship flow without naming every part. The problem is when we’re using the same words for two different futures.",
        "old_sha256": "0eea104b2f9c41b3504b8ea72e1146211e3b88b6d79e5d072ce068a3e2c0aeca",
        "new_sha256": "7814ffc33f9d13a1d31981cc5bd719ca0da7a3b19f9f31a721eac15f90bf4f74",
    },
]


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def words(text: str) -> int:
    return len(text.split())


def git_show(ref_path: str) -> str:
    return subprocess.check_output(["git", "show", ref_path], text=True, encoding="utf-8")


def apply_ops(text: str, half: int) -> tuple[str, list[str]]:
    out = text
    applied = []
    for op in OPS:
        if op["half"] != half:
            continue
        if sha(op["old"]) != op["old_sha256"]:
            raise SystemExit(f"{op['id']} frozen reader old hash mismatch")
        if sha(op["new"]) != op["new_sha256"]:
            raise SystemExit(f"{op['id']} frozen reader new hash mismatch")
        count = out.count(op["old"])
        if count != 1:
            raise SystemExit(f"{op['id']} expected reader old span once in half {half}, found {count}")
        out = out.replace(op["old"], op["new"], 1)
        expected_old_count = op["new"].count(op["old"])
        actual_old_count = out.count(op["old"])
        if actual_old_count != expected_old_count:
            raise SystemExit(
                f"{op['id']} unexpected old reader-span count after replacement: "
                f"expected {expected_old_count}, found {actual_old_count}"
            )
        if out.count(op["new"]) != 1:
            raise SystemExit(f"{op['id']} new reader span not unique")
        applied.append(op["id"])
    return out, applied


p1 = git_show(f"{BASE_REF}:{P1_PATH}")
p2 = git_show(f"{BASE_REF}:{P2_PATH}")
if sha(p1) != EXPECTED_P1_SHA or words(p1) != EXPECTED_P1_WORDS:
    raise SystemExit(f"r22 Part1 identity mismatch sha={sha(p1)} words={words(p1)}")
if sha(p2) != EXPECTED_P2_SHA or words(p2) != EXPECTED_P2_WORDS:
    raise SystemExit(f"r22 Part2 identity mismatch sha={sha(p2)} words={words(p2)}")

r23_p1, p1_ops = apply_ops(p1, 1)
r23_p2, p2_ops = apply_ops(p2, 2)
if p1_ops != ["R23-01", "R23-02A", "R23-02B"]:
    raise SystemExit(f"unexpected Part1 ops: {p1_ops}")
if p2_ops != ["R23-03", "R23-04", "R23-05"]:
    raise SystemExit(f"unexpected Part2 ops: {p2_ops}")
if words(r23_p1) != EXPECTED_R23_P1_WORDS:
    raise SystemExit(f"r23 Part1 word mismatch: {words(r23_p1)}")
if words(r23_p2) != EXPECTED_R23_P2_WORDS:
    raise SystemExit(f"r23 Part2 word mismatch: {words(r23_p2)}")

# Preserve the tested split topology and load-bearing anchors.
if "Key at first asked me innocently, \"Can you be my guru?\"" in r23_p1:
    raise SystemExit("Maturity continuation leaked into Part1")
if not r23_p2.startswith('Key at first asked me innocently, "Can you be my guru?"'):
    raise SystemExit("Part2 no longer starts at the exact retained Maturity continuation")
if "Talk about making love before you do it\n" not in r23_p1:
    raise SystemExit("Talk heading missing from Part1")
for anchor in [
    "Can making love be a spiritual practice?\n",
    "Two Pillars Don't Hold The Roof Up\n",
    "What are you actually choosing together?\n",
]:
    if anchor not in r23_p2:
        raise SystemExit(f"required Part2 heading missing: {anchor!r}")

OUT.mkdir(parents=True, exist_ok=True)
(OUT / "candidate-part-1.txt").write_text(r23_p1, encoding="utf-8")
(OUT / "candidate-part-2.txt").write_text(r23_p2, encoding="utf-8")

manifest_path = OUT / "candidate-manifest.json"
manifest = {}
if manifest_path.exists():
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
manifest["reader_visible_halves"] = {
    "source": {
        "part1": {"path": P1_PATH, "sha256": EXPECTED_P1_SHA, "word_count_whitespace": EXPECTED_P1_WORDS},
        "part2": {"path": P2_PATH, "sha256": EXPECTED_P2_SHA, "word_count_whitespace": EXPECTED_P2_WORDS},
        "split_contract": "reuse exact tested r22 halves; mutate only the authorized reader-visible spans inside each half",
    },
    "candidate": {
        "part1": {
            "path": str((OUT / "candidate-part-1.txt").relative_to(ROOT)),
            "sha256": sha(r23_p1),
            "word_count_whitespace": words(r23_p1),
            "operations": p1_ops,
        },
        "part2": {
            "path": str((OUT / "candidate-part-2.txt").relative_to(ROOT)),
            "sha256": sha(r23_p2),
            "word_count_whitespace": words(r23_p2),
            "operations": p2_ops,
        },
    },
    "unexplained_substantive_deltas": 0,
    "detector_run": False,
    "detector_status": "exact r23 half bytes materialized but unmeasured",
}
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

receipt = OUT / "reader-half-receipt.md"
receipt.write_text(
    f"""# Romance r23 exact reader-visible half receipt\n\nStatus: **MATERIALIZED / PRE-DETECTOR. No Pangram call made.**\n\n- r22 Part 1 source SHA-256: `{EXPECTED_P1_SHA}`; {EXPECTED_P1_WORDS} words.\n- r22 Part 2 source SHA-256: `{EXPECTED_P2_SHA}`; {EXPECTED_P2_WORDS} words.\n- Split contract: reuse the exact tested r22 half files and mutate only the authorized reader-visible spans already assigned to each half. No Markdown-to-reader re-normalization was invented.\n- r23 Part 1 operations: {', '.join(p1_ops)}.\n- r23 Part 1 SHA-256: `{sha(r23_p1)}`; {words(r23_p1)} words.\n- r23 Part 2 operations: {', '.join(p2_ops)}.\n- r23 Part 2 SHA-256: `{sha(r23_p2)}`; {words(r23_p2)} words.\n- Unexplained substantive deltas: **0** by construction.\n- Detector state: **UNMEASURED**.\n\nThese are the composition-aware certification targets. Recover Pangram cache/reservation/call-ledger state before any paid submission.\n""",
    encoding="utf-8",
)

print(json.dumps(manifest["reader_visible_halves"], ensure_ascii=False, indent=2))
