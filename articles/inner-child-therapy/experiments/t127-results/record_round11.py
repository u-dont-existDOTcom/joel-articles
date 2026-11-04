#!/usr/bin/env python3
"""Turn 127: round 11's two results (Joel's links of 2026-11-04 17:12 UTC, experiments/t127-answers/JOEL-20261104-1712.md), his
guide as it will be published (his sense-read answers of turn 125 and his two hyphens for its dashes, turn 126), in the two
temporary Substack drafts (experiments/t126-substack/PASTED.json). He asked whether they were the pages of the tabs I opened
or old ones: both were made at 16:46 UTC, after the paste, and each page's checked text is round 11's (below).

Each feed page was read in the desktop app's built-in browser with tools/humanization/pangram_feed_read.js in compact mode:
the result's fields, the SHA-256 of its checked text, and its windows as compact lines (WINDOWS-A.txt, WINDOWS-B.txt, each
checked here against the page's own SHA-256 of that line). The checked text is the check text made with the payload
(experiments/t126-substack/CHECK-A.txt, CHECK-B.txt); B's matches the page's SHA-256 as it is, and A's once the one no-break
space of his "Breadcrumbing is" is a plain space, as Substack shows it (the preview check of turn 126 found the same).

Every window is kept, and every window that isn't High-confidence Human is listed and placed, with the heading above it,
its words, and whether they are his words as his reorganized guide has them (experiments/t116-joel/JOEL-GUIDE-20261103.md)
(Joel, 2026-10-26: "let's start prioritizing working now on spots that are not high confidence human"; the Low ones first,
AGENTS.md). Writes RESULT-A.json, RESULT-B.json, ROUND11-RESULTS.json and SPOTS.json; --ledger also records the two results
against predictions t126s-A#382 and t126s-B#383."""
import hashlib
import html as H
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SUB = HERE.parent / 't126-substack'
GUIDE = HERE.parent / 't116-joel' / 'JOEL-GUIDE-20261103.md'
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import substack_check_text as S  # noqa: E402

AT = '2026-11-04T17:12:00Z'   # his message, which carried the links
COMMON = {'version': '4.1', 'confidence_policy_id': 'pangram-4.1-calibrated-accuracy-v2', 'headline': 'Human Written',
          'prediction_short': 'Human', 'fraction_human': 1, 'num_ai_segments': 0,
          'document_confidence': {'level': 'High', 'boundary': None}, 'domain': 'substack', 'content_type': 'long_post'}
PAGES = {
    'A': dict(COMMON, link='https://www.pangram.com/feed/aca1a2dd-66a8-4a00-97b8-0d4a64785fdf',
              created_at='2026-11-04T11:46:14.795420-05:00', task_id='6e68f145-91cf-4f10-8a82-be6a18c84764',
              fraction_ai=4.96208330376486e-19,
              fraction_breakdown={'ai': {'low-confidence': 4.96208330376486e-19, 'high-confidence': 0, 'medium-confidence': 0},
                                  'human': {'low-confidence': 0, 'high-confidence': 1, 'medium-confidence': 0},
                                  'ai-assisted': {'lightly': 2.176425427876795e-23, 'moderately': 0}},
              verdict_support={'ai': 0, 'human': 1, 'mixed': 0, 'source': 'sentence_dp', 'ai_threshold': 0.800000011920929,
                               'human_threshold': 0.8999999761581421, 'human_coverage_mean': 0.9997889399528503},
              num_human_segments=3, word_count=16955, n_windows=11,
              text_sha256='c68c4c61b265c1e062c236809a73d80ccdad6631f042f5f14b64433289ab8122',
              compact_sha256='7568ebb883c4a00778b268b713ae1bbaa8d16b90d0e7aca72d2cf1200eb9e5a4',
              windows_word_sum=16270, windows_ai=0, windows_human=11),
    'B': dict(COMMON, link='https://www.pangram.com/feed/6c933a47-c73e-45e2-825b-173a3603969e',
              created_at='2026-11-04T11:46:14.085388-05:00', task_id='1682a878-b4f8-4326-8ce9-12f25d12142b',
              fraction_ai=8.337899407436912e-19,
              fraction_breakdown={'ai': {'low-confidence': 8.337899407436912e-19, 'high-confidence': 0, 'medium-confidence': 0},
                                  'human': {'low-confidence': 0, 'high-confidence': 1, 'medium-confidence': 0},
                                  'ai-assisted': {'lightly': 2.4183645047366034e-21, 'moderately': 0}},
              verdict_support={'ai': 0, 'human': 1, 'mixed': 0, 'source': 'sentence_dp', 'ai_threshold': 0.800000011920929,
                               'human_threshold': 0.8999999761581421, 'human_coverage_mean': 1},
              num_human_segments=5, word_count=11945, n_windows=10,
              text_sha256='b5b37505609860eabd2a26547a2fe32249b30639371df93b1e25fe82e7923823',
              compact_sha256='d366f8d014606d34ac027d9421d85b4119828726c4ae9ffcf82df0c7c34500ab',
              windows_word_sum=11485, windows_ai=0, windows_human=10),
}
PREDICTION = {'A': 't126s-A#382', 'B': 't126s-B#383'}
STRAIGHT = str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"', '\xa0': ' '})


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def page_text(half):
    t = (SUB / ('CHECK-%s.txt' % half)).read_text(encoding='utf-8')
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
    path = {}
    for tag, inner in re.findall(r'<(h[1-6]|p)>(.*?)</\1>', body, flags=re.S):
        t = H.unescape(re.sub(r'<[^>]+>', ' ', inner))
        t = re.sub(r'\s+', ' ', t).strip()
        if tag != 'p':
            lvl = int(tag[1])
            path = {k: v for k, v in path.items() if k < lvl}
            path[lvl] = t
            continue
        if t.translate(STRAIGHT).startswith(lines[n][:50].translate(STRAIGHT)):
            return [path[k] for k in sorted(path)], n
    return [], n


def main():
    guide = re.sub(r'\s+', ' ', GUIDE.read_text(encoding='utf-8').translate(STRAIGHT))
    res, spots = {}, []
    for half in 'AB':
        t, ws = page_text(half), windows(half)
        assert ws[0]['start'] == 0 and ws[-1]['end'] == len(t) and all(x['end'] == y['start'] for x, y in zip(ws, ws[1:]))
        assert len(ws) == PAGES[half]['n_windows']
        assert sum(w['words'] for w in ws) == PAGES[half]['windows_word_sum']
        assert sum(1 for w in ws if w['label'] != 'Human') == PAGES[half]['windows_ai']
        meta = dict(PAGES[half])
        (HERE / ('RESULT-%s.json' % half)).write_text(
            json.dumps(dict(meta, check_text='experiments/t126-substack/CHECK-%s.txt' % half, windows=ws), ensure_ascii=False,
                       indent=1) + '\n', encoding='utf-8')
        for k, w in enumerate(ws):
            if w['label'] == 'Human' and w['confidence'] == 'High':
                continue
            sec, line = section_of(half, t, w['start'])
            words = t[w['start']:w['end']].strip()
            lines = t.split('\n')
            spots.append({'half': half, 'i': k, 'label': w['label'], 'confidence': w['confidence'], 'words': w['words'],
                          'calibrated_confidence': round(w['calibrated_confidence'], 4), 'ai_likelihood': w['ai_likelihood'],
                          'highlighted': w['uncertainty_highlighting'], 'start': w['start'], 'end': w['end'],
                          'text': words, 'in_line': lines[line], 'line': line, 'section': sec,
                          'his_words': re.sub(r'\s+', ' ', lines[line].translate(STRAIGHT)).strip() in guide})
        mine = [s for s in spots if s['half'] == half]
        res[half] = dict(link=meta['link'], created_at=meta['created_at'], version=meta['version'], headline=meta['headline'],
                         fraction_ai=meta['fraction_ai'], num_ai_segments=meta['num_ai_segments'], n_windows=meta['n_windows'],
                         word_count=meta['word_count'], document_confidence=meta['document_confidence'],
                         ai_windows=[{k: s[k] for k in ('i', 'confidence', 'words', 'start', 'end', 'text', 'section')}
                                     for s in mine if s['label'] != 'Human'],
                         not_high_human=len(mine),
                         by_confidence={c: sum(1 for s in mine if s['label'] == 'Human' and s['confidence'] == c)
                                        for c in ('Medium', 'Low')})
    (HERE / 'SPOTS.json').write_text(json.dumps(spots, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'ROUND11-RESULTS.json').write_text(
        json.dumps(dict(round=11, turn=127, how=__doc__.split('\n\n')[1].replace('\n', ' '), **res), ensure_ascii=False,
                   indent=1) + '\n', encoding='utf-8')
    for half in 'AB':
        r = res[half]
        print(half, r['headline'], '%.2f%% AI' % (100 * r['fraction_ai']), len(r['ai_windows']), 'AI windows of', r['n_windows'],
              '|', r['not_high_human'], 'not High-confidence Human:', r['by_confidence'])
    for s in spots:
        print('  %s w%d %s (%s) %d words, his words: %s, %s: %r' % (s['half'], s['i'], s['label'], s['confidence'], s['words'],
                                                                  s['his_words'], ' > '.join(s['section'][-2:]), s['text']))
    if '--ledger' in sys.argv:
        for half in 'AB':
            r = res[half]
            head = '%s, %.2f%% AI, %d AI window%s of %d (%d window%s not High-confidence Human: %d Medium, %d Low)' % (
                r['headline'], 100 * r['fraction_ai'], len(r['ai_windows']), '' if len(r['ai_windows']) == 1 else 's',
                r['n_windows'], r['not_high_human'], '' if r['not_high_human'] == 1 else 's', r['by_confidence']['Medium'],
                r['by_confidence']['Low'])
            cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'result', str(LEDGER),
                   '--key', 't126s_%s' % half, '--verdict', 'Human' if r['fraction_ai'] < 1e-9 else 'Mixed',
                   '--ai-fraction', str(r['fraction_ai']), '--words', str(r['word_count']), '--link', r['link'],
                   '--headline', head, '--detector', 'pangram-4.1-substack', '--at', AT]
            p = subprocess.run(cmd, capture_output=True, text=True)
            print((p.stdout.strip() or p.stderr.strip())[-300:])
    return 0


if __name__ == '__main__':
    sys.exit(main())
