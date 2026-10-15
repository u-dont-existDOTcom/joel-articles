const items = [["t58d_p5d", () => "Your little one might ask about the job, \"But what if they never call back?\" The Guide doesn't know either, and it doesn't need to. If you're someone who follows up, you send the email, and that's today taken care of. Whatever happens after that can stay a mystery for a while.", "f510d500a6c22082210b71ae41f8c4897234d164da7fc98861a6d219015027ea"], ["t58d_p6d", () => "Then there's the stuff you can't move yet. The car needs a part that's on back order, and the old parent in your head is already calling you lazy. Lazy about what, a delivery truck? So you put \"call the shop when it's in\" on the fridge, leave the car where it is instead of rigging something up, and go deal with the gutters. That one can move.", "92a4921db2e1e0af0f273e834d9a07b7062afd8a87652cc79ab3864773f29e40"], ["t58d_p6e", () => "Some things just can't move yet. Say you're waiting on the landlord's signature before you can sign up for the new place. You're not being lazy, whatever the old parent in your head says, and there's no point forging ahead as if you had it. Write down what you're waiting on, so you'll notice when it comes, and go do something that can move today.", "dd565e26c459672870d6ec277987a13854589551db3455d7a51497a136fc637b"], ["t58d_p7d", () => "Maybe the car's stuck and the cat's sick in the same week, and your head keeps going in circles about both. The car can wait for its part. The cat can't, so that's today. I'd usually go with whatever matters most to you and can move now. And when it's all that scrambled, saying it out loud in one go (\"Car's stuck, cat first\") helps, and then you just do the cat thing, without stopping to sort out anything that wouldn't change it.", "93281c24a739606b2889c27dc9467e95bf62bcc8b21b5b772817455b361f9fcc"], ["t58d_p7e", () => "Some weeks it's the car and a sick cat at the same time, and your head's going round and round. The car can wait for its part, but the cat can't, so the cat gets today. That's usually how I'd pick: whatever matters most to you and can move now. And if you're too scrambled to pick at all, say it in one sentence (\"Car's stuck, cat first\") and do just the next thing it tells you. Leave every other question for later, unless the answer would change that.", "e77893356ed90c285d6bbf63082dd408c61fc4170362f8e95c056b7857c6e3e9"]];
window.__t58d = [];
const log = m => window.__t58d.push(m);
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
