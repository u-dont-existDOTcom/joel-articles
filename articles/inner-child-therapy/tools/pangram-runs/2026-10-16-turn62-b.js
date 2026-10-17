const items = [["t62b_p8j", () => "Picture your crew from work, or your church, deciding tomorrow that you're out. I'd want your little one to have somewhere it belongs that can't vote it out, and that's where the Guide points: a belonging that doesn't require betraying yourself. That might be nature, or existence itself, or whatever your tradition recognizes as ultimate. Time outside and contemplative practice make it more than another nice idea. And that ground can make belonging with people a lot less desperate (not overnight), as the Guide keeps reminding your little one that a group's approval isn't the deepest place it belongs.", "ae3c4f81148438e236087fdbb68e535d6656a98d37003a024ca1a6c949fc0a31"], ["t62b_p8k", () => "The Guide also points beyond itself, toward a belonging that doesn't require betraying yourself. That might be nature, or existence itself, or whatever your tradition recognizes as ultimate (God, the divine, the universe, source, the Three Jewels, the Tao, life). Time outside and contemplative practice make it more than another nice idea, and contemplative practice can be as simple as sitting on a rock for a while. That ground can make belonging with people a lot less desperate over time, as the Guide keeps reminding your little one that a group's approval isn't the deepest place it belongs.", "b3c83ab95f6b31c4a5b97ef7861341a86bdcc7c34c2e68f7e05c46b0d7bf4f30"], ["t62b_p8l", () => "The Guide also points beyond itself, toward a belonging that doesn't require betraying yourself: nature, existence itself, or whatever your tradition recognizes as ultimate. Time outside and contemplative practice make that more than another nice idea. Over time, it can make belonging with people a lot less desperate, because your little one isn't stuck thinking, \"if this group drops me, I'm nobody.\" The Guide keeps reminding it that a group's approval, especially the kind you only keep by performing, isn't the deepest place it belongs.", "6f67282f82d836c8e45352e1648046c7588542c26d6a949f55cf56c062b63d6f"], ["t62b_p9i", () => "Call the Guide whatever you like; the Wise One and your Inner Teacher both work. \"Guru\" works too if the word means something good to you, though if you got out of a cult you'd probably rather skip it, since for a lot of survivors it's a trigger word. What matters more than the name is whether it keeps pointing you past itself.", "de7c136b4aab635b56685abca1629a676e2a33b37a0730d22cdfe407afbe3976"]];
window.__t62b = [];
const log = m => window.__t62b.push(m);
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
