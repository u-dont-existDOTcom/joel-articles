"""Joel's comment on question 20 (EM-Q1, 2026-10-25 23:00 UTC): "make sure we are not using "protector" to mean "guard",
i saw that in finish without forcing, p2". In his reparenting guide the Protector is one of the inner adult's three jobs
(Nurturer, Protector, Guide), and the protective parts from childhood are the guards ("Hear the Guard First"; "Your
Protector earns that guard's trust"); that guide has no "protector part" at all. This guide still had 19 places where
"protector" names a guard. Each of the 42 uses of "protector" was read in its paragraph and sorted:
- CHANGES: a guard, so "guard" (or the appositive goes, where "a childhood protector part" only repeated "guard").
- KEPT_ROLE: the adult Protector.
- KEPT_GLOSS: "childhood protector parts" in brackets right after "guard"/"guards", explaining the word; his own revision
  of EM-Q1 kept two of these (Introduction P3, "Offer the care that is actually wanted" P1) while changing the bare uses
  around them ("force down guard parts", "a childhood guard part").

  python3 articles/inner-signal/humanize/fix-20261025/emulate-check/guard_sweep.py [--check]
Writes HUMANIZED-SO-FAR.md and GUARD-SWEEP.json.
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE.parent / 'review'))
import suggestion_review as sr  # noqa: E402
import apply_answers as AA  # noqa: E402

ARTICLE = ROOT / 'articles/inner-signal/humanize/HUMANIZED-SO-FAR.md'
OUT = HERE / 'GUARD-SWEEP.json'
# (where, old, new, why): each old occurs once in the paragraph that `where` names
CHANGES = [
    ('Introduction, P5', 'inner child mind, protector part minds, adult mind', 'inner child mind, guard minds, adult mind',
     'the minds of the guards: P3 two paragraphs up names them "guard mind (childhood protector parts ...)"'),
    ('Do you usually think in words?, P3', 'When it says "ask" the child or protector,', 'When it says "ask" the child or guard,',
     'the part that answers inside, not the grown-up job'),
    ('A useful map of the mind, P5', '(child parts, protectors, critic,', '(child parts, guards, critic,',
     'parts of the subconscious "ecology"'),
    ('Sometimes start with the whole, P5', 'Or is this a protector?', 'Or is this a guard?', 'telling the parts apart'),
    ('the heading "Working with childhood protector parts"', 'Working with childhood protector parts', 'Working with your guards',
     'the section is about the guards ("a very charming guard"); his published heading was "Working with protectors"'),
    ('Working with childhood protector parts, P3', 'a very charming guard, a childhood protector part. It', 'a very charming guard. It',
     'the appositive only repeated "guard" in the word for the adult job; the next sentence says what a guard is'),
    ('Working with childhood protector parts, P4', '(To the guard, the childhood protector part, in the same', '(To the guard, in the same',
     'the same appositive'),
    ('Working with childhood protector parts, P6', '(Now talk to the protector part.', '(Now talk to the guard.', 'the guard of the exercise'),
    ('Working with childhood protector parts, P7', 'Most of the time the protector part wants you', 'Most of the time the guard wants you',
     'the guard of the exercise'),
    ('Inner child reparenting, P1', 'just work with a protector or whatever you find.', 'just work with a guard or whatever you find.',
     'a part that comes in hypnosis instead of the child'),
    ('Don’t rush the repair, P4', 'Find a younger you/protector/feeling/signal', 'Find a younger you/guard/feeling/signal',
     'a part that comes up'),
    ('Non-dominant hand dialogue, P1', 'Tell your child/ protector part to write', 'Tell your child/ guard to write',
     'a part that writes with the other hand'),
    ('The actual inner meeting, P3', 'inner adult(s), protector(s) and all', 'inner adult(s), guard(s) and all',
     'the inner adult is named just before it; these are the parts'),
    ('The actual inner meeting, P7', 'be contacted by a child or protector,', 'be contacted by a child or guard,',
     'a part that makes contact'),
    ('Let the response change the invitation, P3', 'Neither is automatically a protector,', 'Neither is automatically a guard,',
     'a response that isn\'t automatically a guard'),
    ('Finish without forcing a revelation, P2', 'anything that a protector wanted you to know', 'anything that a guard wanted you to know',
     'the one he saw'),
    ('Using synchronicity as your own wake-up bell, P4', 'or from a childhood protector part,', 'or from a childhood guard part,',
     'his own words for it in EM-Q1: "a childhood guard part"'),
    ('Appendix D: Anxiety — body first, P2', 'comes from a childhood protector part of you.', 'comes from a childhood guard part of you.',
     'the same; the "parental Protector" in the next sentence is the grown-up job and stays'),
    ('Appendix F: Self-trust, outside guidance, and oracle-like states, P2', 'a line of communication with protectors, etc.',
     'a line of communication with guards, etc.', 'what doing it yourself gives you: direct contact with your own parts'),
]
KEPT_GLOSS = ['Introduction, P3', 'Offer the care that is actually wanted, P1', 'You get anxious, P3']


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    md = ARTICLE.read_text(encoding='utf-8')
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl)
    by_where = {sr.where(bl, b['i']): b['i'] for b in bl}
    new_text, rec, lost = {}, [], []
    for where, old, new, why in CHANGES:
        i = by_where[where]
        t = new_text.get(i, bl[i]['text'])
        assert t.count(old) == 1, (where, old)
        new_text[i] = t.replace(old, new)
        rec.append({'where': where, 'block': i, 'old': old, 'new': new, 'why': why})
    out = list(raw)
    for i, t in new_text.items():
        out[i] = AA.set_block_text(raw[i], t, lost)
    assert not lost, lost
    new_md = '\n\n'.join(out) + ('\n' if md.endswith('\n') else '')
    left = []
    for b in sr.blocks(new_md):
        for m in re.finditer(r'(?i)\bprotectors?\b|protector\(s\)', b['text']):
            ctx = b['text'][max(0, m.start() - 40):m.end() + 20]
            left.append({'where': sr.where(sr.blocks(new_md), b['i']), 'text': ctx,
                         'kept': 'gloss' if m.group(0).islower() else 'the grown-up job'})
    assert all(x['kept'] == 'the grown-up job' or x['where'] in KEPT_GLOSS for x in left), \
        [x for x in left if x['kept'] == 'gloss' and x['where'] not in KEPT_GLOSS]
    record = {'comment': 'make sure we are not using "protector" to mean "guard", i saw that in finish without forcing, p2',
              'before_sha256': hashlib.sha256(md.encode()).hexdigest(), 'after_sha256': hashlib.sha256(new_md.encode()).hexdigest(),
              'changed': rec, 'kept': left}
    print(len(rec), 'changed;', sum(x['kept'] == 'gloss' for x in left), 'glosses kept;',
          sum(x['kept'] != 'gloss' for x in left), 'uses of the Protector kept')
    if args.check:
        return
    OUT.write_text(json.dumps(record, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    ARTICLE.write_text(new_md, encoding='utf-8')
    print('wrote', ARTICLE.relative_to(ROOT), 'and', OUT.relative_to(ROOT))


if __name__ == '__main__':
    main()
