// Bildschirmfotos eines Entwurfs in den Zuständen aus DESIGN_AUFTRAG.md, Schritt 5 (Chromium, Playwright).
// Aufruf: node simulation/design_entwuerfe/bilder_entwurf.js <ordner mit index.html> <zielordner> [gerätefaktor, Standard 2]
// Bilder: Bildschirmausschnitt (nicht ganze Seite), PNG. Gleiche Bedienfolge für alle Fassungen (auch „Variante 0“).
"use strict";
const { chromium } = require("playwright");
const fs = require("fs"), path = require("path");
const [ordner, ziel, faktorText] = process.argv.slice(2);
if (!ordner || !ziel) { console.error("Aufruf: bilder_entwurf.js <ordner> <ziel> [faktor]"); process.exit(1); }
const SEITE = "file://" + path.resolve(ordner, "index.html");
const FAKTOR = Number(faktorText || 2);
fs.mkdirSync(ziel, { recursive: true });

async function start(p) { await p.check('input[name="wahl-start"][value="1"]'); await p.fill("#frage-zahl", "4"); await p.click("#knopf-fest"); await p.waitForTimeout(120); }
async function frage1(p) { await start(p); await p.fill("#frage-zahl", "50"); await p.click("#knopf-fest"); await p.fill("#z-tEnd", "56"); await p.press("#z-tEnd", "Enter"); await p.waitForTimeout(120); }
const oben = (p, id) => p.evaluate(i => { const el = document.getElementById(i); window.scrollTo(0, el.getBoundingClientRect().top + window.scrollY - 0); }, id);

const ZUSTAENDE = [
  // Name, Sprache, Größen, Aktion
  ["1_startkarte", "de", ["390x844", "1366x768"], async p => {}],
  ["2_nach_vorhersage", "de", ["390x844", "1366x768"], async p => { await start(p); await oben(p, "simulation"); }],
  ["3_frage1_regler", "de", ["390x844", "1366x768"], async p => { await frage1(p); await p.evaluate(() => { const r = document.getElementById("regler-pflicht"); r.scrollIntoView({ block: "end" }); }); }],
  ["4_vertiefung", "de", ["390x844", "1366x768"], async p => { await start(p); await p.evaluate(() => { const v = document.getElementById("vertiefung"); v.open = true; v.dispatchEvent(new Event("toggle")); }); await p.waitForTimeout(120); await p.evaluate(() => document.getElementById("vertiefung").scrollIntoView({ block: "start" })); }],
  ["5_startkarte_en", "en", ["390x844", "1366x768"], async p => {}],
  ["6_beamer_nach_vorhersage", "de", ["1280x720"], async p => { await start(p); await oben(p, "simulation"); }],
];

(async () => {
  const b = await chromium.launch();
  const liste = [];
  for (const [name, sprache, groessen, aktion] of ZUSTAENDE) for (const g of groessen) {
    const [w, h] = g.split("x").map(Number);
    const ctx = await b.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: FAKTOR });
    const p = await ctx.newPage();
    const fehler = []; p.on("pageerror", e => fehler.push(e.message));
    await p.goto(SEITE + (sprache === "en" ? "?lang=en" : ""));
    await p.evaluate(() => document.fonts.ready);
    await aktion(p);
    await p.waitForTimeout(250);
    const datei = name + "_" + g + ".png";
    await p.screenshot({ path: path.join(ziel, datei) });
    const quer = await p.evaluate(() => document.documentElement.scrollWidth > innerWidth + 0.5);
    liste.push(datei + (quer ? "  QUERSCROLLEN" : "") + (fehler.length ? "  FEHLER " + fehler.join("; ") : ""));
    await ctx.close();
  }
  await b.close();
  console.log(liste.join("\n"));
})().catch(e => { console.error(e); process.exit(1); });
