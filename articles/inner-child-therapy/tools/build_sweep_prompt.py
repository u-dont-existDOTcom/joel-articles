#!/usr/bin/env python3
"""Build a fresh-context tell-sweep prompt from the numbered inventory.

Usage:
  python3 build_sweep_prompt.py TARGET [--previous PREVIOUS] [--next NEXT] [--inventory INVENTORY] > prompt.txt

TARGET, PREVIOUS and NEXT are markdown or plain text; links become "text [linked: URL]"
and heading markers are removed. The inventory defaults to docs/HUMANIZATION-TELL-INVENTORY.md.
The prompt carries no detector results and no drafting rationale (score-blind).
"""
import argparse
import pathlib
import re

HERE = pathlib.Path(__file__).resolve()
DEFAULT_INVENTORY = HERE.parents[3] / "docs" / "HUMANIZATION-TELL-INVENTORY.md"

HEADER = """You are performing the ORIGINAL Joel humanization task: a GLOBAL TELL-LEDGER CHECK. You are NOT classifying hidden authorship and you are NOT allowed to average tells into one overall Human/AI judgment.

Audit the literal TARGET against EVERY tell below. Return one ledger row for every tell ID. A tell may be PRESENT, ABSENT, or UNCERTAIN.

Rules:
- PRESENT means the actual operation is instantiated in this prose, not merely that a surface form associated with it appears.
- A list, first person, direct advice, rhetorical question, short sentence, fragment, colloquial word, metaphor, polished sentence, joke, or an organized structure is not itself a tell.
- Judge paragraph/section-scale tells at paragraph/section scale.
- Human-looking features do not cancel a tell that is genuinely present.
- Conversely, do not force a tell because prose is model-authored or because another tell is present.
- Exact evidence must quote the smallest useful span(s).
- You must emit all tell IDs exactly once. Do not add new tell IDs.
- Do not output a global HUMAN/AI classification.

CURRENT TELL INVENTORY:
"""

FOOTER = """
Return valid JSON only:
{
  "ledger": [
    {"tell_id":"T01","status":"PRESENT|ABSENT|UNCERTAIN","evidence":["..."],"reason":"..."}
  ],
  "blocking_present_ids":["..."],
  "audit_complete":true
}
"""


def flatten(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    # Keep the link target: the real reader sees a hyperlink, and dropping it made
    # the round-8 sweep report a sourced study as unsourced (C04 false positive).
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 [linked: \2]", text)
    text = re.sub(r"^#+\s*", "", text, flags=re.M)
    return text.strip()


def tells(inventory_text):
    rows = re.findall(r"^\*\*([TC]\d\d) — (.+?)\*\*\s*(.+)$", inventory_text, flags=re.M)
    if not rows:
        raise SystemExit("no tells found in the inventory")
    return [f"{tid} — {title.rstrip('.')}\n{body.strip()}" for tid, title, body in rows]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--previous")
    ap.add_argument("--next")
    ap.add_argument("--inventory", default=str(DEFAULT_INVENTORY))
    a = ap.parse_args()
    inv = pathlib.Path(a.inventory).read_text(encoding="utf-8")
    items = tells(inv)
    prev = flatten(pathlib.Path(a.previous).read_text(encoding="utf-8")) if a.previous else "(none)"
    nxt = flatten(pathlib.Path(a.next).read_text(encoding="utf-8")) if a.next else "(none: the following section has not been written yet)"
    target = flatten(pathlib.Path(a.target).read_text(encoding="utf-8"))
    ids = [i.split(" ", 1)[0] for i in items]
    print(HEADER + "\n" + "\n\n".join(items) + "\n" + FOOTER)
    print(f"Tell IDs to answer, exactly once each: {', '.join(ids)}\n")
    print("PREVIOUS CONTEXT:\n" + prev + "\n\nTARGET:\n" + target + "\n\nNEXT CONTEXT:\n" + nxt)


if __name__ == "__main__":
    main()
