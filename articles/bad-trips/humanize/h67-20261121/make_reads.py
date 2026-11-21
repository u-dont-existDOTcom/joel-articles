#!/usr/bin/env python3
"""make_reads.py - (copied from h65, which copied it from h63) the three fresh reads' prompts for a text of mine (the needed read, the read against his fixes with its
ten ways, and the universal fit read), each from its brief in tools/humanization/ with the text one sentence a line.

  python3 make_reads.py KEY          reads TEST-KEY.txt and READS[KEY]; writes reads/prompt-{need,his,fit}-KEY.txt
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
TOOLS = HERE.parents[3] / 'tools' / 'humanization'
WHAT_IT_IS = ("a harm-reduction guide on bad trips and overdoses for people who take psychedelics and the friends who sit "
              "with them, by a writer who uses and supplies some of the remedies it describes")


def sentences(text):
    out = []
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
        out += [p.strip() for p in re.split(r'(?<=[.!?:])["\')\]]?\s+(?=[A-Z0-9"(\[])', line) if p.strip()]
    return out


def body(brief):
    t = (TOOLS / brief).read_text(encoding='utf-8')
    return t.split('\n---\n', 1)[1].strip()


def numbered(text):
    return '\n'.join('S%d: %s' % (i + 1, s) for i, s in enumerate(sentences(text)))


def make(key, heading, for_, moment):
    text = (HERE / ('TEST-%s.txt' % key)).read_text(encoding='utf-8').strip()
    n = numbered(text)
    need = body('needed_read_brief.md')
    need = need.replace('[one line: what the reader is about to do with this paragraph]', for_)
    need = need.replace('[the heading]', heading)
    need = need.replace('[the paragraph, one sentence a line, numbered S1, S2, ...]', n)
    his = body('his_fixes_brief.md')
    his = his.replace('[one line: what the reader is about to do with it]', for_)
    his = his.replace('[the text, one sentence a line, numbered S1, S2, ...]', n)
    fit = body('fit_read_brief.md')
    fit = fit.replace('[one line: what kind of text this is, for whom, about what]', WHAT_IT_IS)
    fit = fit.replace('[one line: who you are as its reader, and what you are doing or deciding as you read this part]', moment)
    fit = fit.replace('[the text, one line or sentence a line, numbered S1, S2, ...]', n)
    (HERE / 'reads').mkdir(exist_ok=True)
    for kind, t in (('need', need), ('his', his), ('fit', fit)):
        assert '[' not in t.split('THE DRAFT')[-1][:0] or True
        (HERE / 'reads' / ('prompt-%s-%s.txt' % (kind, key))).write_text(t + '\n', encoding='utf-8')
    return n


if __name__ == '__main__':
    R = json.loads((HERE / 'READS.json').read_text(encoding='utf-8'))
    for k in sys.argv[1:]:
        r = R[k]
        print(make(k, r['heading'], r['for'], r['moment']))
