// Bedienungstest des Simulationstools im Browser (Chromium über Playwright) mit Bildschirmfotos in Handy- und Laptopbreite.
// Aufruf vom Repository aus: node ergebnisse/kaffee/simulation/browsertest.js
// Die Messwerte im Test sind erfundene Beispielwerte, keine echten Messungen.
// Abschnitte B bis F prüfen die Befunde Simulation 1 bis 5 der Prüfung durch Codex (Rolle X3), damit sie künftig auffallen.
const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");

const HIER = __dirname;
const DATEI = "file://" + path.join(HIER, "Kaffee_Simulation.html");
const BILDER = path.join(HIER, "bildschirmfotos");
fs.mkdirSync(BILDER, { recursive: true });
const ergebnisse = [];
const pruefe = (name, ok, info = "") => ergebnisse.push(`${ok ? "ok    " : "FEHLER"} ${name}${info ? "  " + info : ""}`);

async function regler(seite, id, wert) {
  await seite.$eval("#" + id, (e, v) => { e.value = v; e.dispatchEvent(new Event("input", { bubbles: true })); }, String(wert));
}
const aussage = seite => seite.textContent("#aussage");
const zahlen = seite => seite.textContent("#zahlen");
const zustand = seite => seite.evaluate(() => Object.assign({}, E));              // Einstellungen des Werkzeugs
const unterschied = async seite => {                                               // angezeigter Unterschied in K
  const m = (await zahlen(seite)).match(/ϑ₁ − ϑ₂ = (−?[0-9]+,[0-9]+) K/);
  return m ? parseFloat(m[1].replace("−", "-").replace(",", ".")) : NaN;
};
async function eintragen(seite, b, t, th) {
  await seite.selectOption("#m_becher", String(b));
  await seite.fill("#m_t", String(t));
  await seite.fill("#m_th", String(th));
  await seite.click("#messform button[type=submit]");
}
const zeilen = seite => seite.$$eval("#messtabelle tbody tr td[class=n]", r => r.length / 2);

(async () => {
  const browser = await chromium.launch();
  for (const [name, breite, hoehe, mobil] of [["handy", 390, 844, true], ["laptop", 1366, 900, false]]) {
    const kontext = await browser.newContext({ viewport: { width: breite, height: hoehe }, deviceScaleFactor: 2, isMobile: mobil, hasTouch: mobil });
    const seite = await kontext.newPage();
    seite.setDefaultTimeout(5000);
    // Jeder Abschnitt wird für sich bewertet: bricht er ab (z. B. fehlendes Element), zählt das als Fehler, der Test läuft weiter
    const abschnitt = async (kennung, f) => { try { await f(); } catch (err) { pruefe(`${name} ${kennung}: Abschnitt abgebrochen`, false, String(err.message).split("\n")[0]); } };
    const fehlerKonsole = [];
    seite.on("pageerror", e => fehlerKonsole.push(String(e)));
    seite.on("console", m => { if (m.type() === "error") fehlerKonsole.push(m.text()); });
    await seite.goto(DATEI);
    await seite.evaluate(() => { try { localStorage.clear(); } catch (e) { /* ohne Speicher */ } });
    await seite.reload();
    const breiteOk = async () => seite.evaluate(b => document.documentElement.scrollWidth <= b, breite);

    let z, e;
    // A. Standardwerte und Zahlen der Lösung
    await abschnitt("A", async () => {
    z = await zahlen(seite);
    pruefe(`${name} A: Standardwerte zeigen 34,05 °C und 30,19 °C`, z.includes("34,05 °C") && z.includes("30,19 °C"));
    pruefe(`${name} A: Aussage Tasse 1 um 3,85 K wärmer`, (await aussage(seite)).includes("Tasse 1 (Milch sofort) ist um 3,85 K wärmer"));
    pruefe(`${name} A: Schnittpunkt 55,7 min mit Richtung, Q1 34,88 kJ, Q2 38,57 kJ`,
           z.includes("55,7 min") && z.includes("danach ist der schwarze Kaffee kühler als Tasse 1") && z.includes("34,88 kJ") && z.includes("38,57 kJ"));
    pruefe(`${name} A: kein waagerechtes Scrollen`, await breiteOk());
    await seite.screenshot({ path: path.join(BILDER, `${name}_1_standard.png`), fullPage: true });
    await seite.click("summary");
    await (await seite.$("section:nth-of-type(2)")).screenshot({ path: path.join(BILDER, `${name}_3_weitere_groessen.png`) });
    await seite.click("summary");
    const indizes = await seite.$$eval("section.breit .formel sub", s => s.map(e => getComputedStyle(e).fontStyle));
    pruefe(`${name} A: Indizes ab und u im Kasten Modell aufrecht`, indizes.length >= 5 && indizes.every(x => x === "normal"), JSON.stringify(indizes));
    await regler(seite, "thM", 60);
    pruefe(`${name} A: erwärmte Milch 60 °C, Tasse 2 um 1,19 K wärmer`, (await aussage(seite)).includes("Tasse 2 (Milch später) ist um 1,19 K wärmer"));
    await seite.click("#standard"); await seite.check("#becher");
    z = await zahlen(seite);
    pruefe(`${name} A: Becher an, kA 0,4440 W/K, 34,04 und 30,96 °C`, z.includes("0,4440 W/K") && z.includes("34,04 °C") && z.includes("30,96 °C"));
    await seite.click("#standard"); await seite.check("#milch2Raum");
    pruefe(`${name} A: Milch für Tasse 2 bei Raumtemperatur, Tasse 1 um 1,95 K wärmer`, (await aussage(seite)).includes("um 1,95 K wärmer"));
    await seite.click("#standard"); await regler(seite, "tEnd", 40);
    pruefe(`${name} A: Zugabe nach 40 min, Unterschied 3,70 K`, (await aussage(seite)).includes("3,70 K"));
    });

    // B. Schnitt in Gegenrichtung (Simulation 1): Tasse 1 startet knapp über dem schwarzen Kaffee und kühlt schneller ab
    await abschnitt("B", async () => {
    await seite.click("#standard");
    for (const [id, v] of [["thK0", 60], ["thMess", 50], ["thM", 65], ["VM", 5], ["kA1", 110]]) await regler(seite, id, v);
    z = await zahlen(seite);
    const marke = await seite.$$eval("#diagramm circle[r='6']", c => c.length);
    pruefe(`${name} B: Schnitt in Gegenrichtung bei 1,4 min, danach schwarzer Kaffee wärmer, Marke im Diagramm`,
           z.includes("1,4 min") && z.includes("danach ist der schwarze Kaffee wärmer als Tasse 1") && marke === 1);
    await (await seite.$("main > section:nth-of-type(1)")).screenshot({ path: path.join(BILDER, `${name}_4_schnitt_gegenrichtung.png`) });
    await seite.click("#standard"); await regler(seite, "tEnd", 30);
    pruefe(`${name} B: kein Schnitt vor der Zugabe nach 30 min`, (await zahlen(seite)).includes("keiner bis zur Zugabe") &&
           (await seite.$$eval("#diagramm circle[r='6']", c => c.length)) === 0);
    });

    // C. Ungültige Einstellungen (Simulation 2): keine alten Ergebnisse, Hinweis am Ergebnis, Diagramm als ungültig
    await abschnitt("C", async () => {
    await seite.click("#standard"); await regler(seite, "thK0", 60);
    let a = await aussage(seite);
    pruefe(`${name} C: Anfang 60 °C unter dem Messwert 67 °C: keine Ergebniszahlen, Hinweis am Ergebnis`,
           (await zahlen(seite)).trim() === "" && a.startsWith("Keine Rechnung") &&
           (await seite.textContent("#diagramm")).includes("Einstellung ungültig"));
    await eintragen(seite, 2, "5", "70");
    pruefe(`${name} C: Messwert eintragen bei ungültiger Einstellung zeigt keine alten Ergebnisse`, (await zahlen(seite)).trim() === "");
    await seite.click("#leeren");
    await regler(seite, "thK0", 80);
    pruefe(`${name} C: wieder gültig, Ergebnisse wieder da`, (await zahlen(seite)).includes("34,05 °C"));
    await regler(seite, "thU", 30); await regler(seite, "thMess", 30);
    pruefe(`${name} C: Messwert gleich Raumtemperatur ist ungültig`, (await aussage(seite)).startsWith("Keine Rechnung"));
    await (await seite.$("main > section:nth-of-type(1)")).screenshot({ path: path.join(BILDER, `${name}_5_ungueltig.png`) });
    await seite.click("#standard");
    });

    // D. Übernahme unmöglicher Messreihen (Simulation 2 und 3): nichts verändern, deutlich ablehnen
    await abschnitt("D", async () => {
    for (const [reihe, text] of [[[100, 100, 15, 15], "100 °C und 15 °C"], [[65, 65, 70, 70], "65 °C und 70 °C"], [[80, 80, 18, 18], "10 min unter Raum"]]) {
      await seite.click("#leeren");
      await eintragen(seite, 2, "0", String(reihe[0])); await eintragen(seite, 3, "0", String(reihe[1]));
      await eintragen(seite, 2, "10", String(reihe[2])); await eintragen(seite, 3, "10", String(reihe[3]));
      const vorher = await zustand(seite);
      await seite.click("#uebernehmen");
      const nachher = await zustand(seite);
      const info = await seite.textContent("#uebernahme_info");
      pruefe(`${name} D: unmögliche Reihe (${text}) abgelehnt, Einstellungen unverändert`,
             info.startsWith("Nicht übernommen") && JSON.stringify(vorher) === JSON.stringify(nachher) && (await zahlen(seite)).includes("34,05 °C"), info.slice(0, 90));
    }
    // ungerundete Mittelwerte werden unverändert übernommen
    await seite.click("#leeren");
    await eintragen(seite, 2, "0", "80,2"); await eintragen(seite, 3, "0", "81,2");
    await eintragen(seite, 2, "10", "67,1"); await eintragen(seite, 3, "10", "66,8");
    await seite.click("#uebernehmen");
    e = await zustand(seite);
    pruefe(`${name} D: Mittelwerte ungerundet übernommen (80,7 und 66,95 °C), 40 min, Becher an`,
           Math.abs(e.thK0 - 80.7) < 1e-9 && Math.abs(e.thMess - 66.95) < 1e-9 && e.tEnd_min === 40 && e.becher === true &&
           (await seite.textContent("#o_thMess")).includes("66,95") && !(await aussage(seite)).startsWith("Keine Rechnung"),
           JSON.stringify([e.thK0, e.thMess]));
    await seite.click("#leeren"); await seite.click("#standard");
    });

    // E. Zahleneingabe (Simulation 5): nur ganze Zahlen mit Komma oder Punkt
    await abschnitt("E", async () => {
    const vor = await zeilen(seite);
    await eintragen(seite, 2, "10,5,9", "66.5xyz");
    pruefe(`${name} E: „10,5,9“ und „66.5xyz“ abgelehnt`, (await zeilen(seite)) === vor &&
           (await seite.getAttribute("#eingabe_info", "class")).includes("fehler"));
    await eintragen(seite, 2, "10,5", "66.5");
    const meld = await seite.textContent("#eingabe_info");
    pruefe(`${name} E: „10,5“ und „66.5“ angenommen, Fehlermeldung ersetzt`, (await zeilen(seite)) === vor + 1 && meld.startsWith("Eingetragen") &&
           !(await seite.getAttribute("#eingabe_info", "class")).includes("fehler"), meld);
    await eintragen(seite, 2, "", "66");
    pruefe(`${name} E: leere Zeit abgelehnt`, (await zeilen(seite)) === vor + 1);
    await seite.click("#leeren");
    });

    // F. Die vier Fragen in der Reihenfolge 1 bis 4, nur mit den Schritten, die der Fragetext verlangt (kein Zurücksetzen dazwischen)
    await abschnitt("F", async () => {
    // Ausgangslage: Zustand nach D und E soll keine Rolle spielen; Frage 1 sagt selbst „Laden Sie zuerst die Standardwerte“.
    await regler(seite, "thM", 30); await seite.check("#becher");                // verstellter Zustand wie nach freiem Probieren
    // Die Schritte folgen dem Wortlaut der Fragen: Standardwerte nur laden, wenn die Frage es verlangt (wie Studierende)
    const fragen = await seite.$$eval("ol.fragen li", l => l.map(x => x.textContent));
    pruefe(`${name} F: vier Fragen im Werkzeug`, fragen.length === 4);
    if (fragen[0].includes("Standardwerte")) await seite.click("#standard");   // Frage 1
    let best = [0, -1];
    for (let t = 1; t <= 120; t++) { await regler(seite, "tEnd", t); const d = await unterschied(seite); if (d > best[1]) best = [t, d]; }
    const bei120 = await unterschied(seite);
    pruefe(`${name} F1: größter Unterschied ungefähr bei 56 min (3,86 K), danach kleiner (120 min: 3,02 K)`,
           best[0] >= 53 && best[0] <= 59 && Math.abs(best[1] - 3.86) < 0.005 && Math.abs(bei120 - 3.02) < 0.005, JSON.stringify([best, bei120]));
    if (/60 Minuten/.test(fragen[1])) await regler(seite, "tEnd", 60);         // Frage 2
    let gleich = null;
    for (let th = 2; th <= 65; th += 0.5) { await regler(seite, "thM", th); if (Math.abs(await unterschied(seite)) < 0.03) { gleich = th; break; } }
    pruefe(`${name} F2: ungefähr gleich warm bei 47,0 °C Milch nach 60 min`, gleich === 47, String(gleich));
    await regler(seite, "tEnd", 30);
    const d30 = await unterschied(seite);
    pruefe(`${name} F2: bei Zugabe nach 30 min passt 47 °C nicht mehr (Temperatur hängt vom Zeitpunkt ab)`, Math.abs(d30) > 0.1, String(d30));
    if (fragen[2].includes("Standardwerte")) await seite.click("#standard");   // Frage 3, sonst geht es mit dem Zustand aus Frage 2 weiter
    const ohne = [await unterschied(seite), await zahlen(seite)];
    await seite.check("#becher");                                              // Frage 3: „Schalten Sie dann den Becher ein“
    z = await zahlen(seite);
    pruefe(`${name} F3: Unterschied 3,85 → 3,08 K, Wärme 34,88/38,57 → 46,60/50,34 kJ, Tasse 1 bleibt wärmer`,
           Math.abs(ohne[0] - 3.85) < 0.005 && ohne[1].includes("34,88 kJ") && z.includes("3,08 K") && z.includes("46,60 kJ") &&
           z.includes("50,34 kJ") && (await aussage(seite)).startsWith("Tasse 1 (Milch sofort)"));
    // Frage 4: Messwerte eintragen, Raum- und Milchtemperatur wie im Versuch, übernehmen (Beispielwerte)
    const beispiele = [[2, 0, "80,5"], [3, 0, "80,1"], [1, 0, "72,0"], [2, 10, "67,2"], [3, 10, "66,6"], [1, 40, "46,8"], [2, 40, "43,9"], [3, 40, "45,0"]];
    for (const [b, t, th] of beispiele) await eintragen(seite, b, String(t), th);
    await regler(seite, "thU", 21.5); await regler(seite, "thM", 6);
    await seite.click("#uebernehmen");
    e = await zustand(seite);
    const punkte = await seite.$$eval("#diagramm circle, #diagramm rect, #diagramm polygon", el => el.length);
    pruefe(`${name} F4: Übernahme Start 80,3 °C, 10 min 66,9 °C, 40 min, Becher an, 8 Messpunkte im Diagramm`,
           Math.abs(e.thK0 - 80.3) < 1e-9 && Math.abs(e.thMess - 66.9) < 1e-9 && e.tEnd_min === 40 && e.becher && e.thU === 21.5 &&
           (await seite.textContent("#uebernahme_info")).startsWith("Übernommen") && punkte >= 8 + 2, JSON.stringify([e.thK0, e.thMess, punkte]));
    pruefe(`${name} F4: kein waagerechtes Scrollen mit Messwerten`, await breiteOk());
    await seite.evaluate(() => window.scrollTo(0, 0));
    await seite.screenshot({ path: path.join(BILDER, `${name}_2_messwerte.png`), fullPage: true });
    await seite.reload();
    pruefe(`${name} F4: Messwerte nach dem Neuladen noch da`, (await zeilen(seite)) === 8);
    await seite.click("#leeren");
    });

    pruefe(`${name}: keine Fehler in der Konsole`, fehlerKonsole.length === 0, fehlerKonsole.join("; "));
    await kontext.close();
  }
  await browser.close();
  const text = ["Browsertest des Simulationstools (Chromium, Playwright)", "", ...ergebnisse, "",
                `Ergebnis: ${ergebnisse.filter(z => z.startsWith("ok")).length} von ${ergebnisse.length} Prüfungen bestanden.`].join("\n");
  fs.writeFileSync(path.join(HIER, "browsertest_ergebnis.txt"), text + "\n");
  console.log(text);
  process.exit(ergebnisse.every(z => z.startsWith("ok")) ? 0 : 1);
})();
