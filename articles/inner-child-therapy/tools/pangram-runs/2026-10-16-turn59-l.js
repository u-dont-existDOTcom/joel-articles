const items = [["t59l_p9j", () => "Picture your crew from work, or your church, deciding tomorrow that you're out. I'd want your little one to have somewhere it belongs that can't vote it out, and that's where the Guide points. For a lot of people that's the woods behind the house, or the sea. For others it's God, or whatever their tradition puts at the very bottom of things, or just the fact that they're here at all. It sinks in on long walks, and in prayer or meditation, a lot more than it ever does in a book. You'd still be sad about the crew. You just wouldn't feel like you'd stopped existing.", "f99c26cd98ba8ca22a5039de28233309b94c421c079250f6eec0419ec98c8d0f"], ["t59l_p9k", () => "Picture your crew from work, or your church, deciding tomorrow that you're out. I'd want your little one to have somewhere it belongs that can't vote it out, and that's where the Guide points. Some people find that in the woods behind the house. Some find it in God, or in whatever their tradition puts at the very bottom of things, and some in the plain fact of being here at all. It sinks in on long walks, and in prayer or meditation, a lot more than it does in a book. You'd still be sad about the crew, but you wouldn't feel like you'd stopped existing.", "192d70712d2dbc6a06c90ccc4fc87bacc4d9d4a66c6fa68b8ba059ca989ccb1a"]];
window.__t59l = [];
const log = m => window.__t59l.push(m);
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
