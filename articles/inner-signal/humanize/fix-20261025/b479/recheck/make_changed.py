"""CHANGED-A.json and CHANGED-B.json for batch 479's recheck (part_forecast.py make): each candidate of ../CANDIDATES.json
as it reads in the new checked text (TEXT-A.txt, TEXT-B.txt), with my chance that it reads red and why, plus part B's
hypnosis audit questions, unchanged and kept by his answer 2c, red in both checks before. The last check for both parts is
the recheck read after Joel's message of 2026-10-25 23:50 UTC (../../recheck/RESULT-A.json and RESULT-B.json);
part_forecast.py adds each changed paragraph's neighbours and the last check's light green windows itself.

  python3 articles/inner-signal/humanize/fix-20261025/b479/recheck/make_changed.py
"""
import json
import pathlib

X = pathlib.Path(__file__).resolve().parent
B = X.parent
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})

# spot: (chance red, why); written before the paste, after the API checks of the High spots (../PREDICTIONS.md)
CHANCES = json.loads((X / 'CHANCES.json').read_text(encoding='utf-8'))
AUDIT = 'Was I plainly told that induction mechanics are being used?'


def locate(text, para):
    """The candidate paragraph as the check reads it: the post curls straight quotes, so match with quotes made flat."""
    flat_t, flat_p = text.translate(FLAT), para.translate(FLAT)
    k = flat_t.find(flat_p)
    assert k >= 0 and flat_t.count(flat_p) == 1, para[:60]
    return text[k:k + len(para)]


def main():
    cands = json.loads((B / 'CANDIDATES.json').read_text(encoding='utf-8'))['spots']
    for part in ('A', 'B'):
        text = (X / ('TEXT-%s.txt' % part)).read_text(encoding='utf-8')
        out = []
        for k, c in cands.items():
            if c['part'] != part:
                continue
            chance, why = CHANCES[k]
            out.append({'name': '%s %s' % (k, c['card']), 'text': locate(text, c['paragraph_after']), 'chance_red': chance,
                        'why': why})
        if part == 'B':
            k = text.index(AUDIT)
            a = text.rindex('\n', 0, k) + 1
            out.append({'name': 'the hypnosis audit (kept, 2c)', 'text': text[a:text.index('\n', k)], 'chance_red': 0.95,
                        'why': 'unchanged; his answer 2c keeps it a list; read AI, High, in recheck B2 and in the last check'})
        (X / ('CHANGED-%s.json' % part)).write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(part, [(x['name'], x['chance_red']) for x in out])


if __name__ == '__main__':
    main()
