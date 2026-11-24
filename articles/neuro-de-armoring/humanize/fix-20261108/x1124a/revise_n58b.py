#!/usr/bin/env python3
"""58, fitted again after three fresh reads of the first fit (needed/n58, his-fixes/n58, fit/n58, 2026-11-24): every
point of his answer stays, and what the readers couldn't tell or misread is said: which amount is the standard dose and
what it holds, the reason for this form beside the choice, why copper goes with zinc and that its amount is a day's,
"a day" for L-serine, and the stomach limit before the trials' 30 g, which read as permission to go there. The leaky-gut
point and the trials' 30 g are his points, kept though the needed read called them extras.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1124a/revise_n58b.py [--write]
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import apply_x1124a as A  # noqa: E402

N58B = ("For the zinc, I'd use zinc carnosine, since it's better tolerated than other forms of zinc and also helps repair "
        "leaky gut ([Mahmood, et al, 2007](https://pmc.ncbi.nlm.nih.gov/articles/PMC1856764)). A standard dose is up to "
        "75 mg a day, which holds 16 mg of elemental zinc, and if it causes nausea, take less at a time. Zinc can lower "
        "your copper over time, so I'd also take 1–2 mg of elemental copper a day, as copper gluconate or citrate (not "
        "cupric oxide, which is poorly absorbed). For L-serine, I'd do 5–15 g a day, depending how it feels. Higher "
        "doses bring more GI distress, though up to 30 g a day has been used in trials for neurodegenerative conditions "
        "([Levine, et al, 2017](https://doi.org/10.1080/21678421.2016.1221971)).")


def main(write):
    text = A.ARTICLE.read_text(encoding='utf-8')
    if N58B in text:
        print('already in')
        return
    assert text.count(A.NOTE_58) == 1
    out = text.replace(A.NOTE_58, N58B, 1)
    rec_path = HERE / 'APPLIED-X1124A.json'
    rec = json.loads(rec_path.read_text(encoding='utf-8'))
    rec['revised_58'] = {'by': 'revise_n58b.py', 'reads': ['needed/n58/READ.md', 'his-fixes/n58/READ.md',
                                                          'fit/n58/READ.md'],
                         'old': A.NOTE_58, 'new': N58B,
                         'added': ['the reason for this form beside the choice (his "better tolerated", moved up)',
                                   '"which holds 16 mg of elemental zinc": what the 75 mg holds',
                                   'why copper: zinc can lower copper over time; "a day" for its amount; cupric oxide '
                                   '"poorly absorbed" as the reason to avoid it',
                                   '"a day" for L-serine and its trials\' 30 g',
                                   'the stomach limit said before the 30 g, which read as permission']}
    rec['after_sha256'] = hashlib.sha256(out.encode('utf-8')).hexdigest()
    print('after', rec['after_sha256'][:8])
    if write:
        A.ARTICLE.write_text(out, encoding='utf-8')
        rec_path.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main('--write' in sys.argv)
