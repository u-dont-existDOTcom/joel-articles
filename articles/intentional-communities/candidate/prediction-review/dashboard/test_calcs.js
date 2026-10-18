const fs = require('fs');
const path = require('path');
const HERE = __dirname;
const js = fs.readFileSync(path.join(HERE, 'index.html'), 'utf8').match(/<script>([\s\S]*)<\/script>/)[1];
const rows = JSON.parse(fs.readFileSync(path.join(HERE, '..', 'prediction-calls-rows.json'), 'utf8')).rows;
const calcs = {};
const el = () => ({ style: {}, addEventListener() {}, replaceChildren() {}, append() {}, classList: { remove() {} }, dataset: {}, value: '' });
global.document = { getElementById: () => el(), querySelectorAll: () => [], createElement: () => el() };
global.d3 = { format: () => (v) => String(v) };
global.dash = { calc: (id, def) => { calcs[id] = def; }, data: () => ({ status: 'loading' }), onData: () => {}, colors: ['#111', '#222'] };
new Function(js)();
for (const [id, def] of Object.entries(calcs)) {
  const out = def.fn(rows);
  const arr = Array.isArray(out) ? out : [out];
  console.log(id, arr.length, JSON.stringify(arr.length > 3 ? arr.slice(-3) : arr).slice(0, 400));
}
