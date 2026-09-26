"""Apply only Joel's 2026-09-10 sleep-script removal to the exact supplied HTML.

No HTML reserialization, publication, article registration, or other edits.
Usage: python apply_sleep_patch.py SOURCE.html OUTPUT.html
"""
from __future__ import annotations
import argparse
import hashlib
from pathlib import Path

SOURCE_SHA256 = "d7e923898a10edad0601c7cbd581fec7b0c90233f16ae005ca1fad61b6082893"
PLAYLIST = "https://www.youtube.com/watch?v=IqyqE8V2CJg&list=PLZhjR9_8QJZsWUmSS5KpiueoQuq0k-poT"
OLD_REF = "Appendix I contains the full Milton Model sleep script."
NEW_REF = "For sleep hypnosis, see Nimja’s sleep playlist in Appendix I."
START = "<h1>Appendix I: A Milton Model sleep induction</h1>"
END = '<hr contenteditable="false"><h1>Appendix J: The extreme influence story, quarantined from the evidence</h1>'
REPLACEMENT = (
    '<h1>Appendix I: Sleep hypnosis</h1>'
    '<p>For sleep hypnosis, use '
    '<a target="_blank" rel="noopener noreferrer nofollow" '
    'href="' + PLAYLIST.replace('&', '&amp;') + '">Nimja’s sleep playlist</a>.</p>'
    '<p>Do not use this while driving, bathing, supervising children, cooking, '
    'operating equipment, or doing anything that requires active attention.</p>'
)

def transform(raw: bytes) -> tuple[bytes, list[dict]]:
    """Return a hash-guarded derivative and exact reversible character edits."""
    actual = hashlib.sha256(raw).hexdigest()
    if actual != SOURCE_SHA256:
        raise ValueError(f"Source mismatch: {actual}; re-resolve anchors before editing.")
    text = raw.decode("utf-8")
    for anchor in (OLD_REF, START, END):
        if text.count(anchor) != 1:
            raise ValueError(f"Expected one unique anchor: {anchor!r}")
    start, end = text.index(START), text.index(END)
    if end <= start:
        raise ValueError("Invalid sleep-section boundary order")
    edits = [
        {"start": text.index(OLD_REF), "end": text.index(OLD_REF) + len(OLD_REF),
         "before": OLD_REF, "after": NEW_REF, "operation": "repair dependent sleep reference"},
        {"start": start, "end": end, "before": text[start:end],
         "after": REPLACEMENT, "operation": "replace sleep script and obsolete analysis with playlist"},
    ]
    result = text
    for edit in reversed(edits):
        result = result[:edit["start"]] + edit["after"] + result[edit["end"]:]
    return result.encode("utf-8"), edits

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.source.resolve() == args.output.resolve():
        parser.error("Output must differ from source; preserve the original.")
    if args.output.exists():
        parser.error("Output already exists; choose a new derivative filename.")
    result, _ = transform(args.source.read_bytes())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(result)
    print(hashlib.sha256(result).hexdigest())

if __name__ == "__main__":
    main()
