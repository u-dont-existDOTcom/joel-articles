const items = [["t60c_p5v6", () => "The Guide doesn't need certainty. It chooses the next sane step that fits your values, even though the future remains unknown, and that's how it helps your little one grow toward a whole life. Some problems are actually blocked for now (like if you need someone else's signature first), and waiting on that isn't a lack of motivation or avoidance. So it's not about forcing some workaround that just pretends the block isn't there. Keep in mind what it would take to get unblocked, and in the meantime put your energy into something else that matters and can move forward. One stuck problem doesn't need to hold your whole life hostage.", "53a29c7e53446a140fd0c54502caf0a35fb12e2d8022ea59b2e16d63f6c72dc3"], ["t60c_p5v7", () => "I don't think the Guide needs certainty. It just chooses the next sane step that fits your values, even though nobody knows how things will turn out, and that's how your little one gets to keep growing toward a whole life. Some problems are blocked for real for a while, like when someone else has to sign off first. Waiting on that isn't laziness or avoidance, so I wouldn't force a workaround that pretends the block isn't there. I'd keep in mind what would get it moving again, and meanwhile put my energy into something else that matters and can move. One stuck thing doesn't have to hold your whole life hostage.", "c8df641e63b78de8a9c5f27bc1a6b6999b7b9d507a79f063813825bd0ad00ba8"]];
window.__t60c = [];
const log = m => window.__t60c.push(m);
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
