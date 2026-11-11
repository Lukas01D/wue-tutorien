// Schlanke Kaffee-Simulation (Auftrag der TL vom 11.11.2026): Kasten mit den Endwerten, Diagramm, Säulen der an den Raum
// abgegebenen Wärme, Zeitregler mit „Abspielen“ und die Regler der Hauptseite. Keine Fragen, keine Aufträge.
// Die Bausteine mit „// aus oberflaeche.js“ setzt bauen_minimal.py unverändert aus simulation/site/src/oberflaeche.js ein,
// damit Regler, Diagramm, Kasten und Säulen genau so aussehen und rechnen wie auf der Hauptseite.
(function () {
  "use strict";
  const SVGNS = "http://www.w3.org/2000/svg";
  const $ = id => document.getElementById(id);
  const KA_BLATT = kABlatt();
  const TOLERANZ_RECHNUNG = 0.1;
  //@@REGLER@@
  const blatt = () => ({ thM: STANDARD.thM, tZ: STANDARD.tZ, thK0: STANDARD.thK0, thU: STANDARD.thU, kA: KA_BLATT, VM_ml: STANDARD.VM_ml });
  // Zustand in der Form der Hauptseite (Zustand 2: alles erklärt, Milch ohne 30-°C-Sperre, keine Messung, keine eigene Rechnung)
  const S = { z: 2, e: blatt(), e1: "", e2: "", warumFest: true, bsp: false, ln: false, m1: "", m2: "", a: { 3: { fest: true } } };
  let L = new URLSearchParams(location.search).get("lang") === "en" ? "en" : "de";
  let tJetzt = S.e.tZ;     // angezeigter Zeitpunkt in min (0 bis Zugabe)
  let lauf = 0;            // laufende Wiedergabe (requestAnimationFrame), 0 = keine
  let ansageTimer = 0;
  let tZalt = S.e.tZ;

  //@@BAUSTEINE@@

  // ------------------------------------------------------------ Ergänzungen der schlanken Seite
  function obergrenze(r) { return r.max; }
  function messungen() { return { t1: [], t2: [], f1: null, f2: null }; }
  function zeichneLn() { /* auf der schlanken Seite nicht vorhanden */ }
  function diagrammHoehe(svg, W) {
    if (window.innerWidth < 1024) return Math.round(Math.min(360, W * (W < 500 ? 0.82 : 0.68)));
    return Math.round(Math.max(260, Math.min(W * 0.5, window.innerHeight - 330)));
  }
  // Zeitpunkt im Diagramm: Teil nach tJetzt verdeckt, Linie und Punkte bei tJetzt (gleiche Achsen wie zeichne)
  function zeitDarstellen(erg) {
    const e = S.e;
    if (tJetzt >= e.tZ - 1e-9) return;
    const svg = $("dia"), vb = svg.getAttribute("viewBox").split(" ").map(Number), W = vb[2], H = vb[3];
    const xmax = Math.max(60, Math.ceil(e.tZ / 10) * 10);
    const ymax = Math.max(90, Math.ceil((Math.max(e.thK0, erg.th10, erg.th2) + 3) / 10) * 10);
    const ymin = Math.min(10, Math.floor((e.thU - 5) / 10) * 10);
    const Lr = 46, R = 24, Tr = 12, B = 38, P = 12;
    const X = t => Lr + P + (W - Lr - P - R) * t / xmax, Y = v => Tr + (H - Tr - B) * (ymax - v) / (ymax - ymin);
    const x = X(tJetzt);
    svg.appendChild(el("rect", { x: x + 1, y: Y(ymax) - 2, width: Math.max(0, X(xmax) + R - x - 1), height: Y(ymin) - Y(ymax) + 2, class: "zukunft" }));
    svg.appendChild(el("line", { x1: x, x2: x, y1: Y(ymin), y2: Y(ymax), class: "jetzt" }));
    svg.appendChild(el("circle", { cx: x, cy: Y(erg.kurve1(tJetzt * 60)), r: 5, class: "punkt k1" }));
    svg.appendChild(el("circle", { cx: x, cy: Y(erg.kurve2(tJetzt * 60)), r: 5, class: "punkt k2" }));
  }
  // Säulen bis tJetzt, Maßstab aus den Werten bei der Zugabe (so wachsen sie sichtbar)
  function saeulenBis(erg) {
    const t = Math.min(tJetzt, S.e.tZ) * 60;
    const q = Object.assign({}, erg, { Q1: erg.C_G * (erg.th10 - erg.kurve1(t)), Q2: erg.C_K * (S.e.thK0 - erg.kurve2(t)), Q1max: erg.Q1, Q2max: erg.Q2 });
    saeulen(q);
    $("saeulen-titel").innerHTML = tJetzt >= S.e.tZ - 1e-9 ? T("s2_saeulen") : F("schlank_saeulen_t", { t: zahl(tJetzt, 1) });
  }
  // Zeitregler: gleicher Aufbau wie die übrigen Regler
  const ZR = { id: "t", min: 0, schritt: 0.5, stellen: 1 };
  function zeitSetzen(x) {
    if (!isFinite(x)) return;
    tJetzt = Math.min(S.e.tZ, Math.max(0, x));
    zeigen();
  }
  function zeitAnzeigen() {
    const ein = $("rr-t"), max = S.e.tZ;
    ein.max = max; ein.value = tJetzt;
    ein.setAttribute("aria-valuetext", zahl(tJetzt, 1) + " min");
    const feld = $("rf-t");
    if (document.activeElement !== feld) feld.value = zahl(tJetzt, 1);
    const sk = $("rs-t");
    sk.textContent = "";
    const schritt = max > 90 ? 30 : (max > 30 ? 15 : 5);
    const marken = [];
    for (let m = 0; m < max - schritt / 3; m += schritt) marken.push(m);
    marken.push(max);
    for (const m of marken) {
      const sp = document.createElement("span");
      sp.textContent = zahl(m, 0);
      sp.style.left = (100 * m / max).toFixed(2) + "%";
      sk.appendChild(sp);
    }
    $("rminus-t").disabled = tJetzt <= 0;
    $("rplus-t").disabled = tJetzt >= max;
  }
  function zeitBauen() {
    $("rr-t").addEventListener("input", () => { anhalten(); zeitSetzen(Number($("rr-t").value)); });
    $("rminus-t").addEventListener("click", () => { anhalten(); zeitSetzen(tJetzt - 1); });
    $("rplus-t").addEventListener("click", () => { anhalten(); zeitSetzen(tJetzt + 1); });
    const ausFeld = () => { const x = liesZahl($("rf-t").value); if (x >= 0 && x <= S.e.tZ) { anhalten(); zeitSetzen(x); } else $("rf-t").value = zahl(tJetzt, 1); };
    $("rf-t").addEventListener("change", ausFeld);
    $("rf-t").addEventListener("keydown", ev => { if (ev.key === "Enter") { ev.preventDefault(); ausFeld(); } });
    $("abspielen").addEventListener("click", () => {
      if (lauf) { anhalten(); return; }
      if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) { zeitSetzen(S.e.tZ); return; }
      const start = performance.now(), t0 = tJetzt >= S.e.tZ - 1e-9 ? 0 : tJetzt, dauer = 6000 * (S.e.tZ - t0) / S.e.tZ;
      zeitSetzen(t0);
      lauf = 1;
      $("abspielen").textContent = T("schlank_anhalten");
      const schritt = jetzt => {
        if (!lauf) return;
        zeitSetzen(t0 + (S.e.tZ - t0) * Math.min(1, (jetzt - start) / Math.max(dauer, 1)));
        if (tJetzt < S.e.tZ) lauf = requestAnimationFrame(schritt); else anhalten();
      };
      lauf = requestAnimationFrame(schritt);
    });
  }
  function anhalten() {
    if (lauf) cancelAnimationFrame(lauf);
    lauf = 0;
    $("abspielen").textContent = T("schlank_abspielen");
  }

  function texteSetzen() {
    document.documentElement.lang = L;
    document.title = T("titel_seite");
    document.querySelectorAll("[data-t]").forEach(x => { x.innerHTML = T(x.dataset.t); });
    $("sprache").setAttribute("aria-label", T("sprache_knopf_aria"));
    for (const r of REGLER) reglerTexte(r);
    $("rn-t").innerHTML = T("schlank_zeit") + ' <span class="einheit">[min]</span>';
    $("rminus-t").setAttribute("aria-label", T("r_minus") + ": " + textOhneTags(T("schlank_zeit")));
    $("rplus-t").setAttribute("aria-label", T("r_plus") + ": " + textOhneTags(T("schlank_zeit")));
    $("rf-t").setAttribute("aria-label", F("r_feld_aria", { name: textOhneTags(T("schlank_zeit")), einheit: "min" }));
    $("abspielen").textContent = T(lauf ? "schlank_anhalten" : "schlank_abspielen");
    $("fuss-text").textContent = F("fuss", { stand: BAU.stand, version: BAU.version });
  }
  function zeigen() {
    const erg = auswerten(S.e);
    zeichne(erg);
    zeitDarstellen(erg);
    saeulenBis(erg);
    zeitAnzeigen();
  }
  function aktualisiere() {                // nach jeder Änderung eines Reglers (von setze aufgerufen)
    const erg = auswerten(S.e);
    tJetzt = tJetzt >= tZalt - 1e-9 ? S.e.tZ : Math.min(tJetzt, S.e.tZ);   // am Ende bleibt am Ende, sonst bleibt der Zeitpunkt
    tZalt = S.e.tZ;
    kern(erg);
    reglerAnzeigen(erg);
    zeigen();
  }
  function alles() { texteSetzen(); aktualisiere(); }

  reglerBauen();
  zeitBauen();
  $("sprache").addEventListener("click", () => { L = L === "de" ? "en" : "de"; alles(); });
  $("knopf-blatt").addEventListener("click", () => { anhalten(); S.e = blatt(); tJetzt = S.e.tZ; aktualisiere(); ansage(T("status_blatt")); });
  let warten = 0;
  window.addEventListener("resize", () => { cancelAnimationFrame(warten); warten = requestAnimationFrame(zeigen); });
  $("gruppe").addEventListener("toggle", zeigen);
  alles();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(zeigen);
})();
