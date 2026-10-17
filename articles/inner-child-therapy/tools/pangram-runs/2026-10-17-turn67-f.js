const items0 = [["t67f_le2f2g", () => "Meanwhile, the grown-up you still has plenty to do: keep your body and your routines going, and grieve what ended with your little one beside you. That's a lot steadier than grabbing a new identity just because the not-knowing is unbearable, so don't force one. And if it helps, mark the ending with something practical or a small ritual, like boxing up the old keys. Nobody needs to know the next beginning for that.", "ae5ede5a4c757cebc16794e7e000a48f14ef836e1406f2412b82fca58a013b7a"], ["t67f_le2f2h", () => "When the not-knowing gets unbearable, a new identity can look like the way out. Don't force one. Mark the ending instead, if that helps, with something practical or a small ritual (like boxing up the old keys), and leave the next beginning blank for now. Keep your body and your routines going while the next life takes shape, and grieve what ended with your little one beside you.", "e74e716faa3e3211a827c608edf50e10add24ecd5eb3de426496bd797e8d4b7f"], ["t67f_le3am", () => "\"I miss you\" can turn into \"I love you,\" if the love's there. That's one way to use the ache of missing someone, as a cue for love, so it doesn't become one more problem to solve. Don't push it away, then. You could also send a simple wish: \"May you be safe. May you be held in love.\" Picture them if you like, or just feel the care going their way.", "64b31950e5833b5ab9c764a0f77141eea1c742cec94998a38e5d8f464e09bb58"], ["t67f_le3an", () => "When you miss someone, let the ache be a cue for love. It doesn't have to become one more problem to solve, and pushing it away won't help. If love's there, \"I miss you\" becomes \"I love you.\" Or there's the loving-kindness wish: \"May you be safe. May you be held in love.\" You can picture them. Or don't, and just feel the care going their way.", "a1730441077a7547d2d9876f4b0d2866b31f749e543f91a4010904c8561fbb95"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "t67f" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__t67f = [];
const log = m => { window.__t67f.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__t67f)); } catch (e) {} };
const other = () => { try { return JSON.parse(localStorage.getItem(lane(rev ? 'fwd' : 'rev')) || '[]').filter(m => / (clicked|taking)$/.test(m)).map(m => order0.indexOf(m.split(':')[0])); } catch (e) { return []; } };
const setter = Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value').set;
const sha = async t => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))).map(b => b.toString(16).padStart(2, '0')).join('');
const button = () => [...document.querySelectorAll('button[type=submit]')].find(b => /check for ai/i.test(b.innerText));
const wait = ms => new Promise(r => setTimeout(r, ms));
async function run() {
  for (const [k, mk, want] of items) {
    const o = other(), i = order0.indexOf(k);
    if (o.length && (rev ? i <= Math.max(...o) : i >= Math.min(...o))) { log('stop at ' + k + ': the other tab has the rest'); break; }
    log(k + ': taking');  // claimed before the work, so the other tab never takes it too (turn 65: with a margin
                          // of one instead, both tabs stopped short of the last check)
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
