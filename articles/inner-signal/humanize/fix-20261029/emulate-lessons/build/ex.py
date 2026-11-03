"""Exact-text helpers: every quote is cut from a file, never typed, so it stays exact."""
import json, pathlib, functools
H = pathlib.Path(__file__).resolve().parents[3]  # build -> emulate-lessons -> fix-20261029 -> humanize
REL = 'articles/inner-signal/humanize/'

@functools.lru_cache(None)
def raw(f):
    return (H / f).read_text(encoding='utf-8')

def jget(f, path):
    d = json.loads(raw(f))
    for k in path.split('/'):
        d = d[int(k)] if isinstance(d, list) else d[k]
    return d

def cut(text, start, end=None):
    """the stretch of text from the first occurrence of start to the end of the first end after it"""
    a = text.find(start)
    if a < 0:
        raise ValueError('start not found: %r' % start[:60])
    if end is None:
        return start
    b = text.find(end, a)
    if b < 0:
        raise ValueError('end not found: %r' % end[:60])
    return text[a:b + len(end)]

def T(f, start, end=None):
    return {'file': REL + f, 'text': cut(raw(f), start, end)}

def J(f, path, start=None, end=None):
    v = jget(f, path)
    if start is not None:
        v = cut(v, start, end)
    return {'file': REL + f, 'text': v, 'key': path}

def check(file_rel, text):
    f = file_rel.replace(REL, '')
    r = raw(f)
    if text in r:
        return True
    if f.endswith('.json'):
        def walk(x):
            if isinstance(x, str):
                yield x
            elif isinstance(x, dict):
                for v in x.values(): yield from walk(v)
            elif isinstance(x, list):
                for v in x: yield from walk(v)
        return any(text in s for s in walk(json.loads(r)))
    return False
