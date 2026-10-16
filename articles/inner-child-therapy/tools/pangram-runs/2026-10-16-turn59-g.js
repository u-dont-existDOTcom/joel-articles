const items = [["t59g_p9c", () => "The Guide can also point you toward a kind of belonging that doesn't cost you yourself. For some people that's nature, or just being alive at all. For others it's whatever their tradition calls ultimate, God, say, or the Tao. That stops being just an idea once you've spent real time outside, or a long while in prayer or meditation. And with that underneath you, the group chat going quiet stops feeling like the end of the world.", "297eed15ddc6d42c0753badbe89f11981bb1e9d9f3946c08ed38f00887d3fe34"], ["t59g_p10b", () => "Call this part of you whatever you like, by the way. Some people go with the Wise One or their inner teacher. Some like \"Guru,\" and some who got out of a cult would rather never hear that word again, which is fair. Whatever you call it, its job is to point past itself and past whoever's approving of you this week, so your little one doesn't take that kind of approval for the deepest place it belongs.", "92ae114ea5c7f24a753c7a83038bbca3701805eccfd0f90bbd8f125f3cd5c07d"]];
window.__t59g = [];
const log = m => window.__t59g.push(m);
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
