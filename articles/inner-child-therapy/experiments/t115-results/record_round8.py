#!/usr/bin/env python3
"""Turn 115: round 8's two results (Joel's links of 2026-10-26 12:24 UTC, experiments/t115-answers/JOEL-20261026-1224.md),
the guide as installed in turn 114, in the two temporary Substack drafts.

Each feed page was read in the desktop app's built-in browser with tools/humanization/pangram_feed_read.js in compact mode:
the result's fields, the SHA-256 of its checked text, and its windows as compact lines (WINDOWS-A.txt, WINDOWS-B.txt, each
checked here against the page's own SHA-256 of that line). The checked text is rebuilt from the pasted payload
(tools/humanization/substack_check_text.py) with round 6's change to its quote rule (a straight double quote after "(" or
"—" is a closing one in this paste) and the embedded note as one curled line; both halves match the page's SHA-256 only
with them, as in round 6.

Every window is kept, and this time every window that isn't High-confidence Human is listed and placed: the AI windows,
and the Human ones of Medium or Low confidence (Joel, 2026-10-26: "let's start prioritizing working now on spots that are
not high confidence human ... it's important data to see in a large pangram test what's not high conf human, for learning,
and esp because pangram 5 will likely take the lower conf sections and turn some into AI sections as it did when 4.1 came
out"). Each item of round 8 (experiments/t114-substack/ITEMS.json) gets its words in AI windows and in windows that aren't
High-confidence Human, and each prediction (ledger #347 to #359) its result. Writes RESULT-A.json, RESULT-B.json,
TEXT-A.txt, TEXT-B.txt, ROUND8-RESULTS.json and SPOTS.json (every window that isn't High-confidence Human, with its text
and the paragraph of the article it falls in); --ledger also records the results."""
import hashlib
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SUB = HERE.parent / 't114-substack'
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
ART = ROOT / 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import substack_check_text as S  # noqa: E402

AT = '2026-10-26T12:24:00Z'   # his message, which carried the links
NOTE_URL = 'https://substack.com/profile/355021294-u-dont-existcom/note/c-349048098'
NOTE_LINE = ('wow, so true. it’s hard to trust people who trust people that dirsepect [or distrust] you… although, it matters '
             'that they know those people disrespect/distrust you, as well as whether the disrespect or distrust is earned or '
             'unearned, as well as how granular it is… like i don’t trust most people to tell me what i need to change about '
             'myself and be accurate and kind in that, but that doesn’t mean i don’t trust them in other ways. And i’d directly '
             'ask them why they trust those people who disrespect/distrust me?')
PAGES = {
    'A': {'link': 'https://www.pangram.com/feed/909d378e-11d2-4722-b988-a508256c78b4', 'created_at': '2026-10-26T08:21:13.779959-04:00',
          'version': '4.1', 'confidence_policy_id': 'pangram-4.1-calibrated-accuracy-v2', 'headline': 'Human Written',
          'prediction_short': 'Human', 'fraction_ai': 0.0036856394726783037, 'fraction_human': 0.9963143467903137,
          'fraction_breakdown': {'ai': {'low-confidence': 8.598032008588774e-11, 'high-confidence': 0.0023979737889021635,
                                        'medium-confidence': 0.0012876655673608184},
                                 'human': {'low-confidence': 1.3793233222259005e-07, 'high-confidence': 0.9950018525123596,
                                           'medium-confidence': 0.0013123925309628248}},
          'num_ai_segments': 1, 'num_human_segments': 91, 'word_count': 15205, 'n_windows': 93,
          'document_confidence': {'level': 'High', 'boundary': None},
          'text_sha256': 'fe0af5704e776438b1899b772a2c481e077622dad603701b40258fe50b0d71ea',
          'compact_sha256': '3ec2ba7867ce3e5c889659f23c05730037f34eb903797acf3cd9e4336b55d6f1',
          'windows_word_sum': 15108, 'windows_ai': 1, 'windows_human': 92},
    'B': {'link': 'https://www.pangram.com/feed/bd483bd6-edab-4f39-834c-3d959b0abb72', 'created_at': '2026-10-26T08:21:30.731076-04:00',
          'version': '4.1', 'confidence_policy_id': 'pangram-4.1-calibrated-accuracy-v2', 'headline': 'Human Written',
          'prediction_short': 'Human', 'fraction_ai': 0.0020749049726873636, 'fraction_human': 0.9979251027107239,
          'fraction_breakdown': {'ai': {'low-confidence': 4.949316512181667e-09, 'high-confidence': 0.0019322528969496489,
                                        'medium-confidence': 0.00014264702622313052},
                                 'human': {'low-confidence': 4.357226862339303e-05, 'high-confidence': 0.9976464509963989,
                                           'medium-confidence': 0.00023508425510954112}},
          'num_ai_segments': 3, 'num_human_segments': 83, 'word_count': 12815, 'n_windows': 87,
          'document_confidence': {'level': 'High', 'boundary': None},
          'text_sha256': '98e98e95838f4611dd5d4f9aa9929f232952be473aaa3c4459e7a1b5b739a258',
          'compact_sha256': '6165558e7784af90f62557731349144684ed63248238d533eb40809774bdcd08',
          'windows_word_sum': 12694, 'windows_ai': 3, 'windows_human': 84},
}
STRAIGHT = str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"'})


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def page_text(half):
    html = (SUB / ('PAYLOAD-%s.html' % half)).read_text(encoding='utf-8')
    keep = S.OPEN2
    S.OPEN2 = re.compile(r'(^|[\s\[{‘-])"')        # this paste, as round 6's: no opening quote after "(" or "—"
    try:
        t = S.checked_text(html, embeds={NOTE_URL: [NOTE_LINE]})
    finally:
        S.OPEN2 = keep
    assert sha(t) == PAGES[half]['text_sha256'], (half, sha(t))
    return t


def windows(half):
    line = (HERE / ('WINDOWS-%s.txt' % half)).read_text(encoding='utf-8').strip()
    assert sha(line) == PAGES[half]['compact_sha256'], half
    return [{'label': w['label'], 'confidence': w['confidence'], 'start': w['start_index'], 'end': w['end_index'],
             'words': w['word_count'], 'ai_likelihood': w['ai_likelihood'], 'is_humanized': w['is_humanized'],
             'calibrated_confidence': w['calibrated_confidence'], 'uncertainty_highlighting': w['uncertainty_highlighting']}
            for w in S.windows(line)]


def headings():
    md = re.sub(r'<!--.*?-->', '', ART.read_text(encoding='utf-8'), flags=re.S)
    out = []
    for l in md.split('\n'):
        m = re.match(r'^(#{1,6}) (.*)$', l)
        if m:
            out.append((len(m.group(1)), re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', m.group(2)).strip()))
    return out


def place(half, text, payload_lines, a, b):
    """The paragraph lines of the checked text that a window [a, b) touches, and the headings above it in the payload."""
    lines, pos, hit = text.split('\n'), 0, []
    for n, l in enumerate(lines):
        s, e = pos, pos + len(l)
        if s < b and e > a:
            hit.append(n)
        pos = e + 1
    return hit


def section_of(half, first_line):
    """The nearest h1..h4 heading above a checked line, found in the payload (headings aren't in the checked text)."""
    html = (SUB / ('PAYLOAD-%s.html' % half)).read_text(encoding='utf-8')
    blocks = re.findall(r'<(h[1-6]|p)>(.*?)</\1>', html, flags=re.S)
    import html as H
    want = first_line.translate(STRAIGHT)[:80]
    path = {}
    for tag, inner in blocks:
        t = H.unescape(re.sub(r'<[^>]+>', '', inner)).replace('\n', ' ')
        if tag != 'p':
            lvl = int(tag[1])
            path = {k: v for k, v in path.items() if k < lvl}
            path[lvl] = t
            continue
        if t.translate(STRAIGHT).startswith(want[:60]) or want[:60] in t.translate(STRAIGHT):
            return [path[k] for k in sorted(path)]
    return []


def main():
    res, items = {}, json.loads((SUB / 'ITEMS.json').read_text(encoding='utf-8'))
    texts, spots = {}, []
    for half in 'AB':
        t, ws = page_text(half), windows(half)
        assert ws[0]['start'] == 0 and ws[-1]['end'] == len(t) and all(x['end'] == y['start'] for x, y in zip(ws, ws[1:]))
        assert sum(w['words'] for w in ws) == PAGES[half]['windows_word_sum']
        assert sum(1 for w in ws if w['label'] != 'Human') == PAGES[half]['windows_ai']
        texts[half] = t
        (HERE / ('TEXT-%s.txt' % half)).write_text(t, encoding='utf-8')
        meta = dict(PAGES[half])
        (HERE / ('RESULT-%s.json' % half)).write_text(json.dumps(dict(meta, windows=ws, text=t), ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        lines = t.split('\n')
        for k, w in enumerate(ws):
            if w['label'] == 'Human' and w['confidence'] == 'High':
                continue
            hit = place(half, t, None, w['start'], w['end'])
            spots.append({'half': half, 'i': k, 'label': w['label'], 'confidence': w['confidence'], 'words': w['words'],
                          'calibrated_confidence': round(w['calibrated_confidence'], 4), 'ai_likelihood': w['ai_likelihood'],
                          'highlighted': w['uncertainty_highlighting'], 'start': w['start'], 'end': w['end'],
                          'text': t[w['start']:w['end']].strip(), 'lines': hit,
                          'section': section_of(half, lines[hit[0]]) if hit else []})
        ai = [s for s in spots if s['half'] == half and s['label'] != 'Human']
        res[half] = dict(link=meta['link'], created_at=meta['created_at'], version=meta['version'], headline=meta['headline'],
                         fraction_ai=meta['fraction_ai'], num_ai_segments=meta['num_ai_segments'], n_windows=meta['n_windows'],
                         word_count=meta['word_count'], document_confidence=meta['document_confidence'],
                         ai_windows=[{k: s[k] for k in ('i', 'confidence', 'words', 'start', 'end', 'text')} for s in ai],
                         not_high_human=sum(1 for s in spots if s['half'] == half), items={})
    for key, it in items.items():
        if it['scope'] == 'stretch':
            continue
        half, t = it['half'], texts[it['half']]
        body = [b for b in (SUB / 'items' / (key + '.txt')).read_text(encoding='utf-8').split('\n\n')]
        flat = t.translate(STRAIGHT)
        paras = [b for b in body if b.translate(STRAIGHT) in flat and len(b.split()) > 12]
        a = flat.find(paras[0].translate(STRAIGHT))
        b = flat.find(paras[-1].translate(STRAIGHT)) + len(paras[-1])
        assert 0 <= a < b, key
        hit_ai = [s for s in spots if s['half'] == half and s['label'] != 'Human' and s['start'] < b and s['end'] > a]
        hit_low = [s for s in spots if s['half'] == half and s['start'] < b and s['end'] > a]
        res[half]['items'][key] = {'ai_words': sum(s['words'] for s in hit_ai), 'not_high_human_words': sum(s['words'] for s in hit_low),
                                   'words': len(t[a:b].split()), 'ai_windows': [s['i'] for s in hit_ai],
                                   'not_high_human_windows': [s['i'] for s in hit_low], 'prediction': it['prediction'].split(':')[0]}
    (HERE / 'SPOTS.json').write_text(json.dumps(spots, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'ROUND8-RESULTS.json').write_text(json.dumps(dict(round=8, turn=115, how=__doc__.split('\n\n')[1].replace('\n', ' '), **res),
                                                          ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for half in 'AB':
        r = res[half]
        print(half, r['headline'], '%.2f%% AI' % (100 * r['fraction_ai']), len(r['ai_windows']), 'AI windows of', r['n_windows'],
              '|', r['not_high_human'], 'windows not High-confidence Human')
        for k, v in r['items'].items():
            print('   %-18s %3d of %4d words in AI windows, %3d not High Human %s' % (k, v['ai_words'], v['words'],
                                                                               v['not_high_human_words'], v['not_high_human_windows'] or ''))
    if '--ledger' in sys.argv:
        for key, it in items.items():
            half = it['half']
            if it['scope'] == 'stretch':
                r = res[half]
                verdict = 'Human' if r['fraction_ai'] == 0 else 'Mixed'
                head = '%s, %.2f%% AI, %d AI window%s of %d (%d windows not High-confidence Human)' % (
                    r['headline'], 100 * r['fraction_ai'], len(r['ai_windows']), '' if len(r['ai_windows']) == 1 else 's',
                    r['n_windows'], r['not_high_human'])
                frac, words = r['fraction_ai'], r['word_count']
            else:
                v = res[half]['items'][key]
                verdict = 'Human' if v['ai_words'] == 0 else 'Mixed'
                head = '%s inside the half check: %d of %d words in AI windows, %d in windows not High-confidence Human' % (
                    verdict, v['ai_words'], v['words'], v['not_high_human_words'])
                frac, words = round(v['ai_words'] / v['words'], 3), v['words']
            cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'result', str(LEDGER), '--key', key,
                   '--verdict', verdict, '--link', res[half]['link'], '--headline', head, '--ai-fraction', str(frac),
                   '--words', str(words), '--detector', 'pangram-4.1-substack', '--at', AT]
            out = subprocess.run(cmd, capture_output=True, text=True)
            if out.returncode:
                sys.exit(out.stdout + out.stderr)
            print(out.stdout.strip().split('\n')[-1])


if __name__ == '__main__':
    main()
