"""The fresh readers' briefs for x1123a's warning texts (texts_x1123a): the needed read, the read against his fixes and
the fit read, from the briefs in tools/humanization as they are on this branch, into needed/KEY, his-fixes/KEY, fit/KEY.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1123a/make_briefs_x1123a.py [KEY ...]
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import sense_receipt as S  # noqa: E402
import texts_x1123a as T  # noqa: E402

TOOLS = ROOT / 'tools' / 'humanization'
WHAT = ('a self-help protocol for adults with trauma (PTSD, anxiety, numbness, fog) that uses supplements, a keto diet and '
        'iboga or mushroom microdoses; its warnings come first, near the top')
SPEC = {
    'lma2': None,
    'lma': dict(heading='A Complete Guide to Bio-De-Armoring (the warnings at the top)',
                for_='the reader learns that the protocol doesn\'t advise lion\'s mane or ashwagandha, and the rare lasting '
                     'effects people report from them',
                moment='you are an adult with trauma reading the warnings before starting, who may already take lion\'s '
                       'mane or ashwagandha or be thinking of adding them'),
    'agm': dict(heading='Agmatine Warning (The Voltage Governor), in the warnings at the top',
                for_='the reader learns when to stop agmatine, and that the flatness it can cause sometimes lasts after '
                     'stopping',
                moment='you are an adult with trauma about to try agmatine for glutamate storms, deciding what would make '
                       'you stop'),
    'htp': dict(heading='Serotonin Bottleneck Pattern: 5-HTP + Low-Dose P5P',
                for_='the reader learns the signs that mean stopping 5-HTP, the dangerous ones first, and what can linger '
                     'after stopping',
                moment='you are an adult with trauma and low mood or poor sleep, trying 5-HTP for a few nights and '
                       'deciding what would make you stop'),
}


SPEC['lma2'] = SPEC['lma']


def numbered(text):
    return '\n'.join('S%d: %s' % (n, s) for n, s in enumerate(S.sentences(text), 1))


def body(name):
    return (TOOLS / name).read_text(encoding='utf-8').split('\n---\n', 1)[1].lstrip('\n')


def main(keys):
    for key in keys:
        d = SPEC[key]
        text = T.TEXTS[key]()
        lines = numbered(text)
        briefs = {
            'needed': body('needed_read_brief.md')
            .replace('[one line: what the reader is about to do with this paragraph]', d['for_'])
            .replace('[the heading]', d['heading'])
            .replace('[the paragraph, one sentence a line, numbered S1, S2, ...]', lines),
            'his-fixes': body('his_fixes_brief.md')
            .replace('[one line: what the reader is about to do with it]', d['for_'])
            .replace('[the text, one sentence a line, numbered S1, S2, ...]', lines),
            'fit': body('fit_read_brief.md')
            .replace('[one line: what kind of text this is, for whom, about what]', WHAT)
            .replace('[one line: who you are as its reader, and what you are doing or deciding as you read this part]',
                     d['moment'])
            .replace('[the text, one line or sentence a line, numbered S1, S2, ...]', lines),
        }
        for kind, b in briefs.items():
            for gap in ('[one line: what the reader is about to do', '[the heading]', '[the paragraph, one sentence',
                        '[the text, one', '[one line: what kind of text', '[one line: who you are'):
                assert gap not in b, (key, kind, gap)
            out = HERE / kind / key
            out.mkdir(parents=True, exist_ok=True)
            (out / 'BRIEF.txt').write_text(b, encoding='utf-8')
            (out / 'TEXT.txt').write_text(text + '\n', encoding='utf-8')
            print(key, kind, len(b))


if __name__ == '__main__':
    main(sys.argv[1:] or [k for k in SPEC if k != 'lma2'])
