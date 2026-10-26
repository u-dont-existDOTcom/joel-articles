"""Batch 480: Emulate first (E237, E235) on the red stretches of batch 479's recheck (2026-10-26, read after Joel's message of
00:54 UTC: ../../fix-20261025/b479/recheck/RESULT-A.json and RESULT-B.json, SCORE-A.md and SCORE-B.md). Each text is the
paragraph as it stood in that recheck (../../fix-20261025/b479/CANDIDATE-MASTER.md), with the paragraph before it where it
helps; only the red sentences come back from a sample.
- HG-A-jobs2: S1, his inner child guide's whole sentence, read AI, High (it was Low as IC-A2's cut one).
- HG-A-guards: Working with your guards P3 and P4: IC-A14's two sentences and the start of his own exercise lines (IC-A15),
  unchanged, read AI (Medium, High, Medium, Low); one Human, Low window last time.
- HG-A-script: Your inherited parent script P1, unchanged since recheck A4, read AI (Low, Medium, both marked humanized);
  Human, High and Medium, last time.
- HG-B-altered: Appendix G P1, IC-B19's "Borrowed is fine, ..." from his inner child guide, unchanged, read AI (Low);
  Human, Low, last time.

  python3 articles/inner-signal/humanize/fix-20261026/b480/make_bundle.py   (from the repo root)
"""
import hashlib, json, pathlib, sys

B = pathlib.Path(__file__).resolve().parent
ROOT = B.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

MASTER = ROOT / 'articles/inner-signal/humanize/fix-20261025/b479/CANDIDATE-MASTER.md'
ITEMS = {
    'HG-A-jobs2': ["The inner child, the guards, and the inner adult’s three jobs, P1", "The inner child, the guards, and the inner adult’s three jobs, P2"],
    'HG-A-guards': ['Working with your guards, P3', 'Working with your guards, P4'],
    'HG-A-script': ['Your inherited parent script, P1'],
    'HG-B-altered': ['Appendix G: Altered states, P1'],
}


def main():
    md = MASTER.read_text(encoding='utf-8')
    bl = sr.blocks(md)
    by = {sr.where(bl, b['i']): b for b in bl}
    bundle, rec = {}, {'master_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(), 'items': {}}
    for key, wheres in ITEMS.items():
        text = '\n\n'.join(by[w]['text'] for w in wheres)
        n = len(text.split())
        assert 40 <= n <= 3000, (key, n)
        bundle[key] = text
        rec['items'][key] = {'paragraphs': wheres, 'blocks': [by[w]['i'] for w in wheres], 'words': n}
    out = json.dumps(bundle, ensure_ascii=False, indent=1) + '\n'
    (B / 'BUNDLE.json').write_text(out, encoding='utf-8')
    rec['bundle_sha256'] = hashlib.sha256(out.encode('utf-8')).hexdigest()
    (B / 'BUNDLE-RECORD.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print({k: v['words'] for k, v in rec['items'].items()}, rec['bundle_sha256'])


if __name__ == '__main__':
    main()
