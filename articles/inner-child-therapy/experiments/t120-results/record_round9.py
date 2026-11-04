#!/usr/bin/env python3
"""Turn 120: round 9's two results (Joel's links of 2026-11-04 09:42 UTC, experiments/t120-answers/JOEL-20261104-0942.md), his
reorganized guide as it was after turn 118, in the two temporary Substack drafts (experiments/t119-substack/).

Each feed page was read in the desktop app's built-in browser with tools/humanization/pangram_feed_read.js in compact mode:
the result's fields, the SHA-256 of its checked text, and its windows as compact lines (WINDOWS-A.txt, WINDOWS-B.txt, each
checked here against the page's own SHA-256 of that line). The checked text is rebuilt from the pasted payload
(tools/humanization/substack_check_text.py); B's matches the page's SHA-256 as it is, and A's once the one no-break space
of his "Breadcrumbing is" is a plain space, as Substack shows it (the preview check of turn 119 found the same).

Every window is kept, and every window that isn't High-confidence Human is listed and placed, with the heading above it
and its words (Joel, 2026-10-26: "let's start prioritizing working now on spots that are not high confidence human").
Writes RESULT-A.json, RESULT-B.json, TEXT-A.txt, TEXT-B.txt, ROUND9-RESULTS.json and SPOTS.json; --ledger also records
the two results against predictions t119s-A#373 and t119s-B#374."""
import hashlib
import html as H
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SUB = HERE.parent / 't119-substack'
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import substack_check_text as S  # noqa: E402

AT = '2026-11-04T09:42:00Z'   # his message, which carried the links
PAGES = {
    'A': {'link': 'https://www.pangram.com/feed/a3f14949-326d-492a-b65a-8b048ca74940', 'created_at': '2026-11-03T20:05:44.335632-05:00',
          'version': '4.1', 'confidence_policy_id': 'pangram-4.1-calibrated-accuracy-v2', 'headline': 'Human Written',
          'prediction_short': 'Human', 'fraction_ai': 1.0019838691394112e-12, 'fraction_human': 1,
          'fraction_breakdown': {'ai': {'low-confidence': 1.0019838691394112e-12, 'high-confidence': 0, 'medium-confidence': 0},
                                 'human': {'low-confidence': 0, 'high-confidence': 1, 'medium-confidence': 0}},
          'num_ai_segments': 0, 'num_human_segments': 13, 'word_count': 16918, 'n_windows': 20,
          'document_confidence': {'level': 'High', 'boundary': None},
          'text_sha256': 'c5da7add5b14e6a3172c8bcf1f992326147bccf3b726adaf0bdc5aad65a3c7d0',
          'compact_sha256': 'ca5c3705c8c8be12412cc41e45da2235d0ec783b5b8cc6ee322759992a80f236',
          'windows_word_sum': 16296, 'windows_ai': 0, 'windows_human': 20},
    'B': {'link': 'https://www.pangram.com/feed/f3b33647-484f-4203-9709-db0b04ab8f2d', 'created_at': '2026-11-03T20:08:20.086788-05:00',
          'version': '4.1', 'confidence_policy_id': 'pangram-4.1-calibrated-accuracy-v2', 'headline': 'Human Written',
          'prediction_short': 'Human', 'fraction_ai': 0.0029144510626792908, 'fraction_human': 0.9970855712890625,
          'fraction_breakdown': {'ai': {'low-confidence': 1.0502418490432319e-07, 'high-confidence': 0.0029143458232283592,
                                        'medium-confidence': 0},
                                 'human': {'low-confidence': 1.5487692905935546e-08, 'high-confidence': 0.9970855116844177,
                                           'medium-confidence': 0}},
          'num_ai_segments': 1, 'num_human_segments': 35, 'word_count': 11849, 'n_windows': 39,
          'document_confidence': {'level': 'High', 'boundary': None},
          'text_sha256': 'ffdc601f8292c9a41972bab57405361abf066e573ea51c783fe812571a656d6d',
          'compact_sha256': 'e330261fc8938a20eaf74e8edb5ff38e9baf85545ed776376d1c4e4a8df3b302',
          'windows_word_sum': 11502, 'windows_ai': 1, 'windows_human': 38},
}
PREDICTION = {'A': 't119s-A#373', 'B': 't119s-B#374'}


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def page_text(half):
    t = S.checked_text((SUB / ('PAYLOAD-%s.html' % half)).read_text(encoding='utf-8'))
    if sha(t) != PAGES[half]['text_sha256']:
        t = t.replace('\xa0', ' ')   # Substack shows his no-break space as a plain one
    assert sha(t) == PAGES[half]['text_sha256'], (half, sha(t))
    return t


def windows(half):
    line = (HERE / ('WINDOWS-%s.txt' % half)).read_text(encoding='utf-8').strip()
    assert sha(line) == PAGES[half]['compact_sha256'], half
    return [{'label': w['label'], 'confidence': w['confidence'], 'start': w['start_index'], 'end': w['end_index'],
             'words': w['word_count'], 'ai_likelihood': w['ai_likelihood'], 'is_humanized': w['is_humanized'],
             'calibrated_confidence': w['calibrated_confidence'], 'uncertainty_highlighting': w['uncertainty_highlighting']}
            for w in S.windows(line)]


def section_of(half, text, a):
    """The headings above checked-text offset A: the payload's blocks in order, headings kept, matched to the text's lines."""
    body = (SUB / ('PAYLOAD-%s.html' % half)).read_text(encoding='utf-8')
    lines = text.split('\n')
    n, pos = 0, 0
    for k, l in enumerate(lines):
        if pos + len(l) >= a:
            n = k
            break
        pos += len(l) + 1
    want = lines[n][:60].translate(S.STRAIGHT) if hasattr(S, 'STRAIGHT') else lines[n][:60]
    path = {}
    for tag, inner in re.findall(r'<(h[1-6]|p)>(.*?)</\1>', body, flags=re.S):
        t = H.unescape(re.sub(r'<[^>]+>', ' ', inner))
        t = re.sub(r'\s+', ' ', t).strip()
        if tag != 'p':
            lvl = int(tag[1])
            path = {k: v for k, v in path.items() if k < lvl}
            path[lvl] = t
            continue
        st = t.translate(str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"'}))
        if st.startswith(lines[n][:50].translate(str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"'})).replace('\xa0', ' ')):
            return [path[k] for k in sorted(path)], n
    return [], n


def main():
    res, spots = {}, []
    for half in 'AB':
        t, ws = page_text(half), windows(half)
        assert ws[0]['start'] == 0 and ws[-1]['end'] == len(t) and all(x['end'] == y['start'] for x, y in zip(ws, ws[1:]))
        assert sum(w['words'] for w in ws) == PAGES[half]['windows_word_sum']
        assert sum(1 for w in ws if w['label'] != 'Human') == PAGES[half]['windows_ai']
        (HERE / ('TEXT-%s.txt' % half)).write_text(t, encoding='utf-8')
        meta = dict(PAGES[half])
        (HERE / ('RESULT-%s.json' % half)).write_text(json.dumps(dict(meta, windows=ws, text=t), ensure_ascii=False, indent=1) + '\n',
                                                     encoding='utf-8')
        for k, w in enumerate(ws):
            if w['label'] == 'Human' and w['confidence'] == 'High':
                continue
            sec, line = section_of(half, t, w['start'])
            spots.append({'half': half, 'i': k, 'label': w['label'], 'confidence': w['confidence'], 'words': w['words'],
                          'calibrated_confidence': round(w['calibrated_confidence'], 4), 'ai_likelihood': w['ai_likelihood'],
                          'highlighted': w['uncertainty_highlighting'], 'start': w['start'], 'end': w['end'],
                          'text': t[w['start']:w['end']].strip(), 'line': line, 'section': sec})
        mine = [s for s in spots if s['half'] == half]
        res[half] = dict(link=meta['link'], created_at=meta['created_at'], version=meta['version'], headline=meta['headline'],
                         fraction_ai=meta['fraction_ai'], num_ai_segments=meta['num_ai_segments'], n_windows=meta['n_windows'],
                         word_count=meta['word_count'], document_confidence=meta['document_confidence'],
                         ai_windows=[{k: s[k] for k in ('i', 'confidence', 'words', 'start', 'end', 'text', 'section')} for s in mine if s['label'] != 'Human'],
                         not_high_human=len(mine),
                         by_confidence={c: sum(1 for s in mine if s['label'] == 'Human' and s['confidence'] == c) for c in ('Medium', 'Low')})
    (HERE / 'SPOTS.json').write_text(json.dumps(spots, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'ROUND9-RESULTS.json').write_text(json.dumps(dict(round=9, turn=120, how=__doc__.split('\n\n')[1].replace('\n', ' '), **res),
                                                          ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for half in 'AB':
        r = res[half]
        print(half, r['headline'], '%.2f%% AI' % (100 * r['fraction_ai']), len(r['ai_windows']), 'AI windows of', r['n_windows'],
              '|', r['not_high_human'], 'not High-confidence Human:', r['by_confidence'])
    if '--ledger' in sys.argv:
        for half in 'AB':
            r = res[half]
            head = '%s, %.2f%% AI, %d AI window%s of %d (%d windows not High-confidence Human)' % (
                r['headline'], 100 * r['fraction_ai'], len(r['ai_windows']), '' if len(r['ai_windows']) == 1 else 's',
                r['n_windows'], r['not_high_human'])
            cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'result', str(LEDGER),
                   '--key', 't119s_%s' % half, '--verdict', 'Human' if r['fraction_ai'] < 1e-9 else 'Mixed',
                   '--ai-fraction', str(r['fraction_ai']), '--words', str(r['word_count']), '--link', r['link'],
                   '--headline', head, '--detector', 'pangram-4.1-substack', '--at', AT]
            p = subprocess.run(cmd, capture_output=True, text=True)
            print((p.stdout.strip() or p.stderr.strip())[-300:])
    return 0


if __name__ == '__main__':
    sys.exit(main())
