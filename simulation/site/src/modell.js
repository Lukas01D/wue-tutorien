// MODELL-ANFANG: gleiche Gleichungen und Standardwerte wie kaffee_modell.py (P, rechne); unverändert aus dem geprüften Block der Fassung 2
const P = { V_K: 200e-6, rho_K: 1000.0, cp_K: 4180.0, V_M: 30e-6, rho_M: 1030.0, cp_M: 3940.0, th_K0: 80.0, th_M: 5.0,
            th_U: 20.0, t_end: 60 * 60.0, t_mess: 10 * 60.0, th_mess: 67.0, th_Mh: 60.0, m_B: 0.300, c_B: 850.0 };
const K = 273.15;

function rechne(p) {
  const r = Object.assign({}, p);
  r.m_K = p.rho_K * p.V_K;
  r.m_M = p.rho_M * p.V_M;
  r.C_K = r.m_K * p.cp_K;
  r.C_M = r.m_M * p.cp_M;
  r.C_G = r.C_K + r.C_M;
  const T_K0 = p.th_K0 + K, T_M = p.th_M + K, T_U = p.th_U + K;
  Object.assign(r, { T_K0: T_K0, T_M: T_M, T_U: T_U, T_mess: p.th_mess + K });
  r.ln_mess = Math.log((r.T_mess - T_U) / (T_K0 - T_U));
  r.kA = -r.C_K / p.t_mess * r.ln_mess;
  r.a_K = r.kA / r.C_K;
  r.a_G = r.kA / r.C_G;
  const mix = TK => (r.C_K * TK + r.C_M * T_M) / r.C_G;
  r.T1_0 = mix(T_K0);
  r.e_G = Math.exp(-r.a_G * p.t_end);
  r.T1 = T_U + (r.T1_0 - T_U) * r.e_G;
  r.e_K = Math.exp(-r.a_K * p.t_end);
  r.T2_K = T_U + (T_K0 - T_U) * r.e_K;
  r.T2 = mix(r.T2_K);
  r.dT = r.T1 - r.T2;
  r.Q1 = r.C_G * (r.T1_0 - r.T1);
  r.Q2 = r.C_K * (T_K0 - r.T2_K);
  const d = r.a_K - r.a_G;
  r.t_schnitt = d > 0 ? Math.log((T_K0 - T_U) / (r.T1_0 - T_U)) / d : Infinity;
  return r;
}
// MODELL-ENDE

// Werte des Blatts Fassung 3 (werte.py; vorläufig bis zur Messung im Januar 2027). Die einzige Stelle für Standardwerte (SE6).
const STANDARD = { thK0: 80.0, thM: 5.0, thU: 20.0, VK_ml: 200, VM_ml: 30, thMess: 72.0, tZ: 60, thMh: 70.0, trink: 60.0 };
// Beispielwerte der Kontrollseite (werte.py, Modell mit vorgewärmter Tasse, gerundet wie auf dem Blatt; berechnet, keine Messung)
const BEISPIEL = { t1: [72.5, 66.1, 60.6, 55.7, 51.4, 47.6, 44.2], t2: [80.0, 72.0, 65.1, 59.1, 53.9, 49.3, 45.4], t2Milch: 41.4 };

// Parameter für rechne() aus den Einstellungen der Seite. kA bleibt beim Ändern von Kaffee- oder Raumtemperatur fest
// (Eigenschaft der Tasse); rechne() bekommt dafür den gleichwertigen Messwert nach 10 min, aus dem es genau dieses kA bestimmt.
function parameter(e) {
  const p = Object.assign({}, P, { V_K: STANDARD.VK_ml * 1e-6, V_M: e.VM_ml * 1e-6, th_K0: e.thK0, th_M: e.thM, th_U: e.thU,
                                   t_end: e.tZ * 60.0 });
  const C_K = p.rho_K * p.V_K * p.cp_K;
  p.th_mess = e.kA === null ? STANDARD.thMess : e.thU + (e.thK0 - e.thU) * Math.exp(-e.kA * p.t_mess / C_K);
  return p;
}

// kA des Blatts (aus 72 °C nach 10 min bei den Werten des Blatts)
function kABlatt() {
  return rechne(parameter({ thK0: STANDARD.thK0, thM: STANDARD.thM, thU: STANDARD.thU, VM_ml: STANDARD.VM_ml, kA: null, tZ: STANDARD.tZ })).kA;
}

function auswerten(e) {
  const p = parameter(e);
  const r = rechne(p);
  return { kA: r.kA, th_mess: p.th_mess, C_K: r.C_K, C_G: r.C_G, a_K: r.a_K, a_G: r.a_G, t_schnitt: r.t_schnitt,
           th10: r.T1_0 - K, th1: r.T1 - K, th2K: r.T2_K - K, th2: r.T2 - K, dT: r.dT, Q1: r.Q1, Q2: r.Q2, thK0: e.thK0, thU: e.thU,
           kurve1: t => p.th_U + (r.T1_0 - r.T_U) * Math.exp(-r.a_G * t),      // Tasse 1, t in s, Ergebnis in °C
           kurve2: t => p.th_U + (r.T_K0 - r.T_U) * Math.exp(-r.a_K * t) };    // schwarzer Kaffee in Tasse 2 vor der Zugabe
}
