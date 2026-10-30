const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1100, height: 800 } });
  await p.goto('file://' + process.argv[2]);
  await p.waitForTimeout(500);
  const atTop = async () => p.evaluate(() => {
    const cs = [...document.querySelectorAll('section.card')].filter(c => c.offsetParent !== null);
    const near = cs.filter(c => { const t = c.getBoundingClientRect().top; return t > 60 && t < 200; });
    return near.length ? near[0].dataset.id : '(none at the bar, scrollY ' + Math.round(scrollY) + ')';
  });
  const click = async sel => { await p.evaluate(s => document.querySelector(s).click(), sel); await p.waitForTimeout(1200); };
  const out = [];
  await click('#nextBtn'); out.push('next -> ' + await atTop());
  await click('#c-T1 .dec.approve'); await click('#nextBtn'); out.push('approve T1, next -> ' + await atTop());
  await click('#c-J5 .dec.approve'); await click('#prevBtn'); out.push('approve J5, previous -> ' + await atTop());
  await click('#prevBtn'); out.push('previous again -> ' + await atTop() + ' | ' + await p.textContent('#prog'));
  // the middle of a long card: back to its start
  await p.evaluate(() => { const c = document.getElementById('c-R-audit'); window.scrollTo(0, c.getBoundingClientRect().top + scrollY + 300); });
  await p.waitForTimeout(300);
  await click('#prevBtn'); out.push('inside R-audit, previous -> ' + await atTop());
  await click('#prevBtn'); out.push('previous again -> ' + await atTop());
  console.log(out.join('\n'));
  await b.close();
})();
