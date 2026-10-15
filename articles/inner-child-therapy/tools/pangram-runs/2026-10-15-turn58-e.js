const items = [["t58e_p5f", () => "The Guide doesn't have to know how it all turns out before it does anything. Say you're not sure the new job will last. You can still iron a shirt and set the alarm, since showing up ready is who you want to be, and leave the rest as a question mark for now. Nobody gets to know the ending ahead of time anyway.", "b0947c59c7679b7be0e14dba11e80929c3052d60e5c8810289ddbb09ca3a5829"], ["t58e_p5g", () => "The Guide can act without knowing how things will go. Say you've got no idea whether the move will work out. You can still pack up the kitchen tonight, since this is the move you said you wanted, and let tomorrow be tomorrow. That's about as sure as anybody gets.", "3b530e3340aae7219bfe864bf931cc3072a645c931836fcc66010ba71b6fba2f"], ["t58e_p5h", () => "None of this needs you to know how it'll all turn out, and the Guide doesn't know either. Say the new job might not last. You'd still get some sleep the night before and show up the way you want to be at a job, because that part's yours. What happens after that, nobody knows yet.", "30f8e01244247d87be77e6aa5b544f791c10b3ce585a580830bcf43203bcf318"], ["t58e_p7f", () => "And one stuck thing doesn't mean everything has to wait. Say you're still waiting on that signature and the cat's off her food. The signature can sit, so I'd spend today on the cat, since she matters more and you can do something about it. If it's all one big mess in your head, put it in one sentence and do whatever that sentence says comes first. Anything else can wait unless it'd change that.", "70ff8d86b2b8632650a673e0fb39a3e64229af86fbef97d10d729401442368f3"], ["t58e_p7g", () => "The signature being stuck doesn't mean the cat has to wait too. When a few things pile up, I'd pick the one that matters most to you and can move now, and let the stuck one sit. If you're so scrambled you can't pick, say the whole mess in one sentence (\"No signature yet, cat first\") and start there. The rest can wait unless it'd change what you do first.", "d3ef027c4c72dd68ce5faa047c91d60559a2f03561e9e3ad41823578ff95db3e"], ["t58e_p7h", () => "Meanwhile, the cat's off her food. One stuck problem doesn't have to hold up the others, so I'd go with what matters most to you and can happen today, which right now is the cat. When your head's too full to sort it, say it all in one sentence and do just the first thing. You only need to work out more if it would change what that first thing is.", "4083fdae993d8b8105f67bc465cff4769236015b455ace03f18cb813276d5ad5"], ["t58e_p7i", () => "If the signature's stuck, the cat can still go to the vet. Keep the problems separate and pick the one that matters most to you and can move today. When there's too much to sort, I'd say it all in one breath (\"Still no signature, cat first\") and go do that one thing. Leave the other questions alone unless one of them would change it.", "ece7a8197091b3119d41568e9d1834efc1dfcef86eaac0f9474aa8042847516e"]];
window.__t58e = [];
const log = m => window.__t58e.push(m);
const setter = Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value').set;
const sha = async t => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))).map(b => b.toString(16).padStart(2, '0')).join('');
const button = () => [...document.querySelectorAll('button[type=submit]')].find(b => /check for ai/i.test(b.innerText));
const wait = ms => new Promise(r => setTimeout(r, ms));
async function run() {
  for (const [k, mk, want] of items) {
    const T = mk();  // built when its turn comes, so it can use texts stored earlier in this batch
    for (let j = 0; j < 20 && !(button() && document.querySelector('textarea')); j++) await wait(500);
    const ta = document.querySelector('textarea');
    if (!ta) { log(k + ': no textarea'); break; }
    setter.call(ta, T); ta.dispatchEvent(new Event('input', {bubbles: true}));
    let b = null;
    for (let j = 0; j < 30; j++) { await wait(500); b = button(); if (b && !b.disabled) break; }
    const h = await sha(ta.value);
    if (h !== want) { log(k + ': hash mismatch ' + h + ' (is its prefix in sessionStorage?)'); break; }
    if (!b || b.disabled) { log(k + ': button not ready'); break; }
    try { sessionStorage.setItem(k, T); } catch (e) {}
    b.click(); log(k + ': clicked');
    await wait(10000);
  }
  log('end');
}
run(); 'started'
