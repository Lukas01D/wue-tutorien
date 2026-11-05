# Gestaltungswerte der Simulationsseiten im Lernzentrum (Stand v8, Runde 12)

Quelle: lokaler Klon `/home/user/lernzentrum_v8`, Commit `c2af968` (Merge PR #25 „runde-12-v8-abnahme“), Ordner `dist/`. Nur gelesen, nichts geändert.

Vorgehen:

1. Quelltext gelesen (alle CSS-Dateien, die `dist/index.html` lädt, dazu `topic.js`, `pilot.js`, `simulation-layout.js`, `runde6-layout.js`, `i18n.js`, `sprachen.js`, `numeric-input.js`, `parameter-help.js`, `math.js`, Auszüge aus `app.js` und `drawing_language.py`).
2. Weil sich die Regeln über viele Runden überlagern, die **wirksamen** Werte zusätzlich im echten Browser gemessen: Google Chrome ohne Fenster, `dist/` über einen lokalen Lese-Server, Seite `index.html#topic-01/simulation/steady` (Thema 1, „Stationär“) und `#topic-02/simulation/convection_fin`, Fensterbreiten 1440, 1280, 1000 und 390 px.

In den Tabellen steht immer der wirksame Wert. Die Fundstelle ist die Regel, die ihn setzt (Datei:Zeile). Ältere, überstimmte Werte stehen nur dabei, wenn sie verwirren könnten. „gemessen“ heißt: berechneter Wert aus Chrome bei 1440 px, sofern nicht anders angegeben (1 rem = 16 px).

In `dist/01_conduction/` und `dist/02_convection/` liegt **kein HTML** (nur `lesson.js`, `handout.js`, `quiz.js`, `controls.js`, `en/content.js`, Python, Notebooks, Abbildungen). Die einzige Seite ist `dist/index.html`; die Simulationsseite ist dort der Reiter „Simulationen“.

## 0. Ladereihenfolge der Stylesheets

Spätere Dateien gewinnen bei gleicher Spezifität. Reihenfolge laut `index.html:10` bis `index.html:24`:

| Nr. | Datei | Rolle für die Simulationsseite |
|---|---|---|
| 1 | `styles.css` | Grundgerüst, erste Farbvariablen, Knöpfe, Tabellen, Reiter |
| 2 | `audit.css` | `[hidden]{display:none!important}` (Zeile 20), Sprachknopf (199 bis 200), Banner |
| 3 | `pilot.css` | Simulationsgrundlayout (Regler, Status, Rechenwerte, Containerabfragen) |
| 4 | `workspace.css` | Rahmen mit eigenem Scrollbereich, Rechenbudget |
| 5 | `design.css` | **neue Farbwerte** (`:root` Zeile 2 und 159), flache Flächen, Knopfrangfolge G2, Desktopraster ab 1200 px |
| 6 bis 9 | `runde6-review.css`, `runde6-pilot.css`, `runde6-experiments.css`, `runde6-release.css` | Versuche, erweiterte Regler, Vergleich |
| 10 | `runde61-math.css` | Formelschrift (wird von `fonts.css` überstimmt) |
| 11 | `runde7-layout.css` | Fokusringe, Fehlermeldungen, Mindestzielgrößen |
| 12 | `fonts.css` | Fira Sans und Fira Math, jeweils `!important` |
| 13 | `typeset.css` | Formelsatz (Strichstärke, Brüche) |
| 14 | `runde10.css` | Rechenwerte-Raster, Skizzen |
| 15 | `runde11.css` | **aktuelles Simulationsraster**, Reiter Runde 12 (ab Zeile 95) |

## 1. Farben

### 1a. Alle CSS-Variablen

`design.css` definiert die Hauptfarben neu; die Werte aus `styles.css` gelten nur, wo `design.css` sie nicht überschreibt. Gemessen über `getComputedStyle(document.documentElement)`.

| Variable | wirksamer Wert | Fundstelle | alter Wert (überstimmt) | Verwendung auf der Simulationsseite |
|---|---|---|---|---|
| `--ink` | `#142337` | `styles.css:2` | | Fließtext (`body`), Eingabetext, Text in Rechenwerten (`dd`) |
| `--muted` | `#5a6b7f` | `styles.css:3` | | Nebentext: inaktive Themenreiter, `dt` im Rechenwerte-Kasten, Brotkrumen, „Lokal gespeichert“, Sperrhinweis, Fehlertext unter Feldern (siehe 1b) |
| `--line` | `#d8e1ea` | `styles.css:4` | | alle Linien und Rahmen: Reiterleiste unten, Eingabefelder, Ghost-Knöpfe, Trennlinien in Versuchen und Modell, Rand inaktiver Unterreiter |
| `--soft` | `#eef5fb` | `design.css:2` | `#edf4fa` (`styles.css:5`) | Flächen: Rechenwerte-Kasten, sekundäre Knöpfe und inaktive Umschalter, Auflösung der Versuche, „?“-Knopf, Banner, Fortschrittsbalken-Grund |
| `--panel` | `#ffffff` | `styles.css:6` | | Kartenfläche (`.tool-card`) |
| `--page` | `#fff` | `design.css:2` | `#f3f6f9` (`styles.css:7`) | Seitenhintergrund (`body`) |
| `--navy` | `#102d49` | `design.css:2` | `#0b1f33` (`styles.css:8`) | Seitenleiste, Primärknopf „Berechnen“, Text aktiver Umschalter, Tooltip, Formelfarbe in `.formula`, Wert des Fortschrittsbalkens |
| `--navy-2` | `#173d5e` | `design.css:2` | `#112d49` (`styles.css:9`) | `h3` im Lerntext (wird durch `--heading-blue` überstimmt) |
| `--blue` | `#173d5e` | `design.css:2` | `#1d70a8` (`styles.css:10`) | Fokusring im Hauptbereich, Themenkennung „Thema 01: …“, aktiver Themenreiter (Text und Balken), Rahmen des Primärknopfs, `accent-color` der Schieberegler und Radioknöpfe, Rahmen des Sprachknopfs bei EN |
| `--cyan` | `#a9d5ef` | `design.css:2` | `#56c4dd` (`styles.css:11`) | Markenfeld „WÜ“, Fokusring in der Seitenleiste, Marke des aktiven Navigationspunkts, obere Linie des Notizfelds |
| `--cyan-soft` | `#eaf4fc` | `design.css:2` | `#dff5fa` (`styles.css:12`) | Zitate und Beispielkästen im Text (`.lesson-body blockquote`, `.handout-highlight`) |
| `--green` | `#1e8b64` | `styles.css:13` | | Balken „sicher“ in der Lernüberprüfung (nicht auf der Simulationsseite) |
| `--amber` | `#bd7a18` | `styles.css:14` | | im CSS nirgends verwendet |
| `--shadow` | `none` | `design.css:2` | `0 12px 40px rgba(20,35,55,.09)` | keine Schatten an Karten |
| `--radius` | `4px` | `design.css:2` | `16px` | Ecken der Panels (`.lesson-panel`, `.review-workspace`) |
| `--heading-blue` | `#39718e` | `design.css:159` | | `h1` bis `h4` im Hauptbereich (`design.css:160`), Text aller Reiter und Umschalter, Rechenwerte-Überschrift, Prognosefrage, „ohne Vermutung aufdecken“, Rahmen des Reiterpanels |
| `--formula-bold` | `1` | `typeset.css:3` | | Schalter für die Strichverstärkung der Formeln (0 = normal) |

Laufzeitvariablen (per Skript oder nur als Fallback):

| Variable | Wert | Fundstelle | Bedeutung |
|---|---|---|---|
| `--simulation-image-width` | `min(780, naturalWidth)px`, hier `780px` | `simulation-layout.js:10` bis `11`, verwendet `runde11.css:34` | Höchstbreite des Simulationsbilds |
| `--simulation-image-height` | nie gesetzt, Fallback `38dvh` | `pilot.css:227`, `pilot.css:229` | alte Bildhöhe, in Runde 11 durch `height:auto` überstimmt |
| `--pilot-value-columns` | 4, bei `unsteady`/`heat2d` 5, unter 1200 px 4, bis 600 px 2 | `runde6-pilot.css:19`, `:25`, `:66`, `:70` | alte Spaltenzahl der Werte; Runde 11 setzt fest 2 Spalten (`runde11.css:36`) |
| `--duration-limit` | Prozentwert | `pilot.js:327`, `runde7-layout.css:118` | Marke für die maximale Rechendauer am Regler `t_end` |
| `--heading-color` | nie definiert, Fallback `#246d98` | `runde6-pilot.css:3` | Farbe „Für Fortgeschrittene“ unter 1200 px |
| `--sketch-min-width` | nie gesetzt, Fallback `1000px` | `runde10.css:6` | Skizzenzeile |
| `--table-column-width` | Prozentwert je Spalte | `app.js:403`, `runde11.css:125` | feste Spaltenbreiten schmaler Tabellen bis 600 px |
| `--score`, `--score-color`, `--mastery-color` | per Skript | `app.js:527`, `:609`, `:626` | nur Lernüberprüfung |

### 1b. Farben nach Rolle (wirksam, gemessen)

| Rolle | Wert | Fundstelle |
|---|---|---|
| Seitenhintergrund | `#fff` | `--page`, `styles.css:29` |
| Kopfleiste Hintergrund | `#fff` (nicht mehr halbtransparent grau) | `design.css:3` |
| Kopfleiste Unterlinie | `1px solid rgba(216,225,234,.9)` | `styles.css:228` |
| Seitenleiste Hintergrund | `#102d49` einfarbig (der alte Verlauf ist überschrieben) | `design.css:4` (alt `styles.css:79` bis `81`) |
| Seitenleiste Text | `#eff7fc` | `styles.css:78` |
| Seitenleiste Navigation | Text `rgba(239,247,252,.75)`; aktiv `#fff` auf `rgba(86,196,221,.15)` mit `inset 3px 0 var(--cyan)` | `styles.css:198`, `:204` |
| Markenfeld „WÜ“ | Fläche `#a9d5ef`, Schrift `#092134` | `design.css:5`, `styles.css:99` |
| Überschriften `h1` bis `h4` | `#39718e` | `design.css:160` |
| Themenkennung „Thema 01: Wärmeleitung“ (`.lesson-kicker`) | `#173d5e` | `styles.css:297` |
| Fließtext | `#142337` | `styles.css:28` |
| Nebentext | `#5a6b7f` | `--muted` |
| Linien | `#d8e1ea` | `--line` |
| Linien im Rechenwerte-Kasten | `#dfe5ec` | `runde11.css:38` |
| Kopfbereich Thema (`.lesson-intro`) | `linear-gradient(110deg, rgba(86,196,221,.09), transparent 42%), #fff` | `styles.css:293` bis `295` |
| Knopf primär („Berechnen“, auch „Abspielen“) | Fläche `#102d49`, Schrift `#fff`, Rand `1px solid #173d5e`; Hover ändert nichts (gemessen `#102d49`) | `design.css:331`, `styles.css:410` |
| Knopf sekundär („Standardwerte“, „Erneut abspielen“) | Fläche `#eef5fb`, Schrift `#39718e`, Rand `#c9dfed`; Hover ändert nichts | `design.css:330` |
| Ghost-Knopf in den Reitern („Auflösung zeigen“, „Ausgangslage einstellen“, „Alle Versuche zurücksetzen“) | Fläche transparent, Schrift `#102d49`, Rand `1px solid #d8e1ea`; Hover Fläche `#eef5fb` | `styles.css:412` bis `413` |
| Ghost-Knopf gesperrt („Auflösung zeigen“ ohne Vermutung) | Schrift `#5a6b7f`, Fläche `#eef5fb`, Rand `#d8e1ea`, `opacity:1`, `cursor:not-allowed` | `runde7-layout.css:75` bis `82` |
| Primärknopf außerhalb der Simulation (z. B. Fußzeile) | Fläche `#173d5e`, Hover `#17689e` | `styles.css:410` bis `411` |
| Umschalter inaktiv (Simulationswahl, Wand/Rohr/Kugel) | Fläche `#eef5fb`, Schrift `#39718e`, Rand `1px solid #c9dfed` | `design.css:324` bis `325` |
| Umschalter aktiv | Fläche `#d9edf9`, Schrift `#102d49`, Rand `#93bbd4`, `box-shadow: inset 0 -2px #39718e` | `design.css:326` bis `327` |
| Umschalter Hover | Fläche `#dfedf6` | `design.css:328` bis `329` |
| Themenreiter aktiv (Lerntext, Simulationen …) | Schrift `#173d5e`, Balken unten 3px `#173d5e` | `styles.css:328` bis `329` |
| Themenreiter inaktiv | Schrift `#5a6b7f`, kein Balken | `styles.css:321`, `:327` |
| Unterreiter aktiv (Versuche, Modell, So rechnet der Code) | Fläche `#fff`, Rand `#39718e` (oben 3px), Schrift `#39718e` | `runde11.css:99` |
| Unterreiter inaktiv | Fläche `#edf2f6`, Rand `1px solid #d8e1ea`, Schrift `#39718e`; kein Hover | `runde11.css:98`, `design.css:168` |
| Rahmen des Reiterpanels | `1px solid #39718e` | `runde11.css:101` |
| Fokusring Hauptbereich | `outline: 2px solid #173d5e; outline-offset: 2px` | `runde7-layout.css:54` bis `57` |
| Fokusring Seitenleiste | `outline: 2px solid #a9d5ef; outline-offset: 2px` | `runde7-layout.css:46` bis `53` |
| Fehler: Feldrand | `border-color:#b63434; box-shadow: inset 0 0 0 1px #b63434` | `runde7-layout.css:94` bis `97` |
| Fehler: Statuszeile | Schrift `#862828` | `pilot.css:12` |
| Fehler: Text unter dem Feld | gewollt `#862828` (`runde7-layout.css:101`), **wirksam aber `#5a6b7f`**, weil `.pilot-field small` (`pilot.css:9`) spezifischer ist | gemessen |
| Fehler: „Ergebnis gehört noch zu den letzten gültigen Eingaben“ | Schrift `#862828`, Fläche `#fff8f7`, links `3px solid #b63434` | `runde7-layout.css:105` bis `113` |
| Erfolg: Vermutung richtig / falsch | `✓` in `#227b48`, `×` in `#a23838`, Gewicht 800 | `runde6-experiments.css:57` bis `59` |
| Erfolg allgemein (Quiz, nicht Simulation) | richtig `border-left:3px solid #3e8168` auf `#edf7f1`; falsch `#a95555` auf `#fcf0ef` | `design.css:246` bis `247` |
| Rechenwerte-Kasten | Fläche `#eef5fb`, Überschrift `#39718e`, `dt` `#5a6b7f`, `dd` `#142337` | `pilot.css:229`, `:233`, `design.css:333` |
| Auflösung eines Versuchs | Fläche `#eef5fb` | `design.css:37` |
| Tabellenkopf | Fläche `#174d68`, Schrift `#fff` | `styles.css:369` |
| Tabellenkörper | Schrift `#2a4052`, Zeilenlinie `1px solid #dce6ec`, gerade Zeilen `#f5f9fb`, Rahmen oben und unten `1px solid #d8e1ea` | `styles.css:367`, `:370`, `:371`, `design.css:19` |
| Tooltip der „?“-Hilfe | Fläche `#102d49`, Schrift `#fff`, Schatten `0 4px 12px #102d4926` | `design.css:61` |
| „?“-Knopf | Fläche `#eef5fb`, Zeichen `#102d49` | `design.css:59` |
| Fortschrittsbalken | Grund `#eef5fb`, Wert `#102d49`, unbestimmt: Verlauf `#eef5fb 25%, #102d49 45%, #eef5fb 65%` | `design.css:67` bis `72` |
| Entwurfsbanner oben | Schrift `#102d49` auf `#eef5fb` | `design.css:39` |
| Vergleichslinie „Voriger Lauf“ im Diagramm | `#7b8288`, gestrichelt | `drawing_language.py:260`, `:269` |
| Marke „Mitte“ im Diagramm | Text `#143f5c`, Kreuz weiß mit Kontur `#143f5c` | `drawing_language.py:203` bis `208` |
| Kontrollkästchen Vergleich | `accent-color:#216b95` | `runde6-pilot.css:7` |
| Farbskalen-Auswahl (2D) | Rand `#c4d8e6`, Schrift `#244b67` | `runde6-pilot.css:8` |
| Seitenfarbe für Browser (`theme-color`) und Favicon | `#0b1f33`, Favicon-Schrift `#56c4dd` (noch die **alten** Werte) | `index.html:7`, `:25` |
| Dunkelmodus | nicht gefunden (`<meta name="color-scheme" content="light">`, `index.html:6`) | |

## 2. Schrift

### 2a. Familien und `@font-face`

| Punkt | Wert | Fundstelle |
|---|---|---|
| Text | `'Fira Sans', sans-serif !important` für `html, body, button, input, select, textarea, code, pre` | `fonts.css:6` |
| Formeln | `'Fira Math', math !important` für `math, .formula math, .inline-formula math, math *` | `fonts.css:7` |
| überstimmte Altangaben | `Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif` (`styles.css:30`); Formeln `"Cambria Math", Cambria, "STIX Two Math", …` (`styles.css:355`, `:360`, `runde61-math.css:5`). Für den Container `.formula` bleibt Cambria als Familie stehen, die Zeichen selbst stehen aber in `math` und laufen in Fira Math. | |
| Ladeverhalten | `font-display:swap`; die Seite wird erst nach `document.fonts.ready` eingeblendet (`data-wue-ready`) | `fonts.css:1` bis `5`, `bootstrap-ready.js:3` bis `5`, `index.html:26` |
| Schrift im Diagramm (matplotlib) | Text Fira Sans, Formeln Fira Math (`mathtext.rm`), kursiv Fira Sans Italic, `svg.fonttype: path` | `drawing_language.py:29` bis `33` |

| `@font-face` | Gewicht | Stil | Datei | Fundstelle |
|---|---|---|---|---|
| Fira Sans | 400 | normal | `fonts/FiraSans-Regular.woff2` | `fonts.css:1` |
| Fira Sans | 400 | italic | `fonts/FiraSans-Italic.woff2` | `fonts.css:2` |
| Fira Sans | 600 | normal | `fonts/FiraSans-SemiBold.woff2` | `fonts.css:3` |
| Fira Sans | 700 | normal | `fonts/FiraSans-Bold.woff2` | `fonts.css:4` |
| Fira Math | ohne Angabe | ohne Angabe | `fonts/FiraMath-Regular.woff2` | `fonts.css:5` |

Im Ordner liegen zusätzlich `.ttf` und `.otf` (für matplotlib) und die Lizenzen `FiraSans-OFL.txt`, `FiraMath-OFL.txt`.

### 2b. Gewichte

Es gibt nur die Schnitte 400, 400 kursiv, 600 und 700. Das CSS fordert viele Zwischenwerte an; der Browser wählt nach den CSS-Regeln: 500 wird 400; 600 bleibt 600; 650, 700, 720, 750, 780, 800, 820, 850, 900 werden alle mit **Bold 700** gezeichnet. Fira Math hat nur Regular; die „fette“ Formelwirkung entsteht durch eine Kontur (siehe Abschnitt 8).

### 2c. Schriftgrößen und Zeilenhöhen (wirksam)

| Element | Größe | Gewicht (angefordert) | Zeilenhöhe | Fundstelle | gemessen |
|---|---|---|---|---|---|
| Fließtext `body` | `16px` | 400 | `1.58` | `styles.css:31` bis `32` | 16 px / 25,28 px |
| Text in den Reiterpanels | `1rem` | 400 | `1.65` | `design.css:171` | 16 px / 26,4 px |
| Absatzbreite im Panel | `max-width:85ch` | | | `design.css:16`, `:176` | 759 px |
| `h1` (Thementitel) | `clamp(1.9rem, 3.2vw, 3.25rem)`; ab 1200 px `clamp(1.9rem, 2.4vw, 2.5rem)`; bis 640 px `2rem` | 700 (Browser) | `1.08`, `letter-spacing:-.035em` | `styles.css:298`, `design.css:343`, `styles.css:684` | 34,56 px bei 1440; 30,72 px bei 1280; 32 px bei 1000 und 390 |
| Themenkennung „Thema 01: Wärmeleitung“ | `.76rem` | 850 | geerbt | `styles.css:297` (`letter-spacing:.06em`) | 12,16 px |
| `h2` im Lerntext | `1.4rem`; bis 640 px `1.25rem` | 700 | `1.25` | `styles.css:332`, `:688` | auf der Simulationsseite ausgeblendet (`design.css:46`) |
| `h3` (Simulationstitel) | `.95rem` | | `1.35` | `runde11.css:13`, `design.css:137` | nur für Screenreader sichtbar (`design.css:268`) |
| `h3` im Reiterpanel | `1.08rem` | 700 | `1.65` (geerbt) | `styles.css:334` | 17,28 px / 28,5 px, Abstand `1.55rem 0 .5rem` |
| Themenreiter (Lerntext, Simulationen …) | `.84rem` | 750 | geerbt | `styles.css:317` bis `326` | 13,44 px |
| Simulationswahl (Stationär …) | `.85rem` | 400 | geerbt | `design.css:183` | 13,6 px |
| Unterreiter (Versuche, Modell, Code) | `13px` | 600 | `1.3` | `runde11.css:46`, `:98` | 13 px / 16,9 px |
| „Berechnen“, „Standardwerte“ ab 1200 px | `.78rem` | 780 | geerbt | `design.css:355` | 12,48 px |
| dieselben unter 1200 px | `.875rem` | 780 | geerbt | `pilot.css:119` | 14 px |
| Wand/Rohr/Kugel | `.875rem` | 400 | geerbt | `pilot.css:119` | 14 px |
| Ghost-Knöpfe im Panel | `1rem` | 780 | `1.65` | `styles.css:405` bis `412` | 16 px |
| „ohne Vermutung aufdecken“ | `.85rem` | 400 | geerbt | `runde6-experiments.css:41` | 13,6 px |
| Reglerbeschriftung ab 1200 px | `.78rem` | 700 | `1.5` | `design.css:399`, `:184`, `runde11.css:28` | 12,48 px / 18,72 px |
| Reglerbeschriftung unter 1200 px | `.75rem` | 700 | `1.5` | `design.css:129` | 12 px |
| Feld (Grundgröße, Fehlertext) | `.8rem` | 650 | geerbt | `design.css:185` | 12,8 px |
| Zahlenfeld ab 1200 px | `.83rem` | 650 | | `design.css:352` | 13,28 px |
| Zahlenfeld unter 1200 px | `.8rem` | 650 | | `design.css:131` | 12,8 px |
| Fehlertext unter Feld | `.8rem` | 400 | `1.9` | `pilot.css:9`, `typeset.css:26` | 12,8 px / 24,32 px |
| Statuszeile ab 1200 px | `.72rem` | 400 | `1.35` | `design.css:356`, `pilot.css:120` | 11,52 px |
| Statuszeile unter 1200 px | `.8rem` | 400 | `1.35` | `pilot.css:120` | 12,8 px |
| Lesehinweis unter dem Bild | `.8rem` | 400 | `1.4` | `runde11.css:109` | 12,8 px |
| Rechenwerte Überschrift | `.75rem` | 700 | | `pilot.css:230`, `design.css:333` | 12 px |
| Rechenwerte `dt` | `.75rem` | 400 | `1.35` | `runde11.css:40`, `pilot.css:233` | 12 px |
| Rechenwerte `dd` | `.85rem` | 650 | `1.35`, `font-variant-numeric: tabular-nums` | `runde11.css:41`, `pilot.css:234` | 13,6 px |
| Rechenwerte Kasten (Grund) | `.8rem` | | | `pilot.css:229` | 12,8 px |
| „Für Fortgeschrittene“ ab 1200 px | `.77rem` | 650 | | `design.css:366` bis `367` | 12,32 px |
| „Für Fortgeschrittene“ unter 1200 px | `1rem` | 700 | | `runde6-pilot.css:3`, `design.css:161` | 16 px |
| Tooltip | `.8rem` | 400 | `1.5` | `design.css:61` | 12,8 px |
| „?“ | `.7rem` | 650 | `1` | `design.css:59` | 11,2 px |
| Summary Versuch / Modellabschnitt | `1rem` | 700 | | `runde11.css:103` | 16 px |
| Prognosefrage (`legend`) | `1rem` | 700 | | `runde6-experiments.css:8` bis `13` | 16 px |
| Sperrhinweis | `.85rem` | 400 | `1.4` | `runde7-layout.css:83` bis `90` | 13,6 px |
| Tabelle Körper | `.84rem` | 400 | `1.45` | `styles.css:367` | 13,44 px |
| Tabellenkopf | `.76rem`, `letter-spacing:.01em` | 700 (Browser) | `1.45` | `styles.css:369` | 12,16 px |
| Formel als Block (`.formula`) | `1.2rem`; bis 640 px `1.08rem` | 400 | | `styles.css:356`, `:689` | 19,2 px |
| Brotkrumen | `.83rem`, erste Angabe 850 | | | `styles.css:232` bis `233` | 13,28 px |
| Sprachknopf | `.72rem` | 780 | | `audit.css:199` | 11,52 px |
| „↔ EN“ im Sprachknopf | `.65rem` | 400 | | `design.css:86` | |
| „Lokal gespeichert“ | `.72rem` | 400 | | `styles.css:255` | 11,52 px |
| Entwurfsbanner | `.88rem` | | `1.5` | `audit.css:14` | 14,08 px |
| Seitenleiste: Titel / Navigation / Kennung | `1.08rem` 800 / `.79rem` 650 / `.72rem` 850 | | | `styles.css:106`, `:208`, `:207` | |

## 3. Abstände und Maße

### 3a. Seitenrahmen

| Punkt | Wert | Fundstelle | gemessen |
|---|---|---|---|
| Spalten der App | `grid-template-columns: 300px minmax(0, 1fr)` | `styles.css:67` | Seitenleiste 300 px |
| Seitenleiste Innenabstand | `1.4rem 1.15rem 1.1rem`, Abstand `1rem` | `styles.css:76` bis `77` | |
| Kopfleiste | Höhe `64px`, Innenabstand `0 1.5rem` (bis 640 px `0 .8rem`), `gap:1rem` | `styles.css:222`, `:227`, `:676` | 64 px |
| Scrollbereich | eigener Bereich `.workspace-scroll` unter der Kopfleiste, `scrollbar-gutter: stable`; `html` und `body` scrollen nicht | `workspace.css:2` bis `12` | |
| Inhaltsbreite | `.learning-layout { width:min(1480px, 100%); margin:0 auto; padding:1.35rem }`, ab 1200 px `padding-block:1rem`, bis 640 px `.7rem`; eine Spalte (`pilot.css:74`), `gap:2rem` (`design.css:9`) | `styles.css:274` bis `276` | |
| Themenkopf `#topic-header` | `margin:1rem 1.35rem 0`; bis 767 px `.7rem .7rem 0`; weiß | `runde11.css:2`, `:80` | |
| Themenkopf innen | `.lesson-intro { padding:1rem 1.4rem .7rem }`, bis 767 px `.7rem` | `runde11.css:4`, `:81` | |
| Reiterzeile | `padding:.35rem 1.4rem 0`, bis 767 px `.25rem .4rem 0`, Unterlinie `1px solid var(--line)` | `runde11.css:5`, `:82`, `styles.css:316` | |
| Simulationsbereich `#practice-view` | `padding:.3rem 1.4rem 1rem` (gilt auf allen Breiten, weil die ID-Regel die Handyregel schlägt) | `design.css:181`, `:267` | Nutzbreite bei 1440: 1037 px; bei 1280: 877 px; bei 1000: 597 px; bei 390: 308 px |
| Simulationswahl | `margin:0 0 .45rem`, `padding:.25rem 0`, `gap:.5rem`, `position:static` | `runde11.css:11`, `pilot.css:282`, `design.css:182`, `design.css:80` | |
| Unterreiter-Block | `margin-top:1.8rem`, Linie oben `1px solid var(--line)` | `runde11.css:96`, `design.css:166` | |
| Reiterpanel | Rahmen `1px solid #39718e`, `padding:0 .8rem`; Panel innen `1.2rem 0` | `runde11.css:101`, `design.css:171` | |

### 3b. Ecken (`border-radius`)

| Element | Wert | Fundstelle |
|---|---|---|
| Panels (`--radius`) | `4px` | `design.css:2` |
| Primär-, Ghost-, Download-Knopf, Simulationswahl, Wand/Rohr/Kugel | `4px` | `design.css:38`, `:325` |
| Unterreiter | `6px 6px 0 0` | `runde11.css:98` |
| Rechenwerte-Kasten | `4px` | `design.css:78` |
| Tooltip | `4px` | `design.css:61` |
| Sprachknopf | `4px` | `design.css:38` (Ghost) |
| Zahlenfeld, Schieberegler-Box | `8px` | `pilot.css:8` |
| „?“-Knopf | `50%` | `design.css:59` |
| Themenreiter-Balken | `3px 3px 0 0` | `styles.css:327` |
| Auflösung, Tabellenrahmen, Formelkasten, Bilder im Text | `0` | `design.css:37`, `:18` |
| Textknopf, Menüknopf (`.text-button`, `.icon-button`) | `9px` (nicht angeglichen) | `styles.css:406` |
| Suchfeld Seitenleiste | `11px` (die Regel `design.css:7` zielt auf `.search-field`, das Feld heißt `.search-box`) | `styles.css:164` |
| Farbskalen-Auswahl | `3px` | `runde6-pilot.css:8` |
| Fortschrittsbalken | `0` | `design.css:67` |

### 3c. Raster des Simulationsbereichs

| Breite (Fenster) | Raster `.pilot-workspace` | Bild | Knöpfe (`.pilot-commands`) | Regler | Rechenwerte | Fundstelle |
|---|---|---|---|---|---|---|
| ab 1200 px | `grid-template-columns: minmax(0,1fr) 128px 180px; gap: .5rem 24px` | Spalten 1 und 2 (gemessen 833 px breit bei 1440) | Spalte 3, 180 px, Knöpfe untereinander und volle Breite | Spalte 1 unter dem Bild, 3 Spalten | Spalte 2 bis 3 neben den Reglern (128 + 24 + 180 = 332 px) | `runde11.css:15`, `:60`, `:61` |
| 768 bis 1199 px | `minmax(0,1fr) 180px` | Spalte 1 | Spalte 2, Knöpfe nebeneinander mit Umbruch | volle Breite, 3 Spalten | volle Breite unter den Reglern | `runde11.css:69` bis `78` |
| bis 767 px | Spalte (Flex), `gap:.65rem` | oben, **klebt** beim Scrollen (`position:sticky; top:0; z-index:5`, weiß, Schatten `0 6px 8px -6px #0003`) | nach den Rechenwerten | 1 Spalte | direkt unter dem Bild | `runde11.css:79` bis `93` |

Reihenfolge bis 767 px (`order`): Bild 1, Rechenwerte 2, Knöpfe 3, Regler 4, „Für Fortgeschrittene“ 5, Rechenbudget 6, weitere Abbildungen 7 (`runde11.css:85` bis `91`).

Grundwert ohne Breitenabfrage: `minmax(0,1fr) 146px 180px` (`runde11.css:15`); er wird auf allen Breiten von den Abfragen oben überstimmt. Kommentar zu 1200 px: „Move 18 px to the lower controls; the image still spans the same width“ (`runde11.css:59`).

Die Regel `runde7-layout.css:3` bis `23` (700 bis 1365 px: eine Spalte, Bild mit `aspect-ratio: 13/6`, `min-height:260px`) ist durch `runde11.css` überstimmt (gleiche Spezifität, später geladen); gemessen wirkt sie nicht.

### 3d. Simulationsbild

| Punkt | Wert | Fundstelle |
|---|---|---|
| Höchstbreite | `max-width:780px; justify-self:center` am Bildrahmen; am Bild `max-width: var(--simulation-image-width, 780px)` | `runde11.css:33` bis `34` |
| Breitenwert | `Math.min(780, image.naturalWidth \|\| 780) + 'px'` | `simulation-layout.js:10` |
| Bilddateien | PNG 1560 × 720 px (Seitenverhältnis 13:6 = 2,167), also doppelte Pixeldichte bei 780 px | `01_conduction/abbildungen/*.png`, `02_convection/abbildungen/*.png`, `en/abbildungen/` |
| Höhe | `height:auto; aspect-ratio:auto; object-fit:contain` | `runde11.css:34` |
| gemessen | 780 × 360 px bei 1440; 673 × 311 px bei 1280 (Bildspalte schmaler als 780); 393 × 181 px bei 1000; 308 × 142 px bei 390 | |
| weitere Abbildungen (Skizze im Reiter „Modell“) | `max-width:660px`, zentriert, Bildunterschrift `.82rem` muted | `runde10.css:18` bis `21` |

### 3e. Knöpfe und Zielgrößen

| Element | Maße | Fundstelle | gemessen |
|---|---|---|---|
| „Berechnen“, „Standardwerte“ ab 1200 px | `padding:.45rem .55rem; min-height:2rem`, volle Spaltenbreite | `design.css:355`, `runde11.css:61` | 180 × 36 px |
| dieselben unter 1200 px | `padding:.45rem .65rem; min-height:2.2rem`, Breite nach Inhalt, Abstand `.35rem` | `pilot.css:118` bis `119` | 91 × 38 und 119 × 38 px |
| Wand/Rohr/Kugel ab 1200 px | Raster 3 Spalten, `gap:4px`, `padding:.5rem 4px` | `runde11.css:62` bis `63`, `design.css:325` | 57 × 40 px |
| Wand/Rohr/Kugel unter 1200 px | `padding:.5rem .75rem`, `min-height:2.2rem` | `design.css:325`, `pilot.css:119` | 61 × 40 px |
| Simulationswahl | `padding:.5rem .75rem` | `design.css:325` | 83 × 39 px („Stationär“) |
| Unterreiter | `min-height:44px; padding:.65rem .4rem` | `runde11.css:98` | 44 px hoch (bei 390 px: 56 px, Text bricht um) |
| Summary von Versuch und Modellabschnitt | `min-height:44px` | `runde11.css:103` | 44 px |
| Ghost-Knöpfe im Panel | `padding:.62rem .78rem` | `styles.css:412` | 48 px hoch |
| „ohne Vermutung aufdecken“ | `min-height:2.2rem; padding:.2rem 0` | `runde6-experiments.css:34` bis `45` | 35 px hoch |
| „?“-Hilfe | `width:1.05rem; min-height:1.05rem` | `design.css:59` | 16,8 × 16,8 px (unter 24 px) |
| Sprachknopf | `padding:.35rem .55rem` | `audit.css:199` | 93 × 31 px |
| Menüknopf (bis 920 px) | `2.35rem` × `2.35rem` | `styles.css:665` | |
| Links Downloads, Release | `min-width:24px; min-height:24px` („R7-24: … at least 24 by 24 pixels“) | `runde7-layout.css:61` bis `71` | |
| Zielgröße 44 px | nur Unterreiter, Summaries, Quiz (`audit.css:142`, `:154`); nicht für Simulationsknöpfe | | |

### 3f. Regler-Raster

| Punkt | Wert | Fundstelle | gemessen 1440 |
|---|---|---|---|
| Spalten | `repeat(3, minmax(0,1fr))` ab 768 px; `minmax(0,1fr)` bis 767 px | `runde11.css:25`, `:88` | 3 × 224 px |
| Abstand | unter 1200 px `.6rem 1.1rem`; ab 1200 px `.4rem 4px` | `runde11.css:25`, `:64` | |
| Feld innen | `grid-template-columns: minmax(0,1fr) 64px`; Abstand `.2rem .75rem`, ab 1200 px `.15rem 4px` | `runde11.css:26`, `:65` | Regler 156 px, Zahl 64 px |
| Anordnung | Zeile 1 Beschriftung über beide Spalten, Zeile 2 Schieberegler links und Zahlenfeld rechts, Meldungen darunter über beide Spalten | `runde7-layout.css:127` bis `133` | |
| Beschriftung | `display:block; padding-right:1.4rem` (Platz für „?“), Mindesthöhe `1.75rem` ab 1200 px, sonst `2.2rem` | `pilot.css:256`, `runde11.css:28`, `:66` | 28 px |
| Zahlenfeld | Breite `64px`; Höhe `1.7rem` ab 1200 px, sonst `1.55rem`; `padding:.2rem .3rem` bzw. `.25rem .35rem`; rechtsbündig, `tabular-nums`, Rand `1px solid var(--line)`, weiß | `runde11.css:27`, `design.css:352`, `:131`, `pilot.css:8`, `:89`, `:125` | 64 × 27 px |
| Schieberegler | Höhe wie Zahlenfeld, `accent-color: var(--blue)`, ohne Rahmen | `pilot.css:88`, `design.css:353` | 156 × 27 px |
| Hinweis „0 bis 120“ | im Feld vorhanden, aber ausgeblendet | `pilot.css:127` | |
| Einheit | `.parameter-unit { margin-left:.18em; white-space:nowrap }`, Bruch in der Einheit `.85em` | `design.css:275` bis `276` | |
| Mehr Regler (Gitterpunkte, Vergleich, Farbskala) | `<details class="pilot-advanced">` „Für Fortgeschrittene“, 2 Spalten, `gap:.45rem .6rem`; ab 1200 px Linie oben | `pilot.js:92` bis `95`, `design.css:366` bis `368` | |

### 3g. Rechenwerte-Kasten

| Punkt | Wert | Fundstelle |
|---|---|---|
| Kasten | Fläche `--soft`, `border-radius:4px`, `padding:.6rem .65rem`, keine Höhenbegrenzung | `pilot.css:229`, `design.css:78`, `runde11.css:35` |
| Überschrift | immer „Rechenwerte“ / „Calculated values“ (vor und nach der Rechnung), Abstand unten `.3rem` | `pilot.js:232`, `runde6-pilot.css:47` |
| Werteraster | 2 Spalten, `gap:0` | `runde11.css:36` |
| Zeile | `display:block; padding:.35rem .4rem; border-top:1px solid #dfe5ec` | `runde11.css:38` |
| `dd` | `margin:.12rem 0 0`, `font-size:.85rem`, Gewicht 650 | `runde11.css:41`, `pilot.css:234` |
| Inhalt vor der ersten Rechnung | Werte des Standardbeispiels aus `simulation-examples.js` | `pilot.js:169` bis `185` |
| gemessen | 332 × 148 px bei 1440 (vier Werte); Zeile 156 × 53 px | |

## 4. Umbruchbreiten

Alle Abfragen sind Fensterbreiten (`@media`), außer wo „Container“ steht.

| Breite | Was sich ändert | Fundstelle |
|---|---|---|
| ab 1200 px | Dreispaltenraster Bild, Knöpfe 180 px, Regler 3 Spalten darunter, Rechenwerte rechts darunter; Knöpfe gestapelt, kleinere Schrift (`.78rem`); `h1` mit `2.4vw`; „Für Fortgeschrittene“ mit Linie oben; Inhaltsverzeichnis im Lerntext klebt rechts | `runde11.css:58` bis `68`, `design.css:338` bis `371`, `:398` bis `400` |
| 768 bis 1199 px | Zweispaltenraster (Bild links, Knöpfe 180 px rechts); Regler, Rechenwerte, Zusatz darunter über volle Breite; Knöpfe nebeneinander | `runde11.css:69` bis `78` |
| bis 1199 px | Inhaltsverzeichnis des Lerntexts wird waagrechte Leiste oben | `design.css:372` bis `377`, `:389` |
| bis 1120 px | alte Zweispalten-Lernansicht (wirkt nicht, `pilot.css:74` setzt eine Spalte) | `styles.css:646` bis `651` |
| bis 1050 px | alte Simulationsspalten (nicht kompakt); für die Runde-12-Seite überstimmt | `pilot.css:150` bis `155` |
| ab 1000 px | Skizzenzeile, feste Spalten breiter Tabellen | `runde10.css:5` bis `13` |
| bis 920 px | Seitenleiste wird Schublade (`position:fixed`, Breite `min(330px, 88vw)`, `translateX(-105%)`, Übergang `.24s`), Menüknopf erscheint; Notizen und Downloads zweispaltig | `styles.css:653` bis `672`, `workspace.css:27` bis `30` |
| bis 767 px | **Handy: Bild oben und klebend**, dann Rechenwerte, Knöpfe, Regler einspaltig; Themenkopf mit kleineren Rändern | `runde11.css:79` bis `93` |
| bis 640 px | Kopfleiste schmaler, Brotkrumen und „Lokal gespeichert“ ausgeblendet, `h1` `2rem`, Themenreiter waagrecht scrollbar | `styles.css:674` bis `707` |
| bis 600 px | Rechenwerte 2 Spalten mit Umbruch in `dd`, Tabellen im Reiterpanel mit festen Spaltenbreiten und Silbentrennung, Auflösung ohne seitlichen Innenabstand, Modellliste einspaltig | `runde10.css:26` bis `28`, `runde6-pilot.css:68` bis `72`, `runde11.css:120` bis `130`, `design.css:54` |
| bis 540 / 500 / 450 px | alte Regler- und Zusatzspalten auf 1 | `pilot.css:22`, `runde6-pilot.css:15`, `pilot.css:156` bis `159` |
| bis 420 px | „↔ EN“ im Sprachknopf ausgeblendet, engere Kopfleiste | `design.css:87`, `audit.css:202` bis `206` |
| Container ab 500 / 720 px, bis 599 / 499 px | alte Spaltenzahlen der Regler (3 / 4) und Formularflächen; von den `#practice-view`-Regeln überstimmt | `pilot.css:265` bis `281`, `design.css:143` bis `146` |
| `prefers-reduced-motion: reduce` | keine Animation (Fortschrittsbalken, Übergänge), kein weiches Scrollen | `design.css:74`, `styles.css:709` bis `711` |

Reiter als Akkordeon: **nicht gefunden**. Die drei Unterreiter bleiben auch auf dem Handy ein Raster mit drei gleich breiten Spalten (bei 390 px je 97 px, Text bricht um); Kommentar „R12: three full-width tabs with an attached panel, also on narrow screens“ (`runde11.css:95`). Die Themenreiter oben bleiben eine Zeile und scrollen waagrecht (`runde11.css:6` bis `7`).

## 5. Rangfolge der Knöpfe

Grundsatz laut Kommentar: „G2: the calculation is the only dark primary action in the simulation.“ (`design.css:323`)

| Rang | Knöpfe | Stil | Fundstelle |
|---|---|---|---|
| 1 primär | „Berechnen“ (`.primary-button.pilot-run`, `type=submit`); während einer Animation auch „Abspielen“ (`.pilot-play`) | navy `#102d49`, weiße Schrift, Rand `#173d5e`, 4px Ecken, Gewicht 780; kein Hover-Wechsel | `design.css:331`, `styles.css:405` bis `410`, Vorlage `sprachen.js` Schlüssel `pilot_0200` |
| 2 sekundär | „Standardwerte“ (`.ghost-button.pilot-reset`), „Erneut abspielen“, Budget-Vorschläge | Fläche `--soft`, Schrift `#39718e`, Rand `#c9dfed`, 4px Ecken, Gewicht 780 | `design.css:330` |
| 3 Umschalter | Simulationswahl (`role=tab`, `aria-selected`) und Wand/Rohr/Kugel (`aria-pressed`) | inaktiv `--soft` / `#39718e` / Rand `#c9dfed`, Gewicht 400; aktiv `#d9edf9` / navy / Rand `#93bbd4` mit 2px Unterstrich innen `#39718e`; Hover `#dfedf6` | `design.css:324` bis `329`, `:391` bis `393` |
| 4 Ghost im Panel | „Ausgangslage einstellen“, „Auflösung zeigen / verbergen“, „Alle Versuche zurücksetzen“, „Für Fortgeschrittene“ (Versuch 6) | transparent, navy, Rand `--line`, Hover `--soft`; gesperrt grau auf `--soft`, `cursor:not-allowed`; Zurücksetzen ohne Daten `opacity:.45` | `styles.css:412` bis `413`, `runde7-layout.css:75` bis `82`, `runde10.css:31` bis `32` |
| 5 Textknopf | „ohne Vermutung aufdecken“ | ohne Rand, unterstrichen (`text-underline-offset:.18em`), `#39718e`, `.85rem` | `runde6-experiments.css:34` bis `45` |
| gesperrt während einer Rechnung | alle Knöpfe, Regler und Zahlenfelder | `opacity:.6`, `disabled` | `pilot.css:28`, `pilot.js:345` bis `352` |

## 6. Reiter

### 6a. Drei Ebenen

| Ebene | Aufbau | Anzahl und Namen (DE / EN) | Fundstelle |
|---|---|---|---|
| Themenreiter im Themenkopf | `div.lesson-mode-tabs[role=tablist]`, Knöpfe `.tab[role=tab]` mit `aria-selected`, `aria-controls`; Panels `section[role=tabpanel]` | 5: Lerntext / Learning text; Simulationen / Simulations; Wissenstest / Knowledge check; Anwenden & erklären / Apply & explain; Lernziel-Check / Learning objectives check | `index.html:104` bis `110`, `sprachen.js` (`html_0265`, `topic_0238`, `html_0299`, `html_0300`, `html_0292`) |
| Simulationswahl | `div.simulation-tabs[role=tablist]` mit `aria-label` „Simulation wählen“ / „Choose simulation“; Knöpfe `role=tab`, `id=simulation-tab-<modell>`, `aria-controls=simulation-detail`; Panel `section#simulation-detail[role=tabpanel]` | Thema 1: 3 (Stationär / Steady state; Instationär / Transient; Instationär in 2D / Transient in 2D). Thema 2: 2 (Ohne Rippe / Without a fin; Mit Rippe / With a fin) | `sprachen.js` `topic_0239`, `topic.js:227`, `01_conduction/lesson.js:16`, `:151`, `:246`, `02_convection/lesson.js:16`, `:118` |
| Unterreiter unter der Simulation | `div.reference-tabs[role=tablist]` mit `aria-label` „Zur Simulation“ / „About the simulation“; Knöpfe `role=tab`, `id=reference-<modell>-<key>-tab`, `aria-controls`; Panels `section.reference-panel[role=tabpanel]` mit `aria-labelledby` und `tabindex=0` | **3** (in v8 bestätigt): Versuche / Experiments; Modell / Model; So rechnet der Code / How the code calculates. Voreinstellung „Versuche“ | `topic.js:165` bis `225`, `sprachen.js` `reference_experiments`, `r12_reference_model`, `reference_code`, `reference_title` |

### 6b. Tastenbedienung

| Ebene | Tasten | Fundstelle |
|---|---|---|
| alle drei Ebenen | Pfeil links / rechts (mit Umlauf vom letzten zum ersten), Pos1, Ende; wählt den Reiter sofort und setzt den Fokus; „roving tabindex“ (aktiv `0`, sonst `-1`) | Themenreiter `app.js:1228` bis `1232`; Simulationswahl `topic.js:258` bis `263`; Unterreiter `topic.js:207` bis `216` |
| Unterreiter | beim Fokus wird der Reiter in den sichtbaren Bereich geschoben (`reveal`) | `topic.js:201` bis `206` |
| Simulationswahl | Wechsel setzt die Unterreiter dieses Modells auf „Versuche“ zurück und scrollt zur Simulation | `topic.js:231` bis `255` |
| `aria-orientation` | nicht gesetzt (Voreinstellung waagrecht) | |

### 6c. Aussehen

| Ebene | inaktiv | aktiv | Fundstelle |
|---|---|---|---|
| Themenreiter | Text `--muted`, transparent, `padding:.7rem .9rem .78rem` | Text `--blue`, Balken `::after` 3px, `left/right:.8rem`, `bottom:-1px`, Ecken `3px 3px 0 0` | `styles.css:317` bis `329` |
| Simulationswahl | siehe Abschnitt 5, Rang 3 | | `design.css:324` bis `329` |
| Unterreiter | Raster `repeat(3, minmax(0,1fr))`, `gap:8px`; Fläche `#edf2f6`, Rand `1px solid var(--line)` ohne Unterkante, Ecken `6px 6px 0 0`, Text `#39718e` 13px 600, `line-height:1.3`, umbrechend | Fläche weiß, Rand `#39718e`, oben 3px, `z-index:1`; ein weißer Streifen `::after` (2px, `bottom:-1px`) verbindet den Reiter mit dem Panelrahmen | `runde11.css:97` bis `101` |

### 6d. Inhalt der Unterreiter

| Reiter | Inhalt | Fundstelle |
|---|---|---|
| Versuche | Satz „Erst vermuten, dann rechnen.“ / „First predict, then calculate.“; dann je Versuch ein `<details class="experiment-card">` (der **erste offen**, die anderen zu), Summary fett 700, `min-height:44px`; Karte `padding:.65rem 0`, Linie unten; am Ende „Alle Versuche zurücksetzen“ | `topic.js:87` bis `95`, `:109` bis `110`, `:187` bis `189`, `runde11.css:103`, `:105` |
| Modell | fünf `<details class="reference-model-section">`, alle zu: Physikalisches Problem / Physical problem; Annahmen / Assumptions; Was die Simulation macht / What the simulation does; Regler und Einheiten / Sliders and units; So liest du die Ergebnisse / How to read the results. Abschnitt `padding:.6rem 0`, Linie unten | `topic.js:169` bis `186`, `runde11.css:102` bis `104` |
| So rechnet der Code | Inhalt der früheren `details.topic-math` (Hinweissatz, `h3`, Formeln als Block), linksbündig | `topic.js:68` bis `71`, `design.css:193` bis `198` |

Wie „Versuche“ die Auflösung aufklappt (`topic.js:87` bis `163`):

1. Versuch mit Vermutung: `fieldset.experiment-prediction` mit `legend` (Frage, `#39718e`, 700) und Radioknöpfen (`1.1rem`, `accent-color: var(--blue)`); gewählte Antwort wird `#39718e` und 650 (`runde6-experiments.css:2` bis `32`).
2. Knopf „Auflösung zeigen“ (`ghost-button`, `aria-controls=<id>-aufloesung`, `aria-expanded`). Ohne gewählte Vermutung ist er `disabled`, daneben „Wähle zuerst eine Vermutung.“ (`aria-describedby`), daneben der Textknopf „ohne Vermutung aufdecken“.
3. Klick: Text wird „Auflösung verbergen“, `aria-expanded=true`, `div.experiment-resolution` verliert `hidden`. Darin zuerst `div.experiment-comparison[role=status][aria-live=polite]` mit „Deine Vermutung“ (✓ oder ×) und „Richtig“ (zweispaltig `10rem` + Rest), dann der Auflösungstext. Die Radioknöpfe werden gesperrt.
4. Aussehen der Auflösung: Fläche `--soft`, `padding:.9rem 1rem`, `margin-top:.8rem`, keine Ecken (`design.css:37`, `:199`); bis 600 px ohne seitlichen Innenabstand (`runde11.css:129`).
5. Zustand (gewählt, aufgedeckt, übersprungen) wird im Lernstand gespeichert und nach Neuladen wiederhergestellt (`topic.js:79` bis `83`, `:149` bis `152`).
6. Optional „Ausgangslage einstellen“ (setzt die Regler, scrollt zur Simulation, Status „Ausgangslage eingestellt. Ändere jetzt nur, was unter „Das änderst du“ steht.“) vor der Frage (`topic.js:93`, `:97` bis `104`).

## 7. Regler

### 7a. Aufbau eines Feldes (Vorlage `sprachen.js` Schlüssel `pilot_0194`, Aufbau `pilot.js:400`)

```html
<div class="pilot-field" [data-geometry="…"]>
  <label class="parameter-label" for="<modell>-<key>-range">Text <math>Symbol</math><span class="parameter-unit">[Einheit]</span></label>
  <input id="<modell>-<key>-range" class="pilot-slider" type="range" min max step aria-label="<Name> (Gedankenstrich) Regler" aria-valuetext="80,5 °C" data-key="<key>">
  <input class="pilot-value" type="text" inputmode="decimal" required name="<key>" data-min data-max data-step aria-label="<Name> (Gedankenstrich) Wert">
  <small>min bis max</small>           <!-- ausgeblendet -->
  <button class="parameter-help" aria-expanded="false">?</button>   <!-- von parameter-help.js angehängt -->
</div>
```

Im Original steht im `aria-label` zwischen Name und „Regler“ bzw. „Wert“ ein Halbgeviertstrich; hier umschrieben. Beispiel gemessen: `aria-label="Oberflächentemperatur T W eins (°C) … Regler"`.

| Punkt | Wert | Fundstelle |
|---|---|---|
| Kopplung | Schieberegler schreibt formatiert ins Zahlenfeld; gültige Zahl setzt den Schieberegler (der rundet auf sein Raster, die getippte Zahl bleibt) | `pilot.js:249` bis `258`, `:430` bis `437` |
| Zeitpunkt der Prüfung | bei jeder Eingabe (Meldung sofort), übernommen bei `change` oder Enter | `pilot.js:438` bis `443` |
| Neu rechnen | stationär und Thema 2 (`auto:true`) rechnen nach der ersten Rechnung 500 ms nach jeder Änderung selbst neu; instationär nur über „Berechnen“ | `pilot.js:16`, `:428`, `02_convection/controls.js:6`, `:57` |
| Zeitregler `t_end` | logarithmisch: Regler 0 bis 1000 ↔ 0,01 bis 3600 s | `numeric-input.js:9` bis `10`, `pilot.js:405` bis `408` |
| Budgetmarke | 2px Strich `#153d59` im Reglerhintergrund an der erlaubten Höchstdauer, Text `.72rem` `#305f7c` | `runde7-layout.css:117` bis `118` |
| Formular | `novalidate`; Meldungen über `setCustomValidity` und `reportValidity` | Vorlage `pilot_0200`, `pilot.js:296`, `:439` |

### 7b. `numeric-input.js` (Zahlen lesen)

| Regel | Wert | Zeile |
|---|---|---|
| Leerzeichen | werden entfernt | 4 |
| mehrdeutig (abgelehnt) | `/^[1-9]\d{0,2}([.,]\d{3})+$/`, z. B. `7.800`, `7,800`, `1.234` | 5 |
| erlaubtes Format | `/^[+-]?(?:\d+(?:[.,]\d*)?\|[.,]\d+)(?:e[+-]?\d+)?$/i`: Komma **oder** Punkt als Dezimalzeichen, Exponent `e` erlaubt; Komma wird zu Punkt | 6 |
| Ausgabe | `String(value)`; DE mit Komma statt Punkt, EN mit Punkt; keine Tausendertrennung; wäre die Ausgabe mehrdeutig, wird eine `0` angehängt (`1.234` → `1,2340`) | 7 |
| gültig | endlich, `min ≤ x ≤ max`; `Nx` und `Ny` ganzzahlig. Die Schrittweite wird **nicht** geprüft | 8 |

Fehlermeldungen (`pilot.js:290` bis `299`, Texte `sprachen.js`):

| Fall | DE | EN |
|---|---|---|
| mehrdeutig | „„<Name>“: Bitte gib die Zahl ohne Tausendertrennzeichen ein, zum Beispiel 7800 oder 7,8.“ | „“<Name>”: please enter the number without a thousands separator, for example 7800 or 7.8.“ |
| keine Zahl | „Bitte gib bei „<Name>“ eine Zahl ein, zum Beispiel <Standardwert>.“ | „Please enter a number for “<Name>”, for example <default>.“ |
| außerhalb | „Bitte prüfe „<Name>“: Erlaubt sind <min> bis <max> <Einheit>.“ | „Please check “<Name>”: allowed values are <min> to <max> <unit>.“ |
| nicht ganzzahlig | „Bitte prüfe „<Name>“: Erlaubt sind nur ganze Zahlen von <min> bis <max>.“ | „… only whole numbers from <min> to <max> are allowed.“ |
| Status beim Absenden | „Bitte alle Parameter innerhalb der angegebenen Grenzen eingeben.“ (rot) | „Please enter all parameters within the specified limits.“ |
| altes Ergebnis | „Das Ergebnis gehört noch zu den letzten gültigen Eingaben.“ | „The result still refers to the last valid inputs.“ |

Darstellung: `small.pilot-field-error[aria-live=polite]` unter dem Feld über beide Spalten, Name mit MathML-Symbol, Einheit gesetzt; Feld bekommt `aria-invalid=true`, `aria-describedby` und die Klasse `is-invalid` (roter Rand) (`pilot.js:269` bis `284`, `runde7-layout.css:94` bis `104`).

### 7c. `parameter-help.js` (Fragezeichen)

| Punkt | Wert | Zeile |
|---|---|---|
| Erzeugung | je Feld ein `button.parameter-help` mit Text `?`, nur wenn ein Hilfetext `help_<modell>_<key>` oder `help_<key>` existiert | 14 bis 19 |
| Beschriftung | `aria-label` „Erklärung: <Beschriftung>“ / „Explanation: …“, `aria-expanded` | 20 bis 21 |
| Tooltip | `div.pilot-tooltip[role=tooltip]` am Ende von `body`, `aria-describedby` an Knopf, Zahlenfeld **und** Schieberegler | 22 bis 24 |
| Öffnen | Zeiger darüber: nach **500 ms**; Tastaturfokus: sofort; Klick: öffnet und hält offen (zweiter Klick schließt) | 33, 37, 39 |
| Schließen | Zeiger verlässt Knopf: nach 150 ms (außer gehalten oder fokussiert); Escape; Klick außerhalb; Scrollen im Arbeitsbereich; Fenstergröße ändern; Blur | 6 bis 10, 34, 36, 38 |
| Lage | rechtsbündig zum Knopf (`left = max(8, min(innerWidth - w - 8, r.right - w))`), 6px darunter, sonst 6px darüber | 29 bis 31 |
| Aussehen | `position:fixed; z-index:100; max-width:min(280px, calc(100vw - 16px)); padding:.6rem .75rem` | `design.css:61` |
| Knopf | `position:absolute; top:0; right:0` im Feld, Kreis `1.05rem`, `cursor:help`, Fokus `2px solid var(--blue)` | `design.css:57` bis `60` |

## 8. Formelsatz

| Punkt | Wert | Fundstelle |
|---|---|---|
| Technik | eigener TeX-Teilmengen-Parser → **natives MathML** (`<math display="inline">` bzw. `display="block"`, darin `<semantics>…<annotation encoding="application/x-tex">`); kein KaTeX, kein MathJax (nicht gefunden) | `math.js:22` bis `226` |
| Aufruf | `window.PDC_MATH.render(tex, display)`; bei Fehler `<span class="math-fallback">` | `math.js:221` bis `226` |
| kursiv / aufrecht | einzelne Buchstaben `<mi>` (Chrome zeichnet sie kursiv über `text-transform: math-auto`, gemessen); Wörter mit mehr als 3 Buchstaben und `in, out, sp, end, opt, cl, bias` als `<mtext>` aufrecht; `\mathrm{}` und `\text{}` → `<mtext>` aufrecht; `exp, min, max, sin, cos, tan, ln` → `<mi mathvariant="normal">` | `math.js:90` bis `93`, `:108` bis `110`, `:121` bis `127` |
| griechische Buchstaben | als `<mi>` (λ, ρ, α, ϑ …), Operatoren als `<mo>` | `math.js:4` bis `12`, `:114` bis `117` |
| Index | `T_{\mathrm{W}1}` → `T` kursiv, `W` aufrecht, `1` | gemessen `pilot.js:23` |
| Überpunkt | `\dot Q`, `\dot q`: eigener runder Punkt (`mspace.math-dot-mark` `.16em`, `border-radius:50%`) | `math.js:101` bis `107`, `typeset.css:21` |
| Strichstärke | `math { font-weight:400 !important; -webkit-text-stroke: calc(.024em * var(--formula-bold)) currentColor }` (sichtbar etwas kräftiger); im Druck stattdessen `font-weight:700` synthetisch | `typeset.css:5`, `:8` bis `10` |
| Größe | Inline `1em`; Brüche inline `.9em`, im Block `1em`; in `.inline-formula` `.65em` | `typeset.css:11` bis `18` |
| Block | `.formula` `1.2rem`, Farbe navy, transparent, ohne Rand, `padding:16px`; im Reiterpanel linksbündig, `math[display=block]` `margin:1rem 0` | `styles.css:348` bis `359`, `design.css:20`, `:194`, `:198`, `pilot.css:170` |
| Einheiten | in eckigen Klammern hinter dem Symbol: einfache Einheit als Text `[°C]`, `[m]`, `[m²]`, `[mm]`; Bruch-Einheiten als MathML `[\frac{\mathrm{W}}{\mathrm{m} \cdot \mathrm{K}}]` (aufrecht, Malpunkt) | `pilot.js:18` bis `31` |
| Einheiten in Rechenwerten | `W/m²` → `\frac{\mathrm{W}}{\mathrm{m}^2}` als Bruch, sonst Text mit Leerzeichen (`24.000 W`) | `pilot.js:37`, `:505` |
| Dezimalzeichen in TeX | Quelle schreibt `{,}` (z. B. `0{,}49`) → `<mn>0,49</mn>`; in EN wird `{,}` zu `.` | `math.js:139` bis `141`, `i18n.js:53` |
| Tausender in TeX | nur deutsche Quelle: `7.800` wird in EN zu `7\,800` (schmaler Abstand `0.22em`) | `i18n.js:52`, `math.js:73` bis `74` |
| Zahlen in der Oberfläche | `Intl.NumberFormat` mit `de-DE` bzw. `en-GB`; `maximumFractionDigits: 6` (Titel), `3` (Rechenwerte); **mit** Tausendertrennung: DE `24.000`, EN `24,000` (gemessen) | `pilot.js:61`, `:63`, `i18n.js:79` |
| sehr kleine Werte | Betrag kleiner 0,001: wissenschaftlich, Mantisse 4 Stellen: DE `1,234·10⁻⁴` (`\cdot`), EN `1.234×10⁻⁴` (`\times`), in Rechenwerten als MathML | `pilot.js:64` bis `72` |
| Minuszeichen | echtes `−` (U+2212) statt Bindestrich | `pilot.js:71` bis `72`, `math.js:150` |
| Eingabefelder | ohne Tausendertrennung, DE Komma, EN Punkt (siehe 7b) | `numeric-input.js:7` |

## 9. Sprachumschalter

| Punkt | Wert | Fundstelle |
|---|---|---|
| Ort | Kopfleiste rechts (`.topbar-actions`), vor „Lokal gespeichert“ | `index.html:89` bis `92` |
| Element | `button.ghost-button.language-toggle#language-toggle` | `index.html:90` |
| Beschriftung | Flagge (🇩🇪 bzw. 🇬🇧, `aria-hidden`), „DE“ bzw. „EN“, klein „↔ EN“ bzw. „↔ DE“ (`aria-hidden`, bis 420 px ausgeblendet); statischer Platzhalter im HTML „DE \| EN“ | `i18n.js:28` bis `36`, `design.css:84` bis `87` |
| Barrierefreiheit | `aria-label` „Sprache wechseln: Deutsch ist aktiv. Zu Englisch wechseln.“ / „Change language: English is active. Switch to German.“; `aria-pressed=true` bei EN; `data-language` | `i18n.js:30`, `sprachen.js` `language_toggle` |
| Aussehen | Ghost, `.72rem`, `padding:.35rem .55rem`, 4px Ecken; bei EN Rand `--blue` | `audit.css:199` bis `200` |
| Speicher | `localStorage` Schlüssel **`wue-conduction-v04-draft-20260929-language`**, Wert `de` oder `en` (Voreinstellung `de`); bei Fehler Meldung „Sprachwahl bleibt nur bis zum Schließen erhalten …“ in der Speicheranzeige | `i18n.js:4` bis `6`, `:74` |
| Frühstart | Inline-Skript liest den Schlüssel vor dem Laden und setzt `lang` und den Ladetext | `index.html:30` |
| `lang` | `document.documentElement.lang` wird auf `de` / `en` gesetzt (gemessen) | `i18n.js:27` |
| Zustand | bleibt erhalten (gemessen): Reglerwerte (umformatiert, `0,07` → `0.07`), Geometrie, gewählte Simulation und Unterreiter, Ergebnis und Status, offene `details`, Scrollpositionen, Fokus und Textauswahl; Diagramm wird in der neuen Sprache neu gezeichnet (Zwischenspeicher je Sprache) | `app.js:1371` bis `1398`, `pilot.js:613` bis `641` |
| Ereignis | `wue-language-change` mit `{previous, language}` | `i18n.js:77` |
| Locale für Zahlen | `de-DE` / `en-GB` (`window.WUE_I18N.locale`) | `i18n.js:79` |
| Bilder | eigene englische Abbildungen unter `…/en/abbildungen/` | `topic.js:75`, `pilot.js:190` |

Weitere Speicherschlüssel: Lernstand `wue-conduction-v04-draft-20260929-v1` (`app.js:9`), Farbskala `wue-conduction-colormap` (`pilot.js:57`).

## 10. Weiteres auf der Simulationsseite

| Punkt | Wert | Fundstelle |
|---|---|---|
| Statuszeile | `div.pilot-status[role=status][aria-live=polite]` unter den Knöpfen, ohne Fläche und ohne linke Linie; Texte z. B. „Bereit. Beim ersten Start wird Python aus dem Internet geladen.“, „Bereit. Python ist geladen.“, „Berechnet. Parameter ändern oder erneut berechnen.“, „Eingaben geändert. Berechnung starten.“, „Standardwerte wiederhergestellt.“ | Vorlage `pilot_0200`, `design.css:65`, `sprachen.js` |
| Fortschrittsanzeige | `<progress class="pilot-progress" max="100" aria-label="Fortschritt der Berechnung">` in der Statuszeile; Höhe `.35rem`, `margin-top:.3rem`, Grund `--soft`, Wert navy; ohne Zahl: wandernder Verlauf `loading-phase 1.4s linear infinite`. Phasen: „Python wird geladen …“, „Rechenpakete werden geladen …“, „Simulation wird berechnet …“, „Bild n von m wird erstellt …“; nach erfolgreicher Rechnung bleibt der Balken auf 100 stehen | `design.css:66` bis `74`, `pilot.js:301` bis `305`, `:481` |
| Platz für den Balken | gewollt: `[hidden]` nur unsichtbar mit reserviertem Platz (`design.css:68`); **wirksam aber `display:none`**, weil `audit.css:20` `[hidden]{display:none !important}` gewinnt (gemessen: Höhe 0) | |
| „Lokal gespeichert“ | `span.save-state#save-state[aria-live=polite]` in der Kopfleiste rechts, `.72rem`, `--muted`, bis 640 px ausgeblendet; zeigt kurz andere Meldungen (z. B. „Versuche zurückgesetzt.“) und springt nach **1200 ms** zurück; Fehler „Nicht gespeichert. Bitte Lernstand exportieren.“ plus Toast „Browserspeicher nicht verfügbar oder voll …“ | `index.html:91`, `app.js:212` bis `227`, `styles.css:255`, `:680` |
| Toast | `position:fixed`, rechts unten `1.25rem`, navy, weiß, `.82rem`, Ecken `10px`, `max-width:min(360px, calc(100vw - 2rem))` | `styles.css:627` bis `644` |
| Lauf-Vergleich | unter „Für Fortgeschrittene“: Kontrollkästchen „Vorigen Lauf zum Vergleich anzeigen“ (erst sichtbar, wenn es einen vorigen Lauf gibt; vorher Hinweis „Ab dem zweiten Lauf erscheint der vorige Lauf gestrichelt zum Vergleich.“), Zeile „Geändert: <Symbol>: alt → neu · …“ oder „Gegenüber dem vorigen Lauf hat sich nichts geändert.“, aufklappbar „Alle Parameter des vorigen Laufs“; nicht bei 2D (dort Farbskala „Gleichmäßig (Standard)“ / „Regenbogen“). Im Diagramm: voriger Lauf `color="#7b8288", linestyle="--", linewidth=1.7`, Legende „Voriger Lauf“ bzw. „Voriger Lauf (Endprofil), t = … s“, aktueller Lauf „Aktueller Lauf“ | `pilot.js:87` bis `158`, `drawing_language.py:258` bis `270`, `runde7-layout.css:121` bis `124` |
| Lesehinweis | Absatz `.pilot-reading-hint` direkt unter dem Bild (aus `readingHint` der Simulation), `.8rem`, `line-height:1.4` | `pilot.js:217` bis `219`, `runde11.css:109` |
| Animation (instationär) | Zeile unter dem Bild: „Abspielen“ (primär) / „Pause“, „Erneut abspielen“ (sekundär), Status „Pausiert“ / „Wiedergabe läuft“, Regler „Animationsbild“; ab 1200 px zwei Spalten `auto minmax(0,1fr)` | Vorlage `pilot_0200`, `runde11.css:67`, `pilot.css:243` bis `248` |
| Rechenbudget | `div.pilot-budget` mit Linie oben, `.8rem`, Text muted, überschritten `#862828`, Vorschlagsknöpfe ghost | `workspace.css:19` bis `25` |
| Simulationstitel und Kopfzeile | `h2` und Kennzeile im Simulationsreiter ausgeblendet, `h3`-Titel nur für Screenreader | `design.css:46`, `:268`, `runde11.css:12` |
| Entwurfsbanner | über der App: „Entwurfsfassung · Die Inhalte werden noch fachlich geprüft.“, `padding:.65rem 1rem` | `index.html:31`, `audit.css:14`, `design.css:39` |
| Diagramm-Fehler | `details.pilot-error` „Fehlerdetails“ mit `pre` `.8rem`, `max-height:12rem` | Vorlage `pilot_0200`, `pilot.css:20` |
| Ladezustand | während der Rechnung `aria-busy=true`, Ausgabe `opacity:.55` | `pilot.css:21`, `:223` |
| Notizen unter der Simulation | Fläche `--soft`, Linie oben `3px solid var(--cyan)`, Ecken 4px; Notizen und Downloads zweispaltig `minmax(0,2.35fr) minmax(14rem,1fr)`, bis 600 px einspaltig | `design.css:279` bis `283` |
| Fokus | alle Bedienelemente im Hauptbereich: `2px solid var(--blue)`, Abstand 2px (gemessen auch an Unterreitern und Wand/Rohr/Kugel) | `runde7-layout.css:54` bis `57` |
| Druck | eigene Regeln nur für Tabellen und Formeln | `runde10.css:8` bis `17`, `typeset.css:8` bis `10` |
| `hidden` | gilt überall hart (`display:none !important`) | `audit.css:20` |
