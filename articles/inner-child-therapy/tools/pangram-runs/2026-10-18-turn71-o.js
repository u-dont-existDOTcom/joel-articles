const items0 = [["t71o_cs2o", () => "And what's next for you two? Maybe it's making food, or just going to bed. Whatever it is, tell your little one, \"That's enough for today. We're going back to the life we're building.\" Yes, yes, it can feel a bit weird saying that to someone who lives inside you. Nothing has to be resolved first, and whatever you're still feeling can come along. Going back to your life is part of the healing, too.", "546ce322692ec50fa539e46de80bbf491cb7b780a061705898589f8a59e7a9f1"], ["t71o_secsc7", () => "## Close the Session and Return to Life\n\nThat \"Present Time\" ending is worth stealing for every session, photos or no photos. Otherwise the processing can go on and on, until it's just one more way to avoid living your life. So when you're done, look around and say where you are. Feel your feet on the floor, or the chair under you, and unclench your jaw and hands, since they've probably been at it this whole time.\n\nAnd what's next for you two? Maybe it's making food, or just going to bed. Whatever it is, tell your little one, \"That's enough for today. We're going back to the life we're building.\" Yes, yes, it can feel a bit weird saying that to someone who lives inside you. Nothing has to be resolved first, and whatever you're still feeling can come along. Going back to your life is part of the healing, too.", "31090acbd8e992caaf1728d137b972f9a9236a196f9ba660efede2684f049b4d"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "t71o" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__t71o = [];
const log = m => { window.__t71o.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__t71o)); } catch (e) {} };
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
