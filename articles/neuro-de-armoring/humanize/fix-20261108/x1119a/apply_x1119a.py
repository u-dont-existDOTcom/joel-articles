"""Put his answers of 2026-11-19 16:17 UTC into HUMANIZED-SO-FAR.md (his message: ../joel-20261119-1617-message.txt).

- 12a: block 48's last sentence split at his first "although", nothing else changed: "..., although we can see" becomes
  "... . But we can see", the text question 12 showed him.
- 13b: his clause on children stays as he wrote it; no change.
- 14: his version of block 54 (SC-54), the second paragraph of his message, goes in as his. He checked it himself: Human
  Written, every window High (HIS-CHECKS-READ-20261119.json; the SHA-256 of the text he checked is his paragraph's). His
  versions don't go through the apply gate. The links go back on its citations, and on "one man's Alzheimer's improved
  markedly" (the LongeCity thread, as on the card he approved); the script checks that the result, read as plain text, is
  his paragraph word for word.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1119a/apply_x1119a.py [--write]

Each change goes in once: a change already in the article is skipped.
"""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parent
H = FIX.parent
sys.path.insert(0, str(FIX / 'x1113b'))
import texts_x1113b as T  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
MESSAGE = FIX / 'joel-20261119-1617-message.txt'
CHECKS = HERE / 'HIS-CHECKS-READ-20261119.json'
YOUSSEF = '([Youssef, et al, 2022](https://pubmed.ncbi.nlm.nih.gov/36282607/))'
OLD48 = YOUSSEF + ', although we can see'
NEW48 = YOUSSEF + '. But we can see'
Q12 = ('No controlled trial of the diet has been done yet, and the one placebo-controlled trial of BHB supplements alone was '
       'too small to tell either way (Youssef, et al, 2022). But we can see some astounding BHB salt reviews on forums, like '
       'for brain injury repair, and BHB injections work for rats with trauma, although in humans it\'s still an open '
       'question whether the salts work as well as the keto diet (Engelhardt, et al, 2026).')


def his54():
    text = MESSAGE.read_text(encoding='utf-8')
    paras = [p.strip() for p in text.split('\n\n') if p.strip()]
    assert len(paras) == 2 and paras[1].startswith('The Fix: If your brain'), [p[:40] for p in paras]
    mine = paras[1]
    (chk,) = json.loads(CHECKS.read_text(encoding='utf-8'))['results'].values()
    assert hashlib.sha256(mine.encode('utf-8')).hexdigest() == chk['sha'], 'not the text he checked'
    old = T.OLD54
    cunnane = re.search(r'\(\[Cunnane, et al, 2016\]\((\S+?)\)\)', old).group(1)
    chow = re.search(r'\(\[Chowanadisai, et al, 2010\]\((\S+?)\)\)', old).group(1)
    md = mine
    for cite, url in [('Cunnane, et al, 2016', cunnane), ('Newport, et al, 2015', T.NEWPORT),
                      ('VanItallie, et al, 2005', T.VANITALLIE), ('Phillips, et al, 2018', T.PHILLIPS),
                      ('Chowanadisai, et al, 2010', chow)]:
        md = T.swap(md, '(%s)' % cite, '([%s](%s))' % (cite, url))
    md = T.swap(md, "one man's Alzheimer's improved markedly", "[one man's Alzheimer's improved markedly](%s)" % T.LONGECITY)
    assert T.plain(md) == mine
    return md, mine


def main(write=False):
    md = ARTICLE.read_text(encoding='utf-8')
    before = hashlib.sha256(md.encode('utf-8')).hexdigest()
    lines = md.split('\n')
    applied = []
    # 12a: block 48
    (i,) = [k for k, l in enumerate(lines) if YOUSSEF in l]
    if OLD48 in lines[i]:
        new = T.swap(lines[i], OLD48, NEW48)
        assert T.plain(new).endswith(Q12)
        applied.append({'answer': '12a', 'block': 48, 'line': i + 1, 'old': lines[i], 'new': new,
                        'whose': 'his sentence, split at his first "although" as question 12 showed it (2026-11-14)'})
        lines[i] = new
    # 14: block 54
    new54, his = his54()
    if new54 not in lines:
        (j,) = [k for k, l in enumerate(lines) if l.startswith('The Fix: If the brain is burning less sugar')]
        assert lines[j] == T.OLD54
        applied.append({'answer': '14', 'card': 'SC-54', 'block': 54, 'line': j + 1, 'old': lines[j], 'new': new54,
                        'whose': 'his version (2026-11-19 16:17 UTC), as he checked it, with the links back',
                        'his_check': 'https://www.pangram.com/history/b9ba21e6-8d8b-4628-a151-66a39165dadb'})
        lines[j] = new54
    out = '\n'.join(lines)
    rec = {'about': 'his answers of 2026-11-19 16:17 UTC: 12a, 13b, 14', 'message': MESSAGE.name, 'applied': applied,
           'unchanged': ['13b: his clause on children stays as he wrote it (his note: he is not talking about IV use)'],
           'before_sha256': before, 'after_sha256': hashlib.sha256(out.encode('utf-8')).hexdigest()}
    print('before', before[:8], 'after', rec['after_sha256'][:8], [x['answer'] for x in applied])
    if write and applied:
        ARTICLE.write_text(out, encoding='utf-8')
        (HERE / 'APPLIED-X1119A.json').write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main('--write' in sys.argv)
