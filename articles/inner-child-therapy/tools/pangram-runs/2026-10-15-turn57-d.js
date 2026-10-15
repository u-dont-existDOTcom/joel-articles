const items = [["t57d_p3w8c", () => "The opposite trap, forced adulthood, looks more like hauling all the grocery bags up the stairs in one trip while a friend holds the door with nothing to carry. Who needs two trips? You hold yourself to perfect discipline and never let a need show. There isn't much joy in that, or closeness either. Halfway up, with your fingers going purple, all you're thinking about is getting a better grip. The grown-up you might say what you'd like for once, or ask someone safe, \"Could you take the eggs?\"", "da3640f95fe26c1dd410152a01a0c8fd49d2ef76a39fb880c92eda557952627b"], ["t57d_p3w9b", () => "I think the opposite trap is sneakier, since perfect discipline looks so grown-up. You're on your towel twisting one arm up behind you to get sunscreen on the middle of your back, because asking someone would mean letting a need show. Meanwhile everybody you came with is in the water having fun. In forced adulthood, the urge is to try harder alone, maybe with one of those sponges on a long handle. You'll still miss a spot. I'd call someone safe over and say, \"Could you do my back?\" or \"I want to swim too!\"", "2ebb2d71a5231266325ac6ef6be09baa7eeba407b9232435870ef7c89a956159"], ["t57d_p3m2", () => "I think the opposite trap is the sneakier one, since from the outside it just looks like having your act together. It's forced adulthood, and it sounds like \"Nope, all good!\" from somebody with a fever who's cleaning the whole kitchen anyway. Not a lot of fun in that kitchen, and nobody gets very close to the person in it. You'll want to clamp down harder. I'd try croaking, \"Could you pick up some soup?\" Or maybe, \"I'd really like to just watch a movie with you.\"", "654493079d41760fc3604c428b13236e6eb34ef020e27b9b1496d012acc87752"]];
window.__t57d = [];
const log = m => window.__t57d.push(m);
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
