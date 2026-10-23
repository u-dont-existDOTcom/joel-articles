#!/usr/bin/env python3
"""part_forecast.py - which parts of a whole-article check will read AI, forecast before the check and scored after it.

Joel, 2026-10-23 14:14 UTC, after recheck A: "and your predictions about like 35% chance it comes back fully human... i
was thinking you should predict which part comes back as AI?" A whole-article prediction (pangram_ledger.py predict) gives
one chance for the whole text; this gives each part its own, so the forecast says where the red will be and can be scored
part by part.

The parts of a forecast:
- each changed stretch since the last check (given in CHANGED.json, with my chance that it reads red and why);
- each window of the last check that read Human at Low (or Medium) confidence and whose text is still in the new text
  unchanged: that is where new red turned up (Nibbāna's second recheck, 2026-10-23: the one red paragraph had read Human,
  Low, in both checks before; recheck A's troubleshooting questions had read Human, Medium); its default chance is
  LOW_CHANCE or MEDIUM_CHANCE, and CHANGED.json can override it by giving the same text;
- each changed part's neighbours: the paragraph before it and after it, and the rest of the paragraph it sits in, each at
  NEIGHBOUR_CHANCE unless CHANGED.json gives the same text its own chance (gate E244: red spreads to neighbours; E249,
  2026-10-23 18:13 UTC: the rule ran by hand in the guide's forecast and not in Nibbāna's, where the High red was the
  paragraph after one of Joel's rewrites, so the tool adds them; --no-neighbours leaves them out);
- the rest, as one part: my chance that any red turns up outside the parts above.

  python3 tools/humanization/part_forecast.py make --last LAST_RESULT.json --text NEW_TEXT.txt --changed CHANGED.json \\
          --out FORECAST.json [--medium] [--rest 0.3] [--neighbour-chance 0.05 | --no-neighbours]
  python3 tools/humanization/part_forecast.py score FORECAST.json RESULT.json --out SCORE.md

CHANGED.json is [{"name": ..., "text": an exact stretch of NEW_TEXT.txt, "chance_red": 0.3, "why": ...}, ...]. A part's
text must occur in the checked text exactly once (it is located by plain substring, so give enough of it). Scoring: a
part reads red when any AI window overlaps it; its call is red when its chance is at least 0.5; a hit is a call that
matches the reading. The page also gives the Brier score of the chances and every red window no part covered.
"""
import argparse, json, pathlib, sys

# Measured on 2026-10-23 over three pairs of consecutive whole-article checks (Nibbāna 20 Oct to recheck 1 to recheck 2,
# the guide's part A 22 Oct to 23 Oct): of the unchanged windows that had read Human, 2 of 58 Low ones turned red (one
# paragraph), 1 of 120 Medium ones and 2 of 168 High ones. So a light green window is a likelier place for new red
# than a dark one, but rarely red. The defaults count the two Low windows of that one paragraph once (1 in 58) and the
# Medium rate as it is; a forecast raises one when it has a reason (a window next to changed text, say).
LOW_CHANCE = 0.02
MEDIUM_CHANCE = 0.01
# A changed part's neighbours, by default. Measured by 2026-10-23 18:13 UTC: of the neighbours the forecasts named (the
# guide's recheck A3 and A4 by hand, Nibbāna's recheck 4 counted afterwards), about 3 in 80 read red; a forecast raises one
# when it has a reason (a neighbour of a big rewrite, a paragraph whose window will change).
NEIGHBOUR_CHANCE = 0.05


def load(p):
    return json.loads(pathlib.Path(p).read_text(encoding='utf-8'))


def is_ai(w):
    return str(w.get('label', '')).startswith('AI')


def risks(last, text, medium=False):
    """The windows of LAST (a RESULT file) that read Human at Low (or Medium) confidence and whose text occurs once in TEXT."""
    out, t = [], last['text']
    for i, w in enumerate(last['windows']):
        if is_ai(w) or w.get('confidence') not in (('Low', 'Medium') if medium else ('Low',)):
            continue
        s = t[w['start_index']:w['end_index']].strip()
        if len(s) < 12 or text.count(s) != 1:
            continue
        out.append({'name': 'last check\'s window %d (Human, %s, %d words)' % (i, w['confidence'], w['word_count']),
                    'text': s, 'chance_red': LOW_CHANCE if w['confidence'] == 'Low' else MEDIUM_CHANCE,
                    'why': 'read Human, %s, last time; red turns up where the last check was light green' % w['confidence'],
                    'kind': 'risk'})
    return out


def _span(text, s, e):
    """S:E of TEXT without its surrounding white space."""
    while s < e and text[s].isspace():
        s += 1
    while e > s and text[e - 1].isspace():
        e -= 1
    return s, e


def neighbours(text, changed, chance=NEIGHBOUR_CHANCE):
    """The paragraph before and after each changed part, and the rest of the paragraph it sits in (paragraphs are TEXT's
    lines), each one part unless it overlaps a changed part or is too short to place."""
    spans = []
    for c in changed:
        i = text.find(c['text'])
        spans.append((i, i + len(c['text'])))
    out, seen = [], set()
    for c, (a, b) in zip(changed, spans):
        ps = text.rfind('\n', 0, a) + 1
        pe = text.find('\n', b)
        pe = len(text) if pe < 0 else pe
        cands = [('the rest of its paragraph, before it', ps, a), ('the rest of its paragraph, after it', b, pe)]
        if ps > 0:
            cands.append(('the paragraph before it', text.rfind('\n', 0, ps - 1) + 1, ps - 1))
        if pe < len(text):
            qe = text.find('\n', pe + 1)
            cands.append(('the paragraph after it', pe + 1, len(text) if qe < 0 else qe))
        for label, s, e in cands:
            s, e = _span(text, s, e)
            seg = text[s:e]
            if len(seg) < 12 or (s, e) in seen or text.count(seg) != 1:
                continue
            if any(x < e and y > s for x, y in spans):
                continue
            seen.add((s, e))
            out.append({'name': 'neighbour of %s: %s' % (c['name'], label), 'text': seg, 'chance_red': chance,
                        'why': 'next to changed text; red spreads to neighbours (gate E244, E249)', 'kind': 'neighbour'})
    return out


def make(last, text, changed, medium=False, rest=0.3, neighbour_chance=NEIGHBOUR_CHANCE, with_neighbours=True):
    for c in changed:
        if text.count(c['text']) != 1:
            raise SystemExit('a changed part must occur exactly once in the new text: %r' % c['text'][:80])
        c.setdefault('kind', 'changed')
    parts = list(changed)
    if with_neighbours:
        parts += neighbours(text, changed, neighbour_chance)
    taken = [(text.find(p['text']), text.find(p['text']) + len(p['text'])) for p in parts]
    for r in risks(last, text, medium):
        i = text.find(r['text'])
        if any(x < i + len(r['text']) and y > i for x, y in taken):
            continue
        parts.append(r)
    return {'parts': parts, 'rest': {'chance_red': rest, 'why': 'any red outside the parts above'}}


def locate(text, part):
    i = text.find(part['text'])
    if i < 0 or text.find(part['text'], i + 1) >= 0:
        return None
    return i, i + len(part['text'])


def score(fc, res):
    text, ws = res['text'], res['windows']
    rows, covered, brier = [], set(), []
    for p in fc['parts']:
        span = locate(text, p)
        if span is None:
            rows.append((p, 'not found', None))
            continue
        a, b = span
        over = [k for k, w in enumerate(ws) if w['start_index'] < b and w['end_index'] > a]
        red = [k for k in over if is_ai(ws[k])]
        covered.update(red)
        reading = 'red' if red else ('dark' if all(ws[k]['confidence'] == 'High' for k in over) else 'light')
        call = 'red' if p['chance_red'] >= 0.5 else 'green'
        hit = (call == 'red') == (reading == 'red')
        brier.append((p['chance_red'] - (1.0 if reading == 'red' else 0.0)) ** 2)
        rows.append((p, reading, hit))
    loose = [k for k, w in enumerate(ws) if is_ai(w) and k not in covered]
    rest_red = bool(loose)
    brier.append((fc['rest']['chance_red'] - (1.0 if rest_red else 0.0)) ** 2)
    return rows, loose, rest_red, sum(brier) / len(brier)


def page(fc, res, link=None):
    rows, loose, rest_red, b = score(fc, res)
    hits = sum(1 for _p, _r, h in rows if h)
    n = sum(1 for _p, _r, h in rows if h is not None)
    out = ['# Part forecast scored', '', 'Result: %s, %s, %.1f%% AI%s.' % (res.get('headline'), res.get('version'),
                                                                        100 * (res.get('fraction_ai') or 0),
                                                                        ' ([its page](%s))' % link if link else ''),
           '', '%d of %d parts called right; the rest (%s) read %s; Brier score %.3f (0 is perfect, 0.25 is a coin).' % (
               hits, n, 'chance of red %.2f' % fc['rest']['chance_red'], 'red' if rest_red else 'green', b), '',
           '| part | chance of red | call | reading | hit |', '|---|---|---|---|---|']
    for p, reading, hit in rows:
        call = 'red' if p['chance_red'] >= 0.5 else 'green'
        out.append('| %s: "%s" | %.2f | %s | %s | %s |' % (p['name'], p['text'][:70].replace('|', '/').replace('\n', ' '),
                                                         p['chance_red'], call, reading,
                                                         '' if hit is None else ('hit' if hit else '**miss**')))
    if loose:
        out += ['', 'Red that no part covered (each one a miss of the rest\'s forecast):', '']
        for k in loose:
            w = res['windows'][k]
            out.append('- window %d, %s, %d words: "%s"' % (k, w['confidence'], w['word_count'],
                                                           res['text'][w['start_index']:w['end_index']].strip()[:160]))
    return '\n'.join(out) + '\n'


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = ap.add_subparsers(dest='cmd', required=True)
    m = sub.add_parser('make')
    m.add_argument('--last', required=True); m.add_argument('--text', required=True); m.add_argument('--changed', required=True)
    m.add_argument('--out', required=True); m.add_argument('--medium', action='store_true')
    m.add_argument('--rest', type=float, default=0.3)
    m.add_argument('--neighbour-chance', type=float, default=NEIGHBOUR_CHANCE)
    m.add_argument('--no-neighbours', action='store_true')
    s = sub.add_parser('score')
    s.add_argument('forecast'); s.add_argument('result'); s.add_argument('--out', required=True); s.add_argument('--link')
    a = ap.parse_args(argv)
    if a.cmd == 'make':
        fc = make(load(a.last), pathlib.Path(a.text).read_text(encoding='utf-8'), load(a.changed), a.medium, a.rest,
                  a.neighbour_chance, not a.no_neighbours)
        pathlib.Path(a.out).write_text(json.dumps(fc, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print('%s: %d parts (%d changed, %d neighbours, %d from the last check\'s light green)' % (
            a.out, len(fc['parts']), sum(p['kind'] == 'changed' for p in fc['parts']),
            sum(p['kind'] == 'neighbour' for p in fc['parts']), sum(p['kind'] == 'risk' for p in fc['parts'])))
        return 0
    fc, res = load(a.forecast), load(a.result)
    pathlib.Path(a.out).write_text(page(fc, res, a.link or res.get('link')), encoding='utf-8')
    rows, loose, rest_red, b = score(fc, res)
    print('%s: %d of %d parts right, %d red windows outside them, Brier %.3f' % (
        a.out, sum(1 for r in rows if r[2]), sum(1 for r in rows if r[2] is not None), len(loose), b))
    return 0


if __name__ == '__main__':
    sys.exit(main())
