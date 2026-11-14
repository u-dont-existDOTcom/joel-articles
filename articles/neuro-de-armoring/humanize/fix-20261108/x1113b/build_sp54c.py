"""The receipt for SC-54 try 3b (texts_x1113b.K54C): Codex's rewrite (rewrite-sp54/codex-rewrite.md, from the panel's notes
on my try 3) in the reader's order. The reads are needed/sp54c, his-fixes/sp54c and fit/sp54c, each READ.md with what I did.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1113b/build_sp54c.py
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
    text = T.plain(T.K54C)
    s = S.sentences(text)
    assert len(s) == 8, len(s)
    reader = ('someone with trauma and brain fog reading why the protocol gives them ketones: whether their fog may be a '
              'brain short of fuel, and what giving ketones has done for brains like that')
    spec = {
        'The Fix': ('they learn the protocol\'s answer to the fuel problem the paragraph before describes: another fuel',
                    'it answers "The Problem" just before: some regions of PTSD brains burn less sugar', None),
        'Ketones are the brain': ('they learn the other fuel is ketones, and that a brain taking up less sugar still takes '
                                  'them up', 'it names the fuel the sentence before promised', 'Ketones are the brain'),
        'And one man': ('they learn what giving ketones did for one brain short of sugar: a man with Alzheimer\'s got '
                        'markedly better', 'it goes from the Alzheimer\'s brain taking up ketones to what giving them did '
                        'for one', 'And one man\'s Alzheimer\'s'),
        'An early Parkinson': ('they learn the same was seen in Parkinson\'s, and how weak that study was',
                               'it adds a second disease to the first', 'An early Parkinson\'s study'),
        'In a bigger randomized': ('they learn a controlled trial found keto did more for fatigue and daytime sleepiness, '
                                   'part of the fog they have', 'it weighs the small study with a bigger one',
                                   'In a bigger randomized Parkinson\'s trial'),
        'Their thinking problems': ('they learn thinking eased more too, the rest of their fog',
                                    'it adds the trial\'s second finding for the fog', 'Their thinking problems'),
        'Movement improved': ('they learn the diet did no more for movement, which keeps the small study\'s big change in '
                              'proportion', 'it gives the trial\'s other side', 'on both'),
        'PQQ made': ('they learn why the protocol also gives PQQ for the fog, and how far that evidence goes',
                     'it turns from the fuel to the parts of the cell that burn it', 'burn fuel')}
    checked = [
        ('one woman\'s Alzheimer\'s was reversed (his, with his LongeCity link)',
         'Steve Newport, a man with early-onset Alzheimer\'s; improved markedly over 20 months on a ketone monoester '
         '(Newport et al. 2015)', 'yes: they learn what giving ketones did for one brain short of sugar', 'changed'),
        ('one study shows large improvement for Parkinson\'s (his)',
         'VanItallie et al. 2005: five people, 28 days, all improved, no comparison group; Phillips et al. 2018: keto more '
         'than low-fat on fatigue, daytime sleepiness and thinking, the same on movement',
         'yes: they learn the big change he points to, and what the controlled trial found for fog-like symptoms',
         'changed')]
    needed = {'reader': B.reader_line('needed', 'sp54c'), 'unneeded': [s[3], s[6], s[7]],
              'kept': {s[3]: 'they learn the big improvement he points to, sourced, which the trial after it weighs',
                       s[6]: 'they learn the diet did no more for movement, which keeps the small study\'s big change in '
                             'proportion',
                       s[7]: 'they learn why the protocol also gives them PQQ for the fog, the paragraph\'s second fix'}}
    his_fixes = {'reader': B.reader_line('his-fixes', 'sp54c'),
                 'marked': [{'s': s[1], 'difference': '1'}, {'s': s[2], 'difference': '4, 8'},
                            {'s': s[3], 'difference': '3, 4'}, {'s': s[5], 'difference': '4'},
                            {'s': s[6], 'difference': '4'}, {'s': s[7], 'difference': '3'}],
                 'kept': {s[1]: 'Codex\'s sentence, the other family\'s writer the panel rule calls for, kept for this check',
                          s[2]: 'read Human High by itself as he approved it; "improved markedly" is the case report\'s words',
                          s[3]: 'Codex\'s sentence: the caveat is said with the result it limits, kept for this check',
                          s[5]: 'it follows S5, which names the keto and low-fat diets it is more than',
                          s[6]: 'it follows S5, which names the two diets "both" means',
                          s[7]: 'the limit stays with the finding it limits, kept for this check'}}
    fit = {'reader': B.reader_line('fit', 'sp54c'),
           'marked': [{'s': s[0], 'found': 'CAN\'T TELL: the reader can\'t measure their brain\'s sugar use'},
                      {'s': s[5], 'found': 'FROM: "Their" points back to the Parkinson\'s trial'}],
           'kept': {s[0]: 'the paragraph before says scans of PTSD brains show regions burning less sugar, the reader\'s '
                          'case; nothing asks them to measure it',
                    s[5]: 'it follows S5, which names the Parkinson\'s trial and its keto group, the people "Their" means'}}
    same = ('none: read the section from its heading (D. The "Lagging" System) to the next for ketones as the brain\'s '
            'backup fuel and what giving them did; block 53 states the problem, this block the fix')
    r = S.make(text, B.sr.where(B.BL, 54).rsplit(',', 1)[0], reader)
    B.fill(r, spec)
    r['opens'] = {'first_sentence': s[0], 'why_reading': 'they learn the protocol\'s fix for the fuel problem they may '
                                                         'have: a second fuel'}
    r['checked'] = B.chk(checked)
    r['needed'], r['his_fixes'], r['fit'] = needed, his_fixes, fit
    r['same_point'] = same
    r['placement'] = ('block 54, "The Fix", where SC-54 put it: after Cunnane\'s finding, which the new sentences follow up, '
                      'and before the PQQ sentence')
    r['questions'] = dict(B.Q_ANS)
    (HERE / 'SP54C.receipt.json').write_text(json.dumps(r, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    (HERE / 'SP54C.txt').write_text(text + '\n', encoding='utf-8')
    probs = S.check(text, r)
    for p in probs:
        print(p)
    print('ok' if not probs else 'PROBLEMS')
    return 1 if probs else 0


if __name__ == '__main__':
    sys.exit(main())
