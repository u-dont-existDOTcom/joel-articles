const items = [["t59b_p8e", () => "I don't think the Buddha would hold the jingle against you, either. He said kamma is what you intend, and he gave monks a whole set of ways to handle a nasty thought that's already there, like thinking about something better instead, or just not paying it any attention. A king who'd killed his own father got a hearing, too. When the king owned up, the Buddha told him that seeing what you did wrong as wrong, making amends and holding back from then on is how a person grows in the practice. None of that asks you to be some pure-minded person. If you feel bad about something you chose to do, that can sometimes be worth listening to; a jingle that just showed up is another story.", "18a2e43ffd024e33c4b9169aac6da582ae7c3d7652abfc9501112f55ce304600"], ["t59b_p8f", () => "Once, a king who'd killed his own father came to see the Buddha. When the king owned up to it, the Buddha told him that seeing what you did wrong as wrong, making amends and holding back from then on is how a person grows in the practice. So I don't think he'd hold a jingle against you. He said kamma is what you intend, and he gave monks a whole set of ways to handle a nasty thought that's already there, like thinking about something better instead, or just not paying it any attention. None of that asks you to be some pure-minded person. Feeling bad about something you chose to do can sometimes be worth listening to; a jingle that just showed up is another story.", "761a2408e489d68168f4181c5567ab9cb81d8aed22b5de7d034a6f161caec053"], ["t59b_p8g", () => "I don't think the Buddha would hold the jingle against you, either. He said kamma is what you intend. For a nasty thought that's already there, he gave monks a whole set of things to try, like thinking about something better instead, or just not paying it any attention. And when a king who'd killed his own father owned up to it, the Buddha said seeing what you did wrong as wrong, making amends and holding back from then on is how a person grows in the practice. None of that asks you to be some pure-minded person. Feeling bad about something you chose to do can sometimes be worth listening to, though a jingle that just showed up is another story.", "5ca70b54e88a9b655947ae8ae4e398d5a2968d89121db6c3bb5cb4d65815c56d"]];
window.__t59b = [];
const log = m => window.__t59b.push(m);
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
