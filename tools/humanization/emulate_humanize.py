#!/usr/bin/env python3
"""Emulate API: a balance check, or one humanize call. Run it on Joel's laptop, where the key lives.

    python3 emulate_humanize.py balance
    python3 emulate_humanize.py humanize IN.txt OUT

`humanize` sends IN.txt as plain text (40 to 3,000 words) and writes Emulate's reply,
exactly as returned, to OUT.txt, with the request and the full response in OUT.json.
It prints one JSON line: the words charged, the balance before and after, and the text.

The key comes from $EMULATE_API_KEY, else the file named by $EMULATE_KEY_FILE, else
/home/joel/ai-work/claude-dangerous-lane/secrets/emulate.key. The key is never printed,
logged or written anywhere.

A call that may have been charged is never repeated by accident: OUT.pending.json is
written before the request and removed only once the reply is saved. If a run dies in
between, the next run for OUT refuses until someone checks the balance and the files.
"""
import argparse
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = 'https://www.tryemulate.ai'
DEFAULT_KEY_FILE = '/home/joel/ai-work/claude-dangerous-lane/secrets/emulate.key'
MIN_WORDS, MAX_WORDS = 40, 3000


def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def api_key():
    key = os.environ.get('EMULATE_API_KEY', '').strip()
    if not key:
        key = Path(os.environ.get('EMULATE_KEY_FILE', DEFAULT_KEY_FILE)).read_text().strip()
    if not key:
        sys.exit('no Emulate key found')
    return key


def call(path, body=None):
    data = None if body is None else json.dumps(body, ensure_ascii=False).encode('utf-8')
    # A named User-Agent: from 2026-10-03 about 04:30 UTC, Emulate's Cloudflare answered Python's default
    # ("Python-urllib/3.12") with error 1010 (HTTP 403, "Access denied"), on the balance check too. The key was fine.
    req = urllib.request.Request(API + path, data=data, headers={
        'Authorization': 'Bearer ' + api_key(), 'Content-Type': 'application/json',
        'User-Agent': 'joel-articles-emulate-humanize/1.0'})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())


def words_left():
    return call('/v1/me')['words_left']


def save(path, record):
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def humanize(src, out):
    if 'E_holdout' in src.resolve().parts:
        sys.exit('refused: E_holdout texts never go to Emulate')
    text = src.read_text(encoding='utf-8').strip()
    n = len(text.split())
    if not MIN_WORDS <= n <= MAX_WORDS:
        sys.exit(f'refused: {n} words; Emulate takes {MIN_WORDS} to {MAX_WORDS}')
    out_txt, out_json, pending = (out.parent / (out.name + s) for s in ('.txt', '.json', '.pending.json'))
    for p in (out_txt, out_json, pending):
        if p.exists():
            sys.exit(f'refused: {p} exists, so a call may already have been charged. '
                     'Check the balance and the saved files, then use a new OUT.')
    record = {'input_file': str(src), 'input_words': n,
              'input_sha256': hashlib.sha256(text.encode('utf-8')).hexdigest(),
              'balance_before': words_left(), 'started_utc': utc(), 'errors': []}
    save(pending, record)
    reply = None
    for attempt in (1, 2):
        try:
            reply = call('/v1/humanize', {'text': text})
            break
        except urllib.error.HTTPError as e:
            record['errors'].append({'attempt': attempt, 'status': e.code, 'utc': utc(),
                                     'body': e.read().decode('utf-8', 'replace')[:500]})
            save(pending, record)
            if attempt == 1 and e.code in (502, 503):
                time.sleep(30)
                continue
            sys.exit(f'HTTP {e.code}; stopped. The record is in {pending}')
    record.update(finished_utc=utc(), response=reply)
    save(out_json, record)
    if not isinstance(reply.get('text'), str):
        sys.exit(f'the reply has no text; it is saved in {out_json}')
    out_txt.write_text(reply['text'], encoding='utf-8')
    record['balance_after'] = words_left()
    save(out_json, record)
    pending.unlink()
    print(json.dumps({'out': str(out_txt), 'charged': (reply.get('words') or {}).get('charged'),
                      'input_words': n, 'output_words': len(reply['text'].split()),
                      'balance_before': record['balance_before'],
                      'balance_after': record['balance_after'], 'text': reply['text']},
                     ensure_ascii=False))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('balance', help='print the words left')
    h = sub.add_parser('humanize', help='one paid call')
    h.add_argument('input', type=Path)
    h.add_argument('out', type=Path, help='output path without an extension')
    a = ap.parse_args()
    if a.cmd == 'balance':
        print(json.dumps({'words_left': words_left(), 'utc': utc()}))
    else:
        humanize(a.input, a.out)


if __name__ == '__main__':
    main()
