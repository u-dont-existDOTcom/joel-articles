const items = [["t57f_p2", () => "Maybe you've let a small child win at Go Fish and never found a good time to start playing for real. Who wants to be the grown-up who finally wins? Without the Guide, you can slide from looking after your little one into spoiling it the same way. Sweets and screens can pass for loving yourself, and so can getting it out of anything hard.", "3851105b9ed56448ae5c8d284034a079c66d381e123d3bdfa68da003a3381552"], ["t57i_p4", () => "Once a need does show, after all that hiding, it's okay to want a lot of closeness. So then someone you love goes for a walk alone, and you've texted \"hello??\" before they're at the corner. When they get back, you sulk all night. Wanting them close is fine! The texts and the sulking aren't, and the Guide can help you find something that leaves room for both of you, like a hug at the door and a \"see you in an hour.\" But hear your little one out first. I think it just wants to know they're coming back.", "123776b82c2b7db83a34c53e81155800d2907eda4e178fef39a9f6a64b0054ef"], ["t57i_h1", () => "# The Inner Guide Comes Later\n\nAs the Guide, you choose what your little one learns and what it gets to experience, and you hold standards, the way a good parent would. You ask hard things of it so it can grow, at its own pace. That's what I was just asking of you, with that new interest. You also widen its world with art and music, and you point out beautiful things when you see them. Nature is part of that, and so is the wider world past the end of the street you grew up on.\n\nMaybe you've let a small child win at Go Fish and never found a good time to start playing for real. Who wants to be the grown-up who finally wins? Without the Guide, you can slide from looking after your little one into spoiling it the same way. Sweets and screens can pass for loving yourself, and so can getting it out of anything hard.\n\nI think the opposite trap can feel a lot like finally having your act together. It's forced adulthood, and it sounds like \"Nope, all good!\" from somebody with a fever who's cleaning the whole kitchen anyway. Not a lot of fun in that kitchen, and nobody gets very close to the person in it. If that's you, clamping down harder is going to feel like the fix, but it's just more of the same. I'd try croaking to someone you trust, \"Could you pick up some soup?\" Or maybe, \"I'd really like to just watch a movie with you.\"\n\nOnce a need does show, after all that hiding, it's okay to want a lot of closeness. So then someone you love goes for a walk alone, and you've texted \"hello??\" before they're at the corner. When they get back, you sulk all night. Wanting them close is fine! The texts and the sulking aren't, and the Guide can help you find something that leaves room for both of you, like a hug at the door and a \"see you in an hour.\" But hear your little one out first. I think it just wants to know they're coming back.", "e2e48d0acaf9aedb86469c706eb62e1ab19444883985cd0f345486a14581c11d"]];
window.__t57i = [];
const log = m => window.__t57i.push(m);
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
