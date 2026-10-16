const items = [["t60b_p5v4", () => "The Guide doesn't need certainty, which is good news, because the future usually stays unknown. It just chooses the next sane step that fits your values, and that's how it helps your little one grow toward a whole life. Some problems really are blocked for a while (you're waiting on somebody else's decision, say). That's not a lack of motivation, and it isn't avoidance either, so don't bother forcing a workaround that pretends the block isn't there. Keep an eye on what would open it back up, and meanwhile put your energy into something else that matters and can move. One stuck thing doesn't have to put your whole life on hold.", "185f7e7ebbc652f3cde7c7692fc26592d41fcd8e9271f149590e610ffdfcdee5"], ["t60b_p5v5", () => "The Guide doesn't need certainty, which is lucky, because some things just can't move yet. It picks the next sane step that fits your values while the future's still unknown, and that's how it helps your little one grow toward a whole life. When a problem really is blocked for now (you're waiting on someone else's decision, say), that's not a lack of motivation or avoidance, and there's no use forcing a workaround that pretends the block isn't there. Keep in mind what would open it back up, and meanwhile put your energy into something else that matters and can move. One stuck problem doesn't have to put your whole life on hold.", "47f1192a41960b65071592e5f6b6d39fadd07981fb67a2a45046b85b1a3c1f86"]];
window.__t60b = [];
const log = m => window.__t60b.push(m);
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
