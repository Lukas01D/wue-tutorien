// Schlanke Kaffee-Simulation (Aufträge der TL vom 11.11.2026): Kasten mit den Werten zum angezeigten Zeitpunkt, Diagramm,
// Säulen der an den Raum abgegebenen Wärme, „Abspielen“ und Regler im Stil der Hauptseite. Keine Fragen, keine Aufträge.
// Bausteine mit „// aus oberflaeche.js“ setzt bauen_minimal.py unverändert aus simulation/site/src/oberflaeche.js ein.
// Gegenüber der Hauptseite: Zeit t bis 180 min unabhängig von der Zugabe (Zugabe höchstens t), Tasse 2 kühlt nach der Milch
// weiter ab, dazu Kaffeemenge und Wärmekapazität der Tasse. Bei C_T = 0 und t = t_Z rechnet die Seite genau wie die Hauptseite.
(function () {
  "use strict";
  const SVGNS = "http://www.w3.org/2000/svg";
  const $ = id => document.getElementById(id);
  const KA_BLATT = kABlatt();
  const REGLER = [
    { id: "t", t: "schlank_r_t", einheit: "min", min: 1, max: 180, schritt: 1, stellen: 0, marken: [1, 45, 90, 135, 180] },
    { id: "tZ", t: "r_tZ", einheit: "min", min: 1, max: 180, schritt: 1, stellen: 0, marken: [1, 45, 90, 135, 180] },
    { id: "thM", t: "r_thM", einheit: "°C", min: 2, max: 95, schritt: 0.5, stellen: 1, marken: [2, 25, 50, 75, 95] },
    { id: "VM_ml", t: "r_VM", einheit: "ml", min: 10, max: 200, schritt: 5, stellen: 0, marken: [10, 50, 100, 150, 200] },
    { id: "thK0", t: "r_thK0", einheit: "°C", min: 60, max: 95, schritt: 0.5, stellen: 1, marken: [60, 70, 80, 95] },
    { id: "VK_ml", t: "schlank_r_VK", einheit: "ml", min: 50, max: 400, schritt: 10, stellen: 0, marken: [100, 200, 300, 400] },
    { id: "thU", t: "r_thU", einheit: "°C", min: 10, max: 30, schritt: 0.5, stellen: 1, marken: [10, 20, 30] },
    { id: "kA", t: "r_kA", einheit: "W/K", min: 0.05, max: 0.8, schritt: 0.005, stellen: 4, marken: [0.05, 0.4, 0.8] },
    { id: "CT", t: "schlank_r_CT", einheit: "J/K", min: 0, max: 600, schritt: 5, stellen: 0, marken: [0, 150, 300, 450, 600] }
  ];
  const blatt = () => ({ t: STANDARD.tZ, tZ: STANDARD.tZ, thM: STANDARD.thM, VM_ml: STANDARD.VM_ml, thK0: STANDARD.thK0, VK_ml: STANDARD.VK_ml,
                         thU: STANDARD.thU, kA: KA_BLATT, CT: 0 });
  // Zustand in der Form, die die übernommenen Bausteine erwarten (Säulen mit Zahlen)
  const S = { z: 2, e: blatt(), warumFest: true };
  let L = new URLSearchParams(location.search).get("lang") === "en" ? "en" : "de";
  let tJetzt = S.e.t;      // angezeigter Zeitpunkt in min (0 bis t); beim Abspielen läuft er von 0 bis t
  let lauf = 0;            // laufende Wiedergabe (requestAnimationFrame), 0 = keine

  //@@BAUSTEINE@@

  // ------------------------------------------------------------ Rechnung
  // Rechenkern der Hauptseite (rechne aus modell.js) für Stoffwerte und kA; dazu die Tasse mit Wärmekapazität C_T, immer so
  // warm wie ihr Inhalt (wie kaffee_modell.zwei_tassen), und die Abkühlung von Tasse 2 nach der Zugabe. Zeiten in min.
  function modell(e) {
    const p = Object.assign({}, P, { V_K: e.VK_ml * 1e-6, V_M: e.VM_ml * 1e-6, th_K0: e.thK0, th_M: e.thM, th_U: e.thU, t_end: e.tZ * 60.0 });
    p.th_mess = e.thU + (e.thK0 - e.thU) * Math.exp(-e.kA * p.t_mess / (p.rho_K * p.V_K * p.cp_K));   // gleichwertiger Messwert für dieses kA
    const r = rechne(p), u = e.thU;
    const CK = r.C_K + e.CT, CG = r.C_G + e.CT, aK = r.kA / CK, aG = r.kA / CG;
    const th10 = (CK * e.thK0 + r.C_M * e.thM) / CG;
    const thK = t => u + (e.thK0 - u) * Math.exp(-aK * t * 60);
    const th2K = thK(e.tZ), th2Z = (CK * th2K + r.C_M * e.thM) / CG;
    const th1 = t => u + (th10 - u) * Math.exp(-aG * t * 60);
    const th2 = t => (t < e.tZ ? thK(t) : u + (th2Z - u) * Math.exp(-aG * (t - e.tZ) * 60));
    const Q1 = t => CG * (th10 - th1(t));
    const Q2 = t => (t < e.tZ ? CK * (e.thK0 - thK(t)) : CK * (e.thK0 - th2K) + CG * (th2Z - th2(t)));
    return { kA: r.kA, CK: CK, CG: CG, th10: th10, th2K: th2K, th2Z: th2Z, thK: thK, th1: th1, th2: th2, Q1: Q1, Q2: Q2 };
  }

  // ------------------------------------------------------------ Regler
  function obergrenze(r) { return r.id === "tZ" ? S.e.t : r.max; }
  function reglerAnzeigen() {
    for (const r of REGLER) {
      const ein = $("rr-" + r.id), max = obergrenze(r), v = S.e[r.id];
      ein.max = max;
      ein.value = v;
      ein.setAttribute("aria-valuetext", zahl(v, r.stellen) + " " + r.einheit);
      const feld = $("rf-" + r.id);
      if (document.activeElement !== feld || feld.getAttribute("aria-invalid") !== "true") feld.value = zahl(v, r.stellen);
      let marken = r.marken.filter(m => m <= max);
      if (r.id === "tZ" && max - marken[marken.length - 1] > (max - r.min) * 0.12) marken.push(max);
      else if (r.id === "tZ" && marken[marken.length - 1] < max) marken[marken.length - 1] = max;
      const sk = $("rs-" + r.id);
      sk.textContent = "";
      if (max > r.min) for (const m of marken) {
        const sp = document.createElement("span");
        sp.textContent = zahl(m, r.id === "kA" ? 2 : 0);
        sp.style.left = (100 * (m - r.min) / (max - r.min)).toFixed(2) + "%";
        sk.appendChild(sp);
      }
      $("rminus-" + r.id).disabled = v <= r.min;
      $("rplus-" + r.id).disabled = v >= max;
    }
  }

  // ------------------------------------------------------------ Diagramm (Aufbau und Zeichen wie zeichne der Hauptseite)
  function diagrammHoehe(W) {
    if (window.innerWidth < 1024) return Math.round(Math.min(360, W * (W < 500 ? 0.82 : 0.68)));
    return Math.round(Math.max(240, Math.min(W * 0.45, window.innerHeight - 390)));
  }
  function zeichne(m) {
    const e = S.e, tE = e.t, svg = $("dia");
    const W = Math.max(260, Math.round(svg.getBoundingClientRect().width || 600));
    const H = diagrammHoehe(W);
    svg.setAttribute("viewBox", "0 0 " + W + " " + H);
    svg.setAttribute("height", H);
    svg.textContent = "";
    const fs = W >= 600 ? 13 : 12, dick = W >= 600 ? 3 : 2.5;
    const xmax = Math.max(60, Math.ceil(tE / 10) * 10);
    const ymax = Math.max(90, Math.ceil((Math.max(e.thK0, m.th10, m.th2Z) + 3) / 10) * 10);
    const ymin = Math.min(10, Math.floor((e.thU - 5) / 10) * 10);
    const Lr = 46, R = 24, Tr = 12, B = 38, P = 12;
    const X = t => Lr + P + (W - Lr - P - R) * t / xmax, Y = v => Tr + (H - Tr - B) * (ymax - v) / (ymax - ymin);
    const fein = xmax <= 90 ? 5 : 10, grob = xmax <= 90 ? 10 : 30;
    for (let t = 0; t <= xmax + 1e-9; t += fein) svg.appendChild(el("line", { x1: X(t), x2: X(t), y1: Y(ymax), y2: Y(ymin), class: t % grob ? "gitter" : "gitter-haupt" }));
    for (let v = ymin; v <= ymax; v += 5) svg.appendChild(el("line", { x1: Lr, x2: X(xmax), y1: Y(v), y2: Y(v), class: v % 10 ? "gitter" : "gitter-haupt" }));
    svg.appendChild(el("line", { x1: Lr, x2: X(xmax), y1: Y(ymin), y2: Y(ymin), class: "achse" }));
    svg.appendChild(el("line", { x1: Lr, x2: Lr, y1: Y(ymin), y2: Y(ymax), class: "achse" }));
    for (let t = 0; t <= xmax; t += grob) svg.appendChild(el("text", { x: X(t), y: Y(ymin) + 15, "text-anchor": "middle", "font-size": fs, class: "ax" }, String(t)));
    for (let v = ymin; v <= ymax; v += 20) svg.appendChild(el("text", { x: Lr - 6, y: Y(v) + 4, "text-anchor": "end", "font-size": fs, class: "ax" }, String(v)));
    svg.appendChild(el("text", { x: (X(0) + X(xmax)) / 2, y: H - 5, "text-anchor": "middle", "font-size": fs, class: "beschr" }, T("dia_zeit")));
    const ym = (Y(ymin) + Y(ymax)) / 2;
    svg.appendChild(el("text", { x: 12, y: ym, "text-anchor": "middle", "font-size": fs, class: "beschr", transform: "rotate(-90 12 " + ym + ")" }, T("dia_temp")));
    svg.appendChild(el("line", { x1: Lr, x2: X(xmax), y1: Y(e.thU), y2: Y(e.thU), class: "raum" }));
    svg.appendChild(el("text", { x: X(xmax) - 2, y: Y(e.thU) - 6, "text-anchor": "end", "font-size": fs, class: "leise-text" }, F("dia_raum", { th: zahl(e.thU, 1) })));
    // Kurven: Tasse 1 bis t; Tasse 2 als schwarzer Kaffee bis zur Zugabe, danach mit Milch bis t
    const linie = (f, von, bis) => { const p = []; for (let i = 0; i <= 160; i++) { const t = von + (bis - von) * i / 160; p.push(X(t).toFixed(1) + "," + Y(f(t)).toFixed(1)); } return p.join(" "); };
    svg.appendChild(el("polyline", { points: linie(m.th1, 0, tE), class: "kurve k1", "stroke-width": dick }));
    svg.appendChild(el("polyline", { points: linie(m.thK, 0, e.tZ), class: "kurve k2 gestrichelt", "stroke-width": dick }));
    if (tE > e.tZ) svg.appendChild(el("polyline", { points: linie(m.th2, e.tZ, tE), class: "kurve k2 gestrichelt", "stroke-width": dick }));
    // Sprung durch die Milch (wie Hauptseite); liegt die Zugabe am Ende, endet die Spitze von Tasse 2 am Rand ihres Endpunkts
    const abf = [[0, e.thK0, m.th10, "k1", 0], [e.tZ, m.th2K, m.th2Z, "k2", e.tZ >= tE ? 6 : 0]].map(([t, o, u, k, l]) => {
      const r = Y(u) >= Y(o) ? 1 : -1, x = X(t), y1 = Y(o), y2 = Y(u) - r * l, lang = r * (y2 - y1);
      return { t: t, x: x, y1: y1, y2: y2, r: r, k: k, sp: Math.min(W >= 600 ? 9 : 7, lang / 2), ok: lang > 2 };
    });
    for (const a of abf) if (a.ok) svg.appendChild(el("line", { x1: a.x, x2: a.x, y1: a.y1, y2: a.y2 - a.r * a.sp, class: "abfall " + a.k, "stroke-width": dick }));
    svg.appendChild(el("circle", { cx: X(tE), cy: Y(m.th1(tE)), r: 4.5, class: "ende k1" }));
    svg.appendChild(el("circle", { cx: X(tE), cy: Y(m.th2(tE)), r: 4.5, class: "ende k2" }));
    for (const a of abf) {
      if (!a.ok) continue;
      const ecken = [[a.x - a.sp * 0.7, a.y2 - a.r * a.sp], [a.x + a.sp * 0.7, a.y2 - a.r * a.sp], [a.x, a.y2]];
      svg.appendChild(el("polygon", { points: ecken.map(q => q[0].toFixed(1) + "," + q[1].toFixed(1)).join(" "), class: "pfeil " + a.k }));
      if (a.r * (a.y2 - a.y1) > 2.2 * fs) {
        const yt = a.t === 0 || a.r < 0 ? (a.y1 + a.y2) / 2 + fs * 0.35 : a.y1 + fs * 1.1;
        imBild(svg.appendChild(el("text", { x: a.x + 8, y: yt, "font-size": fs, class: "kbeschr " + a.k + "-text" }, T("dia_milch"))), Lr + 2, W - 4);
      }
    }
    // Direktbeschriftung wie Hauptseite: Tasse 2 im ersten, Tasse 1 im zweiten Zeitfenster vor der Zugabe
    const tZs = e.tZ * 60, k1 = s => m.th1(s / 60), k2 = s => m.thK(s / 60);
    const abstand = s => Math.abs(k1(s) - k2(s));
    const Xinv = x => (x - Lr - P) / (W - Lr - P - R) * xmax * 60;
    const beste = (von, bis) => { let tb = tZs * von, ab = -1; for (let i = 0; i <= 24; i++) { const s = tZs * (von + (bis - von) * i / 24); if (abstand(s) > ab) { ab = abstand(s); tb = s; } } return tb; };
    for (const [n, von, bis] of [[2, 0.08, 0.45], [1, 0.5, 0.92]]) {
      const k = n === 1 ? k1 : k2, anders = n === 1 ? k2 : k1;
      const txt = n === 1 ? T("dia_t1") : F("dia_t2", { t: e.tZ }), w = txt.length * fs * 0.56;
      const s = beste(von, bis), oben = k(s) >= anders(s);
      let x, y;
      if (oben) { x = Math.max(Lr + 4, Math.min(X(s / 60), W - R - w, n === 1 ? X(e.tZ) - 8 - w : W)); y = Y(k(Math.max(0, Xinv(x)))) - 10; }
      else { x = Math.min(W - R, n === 1 ? X(e.tZ) - 12 : W, Math.max(X(s / 60), Lr + w + 4)); y = Y(k(Math.min(tZs, Xinv(x)))) + 22; }
      imBild(svg.appendChild(el("text", { x: x, y: y, "text-anchor": oben ? "start" : "end", "font-size": fs, class: "kbeschr " + (n === 1 ? "k1-text" : "k2-text") }, txt)), Lr + 2, W - 4);
    }
    // angezeigter Zeitpunkt beim Abspielen: Teil danach verdeckt, Linie und Punkte bei tJetzt
    if (tJetzt < tE - 1e-9) {
      const x = X(tJetzt);
      svg.appendChild(el("rect", { x: x + 1, y: Y(ymax) - 2, width: Math.max(0, X(xmax) + R - x - 1), height: Y(ymin) - Y(ymax) + 2, class: "zukunft" }));
      svg.appendChild(el("line", { x1: x, x2: x, y1: Y(ymin), y2: Y(ymax), class: "jetzt" }));
      svg.appendChild(el("circle", { cx: x, cy: Y(m.th1(tJetzt)), r: 5, class: "punkt k1" }));
      svg.appendChild(el("circle", { cx: x, cy: Y(m.th2(tJetzt)), r: 5, class: "punkt k2" }));
    }
    $("dia-beschreibung").textContent = F("schlank_dia_beschreibung", { a: zahl(e.thK0, 1), a1: zahl(m.th10, 1), tz: e.tZ, b2: zahl(m.th2K, 1), m2: zahl(m.th2Z, 1),
      t: tE, e1: zahl(m.th1(tE), 1), e2: zahl(m.th2(tE), 1), u: zahl(e.thU, 1),
      v1: T(m.th10 > e.thK0 ? "dia_hoch" : "dia_runter"), v2: T(m.th2Z > m.th2K ? "dia_hoch" : "dia_runter") });
  }

  // ------------------------------------------------------------ Kasten, Säulen, Ansage
  const zeitText = t => zahl(t, Math.abs(t - Math.round(t)) < 1e-9 ? 0 : 1);
  function kasten(m) {
    const t = tJetzt, d1 = m.th1(t), d2 = m.th2(t);
    $("kern-zeit").textContent = F("kern_nach", { t: zeitText(t) });
    $("w1").textContent = zahl(d1, 2) + " °C";
    $("w2").textContent = zahl(d2, 2) + " °C";
    $("wd").textContent = zahl(d1 - d2, 2) + " K";
  }
  function saeulenZeigen(m) {
    saeulen({ Q1: m.Q1(tJetzt), Q2: m.Q2(tJetzt), Q1max: m.Q1(S.e.t), Q2max: m.Q2(S.e.t) });
    $("saeulen-titel").innerHTML = F("schlank_saeulen_t", { t: zeitText(tJetzt) });
  }
  let ansageTimer = 0;
  function ansage(text) {
    window.clearTimeout(ansageTimer);
    $("ansage").textContent = "";
    const m = modell(S.e), t = S.e.t;
    const s = text || F("schlank_status", { t: t, th1: zahl(m.th1(t), 2), th2: zahl(m.th2(t), 2), dT: zahl(m.th1(t) - m.th2(t), 2) });
    ansageTimer = window.setTimeout(() => { $("ansage").textContent = s; }, 60);
  }

  // ------------------------------------------------------------ Abspielen
  function abspielenBauen() {
    $("abspielen").addEventListener("click", () => {
      if (lauf) { anhalten(); return; }
      if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) { tJetzt = S.e.t; zeigen(); return; }
      const tE = S.e.t, t0 = tJetzt >= tE - 1e-9 ? 0 : tJetzt, dauer = (4000 + 50 * tE) * (tE - t0) / tE, start = performance.now();
      tJetzt = t0;
      lauf = 1;
      $("abspielen").textContent = T("schlank_anhalten");
      const schritt = jetzt => {
        if (!lauf) return;
        tJetzt = t0 + (tE - t0) * Math.min(1, (jetzt - start) / Math.max(dauer, 1));
        zeigen();
        if (tJetzt < tE) lauf = requestAnimationFrame(schritt); else anhalten();
      };
      lauf = requestAnimationFrame(schritt);
    });
  }
  function anhalten() {
    if (lauf) cancelAnimationFrame(lauf);
    lauf = 0;
    $("abspielen").textContent = T("schlank_abspielen");
  }

  // ------------------------------------------------------------ Ablauf
  function texteSetzen() {
    document.documentElement.lang = L;
    document.title = T("titel_seite");
    document.querySelectorAll("[data-t]").forEach(x => { x.innerHTML = T(x.dataset.t); });
    $("sprache").setAttribute("aria-label", T("sprache_knopf_aria"));
    for (const r of REGLER) reglerTexte(r);
    $("abspielen").textContent = T(lauf ? "schlank_anhalten" : "schlank_abspielen");
    $("fuss-text").textContent = F("fuss", { stand: BAU.stand, version: BAU.version });
  }
  function zeigen() {
    const m = modell(S.e);
    zeichne(m);
    kasten(m);
    saeulenZeigen(m);
  }
  function aktualisiere() {                // nach jeder Änderung eines Reglers (von setze aufgerufen)
    anhalten();
    if (S.e.tZ > S.e.t) S.e.tZ = S.e.t;    // Zugabe höchstens bis zur Zeit t
    tJetzt = S.e.t;
    reglerAnzeigen();
    zeigen();
  }
  function alles() { texteSetzen(); aktualisiere(); }

  reglerBauen();
  abspielenBauen();
  $("sprache").addEventListener("click", () => { L = L === "de" ? "en" : "de"; alles(); });
  $("knopf-blatt").addEventListener("click", () => { S.e = blatt(); aktualisiere(); ansage(T("status_blatt")); });
  let warten = 0;
  window.addEventListener("resize", () => { cancelAnimationFrame(warten); warten = requestAnimationFrame(zeigen); });
  alles();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(zeigen);
})();
