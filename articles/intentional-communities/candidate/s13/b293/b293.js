const items = [["S13v14-4P8", () => "Do stuff together prior to making them provisional members. (Sorry, hanging out doesn't count! I know, it's the fun part.) Can you actually make a decision as a group? Can you actually work together to get something done (an ordinary work or shared-resource task will do)? Can you even process a small conflict afterwards? Do a trial run like that before anybody sells a house. It won't show you anyone's soul, but it can show you whether your way of coordinating works.", "6c47fb37461760eff77215a716295b3b3c01d99d96bfc37693dc978256517f02"], ["S13v14-5P2", () => "On the other hand, the power to remove people is also one of the easiest to abuse. So work out the process before it's about anyone in particular. What conduct might constitute cause for immediate action to protect people? Who will decide whether to place temporary restrictions on someone? Who will preserve the evidence? Who will recuse themselves? How can the person reply, and what review or appeal is possible without endangering others? What will be done to protect their housing, records, family contact, and access to common resources or outside funds (if any) during separation? When will outside help be sought? (More on that next.)", "7f5436cff724477ea8768fa5700b3dd3da4f40e6f45d4e6955909fd05542d5e1"], ["S13v14-5P4", () => "Also agree on a mediator or ombud in advance. Why bother? People often do not trust someone who they have not met, and who appears at the time of a crisis to act as a \u2018neutral stranger\u2019. Remember that mediation is about trying to restore good relations between people. It does not remove the need for evidence, for safeguarding, for a ruling, or for a final separation when consent to continue in a relationship or a shared life is no longer present.", "15b0f43a767b7da05b71db5813822c1b2373968b23f98c30d218d052f344fed9"], ["S13v14-3hP1", () => "Resources, Land, and Exit Terms\n\nWho has the title to the land? It matters so much! Whoever has it has a massive amount of power over the community. If the deed is in the founder's name, then they're really a landlord just with a philosophy. If three members out of twelve own everything, then there's effectively two classes of members even if the literature says everyone's equal.", "1fd87d9cae26e53a9d9d47ac204c3a6e7ba39398c5aeb01f01f430c1b5f90d51"]];
window.__B293 = [];
const log = m => window.__B293.push(m);
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
