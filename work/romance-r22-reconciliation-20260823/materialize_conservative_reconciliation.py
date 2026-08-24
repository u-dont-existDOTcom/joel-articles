from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

CANONICAL_SHA = "af50b7b93662daf00d484ad83faa0453ff0a2a4fda2867ecfd467166b4c984fe"
R22_SHA = "f0f9a47eba2ac9ab1a56bdd6793316d41e7c23072b0b0c030285caf5e12f83c9"
TASK_REF = "origin/task/romance-detector-repair-20260820"
R22_PATH = "work/romance-detector-repair-20260820/materialized-preservation-r22-patient-affection/candidate-master.md"
MASTER_PATH = Path("articles/romance/master.md")
OUT_DIR = Path("work/romance-r22-reconciliation-20260823/materialized-conservative")


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def git_show(spec: str) -> str:
    return subprocess.check_output(["git", "show", spec], text=True, encoding="utf-8")


def marker_offset(text: str, marker: str) -> int:
    needle = marker + "\n"
    pos = text.find(needle)
    if pos < 0:
        raise RuntimeError(f"marker not found: {marker!r}")
    if text.find(needle, pos + 1) >= 0:
        raise RuntimeError(f"marker not unique: {marker!r}")
    return pos


def replace_between_headings(base: str, source: str, start: str, end: str) -> str:
    b_start = marker_offset(base, start)
    b_start = base.find("\n", b_start) + 1
    b_end = marker_offset(base, end)
    s_start = marker_offset(source, start)
    s_start = source.find("\n", s_start) + 1
    s_end = marker_offset(source, end)
    return base[:b_start] + source[s_start:s_end] + base[b_end:]


def heading_level(line: str) -> int | None:
    m = re.match(r"^(#{1,6})\s+", line)
    return len(m.group(1)) if m else None


def section_span(text: str, heading: str) -> tuple[int, int]:
    lines = text.splitlines(keepends=True)
    offsets: list[int] = []
    p = 0
    for line in lines:
        offsets.append(p)
        p += len(line)
    wanted_level = heading_level(heading)
    if wanted_level is None:
        raise RuntimeError(f"not a heading: {heading}")
    matches = [i for i, line in enumerate(lines) if line.rstrip("\r\n") == heading]
    if len(matches) != 1:
        raise RuntimeError(f"expected heading once: {heading!r}; found {len(matches)}")
    i = matches[0]
    start = offsets[i]
    end = len(text)
    for j in range(i + 1, len(lines)):
        level = heading_level(lines[j].rstrip("\r\n"))
        if level is not None and level <= wanted_level:
            end = offsets[j]
            break
    return start, end


def replace_section(base: str, source: str, heading: str) -> str:
    b0, b1 = section_span(base, heading)
    s0, s1 = section_span(source, heading)
    return base[:b0] + source[s0:s1] + base[b1:]


def replace_exact_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected old text once, found {count}")
    return text.replace(old, new, 1)


def markdown_links(text: str) -> list[str]:
    return re.findall(r"\[[^\]]+\]\(([^\)]+)\)", text)


def headings(text: str) -> list[str]:
    return [line for line in text.splitlines() if re.match(r"^#{1,6}\s+", line)]


canonical = git_show("origin/main:articles/romance/master.md")
r22 = git_show(f"{TASK_REF}:{R22_PATH}")
if sha256(canonical) != CANONICAL_SHA:
    raise SystemExit(f"canonical SHA mismatch: {sha256(canonical)}")
if sha256(r22) != R22_SHA:
    raise SystemExit(f"r22 SHA mismatch: {sha256(r22)}")

candidate = canonical
operations: list[dict[str, str]] = []

# 1. Talk body: current owner-final tail plus the preceding father/readiness material
# that the owner-final source explicitly instructs us to leave unchanged.
candidate = replace_between_headings(
    candidate,
    r22,
    "# Talk about making love before you do it",
    "## Affection and the simmer",
)
operations.append({"id": "RC-01", "type": "owner-supported-section-body", "scope": "Talk body before Affection"})

# 2. Owner-accepted holistic Affection realization.
candidate = replace_between_headings(
    candidate,
    r22,
    "## Affection and the simmer",
    "## Can Casual Sex or a Situationship Actually Be Honest?",
)
operations.append({"id": "RC-02", "type": "owner-accepted-section", "scope": "Affection and the simmer"})

# 3-4. Joel-approved Casual deletions only.
for op_id, sentence in [
    ("RC-03", "Oxytocin, vasopressin, and the rest can start attaching you anyway. "),
    ("RC-04", "You can both mean it when you say this is only sex and still have one of you get attached afterward. "),
]:
    candidate = replace_exact_once(candidate, sentence, "", op_id)
    operations.append({"id": op_id, "type": "owner-approved-deletion", "scope": sentence.strip()})

# 5. Owner-accepted patient/helping block.
patient_old = '''All three women told me at some point that they felt like my patient. Which is true, I really was the one they asked about almost every medical, mental-health, and practical problem:

“I’m sick. What should I take?”

“I’m sad. What should I do?”

Of course I helped. Saying, “I’m not your doctor or therapist,” every time would have been cold. But enough moments become a pattern.'''
patient_new = '''All three women told me at some point that they felt like my patient, and I couldn't exactly argue with them. They asked me about almost every medical, mental-health, and practical problem:

“I’m sick. What should I take?”

“I’m sad. What should I do?”

I usually had some idea, so of course I answered. But enough moments become a pattern.'''
candidate = replace_exact_once(candidate, patient_old, patient_new, "RC-05")
operations.append({"id": "RC-05", "type": "owner-accepted-block", "scope": "patient/helping"})

# 6. Direct-owner Muses rewrite plus owner-accepted leadership tail up to Not A Performance.
candidate = replace_between_headings(candidate, r22, "## Muses & Directors", "## Not A Performance")
operations.append({"id": "RC-06", "type": "direct-owner-plus-owner-accepted-section", "scope": "Muses & Directors"})

# 7. Not A Performance: use the literal assistant-produced passage Joel accepted,
# then return to exact registered canonical prose at the female anti-performance span.
nap_start, nap_end = section_span(candidate, "## Not A Performance")
canonical_nap_start, canonical_nap_end = section_span(canonical, "## Not A Performance")
canonical_nap = canonical[canonical_nap_start:canonical_nap_end]
anchor = "The same is true for a woman."
if canonical_nap.count(anchor) != 1:
    raise SystemExit("Not A Performance canonical suffix anchor mismatch")
accepted_nap_opening = '''## Not A Performance

The moment I have to prove that I’m the man, something has already become fake.

I don’t actually walk around thinking I’m some super-masculine guy. I cry, I need help, I get things wrong. Bee once called me her “wife.” I don’t recommend that as a polarity exercise, by the way.

When a woman appreciates that masculine side of me, it tends to come out by itself.

'''
canonical_suffix = canonical_nap[canonical_nap.index(anchor) :]
hybrid_nap = accepted_nap_opening + canonical_suffix
candidate = candidate[:nap_start] + hybrid_nap + candidate[nap_end:]
operations.append({"id": "RC-07", "type": "exact-owner-accepted-opening-plus-canonical-suffix", "scope": "Not A Performance"})

# 8. Direct-owner Attraction and exclusivity section.
candidate = replace_section(candidate, r22, "### Attraction and exclusivity")
operations.append({"id": "RC-08", "type": "direct-owner-section", "scope": "Attraction and exclusivity"})

# 9. Owner-final pinkest-elephants/dance local replacement only.
pink_old = '''Start with the pinkest elephants in the room:

“I don’t think we really trust each other.”

“I’m resentful about this.”

“I’m attracted to somebody else.”

“I don’t know whether I still want the same kind of relationship.”

See whether the other person will stay in the conversation. If they won’t, that tells you something another perfectly worded speech probably won’t fix.'''
pink_new = '''When did you two last dance? And not the “we dance around our problems” joke (LOL).. if that’s where things are at, the trust is out the window. Ouch. I know that one from experience with my first 2 wives and K, too. That generally marks the point of no return, so try not to wait for that. Because once you're there, as my dad explained a thousand times whenever we had a visitor, unconscious resentment begins to snowball, and we feel colder together than alone. Pretty soon, old Romeo & Juliette might get wandering eye syndrome.'''
candidate = replace_exact_once(candidate, pink_old, pink_new, "RC-09")
operations.append({"id": "RC-09", "type": "owner-final-local-replacement", "scope": "If you're already in it / dance span"})

# Mechanical invariants.
if headings(candidate) != headings(canonical):
    raise SystemExit("Markdown heading sequence changed")
if candidate.count("[NATIVE ") != canonical.count("[NATIVE "):
    raise SystemExit("native-object marker count changed")
if markdown_links(candidate) != markdown_links(canonical):
    raise SystemExit("Markdown link destination sequence changed")

required = [
    "Sex is what you do when you are older and you find a friend you want to have children with.",
    "What I eventually took from my dad's advice was a bigger question: would we like to raise children together? Are we ready?",
    "It's important to talk about sexual compatibility before getting undressed, even if that kills the vibe.",
    "If you’re both really numb or robotic about sex, maybe not.",
    "[Gandarussa](https://thediplomat.com/2013/09/a-male-contraceptive-pill-for-indonesia/)",
    "Some women barely have that poetic quality, and artistic men can live much closer to it.",
    "The moment I have to prove that I’m the man, something has already become fake.\n\nI don’t actually walk around thinking I’m some super-masculine guy.",
    "When a woman appreciates that masculine side of me, it tends to come out by itself.",
    "The same is true for a woman. She should not have to perform softness, helplessness, or cuteness every minute to prove she is feminine.",
    "It's hard to find sexually monogamous animals, have you ever looked?",
    "When did you two last dance?",
    "It might be that I wrote this whole article for my son, Bear, who sadly, I last saw when he was about five, right before he was supposed to get the Rosenblum sex talk.",
    "I believe Rumi was right: A sacred relationship will open and purify your hearts regardless of whether it ends.",
    "[NATIVE BUTTON — Subscribe now — %%checkout_url%%]",
]
missing = [x for x in required if x not in candidate]
if missing:
    raise SystemExit(f"required protected/owner anchors missing: {missing}")

forbidden_r22_only = [
    "After a while, more questions mostly teach me what the person says about themself, and I need ordinary time.",
    "Mostly I have to build my own brakes before I'm alone with her, and they still fail sometimes.",
    "sometimes this isn't two wounded people triggering each other but one person terrorizing or controlling the other.",
    "She also has a ton of student stories where the effects spill out of sex into health, work, money, creativity, the rest of life.",
    "Even if I found my twin flame, she'd still be one person.",
    "The problem is when we’re using the same words for two different futures.",
    "The intimacy can be completely real without telling you whether the two of you actually work together sober.",
    "A breakup can expose things you genuinely couldn't see while you were bonded. Look at what you contributed",
    "Then I have to defend the identity every time I hesitate, cry, need help, or get something wrong.",
]
surviving = [x for x in forbidden_r22_only if x in candidate]
if surviving:
    raise SystemExit(f"unaccepted r22/canonical-overhang realization survived conservative reconciliation: {surviving}")

OUT_DIR.mkdir(parents=True, exist_ok=True)
MASTER_PATH.write_text(candidate, encoding="utf-8")
(OUT_DIR / "candidate-master.md").write_text(candidate, encoding="utf-8")
manifest = {
    "schema_version": 1,
    "candidate_id": "romance-r22-conservative-reconciliation-20260823",
    "base": {"sha256": CANONICAL_SHA, "word_count_whitespace": len(canonical.split())},
    "r22_reference": {"sha256": R22_SHA, "word_count_whitespace": len(r22.split())},
    "candidate": {"sha256": sha256(candidate), "word_count_whitespace": len(candidate.split())},
    "operations": operations,
    "operation_count": len(operations),
    "heading_count": len(headings(candidate)),
    "native_object_count": candidate.count("[NATIVE "),
    "markdown_link_count": len(markdown_links(candidate)),
    "unexplained_substantive_deltas": 0,
    "canonical_main_changed": False,
    "detector_status": "not certified; prior r22 detector result does not apply after conservative reverts",
}
(OUT_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(manifest, indent=2, ensure_ascii=False))