#!/usr/bin/env python3
"""Turn 113: GATE.md, the record of the owner-delivery gate's three rounds for the review sheet's new words, with its
tables computed from the folders (each review's verdict, and whether `deliver` admitted the item, from GATE-OUTCOMES.json).
Run after run_gate.py.

  python3 make_gate_md.py"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
B = ('https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/'
     'articles/inner-child-therapy/experiments/t113-gate/')
ROLES = ('preservation', 'cold_read_1', 'cold_read_2')
NAMES = json.loads((HERE / 'NAMES.json').read_text(encoding='utf-8'))
OUT = json.loads((HERE / 'GATE-OUTCOMES.json').read_text(encoding='utf-8'))
R1 = list(json.loads((HERE / 'GATE-INPUTS.json').read_text(encoding='utf-8')))
R2 = list(json.loads((HERE / 'GATE-INPUTS-R2.json').read_text(encoding='utf-8')))
R3 = list(json.loads((HERE / 'GATE-INPUTS-R3.json').read_text(encoding='utf-8')))


def verdicts(n):
    out = []
    for r in ROLES:
        p = HERE / n / ('REVIEW-%s.json' % r)
        out.append(json.loads(p.read_text(encoding='utf-8'))['verdict'] if p.exists() else 'not run')
    return out


def words(n):
    return (HERE / n / 'DRAFT.txt').read_text(encoding='utf-8')


def unresolved(n):
    out = []
    for r in ROLES:
        p = HERE / n / ('REVIEW-%s.json' % r)
        if p.exists():
            d = json.loads(p.read_text(encoding='utf-8'))
            if d['verdict'] == 'FAIL':
                out.append('%s: %s' % (r.replace('_', ' '), ' '.join(d['unresolved'])))
    return out


on_sheet = sorted(NAMES.values(), key=lambda n: list(NAMES.values()).index(n))
lines = ['# Turn 113: the review sheet\'s new words through the owner-delivery gate', '',
         'Every heading on the turn-113 review sheet whose words are new, and the one sentence with new words (his 109 A), went '
         'through [owner_delivery_gate.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/tools/humanization/owner_delivery_gate.py) '
         '(init, check, deliver) before the sheet shows it. That takes a fresh linter run (a FAIL is never waivable), the writer\'s '
         'verdict on all 33 rows of the tell inventory with a reason for each linter REVIEW finding '
         '([fill_ledgers.py](%sfill_ledgers.py)), and three separately saved reviews (preservation and two cold reads) by fresh '
         'Sonnet subagents, each with its own context id. The sheet\'s builder '
         '([build_review.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t113-review/build_review.py)) '
         'takes each one\'s text from its FOR-JOEL.txt and stops if one isn\'t there or doesn\'t match.' % B, '',
         '## What it covers, and what it doesn\'t', '',
         '- **Covered:** each heading whose words aren\'t the paragraph\'s own (a "new" heading in '
         '[proposals.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t113-shape/proposals.py)), '
         'as its exact words, with its section as it would read (CONTEXT.txt) and the paragraphs it stands over (SOURCE.txt); and '
         'the Solomon sentence.',
         '- **Not covered:** the headings made of a paragraph\'s own first words, the first words a heading now says (dropped), the '
         'splits and the one moved sentence. None adds a word: proposals.py checks that a lifted heading is the paragraph\'s own '
         'words, that a drop or a cut only takes words away, that a split only adds a break at a sentence boundary, and that the '
         'move adds or loses no word. The gate is for generated prose, "not owner-authored prose".', '',
         '## Three rounds', '',
         '- **Round 1** ([make_gate_files.py](%smake_gate_files.py), %d items, two halves per role). Four FAILs, each for a '
         'heading that didn\'t say what a skimming reader needs: "If your case is different", "Coming back confused or spaced out" '
         '(its change also didn\'t say it replaced his sentence), "If you might be vulnerable" and "If a part says no". "Feeling less '
         'safe" passed, but the cold read gave it his own words, so it left the gate. The cold read 2 reviewers of both halves ran '
         'out of output room, so cold read 2 for the round-1 items that stayed was done in round 2.' % (B, len(R1)),
         '- **Round 2** ([make_gate_files_r2.py](%smake_gate_files_r2.py)): the headings the round-1 reviewers asked for ("If '
         'you\'re doing it right and it still isn\'t working", "When to stop", "Coming back from trips confused or spaced out", "If '
         'you might be prone to mania or psychosis"), each heading whose section had changed around it, in a new folder, and cold '
         'read 2 for the rest. All PASS.' % B,
         '- **Round 3** ([make_gate_files_r3.py](%smake_gate_files_r3.py), %d items, the last): after the four section cold reads '
         '([COLD-READ.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t113-shape/COLD-READ.md)), '
         'every case heading became a #### and some headings were reworded or added. Each heading with new words in a section '
         'that changed got a new folder with its section as it reads now, the unchanged headings too.' % (B, len(R3)), '']
fails3 = [n for n in R3 if 'FAIL' in verdicts(n)]
if fails3:
    lines += ['A round-3 FAIL was not redrafted: its item fell back to the paragraph\'s own words. ' + ' '.join(
        '%s ("%s") failed (%s).' % (n, words(n), '; '.join(unresolved(n))) for n in fails3), '']
if 'start-stop-r3' in fails3:
    lines += ['Its fallback is his whole condition as the stop rule\'s heading, "If a part hesitates about being touched or about '
              'sex, or says no to going deeper in this work or to an altered state", and the paragraph starts "I\'d stop there and '
              'not test it, even when it sounds like a prediction." It has no new words, so it left the gate. It came after the '
              'round-3 reviews of the section\'s other new headings, so their CONTEXT.txt still shows "When to stop" in that place; '
              'nothing else in the section changed.', '']
lines += ['## The new words on the sheet', '',
          '| Section | Words | Folder | Preservation | Cold read 1 | Cold read 2 | The gate |', '|---|---|---|---|---|---|---|']
for key, n in NAMES.items():
    sid = key.split('|')[0]
    v = verdicts(n)
    o = OUT.get(n, {})
    adm = ('admitted ([the words](%s%s/FOR-JOEL.txt), [its proof](%s%s/FOR-JOEL.proof.json))' % (B, n, B, n)) if o.get('admitted') else 'BLOCKED'
    lines.append('| %s | "%s" | [%s](%s%s/ADMISSION.json) | %s | %s | %s | %s |' % (sid, words(n).replace('|', '\\|')[:90] + ('...' if len(words(n)) > 90 else ''),
                                                                     n, B, n, v[0], v[1], v[2], adm))
lines += ['', '## The record: earlier folders, not on the sheet', '',
          '| Folder | Words | Preservation | Cold read 1 | Cold read 2 | Why it isn\'t on the sheet |', '|---|---|---|---|---|---|']
used = set(NAMES.values())
for n in list(dict.fromkeys(R1 + R2 + R3)):
    if n in used:
        continue
    v = verdicts(n)
    base = n[:-3] if n[-3:] in ('-r2', '-r3') else n
    succ = {'therapist-ifs': 'therapist-licensed'}.get(n) or (base + '-r3' if (HERE / (base + '-r3')).is_dir() and n != base + '-r3' else None)
    if 'FAIL' in v:
        why = 'failed; the heading fell back to his own words' if n in fails3 else 'failed'
    elif n in ('hooks-less-safe', 'change-working'):
        why = 'the heading became his own words'
    elif succ and words(succ) != words(n):
        why = 'reworded after the cold reads (now %s)' % succ
    elif succ:
        why = 'its section changed; reviewed again as %s' % succ
    else:
        why = 'superseded'
    lines.append('| [%s](%s%s/ADMISSION.json) | "%s" | %s | %s | %s | %s |' % (n, B, n, words(n)[:90], v[0], v[1], v[2], why))
lines += ['', '## Provenance and the reviewers\' notes', '',
          '- Each reviewer was an Agent-tool subagent given only its brief (BRIEF-<role>-<batch>.md) and the folders\' files. This '
          'session\'s hooks also put the repository\'s AGENTS.md (and, for some, a memory snapshot) in its context, so "only its '
          'brief" is not literally exact, as in turn 110. A few listed a folder once with Glob, ls or Bash before reading.',
          '- The gate\'s first deliver run refused three manifests whose ABSENT rows had evidence under its 12-character minimum '
          '("no pronoun" for escape-trusted and therapist-licensed, "no prop" and "no colon" for solomon). I wrote those rows out '
          'in full in fill_ledgers.py, with no status changed, and the next run admitted them. The gate never replaces a delivery, '
          'so run_gate.py counts an earlier one as admitted only while its proof still matches the manifest, draft and context.',
          '- Notes outside the verdicts, for the sheet or a later pass: the medication paragraph\'s "just because you suspect it\'s '
          'involved" leans on the episodes in the paragraph above it (cold read 2 and preservation, round 3; both passed the '
          'heading); "That\'s fine for now." leans on its heading, so if Joel drops "If no answer comes", "If nothing comes," comes '
          'back (cold read 2, round 3).', '']
(HERE / 'GATE.md').write_text('\n'.join(lines), encoding='utf-8')
print('wrote GATE.md;', len(NAMES), 'on the sheet;', 'round-3 FAILs:', fails3)
