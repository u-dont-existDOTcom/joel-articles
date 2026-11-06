"""Joel's message of 2026-11-06 19:40 UTC: his own "The Problem" paragraph replaces block 46 word for word,
and the "The Hardening" paragraph (block 49) is deleted, because he folded it into his paragraph.

Run from the repository root. Refuses if either block is not the text it expects.
"""
import hashlib
import json
import pathlib

ROOT = pathlib.Path("articles/neuro-de-armoring/humanize")
ARTICLE = ROOT / "HUMANIZED-SO-FAR.md"
OUT = ROOT / "fix-20261106" / "APPLIED-1940.json"

OLD_PROBLEM_START = "The Problem: To protect itself from the Glutamate storm, the brain eventually releases Dynorphin"
OLD_HARDENING_START = "The Hardening: Chronic cycles lead to the accumulation of DeltaFosB"

# His paragraph, byte for byte as he sent it (one line break, the double space after "Storm.", the space before the
# line break).
HIS = (
    "The Problem: If you're feeling apathetic, gray, no desire for anything, you might be in a neurochemical \"Void\" "
    "state caused by Dynorphin & DeltaFosB. That's because the brain releases dynorphin to suppress dopamine in order "
    "to protect from trauma's Glutamate Storm.  And as we know, dopamine is the neurotransmitter for motivation (by "
    "showing us what is important to pay attention to). \n"
    "Even though dynorphin clears relatively quickly, allowing us the motivation to learn, DeltaFosB keeps cementing "
    "our neural connections, preventing that learning from really \"clicking\" as durable insights. And because we're "
    "still reacting in the same maladaptive ways (same fears, etc), our psychology then asks for more DeltaFosB to "
    "keep the armor in place, in a vicious cycle. ([Vialou, et al, 2010](https://pubmed.ncbi.nlm.nih.gov/20473292/))."
)


def sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def main() -> None:
    text = ARTICLE.read_text()
    before = sha(text)
    blocks = text.split("\n\n")
    problem = [i for i, b in enumerate(blocks) if b.startswith(OLD_PROBLEM_START)]
    hardening = [i for i, b in enumerate(blocks) if b.startswith(OLD_HARDENING_START)]
    assert len(problem) == 1 and len(hardening) == 1, (problem, hardening)
    old_problem, old_hardening = blocks[problem[0]], blocks[hardening[0]]
    blocks[problem[0]] = HIS
    del blocks[hardening[0]]
    new = "\n\n".join(blocks)
    ARTICLE.write_text(new)
    OUT.write_text(json.dumps({
        "message": "Joel, 2026-11-06 19:40 UTC",
        "his_check": "https://www.pangram.com/history/3d7bf59d-c958-4f82-a268-d33089bfbda1",
        "his_check_reads": "Human Written, 100% human, one window, High confidence, 125 words",
        "article_sha256_before": before,
        "article_sha256_after": sha(new),
        "replaced": {"block": problem[0], "old": old_problem, "new": HIS, "whose": "his own: he wrote it"},
        "deleted": {"block": hardening[0], "old": old_hardening,
                    "why": "his words: 'now you can also delete the \"hardening\" para since i had to incorporate that "
                           "into this one, otherwise it was out of order and a bit redundant'"},
    }, indent=1, ensure_ascii=False) + "\n")
    print(before[:16], "->", sha(new)[:16])


if __name__ == "__main__":
    main()
