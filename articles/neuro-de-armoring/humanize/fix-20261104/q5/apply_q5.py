"""His answer 5a (2026-11-04 12:06 UTC, ../joel-20261104-1206-message.txt: "5a and if you can't figure it out i can help,
low windows can easily flip to AI in different segmentations, medium aren't a big issue usually"): two more tries each
for blocks 82 and 83, a try replacing the card's version only where it reads better.

- Block 82 (lineage ND1104-B082b): Codex's whole rewrite read 62.4% AI (../checks/x1104h); my second try changed only the
  sentence Pangram read Low, and read Human Written, 0.0% AI, with no Low window left (High, Medium, High;
  ../checks/x1104i): https://www.pangram.com/history/426bed99-5f7e-4c53-866c-6917c4c0c8cd. It goes in.
- Block 83 (lineage ND1104-B083b): both tries read worse (84.6% and 99.99% AI); the card's version (Codex's) stays, and its
  Low window goes to him on the cards page, as he offered.

The comparative read of the changed sentence beside his post's (E284, E294) is mine: "dietary UMP increased
potassium-evoked dopamine release and neurite outgrowth in aged rats" is "in old rats, UMP in their food meant their
neurons put out more dopamine when stimulated with potassium, and grew more nerve fibers": the same finding, the neurons
now the subject of both results, as in the study. No finding.

  python3 articles/neuro-de-armoring/humanize/fix-20261104/q5/apply_q5.py [--check]
Writes HUMANIZED-SO-FAR.md, APPLIED-Q5.json and read/READ-RECORD.json.
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
BEFORE = '46c8485f3c1f'
TESTED = 'https://www.pangram.com/history/426bed99-5f7e-4c53-866c-6917c4c0c8cd'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    md = ARTICLE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert sha.startswith(BEFORE), 'the article changed'
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    new = (HERE / '082-try2.md').read_text(encoding='utf-8').strip()
    tested = json.loads((HERE.parent / 'checks' / 'x1104i' / 'TEXTS.json').read_text(encoding='utf-8'))['b082']
    assert re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', new) == tested, 'not the text that was checked'
    (i,) = [k for k, b in enumerate(raw) if b.startswith('The tool: Uridine monophosphate (UMP). There\'s no study')]
    old = raw[i]
    raw[i] = new
    out = '\n\n'.join(raw) + '\n'
    r = fk.check(json.loads((H / 'FIDELITY-KEYS.json').read_text(encoding='utf-8')), out)
    after = hashlib.sha256(out.encode('utf-8')).hexdigest()
    rec = {'about': 'his answer 5a: block 82\'s second try (one sentence changed) replaces the card\'s version, reading better',
           'before_sha256': sha, 'after_sha256': after, 'block': i, 'before': old, 'after': new, 'tested': TESTED,
           'fidelity_pass': r['pass']}
    print(json.dumps(rec, ensure_ascii=False, indent=1))
    assert r['pass'], r
    if a.check:
        return
    ARTICLE.write_text(out, encoding='utf-8')
    (HERE / 'APPLIED-Q5.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    d = HERE / 'read'
    d.mkdir(exist_ok=True)
    cr.record(d, findings=[], coverage=[cr.phash(sr.blocks(out)[i]['text'])], dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: block 82 with its second 5a try, the changed sentence read beside his '
                      'post\'s by the lead session (E284, E294)' % after[:8])


if __name__ == '__main__':
    main()
