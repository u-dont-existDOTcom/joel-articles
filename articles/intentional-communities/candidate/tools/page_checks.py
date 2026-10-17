"""page_checks.py - for a section page, the Pangram check that read each paragraph alone (2026-10-17).

Joel's rule (2026-10-01): every paragraph passes alone. A page shows, beside each paragraph, the check of its exact text
alone, or with its neighbor when it is under 50 words (Pangram's minimum, by spaces), found by exact text in the batch
folders' drafts.json and results files. Results come in two shapes: the full reader's dict (headline, link, ...) and the
compact list [headline, ai, words, windows, time, link tail, flagged]."""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fix-20261014'))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[4] / 'tools' / 'humanization'))
from ptext import plain  # noqa: E402
import paragraphs_alone  # noqa: E402


def load(dirs):
    seen = {}
    for d in dirs:
        d = pathlib.Path(d)
        drafts = json.loads((d / 'drafts.json').read_text(encoding='utf-8'))
        for f in sorted(d.glob('*-results.json')):
            for k, r in json.loads(f.read_text(encoding='utf-8')).items():
                if k not in drafts:
                    continue
                text = drafts[k]['text'] if isinstance(drafts[k], dict) else drafts[k]
                if isinstance(r, dict):
                    rec = (r['headline'], r.get('avg_ai_likelihood', r.get('ai')), r['link'])
                else:
                    rec = (r[0], r[1], 'https://www.pangram.com/history' + r[5])
                seen.setdefault(text, []).append((d.name.lstrip('b') + 'g', k) + rec)
    return seen


def alone(md, dirs):
    """[(paragraph, [(batch, key, headline, ai, link, with_neighbor)])] for each paragraph of md, newest batch first."""
    paras = paragraphs_alone.paragraphs(md)
    seen = load(dirs)
    out = []
    for i, (head, p) in enumerate(paras):
        t = plain(p)
        tries = [(t, '')]
        if len(t.split()) < 50:
            same = lambda j: 0 <= j < len(paras) and paras[j][0] == head
            tries = ([(plain(paras[i - 1][1]) + '\n\n' + t, 'with the paragraph before')] if same(i - 1) else []) + \
                    ([(t + '\n\n' + plain(paras[i + 1][1]), 'with the paragraph after')] if same(i + 1) else [])
        got = [r + (w,) for x, w in tries for r in seen.get(x, [])]
        got.sort(key=lambda r: r[0], reverse=True)
        out.append((p, got))
    return out


def note(r):
    batch, key, headline, ai, link, w = r
    how = ('%s, %s (this one is under 50 words, Pangram\'s minimum)' % (batch, w)) if w else '%s, alone' % batch
    return '%s: %s (AI likelihood %.2f, %s) %s' % (how, headline.replace(' Written', ''), float(ai or 0), key, link)
