const items = [["t62e_w2p8", () => "The Guide also points beyond itself, toward a belonging deeper than any group. That might be nature, or existence itself. It might be whatever your tradition sees as ultimate (that part is optional, and maybe your life already gives you enough love and meaning without it). Love can come from any of these places, and you also belong there, which is a little different. The way in is time in nature and contemplative practice, like meditation. Once you have that ground under you, belonging with people gets less desperate, because your little one stops mistaking approval you have to keep earning for the deepest belonging. The Guide watches out for that mix-up, for the moment your little one starts thinking, \"If they stop liking me, I won't belong anywhere.\"", "b7ec9df96a852f4c59ebd4fdfe6051f6b3890d5646c829ca8ce32e2e932c44ea"], ["t62e_w2p8b", () => "The Guide also points beyond itself, toward a belonging deeper than any group. That might be nature, or existence itself. It might be whatever your tradition sees as ultimate (that part is optional, and maybe your life already gives you enough love and meaning without it). Love can come from any of these places, and you also belong there, which is a little different. The way in is time in nature and contemplative practice, like meditation. Once you have that ground under you, belonging with people can get a lot less desperate, as your little one stops mistaking approval you have to keep earning for the deepest belonging. The Guide watches out for that mix-up, for the moment your little one starts thinking, \"If they stop liking me, I won't belong anywhere.\"", "bc4ea949d021b15764259449eb809b2a10928314eb92eb13bf8847e644624828"]];
window.__t62e = [];
const log = m => window.__t62e.push(m);
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
