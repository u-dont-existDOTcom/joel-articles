import json, hashlib, sys
# usage: gen.py drafts.json out.json key1 key2 key3   (each key's text is checked as-is)
d = json.load(open(sys.argv[1], encoding='utf-8'))
acts = []
for k in sys.argv[3:]:
    T = d[k]
    h = hashlib.sha256(T.encode('utf-8')).hexdigest()
    fill = ("const T = " + json.dumps(T) + "; const ta = document.querySelector('textarea'); "
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
             {"name": "computer", "input": {"action": "wait", "duration": 7, "tabId": "seed"}},
             {"name": "javascript_tool", "input": {"action": "javascript_exec", "text": read, "tabId": "seed"}}]
json.dump(acts, open(sys.argv[2], 'w', encoding='utf-8'))
print(len(acts), 'actions')
