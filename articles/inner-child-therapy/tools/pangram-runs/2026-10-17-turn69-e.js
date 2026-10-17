const items0 = [["t69e_st1i", () => "Ever notice how \"I'm not dependent\" keeps you thinking about being dependent? Words point your attention, whether you want them to or not. So unless the hard thing itself needs naming, talk about what you want more of, like being able to ask for help, or a friendship you're growing. \"Let's find you more ways to feel looked after\" goes somewhere. With your little one, and in hypnosis especially, make it something you can picture, like a warm kitchen or a door that locks, whatever they really need.", "5e1b05fe3e99f4238ba0a28d37bdb22323b6e68bfd30b2b65d696aab449508b6"], ["t69e_st1j", () => "Words point your attention. Tell yourself \"I'm not dependent\" and you're still thinking about being dependent (funny how that works), so unless the painful thing really needs naming, talk toward what you want to grow instead, like a skill or a relationship. \"Let's find you more ways to feel looked after\" is a direction your mind can take. With your little one, and in hypnosis especially, make that direction easy to picture: a warm kitchen, a door that locks, a nap, whatever's needed.", "bbc8d193f0b6ccebb180f7b566cb250d83fad0de139beb3b38dae12260271500"], ["t69e_st2o", () => "Grief is grief, though. Partway through all that steering, you might think, \"But it really was dangerous,\" and if it was, it should be called dangerous. If your little one says \"he hurt me,\" that's harm, and it gets called harm, not \"a learning experience.\" Same for anger, a no, who's responsible, what's possible in practice, all that. Then once it's been said, most of the words go to what you'd choose to protect or repair, and what can still be practiced or grown.", "366519e5494d726a613428a0914daf961d20d0d7aa5c5e5fb0a902c343af3f35"], ["t69e_st2p", () => "Partway through all that steering, you might think, \"But it really was dangerous.\" If it was, it should be called dangerous, and grief should get to be grief. If your little one says \"he hurt me,\" that's harm, and it gets called harm (not \"a learning experience\"). The same goes for anger, a no, who's responsible, what's possible in practice, all that. Once it's been said, most of the words can go to what you'd choose to protect or repair, and what can still be practiced or grown.", "9f4bd41bc3ca2924eecb2113944839daf38af97dbbe60228ec54ad56e7b684d0"], ["t69e_st5i", () => "So is the person you trade listening with supposed to turn into your new parent? They shouldn't, and that's borrowed adulthood at its healthiest: they show you how something's done, you get to try it with them there, and then they hand it back. Afterward it helps to name what you got and do one piece of it yourself. That doesn't make therapy useless, by the way, it's still good for what therapy does. Peers and community just do something different, and a serious healing path can have both.", "efdef0c45cf4adfd412050b7d1d7fc2a537f890c5f76243653dea078b202dae2"], ["t69e_st5j", () => "Say your partner in this is really good at staying calm while you fall apart. They're not going to be your parent forever, and they shouldn't be. They show you what that calm looks like and you practice it with them there. After a while it's more yours than theirs, which is borrowed adulthood at its healthiest. It's also worth naming afterward what you got from them, and doing one piece of it yourself. Therapy still has its place for what therapy does. A peer and a community do something different, and a serious healing path can include both of them.", "d70ac284bced3da9e58ac61b12d4e739fd0053ed6ce5a3bc7c9d80b67cea211d"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "t69e" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__t69e = [];
const log = m => { window.__t69e.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__t69e)); } catch (e) {} };
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
