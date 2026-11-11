// Kaffee-Simulation, schlanke Varianten (Auftrag der TL vom 11.11.2026): nur Diagramm, Säulen der an den Raum abgegebenen
// Wärme und Regler, keine Fragen. A: Säulen zeigen den Stand bei der Zugabe. B: dazu ein Zeitregler, Kurven und Säulen
// wachsen gemeinsam bis zur Zugabe. Rechenkern: modell.js der Hauptseite (unverändert eingebunden).
(function () {
  "use strict";
  const SVGNS = "http://www.w3.org/2000/svg";
  const $ = id => document.getElementById(id);
  const KA_BLATT = kABlatt();
  const REGLER = [
    { id: "thM", t: "Milchtemperatur", e: "°C", min: 2, max: 95, s: 0.5, n: 1 },
    { id: "VM_ml", t: "Milchmenge", e: "ml", min: 10, max: 200, s: 5, n: 0 },
    { id: "tZ", t: "Milch in Tasse 2 nach", e: "min", min: 1, max: 180, s: 1, n: 0 },
    { id: "thK0", t: "Kaffeetemperatur am Anfang", e: "°C", min: 60, max: 95, s: 0.5, n: 1 },
    { id: "thU", t: "Raumtemperatur", e: "°C", min: 10, max: 30, s: 0.5, n: 1 },
    { id: "kA", t: "kA der Tasse", e: "W/K", min: 0.05, max: 0.8, s: 0.005, n: 4 }
  ];
  const blatt = () => ({ thM: STANDARD.thM, tZ: STANDARD.tZ, thK0: STANDARD.thK0, thU: STANDARD.thU, kA: KA_BLATT, VM_ml: STANDARD.VM_ml });
  let E = blatt();
  let tJetzt = E.tZ;          // Variante B: angezeigter Zeitpunkt in min (0 bis Zugabe)
  let lauf = 0;               // laufende Animation (requestAnimationFrame), 0 = keine

  function zahl(x, n) {
    let s = Number(x).toFixed(n);
    if (/^-0(\.0+)?$/.test(s)) s = s.slice(1);
    if (s.startsWith("-")) s = "−" + s.slice(1);
    return s.replace(".", ",");
  }
  function el(name, attr, text) {
    const x = document.createElementNS(SVGNS, name);
    for (const k in attr) x.setAttribute(k, attr[k]);
    if (text !== undefined) x.textContent = text;
    return x;
  }
  const schritt = m => [1, 2, 2.5, 5, 10, 20, 25, 50].map(f => f * Math.pow(10, Math.floor(Math.log10(m)) - 1)).find(f => m / f <= 6) || m;

  // ------------------------------------------------------------ Regler
  function reglerBauen() {
    const r0 = $("regler");
    for (const r of REGLER) {
      const d = document.createElement("div");
      d.className = "regler";
      d.innerHTML = '<label for="r-' + r.id + '">' + r.t + '</label><output id="o-' + r.id + '" for="r-' + r.id + '"></output>' +
        '<input type="range" id="r-' + r.id + '" min="' + r.min + '" max="' + r.max + '" step="' + r.s + '">';
      r0.appendChild(d);
      $("r-" + r.id).addEventListener("input", ev => {
        E[r.id] = Number(ev.target.value);
        if (r.id === "tZ") tJetzt = E.tZ;
        anhalten();
        alles();
      });
    }
    $("blatt").addEventListener("click", () => { E = blatt(); tJetzt = E.tZ; anhalten(); alles(); });
  }
  function reglerAnzeigen() {
    for (const r of REGLER) {
      const ein = $("r-" + r.id), v = E[r.id], txt = zahl(v, r.n) + " " + r.e;
      if (Number(ein.value) !== v) ein.value = v;
      ein.setAttribute("aria-valuetext", txt);
      $("o-" + r.id).textContent = txt;
    }
  }

  // ------------------------------------------------------------ Variante B: Zeit
  function zeitBauen() {
    $("zeit-bereich").hidden = false;
    $("zeit").addEventListener("input", ev => { anhalten(); tJetzt = Number(ev.target.value); alles(); });
    $("abspielen").addEventListener("click", () => {
      if (lauf) { anhalten(); return; }
      if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) { tJetzt = E.tZ; alles(); return; }
      const dauer = 6000, start = performance.now(), t0 = tJetzt >= E.tZ ? 0 : tJetzt;
      $("abspielen").textContent = "Anhalten";
      const schrittB = jetzt => {
        tJetzt = Math.min(E.tZ, t0 + (E.tZ - t0) * (jetzt - start) / (dauer * (E.tZ - t0) / E.tZ || 1));
        alles();
        if (tJetzt < E.tZ) lauf = requestAnimationFrame(schrittB); else anhalten();
      };
      lauf = requestAnimationFrame(schrittB);
    });
  }
  function anhalten() {
    if (lauf) cancelAnimationFrame(lauf);
    lauf = 0;
    if (VARIANTE === "B") $("abspielen").textContent = "Abspielen";
  }

  // ------------------------------------------------------------ Diagramm
  function diagramm(erg, tBis) {
    const svg = $("dia");
    svg.textContent = "";
    const W = Math.max(280, svg.clientWidth || 600);
    const H = Math.round(W < 500 ? W * 0.8 : Math.min(W * 0.5, 400));
    svg.setAttribute("viewBox", "0 0 " + W + " " + H);
    svg.setAttribute("height", H);
    const fs = W < 500 ? 12 : 13, dick = W >= 600 ? 3 : 2.5;
    const xmax = Math.max(60, Math.ceil(E.tZ / 10) * 10);
    const ymin = Math.min(10, Math.floor((E.thU - 5) / 10) * 10);
    const ymax = Math.max(90, Math.ceil((Math.max(E.thK0, erg.th10, erg.th2) + 3) / 10) * 10);
    const Lr = 46, R = 16, Tr = 10, B = 38, P = 12;
    const X = t => Lr + P + (W - Lr - P - R) * t / xmax, Y = v => Tr + (H - Tr - B) * (ymax - v) / (ymax - ymin);
    const xs = schritt(xmax);
    for (let t = 0; t <= xmax + 1e-9; t += xs / 2) svg.appendChild(el("line", { x1: X(t), x2: X(t), y1: Y(ymin), y2: Y(ymax), class: Math.abs(t / xs - Math.round(t / xs)) < 1e-9 ? "gitter-haupt" : "gitter" }));
    for (let v = ymin; v <= ymax; v += 5) svg.appendChild(el("line", { x1: Lr, x2: X(xmax), y1: Y(v), y2: Y(v), class: v % 10 ? "gitter" : "gitter-haupt" }));
    svg.appendChild(el("line", { x1: Lr, x2: X(xmax), y1: Y(ymin), y2: Y(ymin), class: "achse" }));
    svg.appendChild(el("line", { x1: Lr, x2: Lr, y1: Y(ymin), y2: Y(ymax), class: "achse" }));
    for (let v = ymin; v <= ymax; v += 20) svg.appendChild(el("text", { x: Lr - 6, y: Y(v) + 4, "text-anchor": "end", "font-size": fs, class: "ax" }, String(v)));
    for (let t = 0; t <= xmax + 1e-9; t += xs) svg.appendChild(el("text", { x: X(t), y: Y(ymin) + 16, "text-anchor": "middle", "font-size": fs, class: "ax" }, String(t)));
    svg.appendChild(el("text", { x: (X(0) + X(xmax)) / 2, y: H - 4, "text-anchor": "middle", "font-size": fs, class: "beschr" }, "Zeit t [min]"));
    const ym = (Y(ymin) + Y(ymax)) / 2;
    svg.appendChild(el("text", { x: 12, y: ym, "text-anchor": "middle", "font-size": fs, class: "beschr", transform: "rotate(-90 12 " + ym + ")" }, "Temperatur ϑ [°C]"));
    svg.appendChild(el("line", { x1: Lr, x2: X(xmax), y1: Y(E.thU), y2: Y(E.thU), class: "raum" }));
    svg.appendChild(el("text", { x: X(xmax) - 2, y: Y(E.thU) - 5, "text-anchor": "end", "font-size": fs, class: "raum-text" }, "Raum " + zahl(E.thU, 1) + " °C"));

    // Kurven bis zur Zugabe; in B der Teil nach tBis blass
    const n = 160, punkte = (k, von, bis) => { const p = []; for (let i = 0; i <= n; i++) { const t = von + (bis - von) * i / n; p.push(X(t).toFixed(1) + "," + Y(k(t * 60)).toFixed(1)); } return p.join(" "); };
    const teile = [[erg.kurve1, E.tZ, "kurve k1"], [erg.kurve2, E.tZ, "kurve k2 gestrichelt"]];
    for (const [k, ende, kl] of teile) {
      const b = Math.min(ende, tBis);
      if (b < ende) svg.appendChild(el("polyline", { points: punkte(k, b, ende), class: kl + " blass", "stroke-width": dick }));
      if (b > 0) svg.appendChild(el("polyline", { points: punkte(k, 0, b), class: kl, "stroke-width": dick }));
    }
    // Sprung durch die Milch (Tasse 1 bei t = 0, Tasse 2 bei der Zugabe), Richtung nach dem Vorzeichen
    const sprung = (t, o, u, k, luecke, blass) => {
      const r = Y(u) >= Y(o) ? 1 : -1, x = X(t), y1 = Y(o), y2 = Y(u) - r * luecke, lang = r * (y2 - y1);
      if (!(lang > 2)) return;
      const sp = Math.min(W >= 600 ? 9 : 7, lang / 2), g = el("g", blass ? { class: "blass" } : {});
      g.appendChild(el("line", { x1: x, x2: x, y1: y1, y2: y2 - r * sp, class: "abfall " + k, "stroke-width": dick }));
      g.appendChild(el("polygon", { points: [[x - sp * 0.7, y2 - r * sp], [x + sp * 0.7, y2 - r * sp], [x, y2]].map(q => q[0].toFixed(1) + "," + q[1].toFixed(1)).join(" "), class: "pfeil " + k }));
      if (lang > 2.2 * fs && !blass) g.appendChild(el("text", { x: x + 8, y: (r < 0 || t === 0 ? (y1 + y2) / 2 + fs * 0.35 : y1 + fs * 1.1), "font-size": fs, class: "kbeschr " + k + "-text" }, "Milch"));
      svg.appendChild(g);
    };
    const zugegeben = tBis >= E.tZ - 1e-9;
    sprung(0, E.thK0, erg.th10, "k1", 0, false);
    svg.appendChild(el("circle", { cx: X(E.tZ), cy: Y(erg.th1), r: 4.5, class: "ende k1" + (zugegeben ? "" : " blass") }));
    sprung(E.tZ, erg.th2K, erg.th2, "k2", 6, !zugegeben);
    if (zugegeben) svg.appendChild(el("circle", { cx: X(E.tZ), cy: Y(erg.th2), r: 4.5, class: "ende k2" }));
    // Zeitpunkt (nur B, vor der Zugabe)
    if (VARIANTE === "B" && !zugegeben) {
      svg.appendChild(el("line", { x1: X(tBis), x2: X(tBis), y1: Y(ymin), y2: Y(ymax), class: "jetzt" }));
      svg.appendChild(el("circle", { cx: X(tBis), cy: Y(erg.kurve1(tBis * 60)), r: 5, class: "punkt k1" }));
      svg.appendChild(el("circle", { cx: X(tBis), cy: Y(erg.kurve2(tBis * 60)), r: 5, class: "punkt k2" }));
    }
    // Beschriftung der Kurven: oberhalb, wenn die Kurve dort die obere ist, sonst unterhalb
    for (const [txt, k, anders, f] of [["Tasse 2: Milch nach " + zahl(E.tZ, 0) + " min", erg.kurve2, erg.kurve1, 0.1], ["Tasse 1: Milch sofort", erg.kurve1, erg.kurve2, 0.55]]) {
      const t = E.tZ * f, w = txt.length * fs * 0.56, oben = k(t * 60) >= anders(t * 60);
      const x = Math.max(Lr + 4, Math.min(X(t), X(E.tZ) - 10 - w, W - R - w));
      const tx = Math.max(0, (x - Lr - P) / (W - Lr - P - R) * xmax), tm = oben ? tx : Math.min(E.tZ, tx + w / (W - Lr - P - R) * xmax);
      const y = oben ? Y(k(tx * 60)) - 10 : Y(k(tm * 60)) + 20;
      svg.appendChild(el("text", { x: x, y: y, "font-size": fs, class: "kbeschr " + (k === erg.kurve1 ? "k1-text" : "k2-text") }, txt));
    }
    return H;
  }

  // ------------------------------------------------------------ Säulen
  function saeulen(erg, tBis, hoehe) {
    const svg = $("q");
    svg.textContent = "";
    const W = Math.max(200, svg.clientWidth || 228), H = Math.max(190, hoehe);
    svg.setAttribute("viewBox", "0 0 " + W + " " + H);
    svg.setAttribute("height", H);
    const q = t => [erg.C_G * (erg.th10 - erg.kurve1(t * 60)) / 1000, erg.C_K * (E.thK0 - erg.kurve2(t * 60)) / 1000];
    const [q1, q2] = q(tBis), [e1, e2] = q(E.tZ);
    const st = schritt(Math.max(e1, e2, 0.1)), qmax = Math.ceil(Math.max(e1, e2, 0.1) / st) * st;
    const qmin = Math.min(0, Math.floor(Math.min(e1, e2, 0) / st) * st);
    const L = 40, top = 22, unten = H - 48, Yq = v => unten - (unten - top) * (v - qmin) / (qmax - qmin);
    const defs = el("defs", {}), pat = el("pattern", { id: "schraffur", width: 6, height: 6, patternUnits: "userSpaceOnUse", patternTransform: "rotate(45)" });
    pat.appendChild(el("rect", { width: 6, height: 6, class: "schraffur-grund" }));
    pat.appendChild(el("line", { x1: 0, y1: 0, x2: 0, y2: 6, class: "schraffur-linie" }));
    defs.appendChild(pat); svg.appendChild(defs);
    for (let v = qmin; v <= qmax + 1e-9; v += st) {
      svg.appendChild(el("line", { x1: L, x2: W - 6, y1: Yq(v), y2: Yq(v), class: "gitter-haupt" }));
      svg.appendChild(el("text", { x: L - 6, y: Yq(v) + 4, "text-anchor": "end", "font-size": 12, class: "ax" }, zahl(v, st < 1 ? 1 : 0)));
    }
    svg.appendChild(el("text", { x: L - 6, y: top - 10, "text-anchor": "end", "font-size": 12, class: "ax" }, "kJ"));
    svg.appendChild(el("line", { x1: L, x2: W - 6, y1: Yq(0), y2: Yq(0), class: "achse" }));
    const bw = Math.min(56, (W - L - 30) / 3), x1 = L + (W - L) * 0.28 - bw / 2, x2 = L + (W - L) * 0.68 - bw / 2;
    for (const [x, v, kl, name, ktext] of [[x1, q1, "saeule1", "Tasse 1", "k1-text"], [x2, q2, "saeule2", "Tasse 2", "k2-text"]]) {
      const y0 = Yq(Math.max(v, 0)), y1 = Yq(Math.min(v, 0));
      svg.appendChild(el("rect", { x: x, y: y0, width: bw, height: Math.max(0, y1 - y0), class: kl }));
      svg.appendChild(el("text", { x: x + bw / 2, y: y0 - 6, "text-anchor": "middle", "font-size": 13, class: "zahl" }, zahl(v, 2)));
      svg.appendChild(el("text", { x: x + bw / 2, y: unten + 18, "text-anchor": "middle", "font-size": 13, class: "kbeschr " + ktext }, name));
    }
    svg.appendChild(el("text", { x: L + (W - L) / 2, y: H - 6, "text-anchor": "middle", "font-size": 13, class: "diff zahl" }, "Q₂ − Q₁ = " + zahl(q2 - q1, 2) + " kJ"));
    $("q-bis").textContent = VARIANTE === "B" && tBis < E.tZ ? "bis t = " + zahl(tBis, 1) + " min" : "bis zur Zugabe (" + zahl(E.tZ, 0) + " min)";
    $("q-text").textContent = "Säulen: an den Raum abgegebene Wärme " + $("q-bis").textContent + ", Tasse 1 " + zahl(q1, 2) + " kJ, Tasse 2 " + zahl(q2, 2) + " kJ.";
  }

  // ------------------------------------------------------------ Texte
  function texte(erg) {
    $("lage").textContent = "Zwei gleiche Tassen mit Deckel, je " + zahl(STANDARD.VK_ml, 0) + " ml Kaffee mit " + zahl(E.thK0, 1) + " °C, Raum " + zahl(E.thU, 1) +
      " °C. Tasse 1 bekommt " + zahl(E.VM_ml, 0) + " ml Milch mit " + zahl(E.thM, 1) + " °C sofort, Tasse 2 erst nach " + zahl(E.tZ, 0) + " min.";
    const d = erg.dT, wer = Math.abs(d) < 0.005 ? "Beide sind gleich warm." : (d > 0 ? "Tasse 1 ist " : "Tasse 2 ist ") + "<b>" + zahl(Math.abs(d), 2) + " K</b> wärmer.";
    $("ergebnis").innerHTML = "Nach " + zahl(E.tZ, 0) + " min: Tasse 1 <b>" + zahl(erg.th1, 2) + " °C</b>, Tasse 2 <b>" + zahl(erg.th2, 2) + " °C</b>. " + wer;
    const v1 = erg.th10 > E.thK0 ? "steigt" : "fällt", v2 = erg.th2 > erg.th2K ? "steigt" : "fällt";
    $("dia-text").textContent = "Diagramm: Beide Tassen beginnen mit Kaffee bei " + zahl(E.thK0, 1) + " °C. Tasse 1 " + v1 + " durch die Milch sofort auf " + zahl(erg.th10, 1) +
      " °C und kühlt dann auf " + zahl(erg.th1, 1) + " °C ab. Tasse 2 kühlt auf " + zahl(erg.th2K, 1) + " °C ab und " + v2 + " nach " + zahl(E.tZ, 0) + " min durch die Milch auf " + zahl(erg.th2, 1) + " °C.";
    $("fuss").textContent = "Berechnet, nicht gemessen (Modell wie im Blatt, Werte vorläufig bis zur Messung). Variante " + VARIANTE + " · Stand " + BAU.stand + " · Version " + BAU.version;
  }

  function alles() {
    const erg = auswerten(E);
    const tBis = VARIANTE === "B" ? Math.min(tJetzt, E.tZ) : E.tZ;
    reglerAnzeigen();
    if (VARIANTE === "B") {
      const z = $("zeit");
      z.max = E.tZ;
      if (Number(z.value) !== tBis) z.value = tBis;
      $("zeit-wert").textContent = zahl(tBis, 1) + " min";
      z.setAttribute("aria-valuetext", zahl(tBis, 1) + " min");
    }
    const h = diagramm(erg, tBis);
    saeulen(erg, tBis, window.innerWidth >= 760 ? h - 28 : 180);
    texte(erg);
  }

  reglerBauen();
  if (VARIANTE === "B") zeitBauen();
  let warte = 0;
  window.addEventListener("resize", () => { cancelAnimationFrame(warte); warte = requestAnimationFrame(alles); });
  alles();
})();
