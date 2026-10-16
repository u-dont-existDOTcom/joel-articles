const items = [["t59c_p8h", () => "I don't think the Buddha expected anybody to be the spotless-minded type, either. He said kamma is what you intend, and he taught monks several ways to deal with a nasty thought that's already there, like turning to something better, or just not giving it any attention. Then there's the king who'd killed his own father to get the throne. He felt bad enough about it that he finally owned up to the Buddha, who told him that seeing it was wrong, making amends and holding back from then on is how a person grows in the practice. Feeling that bad about something you chose to do can sometimes mean something needs your attention. A jingle that just popped up isn't in that league.", "60b056d4adeac85a21e5e4a11ca51af3dd95b58b578b9233dbe1c7af96c32767"], ["t59c_p8i", () => "A king who'd killed his own father to get the throne felt bad enough about it that he finally owned up to the Buddha. The Buddha told him that seeing it was wrong, making amends and holding back from then on is how a person grows in the practice. Feeling that bad about something you chose to do can sometimes mean something needs your attention. A jingle that just popped up isn't in that league. I don't think the Buddha expected anybody to be the spotless-minded type. He said kamma is what you intend, and he taught monks several ways to deal with a nasty thought that's already there, like turning to something better, or just not giving it any attention.", "129478d557ba12f5aacf5d874858f6847c136c759edd13af9bbe21c43a1f7b8f"], ["t59c_p8k", () => "I don't think the Buddha expected anybody to be the spotless-minded type, either. He said kamma is what you intend, and he taught monks several ways to deal with a nasty thought that's already there, like turning to something better, or just not giving it any attention. Then there's the king who'd killed his own father to get the throne. He felt bad enough about it that he finally owned up, and the Buddha told him that's how a person grows in the practice: you see it was wrong, you make amends, and you hold back from then on. So feeling that bad about something you chose to do can sometimes mean something needs your attention. A jingle that just popped up isn't in that league.", "c3046e03df9ad32009aff0c1e0495eac9e600f4bc21613a3aa53f1aa879ed508"], ["t59c_p8m", () => "I don't think the Buddha expected anybody to be the spotless-minded type, either. He said kamma is what you intend, and he taught monks several ways to deal with a nasty thought once it's already there. Then there's the king who'd killed his own father to get the throne. He felt bad enough about it that he finally owned up to the Buddha, who told him that seeing it was wrong, making amends and holding back from then on is how a person grows in the practice. Feeling that bad about something you chose to do can sometimes mean something needs your attention. A jingle that just popped up isn't in that league.", "02557b387086e25cbc4e10b328cea66f56d4db5aac4ac50f8b1f66d2e5b02841"], ["t59c_p8n", () => "I don't think the Buddha expected anybody to be the spotless-minded type, either. He said kamma is what you intend. He also taught monks several ways to deal with a nasty thought once it's already there, and you wouldn't bother with that if nobody ever had one. And when a king who'd killed his own father to get the throne finally owned up to it, the Buddha told him that seeing it was wrong, making amends and holding back from then on is how a person grows in the practice. Feeling that bad about something you chose to do can sometimes mean something needs your attention. A jingle that just popped up isn't in that league.", "6e0d3b1369bad8240db3286a1cd5c6c7f6064209a5f87a83e66c8bc80702b82b"]];
window.__t59c = [];
const log = m => window.__t59c.push(m);
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
