// Zwei offene Gestaltungsfragen (BAU_AUFTRAG.md 3.4): je zwei begrenzte Prototypen mit denselben Beispieldaten.
// Die Prototypen entstehen nur hier, durch Austausch einzelner Teile der gebauten Seite im Browser; die ausgelieferte
// Datei enthält keinen Prototypcode. Bilder: simulation/bildschirmfotos/prototypen/. Chromium-Prüfung.
// Aufruf: node simulation/prototypen/prototypen.js
"use strict";
const { chromium } = require("playwright");
const path = require("path");
const SEITE = "file://" + path.resolve(__dirname, "..", "site", "index.html");
const BILD = path.resolve(__dirname, "..", "bildschirmfotos", "prototypen");

// Energiesäulen B: wie A, dazu gestrichelte Bezugslinie auf Höhe Q1 und Klammer „Q2 − Q1“ an Säule 2 (Nulllinie bleibt)
function energieB() {
  const R = window.KAFFEE.ergebnis(), de = document.documentElement.lang === "de";
  const f = (x, n) => { const s = x.toFixed(n); return de ? s.replace(".", ",") : s; };
  const q1 = R.Q1, q2 = R.Q2, m = Math.max(q1, q2, 1), W = 240, H = 150, B = 118, hoch = 92, Yb = q => B - hoch * q / m;
  let s = '<svg viewBox="0 0 ' + W + " " + H + '" role="img"><defs><pattern id="mq2b" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" stroke="#222" stroke-width="2"/></pattern></defs>';
  s += '<line x1="20" x2="200" y1="' + B + '" y2="' + B + '" stroke="#5a6b7f"/>';
  s += '<rect x="40" y="' + Yb(q1) + '" width="46" height="' + (B - Yb(q1)) + '" fill="#8b5a2b"/>';
  s += '<rect x="118" y="' + Yb(q2) + '" width="46" height="' + (B - Yb(q2)) + '" fill="url(#mq2b)" stroke="#222" stroke-width="1.5"/>';
  s += '<line x1="40" x2="172" y1="' + Yb(q1) + '" y2="' + Yb(q1) + '" stroke="#173d5e" stroke-dasharray="4 3"/>';
  s += '<path d="M 170 ' + Yb(q2) + " h 6 V " + Yb(q1) + ' h -6" fill="none" stroke="#173d5e" stroke-width="1.6"/>';
  s += '<text x="180" y="' + ((Yb(q1) + Yb(q2)) / 2 + 4) + '" font-size="11" fill="#173d5e" font-weight="600">+' + f(q2 - q1, 2) + " kJ</text>";
  s += '<text x="63" y="' + (Yb(q1) - 6) + '" text-anchor="middle" font-size="12">' + f(q1, 2) + " kJ</text>";
  s += '<text x="141" y="' + (Yb(q2) - 6) + '" text-anchor="middle" font-size="12">' + f(q2, 2) + " kJ</text>";
  s += '<text x="63" y="' + (B + 16) + '" text-anchor="middle" font-size="12">' + (de ? "Tasse 1" : "Cup 1") + '</text><text x="141" y="' + (B + 16) + '" text-anchor="middle" font-size="12">' + (de ? "Tasse 2" : "Cup 2") + "</text></svg>";
  const el = document.getElementById("energie-inhalt"); const satz = el.querySelector(".energie-satz").outerHTML; el.innerHTML = s + satz;
}
// Vertiefung am Handy B: Gruppen als Akkordeon (nur „Kaffee“ offen), Diagramm bleibt angeheftet
function vertiefungB() {
  for (const g of document.querySelectorAll("#vertiefung-inhalt .gruppe")) {
    const h = g.querySelector(".gruppe-titel"); if (!h || g.tagName === "FIELDSET") continue;
    const d = document.createElement("details"); d.className = "gruppe"; d.open = h.textContent.trim() === "Kaffee";
    const sm = document.createElement("summary"); sm.className = "gruppe-titel"; sm.textContent = h.textContent; d.appendChild(sm);
    h.remove(); while (g.firstChild) d.appendChild(g.firstChild); g.replaceWith(d);
  }
}

(async () => {
  const b = await chromium.launch();
  const bericht = [];
  for (const [w, hh] of [[390, 844], [1366, 768]]) {
    for (const fall of ["standard", "milch"]) {
      const p = await b.newPage({ viewport: { width: w, height: hh }, deviceScaleFactor: 2 });
      await p.goto(SEITE);
      await p.check('input[name="wahl-start"][value="1"]'); await p.click("#knopf-fest");
      if (fall === "milch") { await p.evaluate(() => { const v = document.getElementById("vertiefung"); v.open = true; v.dispatchEvent(new Event("toggle")); }); await p.check("#s-milch2Raum"); }
      await p.locator("#energie").screenshot({ path: path.join(BILD, "energie_A_" + fall + "_" + w + ".png") });
      await p.evaluate(energieB);
      await p.locator("#energie").screenshot({ path: path.join(BILD, "energie_B_" + fall + "_" + w + ".png") });
      await p.close();
    }
  }
  for (const art of ["A", "B"]) {
    const p = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
    await p.goto(SEITE);
    await p.check('input[name="wahl-start"][value="1"]'); await p.click("#knopf-fest");
    await p.fill("#frage-zahl", "50"); await p.click("#knopf-fest");
    await p.evaluate(() => { const v = document.getElementById("vertiefung"); v.open = true; v.dispatchEvent(new Event("toggle")); });
    if (art === "B") { await p.evaluate(vertiefungB); await p.evaluate(() => { const d = document.getElementById("z-thM").closest("details.gruppe"); d.open = true; }); }  // ein Tippen auf „Milch“
    const hoehe = await p.evaluate(() => Math.round(document.getElementById("vertiefung").getBoundingClientRect().height));
    // Blick beim Bewegen eines Reglers: Diagramm angeheftet oben, Regler „Milchtemperatur“ darunter
    await p.evaluate(() => document.getElementById("z-thM") && document.getElementById("z-thM").scrollIntoView({ block: "center" }));
    const sichtbar = await p.evaluate(() => { const r = document.getElementById("z-thM"); if (!r) return "zugeklappt"; const b = r.getBoundingClientRect(); return b.height > 0 ? "sichtbar" : "zugeklappt"; });
    await p.screenshot({ path: path.join(BILD, "vertiefung_" + art + "_390_regler.png") });
    await p.evaluate(() => document.getElementById("vertiefung").scrollIntoView({ block: "start" }));
    await p.screenshot({ path: path.join(BILD, "vertiefung_" + art + "_390_oben.png") });
    bericht.push("Vertiefung " + art + ": Höhe des Bereichs " + hoehe + " px bei 390 px Breite; Regler Milchtemperatur " + sichtbar);
    await p.close();
  }
  await b.close();
  console.log(bericht.join("\n"));
})();
