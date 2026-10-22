#!/usr/bin/env python3
"""pangram_ledger.py - one prediction ledger, budget counter and scorecard for every humanization lane (2026-10-20).

Joel, 2026-10-20 17:38 UTC: "can you make the scorecard and improvement work merged so that every humanization lane works on
that also, giving me its own scorecard (or brainstorm how to make this make more sense, i'm thinking individual article work
scorecards which should also feed into universal scorecard and optimization work?)". Until now the community lane kept
predictions in batch tables read by its own scorecard (which the hypnosis lane joined), and the Inner Child lane in one long
table; nothing counted tries. docs/PANGRAM-PRODUCTION-BUDGET-20261020.md asks every lane for an immutable prediction before
each call (scope, Human or AI, the tells behind it, the try number), the result after, every miss recorded with its cause,
a scorecard with rolling accuracy beside the always-AI and always-Human baselines and the boundary mix, and a tries count of
at most six per paragraph lineage, two per section and two per whole article. This tool does those things for any lane.

Each lane keeps one append-only file, `pangram-ledger.jsonl` in its folder (tools/humanization/pangram_lanes.json says where),
with one JSON object per line:
  {"type": "prediction", "id": ..., "lineage": "HG18-P3", "scope": "paragraph", "sha256": ..., "words": ..., "call": "Human",
   "chance": 0.8, "tells": [...], "human_tells": [...], "diagnosis": ..., "decides": ..., "try": 2, "detector": ...}
  {"type": "result", "prediction": ID, "verdict": "Human" | "AI" | "Mixed", "link": ..., "right": true, ...}
  {"type": "explain", "prediction": ID, "cause": ..., "note": ...}       (why a miss happened)
  {"type": "void", "prediction": ID, "reason": ...}                      (shown never to have been submitted)
Nothing is edited in place; a correction is a new line.

  python3 tools/humanization/pangram_ledger.py predict LEDGER --lineage L --scope paragraph --text FILE --call Human \\
      --chance 0.8 --tells "..." --human-tells "..." [--diagnosis "..."] [--decides "..."] [--key K] [--batch 467g]
  python3 tools/humanization/pangram_ledger.py result LEDGER --sha SHA --verdict Human --link URL [--ai-fraction F] [--shading S]
  python3 tools/humanization/pangram_ledger.py results LEDGER RESULTS.json      (a reader's {key: {headline, link, ...}})
  python3 tools/humanization/pangram_ledger.py explain LEDGER --sha SHA --cause CAUSE --note "..."
  python3 tools/humanization/pangram_ledger.py void LEDGER --sha SHA --reason "..."
  python3 tools/humanization/pangram_ledger.py status LEDGER [--lineage L]
  python3 tools/humanization/pangram_ledger.py check LEDGER ITEMS.json           (each text of a batch has its open prediction)
  python3 tools/humanization/pangram_ledger.py build [--lanes tools/humanization/pangram_lanes.json] [--universal OUT.md]

`predict` refuses (exit 2, with the rule) when: the call has no evidence (no tells and no human tells); the lineage has used
its tries (six for a paragraph, pair, heading or sentence; two for a section, stretch or whole article); a submission of the
lineage has no result yet (recover it from Pangram's History, or `void` it if it was never sent); an earlier try of the
lineage failed and no diagnosis is given; the last two results of the lineage were misses and neither is explained (stop and
ask Joel: "I can't find AI tells here, and here are the human tells I see, but it doesn't pass. Can you explain?"); or the
same text (same SHA-256) was already submitted in the lineage (read the cached result instead). A forecast is never a
reason to skip a check a rule requires, and the counter is the floor of the budget rule, not all of it: the rule's diagnosis
and stop conditions still need a person's judgment.

`build` writes, for each lane, `SCORECARD.md` beside its ledger, with --universal one page over every lane, and with --rows
one JSON row per scored call for a dashboard page. Each lane's older records (Pangram 4.0, before the ledger) are read through its "legacy" sources and shown apart
from the ledger's rows, never pooled with them.
"""
import argparse, datetime, hashlib, json, pathlib, re, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
LANES = REPO / 'tools' / 'humanization' / 'pangram_lanes.json'
CAPS = {'sentence': 6, 'heading': 6, 'paragraph': 6, 'pair': 6, 'section': 2, 'stretch': 2, 'article': 2}


def cap_for(scope, detector=None):
    """The tries a lineage may use: CAPS, except a whole article or a stretch of one checked through a temporary Substack
    post, which has no cap (Joel, 2026-10-21 17:56 UTC, question 7 of the hypnosis questions page, "b": "Let Substack
    checks go past two, each with its prediction written first and run only when its result decides something"; those
    checks cost no credits). None means no cap; such a prediction must say what its result decides."""
    if scope in ('article', 'stretch') and 'substack' in (detector or '').lower():
        return None
    return CAPS.get(scope, 0)


def cap_text(scope, detector=None):
    c = cap_for(scope, detector)
    return 'unlimited (Substack)' if c is None else str(c)
CALLS = ('Human', 'AI')


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def sha256(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def read(ledger):
    p = pathlib.Path(ledger)
    if not p.exists():
        return []
    out = []
    for n, line in enumerate(p.read_text(encoding='utf-8').splitlines(), start=1):
        if line.strip():
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise SystemExit('%s line %d is not JSON: %s' % (ledger, n, e))
    return out


def append(ledger, rec):
    p = pathlib.Path(ledger)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False, sort_keys=True) + '\n')


def state(recs):
    """Each prediction with what later lines say about it: its result, explanation, voiding."""
    preds = {}
    for r in recs:
        if r.get('type') == 'prediction':
            preds[r['id']] = dict(r, result=None, explain=None, void=None)
    for r in recs:
        t, pid = r.get('type'), r.get('prediction')
        if t in ('result', 'explain', 'void') and pid in preds:
            preds[pid][t] = r
    return preds


def lineage_view(preds, lineage):
    """The lineage's predictions in order, without the voided ones."""
    return [p for p in preds.values() if p.get('lineage') == lineage and not p['void']]


def is_miss(p):
    return bool(p['result']) and p['result'].get('right') is False


def refusals(recs, rec):
    """Why the budget rule (docs/PANGRAM-PRODUCTION-BUDGET-20261020.md) forbids this submission; empty means it may go."""
    out = []
    if rec['call'] not in CALLS:
        out.append('the call must be Human or AI, not %r' % rec['call'])
    if rec.get('chance') is not None and not 0 <= rec['chance'] <= 1:
        out.append('the chance must be between 0 and 1')
    elif rec.get('chance') is not None and ((rec['call'] == 'AI' and rec['chance'] > 0.5)
                                            or (rec['call'] == 'Human' and rec['chance'] < 0.5)):
        # 2026-10-22 (Inner Child lane, turn 94): 30 of that lane's AI calls had recorded the confidence in the call (AI at
        # 0.9) where the ledger means the chance of a 100% Human result (0.1), which inverted its Brier score and calibration.
        out.append('the chance is of a 100% Human result, not the confidence in the call: a Human call needs at least 0.5 '
                   'and an AI call at most 0.5 (got ' + str(rec['chance']) + ' for a ' + rec['call'] + ' call)')
    if not rec.get('tells') and not rec.get('human_tells'):
        out.append('no evidence: name the AI tells and the human tells in the actual words (the rule asks for both)')
    scope = rec['scope']
    if scope not in CAPS:
        out.append('scope must be one of %s' % ', '.join(sorted(CAPS)))
        return out
    line = lineage_view(state(recs), rec['lineage'])
    if any(p['sha256'] == rec['sha256'] for p in line):
        out.append('this exact text (same SHA-256) was already submitted in lineage %s: read its result from the ledger or '
                   "Pangram's History instead of paying again" % rec['lineage'])
    out += blocks(recs, rec['lineage'], scope, rec.get('detector'))
    if cap_for(scope, rec.get('detector')) is None and not (rec.get('decides') or '').strip():
        out.append('a Substack check past the usual two tries must say what its result decides (--decides; Joel, '
                   '2026-10-21, question 7 b: "run only when its result decides something")')
    done = [p for p in line if p['result']]
    if done and done[-1]['result'].get('verdict') != 'Human' and not (rec.get('diagnosis') or '').strip():
        out.append('the last try of lineage %s read %s: give the specific diagnosis this try tests (what changed, why it should '
                   'help, what counts as better)' % (rec['lineage'], done[-1]['result'].get('verdict')))
    return out


def blocks(recs, lineage, scope, detector=None):
    """What stops any further submission in the lineage, whatever the text: the cap, a submission with no result, two
    unexplained misses in a row. DETECTOR is the new prediction's (a Substack check of an article has no cap)."""
    out = []
    line = lineage_view(state(recs), lineage)
    pending = [p for p in line if not p['result']]
    if pending:
        out.append('try %d of lineage %s (%s) has no result: recover it from the History, or void it if it was never sent'
                   % (pending[0]['try'], lineage, pending[0].get('key') or pending[0]['sha256'][:12]))
    cap = cap_for(scope, detector if detector is not None else (line[-1].get('detector') if line else None))
    if cap is not None and len(line) >= cap:
        out.append('lineage %s has used its %d tries for a %s: stop and ask Joel (a new owner decision is needed)'
                   % (lineage, cap, scope))
    done = [p for p in line if p['result']]
    if len(done) >= 2 and all(is_miss(p) and not p['explain'] for p in done[-2:]):
        out.append('the last two predictions of lineage %s missed and neither is explained: stop and ask Joel ("I can\'t find '
                   'AI tells here, and here are the human tells I see, but it doesn\'t pass. Can you explain?")' % lineage)
    return out


def find(recs, sha=None, key=None, pid=None, open_only=False):
    preds = [p for p in state(recs).values() if not p['void']]
    if pid:
        preds = [p for p in preds if p['id'] == pid]
    if sha:
        preds = [p for p in preds if p['sha256'] == sha]
    if key:
        preds = [p for p in preds if p.get('key') == key]
    if open_only:
        preds = [p for p in preds if not p['result']]
    return preds[-1] if preds else None


def verdict_of(headline, windows=None, fraction_ai=None):
    """Human when Pangram's headline says Human (a 100% Human result), AI when every window is AI, Mixed otherwise."""
    h = (headline or '').lower()
    if h.startswith('human'):
        return 'Human'
    if fraction_ai is not None:
        return 'AI' if fraction_ai >= 0.999 else ('Human' if fraction_ai <= 0.0 else 'Mixed')
    labels = [str(w).split(',')[0].strip().lower() for w in (windows or [])]
    if labels and all(l.startswith('ai') for l in labels):
        return 'AI'
    return 'Mixed' if labels else ('AI' if h.startswith('ai') else 'Mixed')


def result_rec(p, verdict, link, extra):
    right = (p['call'] == 'Human') == (verdict == 'Human')
    rec = {'type': 'result', 'prediction': p['id'], 'at': extra.pop('at', None) or now(), 'sha256': p['sha256'],
           'verdict': verdict, 'link': link, 'right': right}
    rec.update({k: v for k, v in extra.items() if v is not None})
    return rec


# ---------- legacy records (before the ledger) ----------

def legacy_rows(src, lane):
    """Older records in a lane's own format, as rows: call, passed, right, chance, kind, batch, key."""
    path = REPO / src['path']
    if not path.exists():
        return []
    if src['kind'] == 'rows':
        data = json.loads(path.read_text(encoding='utf-8'))
        data = data['rows'] if isinstance(data, dict) and 'rows' in data else data
        out = []
        for r in data:
            if src.get('lane') and r.get('lane') != src['lane']:
                continue
            ch = r.get('chance')
            out.append(scored({'lane': lane, 'era': src.get('era', 'Pangram 4.0 (before the ledger)'), 'batch': r.get('batch'),
                               'key': r.get('text'), 'kind': r.get('kind') or 'unrecorded', 'call': r.get('mine'),
                               'chance': float(ch) if ch not in (None, '') else None, 'passed': bool(int(r.get('passed', 0)))},
                              bool(int(r.get('right', 0)))))
        return out
    if src['kind'] == 'table':  # | date | text | prediction | result | hit |
        out = []
        for line in path.read_text(encoding='utf-8').splitlines():
            if not line.startswith('| ') or line.startswith('| date') or re.match(r'^\|\s*-', line):
                continue
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if len(cells) < 5:
                continue
            date, text, pred, res, hit = cells[0], cells[1], cells[2], cells[3], cells[4]
            if not re.match(r'(hit|miss)', hit, re.I) or re.match(r'not (checked|scanned)', res, re.I):
                continue
            low = pred.lower()
            call = ('Mixed' if re.search(r'\bai window|\bmixed|\bmostly human', low) else
                    'Human' if low.startswith('human') else 'AI' if low.startswith('ai') else 'Mixed')
            passed = bool(re.match(r'(100% human|human written|human\b)', res, re.I)) and '% ai' not in res.lower()[:12]
            kind = 'section' if re.search(r'\bsection\b|\bh1\b|\bh2\b', text, re.I) else ('paragraph' if re.search(
                r'\balone\b|\bparagraph\b|\bP\d', text) else 'unrecorded')
            out.append(scored({'lane': lane, 'era': src.get('era', 'Pangram 4.0 (before the ledger)'), 'batch': date,
                               'key': text[:80], 'kind': kind, 'call': call, 'chance': None, 'passed': passed},
                              hit.lower().startswith('hit')))
        return out
    raise SystemExit('unknown legacy kind %r' % src['kind'])


def scored(row, marked):
    """One rule for every lane: right when I said Human and the text read 100% Human, or said AI (a "Mixed" or "Human with
    an AI window" call counts as not 100% Human) and it didn't. A lane that marked a call differently keeps its mark in
    'marked' (the Inner Child table counted a Mostly Human result as a hit for a Human call; Joel's rule is that Mostly
    Human isn't a pass)."""
    row['right'] = (row['call'] == 'Human') == row['passed']
    if marked != row['right']:
        row['marked'] = marked
    return row


def ledger_rows(recs, lane):
    out = []
    for p in state(recs).values():
        if p['void'] or not p['result']:
            continue
        r = p['result']
        out.append({'lane': lane, 'era': r.get('detector') or p.get('detector') or 'unrecorded', 'batch': p.get('batch'),
                    'key': p.get('key') or p['sha256'][:12], 'kind': p['scope'], 'call': p['call'], 'chance': p.get('chance'),
                    'passed': r['verdict'] == 'Human', 'right': bool(r['right']), 'link': r.get('link'),
                    'lineage': p['lineage'], 'try': p.get('try'), 'cause': (p['explain'] or {}).get('cause'),
                    'explained': bool(p['explain']), 'words': p.get('words')})
    return out


# ---------- the numbers ----------

def stats(rows):
    n = len(rows)
    if not n:
        return {'n': 0}
    right = sum(r['right'] for r in rows)
    passed = sum(r['passed'] for r in rows)
    out = {'n': n, 'right': right, 'acc': right / n, 'pass_rate': passed / n, 'always_human': passed / n,
           'always_ai': (n - passed) / n, 'said_human': sum(r['call'] == 'Human' for r in rows) / n}
    ch = [r for r in rows if r.get('chance') is not None]
    if ch:
        base = sum(r['passed'] for r in ch) / len(ch)
        out['brier'] = sum((r['chance'] - r['passed']) ** 2 for r in ch) / len(ch)
        out['brier_base'] = sum((base - r['passed']) ** 2 for r in ch) / len(ch)
        out['n_chance'] = len(ch)
    return out


def pct(x):
    return '%.0f%%' % (100 * x)


def stat_cells(s):
    if not s.get('n'):
        return ['0', '-', '-', '-', '-', '-']
    brier = ('%.3f (base %.3f, %d)' % (s['brier'], s['brier_base'], s['n_chance'])) if 'brier' in s else '-'
    return [str(s['n']), '%d (%s)' % (s['right'], pct(s['acc'])), pct(s['always_ai']), pct(s['always_human']),
            pct(s['said_human']), brier]


HEAD = 'calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |'


def table(title_col, groups):
    lines = ['| %s %s' % (title_col, HEAD), '|---' * 7 + '|']
    for name, rows in groups:
        lines.append('| %s | %s |' % (name, ' | '.join(stat_cells(stats(rows)))))
    return lines


def calibration(rows):
    ch = [r for r in rows if r.get('chance') is not None]
    if not ch:
        return []
    lines = ['| my chance of a 100% Human result | calls | mean chance | read Human |', '|---|---|---|---|']
    for lo in (0.0, 0.2, 0.4, 0.6, 0.8):
        b = [r for r in ch if lo <= r['chance'] < lo + 0.2 or (lo == 0.8 and r['chance'] == 1.0)]
        if b:
            lines.append('| %.1f to %.1f | %d | %.2f | %s |' % (lo, lo + 0.2, len(b), sum(r['chance'] for r in b) / len(b),
                                                              pct(sum(r['passed'] for r in b) / len(b))))
    return lines


def lane_page(lane, cfg, legacy, rows, recs):
    eras = []
    for r in legacy + rows:
        if r['era'] not in eras:
            eras.append(r['era'])
    out = ['# Pangram prediction scorecard: %s' % lane, '',
           'Built by `tools/humanization/pangram_ledger.py build` from `%s` (the ledger, one line per prediction, result and '
           'explanation) and the lane\'s records from before the ledger. A call is right when I said Human and Pangram read the '
           'text 100%% Human, or I said AI and it didn\'t. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same '
           'text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.' % cfg['ledger'], '']
    out += ['## By detector version', ''] + table('version |', [(e, [r for r in legacy + rows if r['era'] == e]) for e in eras]) + ['']
    remarked = [r for r in legacy if 'marked' in r]
    if remarked:
        out += ['%d of the older calls are scored here differently from the lane\'s own marks (%d marked right there, %d '
                'marked wrong): this page uses one rule for every lane, where only a 100%% Human result is a pass and a "Mixed" or '
                '"Human with an AI window" call counts as not Human.' % (len(remarked), sum(r['marked'] for r in remarked),
                                                                       sum(not r['marked'] for r in remarked)), '']
    for e in eras:
        er = [r for r in legacy + rows if r['era'] == e]
        out += ['## %s' % e, '']
        recent = [('the latest 50', er[-50:]), ('the latest 100', er[-100:]), ('all', er)]
        out += table('window |', recent) + ['']
        kinds = []
        for r in er:
            if r['kind'] not in kinds:
                kinds.append(r['kind'])
        out += ['The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):', '']
        out += table('scope or kind |', [(k, [r for r in er if r['kind'] == k]) for k in kinds]) + ['']
        cal = calibration(er)
        if cal:
            out += ['Calibration:', ''] + cal + ['']
    if rows:
        misses = [r for r in rows if not r['right']]
        causes = {}
        for r in misses:
            causes.setdefault(r['cause'] or 'not explained yet', []).append(r)
        out += ['## Misses since the ledger (%d)' % len(misses), '']
        if causes:
            out += ['| cause | misses |', '|---|---|'] + ['| %s | %d |' % (c, len(v)) for c, v in
                                                      sorted(causes.items(), key=lambda x: -len(x[1]))] + ['']
            out += ['The latest:', '', '| check | lineage, try | said | read | cause |', '|---|---|---|---|---|']
            for r in misses[-15:]:
                out.append('| %s | %s, %s | %s | %s | %s |' % (('[%s](%s)' % (r['key'], r['link'])) if r.get('link') else r['key'],
                                                               r['lineage'], r['try'], r['call'],
                                                               'Human' if r['passed'] else 'AI or mixed',
                                                               r['cause'] or '**not explained yet**'))
            out.append('')
        st = state(recs)
        open_lines = {}
        for p in st.values():
            if not p['void']:
                open_lines.setdefault(p['lineage'], []).append(p)
        live = [(l, ps) for l, ps in open_lines.items() if not (ps[-1]['result'] and ps[-1]['result'].get('verdict') == 'Human')]
        if live:
            out += ['## Lineages still open (tries used of the cap)', '', '| lineage | scope | tries | last read |', '|---|---|---|---|']
            for l, ps in live:
                last = ps[-1]['result']
                out.append('| %s | %s | %d of %s | %s |' % (l, ps[-1]['scope'], len(ps), cap_text(ps[-1]['scope'], ps[-1].get('detector')),
                                                         last.get('verdict') if last else 'pending'))
            out.append('')
    else:
        out += ['## Since the ledger', '', 'No checks recorded in the ledger yet.', '']
    return '\n'.join(out) + '\n'


def universal_page(per_lane):
    out = ['# Pangram prediction scorecard: every lane', '',
           'Built by `tools/humanization/pangram_ledger.py build --universal` from each lane\'s ledger and older records '
           '(`tools/humanization/pangram_lanes.json` lists the lanes; each lane\'s own page has the detail). Rows are pooled only '
           'within one detector version, and the boundary mix is shown beside every pooled number, as the budget rule asks '
           '(`docs/PANGRAM-PRODUCTION-BUDGET-20261020.md`).', '']
    eras = []
    for lane, rows in per_lane:
        for r in rows:
            if r['era'] not in eras:
                eras.append(r['era'])
    for e in eras:
        out += ['## %s' % e, '']
        groups = [(lane, [r for r in rows if r['era'] == e]) for lane, rows in per_lane]
        groups = [g for g in groups if g[1]]
        out += table('lane |', groups + [('**all lanes**', [r for _, rs in groups for r in rs])]) + ['']
        out += ['The latest 100 calls of each lane:', '']
        out += table('lane |', [(lane, rs[-100:]) for lane, rs in groups]) + ['']
        kinds = {}
        for _, rs in groups:
            for r in rs:
                kinds.setdefault(r['kind'], []).append(r)
        out += ['The boundary mix over all lanes:', ''] + table('scope or kind |', sorted(kinds.items(), key=lambda x: -len(x[1]))) + ['']
    causes = {}
    for lane, rows in per_lane:
        for r in rows:
            if 'explained' in r and not r['right']:
                causes.setdefault(r['cause'] or 'not explained yet', []).append((lane, r))
    out += ['## What the misses say (since the ledger)', '']
    if causes:
        out += ['| cause | misses | lanes |', '|---|---|---|']
        for c, v in sorted(causes.items(), key=lambda x: -len(x[1])):
            out.append('| %s | %d | %s |' % (c, len(v), ', '.join(sorted({l for l, _ in v}))))
        out += ['', 'A cause that repeats becomes a check that runs before Pangram (a linter rule, a gate step or a predictor '
                'feature); a miss nobody can explain goes to Joel with the passage.', '']
    else:
        out += ['No misses recorded in a ledger yet.', '']
    return '\n'.join(out) + '\n'


# ---------- commands ----------

def cmd_predict(a):
    recs = read(a.ledger)
    if a.text:
        text = pathlib.Path(a.text).read_text(encoding='utf-8')
        sha, words = sha256(text), len(text.split())
    else:
        sha, words = a.sha, a.words
    if not sha:
        raise SystemExit('give --text FILE (preferred) or --sha')
    line = lineage_view(state(recs), a.lineage)
    rec = {'type': 'prediction', 'id': '%s#%d' % (a.lineage, len(state(recs)) + 1), 'at': now(), 'lineage': a.lineage,
           'scope': a.scope, 'sha256': sha, 'words': words, 'call': a.call, 'chance': a.chance, 'tells': a.tells or [],
           'human_tells': a.human_tells or [], 'diagnosis': a.diagnosis, 'decides': a.decides, 'key': a.key, 'batch': a.batch,
           'detector': a.detector, 'shading_expected': a.shading_expected, 'emulate_share': a.emulate_share,
           'try': len(line) + 1}
    why = refusals(recs, rec)
    if why:
        print('REFUSED: ' + '\n  '.join(why), file=sys.stderr)
        return 2
    append(a.ledger, {k: v for k, v in rec.items() if v not in (None, [], '')})
    print('%s: try %d of %s for %s (%s), predicted %s%s' % (rec['id'], rec['try'], cap_text(a.scope, a.detector), a.lineage, a.scope, a.call,
                                                          '' if a.chance is None else ' at %.2f' % a.chance))
    return 0


def cmd_result(a):
    recs = read(a.ledger)
    p = find(recs, sha=a.sha, key=a.key, open_only=True)
    if not p:
        raise SystemExit('no open prediction for that text: predictions come first (an unpredicted check is not scored)')
    extra = {'headline': a.headline, 'ai_fraction': a.ai_fraction, 'likelihood': a.likelihood, 'words_read': a.words,
             'shading': a.shading, 'detector': a.detector or p.get('detector'), 'at': a.at}
    rec = result_rec(p, a.verdict, a.link, extra)
    append(a.ledger, rec)
    print('%s: read %s, the prediction (%s) was %s' % (p['id'], a.verdict, p['call'], 'right' if rec['right'] else 'a MISS'))
    return 0


def cmd_results(a):
    recs = read(a.ledger)
    res = json.loads(pathlib.Path(a.results).read_text(encoding='utf-8'))
    n = 0
    for key, r in res.items():
        if isinstance(r, list):  # compact form [headline, ai, words, windows, utc, link tail, flagged]
            r = {'headline': r[0], 'likelihood': r[1], 'words': r[2], 'windows': r[3], 'utc': r[4], 'link': r[5]}
        p = find(recs, key=key, open_only=True)
        if not p:
            continue
        verdict = verdict_of(r.get('headline'), r.get('windows'), r.get('fraction_ai'))
        link = r.get('link') or ''
        if link and not link.startswith('http'):
            link = 'https://www.pangram.com/history/' + link
        rec = result_rec(p, verdict, link, {'headline': r.get('headline'), 'ai_fraction': r.get('fraction_ai'),
                                            'likelihood': r.get('avg_ai_likelihood', r.get('likelihood')),
                                            'words_read': r.get('words'), 'windows': r.get('windows'),
                                            'detector': a.detector or p.get('detector'), 'at': r.get('utc')})
        append(a.ledger, rec)
        recs.append(rec)
        n += 1
        print('%s: read %s, the prediction (%s) was %s' % (key, verdict, p['call'], 'right' if rec['right'] else 'a MISS'))
    print(n, 'results recorded')
    return 0


def cmd_explain(a):
    recs = read(a.ledger)
    p = find(recs, sha=a.sha, key=a.key, pid=a.prediction)
    if not p or not is_miss(p):
        raise SystemExit('explain is for a miss: no missed prediction matches')
    append(a.ledger, {'type': 'explain', 'prediction': p['id'], 'at': now(), 'cause': a.cause, 'note': a.note})
    print('%s: explained as %s' % (p['id'], a.cause))
    return 0


def cmd_void(a):
    recs = read(a.ledger)
    p = find(recs, sha=a.sha, key=a.key, pid=a.prediction, open_only=True)
    if not p:
        raise SystemExit('void is for a prediction with no result')
    append(a.ledger, {'type': 'void', 'prediction': p['id'], 'at': now(), 'reason': a.reason})
    print('%s: voided (%s)' % (p['id'], a.reason))
    return 0


def cmd_status(a):
    st = state(read(a.ledger))
    lines = {}
    for p in st.values():
        if not p['void'] and (not a.lineage or p['lineage'] == a.lineage):
            lines.setdefault(p['lineage'], []).append(p)
    recs = read(a.ledger)
    for l, ps in lines.items():
        last = ps[-1]
        b = blocks(recs, l, last['scope'], last.get('detector'))
        print('%s (%s): %d of %s tries; last %s%s' % (l, last['scope'], len(ps), cap_text(last['scope'], last.get('detector')),
                                                       (last['result'] or {}).get('verdict', 'pending'),
                                                       ('; BLOCKED: ' + ' / '.join(b)) if b else ''))
    return 0


def cmd_check(a):
    recs = read(a.ledger)
    items = json.loads(pathlib.Path(a.items).read_text(encoding='utf-8'))
    pairs = items.items() if isinstance(items, dict) else [(i[0], i[1]) for i in items]
    missing = []
    for key, text in pairs:
        text = text if isinstance(text, str) else text.get('text', '')
        if not find(recs, sha=sha256(text), open_only=True):
            missing.append(key)
    if missing:
        print('no open prediction in the ledger for: ' + ', '.join(missing), file=sys.stderr)
        return 1
    print('every text has its open prediction (%d)' % len(list(pairs)))
    return 0


def cmd_build(a):
    cfg = json.loads(pathlib.Path(a.lanes).read_text(encoding='utf-8'))
    per_lane = []
    for lane in cfg['lanes']:
        if a.lane and lane['lane'] != a.lane:
            continue
        ledger = REPO / lane['ledger']
        recs = read(ledger)
        legacy = [r for src in lane.get('legacy', []) for r in legacy_rows(src, lane['lane'])]
        rows = ledger_rows(recs, lane['lane'])
        per_lane.append((lane['lane'], legacy + rows))
        s = stats(legacy + rows)
        if lane.get('page', True) is False:  # an article under a parallel-write lock: its own writer builds its page
            print('%s: %d rows (its page is built by its own writer: %s)' % (lane['lane'], s.get('n', 0), lane.get('why_no_page', '')))
            continue
        page = REPO / lane['page'] if isinstance(lane.get('page'), str) else ledger.parent / 'SCORECARD.md'
        page.write_text(lane_page(lane['lane'], lane, legacy, rows, recs), encoding='utf-8')
        print('%s: %d rows -> %s' % (lane['lane'], s.get('n', 0), page.relative_to(REPO) if REPO in page.parents else page))
    if a.universal:
        pathlib.Path(a.universal).write_text(universal_page(per_lane), encoding='utf-8')
        print('every lane ->', a.universal)
    if a.rows:  # one row per scored call, every lane, for a dashboard page; rebuilt from the sources, so not kept in Git
        pathlib.Path(a.rows).write_text('[\n' + ',\n'.join(json.dumps(r, ensure_ascii=False, sort_keys=True)
                                                             for _, rs in per_lane for r in rs) + '\n]\n', encoding='utf-8')
        print('rows ->', a.rows)
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = ap.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('predict')
    p.add_argument('ledger')
    p.add_argument('--lineage', required=True)
    p.add_argument('--scope', required=True, choices=sorted(CAPS))
    p.add_argument('--text')
    p.add_argument('--sha')
    p.add_argument('--words', type=int)
    p.add_argument('--call', required=True, choices=CALLS)
    p.add_argument('--chance', type=float, help='my chance of a 100%% Human result, not my confidence in the call: '
                   'a Human call is at least 0.5, an AI call at most 0.5')
    p.add_argument('--tells', action='append')
    p.add_argument('--human-tells', action='append')
    p.add_argument('--diagnosis')
    p.add_argument('--decides')
    p.add_argument('--key')
    p.add_argument('--batch')
    p.add_argument('--detector', default='Pangram 4.1 (web app)')
    p.add_argument('--shading-expected')
    p.add_argument('--emulate-share', type=float)
    p.set_defaults(fn=cmd_predict)
    p = sub.add_parser('result')
    p.add_argument('ledger')
    p.add_argument('--sha')
    p.add_argument('--key')
    p.add_argument('--verdict', required=True, choices=('Human', 'AI', 'Mixed'))
    p.add_argument('--link', required=True)
    p.add_argument('--headline')
    p.add_argument('--ai-fraction', type=float)
    p.add_argument('--likelihood', type=float)
    p.add_argument('--words', type=int)
    p.add_argument('--shading')
    p.add_argument('--detector')
    p.add_argument('--at')
    p.set_defaults(fn=cmd_result)
    p = sub.add_parser('results')
    p.add_argument('ledger')
    p.add_argument('results')
    p.add_argument('--detector')
    p.set_defaults(fn=cmd_results)
    for name, fn in (('explain', cmd_explain), ('void', cmd_void)):
        p = sub.add_parser(name)
        p.add_argument('ledger')
        p.add_argument('--sha')
        p.add_argument('--key')
        p.add_argument('--prediction')
        if name == 'explain':
            p.add_argument('--cause', required=True)
            p.add_argument('--note', required=True)
        else:
            p.add_argument('--reason', required=True)
        p.set_defaults(fn=fn)
    p = sub.add_parser('status')
    p.add_argument('ledger')
    p.add_argument('--lineage')
    p.set_defaults(fn=cmd_status)
    p = sub.add_parser('check')
    p.add_argument('ledger')
    p.add_argument('items')
    p.set_defaults(fn=cmd_check)
    p = sub.add_parser('build')
    p.add_argument('--lanes', default=str(LANES))
    p.add_argument('--lane')
    p.add_argument('--universal')
    p.add_argument('--rows')
    p.set_defaults(fn=cmd_build)
    a = ap.parse_args(argv)
    return a.fn(a)


if __name__ == '__main__':
    sys.exit(main())
