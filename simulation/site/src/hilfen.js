// HILFEN-ANFANG: Zahlen lesen und schreiben, Kurslink (ZUSTAENDE.md, Abschnitt 5). Ohne Bezug zur Oberfläche, in Node testbar.
const HILFEN = (() => {
  // Eine Zahl nur, wenn der ganze Text eine Zahl ist (Komma oder Punkt), sonst NaN; aus dem geprüften Werkzeug (Befund Simulation 5),
  // ergänzt: mehr als ein Trennzeichen gilt als Tausendertrennung und wird abgelehnt ("tausender").
  function zahlLesen(text) {
    const t = String(text).trim().replace("−", "-");
    if ((t.match(/[.,]/g) || []).length > 1) return { wert: NaN, grund: "tausender" };
    const u = t.replace(",", ".");
    return /^[+-]?\d+(\.\d+)?$/.test(u) ? { wert: Number(u), grund: "" } : { wert: NaN, grund: t === "" ? "leer" : "keine_zahl" };
  }
  function zahlText(x, stellen, sprache) {
    if (!isFinite(x)) return "";
    let s = (Math.abs(x) < 0.5 * Math.pow(10, -stellen) ? 0 : x).toFixed(stellen);
    if (s.charAt(0) === "-") s = "−" + s.slice(1);
    return sprache === "de" ? s.replace(".", ",") : s;
  }
  // Kurslink, Format Version 1: #kurs1=u:21.5;m:6;d:0;b:1.2;b1:...;b2:...;b3:...  (acht Werte je Becher)
  const ZEILEN = 8, MAX_LAENGE = 400;
  function kurslinkBauen(kurs) {
    const z = v => (v === null || v === undefined || !isFinite(v)) ? "" : String(Math.round(v * 100) / 100);
    const becher = ["1", "2"].concat(kurs.b3 ? ["3"] : []);
    const teile = ["u:" + z(kurs.u), "m:" + z(kurs.m), "d:" + (kurs.d ? 1 : 0), "b:" + becher.join(".")];
    for (const b of becher) teile.push("b" + b + ":" + kurs.werte["b" + b].map(z).join(","));
    return "kurs1=" + teile.join(";");
  }
  function kurslinkLesen(hash) {
    const h = String(hash || "").replace(/^#/, "");
    if (!h) return { art: "leer" };
    if (!/^kurs1=/.test(h)) return { art: "fremd" };
    if (h.length > MAX_LAENGE) return { art: "defekt", grund: "zu_lang" };
    let roh;
    try { roh = decodeURIComponent(h.slice(6)); } catch (e) { return { art: "defekt", grund: "kodierung" }; }
    const felder = {};
    for (const teil of roh.split(";")) {
      const i = teil.indexOf(":");
      if (i < 1) return { art: "defekt", grund: "feld" };
      const k = teil.slice(0, i), v = teil.slice(i + 1);
      if (!/^(u|m|d|b|b1|b2|b3)$/.test(k) || k in felder) return { art: "defekt", grund: "feld:" + k };
      felder[k] = v;
    }
    const zahl = (v, lo, hi, name) => {
      if (v === "" || v === undefined) return { ok: true, wert: null };
      if (!/^-?\d{1,3}(\.\d{1,2})?$/.test(v)) return { ok: false, grund: name };
      const x = Number(v); return (x >= lo && x <= hi) ? { ok: true, wert: x } : { ok: false, grund: name };
    };
    const u = zahl(felder.u, 5, 40, "u"), m = zahl(felder.m, 0, 70, "m");
    if (!u.ok) return { art: "defekt", grund: "u" };
    if (!m.ok) return { art: "defekt", grund: "m" };
    if (!(felder.d === "0" || felder.d === "1")) return { art: "defekt", grund: "d" };
    const becher = (felder.b || "").split(".");
    if (!becher.length || becher.some(b => !/^[123]$/.test(b)) || becher.indexOf("2") < 0 || new Set(becher).size !== becher.length)
      return { art: "defekt", grund: "b" };
    const werte = { b1: Array(ZEILEN).fill(null), b2: Array(ZEILEN).fill(null), b3: Array(ZEILEN).fill(null) };
    for (const b of becher) {
      const liste = (felder["b" + b] || "").split(",");
      if (liste.length !== ZEILEN) return { art: "defekt", grund: "b" + b + ":anzahl" };
      for (let i = 0; i < ZEILEN; i++) {
        const w = zahl(liste[i], 0, 100, "b" + b + ":" + (i + 1));
        if (!w.ok) return { art: "defekt", grund: w.grund };
        if (b === "1" && i === 7 && w.wert !== null) return { art: "defekt", grund: "b1:8" };
        werte["b" + b][i] = w.wert;
      }
    }
    for (const k of ["b1", "b2", "b3"]) if (k in felder && becher.indexOf(k.slice(1)) < 0) return { art: "defekt", grund: k };
    return { art: "ok", kurs: { v: 1, u: u.wert, m: m.wert, d: felder.d === "1", b3: becher.indexOf("3") >= 0, werte: werte } };
  }
  return { zahlLesen, zahlText, kurslinkBauen, kurslinkLesen, ZEILEN };
})();
// HILFEN-ENDE
