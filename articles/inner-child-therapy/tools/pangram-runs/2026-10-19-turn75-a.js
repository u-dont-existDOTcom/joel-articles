const items0 = [["t75a_fat4b", () => "Before choosing a therapist, get to know the strengths and pitfalls of their approach, including any modifications they make to the standard protocol. I'd especially want to interview them regarding how they treat spiritual experiences. You want someone who won't tell you what yours really mean, downplay them, force them, or treat them as a symptom. I'd also want one who doesn't put ideas in your head, and who understands dissociation. What have they found too challenging to deal with so far, and where have they seen the best results? A good therapist won't charge you an arm and a leg just for this kind of interview, and they should already have this information on their website to avoid wasting too much time. A certificate on the wall can't tell you any of that.", "9123d117277efa24c278ef7e5a4fbd0d9ef240e01a9a09a67d9e782cb8382d74"], ["t75a_h1fat", () => "# Finding a Therapist to Borrow Adulthood\n\nWe all need some support, especially when taking our first steps. First and easiest is to start with finding a somatic therapist, if that resonates, as per my [Somatic Therapies Guide](http://somatic.u-dont-exist.com/).\n\nInner Child Reparenting therapists do exist, and you can find them, although they often are not licensed, and I don't know of any central directory, nor of any protocol they'd have in common. There are none which work with my guide yet. I can consult, and if you like the guide, you can ask a therapist to check it out and see what they agree with or disagree with as a great way to vet them.\n\nThe best licensed, listed therapists you'll find that come close will be doing Internal Family Systems (IFS), or Schema Therapy. I'll talk more about those next, but Schema Therapy comes closest to my approach. [Open Path Collective](https://openpathcollective.org/pricing-and-eligibility-for-affordable-therapy/) (or a similar resource in your country) lists thousands of affordable therapists. You can filter them by Schema or IFS. You can often find [even more Schema therapists at the official site](https://schematherapysociety.org/Search?&tab=1).\n\nBefore choosing a therapist, get to know the strengths and pitfalls of their approach, including any modifications they make to the standard protocol. I'd especially want to interview them regarding how they treat spiritual experiences. You want someone who won't tell you what yours really mean, downplay them, force them, or treat them as a symptom. I'd also want one who doesn't put ideas in your head, and who understands dissociation. What have they found too challenging to deal with so far, and where have they seen the best results? A good therapist won't charge you an arm and a leg just for this kind of interview, and they should already have this information on their website to avoid wasting too much time. A certificate on the wall can't tell you any of that.\n\nRegarding AI therapy, I've tried all the top AI therapy apps, and they're all pretty bad. I'm trying to make my own based on this guide, but I'm becoming more convinced that unsupervised AI therapy is just a toss up. That doesn't mean you can't get a lot of great insights sometimes when talking to AI, though, but just expect it to go sideways sometimes.", "480623b5995e32d51cfefd718e1a784939f24b9fd8217e8389d752c4f5e1bfb1"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "t75a" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__t75a = [];
const log = m => { window.__t75a.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__t75a)); } catch (e) {} };
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
