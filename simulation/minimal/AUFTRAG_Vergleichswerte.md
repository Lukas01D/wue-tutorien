# Auftrag: Alltagsvergleiche für kA und Wärmekapazität der Tasse (schlanke Kaffee-Simulation)

Startsatz der TL: „Arbeite an den Vergleichswerten nach simulation/minimal/AUFTRAG_Vergleichswerte.md.“

## Ziel

Auf der schlanken Seite (`simulation/minimal/Kaffee_Simulation_schlank.html`) steht neben den Reglern „$kA$ der Tasse“ und „Wärmekapazität der Tasse $C_\mathrm{T}$“ zum eingestellten Wert ein kurzer Alltagsvergleich, zum Beispiel „≈ Porzellantasse mit Deckel“ oder „≈ Thermoskanne“. Studierende sollen so ein Gefühl dafür bekommen, was ein Wert bedeutet. Jeder Vergleich muss belegt oder nachvollziehbar abgeschätzt sein.

## Rahmen

- Die TL (Lukas) entscheidet, du empfiehlst klar. Deutsch, einfach, kurze Tabellen, keine Gedankenstriche (– oder —).
- Rechenkern (`simulation/site/src/modell.js`, `simulation/modell/`) bleibt unverändert. Änderungen nur in `simulation/minimal/src/` (und Tests).
- Aufbau der schlanken Seite: `simulation/minimal/LIESMICH.md`. Bauen: `python3 simulation/minimal/bauen_minimal.py`, testen: `node simulation/tests/minimal_test.js`.
- Modell der Seite: Abkühlung $C\,\mathrm{d}\vartheta/\mathrm{d}t = -kA\,(\vartheta - \vartheta_u)$ mit $C = m_K c_{p,K} + C_\mathrm{T}$ (Tasse immer so warm wie der Inhalt, Deckel dicht, keine Verdunstung). Werte des Blatts: 200 ml Kaffee, $kA$ = 0,1994 W/K (vorläufig, aus 72 °C nach 10 min), $C_\mathrm{T}$ = 0 (Blatt), Porzellantasse im Experiment etwa 300 g.
- Nichts veröffentlichen, nichts nach `main` mergen. Arbeitszweig, Commit, Push, Pull Request; die TL merged.

## Schritt 1: Recherche (gründlich, mit Quellen)

Websuche über die Such- und Abrufwerkzeuge, nicht über die Shell. Jede Zahl mit Quelle (Titel, Link, Abrufdatum) oder als eigene Abschätzung mit Rechenweg kennzeichnen. Keine Zahl aus dem Gedächtnis ohne Beleg.

| Größe | Was gesucht ist |
|:--|:--|
| Wärmekapazität $C_\mathrm{T} = m\,c$ | spezifische Wärmekapazität von Kalk-Natron-Glas, Borosilikatglas, Porzellan, Steingut, Edelstahl, Pappe mit Beschichtung, Kunststoff (PP); typische Massen von Pappbecher, dünnem Trinkglas, doppelwandigem Glas, Porzellantasse, dickem Steingutbecher, Einmachglas (etwa 500 ml), Edelstahl-Thermobecher (Innenwand) |
| $kA$ in W/K | gemessene Abkühlkurven von Tassen mit und ohne Deckel, Coffee-to-go-Bechern, doppelwandigen Gläsern, Thermobechern und Thermoskannen (Fachartikel, Physikdidaktik, Normen, seriöse Tests); daraus $kA = C/t \cdot \ln[(\vartheta_0 - \vartheta_u)/(\vartheta - \vartheta_u)]$ mit der jeweiligen Füllung. Spur zum Prüfen: die Norm zu Isolierflaschen (DIN EN 12546-1) mit ihrer Prüfung der Wärmehaltung. Abschätzung zur Kontrolle: $kA \approx h\,A$ mit freier Konvektion und Strahlung (etwa 5 bis 12 W/(m²K)) und der Außenfläche einer Tasse |
| Grenzen | Wie stark hängen die Werte von Füllmenge, Deckel und Verdunstung ab? Offene Tassen kühlen vor allem durch Verdunstung, die das Modell nicht enthält: Vergleiche dann nur „mit Deckel“ oder ausdrücklich kennzeichnen. |

Ergebnis von Schritt 1: `simulation/minimal/QUELLEN_Vergleichswerte.md` mit einer Tabelle je Größe (Gegenstand, Wert oder Spanne, Quelle, Bemerkung) und den Rechenwegen; Rechnungen als kleines Python-Skript `simulation/minimal/vergleichswerte.py`, das die Tabellen erzeugt.

## Schritt 2: Bereiche festlegen

- Je Regler 4 bis 7 Bereiche mit einem kurzen, eindeutigen Vergleich (höchstens etwa 30 Zeichen), zum Beispiel für $C_\mathrm{T}$: 0 „Blatt: Tasse speichert nichts“, „≈ Pappbecher“, „≈ dünnes Glas“, „≈ Porzellantasse“, „≈ dicker Steingutbecher“.
- Prüfen, ob der Reglerbereich passt. Für $kA$ reicht 0,05 bis 0,8 W/K vermutlich nicht (Thermoskanne deutlich kleiner); dann einen neuen Bereich und eine logarithmische Skala vorschlagen und begründen.
- Vergleiche gelten für etwa 200 ml Inhalt; das kurz unter dem Regler oder im Vergleich selbst sagen, wenn nötig.
- Bereiche, Grenzen und Texte der TL als Tabelle mit Empfehlung vorlegen, **bevor** du baust (Haltepunkt).

## Schritt 3: Gestaltung und Umsetzung (nach Freigabe)

- Optik der Hauptseite beibehalten (`site/src/stil.css`); der Vergleich steht klein und leise neben oder unter dem Reglernamen und ändert sich beim Ziehen mit. Kein zusätzlicher Erklärtext.
- Barrierefrei: Vergleich auch im `aria-valuetext` des Reglers; Kontrast nach WCAG AA.
- Deutsch und Englisch (Texte in `minimal/src/texte_schlank_*.txt`).
- Tests in `simulation/tests/minimal_test.js` ergänzen (je Bereich ein Wert, Grenzen, Englisch, axe-core), Bildschirmfotos Laptop 1366 × 768 und Handy 390 × 844 ansehen.

## Abschluss

Kurzer Bericht an die TL: Tabelle der Bereiche mit Quellen, was unsicher bleibt, Bilder, Link zum Pull Request, was die TL noch tun muss.
