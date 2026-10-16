const items = [["t58a_p5m1", () => "The Guide doesn't need to know how things will turn out. Will the new job work out? Will they ever text back? Nobody knows yet, and the Guide can still pick the next step that makes sense and fits what you care about. You don't need a five-year plan to know the library books are due.", "8140669d17ebb43d405f40058260281f0c67795b75f08499bd8fa09a9f422e88"], ["t58a_p6m1", () => "Some problems have a next step you can take today, and some just can't move yet. Say the car needs a part that's on back order. Waiting for it isn't you being lazy or avoiding anything, so it's fine to let that one sit. Just don't tape the old part back on and pretend it's fixed. Remember what you're waiting on and what would get things moving again (the shop calling to say it's in), and spend your energy on something else that can move in the meantime.", "8469f8838eb1d20572d5f259351993c966b5384e632f659d83a4bafa9e7a9376"], ["t58a_p7m1", () => "When a few things go wrong at once, one can be stuck while another still has a next step. So which one gets you today? I'd go with whatever helps most with what you're going for and can move now, unless something else is due tomorrow. If it's all one big scramble, say what's going on in one sentence and pick one thing to do next. That's plenty. Only stop to work something out if the answer would change what that one thing is.", "7a56d83fc37e466f81fa6da0e92240c2100185d5c6e5be820098e4063862f96b"]];
window.__t58a = [];
const log = m => window.__t58a.push(m);
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
