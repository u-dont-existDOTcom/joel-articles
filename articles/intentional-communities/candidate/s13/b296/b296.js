const items = [["S13v20-4P6", () => "How do you know? At each stage, always judge people based on their conduct. No matter how good it sounds when they talk about their spirituality or their therapy, don\u2019t go by that. It\u2019s too easy to go by vibes. It\u2019s also easy to mistake people just doing what everyone else is doing for safety. Even giving it six months will give you more data, but there\u2019s still no \u201cgood person\u201d detector.", "e6cccc90f8c6f451a23158cc8e2c741a4f594ba3b2937b209f5978168e9f9a7e"], ["S13v20-5P4", () => "Also agree on a mediator or ombud in advance. Why bother? People often do not trust someone who they have not met, and who appears at the time of a crisis to act as a \u2018neutral stranger\u2019. Remember that mediation is about trying to restore good relations between people. It does not remove the need for evidence, for safeguarding, for a ruling, or for a final separation when consent to continue in a shared life is no longer present.", "323315fafc01d13ecd1a00239df8b7483062dd5d796dcd9f4fbbbefce61d0910"]];
window.__B296 = [];
const log = m => window.__B296.push(m);
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
