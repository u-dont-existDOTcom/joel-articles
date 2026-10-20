const items0 = [["t71y_secjww1", () => "## Journal With Each Hand\n\nGet a notebook and let your two hands take turns. The one you don't usually write with is for your little one, so give it the vulnerable stuff, whatever you're thinking or feeling that's hard to show. It's slow going, and the letters already look like a child's. You might look down at the page and think, huh, that's my writing from when I was little. Then switch to your usual hand and write back as the grown-up you: the Nurturer, the Protector and the Guide. Some people get only silence when they talk to their little one or try to picture them, and writing it out like this can get past that silence. If a protective part shows up instead of your little one, it gets the clumsy hand first.\n\nIf thinking things through on paper starts to leave you more confused about what's going on, you can switch to a memory aid instead. Write the date and a line or two about what happened, or a note about what helped. A reminder works too, or the next step you're planning. Or skip the pen and leave yourself a voice note, which hardly looks like journaling at all. Each of these keeps the thread of what's been happening, and you don't have to work out what it means at the same time. A memory aid doesn't need to explain your life. Looking for patterns can come later, if that turns out to be useful.", "d29f86f91c1b760be1050c7f8b22404b7dc11b95ec7c8706060564cd9b2f0164"], ["t71y_secjww2", () => "## Journal With Each Hand\n\nPut the vulnerable thoughts and feelings down with the hand you don't write with, then answer them with the one you do, as the grown-up you. If talking to your little one or picturing them has only gotten you silence, this can get you past it. A protective part might show up ahead of your little one, and if it does, it gets the clumsy hand first. When you switch, that's your grown-up holding the pen. The other hand already writes like a child, so let it take as long as it takes.\n\nSometimes you write and write to make sense of things, and come out more mixed up than when you started. Then try a memory aid instead: the date and what happened, kept short, or a note about what helped. A reminder or a next step works too. Or a voice note, if you'd rather skip the paper. You're keeping track of what's been going on, and you don't have to make sense of it while you're doing that. A memory aid doesn't need to explain your life. If looking for patterns seems useful later, the notes will be there.", "37a32bd3e72eeb4816b53daec7dbfd32cbfe4799ba2b4cbec5de1ea686e49789"], ["t71y_secjww3", () => "## Journal With Each Hand\n\nFor this one, your usual hand belongs to the grown-up you, and the hand you don't write with belongs to your little one. It's a way some people get past the silence they run into when they talk to their little one or try to picture them. Let the clumsy hand put down the vulnerable thoughts and feelings, slowly, in letters that already look like a child's. If a protective part shows up, though, it gets that hand before your little one does. Then you might sit a moment with the pen back in your good hand, wondering what the grown-up you would say to that. Write back as that grown-up.\n\nSome entries can be as short as the date and a few words about what happened. Those are for when journaling to make sense of things starts making them more confusing. A note of what helped works too. So does a reminder. Or write down the next step. That way you don't lose track of what's been happening. And what does it all mean? That part can wait, and you can look for patterns later if it turns out to be useful. A memory aid doesn't need to explain your life. You could also leave yourself a voice note, if you'd rather say it out loud.", "cee9b0edc4548bff0e2ecda98a06be74d6ebfadd88196a3d29bbc4e058de3ae5"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "t71y" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__t71y = [];
const log = m => { window.__t71y.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__t71y)); } catch (e) {} };
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
