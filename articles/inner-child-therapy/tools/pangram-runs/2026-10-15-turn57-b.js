const items = [["t57b_p3w6", () => "Or did you walk laps around the kitchen every day this week to hit your step count, and chew on one side because of a tooth you haven't told anyone about? Maybe the nicest part of the week was the hairdresser washing your hair. That's forced adulthood, the opposite trap. I'd guess you'll want to tighten your grip again, but asking someone safe to come with you to the dentist might be the next grown-up step. Or telling someone you'd like them to stay longer.", "29508a0d75e825320404fbd40acd8053640c1306ab2b007c708407d3f8ac9cce"], ["t57b_p3w7", () => "Or maybe you answered every email in the recovery room, then told the nurse your ride was downstairs and took the bus. The good tea's still saved for guests, and nobody's been over. That's forced adulthood, the opposite trap. I think this one's harder to spot, since it looks so responsible. You'll probably want to tighten your grip again, but the next grown-up step might be turning to someone safe with \"Could you pick me up after the follow-up?\" or \"I'd like a birthday party this year.\"", "ba8b9ad069231c056a7b09969b006a45cff34e9b7fef2ff7efca7aad4db3dcd8"]];
window.__t57b = [];
const log = m => window.__t57b.push(m);
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
