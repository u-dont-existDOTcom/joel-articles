"""READ-RECORD.json and VERIFY.md for the paragraphs apply_fullread.py changed: each one read by me (the lead session,
Claude Opus 5.5, never a cheaper reader: E294) beside its words before the fix and his published version
(../VERIFY-PAIRS.md has all three for every paragraph), then in place in the guide. Every one reads clearly and says what
his published version says; the notes below say where a fix brings back a point the guide had lost, or is new words.

  python3 articles/inner-signal/humanize/fix-20261030/fullread/read/record_fixes_read.py
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
FR = HERE.parent
H = FR.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402

NOTES = {
    11: 'brings back what each mind is doing (published P3), split into sentences',
    35: 'brings back the contrast: ads, screens, fear and the rest are already training the mind',
    80: 'brings back what each part wants (the published map)',
    99: 'you pick the words or the action yourself (published), said once',
    172: 'rest without helplessness, and you can still move, stop and come back (published)',
    337: 'tightening doesn\'t explain itself; don\'t repeat a suggestion more persuasively (published)',
    339: 'a new possibility can bring a feeling worth meeting; you needn\'t know which before finding out (published)',
    345: 'the published titration line, with the stop line kept',
    353: 'the love isn\'t failing; more tears aren\'t more healing (published), without "prove"',
    362: 'fifteen minutes is an appointment, and your feelings needn\'t keep to it (published)',
    365: 'what you can now carry yourself (published), not what you take away',
    505: 'what a presupposition is, and no obedience smuggled in (published); its example is the next paragraph',
    507: 'the published better bridge, as a small claim',
    601: 'new words: his audit fix applied to Appendix C\'s list, every item kept (urgency, secrecy, shame, exclusion, '
         'specialness, sexual charge, spiritual superiority; money, sex, loyalty, silence, obedience; narrowed choices, '
         'questioning made wrong, not obeying made a problem, normal life made boring, the inner child seduced, scared or '
         'rescued, the adult\'s no stopped), with a bridge in his strategy\'s place: people who mean well can ask for some '
         'of these too, and a no they take well is a good sign (his next two paragraphs: "A good guide can take no")',
    588: 'the sequence is for yourself, as published (it had become a practitioner\'s protocol, "the person")',
}


def main():
    ap = json.loads((FR / 'APPLIED-FULLREAD.json').read_text(encoding='utf-8'))
    bl = sr.blocks((H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'))
    assert cr.hashlib.sha256((H / 'HUMANIZED-SO-FAR.md').read_bytes()).hexdigest() == ap['after_sha256']
    now = {cr.phash(b['text']): b for b in bl if not b['level']}
    cov, lines = [], ['# My read of the paragraphs fixed after the full read (2026-10-30)', '',
                      'Each paragraph below was read by me (the lead session, never a cheaper reader: E294) beside its '
                      'words before the fix and Joel\'s published version ([the three side by side](../VERIFY-PAIRS.md)), '
                      'then in place. Verdict for every one: reads clearly, and says what his published version says.', '']
    for c in sorted(ap['changed'], key=lambda c: (c['block'], bool(c.get('inserted_after') is not None))):
        if c.get('deleted'):
            lines.append('- Block %d (%s): taken out (%s): "%s"' % (c['block'], c['where'], ', '.join(c['findings']),
                                                                     c['before'][:90]))
            continue
        for para in c['after'].split('\n\n'):
            t = sr.blocks(para)[0]['text'] if para.lstrip().startswith(('-', '*')) or '](' in para else para
            h = cr.phash(t)
            assert h in now, (c['block'], t[:80])
            cov.append(h)
        note = NOTES.get(c['block'], '')
        lines.append('- Block %d (%s; %s)%s' % (c['block'], c['where'], ', '.join(c['findings']),
                                               (': ' + note) if note else ''))
    cr.record(HERE, findings=[], coverage=cov, dispositions={},
              article='HUMANIZED-SO-FAR.md: the paragraphs fixed after the full read of 2026-10-30, read by the lead '
                      'session (E294)')
    (HERE / 'VERIFY.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(len(set(cov)), 'paragraphs recorded')


if __name__ == '__main__':
    main()
