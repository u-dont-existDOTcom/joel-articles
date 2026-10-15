const items = [["t58f_p5h3", () => "None of this needs you to know how it'll all turn out, and the Guide doesn't know either. Say the new job might not last. You'd still get some sleep the night before and show up the way you'd want to at any job, since that part's up to you. What comes after, nobody knows yet.", "205cf1cc3b9f94950ad5954ff1379477776f7fb32c61cf75818c8ebe4f87f4b2"], ["t58f_p56a", () => "The Guide doesn't need to know how things will turn out, which is lucky, because some things just can't move yet. Say you're waiting on the landlord's signature before you can sign up for the new place. You're not being lazy, whatever the old parent in your head says, and there's no point forging ahead as if you had it. Write down what you're waiting on, so you'll notice when it comes, and go do the next thing that matters to you and can move today.", "8b8f1700dfae72650d6bf457e33c7a81c169d19094155d445089dd93504e21db"], ["t58f_p7f2", () => "And one stuck thing doesn't mean everything has to wait. Say you're still waiting on that signature and the cat's off her food. The signature can sit, so I'd spend today on the cat: she matters more, and you can do something about her. If it's all one big mess in your head, put it in one sentence and do whatever it says comes first. Anything else can wait unless it'd change that.", "85d4ac0c021dcc78ea300e0a7d968636e0218d085ff15917a5dd1ee7f2750828"], ["t58f_p7f3", () => "One stuck thing doesn't mean everything has to wait, either. Say you're still waiting on that signature and the cat's off her food. The signature can sit. I'd spend today on the cat, since she matters more to you and you can do something about her. And if it's all one big mess in your head, put it in one sentence and do whatever that sentence says comes first; anything else can wait unless it'd change that.", "42229f0d6d8ca58b15ba522e9eb29e09352a9774695353e4b1d8bb4d6dbc686b"], ["t58f_p7h2", () => "Meanwhile, the cat's off her food. One stuck problem doesn't get to hold up the others, so I'd go with whatever matters most to you and can happen today, and right now that's the cat. When your head's too full to sort any of it, say it all in one sentence and do just the first thing. Only work out more if it would change what that first thing is.", "414f57d99ed6bca0738e556298b00ad2e58e54618c1c3944abcfaaba05e00e94"]];
window.__t58f = [];
const log = m => window.__t58f.push(m);
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
