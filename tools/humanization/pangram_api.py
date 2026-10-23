#!/usr/bin/env python3
"""pangram_api.py - Pangram checks through Joel's API key, run on his laptop.

Joel, 2026-10-03 04:03 UTC: "i have a new pangram key you can use for api:
/mnt/hdd/storage/joel/SSD-offload/Documents/api keys/pangram.txt". That night the dashboard's monthly credits had
run out ("Your monthly credits will refill in 15 days"). Another session was checking on the same account at the
same time, and the dashboard had started showing stale results (`docs/HUMANIZATION-GATE.md`, step 8).

Usage (on the laptop, with Desktop Commander, from the lane folder /home/joel/ai-work/claude-dangerous-lane):
  python3 pangram_api.py probe
  python3 pangram_api.py check TEXTS.json OUTDIR [--names a,b,c] [--expect 4.1] [--windows] [--public]

`probe` checks the key without creating a billable task. TEXTS.json maps names to texts, as plain text the way
Pangram should see them. For each name, `check` does the following:
- If OUTDIR/cache/<sha256>.json already holds a result for exactly this text, it reuses that result instead of
  paying again.
- Otherwise it POSTs once (model "pangram-4") and saves the task id (OUTDIR/cache/<sha256>.pending.json) before
  polling. A rerun resumes that task instead of posting again. A POST that fails in a way that leaves it unclear
  whether Pangram took it is never retried automatically.
- It polls until the task finishes and saves the whole result, whatever version answered. With --expect, a result of
  another version stops the run after it is saved (so it is never paid for twice). Until 2026-10-22 the tool required
  4.0; the Inner Child lane's gate is 4.1 (Joel's Substack check), and turn 97's first call is there to see which
  version the API answers with.
- It appends one summary line to OUTDIR/results.jsonl: name, sha256 of the text, local word count, the headline,
  fraction_ai, fraction_ai_assisted, fraction_human, version, task id and UTC time.

With --public it asks Pangram for a public page of each result (public_dashboard_link) and puts its link in the summary:
Joel, 2026-10-23 02:29 UTC: "public pangram links are ok." That is the link he gets for a stretch he should look at (E214).
It prints only those summaries; with --windows each line also lists the result's windows (label, confidence, words,
start and end, and the window's text), which is what a reader needs to see what was flagged. The key is read from the
file each run and is never printed, copied or logged.

The protocol is pangram-humanization-lab's (`src/pangram_lab/pangram4.py`, proven 2026-08-12): x-api-key, an
explicit model, a version check, no automatic POST retry, the task id checkpointed before polling, and a cache
keyed on the text's bytes.
"""
import argparse, datetime, hashlib, json, os, pathlib, sys, time, urllib.error, urllib.request

BASE = 'https://text.external-api.pangram.com'
MODEL = 'pangram-4'
KEY_FILE = os.environ.get('PANGRAM_KEY_FILE', '/mnt/hdd/storage/joel/SSD-offload/Documents/api keys/pangram.txt')


def key():
    k = pathlib.Path(KEY_FILE).read_text(encoding='utf-8').strip()
    if not k:
        sys.exit('pangram key file is empty')
    return k


def request(method, url, body=None, timeout=60):
    data = json.dumps(body, ensure_ascii=False).encode('utf-8') if body is not None else None
    headers = {'x-api-key': key(), 'Accept': 'application/json'}
    if body is not None:
        headers['Content-Type'] = 'application/json'
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read().decode('utf-8')
            return r.status, (json.loads(raw) if raw else {})
    except urllib.error.HTTPError as e:
        raw = e.read().decode('utf-8', errors='replace')
        try:
            return e.code, (json.loads(raw) if raw else {})
        except json.JSONDecodeError:
            return e.code, {'raw': raw[:500]}


def probe():
    status, obj = request('GET', BASE + '/task/00000000-0000-0000-0000-000000000000')
    meaning = {200: 'key accepted', 403: 'key accepted (task not ours)', 404: 'key accepted (no such task)',
               401: 'KEY REJECTED', 402: 'NO CREDITS'}.get(status, 'unexpected')
    print(json.dumps({'probe_http': status, 'meaning': meaning}))
    return status in (200, 403, 404)


def poll(task_id, timeout=300):
    end = time.monotonic() + timeout
    delay = 1.0
    while True:
        status, obj = request('GET', '%s/task/%s' % (BASE, task_id))
        if status in (429, 500, 502, 503, 504):
            time.sleep(delay); delay = min(8.0, delay * 2)
        elif status != 200:
            raise RuntimeError('poll HTTP %s: %s' % (status, obj))
        else:
            stage = obj.get('stage') or ''
            if stage == 'STAGE_SUCCESS':
                return obj
            if stage == 'STAGE_FAILED':
                raise RuntimeError('task %s failed: %s' % (task_id, obj))
            time.sleep(2.0)
        if time.monotonic() > end:
            raise RuntimeError('task %s not done after %ss; rerun to resume it (no new POST)' % (task_id, timeout))


def check(texts_path, outdir, names=None, expect=None, show_windows=False, public=False):
    texts = json.loads(pathlib.Path(texts_path).read_text(encoding='utf-8'))
    out = pathlib.Path(outdir); cache = out / 'cache'; cache.mkdir(parents=True, exist_ok=True)
    for name in (names or list(texts)):
        text = texts[name]
        sha = hashlib.sha256(text.encode('utf-8')).hexdigest()
        done, pending, ambiguous = cache / (sha + '.json'), cache / (sha + '.pending.json'), cache / (sha + '.ambiguous.json')
        source = 'cache'
        if done.exists():
            result = json.loads(done.read_text(encoding='utf-8'))['result']
        else:
            if ambiguous.exists():
                sys.exit('%s: an earlier POST for this text ended ambiguously (%s); check the account before any new POST' % (name, ambiguous))
            if pending.exists():
                task_id = json.loads(pending.read_text(encoding='utf-8'))['task_id']; source = 'resumed'
            else:
                try:
                    status, obj = request('POST', BASE + '/task', {'text': text, 'public_dashboard_link': bool(public), 'model': MODEL})
                except (OSError, urllib.error.URLError) as e:
                    ambiguous.write_text(json.dumps({'name': name, 'error': str(e)}), encoding='utf-8')
                    sys.exit('%s: POST failed ambiguously (%s); not retried' % (name, e))
                if status in (429, 500, 502, 503, 504):
                    ambiguous.write_text(json.dumps({'name': name, 'http': status, 'body': obj}), encoding='utf-8')
                    sys.exit('%s: POST HTTP %s; not retried' % (name, status))
                if status != 200 or not obj.get('task_id'):
                    sys.exit('%s: POST HTTP %s: %s' % (name, status, obj))
                task_id = obj['task_id']; source = 'new'
                pending.write_text(json.dumps({'name': name, 'task_id': task_id, 'model': MODEL,
                                               'dashboard_link': obj.get('dashboard_link')}), encoding='utf-8')
            result = poll(task_id)
            if not result.get('dashboard_link'):  # the link may come with the POST's answer rather than the result
                link = json.loads(pending.read_text(encoding='utf-8')).get('dashboard_link')
                if link:
                    result['dashboard_link'] = link
            done.write_text(json.dumps({'name': name, 'task_id': task_id, 'result': result}, ensure_ascii=False), encoding='utf-8')
            pending.unlink()
        line = {'name': name, 'sha256': sha, 'words': len(text.split()), 'headline': result.get('headline'),
                'prediction_short': result.get('prediction_short'), 'fraction_ai': result.get('fraction_ai'),
                'fraction_ai_assisted': result.get('fraction_ai_assisted'), 'fraction_human': result.get('fraction_human'),
                'version': result.get('version'), 'source': source, 'dashboard_link': result.get('dashboard_link'),
                'utc': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}
        with open(out / 'results.jsonl', 'a', encoding='utf-8') as f:
            f.write(json.dumps(line, ensure_ascii=False) + '\n')
        if show_windows:
            line['windows'] = [[w.get('label'), w.get('confidence'), w.get('word_count'), w.get('start_index'),
                                w.get('end_index'), w.get('text')] for w in result.get('windows') or []]
        print(json.dumps(line, ensure_ascii=False), flush=True)
        if expect and str(result.get('version')) != expect:
            sys.exit('%s: version %r, expected %s; the result is saved in %s, and nothing after it was sent'
                     % (name, result.get('version'), expect, done))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('probe')
    c = sub.add_parser('check'); c.add_argument('texts'); c.add_argument('outdir'); c.add_argument('--names')
    c.add_argument('--expect', help='stop after a result of another version (it is saved first)')
    c.add_argument('--windows', action='store_true', help="add each result's windows to its printed line")
    c.add_argument('--public', action='store_true', help="ask for a public Pangram page of each new result (its link is printed)")
    a = ap.parse_args()
    if a.cmd == 'probe':
        sys.exit(0 if probe() else 1)
    check(a.texts, a.outdir, a.names.split(',') if a.names else None, a.expect, a.windows, a.public)


if __name__ == '__main__':
    main()
