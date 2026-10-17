const items = [["S13v34-H3-P4+P5", () => "Good people leave for good reasons -- dying parent, love, work, health, exhaustion, change of mind, etc. You don't want them to lose everything they've put in! That's coercive -- they HAVE to stay if they can't afford to go. Whether or not you use money, you'll need to have a way of providing people with resources when they leave (cash, if you use it, but also tools, transportation, temporary housing, stored up goods, the right to keep using something, or whatever). Otherwise their \"right\" to leave is only on paper -- it only works when the community happens to have spare money! Write up the exit terms while leaving is still only theoretical -- like a pre-nup when you're planning the wedding. Not romantic, but protective! Much easier than doing it once anybody's furious.\n\nHonestly? For the nuts and bolts of all this (members, resources, land, agreements, etc.), I'd go to Diana Leafe Christian's Creating a Life Together (on the reading list at the end).", "aec0aaee9fffdbb1dcc607641881a97c5a51c363279f55ff087fb6581791f40a"], ["S13v34-H4-P6", () => "At each stage, always judge people based on their conduct. No matter how good it sounds when they talk about their spirituality or their therapy, don\u2019t go by that. What do they actually do? It\u2019s too easy to go by vibes. It\u2019s also easy to think someone\u2019s safe just because they\u2019re going along with everyone else. Six months with someone will give you more data, but there\u2019s still no \u201cgood person\u201d detector.", "f4c7b66887c37ecc5ad148509b3bac64495e55dfc46c898fbc6b1d826f0135d4"], ["S13v34-H5-P4", () => "Also decide on a mediator or ombudsperson in advance. Why bother? People often won't trust someone they haven't already met, who comes in during a crisis as a \"neutral stranger.\" A mediator doesn't obviate the need for evidence, safeguarding, rulings, etc. Mediation is an attempt to restore good relations between people. When people can't or won't consent to being in community any more, they still need a final separation.", "87912d740f360cf23849ded45888b9f95adc0c3ef6b3780ffdb135dd3b1928eb"]];
window.__B318 = [];
const log = m => window.__B318.push(m);
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
