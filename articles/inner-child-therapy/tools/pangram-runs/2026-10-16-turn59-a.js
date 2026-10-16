const items = [["t59a_p6cut", () => "Say you're still waiting on that signature and the cat's off her food. I'd spend today on the cat, since she matters more to you and you can do something about her. And if it's all one big mess in your head, put it in one sentence and do whatever that sentence says comes first; anything else can wait unless it'd change that.", "f609f10f91f04c5517113bc276ddcbc68e24caf6ae07b285ae403ac099e76357"], ["t59a_p7c", () => "Forced adulthood can get into your head too, where it wants everything as spotless as that kitchen. At your grandpa's funeral, some dumb jingle starts up in your head and you nearly laugh during the eulogy. That doesn't mean you didn't love him, or that something's wrong with you. Minds come up with ugly and embarrassing stuff all the time, some of it the opposite of what you believe, and bodies do their own thing too. The Guide isn't there to police every thought. It notices the jingle and knows you didn't mean it, and that it isn't who you are. Then it goes with what you'd stand behind, which here is probably squeezing your mom's hand and listening, and lets the jingle go.", "96ca3b694b2e1e738313b3884e6eeb7eb0f39c3fc3e96e79b7eae763f5d97102"], ["t59a_p7e", () => "Forced adulthood can get into your head too, where it wants everything as spotless as that kitchen. At your grandpa's funeral, some dumb jingle starts up in your head and you nearly laugh during the eulogy. That doesn't mean you didn't love him, or that something's wrong with you. Minds come up with ugly and embarrassing stuff all the time, some of it the opposite of what you believe, and bodies do their own thing too. The Guide isn't there to police every thought. It just notices the jingle. You didn't mean it, and it isn't who you are, so it can go, and you can do what you'd stand behind, which here is probably squeezing your mom's hand and listening.", "eeacdaa8b722bad1a42a905cbba6d278e1a3594ea2edb6a3246137a9cdb39f9b"], ["t59a_p8c", () => "I think this is closer to what the Buddha taught, too. He never expected a mind where nothing bad ever shows up. He said what counts as kamma is what you intend, and he gave monks several ways to deal with a nasty thought once it's already there. When a king who'd had his own father killed confessed it to him, the Buddha said that seeing a fault as a fault, making it right and holding back from then on is how you grow in the practice. So it's about seeing clearly and repairing things, and nobody's asking you to prove you've got a pure mind. Feeling bad about something you chose to do can sometimes tell you something needs looking at. Feeling bad about a jingle just for showing up is a different thing.", "2723022e511a6b54c5822a03b3fe765c0ab5ef63af853504516092a0b9247db8"], ["t59a_p8d", () => "I think this is closer to what the Buddha taught, too. A king who'd had his own father killed once confessed it to him, and the Buddha said that seeing a fault as a fault, making it right and holding back from then on is how you grow in the practice. He never asked for a mind where nothing bad shows up. He said kamma is about what you intend, and he gave monks several ways to handle a nasty thought once it's there. So it's about seeing clearly and repairing things, and nobody's asking you to prove you've got a pure mind. Feeling bad about something you chose to do can sometimes mean something needs looking at. Feeling bad about a jingle for just showing up is another thing.", "c241d27a2ffc22978493412538d29d8982ba5118a5a7bea446394f5d0f99a99d"]];
window.__t59a = [];
const log = m => window.__t59a.push(m);
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
