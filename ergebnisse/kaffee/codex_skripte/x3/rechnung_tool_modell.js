// Adapter des Prüflings. Keine unabhängigen Sollwerte in diesem Skript.
const fs = require('fs');
const vm = require('vm');
const path = require('path');
const root = path.resolve(__dirname, '../../../..');
const html = fs.readFileSync(path.join(root,'ergebnisse/kaffee/simulation/Kaffee_Simulation.html'),'utf8');
const code = html.split('// MODELL-ANFANG')[1].split('// MODELL-ENDE')[0];
const input = JSON.parse(fs.readFileSync(0,'utf8'));
const context = vm.createContext({});
vm.runInContext('// MODELL-ANFANG'+code, context);
const output = input.map(c => {
  context.settings=c.settings;
  context.times=c.times;
  return vm.runInContext(`(() => {
    const m=berechne(settings);
    return { ...m, kurve1: times.map(t=>m.kurve1(t*60)-K), kurve2: times.map(t=>m.kurve2(t*60)-K) };
  })()`,context);
});
process.stdout.write(JSON.stringify(output));
