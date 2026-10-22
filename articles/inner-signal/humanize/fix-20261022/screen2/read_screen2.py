"""The second screening post's result (2026-10-22), sample by sample, and each sample's result in the ledger.

Before this: the windows read from Joel's result page in the app's browser (tools/humanization/pangram_feed_read.js, its
compact line saved as WINDOWS-S2.txt and the rest as META-S2.json), then
  python3 tools/humanization/substack_check_text.py result fix-20261022/screen2/PAYLOAD-S2.html WINDOWS-S2.txt META-S2.json --out RESULT-S2.json
which rebuilds the checked text and checks it against the page's SHA-256 (it must be TEXT-S2.txt's, b1bf8832...).

Each window belongs to every sample its span touches (SPANS-S2.json), as in the first screening (../screen/). A sample's
verdict: Human when none of its windows is AI, AI when all are, Mixed otherwise; its AI fraction is its AI windows' words
over its windows' words.

  python3 articles/inner-signal/humanize/fix-20261022/screen2/read_screen2.py [--ledger]   (from the repo root)
Writes SCREEN2-RESULT.json; with --ledger, adds each sample's result to the lane's ledger (keys screen2-B0 to screen2-C2).
"""
import json, pathlib, subprocess, sys

S = pathlib.Path(__file__).resolve().parent
REPO = S.parents[4]
LEDGER = S.parents[1] / 'pangram-ledger.jsonl'
DETECTOR = "pangram 4.1, Pangram's check of the Substack draft (free, Joel's account)"
TEXT_SHA = 'b1bf88324455624805f1123f331b4a17119d3a1a03dd56e2a2163c45b00507b3'


def main():
    res = json.loads((S / 'RESULT-S2.json').read_text(encoding='utf-8'))
    assert res.get('text_sha256') == TEXT_SHA, 'the checked text is not TEXT-S2.txt'
    ws = res['windows']
    if isinstance(ws, str):
        import ast
        ws = ast.literal_eval(ws)
    spans = json.loads((S / 'SPANS-S2.json').read_text(encoding='utf-8'))
    out = {}
    for label, sp in spans.items():
        mine = [(i + 1, w) for i, w in enumerate(ws) if w['end_index'] > sp['start'] and w['start_index'] < sp['end']]
        ai = [(i, w) for i, w in mine if w['label'] != 'Human']
        words = sum(w['word_count'] for _, w in mine) or 1
        aiw = sum(w['word_count'] for _, w in ai)
        verdict = 'Human' if not ai else ('AI' if len(ai) == len(mine) else 'Mixed')
        out[label] = {'what': sp['what'], 'verdict': verdict, 'windows': [i for i, _ in mine], 'ai_windows': [i for i, _ in ai],
                      'ai_words': aiw, 'words': sp['words'], 'ai_fraction': round(aiw / words, 4),
                      'light_windows': sum(1 for _, w in mine if w['label'] == 'Human' and w['confidence'] != 'High'),
                      'humanized': sum(1 for _, w in mine if w.get('is_humanized'))}
    (S / 'SCREEN2-RESULT.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for k, v in out.items():
        print(k, v['verdict'], 'windows %d, AI %d (%s), light %d' % (len(v['windows']), len(v['ai_windows']),
                                                                       v['ai_windows'], v['light_windows']), v['what'])
    if '--ledger' in sys.argv:
        for k, v in out.items():
            r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_ledger.py'), 'result', str(LEDGER),
                                '--key', 'screen2-' + k, '--verdict', v['verdict'], '--link', res['link'],
                                '--headline', '%s (the whole post); this sample\'s span: %s' % (res['headline'], v['verdict']),
                                '--ai-fraction', str(v['ai_fraction']), '--detector', DETECTOR],
                               capture_output=True, text=True, cwd=REPO)
            print(k, (r.stdout or r.stderr).strip()[-300:])


if __name__ == '__main__':
    main()
