import json, hashlib, sys
# usage: python3 tools/humanization/pangram_batch_gen.py drafts.json out.json key1 key2 key3 [--url RAW_URL] [--wait N]
#   (drafts.json maps keys to texts; each key's text is checked as-is)
#   --url: the page fetches the texts from RAW_URL (the same drafts.json, pushed; use a commit's
#   raw.githubusercontent.com address) instead of carrying them in the batch. The batch stays small,
#   and the SHA-256 of each text, taken here from the local file, is still checked before the click.
#   Pangram's dashboard can fetch from raw.githubusercontent.com (tested 2026-10-01).
#   --wait N: seconds to wait for each result before reading it (default 7; the tool's maximum is 10).
args = sys.argv[1:]
url = None
wait = 7
if '--url' in args:
    i = args.index('--url'); url = args[i + 1]; del args[i:i + 2]
if '--wait' in args:
    i = args.index('--wait'); wait = int(args[i + 1]); del args[i:i + 2]
d = json.load(open(args[0], encoding='utf-8'))
acts = []
for k in args[2:]:
    T = d[k]
    h = hashlib.sha256(T.encode('utf-8')).hexdigest()
    src = ("const T = (await (await fetch(" + json.dumps(url) + ", {cache: 'no-store'})).json())[" + json.dumps(k) + "]; ") if url else ("const T = " + json.dumps(T) + "; ")
    fill = (src + "const ta = document.querySelector('textarea'); "
            "const setter = Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value').set; "
            "setter.call(ta, T); ta.dispatchEvent(new Event('input', {bubbles: true})); "
            "await new Promise(r => setTimeout(r, 400)); "
            "const h = Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(ta.value)))).map(b => b.toString(16).padStart(2, '0')).join(''); "
            f"if (h !== '{h}') {{ throw new Error('hash mismatch {k} ' + h); }} "
            "const btn = [...document.querySelectorAll('button[type=submit]')].find(b => /check for ai/i.test(b.innerText)); btn.click(); "
            f"'clicked {k}'")
    read = ("await new Promise(r => setTimeout(r, 1200)); const b = document.body.innerText; const i = b.indexOf('words scanned'); "
            "const red = [...document.querySelectorAll('*')].filter(e => /255, 86, 48/.test(getComputedStyle(e).backgroundColor) && !/255, 86, 48/.test(getComputedStyle(e.parentElement).backgroundColor)).map(e => e.innerText); "
            f"JSON.stringify({{{json.dumps(k)}: i < 0 ? 'NOT READY' : b.slice(Math.max(0, i - 40), i + 70), red: red}})")
    acts += [{"name": "navigate", "input": {"url": "https://www.pangram.com/dashboard", "tabId": "seed"}},
             {"name": "computer", "input": {"action": "wait", "duration": 2, "tabId": "seed"}},
             {"name": "javascript_tool", "input": {"action": "javascript_exec", "text": fill, "tabId": "seed"}},
             {"name": "computer", "input": {"action": "wait", "duration": wait, "tabId": "seed"}},
             {"name": "javascript_tool", "input": {"action": "javascript_exec", "text": read, "tabId": "seed"}}]
json.dump(acts, open(args[1], 'w', encoding='utf-8'))
print(len(acts), 'actions')
