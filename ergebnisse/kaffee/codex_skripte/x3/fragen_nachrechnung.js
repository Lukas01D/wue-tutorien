/* Erst NACH fragen_erstbefund.md und Erwartungslektüre erstellt.
 * Eigene skalare Nachrechnung aus den sichtbaren Abkuehl- und Mischgleichungen.
 * Kein Import von Werkzeugmodell, Referenzmodell oder Tests.
 */
const fs = require('fs');
const path = require('path');
const CK = 0.200 * 4180;
const CM = 0.030 * 1.030 * 3940;
const raum = 20, start = 80, mess = 67;
const rate = -Math.log((mess - raum) / (start - raum)) / (10 * 60);
function rechnen(tMin, milch = 5, becher = false) {
  const Cschwarz = CK + (becher ? 0.300 * 850 : 0);
  const Cgesamt = Cschwarz + CM;
  const kA = rate * Cschwarz;
  const mix = (Cschwarz * start + CM * milch) / Cgesamt;
  const schwarz = raum + (start - raum) * Math.exp(-rate * tMin * 60);
  const sofort = raum + (mix - raum) * Math.exp(-kA * tMin * 60 / Cgesamt);
  const spaeter = (Cschwarz * schwarz + CM * milch) / Cgesamt;
  return { sofort, spaeter, unterschied: sofort - spaeter,
    Q1_kJ: Cgesamt * (mix - sofort) / 1000,
    Q2_kJ: Cschwarz * (start - schwarz) / 1000, kA };
}
function bisektion(fn, lo, hi) {
  for (let n = 0; n < 80; n++) { const mid = (lo + hi) / 2; if (fn(mid) > 0) lo = mid; else hi = mid; }
  return (lo + hi) / 2;
}
// Maximierung auf der Zeitachse mit unabhängiger Intervallsuche.
let lo = 1, hi = 120;
for (let n = 0; n < 100; n++) {
  const a = lo + (hi - lo) / 3, b = hi - (hi - lo) / 3;
  if (rechnen(a).unterschied < rechnen(b).unterschied) lo = a; else hi = b;
}
const maximal = (lo + hi) / 2;
const ergebnis = {
  zeitpunktMaximumMin: maximal, maximum: rechnen(maximal),
  gleichheitMilchGrad: Object.fromEntries([30, 60, 90].map(t => [t, bisektion(m => rechnen(t, m).unterschied, 2, 80)])),
  becherAus: rechnen(60), becherAn: rechnen(60, 5, true),
  nachFrage2OhneRuecksetzung: rechnen(60, 47, true)
};
fs.writeFileSync(path.join(__dirname, 'fragen_nachrechnung.json'), JSON.stringify(ergebnis, null, 2) + '\n');
console.log(JSON.stringify(ergebnis, null, 2));
