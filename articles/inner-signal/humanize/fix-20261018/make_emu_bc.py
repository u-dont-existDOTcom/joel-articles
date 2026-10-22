"""emu-bc to emu-bh (2026-10-22, after the recheck of 2026-10-21 22:44 UTC): new Emulate samples to screen before any
meaning work.

The recheck read the induction section (HG17, sample ba with every lost point put back) AI from its first paragraph to the
shortcut, and Pangram marked most of its windows "humanized"; Appendix C's prose (469g) read AI as one window. Sample ba
had been chosen by meaning alone: under gate E200 no sample went through a Pangram screen, while HG18's sample, which reads
Human in 4.1, was chosen because its screen read 100% Human in 4.0. So these samples are screened first, in a temporary
Substack post (free), and the meaning work goes into the one that reads Human:
  emu-bc, emu-bd  HG17-pub2  the induction section from the published text (as az, ba and bb were)
  emu-be, emu-bf  HG17-fx1   the installed fixed section (every point kept; Joel's 11 b put in: "overwhelmed by
                             chemicals"), so a sample starts with all the points
  emu-bg, emu-bh  HG32-pr1   Appendix C's general checklist as the installed prose (469g; its audit list stays a list)
Run from fix-20261018/: python3 make_emu_bc.py
"""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(H / 'tools'))
import make_emu_ac as E  # noqa: E402
import assemble as A  # noqa: E402

kb = A.kb()['HG17']
Q11 = ('If you are intoxicated, acutely confused, or not able to keep yourself safe,',
       'If you are overwhelmed by chemicals, acutely confused, or not able to keep yourself safe,')


def pub():
    text = '\n\n'.join(kb[b][1] for b in range(len(kb)))
    heads = [b for b in range(len(kb)) if kb[b][0].lstrip().startswith('#')]
    return ('HG17-pub2', text, {'key': 'HG17', 'sent': list(range(len(kb))), 'headings': heads, 'words': len(text.split()),
                                'input': 'published text', 'from': 'source/published-20260928.md B0-B%d' % (len(kb) - 1)})


def fixed():
    d = json.loads((HERE / 'rf-zg' / 'HG17.fixed.json').read_text(encoding='utf-8'))
    paras = []
    for u in d['units']:
        if u['kind'] == 'emulate':
            paras += u['paras']
        else:
            paras += [kb[b][1] for b in u['blocks']]
    text = '\n\n'.join(paras)
    assert text.count(Q11[0]) == 1
    text = text.replace(*Q11)
    return ('HG17-fx1', text, {'key': 'HG17', 'words': len(text.split()), 'input': 'the installed fixed section with 11 b',
                               'from': 'fix-20261018/rf-zg/HG17.fixed.json (headings from the published text)'})


def appc():
    meta = json.loads((H / 'fix-20261021' / 'b469' / 'meta.json').read_text(encoding='utf-8'))
    e = next(x for x in meta['edits'] if x['key'] == 'HG32-prose')
    text = 'Appendix C: The extended de-hypnosis checklist\n\n' + e['new'].strip()
    return ('HG32-pr1', text, {'key': 'HG32', 'words': len(text.split()), 'input': 'the installed prose (469g)',
                               'from': 'fix-20261021/b469/meta.json HG32-prose new'})


if __name__ == '__main__':
    for folder, run in (('emu-bc', pub()), ('emu-bd', pub()), ('emu-be', fixed()), ('emu-bf', fixed()),
                        ('emu-bg', appc()), ('emu-bh', appc())):
        E.write(folder, [run], [])
