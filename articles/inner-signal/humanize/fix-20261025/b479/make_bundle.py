"""Batch 479: the red windows of the whole guide's recheck of 2026-10-25 (parts A and B, read after Joel's message of
23:50 UTC: ../recheck/RESULT-A.json and RESULT-B.json, scored in SCORE-A.md and SCORE-B.md) go to Emulate first (E237,
E235): BUNDLE.json, one text per red stretch, each the red paragraph as it stands in HUMANIZED-SO-FAR.md with the
paragraph before it where the red paragraph alone is short. Only the red sentences come back from a sample (the splice);
the hypnosis audit's questions (part B, High) stay a list by his answer 2c and are not sent.

  python3 articles/inner-signal/humanize/fix-20261025/b479/make_bundle.py   (from the repo root)
"""
import hashlib, json, pathlib, re, sys

B = pathlib.Path(__file__).resolve().parent
ROOT = B.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

# key: (the paragraphs sent, by sr.where label, in order; what's red in it, from the recheck)
ITEMS = {
    'HG-A-jobs': (["The inner child, the guards, and the inner adult’s three jobs, P1",
                   "The inner child, the guards, and the inner adult’s three jobs, P2"],
                  'part A, Low: "That’s one grown-up doing three jobs, and each job keeps the others in balance." (IC-A2)'),
    'HG-A-borrowed': (["When the adult role is not available yet, P1", "When the adult role is not available yet, P2"],
                      'part A, High: P2 whole (EM-2: Emulate\'s first sentence and my plainer words for his published line)'),
    'HG-A-stop': (["Before you begin, P3", "Before you begin, P4"],
                  'part A, five Low windows marked humanized: P3\'s last sentence (RR-4.6), P4\'s "Deciding to do it." (TY-6) '
                  'and its last four sentences (RR-4.1\'s quote marks and "say"; the last two unchanged since A4)'),
    'HG-B-act': (["Core prompts, P8"],
                 'part B, Low and High: "It should make sense, too. Even then, anything big or hard to undo can wait until '
                 'you’re calm and you’ve checked it against what you actually know." (IC-B12, his inner child guide\'s words)'),
    'HG-B-love': (["Inner child love, P1"],
                  'part B, Low, Medium, High: from "You don’t have to fix it." to the end, the High one IC-B14\'s added '
                  '"No warmth today? ..." (also in part A, IC-A10, where it read Human), and the anxiety script\'s opening after it (Low)'),
    'HG-B-test': (["A response check, not a verdict about what it is, P3", "A response check, not a verdict about what it is, P4"],
                  'part B, High: P4\'s last sentence, his published test, put back by EM-16'),
}


def main():
    md = (ROOT / 'articles/inner-signal/humanize/HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    bl = sr.blocks(md)
    by = {sr.where(bl, b['i']): b for b in bl}
    bundle, record = {}, {'guide_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(), 'items': {}}
    for key, (wheres, red) in ITEMS.items():
        paras = [by[w]['text'] for w in wheres]
        text = '\n\n'.join(paras)
        n = len(text.split())
        assert 40 <= n <= 3000, (key, n)
        bundle[key] = text
        record['items'][key] = {'paragraphs': wheres, 'blocks': [by[w]['i'] for w in wheres], 'words': n, 'red': red}
    out = json.dumps(bundle, ensure_ascii=False, indent=1) + '\n'
    (B / 'BUNDLE.json').write_text(out, encoding='utf-8')
    record['bundle_sha256'] = hashlib.sha256(out.encode('utf-8')).hexdigest()
    (B / 'BUNDLE-RECORD.json').write_text(json.dumps(record, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print({k: v['words'] for k, v in record['items'].items()}, 'total', sum(v['words'] for v in record['items'].values()))
    print('BUNDLE.json sha256', record['bundle_sha256'])


if __name__ == '__main__':
    main()
