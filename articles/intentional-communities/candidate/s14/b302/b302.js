const items = [["S14v2-P567", () => "Institutions and the relationships that make them up don\u2019t have to die at the same time. What a relief! American Commune follows two sisters who grew up on The Farm. When one of them later became ill, former members who hadn\u2019t seen her in years reached out with support. The communal economy they were born into had changed dramatically, but the bonds hadn\u2019t vanished.\n\nMy father carried the Bruderhof with him long after he left it. It shaped the foundation he started, the film he made, the places he took me, and the questions I\u2019m still asking.\n\nEven if the legal entity dies, some of what people learned to give one another can go on. That gives me hope.", "d2cd80413192dc644722d076c7c04c587ccc70fe0e7e9ef67cfc8c6b24ee0424"]];
window.__B302 = [];
const log = m => window.__B302.push(m);
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
