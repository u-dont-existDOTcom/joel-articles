#!/usr/bin/env python3
"""pangram_api_check.py - run Pangram checks through Joel's API key, the lab's way.

Joel made a Pangram account with an API key on 2026-10-03 (the dashboard's credits had run out).
The key stays on his laptop: run this there (Desktop Commander), never in the cloud container,
and never print, log, commit or copy the key. The key file's path comes from the environment
variable PANGRAM_KEY_FILE; it isn't written in the repo.

The texts come from a pushed run file (articles/<article>/tools/pangram-runs/<file>.json, a JSON
object of key -> text), fetched from raw.githubusercontent.com at a commit, so what's checked is
exactly what the repo records. Log a prediction in PREDICTIONS.md and push before running.

The lab's rules: one POST per text, model "pangram-4", no automatic repost after a failed or
ambiguous POST, check that every result's version is 4.0, and record each task id.

Usage (on the laptop, from the lane folder):
  PANGRAM_KEY_FILE=... python3 pangram_api_check.py --sha COMMIT --run articles/A/tools/pangram-runs/F.json [KEY ...]
  python3 pangram_api_check.py --sha COMMIT --run ... --dry-run   (fetch and list the texts, no POST)
"""
import argparse
import json
import os
import sys
import time
import urllib.request

BASE = 'https://text.external-api.pangram.com'
RAW = 'https://raw.githubusercontent.com/u-dont-existDOTcom/joel-articles/%s/%s'


def get(url, headers=None, data=None, method=None):
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--sha', required=True, help='the pushed commit the run file is read from')
    ap.add_argument('--run', required=True, help='the run file, relative to the repo root')
    ap.add_argument('keys', nargs='*', help='which texts to check (default: all, in file order)')
    ap.add_argument('--dry-run', action='store_true', help='fetch and list the texts without checking')
    ap.add_argument('--wait', type=int, default=240, help='seconds to poll each task (default 240)')
    a = ap.parse_args()
    texts = get(RAW % (a.sha, a.run))
    keys = a.keys or list(texts)
    missing = [k for k in keys if k not in texts]
    if missing:
        sys.exit('not in the run file: %s' % ', '.join(missing))
    if a.dry_run:
        for k in keys:
            print('TEXT', k, len(texts[k].split()), 'words')
        return
    path = os.environ.get('PANGRAM_KEY_FILE')
    if not path:
        sys.exit('set PANGRAM_KEY_FILE to the key file Joel named')
    with open(path) as f:
        key = f.read().strip()
    headers = {'x-api-key': key, 'Content-Type': 'application/json'}
    for k in keys:
        body = json.dumps({'text': texts[k], 'public_dashboard_link': False, 'model': 'pangram-4'}).encode()
        try:
            r = get(BASE + '/task', headers, body, 'POST')
        except Exception as e:  # no repost: an ambiguous failure may still have made a task
            print('POST_FAILED', k, type(e).__name__, str(e)[:300], flush=True)
            continue
        tid = r.get('task_id') or r.get('id')
        print('POSTED', k, len(texts[k].split()), 'words', tid, flush=True)
        res, t0 = None, time.time()
        while time.time() - t0 < a.wait:
            time.sleep(3)
            try:
                g = get(BASE + '/task/' + str(tid), headers)
            except Exception as e:
                print('POLL_ERR', k, type(e).__name__, str(e)[:200], flush=True)
                continue
            if g.get('stage') in ('STAGE_SUCCESS', 'STAGE_FAILED'):
                res = g
                break
        if res is None:
            print('TIMEOUT', k, tid, '(read it later with GET /task/<id>; do not repost)', flush=True)
            continue
        out = {'key': k, 'task': tid, 'stage': res.get('stage'), 'version': res.get('version'),
               'headline': res.get('headline'), 'prediction_short': res.get('prediction_short'),
               'fraction_ai': res.get('fraction_ai'), 'fraction_human': res.get('fraction_human'),
               'windows': [{'label': w.get('label'), 'confidence': w.get('confidence'),
                            'words': w.get('word_count'), 'start': w.get('start_index'),
                            'begins': (w.get('text') or '')[:60]} for w in res.get('windows', [])]}
        if res.get('version') != '4.0':
            out['WARNING'] = 'version is not 4.0'
        print('RESULT', json.dumps(out, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
