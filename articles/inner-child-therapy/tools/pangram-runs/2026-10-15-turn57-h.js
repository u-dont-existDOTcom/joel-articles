const items = [["t57h_p4w2e", () => "Once a need does show, after all that hiding, it's okay to want a lot of closeness. Then someone you love goes for a walk alone, and you've sent \"hello??\" before they've reached the corner. When they get back, maybe you go quiet on them for the rest of the night. The need's fine. That's just not a great way to meet it. The Guide can help you find one that works for you and leaves them their walk, like a hug at the door and a \"see you in an hour.\" Hear the need out first, though. I think your little one just wants to know they're coming back.", "4efc2c75f8c48ecfbc22b1a972aed4d6acf535d2b70d5b532d3d979e1188c131"], ["t57h_p4w2f", () => "Once a need does show, after all that hiding, it's okay to want a lot of closeness. Then someone you love goes for a walk alone, and you've sent \"hello??\" before they've reached the corner. And when they get back, you go quiet on them all night. Look at how you're going about getting the need met, too. The Guide can help you find a way that leaves room for both of you, like a hug at the door and a \"see you in an hour.\" But give the need a fair hearing first: I think your little one wants to know they're coming back.", "b5e5166661323bff6b0b6ff930e0911bc2c60e232aadebc2cb9b518fc373f21a"], ["t57h_p4w2g", () => "Once a need does show, after all that hiding, it's okay to want a lot of closeness. So then someone you love goes for a walk alone, and you've texted \"hello??\" before they're at the corner. When they get back, you sulk all night. Wanting them close is fine! The texts and the sulking aren't, and the Guide can help you find something that leaves room for both of you, like a hug at the door and a \"see you in an hour.\" But hear your little one out first. I think it just wants to know they're coming back.", "123776b82c2b7db83a34c53e81155800d2907eda4e178fef39a9f6a64b0054ef"]];
window.__t57h = [];
const log = m => window.__t57h.push(m);
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
