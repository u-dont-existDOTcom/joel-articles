"""Writes the fresh readers' briefs for x1120a's text of mine (texts_x1120a.W35): the needed read, the read against his
fixes and the fit read, from the briefs in tools/humanization as they are on this branch.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1120a/make_briefs_x1120a.py [KEY NAME]
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import sense_receipt as S  # noqa: E402
import texts_x1120a as T  # noqa: E402

TOOLS = ROOT / 'tools' / 'humanization'
# the reads of each version: w35, w35b, w35c and w35d hold the reads of W35A, W35B, W35C and W35; w35e of W35E
# (2026-11-23). Give the key and the text's name: python3 make_briefs_x1120a.py w35e W35E
KEY, NAME = (sys.argv[1], sys.argv[2]) if len(sys.argv) > 2 else ('w35e', 'W35E')
D = dict(
    text=getattr(T, NAME),
    heading='Weeks 3–5: The Dynorphin Void (Depression Phase)',
    for_='the reader starting the Weeks 3-5 phase learns to start its new supplements, microdoses and diet one at a time, '
         'and what to do about UMP and 5-HTP on the days they microdose',
    what='a self-help protocol for adults with trauma (PTSD, anxiety, numbness, fog), at the top of its Weeks 3-5 plan '
         '(the "Void": numb, gray, low drive), which lists a UMP trial and a 5-HTP trial (supplements, each taken for a '
         'few days to see if it helps), iboga and mushroom microdoses, and a move to the keto diet; an earlier rule says '
         'not to take UMP or 5-HTP on psychedelic days',
    moment='you are an adult with trauma in the numb, gray phase, about to start that phase\'s supplements, microdoses '
           'and diet')


def numbered(text):
    return '\n'.join('S%d: %s' % (n, s) for n, s in enumerate(S.sentences(text), 1))


def body(name):
    return (TOOLS / name).read_text(encoding='utf-8').split('\n---\n', 1)[1].lstrip('\n')


def main():
    lines = numbered(D['text'])
    briefs = {
        'needed': body('needed_read_brief.md')
        .replace('[one line: what the reader is about to do with this paragraph]', D['for_'])
        .replace('[the heading]', D['heading'])
        .replace('[the paragraph, one sentence a line, numbered S1, S2, ...]', lines),
        'his-fixes': body('his_fixes_brief.md')
        .replace('[one line: what the reader is about to do with it]', D['for_'])
        .replace('[the text, one sentence a line, numbered S1, S2, ...]', lines),
        'fit': body('fit_read_brief.md')
        .replace('[one line: what kind of text this is, for whom, about what]', D['what'])
        .replace('[one line: who you are as its reader, and what you are doing or deciding as you read this part]',
                 D['moment'])
        .replace('[the text, one line or sentence a line, numbered S1, S2, ...]', lines),
    }
    for kind, b in briefs.items():
        for gap in ('[one line: what the reader is about to do', '[the heading]', '[the paragraph, one sentence',
                    '[the text, one', '[one line: what kind of text', '[one line: who you are'):
            assert gap not in b, (kind, gap)
        d = HERE / kind / KEY
        d.mkdir(parents=True, exist_ok=True)
        (d / 'BRIEF.txt').write_text(b, encoding='utf-8')
        (d / 'TEXT.txt').write_text(D['text'] + '\n', encoding='utf-8')
        print(kind, len(b), d)


if __name__ == '__main__':
    main()
