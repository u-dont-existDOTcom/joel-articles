const items0 = [["t71jj_jwq", () => "Lucia Capacchione, an art therapist, wrote a whole book on this one, [The Power of Your Other Hand](https://www.luciac.com/). Love that title. Your other hand, the clumsy one, writes like a first grader anyway, so it gets the scared or hurt feelings (nothing made up). Then your usual hand writes back as the grown-up. Plenty of people who get only silence when they try talking to their little one find that other hand has a lot to say. And if a protective part grabs the pen first, it gets that hand until it's had its say.", "1d21e6114b759ecec7533f4c2922a3d22f38c6bf08064a059cd70ca5d146e236"], ["t71jj_oiw", () => "The night half of this is a lot like the [Examen](https://www.ignatianspirituality.com/ignatian-prayer/the-examen/), the evening review Jesuits have done for centuries, just aimed at hooks. It sounds like an exam, but nobody's grading you, here either. In the morning you pick one small intention, like \"Today I'll notice one hook before I act on it.\" At bedtime you look back. Where did you catch the hook, and where did it run its routine anyway? Then what's the next small repair, or something that'd protect your little one?", "e9a240b2d0f466899ef72891e34b3259bd6dc2f5325a8b2e67992bf5aaf419f5"], ["t71jj_secjwq", () => "## Journal With Each Hand\n\nLucia Capacchione, an art therapist, wrote a whole book on this one, [The Power of Your Other Hand](https://www.luciac.com/). Love that title. Your other hand, the clumsy one, writes like a first grader anyway, so it gets the scared or hurt feelings (nothing made up). Then your usual hand writes back as the grown-up. Plenty of people who get only silence when they try talking to their little one find that other hand has a lot to say. And if a protective part grabs the pen first, it gets that hand until it's had its say.\n\nIf thinking things through on paper leaves you more confused, a simpler memory aid is fine. It keeps track of things without you having to work out what they mean at the same time. Looking for patterns can come later, if it's useful at all. A memory aid doesn't have to explain your life. It could be a short note of what happened, with the date, or a note of what helped. A reminder or a next step works too. Or you can leave yourself a voice note.", "982714abc131f277ccf8e46ee74b620ce2618929ebee6b6954e0fe360521ee04"], ["t71jj_secoiw", () => "## One Intention in the Morning, One Review at Night\n\nThe night half of this is a lot like the [Examen](https://www.ignatianspirituality.com/ignatian-prayer/the-examen/), the evening review Jesuits have done for centuries, just aimed at hooks. It sounds like an exam, but nobody's grading you, here either. In the morning you pick one small intention, like \"Today I'll notice one hook before I act on it.\" At bedtime you look back. Where did you catch the hook, and where did it run its routine anyway? Then what's the next small repair, or something that'd protect your little one?\n\nAnd what good did you get today? Count the small stuff, like a warm moment, or some nerve you didn't know you had. Noticing the hook counts too, and it counts if you're only seeing it now, in the review. Same if you broke the pattern somewhere. Then repair what you can, and that's the day. Same intention tomorrow. Bed.", "87208dee6a37ded412a9b56be46a66df507b5dd4c7734314d9f6fd59c9cfd81f"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "t71jj" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__t71jj = [];
const log = m => { window.__t71jj.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__t71jj)); } catch (e) {} };
const other = () => { try { return JSON.parse(localStorage.getItem(lane(rev ? 'fwd' : 'rev')) || '[]').filter(m => / (clicked|taking)$/.test(m)).map(m => order0.indexOf(m.split(':')[0])); } catch (e) { return []; } };
const setter = Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value').set;
const sha = async t => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))).map(b => b.toString(16).padStart(2, '0')).join('');
const button = () => [...document.querySelectorAll('button[type=submit]')].find(b => /check for ai/i.test(b.innerText));
const wait = ms => new Promise(r => setTimeout(r, ms));
async function run() {
  for (const [k, mk, want] of items) {
    const o = other(), i = order0.indexOf(k);
    if (o.length && (rev ? i <= Math.max(...o) : i >= Math.min(...o))) { log('stop at ' + k + ': the other tab has the rest'); break; }
    log(k + ': taking');  // claimed before the work, so the other tab never takes it too (turn 65: with a margin
                          // of one instead, both tabs stopped short of the last check)
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
