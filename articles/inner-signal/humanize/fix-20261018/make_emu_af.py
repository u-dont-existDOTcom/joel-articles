"""emu-af, emu-ag (2026-10-18): HG17's listening script (B17-B31) in seven small windows, two samples each.

Three samples of the whole script as one window (emu-x, emu-ac, emu-ad) each lost 11 to 26 of its steps and details
("give each number its own moment", "leave a little space after the words", "without preparing an answer"): Emulate
compresses a long script. A causally different try: windows of two or three blocks (54 to 78 words), so there is little to
compress, and the better of two samples is chosen per window by the second reader. Input: my meaning-fixed text
(rev-g/HG17.fixed.json, the units the triage's resample points at). Run from fix-20261018/: python3 make_emu_af.py
"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_emu_ac as E  # noqa: E402

g444 = json.loads((HERE / 'b444' / 'GATE.json').read_text(encoding='utf-8'))
FIX = HERE / g444['HG17-fix']['reviews']
WINDOWS = [range(17, 18), range(18, 20), range(20, 22), range(22, 24), range(24, 26), range(26, 28), range(28, 32)]

if __name__ == '__main__':
    runs = []
    for n, w in enumerate(WINDOWS, 1):
        text, rec = E.window('HG17', FIX, w)
        if n > 1:  # the heading before B17 goes only with the first window
            rec['sent'] = [b for b in rec['sent'] if b >= w[0]]
            rec['headings'] = [b for b in rec['headings'] if b >= w[0]]
            text = '\n\n'.join(p for u in json.loads(FIX.read_text(encoding='utf-8'))['units'] if u['blocks'][0] in w for p in u['paras'])
            rec['words'] = len(text.split())
        runs.append(('HG17-sw%d' % n, text, rec))
        print(n, rec['sent'], rec['words'])
    E.write('emu-af', runs, [])
    E.write('emu-ag', runs, [])
