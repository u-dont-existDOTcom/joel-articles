"""Batch 469g's predictions, written before the run (2026-10-21): batch/PREDICTIONS.md, and one ledger prediction per
text (tools/humanization/pangram_ledger.py, articles/inner-signal/humanize/pangram-ledger.jsonl), which refuses what the
2026-10-20 budget rule forbids (a retry with no diagnosis, a lineage past its tries, the same text twice).

Only the paragraph texts go to pangram.com. The two sections' readings in 4.1 (the return steps, installed after the
first whole-guide reading, and Appendix C with its prose) come from the whole-guide recheck through Substack, which reads
every sentence in its place and costs no credits (Joel, 2026-10-20 22:01 UTC; question 7, b).

  python3 articles/inner-signal/humanize/fix-20261021/b469/make_preds_b469.py   (from the repo root)
"""
import json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[5]
B = pathlib.Path(__file__).resolve().parent
LEDGER = REPO / 'articles' / 'inner-signal' / 'humanize' / 'pangram-ledger.jsonl'

APPC = ('Appendix C as published read AI, high, as one window with the end of Appendix B in the whole guide (4.1), and '
        'AI 1.00 alone in 4.0; ')
# key: (lineage, call, chance, why, tells, human tells)
PREDS = {
    'HG18-count-feet': ('HG18-p3', 'Human', 0.55,
                        "the count as installed read Human in 4.0 (466g, whole and every paragraph); the edit is small (\"these "
                        "five steps\", \"and what it's resting on\", a stray quotation mark out); but it's five numbered steps in "
                        "a row, and 4.1 reads a run of parallel steps red",
                        'five numbered imperative steps, each a short parallel clause ("feel your breathing return to normal")',
                        '"1...", "(of your choice)", "This session is now over."'),
    'HG18-stopped-press': ('HG18-p5', 'Human', 0.6,
                           'one plain sentence added after the installed one, checked with the paragraph before it, which read '
                           'Human in 4.0 (466g); that paragraph is a run of short instructions, the pattern 4.1 reads red',
                           'a run of short instructions ("Look to your left and your right. Look at something near, and '
                           'something far. Move around a bit ..."), and one more at the end',
                           '"(or date)", "Don\'t just assume it because you\'ve done the count.", "for some reason"'),
    'HG32-prose-p1': ('HG32-c-p1', 'AI', 0.4,
                      APPC + "the opening line and the statement to say in one paragraph: Joel's catch-all, his lead-in, "
                      "\"Let me slow down\", the body line as a statement and the last test as a question; still a list of "
                      'six kinds of influence and an abstract list of four',
                      '"love, truth, humility and ordinary life"; a list of six kinds of influence; "I don\'t have to ... I '
                      'don\'t have to"', '"stuff like that", "Okay,", "Let me slow down", "taking for granted", the question'),
    'HG32-prose-p2': ('HG32-c-p2', 'AI', 0.35,
                      APPC + "the statement's four tests in four shapes, one a question, checked with the paragraph before; "
                      'still four tests that close the statement like aphorisms',
                      'a run of tests ("If it\'s true ... Would real love mind ... real guidance will still be there ... '
                      'Anything that\'s really for me")', '"after I sleep on it", "Would real love mind my boundaries?"'),
    'HG32-prose-p3': ('HG32-c-p3', 'AI', 0.4,
                      APPC + 'the signs as statements and one question, one list ending on a catch-all and the rest split; '
                      'still a paragraph of signs, most of them abstract nouns',
                      'a run of signs; abstract nouns (urgency, secrecy, shame); "Demands ... demand"',
                      '"that kind of thing", "Is there a sexual charge, or spiritual superiority?", "Be wary if it"'),
    'HG32-prose-p4': ('HG32-c-p4', 'AI', 0.4,
                      APPC + 'the warnings in loose spoken shapes ("Same if ...", "Or if ...") with a particular ("like the '
                      'dishes and your friends don\'t matter anymore"), checked with the signs before them',
                      'the signs paragraph before; three warnings in a row', '"Same if", "the dishes and your friends"'),
    'HG32-prose-p5': ('HG32-c-p5', 'AI', 0.45,
                      APPC + 'the warnings with the child part and the adult self (a question), short sentences',
                      'three warnings in a row before it; "Notice whether"', '"Being rescued counts too.", "Same if", the question'),
    'HG32-prose-p6': ('HG32-c-p6', 'AI', 0.45,
                      APPC + 'the child part with what to do when you see several: imperatives, then "Just come back to the room '
                      'and your body for a while", then the list ending on "and so on"',
                      'a run of imperatives ("slow down. Don\'t ... don\'t ... Just come back ... Then eat, sleep")',
                      '"and so on", "for a while", "Being rescued counts too."'),
    'HG32-prose-p7': ('HG32-c-p7', 'AI', 0.4,
                      APPC + 'the good and bad guide with a question in the middle ("And can they take your no? A bad guide '
                      'can\'t."), less balanced than the four parallel sentences; still a good/bad contrast',
                      'a good/bad guide contrast; a list of labels', '"you name it", "And can they take your no?"'),
    'HG14-cf-addressee': ('HG14-cf1', 'Human', 0.65,
                          'three words and a closing quotation mark added to a script line; both paragraphs read Human, '
                          'high, in the whole guide (4.1, window 36), but never alone in 4.1',
                          'the inherited-parent paragraph explains in a run ("This is ... This is not the same as ... Often '
                          '...")', '"(parent(s)", "by…..?", "not to be “needy”", "etc."'),
    'HG20-cf-roles': ('HG20-cf2', 'Human', 0.6,
                      'three capitals and one clause said plainly ("and if you can\'t do one yet, borrow it"); the paragraph '
                      'read Human, high, in the whole guide (4.1, window 66)',
                      'a list of three uses ("change the “tone” ..., set boundaries, or help you figure out"); capitalized '
                      'role names in quotes', '"etc to help you", "in a better fashion", "feel free to do so"'),
    'HG24-cf-grownup': ('HG24-cf3', 'Human', 0.65,
                        "Joel's name for the internalized voice and \"of your own\"; the paragraph read Human, high, in "
                        "the whole guide (4.1, window 71)",
                        '"inherited inner parent" is a term; "it isn\'t useful to argue with this part, but find out"',
                        '"that you are picking up", "\'grown up\' voice", "Again,"'),
    'HG36-cf-protector': ('HG36-cf5', 'Human', 0.75,
                          '"a protector part" for "a Protector"; the paragraph read Human, high, in the whole guide (4.1, '
                          'window 30 of part B)', 'three "regardless of" clauses in a row',
                          '"etc, etc, etc", "/ sad about / angry about /", the exclamation'),
    'HG37-cf-nurturer': ('HG37-cf6', 'Human', 0.65,
                         'the published sign put back in plain words ("like you\'re trying to protect something"); the '
                         'paragraph read Human, high, in the whole guide (4.1, window 30 of part B)',
                         'three "if you feel" clauses in a row', '"call upon your Nurturer", "stop trying to deal with it"'),
}


def main():
    drafts = json.loads((B / 'drafts.json').read_text(encoding='utf-8'))
    edits = {e['key']: e for e in json.loads((B / 'meta.json').read_text(encoding='utf-8'))['edits']}
    rows = ['# Predictions and Pangram results: batch 469g', '',
            "Pangram's web app (4.1). Joel's answers of 2026-10-21 17:56 UTC put into the guide: Appendix C's general "
            'checklist as prose (question 2, c), the one point the installed return steps lost (question 4, d), and the '
            "inner-adult sweep's five fixes (his \"check the guide for that conflation\"). Each paragraph as Pangram reads "
            'it (a paragraph under 50 words with its neighbor). Predictions written before the run; chance = my chance of '
            'a 100% Human result.', '', '## Batch 469g', '', '| text | mine | chance | why | Pangram |', '|---|---|---|---|---|']
    tmp = B / 'batch' / 'texts'
    tmp.mkdir(parents=True, exist_ok=True)
    for key, (lineage, call, chance, why, tells, human) in PREDS.items():
        rows.append('| %s | %s | %d%% | %s | |' % (key, call, round(chance * 100), why))
        f = tmp / ('%s.txt' % key)
        f.write_text(drafts[key], encoding='utf-8')
        edit = edits[key] if key in edits else edits['HG32-prose']
        r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
                            '--lineage', lineage, '--scope', 'paragraph', '--text', str(f), '--key', key, '--batch', 'b469g',
                            '--call', call, '--chance', str(chance), '--tells', tells, '--human-tells', human,
                            '--diagnosis', edit['diagnosis'], '--detector', 'pangram 4.1, web app'],
                           capture_output=True, text=True, cwd=REPO)
        print(key, (r.stdout or r.stderr).strip()[-300:])
        if r.returncode:
            return r.returncode
    (B / 'batch' / 'PREDICTIONS.md').write_text('\n'.join(rows) + '\n', encoding='utf-8')
    return 0


if __name__ == '__main__':
    sys.exit(main())
