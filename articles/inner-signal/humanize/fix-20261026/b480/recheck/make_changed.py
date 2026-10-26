"""CHANGED-A.json and CHANGED-B.json for batch 480's recheck (part_forecast.py make): each candidate of ../CANDIDATES.json
(its new words only, so the rest of its paragraph is a neighbour of its own) as it reads in the new checked text
(TEXT-A.txt, TEXT-B.txt), with my chance that it reads red and why, written before the paste (CHANCES.json); two unchanged
stretches with chances of their own (the guard prompt after S8, red in place last time; the parent script paragraph's
last two sentences, red alone in 480g); and part B's hypnosis audit, unchanged and kept by his answer 2c, as one part from its lead-in to its last line. The
last check for both parts is batch 479's recheck (../../../fix-20261025/b479/recheck/RESULT-A.json and RESULT-B.json);
part_forecast.py adds each part's neighbours and the last check's light green windows itself.

  python3 articles/inner-signal/humanize/fix-20261026/b480/recheck/make_changed.py
"""
import json
import pathlib

X = pathlib.Path(__file__).resolve().parent
B = X.parent
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})
CHANCES = json.loads((X / 'CHANCES.json').read_text(encoding='utf-8'))
AUDIT_FIRST, AUDIT_LAST = 'Before accepting a recording or live suggestion, ask:', 'change the method, or leave.'
EXTRA = {'A': [('guard prompt', '(To the guard, in the same Nurturer voice you meant for your inner child:', 'by…..?”)'),
               ('parent script tail', 'Often this script acts as a critic or warden', 'what you’re doing is “fake”.')]}


def locate(text, para):
    """The words as the check reads them: the post curls straight quotes, so match with quotes made flat."""
    flat_t, flat_p = text.translate(FLAT), para.translate(FLAT)
    k = flat_t.find(flat_p)
    assert k >= 0 and flat_t.count(flat_p) == 1, para[:60]
    return text[k:k + len(para)]


def between(text, first, last):
    flat_t = text.translate(FLAT)
    a = flat_t.find(first.translate(FLAT))
    b = flat_t.find(last.translate(FLAT), a)
    assert a >= 0 and b > a and flat_t.count(first.translate(FLAT)) == 1, first
    return text[a:b + len(last)]


def main():
    cands = json.loads((B / 'CANDIDATES.json').read_text(encoding='utf-8'))['spots']
    for part in ('A', 'B'):
        text = (X / ('TEXT-%s.txt' % part)).read_text(encoding='utf-8')
        out = []
        for k, c in cands.items():
            if c['part'] != part:
                continue
            chance, why = CHANCES[k]
            out.append({'name': '%s %s' % (k, c['card'] or 'parent script'), 'text': locate(text, c['new']), 'chance_red': chance, 'why': why})
        for name, first, last in EXTRA.get(part, []):
            chance, why = CHANCES[name]
            out.append({'name': name + ' (unchanged)', 'text': between(text, first, last), 'chance_red': chance, 'why': why,
                        'kind': 'neighbour'})
        if part == 'B':
            # the whole audit block, its lead-in and its last line too: batch 479's forecast gave those two neighbour chances
            # (0.05) and both read red with the questions, in one High window of 120 words (SCORE-B.md there)
            out.append({'name': 'the hypnosis audit (kept, 2c)', 'text': between(text, AUDIT_FIRST, AUDIT_LAST), 'chance_red': 0.95,
                        'why': 'unchanged; his answer 2c keeps it a list; read AI, High, in each check since recheck B2, lead-in to last line'})
        (X / ('CHANGED-%s.json' % part)).write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(part, [(x['name'], x['chance_red'], len(x['text'])) for x in out])


if __name__ == '__main__':
    main()
