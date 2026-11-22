"""The receipt for SC-54 humanized (texts_x1113b.K54H), the paragraph he approved on 2026-11-14 after its check as approved
read AI Detected, 69% AI (checks-1114, https://www.pangram.com/history/6ed0e3e9-ac92-4b1a-b6fa-3f19e03445d9). Same facts and
citations; the reads are needed/sp54h, his-fixes/sp54h and fit/sp54h, each READ.md with what I did about it.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1113b/build_sp54h.py
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_x1113b as B  # noqa: E402
import texts_x1113b as T  # noqa: E402

S = B.S


def main():
    text = T.plain(T.K54H)
    s = S.sentences(text)
    assert len(s) == 5, len(s)
    reader = ('someone with trauma and brain fog reading why the protocol gives them ketones: whether their fog may be a '
              'brain short of fuel, and what giving ketones has done for brains like that')
    spec = {
        'The Fix': ('they learn the protocol\'s answer to the fuel problem the paragraph before describes: another fuel',
                    'it answers "The Problem" just before: some regions of PTSD brains burn less sugar', None),
        'Ketones are its backup fuel': ('they learn the other fuel is ketones, and that a brain taking up less sugar '
                                        'still takes them up', 'it names the fuel the sentence before promised',
                                        'Ketones are its backup fuel'),
        'And one man': ('they learn what giving ketones did for one brain short of sugar: a man with Alzheimer\'s got '
                        'markedly better', 'it goes from the Alzheimer\'s brain taking up ketones to what giving them did '
                        'for one', 'And one man\'s Alzheimer\'s'),
        'In Parkinson': ('they learn the same was seen in another brain disease short of fuel, how weak that study was, and '
                         'that a controlled trial found the diet did more for tiredness and thinking, the fog they have',
                         'it adds a second disease to the first, with the trial that weighs it', 'In Parkinson\'s too'),
        'PQQ may help too': ('they learn why the protocol also gives PQQ for the fog, and how far that evidence goes',
                             'it turns from the fuel to the parts of the cell that burn it', 'PQQ may help too')}
    checked = [
        ('one woman\'s Alzheimer\'s was reversed (his, with his LongeCity link)',
         'his link (2008, quoting the Tampa Bay Times): Steve Newport, a man with early-onset Alzheimer\'s, on coconut oil; '
         'the case report: improved markedly over 20 months on a ketone monoester (Newport et al. 2015)',
         'yes: they learn what giving ketones did for one brain short of sugar', 'changed'),
        ('one study shows large improvement for Parkinson\'s (his)',
         'VanItallie et al. 2005: five people, 28 days, all improved, placebo not ruled out; Phillips et al. 2018: 47 '
         'randomized, keto more than low-fat on fatigue, daytime sleepiness and thinking, the same on movement',
         'yes: they learn the big change he points to, and what the controlled trial found for fog-like symptoms',
         'changed')]
    needed = {'reader': B.reader_line('needed', 'sp54h'), 'unneeded': [s[4]],
              'kept': {s[4]: 'they learn why the protocol also gives them PQQ for the fog: the paragraph\'s second fix, '
                             'there before this card, reworded only to read human'}}
    his_fixes = {'reader': B.reader_line('his-fixes', 'sp54h'),
                 'marked': [{'s': s[2], 'difference': '4, 8'}, {'s': s[3], 'difference': '1, 3'},
                            {'s': s[4], 'difference': '8'}],
                 'kept': {s[2]: 'read Human High by itself as he approved it; "improved markedly" is the case report\'s '
                                'own words and "one" says it is a single case',
                          s[3]: 'joined on purpose: the trial is there to weigh the small study, and the two apart read '
                                'AI Low and Human Medium in the first check',
                          s[4]: '", but" is the join his fixes make (the brief\'s eighth difference); the caveat stays '
                                'with the finding it limits'}}
    fit_read = (HERE / 'fit' / 'sp54h' / 'READ.md')
    fit = {'reader': B.reader_line('fit', 'sp54h'), 'marked': [], 'kept': {}}
    if fit_read.exists():
        fit = json.loads((HERE / 'fit' / 'sp54h' / 'MARKS.json').read_text(encoding='utf-8'))
        fit['reader'] = B.reader_line('fit', 'sp54h')
    same = ('none: read the section from its heading (D. The "Lagging" System) to the next for ketones as the brain\'s '
            'backup fuel and what giving them did; block 53 states the problem, this block the fix. Block 48 is PTSD, '
            'block 94 anxiety and depression, block 95 what the salts do: none gives this evidence')
    r = S.make(text, B.sr.where(B.BL, 54).rsplit(',', 1)[0], reader)
    B.fill(r, spec)
    r['opens'] = {'first_sentence': s[0], 'why_reading': 'they learn the protocol\'s fix for the fuel problem they may '
                                                         'have: a second fuel'}
    r['checked'] = B.chk(checked)
    r['needed'], r['his_fixes'], r['fit'] = needed, his_fixes, fit
    r['same_point'] = same
    r['placement'] = ('block 54, "The Fix", where SC-54 put it: after Cunnane\'s finding that early-Alzheimer\'s brains still '
                      'take up ketones, which the new sentences follow up, and before the PQQ sentence')
    r['questions'] = dict(B.Q_ANS)
    (HERE / 'SP54H.receipt.json').write_text(json.dumps(r, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    (HERE / 'SP54H.txt').write_text(text + '\n', encoding='utf-8')
    probs = S.check(text, r)
    for p in probs:
        print(p)
    print('ok' if not probs else 'PROBLEMS')
    return 1 if probs else 0


if __name__ == '__main__':
    sys.exit(main())
