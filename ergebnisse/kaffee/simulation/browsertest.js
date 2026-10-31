// Bedienungstest des Simulationstools im Browser (Chromium über Playwright) mit Bildschirmfotos in Handy- und Laptopbreite.
// Aufruf vom Repository aus: node ergebnisse/kaffee/simulation/browsertest.js
// Die Messwerte im Test sind erfundene Beispielwerte, keine echten Messungen.
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

(async () => {
  const browser = await chromium.launch();
  for (const [name, breite, hoehe, mobil] of [["handy", 390, 844, true], ["laptop", 1366, 900, false]]) {
    const kontext = await browser.newContext({ viewport: { width: breite, height: hoehe }, deviceScaleFactor: 2, isMobile: mobil, hasTouch: mobil });
    const seite = await kontext.newPage();
    const fehlerKonsole = [];
    seite.on("pageerror", e => fehlerKonsole.push(String(e)));
    seite.on("console", m => { if (m.type() === "error") fehlerKonsole.push(m.text()); });
    await seite.goto(DATEI);

    // Standardwerte wie in der Aufgabe
    let z = await zahlen(seite);
    pruefe(`${name}: Standardwerte zeigen 34,05 °C und 30,19 °C`, z.includes("34,05 °C") && z.includes("30,19 °C"));
    pruefe(`${name}: Aussage Tasse 1 um 3,85 K wärmer`, (await aussage(seite)).includes("Tasse 1 (Milch sofort) ist um 3,85 K wärmer"));
    pruefe(`${name}: Schnittpunkt 55,7 min, Q1 34,88 kJ, Q2 38,57 kJ`, z.includes("55,7 min") && z.includes("34,88 kJ") && z.includes("38,57 kJ"));
    const breiteOk = async () => seite.evaluate(b => document.documentElement.scrollWidth <= b, breite);
    pruefe(`${name}: kein waagerechtes Scrollen`, await breiteOk());
    await seite.screenshot({ path: path.join(BILDER, `${name}_1_standard.png`), fullPage: true });
    await seite.click("summary");
    await (await seite.$("section:nth-of-type(2)")).screenshot({ path: path.join(BILDER, `${name}_3_weitere_groessen.png`) });
    await seite.click("summary");

    // Milchtemperatur wie in Teil f
    await regler(seite, "thM", 60);
    pruefe(`${name}: erwärmte Milch 60 °C, Tasse 2 um 1,19 K wärmer`, (await aussage(seite)).includes("Tasse 2 (Milch später) ist um 1,19 K wärmer"));
    // Gleichstand bei 47 °C
    await regler(seite, "thM", 47);
    pruefe(`${name}: Milch 47 °C, beide gleich warm`, (await aussage(seite)).includes("gleich warm"));
    // Becher wie in Teil g
    await seite.click("#standard");
    await seite.check("#becher");
    z = await zahlen(seite);
    pruefe(`${name}: Becher an, kA 0,4440 W/K, 34,04 und 30,96 °C`, z.includes("0,4440 W/K") && z.includes("34,04 °C") && z.includes("30,96 °C"));
    // Milch für Tasse 2 bei Raumtemperatur (Zusatzfrage 2)
    await seite.click("#standard");
    await seite.check("#milch2Raum");
    pruefe(`${name}: Milch für Tasse 2 bei Raumtemperatur, Tasse 1 um 1,95 K wärmer`, (await aussage(seite)).includes("um 1,95 K wärmer"));
    await seite.click("#standard");
    // Zeitpunkt 40 min
    await regler(seite, "tEnd", 40);
    pruefe(`${name}: Zugabe nach 40 min, Unterschied 3,70 K`, (await aussage(seite)).includes("3,70 K"));
    await seite.click("#standard");

    // Messwerte eintragen (Beispielwerte)
    const beispiele = [[2, 0, 80.5], [3, 0, 80.1], [1, 0, 72.0], [2, 10, 67.2], [3, 10, 66.6], [1, 40, 46.8], [2, 40, 43.9], [3, 40, 45.0]];
    for (const [b, t, th] of beispiele) {
      await seite.selectOption("#m_becher", String(b));
      await seite.fill("#m_t", String(t).replace(".", ","));
      await seite.fill("#m_th", String(th).replace(".", ","));
      await seite.click("#messform button[type=submit]");
    }
    const zeilenTab = await seite.$$eval("#messtabelle tbody tr", r => r.length);
    pruefe(`${name}: 8 Messwerte in der Tabelle`, zeilenTab === 8);
    const punkte = await seite.$$eval("#diagramm circle, #diagramm rect, #diagramm polygon", e => e.length);
    pruefe(`${name}: Messpunkte im Diagramm`, punkte >= 8 + 2, `(${punkte} Marken)`);
    pruefe(`${name}: kein waagerechtes Scrollen mit Messwerten`, await breiteOk());
    await seite.click("#uebernehmen");
    const werte = await seite.evaluate(() => [document.getElementById("thK0").value, document.getElementById("thMess").value,
                                              document.getElementById("tEnd").value, document.getElementById("becher").checked]);
    pruefe(`${name}: Übernahme Start 80,5 °C, 10 min 67 °C, 40 min, Becher an`,
           werte[0] === "80.5" && werte[1] === "67" && werte[2] === "40" && werte[3] === true, JSON.stringify(werte));
    await seite.evaluate(() => window.scrollTo(0, 0));
    await seite.screenshot({ path: path.join(BILDER, `${name}_2_messwerte.png`), fullPage: true });
    // Messwerte bleiben nach dem Neuladen
    await seite.reload();
    pruefe(`${name}: Messwerte nach dem Neuladen noch da`, (await seite.$$eval("#messtabelle tbody tr", r => r.length)) === 8);
    await seite.click("#leeren");
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
