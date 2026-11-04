"""His version of the uridine section's "Who this is for" paragraph (block 81), into the article.

His message of 2026-11-04 10:01 UTC (../joel-20261104-1001-message.txt) took my round-2 version of it and gave his: "fixed
it, just clarified and uncompressed". It goes in as he wrote it, after the typographic swap (E337 (gut): the curly marks
he kept from my text become straight; his own straight ones stay), with the post's link kept on "dopamine agonist
withdrawal syndrome". The heading above it is unchanged.

His version leaves out "especially a history of dopamine agonist withdrawal from drugs like pramipexole or ropinirole",
the only place the article names those two drugs, and the closer of mine he cut. A compound his version drops goes back
to him as a question, never put back over his words: FIDELITY-KEYS.json holds the two names open ("owner_open") with
question 3 on OWNER-QUESTIONS.md. His "isn't for" stands for the post's "not for" in W030 ("owner_wording").

  python3 articles/neuro-de-armoring/humanize/fix-20261104/b081/apply_b081.py [--check]
Writes HUMANIZED-SO-FAR.md, APPLIED-B081.json and read/READ-RECORD.json.
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(ROOT / 'articles' / 'inner-signal' / 'humanize' / 'fix-20261025' / 'review'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402
import typography_swap as ts  # noqa: E402
from apply_answers import set_block_text  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
BEFORE = '6cf2ad04dfa69221175161d37c149475680aefe66fbe0f186a05630dda58f0f3'
MESSAGE = HERE.parent / 'joel-20261104-1001-message.txt'
HIS = ("Who this is for: Uridine isn't for everyone with depression. It could be helpful, though, for folks that show a "
       "“burned-out dopamine receptor” pattern, where everything feels gray and there's no desire for anything (anhedonia). "
       "These folks also find that dreams and psychedelic visuals are weak, so they need unusually high doses to feel "
       "anything, and as a result they tend to compulsively reach for ketamine/LSD/novelty just to get a hit. In the medical "
       "literature, this burnout pattern is talked about with regard to dopamine agonist withdrawal syndrome (DAWS). People "
       "with DAWS, after tapering off dopamine agonist drugs, present with symptoms of anxiety, panic, dysphoria, depression, "
       "agitation, fatigue, autonomic symptoms, pain, and drug cravings. Scott’s case looked like DAWS with dopamine receptor "
       "D2/D3 reward-system downregulation, which then got worse from frequent LSD microdosing and from trying to force "
       "dopamine hits with ketamine.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    assert HIS in MESSAGE.read_text(encoding='utf-8'), 'his version is not word for word in his message'
    md = ARTICLE.read_text(encoding='utf-8')
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == BEFORE, 'the article changed'
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    (i,) = [b['i'] for b in bl if b['text'].startswith('Who this is for: This is not for everyone with depression.')]
    assert bl[i - 1]['text'] == 'Dopamine Receptor Burnout / DAWS Pattern: Uridine Monophosphate'
    new, n = ts.swap_text(HIS)
    lost = []
    raw[i] = set_block_text(raw[i], new, lost)
    assert not lost, lost
    assert '[dopamine agonist withdrawal syndrome](https://pubmed.ncbi.nlm.nih.gov/23686524/)' in raw[i], raw[i]
    out = '\n\n'.join(raw) + '\n'
    after = hashlib.sha256(out.encode('utf-8')).hexdigest()
    nb = sr.blocks(out)
    assert len(nb) == len(bl) and nb[i]['text'] == new
    rec = {'about': 'his version of block 81 (the uridine section, "Who this is for"), from his message of 2026-11-04 10:01 UTC',
           'before_sha256': BEFORE, 'after_sha256': after, 'block': i, 'where': sr.where(bl, i),
           'before': bl[i]['text'], 'his_version': HIS, 'after': new, 'marks_swapped': n,
           'his_comment': 'fixed it, just clarified and uncompressed',
           'left_out': ['especially a history of dopamine agonist withdrawal from drugs like pramipexole or ropinirole '
                        '(question 3)', 'my closer: "That\'s a pretty specific phenotype, and I\'m not saying everyone '
                        'needs dopamine." (the post\'s "That is a specific phenotype, not a generic “everyone needs dopamine” '
                        'claim.")']}
    print(json.dumps(rec, ensure_ascii=False, indent=1))
    if a.check:
        return
    ARTICLE.write_text(out, encoding='utf-8')
    (HERE / 'APPLIED-B081.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    d = HERE / 'read'
    d.mkdir(parents=True, exist_ok=True)
    cr.record(d, findings=[], coverage=[cr.phash(new)], dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: his version of block 81, read in place beside the paragraph it replaces by '
                      'the lead session (E284, E331): his words, the typographic swap only' % after[:8])


if __name__ == '__main__':
    main()
