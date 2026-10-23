"""Joel's own Appendix C (his message of 2026-10-23 01:10 UTC, question 13): EDITS-joel-0110.json, one 4.1 edit that
replaces Appendix C's prose (batch 469g's, from "Use this checklist" to the bad guide) by his five paragraphs.

Question 13 asked whether he would write Appendix C's opening (two short paragraphs) and the bad guide's last sentence in
his own words, since the opening had read AI in six versions. He sent five paragraphs: the opening ("13 human high conf
learn some lessons:", then two paragraphs), and after "also it seems like you duplicated this in your check" (the second
screening post repeated the middle and the end in both new openings' samples) three more: the signs, what to do, and the
good and bad guide, its last sentence among them. They go in as he typed them, his whole Appendix C prose, with one obvious
typo fixed ("accomodate"); his "etc)" stays, as he writes it in fifteen other places in the guide.

  python3 articles/inner-signal/humanize/fix-20261023/make_joel_0110.py   (from the repo root)
  then: python3 articles/inner-signal/humanize/fix-20261020/apply_edits41.py --add articles/inner-signal/humanize/fix-20261023/EDITS-joel-0110.json
"""
import json, pathlib

D = pathlib.Path(__file__).resolve().parent
H = D.parent
START = 'Use this checklist when something is pressing on you too hard'
END = 'or proof that you need more of their guidance.'
TYPOS = [('accomodate', 'accommodate')]


def his_paragraphs():
    msg = (D / 'joel-20261023-0110-message.txt').read_text(encoding='utf-8')
    head, tail = msg.split('13 human high conf learn some lessons:\n', 1)
    opening, rest = tail.split('\n---\n', 1)
    rest = rest.split('also it seems like you duplicated this in your check\n', 1)[1]
    paras = [p.strip() for p in (opening + '\n\n' + rest).split('\n\n') if p.strip()]
    assert len(paras) == 5, paras
    out = []
    for p in paras:
        for a, b in TYPOS:
            p = p.replace(a, b)
        out.append(p)
    return out


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    a = md.index(START)
    b = md.index(END, a) + len(END)
    old = md[a:b]
    assert md.count(old) == 1 and '\n#' not in old, 'the prose span must be inside Appendix C'
    assert md[b:].startswith('\n\n## Hypnosis-specific audit'), 'Appendix C\'s prose must end before its audit'
    new = '\n\n'.join(his_paragraphs())
    edit = {
        'key': 'HG32-joel-0110',
        'section': 'HG32',
        'source': ('Joel\'s own words (his message of 2026-10-23 01:10 UTC, question 13: A; '
                   'fix-20261023/joel-20261023-0110-message.txt), his whole Appendix C prose: the opening he checked '
                   '("13 human high conf", no link given) and the signs, what to do and the good and bad guide; one typo '
                   'fixed ("accomodate")'),
        'batch': 'joel-20261023-0110',
        'old': old,
        'new': new,
        'paragraph_check': None,
        'paragraph_result': 'Human, high confidence: Joel\'s own check of his opening (his words, "13 human high conf"); '
                            'the five paragraphs in place are read in recheck B',
        'section_check': None,
        'section_result': None,
    }
    (D / 'EDITS-joel-0110.json').write_text(json.dumps([edit], ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('EDITS-joel-0110.json: Appendix C\'s prose, %d words -> his %d words (%d paragraphs)'
          % (len(old.split()), len(new.split()), len(new.split('\n\n'))))


if __name__ == '__main__':
    main()
