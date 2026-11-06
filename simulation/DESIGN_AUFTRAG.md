# Auftrag: freie Gestaltungsentwürfe für die Kaffee-Simulation

> Stand 06.11.2026, geschrieben im Projekt-Chat für die Tutoriumsleitung (TL, Lukas). Für eine **neue, unabhängige** Claude-Code-Sitzung. Deutsch, keine Gedankenstriche (– oder —), stattdessen Komma, Punkt, Doppelpunkt oder Klammern. Die TL entscheidet, du empfiehlst klar.

## Ziel

Für die fertig gebaute Simulation „Kaffee mit Milch“ entwirfst du **drei eigenständige, klar unterschiedliche Gestaltungsrichtungen**. Die TL wählt danach eine aus oder mischt. Die Gestaltung ist frei. Es gibt **keine Vorgabe**, wie ein anderes Angebot aussieht, und es soll bewusst keine geben.

## Damit du unvoreingenommen bleibst

Lies und öffne **nicht**:
- `simulation/VORBILD_LERNZENTRUM.md`;
- `simulation/vorbild/`;
- `simulation/bildschirmfotos/lernzentrum/`;
- `simulation/gutachten/G6_*` (Gestaltungsvergleich);
- `simulation/PROTOTYPEN.md`;
- das Repository `waermeuebertragung-lernzentrum` und seine Websites.

Abschnitte in `AUFTRAG_Simulation_Kaffee.md` und `KONZEPT.md`, die ein Vorbild für das Aussehen beschreiben, überspringst du. Den heutigen Stand der Seite siehst du dir erst **ganz am Ende** an (Schritt 6).

## Grundlage

- **Gebauter Stand:** Commit `da7deb1` auf dem Zweig `claude/simulation-tool-kaffee-4kcacl`. So holst du ihn:
  1. `git fetch origin claude/simulation-tool-kaffee-4kcacl`
  2. `git checkout da7deb1 -- simulation/site simulation/tests simulation/ZUSTAENDE.md simulation/KONZEPT.md`
  3. diese Dateien in deinem eigenen Zweig committen.
- **Aufbau der Seite:** Quellen in `simulation/site/src/` (Texte DE und EN, CSS, Rechenkern, Oberfläche), Bauskript `simulation/site/bauen.py`.
- **Was die Seite leisten muss:** `simulation/ZUSTAENDE.md` (Abläufe und Zustände) und aus `simulation/KONZEPT.md` die Abschnitte 2 (Lernziele), 3 (Ablauf in der Sitzung) und 6 (Fragen).
- **Wer sie nutzt:**
  - Studierende im dritten Semester Maschinenbau, zu zweit, meist am Handy im Hörsaal, etwa 10 Minuten im Pflichtweg, auch internationale Studierende (Deutsch und Englisch);
  - die Tutorin oder der Tutor zeigt sie am Beamer.
- **Fachlicher Kern:** Zwei Tassen Kaffee kühlen ab, die Milch kommt sofort oder später dazu. Studierende sagen erst voraus und prüfen dann. Es geht um Energiebilanz und Abkühlkurven. Das Diagramm ist das Herz der Seite.

## Feste Grenzen (gelten für jeden Entwurf)

- **Nur die Gestaltung ändert sich:** CSS, Anordnung, Typografie, Farben, Diagrammgestaltung, Bedienelemente, dezente Bewegung. Diese Dinge bleiben unverändert:
  - Rechenkern (Blöcke MODELL und ERWEITERUNG);
  - Texte, Fragen und Auflösungen;
  - Abläufe und Zustände;
  - Reihenfolge „erst vorhersagen, dann prüfen“.

  Kleine Änderungen am Markup sind erlaubt, wenn die Gestaltung sie braucht.
- **Technik:** eine Datei, offline, keine fremden Server, Schrift eingebettet (nur freie Lizenzen wie SIL OFL), unter 450 000 Bytes unkomprimiert.
- **Barrierefreiheit nach WCAG 2.2 AA:**
  - Kontrast, auch der Kurven;
  - sichtbarer Fokus, Tastaturbedienung;
  - Zielgrößen;
  - reduzierte Bewegung;
  - Farbe nie als einziges Merkmal: Kurven direkt beschriftet und zusätzlich durch die Linienart unterschieden.
- **Größen:**
  - Handy 390 × 844 und 360 × 640;
  - Laptop 1366 × 768;
  - Beamer 1280 × 720.

  Kein waagerechtes Scrollen. Das Diagramm bleibt am Handy lesbar (Schrift im Diagramm nicht unter 11 px).

## Vorgehen

1. **Kurze Gestaltungsanalyse:** Was muss die Seite auf einen Blick vermitteln? Was ist am Handy im Hörsaal schwierig? Höchstens eine Seite.
2. **Drei Richtungen**, deutlich verschieden in Haltung, Farbe, Schrift und Anordnung. Die Richtungen wählst du selbst. Je Richtung:
   - Name;
   - Idee in drei Sätzen;
   - Farbpalette mit Kontrastwerten;
   - Schriften;
   - die wichtigsten Entscheidungen (Diagramm, Startkarte, Regler, Reiter).

   Nutze, falls vorhanden, einen Skill für Gestaltung.
3. **Bauen:** jede Richtung als lauffähige Fassung der echten Seite in `simulation/design_entwuerfe/<name>/` (eigene CSS und, wo nötig, Markup; gebaut mit einer Kopie des Bauskripts zu einer Datei `index.html`).
4. **Prüfen:** Rechenkern-Tests und Browsertests aus `simulation/tests/` gegen jede Fassung laufen lassen, dazu axe-core. Was rein gestaltungsbedingt anders ist (zum Beispiel ein umbenannter Selektor), passt du im Test an und begründest es. Ergebnisse je Fassung festhalten.
5. **Bildschirmfotos** jeder Fassung in denselben Zuständen, jeweils bei 390 × 844 und 1366 × 768:
   - Startkarte;
   - nach der Vorhersage mit Diagramm;
   - Frage 1 mit Regler;
   - Vertiefung geöffnet;
   - englische Startkarte;
   - Beamer 1280 × 720 nach der Vorhersage.

   Ablage in `simulation/design_entwuerfe/<name>/bilder/`.
6. **Vergleich:** Erst jetzt den heutigen Stand (`da7deb1`) in denselben Zuständen fotografieren, als „Variante 0“. Dann eine Vergleichsseite `simulation/design_entwuerfe/VERGLEICH.html`: alle vier nebeneinander je Zustand, Bilder eingebettet, offline lesbar.
7. **Bericht** `simulation/DESIGN_ENTWUERFE.md`:
   - die drei Richtungen;
   - Testergebnisse;
   - Stärken und Schwächen je Entwurf (Handy, Beamer, Lesbarkeit des Diagramms, Barrierefreiheit);
   - deine klare Empfehlung;
   - Aufwand der Übertragung auf den korrigierten Stand.

## Regeln

- Arbeite auf dem eigenen Zweig dieser Sitzung. `claude/simulation-tool-kaffee-4kcacl` nicht verändern (dort läuft parallel eine Korrekturrunde), nicht mergen, nichts veröffentlichen, nichts an andere senden.
- Nach jedem Schritt committen und pushen.
- Am Ende anhalten und der TL in einer kurzen Tabelle nennen: Zweigname, die drei Entwürfe mit je einem Satz, Empfehlung, Pfad der Vergleichsseite.
