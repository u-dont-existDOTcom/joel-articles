const items = [["t59h_p9d", () => "You post something in the group chat and nobody answers, so you're checking it every five minutes all evening. I think this is where the Guide points you to a kind of belonging that doesn't cost you yourself. For some people that's nature, or just being alive at all. For others it's what their tradition calls ultimate, God, say, or the Tao. It gets a lot more solid than an idea once you've spent real time outside, and prayer or meditation does it too. With that underneath you, a quiet group chat stops feeling like the end of the world.", "8de8b869e9dc2e7f7611fab6e573ab318e7bf0262b4b021004fc50436fc15d26"], ["t59h_p10c", () => "I've been calling this part the Guide, but call it whatever works for you. Plenty of people would go with \"Guru,\" and plenty who got out of a cult would rather never hear that word again, which is fair enough. The Wise One works, or your inner teacher. Whatever the name, it points past itself, and past whoever happens to be approving of you this week, so your little one doesn't take that for the deepest belonging there is.", "6be526aaf74f94abb7334ec6205d542482d96da13b2d040a47d21b4a5a28d5b7"], ["t59h_p910a", () => "You post something in the group chat and nobody answers, so you're checking it every five minutes all evening. I think this is where the Guide points past itself, and past whoever's approving of you this week, to a kind of belonging that doesn't cost you yourself. For some people that's nature, or just being alive at all. For others it's what their tradition calls ultimate, God, say, or the Tao. It gets a lot more solid than an idea once you've spent real time outside, and prayer or meditation does it too. With that underneath you, a quiet group chat stops feeling like the end of the world, and your little one doesn't have to take somebody's approval for the deepest place it belongs.", "4c7c9a4ee4e79cc30a2944b15c427ce946f2f1612753f209d8fe0809fcec3e28"]];
window.__t59h = [];
const log = m => window.__t59h.push(m);
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
