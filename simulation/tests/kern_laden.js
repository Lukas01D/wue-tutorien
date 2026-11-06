// Lädt die Rechenblöcke der Seite (MODELL unverändert, ERWEITERUNG) in Node, ohne Oberfläche.
// Aufruf: node kern_laden.js <auftrag.json>  (Auftrag: {"faelle": [...], "zeiten": {...}}), Ausgabe JSON auf stdout.
const fs = require("fs"), path = require("path"), vm = require("vm");
const SRC = path.join(__dirname, "..", "site", "src");
function kern(quelleHtml) {
  const ctx = {}; vm.createContext(ctx);
  let code;
  if (quelleHtml) {                                  // aus der fertigen Seite: Blöcke zwischen den Marken
    const h = fs.readFileSync(quelleHtml, "utf8");
    code = h.slice(h.indexOf("// MODELL-ANFANG"), h.indexOf("// MODELL-ENDE") + 14) + "\n" +
           h.slice(h.indexOf("// ERWEITERUNG-ANFANG"), h.indexOf("// ERWEITERUNG-ENDE") + 19);
  } else {
    code = fs.readFileSync(path.join(SRC, "modell.js"), "utf8") + "\n" + fs.readFileSync(path.join(SRC, "erweiterung.js"), "utf8");
  }
  vm.runInContext(code + "\nthis.ERW = ERW; this.berechne = berechne; this.P = P;", ctx);
  return ctx;
}
module.exports = { kern };
if (require.main === module) {
  const auftrag = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
  const k = kern(auftrag.html || null), E = k.ERW;
  const zahl = v => (typeof v === "number" ? (isFinite(v) ? v : (v > 0 ? "inf" : (v < 0 ? "-inf" : "nan"))) : v);
  const aus = auftrag.faelle.map(f => {
    const e = f.e, o = { fehler: E.fehler(e) };
    if (o.fehler) return o;
    const r = E.auswerten(e);
    for (const k2 of Object.keys(r)) if (typeof r[k2] === "number" || typeof r[k2] === "boolean") o[k2] = zahl(r[k2]);
    o.k1 = (f.zeiten || []).map(t => r.kurve1(t)); o.k2 = (f.zeiten || []).map(t => r.kurve2(t));
    o.q1 = (f.zeiten || []).map(t => r.qdot1(t)); o.q2 = (f.zeiten || []).map(t => r.qdot2(t));
    if (f.tV !== undefined) o.nach = E.nachZugabe(e, f.tV);
    if (f.trink !== undefined) { const tz = E.trinkzeit(e, f.trink); o.trink = { tasse1: zahl(tz.tasse1), schwarz: zahl(tz.schwarz) }; }
    if (f.kalt) o.kalt = E.becherKalt(e);
    if (f.gu) { const g = E.groessterUnterschied(e); o.gu = g; }
    return o;
  });
  const extra = {};
  if (auftrag.ausgleich) extra.ausgleich = auftrag.ausgleich.map(a => E.ausgleich(a.punkte, a.th0, a.thU, a.C_KB));
  extra.KA_AUFGABE = E.KA_AUFGABE; extra.VOREINSTELLUNGEN = E.VOREINSTELLUNGEN;
  process.stdout.write(JSON.stringify({ faelle: aus, extra: extra }));
}
