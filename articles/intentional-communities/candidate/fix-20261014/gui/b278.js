const items = [["J4-orig-pair", () => "Inner-child reparenting means learning to identify as the best inner adult, which is comprised of the three inner adult roles: Nurturer, Protector, and Guide. The newly developed adult reparents their newly recognized inner child. The child receives all that love, protection, and guidance that you give it, and in this process actually gains more freedom to remain alive inside you.\n\nAnd it's built on somatic regulation first. Listening to the body's feelings before making a decision with the mind. And that actually symbolizes the adult/child relationship to me in some way as well.", "115e7cf081f253470e4fcaa322960bcbb24032aa333ff3638488ac8c0cf4ab5b"], ["J4-reparent", () => "Inner-child reparenting means learning to identify as the best inner adult, which is comprised of the three inner adult roles: Nurturer, Protector, and Guide. The newly developed adult reparents their newly recognized inner child. The child receives all that love, protection, and guidance that you give it, and in this process actually gains more freedom to remain alive inside you.", "a6c75de1e3341123349e30b8b6961aa5491e86f8a7d3604db97c849544291107"]];
window.__B278 = [];
const log = m => window.__B278.push(m);
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
