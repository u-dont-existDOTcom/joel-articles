const items = [["S14v9-P2", () => "If the community dissolves, what happens to the land and any outside debts? What about its buildings, equipment, common stores or funds? What happens to each member\u2019s agreed rights? More immediately, who is responsible for ensuring that everyone has a place to live and food to eat? Who takes responsibility for making sure people get their medications and the other care they need? Who keeps childcare going, and makes sure the kids\u2019 schooling carries on? Who takes responsibility for transportation, for the records, for family contact, for the animals, for making sure land obligations are met, and for any unresolved claims? That\u2019s a lot of loose ends!", "9a5634ef25cf07e45e74a7589ebd82eca5c7c96ccb3887b4bda096580efd2143"], ["S14v9", () => "Dissolution and Exit\n\nDissolution is something founders rarely want to talk about while they\u2019re picking a name for their community and looking forward to its first harvest. Who would? But that\u2019s exactly when it needs to be talked about.\n\nIf the community dissolves, what happens to the land and any outside debts? What about its buildings, equipment, common stores or funds? What happens to each member\u2019s agreed rights? More immediately, who is responsible for ensuring that everyone has a place to live and food to eat? Who takes responsibility for making sure people get their medications and the other care they need? Who keeps childcare going, and makes sure the kids\u2019 schooling carries on? Who takes responsibility for transportation, for the records, for family contact, for the animals, for making sure land obligations are met, and for any unresolved claims? That\u2019s a lot of loose ends!\n\nThink of it like a living will, and assign a bridge or successor for each critical function in advance, so basic life doesn\u2019t depend on reviving the commune. The institution may not be salvageable, but who\u2019s making breakfast tomorrow?\n\nDissolution terms are also a way for a group to end without turning every friendship into evidence. Who wants that? People may leave hurt, but they keep the transition support they agreed on, and their dignity. And they can tell a coherent story of what happened.\n\nInstitutions and relationships don\u2019t die at the same time, and some of what people learned to give one another may go on too. What a relief! The film American Commune follows two sisters who grew up on The Farm. When one of them later became ill, former members who hadn\u2019t seen her in years reached out with support. The Farm\u2019s communal economy had changed dramatically, but the bonds hadn\u2019t vanished.\n\nMy father carried the Bruderhof with him long after he left it. It shaped the foundation he started and the film he made. It shaped the places he took me, too, and the questions I\u2019m still asking (as you may have noticed!).", "0ee2caa5e9e43715dd053593b764948525c4c03afefc7e5abd11dd9a9a2a7efe"]];
window.__B319 = [];
const log = m => window.__B319.push(m);
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
