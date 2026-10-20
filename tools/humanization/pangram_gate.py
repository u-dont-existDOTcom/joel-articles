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
   "h2":  {"kind": "section", "parts": ["P1", "installed"], "repeats": 0},
   "P7e": {"kind": "edit", "was": "batch 267g: P7 alone, 100% Human", "march_was": ["S S S"], "march": ["S S S"],
           "cold": "OK", "grounding": "OK", "stance": 0, "lint": "REVIEW", "missing": []}}

A draft goes to Pangram only with a march read that has a break in every reading, a cold read with
every sentence OK, a clean grounding, a stance check with no conflicts, a linter verdict that isn't
FAIL (docs/HUMANIZATION-GATE.md: "The march blocks the call", and every candidate gets the whole-article
stance check before any Pangram call), and "missing": the guide points it leaves out. A draft that leaves
one out goes only as a probe, a test of what Pangram reacts to, and a probe is never installed (E168:
faithful first). "same claims as KEY" carries KEY's grounding or stance check
over to an edit that changes no claim (a sentence split in two, say); KEY needs its own record. An
owner text is Joel's own words, which the march doesn't block. A section passes when each of its new
parts does ("installed" for paragraphs already in the article) and the assembled section has had a repeats
check ("repeats": 0 once every repeat inside it is fixed or answered; E172, Joel 2026-10-13: "duplication is
very AI").

An edit (E173, 2026-10-14) is a fix of a few words in a paragraph that is already in the article after its
own Pangram pass ("was" says where). It needs everything a draft needs except that its march is read against
the installed version's ("march_was"): it is blocked when the installed version had a break and the edit has
none, since then the fix made the march. A cut is the exception (2026-10-17): an edit whose record gives the
installed text as "cut_of", and whose text is that text with words taken out and nothing added (checked here),
goes to Pangram whatever the march says, and the march labels stay in the record. Why: two cuts this rule held,
each its paragraph's only break, made no difference to Pangram when Joel ran them himself (21:37 UTC: "it made
no difference taking those exclamation phrases out for pangram"). A paragraph that passed without a break keeps its structure through a
fix of a few words, and Pangram is the test of it. Why: on 2026-10-14 the march read labeled 15 of the 20
paragraphs that the sweep's fixes changed with no break, and their installed versions got the same labels,
though each of those had read Human alone and in its section; the draft rule would have had every one of them
rewritten to add a break.

An Emulate text (2026-10-18) is made only of Emulate's output as it came back and the published text, no word of mine:
{"kind": "emulate", "emulate": ["path/to/run.out.txt", ...], "published": "path/to/published.md", "lint": "REVIEW"}. The gate
checks that every block of it (the text between blank lines) is a block of one of those files, and lints it. It goes to
Pangram without a march read: the march steers my own drafting, and Emulate's output can't be given a break without
putting my words into it (the queue's directive: "Never edit Emulate's output with your own words"), so a march with no
break would make an output unusable before Pangram ever saw it (Joel, 2026-10-18 01:29 UTC: "your mission is to improve
the scorecard especially for predictions and fixes, as well as the speed of fixing"). Like a screen it is never
installed and never part of a section check until it has its meaning reviews: "cold": "OK", "grounding": "OK" (every
point of the published text kept, nothing invented), "stance": 0 and "missing": []. The linter runs on it and its verdict
is kept, but a FAIL doesn't stop the call: the linter's tells were found in my sentences, the guide's own lists carry its
meaning (the first six Emulate texts, 2026-10-18: four FAILs, each on a list Emulate kept from the published text), and
Pangram is the test that costs a credit; whether the linter predicts Pangram on Emulate's text is what the record shows.
It doesn't: 57 of the 59 screens of 430g to 437g FAILed, and 28 of the 30 that read 100% Human. So an edit of an
Emulate text (my meaning fixes, "was_kind": "emulate", "lint_was": the screen's verdict) isn't held by a FAIL that its
screen had too; one the screen didn't have still holds it.

A baseline (2026-10-18) is a published text checked as it stands, before any of it is rewritten:
{"kind": "baseline", "source": "source/published-20260928.md, SHA-256 3b5cb6cc..."}. It needs only its source.

A screen (E175, 2026-10-15) is a candidate that has passed only the cheap checks, a linter verdict that isn't FAIL
and a march read with a break in every reading: {"kind": "screen", "march": [...], "lint": "REVIEW"}. It goes to
Pangram before the long meaning reviews (cold read, grounding, stance check, repeats), and only the screens that
read Human go on to them; a screen is never installed and is never a part of a section check. Why: on 2026-10-15
the h1 opening of The Inner Guide Comes Later went through six rounds of meaning reviews (10 to 18 minutes each)
for two Pangram tries per paragraph, 3 hours 20 minutes in all (Joel, 16:39 UTC: "why did that take you 4 hours
22 minutes to humanize 1 paragraph? that's like 4x longer than normal for a whole section").

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
    if kind == 'emulate':
        out = []
        if not g.get('emulate'):
            out.append("an Emulate text needs 'emulate': the run output files its blocks come from")
        if not g.get('_blocks_ok'):
            out.append('its blocks are not all from the named Emulate outputs and the published text (main() checks this)')
        if not g.get('lint') or str(g.get('lint')).upper() not in ('CLEAR', 'REVIEW', 'FAIL'):
            out.append('linter: %r (run it: pass --lint-article, so its verdict is recorded)' % (g.get('lint'),))
        return out
    if kind == 'baseline':
        # 2026-10-18: a new article's published text, checked as it stands before anything in it is rewritten (the hypnosis
        # guide, after Joel's 01:29 UTC "let's move onto the next article in the queue"). Nothing in it is mine, so there is
        # nothing for the meaning reviews to check; it says where the text comes from, and it is never installed.
        return [] if g.get('source') else ["a baseline needs 'source': the published file (and its SHA-256) the text is from"]
    if kind == 'section':
        parts = g.get('parts') or []
        out = [] if parts else ["a section needs 'parts': its new paragraphs' keys, or \"installed\""]
        rep = g.get('repeats')
        if rep != 0 and not (isinstance(rep, str) and rep.lower().startswith('joel')):
            out.append("no repeats check of the assembled section: run reviewer.py repeats --focus on it, fix or answer "
                       "every repeat, then \"repeats\": 0 (or \"joel: ...\" for repeats he chose to keep). E172; Joel, "
                       "2026-10-13: \"duplication is very AI we already knew that but you're not checking that well enough\"")
        for p in parts:
            pg = gate.get(p) or {}
            if p != 'installed' and pg.get('kind') == 'emulate':
                miss = [f for f, want in (('cold', 'OK'), ('grounding', 'OK'), ('stance', 0), ('missing', [])) if pg.get(f) != want]
                if miss:
                    out.append('part %s is an Emulate text without its meaning reviews (%s): it can be part of a section '
                               'check once they are done' % (p, ', '.join(miss)))
                if p not in seen:
                    out += ['part %s: %s' % (p, q) for q in problems(p, gate, seen + (key,))]
                continue
            if p != 'installed' and pg.get('kind') == 'screen':
                out.append('part %s is a screen: it needs its meaning reviews (a draft record) before it can be part '
                           'of a section check (E175)' % p)
            elif p != 'installed' and p not in seen:
                out += ['part %s: %s' % (p, q) for q in problems(p, gate, seen + (key,))]
        return out
    if kind == 'screen':
        # E175 (Joel, 2026-10-15 16:39 UTC: "why did that take you 4 hours 22 minutes to humanize 1 paragraph?"):
        # a candidate that passes the cheap checks is screened in Pangram before the long meaning reviews, and only
        # the ones that read Human go on to them. A screen is never installed and never part of a section check.
        out = []
        march = g.get('march') or []
        if not march:
            out.append('no march read (the march blocks the call)')
        for m in march:
            if 'B' not in m.split():
                out.append('the march blocks the call: %r has no break (E131)' % m)
        if not g.get('lint') or str(g.get('lint')).upper() == 'FAIL':
            out.append('linter: %r (run it; a FAIL means rewrite)' % (g.get('lint'),))
        return out
    if kind not in ('draft', 'edit'):
        return ['kind must be draft, edit, screen, emulate, owner, baseline or section, not %r' % (kind,)]
    out = []
    march = g.get('march') or []
    if not march:
        out.append('no march read (the march blocks the call)')
    if kind == 'edit':
        if not g.get('was'):
            out.append("an edit needs 'was': where the installed version it changes passed Pangram (E173)")
        was = g.get('march_was') or []
        if not was:
            out.append("an edit needs 'march_was': the march read of the installed version (E173)")
        elif march and sum('B' in m.split() for m in march) < sum('B' in m.split() for m in was):
            # 2026-10-18: an edit of several paragraphs (an Emulate stretch with my meaning fixes) is held when it has fewer
            # paragraphs with a break than the version that passed; for one paragraph this is the rule as it was (the
            # version that passed had a break and the edit has none). Paragraphs that had no break before don't hold it.
            # 2026-10-17: a cut that only takes words out goes to Pangram whatever the march says (main() checks "cut_of"
            # against the text). Joel, 21:37 UTC, on two cuts this rule held because each took out its paragraph's only
            # break: "it made no difference taking those exclamation phrases out for pangram".
            if not g.get('_cut_ok'):
                out.append('the march blocks the call: the installed version had a break (%r) and the edit has none (%r). '
                           'The fix made the march; put the break back (E131, E173), unless the edit only takes words out '
                           '("cut_of": the installed text)' % (was, march))
    else:
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
    elif not missing and str(g.get('missing_note') or '').strip() and not g.get('owner_ok'):
        # 2026-10-16: section 13 v31 went in with "missing": [] and the dropped "if the community uses them" written in
        # "missing_note", so this check never saw the loss. Joel, 23:38 UTC: "yes i want "if the community uses them" back".
        out.append("'missing' is empty but 'missing_note' describes something: a note can't waive a dropped point. Put it in "
                   "'missing' (the draft then goes only as a probe), or quote Joel's answer that the loss is fine in "
                   "'owner_ok' (Joel, 2026-10-12: \"never take out something important in order to pass pangram\")")
    if g.get('cold') != 'OK':
        out.append('cold read: %r (every sentence OK first)' % (g.get('cold'),))
    # 2026-10-18: an edit of an Emulate text (my meaning fixes in a section whose Emulate screen read 100% Human, "was_kind":
    # "emulate") is held by a linter FAIL only when the screen it edits wasn't FAIL too ("lint_was", the screen's own
    # recorded verdict). The linter FAILed 57 of the 59 Emulate screens of 430g to 437g, and 28 of the 30 that read 100%
    # Human (articles/inner-signal/humanize/fix-20261018/b43*/GATE.json), so on Emulate's text its FAIL says nothing about
    # Pangram; a FAIL the screen didn't have is one my fixes made, and that still holds the call.
    emu_fail_ok = (kind == 'edit' and g.get('was_kind') == 'emulate' and str(g.get('lint_was', '')).upper() == 'FAIL'
                   and str(g.get('lint', '')).upper() == 'FAIL')
    if (not g.get('lint') or str(g.get('lint')).upper() == 'FAIL') and not emu_fail_ok:
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


def emulate_blocks_ok(text, g, base):
    """Every blank-line block of TEXT is a block of one of g['emulate']'s files or of g['published'] (headings may
    have lost their #, and list marks may have been taken off). Paths are from the repository root or from BASE."""
    import re
    def blocks_of(path):
        f = pathlib.Path(path)
        if not f.is_file():
            f = base / path
        if not f.is_file():
            root = pathlib.Path(__file__).resolve().parents[2]
            f = root / path
        if not f.is_file():
            return None
        t = f.read_text(encoding='utf-8')
        out = set()
        for b in re.split(r'\n\s*\n', t):
            b = b.strip()
            if not b:
                continue
            out.add(b)
            p = re.sub(r'^#{1,6}\s+', '', b)
            p = re.sub(r'\[([^\]]+)\]\((?:[^()\s]|\([^()\s]*\))*\)', r'\1', p).replace('*', '')
            p = re.sub(r'(?m)^>\s?', '', p)
            p = re.sub(r'(?m)^\s*(?:[-*+]|\d+[.)])\s+', '', p)
            out.add(re.sub(r'[ \t]+', ' ', p).strip())
        return out
    allowed = set()
    for path in list(g.get('emulate') or []) + ([g['published']] if g.get('published') else []):
        bs = blocks_of(path)
        if bs is None:
            return False, 'no such file: %s' % path
        allowed |= bs
    # 2026-10-18 (434g: my meaning fixes made 21 of 25 Human sections read AI): a screen may also hold paragraphs of a
    # meaning-fixed section ("fixed": [its fixed.json]), the stretches that read Human with the fixes in, beside Emulate's
    # new run of the ones that didn't. Those paragraphs went through the meaning reviews already.
    for path in g.get('fixed') or []:
        f = pathlib.Path(path)
        if not f.is_file():
            f = base / path
        if not f.is_file():
            f = pathlib.Path(__file__).resolve().parents[2] / path
        if not f.is_file():
            return False, 'no such file: %s' % path
        for u in json.loads(f.read_text(encoding='utf-8')).get('units', []):
            allowed |= {x.strip() for p in u.get('paras', []) for x in re.split(r'\n\s*\n', p) if x.strip()}
    emu = set()
    for path in g.get('emulate') or []:
        emu |= blocks_of(path) or set()

    def spliced(b):
        # a mechanical cut (the queue's directive: "cutting and joining whole sentences or paragraphs taken from the two
        # versions"): whole sentences from one Emulate block, starting and ending at sentence ends
        for e in emu:
            i = e.find(b)
            if i < 0:
                continue
            starts = i == 0 or re.search(r'[.!?:]["”’)]?\s+$', e[:i])
            ends = i + len(b) == len(e) or re.match(r'\s+\S', e[i + len(b):]) and re.search(r'[.!?]["”’)]?$', b)
            if starts and ends:
                return True
        return False
    stray = [b for b in (x.strip() for x in re.split(r'\n\s*\n', text)) if b and b not in allowed and not spliced(b)]
    if stray:
        return False, '%d block(s) are in neither the Emulate outputs nor the published text, first: %r' % (len(stray), stray[0][:80])
    return True, ''


def is_cut(new, old):
    """True when NEW is OLD with words taken out and nothing added, changed or moved: its words, split on white space,
    are OLD's words in order with some left out (a sentence, a phrase, a question)."""
    n, o = new.split(), old.split()
    if not n or len(n) >= len(o):
        return False
    it = iter(o)
    return all(any(w == x for x in it) for w in n)


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
    # Two tabs can share a batch (turn 65: a 69-check batch took 20 minutes in one): one runs it as it is, the
    # other with window.__reverse = true from the end, and each stops where the other has got to; they meet in the
    # middle through localStorage, which tabs of the same site share.
    return ("const items0 = [" + ', '.join(rows) + "];\n"
            "const rev = !!window.__reverse;\n"
            "const items = rev ? items0.slice().reverse() : items0;\n"
            "const order0 = items0.map(x => x[0]);\n"
            "const lane = k => " + json.dumps(name) + " + '_' + k;\n"
            "try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}\n"
            "window.__" + name + " = [];\n"
            "const log = m => { window.__" + name + ".push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__" + name + ")); } catch (e) {} };\n"
            "const other = () => { try { return JSON.parse(localStorage.getItem(lane(rev ? 'fwd' : 'rev')) || '[]').filter(m => / (clicked|taking)$/.test(m)).map(m => order0.indexOf(m.split(':')[0])); } catch (e) { return []; } };\n"
            "const setter = Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value').set;\n"
            "const sha = async t => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))).map(b => b.toString(16).padStart(2, '0')).join('');\n"
            "const button = () => [...document.querySelectorAll('button[type=submit]')].find(b => /check for ai/i.test(b.innerText));\n"
            "const wait = ms => new Promise(r => setTimeout(r, ms));\n"
            "async function run() {\n"
            "  for (const [k, mk, want] of items) {\n"
            "    const o = other(), i = order0.indexOf(k);\n"
            "    if (o.length && (rev ? i <= Math.max(...o) : i >= Math.min(...o))) { log('stop at ' + k + ': the other tab has the rest'); break; }\n"
            "    log(k + ': taking');  // claimed before the work, so the other tab never takes it too (turn 65: with a margin\n"
            "                          // of one instead, both tabs stopped short of the last check)\n"
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
            "  // each page's details in parallel (2026-10-17: the History is shared with other lanes and fills fast)\n"
            "  const ds = await Promise.all((l.results || []).map(it => fetch('https://web.pangram.com/api/history/' + it.uuid + '/', {credentials: 'include'}).then(r => r.json()).then(d => [it, d])));\n"
            "  for (const [it, d] of ds) {\n"
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


def lint_verdict(text, article):
    """tells_lint.py's verdict (CLEAR, REVIEW or FAIL) on TEXT, with ARTICLE as the installed text. Turn 60
    (2026-10-16): a draft the linter FAILs went into a batch as REVIEW, because the gate file's "lint" was typed
    by hand (E179)."""
    import subprocess
    import tempfile
    with tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False, encoding='utf-8') as f:
        f.write(text)
        name = f.name
    try:
        out = subprocess.run([sys.executable, str(pathlib.Path(__file__).with_name('tells_lint.py')), name,
                              '--installed', article], capture_output=True, text=True).stdout
    finally:
        pathlib.Path(name).unlink()
    for line in out.splitlines():
        if line.startswith('verdict:'):
            return line.split(':', 1)[1].strip().upper()
    return 'UNKNOWN'


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('drafts'); ap.add_argument('gate'); ap.add_argument('out')
    ap.add_argument('--name', required=True, help='window.__NAME keeps the batch progress')
    ap.add_argument('--lint-article', help='the installed article: the linter runs on every screen, draft and edit '
                    'here, and its verdict, not the one typed in GATE.json, decides (E179)')
    ap.add_argument('keys', nargs='+')
    a = ap.parse_args(argv)
    drafts = json.loads(pathlib.Path(a.drafts).read_text(encoding='utf-8'))
    gate = json.loads(pathlib.Path(a.gate).read_text(encoding='utf-8'))
    bad = False
    # The linter takes about 5 seconds a text, so the texts are linted side by side (2026-10-17, turn 65: Joel asked
    # for the work to go faster). A record's own "lint_article" is the article it goes into, when a batch holds
    # paragraphs for different sections (pangram_round.py --spec); otherwise it's --lint-article.
    todo = [k for k in a.keys if k in drafts and a.lint_article and (gate.get(k) or {}).get('kind') in ('screen', 'draft', 'edit', 'emulate')]
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=4) as ex:
        verdicts = dict(zip(todo, ex.map(lambda k: lint_verdict(drafts[k] if isinstance(drafts[k], str) else drafts[k]['text'],
                                                                 (gate.get(k) or {}).get('lint_article') or a.lint_article), todo)))
    for k in a.keys:
        if k not in drafts:
            print('%s: not in %s' % (k, a.drafts), file=sys.stderr); bad = True
        elif k in verdicts:
            v = verdicts[k]
            if v != str((gate.get(k) or {}).get('lint', '')).upper():
                print('%s: the linter says %s, GATE.json says %r; it now says %s' % (k, v, gate[k].get('lint'), v), file=sys.stderr)
            gate[k] = dict(gate[k], lint=v)
        if k in drafts and (gate.get(k) or {}).get('kind') == 'emulate':
            text = drafts[k] if isinstance(drafts[k], str) else drafts[k]['text']
            ok, why = emulate_blocks_ok(text, gate[k], pathlib.Path(a.gate).parent)
            if ok:
                gate[k] = dict(gate[k], _blocks_ok=True)
            else:
                print('%s: %s' % (k, why), file=sys.stderr); bad = True
        if k in drafts and (gate.get(k) or {}).get('kind') == 'edit' and gate[k].get('cut_of') is not None:
            if is_cut(drafts[k] if isinstance(drafts[k], str) else drafts[k]['text'], gate[k]['cut_of']):
                gate[k] = dict(gate[k], _cut_ok=True)
            else:
                print('%s: "cut_of" is given, but the text is not that text with words taken out' % k, file=sys.stderr); bad = True
        for p in problems(k, gate):
            print('%s: %s' % (k, p), file=sys.stderr); bad = True
    if bad:
        print('No batch written: the gate comes before Pangram (docs/HUMANIZATION-GATE.md).', file=sys.stderr)
        return 2
    if verdicts:  # the record keeps the linter's verdict, not the one typed or guessed (turn 65)
        pathlib.Path(a.gate).write_text(json.dumps(gate, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
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
