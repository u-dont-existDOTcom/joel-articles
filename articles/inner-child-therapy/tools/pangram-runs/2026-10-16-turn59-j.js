const items = [["t59j_p9g", () => "Picture your crew from work, or your church, deciding tomorrow that you're out. I'd want your little one to have somewhere it belongs that can't vote it out. For some people that's the ocean, or just being alive at all. For others it's God or the Tao, whatever their tradition puts at the very bottom of things. The Guide can point you there, and long walks outside will make it more than an idea, the same as prayer or meditation will. Getting voted out would still hurt, but it wouldn't be life or death.", "c59952b44b770bec4437d0bf739f2b4d986fe2d7d41b5059b3788741a54b1826"], ["t59j_p10f", () => "I keep saying \"the Guide,\" but you can call it whatever you like. The Wise One works, or your inner teacher, and \"Guru\" is fine unless that word comes with a cult attached for you. Either way it's pointing past itself, and past whoever's handing out approval this week, so your little one doesn't confuse being liked with the deepest place it belongs.", "a9184020e79f9f9286da4cc18d19ed05de776490f0e75c486486dfd02ad57830"]];
window.__t59j = [];
const log = m => window.__t59j.push(m);
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
