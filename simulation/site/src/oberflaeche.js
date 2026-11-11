// Oberfläche der Kaffee-Simulation Fassung 3 (simulation/KONZEPT_F3.md, Abschnitt 2; Entscheidungen in ENTSCHEIDUNGEN_F3.md).
// Zustände: 0 Start (nur Vorhersage), 1 Ergebnis (Kurven, Warum-Frage), 2 erklärt (Regler, Messung, Schluss, Weiterdenken, Modell).
(function () {
  "use strict";
  const SPEICHER = "kaffee-simulation-f3-45min";   // neuer Schlüssel: alte Stände mit 30 ml und 60 min nicht übernehmen
  const SPRACHE = "kaffee-simulation-sprache";
  const KA_BLATT = kABlatt();
  const MILCH_GRENZE = 30;
  const TOLERANZ_RECHNUNG = 0.1;   // K: Abweichung der eigenen Rechnung, ab der die Seite „weicht ab“ sagt
  const REGLER = [
    { id: "thM", t: "r_thM", einheit: "°C", min: 2, max: 95, schritt: 0.5, stellen: 1, marken: [2, 20, 40, 60, 80, 95], gruppe: false },
    { id: "tZ", t: "r_tZ", einheit: "min", min: 1, max: 180, schritt: 1, stellen: 0, marken: [1, 45, 90, 135, 180], gruppe: false },
    { id: "thK0", t: "r_thK0", einheit: "°C", min: 60, max: 95, schritt: 0.5, stellen: 1, marken: [60, 70, 80, 95], gruppe: true },
    { id: "thU", t: "r_thU", einheit: "°C", min: 10, max: 30, schritt: 0.5, stellen: 1, marken: [10, 20, 30], gruppe: true },
    { id: "kA", t: "r_kA", einheit: "W/K", min: 0.05, max: 0.8, schritt: 0.005, stellen: 4, marken: [0.05, 0.2, 0.4, 0.6, 0.8], gruppe: true },
    { id: "VM_ml", t: "r_VM", einheit: "ml", min: 10, max: 200, schritt: 5, stellen: 0, marken: [10, 50, 100, 150, 200], gruppe: true }
  ];
  const SVGNS = "http://www.w3.org/2000/svg";
  const $ = id => document.getElementById(id);

  // ------------------------------------------------------------ Zustand
  const blatt = () => ({ thM: STANDARD.thM, tZ: STANDARD.tZ, thK0: STANDARD.thK0, thU: STANDARD.thU, kA: KA_BLATT, VM_ml: STANDARD.VM_ml });
  const neu = () => ({ v: 3, z: 0, tasse: null, grund: null, freitext: "", e1: "", e2: "", warum: null, warumFest: false, e: blatt(),
    m1: "", m2: "", bsp: false, ln: false, aktiv: null, schluss: "", schlussGez: false,
    a: { 1: { v: null, fest: false, ged: false }, 2: { v: null, fest: false, ged: false }, 3: { v: null, fest: false, ged: false } } });
  let S = neu();
  let L = "de";
  let speicherOk = true;

  function speichern() {
    if (!speicherOk) return;
    try { localStorage.setItem(SPEICHER, JSON.stringify(S)); } catch (err) { speicherOk = false; fussText(); }
  }
  function laden() {
    try {
      const t = "kaffee-test"; localStorage.setItem(t, "1"); localStorage.removeItem(t);
    } catch (err) { speicherOk = false; }
    let alt = null;
    if (speicherOk) { try { alt = JSON.parse(localStorage.getItem(SPEICHER) || "null"); } catch (err) { alt = null; } }
    if (alt && alt.v === 3) {
      const n = neu();
      for (const k of Object.keys(n)) if (k in alt && typeof alt[k] === typeof n[k] || (k in alt && n[k] === null)) n[k] = alt[k];
      for (const r of REGLER) { const x = alt.e && alt.e[r.id]; n.e[r.id] = typeof x === "number" && isFinite(x) ? begrenze(r, x, n) : blatt()[r.id]; }
      for (const i of [1, 2, 3]) n.a[i] = Object.assign(neu().a[i], alt.a && alt.a[i]);
      if (![0, 1, 2].includes(n.z)) n.z = 0;
      S = n;
    }
    const q = new URLSearchParams(location.search).get("lang");
    let gesp = null;
    if (speicherOk) { try { gesp = localStorage.getItem(SPRACHE); } catch (err) { gesp = null; } }
    L = q === "en" || q === "de" ? q : (gesp === "en" ? "en" : "de");
  }

  // ------------------------------------------------------------ Texte und Zahlen
  const T = k => (TEXTE[L][k] !== undefined ? TEXTE[L][k] : "[" + k + "]");
  const F = (k, v) => T(k).replace(/\{(\w+)\}/g, (m, n) => (v[n] !== undefined ? v[n] : m));
  function zahl(x, n) {
    let s = Number(x).toFixed(n);
    if (/^-0(\.0+)?$/.test(s)) s = s.slice(1);          // keine „−0,00“
    if (s.startsWith("-")) s = "−" + s.slice(1);
    return L === "de" ? s.replace(".", ",") : s;
  }
  function liesZahl(s) {
    const t = String(s).trim().replace("−", "-").replace(",", ".");
    return /^-?(\d+(\.\d*)?|\.\d+)$/.test(t) ? Number(t) : NaN;
  }
  const textOhneTags = html => { const d = document.createElement("div"); d.innerHTML = html; return d.textContent.replace(/\s+/g, " ").trim(); };

  function texteSetzen() {
    document.documentElement.lang = L;
    document.title = T("titel_seite");
    document.querySelectorAll("[data-t]").forEach(el => {
      const bereich = el.closest("[data-ab]");
      el.innerHTML = !bereich || S.z >= Number(bereich.dataset.ab) ? T(el.dataset.t) : "";
    });
    $("sprache").setAttribute("aria-label", T("sprache_knopf_aria"));
    for (const r of REGLER) reglerTexte(r);
    auftraegeTexte();
    fussText();
  }
  function fussText() {
    $("fuss-text").textContent = F("fuss", { stand: BAU.stand, version: BAU.version });
    $("speicher-text").textContent = T(speicherOk ? "speicher_ok" : "speicher_aus");
  }

  // ------------------------------------------------------------ Regler
  function obergrenze(r, s) { return r.id === "thM" && !(s || S).a[3].fest ? MILCH_GRENZE : r.max; }
  function begrenze(r, x, s) { return Math.min(obergrenze(r, s), Math.max(r.min, x)); }
  function reglerBauen() {
    for (const r of REGLER) {
      const d = document.createElement("div");
      d.className = "regler"; d.dataset.r = r.id;
      d.innerHTML = '<p class="name" id="rn-' + r.id + '"></p>' +
        '<button type="button" class="pm" id="rminus-' + r.id + '">−</button>' +
        '<div class="lineal"><input type="range" id="rr-' + r.id + '" aria-labelledby="rn-' + r.id + '"><div class="skala" aria-hidden="true" id="rs-' + r.id + '"></div></div>' +
        '<button type="button" class="pm" id="rplus-' + r.id + '">+</button>' +
        '<input class="feld" id="rf-' + r.id + '" inputmode="decimal" autocomplete="off">' +
        '<p class="hinweis" id="rh-' + r.id + '"></p><p class="meldung" id="rm-' + r.id + '" role="alert"></p>';
      $(r.gruppe ? "regler-gruppe" : "regler-sichtbar").appendChild(d);
      const ein = $("rr-" + r.id), feld = $("rf-" + r.id);
      ein.min = r.min; ein.step = r.schritt;
      ein.addEventListener("input", () => setze(r, Number(ein.value), false));
      ein.addEventListener("change", () => ansage());
      $("rminus-" + r.id).addEventListener("click", () => { setze(r, S.e[r.id] - r.schritt, true); });
      $("rplus-" + r.id).addEventListener("click", () => { setze(r, S.e[r.id] + r.schritt, true); });
      const ausFeld = () => {
        const x = liesZahl(feld.value);
        if (isNaN(x) || x < r.min || x > obergrenze(r)) {
          feld.setAttribute("aria-invalid", "true");
          $("rm-" + r.id).textContent = F("r_falsch", { min: zahl(r.min, r.stellen > 1 ? 2 : r.stellen), max: zahl(obergrenze(r), r.stellen > 1 ? 2 : r.stellen) });
          return;
        }
        feld.removeAttribute("aria-invalid"); $("rm-" + r.id).textContent = "";
        setze(r, x, true);
      };
      feld.addEventListener("change", ausFeld);
      feld.addEventListener("keydown", ev => { if (ev.key === "Enter") { ev.preventDefault(); ausFeld(); } });
    }
  }
  function reglerTexte(r) {
    $("rn-" + r.id).innerHTML = T(r.t) + ' <span class="einheit">[' + r.einheit + "]</span>";
    const name = textOhneTags(T(r.t));
    $("rminus-" + r.id).setAttribute("aria-label", T("r_minus") + ": " + name);
    $("rplus-" + r.id).setAttribute("aria-label", T("r_plus") + ": " + name);
    $("rf-" + r.id).setAttribute("aria-label", F("r_feld_aria", { name: name, einheit: r.einheit }));
  }
  function setze(r, x, ansagen) {
    if (!isFinite(x)) return;
    S.e[r.id] = begrenze(r, x);
    $("rf-" + r.id).removeAttribute("aria-invalid"); $("rm-" + r.id).textContent = "";
    aktualisiere();
    if (ansagen) ansage();
  }
  function reglerAnzeigen(erg) {
    for (const r of REGLER) {
      const ein = $("rr-" + r.id), max = obergrenze(r), v = S.e[r.id];
      ein.max = max;
      ein.value = v;
      ein.setAttribute("aria-valuetext", zahl(v, r.stellen) + " " + r.einheit);
      const feld = $("rf-" + r.id);
      if (document.activeElement !== feld || feld.getAttribute("aria-invalid") !== "true") feld.value = zahl(v, r.stellen);
      const marken = r.id === "thM" && max < r.max ? [2, 10, 20, 30] : r.marken;
      const sk = $("rs-" + r.id);
      sk.textContent = "";
      for (const m of marken) {
        const sp = document.createElement("span");
        sp.textContent = zahl(m, r.id === "kA" ? 2 : 0);
        sp.style.left = (100 * (m - r.min) / (max - r.min)).toFixed(2) + "%";
        sk.appendChild(sp);
      }
      const h = $("rh-" + r.id);
      if (r.id === "thM") h.textContent = max < r.max ? T("r_thM_sperre") : (v >= 40 ? T("r_thM_warm") : "");
      else if (r.id === "kA") h.textContent = F("r_kA_mess", { th: zahl(erg.th_mess, 1) });
      $("rminus-" + r.id).disabled = v <= r.min;
      $("rplus-" + r.id).disabled = v >= max;
    }
    const e = S.e;
    const gruppeBlatt = e.thK0 === STANDARD.thK0 && e.thU === STANDARD.thU && e.kA === KA_BLATT && e.VM_ml === STANDARD.VM_ml;
    $("gruppe-zus").innerHTML = F("gruppe_zus", { thK0: zahl(e.thK0, 1), thU: zahl(e.thU, 1), kA: zahl(e.kA, 4), VM: zahl(e.VM_ml, 0) }) +
      (gruppeBlatt ? ' <span class="vorl">' + T("vorlaeufig") + "</span>" : "");
  }
  const istBlatt = () => { const b = blatt(); return Object.keys(b).every(k => S.e[k] === b[k]); };

  // ------------------------------------------------------------ Messpunkte
  function messreihe(text, n) {
    const teile = String(text).trim().split(/[\s;]+/).filter(Boolean);
    if (teile.length > n) return { fehler: F("s3_f_viele", { n: n }) };
    const werte = [];
    for (const tk of teile) {
      if (/^[xX]$/.test(tk)) { werte.push(null); continue; }
      const v = liesZahl(tk);
      if (isNaN(v)) return { fehler: F("s3_f_zahl", { w: tk }) };
      if (v < 0 || v > 100) return { fehler: F("s3_f_bereich", { w: zahl(v, 1) }) };
      werte.push(v);
    }
    return { werte: werte };
  }
  function messungen() {
    const m1 = messreihe(S.m1, ZEITEN.length), m2 = messreihe(S.m2, ZEITEN.length + 1);
    return { t1: m1.werte || [], t2: m2.werte || [], f1: m1.fehler || null, f2: m2.fehler || null };
  }
  function messInfo() {
    const m = messungen();
    const start2 = m.t2.length && m.t2[0] !== null ? m.t2[0] : null;
    for (const [nr, werte, fehler] of [[1, m.t1, m.f1], [2, m.t2, m.f2]]) {
      const info = $("m" + nr + "-info"), feld = $("m" + nr);
      if (fehler) { info.textContent = fehler; info.classList.add("fehler"); feld.setAttribute("aria-invalid", "true"); continue; }
      info.classList.remove("fehler"); feld.removeAttribute("aria-invalid");
      const liste = [];
      let hoch = null;
      werte.forEach((v, i) => {
        if (v === null) return;
        const t = i === ZEITEN.length ? STANDARD.tZ + " min, " + T("s3_nach_milch") : ZEITEN[i] + " min";
        liste.push(t + " " + zahl(v, 1));
        if (start2 !== null && !(nr === 2 && i === 0) && v > start2 + 0.5) hoch = v;
      });
      info.textContent = liste.length ? F("s3_erkannt", { liste: liste.join(" · ") }) + (hoch !== null ? " " + F("s3_f_hoch", { w: zahl(hoch, 1) }) : "") : "";
    }
  }

  // ------------------------------------------------------------ Diagramm
  function el(tag, at, txt) {
    const n = document.createElementNS(SVGNS, tag);
    for (const k in at) n.setAttribute(k, at[k]);
    if (txt !== undefined) n.textContent = txt;
    return n;
  }
  function diagrammHoehe(svg, W) {
    if (window.innerWidth < 1024) return Math.round(Math.min(360, W * (W < 500 ? 0.82 : 0.68)));   // Handy etwas höher, damit die Abfälle durch die Milch deutlich bleiben
    const b = $("buehne"), fig = svg.parentNode;
    let rest = 4;
    for (const c of b.children) if (c !== fig && !c.hidden && c.getClientRects().length) rest += c.getBoundingClientRect().height;
    return Math.round(Math.max(240, Math.min(W * 0.55, window.innerHeight - rest - 24)));
  }
  function zeichne(erg) {
    const svg = $("dia");
    const W = Math.max(260, Math.round(svg.getBoundingClientRect().width || 600));
    const H = diagrammHoehe(svg, W);
    svg.setAttribute("viewBox", "0 0 " + W + " " + H);
    svg.setAttribute("height", H);
    svg.textContent = "";
    const fs = W >= 600 ? 13 : 12;
    if (S.z >= 2 && S.ln) return zeichneLn(svg, W, H, fs, erg);
    const e = S.e, m = messungen();
    const pkt = [...m.t1, ...m.t2, ...(S.bsp ? [...BEISPIEL.t1, ...BEISPIEL.t2] : [])].filter(v => v !== null);
    const xmax = Math.max(60, Math.ceil(e.tZ / 10) * 10);
    const ymax = Math.max(90, Math.ceil((Math.max(e.thK0, erg.th10, erg.th2, ...pkt) + 3) / 10) * 10);
    const ymin = Math.min(10, Math.floor((e.thU - 5) / 10) * 10, ...pkt.map(v => Math.floor((v - 2) / 10) * 10));
    const Lr = 46, R = 24, Tr = 12, B = 38, P = 12;   // P: Abstand der Achse von t = 0, damit der Abfall von Tasse 1 nicht auf der Achse liegt
    const X = t => Lr + P + (W - Lr - P - R) * t / xmax, Y = v => Tr + (H - Tr - B) * (ymax - v) / (ymax - ymin);
    const fein = xmax <= 90 ? 5 : 10, grob = xmax <= 90 ? 10 : 30;
    for (let t = 0; t <= xmax + 1e-9; t += fein) svg.appendChild(el("line", { x1: X(t), x2: X(t), y1: Y(ymax), y2: Y(ymin), class: t % grob ? "gitter" : "gitter-haupt" }));
    for (let v = ymin; v <= ymax; v += 5) svg.appendChild(el("line", { x1: Lr, x2: X(xmax), y1: Y(v), y2: Y(v), class: v % 10 ? "gitter" : "gitter-haupt" }));
    svg.appendChild(el("line", { x1: Lr, x2: X(xmax), y1: Y(ymin), y2: Y(ymin), class: "achse" }));
    svg.appendChild(el("line", { x1: Lr, x2: Lr, y1: Y(ymin), y2: Y(ymax), class: "achse" }));
    for (let t = 0; t <= xmax; t += grob) svg.appendChild(el("text", { x: X(t), y: Y(ymin) + 15, "text-anchor": "middle", "font-size": fs, class: "ax" }, String(t)));
    for (let v = ymin; v <= ymax; v += (ymax - ymin > 80 ? 20 : 20)) svg.appendChild(el("text", { x: Lr - 6, y: Y(v) + 4, "text-anchor": "end", "font-size": fs, class: "ax" }, String(v)));
    svg.appendChild(el("text", { x: (X(0) + X(xmax)) / 2, y: H - 5, "text-anchor": "middle", "font-size": fs, class: "beschr" }, T("dia_zeit")));
    const ym = (Y(ymin) + Y(ymax)) / 2;
    svg.appendChild(el("text", { x: 12, y: ym, "text-anchor": "middle", "font-size": fs, class: "beschr", transform: "rotate(-90 12 " + ym + ")" }, T("dia_temp")));
    svg.appendChild(el("line", { x1: Lr, x2: X(xmax), y1: Y(e.thU), y2: Y(e.thU), class: "raum" }));
    svg.appendChild(el("text", { x: X(xmax) - 2, y: Y(e.thU) - 6, "text-anchor": "end", "font-size": fs, class: "leise-text" }, F("dia_raum", { th: zahl(e.thU, 1) })));
    if (S.z === 0) {
      svg.appendChild(el("text", { x: (X(0) + X(xmax)) / 2, y: Y((ymin + ymax) / 2), "text-anchor": "middle", "font-size": fs + 1, class: "leise-text" }, T("dia_leer")));
      $("dia-beschreibung").textContent = T("dia_leer");
      return;
    }
    const tZ = e.tZ * 60, p1 = [], p2 = [];
    for (let i = 0; i <= 160; i++) {
      const t = tZ * i / 160;
      p1.push(X(t / 60).toFixed(1) + "," + Y(erg.kurve1(t)).toFixed(1));
      p2.push(X(t / 60).toFixed(1) + "," + Y(erg.kurve2(t)).toFixed(1));
    }
    const dick = W >= 600 ? 3 : 2.5;
    svg.appendChild(el("polyline", { points: p1.join(" "), class: "kurve k1", "stroke-width": dick }));
    svg.appendChild(el("polyline", { points: p2.join(" "), class: "kurve k2 gestrichelt", "stroke-width": dick }));
    // Sprung durch die Milch: kräftig gestrichelt (Tasse 1 bei t = 0 vom Kaffee auf die Mischtemperatur, Tasse 2 bei tZ).
    // Meist nach unten; ist die Milch wärmer als der Kaffee, zeigt der Pfeil nach oben (r = Richtung in Pixeln, +1 abwärts).
    const abf = [[0, e.thK0, erg.th10, "k1", 0], [e.tZ, erg.th2K, erg.th2, "k2", 6]].map(([t, o, u, k, l]) => {
      const r = Y(u) >= Y(o) ? 1 : -1, x = X(t), y1 = Y(o), y2 = Y(u) - r * l, lang = r * (y2 - y1);
      return { t: t, x: x, y1: y1, y2: y2, r: r, k: k, sp: Math.min(W >= 600 ? 9 : 7, lang / 2), ok: lang > 2 };
    });
    for (const a of abf) if (a.ok) svg.appendChild(el("line", { x1: a.x, x2: a.x, y1: a.y1, y2: a.y2 - a.r * a.sp, class: "abfall " + a.k, "stroke-width": dick }));
    // Messpunkte: eigene gefüllt, Beispielwerte hohl
    const punkt = (t, v, tasse, hohl) => {
      if (tasse === 1) svg.appendChild(el("circle", { cx: X(t), cy: Y(v), r: 4.2, class: "punkt k1" + (hohl ? " hohl" : "") }));
      else svg.appendChild(el("rect", { x: X(t) - 4, y: Y(v) - 4, width: 8, height: 8, class: "punkt k2" + (hohl ? " hohl" : "") }));
    };
    if (S.bsp) {
      BEISPIEL.t1.forEach((v, i) => punkt(ZEITEN[i], v, 1, true));
      BEISPIEL.t2.forEach((v, i) => punkt(ZEITEN[i], v, 2, true));
      punkt(STANDARD.tZ, BEISPIEL.t2Milch, 2, true);
    }
    m.t1.forEach((v, i) => { if (v !== null) punkt(ZEITEN[i], v, 1, false); });
    m.t2.forEach((v, i) => { if (v !== null) punkt(i === ZEITEN.length ? STANDARD.tZ : ZEITEN[i], v, 2, false); });
    svg.appendChild(el("circle", { cx: X(e.tZ), cy: Y(erg.th1), r: 4.5, class: "ende k1" }));
    svg.appendChild(el("circle", { cx: X(e.tZ), cy: Y(erg.th2), r: 4.5, class: "ende k2" }));
    // Pfeilspitzen und Beschriftung der Abfälle über den Endpunkten (Spitze von Tasse 2 endet am Rand ihres Endpunkts)
    for (const a of abf) {
      if (!a.ok) continue;
      const ecken = [[a.x - a.sp * 0.7, a.y2 - a.r * a.sp], [a.x + a.sp * 0.7, a.y2 - a.r * a.sp], [a.x, a.y2]];
      svg.appendChild(el("polygon", { points: ecken.map(q => q[0].toFixed(1) + "," + q[1].toFixed(1)).join(" "), class: "pfeil " + a.k }));
      if (a.r * (a.y2 - a.y1) > 2.2 * fs) {
        const yt = a.t === 0 || a.r < 0 ? (a.y1 + a.y2) / 2 + fs * 0.35 : a.y1 + fs * 1.1;   // Tasse 2 nach unten: oben neben dem Sprung, frei von den Endpunkten
        imBild(svg.appendChild(el("text", { x: a.x + 8, y: yt, "font-size": fs, class: "kbeschr " + a.k + "-text" }, T("dia_milch"))), Lr + 2, W - 4);
      }
    }
    // eigene Rechnung aus e (nur bei den Werten des Blatts)
    const r1 = liesZahl(S.e1), r2 = liesZahl(S.e2), mitRechnung = istBlatt() && (isFinite(r1) || isFinite(r2));
    if (mitRechnung) for (const v of [r1, r2]) if (isFinite(v) && v >= ymin && v <= ymax) svg.appendChild(el("text", { x: X(e.tZ) + 13, y: Y(v) + 5, "text-anchor": "middle", "font-size": 15, class: "kreuz" }, "×"));
    // Direktbeschriftung: Tasse 2 im ersten, Tasse 1 im zweiten Zeitfenster, je dort, wo die Kurven am weitesten auseinanderliegen.
    // Ist die Kurve dort die obere, steht der Text darüber und beginnt dort (Kurve fällt nach rechts weg); ist sie die untere,
    // steht er darunter und endet dort (tiefster Punkt seines Bereichs). So berühren Text und Linien sich nicht.
    const abstand = t => Math.abs(erg.kurve1(t) - erg.kurve2(t));
    const Xinv = x => (x - Lr - P) / (W - Lr - P - R) * xmax * 60;
    const beste = (von, bis) => { let tb = tZ * von, ab = -1; for (let i = 0; i <= 24; i++) { const t = tZ * (von + (bis - von) * i / 24); if (abstand(t) > ab) { ab = abstand(t); tb = t; } } return tb; };
    for (const [n, von, bis] of [[2, 0.08, 0.45], [1, 0.5, 0.92]]) {
      const k = n === 1 ? erg.kurve1 : erg.kurve2, anders = n === 1 ? erg.kurve2 : erg.kurve1;
      const txt = n === 1 ? T("dia_t1") : F("dia_t2", { t: e.tZ }), w = txt.length * fs * 0.56;
      const t = beste(von, bis), oben = k(t) >= anders(t);
      let x, y;
      if (oben) { x = Math.max(Lr + 4, Math.min(X(t / 60), W - R - w, n === 1 ? X(e.tZ) - 8 - w : W)); y = Y(k(Math.max(0, Xinv(x)))) - 10; }
      else { x = Math.min(W - R, Math.max(X(t / 60), Lr + w + 4)); y = Y(k(Math.min(tZ, Xinv(x)))) + 22; }
      imBild(svg.appendChild(el("text", { x: x, y: y, "text-anchor": oben ? "start" : "end", "font-size": fs, class: "kbeschr " + (n === 1 ? "k1-text" : "k2-text") }, txt)), Lr + 2, W - 4);
    }
    $("dia-beschreibung").textContent = F("dia_beschreibung", { a1: zahl(erg.th10, 1), e1: zahl(erg.th1, 1), a2: zahl(e.thK0, 1), e2: zahl(erg.th2K, 1), m2: zahl(erg.th2, 1), u: zahl(e.thU, 1), t: e.tZ,
      v1: T(erg.th10 > e.thK0 ? "dia_hoch" : "dia_runter"), v2: T(erg.th2 > erg.th2K ? "dia_hoch" : "dia_runter") });
    // Legende nur für vorhandene Zeichen
    const leg = [];
    if (mitRechnung) leg.push(T("leg_rechnung"));
    if (S.bsp) leg.push(T("leg_beispiel"));
    if (m.t1.some(v => v !== null) || m.t2.some(v => v !== null)) leg.push(T("leg_messung"));
    $("legende").textContent = leg.join(" · ");
    $("legende").hidden = !leg.length;
  }
  function imBild(t, links, rechts) {             // verschiebt einen SVG-Text waagerecht, bis er ganz zwischen links und rechts liegt
    const b = t.getBBox();
    if (!b.width) return;
    const dx = b.x + b.width > rechts ? rechts - (b.x + b.width) : (b.x < links ? links - b.x : 0);
    if (dx) t.setAttribute("x", Number(t.getAttribute("x")) + dx);
  }
  function zeichneLn(svg, W, H, fs, erg) {
    const m = messungen(), u = S.e.thU;
    let reihe = m.t2.slice(0, ZEITEN.length), eigene = true;
    if (!(reihe.length >= 2 && reihe[0] !== null) && S.bsp) { reihe = BEISPIEL.t2.slice(); eigene = false; }
    const pkte = [];
    if (reihe.length >= 2 && reihe[0] !== null && reihe[0] > u) reihe.forEach((v, i) => { if (v !== null && v > u) pkte.push([ZEITEN[i], Math.log((v - u) / (reihe[0] - u))]); });
    const steigung = -erg.kA * 60 / erg.C_K;   // je min
    const ymin = Math.floor(Math.min(steigung * 60, ...pkte.map(q => q[1])) * 10 - 0.5) / 10, ymax = 0.05;
    const Lr = 54, R = 24, Tr = 12, B = 38;
    const X = t => Lr + (W - Lr - R) * t / 60, Y = v => Tr + (H - Tr - B) * (ymax - v) / (ymax - ymin);
    for (let t = 0; t <= 60; t += 5) svg.appendChild(el("line", { x1: X(t), x2: X(t), y1: Y(ymax), y2: Y(ymin), class: t % 10 ? "gitter" : "gitter-haupt" }));
    const dy = ymax - ymin > 1.2 ? 0.2 : 0.1;
    for (let v = 0; v >= ymin - 1e-9; v -= dy) {
      svg.appendChild(el("line", { x1: X(0), x2: X(60), y1: Y(v), y2: Y(v), class: "gitter-haupt" }));
      svg.appendChild(el("text", { x: X(0) - 6, y: Y(v) + 4, "text-anchor": "end", "font-size": fs, class: "ax" }, zahl(v, 1)));
    }
    svg.appendChild(el("line", { x1: X(0), x2: X(60), y1: Y(ymin), y2: Y(ymin), class: "achse" }));
    svg.appendChild(el("line", { x1: X(0), x2: X(0), y1: Y(ymin), y2: Y(ymax), class: "achse" }));
    for (let t = 0; t <= 60; t += 10) svg.appendChild(el("text", { x: X(t), y: Y(ymin) + 15, "text-anchor": "middle", "font-size": fs, class: "ax" }, String(t)));
    svg.appendChild(el("text", { x: (X(0) + X(60)) / 2, y: H - 5, "text-anchor": "middle", "font-size": fs, class: "beschr" }, T("dia_zeit")));
    const ym = (Y(ymin) + Y(ymax)) / 2;
    svg.appendChild(el("text", { x: 12, y: ym, "text-anchor": "middle", "font-size": fs, class: "beschr", transform: "rotate(-90 12 " + ym + ")" }, T("dia_ln_y")));
    svg.appendChild(el("line", { x1: X(0), y1: Y(0), x2: X(60), y2: Y(steigung * 60), class: "kurve k2 gestrichelt", "stroke-width": 2.5 }));
    const lnText = svg.appendChild(el("text", { x: X(32), y: Y(steigung * 32) - 10, "font-size": fs, class: "kbeschr k2-text" }, F("dia_ln_modell", { kA: zahl(erg.kA, 4) })));
    imBild(lnText, Lr + 2, W - 4);
    const xl = Number(lnText.getAttribute("x"));
    lnText.setAttribute("y", Y(steigung * Math.max(0, Math.min(60, (xl - Lr) / (W - Lr - R) * 60))) - 10);   // über der Geraden am Textanfang
    for (const [t, v] of pkte) svg.appendChild(el("rect", { x: X(t) - 4, y: Y(v) - 4, width: 8, height: 8, class: "punkt k2" + (eigene ? "" : " hohl") }));
    if (!pkte.length) svg.appendChild(el("text", { x: (X(0) + X(60)) / 2, y: Y(ymin * 0.25), "text-anchor": "middle", "font-size": fs, class: "leise-text" }, T("dia_ln_leer")));
    $("dia-beschreibung").textContent = T("dia_ln_titel") + ". " + F("dia_ln_modell", { kA: zahl(erg.kA, 4) }) + ".";
    $("legende").hidden = true;
  }

  // ------------------------------------------------------------ Säulen
  function saeulen(erg) {
    const s = $("saeulen");
    s.textContent = "";
    const b = 146, top = 26, max = Math.max(erg.Q1, erg.Q2, 1e-9);
    const h1 = (b - top) * Math.max(erg.Q1, 0) / max, h2 = (b - top) * Math.max(erg.Q2, 0) / max;
    const defs = el("defs", {}), pat = el("pattern", { id: "schraffur", width: 6, height: 6, patternUnits: "userSpaceOnUse", patternTransform: "rotate(45)" });
    pat.appendChild(el("rect", { width: 6, height: 6, class: "schraffur-grund" }));
    pat.appendChild(el("line", { x1: 0, y1: 0, x2: 0, y2: 6, class: "schraffur-linie" }));
    defs.appendChild(pat); s.appendChild(defs);
    s.appendChild(el("rect", { x: 20, y: b - h1, width: 56, height: h1, class: "saeule1" }));
    s.appendChild(el("rect", { x: 100, y: b - h2, width: 56, height: h2, class: "saeule2" }));
    s.appendChild(el("line", { x1: 10, x2: 170, y1: b, y2: b, class: "achse" }));
    const oben = Math.min(b - h1, b - h2), unten = Math.max(b - h1, b - h2);
    s.appendChild(el("line", { x1: 78, x2: 168, y1: b - h1, y2: b - h1, class: "bezug" }));
    s.appendChild(el("path", { d: "M162 " + oben + " h8 V" + unten + " h-8", class: "klammer" }));
    const ymid = (oben + unten) / 2;
    s.appendChild(el("text", { x: 176, y: ymid - 2, "font-size": 13, class: "diff-text" }, T("saeule_diff")));
    s.appendChild(el("text", { x: 48, y: b + 18, "text-anchor": "middle", "font-size": 13, class: "kbeschr k1-text" }, T("saeule_t1")));
    s.appendChild(el("text", { x: 128, y: b + 18, "text-anchor": "middle", "font-size": 13, class: "kbeschr k2-text" }, T("saeule_t2")));
    const q1 = zahl(erg.Q1 / 1000, 2), q2 = zahl(erg.Q2 / 1000, 2), dq = zahl((erg.Q2 - erg.Q1) / 1000, 2);
    if (S.warumFest) {
      s.appendChild(el("text", { x: 176, y: ymid + 14, "font-size": 13, class: "diff-text zahl" }, dq + " kJ"));
      s.appendChild(el("text", { x: 48, y: b - h1 - 6, "text-anchor": "middle", "font-size": 12, class: "zahl" }, q1 + " kJ"));
      s.appendChild(el("text", { x: 128, y: b - h2 - 6, "text-anchor": "middle", "font-size": 12, class: "zahl" }, q2 + " kJ"));
      s.setAttribute("aria-label", F("s2_saeulen_aria_zahl", { q1: q1, q2: q2, dq: dq }));
    } else {
      s.setAttribute("aria-label", T("s2_saeulen_aria"));
    }
  }

  // ------------------------------------------------------------ Aufträge (Weiterdenken)
  const AUFTRAEGE = [
    { n: 1, art: "wahl", optionen: ["a1_o1", "a1_o2", "a1_o3"] },
    { n: 2, art: "zahl" },
    { n: 3, art: "wahl", optionen: ["a3_o1", "a3_o2", "a3_o3"] }
  ];
  function auftraegeBauen() {
    const box = $("auftraege");
    for (const a of AUFTRAEGE) {
      const d = document.createElement("details");
      d.className = "auftrag"; d.id = "a" + a.n;
      let eingabe;
      if (a.art === "wahl") {
        eingabe = '<fieldset><legend class="nur-leser" id="a' + a.n + '-leg"></legend><div class="wahl">' +
          a.optionen.map((o, i) => '<label><input type="radio" name="a' + a.n + '" value="' + i + '"> <span id="a' + a.n + "-o" + i + '"></span></label>').join("") + "</div></fieldset>";
      } else {
        eingabe = '<div class="zahlen-zeile"><label><span id="a2-label"></span> <input class="feld" id="a2-zahl" inputmode="decimal" autocomplete="off" size="6"></label></div>';
      }
      d.innerHTML = '<summary id="a' + a.n + '-titel"></summary><p id="a' + a.n + '-frage"></p>' + eingabe +
        '<button type="button" class="knopf" id="a' + a.n + '-knopf"></button><p class="meldung" id="a' + a.n + '-meldung" role="alert"></p>' +
        '<div id="a' + a.n + '-pruefen" hidden><p id="a' + a.n + '-vermutung"></p><p id="a' + a.n + '-auftrag"></p>' +
        '<button type="button" class="knopf" id="a' + a.n + '-ged-knopf"></button><div class="rueck" id="a' + a.n + '-ged" tabindex="-1" hidden></div></div>';
      box.appendChild(d);
      $("a" + a.n + "-knopf").addEventListener("click", () => vermutungFesthalten(a));
      $("a" + a.n + "-ged-knopf").addEventListener("click", () => { S.a[a.n].ged = true; zeigeAuftraege(); speichern(); $("a" + a.n + "-ged").focus(); });
    }
  }
  function auftraegeTexte() {
    for (const a of AUFTRAEGE) {
      $("a" + a.n + "-titel").innerHTML = T("a" + a.n + "_titel");
      $("a" + a.n + "-frage").innerHTML = T("a" + a.n + "_frage");
      if (a.art === "wahl") { $("a" + a.n + "-leg").innerHTML = T("a" + a.n + "_frage"); a.optionen.forEach((o, i) => { $("a" + a.n + "-o" + i).innerHTML = T(o); }); }
      else $("a2-label").textContent = T("a2_label");
      $("a" + a.n + "-knopf").textContent = T("knopf_vermutung");
      $("a" + a.n + "-ged-knopf").textContent = T("knopf_gedanken");
      $("a" + a.n + "-auftrag").innerHTML = T("a" + a.n + "_pruefen");
      $("a" + a.n + "-ged").innerHTML = S.a[a.n].ged ? "<p>" + T("a" + a.n + "_gedanken") + "</p>" : "";
    }
  }
  function vermutungText(n) {
    const a = AUFTRAEGE[n - 1], v = S.a[n].v;
    if (v === null) return "";
    return a.art === "wahl" ? textOhneTags(T(a.optionen[v])) : zahl(v, 0) + " min";
  }
  function vermutungFesthalten(a) {
    let v = null;
    if (a.art === "wahl") { const x = document.querySelector('input[name="a' + a.n + '"]:checked'); v = x ? Number(x.value) : null; }
    else { const x = liesZahl($("a2-zahl").value); v = isFinite(x) && x >= 0 && x <= 600 ? x : null; }
    if (v === null) { $("a" + a.n + "-meldung").textContent = T("vermutung_fehlt"); return; }
    $("a" + a.n + "-meldung").textContent = "";
    S.a[a.n] = { v: v, fest: true, ged: S.a[a.n].ged };
    S.e = blatt();
    S.aktiv = a.n;
    aktualisiere();
    zeigeAuftraege();
    ansage(T("status_blatt"));
    if (window.innerWidth < 1024) $("buehne").scrollIntoView({ block: "start" });
  }
  function zeigeAuftraege() {
    for (const a of AUFTRAEGE) {
      const z = S.a[a.n];
      if (a.art === "wahl") document.querySelectorAll('input[name="a' + a.n + '"]').forEach(x => { x.checked = z.v !== null && Number(x.value) === z.v; x.disabled = z.fest; });
      else { if (z.v !== null) $("a2-zahl").value = zahl(z.v, 0); $("a2-zahl").disabled = z.fest; }
      $("a" + a.n + "-knopf").hidden = z.fest;
      $("a" + a.n + "-pruefen").hidden = !z.fest;
      $("a" + a.n + "-vermutung").textContent = z.fest ? F("deine_vermutung", { v: vermutungText(a.n) }) : "";
      $("a" + a.n + "-ged-knopf").hidden = z.ged;
      $("a" + a.n + "-ged").hidden = !z.ged;
      $("a" + a.n + "-ged").innerHTML = z.ged ? "<p>" + T("a" + a.n + "_gedanken") + "</p>" : "";
    }
    const zeile = $("auftrag-zeile");
    if (S.aktiv && S.a[S.aktiv].fest && S.z >= 2) {
      zeile.innerHTML = F("auftrag_zeile", { n: S.aktiv, frage: T("a" + S.aktiv + "_frage"), v: vermutungText(S.aktiv) });
      zeile.hidden = false;
    } else zeile.hidden = true;
  }

  // ------------------------------------------------------------ Ansage, Kernzahlen, Kernsatz
  let ansageTimer = 0;
  function ansage(text) {
    window.clearTimeout(ansageTimer);
    $("ansage").textContent = "";
    if (S.z < 1) return;                                   // vor der Vorhersage keine Ergebnisansage (X6-01)
    const erg = auswerten(S.e);
    const t = text || F("status_werte", { t: S.e.tZ, th1: zahl(erg.th1, 2), th2: zahl(erg.th2, 2), dT: zahl(erg.dT, 2) });
    ansageTimer = window.setTimeout(() => { if (S.z >= 1) $("ansage").textContent = t; }, 60);
  }
  // Im Startzustand alle Ergebnisinhalte und -attribute leeren, auch nach „Von vorn“ (X6-01)
  function ergebnisseLeeren() {
    window.clearTimeout(ansageTimer);
    for (const id of ["ansage", "w1", "w2", "wd", "kern-zeit", "kernsatz", "s1-zusammenfassung", "s2-rueck", "s4-rueck", "auftrag-zeile", "legende", "gruppe-zus"]) $(id).textContent = "";
    $("saeulen").textContent = "";
    $("saeulen").removeAttribute("aria-label");
    for (const r of REGLER) {
      $("rf-" + r.id).value = "";
      $("rr-" + r.id).removeAttribute("aria-valuetext");
      $("rh-" + r.id).textContent = "";
      $("rm-" + r.id).textContent = "";
    }
  }
  function kern(erg) {
    $("kern-zeit").textContent = F("kern_nach", { t: S.e.tZ });
    $("w1").textContent = zahl(erg.th1, 2) + " °C";
    $("w2").textContent = zahl(erg.th2, 2) + " °C";
    $("wd").textContent = zahl(erg.dT, 2) + " K";
    const r1 = liesZahl(S.e1), r2 = liesZahl(S.e2);
    let html = T("kernsatz");
    if (istBlatt() && (isFinite(r1) || isFinite(r2))) {
      const ab = [];
      if (isFinite(r1) && Math.abs(r1 - erg.th1) > TOLERANZ_RECHNUNG) ab.push(F("kernsatz_ab_teil", { tasse: T("kern_t1"), e: zahl(r1, 2), s: zahl(erg.th1, 2) }));
      if (isFinite(r2) && Math.abs(r2 - erg.th2) > TOLERANZ_RECHNUNG) ab.push(F("kernsatz_ab_teil", { tasse: T("kern_t2"), e: zahl(r2, 2), s: zahl(erg.th2, 2) }));
      html = ab.length ? F("kernsatz_ab", { abw: ab.join("; ") }) : T("kernsatz_gleich");
    }
    $("kernsatz").innerHTML = html;
  }

  // ------------------------------------------------------------ Zustand anzeigen
  function zeigeZustand() {
    const z = S.z;
    if (z === 0) ergebnisseLeeren();
    // X6-04: Link „Modell“ erst mit seinem Ziel (ab Zustand 2), dann klappt er den Bereich auf
    const link = $("zum-modell");
    if (link && z < 2) link.remove();
    document.body.classList.toggle("z0", z === 0);
    $("s1-offen").hidden = z !== 0;
    $("s1-zu").hidden = z === 0;
    $("s1").classList.toggle("erledigt", z > 0);
    $("kern").hidden = z === 0;
    $("kernsatz").hidden = z === 0;
    $("s2").hidden = z === 0;
    for (const id of ["s3", "s4", "weiter", "modell", "von-vorn-zeile", "regler-bereich"]) $(id).hidden = z < 2;
    if (z === 0) $("legende").hidden = true;
    // 01
    document.querySelectorAll('input[name="tasse"]').forEach(x => { x.checked = S.tasse !== null && x.value === String(S.tasse); });
    document.querySelectorAll('input[name="grund"]').forEach(x => { x.checked = S.grund !== null && x.value === S.grund; });
    $("freitext").value = S.freitext; $("e1").value = S.e1; $("e2").value = S.e2;
    $("s1-knopf").disabled = !(S.tasse !== null && S.grund !== null);
    if (z > 0) {
      const wahl = textOhneTags(T("s1_wahl_" + S.tasse)), grund = textOhneTags(T("s1_grund_" + S.grund));
      let html = F("s1_zus", { wahl: wahl, grund: grund }) + (S.freitext.trim() ? " „" + escape(S.freitext.trim()) + "“" : "");
      const r1 = liesZahl(S.e1), r2 = liesZahl(S.e2);
      if (isFinite(r1) || isFinite(r2)) html += " " + F("s1_zus_rechnung", { e1: isFinite(r1) ? zahl(r1, 2) : "…", e2: isFinite(r2) ? zahl(r2, 2) : "…" });
      $("s1-zusammenfassung").innerHTML = html;
    }
    // 02
    document.querySelectorAll('input[name="warum"]').forEach(x => { x.checked = S.warum !== null && x.value === S.warum; x.disabled = S.warumFest; });
    $("s2-knopf").disabled = S.warum === null || S.warumFest;
    $("s2-knopf").hidden = S.warumFest;
    $("s2-fehlt").hidden = S.warumFest;
    $("s2-rueck").hidden = !S.warumFest;
    $("s2-rueck").innerHTML = S.warumFest ? T("s2_rueck_" + S.warum) + "<p>" + T("s2_weiter") + "</p>" : "";
    // 03
    $("m1").value = S.m1; $("m2").value = S.m2; $("beispiel").checked = S.bsp; $("ln").checked = S.ln; $("ln-hinweis").hidden = !S.ln;
    messInfo();
    // 04
    $("s4-text").value = S.schluss;
    $("s4-knopf").disabled = !S.schluss.trim() || S.schlussGez;
    $("s4-knopf").hidden = S.schlussGez;
    $("s4-fehlt").hidden = S.schlussGez;
    $("s4-rueck").hidden = !S.schlussGez;
    $("s4-rueck").innerHTML = S.schlussGez ? T("s4_gedanken") : "";
    zeigeAuftraege();
  }
  function escape(s) { const d = document.createElement("div"); d.textContent = s; return d.innerHTML; }

  function aktualisiere() {
    const erg = auswerten(S.e);
    if (S.z >= 1) { kern(erg); saeulen(erg); }
    if (S.z >= 2) reglerAnzeigen(erg);
    zeichne(erg);
    zeigeAuftraege();
    speichern();
  }
  function alles() { texteSetzen(); zeigeZustand(); aktualisiere(); }

  // ------------------------------------------------------------ Ereignisse
  function verbinden() {
    $("sprache").addEventListener("click", () => {
      L = L === "de" ? "en" : "de";
      if (speicherOk) { try { localStorage.setItem(SPRACHE, L); } catch (err) { /* nur Arbeitsspeicher */ } }
      alles();
    });
    document.querySelectorAll('input[name="tasse"]').forEach(x => x.addEventListener("change", () => { S.tasse = Number(x.value); zeigeZustand(); speichern(); }));
    document.querySelectorAll('input[name="grund"]').forEach(x => x.addEventListener("change", () => { S.grund = x.value; zeigeZustand(); speichern(); }));
    $("freitext").addEventListener("input", () => { S.freitext = $("freitext").value; speichern(); });
    for (const id of ["e1", "e2"]) $(id).addEventListener("input", () => { S[id] = $(id).value; speichern(); });
    $("s1-knopf").addEventListener("click", () => {
      const falsch = ["e1", "e2"].filter(id => { const s = $(id).value.trim(); const x = liesZahl(s); return s !== "" && !(x >= 0 && x <= 100); });
      ["e1", "e2"].forEach(id => { if (falsch.includes(id)) $(id).setAttribute("aria-invalid", "true"); else $(id).removeAttribute("aria-invalid"); });
      if (falsch.length) { $("e-meldung").textContent = T("s1_feld_falsch"); $(falsch[0]).focus(); return; }
      $("e-meldung").textContent = "";
      S.z = 1;
      alles();
      nachOben();
      $("kern").focus({ preventScroll: true });
      ansage();
    });
    document.querySelectorAll('input[name="warum"]').forEach(x => x.addEventListener("change", () => { S.warum = x.value; zeigeZustand(); speichern(); }));
    $("s2-knopf").addEventListener("click", () => {
      if (S.warum === null) return;
      S.warumFest = true; S.z = 2;
      alles();
      $("s2-rueck").focus();
    });
    for (const nr of [1, 2]) $("m" + nr).addEventListener("input", () => { S["m" + nr] = $("m" + nr).value; messInfo(); aktualisiere(); });
    $("beispiel").addEventListener("change", () => { S.bsp = $("beispiel").checked; aktualisiere(); });
    $("ln").addEventListener("change", () => { S.ln = $("ln").checked; $("ln-hinweis").hidden = !S.ln; aktualisiere(); });
    $("s4-text").addEventListener("input", () => { S.schluss = $("s4-text").value; $("s4-knopf").disabled = !S.schluss.trim(); speichern(); });
    $("s4-knopf").addEventListener("click", () => { if (!S.schluss.trim()) return; S.schlussGez = true; zeigeZustand(); speichern(); $("s4-rueck").focus(); });
    $("knopf-blatt").addEventListener("click", () => { S.e = blatt(); aktualisiere(); ansage(T("status_blatt")); });
    $("von-vorn").addEventListener("click", () => {
      if (!window.confirm(T("von_vorn_frage"))) return;
      S = neu();
      if (speicherOk) { try { localStorage.removeItem(SPEICHER); } catch (err) { /* egal */ } }
      document.querySelectorAll(".auftrag").forEach(d => { d.open = false; });
      $("gruppe").open = false; $("modell").open = false;
      alles();
      window.scrollTo(0, 0);
      $("s1-titel").setAttribute("tabindex", "-1"); $("s1-titel").focus();
    });
    let warten = 0;
    window.addEventListener("resize", () => { cancelAnimationFrame(warten); warten = requestAnimationFrame(() => zeichne(auswerten(S.e))); });
    $("gruppe").addEventListener("toggle", () => zeichne(auswerten(S.e)));
    document.addEventListener("click", ev => { if (ev.target.closest && ev.target.closest("#zum-modell")) $("modell").open = true; });
  }
  function nachOben() {
    if (window.innerWidth >= 1024) window.scrollTo(0, Math.max(0, document.querySelector(".raster").getBoundingClientRect().top + window.scrollY - 10));
    else $("buehne").scrollIntoView({ block: "start" });
  }

  // ------------------------------------------------------------ Start
  laden();
  reglerBauen();
  auftraegeBauen();
  verbinden();
  alles();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => zeichne(auswerten(S.e)));
  window.KAFFEE = { auswerten: auswerten, STANDARD: STANDARD, BEISPIEL: BEISPIEL, KA_BLATT: KA_BLATT, zustand: () => JSON.parse(JSON.stringify(S)) };
})();
