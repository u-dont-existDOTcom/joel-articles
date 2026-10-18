"""para_chance.py - my chance that a paragraph check reads 100% Human, from how much of it isn't Emulate's (2026-10-18).

Until 453g a paragraph check's chance came from its length (0.70 to 0.79, the community lane's rate). The hypnosis
guide's own 235 paragraph checks (442g to 453g) say length isn't what matters; how much of the text Emulate wrote is:

  share of the checked text's words not in an Emulate output   checks   read Human   chance used
  under 5% (Emulate's words, or a word or two fixed)                141        99%          0.97
  5% to 15%                                                          45        93%          0.90
  15% to 30%                                                         33        70%          0.70
  30% or more (my or the published wording)                          16        81%          0.75

Brier score on those checks: 0.104 with the length chances, 0.057 with these (fitted on the same checks, coarse bins).
A word counts as Emulate's when it is in the matching blocks of the closest paragraph of any fix-*/emu-*/*.out.txt.

  python3 tools/para_chance.py TEXT_FILE     the share and the chance for one text
"""
import difflib, pathlib, re, sys

H = pathlib.Path(__file__).resolve().parent.parent
BINS = [(0.05, 0.97), (0.15, 0.90), (0.30, 0.70), (1.01, 0.75)]
_emu = None


def emulate_paragraphs():
    global _emu
    if _emu is None:
        _emu = []
        for f in sorted(H.glob('fix-*/emu-*/*.out.txt')):
            for p in re.split(r'\n\s*\n', f.read_text(encoding='utf-8')):
                if p.split():
                    _emu.append(p.split())
        _emu = (_emu, {' '.join(w) for w in _emu})
    return _emu


def changed_share(text):
    """The share of the text's words that no Emulate paragraph has in the same place (0.0: all Emulate's)."""
    emu, emuset = emulate_paragraphs()
    tot = ch = 0
    for p in [p for p in re.split(r'\n\s*\n', text) if p.strip()]:
        w = p.split()
        tot += len(w)
        if ' '.join(w) in emuset:
            continue
        best, bm = 0, None
        for e in emu:
            sm = difflib.SequenceMatcher(None, w, e, autojunk=False)
            if sm.real_quick_ratio() <= best or sm.quick_ratio() <= best:
                continue
            r = sm.ratio()
            if r > best:
                best, bm = r, sm
        if best < 0.5:
            ch += len(w)
        else:
            ch += len(w) - sum(b.size for b in bm.get_matching_blocks())
    return ch / max(tot, 1)


def chance(text):
    """(chance of a 100% Human result, why) for a paragraph check's text."""
    s = changed_share(text)
    c = next(c for hi, c in BINS if s < hi)
    return c, '%d%% of its words not Emulate\'s (paragraph checks 442g-453g: under 5%% 99%% Human, 5-15%% 93%%, 15-30%% 70%%, over 30%% 81%%)' % round(100 * s)


if __name__ == '__main__':
    t = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8')
    print('%.3f' % changed_share(t), chance(t))
