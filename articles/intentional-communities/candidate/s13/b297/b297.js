const items = [["S13v21-2P3", () => "Throw sexuality and gender onto that list. Could an LGBTQ+ member live openly there? Date and/or be in a relationship? Would the community keep them fully protected? Should children be taught to question their sexual identities at an early age? Should one of the children grow up to be gay or transgender, what happens then? Until a group has answered these questions, its values on freedom and child-rearing are incomplete. Both of them!", "bde95779d30a65af04fbba3182caebeba8e8018d274315aa33f1ba70f6ef1806"], ["S13v21-3P4P5", () => "Good people leave for good reasons, like a dying parent, love, work, health, exhaustion, or just a simple change of mind. Leaving should not require someone to leave everything they\u2019ve put in, as that\u2019s effectively coercing someone to stay. You should write down the exit terms while no one is leaving yet, and it\u2019s still just a theoretical discussion. Think of it as a pre-nup while you\u2019re planning the wedding. It\u2019s not that romantic, but it\u2019s protective, and a lot easier than doing it when people are furious.\n\nFor the full sequence, see Diana Leafe Christian\u2019s Creating a Life Together: the vision comes before the members, the members before you pool the major resources, and the land comes last. (It's in the reading list at the end, too.)", "b1b7fd494d36a36ca57d2004861ca1d74e29816040b95a7168299d7a06e3b464"], ["S13v21-4P5", () => "Write down your answers to these questions: How long will a provisional membership be? What will a provisional member be responsible for and what are their rights? How will a provisional member's membership be reviewed? How might a person leave provisional membership? Who will make the decision about a person becoming a full member? (Hint: not the person who recruited them! \ud83d\ude1c) What rights will a full member have in terms of the land, other shared resources, and their voice within the group? What will a member be responsible for over the long term? (A full member's rights and responsibilities should be addressed in your founding agreements.)", "f694abb8ca0bd17df9c56d5d4e5f6e4784e4cc40711879435c102efbf9e7f746"], ["S13v21-5P3", () => "'Outside' doesn't always mean the nation-state. My research initially leaned too far that way. What's really needed is that there be a competent layer that isn't reviewing its own conduct. That can be another community, a federation, a professional, an autonomous regional institution, a court, a regulatory agency, an emergency service. Just not whoever's being reviewed! The Zapatistas are an important correction here: autonomous institutions can review local power without becoming the state, and when power crept up in their own system, they pushed it back down. But autonomy doesn't mean that anyone can erase non-waivable individual rights, or that outside jurisdiction disappears.", "f6ee58f24cef8db1016e6ba248d5b1e3b14979bfeb0ae59992a6562f7f6a9d2f"]];
window.__B297 = [];
const log = m => window.__B297.push(m);
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
