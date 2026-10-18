"""lane_status.py - each section's Pangram history in this lane, newest result last, as a Markdown table (2026-10-18).

  python3 tools/lane_status.py [--out FILE]

Reads every fix-*/b*/b*-results.json (batch order) and names each text by its section key (the part before "-emu", "-probe"
or "-edit"). A section's state is its newest Emulate screen or edit: Human (100% Human headline), or what is left.
"""
import argparse, glob, json, pathlib, re

H = pathlib.Path(__file__).resolve().parent.parent


def history():
    rows = {}
    for f in sorted(glob.glob(str(H / 'fix-*' / 'b*' / 'b*-results.json')), key=lambda p: int(re.search(r'/b(\d+)/', p).group(1))):
        b = re.search(r'/b(\d+)/', f).group(1) + 'g'
        for name, v in json.load(open(f, encoding='utf-8')).items():
            key = re.split(r'-(?:emu|probe|edit|sec)', name)[0]
            rows.setdefault(key, []).append((b, name, v[0], v[1], v[2], 'https://www.pangram.com/history' + v[5]))
    return rows


def human(head):
    return head.startswith('Human')


def table(rows):
    out = ['| section | state | newest check | before |', '|---|---|---|---|']
    for key in sorted(rows, key=lambda k: int(re.match(r'HG(\d+)', k).group(1)) if re.match(r'HG(\d+)', k) else 999):
        h = rows[key]
        b, name, head, ai, words, link = h[-1]
        state = 'Human' if human(head) else ('Mixed (AI %.2f)' % ai if ai < 0.9 else 'AI (%.2f)' % ai)
        if len(h) == 1 and human(head):
            state = 'Human as published'
        before = '; '.join('%s %s %.2f' % (x[0], 'H' if human(x[2]) else 'AI', x[3]) for x in h[:-1])
        out.append('| %s | %s | [%s %s](%s) | %s |' % (key, state, b, name, link, before or '-'))
    return '\n'.join(out)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--out')
    a = ap.parse_args()
    t = table(history())
    if a.out:
        pathlib.Path(a.out).write_text(t + '\n', encoding='utf-8')
    print(t)
