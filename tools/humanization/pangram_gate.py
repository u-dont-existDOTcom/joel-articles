"""pangram_gate.py - the Pangram web-app batch, built only for texts that passed the gate.

Usage (from the repo root):
  python3 tools/humanization/pangram_gate.py DRAFTS.json GATE.json OUT.js --name NAME KEY [KEY ...]

DRAFTS.json maps each key to the exact text Pangram should read. A long text can start with one the
page already holds: {"text": FULL, "prefix": PREFIX, "prefix_from_storage": "t47svh1"} has the page
build FULL from sessionStorage["t47svh1"] (which must hold PREFIX) plus the rest. Or it can be joined
from parts: {"text": FULL, "concat": [{"key": "P3"}, {"lit": "\n\n"}, {"key": "old", "text": OLD}]},
where a key is an earlier item of the batch or a stored text given with its words (2026-10-13: an h2
and its h1 no longer get pasted in full, which cost a turn's worth of output for every check). Every text checked
is also kept in sessionStorage under its own key, so a later batch can start from it.

GATE.json holds each key's gate record:
  {"P1":  {"kind": "draft", "march": ["S S B S S", "S S B S S"], "cold": "OK", "grounding": "OK",
           "stance": 0, "lint": "REVIEW", "missing": []},
   "P1b": {"kind": "draft", "march": ["S B S"], "cold": "OK", "lint": "REVIEW", "missing": [],
           "grounding": "same claims as P1", "stance": "same claims as P1"},
   "P1c": {"kind": "draft", ..., "missing": ["the tribes' predictable reactions"], "probe": true},
   "J4":  {"kind": "owner", "joel": "2026-10-12 03:13 UTC: ..."},
   "h2":  {"kind": "section", "parts": ["P1", "installed"]}}

A draft goes to Pangram only with a march read that has a break in every reading, a cold read with
every sentence OK, a clean grounding, a stance check with no conflicts, a linter verdict that isn't
FAIL (docs/HUMANIZATION-GATE.md: "The march blocks the call", and every candidate gets the whole-article
stance check before any Pangram call), and "missing": the guide points it leaves out. A draft that leaves
one out goes only as a probe, a test of what Pangram reacts to, and a probe is never installed (E168:
faithful first). "same claims as KEY" carries KEY's grounding or stance check
over to an edit that changes no claim (a sentence split in two, say); KEY needs its own record. An
owner text is Joel's own words, which the march doesn't block. A section passes when each of its new
parts does ("installed" for paragraphs already in the article).

Why (turn 48, 2026-10-12): in the web app the batch was a script I wrote by hand each time, so nothing
stopped a call. Round 1's draft went to Pangram with a march of S S S and read 100% AI; later drafts
went before their stance checks and march reads. Lesson E167.

Writes OUT.js, the in-page batch for the dashboard tab (it fills each text, checks its SHA-256, clicks,
and keeps its progress in window.__NAME; it returns 'started' at once and runs on), and
OUT-read.js, which finds each text's result in the History by its SHA-256 and returns the UTC time,
history id, the result's link, words, AI likelihood, headline and windows, with the words of every window
that isn't Human. A flag is reported with that link, those words and what the checked text was made of
(Joel, 2026-10-13 12:46 UTC, after I'd written that the seam of P2 and his P3 reads AI when only the whole
919-word h2 did: "show me the exact thing you tested". Lesson E171).
"""
import argparse
import hashlib
import json
import pathlib
import sys

SAME = 'same claims as '


def sha(t):
    return hashlib.sha256(t.encode('utf-8')).hexdigest()


def problems(key, gate, seen=()):
    """What keeps KEY from going to Pangram; an empty list means it may go."""
    g = gate.get(key)
    if g is None:
        return ['no gate record']
    kind = g.get('kind')
    if kind == 'owner':
        return [] if g.get('joel') else ["an owner text needs 'joel': where his words come from"]
    if kind == 'section':
        parts = g.get('parts') or []
        out = [] if parts else ["a section needs 'parts': its new paragraphs' keys, or \"installed\""]
        for p in parts:
            if p != 'installed' and p not in seen:
                out += ['part %s: %s' % (p, q) for q in problems(p, gate, seen + (key,))]
        return out
    if kind != 'draft':
        return ['kind must be draft, owner or section, not %r' % (kind,)]
    out = []
    march = g.get('march') or []
    if not march:
        out.append('no march read (the march blocks the call)')
    for m in march:
        if 'B' not in m.split():
            out.append('the march blocks the call: %r has no break. Break it where a person would react, '
                       'pause, allow something or wonder what it feels like (E131)' % m)
    missing = g.get('missing')
    if missing is None:
        out.append("no 'missing' list: the guide points the draft leaves out ([] when it carries them all; E168)")
    elif missing and not g.get('probe'):
        out.append('leaves out %s. A draft that drops a point goes to Pangram only as a probe ("probe": true), and a probe '
                   'is never installed (E168; Joel, 2026-10-12: "never take out something important in order to pass '
                   'pangram")' % '; '.join(missing))
    if g.get('cold') != 'OK':
        out.append('cold read: %r (every sentence OK first)' % (g.get('cold'),))
    if not g.get('lint') or str(g.get('lint')).upper() == 'FAIL':
        out.append('linter: %r (run it; a FAIL means rewrite)' % (g.get('lint'),))
    for field, good, need in (('grounding', 'OK', 'a clean grounding'), ('stance', 0, 'a stance check with 0 conflicts')):
        v = g.get(field)
        if isinstance(v, str) and v.startswith(SAME):
            other = v[len(SAME):].strip()
            ov = (gate.get(other) or {}).get(field)
            if other in seen or ov != good:
                out.append('%s: %r, but %s has %r' % (field, v, other, ov))
        elif v != good:
            out.append('%s: %r (%s before any Pangram call)' % (field, v, need))
    return out


def batch_js(name, items):
    rows = []
    known = {k: (e if isinstance(e, str) else e['text']) for k, e in items}
    for key, entry in items:
        full = entry if isinstance(entry, str) else entry['text']
        if isinstance(entry, dict) and entry.get('concat'):
            # [{"key": K} (an earlier item of this batch, or {"key": K, "text": T} for one stored before),
            #  {"lit": "..."}]: the page joins them, so a section isn't pasted again in full.
            js, txt = [], ''
            for c in entry['concat']:
                if 'lit' in c:
                    js.append(json.dumps(c['lit'])); txt += c['lit']
                else:
                    js.append('sessionStorage.getItem(%s)' % json.dumps(c['key'])); txt += c.get('text', known.get(c['key'], '\0'))
            if txt != full:
                sys.exit('%s: its concat parts do not join up to its text' % key)
            rows.append('[%s, () => %s, %s]' % (json.dumps(key), ' + '.join(js), json.dumps(sha(full))))
            continue
        if isinstance(entry, dict) and entry.get('prefix_from_storage'):
            pre = entry['prefix']
            if not full.startswith(pre):
                sys.exit('%s: its text does not start with its prefix' % key)
            src = 'sessionStorage.getItem(%s) + %s' % (json.dumps(entry['prefix_from_storage']), json.dumps(full[len(pre):]))
        else:
            src = json.dumps(full)
        rows.append('[%s, () => %s, %s]' % (json.dumps(key), src, json.dumps(sha(full))))
    return ("const items = [" + ', '.join(rows) + "];\n"
            "window.__" + name + " = [];\n"
            "const log = m => window.__" + name + ".push(m);\n"
            "const setter = Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value').set;\n"
            "const sha = async t => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))).map(b => b.toString(16).padStart(2, '0')).join('');\n"
            "const button = () => [...document.querySelectorAll('button[type=submit]')].find(b => /check for ai/i.test(b.innerText));\n"
            "const wait = ms => new Promise(r => setTimeout(r, ms));\n"
            "async function run() {\n"
            "  for (const [k, mk, want] of items) {\n"
            "    const T = mk();  // built when its turn comes, so it can use texts stored earlier in this batch\n"
            "    for (let j = 0; j < 20 && !(button() && document.querySelector('textarea')); j++) await wait(500);\n"
            "    const ta = document.querySelector('textarea');\n"
            "    if (!ta) { log(k + ': no textarea'); break; }\n"
            "    setter.call(ta, T); ta.dispatchEvent(new Event('input', {bubbles: true}));\n"
            "    let b = null;\n"
            "    for (let j = 0; j < 30; j++) { await wait(500); b = button(); if (b && !b.disabled) break; }\n"
            "    const h = await sha(ta.value);\n"
            "    if (h !== want) { log(k + ': hash mismatch ' + h + ' (is its prefix in sessionStorage?)'); break; }\n"
            "    if (!b || b.disabled) { log(k + ': button not ready'); break; }\n"
            "    try { sessionStorage.setItem(k, T); } catch (e) {}\n"
            "    b.click(); log(k + ': clicked');\n"
            "    await wait(10000);\n"
            "  }\n"
            "  log('end');\n"
            "}\n"
            "run(); 'started'\n")


def reader_js(items, pages=5):
    want = {sha(e if isinstance(e, str) else e['text']): k for k, e in items}
    return ("const want = " + json.dumps(want) + ";\n"
            "const sha = async t => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))).map(b => b.toString(16).padStart(2, '0')).join('');\n"
            "const out = {};\n"
            "let url = 'https://web.pangram.com/api/history-list/?limit=20&offset=0';\n"
            "for (let p = 0; url && p < " + str(pages) + " && Object.keys(out).length < Object.keys(want).length; p++) {\n"
            "  const l = await fetch(url, {credentials: 'include'}).then(r => r.json());\n"
            "  for (const it of l.results || []) {\n"
            "    const d = await fetch('https://web.pangram.com/api/history/' + it.uuid + '/', {credentials: 'include'}).then(r => r.json());\n"
            "    const k = want[await sha(d.prompt || '')];\n"
            "    if (!k || out[k]) continue;\n"
            "    const o = d.response.overall;\n"
            "    const n = (d.prompt || '').replace(/\\n{2,}/g, '\\n');  // window indexes count a blank line as one newline\n"
            "    const words = w => { const s = n.slice(w.start_index, w.end_index).trim();\n"
            "      return s.startsWith((w.text || '').trim().slice(0, 30)) ? s : (w.text || '').trim() + '…'; };\n"
            "    out[k] = {history_id: Number(it.id), link: 'https://www.pangram.com/history/' + it.uuid,\n"
            "              utc: new Date(it.timestamp).toISOString().replace(/\\.\\d+Z$/, 'Z'), words: o.word_count,\n"
            "              avg_ai_likelihood: o.avg_ai_likelihood, headline: o.headline, version: o.version,\n"
            "              windows: (o.windows || []).map(w => w.label + ', ' + w.confidence + ', ' + w.word_count),\n"
            "              flagged: (o.windows || []).filter(w => w.label !== 'Human').map(w => w.label + ' (' + w.word_count + ' words): ' + words(w))};\n"
            "  }\n"
            "  url = l.next;\n"
            "}\n"
            "JSON.stringify(out)\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('drafts'); ap.add_argument('gate'); ap.add_argument('out')
    ap.add_argument('--name', required=True, help='window.__NAME keeps the batch progress')
    ap.add_argument('keys', nargs='+')
    a = ap.parse_args(argv)
    drafts = json.loads(pathlib.Path(a.drafts).read_text(encoding='utf-8'))
    gate = json.loads(pathlib.Path(a.gate).read_text(encoding='utf-8'))
    bad = False
    for k in a.keys:
        if k not in drafts:
            print('%s: not in %s' % (k, a.drafts), file=sys.stderr); bad = True
        for p in problems(k, gate):
            print('%s: %s' % (k, p), file=sys.stderr); bad = True
    if bad:
        print('No batch written: the gate comes before Pangram (docs/HUMANIZATION-GATE.md).', file=sys.stderr)
        return 2
    items = [(k, drafts[k]) for k in a.keys]
    out = pathlib.Path(a.out)
    out.write_text(batch_js(a.name, items), encoding='utf-8')
    out.with_name(out.stem + '-read.js').write_text(reader_js(items), encoding='utf-8')
    for k, e in items:
        t = e if isinstance(e, str) else e['text']
        print('%s %s %d words' % (k, sha(t), len(t.split())))
    print('-> %s and %s' % (out, out.with_name(out.stem + '-read.js')))
    return 0


if __name__ == '__main__':
    sys.exit(main())
