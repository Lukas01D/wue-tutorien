// MODELL-ANFANG: gleiche Gleichungen und Standardwerte wie kaffee_modell.py (rechne, zwei_tassen)
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

function zweiTassen(p, C_T = 0.0, th_M1 = null, th_M2 = null, kA1_faktor = 1.0, t_end = null) {
  const r = rechne(p);
  th_M1 = th_M1 === null ? p.th_M : th_M1;
  th_M2 = th_M2 === null ? th_M1 : th_M2;
  const t = t_end === null ? p.t_end : t_end;
  const CKT = r.C_K + C_T, CGT = r.C_G + C_T;
  const kA = -CKT / p.t_mess * r.ln_mess;
  const T10 = (CKT * r.T_K0 + r.C_M * (th_M1 + K)) / CGT;
  const T1 = r.T_U + (T10 - r.T_U) * Math.exp(-kA1_faktor * kA * t / CGT);
  const T2K = r.T_U + (r.T_K0 - r.T_U) * Math.exp(-kA * t / CKT);
  const T2 = (CKT * T2K + r.C_M * (th_M2 + K)) / CGT;
  return { kA: kA, T1_0: T10, T1: T1, T2_K: T2K, T2: T2, dT: T1 - T2, th1: T1 - K, th2: T2 - K };
}

// Einstellungen des Werkzeugs (Einheiten der Regler) in die Größen des Modells übersetzen und auswerten
function berechne(e) {
  const p = Object.assign({}, P, { V_K: e.VK_ml * 1e-6, V_M: e.VM_ml * 1e-6, th_K0: e.thK0, th_M: e.thM, th_U: e.thU,
                                   th_mess: e.thMess, m_B: e.mB_g / 1000, t_end: e.tEnd_min * 60.0 });
  const r = rechne(p);
  const C_T = e.becher ? p.m_B * p.c_B : 0.0;
  const th_M2 = e.milch2Raum ? p.th_U : p.th_M;
  const z = zweiTassen(p, C_T, p.th_M, th_M2, e.kA1Faktor, p.t_end);
  const CKT = r.C_K + C_T, CGT = r.C_G + C_T;
  const a1 = e.kA1Faktor * z.kA / CGT, a2 = z.kA / CKT;          // Abklingraten von Tasse 1 und vom schwarzen Kaffee
  // abgegebene Wärme bis zur Zugabe: Energiebilanz um den Bilanzraum (Inhalt, mit Becher auch der Becher), wie Teil e
  const Q1 = CGT * (z.T1_0 - z.T1), Q2 = CKT * (r.T_K0 - z.T2_K);
  // Schnittpunkt der beiden Kurven vor der Zugabe, in beiden Richtungen (wie t_schnitt in rechne(), dort nur für a2 > a1):
  // (T_K0 - T_U) exp(-a2 t) = (T1_0 - T_U) exp(-a1 t)  =>  t = ln((T_K0 - T_U) / (T1_0 - T_U)) / (a2 - a1), gültig für t > 0
  const d = a2 - a1, q = (r.T_K0 - r.T_U) / (z.T1_0 - r.T_U);
  let tS = Infinity;
  if (d !== 0 && q > 0) { const t = Math.log(q) / d; if (t > 0) tS = t; }
  return { kA: z.kA, T1_0: z.T1_0, T1: z.T1, T2_K: z.T2_K, T2: z.T2, dT: z.dT, th1: z.th1, th2: z.th2, Q1: Q1, Q2: Q2,
           t_schnitt: tS, kaffee_danach_kuehler: d > 0, T_K0: r.T_K0, T_U: r.T_U,
           kurve1: t => r.T_U + (z.T1_0 - r.T_U) * Math.exp(-a1 * t),          // Tasse 1, t in s
           kurve2: t => r.T_U + (r.T_K0 - r.T_U) * Math.exp(-a2 * t) };        // Tasse 2 vor der Zugabe
}
// MODELL-ENDE
