const items0 = [["t71ff_ifs1r", () => "Richard Schwartz started [Internal Family Systems](https://ifs-institute.com/) (IFS) back in the 1980s. This method overlaps with it a lot. IFS recognizes protective parts too, and teaches people to approach them without shame or a fight, so \"meet the protector first\" fits right in. My reparenting method diverges from IFS at an important point. In standard IFS, the healer is the Self, a calm, compassionate source that's supposed to show up once your parts \"unblend.\" I emphasize the inner adult you build and practice occupying: Nurturer, Protector, and Leader, Guide, or Guru.", "a52085204423cafdc745a051aa2d41d6d572ce57b5ae10cdda9626337eed4e70"], ["t71ff_secifsr", () => "## How This Relates to IFS\n\nRichard Schwartz started [Internal Family Systems](https://ifs-institute.com/) (IFS) back in the 1980s. This method overlaps with it a lot. IFS recognizes protective parts too, and teaches people to approach them without shame or a fight, so \"meet the protector first\" fits right in. My reparenting method diverges from IFS at an important point. In standard IFS, the healer is the Self, a calm, compassionate source that's supposed to show up once your parts \"unblend.\" I emphasize the inner adult you build and practice occupying: Nurturer, Protector, and Leader, Guide, or Guru.\n\nAnd what if that calm inner source just won't show up for you? That's where borrowed adulthood comes in. Maybe you borrow one grown-up job from a friend, or from a plan you've made, and take it in bit by bit. I have no use for another neo-Advaita, [spiritual-bypassing](http://goenka.u-dont-exist.com/) claim that a perfect Higher Self is already waiting underneath everything. A grown-up you can trust gets built through care and boundaries, and through action and direction.\n\nIFS calls these wounded young parts \"exiles.\" I find that pathologizing. I prefer to speak of a child who needs parenting and integration, rather than naming them by their wounded or excluded condition. IFS \"unburdening,\" often done after witnessing a part's origin story, can be powerful. But it can also get dramatic, with a lot of focus on memories and plenty of room for suggestion, and that can knock people off balance, especially if they tend to dissociate (DID-like fragmentation included) or to spiritually bypass.\n\nAnd then there's the map itself. Managers, firefighters, exiles, polarized parts, legacy burdens, Self-energy, guides, new subparts... how many parts is that now? It can turn into a maze. Some practitioners use the model gently, and others seem to leave people more fragmented while trying to fix the fragmenting. Having institutes and certifications behind a framework doesn't make it any more true, or safer for that matter.\n\nBefore choosing a therapist, get to know the strengths and pitfalls of IFS and reparenting. Could an IFS therapist help? They may, if they're skilled and grounded. You'd want one who's trauma-informed and doesn't put ideas in your head, especially one who understands dissociation. For your little one's pain, or for shame, a good reparenting therapist may fit better. The same goes for attachment wounds or abandoning yourself, or not having an inner adult you can count on.\n\n### Related Clinical Work\n\nThis framework grew out of my own practice, plus the teachers and collaborators I credit below. Later revisions also compare notes with other approaches, like schema therapy, compassion-focused therapy, attachment repair, motivational interviewing, mentalizing, metacognitive therapy, behavioral activation, radically open DBT, emotion-focused therapy, spiritually integrated psychotherapy and so on. Those don't even agree with each other on everything! So I borrow particular ideas and practices from them, and that's it. I'm not saying they'd sign off on the whole synthesis, or that their research proves it as a package.", "e421b2a4c0b9ee16373b98ea4b4c7b9a62d21fc7d272e97528cae52b506809d7"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "t71ff" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__t71ff = [];
const log = m => { window.__t71ff.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__t71ff)); } catch (e) {} };
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
