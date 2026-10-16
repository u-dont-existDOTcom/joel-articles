const items = [["t59k_p9h", () => "Picture your crew from work, or your church, deciding tomorrow that you're out. I'd want your little one to have somewhere it belongs that can't vote it out, and that's where the Guide points. Maybe yours is the ocean. If you pray, you probably already know where yours is, and other traditions have their own names for it. If you meditate, it might be the plain fact of being here at all. Reading about it won't do much, though. Long walks outside will, and so will the praying or the sitting. Getting voted out would still hurt, but it wouldn't be life or death.", "bb9fdc118dd9f40f15db3ffbdf9484f4c3abfcca96534debfb9887adf3f3d659"], ["t59k_p9i", () => "Picture your crew from work, or your church, deciding tomorrow that you're out. I'd want your little one to have somewhere it belongs that can't vote it out, and that's where the Guide points. Maybe yours is the ocean. If you pray, you probably already know where yours is, and other traditions have their own names for it. If you meditate, it might be the plain fact of being here at all. Reading about it won't do much, though. Long walks outside will, and so will the praying or the sitting. Getting voted out would still hurt, but it wouldn't be life or death. And call that part of you whatever you like. \"Guru\" works too, if the word doesn't come with a cult attached.", "e14df7e1e6348f499ad0787a56706d89bbebb82395b8ef1df1eb57fa5b04b5da"]];
window.__t59k = [];
const log = m => window.__t59k.push(m);
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
