"""Writes the fresh readers' briefs for x1113b: the needed read, the read against his fixes and the fit read, for each of
the three texts (block 95, block 54, the DMSO item), from the briefs in tools/humanization as they are on this branch.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1113b/make_briefs.py
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import sense_receipt as S  # noqa: E402
import texts_x1113b as T  # noqa: E402

TOOLS = ROOT / 'tools' / 'humanization'
TEXTS = {
    'sp95b': dict(
        text=T.plain(T.K95),
        heading='Fixing ATP Signaling if Cortisol Isn\'t High',
        for_='the reader choosing between the two ketone strategies learns what the choice changes in their salt plan, '
             'what Strategy A is for, and what the salts do for brain fog',
        what='a self-help protocol for adults with trauma (PTSD, anxiety, numbness, fog), at the point where it has you '
             'pick one of two ways to get ketones (a backup brain fuel): drinking ketone salts, or a keto diet',
        moment='you are an adult with trauma and brain fog, deciding whether to start with the ketone salt drinks '
               '(Strategy A) or with the keto diet'),
    'sp54': dict(
        text=T.plain(T.K54),
        heading='D. The "Lagging" System: Toxicity & Hypometabolism (The Fog)',
        for_='the reader whose brain fog may come from a brain burning less sugar learns that ketones are a backup fuel '
             'such a brain still takes up, and what giving ketones has done for people whose brains struggle with fuel',
        what='a self-help protocol for adults with trauma (PTSD, anxiety, numbness, fog), in the part that explains why '
             'brain fog may be a fuel problem and what the protocol gives for it',
        moment='you are an adult with trauma and brain fog, reading why the protocol has you take ketones'),
    'spdmsoc': dict(
        text='\n\n'.join(T.plain(m) for m in T.DMSO),
        heading='2. The Glutamate Shield (Anxiety):',
        for_='the reader with anxiety and glutamate storms learns what DMSO, which the protocol has them smell, has done '
             'in a dish, in people and in animals, how safe it is and who should be careful with it, and how it feels '
             'to the author',
        what='a self-help protocol for adults with trauma (PTSD, anxiety, numbness, fog), at an item in its list of '
             'supplements that calm glutamate, the brain\'s main "go" signal',
        moment='you are an adult with trauma whose anxiety comes in "glutamate storms", deciding whether to smell DMSO as '
               'the protocol suggests and whether it is safe for you'),
}


def numbered(text):
    out, n = [], 0
    for para in text.split('\n\n'):
        if out:
            out.append('')
        for s in S.sentences(para):
            n += 1
            out.append('S%d: %s' % (n, s))
    return '\n'.join(out)


def body(name):
    t = (TOOLS / name).read_text(encoding='utf-8')
    return t.split('\n---\n', 1)[1].lstrip('\n')


def main():
    for key, d in TEXTS.items():
        lines = numbered(d['text'])
        briefs = {
            'needed': body('needed_read_brief.md')
            .replace('[one line: what the reader is about to do with this paragraph]', d['for_'])
            .replace('[the heading]', d['heading'])
            .replace('[the paragraph, one sentence a line, numbered S1, S2, ...]', lines),
            'his-fixes': body('his_fixes_brief.md')
            .replace('[one line: what the reader is about to do with it]', d['for_'])
            .replace('[the text, one sentence a line, numbered S1, S2, ...]', lines),
            'fit': body('fit_read_brief.md')
            .replace('[one line: what kind of text this is, for whom, about what]', d['what'])
            .replace('[one line: who you are as its reader, and what you are doing or deciding as you read this part]',
                     d['moment'])
            .replace('[the text, one line or sentence a line, numbered S1, S2, ...]', lines),
        }
        for kind, b in briefs.items():
            for gap in ('[one line: what the reader is about to do', '[the heading]', '[the paragraph, one sentence',
                        '[the text, one', '[one line: what kind of text', '[one line: who you are'):
                assert gap not in b, (key, kind, gap)
            d_ = HERE / kind / key
            d_.mkdir(parents=True, exist_ok=True)
            (d_ / 'BRIEF.txt').write_text(b, encoding='utf-8')
            (d_ / 'TEXT.txt').write_text(d['text'] + '\n', encoding='utf-8')
            print(kind, key, len(b))


if __name__ == '__main__':
    main()
