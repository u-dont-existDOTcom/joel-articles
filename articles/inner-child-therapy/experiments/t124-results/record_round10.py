#!/usr/bin/env python3
"""Turn 124: round 10's two results (Joel's links of 2026-11-04 15:00 UTC, experiments/t124-answers/JOEL-20261104-1500.md), his
reorganized guide as it was after turn 123 (his marking-page versions of turn 122 in, his three typos fixed), in the two
temporary Substack drafts (experiments/t123-substack/PASTED.json).

Each feed page was read in the desktop app's built-in browser with tools/humanization/pangram_feed_read.js in compact mode:
the result's fields, the SHA-256 of its checked text, and its windows as compact lines (WINDOWS-A.txt, WINDOWS-B.txt, each
checked here against the page's own SHA-256 of that line). The checked text is the check text made with the payload
(experiments/t123-substack/CHECK-A.txt, CHECK-B.txt); B's matches the page's SHA-256 as it is, and A's once the one no-break
space of his "Breadcrumbing is" is a plain space, as Substack shows it (the preview check of turn 123 found the same).

Every window is kept, and every window that isn't High-confidence Human is listed and placed, with the heading above it,
its words, and whether they are his words as his reorganized guide has them (experiments/t116-joel/JOEL-GUIDE-20261103.md)
(Joel, 2026-10-26: "let's start prioritizing working now on spots that are not high confidence human"; the Low ones first,
AGENTS.md). Writes RESULT-A.json, RESULT-B.json, ROUND10-RESULTS.json and SPOTS.json; --ledger also records the two results
against predictions t123s-A#380 and t123s-B#381."""
import hashlib
import html as H
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SUB = HERE.parent / 't123-substack'
GUIDE = HERE.parent / 't116-joel' / 'JOEL-GUIDE-20261103.md'
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import substack_check_text as S  # noqa: E402

AT = '2026-11-04T15:00:00Z'   # his message, which carried the links
COMMON = {'version': '4.1', 'confidence_policy_id': 'pangram-4.1-calibrated-accuracy-v2', 'headline': 'Human Written',
          'prediction_short': 'Human', 'fraction_human': 1, 'num_ai_segments': 0,
          'document_confidence': {'level': 'High', 'boundary': None}, 'domain': 'substack', 'content_type': 'long_post'}
PAGES = {
    'A': dict(COMMON, link='https://www.pangram.com/feed/26ca9a6d-2636-43b6-a68f-5478fe8e388d',
              created_at='2026-11-04T09:34:45.484384-05:00', task_id='deff62a6-b431-4e00-8128-19a24e5a97bf',
              fraction_ai=5.31043814027935e-20,
              fraction_breakdown={'ai': {'low-confidence': 5.31043814027935e-20, 'high-confidence': 0, 'medium-confidence': 0},
                                  'human': {'low-confidence': 0, 'high-confidence': 1, 'medium-confidence': 0},
                                  'ai-assisted': {'lightly': 6.13891950873444e-24, 'moderately': 0}},
              verdict_support={'ai': 0, 'human': 1, 'mixed': 0, 'source': 'sentence_dp', 'ai_threshold': 0.800000011920929,
                               'human_threshold': 0.8999999761581421, 'human_coverage_mean': 0.9997223019599915},
              num_human_segments=3, word_count=16953, n_windows=11,
              text_sha256='7f3a9506b810be9219c52ce91e957e61e731b4fb0beb35d4090c24bf5926a297',
              compact_sha256='9ce351707c30a78b231ad12d090eb2b553af26710338d68caf7400bbb15973be',
              windows_word_sum=16276, windows_ai=0, windows_human=11),
    'B': dict(COMMON, link='https://www.pangram.com/feed/fd028698-3e86-44a3-ba40-17c95dcbcb08',
              created_at='2026-11-04T09:35:39.979458-05:00', task_id='bb66e4e3-37b9-4354-9070-6c960957a991',
              fraction_ai=1.0215352794712168e-18,
              fraction_breakdown={'ai': {'low-confidence': 1.0215352794712168e-18, 'high-confidence': 0, 'medium-confidence': 0},
                                  'human': {'low-confidence': 0, 'high-confidence': 1, 'medium-confidence': 0},
                                  'ai-assisted': {'lightly': 2.1274962166344912e-21, 'moderately': 0}},
              verdict_support={'ai': 0, 'human': 1, 'mixed': 0, 'source': 'sentence_dp', 'ai_threshold': 0.800000011920929,
                               'human_threshold': 0.8999999761581421, 'human_coverage_mean': 0.999814510345459},
              num_human_segments=5, word_count=11941, n_windows=10,
              text_sha256='2db7a2d3a917083b0d84c7110ad87767d26aafac294a515e6bb4e56f4a49e123',
              compact_sha256='53dd9945daa96cd113b174ff209a720d6ff846fbb47325edc42828490832f6f8',
              windows_word_sum=11481, windows_ai=0, windows_human=10),
}
PREDICTION = {'A': 't123s-A#380', 'B': 't123s-B#381'}
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
            json.dumps(dict(meta, check_text='experiments/t123-substack/CHECK-%s.txt' % half, windows=ws), ensure_ascii=False,
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
    (HERE / 'ROUND10-RESULTS.json').write_text(
        json.dumps(dict(round=10, turn=124, how=__doc__.split('\n\n')[1].replace('\n', ' '), **res), ensure_ascii=False,
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
            head = '%s, %.2f%% AI, %d AI window%s of %d (%d windows not High-confidence Human: %d Medium, %d Low)' % (
                r['headline'], 100 * r['fraction_ai'], len(r['ai_windows']), '' if len(r['ai_windows']) == 1 else 's',
                r['n_windows'], r['not_high_human'], r['by_confidence']['Medium'], r['by_confidence']['Low'])
            cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'result', str(LEDGER),
                   '--key', 't123s_%s' % half, '--verdict', 'Human' if r['fraction_ai'] < 1e-9 else 'Mixed',
                   '--ai-fraction', str(r['fraction_ai']), '--words', str(r['word_count']), '--link', r['link'],
                   '--headline', head, '--detector', 'pangram-4.1-substack', '--at', AT]
            p = subprocess.run(cmd, capture_output=True, text=True)
            print((p.stdout.strip() or p.stderr.strip())[-300:])
    return 0


if __name__ == '__main__':
    sys.exit(main())
