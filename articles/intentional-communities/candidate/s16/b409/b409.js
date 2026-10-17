const items = [["S16v26kni-H3-P6", () => "By visiting some communities, you'll get a better idea of how much togetherness you enjoy and what kind of privacy you need, and what kind of labor system irritates you. And whether communal showers feel liberating, or make you start looking at studio apartments! No manifesto is going to tell you any of that!", "8fa05767905f68982dd1f2ae7979cc549bb29c770ce4a6ee850749d806fbe3a6"], ["S16v26kni-H3-P5+P6", () => "Go visit some real communities. Really, go! Twin Oaks is one. East Wind is another, and so is Acorn, and there are plenty of other intentional communities. Lots of ecovillages are open to visitors too. Check their current visitor requirements first.\n\nBy visiting some communities, you'll get a better idea of how much togetherness you enjoy and what kind of privacy you need, and what kind of labor system irritates you. And whether communal showers feel liberating, or make you start looking at studio apartments! No manifesto is going to tell you any of that!", "2edf4bfe75413e261b70c46d6761a7f080573cc2d2c84302755382f84f519850"], ["S16v26kni-H3-P6+P7", () => "By visiting some communities, you'll get a better idea of how much togetherness you enjoy and what kind of privacy you need, and what kind of labor system irritates you. And whether communal showers feel liberating, or make you start looking at studio apartments! No manifesto is going to tell you any of that!\n\nDo those three things before you spend serious time or money looking for land. I know, I know!", "4c6937e2da38abd387b2b547b9fccabccdde44e035788a0ed42d148ee6745cf4"], ["S16v26kni-H3-P7+P8", () => "Do those three things before you spend serious time or money looking for land. I know, I know!\n\nI'm not trying to sell you a retreat or get you to fill out an application or anything. The manuals I mentioned are free. I've just noticed that wherever people are taking real care of each other and playing, feeling useful and having room to become more honest, community tends to gather.", "20b3ccd5a1a02947ec504466460d2d947ea30dad9c23b07f09e2fb1f836a576e"]];
window.__B409 = [];
const log = m => window.__B409.push(m);
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
