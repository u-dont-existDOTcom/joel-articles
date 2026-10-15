const items = [["t56_grat", () => "This is a bit tricky to put into words, but let me try anyway\u2026 You may be suffering now, but you could be suffering more. That\u2019s something to be grateful for. I\u2019m not talking just about changing your \u201cglass half empty\u201d perception to a glass \u201chalf full perception.\u201d I\u2019m not pushing \u201ctoxic positivity.\u201d And I\u2019m certainly not preaching \u201cprosperity philosophy,\" even though it can seem to start at that. We still need to remember that if we can only be thankful for the good things we have, we can fall into the trap of thinking that what we have is happiness itself. I'm ultimately reaching for something much deeper.", "ccddac7f40191d161f14432f446ba539117e937c28404f13582a8b7e0ca952ea"], ["t56_unt_p2", () => "Then there's another bargain, where you have to earn your worth: when you don't feel your value inside, you can become a \"human doer,\" working for it in some arena outside yourself. That might be beauty, athleticism, sexual desirability, intelligence or grades. For some people it's money or status, and for others it's a sophisticated spiritual identity or becoming indispensable to everybody else's problems. It can feel really good to be the one everybody calls. In the more shadowy presentation, when you really need to feel needed, you might be like the firefighters who become arsonists to keep themselves employed.", "7864ba6a011caf2cab7c07150e7bd6489e8185adb198f704489b85aab0ef6bbf"]];
window.__t56a = [];
const log = m => window.__t56a.push(m);
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
