const items = [["t56_ig_p1", () => "As the Guide, you choose what your little one learns and what it gets to experience, and you hold standards, the way a good parent would. You ask hard things of it so it can grow, at its own pace. That's what I was just asking of you, with that new interest. You also widen its world with art and music, and you point out beautiful things when you see them. Nature is part of that, and so is the wider world past the end of the street you grew up on.", "e92def6bae34a58dda5881d2b4a3129dc058c3b89f33a9a0780d03e52ec5f7e6"], ["t56_ig_p12", () => "As the Guide, you choose what your little one learns and what it gets to experience, and you hold standards, the way a good parent would. You ask hard things of it so it can grow, at its own pace. That's what I was just asking of you, with that new interest. You also widen its world with art and music, and you point out beautiful things when you see them. Nature is part of that, and so is the wider world past the end of the street you grew up on.\n\nWithout that kind of direction, reparenting can turn permissive. Candy and screens can pass for self-love. So can escaping anything difficult. In the moment, that one sounds like the kindest thing you could do for your little one: \"Why make it do anything hard?\"", "77c859b0c1ee3d7f13208f307350dbbd818d9fd574890a3389ba3396f0ed19b7"], ["t56_ig_p3", () => "The opposite trap is forced adulthood, where you demand perfect discipline of yourself and have no visible needs, and very little joy or closeness. If you're stuck there, the next adult act may be asking for help or saying what you'd prefer, instead of tightening control again. Either of those can feel like turning into the needy one. Once a need does show, judge the strategy as well as the need: wanting closeness is legitimate, and demanding instant replies or punishing someone for needing space isn't the same thing. The Guide helps you find a workable way to meet the need without erasing you or the other person.", "487ac1857960bc16c06aa0100bb3e1e5ac10d7fae7024959549d5572db7c131a"], ["t56_ig_h1", () => "# The Inner Guide Comes Later\n\nAs the Guide, you choose what your little one learns and what it gets to experience, and you hold standards, the way a good parent would. You ask hard things of it so it can grow, at its own pace. That's what I was just asking of you, with that new interest. You also widen its world with art and music, and you point out beautiful things when you see them. Nature is part of that, and so is the wider world past the end of the street you grew up on.\n\nWithout that kind of direction, reparenting can turn permissive. Candy and screens can pass for self-love. So can escaping anything difficult. In the moment, that one sounds like the kindest thing you could do for your little one: \"Why make it do anything hard?\"\n\nThe opposite trap is forced adulthood, where you demand perfect discipline of yourself and have no visible needs, and very little joy or closeness. If you're stuck there, the next adult act may be asking for help or saying what you'd prefer, instead of tightening control again. Either of those can feel like turning into the needy one. Once a need does show, judge the strategy as well as the need: wanting closeness is legitimate, and demanding instant replies or punishing someone for needing space isn't the same thing. The Guide helps you find a workable way to meet the need without erasing you or the other person.", "2d91d6bc63d3d8328033fbf888573a02403b052ca254465f4f4b3cbf74d9f5cc"]];
window.__t56d = [];
const log = m => window.__t56d.push(m);
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
