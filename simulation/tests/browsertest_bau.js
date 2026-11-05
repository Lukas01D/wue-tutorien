// Browsertests der gebauten Kaffee-Seite (BAU_AUFTRAG.md Teil 3; ZUSTAENDE.md). Alle Prüfungen sind CHROMIUM-PRÜFUNGEN
// (Playwright mit dem vorinstallierten Chromium im Cloud-Container); WebKit ist nicht verfügbar, das iPhone bleibt offen
// (simulation/ABNAHME_IPHONE.md).
// Aufruf: node simulation/tests/browsertest_bau.js   (schreibt simulation/tests/browsertest_bau_ergebnis.txt)
// Erwartete Zahlen kommen aus der Python-Referenz (simulation/tests/erwartung_browser.py), nicht aus dem JavaScript der Seite.
//
// LEISTUNGSGRENZEN, festgelegt vor der ersten Messung (Messung im Cloud-Container, nicht auf einem Gerät der TL):
//   L1 Dateigröße unter 450 000 Bytes (Auftrag)
//   L2 Zeit bis bedienbar (Navigationsbeginn bis Startkarte mit aktivem Auswahlfeld): höchstens 1500 ms
//   L3 Reaktionszeit je Reglerschritt (Ereignis bis fertige Zeichnung, synchron gemessen): Median höchstens 25 ms,
//      95. Perzentil höchstens 50 ms, Maximum höchstens 150 ms
//   L4 Bedienfolge 30 s: keine Fehler, angezeigte Werte nach jedem Schritt gleich der Rechnung zum Zustand (nicht veraltet),
//      offene Zeitgeber nach 1 s Ruhe höchstens 2, Zuwachs des JS-Speichers nach Speicherbereinigung höchstens 5 MB
"use strict";
const { chromium } = require("playwright");
const fs = require("fs"), path = require("path"), os = require("os"), crypto = require("crypto"), http = require("http");
const { execFileSync } = require("child_process");

const SIM = path.resolve(__dirname, "..");
const SEITE = path.join(SIM, "site", "index.html");
const KOPIE = path.join(SIM, "site", "Kaffee_Simulation.html");
const SOLL = JSON.parse(execFileSync("python3", [path.join(__dirname, "erwartung_browser.py")]).toString());
const ERG = [];
let nr = 0;
function pruefe(name, ok, info) {
  nr++;
  const zeile = (ok ? "ok    " : "FEHLT ") + "B" + String(nr).padStart(2, "0") + " " + name + (info ? "  " + info : "");
  ERG.push({ name, ok: !!ok, zeile }); console.log(zeile);
}
const warte = ms => new Promise(r => setTimeout(r, ms));
const text = async (p, sel) => (await p.textContent(sel)).replace(/\s+/g, " ").trim();

// frisches Verzeichnis nur mit der Seite (ohne Begleitdateien)
const TMP = fs.mkdtempSync(path.join(os.tmpdir(), "kaffee-test-"));
fs.copyFileSync(KOPIE, path.join(TMP, "Kaffee_Simulation.html"));
const DATEI_URL = "file://" + path.join(TMP, "Kaffee_Simulation.html");

async function kontext(browser, opt = {}) {
  const ctx = await browser.newContext(Object.assign({ viewport: { width: 1366, height: 768 } }, opt));
  await ctx.addInitScript(() => {
    window.__csp = []; window.__timer = 0;
    document.addEventListener("securitypolicyviolation", e => window.__csp.push(e.violatedDirective + " " + e.blockedURI));
  });
  return ctx;
}
async function seite(ctx, url, fehler) {
  const p = await ctx.newPage();
  p.on("console", m => { if (m.type() === "error" || m.type() === "warning") fehler.push(m.type() + ": " + m.text()); });
  p.on("pageerror", e => fehler.push("pageerror: " + e.message));
  if (url) await p.goto(url);
  return p;
}
async function startFesthalten(p, wahl = "1", k = "4") {
  await p.check('input[name="wahl-start"][value="' + wahl + '"]');
  if (k !== null) await p.fill("#frage-zahl", k);
  await p.click("#knopf-fest");
}
async function f1Festhalten(p, min = "50") { await p.fill("#frage-zahl", min); await p.click("#knopf-fest"); }
async function messblattFuellen(p, mitB3) {
  if (mitB3) { await p.check("#mess-b3"); }
  for (const b of mitB3 ? [1, 2, 3] : [1, 2]) for (let i = 0; i < 8; i++) {
    const v = SOLL.KURS["b" + b][i]; if (v === null) continue;
    const sel = 'input[data-b="' + b + '"][data-i="' + i + '"]';
    await p.fill(sel, String(v).replace(".", ",")); await p.press(sel, "Tab");
  }
  await p.fill("#mess-u", "21,5"); await p.press("#mess-u", "Tab");
  await p.fill("#mess-m", "6"); await p.press("#mess-m", "Tab");
}
const RESULTATE = s => [SOLL.standard[s].th1, SOLL.standard[s].th2, SOLL.standard[s].dT, SOLL.standard[s].Q1, SOLL.standard[s].Q2];
async function domOhneSkript(p) {
  return p.evaluate(() => { const k = document.documentElement.cloneNode(true); for (const x of k.querySelectorAll("script")) x.remove(); return k.innerHTML; });
}

(async () => {
  const browser = await chromium.launch({ args: ["--js-flags=--expose-gc", "--enable-precise-memory-info"] });
  const allgemeineFehler = [];

  // ---------------------------------------------------------------- Artefakt
  const a = fs.readFileSync(SEITE), b = fs.readFileSync(KOPIE);
  pruefe("Artefakt: index.html und Kaffee_Simulation.html bytegleich", Buffer.compare(a, b) === 0, a.length + " Bytes");
  pruefe("Artefakt (L1): unter 450 000 Bytes unkomprimiert", a.length < 450000, a.length + " Bytes");
  const html = a.toString("utf8");
  const csp = (html.match(/http-equiv="Content-Security-Policy" content="([^"]+)"/) || [])[1] || "";
  const skript = (html.match(/<script>([\s\S]*?)<\/script>/) || [])[1] || "";
  const stil = (html.match(/<style>([\s\S]*?)<\/style>/) || [])[1] || "";
  const h = s => "'sha256-" + crypto.createHash("sha256").update(s, "utf8").digest("base64") + "'";
  pruefe("Artefakt: CSP mit default-src 'none' und Hashes, die zu Skript und Stil passen",
    /default-src 'none'/.test(csp) && csp.includes("script-src " + h(skript)) && csp.includes("style-src " + h(stil)) && !/unsafe/.test(csp), csp.slice(0, 60) + "…");
  pruefe("Artefakt: genau ein Skript- und ein Stilblock, keine externen Verweise (src=, href=http)",
    (html.match(/<script/g) || []).length === 1 && (html.match(/<style/g) || []).length === 1 && !/\ssrc="http|\shref="http|@import|url\(http/.test(html));
  pruefe("Artefakt: Schriften eingebettet (Fira Sans, Fira Math als woff2-data-URL)", /font-family: "Fira Sans"[^}]*data:font\/woff2/.test(html) && /font-family: "Fira Math"[^}]*data:font\/woff2/.test(html));

  // als Datei und über lokalen Server, frisches Profil, Anfragen protokolliert
  const server = http.createServer((req, res) => { const d = fs.readFileSync(path.join(TMP, "Kaffee_Simulation.html")); res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" }); res.end(d); });
  await new Promise(r => server.listen(0, "127.0.0.1", r));
  const SERVER_URL = "http://127.0.0.1:" + server.address().port + "/Kaffee_Simulation.html";
  for (const [art, url] of [["Datei (file:)", DATEI_URL], ["lokaler Server", SERVER_URL]]) {
    const profil = fs.mkdtempSync(path.join(os.tmpdir(), "kaffee-profil-"));
    const ctx = await chromium.launchPersistentContext(profil, { viewport: { width: 1366, height: 768 } });
    await ctx.addInitScript(() => { window.__csp = []; document.addEventListener("securitypolicyviolation", e => window.__csp.push(e.violatedDirective + " " + e.blockedURI)); });
    const fehler = [], anfragen = [];
    ctx.on("request", r => anfragen.push(r.url()));
    const p = await seite(ctx, null, fehler);
    await p.goto(url); await p.evaluate(() => document.fonts.ready);
    const schrift = await p.evaluate(() => document.fonts.check('16px "Fira Sans"') && document.fonts.check('700 16px "Fira Sans"') && document.fonts.check('16px "Fira Math"'));
    await startFesthalten(p);
    const kurven = await p.$$eval("#diagramm polyline", l => l.length);
    const cspV = await p.evaluate(() => window.__csp);
    const fremd = anfragen.filter(u => u !== url && !u.startsWith("data:"));
    pruefe("Artefakt " + art + ": frisches Profil, keine Fehler, keine CSP-Verletzung, keine Anfrage nach außen, Schrift geladen, bedienbar",
      !fehler.length && !cspV.length && !fremd.length && schrift && kurven >= 2,
      "Fehler " + fehler.length + ", CSP " + cspV.length + ", fremde Anfragen " + fremd.length + (fremd.length ? " (" + fremd.slice(0, 2).join(", ") + ")" : "") + ", Schrift " + schrift + ", Kurven " + kurven);
    await ctx.close();
  }

  // ---------------------------------------------------------------- Sperre vor der Vorhersage (P0, P1)
  for (const sprache of ["de", "en"]) {
    const ctx = await kontext(browser); const fehler = [];
    const p = await seite(ctx, DATEI_URL + (sprache === "en" ? "?lang=en" : ""), fehler);
    const verboten = RESULTATE("de").concat(RESULTATE("en"), [SOLL.standard.de.kA, SOLL.standard.en.kA]);
    const pruefen = async () => { const d = await domOhneSkript(p); return verboten.filter(x => d.includes(x)); };
    let treffer = await pruefen();
    for (const tab of ["modell", "code", "versuche"]) { await p.click("#tab-" + tab); await p.evaluate(() => { for (const d of document.querySelectorAll("details")) d.open = true; }); treffer = treffer.concat(await pruefen()); }
    const live = await p.$$eval('[aria-live], [role="status"], [role="alert"]', l => l.map(x => x.textContent).join("|"));
    const kurven = await p.$$eval("#diagramm polyline, #diagramm polygon", l => l.length);
    const tabelle = await text(p, "#wertetabelle-inhalt");
    pruefe("Sperre P0 (" + sprache + "): keine Ergebniszahl im DOM (ohne Skriptquelle), in Reitern, Tabellen, Ansagen; keine Kurven",
      !treffer.length && !/\d,\d\d|\d\.\d\d/.test(live) && kurven === 0 && !/\d/.test(tabelle), "Treffer " + JSON.stringify(treffer) + ", Kurven " + kurven);
    if (sprache === "de") {
      pruefe("P1: „Vorhersage festhalten“ erst nach einer Auswahl aktiv; Regler „Zugabe nach“ gesperrt", await p.isDisabled("#knopf-fest") && await p.isDisabled("#z-tEnd") && await p.isDisabled("#r-tEnd"));
      await p.check('input[name="wahl-start"][value="2"]');
      pruefe("P1: nach Auswahl aktiv, weiterhin kein Ergebnis", !(await p.isDisabled("#knopf-fest")) && !(await pruefen()).length);
    }
    pruefe("Sperre P0 (" + sprache + "): keine Konsolenfehler", !fehler.length, fehler.join("; "));
    await ctx.close();
  }

  // ---------------------------------------------------------------- Pflichtweg mit Zahlen gegen die Referenz
  {
    const ctx = await kontext(browser); const fehler = [];
    const p = await seite(ctx, DATEI_URL, fehler);
    await startFesthalten(p, "1", "4");
    const rw = await text(p, "#rechenwerte-liste"), st = SOLL.standard.de;
    const fehlt = ["th1", "th2", "dT", "Q1", "Q2", "kA", "th10", "tSchnitt"].filter(k => !rw.includes(st[k]));
    pruefe("P2 Freigabe: Rechenwerte gleich der Python-Referenz (ϑ1, ϑ2, Unterschied, Q1, Q2, kA, Mischtemperatur, Schnitt)", !fehlt.length, fehlt.length ? "fehlt " + fehlt.join(", ") + " in: " + rw.slice(0, 160) : st.th1 + " / " + st.th2 + " / " + st.dT);
    const en = await text(p, "#energie-inhalt");
    pruefe("P2: Energiesäulen mit Q1, Q2 und Satz Q2 − Q1 (3,69 kJ) und Unterschied", en.includes(st.Q1) && en.includes(st.Q2) && en.includes("3,69") && en.includes(st.dT), en.slice(0, 120));
    const fl = await text(p, "#frageleiste");
    pruefe("P2: Frageleiste bei Frage 1 mit Rückblick (Vorhersage, Auftrag Q1 und Q2, Auflösung zum Start)", /Frage 1 von 2/.test(fl) && /Erklärt den Unterschied/.test(fl) && await p.$("#knopf-aufl-start") !== null);
    pruefe("P2: Vorhersage als beschrifteter Kasten im Diagramm", (await p.$$eval("#diagramm text", l => l.map(x => x.textContent).join("|"))).includes("Tasse 1 (Milch sofort), etwa 4 K"));
    await p.click("#knopf-aufl-start");
    pruefe("P2: Auflösung zum Start nennt Unterschied, Temperaturen und C", (await text(p, "#aufl-start")).includes(st.dT) && (await text(p, "#aufl-start")).includes("957,7"));
    // Frage 1
    pruefe("P3: Regler „Zugabe nach“ gesperrt bis zur Vorhersage zu Frage 1", await p.isDisabled("#z-tEnd") && await p.isDisabled('.pm[data-r="tEnd"]'));
    await f1Festhalten(p, "50");
    pruefe("P4: Regler frei nach der Vorhersage", !(await p.isDisabled("#z-tEnd")) && !(await p.isDisabled("#r-tEnd")));
    await p.fill("#z-tEnd", "56"); await p.press("#z-tEnd", "Enter"); await warte(450);
    const rw56 = await text(p, "#rechenwerte-liste"), s56 = SOLL.t56.de;
    const ans = await text(p, "#ansage");
    pruefe("P4: Zugabe 56 min, Rechenwerte gleich der Referenz und Statusansage aktuell", ["th1", "th2", "dT", "Q1", "Q2"].every(k => rw56.includes(s56[k])) && ans.includes(s56.dT),
      s56.th1 + " / " + s56.th2 + " / " + s56.dT + "; Ansage: " + ans.slice(0, 80));
    await p.focus("#r-tEnd"); await p.keyboard.press("ArrowRight"); await warte(50);
    pruefe("P4: Pfeiltaste am Schieberegler ändert die Zugabe (57 min)", (await p.inputValue("#z-tEnd")) === "57");
    await p.click('.pm[data-r="tEnd"][data-pm="-1"]'); await warte(50);
    pruefe("P4: Minus-Knopf ändert die Zugabe (56 min)", (await p.inputValue("#z-tEnd")) === "56");
    // Frage 2
    await p.click("#knopf-weiter");
    pruefe("P5: Frage 2 ohne Kurswerte: Prüfen gesperrt, Überspringen angeboten", await p.isDisabled("#knopf-fest") && await p.$("#knopf-f2-weg") !== null);
    await messblattFuellen(p, false);
    await p.check('input[name="wahl-f2"][value="ueber"]');
    pruefe("P5: mit Kurswerten und Auswahl ist Prüfen aktiv", !(await p.isDisabled("#knopf-fest")));
    await p.click("#knopf-fest"); await warte(100);
    const z2 = await p.evaluate(() => window.KAFFEE.zustand().e), s2 = SOLL.kurs2.de;
    const rw2 = await text(p, "#rechenwerte-liste");
    pruefe("P6: Übernahme beim Prüfen (Mittel Becher 2 bei 0 und 10 min, kA aus der Messung, Becher an, 60 min, Raum 21,5, Milch 6)",
      z2.thK0 === 80 && z2.thMess === 67.6 && z2.kAQuelle === "messung" && z2.becher === true && z2.tEnd_min === 60 && z2.thU === 21.5 && z2.thM === 6, JSON.stringify(z2).slice(0, 150));
    pruefe("P6: Rechenwerte nach Übernahme gleich der Referenz", ["th1", "th2", "dT", "kA", "Q1", "Q2"].every(k => rw2.includes(s2[k])), s2.kA + " / " + s2.dT);
    const punkte = await p.$$eval("#diagramm rect[width='9'], #diagramm circle[r='4.8']", l => l.length);
    pruefe("P6: 15 Messpunkte im Diagramm (7 Becher 1, 8 Becher 2), Legende nennt nur gemessene Becher", punkte === 15 && !(await text(p, "#legende-mess")).includes("3"), punkte + " Punkte");
    pruefe("P7: Pflichtweg fertig, Knopf „Vertiefung öffnen“", await p.$("#knopf-vt-auf") !== null);
    // Neuladen behält alles
    const vor = await p.evaluate(() => JSON.stringify(window.KAFFEE.zustand()));
    await p.reload(); await warte(200);
    const nach = await p.evaluate(() => JSON.stringify(window.KAFFEE.zustand()));
    pruefe("Neuladen: Antworten, Einstellungen, Kurswerte und Ansicht bleiben", vor === nach);
    // Sprachwechsel
    await p.click("#sprachknopf"); await warte(100);
    const zen = await p.evaluate(() => window.KAFFEE.zustand());
    const rwEn = await text(p, "#rechenwerte-liste"), s2e = SOLL.kurs2.en;
    const fokus = await p.evaluate(() => document.activeElement.id);
    pruefe("Sprachwechsel: Zustand bleibt (außer Sprache), Zahlen mit Punkt, Fokus auf dem Umschalter, lang=en",
      JSON.stringify(Object.assign({}, zen, { sprache: "de" })) === nach && ["th1", "th2", "dT", "kA"].every(k => rwEn.includes(s2e[k])) && fokus === "sprachknopf" && await p.evaluate(() => document.documentElement.lang) === "en",
      s2e.th1 + " / " + s2e.kA);
    await p.reload(); await warte(100);
    pruefe("Sprachwahl bleibt beim Neuladen", await p.evaluate(() => document.documentElement.lang) === "en");
    await p.click("#sprachknopf");
    // Vertiefung: Ansichten, Becher 3, Ausgleichsgerade
    await p.click("#knopf-vt-auf"); await warte(100);
    pruefe("Vertiefung öffnen: Frageleiste bei V1, Vertiefung offen, Ansichten sichtbar", (await text(p, "#frageleiste")).includes("V1") && await p.evaluate(() => document.getElementById("vertiefung").open) && await p.isVisible('[data-ansicht="ln"]'));
    await p.click('[data-ansicht="ln"]'); await warte(100);
    const ln = await text(p, "#flaechen-text");
    pruefe("Ansicht ln: kA der Ursprungsgeraden aus Becher 2 gleich der unabhängigen Rechnung (6 Punkte)", ln.includes(SOLL.ln2.de) && ln.includes("6 Punkte"), ln.slice(0, 110));
    await p.check("#mess-b3");
    for (let i = 0; i < 8; i++) { const sel = 'input[data-b="3"][data-i="' + i + '"]'; await p.fill(sel, String(SOLL.KURS.b3[i]).replace(".", ",")); await p.press(sel, "Tab"); }
    await warte(100);
    const ln3 = await text(p, "#flaechen-text");
    pruefe("Ansicht ln mit Becher 3: Becher 2 und 3, 12 Punkte, gleich der Referenz", ln3.includes(SOLL.ln23.de) && ln3.includes("12 Punkte"), ln3.slice(0, 110));
    await p.click("#mess-ueber"); await warte(100);
    const z23 = await p.evaluate(() => window.KAFFEE.zustand().e), rw23 = await text(p, "#rechenwerte-liste");
    pruefe("Übernahme mit Becher 3: Mittel aus Becher 2 und 3; Rechenwerte inkl. Becher 3 gleich der Referenz",
      Math.abs(z23.thK0 - 79.8) < 1e-9 && Math.abs(z23.thMess - 67.4) < 1e-9 && ["th1", "th2", "dT", "kA", "th2Raum"].every(k => rw23.includes(SOLL.kurs23.de[k])), SOLL.kurs23.de.th2Raum);
    await p.click('[data-ansicht="waermestrom"]'); await warte(100);
    await p.click("#knopf-standard"); await warte(100);
    const fw = await text(p, "#flaechen-text");
    pruefe("Ansicht Wärmestrom (Standardwerte): Teilflächen mit Vorzeichen gleich der Referenz (3,70 und −0,01 kJ), Summe Q2 − Q1",
      fw.includes(SOLL.flaechen.de[0]) && fw.includes(SOLL.flaechen.de[1]) && fw.includes("3,69"), fw.slice(0, 140));
    const muster = await p.$$eval("#diagramm polygon", l => l.map(x => x.getAttribute("fill")));
    pruefe("Ansicht Wärmestrom: zwei verschieden schraffierte Teilflächen", muster.includes("url(#muster-vor)") && muster.includes("url(#muster-nach)"));
    await p.click('[data-ansicht="temperatur"]');
    pruefe("Pflichtweg und Vertiefung: keine Konsolenfehler", !fehler.length, fehler.join("; "));
    await ctx.close();
  }

  // ---------------------------------------------------------------- Vertiefung: Fragen V1 bis V5 und Voreinstellungen
  {
    const ctx = await kontext(browser); const fehler = [];
    const p = await seite(ctx, DATEI_URL, fehler);
    await startFesthalten(p);
    await p.evaluate(() => { document.getElementById("vertiefung").open = true; document.getElementById("vertiefung").dispatchEvent(new Event("toggle")); });
    await warte(100);
    pruefe("Vertiefung vor Frage 1: Hinweis „für danach gedacht“, nicht gesperrt", await p.isVisible("#vertiefung-frueh") && !(await p.isDisabled("#z-VK")));
    const erwartung = { v1: e => e.kAQuelle === "fest", v2: e => e.kAQuelle === "fest", v3: e => e.kAQuelle === "messung" && e.becher === true, v4: e => e.kAQuelle === "fest", v5: e => e.kAQuelle === "fest" };
    const eingabe = { v1: async () => p.fill("#frage-zahl", "20"), v2: async () => { await p.check('input[name="wahl-v2"][value="gleich"]'); }, v3: async () => p.check('input[name="wahl-v3"][value="kleiner"]'),
      v4: async () => p.check('input[name="wahl-v4"][value="ungleich"]'), v5: async () => p.check('input[name="wahl-v5"][value="thermo_offen"]') };
    const fehlerV = [];
    for (const v of ["v1", "v2", "v3", "v4", "v5"]) {
      await p.click("#tab-versuche"); await p.evaluate(id => { const d = document.querySelector('[data-karte="' + id + '"]'); d.open = true; }, v);
      await p.click('[data-zur="' + v + '"]'); await warte(50);
      if (!(await p.isDisabled("#knopf-fest"))) fehlerV.push(v + ": Prüfen vor Eingabe aktiv");
      await eingabe[v](); await p.click("#knopf-fest"); await warte(80);
      const z = await p.evaluate(() => window.KAFFEE.zustand());
      if (!z.antworten[v].fest) fehlerV.push(v + ": nicht festgehalten");
      if (!erwartung[v](z.e)) fehlerV.push(v + ": Ausgangslage " + JSON.stringify({ q: z.e.kAQuelle, b: z.e.becher }));
      await p.click("#knopf-aufl"); await warte(30);
      if (!(await p.isVisible("#aufl-leiste"))) fehlerV.push(v + ": Auflösung fehlt");
    }
    pruefe("Vertiefung V1 bis V5: Prüfen erst nach Eingabe, Ausgangslage wie ZUSTAENDE.md 2, Auflösung danach", !fehlerV.length, fehlerV.join("; "));
    await p.click("#knopf-standard"); await p.check('input[name="kaq"][value="fest"]');
    await p.click('[data-vor="keramik_deckel"]'); await warte(80);
    const info = await text(p, "#info-kasten"), rw = await text(p, "#rechenwerte-liste");
    pruefe("Voreinstellung Keramik mit Deckel: kA = 0,1905 W/K (0,56 · kA der Aufgabe), Anzeige 30 min gleich der Referenz, Herkunft genannt",
      rw.includes(SOLL.deckel.de.kA) && info.includes(SOLL.deckel.de.schwarz30) && /Keramik mit Deckel/.test(rw), SOLL.deckel.de.kA + ", " + SOLL.deckel.de.schwarz30 + " °C nach 30 min");
    await p.click("#knopf-standard"); await p.check("#s-milch2Raum"); await warte(80);
    const en = await text(p, "#energie-inhalt");
    pruefe("Milch für Tasse 2 bei Raumtemperatur: Unterschied gleich der Referenz (Pflichttest M3) und Milchbeitrag im Satz", en.includes(SOLL.milch2raum.de.dT) && /Milch/.test(en), SOLL.milch2raum.de.dT + " K: " + en.slice(0, 120));
    await p.uncheck("#s-milch2Raum");
    // ungültige Einstellung: Messung nach 10 min über der Anfangstemperatur
    await p.check('input[name="kaq"][value="messung"]'); await warte(50);
    await p.fill("#z-thMess", "85"); await p.press("#z-thMess", "Enter"); await warte(80);
    const fehlerText = await text(p, "#einstellung-fehler"), rwF = await text(p, "#rechenwerte-liste");
    pruefe("Ungültige Einstellung (Messung über dem Anfang): Meldung, Ergebnisse verdeckt, keine Kurven", await p.isVisible("#einstellung-fehler") && fehlerText.length > 10 && !/\d,\d\d/.test(rwF) &&
      (await p.$$eval("#diagramm polyline", l => l.length)) === 0, fehlerText.slice(0, 90));
    await p.fill("#z-thMess", "67"); await p.press("#z-thMess", "Enter"); await warte(50);
    // unsinnige Zahl im Feld
    const vorE = await p.evaluate(() => window.KAFFEE.zustand().e.VK_ml);
    await p.fill("#z-VK", "zwei"); await p.press("#z-VK", "Enter"); await warte(50);
    const meld = await text(p, "#rf-VK");
    pruefe("Unsinnige Zahl im Feld: Meldung, aria-invalid, Wert bleibt", meld.length > 5 && (await p.getAttribute("#z-VK", "aria-invalid")) === "true" && (await p.evaluate(() => window.KAFFEE.zustand().e.VK_ml)) === vorE, meld.slice(0, 80));
    await p.fill("#z-VK", "1.234,5"); await p.press("#z-VK", "Enter"); await warte(50);
    pruefe("Tausendertrennung im Feld wird abgelehnt", /Tausender/i.test(await text(p, "#rf-VK")));
    await p.fill("#z-VK", "250"); await p.press("#z-VK", "Enter"); await warte(50);
    await p.fill("#z-thK0", "79.5"); await p.press("#z-thK0", "Enter"); await warte(50);
    const zz = await p.evaluate(() => window.KAFFEE.zustand().e);
    pruefe("Feldeingaben mit Komma oder Punkt übernommen", zz.VK_ml === 250 && zz.thK0 === 79.5);
    // Für die nächste Gruppe zurücksetzen (Kurswerte bleiben)
    await messblattFuellen(p, false);
    await p.click("#knopf-gruppe"); await p.click("#rueck-ja"); await warte(80);
    const zr = await p.evaluate(() => window.KAFFEE.zustand());
    pruefe("Für die nächste Gruppe zurücksetzen: Startkarte (P0), Standardwerte, Kurswerte bleiben",
      zr.aktuell === "start" && !zr.antworten.start.fest && zr.e.VK_ml === 200 && zr.kurs.werte.b2[0] === 80 && (await p.$$eval("#diagramm polyline", l => l.length)) === 0);
    pruefe("Vertiefung und Fehlerfälle: keine Konsolenfehler", !fehler.length, fehler.join("; "));
    await ctx.close();
  }

  // ---------------------------------------------------------------- Kann-Punkte (Konzept K-3, K-4, K-5; Werte aus M9, M10, M11)
  {
    const ctx = await kontext(browser, { acceptDownloads: true }); const fehler = [];
    const p = await seite(ctx, DATEI_URL, fehler);
    await startFesthalten(p);
    await p.evaluate(() => { const v = document.getElementById("vertiefung"); v.open = true; v.dispatchEvent(new Event("toggle")); }); await warte(50);
    await p.check("#s-trink"); await warte(50);
    const tr = await text(p, "#zusatz-text");
    const linie = await p.$$eval("#diagramm line[stroke='#227b48']", l => l.length);
    pruefe("Kann K-3 Trinkzeit 60 °C: Tasse 1 nach 10,9 min, schwarzer Kaffee nach 16,6 min (M10: 10,90 und 16,60), Linie im Diagramm", tr.includes("10,9 min") && tr.includes("16,6 min") && linie === 1, tr.slice(0, 90));
    pruefe("Kann K-4 Becher kalt: nur mit Becher und festgehaltenem kA wählbar", await p.isDisabled("#s-kalt"));
    await p.check("#s-becher"); await warte(50);
    await p.fill("#z-kA", "0,444"); await p.press("#z-kA", "Enter"); await warte(50);
    await p.check("#s-kalt"); await warte(50);
    const kt = await text(p, "#zusatz-text");
    pruefe("Kann K-4 Becher kalt (kA 0,4440, C_B 255 J/K): 59,85 / 65,98 °C, nach 60 min 30,67 und 28,05 °C, 2,62 K (vorgewärmt 3,08 K) wie M9",
      ["59,85", "65,98", "30,67", "28,05", "2,62", "3,08"].every(x => kt.includes(x)), kt.slice(-130));
    await p.click("#knopf-standard"); await warte(50);
    const csv = await p.evaluate(() => window.KAFFEE.csv());
    const z = csv.replace(/^\ufeff/, "").split("\r\n");
    const soll = { 1: "0;70,47;80,00", 2: "1;69,40;78,55", 3: "2;68,36;77,14", 11: "10;60,78;67,00" };
    const csvOk = Object.entries(soll).every(([i, v]) => z[i].startsWith(v)) && /^t \[min\];Modell Tasse 1 \[°C\]/.test(z[0]) && csv.startsWith("\ufeff") && z.length === 64;
    const [dl] = await Promise.all([p.waitForEvent("download"), p.click("#mess-csv")]);
    const pfad = await dl.path(); const inhalt = fs.readFileSync(pfad, "utf8");
    await p.click("#sprachknopf"); const csvEn = await p.evaluate(() => window.KAFFEE.csv()); await p.click("#sprachknopf");
    pruefe("Kann K-5 CSV: Kopfzeile mit Einheiten, UTF-8 mit BOM, Werte wie M11 (0;70,47;80,00 · 1;69,40;78,55 · 2;68,36;77,14 · 10;60,78;67,00), Englisch mit Komma und Punkt, Download aus der Datei",
      csvOk && inhalt === csv && dl.suggestedFilename() === "kaffee_simulation.csv" && csvEn.split("\r\n")[1] === "0,70.47,80.00,,", z.slice(1, 4).join(" | ") + " · " + dl.suggestedFilename());
    pruefe("Kann-Punkte: keine Konsolenfehler", !fehler.length, fehler.join("; "));
    await ctx.close();
  }

  // ---------------------------------------------------------------- Kurslink
  {
    const ctx = await kontext(browser); const fehler = [];
    const p = await seite(ctx, DATEI_URL, fehler);
    await startFesthalten(p); await messblattFuellen(p, true);
    await ctx.grantPermissions(["clipboard-read", "clipboard-write"]).catch(() => {});
    await p.click("#mess-link"); await warte(150);
    const link = await text(p, ".link-ausgabe");
    const kurs = await p.evaluate(() => window.KAFFEE.zustand().kurs);
    const ctx2 = await kontext(browser); const f2 = [];
    const p2 = await seite(ctx2, link, f2); await warte(100);
    const frage = await text(p2, "#link-banner");
    await p2.click("#link-ja"); await warte(80);
    const kurs2 = await p2.evaluate(() => window.KAFFEE.zustand().kurs);
    const hashWeg = await p2.evaluate(() => location.hash === "");
    pruefe("Kurslink: Hin und zurück gleich (mit Becher 3), Rückfrage vor dem Ersetzen, # danach aus der Adresse", JSON.stringify(kurs2.werte) === JSON.stringify(kurs.werte) && kurs2.u === 21.5 && kurs2.m === 6 && kurs2.b3 && /ersetzt/.test(frage) && hashWeg, link.length + " Zeichen");
    // Nein ändert nichts
    const vorher = await p2.evaluate(() => JSON.stringify(window.KAFFEE.zustand().kurs));
    await p2.goto(link.replace("b2:80", "b2:79")); await p2.reload(); await warte(80);
    await p2.click("#link-nein"); await warte(50);
    pruefe("Kurslink „Nicht übernehmen“: Kurswerte unverändert", (await p2.evaluate(() => JSON.stringify(window.KAFFEE.zustand().kurs))) === vorher);
    await ctx2.close();
    // beschädigte und fremde Links
    const basis = "kurs1=u:21.5;m:6;d:0;b:1.2;b1:70,,,,,,34.1,;b2:80.4,67.8,57,49.2,43.1,38.2,34.6,31.2";
    const faelle = [
      ["#" + basis.replace("b2:80.4", "b2:180.4"), /Wert 1 von Becher 2/],
      ["#" + basis.replace("67.8", "abc"), /Wert 2 von Becher 2/],
      ["#" + basis.replace("u:21.5", "u:60"), /Raumtemperatur/],
      ["#" + basis.replace("b:1.2", "b:1"), /Becher 2 muss/],
      ["#" + basis.replace("34.1,;", "34.1,30;"), /keinen Wert/],
      ["#" + basis.replace(",31.2", ""), /acht Werte/],
      ["#" + basis + ";b3:1,2,3,4,5,6,7,8", /nicht als gemessen/],
      ["#kurs1=" + "x".repeat(420), /400 Zeichen/],
      ["#etwas-anderes", /keine Kurswerte dieser Seite/]
    ];
    const falsch = [];
    for (const [hash, muster] of faelle) {
      const c = await kontext(browser); const ff = [];
      const q = await seite(c, DATEI_URL + hash, ff); await warte(60);
      const meldung = await text(q, "#link-banner"), k = await q.evaluate(() => window.KAFFEE.zustand().kurs);
      const nichts = k.werte.b2.every(x => x === null) && k.u === null;
      if (!muster.test(meldung) || !nichts || !(await q.evaluate(() => location.hash === "")) || ff.length) falsch.push(hash.slice(0, 40) + " → " + meldung.slice(0, 60));
      await c.close();
    }
    pruefe("Kurslink beschädigt oder fremd (" + faelle.length + " Fälle): Grund in Worten, nichts geändert, # entfernt", !falsch.length, falsch.join(" | "));
    pruefe("Kurslink: keine Konsolenfehler", !fehler.length && !f2.length, fehler.concat(f2).join("; "));
    await ctx.close();
  }

  // ---------------------------------------------------------------- Messblatt-Eingaben
  {
    const ctx = await kontext(browser); const fehler = [];
    const p = await seite(ctx, DATEI_URL, fehler);
    await startFesthalten(p);
    const z = async (b, i, v) => { const s = 'input[data-b="' + b + '"][data-i="' + i + '"]'; await p.fill(s, v); await p.press(s, "Tab"); await warte(30); return p.evaluate(([b, i]) => window.KAFFEE.zustand().kurs.werte["b" + b][i], [b, i]); };
    const r1 = await z(2, 0, "80,4"), r2 = await z(2, 1, "67.8"), r3 = await z(2, 2, "  57 ");
    const r4 = await z(2, 3, "abc"); const m4 = await text(p, "#mess-fehler");
    const r5 = await z(2, 3, ""); const r6 = await z(2, 4, "1.043,1"); const m6 = await text(p, "#mess-fehler");
    const r7 = await z(2, 5, "150");
    pruefe("Messblatt: Komma, Punkt, Leerzeichen gelesen; Unsinn, Tausender, außerhalb 0 bis 100 °C abgelehnt mit Meldung; leer = kein Wert",
      r1 === 80.4 && r2 === 67.8 && r3 === 57 && r4 === null && m4.length > 5 && r5 === null && r6 === null && /Tausender/i.test(m6) && r7 === null,
      [r1, r2, r3, r4, r5, r6, r7].join(", ") + " | " + m4.slice(0, 60));
    pruefe("Messblatt: Becher 1 hat keine Zeile „60 nach der Milch“", await p.isDisabled('input[data-b="1"][data-i="7"]'));
    await p.click("#mess-ueber"); await warte(50);
    const info = await text(p, "#mess-info");
    pruefe("Übernahme mit unvollständigen Werten: Meldung, Einstellungen unverändert (D116: ganz oder gar nicht)", /nicht übernommen/i.test(info) || (await p.evaluate(() => window.KAFFEE.zustand().e.kAQuelle)) === "messung", info.slice(0, 90));
    await p.click("#mess-weg"); await p.click("#rueck-ja"); await warte(50);
    pruefe("Kurswerte löschen (mit Rückfrage): Werte weg, Antworten bleiben", (await p.evaluate(() => window.KAFFEE.zustand().kurs.werte.b2.every(x => x === null))) && (await p.evaluate(() => window.KAFFEE.zustand().antworten.start.fest)));
    pruefe("Messblatt: keine Konsolenfehler", !fehler.length, fehler.join("; "));
    await ctx.close();
  }

  // ---------------------------------------------------------------- Speicher gesperrt
  {
    const ctx = await kontext(browser); const fehler = [];
    await ctx.addInitScript(() => { const nein = () => { throw new Error("gesperrt"); }; Storage.prototype.setItem = nein; Storage.prototype.getItem = nein; });
    const p = await seite(ctx, DATEI_URL, fehler);
    const hinweis = await text(p, "#speicher-hinweis");
    await startFesthalten(p);
    pruefe("Speicher gesperrt: Hinweis „nicht gespeichert“, Seite bleibt bedienbar", /nicht gespeichert/.test(hinweis) && (await p.$$eval("#diagramm polyline", l => l.length)) >= 2 && !fehler.filter(f => /pageerror/.test(f)).length, hinweis);
    await ctx.close();
  }

  // ---------------------------------------------------------------- Umbruch, Größen, Ziele, Tastatur, Anheften
  const GROESSEN = [[320, 640], [360, 640], [390, 844], [844, 390], [1280, 720], [1366, 768], [1920, 1080]];
  {
    const quer = [];
    for (const [w, hh] of GROESSEN) for (const sprache of ["de", "en"]) {
      const ctx = await kontext(browser, { viewport: { width: w, height: hh } }); const fehler = [];
      const p = await seite(ctx, DATEI_URL + (sprache === "en" ? "?lang=en" : ""), fehler);
      const breit = async zst => { const d = await p.evaluate(() => [document.documentElement.scrollWidth, window.innerWidth]); if (d[0] > d[1]) quer.push(w + "×" + hh + " " + sprache + " " + zst + ": " + d[0]); };
      await breit("P0"); await startFesthalten(p); await breit("P2");
      await p.evaluate(() => { const v = document.getElementById("vertiefung"); v.open = true; v.dispatchEvent(new Event("toggle")); }); await warte(50); await breit("Vertiefung");
      await p.click("#tab-code"); await breit("Reiter Code");
      if (fehler.length) quer.push(w + " " + sprache + ": " + fehler[0]);
      await ctx.close();
    }
    pruefe("Umbruch: kein waagrechtes Scrollen bei 320 bis 1920 px, beide Sprachen, P0, P2, Vertiefung, Reiter (320 px = 400 % Zoom bei 1280 px)", !quer.length, quer.slice(0, 5).join("; "));
    const ctx = await kontext(browser, { viewport: { width: 1366, height: 768 } });
    const p = await seite(ctx, DATEI_URL, []);
    await startFesthalten(p);
    await p.evaluate(() => { document.documentElement.style.fontSize = "200%"; });
    const d = await p.evaluate(() => [document.documentElement.scrollWidth, window.innerWidth]);
    pruefe("200 % Text bei 1366 px: kein waagrechtes Scrollen", d[0] <= d[1], d.join(" / "));
    await ctx.close();
  }
  {
    const ctx = await kontext(browser, { viewport: { width: 390, height: 844 } });
    const p = await seite(ctx, DATEI_URL, []);
    const klein = async () => p.evaluate(() => {
      const out = [];
      for (const el of document.querySelectorAll("button, input, summary, select, a[href]")) {
        const r = el.getBoundingClientRect(); if (!r.width || !r.height || getComputedStyle(el).visibility === "hidden") continue;
        if (el.type === "radio" || el.type === "checkbox") { const l = el.closest("label"); const lr = l ? l.getBoundingClientRect() : r; if (lr.height < 24) out.push("Label " + (l ? l.textContent.trim().slice(0, 20) : el.name) + " " + Math.round(lr.height)); continue; }
        const textlink = el.classList.contains("knopf-text") || el.classList.contains("sprung");
        const min = textlink ? 24 : 44;
        if (r.height < min - 0.5 || (!textlink && r.width < 43.5)) out.push((el.id || el.className || el.tagName) + " " + Math.round(r.width) + "×" + Math.round(r.height));
      }
      return out;
    });
    let zu = await klein(); await startFesthalten(p); zu = zu.concat(await klein());
    await p.evaluate(() => { const v = document.getElementById("vertiefung"); v.open = true; v.dispatchEvent(new Event("toggle")); }); await warte(50);
    zu = zu.concat(await klein());
    pruefe("Zielgrößen bei 390 px: Knöpfe, Felder, Regler mindestens 44 px; Textverweise und Auswahl-Labels mindestens 24 px", !zu.length, [...new Set(zu)].slice(0, 8).join("; "));
    // Anheften
    const pos = async () => p.evaluate(() => getComputedStyle(document.getElementById("diagramm-halter")).position);
    const hoch = await pos();
    await p.evaluate(() => { const v = document.getElementById("vertiefung"); v.open = true; v.dispatchEvent(new Event("toggle")); });
    await p.evaluate(() => document.getElementById("z-thM").scrollIntoView({ block: "end" })); await warte(100);
    const lage = await p.evaluate(() => { const d = document.getElementById("diagramm-halter").getBoundingClientRect(), r = document.getElementById("z-thM").getBoundingClientRect(); return [Math.round(d.top), Math.round(d.bottom), Math.round(r.top), Math.round(r.bottom), window.innerHeight]; });
    pruefe("Anheften wirkt beim Bedienen: Diagramm oben sichtbar, Regler Milchtemperatur darunter frei (390×844)", lage[0] >= -1 && lage[0] <= 5 && lage[2] >= lage[1] && lage[3] <= lage[4], lage.join(", "));
    await p.setViewportSize({ width: 390, height: 420 }); await warte(200);
    const tastatur = await pos();
    await p.setViewportSize({ width: 844, height: 390 }); await warte(200);
    const querf = await pos();
    pruefe("Diagramm angeheftet nur im Hochformat mit genug Höhe (390×844 sticky; 390×420 wie mit Tastatur und 844×390 nicht)", hoch === "sticky" && tastatur !== "sticky" && querf !== "sticky", [hoch, tastatur, querf].join(", "));
    await ctx.close();
  }
  {
    const ctx = await kontext(browser); const p = await seite(ctx, DATEI_URL, []);
    await p.focus("#tab-versuche");
    const sel = async () => p.evaluate(() => [document.activeElement.id, document.querySelector('[role=tab][aria-selected="true"]').id, [...document.querySelectorAll("[role=tabpanel]")].filter(x => !x.hidden).map(x => x.id).join()]);
    const folge = [];
    for (const taste of ["ArrowRight", "ArrowRight", "ArrowRight", "ArrowLeft", "End", "Home"]) { await p.keyboard.press(taste); folge.push((await sel()).join("/")); }
    const soll = ["tab-modell/tab-modell/panel-modell", "tab-code/tab-code/panel-code", "tab-versuche/tab-versuche/panel-versuche", "tab-code/tab-code/panel-code", "tab-code/tab-code/panel-code", "tab-versuche/tab-versuche/panel-versuche"];
    pruefe("Reiter mit Tastatur (Pfeile, Pos1, Ende), Auswahl und Fokus folgen, ein Panel sichtbar", JSON.stringify(folge) === JSON.stringify(soll), folge.join(" | "));
    // Fokus sichtbar und Reihenfolge im Kopf
    await p.keyboard.press("Tab"); await p.goto(DATEI_URL); await p.keyboard.press("Tab");
    const erster = await p.evaluate(() => document.activeElement.className);
    const umriss = await p.evaluate(() => getComputedStyle(document.activeElement).outlineStyle);
    pruefe("Tastatur: erster Tab „Zum Inhalt springen“, Fokus sichtbar", /sprung/.test(erster) && umriss !== "none", erster + ", " + umriss);
    await ctx.close();
  }

  // ---------------------------------------------------------------- axe-core (WCAG 2.2 AA, automatisch prüfbarer Teil)
  {
    const axeQuelle = fs.readFileSync(require.resolve("axe-core/axe.min.js", { paths: [__dirname] }), "utf8");
    const befunde = [];
    const lauf = async (p, wo) => {
      await p.evaluate(axeQuelle);
      const r = await p.evaluate(() => axe.run(document, { runOnly: { type: "tag", values: ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"] } }));
      for (const v of r.violations) befunde.push(wo + ": " + v.id + " (" + v.nodes.length + ")");
    };
    for (const [w, hh, sprache] of [[1366, 768, "de"], [390, 844, "de"], [1366, 768, "en"]]) {
      const ctx = await kontext(browser, { viewport: { width: w, height: hh } });
      const p = await seite(ctx, DATEI_URL + (sprache === "en" ? "?lang=en" : ""), []);
      await lauf(p, w + " " + sprache + " P0");
      await startFesthalten(p); await lauf(p, w + " " + sprache + " P2");
      await p.evaluate(() => { const v = document.getElementById("vertiefung"); v.open = true; v.dispatchEvent(new Event("toggle")); }); await warte(50);
      await messblattFuellen(p, false); await p.click('[data-ansicht="waermestrom"]').catch(() => {});
      await p.click("#tab-modell"); await p.evaluate(() => { for (const d of document.querySelectorAll("details")) d.open = true; });
      await lauf(p, w + " " + sprache + " Vertiefung");
      await ctx.close();
    }
    pruefe("axe-core 4.14.0 (wcag2a, 2aa, 21a, 21aa, 22aa): keine Verstöße in P0, P2, Vertiefung, DE und EN, 1366 und 390 px", !befunde.length, befunde.join("; "));
  }

  // ---------------------------------------------------------------- Leistung (Cloud-Container, Chromium)
  {
    const ctx = await kontext(browser);
    await ctx.addInitScript(() => {
      const offen = new Set(); const st = window.setTimeout, ct = window.clearTimeout;
      window.setTimeout = (f, ms, ...r) => { const id = st(() => { offen.delete(id); f(...r); }, ms); offen.add(id); return id; };
      window.clearTimeout = id => { offen.delete(id); ct(id); };
      window.__offen = () => offen.size;
    });
    const fehler = [];
    const p = await seite(ctx, null, fehler);
    const t0 = Date.now();
    await p.goto(DATEI_URL);
    await p.waitForSelector('input[name="wahl-start"]:not([disabled])');
    const bereit = await p.evaluate(() => performance.now());
    pruefe("Leistung L2: bedienbar nach höchstens 1500 ms (Cloud-Chromium)", bereit <= 1500, Math.round(bereit) + " ms (gemessen im Cloud-Container)");
    await startFesthalten(p); await f1Festhalten(p);
    await p.evaluate(() => { const v = document.getElementById("vertiefung"); v.open = true; v.dispatchEvent(new Event("toggle")); });
    const zeiten = await p.evaluate(() => {
      const r = document.getElementById("r-tEnd"), out = [];
      for (let i = 0; i < 120; i++) { const a = performance.now(); r.value = String(1 + (i * 7) % 180); r.dispatchEvent(new Event("input", { bubbles: true })); out.push(performance.now() - a); }
      return out.sort((x, y) => x - y);
    });
    const med = zeiten[60], p95 = zeiten[Math.floor(0.95 * zeiten.length)], max = zeiten[zeiten.length - 1];
    pruefe("Leistung L3: Reaktionszeit je Reglerschritt (120 Schritte): Median ≤ 25 ms, 95 % ≤ 50 ms, Max ≤ 150 ms", med <= 25 && p95 <= 50 && max <= 150, "Median " + med.toFixed(1) + " ms, 95 % " + p95.toFixed(1) + " ms, Max " + max.toFixed(1) + " ms (Cloud)");
    // Bedienfolge 30 s
    await p.evaluate(() => gc && gc());
    const speicher0 = await p.evaluate(() => performance.memory ? performance.memory.usedJSHeapSize : 0);
    const ende = Date.now() + 30000; let schritte = 0; const veraltet = [];
    const regler = ["tEnd", "VK", "thK0", "VM", "thM", "thU", "kA", "kA1"];
    let zufall = 20261105;
    const rnd = () => { zufall = (zufall * 1103515245 + 12345) % 2147483648; return zufall / 2147483648; };
    while (Date.now() < ende) {
      const id = regler[Math.floor(rnd() * regler.length)];
      const ok = await p.evaluate(([id, x]) => {
        const r = document.getElementById("r-" + id); if (!r || r.disabled) return "fehlt";
        const lo = Number(r.min), hi = Number(r.max), st = Number(r.step);
        r.value = String(lo + Math.round(x * (hi - lo) / st) * st); r.dispatchEvent(new Event("input", { bubbles: true })); r.dispatchEvent(new Event("change", { bubbles: true }));
        const R = window.KAFFEE.ergebnis(); const z = window.KAFFEE.zustand();
        const soll = R ? R.th1 : null;
        const dd = document.querySelector("#rechenwerte-liste dd");
        const ist = dd ? Number(dd.textContent.replace(",", ".").replace(/[^0-9.−-]/g, "").replace("−", "-")) : null;
        return soll === null ? "ungueltig" : (Math.abs(ist - Math.round(soll * 100) / 100) < 0.006 ? "ok" : "veraltet " + ist + " statt " + soll);
      }, [id, rnd()]);
      if (ok.startsWith("veraltet")) veraltet.push(id + ": " + ok);
      schritte++;
      if (schritte % 40 === 0) await p.click("#sprachknopf");
      if (schritte % 25 === 0) await p.click('[data-ansicht="' + ["temperatur", "waermestrom", "ln"][schritte / 25 % 3] + '"]');
      if (schritte % 60 === 0) await p.click("#knopf-standard");
      await warte(15);
    }
    await warte(1000);
    const offen = await p.evaluate(() => window.__offen());
    await p.evaluate(() => gc && gc());
    const speicher1 = await p.evaluate(() => performance.memory ? performance.memory.usedJSHeapSize : 0);
    const zuwachs = (speicher1 - speicher0) / 1e6;
    pruefe("Leistung L4: Bedienfolge 30 s (" + schritte + " Schritte, Regler, Sprache, Ansichten): keine Fehler, keine veralteten Werte, Zeitgeber ≤ 2, Speicherzuwachs ≤ 5 MB",
      !fehler.length && !veraltet.length && offen <= 2 && zuwachs <= 5, "Fehler " + fehler.length + ", veraltet " + veraltet.length + (veraltet.length ? " (" + veraltet[0] + ")" : "") + ", offene Zeitgeber " + offen + ", Speicher " + zuwachs.toFixed(2) + " MB (Cloud)");
    await ctx.close();
  }

  server.close();
  await browser.close();
  const n = ERG.filter(e => e.ok).length;
  const kopf = "Browsertests der Kaffee-Seite (Chromium-Prüfungen, Playwright, Cloud-Container), Stand " + new Date().toISOString().slice(0, 10) +
    "\nSeite: simulation/site/index.html, SHA-256 " + crypto.createHash("sha256").update(a).digest("hex") + "\n\n";
  fs.writeFileSync(path.join(__dirname, "browsertest_bau_ergebnis.txt"), kopf + ERG.map(e => e.zeile).join("\n") + "\n\nErgebnis: " + n + " von " + ERG.length + " Prüfungen bestanden.\n");
  console.log("\nErgebnis: " + n + " von " + ERG.length + " Prüfungen bestanden.");
  fs.rmSync(TMP, { recursive: true, force: true });
  process.exit(n === ERG.length ? 0 : 1);
})().catch(e => { console.error(e); process.exit(2); });
