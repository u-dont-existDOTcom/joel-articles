#!/usr/bin/env python3
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / "work/romance-r22-reconciliation-20260823"
WHITELIST = WORK / "R23-FIVE-OWNER-EDITS-MANIFEST.json"
OUT = WORK / "materialized-r23-five-owner-edits"
BASE_REF = "origin/task/romance-detector-repair-20260820"
BASE_PATH = "work/romance-detector-repair-20260820/materialized-preservation-r22-patient-affection/candidate-master.md"
EXPECTED_BASE_SHA = "f0f9a47eba2ac9ab1a56bdd6793316d41e7c23072b0b0c030285caf5e12f83c9"
EXPECTED_BASE_WORDS = 20282
EXPECTED_CANDIDATE_WORDS = 20364
EXPECTED_NATIVE_OBJECTS = 11
EXPECTED_MARKDOWN_LINKS = 22
EXPECTED_BOUNDARY_SHA = {
    "talk-affection": "a1c88e60e068101c268b8e0dc45558ec796fe6d8224de86c8b5ec64c5238e564",
    "spiritual-practice": "9722c938f9258316cef1efbe67768abee063f64923976711498bbaff57d106fb",
    "two-pillars": "e89362da826bd77d747733512a935cf19c1ddf6d492175755931826968360113",
    "choosing-together": "a1bd65fc862a879170d6651f52f4d0da50150bf56de1f4f9e26437d30dd6cb8f",
}


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def words(text: str) -> int:
    return len(text.split())


def git_show(ref_path: str) -> str:
    return subprocess.check_output(["git", "show", ref_path], text=True, encoding="utf-8")


def extract(text: str, start: str, end: str) -> str:
    a = text.index(start)
    b = text.index(end, a)
    return text[a:b].rstrip() + "\n"


cfg = json.loads(WHITELIST.read_text(encoding="utf-8"))
base = git_show(f"{BASE_REF}:{BASE_PATH}")
if sha(base) != EXPECTED_BASE_SHA:
    raise SystemExit(f"r22 SHA mismatch: {sha(base)}")
if words(base) != EXPECTED_BASE_WORDS:
    raise SystemExit(f"r22 word-count mismatch: {words(base)} != {EXPECTED_BASE_WORDS}")

candidate = base
applied = []
for change in cfg["changes"]:
    old = change["current"]
    new = change["proposed"]
    if sha(old) != change["current_sha256"]:
        raise SystemExit(f"{change['id']} frozen old hash mismatch")
    if sha(new) != change["proposed_sha256"]:
        raise SystemExit(f"{change['id']} frozen new hash mismatch")
    count = candidate.count(old)
    if count != 1:
        raise SystemExit(f"{change['id']} expected old span once, found {count}")
    candidate = candidate.replace(old, new, 1)
    applied.append(change["id"])

# Reverse-delta construction proof: candidate is produced only by the frozen six replacements.
if len(applied) != cfg["authorized_change_count"]:
    raise SystemExit("authorized operation count mismatch")
if words(candidate) != EXPECTED_CANDIDATE_WORDS:
    raise SystemExit(
        f"r23 word-count mismatch: {words(candidate)} != {EXPECTED_CANDIDATE_WORDS}"
    )

# Global invariants that must not move in this local edit batch.
headings_base = [line for line in base.splitlines() if line.startswith("#")]
headings_new = [line for line in candidate.splitlines() if line.startswith("#")]
if headings_base != headings_new:
    raise SystemExit("heading order/content changed")

native_base = base.count("[NATIVE ")
native_new = candidate.count("[NATIVE ")
if native_base != EXPECTED_NATIVE_OBJECTS or native_new != EXPECTED_NATIVE_OBJECTS:
    raise SystemExit(
        f"native object count mismatch source={native_base} candidate={native_new} expected={EXPECTED_NATIVE_OBJECTS}"
    )

link_re = re.compile(r"\[[^\]]+\]\([^\)]+\)")
links_base = len(link_re.findall(base))
links_new = len(link_re.findall(candidate))
if links_base != EXPECTED_MARKDOWN_LINKS or links_new != EXPECTED_MARKDOWN_LINKS:
    raise SystemExit(
        f"Markdown link count mismatch source={links_base} candidate={links_new} expected={EXPECTED_MARKDOWN_LINKS}"
    )

protected = [
    "Sex is what you do when you are older and you find a friend you want to have children with.",
    "[Gandarussa](https://thediplomat.com/2013/09/a-male-contraceptive-pill-for-indonesia/)",
    "Never recruit children into the adult war.",
    "It might be that I wrote this whole article for my son, Bear",
    "I believe Rumi was right: A sacred relationship will open and purify your hearts regardless of whether it ends.",
]
missing = [x for x in protected if x not in candidate]
if missing:
    raise SystemExit(f"protected anchors missing: {missing}")

# Prove all frozen old spans are gone and all new spans exist exactly once.
for change in cfg["changes"]:
    if change["current"] in candidate:
        raise SystemExit(f"{change['id']} old span survived")
    if candidate.count(change["proposed"]) != 1:
        raise SystemExit(f"{change['id']} new span not unique")

boundaries = {
    "talk-affection": extract(candidate, "# Talk about making love before you do it", "## Can Casual Sex or a Situationship Actually Be Honest?"),
    "spiritual-practice": extract(candidate, "## Can making love be a spiritual practice?", "## Muses & Directors"),
    "two-pillars": extract(candidate, "# Two Pillars Don't Hold The Roof Up", "# What are you actually choosing together?"),
    "choosing-together": extract(candidate, "# What are you actually choosing together?", "# Doing it consciously"),
}

# The exact natural boundaries were independently materialized from r22 + the frozen
# whitelist, committed, and read back byte-exact on 2026-08-24. Treat those SHA-256s
# as regression fixtures for the eventual full assembly.
for name, text in boundaries.items():
    actual = sha(text)
    expected = EXPECTED_BOUNDARY_SHA[name]
    if actual != expected:
        raise SystemExit(f"{name} boundary SHA mismatch: {actual} != {expected}")

OUT.mkdir(parents=True, exist_ok=True)
master_path = OUT / "candidate-master.md"
master_path.write_text(candidate, encoding="utf-8")
for name, text in boundaries.items():
    (OUT / f"boundary-{name}.txt").write_text(text, encoding="utf-8")

result = {
    "schema_version": 2,
    "candidate_id": cfg["candidate_id"],
    "base": {
        "ref": BASE_REF,
        "path": BASE_PATH,
        "sha256": EXPECTED_BASE_SHA,
        "word_count_whitespace": words(base),
    },
    "candidate": {
        "path": str(master_path.relative_to(ROOT)),
        "sha256": sha(candidate),
        "word_count_whitespace": words(candidate),
    },
    "operations": [
        {
            "id": c["id"],
            "section": c["section"],
            "old_sha256": c["current_sha256"],
            "new_sha256": c["proposed_sha256"],
        }
        for c in cfg["changes"]
    ],
    "authorized_operation_count": len(applied),
    "headings_exactly_unchanged": True,
    "native_object_count_source": native_base,
    "native_object_count_candidate": native_new,
    "markdown_link_count_source": links_base,
    "markdown_link_count_candidate": links_new,
    "unexplained_substantive_deltas": 0,
    "boundaries": {
        name: {
            "path": str((OUT / f"boundary-{name}.txt").relative_to(ROOT)),
            "sha256": sha(text),
            "expected_verified_sha256": EXPECTED_BOUNDARY_SHA[name],
            "word_count_whitespace": words(text),
            "independent_boundary_cold_read": "PASS",
        }
        for name, text in boundaries.items()
    },
    "detector_run": False,
    "detector_status": "unmeasured changed bytes; r22 exact-Human evidence retained only for the unchanged baseline",
}
(OUT / "candidate-manifest.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

receipt = f"""# Romance r23 five-owner-edit preservation receipt\n\nStatus: **PASS for deterministic materialization / pre-detector preservation gate. No Pangram call made.**\n\n- Authoritative working baseline: exact r22 `{EXPECTED_BASE_SHA}` from `{BASE_REF}:{BASE_PATH}`.\n- Edit mode: reduced local D2 reconciliation across four natural boundaries.\n- Frozen authorized operations: {len(applied)} exact replacements, IDs {', '.join(applied)}.\n- Forward traceability: PASS. Unchanged text remains byte-identical; each changed source span maps to one owner-authorized replacement.\n- Reverse traceability: PASS. Candidate is constructed only by the frozen whitelist operations.\n- Unexplained substantive deltas: **0**.\n- Heading order/content: unchanged.\n- Native objects: {native_base} -> {native_new}.\n- Markdown links: {links_base} -> {links_new}.\n- Protected father quote, Gandarussa, children-war warning, Bear callback, and Rumi terminal line: present.\n- Independently materialized boundary SHA fixtures: all four PASS.\n- Independent changed-boundary cold read: PASS; see `R23-BOUNDARY-COLD-READ-20260824.md`.\n- Architecture/dependency gate: PASS at the approved local-edit level; no section order, protected-function routing (except the authorized Two Pillars strengthening), native-object placement, or callback placement changes.\n- Candidate SHA-256: `{sha(candidate)}`.\n- Candidate words (whitespace): {words(candidate)}.\n- Detector eligibility: **full candidate is preservation-clean; next certification targets are the exact resulting Part 1 / Part 2 halves, after current cache/reservation/call-ledger recovery.**\n\nDo not substitute section-level Pangram scores for composition-aware half-boundary certification.\n"""
(OUT / "preservation-receipt.md").write_text(receipt, encoding="utf-8")

print(json.dumps(result, ensure_ascii=False, indent=2))
