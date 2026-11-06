// Korrekturrunde nach X5 (06.11.2026): je behobenem Befund ein Test, der auf dem Stand vor der Korrektur fehlschlägt
// und auf dem neuen Stand besteht. CHROMIUM-PRÜFUNGEN im Cloud-Container.
// Aufruf:  node simulation/tests/browsertest_korrektur.js                     (neuer Stand, simulation/site)
//          KAFFEE_ORDNER=<ordner mit index.html> node simulation/tests/browsertest_korrektur.js   (z. B. alter Stand)
// Ergebnis: simulation/tests/browsertest_korrektur_ergebnis.txt (nur beim neuen Stand) und Ausgabe auf der Konsole.
"use strict";
const { chromium } = require("playwright");
const fs = require("fs"), path = require("path");
const ORDNER = process.env.KAFFEE_ORDNER || path.resolve(__dirname, "..", "site");
const URL = "file://" + path.join(ORDNER, "index.html");
const ERG = [];
let nr = 0;
function pruefe(id, name, ok, info) {
  nr++;
  const zeile = (ok ? "ok    " : "FEHLT ") + "K" + String(nr).padStart(2, "0") + " " + id + " " + name + (info ? "  " + String(info).replace(/\s+/g, " ").slice(0, 220) : "");
  ERG.push({ id, ok: !!ok, zeile }); console.log(zeile);
}
const warte = ms => new Promise(r => setTimeout(r, ms));
async function neu(b, w = 1366, h = 768, extra = "") {
  const ctx = await b.newContext({ viewport: { width: w, height: h } });
  const p = await ctx.newPage(); p.fehler = [];
  p.on("pageerror", e => p.fehler.push(e.message));
  await p.goto(URL + extra); return p;
}
const zustand = p => p.evaluate(() => window.KAFFEE.zustand());
const txt = async (p, sel) => (await p.evaluate(s => { const e = document.querySelector(s); return e ? e.textContent : ""; }, sel)).replace(/\s+/g, " ");
async function start(p) { await p.check('input[name="wahl-start"][value="1"]'); await p.fill("#frage-zahl", "4"); await p.click("#knopf-fest"); await warte(60); }
async function f1(p) { await p.fill("#frage-zahl", "50"); await p.click("#knopf-fest"); await warte(60); }
async function vt(p) { await p.evaluate(() => { const v = document.getElementById("vertiefung"); v.open = true; v.dispatchEvent(new Event("toggle")); }); await warte(60); }
async function feld(p, sel, v) { await p.fill(sel, v); await p.press(sel, "Enter"); await warte(40); }
const KURS = { b1: ["80,2", "68,1", "59", "52,3", "47,1", "43", "39,8"], b2: ["80", "67,6", "58,8", "52", "46,9", "42,8", "39,6", "35,2"], b3: ["79,6", "67,2", "58,5", "51,8", "46,6", "42,6", "39,4", "37,9"] };
async function messblatt(p, b3) {
  if (b3) { await p.check("#mess-b3"); await warte(40); }
  for (const b of b3 ? ["b1", "b2", "b3"] : ["b1", "b2"]) for (let i = 0; i < KURS[b].length; i++) {
    const s = 'input[data-b="' + b.slice(1) + '"][data-i="' + i + '"]'; await p.fill(s, KURS[b][i]); await p.press(s, "Tab");
  }
  await p.fill("#mess-u", "21,5"); await p.press("#mess-u", "Tab"); await p.fill("#mess-m", "6"); await p.press("#mess-m", "Tab");
}
async function f2(p) { await p.click("#knopf-weiter"); await warte(60); await p.check('input[name="wahl-f2"][value="ueber"]'); await p.click("#knopf-fest"); await warte(80); }
async function test(id, name, fn, b) {
  let ok = false, info = "";
  try { const r = await fn(b); ok = r[0]; info = r[1]; } catch (e) { ok = false; info = "Abbruch: " + e.message.split("\n")[0]; }
  pruefe(id, name, ok, info);
}

(async () => {
  const b = await chromium.launch();
  console.log("Stand: " + URL);

  await test("X5-01", "V3 nach Frage 2 mit Kurswerten: vor der Vorhersage keine Becher-Lage (Rechenwerte ohne 3,08 K), Standardwerte angesagt", async b => {
    const p = await neu(b); await start(p); await f1(p); await messblatt(p, false); await f2(p);
    await p.click("#tab-versuche"); await p.evaluate(() => document.querySelector("#panel-versuche [data-zur='v3']").click()); await warte(100);
    const z = await zustand(p), rw = await txt(p, "#rechenwerte");
    return [z.aktuell === "v3" && !z.antworten.v3.fest && z.e.becher === false && !rw.includes("3,08"), "becher=" + z.e.becher + " · " + rw.slice(0, 80)];
  }, b);

  await test("X5-02", "So rechnet der Code: Energiedifferenz und Ableitung nennen C_GB mit Becher (DE und EN)", async b => {
    const p = await neu(b); await start(p); await f1(p); await p.click("#tab-code"); await warte(60);
    const de = await p.evaluate(() => document.getElementById("panel-code").innerHTML);
    await p.click("#sprachknopf"); await warte(60);
    const en = await p.evaluate(() => document.getElementById("panel-code").innerHTML);
    const n = h => (h.match(/<mi>C<\/mi><mi mathvariant="normal">GB<\/mi>/g) || []).length;
    return [n(de) >= 2 && n(en) >= 2, "C_GB in DE " + n(de) + ", EN " + n(en)];
  }, b);

  await test("X5-03", "Quellenwechsel: eigene Messung 66,5 °C wird nicht als Messung überschrieben; Ersatzwert gekennzeichnet; außerhalb des Bereichs abgelehnt", async b => {
    const p = await neu(b); await start(p); await f1(p); await vt(p);
    await p.check('input[name="kaq"][value="messung"]'); await warte(60); await feld(p, "#z-thMess", "66,5");
    await p.check('input[name="kaq"][value="fest"]'); await warte(60); await feld(p, "#z-kA", "0,25");
    const vor = await p.evaluate(() => window.KAFFEE.ergebnis().dT);
    await p.check('input[name="kaq"][value="messung"]'); await warte(80);
    const z = await zustand(p), nach = await p.evaluate(() => window.KAFFEE.ergebnis().dT), name = await txt(p, "#rl-thMess"), hin = await txt(p, "#thmess-ersatz");
    const teil1 = z.e.thMessErsatz === true && z.e.thMessEigen === 66.5 && Math.abs(nach - vor) < 1e-9 && !/^Messung/.test(name) && hin.includes("keine Messung");
    // außerhalb: 100 ml, 60 °C, Raum 10 °C, kA 1
    const q = await neu(b); await start(q); await f1(q); await vt(q);
    await feld(q, "#z-VK", "100"); await feld(q, "#z-thK0", "60"); await feld(q, "#z-thU", "10"); await feld(q, "#z-kA", "1");
    const kA0 = await q.evaluate(() => window.KAFFEE.ergebnis().kA);
    await q.click('input[name="kaq"][value="messung"]'); await warte(80);
    const z2 = await zustand(q), kA1 = await q.evaluate(() => window.KAFFEE.ergebnis().kA);
    const teil2 = z2.e.kAQuelle === "fest" && Math.abs(kA1 - kA0) < 1e-12 && (await txt(q, "#kaq-meldung")).includes("Nicht umgestellt");
    return [teil1 && teil2, "Eigen " + z.e.thMessEigen + ", Ersatz " + z.e.thMessErsatz + ", Name „" + name.slice(0, 30) + "“; außerhalb: Quelle " + z2.e.kAQuelle + ", kA " + kA0 + " → " + kA1];
  }, b);

  await test("X5-04", "Fokus nicht verdeckt bei 768 × 1024 und 32 px Grundschrift (Vertiefung, vorwärts und rückwärts)", async b => {
    const p = await neu(b, 768, 1024); await start(p); await f1(p); await vt(p);
    await p.evaluate(() => { document.documentElement.style.fontSize = "32px"; }); await warte(250);
    await p.focus("#knopf-standard").catch(() => {});
    let verdeckt = 0, n = 0;
    const mess = () => p.evaluate(() => { const a = document.activeElement, k = document.getElementById("kern-leiste"); if (!a || !k || !a.closest("#vertiefung")) return null; const r = a.getBoundingClientRect(), kr = k.getBoundingClientRect(); const sticky = getComputedStyle(k).position === "sticky" && kr.top <= 1; return sticky && r.top < kr.bottom - 1 && r.bottom > kr.top ? 1 : 0; });
    await p.focus("#vertiefung summary");
    for (let i = 0; i < 60; i++) { await p.keyboard.press("Tab"); await warte(15); const m = await mess(); if (m !== null) { n++; verdeckt += m; } }
    for (let i = 0; i < 60; i++) { await p.keyboard.press("Shift+Tab"); await warte(15); const m = await mess(); if (m !== null) { n++; verdeckt += m; } }
    return [n > 40 && verdeckt === 0, verdeckt + " von " + n + " Fokusstopps teilweise unter der Kernleiste"];
  }, b);

  await test("X5-05", "200 % Text: kein waagerechter Überlauf und keine Regler mit Breite 0 (320, 360, 390, 768, 1024 px)", async b => {
    const aus = [];
    for (const [w, h] of [[320, 640], [360, 640], [390, 844], [768, 768], [1024, 768]]) {
      const p = await neu(b, w, h); await start(p); await f1(p); await vt(p);
      await p.evaluate(() => { document.documentElement.style.fontSize = "200%"; }); await warte(200);
      aus.push(await p.evaluate(() => [innerWidth, document.documentElement.scrollWidth, [...document.querySelectorAll("input[type=range]")].filter(x => x.offsetParent).map(x => x.getBoundingClientRect().width).filter(x => x < 44).length]));
      await p.context().close();
    }
    return [aus.every(([w, sw, null0]) => sw <= w && null0 === 0), aus.map(a => a.join("/")).join(" ")];
  }, b);

  await test("X5-06", "Schnittkreis immer mit Beschriftung im Diagramm (6 Breiten, DE und EN, 19 Einstellungen)", async b => {
    let n = 0, ohne = 0; const bsp = [];
    for (const [w, h] of [[320, 640], [360, 640], [390, 844], [768, 1024], [1366, 768], [1920, 1080]]) for (const lang of ["de", "en"]) {
      const p = await neu(b, w, h, lang === "en" ? "?lang=en" : ""); await start(p); await f1(p); await vt(p);
      for (const [id, werte, std] of [["#z-tEnd", ["20", "40", "56", "60", "75", "90", "120", "150", "180"], "60"], ["#z-thM", ["20", "35", "47", "55", "65"], "5"], ["#z-thU", ["10", "15", "25", "30"], "20"]]) {
        for (const v of werte) {
          await feld(p, id, v);
          const r = await p.evaluate(() => { const s = document.getElementById("diagramm"); return [[...s.querySelectorAll("circle")].some(c => c.getAttribute("r") === "5.5"), [...s.querySelectorAll("text")].some(t => /^(schnitt|intersection)$/i.test(t.textContent))]; });
          if (r[0]) { n++; if (!r[1]) { ohne++; if (bsp.length < 3) bsp.push(w + lang + id + "=" + v); } }
        }
        await feld(p, id, std);
      }
      await p.context().close();
    }
    return [n > 100 && ohne === 0, ohne + " von " + n + " ohne Beschriftung " + bsp.join(", ")];
  }, b);

  await test("X5-07", "Messblatt nimmt höchstens zwei Nachkommastellen an (wie der Kurslink); Link hin und zurück ohne Verlust", async b => {
    const p = await neu(b); await feld(p, "#mess-u", "21,555"); await feld(p, "#mess-m", "6,12");
    const z = await zustand(p), ung = await p.evaluate(() => document.getElementById("mess-u").getAttribute("aria-invalid"));
    await p.fill('input[data-b="2"][data-i="0"]', "80,123"); await p.press('input[data-b="2"][data-i="0"]', "Tab"); await warte(40);
    const z2 = await zustand(p);
    const link = await p.evaluate(() => HILFEN.kurslinkBauen(window.KAFFEE.zustand().kurs));
    const zur = await p.evaluate(l => HILFEN.kurslinkLesen("#" + l), link);
    return [z.kurs.u === null && ung === "true" && z2.kurs.werte.b2[0] === null && z.kurs.m === 6.12 && zur.art === "ok" && zur.kurs.m === 6.12, "u " + z.kurs.u + ", m " + z.kurs.m + ", b2[0] " + z2.kurs.werte.b2[0] + ", Link " + zur.art];
  }, b);

  await test("X5-08", "Sprachwechsel übersetzt die stehende Fehlermeldung und den Hinweis zu einem fremden Link", async b => {
    const p = await neu(b); await start(p); await f1(p); await vt(p);
    await p.check('input[name="kaq"][value="messung"]'); await warte(60); await feld(p, "#z-thK0", "60");
    const de = await txt(p, "#einstellung-fehler"); await p.click("#sprachknopf"); await warte(80);
    const en = await txt(p, "#einstellung-fehler");
    const q = await neu(b, 1366, 768, "#kurs9=x"); await warte(80); await q.click("#sprachknopf"); await warte(80);
    const ban = await txt(q, "#link-banner");
    return [/Messwert/.test(de) && !/Messwert|zwischen/.test(en) && en.length > 10 && !/Link|Kurswerte/.test(ban) && ban.length > 10, "DE „" + de.slice(0, 40) + "“ EN „" + en.slice(0, 40) + "“ Link „" + ban.slice(0, 40) + "“"];
  }, b);

  await test("X5-09", "Angeheftetes Diagramm: kleinste Schrift mindestens 10 px (320 × 640 bis 412 × 915)", async b => {
    const m = [];
    for (const [w, h] of [[320, 640], [360, 640], [375, 667], [390, 844], [412, 915]]) {
      const p = await neu(b, w, h); await start(p); await f1(p); await warte(150);
      m.push(await p.evaluate(() => { const s = document.getElementById("diagramm"), a = s.getScreenCTM().a; let k = 99; for (const t of s.querySelectorAll("text")) k = Math.min(k, parseFloat(t.getAttribute("font-size") || 12) * a); return [document.documentElement.classList.contains("anheften"), +k.toFixed(1)]; }));
      await p.context().close();
    }
    return [m.filter(x => x[0]).length >= 4 && m.every(([an, k]) => !an || k >= 10), m.map(x => (x[0] ? "an " : "aus ") + x[1]).join(", ")];
  }, b);

  await test("X5-10", "Angehefteter Bereich höchstens 45 % auch bei 125 bis 200 % Grundschrift", async b => {
    const m = [];
    for (const f of ["125%", "150%", "200%"]) for (const [w, h] of [[320, 640], [360, 640], [390, 844]]) {
      const p = await neu(b, w, h); await start(p); await p.evaluate(x => { document.documentElement.style.fontSize = x; }, f); await warte(200); await f1(p); await warte(200);
      m.push(await p.evaluate(() => [document.documentElement.classList.contains("anheften"), document.getElementById("diagramm-halter").getBoundingClientRect().height / innerHeight]));
      await p.context().close();
    }
    return [m.every(([an, r]) => !an || r <= 0.45), m.map(([an, r]) => (an ? "" : "(aus)") + (100 * r).toFixed(1)).join(" ")];
  }, b);

  await test("X5-11", "Fremdes Fragment: Hinweis und Entfernen aus der Adresse; eigener Sprunganker #hauptinhalt bleibt", async b => {
    const p = await neu(b, 1366, 768, "#foreign-data=123"); await warte(80);
    const ban = await txt(p, "#link-banner"), h = await p.evaluate(() => location.hash);
    const q = await neu(b, 1366, 768, "#hauptinhalt"); await warte(80);
    const sicht = await q.evaluate(() => !document.getElementById("link-banner").hidden), h2 = await q.evaluate(() => location.hash);
    return [/keine Kurswerte/.test(ban) && h === "" && !sicht && h2 === "#hauptinhalt", "Hinweis „" + ban.slice(0, 40) + "“, Adresse „" + h + "“; #hauptinhalt: Hinweis " + sicht];
  }, b);

  await test("F3, F6, G1-R4-01", "Startkarte mit Mitbewohner; Auflösung zum Start mit Erhaltung; „bis etwa 56 min“ erst nach der Vorhersage zu Frage 1", async b => {
    const p = await neu(b); const karte = await txt(p, "#frageleiste"); await start(p);
    await p.click("#knopf-aufl-start"); await warte(60); const a = await txt(p, "#aufl-start");
    await f1(p); await p.click("#tab-versuche"); await p.evaluate(() => { const d = document.querySelector("[data-karte='start']"); d.open = true; }); await p.evaluate(() => document.querySelector("[data-aufl='start']") && !document.getElementById("aufl-karte-start") && document.querySelector("[data-aufl='start']").click()); await warte(60);
    const nach = await txt(p, "#aufl-karte-start");
    return [/Mitbewohner/.test(karte) && /Erhalten bleibt die Energie von Kaffee, Milch und Raum/.test(a) && /fast bis zur Zugabe heißer/.test(a) && !/56 min/.test(a) && /bis etwa 56 min/.test(nach), a.slice(60, 200)];
  }, b);

  await test("F4, G10-03", "Frage 1: Vorhersage offen gefragt, „wieder kleiner“ erst nach dem Festhalten sichtbar", async b => {
    const p = await neu(b); await start(p); const vor = await txt(p, "#frageleiste"); await f1(p);
    const nachAuftrag = await txt(p, "#frageleiste .auftrag");
    return [/Wie ändert sich der Unterschied/.test(vor) && !/wieder kleiner/.test(vor) && /wieder kleiner/.test(nachAuftrag) && /Verschiebt die Zugabe/.test(nachAuftrag), nachAuftrag.slice(0, 100)];
  }, b);

  await test("F5", "Frage 2: Wortlaut ohne und mit Kurswerten", async b => {
    const p = await neu(b); await start(p); await f1(p); await p.click("#knopf-weiter"); await warte(60);
    const ohne = await txt(p, "#frageleiste .frage-text"); await messblatt(p, false); await warte(60);
    const p2 = await neu(b); await start(p2); await f1(p2); await messblatt(p2, false); await p2.click("#knopf-weiter"); await warte(60);
    const mit = await txt(p2, "#frageleiste .frage-text");
    return [/Ladet die Messwerte/.test(ohne) && /beim Prüfen aus den Messwerten übernommen/.test(ohne) && !/Ladet/.test(mit) && /Prüft dann: Beschreibt/.test(mit) && !/übernehmt/.test(ohne + mit), mit.slice(-90)];
  }, b);

  await test("F8, G4-16", "Abschluss erst nach geöffneter Auflösung von Frage 2, mit Kernsatz; V1 beantwortet die Teilfrage", async b => {
    const p = await neu(b); await start(p); await f1(p); await messblatt(p, false); await f2(p);
    const vor = await p.$("#knopf-vt-auf") === null; await p.click("#knopf-aufl"); await warte(60);
    const ls = await txt(p, "#frageleiste");
    await p.click("#knopf-vt-auf"); await warte(80); await p.fill("#frage-zahl", "47"); await p.click("#knopf-fest"); await warte(60); await p.click("#knopf-aufl"); await warte(60);
    const v1 = await txt(p, "#aufl-leiste");
    return [vor && /Wer heißer ist, gibt mehr Wärme ab/.test(ls) && /Ja, die Temperatur hängt vom Zeitpunkt ab/.test(v1), v1.slice(-120)];
  }, b);

  await test("F9", "V1, V3, V5 mit „Notiert für euch“; V4 nennt das Werkzeug (105 %); V5 nennt die Richtwerte", async b => {
    const p = await neu(b); await start(p); await p.click("#tab-versuche").catch(() => {});
    const k = await txt(p, "#panel-versuche");
    return [(k.match(/Notiert für euch/g) || []).length >= 3 && /105 %/.test(k) && /relativ/.test(k), (k.match(/Notiert für euch/g) || []).length + "× „Notiert für euch“"];
  }, b);

  await test("F11, G1-16, G1-07", "Modell vor dem Start ganz verdeckt; Sätze zum Schnitt in Modell und Code erst nach Frage 1", async b => {
    const p = await neu(b); await p.click("#tab-modell"); await p.evaluate(() => { for (const d of document.querySelectorAll("#panel-modell details")) d.open = true; });
    const vorStart = await txt(p, "#panel-modell");
    await start(p); await p.click("#tab-modell"); await p.evaluate(() => { for (const d of document.querySelectorAll("#panel-modell details")) d.open = true; });
    const vorF1 = await txt(p, "#panel-modell"); await p.click("#tab-code"); const codeVor = await txt(p, "#panel-code");
    await f1(p); await p.click("#tab-modell"); await p.evaluate(() => { for (const d of document.querySelectorAll("#panel-modell details")) d.open = true; });
    const nachF1 = await txt(p, "#panel-modell"); await p.click("#tab-code"); const codeNach = await txt(p, "#panel-code");
    return [!/Wärme an den Raum ab/.test(vorStart) && !/Links davon/.test(vorF1) && /Links davon/.test(nachF1) && !/Er wächst, solange/.test(codeVor) && /Er wächst, solange/.test(codeNach), "vor Start „" + vorStart.slice(0, 60) + "“"];
  }, b);

  await test("F12 (G3-06, G3-07, G3-10)", "Lesehilfe „bei Standardwerten“, „Schnitt der Temperaturkurven“, Annahmentext mit τ ≈ 41 min und Faktor 0,56", async b => {
    const p = await neu(b); await start(p); await f1(p); await p.click("#tab-modell"); await p.evaluate(() => { for (const d of document.querySelectorAll("#panel-modell details")) d.open = true; });
    const m = await txt(p, "#panel-modell"), rw = await txt(p, "#rechenwerte");
    return [/bei Standardwerten/.test(m) && /≈ 41 min/.test(m) && /0,56/.test(m) && /Schnitt der Temperaturkurven/.test(rw), rw.slice(0, 60)];
  }, b);

  await test("G2-R3-01", "Aufklapper der Frage heißt geöffnet „Frage ausblenden“", async b => {
    const p = await neu(b); await start(p); await f1(p);
    await p.click(".frage-text-zu summary"); await warte(60);
    return [(await txt(p, ".frage-text-zu summary")).includes("ausblenden"), await txt(p, ".frage-text-zu summary")];
  }, b);

  await test("G4-R3-01", "Übersprungene Frage 2: keine Aufforderung zum Laden und keine Ausgangslage mehr", async b => {
    const p = await neu(b); await start(p); await f1(p); await p.click("#knopf-weiter"); await warte(60); await p.click("#knopf-f2-weg"); await warte(80);
    const l = await txt(p, "#frageleiste");
    return [/übersprungen/.test(l) && !/Noch keine Kurswerte/.test(l) && !/Ausgangslage/.test(l), l.slice(0, 120)];
  }, b);

  await test("G6-R3-04", "Regler „Zugabe nach“ springt beim Schieben nicht (390 × 844, 1 bis 180 min)", async b => {
    const p = await neu(b, 390, 844); await start(p); await f1(p); await p.evaluate(() => { document.documentElement.classList.remove("anheften"); });
    const ys = new Set();
    for (let tz = 5; tz <= 180; tz += 4) { await feld(p, "#z-tEnd", String(tz)); ys.add(Math.round(await p.evaluate(() => document.getElementById("r-tEnd").getBoundingClientRect().top + scrollY))); }
    return [ys.size === 1, [...ys].join(", ")];
  }, b);

  await test("G6-R3-05", "Beschriftung der Trinklinie 60 °C liegt nicht auf Kurven, Messpunkten oder Marken (390 px, mehrere Zugaben)", async b => {
    const p = await neu(b, 390, 844); await start(p); await f1(p); await vt(p); await p.check("#s-trink"); await warte(60);
    let schlecht = 0, n = 0;
    for (const tz of ["20", "30", "45", "60", "90", "120"]) {
      await feld(p, "#z-tEnd", tz); n++;
      schlecht += await p.evaluate(() => { const s = document.getElementById("diagramm"); const t = [...s.querySelectorAll("text")].find(x => /Trink/.test(x.textContent)); if (!t) return 0; const r = t.getBBox(); const hit = (x, y) => x >= r.x && x <= r.x + r.width && y >= r.y && y <= r.y + r.height; for (const pl of s.querySelectorAll("polyline")) { for (const q of pl.getAttribute("points").split(" ")) { const [x, y] = q.split(",").map(Number); if (hit(x, y)) return 1; } } return 0; });
    }
    return [schlecht === 0, schlecht + " von " + n + " Lagen auf einer Kurve"];
  }, b);

  await test("G7-R3-01", "Becher 3 (Dreieck, Rechenwerte) erst nach der Vorhersage zu Frage 2", async b => {
    const p = await neu(b); await messblatt(p, true); await start(p);
    const vor = await p.evaluate(() => [document.querySelectorAll("#diagramm path[stroke='#3d70a3']").length, document.getElementById("rechenwerte").textContent.includes("Becher 3")]);
    await f1(p); await f2(p);
    const nach = await p.evaluate(() => [document.querySelectorAll("#diagramm path[stroke='#3d70a3']").length, document.getElementById("rechenwerte").textContent.includes("Becher 3")]);
    return [vor[0] === 0 && !vor[1] && nach[0] > 0 && nach[1], "vor " + vor.join("/") + ", nach " + nach.join("/")];
  }, b);

  await test("G8-R3-01", "Zweimal Enter auf „ohne Vorhersage aufdecken“ überspringt die Rückfrage nicht", async b => {
    const p = await neu(b); await start(p);
    await p.focus("#knopf-ohne"); await p.keyboard.press("Enter"); await p.keyboard.press("Enter"); await warte(80);
    const z = await zustand(p), box = await p.$("#rueck-box") !== null;
    return [!z.antworten.f1.fest && box, "f1 fest " + z.antworten.f1.fest + ", Rückfrage offen " + box];
  }, b);

  await test("G8-R3-02", "Zweiter Tipp 120 ms nach „Vorhersage festhalten“ (V3, 360 × 640) löst „Zurück“ nicht aus", async b => {
    // wie G8 (t19, s02): nach dem Neuaufbau liegt „Zurück“ unter dem Finger; hier direkt: Festhalten, nach 120 ms Klick auf „Zurück“
    const ctx = await b.newContext({ viewport: { width: 360, height: 640 }, hasTouch: true, isMobile: true }); const p = await ctx.newPage(); await p.goto(URL);
    await start(p); await f1(p); await p.click("#tab-versuche"); await p.evaluate(() => document.querySelector("#panel-versuche [data-zur='v3']").click()); await warte(500);
    await p.check('input[name="wahl-v3"][value="kleiner"]'); await warte(40);
    // zweiter Tipp an derselben Stelle (Koordinaten des ersten Tipps), dort liegt nach dem Neuaufbau „Zurück“
    await p.evaluate(() => new Promise(r => { const k = document.getElementById("knopf-fest").getBoundingClientRect(), x = k.x + k.width / 2, y = k.y + k.height / 2;
      document.getElementById("knopf-fest").dispatchEvent(new MouseEvent("click", { bubbles: true, detail: 1, clientX: x, clientY: y }));
      setTimeout(() => { const z = document.getElementById("knopf-zurueck"); if (z) z.dispatchEvent(new MouseEvent("click", { bubbles: true, detail: 1, clientX: x, clientY: y })); r(); }, 120); }));
    await warte(150);
    const z = await zustand(p);
    return [z.aktuell === "v3" && z.antworten.v3.fest, "aktuell " + z.aktuell + ", v3 fest " + z.antworten.v3.fest];
  }, b);

  await test("G8-R3-03", "CSV: Messwert „60 nach der Milch“ auch bei anderer Zugabe; Meldung vor der Vorhersage ohne Modellkurven", async b => {
    const p = await neu(b); await messblatt(p, false); await p.click("#mess-csv"); await warte(60);
    const meld = await txt(p, "#mess-info"); await start(p); await f1(p); await feld(p, "#z-tEnd", "90");
    const csv = await p.evaluate(() => window.KAFFEE.csv());
    return [!/Modellkurven in/.test(meld) && /60 nach der Milch[^\n]*;35,20/.test(csv), meld.slice(0, 60)];
  }, b);

  await test("G10-06", "Frage 2 vor ihrer Vorhersage zeigt nicht die Startvorhersage im Diagramm", async b => {
    const p = await neu(b); await start(p); await f1(p); await p.click("#knopf-weiter"); await warte(80);
    const k = await p.evaluate(() => (document.getElementById("vh-text") || {}).textContent || document.getElementById("vorhersage-zeile").textContent);
    return [!/Tasse 1 \(Milch sofort\)/.test(k), "„" + k + "“"];
  }, b);

  await test("G10-07", "Bestätigung des Kurslinks lässt sich schließen", async b => {
    const p = await neu(b, 1366, 768, "#kurs1=b1:70.9,,,,,,34.1,;b2:80.4,67.8,57,49.2,43.1,38.2,34.6,31.2;u:21.5;m:6;d:0;b:1.2"); await warte(80);
    await p.click("#link-ja"); await warte(60); const da = await p.$("#link-zu") !== null; if (da) await p.click("#link-zu"); await warte(40);
    return [da && await p.evaluate(() => document.getElementById("link-banner").hidden), "Knopf " + da];
  }, b);

  await test("G10-08", "Knopf zum Anheften nennt die Aktion je Zustand (Name gleich sichtbarem Text, kein aria-pressed)", async b => {
    const p = await neu(b, 390, 844); await start(p); const a = await txt(p, "#knopf-anheften"); await p.click("#knopf-anheften"); await warte(60); const c = await txt(p, "#knopf-anheften");
    const pr = await p.evaluate(() => document.getElementById("knopf-anheften").hasAttribute("aria-pressed"));
    return [a !== c && !pr, "„" + a + "“ → „" + c + "“"];
  }, b);


  await test("G1-R4-02, G1-R4-06", "Bestätigung des Kurslinks bleibt stehen (16 s) und „Hinweis schließen“ führt zur Frage, nicht ins Messblatt", async b => {
    const p = await neu(b, 390, 844); await start(p); await f1(p); await p.click("#knopf-weiter"); await warte(80);
    await p.evaluate(() => { location.hash = "#kurs1=b1:70.9,,,,,,34.1,;b2:80.4,67.8,57,49.2,43.1,38.2,34.6,31.2;u:21.5;m:6;d:0;b:1.2"; }); await warte(150);
    await p.click("#link-ja"); await warte(16200);
    const steht = await p.evaluate(() => !document.getElementById("link-banner").hidden);
    await p.click("#link-zu"); await warte(150);
    const r = await p.evaluate(() => [document.activeElement.id, Math.round(document.getElementById("frageleiste").getBoundingClientRect().top)]);
    return [steht && r[0] === "frage-titel" && r[1] > -100 && r[1] < 844, "Hinweis nach 16 s " + steht + ", Fokus " + r[0] + ", Frageleiste oben " + r[1]];
  }, b);

  await test("G1-R4-03", "V3 nach Frage 2: Hinweis zur Ausgangslage in der Frageleiste; vor dem Festhalten „Ausgangslage beim Prüfen“", async b => {
    const p = await neu(b, 390, 844); await start(p); await f1(p); await messblatt(p, false); await f2(p);
    await p.click("#tab-versuche"); await p.evaluate(() => document.querySelector("#panel-versuche [data-zur='v3']").click()); await warte(120);
    const l = await txt(p, "#frageleiste");
    return [/Ausgangslage vor deiner Vorhersage/.test(l) && /Ausgangslage beim Prüfen/.test(l), l.slice(0, 160)];
  }, b);

  await test("G1-R4-07", "„Schnitt“ steht nicht direkt an einem Endkreis (390 × 844, mit Messpunkten, Zugabe 60 min)", async b => {
    const p = await neu(b, 390, 844); await start(p); await f1(p); await messblatt(p, false); await f2(p); await feld(p, "#z-tEnd", "60");
    const d = await p.evaluate(() => { const s = document.getElementById("diagramm"); const t = [...s.querySelectorAll("text")].find(x => /^Schnitt$/.test(x.textContent)); if (!t) return -1; const r = t.getBBox(); let m = 99; for (const c of s.querySelectorAll("circle[r='4.5']")) { const cx = +c.getAttribute("cx"), cy = +c.getAttribute("cy"); const dx = Math.max(r.x - cx, 0, cx - r.x - r.width), dy = Math.max(r.y - cy, 0, cy - r.y - r.height); m = Math.min(m, Math.hypot(dx, dy)); } return m; });
    return [d >= 8, "Abstand zum nächsten Endkreis " + (typeof d === "number" ? d.toFixed(1) : d) + " px"];
  }, b);

  await test("G1-R4-08", "Angeheftet bleibt die Höhe beim Schieben gleich (360 × 640, 5 bis 180 min)", async b => {
    const p = await neu(b, 360, 640); await start(p); await f1(p);
    const hs = new Set();
    for (const tz of ["5", "8", "10", "20", "40", "56", "60", "90", "120", "180"]) { await feld(p, "#z-tEnd", tz); await warte(40); hs.add(await p.evaluate(() => document.documentElement.classList.contains("anheften") ? Math.round(document.getElementById("diagramm-halter").getBoundingClientRect().height) : -1)); }
    return [hs.size === 1 && !hs.has(-1), [...hs].join(", ")];
  }, b);

  await test("G1-R4-09", "Zweiter Tipp an derselben Stelle 600 ms nach „Vorhersage festhalten“ löst „Zurück“ nicht aus", async b => {
    const p = await neu(b, 390, 844); await start(p); await p.fill("#frage-zahl", "50");
    await p.evaluate(() => new Promise(r => { const k = document.getElementById("knopf-fest").getBoundingClientRect(), x = k.x + k.width / 2, y = k.y + k.height / 2;
      document.getElementById("knopf-fest").dispatchEvent(new MouseEvent("click", { bubbles: true, detail: 1, clientX: x, clientY: y }));
      setTimeout(() => { const z = document.getElementById("knopf-zurueck"); if (z) z.dispatchEvent(new MouseEvent("click", { bubbles: true, detail: 1, clientX: x, clientY: y })); r(); }, 600); }));
    await warte(100); const z = await zustand(p);
    return [z.aktuell === "f1" && z.antworten.f1.fest, "aktuell " + z.aktuell];
  }, b);

  await test("G1-R4-10", "Nach „Diagramm oben anheften“ liegt der Knopf nicht unter dem Diagramm", async b => {
    const p = await neu(b, 390, 844); await start(p); await f1(p);
    await p.click("#knopf-anheften"); await warte(80); await p.evaluate(() => scrollBy(0, 300)); await warte(80);
    await p.click("#knopf-anheften"); await warte(200);
    const r = await p.evaluate(() => [document.getElementById("diagramm-halter").getBoundingClientRect().bottom, document.getElementById("knopf-anheften").getBoundingClientRect().top, document.documentElement.classList.contains("anheften")]);
    return [r[2] && r[1] >= r[0] - 1, "Diagramm unten " + Math.round(r[0]) + ", Knopf oben " + Math.round(r[1])];
  }, b);

  await test("G1-R4-12", "„ohne Vorhersage aufdecken“ zeigt die Auflösung sofort", async b => {
    const p = await neu(b); await start(p); await p.click("#knopf-ohne"); await warte(60); await p.click("#rueck-ja"); await warte(80);
    return [await p.$("#aufl-leiste") !== null, "Auflösung offen " + (await p.$("#aufl-leiste") !== null)];
  }, b);


  await test("G3-R4-02, G3-R4-07", "Wärmestrom: Teilflächen nach dem Vorzeichen beschriftet (400 ml, kA Tasse 1 110 %, 180 min); negativer Gesamtwert als „weniger“", async b => {
    const p = await neu(b); await start(p); await f1(p); await vt(p); await p.click('[data-ansicht="waermestrom"]'); await warte(60);
    await feld(p, "#z-VK", "400"); await feld(p, "#z-kA1", "110"); await feld(p, "#z-tEnd", "180");
    const ft = await txt(p, "#flaechen-text"), r = await p.evaluate(() => window.KAFFEE.ergebnis());
    const ok1 = r.flaecheVor < 0 && /vor dem Schnitt der Wärmeströme: Tasse 2 gibt weniger ab/.test(ft) && /nach dem Schnitt der Wärmeströme: Tasse 2 gibt mehr ab/.test(ft);
    await feld(p, "#z-VK", "200"); await feld(p, "#z-kA1", "105"); await feld(p, "#z-thM", "60"); await feld(p, "#z-tEnd", "60");
    const ft2 = await txt(p, "#flaechen-text"), r2 = await p.evaluate(() => window.KAFFEE.ergebnis());
    const ok2 = r2.Q2 - r2.Q1 >= 0 || (/weniger Wärme ab als Tasse 1/.test(ft2) && !/−/.test(ft2.split("Tasse 2 gibt")[1] || ""));
    return [ok1 && ok2, ft.slice(0, 140) + " | " + ft2.slice(0, 90)];
  }, b);

  await test("G3-R4-03, G3-R4-10", "Lesehilfe nennt den Becher bei „geteilt durch m c_p“ und bei der Steigung; Code-Reiter nennt den Ersatzwert nicht „Messwert“", async b => {
    const p = await neu(b); await start(p); await f1(p); await p.click("#tab-modell"); await p.evaluate(() => { for (const d of document.querySelectorAll("#panel-modell details")) d.open = true; });
    const m = await txt(p, "#panel-modell"); await p.click("#tab-code"); const c = await txt(p, "#panel-code");
    return [/des Gemischs \(mit Becher zuzüglich/.test(m) && /des schwarzen Kaffees \(mit Becher zuzüglich/.test(m) && /gleichwertigen Wert nach 10 min \(keine Messung\)/.test(c), ""];
  }, b);

  await test("G3-R4-08, G3-R4-09", "Meldungen zur kA-Quelle: „Bereich des Feldes“ statt „Messbereich“; „Messwert … wieder verwenden“", async b => {
    const p = await neu(b); await start(p); await f1(p); await vt(p);
    await feld(p, "#z-kA", "0,25"); await p.check('input[name="kaq"][value="messung"]'); await warte(80);
    const k = await txt(p, "#knopf-eigene-messung");
    const q = await neu(b); await start(q); await f1(q); await vt(q);
    await feld(q, "#z-VK", "100"); await feld(q, "#z-thK0", "60"); await feld(q, "#z-thU", "10"); await feld(q, "#z-kA", "1");
    await q.click('input[name="kaq"][value="messung"]'); await warte(80); const m = await txt(q, "#kaq-meldung");
    return [/^Messwert 67,0 °C wieder verwenden/.test(k.trim()) && /Bereichs des Feldes/.test(m), JSON.stringify(k) + " | " + m.slice(60, 160)];
  }, b);


  await test("G5-R4-01, G5-R4-02", "Keine zwei Beschriftungen im Diagramm überdecken sich; Verbindungslinie zu „Schnitt“ nicht an den Kurven entlang (320 bis 390 px, mit Trinklinie)", async b => {
    let ueber = 0, linie = 0, n = 0; const bsp = [];
    for (const [w, h] of [[320, 640], [360, 640], [375, 667], [390, 844]]) for (const lang of ["de", "en"]) {
      const p = await neu(b, w, h, lang === "en" ? "?lang=en" : ""); await start(p); await f1(p); await vt(p);
      for (const trink of [false, true]) {
        if (trink) { await p.check("#s-trink"); await warte(40); }
        for (const tz of ["20", "40", "56", "60", "75", "90", "120", "180"]) {
          await feld(p, "#z-tEnd", tz); n++;
          const r = await p.evaluate(() => { const s = document.getElementById("diagramm"); const ts = [...s.querySelectorAll("text")].filter(x => x.textContent.trim() && !/^[−\d.,]+$/.test(x.textContent.trim())).map(x => [x.textContent, x.getBoundingClientRect()]); let u = []; for (let i = 0; i < ts.length; i++) for (let j = i + 1; j < ts.length; j++) { const a = ts[i][1], c = ts[j][1]; const ox = Math.min(a.right, c.right) - Math.max(a.left, c.left), oy = Math.min(a.bottom, c.bottom) - Math.max(a.top, c.top); if (ox > 2 && oy > 2) u.push(ts[i][0] + " × " + ts[j][0]); } const l = [...s.querySelectorAll("line[stroke='#142337']")].length; return [u, l]; });
          if (r[0].length) { ueber++; if (bsp.length < 3) bsp.push(w + lang + " " + tz + ": " + r[0][0]); }
        }
      }
      await p.context().close();
    }
    return [ueber === 0, ueber + " von " + n + " Zuständen mit Überdeckung " + bsp.join("; ")];
  }, b);

  await test("G5-R4-04", "Abgelehnter Wechsel der kA-Quelle: Meldung in der bleibenden Ansage und am fieldset verknüpft", async b => {
    const q = await neu(b); await start(q); await f1(q); await vt(q);
    await feld(q, "#z-VK", "100"); await feld(q, "#z-thK0", "60"); await feld(q, "#z-thU", "10"); await feld(q, "#z-kA", "1");
    await q.click('input[name="kaq"][value="messung"]'); await warte(400);
    const r = await q.evaluate(() => [document.getElementById("ansage").textContent, document.querySelector("fieldset[aria-describedby='kaq-meldung']") !== null]);
    return [/Nicht umgestellt/.test(r[0]) && r[1], r[0].slice(0, 60)];
  }, b);

  await test("G5-R4-05", "Messblatt Raum- und Milchtemperatur: Fehler mit Feldname, aria-describedby und rotem Rand", async b => {
    const p = await neu(b); await feld(p, "#mess-u", "21,555");
    const r = await p.evaluate(() => { const u = document.getElementById("mess-u"); return [u.getAttribute("aria-describedby"), document.getElementById("mess-fehler").textContent, getComputedStyle(u).borderTopColor]; });
    return [r[0] === "mess-fehler" && /Raumtemperatur/.test(r[1]) && r[2] === "rgb(182, 52, 52)", r.join(" | ")];
  }, b);

  await test("G5-R4-06", "Schrift zur Laufzeit vergrößert: überlaufende Tabellen bekommen Tastaturzugang und Namen", async b => {
    const p = await neu(b, 360, 640); await start(p); await f1(p);
    await p.evaluate(() => { document.querySelector(".wertetabelle").open = true; document.documentElement.style.fontSize = "200%"; }); await warte(300);
    const r = await p.evaluate(() => [...document.querySelectorAll(".tabelle-wrap")].filter(e => e.offsetParent && e.scrollWidth > e.clientWidth + 1).map(e => e.getAttribute("tabindex") === "0" && !!(e.getAttribute("aria-label") || e.getAttribute("aria-labelledby"))));
    return [r.length > 0 && r.every(Boolean), r.join(",")];
  }, b);

  await b.close();
  const ok = ERG.filter(x => x.ok).length;
  console.log("\nErgebnis: " + ok + " von " + ERG.length + " Prüfungen bestanden.");
  if (!process.env.KAFFEE_ORDNER) fs.writeFileSync(path.join(__dirname, "browsertest_korrektur_ergebnis.txt"), "Korrekturrunde nach X5, " + new Date().toISOString().slice(0, 10) + ", Chromium im Cloud-Container\n" + ERG.map(x => x.zeile).join("\n") + "\n\nErgebnis: " + ok + " von " + ERG.length + " Prüfungen bestanden.\n");
})().catch(e => { console.error(e); process.exit(1); });
