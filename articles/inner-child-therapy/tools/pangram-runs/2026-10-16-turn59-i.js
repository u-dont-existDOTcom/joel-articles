const items = [["t59i_p9e", () => "Not every bargain is with people, though. The Guide can point your little one toward somewhere it belongs no matter what, without signing anything away. That might be a forest you love, or just the fact of being here at all. It might be God or the Tao, whatever your tradition puts at the very bottom of things. You'll know it better from an afternoon by the river than from reading about it, and a long sit in prayer or meditation works too. Once that's under your feet, losing a friend's approval still hurts, but it doesn't feel like life or death anymore.", "fcf26cc9508d0f74c2fcf23f8dc8f5ce87193360390f03ed16d99209a9e09cf8"], ["t59i_p9f", () => "Not every bargain is with people, though. The Guide can point your little one toward somewhere it belongs no matter what, without signing anything away. That might be a forest you love, or just the fact of being here at all. It might be God or the Tao, whatever your tradition puts at the very bottom of things. You'll know it better from an afternoon by the river than from reading about it, and a long sit in prayer or meditation works too. Once that's under your feet, losing a friend's approval still hurts, but it doesn't feel like life or death anymore. (And if \"the Guide\" doesn't sound right, call it the Wise One or your inner teacher. \"Guru\" is fine too, as long as the word doesn't come with a cult attached for you.)", "63cd703ece15da97fabdfc410456815d98b8bf1b62811933057efb695be50f87"], ["t59i_p10e", () => "If \"the Guide\" doesn't sound right to you, call it something else, like the Wise One or your inner teacher. \"Guru\" is fine too, as long as that word doesn't come with a cult attached for you. Whatever you call it, its job is to point past itself, so your little one doesn't take somebody's approval for the deepest place it belongs.", "6d8c2de9c6e8176295272ea4e86f65bcedd2c84a0dce14f39ff7489d278d77ef"]];
window.__t59i = [];
const log = m => window.__t59i.push(m);
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
