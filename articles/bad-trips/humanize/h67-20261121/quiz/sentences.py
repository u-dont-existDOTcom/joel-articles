"""sentences.py - split a text into sentences and say which of a draft's sentences his version kept (code, so the quiz's
key doesn't depend on a reader): a draft sentence is kept when some sentence of his matches it at 0.9 or more, word for
word (difflib over lowercased words); otherwise he changed or cut it."""
import difflib, re


def split(text):
    text = re.sub(r'\s+', ' ', text.replace('\n', ' ')).strip()
    parts = re.split(r'(?<=[.!?:])["”)]?\s+(?=["“(]?[A-Z0-9*\[])', text)
    return [p.strip() for p in parts if p.strip()]


def words(t):
    return re.findall(r"[a-z0-9']+", t.lower().replace('’', "'"))


def kept(draft, his):
    hs = [words(s) for s in split(his)]
    out = []
    for s in split(draft):
        w = words(s)
        best = max((difflib.SequenceMatcher(None, w, h, autojunk=False).ratio() for h in hs), default=0)
        out.append((s, best >= 0.9, round(best, 2)))
    return out
