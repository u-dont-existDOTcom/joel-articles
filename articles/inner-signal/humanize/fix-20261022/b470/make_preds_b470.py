"""Batch 470g's forecasts, written before any check (2026-10-22): batch/PREDICTIONS.md and batch/FORECAST.json, one row per
changed paragraph as Pangram would read it in the next whole-guide recheck.

No paragraph goes to pangram.com (gate E200): the changed paragraphs are read in the real article through the temporary
Substack drafts, whose ledger predictions are written when the recheck is pasted. These rows say what I expect each
changed paragraph to read there, so the recheck scores them (as fix-20261021/b469/score_b469.py did 469g's, 15 of 15).
Every paragraph here read Human in the recheck of 2026-10-21 (all high but one, Appendix B's reframing questions, medium or
low in one of its windows), and the changes are names; the ones that add a sentence or a definition carry the risk.
The induction section's line (b470-chemicals) has no row: that section is replaced by the screened sample, which carries
Joel's 11 b in its own words.

  python3 articles/inner-signal/humanize/fix-20261022/b470/make_preds_b470.py   (from the repo root)
"""
import json, pathlib

B = pathlib.Path(__file__).resolve().parent
NAME = ('a name changed in a paragraph that read dark green; nothing else in it moves', 'none new',
        'the paragraph\'s own voice, as it read Human, high')
# key: (call, chance, why, tells, human tells)
P = {
    'b470-guard-first-read': ('Human', 0.85, 'a gloss in brackets added to a long, rambling paragraph that read dark green',
                              'a definitional gloss ("the protective reactions you learned as a child")',
                              '"etc etc etc", "mind you deeper mind", "supress", the run-on list of minds'),
    'b470-three-jobs-named': ('Human', 0.85, 'three adjectives and "(hereafter just the Protector)" added to the first naming, '
                                             'and "what you develop in yourself as you reparent" (the stance fix)',
                              'a triad of adjectives (loving, safe, wise); "hereafter" is formal',
                              '"but I don’t mean them as if there were really three people in you", "It’s you that needs"'),
    'b470-guide-label': ('Human', 0.9) + NAME,
    'b470-guide-work': ('Human', 0.9) + NAME,
    'b470-protector-parts-label': ('Human', 0.9) + NAME,
    'b470-guard-defined': ('Human', 0.75, 'a sentence of explanation added at the end: Joel\'s reason, in a paragraph that '
                                          'read dark green',
                           'a tidy explanatory closer ("the same as when you were a child")',
                           'the long, uneven list ("sexually aroused, like you need to make plans, sleepy"), "you might even '
                           'think that what you\'re doing is stupid", "charming guard"'),
    'b470-parent-script': ('Human', 0.75, 'the definition of the script rewritten in its first two sentences; "the script '
                                          'may jump in"; "that you build up on purpose"',
                           'a definition ("the set of rules and ways of treating yourself"), a hedge ("it doesn’t always '
                           'sound like a voice")',
                           '"not to embarrass them, not to be too independent, etc.", "“fake”", "parent(s)"'),
    'b470-to-the-part': ('Human', 0.85, 'a longer stage direction ("To the guard, the childhood protector part:") in a short '
                                        'script line that read dark green with its neighbors',
                         'an appositive label', 'the ellipses ("by…..?"), the question as said'),
    'b470-talk-to-part': ('Human', 0.9) + NAME,
    'b470-part-wants': ('Human', 0.9) + NAME,
    'b470-script-humiliating': ('Human', 0.85, 'a name changed, and "no value for its resume" put right in the first '
                                               'sentence (the stance fix)', 'none new',
                                'Joel\'s own sentences (his edit of 2026-10-21, Human in his check), "etc."'),
    'b470-guide-care': ('Human', 0.9) + NAME,
    'b470-script-fake': ('Human', 0.9, 'a name changed and "the voice of" out',
                         'none new', 'the paragraph\'s own voice'),
    'b470-anxious-parts': ('Human', 0.9) + NAME,
    'b470-guide-stuck': ('Human', 0.9) + NAME,
    'b470-guide-proportion': ('Human', 0.85, 'a name changed and two limits widened ("shut out all love", "disregard '
                                             'consequences")', 'a parenthesized list of parallel limits, as installed',
                              '"DO NOT:", the quotes around each role'),
    'b470-synchronicity': ('Human', 0.85, 'a name changed and a hedge added ("as objectively and clearly as I can") in a '
                                          'long first-person paragraph', 'none new',
                           'his own practice in the first person, "whilst", the long run-on sentences'),
    'b470-guide-cue': ('Human', 0.9) + NAME,
    'b470-guide-reframe': ('Human', 0.7, 'a name changed in a paragraph whose windows read Human, one of them medium or low',
                           'a run of "or How might my X reframe this?" questions', '"etc., etc."'),
    'b470-guide-nlp': ('Human', 0.9) + NAME,
    'b470-anxiety-part': ('Human', 0.75, 'two sentences added (Joel\'s reason) to the appendix\'s opening, which read dark '
                                         'green',
                          'an explanatory sentence repeated word for word from "Working with childhood protector parts"; two '
                          'sentences opening "It’s"',
                          'the list of fears ("or be exposed, or be sick, or be rejected, or lose control, or whatever")'),
    'b470-altered-part': ('Human', 0.9) + NAME,
}


def main():
    meta = json.loads((B / 'meta.json').read_text(encoding='utf-8'))
    drafts = json.loads((B / 'drafts.json').read_text(encoding='utf-8'))
    out, lines = {}, ['# Batch 470g: what I expect each changed paragraph to read in the next whole-guide recheck', '',
                      'Written by `make_preds_b470.py` before any check. Each row is one changed paragraph as Pangram reads '
                      'it (alone, or with a neighbor when under 50 words). "Was" is its reading in the recheck of '
                      '2026-10-21.', '', '| Paragraph | Section | Was | Call | Chance of Human | Why |', '|---|---|---|---|---|---|']
    for k, t in meta['texts'].items():
        if t.get('heading') or k not in P:
            continue
        call, chance, why, tells, human = P[k]
        r = t.get('reading_41') or {}
        out[k] = {'lineage': t['lineage'], 'call': call, 'chance': chance, 'why': why, 'tells': tells, 'human_tells': human,
                  'words': t['words'], 'first_words': ' '.join(drafts[k].split()[:12]), 'was': r.get('shade')}
        lines.append('| %s | %s | %s | %s | %.2f | %s |' % (k, t['section'], r.get('shade'), call, chance, why))
    missing = [k for k, t in meta['texts'].items() if not t.get('heading') and k not in P]
    lines += ['', 'No row: %s (the induction section is replaced by its screened sample).' % ', '.join(missing)]
    (B / 'batch').mkdir(exist_ok=True)
    (B / 'batch' / 'FORECAST.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (B / 'batch' / 'PREDICTIONS.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(len(out), 'forecasts; no row:', missing)


if __name__ == '__main__':
    main()
