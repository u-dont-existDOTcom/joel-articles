"""The appendix, draft v4 (2026-10-17): v3 with a break in the two runs whose march (review-r2) still had none in a reading.
- Rubin, Willis and Ludwig with Kanter (T10, "S S S" in both readings): the paper's question as the reader's own question,
  then the paper named ("Is longevity alone a meaningful measure ...? That's the question in ..."); the same question.
- The research paragraph (T12, "S S S" in reading a, "S S B" in b; both readings had a break in v2's march): "Can you
  imagine?" after the ledger, a question that claims nothing.
Writes v4.md and v4-breaks.json. Run from this folder: python3 make_v4.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
t = (HERE / 'v3.md').read_text(encoding='utf-8')
R = ('https://www.researchgate.net/publication/334857266_Measuring_Success_in_Intentional_Communities_A_Critical_Evaluation_'
     'of_Commitment_and_Longevity_Theories')
FIX = [
 ("[“Measuring Success in Intentional Communities”](%s) by Rubin, Willis and Ludwig is a paper with this question: is longevity "
  "alone a meaningful measure, when a community may keep going without its members flourishing?" % R,
  "Is longevity alone a meaningful measure, when a community may keep going without its members flourishing? That's the "
  "question in [“Measuring Success in Intentional Communities”](%s), a paper by Rubin, Willis and Ludwig." % R,
  'the paper\'s question asked of the reader first (march T10 had no break); the same question'),
 ("and this article doesn't have to turn into a 200-row ledger!",
  "and this article doesn't have to turn into a 200-row ledger. Can you imagine?",
  'a question that claims nothing after the published ledger (march T12, reading a, had no break)'),
]
log = []
for old, new, why in FIX:
    assert t.count(old) == 1, old[:60]
    t = t.replace(old, new)
    log.append({'old': old, 'new': new, 'why': why})
(HERE / 'v4.md').write_text(t, encoding='utf-8')
(HERE / 'v4-breaks.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v4.md,', len(log), 'changes')
