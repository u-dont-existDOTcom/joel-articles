const items = [["t62c_p8m2", () => "The Guide also points past itself, to somewhere you belong without having to give up being yourself. That might be the woods or the ocean, or just being alive at all. It might be God, if that's your word for it, or whatever your tradition puts at the bottom of everything. You don't get there by thinking about it so much as by spending real time outside, or sitting with it in prayer or meditation. Once that's under you, a group cooling on you can still sting, but it isn't the end of the world anymore, as the Guide keeps showing your little one that it doesn't need the group's thumbs-up to belong.", "c61e27e80519ed20e82cd1ca89f9003abbd348042d10847ed50f8dd615e53fbd"], ["t62c_p8n2", () => "The Guide also points past itself, to somewhere you belong without having to give up being yourself. For some of us that's the woods or the ocean, or just being alive at all, and for a lot of people it's God, or whatever their tradition puts at the bottom of everything. It sinks in when you actually spend time outside, or sit with it in prayer or meditation (reading about it is a start, but only a start). Then a group cooling on you can still sting, but it isn't the end of the world anymore. The Guide keeps showing your little one that it doesn't need the group's thumbs-up to belong.", "a867d529eb9577d57b942baa2be4adcbb50dec432af9a2b5f3c67d500a6306c4"]];
window.__t62c = [];
const log = m => window.__t62c.push(m);
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
