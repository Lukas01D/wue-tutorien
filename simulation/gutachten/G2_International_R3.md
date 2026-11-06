# Gutachten G2, Runde 3: Internationaler Student (nur Englisch)

- **Rolle:** G2 „Internationaler Student“, 3. Semester, Deutsch nicht Erstsprache, nutzt die Seite nur auf Englisch
- **Datum:** 06.11.2026
- **Runde:** 3 (letzte Runde; Nachprüfung der offenen Punkte aus `G2_International_R2.md` und kurzer Durchgang auf Rückfälle)
- **Art:** getrennte Rollenprüfung desselben Modells
- **Gegenstand:** `simulation/site/index.html`, SHA-256 `1d90ce2f84349754592a5dd572a760a5d212cd3383bcafbeb1cceaf06e07292b` (vor und nach der Prüfung mit sha256sum geprüft: gleich)
- **Maßstab:** KONZEPT.md (M-19, Anhang C), Leitfaden_Lerntexte_DE_EN.md Abschnitt 4; in ZUSAMMENFUEHRUNG.md nur die Zeilen G2-01 bis G2-27 und G2-R2-01 bis G2-R2-08
- **Umgebung:** Node, Playwright, Chromium headless (`chromium.launch()` ohne Optionen), `file://…/index.html?lang=en`; Laptop 1366 × 768; Handy 390 × 844 (isMobile, hasTouch, Tippen mit `touchscreen.tap` bzw. `tap()`)
- **Durchgespielt:** Laptop: Start, Frage 1 (auch „abc“, leer), Frage 2 ohne und mit Kurswerten (Kurslink mit Becher 3 und Deckel), V1 bis V5 mit Auflösungen, drei Ansichten, Wertetabelle, ungültige Einstellung, Reiter Model und How the code calculates (alle Abschnitte offen), Tab-Folge, Sprachwechsel DE → EN mit Live-Region, `?lang=en` erneut öffnen. Handy: Kurslink, Start mit „2,5“, Frage 1, Frage 2, V1 mit einem Tipp nach Zahleneingabe, alle drei Reiter
- **Skripte und Bilder:** `/tmp/claude-0/-home-user/8bff1287-c5bb-5641-9916-90393029086f/scratchpad/r3_G247/g2/` (Skripte der Runde 2 erneut ausgeführt: a3, a4, a5, a6, a7, a8, a9, a11b, a12, a13, a18, a19, a20, a21, a22; neu: b1 bis b5)

## Nachprüfung

| ID | Ergebnis am neuen Stand | Beleg |
|:--|:--|:--|
| G2-06 | **behoben.** Code-Reiter erklärt die deutschen Indizes jetzt an Ort und Stelle: „*Q* = *C* (*ϑ*_Anfang − *ϑ*_Ende) (Anfang start, Ende end)“; Liste mit „ab released, mess measured, misch mixture“ bleibt. | a12_code_open.txt, Zeilen 139 bis 144 |
| G2-08 | **teilweise.** Titel jetzt „When to add the milk“ (Karte, Leiste, Reiter): gut. Geblieben ist die Nominalgruppe an zwei Stellen: V1 „Does this temperature depend on the time of adding the milk?“ und V2 „as in question 1, find the time of adding with the largest difference“. | a3.js, a7.js, Quelltextsuche „time of adding“ (2 Treffer). Vorschlag: V1 „Does this temperature depend on when the milk is added?“, V2 „…, find when to add the milk so that the difference is largest.“ |
| G2-09 | **behoben.** Model-Reiter: „“Measured values, linearised (ln)” view (going further)“, gleich dem Knopf. | a13_modell.txt, Zeile 212 |
| G2-12 | **teilweise (Rest low).** „mug on“ und „switch the mug on“ sind überall weg („mug included“ in Q2, Übernahme, „As in the experiment“, Assumptions „except when you include the mug“); „data sheet“ ist weg. Geblieben: zwei Namen für das Messblatt, Überschrift „Measured values from the experiment“, in vier Texten „measurement sheet“ („enter the values in the measurement sheet“, „The measurement sheet is empty“, „CSV created (… measurement sheet)“, „stays in the measurement sheet“). Wer „measurement sheet“ sucht, findet keine so benannte Überschrift. | a4.js, a21.js, Quelltextsuche. Vorschlag: Überschrift „Measurement sheet: values from the experiment“ |
| G2-13 | **behoben.** „Starting point as in the experiment: milk added after 60 min, mug included.“; „starting situation“ kommt nicht mehr vor. | a21.js, Quelltextsuche |
| G2-14 | **teilweise (9 von 10).** (8) behoben: „the tool works out the value after 10 min that belongs to this *kA* and passes it to the unchanged model.“ (9) geblieben: Fuß „Belongs to: Tutorial 5, “Coffee with milk” (problem sheet and solution of the tutorial).“ (deutsches Muster „Gehört zu“). | a12_code_open.txt, Zeile 241; a9_full.txt, Zeile 332. Vorschlag: „Part of Tutorial 5, “Coffee with milk” (problem sheet and solution).“ |
| G2-15 | **behoben.** Fuß „Tutorial 5“, Kopf der Wertetabelle „Cup 1 [°C] / Cup 2 [°C] / Mug 1 (milk right away) [°C]“ einheitlich groß. | a9.js („table head“), a9_full.txt |
| G2-17 | **behoben.** „No calculated values yet“ erscheint bei ungültiger Einstellung nicht mehr. Kleinigkeit: der Kasten sagt jetzt zweimal dasselbe („No calculation“ und darunter fett „No calculation: settings not valid“). | b2.js, b2_rw_invalid.png |
| G2-19 | **behoben, Nebenpunkt weiter offen** (in der Zusammenführung nicht entschieden): Öffnen mit `?lang=en`, danach `index.html` ohne Zusatz: wieder Deutsch. Wer die Seite nur über einen englischen Link kennt, bekommt den Kurslink der TL deutsch, bis er einmal „EN ↔ DE“ drückt. | a5.js („T1 reopen lang de“) |
| G2-20 | **teilweise.** (a) Ausgleichsgerade bleibt im Zeichenbereich: behoben. (b) Einheit von *kA* weiter als winziger gestapelter Bruch „W über K“ in den Rechenwerten. (c) Logo „WÜ“ sichtbar unverändert (für Bildschirmleser verborgen). (b) und (c) sind in der Zusammenführung weder umgesetzt noch abgelehnt. | b1.js, b1_rw.png; a22.js |
| G2-22 | **behoben (simuliert)**, Folgefehler G2-R2-01 behoben (siehe unten). Echte Bildschirmtastatur weiter offen (ABNAHME_IPHONE.md). | a18.js |
| G2-26 | **teilweise, unverändert.** Escape schließt die Hilfe. Tab-Folge springt weiter: „Values as a table“ (y = 924) → „Default values“ (x = 883, y = 407) → „As in the experiment“ (y = 461) → „Going further“ (y = 982). | a20.js |
| G2-07 | offen (Frage an die TL), unverändert: Reiter heißt „Experiments“, enthält aber Fragen; „Experiment“ heißt auch Frage 2 und der Kursversuch. Empfehlung aus Runde 2 bleibt: englischen Namen unabhängig wählen („Questions“). | Reiterknopf „Experiments“ (g7/s6.js nach Sprachwechsel), a12_tab-versuche.txt |
| G2-R2-01 | **behoben.** Handy, V1, Zahl getippt, ein Tipp auf „Lock in your prediction, then check“: Ereignisse `pointerdown, pointerup, focusout, click` alle auf `knopf-fest`, festgehalten; ebenso mit Maus. V1, V2 und „Use settings from the measurements“ je mit einem Tipp. | a18.js, a19.js, b3.js („V1 locked after 1 tap: true“) |
| G2-R2-02 | **behoben.** DE: Regler bewegt, `#ansage` „Tasse 1 37,38 °C, …“; nach „DE ↔ EN“ leer, `lang="en"`. | b1.js |
| G2-R2-03 | **behoben.** Beispiel je Frage: Start „for example 3.5“, Frage 1 „for example 50“, V1 „for example 40“, V2 „for example 80“. | a3.js, a8.js, a7.js |
| G2-R2-04 | **behoben.** Messblatt gefüllt, vor dem Prüfen: „Class data loaded: 23 measured values.“ und „Starting point: class values, applied when you check“; danach „class data used (*kA* from 0 and 10 min, mug included)“. | a4.js |
| G2-R2-05 | **behoben.** „Intersection of the curves: shown once you have made your prediction for question 1“; liest sich nicht mehr als Zeitangabe. Weiter fett wie ein Wert (Kosmetik). | a21.js, b2.js, b2_rw_vorF1.png |
| G2-R2-06 | **behoben** für Flächentext und Beschreibung: ohne Schnitt „Up to adding the milk, cup 2 releases 3.58 kJ more heat in total than cup 1.“, keine zweite Fläche in der Legende. Rest im Lesehinweis darüber: G2-R3-02. | a9.js, a9_dia_Heat.png |
| G2-R2-07 | **behoben.** Am Feld „Measurement after 10 min“: `aria-invalid="true"`, Text „The measured value after 10 min must lie between the room temperature and the initial coffee temperature.“ direkt unter dem Feld. | a11b.js |
| G2-R2-08 | **behoben** (V5): „from 80 to 63.5 °C in 30 min, compared with 48.8 °C for the open ceramic mug“. Stellenzahl („from 77.6 to 36.85 °C“) wie entschieden nach Konzept 6.2 belassen. | a7.js, a9.js |

**Zählung Nachprüfung:** behoben 14 (G2-06, 09, 13, 15, 17, 22, R2-01 bis R2-08; G2-19 behoben mit offenem Nebenpunkt nicht mitgezählt), teilweise 5 (G2-08, 12, 14, 20, 26), nicht behoben 0; G2-07 offen bei der TL.

## Neue Befunde

| ID | Schwere | Befund | Beleg | Vorschlag | CONFIRMED/INFERRED |
|:--|:--|:--|:--|:--|:--|
| G2-R3-01 | low | **„Show question“ heißt auch bei offener Frage so.** Der neue Aufklapper nach dem Festhalten (`details`/`summary`) behält seinen Text, während der Knopf daneben richtig zwischen „Show explanation“ und „Hide explanation“ wechselt (G2-23). Uneinheitlich; Bildschirmleser melden den Zustand über `details` trotzdem. | Frage 1 festgehalten, „Show question“ geklickt: `open=true`, Text weiter „Show question“ (b5.js) | „Hide question“ bei offener Frage (deutsch „Frage ausblenden“), wie beim Erklärknopf. | CONFIRMED |
| G2-R3-02 | low | **Lesehinweis zum Wärmestrom spricht immer vom Schnitt.** Unter dem Diagramm „Heat flow rate“ steht fest „before the intersection cup 2 releases more, afterwards less; the two areas are hatched differently, and their sum is *Q*₂ − *Q*₁“, auch wenn es vor der Zugabe keinen Schnitt und nur eine Fläche gibt. Die Zeile darunter sagt dann richtig „Up to adding the milk, cup 2 releases 3.58 kJ more heat …“. Wer langsam liest, sucht zwei Flächen. | Kurslink mit Deckel, Übernahme, Ansicht „Heat flow rate“ (a9.js, a9_dia_Heat.png) | Satz bedingt: „… The area between the curves is an energy (*Q*₂ − *Q*₁). If the curves cross before the milk is added, the part after the intersection is hatched differently: there cup 2 releases less.“ | CONFIRMED |

**Zählung neue Befunde:** blocker 0, high 0, medium 0, low 2.

## Durchgang auf Rückfälle (Englisch, Laptop und Handy)

- Keine deutschen Reste im sichtbaren Text in Start, Frage 1, Frage 2, V1 und allen drei Reitern (Handy, Suche nach typischen deutschen Wörtern: leer); nach DE → EN ebenso leer (b1.js, b3.js).
- Dezimalpunkt durchgehend, auch bei Komma-Eingabe („2,5“ → „about 2.5 K“); britische Schreibweise (keine „color/center/-ize“-Treffer); klein nach Doppelpunkt eingehalten.
- Kein waagerechtes Scrollen bei 390 px, keine Skriptfehler in allen Läufen.
- Zahlen stichprobenhaft wie in Runde 2 (34.05 / 30.19 °C, 3.85 K; Kurslink 36.76 / 33.80 / 35.31 °C, *Q*₂ − *Q*₁ = 44.46 − 40.88 = 3.58 kJ); keine Abweichung.
