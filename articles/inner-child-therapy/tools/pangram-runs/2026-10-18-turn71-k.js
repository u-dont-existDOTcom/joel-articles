const items0 = [["t71k_oik", () => "Mornings, pick one small intention, like \"Today I'll notice one hook before I act on it.\" At night, look back over the day, kindly. Maybe it sounds like, \"Oh, there it was at lunch, when my boss sighed. Caught that one! And there it got me anyway, with my sister, before I even noticed.\" Then think about what small repair you could make, or what would protect your little one tomorrow.", "73d34f813639eae6c4dd30cf6eb0361335ca63ed75783563b3c3bd80f04d465b"], ["t71k_jwg", () => "Maybe you've asked your little one how they're feeling and gotten nothing, and you're thinking, \"Great, even they won't talk to me.\" Try a pen. Write with your clumsy hand, whose letters already look like a first grader's, and let it put down whatever scared or hurt feelings are really there, nothing made up. Then answer with your usual hand, as the grown-up who's got their back. If the protective part grabs the pen first, it gets the clumsy hand until it's said its piece.", "76a9d8c5996fc1ae2a1b08e408d6db40906e581217c65295f0179e05c64976a1"], ["t71k_cspa", () => "## Close the Session and Return to Life\n\nThat \"Present Time\" ending is worth stealing for every session, photos or no photos. Otherwise the processing can go on and on, until it's just one more way to avoid living your life. So when you're done, look around and say where you are. Feel your feet on the floor, or the chair under you, and unclench your jaw and hands, since they've probably been at it this whole time.", "3939eb12d07e7f87efb3e0fd75b40ff5eb5f6e81128d1270cdfc083359804e8b"], ["t71k_cspb", () => "That \"Present Time\" ending is worth stealing for every session, photos or no photos. Otherwise the processing can go on and on, until it's just one more way to avoid living your life. So when you're done, look around and say where you are. Feel your feet on the floor, or the chair under you, and unclench your jaw and hands, since they've probably been at it this whole time.\n\nThen pick the next normal thing you'll do, like making food or going to sleep, and tell your little one, \"That's enough for today. We're going back to the life we're building.\" Yes, yes, it can feel a bit weird saying that to someone who lives inside you. Nothing has to be resolved first, and whatever you're still feeling can come along. Going back to your life is part of the healing, too.", "e57631de66aca2318c0e3f0e75318a6c3ca0416cd6d48b155735f0eed9a29a85"], ["t71k_cspc", () => "## Close the Session and Return to Life\n\nThen pick the next normal thing you'll do, like making food or going to sleep, and tell your little one, \"That's enough for today. We're going back to the life we're building.\" Yes, yes, it can feel a bit weird saying that to someone who lives inside you. Nothing has to be resolved first, and whatever you're still feeling can come along. Going back to your life is part of the healing, too.", "56963778dd49b28a558a175e1fb58de414017c041cf3e316a0d083dbd002ded1"], ["t71k_jlpb", () => "This one works best on a steadier day, when thinking about other people won't pull you out of your own shoes. Name the feeling plainly. Lonely, say. Then think of how many people are feeling that exact thing right now, and wanting it to stop, just like you. Some of them make it worse trying to get away from it. Just like you, sometimes. \ud83d\ude05 Wish all of you, you first, enough support to stay with it, so the pain stops with you.\n\nYou don't need any special breathing. And forgiving whoever hurt you, or imagining their childhood? Also not required, and neither is getting in touch with them (if that ever happens, it's its own decision, made on a calmer day than this). Funny how every one of us figures we're the only one who feels this way. The wish just helps you stop treating a feeling this many people have had as proof that you, specifically, are defective.", "619b4c663436c2700a4325f81a552643d42410ae4b2f16987fdf92f039ef991b"], ["t71k_jlpc", () => "## Just Like Me\n\nYou don't need any special breathing. And forgiving whoever hurt you, or imagining their childhood? Also not required, and neither is getting in touch with them (if that ever happens, it's its own decision, made on a calmer day than this). Funny how every one of us figures we're the only one who feels this way. The wish just helps you stop treating a feeling this many people have had as proof that you, specifically, are defective.", "c9104dd38ba752ed2a69df40274002f300e92245759ddfac6557e5a7c875d7cc"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "t71k" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__t71k = [];
const log = m => { window.__t71k.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__t71k)); } catch (e) {} };
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
