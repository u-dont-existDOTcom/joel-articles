"""The second and last check, by itself, of each section Joel's answers of 2 November changed, and a check of each of
his four paragraphs that has no try left as a section, with my predictions written before the run (gate E307, E315).

His answers (../APPLIED-S1101.json) changed 22 sections of batch s1101. Eighteen have their second section check left
(lineage HG1101-NN, try 2 of 2): each is cut at the same blocks as the first check (../../fix-20261101/sections/
SECTIONS.json), mapped to the guide as it is now (APPLIED-S1101.json's block_map), so the two results compare window by
window. Four (Let the child speak, Come all the way back, The weekly deeper practice, You become too blissful) used both
section tries on 1 November; what changed there is his own text, which he checked in Pangram before sending, so each of
those is checked again as he'll read it now (with the typos fixed and in its place's words), as a paragraph lineage of its
own (HG1102-<card>, try 1 of 6). Every check goes through the API with a public link (Joel, 2 November: "always give me
the links").

My chance of a 100% Human result per text starts from the first check and from his own check of the words that changed:
where nearly the whole text is his, checked by him and read Human (High), 0.8 to 0.85; where his checked text sits beside
paragraphs of ours or his that read Low or AI on 1 November, less.

  python3 articles/inner-signal/humanize/fix-20261102/recheck/make_recheck2.py [--ledger]
Writes TEXTS.json (name -> text, for pangram_api.py), SECTIONS-R1102.json and PREDICTIONS.md / .json; with --ledger,
adds each prediction to ../../pangram-ledger.jsonl.
"""
import argparse
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
F = HERE.parent
H = F.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

LEDGER = H / 'pangram-ledger.jsonl'
FIRST = H / 'fix-20261101' / 'sections'
BATCH = 'r1102'
DETECTOR = 'pangram 4.1, the API (Joel\'s key, run on his laptop; E218)'
L = 'https://www.pangram.com/history/'

# section: (chance, what the chance rests on)
CHANCE = {
    's1101-15': (0.75, 'Human Written on 1 November with one Human (Low) line, now his inner child guide\'s full line (W-92)'),
    's1101-18': (0.75, 'Human Written with one Human (Low) line, now the last sentence he approved (W-111)'),
    's1101-20': (0.6, 'AI Detected (0.17); our windows rewritten on 1 November, his inner child guide line back with the '
                      'sentence he approved (W-119)'),
    's1101-23': (0.5, 'AI Detected (0.23) with an AI (High) window across his and our words; ours rewritten, his inner '
                      'child guide lines back and G-23 approved'),
    's1101-27': (0.65, 'AI Detected (0.15); its first six paragraphs are now his text that read Human Written by itself '
                       '(14c44cec); the rest is ours, rewritten on 1 November'),
    's1101-37': (0.8, 'Human Written; only the name of the section it points to changed (W-270)'),
    's1101-39': (0.6, 'Mostly Human Written (0.045); the heading and first paragraph he approved (W-270, W-271, which he '
                      'says read Human (High) for him), his words for the prayer (W-274) and the wish (W-282)'),
    's1101-40': (0.7, 'AI Generated (1.0) on 1 November; now his rewrite of the whole section ("now it\'s human high '
                      'conf") and the script he approved (W-283, "read human with the last section")'),
    's1101-41': (0.7, 'AI Detected (0.26); its first paragraph is the version he approved and checked ("this did fix it '
                      'on pangram", W-289)'),
    's1101-51': (0.75, 'Human Written with two Human (Low) lines; the first paragraph is now his ("fixed in pangram", '
                       'W-358)'),
    's1101-69': (0.45, 'AI Detected (0.44) on 1040 words; Patterns 3 to 7 are now his text that read Human (High) by '
                       'itself, but Patterns 1, 2 and 8 to 10 are ours, rewritten on 1 November, and long'),
    's1101-71': (0.65, 'AI Detected (0.12); the first five paragraphs are now his text that read Human Written by itself '
                       '(a25e487f); the consent paragraphs after them are his, as before'),
    's1101-72': (0.85, 'AI Detected (0.24); the whole section is now his text that read Human Written (High) by itself '
                       '(222e4bec), one typo fixed'),
    's1101-73': (0.7, 'Human Written with two Human (Low) lines; his wording of the first paragraph ("sounds better to '
                      'me"), not checked by him in this form'),
    's1101-74': (0.85, 'AI Generated (1.0) on 1 November; now his text that read Human Written (High) by itself '
                       '(c341e75a), one typo fixed'),
    's1101-84': (0.85, 'Mostly Human Written (0.06); the whole section is now his text that read Human Written (High) by '
                       'itself (0ace8ab7)'),
    's1101-85': (0.75, 'Human Written with one Human (Low) line; his last line ("now it\'s high conf", W-687)'),
    's1101-99': (0.45, 'AI Detected (0.18); Resource embodiment is ours, rewritten on 1 November, and his No-trance '
                       'inner contact read Human (High) by itself (2a567edc) without the heading\'s "9.", which read AI '
                       '(Low) by itself in his first check and is back with the other practices\' numbers'),
}
# his paragraphs whose sections have no try left: (card, old blocks, scope, chance, why, his check)
PARAS = [
    ('E-107', [104, 105, 106, 107], 'pair', 0.85, 'his text (3cd6c871, Human Written, High) with three typos fixed: '
     '"access to", "to be as free", a double space', '3cd6c871-fffc-4f28-99bd-c3bcd828c4f1'),
    ('E-315', [315, 316], 'pair', 0.85, 'his text (4dea2bac, Human Written, High) with one word added ("wake you up")',
     '4dea2bac-7ab8-496d-84a0-2e5ff003de09'),
    ('E-368', [368, 369], 'pair', 0.85, 'his text ("high conf human on first try", no link sent)', None),
    ('E-406', [405, 406], 'paragraph', 0.85, 'his text (ff307b0a, Human Written, High) with "is" taken out of '
     '"this lofty love is asking" and the closing quote mark matched', 'ff307b0a-ff97-476c-be72-68ceef371b0e'),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ledger', action='store_true')
    a = ap.parse_args()
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    bl = sr.blocks(md)
    app = json.loads((F / 'APPLIED-S1101.json').read_text(encoding='utf-8'))
    assert app['after_sha256'] == hashlib.sha256(md.encode('utf-8')).hexdigest(), 'the guide changed since the answers'
    bm = {int(k): v for k, v in app['block_map'].items()}
    first = {s['key']: s for s in json.loads((FIRST / 'SECTIONS.json').read_text(encoding='utf-8'))['sections']}
    res = json.loads((FIRST / 'RESULTS.json').read_text(encoding='utf-8'))
    changed = set(app['changed_blocks'])
    touched = sorted(k for k, s in first.items() if changed & set(s['blocks']))
    capped = [k for k in touched if k not in CHANCE]
    assert capped == ['s1101-17', 's1101-44', 's1101-53', 's1101-59'], capped
    texts, secs, rows = {}, [], []

    def add(key, lineage, scope, blocks_new, name, chance, why, first_result, his):
        text = '\n\n'.join(bl[i]['text'] for i in blocks_new)
        texts[key] = text
        secs.append({'key': key, 'name': name, 'blocks': blocks_new, 'words': len(text.split()),
                     'sha256': hashlib.sha256(text.encode('utf-8')).hexdigest(), 'text': text})
        rows.append({'key': key, 'lineage': lineage, 'scope': scope, 'name': name, 'words': len(text.split()),
                     'call': 'Human' if chance >= 0.5 else 'AI', 'chance': chance, 'why': why,
                     'first_result': first_result, 'his_check': (L + his) if his else None})

    for k in touched:
        if k not in CHANCE:
            continue
        f = first[k]
        nb = [j for i in f['blocks'] for j in bm[i]]
        r1 = res[k]
        add('%s-%s' % (BATCH, k.split('-')[1]), 'HG1101-%s' % k.split('-')[1], 'section', nb, f['name'],
            *CHANCE[k], '%s (%.3f), %s' % (r1['headline'], r1['likelihood'], r1['link']), None)
    for card, old, scope, chance, why, his in PARAS:
        nb = [j for i in old for j in bm[i]]
        sec = next(k for k, s in first.items() if old[-1] in s['blocks'])
        r1 = res[sec]
        add('%s-%s' % (BATCH, card), 'HG1102-%s' % card, scope, nb, '%s (%s)' % (first[sec]['name'], card), chance, why,
            'its section %s: %s (%.3f), %s' % (sec, r1['headline'], r1['likelihood'], r1['link']), his)
    (HERE / 'TEXTS.json').write_text(json.dumps(texts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'SECTIONS-R1102.json').write_text(json.dumps({'guide_sha256': app['after_sha256'], 'sections': secs},
                                                         ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    out = ['# Batch r1102: the changed sections and his four paragraphs, checked by themselves (predictions, before '
           'the run)', '', 'Gates E307, E315. Chance = my chance of a 100% Human result. The Pangram column is filled '
           'after the run.', '', '| text | mine | chance | why | before | Pangram |', '|---|---|---|---|---|---|']
    for r in rows:
        out.append('| %s: %s (%d words) | %s | %.2f | %s | %s | |' % (
            r['key'], r['name'].replace('|', '/'), r['words'], r['call'], r['chance'], r['why'], r['first_result']))
    (HERE / 'PREDICTIONS.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    (HERE / 'PREDICTIONS.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(rows), 'texts,', sum(r['words'] for r in rows), 'words')
    if not a.ledger:
        return
    td = HERE / 'texts'
    td.mkdir(exist_ok=True)
    for s, r in zip(secs, rows):
        f = td / (s['key'] + '.txt')
        f.write_text(s['text'], encoding='utf-8')
        cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
               '--lineage', r['lineage'], '--scope', r['scope'], '--text', str(f), '--call', r['call'],
               '--chance', str(r['chance']), '--key', s['key'], '--batch', BATCH, '--detector', DETECTOR,
               '--tells', 'before: ' + r['first_result'].split(',')[0],
               '--human-tells', 'his own words, or ours rewritten and read beside his published version',
               '--diagnosis', r['why'],
               '--decides', 'whether this text reads Human by itself after his answers of 2 November (E307, E315)'
                            + ('' if r['scope'] != 'section' else ': try 2 of 2')]
        p = subprocess.run(cmd, capture_output=True, text=True)
        if p.returncode:
            sys.exit('%s: %s%s' % (s['key'], p.stdout, p.stderr))
    print('ledger: %d predictions added' % len(rows))


if __name__ == '__main__':
    main()
