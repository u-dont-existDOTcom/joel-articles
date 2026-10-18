"""faithful.py - the meaning review of Emulate's stretches against the published guide, and putting its fixes in
(2026-10-18).

Emulate's text reads Human, but it drops and bends points (the first sections, 430g: invented FTC and OECD quotations,
"earlier-life events" turned into "past life events", the inner child turned into "her", "meet the difficulty rather than
escalating the intensity" turned into its opposite). One reviewer reads a section's changed stretches against the
published blocks and gives, per stretch, OK or the problems with the smallest fix, in the published words where it can;
the fixes go in mechanically (each "replace" must be found exactly once in its stretch), and a second reader checks the
fixed stretches.

  python3 tools/faithful.py prompt UNITS.json OUT.txt        the reviewer's prompt (UNITS.json: assemble.units() for a key)
  python3 tools/faithful.py apply UNITS.json REVIEW.json OUT.json   the fixes put in; reports any that don't fit
  python3 tools/faithful.py verify UNITS.json OUT.txt        the second reader's prompt, for the fixed units

A stretch is named by its first published block: "block": 5 for the stretch that replaces B5 (to B9).
"""
import argparse, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
sys.path.insert(0, str(HERE))
import assemble as A  # noqa: E402

ABOUT = ('a long self-hypnosis guide by Joel, published on his Substack. It teaches gathering attention, listening to the '
         'subconscious as an ecology of parts (the inner child, protectors or "guards", the body, intuition), three adult '
         'functions he calls the Nurturer, the Protector and the Leader/Guru, Higher Self, "borrowed adulthood", inductions '
         'and a complete return, influence literacy ("de-hypnosis": noticing and resisting other people\'s influence), and '
         'safety limits (when to stop, when to get help). Its quoted lines are scripts the reader says or thinks.')

REVIEW = """You are checking a rewrite of one section of {about}

The PUBLISHED section is the author's text, its blocks numbered. In the REWRITE, some stretches were replaced by a
humanizer's paraphrase, which reads more like a person wrote it; that loose, casual voice is wanted. Each CHANGED
stretch says which published blocks it replaces. Your job is only the meaning: a stretch must say everything its
published blocks say, the same way round, and nothing they don't. Don't polish the rewrite's style, don't make it more
formal, and don't fix what isn't a meaning problem: a casual phrase, a long sentence, "etc.", a missing full stop,
British spelling, a list run into a sentence and a different order of the same points are all fine.

For each CHANGED stretch, go through every point of its published blocks in your head (don't write them out): each
claim, instruction, condition, caution, limit, example, name, number, title, source and quoted script line. Then check
the stretch against them. Report a problem only when a reader of the rewrite would come away with a different understanding than a
reader of the published blocks:
- LOST: a point is missing (a condition, a caution, an item of a list that matters, a limit, a script line).
- SHIFT: a point is there but changed: stronger or weaker, a different condition or subject, a safety instruction
  softened, hardened or turned round, a script line with a different meaning, "never" for "not automatically".
- INVENTED: something the published blocks don't say: a new claim, fact, example, story detail, a gender or a person that
  isn't there, words in quotation marks presented as a quotation that the published blocks don't quote.
- WRONG: a factual slip: a name, number, date, title or source changed; "past life" for "earlier life"; a study's
  finding changed; "ways to influence others" for resisting influence.
- UNCLEAR: a cold reader couldn't follow it (a broken sentence, a script that lost its quotation marks so it reads as
  narration, a pronoun with nothing to point to).

For every problem give the smallest fix: replace an exact stretch of the REWRITE (copy it character for character, quotes
and dashes as they are) with new words. Use the published blocks' own words for what was lost or changed, fitted into the
rewrite's sentence; change as few words as you can; keep the rewrite's voice. A fix must not add anything the published
blocks don't say. If a stretch is past fixing, give "redo": true and no fixes.

Return only JSON, one object per CHANGED stretch, in a JSON array:
[{{"block": 3, "verdict": "OK"}},
 {{"block": 4, "verdict": "FIX", "problems": [{{"type": "LOST", "what": "the condition 'when that is useful'",
   "replace": "spend a bit more time with it", "with": "spend a bit more time with it when that is useful"}}]}}]

PUBLISHED section:
{published}

REWRITE:
{rewrite}
"""

VERIFY = """Below is one section of {about}

For each CHANGED stretch, compare it with the PUBLISHED blocks it replaces. Answer with one line per stretch: "B<n>: OK"
(n = its first block) when a reader of it would understand everything those published blocks say and nothing more, or
"B<n>: <LOST|SHIFT|INVENTED|WRONG|UNCLEAR> <what, in a few words>" for each remaining problem (one line each). Style
doesn't matter, only meaning. Then one last line: "REPEATS: 0" if no point is made twice in the REWRITE where the
PUBLISHED section makes it once, or "REPEATS: <n>" followed by one line per repeat ("R: <the point>, in B<a> and B<b>").
Nothing else.

PUBLISHED section:
{published}

REWRITE:
{rewrite}
"""


def pub_blocks(key):
    return [p for _, p, _ in A.kb()[key]]


def render(key, us):
    pub = pub_blocks(key)
    published = '\n\n'.join('[B%d] %s' % (i, b) for i, b in enumerate(pub))
    parts = []
    for u in us:
        if u['kind'] == 'emulate':
            rng = 'B%d' % u['blocks'][0] + ('-B%d' % u['blocks'][-1] if len(u['blocks']) > 1 else '')
            parts.append('[CHANGED, replaces %s]\n%s' % (rng, '\n\n'.join(u['paras'])))
        else:
            parts.append('[B%d, as published] %s' % (u['blocks'][0], u['paras'][0]))
    return published, '\n\n'.join(parts)


def prompt(units_path, out, tmpl=REVIEW):
    d = json.loads(pathlib.Path(units_path).read_text(encoding='utf-8'))
    published, rewrite = render(d['key'], d['units'])
    pathlib.Path(out).write_text(tmpl.format(about=ABOUT, published=published, rewrite=rewrite), encoding='utf-8')
    print('%s: %d stretches changed -> %s' % (d['key'], sum(u['kind'] == 'emulate' for u in d['units']), out))


CHUNK_NOTE = ("\n\nThis is PART {n} of {m} of the section: only the stretches below are yours; the published blocks shown are the "
              "ones they replace, with the headings around them. Go through the points in your head; don't write them out. "
              "Return only the JSON array, nothing before or after it.\n")


def chunks(units_path, out_prefix, size=12, tmpl=REVIEW):
    """The review prompt cut into parts of SIZE changed stretches (2026-10-18: a whole long section in one prompt made the
    review agents run out of output); each part shows the published blocks its stretches replace and the headings
    between them. Writes OUT_PREFIX.partN.txt."""
    d = json.loads(pathlib.Path(units_path).read_text(encoding='utf-8'))
    pub = pub_blocks(d['key'])
    emu = [i for i, u in enumerate(d['units']) if u['kind'] == 'emulate']
    groups = [emu[i:i + size] for i in range(0, len(emu), size)]
    for n, g in enumerate(groups, 1):
        lo, hi = g[0], g[-1]
        us = d['units'][lo:hi + 1]
        blocks = sorted({b for u in us for b in u['blocks']})
        published = '\n\n'.join('[B%d] %s' % (b, pub[b]) for b in blocks)
        parts = []
        for u in us:
            if u['kind'] == 'emulate':
                rng = 'B%d' % u['blocks'][0] + ('-B%d' % u['blocks'][-1] if len(u['blocks']) > 1 else '')
                parts.append('[CHANGED, replaces %s]\n%s' % (rng, '\n\n'.join(u['paras'])))
            else:
                parts.append('[B%d, as published] %s' % (u['blocks'][0], u['paras'][0]))
        text = tmpl.format(about=ABOUT, published=published, rewrite='\n\n'.join(parts)) + CHUNK_NOTE.format(n=n, m=len(groups))
        f = '%s.part%d.txt' % (out_prefix, n)
        pathlib.Path(f).write_text(text, encoding='utf-8')
        print('%s part %d/%d: %d stretches, B%d-B%d -> %s' % (d['key'], n, len(groups), len(g), blocks[0], blocks[-1], f))
    return len(groups)


def straight(t):
    return t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')


def merge(review, patch, out=None):
    """Add a later round's fixes (PATCH: [{"block": n, "problems": [...]}, ...], each problem with "round" and "from") to a
    review, after the earlier rounds' fixes of the same stretch, so they apply to the text those left; a problem already
    there is not added twice. (2026-10-18: the second reader's and the adjudication's fixes.)"""
    rv = json.loads(pathlib.Path(review).read_text(encoding='utf-8'))
    by = {r['block']: r for r in rv}
    added = 0
    for pr in json.loads(pathlib.Path(patch).read_text(encoding='utf-8')):
        r = by.get(pr['block'])
        if r is None:
            r = {'block': pr['block'], 'verdict': 'FIX', 'problems': []}
            rv.append(r); by[pr['block']] = r
        r.setdefault('problems', [])
        for p in pr.get('problems', []):
            if any(q.get('replace') == p['replace'] and q.get('with') == p['with'] for q in r['problems']):
                continue
            r['problems'].append(p); r['verdict'] = 'FIX'; added += 1
        for k in ('note', 'links'):
            if pr.get(k):
                r[k] = pr[k]
    pathlib.Path(out or review).write_text(json.dumps(rv, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('%s: %d fixes added from %s' % (review, added, patch))


def apply(units_path, review, out):
    d = json.loads(pathlib.Path(units_path).read_text(encoding='utf-8'))
    txt = pathlib.Path(review).read_text(encoding='utf-8')
    rv = json.loads(txt[txt.index('['): txt.rindex(']') + 1])
    by_first = {u['blocks'][0]: u for u in d['units'] if u['kind'] == 'emulate'}
    bad, done, redo = [], 0, []
    for r in rv:
        u = by_first.get(r['block'])
        if u is None:
            bad.append((r['block'], 'no such stretch', '', 0)); continue
        if r.get('redo'):
            redo.append(r['block']); u['redo'] = True
        if r.get('links'):
            u['links'] = r['links']
        for p in r.get('problems') or []:
            body = '\n\n'.join(u['paras'])
            n = body.count(p['replace'])
            if n != 1 and body.count(straight(p['replace'])) == 1:
                # Emulate keeps straight quotes in some runs: a fix written with curly ones takes the stretch's style
                p = dict(p, replace=straight(p['replace']), **{'with': straight(p['with'])})
                n = 1
            if n != 1:
                bad.append((r['block'], p['type'], p['replace'][:60], n)); continue
            body = body.replace(p['replace'], p['with'])
            u['paras'] = [x.strip() for x in re.split(r'\n\s*\n', body) if x.strip()]
            u.setdefault('fixes', []).append(p)
            done += 1
    for u in d['units']:   # every link the stretch carries must have its words in the fixed text
        for l in u.get('links') or []:
            if l['new'] not in '\n\n'.join(u['paras']):
                bad.append((u['blocks'][0], 'link anchor', l['new'][:60], 0))
        u['verdict'] = 'redo' if u.get('redo') else ('fixed' if u.get('fixes') else ('OK' if u['kind'] == 'emulate' else None))
    pathlib.Path(out).write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('%s: %d fixes in, %d did not fit, redo: %s -> %s' % (d['key'], done, len(bad), redo or 'none', out))
    for x in bad:
        print('  B%s %s %r found %d times' % x)
    return bad, redo


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cmd', choices=('prompt', 'apply', 'verify', 'chunks', 'merge'))
    ap.add_argument('args', nargs='+')
    a = ap.parse_args()
    if a.cmd == 'prompt':
        prompt(a.args[0], a.args[1])
    elif a.cmd == 'verify':
        prompt(a.args[0], a.args[1], tmpl=VERIFY)
    elif a.cmd == 'merge':
        merge(a.args[0], a.args[1])
    elif a.cmd == 'chunks':
        chunks(a.args[0], a.args[1], int(a.args[2]) if len(a.args) > 2 else 12)
    else:
        apply(a.args[0], a.args[1], a.args[2])


if __name__ == '__main__':
    main()
