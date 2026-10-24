"""Every difference between the eighth recheck's text (its draft, which read 100% Human) and the two texts Joel's GPT made
from it (2026-10-24): Nibbana_After_Approved_Cuts.txt (his N6 picks applied, plus edits) and Nibbana_Updated_Draft.txt
(then ten style edits). GPT's files are the draft page's text as a browser copies it, so headings, captions, the page
header and the verse's line breaks are lines of their own there; a line of ours matches when it is a GPT line, or several
consecutive GPT lines joined without their breaks. Writes DIFF.json beside this file.

  python3 articles/nibbana/humanize/fix-20261024/gpt/diff_gpt.py   (from the repo root)
"""
import difflib, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
OURS = HERE.parents[1] / 'fix-20261023' / 'recheck8' / 'DRAFT-TEXT.txt'
norm = lambda s: re.sub(r'\s+', ' ', s.replace('‍', '').replace('️', '')).strip()
squash = lambda s: re.sub(r'\s+', '', s.replace('‍', '').replace('️', ''))


def gpt_lines(name):
    return [l for l in (HERE / name).read_text(encoding='utf-8').split('\n') if l.strip()]


def match(ours, gl):
    """For each of our lines: ('same', j, k) when GPT lines j..k-1 joined are the same text, else None."""
    gsq = [squash(x) for x in gl]
    out, j = [], 0
    for o in ours:
        so, hit = squash(o), None
        for start in range(j, min(len(gl), j + 40)):
            acc = ''
            for k in range(start, min(len(gl), start + 12)):
                acc += gsq[k]
                if acc == so:
                    hit = (start, k + 1)
                    break
                if not so.startswith(acc):
                    break
            if hit:
                break
        if hit:
            j = hit[1]
        out.append(hit)
    return out


def main():
    ours = [l for l in OURS.read_text(encoding='utf-8').split('\n')]
    res = {}
    for name in ('Nibbana_After_Approved_Cuts.txt', 'Nibbana_Updated_Draft.txt'):
        gl = gpt_lines(name)
        m = match(ours, gl)
        used = set()
        for h in m:
            if h:
                used.update(range(*h))
        changed = []
        for i, (o, h) in enumerate(zip(ours, m)):
            if h:
                continue
            # the nearest unused GPT line between the neighbours' matches
            lo = next((m[x][1] for x in range(i - 1, -1, -1) if m[x]), 0)
            hi = next((m[x][0] for x in range(i + 1, len(ours)) if m[x]), len(gl))
            cands = [k for k in range(lo, hi) if k not in used]
            best = max(cands, key=lambda k: difflib.SequenceMatcher(None, norm(o), norm(gl[k])).ratio(), default=None)
            r = difflib.SequenceMatcher(None, norm(o), norm(gl[best])).ratio() if best is not None else 0
            changed.append({'line': i, 'ours': o, 'gpt': gl[best] if best is not None and r > 0.3 else None,
                            'ratio': round(r, 3), 'gpt_line': best})
            if best is not None and r > 0.3:
                used.add(best)
        extra = [gl[k] for k in range(len(gl)) if k not in used]
        res[name] = {'changed': changed, 'gpt_lines_not_ours': extra}
    (HERE / 'DIFF.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for name, r in res.items():
        print(name, ':', len(r['changed']), 'of our lines changed;', len(r['gpt_lines_not_ours']), 'GPT lines not ours')


if __name__ == '__main__':
    main()
