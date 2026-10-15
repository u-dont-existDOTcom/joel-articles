const items = [["t57e_p3m2b", () => "I think the opposite trap can feel a lot like finally having your act together. It's forced adulthood, and it sounds like \"Nope, all good!\" from somebody with a fever who's cleaning the whole kitchen anyway. Not a lot of fun in that kitchen, and nobody gets very close to the person in it. If that's you, clamping down harder is going to feel like the fix, but it's just more of the same. I'd try croaking, \"Could you pick up some soup?\" Or maybe, \"I'd really like to just watch a movie with you.\"", "84dc8ea3f95401f28ea14757ea867c293c05a90ab278e8ba102daf2e2fe60907"], ["t57e_p4w2b", () => "Once a need does show, after all that hiding, it's okay to want a lot of closeness. Then someone you love goes for a walk alone, and you've sent \"hello??\" before they've reached the corner. Look at how you're going about getting the need met, since demanding instant replies, or making someone pay for needing space, is another matter. The Guide helps you find a way that leaves room for both of you. But give the need a fair hearing first: I think your little one wants to know they're coming back.", "62d61e2f01870142fb486e600d8b9aa8f2c64144388f6e2eb7dd9738f33ead71"]];
window.__t57e = [];
const log = m => window.__t57e.push(m);
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
