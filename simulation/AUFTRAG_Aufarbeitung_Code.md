# Auftrag: Aufarbeitung des Codes der Kaffee-Simulation

Startsatz der TL: „Arbeite an der Aufarbeitung des Simulationscodes nach simulation/AUFTRAG_Aufarbeitung_Code.md.“

## Ziel

Die TL (Lukas) will sich selbst und anderen zeigen, **wie der Code der Kaffee-Simulation aussieht, wie er funktioniert, ob er valide ist und wie er gebaut wurde.** Publikum: die TL selbst (lernt Code und mag kurze Erklärungen zu einzelnen Stellen), Tutorinnen und Tutoren, der Lehrstuhl FVT und Fachleute aus der Hochschuldidaktik. Ergebnis sind eine Präsentation und ein Bericht zum Nachlesen, beide belegt bis auf Datei, Zeile und Commit.

## Rahmen

- Die TL entscheidet, du empfiehlst klar. Deutsch, einfach, kurze Tabellen, keine Gedankenstriche (– oder —), stattdessen Komma, Punkt, Doppelpunkt oder Klammern. Ein Satz, ein Gedanke.
- **Nur lesen und prüfen, nichts am Code ändern.** Prüfskripte und Ergebnisse kommen in den neuen Ordner `simulation/aufarbeitung/`. Fehler, die du findest, meldest du als Befund mit Vorschlag; behoben wird erst nach Freigabe der TL in einem eigenen Pull Request.
- Jede Aussage mit Beleg (Datei und Zeile, Commit, Pull Request, Testausgabe) und mit CONFIRMED (selbst geprüft) oder INFERRED (geschlossen, nicht geprüft). Zahlen nur aus eigener Rechnung oder aus Testausgaben dieser Sitzung.
- Befunde im Format `| ID | Schwere (blocker/high/medium/low) | Befund | Beleg | Vorschlag | CONFIRMED/INFERRED |`.
- Nichts veröffentlichen, nichts nach `main` mergen, nichts an andere senden. Arbeitszweig, Commit, Push, Pull Request; die TL merged. Keine E-Mail-Adressen oder Zugangsdaten in Dateien.
- Lernzentrum und Tutorien sind getrennte Stränge: nur dieses Repository (`wue-tutorien`), Ordner `simulation/`.

## Was es gibt (Stand 12.11.2026, vor Beginn mit `git log` und `ls` bestätigen)

| Teil | Dateien | Rolle |
|:--|:--|:--|
| Modell des Blatts (Python) | `modell/kaffee_modell.py`, `modell/werte.py`, `modell/HERKUNFT.md` | Rechnung der Aufgabe; Quelle aller Zahlen |
| Rechenkern im Browser | `site/src/modell.js` (Block MODELL, STANDARD, ZEITEN, BEISPIEL) | gleiche Rechnung in JavaScript |
| Hauptseite (bis Version 3 online) | `site/src/oberflaeche.js`, `stil.css`, `texte_de.txt`, `texte_en.txt`, `vorlage.html`, `site/bauen.py`, `site/zahlen.py`, `site/tex2mathml.py`, `site/schriften_teilen.py` | Oberfläche mit Fragen und Aufträgen; Bau zu einer HTML-Datei |
| Schlanke Seite (seit Version 4 online) | `minimal/src/schlank.js`, `schlank.css`, `vorlage.html`, `texte_schlank_*.txt`, `minimal/bauen_minimal.py` | übernimmt beim Bau Stil, Texte und Bausteine der Hauptseite; eigene Rechnung mit Zeit bis 180 min, Kaffeemenge, Tassenwärmer, Wärmekapazität der Tasse |
| Vergleichswerte | `minimal/vergleichswerte.py`, `minimal/QUELLEN_Vergleichswerte.md` | Alltagsvergleiche für kA und Wärmekapazität, 13 Quellen |
| Tests | `tests/test_kern.py`, `tests/test_texte.py`, `tests/browsertest.js`, `tests/minimal_test.js`, `tests/bilder.js` | Rechenkern, Texte, Browser mit axe-core, Bildschirmfotos |
| Entstehung und Prüfung | `KONZEPT*.md`, `AUFTRAG_Simulation_Kaffee.md`, `ENTSCHEIDUNGEN_F3.md`, `X4` bis `X6` (Aufträge und Prüfungen durch Codex), `AENDERUNG_*.md`, `LIVE_ABNAHME.md`, `VEROEFFENTLICHUNG.md`, `VEROEFFENTLICHUNG_NACHWEIS.md`, Pull Requests auf GitHub | wer was wann entschieden, gebaut und geprüft hat |

## Schritt 1: Bestandsaufnahme

- Karte des Codes: Dateien, Zeilen, Sprachen, Abhängigkeiten (was ruft was auf, was übernimmt der Bau von wo). Kennzahlen mit `wc -l` und `git log`.
- Bauweg von der Quelle bis zur veröffentlichten Datei: Eingaben, Schritte, Ausgabe, Prüfsumme. Prüfen, ob die veröffentlichte Fassung (Fuß „Stand … · Version …“) zur Datei auf `main` passt.

## Schritt 2: Wie funktioniert er?

- **Physik zu Code:** Jede Gleichung des Blatts (Mischtemperatur, Abkühlung $C\,\mathrm{d}\vartheta/\mathrm{d}t = -kA(\vartheta - \vartheta_u)$, Lösung mit $e^{-t/\tau}$, abgegebene Wärme, $Q_2 - Q_1 = C_G(\vartheta_1 - \vartheta_2)$, Tassenwärmer, Wärmekapazität der Tasse) einer Funktion und Zeile zuordnen, in Python und in JavaScript. Bezug zur Vorlesung in der Form „Vorlesung XX, Folie XX“, wo es passt.
- **Datenfluss:** vom Regler bis zum Pixel (Eingabe, Zustand, Rechnung, Diagramm, Kasten, Säulen, Bildbeschreibung), einmal für die schlanke Seite ausführlich, für die Hauptseite kurz.
- **Bau:** wie aus mehreren Quelldateien eine einzige HTML-Datei wird (Schriften eingebettet, Formeln als MathML, Inhaltssicherheitsrichtlinie mit Prüfsummen, Bausteine aus `oberflaeche.js`), warum deterministisch.
- Zu 5 bis 8 Code-Stellen je einen kurzen Erklärkasten (2 bis 3 Minuten Lesezeit) für die TL: Ausschnitt, was er tut, warum so, was man daraus lernen kann.

## Schritt 3: Ist er valide?

Prüfe unabhängig vom vorhandenen Code und halte jede Prüfung als Skript in `simulation/aufarbeitung/` fest:

| Prüfung | Wie |
|:--|:--|
| Unabhängige Nachrechnung | eigenes kleines Skript nur aus den Formeln des Blatts (ohne `kaffee_modell.py` zu importieren); Werte des Blatts (43,01 °C, 36,31 °C, 6,69 K, 15,50 kJ, 23,82 kJ) und einige andere Punkte |
| Python gegen JavaScript | `modell.js` und `schlank.js` mit Node über ein Raster von Eingaben (alle Regler, auch Grenzen) gegen das Python-Modell; größte Abweichung angeben |
| Physikalische Proben | Energiebilanz bei jeder Einstellung; $C_\mathrm{T} = 0$ und $t = t_\mathrm{Z}$ ergibt die Hauptseite; Milch so warm wie der Kaffee ergibt keinen Sprung; großes kA kühlt schneller; Tassenwärmer: Grenzwert $\vartheta_u + \dot Q_\mathrm{W}/kA \le$ 95 °C; Monotonie und keine Werte über 100 °C |
| Vorhandene Tests | alle ausführen; je Testdatei sagen, was sie prüft und was nicht (Lücken als Befund) |
| Bau und Veröffentlichung | Bau zweimal, gleiche Bytes; Datei auf `main` gleich der veröffentlichten (Nachweise lesen; den Abruf im Browser der TL nur mit ihrer Zustimmung) |
| Barrierefreiheit und Sicherheit | axe-core, Kontraste, Tastatur; keine Netzanfragen, kein Speicher, Inhaltssicherheitsrichtlinie |
| Grenzen | was das Modell nicht kann (Verdunstung, Wärmekapazität im Blatt null, kA konstant, vorläufige Werte bis zur Messung im Januar) und wo die Seite das zeigt oder nicht |

Am Ende ein klares Urteil in drei Stufen (valide für den Zweck, valide mit Einschränkungen, nicht valide), mit Begründung. Wenn die TL es möchte: einen kurzen Auftrag für eine Gegenprüfung durch Codex vorbereiten (nur den Text, nicht senden).

## Schritt 4: Wie wurde er gebaut?

- Zeitleiste aus Commits, Pull Requests (`gh api repos/Lukas01D/wue-tutorien/pulls?state=all`) und den Dokumenten: Konzept, Prototypen, Fassung 3, schlanke Seite, Versionen 1 bis 5.
- Rollen: TL entscheidet und gibt frei, Claude baut, Codex prüft und veröffentlicht. Wo hat eine Prüfung etwas gefunden, und was wurde daraufhin geändert?
- Kennzahlen: Commits, Pull Requests, Zahl der Tests, Prüfrunden, Dauer.
- Was lief gut, was würde man wieder so machen, was nicht (zum Beispiel: Pull Request gemergt, bevor alle Commits drin waren).

## Haltepunkt

Bevor du Präsentation und Bericht baust: der TL eine Gliederung (Folienliste) und die Befunde aus Schritt 3 vorlegen, mit Empfehlung. Erst nach ihrer Rückmeldung weiter.

## Schritt 5: Ergebnisse

| Ergebnis | Form |
|:--|:--|
| Präsentation | Folien (Artefakttyp Slides, falls verfügbar), 12 bis 18 Folien: Frage, Überblick, Architektur (Bild), Physik zu Code, Datenfluss, Bau, Validität (Tabelle der Prüfungen mit Ergebnis), Grenzen, Entstehung (Zeitleiste), Rollen von Mensch und KI, Lehren, Ausblick. Kurze Codeausschnitte, große Schrift, wenig Text. |
| Bericht | Dokument (Artefakttyp Docs, falls verfügbar) mit allen Belegen und den Erklärkästen; Anhang mit Befunden |
| Prüfskripte | `simulation/aufarbeitung/` mit LIESMICH (wie ausführen, Ergebnisse vom Datum) |

Bilder (Architektur, Datenfluss, Zeitleiste) selbst zeichnen, schlicht und lesbar am Beamer.

## Abschluss

Kurzer Bericht an die TL: was steht, Urteil zur Validität in einem Satz, Befunde mit Empfehlung, Links zu Präsentation, Bericht und Pull Request, Tabelle „was die TL noch tun muss“.
