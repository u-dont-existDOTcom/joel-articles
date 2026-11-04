"""The 5-HTP interaction paragraph (his post's block 93, raw block 92 since the merge), fourth try, into the article: it read
Human Written, 0.0% AI, by itself in Pangram's web app (batch x1104s,
https://www.pangram.com/history/2be95f74-b2cf-45ec-a669-1807880af623), its windows High, Medium, Low, Medium and High (the Low
one is the case report's story, 65 words: work for later, E278).

The comparative read beside his post (E284, E294) is mine, sentence by sentence. "Don't mix 5-HTP casually with anything else
that raises serotonin, like antidepressants or MAOIs" is his "5-HTP should not be mixed casually with serotonin-raising drugs
or supplements", with the antidepressants and MAOIs of his next sentence named as the examples; "Most of the time serotonin
syndrome comes from an interaction like that, with a few different drugs or supplements stacked on top of each other" is his
"serotonin syndrome is most often a multi-drug / stack problem", the drugs and supplements kept, and MedlinePlus's page is his
"general serotonin-syndrome overview from MedlinePlus", linked where it was; "Case reports and reviews keep warning about the
risk with 5-HTP, like this case report" is his "Case literature and clinical reviews warn about serotonin syndrome risk when
5-HTP is combined with antidepressants or MAOIs. See the dietary supplement interaction case report", the same report linked;
"If you're doing psychedelics, avoid 5-HTP on your psychedelic days, and be especially strict around ayahuasca's harmala MAOI
chemistry and around iboga or ibogaine" is his "For this readership: avoid 5-HTP on psychedelic days, and be especially strict
around ayahuasca / harmala MAOI chemistry and iboga / ibogaine", the same review linked. The label "Hard interaction rule:" is
dropped, as his Y-90 and Y-91 dropped "Scott's version:" and "Trial:". No finding.

One addition of mine, which he sees in the turn's answer: what happened in the linked case report, read in full through
PubMed (Patel and Marzella 2017, PMC5580516, doi 10.12659/AJCR.904375): a 28-year-old man on sertraline took 5-HTP (Natrol
5-HTP) among many weight-loss and energy supplements on the day of a workout, and serotonin syndrome with rhabdomyolysis led
to acute compartment syndrome and fasciotomies of both lower legs and the right forearm; he recovered completely. The draft
says "a young guy", "a whole pile of weight-loss and energy supplements", "before a workout", "both of his legs and his
forearm" and "Luckily he recovered": nothing the report doesn't say.

  python3 articles/neuro-de-armoring/humanize/fix-20261104/next5/apply_b093.py [--check]
Writes HUMANIZED-SO-FAR.md, APPLIED-B093.json and read/READ-RECORD.json.
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
import compare_read as cr  # noqa: E402
import fidelity_keys as fk  # noqa: E402
import suggestion_review as sr  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
BEFORE = 'fb1168c8'
TESTED = 'https://www.pangram.com/history/2be95f74-b2cf-45ec-a669-1807880af623'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    md = ARTICLE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert sha.startswith(BEFORE), 'the article changed'
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    new = (HERE / 'blocks' / '093.md').read_text(encoding='utf-8').strip()
    tested = json.loads((HERE.parent / 'checks' / 'x1104s' / 'TEXTS.json').read_text(encoding='utf-8'))['b093']
    tested = tested if isinstance(tested, str) else tested['text']
    assert re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', new) == tested, 'not the text that was checked'
    (i,) = [k for k, b in enumerate(raw) if b.startswith('Hard interaction rule: 5-HTP should not be mixed casually')]
    old = raw[i]
    raw[i] = new
    out = '\n\n'.join(raw) + '\n'
    r = fk.check(json.loads((H / 'FIDELITY-KEYS.json').read_text(encoding='utf-8')), out)
    after = hashlib.sha256(out.encode('utf-8')).hexdigest()
    rec = {'about': 'his post\'s block 93, the 5-HTP interaction paragraph, fourth try: Human Written, 0.0% AI by itself in '
                    'the web app',
           'before_sha256': sha, 'after_sha256': after, 'block': i, 'before': old, 'after': new, 'tested': TESTED,
           'windows': ['Human, High, 16', 'Human, Medium, 34', 'Human, Low, 65', 'Human, Medium, 3', 'Human, High, 27'],
           'tries': ['https://www.pangram.com/history/5e797c26-95a2-4caa-aedb-6a88b723f6f5 (try 1, AI Generated, 100% AI)',
                     'https://www.pangram.com/history/cb693d91-b9c2-41cc-9a8e-20bd56779126 (try 2, AI Detected, 46.5% AI)',
                     'https://www.pangram.com/history/d2dffc85-efd5-42d0-af45-13a7c3917e05 (try 3, after the readers\' panel, '
                     'AI Detected, 24.3% AI)'],
           'addition': 'the linked case report said as what happened in it (PMC5580516, read in full through PubMed)',
           'fidelity_pass': r['pass']}
    print(json.dumps(rec, ensure_ascii=False, indent=1))
    assert r['pass'], r
    if a.check:
        return
    ARTICLE.write_text(out, encoding='utf-8')
    (HERE / 'APPLIED-B093.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    d = HERE / 'read'
    d.mkdir(exist_ok=True)
    cr.record(d, findings=[], coverage=[cr.phash(sr.blocks(out)[i]['text'])], dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: his post\'s block 93 (the 5-HTP interaction paragraph, fourth try) read '
                      'beside his post\'s by the lead session (E284, E294)' % after[:8])


if __name__ == '__main__':
    main()
