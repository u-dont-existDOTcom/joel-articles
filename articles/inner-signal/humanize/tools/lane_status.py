"""lane_status.py - each section's Pangram history in this lane, as a Markdown table (2026-10-18).

  python3 tools/lane_status.py [--out FILE]

Reads every fix-*/b*/b*-results.json (batch order) and names each text by its section key and its stage:
  published   the text as published (429g), or a probe of it
  screen      an Emulate rewrite ("-emu...")
  fixed       my meaning fixes in a screen that read Human ("-fix")
  refix       Emulate's rewrite of the fixed text in the windows that read AI ("-refix", "-refix2", ...)
  triaged     a refix with the triaged meaning fixes of its second reading ("-rfix")
  paragraph   a paragraph check of a fixed or refix text ("-p<n>", alone or with a neighbour)
A section's state is "installed" when fix-20261018/installed.json lists it (the section is in HUMANIZED-SO-FAR.md, every
paragraph checked), else its newest whole-section check (Human means a 100% Human headline), with its paragraph checks.
"""
import argparse, glob, json, pathlib, re

H = pathlib.Path(__file__).resolve().parent.parent
STAGE = [(r'-p\d+(\+\w+)?$', 'paragraph'), (r'-rfix$', 'triaged'), (r'-refix\d*$', 'refix'), (r'-fix$', 'fixed'), (r'-emu', 'screen'),
         (r'-probe', 'published')]


def stage_of(name):
    for pat, s in STAGE:
        if re.search(pat, name):
            return s
    return 'published'


def key_of(name):
    m = re.match(r'(HG\d+(?:\+\d+)*)', name)
    return m.group(1) if m else re.split(r'-(?:emu|probe|edit|sec|fix|refix|p\d)', name)[0]


def history():
    rows = {}
    for f in sorted(glob.glob(str(H / 'fix-*' / 'b*' / 'b*-results.json')), key=lambda p: int(re.search(r'/b(\d+)/', p).group(1))):
        b = re.search(r'/b(\d+)/', f).group(1) + 'g'
        for name, v in json.load(open(f, encoding='utf-8')).items():
            rows.setdefault(key_of(name), []).append((b, name, v[0], v[1], v[2], 'https://www.pangram.com/history' + v[5], stage_of(name)))
    return rows


def human(head):
    return head.startswith('Human')


def installed():
    f = H / 'fix-20261018' / 'installed.json'
    return json.loads(f.read_text(encoding='utf-8')) if f.exists() else {}


def table(rows):
    inst = installed()
    out = ['| section | state | newest whole check | paragraph checks | earlier |', '|---|---|---|---|---|']
    for key in sorted(rows, key=lambda k: int(re.match(r'HG(\d+)', k).group(1)) if re.match(r'HG(\d+)', k) else 999):
        h = rows[key]
        whole = [x for x in h if x[6] != 'paragraph' and '+TOC' not in x[1]]
        paras = [x for x in h if x[6] == 'paragraph']
        if not whole:
            continue
        b, name, head, ai, words, link, st = whole[-1]
        state = ('Human' if human(head) else ('Mixed, AI %.2f' % ai if ai < 0.9 else 'AI %.2f' % ai)) + ' (%s)' % st
        if key in inst:
            state = '**installed** (%s)' % inst[key].get('stage', st)
        # paragraph checks of the newest whole text's stage only
        pc = [x for x in paras if x[0] >= b] if paras else []
        pcs = ('%d of %d Human' % (sum(human(x[2]) for x in pc), len(pc))) if pc else '-'
        before = '; '.join('%s %s %s %.2f' % (x[0], x[6], 'H' if human(x[2]) else 'AI', x[3]) for x in whole[:-1])
        out.append('| %s | %s | [%s %s](%s) | %s | %s |' % (key, state, b, name, link, pcs, before or '-'))
    return '\n'.join(out)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--out')
    a = ap.parse_args()
    t = table(history())
    if a.out:
        pathlib.Path(a.out).write_text(t + '\n', encoding='utf-8')
    print(t)
