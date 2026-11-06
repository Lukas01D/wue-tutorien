// Bilder der Abdeckungsmatrix (ZUSTAENDE.md, Abschnitt 7) nach simulation/bildschirmfotos/bau/.
// Chromium-Aufnahmen (Playwright, Cloud-Container), Gerätefaktor 2, Ausschnitt = Bildschirm (nicht ganze Seite), JPEG 85.
// Messblatt-Werte sind TESTDATEN aus simulation/tests/erwartung_browser.py, keine Messung der TL.
// Aufruf: node simulation/tests/bilder_bau.js
"use strict";
const { chromium } = require("playwright");
const fs = require("fs"), path = require("path");
const { execFileSync } = require("child_process");
const SEITE = "file://" + path.join(process.env.KAFFEE_ORDNER || path.resolve(__dirname, "..", "site"), "index.html");
const ZIEL = path.resolve(__dirname, "..", "bildschirmfotos", "bau");
const SOLL = JSON.parse(execFileSync("python3", [path.join(__dirname, "erwartung_browser.py")]).toString());
fs.mkdirSync(ZIEL, { recursive: true });
const G = { "390": [390, 844], "360": [360, 640], "844q": [844, 390], "1366": [1366, 768], "1280": [1280, 720], "1920": [1920, 1080] };
const ALLE = Object.keys(G);
const liste = [];

async function start(p) { await p.check('input[name="wahl-start"][value="1"]'); await p.fill("#frage-zahl", "4"); await p.click("#knopf-fest"); }
async function messblatt(p, bis, b3, deckel) {
  if (b3) await p.check("#mess-b3");
  if (deckel) await p.check("#mess-d");
  for (const b of b3 ? [1, 2, 3] : [1, 2]) for (let i = 0; i < bis; i++) {
    const v = SOLL.KURS["b" + b][i]; if (v === null) continue;
    const s = 'input[data-b="' + b + '"][data-i="' + i + '"]'; await p.fill(s, String(v).replace(".", ",")); await p.press(s, "Tab");
  }
  if (bis >= 8) { await p.fill("#mess-u", "21,5"); await p.press("#mess-u", "Tab"); await p.fill("#mess-m", "6"); await p.press("#mess-m", "Tab"); }
}
const vertiefungAuf = p => p.evaluate(() => { const v = document.getElementById("vertiefung"); v.open = true; v.dispatchEvent(new Event("toggle")); });

const ZUSTAENDE = [
  ["P0_start", ALLE, ["390", "1366"], async p => {}],
  ["P2_freigabe", ALLE, ["390", "1366"], async p => { await start(p); await p.evaluate(() => document.getElementById("simulation").scrollIntoView()); }],
  ["P4_frage1_56min", ["390", "1366"], ["390"], async p => { await start(p); await p.fill("#frage-zahl", "50"); await p.click("#knopf-fest"); await p.fill("#z-tEnd", "56"); await p.press("#z-tEnd", "Enter"); await p.evaluate(() => document.getElementById("simulation").scrollIntoView()); }],
  ["P6_frage2_kurswerte", ["390", "1366", "1280"], ["1366"], async p => { await start(p); await p.fill("#frage-zahl", "50"); await p.click("#knopf-fest"); await p.click("#knopf-weiter"); await messblatt(p, 8, false, false); await p.check('input[name="wahl-f2"][value="ueber"]'); await p.click("#knopf-fest"); await p.evaluate(() => document.getElementById("simulation").scrollIntoView()); }],
  ["V_voreinstellungen", ["390", "1366"], ["390"], async p => { await start(p); await vertiefungAuf(p); await p.click('[data-vor="keramik_deckel"]'); await p.evaluate(() => document.getElementById("info-kasten").scrollIntoView({ block: "end" })); }],
  ["V_waermestrom", ["1366"], [], async p => { await start(p); await vertiefungAuf(p); await p.click('[data-ansicht="waermestrom"]'); await p.evaluate(() => document.getElementById("ansichten").scrollIntoView()); }],
  ["V_ln_ausgleich", ["1366", "390"], [], async p => { await start(p); await vertiefungAuf(p); await messblatt(p, 8, false, false); await p.click('[data-ansicht="ln"]'); await p.evaluate(() => document.getElementById(innerWidth < 768 ? "diagramm-halter" : "ansichten").scrollIntoView()); }],
  ["M_messblatt_leer", ["390", "1366"], [], async p => { await start(p); await p.evaluate(() => document.getElementById("messblatt").scrollIntoView()); }],
  ["M_messblatt_halb", ["390", "1366"], [], async p => { await start(p); await messblatt(p, 4, false, false); await p.evaluate(() => document.getElementById("messblatt").scrollIntoView()); }],
  ["M_messblatt_voll", ["390", "1366"], [], async p => { await start(p); await messblatt(p, 8, false, false); await p.evaluate(() => document.getElementById("messblatt").scrollIntoView()); }],
  ["M_messblatt_deckel_becher3", ["390", "1366"], [], async p => { await start(p); await messblatt(p, 8, true, true); await p.evaluate(() => document.getElementById("messblatt").scrollIntoView()); }],
  ["R_modell", ["1366", "390"], ["1366"], async p => { await start(p); await p.click("#tab-modell"); await p.evaluate(() => { const d = document.querySelector("#panel-modell details"); if (d) d.open = true; document.getElementById("reiter-bereich").scrollIntoView(); }); }],
  ["R_code", ["1366", "390"], ["1366"], async p => { await start(p); await p.click("#tab-code"); await p.evaluate(() => document.getElementById("reiter-bereich").scrollIntoView()); }],
  ["R_modell_vor_P2_gesperrt", ["1366"], [], async p => { await p.click("#tab-modell"); await p.evaluate(() => { for (const d of document.querySelectorAll("#panel-modell details")) d.open = true; document.getElementById("reiter-bereich").scrollIntoView(); }); }],
  ["F_ungueltige_einstellung", ["390", "1366"], ["390"], async p => { await start(p); await vertiefungAuf(p); await p.check('input[name="kaq"][value="messung"]'); await p.fill("#z-thMess", "85"); await p.press("#z-thMess", "Enter"); await p.evaluate(() => document.getElementById("simulation").scrollIntoView()); }],
  ["F_kurslink_defekt", ["390"], ["390"], null, "#kurs1=u:21.5;m:6;d:0;b:1.2;b1:70,,,,,,34.1,;b2:180.4,67.8,57,49.2,43.1,38.2,34.6,31.2"],
  ["F_speicher_gesperrt", ["390"], [], async p => {}, "", true],
  ["F_unsinnige_zahl", ["390"], ["390"], async p => { await start(p); await vertiefungAuf(p); await p.fill("#z-VK", "zwei"); await p.press("#z-VK", "Enter"); await p.evaluate(() => document.getElementById("z-VK").scrollIntoView({ block: "center" })); }],
  ["T_fokus_sichtbar", ["1366"], [], async p => { for (let i = 0; i < 6; i++) await p.keyboard.press("Tab"); }],
];

(async () => {
  const b = await chromium.launch();
  for (const [name, de, en, aktion, hash, gesperrt] of ZUSTAENDE) {
    for (const [sprache, groessen] of [["de", de], ["en", en]]) for (const g of groessen) {
      const ctx = await b.newContext({ viewport: { width: G[g][0], height: G[g][1] }, deviceScaleFactor: 2 });
      if (gesperrt) await ctx.addInitScript(() => { const nein = () => { throw new Error("gesperrt"); }; Storage.prototype.setItem = nein; Storage.prototype.getItem = nein; });
      const p = await ctx.newPage();
      await p.goto(SEITE + (sprache === "en" ? "?lang=en" : "") + (hash || ""));
      if (aktion) await aktion(p);
      await p.waitForTimeout(150);
      const datei = name + "_" + sprache + "_" + g + ".jpg";
      await p.screenshot({ path: path.join(ZIEL, datei), type: "jpeg", quality: 85 });
      liste.push(datei);
      await ctx.close();
    }
  }
  // Handy mit Bildschirmtastatur (Zahlenfeld fokussiert, kleinere Fensterhöhe): Anheften aus
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
  const p = await ctx.newPage(); await p.goto(SEITE); await start(p); await vertiefungAuf(p);
  await p.focus("#z-thM"); await p.setViewportSize({ width: 390, height: 420 }); await p.waitForTimeout(250);
  await p.screenshot({ path: path.join(ZIEL, "T_tastatur_anheften_aus_de_390.jpg"), type: "jpeg", quality: 85 }); liste.push("T_tastatur_anheften_aus_de_390.jpg");
  await b.close();
  fs.writeFileSync(path.join(ZIEL, "LISTE.txt"), "Bilder der Abdeckungsmatrix (ZUSTAENDE.md 7), Chromium, Gerätefaktor 2, Bildschirmausschnitt.\nMessblatt-Werte sind Testdaten.\n\n" + liste.join("\n") + "\n");
  console.log(liste.length + " Bilder");
})().catch(e => { console.error(e); process.exit(1); });
