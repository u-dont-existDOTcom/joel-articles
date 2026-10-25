#!/usr/bin/env python3
"""Turn 108: round 6's two results (Joel's links of 2026-10-25 12:39 UTC, experiments/t108-answers/JOEL-20261025-1239.md).

Each feed page was read in his Brave through Claude in Chrome: the result's fields and the SHA-256 of its checked text, and
its windows as compact lines (WINDOWS-A.txt, WINDOWS-B.txt, each checked against the page's own SHA-256 of that line).
The checked text is rebuilt from the pasted payload (tools/humanization/substack_check_text.py) with two changes that
this paste needed to reach the page's SHA-256:
  - Substack showed a straight double quote after "(" or "—" as a closing quote (four places: Céline's song, the porch
    story's "Once upon a time", the photos' "You hated that coat", and "I hate cooking"), where the tool's rule makes it
    an opening one;
  - half B's embedded note reads as one line, its body with curly apostrophes, given here as NOTE_LINE.
Then every item of round 6 (experiments/t107-substack/ITEMS.json) is found in its half's checked text, its words in AI
windows are counted, and each prediction (ledger #262 to #280) gets its result. Writes RESULT-A.json, RESULT-B.json,
TEXT-A.txt, TEXT-B.txt (the checked texts) and ROUND6-RESULTS.json; --ledger also records the results."""
import hashlib
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SUB = HERE.parent / 't107-substack'
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import substack_check_text as S  # noqa: E402

AT = '2026-10-25T12:39:00Z'   # his message, which carried the links
NOTE_URL = 'https://substack.com/profile/355021294-u-dont-existcom/note/c-349048098'
NOTE_LINE = ('wow, so true. it’s hard to trust people who trust people that dirsepect [or distrust] you… although, it matters '
             'that they know those people disrespect/distrust you, as well as whether the disrespect or distrust is earned or '
             'unearned, as well as how granular it is… like i don’t trust most people to tell me what i need to change about '
             'myself and be accurate and kind in that, but that doesn’t mean i don’t trust them in other ways. And i’d directly '
             'ask them why they trust those people who disrespect/distrust me?')
PAGES = {
    'A': {'link': 'https://www.pangram.com/feed/41dfb451-494d-4a13-a76c-335d372dbd4a', 'created_at': '2026-10-24T21:02:10.258793-04:00',
          'version': '4.1', 'headline': 'Human Written', 'prediction_short': 'Human', 'fraction_ai': 0.0019581743981689215,
          'fraction_human': 0.9980418086051941, 'num_ai_segments': 1, 'word_count': 15393, 'n_windows': 102,
          'document_confidence': {'level': 'High', 'boundary': None},
          'text_sha256': '30ca43e5d0810ea084d600f18ab14a06ee0b304587d7e5f6664cc70a602291e4',
          'compact_sha256': '4fc9fd57882af813d92b04db84203dcf8bb124c51f49dfdc71531183c9c8043b'},
    'B': {'link': 'https://www.pangram.com/feed/64c71597-3987-48a7-8431-c8bdc70fddcc', 'created_at': '2026-10-24T21:05:30.200060-04:00',
          'version': '4.1', 'headline': 'Human Written', 'prediction_short': 'Human', 'fraction_ai': 0.0038868840783834457,
          'num_ai_segments': 3, 'word_count': 12866, 'n_windows': 106, 'document_confidence': {'level': 'High', 'boundary': None},
          'text_sha256': '9659da7d06eb2c1866caa2d2b877bbee9f9753221db63cba5a0988890f9b3711',
          'compact_sha256': 'dc1a697aef6be59e412564a2365a0dc74417e3ae96f5e9e1749c9b585f8c3f96'},
}
STRAIGHT = str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"'})


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def page_text(half):
    html = (SUB / ('PAYLOAD-%s.html' % half)).read_text(encoding='utf-8')
    keep = S.OPEN2
    S.OPEN2 = re.compile(r'(^|[\s\[{‘-])"')        # this paste: no opening quote after "(" or "—"
    try:
        t = S.checked_text(html, embeds={NOTE_URL: [NOTE_LINE]})
    finally:
        S.OPEN2 = keep
    assert sha(t) == PAGES[half]['text_sha256'], (half, sha(t))
    return t


def windows(half):
    line = (HERE / ('WINDOWS-%s.txt' % half)).read_text(encoding='utf-8').strip()
    assert sha(line) == PAGES[half]['compact_sha256'], half
    out = []
    for e in line.split(';'):
        f = e.split(',')
        out.append({'label': 'AI-Generated' if f[0] == 'A' else 'Human', 'confidence': {'H': 'High', 'M': 'Medium', 'L': 'Low'}[f[1]],
                    'start': int(f[2]), 'end': int(f[3]), 'words': int(f[4]), 'ai_likelihood': float(f[5]),
                    'is_humanized': f[6] == '1', 'calibrated_confidence': float(f[7]), 'uncertainty_highlighting': f[8] == '1'})
    return out


HEADS = None


def span(item_text, text):
    """(start, end) of an item in the checked text: its paragraphs without its heading, matched with quotes straightened."""
    global HEADS
    if HEADS is None:
        md = re.sub(r'<!--.*?-->', '', (ROOT / 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8'), flags=re.S)
        HEADS = {re.sub(r'^#+\s*', '', l).strip() for l in md.split('\n') if re.match(r'^#{1,5} ', l)}
    blocks = [b for b in item_text.split('\n\n') if b.strip() and b.strip() not in HEADS]
    flat = text.translate(STRAIGHT)
    first, last = blocks[0].translate(STRAIGHT), blocks[-1].translate(STRAIGHT)
    a = flat.find(first[:120])
    assert a >= 0 and flat.find(first[:120], a + 1) < 0, ('not once', item_text[:60])
    b = flat.find(last[-120:], a)
    assert b >= 0, ('end not found', item_text[:60])
    return a, b + len(last[-120:])


def main():
    res, items = {}, json.loads((SUB / 'ITEMS.json').read_text(encoding='utf-8'))
    texts = {}
    for half in 'AB':
        t, ws = page_text(half), windows(half)
        assert ws[0]['start'] == 0 and ws[-1]['end'] == len(t) and all(x['end'] == y['start'] for x, y in zip(ws, ws[1:]))
        texts[half] = t
        (HERE / ('TEXT-%s.txt' % half)).write_text(t, encoding='utf-8')
        meta = dict(PAGES[half])
        (HERE / ('RESULT-%s.json' % half)).write_text(json.dumps(dict(meta, windows=ws, text=t), ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        ai = [dict(i=k, confidence=w['confidence'], words=w['words'], start=w['start'], end=w['end'], text=t[w['start']:w['end']].strip())
              for k, w in enumerate(ws) if w['label'] != 'Human']
        res[half] = dict(link=meta['link'], created_at=meta['created_at'], version=meta['version'], headline=meta['headline'],
                         fraction_ai=meta['fraction_ai'], num_ai_segments=meta['num_ai_segments'], n_windows=meta['n_windows'],
                         word_count=meta['word_count'], document_confidence=meta['document_confidence'], ai_windows=ai, items={})
    for key, it in items.items():
        if it['scope'] == 'stretch':
            continue
        half = it['half']
        t = texts[half]
        a, b = span((SUB / 'items' / (key + '.txt')).read_text(encoding='utf-8'), t)
        hit = [w for w in res[half]['ai_windows'] if w['start'] < b and w['end'] > a]
        words = len(t[a:b].split())
        res[half]['items'][key] = {'ai_words': sum(w['words'] for w in hit), 'words': words, 'windows': [w['i'] for w in hit],
                                   'prediction': it['prediction'].split(':')[0]}
    (HERE / 'ROUND6-RESULTS.json').write_text(json.dumps(dict(round=6, turn=108, how=__doc__.split('\n\n')[1].replace('\n', ' '), **res),
                                                          ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for half in 'AB':
        r = res[half]
        print(half, r['headline'], '%.2f%% AI' % (100 * r['fraction_ai']), len(r['ai_windows']), 'AI windows of', r['n_windows'])
        for w in r['ai_windows']:
            print('   ', w['i'], w['confidence'], w['words'], '|', w['text'][:110])
        for k, v in r['items'].items():
            print('   %-18s %3d of %4d words in AI windows %s' % (k, v['ai_words'], v['words'], v['windows'] or ''))
    if '--ledger' in sys.argv:
        for key, it in items.items():
            half = it['half']
            if it['scope'] == 'stretch':
                r = res[half]
                verdict = 'Human' if r['fraction_ai'] == 0 else 'Mixed'
                head = '%s, %.2f%% AI, %d AI window%s of %d' % (r['headline'], 100 * r['fraction_ai'], len(r['ai_windows']),
                                                               '' if len(r['ai_windows']) == 1 else 's', r['n_windows'])
                frac, words = r['fraction_ai'], r['word_count']
            else:
                v = res[half]['items'][key]
                verdict = 'Human' if v['ai_words'] == 0 else 'Mixed'
                head = '%s inside the half check: %d of %d words in AI windows' % (verdict, v['ai_words'], v['words'])
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
