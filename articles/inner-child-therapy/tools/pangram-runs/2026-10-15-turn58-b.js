const items = [["t58b_p5m2", () => "Maybe you're lying awake at night going, \"But what if the new job doesn't work out?\" The Guide doesn't need to know that. It just picks the next step that makes sense and fits what you care about (ironing a shirt for the first day is a perfectly good one), while the rest of it stays unknown, the way it does for everybody.", "337e0f10d7e2ff4a65dc4830b8ad7711aa122a64e5c968227cf73662c4c3ab86"], ["t58b_p6m2", () => "\"I should be doing more about the car.\" Maybe, but if the part's on back order, there's nothing to do except wait for the shop to call, and that isn't laziness or avoiding it. Some problems are like that: everything that matters is stuck on something outside you. So I'd keep an eye on what you're waiting for, and not talk yourself into driving around on the old part as if it were fine. Meanwhile there's probably something else that can move.", "9d895e08da29b87a2e5add0b48510b7f7b602d3f88ea3a9da51353d388f38463"], ["t58b_p7m2", () => "And when the car's stuck and the rent's coming up in the same week, the stuck one doesn't get to stop the other. I'd pick whichever helps most with what you're going for and can move today, unless something else really can't wait. If it all feels like one big tangle, try saying it in one sentence (\"Car's stuck, but the rent can't wait\") and pick one thing to do next. You don't have to work anything else out first, unless the answer would change what that thing is.", "9aec6ddc502f3b90c28369c3ef7db777f96f37c5d75f7e66c66ee876f1dab82f"]];
window.__t58b = [];
const log = m => window.__t58b.push(m);
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
