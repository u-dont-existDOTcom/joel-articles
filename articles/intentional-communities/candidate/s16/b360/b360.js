const items = [["S16v16hhhk-H3", () => "What to Do This Month\n\nSo what do you actually do this month? Start doing some inner pl/ork, with the free reparenting guide and Hearthwork manual or with another serious practice you already trust. And practice before you have an audience!\n\nGet two or three people together to form a practice group. Call it that, not a commune! Meet regularly, and practice listening and switching roles, and get through at least one disagreement together, and keep your commitments to each other. One disagreement is enough, I promise! Hold off on talking about a shared future until you've done all of that.\n\nWhere do you find these people? Try an unprogrammed Quaker meeting, a restorative-practice group, an open-hearted congregation, a mature recovery group, a meditation group, or find some people who have gone on long retreats and come back kinder, rather than more impressed with themselves.\n\nGo visit some real communities. Really, go! Twin Oaks, East Wind, Acorn and other intentional communities are used to having people visit them. Many ecovillages are too. Check their current visitor requirements first.\n\nBy visiting some communities, you'll get a better idea of things no manifesto can tell you, like how much togetherness you enjoy, what kind of privacy you need, and what kind of labor system irritates you. And whether communal showers feel liberating, or you'll start looking at studio apartments for rent right after the first communal shower you take!\n\nDo those three things before you spend serious time or money looking for land. The land can wait!\n\nI'm not trying to sell you a retreat or get you to fill out an application or anything, the manuals I mentioned are free. I've just noticed that community tends to gather wherever people find real care, play, usefulness and room to become more honest.\n\nDecades after the Bruderhof shaped my father, I'm publishing the film he made, and writing this.\n\nMaybe some of you will build something useful from this. Maybe that community will teach someone else, who'll build another. Passing it on doesn't need one institution, one founder or one official version.\n\nIf you build something real, maybe we'll hear about each other. And if you teach other people to build, hearing about it matters less.", "244b7ccb7eecb117edc3b8a29a0f071f34effdb23942e661a839b680d8435644"]];
window.__B360 = [];
const log = m => window.__B360.push(m);
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
