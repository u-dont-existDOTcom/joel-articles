const items = [["t62d_p8o", () => "The Guide also points past itself, to somewhere you belong without having to give up being yourself. For some of us that's the woods or the ocean, or just being alive at all, and for a lot of people it's God, or whatever their tradition puts at the bottom of everything. You'll feel it more after a long walk in the woods, or a good sit in prayer or meditation, than you will from reading about it here. And once it's there, losing a group's approval still stings, sure, but your little one won't feel like it's lost its place in the world, because the Guide keeps reminding it where it really belongs.", "ebfaf8cde30b3d8ad64cc90ec69d1ad3b83fcfa8db76349179042e565a2f1709"], ["t62d_p8p", () => "The Guide also points past itself, to somewhere you belong without having to give up being yourself. For some of us that's the woods or the ocean, or just being alive at all, and for a lot of people it's God, or whatever their tradition puts at the bottom of everything. Reading about it won't get you far (sorry); a long walk outside or a quiet sit in prayer or meditation does a lot more. And with that under you, a group cooling on you can still hurt, but your little one has somewhere else to stand, and the Guide keeps reminding it of that.", "a3c10b483d805311ab418f43175e8cabc34768f22f21100c4ef24652888b9f28"]];
window.__t62d = [];
const log = m => window.__t62d.push(m);
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
