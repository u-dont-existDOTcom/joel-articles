const items = [["S13v19-3P3", () => "Visibility is important even in a money-free community. There are always scarce things and bottlenecks. It is important that people be able to know what the community owns or holds in common, what is set aside, what it owes to outsiders. Who has authority over distribution of major resources? Where are the conflicts of interest? Large transfers (land, equipment, stores or outside cash) can't depend on one person's memory or permission. It is also important to specify what rights people have to resources when they leave the community. Whether or not the community uses money, it still needs to be able to provide people with resources when they leave, in whatever form makes sense (cash if it uses money, but also tools, transportation, temporary housing, stored goods or the right to keep using something). Otherwise the \"right\" to leave is just something on paper that can only be exercised if the community has spare money. That's not much of a right.", "d5bf924404611aa61eb4f66192e122da24164e4974fcc120e1ff23af0dc33665"], ["S13v19-5P3", () => "'Outside' doesn't always mean the nation-state. My research initially leaned too far that way. What's really needed is that there be a competent layer that isn't reviewing its own conduct. That can be another community, a federation, a professional, an autonomous regional institution, a court, a regulatory agency, an emergency service. Just not the community itself! The Zapatistas are an important correction here: autonomous institutions can review local power without becoming the state, and when power crept up in their own system, they pushed it back down. But autonomy doesn't mean that anyone can erase non-waivable individual rights, or that outside jurisdiction disappears.", "f195e6f72de4b922bb455001ea5953a60ed78cb7c28074d498c555178328a924"]];
window.__B295 = [];
const log = m => window.__B295.push(m);
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
