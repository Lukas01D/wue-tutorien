// OBERFLAECHE: Zustand, Pflichtweg mit Sperre (ZUSTAENDE.md), Diagramm, Regler, Rechenwerte, Messblatt, Kurslink, Reiter, Sprache.
// Bekommt vom Bau: TEXTE (de, en; Formeln schon als MathML), REGLER_DEF (regler.json mit MathML), BAU (Stand, Version).
(() => {
  "use strict";
  const $ = id => document.getElementById(id);
  const SPEICHER = "kaffee-sim-v2-";
  const N_ABTAST = 241;
  const FRAGEN = [
    { id: "start", titel: "start_titel", text: "start_text", wahl: ["1", "2", "gleich"], wahlText: { "1": "start_opt_1", "2": "start_opt_2", gleich: "start_opt_gleich" }, richtig: "1",
      zahl: { label: "start_k_label", einheit: "K", stellen: 1 }, aufl: "aufl_start", ausgang: "start_ausgangslage", setze: "standard" },
    { id: "f1", titel: "f1_titel", text: "f1_text", zahl: { label: "f1_eingabe", einheit: "min", stellen: 0, pflicht: true }, aufl: "aufl_f1", ausgang: "f1_ausgangslage", setze: "standard" },
    { id: "f2", titel: "f2_titel", text: "f2_text", wahl: ["ueber", "unter", "auf", "wechselnd"], wahlText: { ueber: "f2_opt_ueber", unter: "f2_opt_unter", auf: "f2_opt_auf", wechselnd: "f2_opt_wechselnd" },
      richtig: null, aufl: "aufl_f2", ausgang: "f2_ausgangslage", setze: "kurs" },
    { id: "v1", titel: "v1_titel", text: "v1_text", zahl: { label: "v1_eingabe", einheit: "°C", stellen: 1, pflicht: true }, aufl: "aufl_v1", ausgang: "start_ausgangslage", setze: "standard" },
    { id: "v2", titel: "v2_titel", text: "v2_text", wahl: ["groesser", "kleiner", "gleich"], wahlText: { groesser: "v_opt_groesser", kleiner: "v_opt_kleiner", gleich: "v_opt_gleich" }, richtig: "gleich",
      zahl: { label: "v2_eingabe", einheit: "min", stellen: 0 }, aufl: "aufl_v2", ausgang: "start_ausgangslage", setze: "standard" },
    { id: "v3", titel: "v3_titel", text: "v3_text", wahl: ["groesser", "kleiner"], wahlText: { groesser: "v_opt_groesser", kleiner: "v_opt_kleiner" }, richtig: "kleiner",
      aufl: "aufl_v3", ausgang: "v3_ausgangslage", setze: "becher" },
    { id: "v4", titel: "v4_titel", text: "v4_text", wahl: ["ungleich", "falsch"], wahlText: { ungleich: "v4_opt_ungleich", falsch: "v4_opt_falsch" }, richtig: "ungleich",
      aufl: "aufl_v4", ausgang: "start_ausgangslage", setze: "standard" },
    { id: "v5", titel: "v5_titel", text: "v5_text", wahl: ERW.VOREINSTELLUNGEN.map(v => v.id), wahlText: Object.fromEntries(ERW.VOREINSTELLUNGEN.map(v => [v.id, "vor_" + v.id])), richtig: "thermo_offen",
      aufl: "aufl_v5", ausgang: "start_ausgangslage", setze: "standard" }
  ];
  const PFLICHT = ["start", "f1", "f2"];
  const REG = Object.fromEntries(REGLER_DEF.regler.map(r => [r.id, r]));

  // ------------------------------------------------------------------ Zustand und Speicher
  function standardE() {
    const e = { kAQuelle: "fest", kA: ERW.KA_AUFGABE, kAHerkunft: "aufgabe", milch2Raum: false, becher: false };
    for (const r of REGLER_DEF.regler) if (r.standard !== null) e[r.key] = r.faktor ? r.standard / r.faktor : r.standard;
    return e;
  }
  function leereAntworten() { return Object.fromEntries(FRAGEN.map(f => [f.id, { wahl: null, zahl: "", warum: "", fest: false, ohne: false, aufl: false }])); }
  function leererKurs() { return { v: 1, u: null, m: null, d: false, b3: false, werte: { b1: Array(8).fill(null), b2: Array(8).fill(null), b3: Array(8).fill(null) } }; }
  let speicherOk = true;
  function lies(k) { try { return JSON.parse(localStorage.getItem(SPEICHER + k)); } catch (e) { speicherOk = false; return null; } }
  function schreib(k, v) { try { localStorage.setItem(SPEICHER + k, JSON.stringify(v)); } catch (e) { if (speicherOk) { speicherOk = false; const h = document.getElementById("speicher-hinweis"); if (h) { h.innerHTML = t("speicher_aus"); h.classList.add("aus"); } } } }
  try { localStorage.setItem(SPEICHER + "probe", "1"); localStorage.removeItem(SPEICHER + "probe"); } catch (e) { speicherOk = false; }
  const S = {
    sprache: "de", e: standardE(), antworten: leereAntworten(), aktuell: "start", kurs: leererKurs(),
    ansicht: { reiter: "versuche", vertiefung: false, diagramm: "temperatur", anheften: true }, vergleich: null, f2Uebersprungen: false
  };
  const zahlOk = x => typeof x === "number" && isFinite(x);
  function laden() {
    const a = lies("antworten"), e = lies("einstellungen"), k = lies("kurswerte"), v = lies("ansicht");
    S.antworten = leereAntworten(); S.aktuell = "start"; S.f2Uebersprungen = false; S.e = standardE(); S.kurs = leererKurs();
    try {
      if (a && a.antworten && typeof a.antworten === "object") {
        for (const f of FRAGEN) {
          const q = a.antworten[f.id]; if (!q || typeof q !== "object") continue;
          const z0 = S.antworten[f.id];
          if (typeof q.wahl === "string" && f.wahl && f.wahl.indexOf(q.wahl) >= 0) z0.wahl = q.wahl;
          if (typeof q.zahl === "string") z0.zahl = q.zahl.slice(0, 40);
          if (typeof q.warum === "string") z0.warum = q.warum.slice(0, 400);
          for (const b of ["fest", "ohne", "aufl"]) z0[b] = q[b] === true;
        }
        if (FRAGEN.some(f => f.id === a.aktuell)) S.aktuell = a.aktuell;
        S.f2Uebersprungen = a.f2Uebersprungen === true;
      }
    } catch (x) { S.antworten = leereAntworten(); S.aktuell = "start"; }
    try {
      if (e && typeof e === "object") {
        const neu = standardE();
        for (const r of REGLER_DEF.regler) { const w = e[r.key]; if (zahlOk(w)) { const wa = r.faktor ? w * r.faktor : w; if (wa >= r.min && wa <= r.max) neu[r.key] = w; } }
        if (zahlOk(e.kA) && e.kA > 0 && e.kA <= 5) neu.kA = e.kA;
        if (e.kAQuelle === "fest" || e.kAQuelle === "messung") neu.kAQuelle = e.kAQuelle;
        if (typeof e.kAHerkunft === "string") neu.kAHerkunft = e.kAHerkunft.slice(0, 40);
        for (const b of ["milch2Raum", "becher"]) neu[b] = e[b] === true;
        S.e = neu;
      }
    } catch (x) { S.e = standardE(); }
    try {
      if (k && k.werte) {
        const neu = leererKurs();
        for (const b of ["b1", "b2", "b3"]) if (Array.isArray(k.werte[b]) && k.werte[b].length === 8) neu.werte[b] = k.werte[b].map(x => zahlOk(x) && x >= 0 && x <= 100 ? x : null);
        neu.werte.b1[7] = null;
        if (zahlOk(k.u) && k.u >= 5 && k.u <= 40) neu.u = k.u;
        if (zahlOk(k.m) && k.m >= 0 && k.m <= 70) neu.m = k.m;
        neu.d = k.d === true; neu.b3 = k.b3 === true;
        S.kurs = neu;
      }
    } catch (x) { S.kurs = leererKurs(); }
    try {
      if (v && typeof v === "object" && v.ansicht && typeof v.ansicht === "object") {
        const w = v.ansicht;
        if (["versuche", "modell", "code"].indexOf(w.reiter) >= 0) S.ansicht.reiter = w.reiter;
        if (["temperatur", "waermestrom", "ln"].indexOf(w.diagramm) >= 0) S.ansicht.diagramm = w.diagramm;
        for (const b of ["vertiefung", "anheften", "trinkzeit", "kalt"]) if (typeof w[b] === "boolean") S.ansicht[b] = w[b];
      }
      if (v && (v.sprache === "en" || v.sprache === "de")) S.sprache = v.sprache;
    } catch (x) { }
    const q = new URLSearchParams(location.search).get("lang");
    if ((q === "en" || q === "de") && !laden.schonEinmal) S.sprache = q;
    laden.schonEinmal = true;
  }
  laden();
  function sichern() {
    schreib("antworten", { antworten: S.antworten, aktuell: S.aktuell, f2Uebersprungen: S.f2Uebersprungen });
    schreib("einstellungen", S.e); schreib("kurswerte", S.kurs); schreib("ansicht", { ansicht: S.ansicht, sprache: S.sprache });
  }
  const freigabe = () => S.antworten.start.fest;
  const reglerTZfrei = () => S.antworten.f1.fest || FRAGEN.some(f => f.id[0] === "v" && S.antworten[f.id].fest);

  // ------------------------------------------------------------------ Texte
  function t(k, werte) {
    let s = (TEXTE[S.sprache] && TEXTE[S.sprache][k]);
    if (s === undefined) s = TEXTE.de[k];
    if (s === undefined) { console.error("Text fehlt: " + k); return k; }
    if (werte) s = s.replace(/\{(\w+)\}/g, (m, n) => (n in werte ? werte[n] : m));
    return s;
  }
  const z = (x, n) => HILFEN.zahlText(x, n, S.sprache);
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
  // Kleine Zeichen als SVG (die eingebettete Schrift hat keine Kästchen, Haken oder Schraffur), immer aria-hidden
  const SYM = {
    haken: '<svg class="sym" viewBox="0 0 12 12" aria-hidden="true" focusable="false"><path d="M2 6.5 L5 9.5 L10.5 2.5" fill="none" stroke="currentColor" stroke-width="2"/></svg>',
    b1: '<svg class="sym" viewBox="0 0 12 12" aria-hidden="true" focusable="false"><circle cx="6" cy="6" r="4.8" fill="#8b5a2b"/></svg>',
    b2: '<svg class="sym" viewBox="0 0 12 12" aria-hidden="true" focusable="false"><rect x="1.5" y="1.5" width="9" height="9" fill="#222"/></svg>',
    b3: '<svg class="sym" viewBox="0 0 12 12" aria-hidden="true" focusable="false"><path d="M6 0.8 L11.5 10.5 L0.5 10.5 Z" fill="#3d70a3"/></svg>',
    vor: '<svg class="sym sym-flaeche" viewBox="0 0 14 14" aria-hidden="true" focusable="false"><rect x="0.5" y="0.5" width="13" height="13" fill="#fff" stroke="#222"/><path d="M0 7 L7 0 M0 14 L14 0 M7 14 L14 7" stroke="#222" stroke-width="1.5"/></svg>',
    nach: '<svg class="sym sym-flaeche" viewBox="0 0 14 14" aria-hidden="true" focusable="false"><rect x="0.5" y="0.5" width="13" height="13" fill="#fff" stroke="#8b5a2b"/><circle cx="4" cy="4" r="1.4" fill="#8b5a2b"/><circle cx="10" cy="4" r="1.4" fill="#8b5a2b"/><circle cx="4" cy="10" r="1.4" fill="#8b5a2b"/><circle cx="10" cy="10" r="1.4" fill="#8b5a2b"/><circle cx="7" cy="7" r="1.4" fill="#8b5a2b"/></svg>'
  };
  const svgText = s => esc(s).replace(/\*([^*]+)\*/g, '<tspan font-style="italic">$1</tspan>').replace(/_([A-Za-z0-9]+)/g, '<tspan baseline-shift="sub" font-size="75%">$1</tspan>');
  const BRUCH = (a, b) => '<math><mfrac><mi mathvariant="normal">' + a + '</mi><mi mathvariant="normal">' + b + "</mi></mfrac></math>";
  const EINHEIT_HTML = { "W/K": BRUCH("W", "K") };
  const einheit = u => EINHEIT_HTML[u] || esc(u);
  const nurText = html => { const d = document.createElement("div"); d.innerHTML = html; return d.textContent; };
  function texteSetzen() {
    document.documentElement.lang = S.sprache;
    document.title = nurText(t("titel_seite"));
    for (const el of document.querySelectorAll("[data-t]")) el.innerHTML = t(el.getAttribute("data-t"));
    for (const el of document.querySelectorAll("[data-t-aria]")) el.setAttribute("aria-label", nurText(t(el.getAttribute("data-t-aria"))));
    $("sprachknopf").setAttribute("aria-label", nurText(t("sprache_knopf_aria")));
    $("speicher-hinweis").innerHTML = t(speicherOk ? "speicher_ok" : "speicher_aus");
    $("speicher-hinweis").classList.toggle("aus", !speicherOk);
    $("fuss-stand").textContent = nurText(t("fuss_stand", { stand: BAU.stand, version: BAU.version }));
  }

  // ------------------------------------------------------------------ Rechnen
  let R = null, FEHLER = "";
  function rechnen() {
    FEHLER = ERW.fehler(S.e);
    R = FEHLER ? null : ERW.auswerten(S.e);
  }
  function ausgangslage(art) {
    const sprache = S.sprache;
    if (art === "kurs") return uebernehmen(true);
    S.e = standardE();
    if (art === "becher") Object.assign(S.e, { kAQuelle: "messung", thMess: 67, becher: true, kAHerkunft: "messung" });
    S.sprache = sprache;
    return { ok: true };
  }

  // ------------------------------------------------------------------ Frageleiste
  function frage(id) { return FRAGEN.find(f => f.id === id); }
  function vorhersageZahl(f, roh) {        // „4 K“, „ca. 4“, „~4“, „40 min“ gelten als Zahl (G1-05, G2)
    const t0 = String(roh || "").trim().replace(/^(ca\.?|etwa|about|approx\.?|~|≈)\s*/i, "").replace(/\s*(K|min|°\s*C|°)$/i, "").trim();
    const l = HILFEN.zahlLesen(t0);
    if (isFinite(l.wert) && f.id === "start" && l.wert < 0) return { wert: NaN, grund: "negativ" };
    return l;
  }
  function zahlAnzeige(f, roh) {
    const l = vorhersageZahl(f, roh); if (!isFinite(l.wert)) return esc(roh);
    const d = (String(roh).match(/[.,](\d+)/) || ["", ""])[1].length;
    return z(l.wert, Math.min(2, d));
  }
  function vorhersageText(f, a) {
    if (a.ohne) return t("ohne_vorhersage");
    const teile = [];
    if (f.wahl && a.wahl) teile.push(nurText(t(f.wahlText[a.wahl])));
    if (f.zahl && a.zahl !== "") teile.push((f.id === "start" ? nurText(t("etwa")) + " " : "") + zahlAnzeige(f, a.zahl) + " " + f.zahl.einheit);
    return teile.join(", ");
  }
  function vorhersageGueltig(f, a) {
    if (f.wahl && !a.wahl) return false;
    if (f.zahl && f.zahl.pflicht && !isFinite(vorhersageZahl(f, a.zahl).wert)) return false;
    if (f.zahl && a.zahl.trim() !== "" && !isFinite(vorhersageZahl(f, a.zahl).wert)) return false;
    return true;
  }
  function kursAnzahl() { let n = 0; for (const k of ["b1", "b2"].concat(S.kurs.b3 ? ["b3"] : [])) n += S.kurs.werte[k].filter(v => v !== null).length; return n; }
  function frageleisteZeichnen() {
    const f = frage(S.aktuell), a = S.antworten[f.id], el = $("frageleiste");
    const pflichtNr = PFLICHT.indexOf(f.id);
    const nr = f.id === "start" ? t("leiste_start") : (pflichtNr > 0 ? t("leiste_frage", { n: pflichtNr }) : t("leiste_vertiefung") + " " + f.id.toUpperCase());
    let h = "";
    const st = S.antworten.start;
    if (f.id === "f1" && st.fest && !a.fest) {
      h += '<div class="rueckblick"><p><strong>' + t("leiste_start") + ":</strong> " + t("eure_vorhersage") + ": " + esc(vorhersageText(frage("start"), st)) + "</p>" +
        '<p class="auftrag">' + t("auftrag_start") + '</p><div class="frage-knoepfe"><button type="button" class="knopf-zweit" id="knopf-aufl-start" aria-expanded="' +
        (st.aufl ? "true" : "false") + '" aria-controls="aufl-start">' + t(st.aufl ? "knopf_aufloesung_zu" : "knopf_aufloesung") + "</button></div>" +
        (st.aufl ? '<div class="aufloesung" id="aufl-start">' + vergleichHtml(frage("start"), st) + "<p>" + t("aufl_start") + "</p></div>" : "") + "</div>";
    }
    h += '<p class="frage-nr">' + nr + '</p><h2 id="frage-titel">' + t(f.titel) + "</h2>";
    h += '<p class="frage-text">' + t(f.text) + "</p>";
    if (f.id === "f2") h += '<p class="hinweis" id="f2-werte">' + (kursAnzahl() ? t("f2_werte_da", { n: kursAnzahl() }) : t("f2_keine_werte")) + "</p>";
    h += '<p class="hinweis"><strong>' + t("ausgangslage") + ":</strong> " + t(f.id === "f2" && !kursAnzahl() && !a.fest ? "f2_ausgang_leer" : f.ausgang) + "</p>";
    const gesperrt = a.fest;
    if (!a.fest) {          // nach dem Festhalten keine gesperrten Felder mehr: die Leiste wird kurz (G7-03, G4-10)
      h += '<div class="frage-eingabe">';
      if (f.wahl) {
        h += '<fieldset><legend>' + t("eure_vorhersage") + '</legend><div class="wahl">';
        for (const w of f.wahl) h += '<label><input type="radio" name="wahl-' + f.id + '" value="' + w + '"' + (a.wahl === w ? " checked" : "") + "> <span>" + t(f.wahlText[w]) + "</span></label>";
        h += "</div></fieldset>";
      }
      if (f.zahl) h += '<label class="feld">' + t(f.zahl.label) + ' <span class="feld-einheit"><input type="text" inputmode="decimal" autocomplete="off" id="frage-zahl" maxlength="16" value="' + esc(a.zahl) + '"> ' + esc(f.zahl.einheit) + "</span></label>";
      h += '<label class="feld feld-breit">' + t("begruendung_label") + ' <input type="text" id="frage-warum" autocomplete="off" maxlength="300" value="' + esc(a.warum) + '"></label>';
      h += "</div>";
    }
    h += '<div class="frage-knoepfe">';
    if (!a.fest) {
      const ok = vorhersageGueltig(f, a) && !(f.id === "f2" && !kursAnzahl());
      h += '<button type="button" class="knopf-haupt" id="knopf-fest"' + (ok ? "" : " disabled") + ">" + t(f.id === "start" ? "knopf_vorhersage_start" : "knopf_vorhersage") + "</button>";
      h += '<span class="hinweis" id="hinweis-waehlen"' + (ok ? " hidden" : "") + ">" + t(hinweisSchluessel(f, a)) + "</span>";
      h += '<button type="button" class="knopf-text" id="knopf-ohne">' + t("knopf_ohne") + "</button>";
      if (f.id === "f2" && !kursAnzahl()) h += '<button type="button" class="knopf-schlicht" id="knopf-f2-weg">' + t("f2_ueberspringen") + "</button>";
    }
    h += '<div class="frage-nav">';
    const reihe = FRAGEN.map(x => x.id), i = reihe.indexOf(f.id);
    if (i > 0 && freigabe()) h += '<button type="button" class="knopf-schlicht" id="knopf-zurueck">' + t("knopf_zurueck") + "</button>";
    if (freigabe() && i < reihe.length - 1 && (a.fest || f.id === "f2" && S.f2Uebersprungen)) h += '<button type="button" class="knopf-schlicht" id="knopf-weiter">' + t("knopf_weiter") + "</button>";
    h += "</div></div>";
    if (a.fest) {
      h += '<p class="hinweis"><strong>' + t("eure_vorhersage") + ":</strong> " + esc(vorhersageText(f, a)) + (a.warum ? " (" + esc(a.warum) + ")" : "") + "</p>";
      h += '<p class="auftrag">' + (f.id === "start" ? t("auftrag_start") : (f.id === "f2" ? t("f2_auftrag") : t("auftrag_erklaeren"))) + "</p>";
      h += '<div class="frage-knoepfe"><button type="button" class="knopf-zweit" id="knopf-aufl" aria-expanded="' + (a.aufl ? "true" : "false") + '" aria-controls="aufl-leiste">' + t(a.aufl ? "knopf_aufloesung_zu" : "knopf_aufloesung") + "</button></div>";
      if (a.aufl) h += '<div class="aufloesung" id="aufl-leiste">' + vergleichHtml(f, a) + "<p>" + t(f.aufl) + "</p></div>";
    }
    if (f.id === "f2" && S.f2Uebersprungen && !a.fest) h += '<p class="hinweis">' + t("f2_uebersprungen") + "</p>";
    if (PFLICHT.indexOf(f.id) === 2 && (a.fest || S.f2Uebersprungen)) h += '<p class="auftrag">' + t("fertig_pflicht") + ' <button type="button" class="knopf-schlicht" id="knopf-vt-auf">' + t("knopf_vertiefung_oeffnen") + "</button></p>";
    el.innerHTML = h;
    // Ereignisse
    for (const r of el.querySelectorAll('input[type="radio"]')) r.addEventListener("change", () => { a.wahl = r.value; sichern(); frageKnopfAktualisieren(); });
    const zf = $("frage-zahl"); if (zf) zf.addEventListener("input", () => { a.zahl = zf.value; sichern(); frageKnopfAktualisieren(); });
    const wf = $("frage-warum"); if (wf) wf.addEventListener("input", () => { a.warum = wf.value; sichern(); });
    const kf = $("knopf-fest"); if (kf) kf.addEventListener("click", () => festhalten(f, false));
    const ko = $("knopf-ohne"); if (ko) ko.addEventListener("click", () => bestaetigen(t("ohne_frage"), () => festhalten(f, true), ko));
    const kas = $("knopf-aufl-start"); if (kas) kas.addEventListener("click", () => { st.aufl = !st.aufl; sichern(); alles(); fokus("knopf-aufl-start"); });
    const ka = $("knopf-aufl"); if (ka) ka.addEventListener("click", () => { a.aufl = !a.aufl; sichern(); alles(); fokus("knopf-aufl"); });
    const ruhig = () => Date.now() - (frageleisteZeichnen.zuletzt || 0) > 400;     // G8-19: zweiter Klick eines Doppelklicks trifft sonst den neuen Knopf
    const kz = $("knopf-zurueck"); if (kz) kz.addEventListener("click", () => { if (ruhig()) { frageleisteZeichnen.zuletzt = Date.now(); geheZu(reihe[i - 1]); } });
    const kw = $("knopf-weiter"); if (kw) kw.addEventListener("click", () => { if (ruhig()) { frageleisteZeichnen.zuletzt = Date.now(); geheZu(reihe[i + 1]); } });
    const k2 = $("knopf-f2-weg"); if (k2) k2.addEventListener("click", () => { S.f2Uebersprungen = true; sichern(); alles(); fokus("knopf-weiter"); });
    const kv = $("knopf-vt-auf"); if (kv) kv.addEventListener("click", () => { S.ansicht.vertiefung = true; geheZu("v1"); $("frageleiste").scrollIntoView({ block: "start" }); });
  }
  function hinweisSchluessel(f, a) {
    if (f.id === "f2" && !kursAnzahl()) return "f2_erst_laden";
    if (f.wahl && !a.wahl) return "hinweis_erst_waehlen";
    if (f.zahl && a.zahl.trim() === "") return "hinweis_zahl_fehlt";
    return "hinweis_zahl";
  }
  function frageleisteStill() {      // nur Hinweis und Knopf der Frage 2 nachziehen, ohne die Leiste neu aufzubauen
    const h2 = $("f2-werte"); if (h2) h2.innerHTML = kursAnzahl() ? t("f2_werte_da", { n: kursAnzahl() }) : t("f2_keine_werte");
    frageKnopfAktualisieren();
  }
  function frageKnopfAktualisieren() {
    const f = frage(S.aktuell), a = S.antworten[f.id], k = $("knopf-fest");
    if (!k) return;
    const ok = vorhersageGueltig(f, a) && !(f.id === "f2" && !kursAnzahl());
    k.disabled = !ok;
    const h = $("hinweis-waehlen"); if (h) { h.hidden = ok; h.innerHTML = t(hinweisSchluessel(f, a)); }
    const zf = $("frage-zahl");
    if (zf) { const falsch = a.zahl.trim() !== "" && !isFinite(vorhersageZahl(f, a.zahl).wert); if (falsch) { zf.setAttribute("aria-invalid", "true"); zf.setAttribute("aria-describedby", "hinweis-waehlen"); } else { zf.removeAttribute("aria-invalid"); zf.removeAttribute("aria-describedby"); } }
  }
  const SOLL = { start: "soll_start", f1: "soll_f1", v1: "soll_v1", v2: "soll_v2" };   // Modellwerte der Standardlage (Konzept 6)
  function vergleichHtml(f, a) {
    let h = "<p><strong>" + t("eure_vorhersage") + ":</strong> " + esc(vorhersageText(f, a));
    if (f.richtig && a.wahl && !a.ohne) h += " · " + (a.wahl === f.richtig ? '<span class="vergleich-ok">' + SYM.haken + " " + t("passt") + "</span>" : '<span class="vergleich-nein">× ' + t("passt_nicht") + "</span>");
    if (SOLL[f.id] && f.zahl && a.zahl !== "" && !a.ohne) h += "<br>" + t("vergleich_zahl", { ist: zahlAnzeige(f, a.zahl) + " " + esc(f.zahl.einheit), soll: t(SOLL[f.id]) });
    return h + (a.warum && !a.ohne ? '<br><span class="klein">' + t("eure_begruendung") + ": " + esc(a.warum) + "</span>" : "") + "</p>";
  }
  function festhalten(f, ohne) {
    const a = S.antworten[f.id];
    if (ohne) { a.ohne = true; a.wahl = a.wahl || null; }
    a.fest = true;
    let meldung = "";
    if (f.id !== "start" || !freigabe()) {
      const erg = ausgangslage(f.setze);
      if (erg && erg.ok === false) { a.fest = false; a.ohne = false; meldung = erg.text; }
      else meldung = t("ausgangslage_gesetzt", { was: nurText(t(f.ausgang)) });
    }
    if (a.fest && f.id === "start") S.aktuell = "f1";
    sichern(); alles();
    if (meldung) $("knopf-info").textContent = meldung;
    if (a.fest) { ansagen(true); $("simulation").scrollIntoView({ block: "start" }); }
    const ziel = $(f.id === "start" ? "frage-titel" : "knopf-aufl");
    if (ziel) { if (!ziel.hasAttribute("tabindex") && ziel.tagName !== "BUTTON") ziel.setAttribute("tabindex", "-1"); ziel.focus({ preventScroll: true }); }
  }
  function geheZu(id) {
    S.aktuell = id;
    if (id[0] === "v") S.ansicht.vertiefung = true;
    sichern(); alles(); fokus("frage-titel");
  }
  function fokus(id) { const el = $(id); if (el) { if (!el.hasAttribute("tabindex") && !/^(BUTTON|INPUT|A|SUMMARY)$/.test(el.tagName)) el.setAttribute("tabindex", "-1"); el.focus({ preventScroll: false }); } }

  // ------------------------------------------------------------------ Diagramm
  const NS = "http://www.w3.org/2000/svg";
  function mittelText(text, W, H, L, Rr, O, U) {
    const zeilen = [], maxZ = Math.floor((W - L - Rr - 20) / 7.4);
    for (const w of text.split(" ")) { if (zeilen.length && (zeilen[zeilen.length - 1] + " " + w).length <= maxZ) zeilen[zeilen.length - 1] += " " + w; else zeilen.push(w); }
    const x = (L + W - Rr) / 2;
    return '<text x="' + x + '" y="' + ((O + H - U) / 2 - (zeilen.length - 1) * 9) + '" text-anchor="middle" font-size="13" fill="#5a6b7f">' + zeilen.map((zz, i) => '<tspan x="' + x + '"' + (i ? ' dy="18"' : "") + ">" + esc(zz) + "</tspan>").join("") + "</text>";
  }
  const stellenVon = st => { let d = 0; while (d < 3 && Math.abs(st * Math.pow(10, d) - Math.round(st * Math.pow(10, d))) > 1e-9) d++; return d; };
  function schritt(spanne) { const roh = spanne / 6; const p = Math.pow(10, Math.floor(Math.log10(roh))); for (const m of [1, 2, 2.5, 5, 10]) if (m * p >= roh) return m * p; return 10 * p; }
  function diagrammZeichnen() {
    const svg = $("diagramm"), halter = $("diagramm-halter");
    const W = Math.round(Math.min(780, Math.max(280, halter.getBoundingClientRect().width || 640)));
    const H = Math.round(W < 520 ? W * 0.78 : Math.min(W * 0.56, Math.max(window.innerHeight < 500 ? 170 : 280, window.innerHeight * 0.5)));
    svg.setAttribute("viewBox", "0 0 " + W + " " + H);
    svg.setAttribute("width", W); svg.setAttribute("height", H);
    const fs = 12, L = 52, Rr = 14, O = 16, U = 44;
    const s = [];
    s.push('<defs><pattern id="muster-vor" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="7" stroke="#222" stroke-width="1.6"/></pattern>' +
      '<pattern id="muster-nach" width="6" height="6" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="1.3" fill="#8b5a2b"/></pattern></defs>');
    const ansicht = freigabe() ? S.ansicht.diagramm : "temperatur";
    const tz = S.e.tEnd_min;
    const punkte = freigabe() && messFrei() ? messPunkte() : [];
    const xMaxDaten = Math.max(tz, punkte.length ? Math.max(...punkte.map(p => p.t)) : 0);
    const xMax = Math.max(10, xMaxDaten * 1.04 + 0.5);
    let yMin, yMax, yLabel;
    let kurven = [];
    if (ansicht === "temperatur") {
      yLabel = t("dia_achse_th_txt");
      const ys = [S.e.thU, S.e.thK0].concat(punkte.map(p => p.th));
      if (R && freigabe()) ys.push(R.th2, R.th1, R.th2K, R.th10, R.th2Raum);
      yMin = Math.min(...ys.filter(isFinite)) - 3; yMax = Math.max(...ys.filter(isFinite)) + 3;
    } else if (ansicht === "waermestrom") {
      yLabel = t("dia_achse_q_txt");
      yMin = 0; yMax = R ? Math.max(R.qdot1(0), R.qdot2(0)) * 1.1 : 25;
    } else {
      yLabel = t("dia_achse_ln_txt");
      const lp = lnPunkte(); yMin = lp.length ? Math.min(...lp.map(p => p.y)) * 1.15 : -1.5; yMax = 0.08;
      if (!(yMin < -0.05)) yMin = -1.5;
    }
    const st = schritt(yMax - yMin);
    const raster = ansicht === "temperatur" && st >= 10 ? 10 : st;
    yMin = Math.floor(yMin / raster) * raster; yMax = Math.ceil(yMax / raster) * raster;
    const X = x => L + (W - L - Rr) * x / xMax, Y = y => O + (H - O - U) * (yMax - y) / (yMax - yMin);
    const xs = schritt(xMax);
    for (let y = yMin; y <= yMax + 1e-9; y += (raster < st ? st : st)) {
      s.push('<line x1="' + L + '" x2="' + (W - Rr) + '" y1="' + Y(y).toFixed(1) + '" y2="' + Y(y).toFixed(1) + '" stroke="#e6ebf0"/>');
      s.push('<text x="' + (L - 6) + '" y="' + (Y(y) + 4).toFixed(1) + '" text-anchor="end" font-size="' + fs + '" fill="#5a6b7f">' + z(y, stellenVon(st)) + "</text>");
    }
    for (let x = 0; x <= xMax + 1e-9; x += xs) {
      s.push('<line x1="' + X(x).toFixed(1) + '" x2="' + X(x).toFixed(1) + '" y1="' + (H - U) + '" y2="' + (H - U + 5) + '" stroke="#5a6b7f"/>');
      s.push('<text x="' + X(x).toFixed(1) + '" y="' + (H - U + 18) + '" text-anchor="middle" font-size="' + fs + '" fill="#5a6b7f">' + z(x, stellenVon(xs)) + "</text>");
    }
    s.push('<line x1="' + L + '" x2="' + (W - Rr) + '" y1="' + (H - U) + '" y2="' + (H - U) + '" stroke="#5a6b7f"/><line x1="' + L + '" x2="' + L + '" y1="' + O + '" y2="' + (H - U) + '" stroke="#5a6b7f"/>');
    s.push('<text x="' + ((L + W - Rr) / 2) + '" y="' + (H - 8) + '" text-anchor="middle" font-size="13" fill="#142337">' + svgText(t("dia_achse_t_txt")) + "</text>");
    s.push('<text x="14" y="' + ((O + H - U) / 2) + '" text-anchor="middle" font-size="13" fill="#142337" transform="rotate(-90 14 ' + ((O + H - U) / 2) + ')">' + svgText(yLabel) + "</text>");
    const belegt = [];   // Rechtecke für die Kollisionsprüfung der Beschriftungen
    const pfad = (f, a, b, n) => { const p = []; for (let i = 0; i <= n; i++) { const x = a + (b - a) * i / n; p.push(X(x).toFixed(1) + "," + Y(f(x)).toFixed(1)); } return p.join(" "); };
    let kurvenPx = [], raumY = null, vorhersageUnten = "";
    // Direkte Beschriftung mit Kollisionsprüfung (E6/F19: nie auf einer Linie)
    const etikett = (text, farbe, kurve, oben, bevorzugt) => {
      const breite = text.length * fs * 0.56 + 6, hoehe = fs + 6;
      const kand = [];
      for (const fr of bevorzugt) for (const dy of (oben ? [-14, -26, 22, 34] : [22, 34, -14, -26])) kand.push([fr, dy]);
      for (const [fr, dy] of kand) {
        const x0 = X(tz * fr); if (x0 + breite > W - Rr || x0 < L + 4) continue;
        const yb = Y(kurve(tz * fr)) + dy, yo = yb - fs;
        if (yo < O || yb > H - U - 2) continue;
        let frei = true;
        for (let i = 0; i <= 24 && frei; i++) {
          const xp = x0 + breite * i / 24, tt = (xp - L) / (W - L - Rr) * xMax;
          if (tt < 0 || tt > tz) continue;
          for (const k of kurvenPx) { const yk = k(tt); if (yk > yo - 4 && yk < yb + 5) { frei = false; break; } }
        }
        if (raumY !== null && raumY > yo - 3 && raumY < yb + 4) frei = false;
        for (const b of belegt) if (x0 < b[0] + b[2] && x0 + breite > b[0] && yo - 2 < b[1] + b[3] && yb + 2 > b[1]) frei = false;
        if (frei) { belegt.push([x0, yo - 2, breite, hoehe]); return '<text x="' + x0.toFixed(1) + '" y="' + yb.toFixed(1) + '" font-size="' + (fs + 1) + '" font-weight="600" fill="' + farbe + '">' + esc(text) + "</text>"; }
      }
      return null;
    };
    if (ansicht === "temperatur") {
      raumY = Y(S.e.thU); if (R) kurvenPx = [t2 => Y(R.kurve1(t2)), t2 => Y(R.kurve2(t2))];
      s.push('<line x1="' + L + '" x2="' + (W - Rr) + '" y1="' + Y(S.e.thU).toFixed(1) + '" y2="' + Y(S.e.thU).toFixed(1) + '" stroke="#8a8984" stroke-width="1.5" stroke-dasharray="1.5 4" stroke-linecap="round"/>');
      const raumRechts = !(R && freigabe() && Math.min(Math.abs(Y(R.th2) - Y(S.e.thU)), Math.abs(Y(R.th1) - Y(S.e.thU)), Math.abs(Y(R.th2K) - Y(S.e.thU))) < 22 && X(tz) > W - Rr - 110);
      s.push('<text x="' + (raumRechts ? W - Rr - 4 : L + 6) + '" y="' + (Y(S.e.thU) - 5).toFixed(1) + '" text-anchor="' + (raumRechts ? "end" : "start") + '" font-size="' + fs + '" fill="#5a6b7f">' + esc(t("dia_raum", { th: z(S.e.thU, 1) })) + "</text>");
      if (!freigabe()) {
        s.push('<circle cx="' + X(0) + '" cy="' + Y(S.e.thK0).toFixed(1) + '" r="4.5" fill="#222"/><text x="' + (X(0) + 9) + '" y="' + (Y(S.e.thK0) + 4).toFixed(1) + '" font-size="' + fs + '">' + z(S.e.thK0, 0) + " °C</text>");
        const zeilen = [], wo = nurText(t("dia_beschreibung_start")).split(" "), maxZ = Math.floor((W - L - Rr - 20) / 7.6);
        for (const w of wo) { if (zeilen.length && (zeilen[zeilen.length - 1] + " " + w).length <= maxZ) zeilen[zeilen.length - 1] += " " + w; else zeilen.push(w); }
        s.push('<text x="' + ((L + W - Rr) / 2) + '" y="' + ((O + H - U) / 2 - (zeilen.length - 1) * 9) + '" text-anchor="middle" font-size="14" fill="#5a6b7f">' + zeilen.map((zz, i) => '<tspan x="' + ((L + W - Rr) / 2) + '"' + (i ? ' dy="18"' : "") + ">" + esc(zz) + "</tspan>").join("") + "</text>");
      } else if (!R) {
        s.push('<rect x="' + (L + 1) + '" y="' + (O + 1) + '" width="' + (W - L - Rr - 2) + '" height="' + (H - O - U - 2) + '" fill="#fbecec" stroke="#b63434" stroke-dasharray="6 5"/>');
        s.push('<text x="' + ((L + W - Rr) / 2) + '" y="' + ((O + H - U) / 2) + '" text-anchor="middle" font-size="15" fill="#862828">' + esc(t("dia_ungueltig")) + "</text>");
      } else {
        if (S.vergleich) {
          const rv = ERW.fehler(S.vergleich) ? null : ERW.auswerten(S.vergleich);
          if (rv) {
            s.push('<polyline points="' + pfad(rv.kurve2, 0, S.vergleich.tEnd_min, N_ABTAST) + '" fill="none" stroke="#222" stroke-width="2" stroke-dasharray="9 5" opacity="0.5"/>');
            s.push('<line x1="' + X(S.vergleich.tEnd_min).toFixed(1) + '" x2="' + X(S.vergleich.tEnd_min).toFixed(1) + '" y1="' + Y(rv.th2K).toFixed(1) + '" y2="' + Y(rv.th2).toFixed(1) + '" stroke="#222" stroke-width="1.6" stroke-dasharray="2 3" opacity="0.5"/>');
            s.push('<polyline points="' + pfad(rv.kurve1, 0, S.vergleich.tEnd_min, N_ABTAST) + '" fill="none" stroke="#8b5a2b" stroke-width="2" stroke-dasharray="2 3" opacity="0.6"/>');
          }
        }
        s.push('<line x1="' + X(0) + '" x2="' + X(0) + '" y1="' + Y(S.e.thK0).toFixed(1) + '" y2="' + Y(R.th10).toFixed(1) + '" stroke="#8b5a2b" stroke-width="2" stroke-dasharray="2 3"/>');
        s.push('<polyline points="' + pfad(R.kurve2, 0, tz, N_ABTAST) + '" fill="none" stroke="#222" stroke-width="2.6" stroke-dasharray="9 5"/>');
        s.push('<polyline points="' + pfad(R.kurve1, 0, tz, N_ABTAST) + '" fill="none" stroke="#8b5a2b" stroke-width="2.8"/>');
        s.push('<line x1="' + X(tz).toFixed(1) + '" x2="' + X(tz).toFixed(1) + '" y1="' + Y(R.th2K).toFixed(1) + '" y2="' + Y(R.th2).toFixed(1) + '" stroke="#222" stroke-width="2" stroke-dasharray="2 3"/>');
        s.push('<circle cx="' + X(tz).toFixed(1) + '" cy="' + Y(R.th1).toFixed(1) + '" r="4.5" fill="#fff" stroke="#8b5a2b" stroke-width="2.2"/><circle cx="' + X(tz).toFixed(1) + '" cy="' + Y(R.th2).toFixed(1) + '" r="4.5" fill="#fff" stroke="#222" stroke-width="2.2"/>');
        if (S.kurs.b3) s.push('<line x1="' + (X(tz) + 5).toFixed(1) + '" x2="' + (X(tz) + 5).toFixed(1) + '" y1="' + Y(R.th2K).toFixed(1) + '" y2="' + Y(R.th2Raum).toFixed(1) + '" stroke="#3d70a3" stroke-width="2" stroke-dasharray="2 3"/>');
        if (S.kurs.b3) s.push('<path d="M ' + X(tz).toFixed(1) + " " + (Y(R.th2Raum) - 6).toFixed(1) + " l 5.5 9.5 l -11 0 z\" fill=\"#fff\" stroke=\"#3d70a3\" stroke-width=\"2\"/>");
        if (schnittFrei() && isFinite(R.tSchnitt) && R.tSchnitt < tz) {
          const sx = X(R.tSchnitt), sy = Y(R.kurve1(R.tSchnitt));
          s.push('<circle cx="' + sx.toFixed(1) + '" cy="' + sy.toFixed(1) + '" r="5.5" fill="#fff" stroke="#222" stroke-width="1.8"/>');
          belegt.push([sx - 7, sy - 7, 14, 14]);
        }
        // Vorhersage der aktuellen Frage als beschrifteter Kasten oben rechts (frei von Kurven), sonst als Zeile unter dem Diagramm (G1-11, G4-08)
        const fq = frage(S.aktuell), aq = S.antworten[fq.id];
        const [fv, av] = (aq.fest && !aq.ohne) ? [fq, aq] : [frage("start"), S.antworten.start];
        if (av.fest && !av.ohne) {
          const txt = t("dia_vorhersage", { text: vorhersageText(fv, av) });
          const bw = txt.length * 11 * 0.56 + 14, bx = W - Rr - bw - 4, by = O + 4;
          let frei = bx > L + 4;
          for (let i = 0; i <= 20; i++) { const xp = bx + bw * i / 20, tt = (xp - L) / (W - L - Rr) * xMax; if (tt <= tz) for (const k of kurvenPx) { const yk = k(tt); if (yk < by + 26 && yk > by - 4) frei = false; } }
          if (frei) { s.push('<rect id="vh-kasten" x="' + bx.toFixed(1) + '" y="' + by + '" width="' + bw.toFixed(1) + '" height="22" rx="3" fill="#e8f5ef" stroke="#227b48"/><text id="vh-text" x="' + (bx + 7).toFixed(1) + '" y="' + (by + 15) + '" font-size="11" fill="#14603f">' + esc(txt) + "</text>"); belegt.push([bx, by, bw, 22]); }
          else vorhersageUnten = txt;
          if ((fv.id === "f1" || fv.id === "v2") && isFinite(vorhersageZahl(fv, av.zahl).wert)) {
            const tv = vorhersageZahl(fv, av.zahl).wert;
            if (tv > 0 && tv <= xMax) s.push('<line x1="' + X(tv).toFixed(1) + '" x2="' + X(tv).toFixed(1) + '" y1="' + (O + 28) + '" y2="' + (H - U) + '" stroke="#227b48" stroke-width="1.6" stroke-dasharray="3 3"/>');
          }
        }
        // Messpunkte
        punkte.sort((a, b) => (b.b === 3) - (a.b === 3));
        for (const p of punkte) {
          const px = X(p.t), py = Y(p.th), c = p.b === 1 ? "#8b5a2b" : (p.b === 2 ? "#222" : "#3d70a3");
          if (p.b === 1) s.push('<circle cx="' + px.toFixed(1) + '" cy="' + py.toFixed(1) + '" r="4.8" fill="' + c + '" stroke="#fff" stroke-width="1"/>');
          else if (p.b === 2) s.push('<rect x="' + (px - 4.5).toFixed(1) + '" y="' + (py - 4.5).toFixed(1) + '" width="9" height="9" fill="' + c + '" stroke="#fff" stroke-width="1"/>');
          else s.push('<path d="M ' + px.toFixed(1) + " " + (py - 6).toFixed(1) + ' l 5.5 9.5 l -11 0 z" fill="none" stroke="' + c + '" stroke-width="1.8"/>');
          belegt.push([px - 6, py - 6, 12, 12]);
        }
        if (schnittFrei() && isFinite(R.tSchnitt) && R.tSchnitt < tz) {     // Beschriftung „Schnitt“ nach den Messpunkten, frei von Punkten
          const sx = X(R.tSchnitt), sy = Y(R.kurve1(R.tSchnitt)), txt = t("dia_schnitt"), bw = txt.length * fs * 0.56 + 4;
          const kand = [[sx - bw / 2, sy - 10], [sx - bw / 2, sy + fs + 10], [sx - bw - 10, sy - 8], [sx - bw - 10, sy + fs + 6], [sx - bw / 2, sy - 24]];
          let wahl = kand[0];
          for (const [x0, yb] of kand) {
            if (x0 < L + 2 || x0 + bw > W - Rr + 6 || yb - fs < O || yb > H - U - 2) continue;
            let aufKurve = false;
            for (let i = 0; i <= 12 && !aufKurve; i++) { const xp = x0 + bw * i / 12, tt = (xp - L) / (W - L - Rr) * xMax; if (tt >= 0 && tt <= tz) for (const k of kurvenPx) { const yk = k(tt); if (yk > yb - fs - 3 && yk < yb + 4) aufKurve = true; } }
            if (raumY !== null && raumY > yb - fs - 3 && raumY < yb + 4) aufKurve = true;
            if (!aufKurve && !belegt.some(b => x0 < b[0] + b[2] && x0 + bw > b[0] && yb - fs < b[1] + b[3] && yb + 2 > b[1])) { wahl = [x0, yb]; break; }
          }
          s.push('<text x="' + wahl[0].toFixed(1) + '" y="' + wahl[1].toFixed(1) + '" font-size="' + fs + '" fill="#142337">' + esc(txt) + "</text>");
          belegt.push([wahl[0], wahl[1] - fs, bw, fs + 4]);
        }
        if (S.ansicht.trinkzeit && S.ansicht.vertiefung) {      // K-3 Trinkzeit: Linie bei 60 °C, Marken an den Kurven
          const yT = Y(TRINK);
          if (yT > O && yT < H - U) {
            s.push('<line x1="' + L + '" x2="' + (W - Rr) + '" y1="' + yT.toFixed(1) + '" y2="' + yT.toFixed(1) + '" stroke="#227b48" stroke-width="1.4" stroke-dasharray="6 3"/>');
            const tl = nurText(t("dia_trinklinie")), tw = tl.length * fs * 0.56 + 6;
            let tx = W - Rr - tw;
            for (const x0 of [W - Rr - tw, L + 6, (L + W - Rr - tw) / 2]) {
              let frei = true;
              for (let i = 0; i <= 10 && frei; i++) { const tt = (x0 + tw * i / 10 - L) / (W - L - Rr) * xMax; if (tt >= 0 && tt <= tz) for (const k of kurvenPx) { const yk = k(tt); if (yk > yT - fs - 8 && yk < yT + 2) frei = false; } }
              if (frei) { tx = x0; break; }
            }
            s.push('<text x="' + tx.toFixed(1) + '" y="' + (yT - 5).toFixed(1) + '" font-size="' + fs + '" fill="#14603f">' + esc(tl) + "</text>");
            const tr = ERW.trinkzeit(S.e, TRINK);
            for (const [tt, k] of [[tr.tasse1, R.kurve1], [tr.schwarz, R.kurve2]]) if (tt > 0 && tt < tz) s.push('<line x1="' + X(tt).toFixed(1) + '" x2="' + X(tt).toFixed(1) + '" y1="' + (yT - 6).toFixed(1) + '" y2="' + (yT + 6).toFixed(1) + '" stroke="#14603f" stroke-width="2"/>');
            belegt.push([tx, yT - 5 - fs, tw, fs + 4]);
          }
        }
        const e2 = etikett(t("dia_tasse2", { t: z(tz, 0) }), "#222", R.kurve2, true, [0.12, 0.2, 0.06, 0.3, 0.4]);
        const e1 = etikett(t("dia_tasse1"), "#7a4e24", R.kurve1, false, [0.22, 0.3, 0.14, 0.4, 0.5, 0.06]);
        const fehlend = [];
        if (e2) s.push(e2); else fehlend.push("2");
        if (e1) s.push(e1); else fehlend.push("1");
        if (fehlend.length) {           // Ersatz: Legende unter der Zeichenfläche (außerhalb der Achsen)
          let lx = L;
          for (const n of fehlend.reverse()) {
            const txt = n === "1" ? t("dia_tasse1") : t("dia_tasse2", { t: z(tz, 0) });
            s.push('<line x1="' + lx + '" x2="' + (lx + 22) + '" y1="' + (H - 26) + '" y2="' + (H - 26) + '" stroke="' + (n === "1" ? "#8b5a2b" : "#222") + '" stroke-width="2.6"' + (n === "2" ? ' stroke-dasharray="7 4"' : "") + "/>");
            s.push('<text x="' + (lx + 26) + '" y="' + (H - 22) + '" font-size="' + (fs - 1) + '" fill="#142337">' + esc(txt) + "</text>");
            lx += 30 + txt.length * (fs - 1) * 0.55 + 14;
          }
        }
      }
    } else if (ansicht === "waermestrom" && R) {
      const f1 = R.qdot1, f2 = R.qdot2, tq = Math.min(R.tWaermestrom, tz);
      const flaeche = (a, b, muster) => { if (!(b > a)) return ""; const p1 = [], p2 = []; for (let i = 0; i <= 120; i++) { const x = a + (b - a) * i / 120; p1.push(X(x).toFixed(1) + "," + Y(f2(x)).toFixed(1)); p2.unshift(X(x).toFixed(1) + "," + Y(f1(x)).toFixed(1)); } return '<polygon points="' + p1.concat(p2).join(" ") + '" fill="url(#' + muster + ')" opacity="0.75"/>'; };
      s.push(flaeche(0, tq, "muster-vor")); s.push(flaeche(tq, tz, "muster-nach"));
      s.push('<polyline points="' + pfad(f2, 0, tz, N_ABTAST) + '" fill="none" stroke="#222" stroke-width="2.6" stroke-dasharray="9 5"/>');
      s.push('<polyline points="' + pfad(f1, 0, tz, N_ABTAST) + '" fill="none" stroke="#8b5a2b" stroke-width="2.8"/>');
      kurvenPx = [t2 => Y(f1(t2)), t2 => Y(f2(t2))];
      const w2 = etikett(t("dia_tasse2", { t: z(tz, 0) }), "#222", f2, true, [0.04, 0.1, 0.2, 0.3, 0.45]);
      const w1 = etikett(t("dia_tasse1"), "#7a4e24", f1, false, [0.3, 0.45, 0.2, 0.55, 0.1, 0.65]);
      if (w2) s.push(w2); if (w1) s.push(w1);
    } else if (ansicht === "ln") {
      const lp = lnPunkte();
      for (const p of lp) s.push(p.b === 2 ? '<rect x="' + (X(p.t) - 4.5).toFixed(1) + '" y="' + (Y(p.y) - 4.5).toFixed(1) + '" width="9" height="9" fill="#222"/>' :
        '<path d="M ' + X(p.t).toFixed(1) + " " + (Y(p.y) - 6).toFixed(1) + ' l 5.5 9.5 l -11 0 z" fill="#3d70a3"/>');
      const fit = ausgleichRechnen();
      if (fit) {
        const C = ERW.kapazitaeten(S.e).C_KB, b0 = -fit.kA_ursprung / C, b1 = -fit.kA_frei / C;
        s.push('<clipPath id="feld"><rect x="' + L + '" y="' + O + '" width="' + (W - L - Rr) + '" height="' + (H - O - U) + '"/></clipPath>');
        s.push('<line clip-path="url(#feld)" x1="' + X(0) + '" y1="' + Y(0).toFixed(1) + '" x2="' + X(xMax).toFixed(1) + '" y2="' + Y(b0 * xMax * 60).toFixed(1) + '" stroke="#173d5e" stroke-width="2"/>');
        s.push('<line clip-path="url(#feld)" x1="' + X(0) + '" y1="' + Y(fit.achsenabschnitt).toFixed(1) + '" x2="' + X(xMax).toFixed(1) + '" y2="' + Y(fit.achsenabschnitt + b1 * xMax * 60).toFixed(1) + '" stroke="#173d5e" stroke-width="1.5" stroke-dasharray="6 4"/>');
      } else s.push(mittelText(nurText(t(messFrei() ? "ln_kein" : "ln_erst_f2")), W, H, L, Rr, O, U));
    }
    svg.innerHTML = s.join("");
    const vk = $("vh-kasten"), vt = $("vh-text");
    if (vk && vt && vt.getBBox) { try { const bb = vt.getBBox(); if (bb.width > 0) { const bw2 = bb.width + 14, bx2 = W - Rr - bw2 - 4; vk.setAttribute("width", bw2.toFixed(1)); vk.setAttribute("x", bx2.toFixed(1)); vt.setAttribute("x", (bx2 + 7).toFixed(1)); } } catch (x) { } }
    $("vorhersage-zeile").hidden = !vorhersageUnten; $("vorhersage-zeile").textContent = vorhersageUnten;
    zusatzZeichnen();
    document.querySelector(".lesehinweis").innerHTML = (freigabe() && !R) ? "" : t(ansicht === "temperatur" ? "lesehinweis" : "lesehinweis_" + ansicht);   // G6-21
    // Beschreibung für Bildschirmleser
    $("diagramm-name").textContent = nurText(t(ansicht === "temperatur" ? "dia_titel" : "dia_titel_" + ansicht));
    $("diagramm-beschreibung").textContent = (!freigabe()) ? nurText(t("dia_beschreibung_start")) : (R && ansicht === "waermestrom") ? nurText(t("dia_beschreibung_waermestrom", { v: z(R.flaecheVor, 2), n: z(R.flaecheNach, 2), d: z(R.Q2 - R.Q1, 2) })) : (ansicht === "ln") ? nurText(t("dia_beschreibung_ln", { n: lnPunkte().length })) :
      (R ? nurText(t("dia_beschreibung", { a: z(S.e.thK0, 1), m: z(R.th10, 2), b: z(R.th1, 2), t: z(tz, 0), k: z(R.th2K, 2), c: z(R.th2, 2), d: z(R.dT, 2) })) : nurText(t("dia_ungueltig")));
    const lnZeigen = ansicht === "ln" && lnPunkte().length;
    $("legende-mess").hidden = !(freigabe() && ((punkte.length && ansicht === "temperatur") || lnZeigen));
    if (!$("legende-mess").hidden) {
      const da = lnZeigen ? [2, 3].filter(n => lnPunkte().some(p => p.b === n)) : [1, 2, 3].filter(n => punkte.some(p => p.b === n));
      $("legende-mess").innerHTML = t("dia_legende_mess", { liste: da.map(n => SYM["b" + n] + " " + t("dia_becher_n", { n: n })).join(" · ") });
    }
    const ft = $("flaechen-text");
    if (freigabe() && R && ansicht === "waermestrom") {
      ft.hidden = false;
      ft.innerHTML = SYM.vor + " " + t("flaeche_vor") + ": " + z(R.flaecheVor, 2) + " kJ · " + SYM.nach + " " + t("flaeche_nach") + ": " + z(R.flaecheNach, 2) + " kJ · " + t("flaeche_summe", { wert: z(R.Q2 - R.Q1, 2) });
    } else if (freigabe() && ansicht === "ln") {
      const fit = ausgleichRechnen(); ft.hidden = !fit;
      const bn = n => nurText(t("dia_becher_n", { n: n }));
      if (fit) ft.innerHTML = t("ausgleich_text", { becher: S.kurs.b3 ? nurText(t("becher_und", { a: bn(2), b: bn(3) })) : bn(2), ka: z(fit.kA_ursprung, 4), n: fit.n, von: z(fit.von, 0), bis: z(fit.bis, 0), kaf: z(fit.kA_frei, 4) }) + ' <button type="button" class="knopf-schlicht" id="knopf-ausgleich">' + t("ausgleich_nehmen") + "</button>";
      const kn = $("knopf-ausgleich"); if (kn) kn.addEventListener("click", () => { S.e.kAQuelle = "fest"; S.e.kA = fit.kA_ursprung; S.e.kAHerkunft = "ausgleich"; sichern(); alles(); $("knopf-info").innerHTML = t("ausgleich_genommen"); });
    } else ft.hidden = true;
    // Kernzahlen für das angeheftete Bild am Handy
    if ($("kern-leiste")) $("kern-leiste").innerHTML = (freigabe() && R) ? "<span>ϑ₁ <b>" + z(R.th1, 2) + " °C</b></span><span>ϑ₂ <b>" + z(R.th2, 2) + " °C</b></span><span>Δ <b>" + z(R.dT, 2) + " K</b></span>" : "";
    $("kernzahlen").innerHTML = (freigabe() && R) ? "<span>ϑ₁<b>" + z(R.th1, 2) + " °C</b></span><span>ϑ₂<b>" + z(R.th2, 2) + " °C</b></span><span>Δ<b>" + z(R.dT, 2) + " K</b></span>" : "";
  }
  const ZEIT = [0, 10, 20, 30, 40, 50, 60, 60];
  const schnittFrei = () => S.antworten.f1.fest || FRAGEN.some(f => f.id[0] === "v" && S.antworten[f.id].fest);
  const messFrei = () => S.antworten.f2.fest;      // G1-01, G4-01, G7-01: Lage der Punkte erst nach der Vorhersage zu Frage 2
  function messPunkte() {
    const p = [];
    const becher = [1, 2].concat(S.kurs.b3 ? [3] : []);
    for (const b of becher) S.kurs.werte["b" + b].forEach((v, i) => { if (v !== null && isFinite(v)) p.push({ b: b, t: ZEIT[i], th: v, nach: i === 7 }); });
    return p;
  }
  function lnPunkte() {        // Becher 2 (und 3, falls gezeigt), Zeilen 10 bis „60 vor der Milch“, je Becher mit eigenem Startwert (ZUSTAENDE.md 6)
    const u = S.kurs.u !== null ? S.kurs.u : S.e.thU, out = [];
    if (!messFrei()) return out;
    for (const b of [2].concat(S.kurs.b3 ? [3] : [])) {
      const w = S.kurs.werte["b" + b], th0 = w[0];
      if (th0 === null || !(th0 > u)) continue;
      for (let i = 1; i <= 6; i++) if (w[i] !== null && w[i] > u) out.push({ t: ZEIT[i], y: Math.log((w[i] - u) / (th0 - u)), th: w[i], b: b });
    }
    return out;
  }
  function ausgleichRechnen() {
    const lp = lnPunkte(); if (lp.length < 3) return null;
    const u = S.kurs.u !== null ? S.kurs.u : S.e.thU, th0 = u + 1;
    // ERW.ausgleich erwartet Temperaturen zu einem Startwert; aus y = ln((ϑ − ϑu)/(ϑ0 − ϑu)) zurückgerechnet (exakt, gleiche y)
    const extra = [...new Set(lp.map(p => p.b))].slice(1).map(() => [0, th0]);   // je weiterer Becher ein Startpunkt (0, 0) für die freie Gerade
    const f = ERW.ausgleich(lp.map(p => [p.t, u + (th0 - u) * Math.exp(p.y)]).concat(extra), th0, u, ERW.kapazitaeten(S.e).C_KB);
    f.n = lp.length;
    f.von = Math.min(...lp.map(p => p.t)); f.bis = Math.max(...lp.map(p => p.t));
    return f;
  }
  // ------------------------------------------------------------------ Kann-Punkte: Trinkzeit (M10), Becher kalt (M9), CSV (M11)
  const TRINK = 60;
  function zusatzZeichnen() {
    const el = $("zusatz-text"), teile = [];
    if (freigabe() && R && S.ansicht.vertiefung && S.ansicht.trinkzeit) {
      const tr = ERW.trinkzeit(S.e, TRINK), f = x => x === 0 ? nurText(t("trink_sofort")) : (isFinite(x) ? t("trink_nach", { t: z(x, 1) }) : nurText(t("trink_nie")));
      teile.push(t("trinkzeit_text", { a: f(tr.tasse1), b: f(tr.schwarz) }));
    }
    if (freigabe() && R && S.ansicht.vertiefung && S.ansicht.kalt && S.e.becher && S.e.kAQuelle === "fest") {
      const k = ERW.becherKalt(S.e);
      teile.push(t("kalt_text", { a: z(k.th1_0, 2), b: z(k.thK_0, 2), t: z(S.e.tEnd_min, 0), c: z(k.th1, 2), d: z(k.th2, 2), dt: z(k.dT, 2), dtv: z(R.dT, 2) }));
    }
    if (freigabe() && R && S.vergleich && !ERW.fehler(S.vergleich)) {
      const rv = ERW.auswerten(S.vergleich);
      teile.push(t("vergleich_text", { a: z(rv.th1, 2), b: z(rv.th2, 2), d: z(rv.dT, 2), t: z(S.vergleich.tEnd_min, 0) }));
    }
    el.hidden = !teile.length; el.innerHTML = teile.map(x => "<span>" + x + "</span>").join("<br>");
  }
  function csvBauen() {
    const de = S.sprache === "de", tr = de ? ";" : ",", zz = (x, n) => (x === null || x === undefined || !isFinite(x)) ? "" : HILFEN.zahlText(x, n, S.sprache).replace("\u2212", "-");
    const becher = [1, 2].concat(S.kurs.b3 ? [3] : []);
    const kopf = [nurText(t("csv_t")), nurText(t("csv_tasse1")), nurText(t("csv_tasse2"))].concat(becher.map(b => nurText(t("csv_becher", { n: b }))));
    const feld = x => /[",;\r\n]/.test(x) && x.indexOf(tr) >= 0 || /["\r\n]/.test(x) ? '"' + x.replace(/"/g, '""') + '"' : x;   // RFC 4180
    const zeilen = ["\ufeff" + kopf.map(feld).join(tr)];
    const tz = S.e.tEnd_min, mess = (b, tt, nach) => { const i = nach ? 7 : (tt % 10 === 0 && tt <= 60 ? tt / 10 : -1); return i >= 0 ? S.kurs.werte["b" + b][i] : null; };
    for (let tt = 0; tt <= Math.max(tz, 60); tt++) {
      const m1 = R && tt <= tz ? R.kurve1(tt) : null, m2 = R && tt <= tz ? R.kurve2(tt) : null;
      zeilen.push([String(tt), zz(m1, 2), zz(m2, 2)].concat(becher.map(b => zz(mess(b, tt, false), 2))).join(tr));
    }
    zeilen.push([feld(nurText(t("csv_nach_milch", { t: HILFEN.zahlText(tz, 0, S.sprache) }))), zz(R ? R.th1 : null, 2), zz(R ? R.th2 : null, 2)].concat(becher.map(b => zz(S.kurs.werte["b" + b][7], 2))).join(tr));
    return zeilen.join("\r\n") + "\r\n";
  }
  function csvLaden() {
    const blob = new Blob([csvBauen()], { type: "text/csv;charset=utf-8" }), url = URL.createObjectURL(blob), a = document.createElement("a");
    a.href = url; a.download = nurText(t("csv_datei")); document.body.appendChild(a); a.click(); a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
    $("mess-info").innerHTML = t("csv_fertig");
  }
  function wertetabelle() {
    const el = $("wertetabelle-inhalt");
    if (!freigabe() || !R) { el.innerHTML = '<p class="klein">' + t(freigabe() ? "dia_ungueltig" : "ergebnis_verdeckt") + "</p>"; return; }
    const mb = messFrei() ? [1, 2].concat(S.kurs.b3 ? [3] : []).filter(b => S.kurs.werte["b" + b].some(v => v !== null)) : [];
    let h = '<div class="tabelle-wrap"><table class="messtabelle"><thead><tr><th>' + t("werte_tabelle_kopf_t") + "</th><th>" + t("werte_tabelle_kopf_1") + "</th><th>" + t("werte_tabelle_kopf_2") + "</th>" + mb.map(b => "<th>" + t("mess_kopf_b" + b) + "</th>").join("") + "</tr></thead><tbody>";
    const tz = S.e.tEnd_min, schritte = [];
    for (let x = 0; x < tz; x += 5) schritte.push(x);
    schritte.push(tz);
    const mw = (b, x) => { const i = x % 10 === 0 && x <= 60 ? x / 10 : -1; const v = i >= 0 ? S.kurs.werte["b" + b][i] : null; return v === null ? "" : z(v, 1); };
    for (const x of schritte) h += "<tr><td>" + z(x, 0) + "</td><td>" + z(R.kurve1(x), 2) + "</td><td>" + z(R.kurve2(x), 2) + "</td>" + mb.map(b => "<td>" + mw(b, x) + "</td>").join("") + "</tr>";
    h += "<tr><td>" + nurText(t("csv_nach_milch", { t: z(tz, 0) })) + "</td><td>" + z(R.th1, 2) + "</td><td>" + z(R.th2, 2) + "</td>" + mb.map(b => "<td>" + (S.kurs.werte["b" + b][7] === null || tz !== 60 ? "" : z(S.kurs.werte["b" + b][7], 1)) + "</td>").join("") + "</tr>";
    el.innerHTML = h + "</tbody></table></div>";
  }

  // ------------------------------------------------------------------ Energie und Bilanzraum
  function energieZeichnen() {
    const el = $("energie-inhalt");
    if (!freigabe() || !R) { el.innerHTML = '<p class="klein">' + t(freigabe() ? "dia_ungueltig" : "ergebnis_verdeckt") + "</p>"; $("energie").removeAttribute("aria-label"); return; }
    // Gewählt nach Prototypvergleich (simulation/PROTOTYPEN.md): Säulen auf gemeinsamer Nulllinie, Bezugslinie auf Höhe Q1, Klammer Q2 − Q1
    const q1 = R.Q1, q2 = R.Q2, m = Math.max(q1, q2, 1), W = 240, H = 156, B = 122, hoch = 92;
    const Yb = q => B - hoch * q / m, dq0 = q2 - q1;
    let s = '<svg viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + esc(nurText(t("energie_aria", { q1: z(q1, 2), q2: z(q2, 2) }))) + '"><defs><pattern id="muster-q2" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" stroke="#222" stroke-width="2"/></pattern></defs>';
    s += '<line x1="20" x2="200" y1="' + B + '" y2="' + B + '" stroke="#5a6b7f"/>';
    s += '<rect x="40" y="' + Yb(q1).toFixed(1) + '" width="46" height="' + (B - Yb(q1)).toFixed(1) + '" fill="#8b5a2b"/>';
    s += '<rect x="118" y="' + Yb(q2).toFixed(1) + '" width="46" height="' + (B - Yb(q2)).toFixed(1) + '" fill="url(#muster-q2)" stroke="#222" stroke-width="1.5"/>';
    s += '<line x1="40" x2="172" y1="' + Yb(q1).toFixed(1) + '" y2="' + Yb(q1).toFixed(1) + '" stroke="#173d5e" stroke-dasharray="4 3"/>';
    s += '<path d="M 170 ' + Yb(q2).toFixed(1) + " h 6 V " + Yb(q1).toFixed(1) + ' h -6" fill="none" stroke="#173d5e" stroke-width="1.6"/>';
    s += '<text x="180" y="' + ((Yb(q1) + Yb(q2)) / 2 + 4).toFixed(1) + '" font-size="14" font-weight="600" fill="#173d5e">' + (dq0 >= 0 ? "+" : "") + z(dq0, 2) + " kJ</text>";
    s += '<text x="63" y="' + (Yb(q1) - 6).toFixed(1) + '" text-anchor="middle" font-size="15">' + z(q1, 2) + " kJ</text>";
    s += '<text x="141" y="' + (Math.min(Yb(q2), Yb(q1)) - 6).toFixed(1) + '" text-anchor="middle" font-size="15">' + z(q2, 2) + " kJ</text>";
    s += '<text x="63" y="' + (B + 19) + '" text-anchor="middle" font-size="15">' + esc(nurText(t("tasse_n", { n: 1 }))) + "</text>";
    s += '<text x="141" y="' + (B + 19) + '" text-anchor="middle" font-size="15">' + esc(nurText(t("tasse_n", { n: 2 }))) + "</text></svg>";
    const dq = q2 - q1;
    const satz = Math.abs(R.milch) > 1e-12
      ? t("energie_satz_milch", { dq: z(dq, 2), m: z(R.milch, 2), s: z(dq + R.milch, 2), dt: z(R.dT, 2) })
      : t("energie_satz", { dq: z(dq, 2), dt: z(R.dT, 2) });
    el.innerHTML = s + '<p class="energie-satz">' + satz + "</p>";
  }
  function bilanzZeichnen() {
    const box = $("bilanz");
    box.hidden = !(S.ansicht.vertiefung && freigabe() && R);
    if (box.hidden) return;
    const tz = S.e.tEnd_min, q1 = R.qdot1(tz), q2 = R.qdot2(tz), m = Math.max(q1, q2, 0.1);
    const breite = q => 1.5 + 7 * q / m;
    let s = '<svg viewBox="0 0 200 104" role="img" aria-label="' + esc(nurText(t("bilanz_titel"))) + ': Q̇1 ' + z(q1, 2) + " W, Q̇2 " + z(q2, 2) + ' W"><defs><marker id="pfeil" markerWidth="5" markerHeight="5" refX="3" refY="2.5" orient="auto"><path d="M0,0 L5,2.5 L0,5 z" fill="#173d5e"/></marker></defs>';
    [[18, "#8b5a2b", q1, nurText(t("tasse_n", { n: 1 }))], [110, "#222", q2, nurText(t("tasse_n", { n: 2 }))]].forEach(([x, c, q, n]) => {
      s += '<path d="M' + x + " 24 L" + (x + 6) + " 72 L" + (x + 44) + " 72 L" + (x + 50) + ' 24" fill="#f3e9df" stroke="' + c + '" stroke-width="2"/>';
      s += '<rect x="' + (x - 6) + '" y="16" width="62" height="64" fill="none" stroke="#173d5e" stroke-dasharray="5 4"/>';
      s += '<line x1="' + (x + 58) + '" y1="46" x2="' + (x + 80) + '" y2="46" stroke="#173d5e" stroke-width="' + breite(q).toFixed(1) + '" marker-end="url(#pfeil)"/>';
      s += '<text x="' + (x + 25) + '" y="94" text-anchor="middle" font-size="11">' + esc(n) + " · " + z(q, 2) + " W</text>";
    });
    $("bilanz-inhalt").innerHTML = s + "</svg>";
  }

  // ------------------------------------------------------------------ Regler
  const wertText = (r, w) => z(w, r.stellen) + " " + (r.einheit === "W/K" ? nurText(t("einheit_wk")) : r.einheit);   // M-12
  function reglerHtml(r) {
    const gesperrt = r.id === "tEnd" && !reglerTZfrei();
    const wert = r.faktor ? S.e[r.key] * r.faktor : S.e[r.key];
    const name = t("regler_" + r.id) + " " + r.mathml + " [" + einheit(r.einheit) + "]";
    let h = '<div class="regler' + (gesperrt ? " gesperrt" : "") + '" data-regler="' + r.id + '">';
    h += '<div class="regler-kopf"><label class="regler-name" for="r-' + r.id + '" id="rl-' + r.id + '">' + name + "</label>";
    h += '<button type="button" class="hilfe-knopf" aria-expanded="false" aria-controls="h-' + r.id + '" data-hilfe="' + r.id + '"><span aria-hidden="true">?</span><span class="nur-leser">' + nurText(t("hilfe_zu", { name: t("regler_" + r.id) })) + "</span></button></div>";
    h += '<p class="hilfe-text" id="h-' + r.id + '" hidden>' + t("hilfe_" + r.id) + "</p>";
    h += '<div class="regler-zeile"><button type="button" class="pm" data-pm="-1" data-r="' + r.id + '" aria-label="' + esc(nurText(t("knopf_minus")) + ": " + nurText(t("regler_" + r.id))) + '"' + (gesperrt ? " disabled" : "") + ">−</button>";
    h += '<input type="range" id="r-' + r.id + '" min="' + r.min + '" max="' + r.max + '" step="' + r.schritt + '" value="' + wert + '" aria-valuetext="' + esc(wertText(r, wert)) + '" aria-label="' + esc(nurText(t("regler_" + r.id)) + " (" + (r.einheit === "W/K" ? nurText(t("einheit_wk")) : r.einheit) + ")") + '"' + (gesperrt ? " disabled" : "") + ' aria-describedby="rf-' + r.id + '">';
    h += '<button type="button" class="pm" data-pm="1" data-r="' + r.id + '" aria-label="' + esc(nurText(t("knopf_plus")) + ": " + nurText(t("regler_" + r.id))) + '"' + (gesperrt ? " disabled" : "") + ">+</button>";
    h += '<input type="text" class="zahlfeld" inputmode="decimal" autocomplete="off" id="z-' + r.id + '" value="' + z(wert, r.stellen) + '" aria-label="' + esc(nurText(t("feld_aria", { name: t("regler_" + r.id) }))) + " [" + esc(r.einheit) + ']"' + (gesperrt ? " disabled" : "") + ' aria-describedby="rf-' + r.id + '"></div>';
    h += '<p class="feld-fehler' + (gesperrt ? " neutral" : "") + '" id="rf-' + r.id + '" aria-live="polite">' + (gesperrt ? t(freigabe() ? "regler_gesperrt" : "regler_gesperrt_start") : "") + "</p></div>";
    return h;
  }
  function reglerSetzen(r, wertAnzeige, quelle) {
    const w = r.faktor ? wertAnzeige / r.faktor : wertAnzeige;
    S.e[r.key] = w;
    if (r.id === "kA") { S.e.kAQuelle = "fest"; S.e.kAHerkunft = "eigen"; }
    rechnen(); sichern();
    teilZeichnen(quelle === "zahl" ? "z-" + r.id : (quelle === "pm" ? null : "r-" + r.id));
    const rf = $("rf-" + r.id); if (rf && !rf.classList.contains("neutral")) rf.innerHTML = FEHLER ? t("fehler_am_feld") : "";
  }
  function reglerEreignisse(wurzel) {
    for (const r of REGLER_DEF.regler) {
      const range = wurzel.querySelector("#r-" + r.id), feld = wurzel.querySelector("#z-" + r.id);
      if (!range) continue;
      range.addEventListener("input", () => { reglerSetzen(r, Number(range.value), "range"); });
      range.addEventListener("change", ansagen);
      feld.addEventListener("change", () => feldPruefen(r, feld));
      feld.addEventListener("keydown", ev => { if (ev.key === "Enter") feldPruefen(r, feld); });
    }
    for (const b of wurzel.querySelectorAll(".pm")) b.addEventListener("click", () => {
      const r = REG[b.getAttribute("data-r")], alt = r.faktor ? S.e[r.key] * r.faktor : S.e[r.key];
      const neu = Math.min(r.max, Math.max(r.min, Math.round((alt + Number(b.getAttribute("data-pm")) * r.schritt) / r.schritt) * r.schritt));
      reglerSetzen(r, Number(neu.toFixed(6)), "pm"); ansagen();
    });
    for (const b of wurzel.querySelectorAll("[data-hilfe]")) b.addEventListener("keydown", ev => { if (ev.key === "Escape") { $("h-" + b.getAttribute("data-hilfe")).hidden = true; b.setAttribute("aria-expanded", "false"); } });
    for (const b of wurzel.querySelectorAll("[data-hilfe]")) b.addEventListener("click", () => {
      const p = $("h-" + b.getAttribute("data-hilfe")), auf = p.hidden; p.hidden = !auf; b.setAttribute("aria-expanded", auf ? "true" : "false");
    });
  }
  function feldPruefen(r, feld) {
    const l = HILFEN.zahlLesen(feld.value), f = $("rf-" + r.id);
    let text = "";
    if (l.grund === "tausender") text = t("feld_tausender");
    else if (!isFinite(l.wert)) text = t("feld_keine_zahl", { beispiel: z(r.standard !== null ? r.standard : ERW.KA_AUFGABE, r.stellen > 2 ? 2 : r.stellen) });
    else if (l.wert < r.min || l.wert > r.max) text = t("feld_bereich", { min: z(r.min, r.stellen > 2 ? 2 : r.stellen), max: z(r.max, r.stellen > 2 ? 2 : r.stellen), einheit: r.einheit });
    if (text) { feld.setAttribute("aria-invalid", "true"); f.innerHTML = text; return; }
    feld.removeAttribute("aria-invalid"); f.innerHTML = "";
    reglerSetzen(r, Number(l.wert.toFixed(r.stellen)), "zahl"); ansagen();
  }
  function infoKastenInhalt() {
    const a30 = R ? t("kA_anzeige_30", { a: z(S.e.thK0, 1), b: z(R.schwarz30, 2), tau: z(R.tauMin, 1) }) : "";
    if (S.e.kAQuelle !== "fest") return a30;
    const vor = S.e.kAHerkunft.indexOf("vor:") === 0 ? ERW.VOREINSTELLUNGEN.find(v => "vor:" + v.id === S.e.kAHerkunft) : null;
    return a30 + (vor ? "<br>" + t("vor_text_" + vor.id) + (vor.art === "richtwert" ? " *" : "") : "") +
      '<br><span class="klein">* ' + t("kA_richtwert") + ". " + t("vor_kein_thermo_deckel") + "</span>";
  }
  function reglerZeichnen() {
    $("regler-pflicht").innerHTML = '<div class="regler-gitter">' + reglerHtml(REG.tEnd) + "</div>";
    reglerEreignisse($("regler-pflicht"));
    const vt = $("vertiefung");
    vt.hidden = !freigabe();
    vt.open = !!S.ansicht.vertiefung;
    $("vertiefung-frueh").hidden = !(S.ansicht.vertiefung && !S.antworten.f1.fest);
    $("ansichten").hidden = !(S.ansicht.vertiefung && freigabe());
    for (const b of document.querySelectorAll("[data-ansicht]")) b.setAttribute("aria-pressed", b.getAttribute("data-ansicht") === S.ansicht.diagramm ? "true" : "false");
    if (!freigabe()) { $("vertiefung-inhalt").innerHTML = ""; return; }
    let h = '<div class="kern-leiste" id="kern-leiste" aria-hidden="true"></div><p class="hinweis">' + t("v_einleitung") + "</p>";
    h += '<div class="regler-gitter">';
    h += '<div class="gruppe"><h3 class="gruppe-titel">' + t("gruppe_kaffee") + "</h3>" + reglerHtml(REG.VK) + reglerHtml(REG.thK0) + "</div>";
    h += '<div class="gruppe"><h3 class="gruppe-titel">' + t("gruppe_milch") + "</h3>" + reglerHtml(REG.VM) + reglerHtml(REG.thM) +
      '<label class="schalter"><input type="checkbox" id="s-milch2Raum"' + (S.e.milch2Raum ? " checked" : "") + "> " + t("schalter_milch2Raum") + "</label>" + "</div>";
    h += '<div class="gruppe"><h3 class="gruppe-titel">' + t("gruppe_tasse") + "</h3>" + reglerHtml(REG.thU);
    h += '<fieldset class="gruppe"><legend class="regler-name">' + t("kA_quelle") + '</legend><div class="radio-zeile">' +
      '<label><input type="radio" name="kaq" value="fest"' + (S.e.kAQuelle === "fest" ? " checked" : "") + "> " + t("kA_quelle_fest") + "</label>" +
      '<label><input type="radio" name="kaq" value="messung"' + (S.e.kAQuelle === "messung" ? " checked" : "") + "> " + t("kA_quelle_messung") + "</label></div>";
    h += '<p class="hinweis">' + t(S.e.kAQuelle === "fest" ? "kA_quelle_info_fest" : "kA_quelle_info_messung") + "</p></fieldset>";
    if (S.e.kAQuelle === "fest") {
      h += '<p class="regler-name">' + t("kA_voreinstellungen") + '</p><div class="voreinstellungen" role="group" aria-label="' + esc(nurText(t("kA_voreinstellungen"))) + '">';
      for (const v of ERW.VOREINSTELLUNGEN) h += '<button type="button" class="umschalter" data-vor="' + v.id + '" aria-pressed="' + (S.e.kAHerkunft === "vor:" + v.id ? "true" : "false") + '">' + t("vor_" + v.id) + (v.art === "richtwert" ? "*" : "") + "</button>";
      h += "</div>" + reglerHtml(REG.kA);
      h += '<div class="info-kasten" id="info-kasten">' + infoKastenInhalt() + "</div>";
    } else {
      h += reglerHtml(REG.thMess);
      h += '<div class="info-kasten" id="info-kasten">' + infoKastenInhalt() + "</div>";
    }
    h += '<label class="schalter"><input type="checkbox" id="s-becher"' + (S.e.becher ? " checked" : "") + "> " + t("schalter_becher") + "</label>";
    if (S.e.becher) h += reglerHtml(REG.mB);
    h += "</div>";
    const kaltMoeglich = S.e.becher && S.e.kAQuelle === "fest";
    h += '<div class="gruppe"><h3 class="gruppe-titel">' + t("gruppe_weitere") + "</h3>" + reglerHtml(REG.kA1) +
      '<label class="schalter"><input type="checkbox" id="s-trink"' + (S.ansicht.trinkzeit ? " checked" : "") + "> " + t("schalter_trinkzeit") + "</label>" +
      '<label class="schalter"><input type="checkbox" id="s-kalt"' + (S.ansicht.kalt && kaltMoeglich ? " checked" : "") + (kaltMoeglich ? "" : " disabled") + ' aria-describedby="kalt-hinweis"> ' + t("schalter_kalt") + "</label>" +
      '<p class="klein" id="kalt-hinweis">' + t("kalt_nur") + "</p></div>";
    h += '<div class="gruppe"><h3 class="gruppe-titel">' + t("gruppe_fortgeschritten") + '</h3><div class="knopfzeile"><button type="button" class="knopf-schlicht" id="knopf-vergleich">' + t(S.vergleich ? "knopf_vergleich_weg" : "knopf_vergleich") + "</button></div>" + (S.vergleich ? '<p class="klein">' + t("dia_vergleich") + "</p>" : "") + "</div>";
    h += "</div>";
    const vi = $("vertiefung-inhalt");
    vi.innerHTML = h;
    reglerEreignisse(vi);
    $("s-milch2Raum").addEventListener("change", ev => { S.e.milch2Raum = ev.target.checked; rechnen(); sichern(); teilZeichnen("s-milch2Raum"); ansagen(); });
    $("s-trink").addEventListener("change", ev => { S.ansicht.trinkzeit = ev.target.checked; sichern(); teilZeichnen("s-trink"); });
    $("s-kalt").addEventListener("change", ev => { S.ansicht.kalt = ev.target.checked; sichern(); teilZeichnen("s-kalt"); });
    $("s-becher").addEventListener("change", ev => { S.e.becher = ev.target.checked; rechnen(); sichern(); alles(); fokus("s-becher"); ansagen(); });
    for (const r of vi.querySelectorAll('input[name="kaq"]')) r.addEventListener("change", () => {
      if (r.value === "fest" && R) { S.e.kA = R.kA; S.e.kAHerkunft = "eigen"; }
      if (r.value === "messung" && R) { S.e.thMess = Math.min(90, Math.max(30, R.thMessModell)); S.e.kAHerkunft = "messung"; }
      S.e.kAQuelle = r.value; rechnen(); sichern(); alles(); const neu = document.querySelector('input[name="kaq"][value="' + r.value + '"]'); if (neu) neu.focus();
    });
    for (const b of vi.querySelectorAll("[data-vor]")) b.addEventListener("click", () => {
      const v = ERW.VOREINSTELLUNGEN.find(x => x.id === b.getAttribute("data-vor"));
      S.e.kAQuelle = "fest"; S.e.kA = v.faktor * ERW.KA_AUFGABE; S.e.kAHerkunft = "vor:" + v.id; rechnen(); sichern(); alles(); fokus(b.id || null); ansagen();
      const neu = document.querySelector('[data-vor="' + v.id + '"]'); if (neu) neu.focus();
    });
    $("knopf-vergleich").addEventListener("click", () => { S.vergleich = S.vergleich ? null : JSON.parse(JSON.stringify(S.e)); alles(); fokus("knopf-vergleich"); });
  }

  // ------------------------------------------------------------------ Rechenwerte und Ansage
  function rechenwerteZeichnen() {
    const fehler = $("einstellung-fehler");
    fehler.hidden = !(freigabe() && FEHLER);
    if (freigabe() && FEHLER && fehler.getAttribute("data-code") !== FEHLER) { fehler.innerHTML = t("fehler_" + FEHLER); fehler.setAttribute("data-code", FEHLER); }
    if (!FEHLER) fehler.removeAttribute("data-code");
    const dl = $("rechenwerte-liste");
    $("rechenwerte-bezug").textContent = (freigabe() && R) ? nurText(t("rw_bezug", { t: z(S.e.tEnd_min, 0) })) : "";
    if (freigabe() && !R) { dl.innerHTML = '<div class="breit"><dt>' + t("rw_noch_nicht") + "</dt><dd>" + t("dia_ungueltig") + "</dd></div>"; return; }
    if (!freigabe() || !R) { dl.innerHTML = '<div class="breit"><dt>' + t("rw_noch_nicht") + "</dt><dd>" + t("ergebnis_verdeckt") + "</dd></div>"; return; }
    const satz = R.dT > 0.005 ? t("rw_satz_1") : (R.dT < -0.005 ? t("rw_satz_2") : t("rw_satz_gleich"));
    const herkunft = S.e.kAQuelle === "messung" ? t("rw_kA_herkunft_messung") : (S.e.kAHerkunft === "ausgleich" ? t("rw_kA_herkunft_ausgleich") :
      (S.e.kAHerkunft.indexOf("vor:") === 0 ? t("rw_kA_herkunft_vor", { name: nurText(t("vor_" + S.e.kAHerkunft.slice(4))) }) : t("rw_kA_herkunft_fest")));
    let h = "<div><dt>" + t("rw_tasse1") + "</dt><dd>" + z(R.th1, 2) + " °C</dd></div>";
    h += "<div><dt>" + t("rw_tasse2") + "</dt><dd>" + z(R.th2, 2) + " °C</dd></div>";
    if (S.kurs.b3) h += '<div class="breit"><dt>' + t("rw_becher3") + "</dt><dd>" + z(R.th2Raum, 2) + " °C</dd></div>";
    h += '<div class="breit"><dt>' + t("rw_unterschied") + "</dt><dd>" + z(R.dT, 2) + " K · " + satz + "</dd></div>";
    if (S.kurs.b3) h += '<div class="breit"><dt>' + t("rw_unterschied_b3") + "</dt><dd>" + z(R.th1 - R.th2Raum, 2) + " K</dd></div>";
    h += "<div><dt>" + t("rw_schnitt") + "</dt><dd>" + (!schnittFrei() ? t("rw_schnitt_spaeter") : (isFinite(R.tSchnitt) && R.tSchnitt < S.e.tEnd_min ? t("rw_schnitt_wert", { t: z(R.tSchnitt, 1) }) : t("rw_schnitt_kein"))) + "</dd></div>";
    h += "<div><dt>" + t("rw_Q") + "</dt><dd>" + z(R.Q1, 2) + " / " + z(R.Q2, 2) + " kJ</dd></div>";
    h += "<div><dt>" + t("rw_kA") + "</dt><dd>" + z(R.kA, 4) + " " + einheit("W/K") + '<br><span class="klein">' + herkunft + "</span></dd></div>";
    h += "<div><dt>" + t("rw_misch") + "</dt><dd>" + z(R.th10, 2) + " °C</dd></div>";
    const a = S.antworten.start;
    h += '<div class="breit"><dt>' + t("rw_vorhersage") + "</dt><dd>" + esc(vorhersageText(frage("start"), a)) + "</dd></div>";
    dl.innerHTML = h;
  }
  let ansageZeit = null;
  function ansagen(festgehalten) {
    clearTimeout(ansageZeit);
    ansageZeit = setTimeout(() => {
      $("ansage").textContent = (freigabe() && R) ? (festgehalten === true ? nurText(t("status_festgehalten")) + " " : "") + nurText(t("status_ansage", { a: z(R.th1, 2), b: z(R.th2, 2), d: z(R.dT, 2) })) : "";
    }, 250);
  }

  // ------------------------------------------------------------------ Messblatt
  const ZEILEN_NAME = () => ["0", "10", "20", "30", "40", "50", nurText(t("mess_zeile_60v")), nurText(t("mess_zeile_60n"))];
  function messblattZeichnen() {
    const el = $("messblatt-inhalt");
    const becher = [1, 2].concat(S.kurs.b3 ? [3] : []);
    let h = '<div class="tabelle-wrap" role="region" aria-labelledby="mess-titel"><table class="messtabelle"><thead><tr><th scope="col">' + t("mess_kopf_t") + "</th>";
    for (const b of becher) h += '<th scope="col">' + t("mess_kopf_b" + b) + "</th>";
    h += "</tr></thead><tbody>";
    ZEILEN_NAME().forEach((name, i) => {
      h += '<tr><th scope="row">' + esc(name) + "</th>";
      for (const b of becher) {
        const v = S.kurs.werte["b" + b][i], aus = b === 1 && i === 7;
        h += '<td class="zelle"><input type="text" inputmode="decimal" autocomplete="off" data-b="' + b + '" data-i="' + i + '" value="' + (v === null ? "" : z(v, Math.round(v * 100) % 10 === 0 ? (Math.round(v * 10) % 10 === 0 ? 1 : 1) : 2)) + '"' + (aus ? " disabled" : "") +
          ' aria-label="' + esc(nurText(t("mess_feld_aria", { becher: nurText(t("mess_kopf_b" + b)).replace(/ \[.*\]$/, ""), zeile: i < 6 ? name + " min" : name }))) + '"></td>';
      }
      h += "</tr>";
    });
    h += "</tbody></table></div>";
    h += '<p class="feld-fehler" id="mess-fehler" aria-live="polite"></p>';
    h += '<div class="mess-zusatz"><label class="feld">' + t("mess_raum") + ' <input type="text" inputmode="decimal" id="mess-u" value="' + (S.kurs.u === null ? "" : z(S.kurs.u, 1)) + '"></label>';
    h += '<label class="feld">' + t("mess_milch") + ' <input type="text" inputmode="decimal" id="mess-m" value="' + (S.kurs.m === null ? "" : z(S.kurs.m, 1)) + '"></label>';
    h += '<label class="schalter"><input type="checkbox" id="mess-d"' + (S.kurs.d ? " checked" : "") + "> " + t("mess_deckel") + "</label>";
    h += '<label class="schalter"><input type="checkbox" id="mess-b3"' + (S.kurs.b3 ? " checked" : "") + "> " + t("mess_becher3") + "</label></div>";
    if (S.kurs.d) h += '<p class="hinweis">' + t("mess_deckel_hinweis") + "</p>";
    h += '<div class="knopfzeile">' + (freigabe() ? '<button type="button" class="knopf-zweit" id="mess-ueber">' + t("mess_uebernehmen") + "</button>" : "") + '<button type="button" class="knopf-schlicht" id="mess-link">' + t("mess_teilen") + '</button><button type="button" class="knopf-schlicht" id="mess-weg">' + t("mess_loeschen") + '</button><button type="button" class="knopf-schlicht" id="mess-csv">' + t("csv_knopf") + "</button></div>";
    h += '<p class="hinweis" id="mess-info" role="status"></p><div id="link-ausgabe"></div>';
    el.innerHTML = h;
    for (const inp of el.querySelectorAll(".zelle input")) inp.addEventListener("change", () => {
      const b = inp.getAttribute("data-b"), i = Number(inp.getAttribute("data-i")), l = HILFEN.zahlLesen(inp.value);
      if (inp.value.trim() === "") { S.kurs.werte["b" + b][i] = null; inp.removeAttribute("aria-invalid"); inp.removeAttribute("aria-describedby"); $("mess-fehler").textContent = ""; }
      else if (!isFinite(l.wert) || l.wert < 0 || l.wert > 100) { inp.setAttribute("aria-invalid", "true"); inp.setAttribute("aria-describedby", "mess-fehler"); $("mess-fehler").innerHTML = esc(inp.getAttribute("aria-label")) + ": " + t(l.grund === "tausender" ? "feld_tausender" : "mess_ungueltig"); return; }
      else { S.kurs.werte["b" + b][i] = Math.round(l.wert * 100) / 100; inp.removeAttribute("aria-invalid"); inp.removeAttribute("aria-describedby"); $("mess-fehler").textContent = ""; }
      sichern(); teilZeichnen("messblatt"); frageleisteStill();
    });
    const feldZahl = (id, key, lo, hi) => $(id).addEventListener("change", () => {
      const l = HILFEN.zahlLesen($(id).value);
      if ($(id).value.trim() === "") S.kurs[key] = null;
      else if (!isFinite(l.wert) || l.wert < lo || l.wert > hi) { $(id).setAttribute("aria-invalid", "true"); $("mess-fehler").innerHTML = t("feld_bereich", { min: lo, max: hi, einheit: "°C" }); return; }
      else S.kurs[key] = l.wert;
      $(id).removeAttribute("aria-invalid"); $("mess-fehler").textContent = ""; sichern(); teilZeichnen("messblatt"); frageleisteStill();
    });
    feldZahl("mess-u", "u", 5, 40); feldZahl("mess-m", "m", 0, 70);
    $("mess-d").addEventListener("change", ev => { S.kurs.d = ev.target.checked; sichern(); alles(); fokus("mess-d"); });
    $("mess-csv").addEventListener("click", csvLaden);
    $("mess-b3").addEventListener("change", ev => { S.kurs.b3 = ev.target.checked; sichern(); alles(); fokus("mess-b3"); });
    if ($("mess-ueber")) $("mess-ueber").addEventListener("click", () => { const r = uebernehmen(false); alles(); $("mess-info").innerHTML = r.text; fokus("mess-ueber"); });
    $("mess-link").addEventListener("click", linkTeilen);
    $("mess-weg").addEventListener("click", () => bestaetigen(t("mess_loeschen_frage"), () => { S.kurs = leererKurs(); sichern(); alles(); fokus("mess-weg"); }));
  }
  // Übernahme wie D116: Mittelwerte ungerundet prüfen und unverändert übernehmen oder gar nicht
  function uebernehmen(still) {
    const becher = [2].concat(S.kurs.b3 ? [3] : []);
    const mittel = i => { const v = becher.map(b => S.kurs.werte["b" + b][i]).filter(x => x !== null); return v.length ? v.reduce((a, b) => a + b, 0) / v.length : null; };
    const start = mittel(0), zehn = mittel(1);
    const u = S.kurs.u !== null ? S.kurs.u : S.e.thU, m = S.kurs.m !== null ? S.kurs.m : S.e.thM;
    if (start === null || zehn === null) return { ok: false, text: t("mess_nicht_uebernommen", { grund: t("mess_grund_fehlt") }) };
    const neu = Object.assign({}, S.e, { thK0: start, thMess: zehn, thU: u, thM: m, kAQuelle: "messung", kAHerkunft: "messung", becher: true, tEnd_min: 60, milch2Raum: false });
    const fehlerBereich = start < REG.thK0.min || start > REG.thK0.max || zehn < REG.thMess.min || zehn > REG.thMess.max || u < REG.thU.min || u > REG.thU.max || m < REG.thM.min || m > REG.thM.max;
    if (fehlerBereich) {
      const pruef = [["mess_was_start", start, REG.thK0], ["mess_was_zehn", zehn, REG.thMess], ["mess_was_raum", u, REG.thU], ["mess_was_milch", m, REG.thM]].find(([, w, r]) => w < r.min || w > r.max);
      return { ok: false, text: t("mess_nicht_uebernommen", { grund: t("mess_grund_wert", { was: t(pruef[0]), wert: z(pruef[1], 1), min: z(pruef[2].min, 0), max: z(pruef[2].max, 0) }) }) };
    }
    if (ERW.fehler(neu)) return { ok: false, text: t("mess_nicht_uebernommen", { grund: t("fehler_" + ERW.fehler(neu)) }) };
    S.e = neu; rechnen(); sichern();
    return { ok: true, text: t("mess_uebernommen", { a: z(start, 2), b: z(zehn, 2), u: z(u, 1), m: z(m, 1) }) };
  }
  function linkTeilen() {
    if (!kursAnzahl()) { $("mess-info").innerHTML = t("link_leer"); return; }
    const basis = location.href.split("#")[0].replace(/([?&])lang=(de|en)(&|$)/, (m, a, b, c) => (c ? a : "")).replace(/\?$/, "");
    const link = basis + "#" + HILFEN.kurslinkBauen(S.kurs);
    const zeige = () => { $("link-ausgabe").innerHTML = (location.protocol === "file:" ? '<p class="hinweis">' + t("link_nur_lokal") + "</p>" : "") + '<p class="hinweis">' + t("link_anzeigen") + '</p><p class="link-ausgabe">' + esc(link) + "</p>"; };
    try { navigator.clipboard.writeText(link).then(() => { $("mess-info").innerHTML = t("link_kopiert"); zeige(); }, zeige); } catch (e) { zeige(); }
  }
  function linkGrund(g) {      // Grund aus HILFEN.kurslinkLesen in Worten (ZUSTAENDE.md, Abschnitt 5)
    let m;
    if (g === "zu_lang" || g === "u" || g === "m" || g === "d" || g === "b") return t("link_grund_" + g);
    if (g === "b1:8") return t("link_grund_b1_8");
    if ((m = /^b([123]):anzahl$/.exec(g))) return t("link_grund_anzahl", { becher: m[1] });
    if ((m = /^b([123]):([1-8])$/.exec(g))) return t("link_grund_wert", { becher: m[1], nr: m[2] });
    if ((m = /^b([123])$/.exec(g))) return t("link_grund_becher", { becher: m[1] });
    return t("link_grund_aufbau");
  }
  function kurslinkPruefen() {
    const l = HILFEN.kurslinkLesen(location.hash), b = $("link-banner");
    if (l.art === "leer" || (l.art === "fremd" && !/^#kurs/i.test(location.hash))) return;
    const weg = () => { try { history.replaceState(null, "", location.pathname + location.search); } catch (e) { } };
    if (l.art !== "ok") { b.hidden = false; b.setAttribute("role", "alert"); b.innerHTML = "<p>" + (l.art === "fremd" ? t("link_fremd") : t("link_defekt", { grund: linkGrund(l.grund) })) + "</p>"; weg(); return; }
    b.hidden = false;
    b.innerHTML = '<p id="link-frage">' + t("link_frage") + '</p><div class="knopfzeile"><button type="button" class="knopf-zweit" id="link-ja">' + t("link_ja") + '</button><button type="button" class="knopf-schlicht" id="link-nein">' + t("link_nein") + "</button></div>";
    b.setAttribute("role", "region"); b.setAttribute("aria-labelledby", "link-frage");
    const fertig = schluessel => { b.innerHTML = '<p id="link-ende" tabindex="-1">' + t(schluessel) + "</p>"; b.setAttribute("aria-labelledby", "link-ende"); $("ansage").textContent = nurText(t(schluessel)); $("link-ende").focus(); };   // G5-24
    $("link-ja").addEventListener("click", () => { S.kurs = l.kurs; sichern(); weg(); alles(); fertig("link_ok"); });
    $("link-nein").addEventListener("click", () => { weg(); fertig("link_abgelehnt"); });
    b.addEventListener("keydown", ev => { if (ev.key === "Escape" && $("link-nein")) $("link-nein").click(); });
  }

  // ------------------------------------------------------------------ Reiter
  function reiterZeichnen() {
    for (const b of document.querySelectorAll("#reiter-leiste [role=tab]")) {
      const aktiv = b.getAttribute("data-tab") === S.ansicht.reiter;
      b.setAttribute("aria-selected", aktiv ? "true" : "false"); b.tabIndex = aktiv ? 0 : -1;
      $("panel-" + b.getAttribute("data-tab")).hidden = !aktiv;
    }
    // Versuche
    let h = t("text_probier");
    for (const f of FRAGEN) {
      const a = S.antworten[f.id], offen = f.id === S.aktuell;
      const gesperrt = f.id !== "start" && !freigabe();
      const status = a.fest ? SYM.haken + " " + esc(vorhersageText(f, a)) : (gesperrt ? t("gesperrt_nach_start") : "");
      const nr = f.id === "start" ? t("leiste_start") : (f.id[0] === "f" ? t("leiste_frage", { n: f.id.slice(1) }) : t("leiste_vertiefung") + " " + f.id.toUpperCase());
      h += '<details class="karte" data-karte="' + f.id + '"' + (offen ? " open" : "") + "><summary>" + nr + " · " + t(f.titel) + '<span class="karte-status">' + status + "</span></summary>";
      if (!gesperrt) {
        h += "<p>" + t(f.text) + '</p><p class="hinweis"><strong>' + t("ausgangslage") + ":</strong> " + t(f.ausgang) + "</p>";
        h += '<div class="knopfzeile"><button type="button" class="knopf-schlicht" data-zur="' + f.id + '">' + t("knopf_zur_karte") + "</button>" +
          (a.fest ? '<button type="button" class="knopf-zweit" data-aufl="' + f.id + '" aria-expanded="' + (a.aufl ? "true" : "false") + '" aria-controls="aufl-karte-' + f.id + '">' + t(a.aufl ? "knopf_aufloesung_zu" : "knopf_aufloesung") + "</button>" : "") + "</div>";
        if (a.fest && a.aufl) h += '<div class="aufloesung" id="aufl-karte-' + f.id + '">' + vergleichHtml(f, a) + "<p>" + t(f.aufl) + "</p></div>";
      }
      h += "</details>";
    }
    h += '<div class="knopfzeile"><button type="button" class="knopf-schlicht" id="knopf-fragen-weg">' + t("knopf_fragen_zuruecksetzen") + "</button></div>";
    $("panel-versuche").innerHTML = h;
    for (const b of $("panel-versuche").querySelectorAll("[data-zur]")) b.addEventListener("click", () => { geheZu(b.getAttribute("data-zur")); $("frageleiste").scrollIntoView({ block: "start" }); });
    for (const b of $("panel-versuche").querySelectorAll("[data-aufl]")) b.addEventListener("click", () => {
      const id = b.getAttribute("data-aufl"); S.antworten[id].aufl = !S.antworten[id].aufl; sichern(); alles();
      const neu = $("panel-versuche").querySelector('[data-aufl="' + id + '"]'); if (neu) neu.focus();
    });
    $("knopf-fragen-weg").addEventListener("click", () => bestaetigen(t("knopf_fragen_zuruecksetzen") + "?", () => {
      for (const f of FRAGEN) if (f.id !== "start") S.antworten[f.id] = { wahl: null, zahl: "", warum: "", fest: false, ohne: false, aufl: false };
      S.f2Uebersprungen = false; S.aktuell = freigabe() ? "f1" : "start"; S.e = standardE(); rechnen(); sichern(); alles(); fokus("knopf-fragen-weg");
    }));
    // Modell
    const abschnitte = [["modell_problem", "text_problem"], ["modell_annahmen", "text_annahmen"], ["modell_macht", "text_macht"], ["modell_regler", null], ["modell_lesen", "text_lesen"]];
    h = "";
    for (const [titel, text] of abschnitte) {
      const verdeckt = !freigabe() && titel !== "modell_problem";
      h += '<details class="abschnitt"><summary>' + t(titel) + "</summary>" + (verdeckt ? '<p class="klein">' + t("reiter_verdeckt") + "</p>" : (text ? t(text) : reglerTabelle())) + "</details>";
    }
    $("panel-modell").innerHTML = h;
    $("panel-code").innerHTML = freigabe() ? t("text_rechenweg") + t("text_code", { stand: BAU.stand, version: BAU.version }) : '<p class="klein">' + t("reiter_verdeckt") + "</p>";
  }
  function reglerTabelle() {
    const k = t("regler_tabelle_kopf").split("|");
    let h = t("text_regler_einleitung") + '<div class="tabelle-wrap"><table><thead><tr>' + k.map(x => "<th>" + x + "</th>").join("") + "</tr></thead><tbody>";
    for (const r of REGLER_DEF.regler) {
      const std = r.standard === null ? z(ERW.KA_AUFGABE, 4) : z(r.standard, r.stellen > 2 ? 2 : r.stellen);
      h += "<tr><td>" + t("regler_" + r.id) + "</td><td>" + r.mathml + "</td><td>" + std + " " + einheit(r.einheit) + "</td><td>" + z(r.min, r.stellen > 2 ? 2 : r.stellen) + " " + nurText(t("bis")) + " " + z(r.max, r.stellen > 2 ? 2 : r.stellen) + ", " + z(r.schritt, r.schritt < 1 ? (r.schritt < 0.1 ? 2 : 1) : 0) + " " + einheit(r.einheit) + "</td><td>" + t(r.grundlage) + "</td></tr>";
    }
    h += "<tr><td>" + t("schalter_milch2Raum") + "</td><td></td><td></td><td></td><td>" + t("g_milch2Raum") + "</td></tr>";
    return h + "</tbody></table></div>";
  }
  function reiterTasten() {
    const leiste = $("reiter-leiste"), tabs = [...leiste.querySelectorAll("[role=tab]")];
    for (const b of tabs) b.addEventListener("click", () => { S.ansicht.reiter = b.getAttribute("data-tab"); sichern(); reiterZeichnen(); scrollbereichePruefen(); });
    leiste.addEventListener("keydown", ev => {
      const i = tabs.indexOf(document.activeElement); if (i < 0) return;
      let j = null;
      if (ev.key === "ArrowRight") j = (i + 1) % tabs.length; else if (ev.key === "ArrowLeft") j = (i + tabs.length - 1) % tabs.length;
      else if (ev.key === "Home") j = 0; else if (ev.key === "End") j = tabs.length - 1;
      if (j !== null) { ev.preventDefault(); S.ansicht.reiter = tabs[j].getAttribute("data-tab"); sichern(); reiterZeichnen(); scrollbereichePruefen(); tabs[j].focus(); }
    });
  }

  // ------------------------------------------------------------------ Rückfrage, Rücksetzen, Sprache
  function bestaetigen(frageText, wennJa, ausloeser) {
    const alt = $("rueck-box"); if (alt) alt.remove();
    const b = document.createElement("div");
    b.id = "rueck-box"; b.className = "banner rueck-box"; b.setAttribute("role", "group"); b.setAttribute("aria-labelledby", "rueck-frage");
    b.innerHTML = '<p id="rueck-frage">' + frageText + '</p><div class="knopfzeile"><button type="button" class="knopf-zweit" id="rueck-ja">' + t("ja") + '</button><button type="button" class="knopf-schlicht" id="rueck-nein">' + t("abbrechen") + "</button></div>";
    const ort = ausloeser || document.activeElement;
    if (ort && ort.parentNode && ort !== document.body) ort.parentNode.insertBefore(b, ort.nextSibling); else $("link-banner").after(b);
    $("rueck-ja").addEventListener("click", () => { b.remove(); wennJa(); if (frageText !== t("ohne_frage")) $("knopf-info").textContent = nurText(t("zurueckgesetzt")); });
    $("rueck-nein").addEventListener("click", () => { b.remove(); if (ort && ort.focus) ort.focus(); });
    $("rueck-ja").focus();
  }
  function fussZeichnen() {
    $("fuss-reset").innerHTML = '<button type="button" class="knopf-schlicht" id="knopf-gruppe">' + t("knopf_gruppe_zuruecksetzen") + "</button>";
    $("knopf-gruppe").addEventListener("click", () => bestaetigen(t("gruppe_zuruecksetzen_frage"), () => {
      S.antworten = leereAntworten(); S.aktuell = "start"; S.e = standardE(); S.vergleich = null; S.f2Uebersprungen = false;
      S.ansicht = { reiter: "versuche", vertiefung: false, diagramm: "temperatur", anheften: true };
      rechnen(); sichern(); alles(); window.scrollTo(0, 0); fokus("frage-titel");
    }));
  }

  // ------------------------------------------------------------------ Zeichnen
  function teilZeichnen(fokusId) {     // nach Reglerbewegung: nur Ergebnisse neu, Regler bleiben (kein Fokusverlust)
    diagrammZeichnen(); rechenwerteZeichnen(); energieZeichnen(); bilanzZeichnen(); wertetabelle();
    for (const r of REGLER_DEF.regler) {
      const range = $("r-" + r.id), feld = $("z-" + r.id); if (!range) continue;
      const w = r.faktor ? S.e[r.key] * r.faktor : S.e[r.key];
      if (document.activeElement !== range) range.value = w;
      range.setAttribute("aria-valuetext", wertText(r, w));
      if (document.activeElement !== feld) { feld.value = z(w, r.stellen); feld.removeAttribute("aria-invalid"); }
    }
    const info = $("info-kasten");
    if (info) info.innerHTML = infoKastenInhalt();
    for (const b of document.querySelectorAll("[data-vor]")) b.setAttribute("aria-pressed", S.e.kAHerkunft === "vor:" + b.getAttribute("data-vor") ? "true" : "false");
    if (fokusId === null) frageleisteZeichnen();
  }
  function alles() {
    rechnen(); texteSetzen(); frageleisteZeichnen(); reglerZeichnen(); diagrammZeichnen(); rechenwerteZeichnen(); energieZeichnen(); bilanzZeichnen();
    wertetabelle(); messblattZeichnen(); reiterZeichnen(); fussZeichnen(); anheftenPruefen(); scrollbereichePruefen();
  }
  function scrollbereichePruefen() {     // breite Formeln und Tabellen: nur wenn sie überlaufen, per Tastatur erreichbar (WCAG 2.1.1)
    for (const el of document.querySelectorAll(".formel, .tabelle-wrap")) {
      if (el.scrollWidth > el.clientWidth + 1) { el.setAttribute("tabindex", "0"); if (!el.hasAttribute("aria-labelledby")) { el.setAttribute("role", "region"); el.setAttribute("aria-label", nurText(t(el.classList.contains("formel") ? "bereich_formel" : "bereich_tabelle"))); } }
      else { el.removeAttribute("tabindex"); if (!el.hasAttribute("aria-labelledby")) { el.removeAttribute("role"); el.removeAttribute("aria-label"); } }
    }
  }
  function anheftenPruefen() {
    const vv = window.visualViewport, hoehe = vv ? vv.height : window.innerHeight;
    const feldFokus = document.activeElement && document.activeElement.type === "text" && !!document.activeElement.closest("#messblatt, #frageleiste");
    const tastatur = feldFokus || vv && document.activeElement && /^(INPUT|TEXTAREA)$/.test(document.activeElement.tagName) && document.activeElement.type !== "range" && hoehe < window.innerHeight * 0.8;
    const an = S.ansicht.anheften && freigabe() && hoehe >= 500 && !tastatur && window.innerWidth <= 767 && window.innerHeight > window.innerWidth;
    document.documentElement.classList.toggle("anheften", !!an);
    document.documentElement.classList.toggle("handy", freigabe() && window.innerWidth <= 767);   // Reihenfolge Diagramm, Frage, Regler (M-6)
    const moeglich = freigabe() && window.innerWidth <= 767 && window.innerHeight > window.innerWidth && hoehe >= 500;
    const kn = $("knopf-anheften");
    if (kn) { kn.hidden = !moeglich; kn.textContent = nurText(t(S.ansicht.anheften ? "anheften_aus" : "anheften_an")); kn.setAttribute("aria-pressed", S.ansicht.anheften ? "true" : "false"); }
    document.documentElement.style.setProperty("--anheft", an ? Math.ceil($("diagramm-halter").getBoundingClientRect().height) + "px" : "0px");
  }
  $("sprachknopf").addEventListener("click", () => { S.sprache = S.sprache === "de" ? "en" : "de"; $("knopf-info").textContent = ""; sichern(); alles();
    try { if (/[?&]lang=/.test(location.search)) history.replaceState(null, "", location.pathname + location.search.replace(/([?&])lang=(de|en)(&|$)/, (m, a, b, c) => (c ? a : "")).replace(/\?$/, "") + location.hash); } catch (x) { }
    if ($("link-ja")) kurslinkPruefen();
    $("sprachknopf").focus(); });
  $("knopf-standard").addEventListener("click", () => { ausgangslage("standard"); rechnen(); sichern(); alles(); $("knopf-info").innerHTML = t("knopf_standard_info"); ansagen(); });
  $("knopf-versuch").addEventListener("click", () => { Object.assign(S.e, { tEnd_min: 60, becher: true, kAQuelle: "messung", kAHerkunft: "messung" }); if (!(S.e.thMess > S.e.thU && S.e.thMess < S.e.thK0)) S.e.thMess = 67; rechnen(); sichern(); alles(); $("knopf-info").innerHTML = t("knopf_versuch_info"); ansagen(); });
  for (const b of document.querySelectorAll("[data-ansicht]")) b.addEventListener("click", () => { S.ansicht.diagramm = b.getAttribute("data-ansicht"); sichern(); alles(); b.focus(); });
  $("vertiefung").addEventListener("toggle", () => { const auf = $("vertiefung").open; if (auf !== !!S.ansicht.vertiefung) { S.ansicht.vertiefung = auf; if (!auf && S.ansicht.diagramm !== "temperatur") S.ansicht.diagramm = "temperatur"; sichern(); alles(); } });
  reiterTasten();
  let groesse = null;
  document.addEventListener("toggle", scrollbereichePruefen, true);
  $("knopf-anheften").addEventListener("click", () => { S.ansicht.anheften = !S.ansicht.anheften; sichern(); anheftenPruefen(); $("knopf-anheften").focus(); });
  window.addEventListener("resize", () => { clearTimeout(groesse); groesse = setTimeout(() => { diagrammZeichnen(); anheftenPruefen(); scrollbereichePruefen(); }, 80); });
  if (window.visualViewport) window.visualViewport.addEventListener("resize", anheftenPruefen);
  document.addEventListener("focusin", anheftenPruefen); document.addEventListener("focusout", () => setTimeout(anheftenPruefen, 50));
  alles();
  kurslinkPruefen();
  window.addEventListener("storage", ev => { if (ev.key && ev.key.indexOf(SPEICHER) === 0 && ev.key !== SPEICHER + "probe") { laden(); alles(); } });
  window.addEventListener("hashchange", kurslinkPruefen);
  window.KAFFEE = { zustand: () => JSON.parse(JSON.stringify({ e: S.e, antworten: S.antworten, aktuell: S.aktuell, kurs: S.kurs, ansicht: S.ansicht, sprache: S.sprache })), ergebnis: () => (freigabe() ? R : null), speicherOk: () => speicherOk, csv: () => csvBauen() };
})();
