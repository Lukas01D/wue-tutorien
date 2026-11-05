// ERWEITERUNG-ANFANG: Erweiterungen nach KONZEPT.md Fassung 2, Abschnitt 8.2 (M2, M3, M4, M8, M9, M10), ohne Bezug zur Oberfläche.
// Setzt auf dem unveränderten Block MODELL auf (P, K, rechne, zweiTassen, berechne). Python-Referenz: simulation/modell/kaffee_erweitert.py.
// Einstellungen e: VK_ml, VM_ml, thK0, thM, thU (°C), tEnd_min (Zugabe, min), becher, mB_g, milch2Raum, kA1Faktor,
// kAQuelle ("fest" oder "messung"), kA (W/K bei "fest"), thMess (°C bei "messung").
const ERW = (() => {
  const VOREINSTELLUNGEN = [
    { id: "keramik", faktor: 1.00, art: "belegt" },
    { id: "keramik_deckel", faktor: 0.56, art: "belegt" },
    { id: "glas", faktor: 1.00, art: "richtwert" },
    { id: "pappe", faktor: 1.00, art: "richtwert" },
    { id: "edelstahl", faktor: 0.90, art: "richtwert" },
    { id: "thermo_offen", faktor: 0.44, art: "richtwert" }
  ];
  const KA_AUFGABE = rechne(P).kA;                      // Teil c: 80 auf 67 °C in 10 min, 200 ml, ohne Becher

  function kapazitaeten(e) {
    const C_K = P.rho_K * e.VK_ml * 1e-6 * P.cp_K, C_M = P.rho_M * e.VM_ml * 1e-6 * P.cp_M;
    const C_B = e.becher ? e.mB_g / 1000 * P.c_B : 0.0;
    return { C_K: C_K, C_M: C_M, C_B: C_B, C_KB: C_K + C_B, C_GB: C_K + C_M + C_B };
  }
  // M8: gleichwertiger Messwert nach 10 min, aus dem der Block MODELL genau dieses kA rechnet (nie als Messung angezeigt)
  function messwertFuer(kA, e) {
    return e.thU + (e.thK0 - e.thU) * Math.exp(-kA * 600 / kapazitaeten(e).C_KB);
  }
  // Gültigkeit wie im geprüften Werkzeug (D116); bei kA festhalten zusätzlich kA > 0. Leer heißt gültig.
  function fehler(e) {
    if (!(e.thK0 > e.thU)) return "anfang_ueber_raum";
    if (e.kAQuelle === "fest") return e.kA > 0 ? "" : "kA_positiv";
    if (!(e.thMess > e.thU && e.thMess < e.thK0)) return "messung_zwischen";
    return "";
  }
  function modellEinstellung(e) {
    return e.kAQuelle === "fest" ? Object.assign({}, e, { thMess: messwertFuer(e.kA, e) }) : e;
  }
  function auswerten(e) {
    const em = modellEinstellung(e), m = berechne(em), m3 = berechne(Object.assign({}, em, { milch2Raum: true }));
    const c = kapazitaeten(e), T_U = e.thU + K, T_K0 = e.thK0 + K, kA = m.kA, f1 = e.kA1Faktor;
    const a1 = f1 * kA / c.C_GB, a2 = kA / c.C_KB, thM2 = e.milch2Raum ? e.thU : e.thM;
    const T1 = t => T_U + (m.T1_0 - T_U) * Math.exp(-a1 * t), T2K = t => T_U + (T_K0 - T_U) * Math.exp(-a2 * t);
    const dQ = t => c.C_KB * (T_K0 - T2K(t)) - c.C_GB * (m.T1_0 - T1(t));       // Q2(t) - Q1(t) in J
    let t_q = Infinity;                                                          // gleiche Wärmeströme
    const zq = (T_K0 - T_U) / (f1 * (m.T1_0 - T_U));
    if (a2 !== a1 && zq > 0) { const t = Math.log(zq) / (a2 - a1); if (t > 0) t_q = t; }
    const tz = e.tEnd_min * 60;
    const vor = t_q < tz ? dQ(t_q) : dQ(tz), nach = t_q < tz ? dQ(tz) - dQ(t_q) : 0;
    const milch = c.C_M * (e.thM - thM2);
    return {
      kA: kA, thMessModell: em.thMess, th10: m.T1_0 - K, th1: m.th1, th2: m.th2, th2K: m.T2_K - K, th2Raum: m3.th2,
      dT: m.dT, Q1: m.Q1 / 1e3, Q2: m.Q2 / 1e3, milch: milch / 1e3,
      energieRest: (c.C_GB * m.dT - (m.Q2 - m.Q1) - milch) / 1e3,
      tSchnitt: m.t_schnitt / 60, kaffeeDanachKuehler: m.kaffee_danach_kuehler, tWaermestrom: t_q / 60,
      flaecheVor: vor / 1e3, flaecheNach: nach / 1e3,
      qdot1: t_min => f1 * kA * (T1(t_min * 60) - T_U), qdot2: t_min => kA * (T2K(t_min * 60) - T_U),
      kurve1: t_min => m.kurve1(t_min * 60) - K, kurve2: t_min => m.kurve2(t_min * 60) - K,
      schwarz30: m.kurve2(1800) - K, tauMin: c.C_KB / kA / 60,
      C_K: c.C_K, C_M: c.C_M, C_B: c.C_B, C_KB: c.C_KB, C_GB: c.C_GB
    };
  }
  // M4 (kann): beide Tassen nach der Zugabe bis tV, Tasse 1 mit f1 kA
  function nachZugabe(e, tV_min) {
    const r = auswerten(e), c = kapazitaeten(e), dt = (tV_min - e.tEnd_min) * 60;
    const th1 = e.thU + (r.th1 - e.thU) * Math.exp(-e.kA1Faktor * r.kA * dt / c.C_GB);
    const th2 = e.thU + (r.th2 - e.thU) * Math.exp(-r.kA * dt / c.C_GB);
    return { th1: th1, th2: th2, dT: th1 - th2 };
  }
  // M9 (kann): Becher beim Eingießen auf Raumtemperatur, sofortiger Ausgleich bei t = 0; nur mit kA festhalten und Becher an
  function becherKalt(e) {
    const c = kapazitaeten(e), kA = e.kA, t = e.tEnd_min * 60;
    const th1_0 = (c.C_K * e.thK0 + c.C_M * e.thM + c.C_B * e.thU) / c.C_GB;
    const thK_0 = (c.C_K * e.thK0 + c.C_B * e.thU) / c.C_KB;
    const th1 = e.thU + (th1_0 - e.thU) * Math.exp(-e.kA1Faktor * kA * t / c.C_GB);
    const thK = e.thU + (thK_0 - e.thU) * Math.exp(-kA * t / c.C_KB);
    const th2 = (c.C_KB * thK + c.C_M * (e.milch2Raum ? e.thU : e.thM)) / c.C_GB;
    return { th1_0: th1_0, thK_0: thK_0, th1: th1, th2: th2, dT: th1 - th2 };
  }
  // M10 (kann): Zeit in min bis zur Trinktemperatur thT
  function trinkzeit(e, thT) {
    const r = auswerten(e);
    const zeit = (th0, C, f) => th0 <= thT ? 0 : (thT <= e.thU ? Infinity : C / (f * r.kA) * Math.log((th0 - e.thU) / (thT - e.thU)) / 60);
    return { tasse1: zeit(r.th10, r.C_GB, e.kA1Faktor), schwarz: zeit(e.thK0, r.C_KB, 1) };
  }
  // M2: Ausgleichsgerade durch den Ursprung und mit freiem Achsenabschnitt; punkte = [[t_min, theta], ...] ohne Startpunkt
  function ausgleich(punkte, th0, thU, C_KB) {
    const xs = punkte.map(p => p[0] * 60), ys = punkte.map(p => Math.log((p[1] - thU) / (th0 - thU)));
    let sxy = 0, sxx = 0; for (let i = 0; i < xs.length; i++) { sxy += xs[i] * ys[i]; sxx += xs[i] * xs[i]; }
    const b0 = sxy / sxx, X = [0].concat(xs), Y = [0].concat(ys), n = X.length;
    const mx = X.reduce((a, v) => a + v, 0) / n, my = Y.reduce((a, v) => a + v, 0) / n;
    let s1 = 0, s2 = 0; for (let i = 0; i < n; i++) { s1 += (X[i] - mx) * (Y[i] - my); s2 += (X[i] - mx) ** 2; }
    const b1 = s1 / s2;
    return { kA_ursprung: -C_KB * b0, kA_frei: -C_KB * b1, achsenabschnitt: my - b1 * mx, n: punkte.length };
  }
  // Konzept 8.1: größter Unterschied über t_Z bei gleichem kA (analytisch über den Schnitt)
  function groessterUnterschied(e) {
    const c = kapazitaeten(e), r = auswerten(Object.assign({}, e, { tEnd_min: 1 }));
    const q = (e.thK0 - e.thU) / (r.th10 - e.thU), thx = e.thU + (e.thK0 - e.thU) * Math.pow(q, -c.C_GB / c.C_M);
    return { dT_max: c.C_M * (thx - e.thM) / c.C_GB, th_x: thx, t_min: Math.log(q) / (r.kA / c.C_KB - r.kA / c.C_GB) / 60 };
  }
  return { VOREINSTELLUNGEN, KA_AUFGABE, kapazitaeten, messwertFuer, fehler, modellEinstellung, auswerten, nachZugabe,
           becherKalt, trinkzeit, ausgleich, groessterUnterschied };
})();
// ERWEITERUNG-ENDE
