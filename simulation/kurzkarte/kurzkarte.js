// Kurzkarte für Studierende (BAU_AUFTRAG.md 5.2), Deutsch und Englisch, je eine A4-Seite als PDF mit auswählbarem Text.
// Fragen im Wortlaut der Seite (Texte aus der gebauten index.html, Formeln schon als MathML), Schrift Fira wie auf der Seite.
// QR-Code: nur Platzhalter, die Adresse entsteht erst mit der Veröffentlichung.
// Aufruf: node simulation/kurzkarte/kurzkarte.js   (schreibt Kurzkarte_DE.pdf, Kurzkarte_EN.pdf und Vorschaubilder)
"use strict";
const { chromium } = require("playwright");
const fs = require("fs"), path = require("path");
const HIER = __dirname, SITE = path.resolve(HIER, "..", "site");
const schrift = (f) => fs.readFileSync(path.join(SITE, "src", "schriften", f)).toString("base64");
const FONT = `@font-face{font-family:"Fira Sans";font-weight:400;src:url(data:font/woff2;base64,${schrift("FiraSans-Regular-teil.woff2")}) format("woff2")}
@font-face{font-family:"Fira Sans";font-weight:600;src:url(data:font/woff2;base64,${schrift("FiraSans-SemiBold-teil.woff2")}) format("woff2")}
@font-face{font-family:"Fira Sans";font-weight:700;src:url(data:font/woff2;base64,${schrift("FiraSans-Bold-teil.woff2")}) format("woff2")}
@font-face{font-family:"Fira Math";font-weight:400;src:url(data:font/woff2;base64,${schrift("FiraMath-teil.woff2")}) format("woff2")}`;

const K = {
  de: { titel: "Kaffee mit Milch: Simulation", zeile: "Kurzkarte",
    qr: "QR-Code der Seite<br>(wird nach der Veröffentlichung eingesetzt)",
    los: "So geht es", schritte: [
      "Öffne die Seite über den QR-Code. Arbeitet zu zweit an einem Gerät.",
      "Bei jeder Frage: Notiere zuerst für dich, dann einigt euch und haltet eure Vorhersage fest. Erst dann prüft ihr.",
      "Die Seite zeigt Ergebnisse erst nach eurer Vorhersage. Die Auflösung steht in der Karte der Frage (Reiter „Versuche“).",
      "Für Frage 2 lädt die Tutoriumsleitung die Messwerte eures Kurses als Link; ihr übernehmt sie mit einem Tipp."],
    fragen: "Die drei Fragen des Pflichtwegs", tassen: "Tasse 1 bekommt die Milch sofort, Tasse 2 erst nach 60 min.", start: "Start", f1: "Frage 1: Zeitpunkt", f2: "Frage 2: Versuch",
    danach: "Danach", danachText: "Für Schnelle und zum Nachbereiten: Vertiefung V1 bis V5 (Milchtemperatur, Deckel, Becher, Versuchsplan, welcher Becher). Jede Frage wieder mit Vorhersage.",
    hinweis: "Eingaben bleiben nur in deinem Browser; nichts wird verschickt. Die Seite funktioniert auch auf Englisch (Knopf „DE ↔ EN“) und offline als Datei." },
  en: { titel: "Coffee with milk: simulation", zeile: "quick guide",
    qr: "QR code of the page<br>(added after publication)",
    los: "How it works", schritte: [
      "Open the page with the QR code. Work in pairs on one device.",
      "For every question: first note your own answer, then agree in your pair and record your prediction. Only then check it.",
      "The page shows results only after your prediction. The explanation is in the card of the question (tab “Experiments”).",
      "For question 2 the tutor shares your class's measured values as a link; you take them over with one tap."],
    fragen: "The three questions of the core path", tassen: "Cup 1 gets the milk right away, cup 2 only after 60 min.", start: "Start", f1: "Question 1: time", f2: "Question 2: experiment",
    danach: "Afterwards", danachText: "For fast pairs and for revision: going further V1 to V5 (milk temperature, lid, mug, experiment design, which mug). Again with a prediction for each question.",
    hinweis: "Your inputs stay in your browser only; nothing is sent. The page also works in German (button “DE ↔ EN”) and offline as a file." }
};

function seite(s, T) {
  const k = K[s];
  return `<!doctype html><html lang="${s}"><head><meta charset="utf-8"><style>${FONT}
@page{size:A4;margin:16mm 17mm}
body{font-family:"Fira Sans",sans-serif;color:#142337;font-size:11.5pt;line-height:1.42;margin:0}
math{font-family:"Fira Math","Fira Sans";font-weight:700}
mfrac{font-size:0.8em}
.kopf{display:flex;align-items:center;gap:5mm;background:#102d49;color:#fff;padding:4mm 5mm;border-radius:1.5mm}
.marke{width:11mm;height:11mm;border-radius:1mm;background:#a9d5ef;color:#102d49;font-weight:700;display:grid;place-items:center;font-size:13pt}
.zeile{font-size:8.5pt;letter-spacing:.05em;text-transform:uppercase;opacity:.9;margin:0}
h1{font-size:19pt;margin:0;color:#fff}
.oben{display:grid;grid-template-columns:1fr 46mm;gap:7mm;margin-top:6mm}
.qr{border:1.2mm dashed #93bbd4;border-radius:2mm;height:46mm;display:grid;place-items:center;text-align:center;font-size:9pt;color:#5a6b7f;padding:2mm}
h2{color:#39718e;font-size:13.5pt;margin:0 0 2mm}
ol{margin:0;padding-left:5.5mm} li{margin:0 0 1.6mm}
.frage{border-left:1.2mm solid #39718e;background:#eef5fb;padding:2.5mm 4mm;margin:0 0 3mm;border-radius:0 1.5mm 1.5mm 0}
.frage b{display:block;color:#102d49;margin-bottom:.8mm}
.fragen{margin-top:6mm}
.danach{margin-top:5mm}
.fuss{margin-top:6mm;font-size:9.5pt;color:#5a6b7f;border-top:.3mm solid #d8e1ea;padding-top:2.5mm}
</style></head><body>
<div class="kopf"><div class="marke">WÜ</div><div><p class="zeile">${T.kopf_zeile} · ${k.zeile}</p><h1>${T.titel_seite}</h1></div></div>
<div class="oben"><div><h2>${k.los}</h2><ol>${k.schritte.map(x => "<li>" + x + "</li>").join("")}</ol></div><div class="qr">${k.qr}</div></div>
<div class="fragen"><h2>${k.fragen}</h2><p style="margin:0 0 2.5mm">${k.tassen}</p>
<div class="frage"><b>${k.start}</b>${T.start_text}</div>
<div class="frage"><b>${k.f1}</b>${T.f1_text}</div>
<div class="frage"><b>${k.f2}</b>${T.f2_text}</div></div>
<div class="danach"><h2>${k.danach}</h2><p style="margin:0">${k.danachText}</p></div>
<p class="fuss">${k.hinweis}</p>
</body></html>`;
}

(async () => {
  const b = await chromium.launch();
  const p0 = await b.newPage();
  await p0.goto("file://" + path.join(SITE, "index.html"));
  const TEXTE = await p0.evaluate(() => TEXTE);
  for (const s of ["de", "en"]) {
    const p = await b.newPage();
    await p.setContent(seite(s, TEXTE[s]), { waitUntil: "load" });
    await p.evaluate(() => document.fonts.ready);
    const datei = path.join(HIER, "Kurzkarte_" + s.toUpperCase() + ".pdf");
    await p.pdf({ path: datei, format: "A4", printBackground: true, preferCSSPageSize: true });
    console.log(datei, fs.statSync(datei).size + " Bytes");
    await p.close();
  }
  await b.close();
})();
