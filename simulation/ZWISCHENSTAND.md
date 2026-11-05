# Zwischenstand des Baus (Pause auf Wunsch der TL, 05.11.2026)

> Die TL hat wegen ihres Nutzungslimits um eine geordnete Pause gebeten. Gearbeitet wurde nach `simulation/BAU_AUFTRAG.md` (Stand 6526feb). Diese Datei sagt, was fertig ist, was offen ist und wie es nach Teil 4 weitergeht. Zweig: `claude/simulation-tool-kaffee-4kcacl`.

## 1 Geprüfter Stand der Seite

- `simulation/site/index.html` und bytegleich `simulation/site/Kaffee_Simulation.html`: **369 081 Bytes, SHA-256 `f519052cadf6745eeeb4eb97f5a0042c74688f3495cada09c059970b25016707`** (Grenze 450 000 Bytes). Diesen Stand haben alle Rollen G1 bis G8 geprüft; seit dem Start der Rollenprüfungen wurde die Seite **nicht** mehr verändert.
- Neu bauen: `python3 simulation/site/bauen.py` (prüfen ohne Schreiben: `--pruefen`).

## 2 Was fertig ist

| Teil | Stand | Belege |
|:--|:--|:--|
| 0 Voraussetzungen | fertig | `simulation/BAU_BERICHT.md` (Umgebung, Quellprüfsummen; WebKit und Bildschirmleser nicht verfügbar, Live-Lernzentrum 401) |
| 1 Vorbild und Zustände | fertig | `simulation/VORBILD_LERNZENTRUM.md`, `simulation/ZUSTAENDE.md`, `simulation/vorbild/`, `simulation/bildschirmfotos/lernzentrum/` |
| 2 Rechenkern, Tests, Zahlen in Texten | fertig | `simulation/site/src/modell.js` (Block MODELL unverändert), `erweiterung.js`, Python-Referenz `simulation/modell/kaffee_erweitert.py`; `simulation/tests/test_kern.py` 135 von 135 (auch gegen die gebaute Seite, `test_kern_html_ergebnis.txt`); `simulation/tests/test_texte.py` 14 von 14; Zahlen der Texte aus `simulation/site/zahlen.py` |
| 3 Oberfläche | gebaut, Rollenprüfung Runde 1 läuft | Quellen `simulation/site/src/`, Bauskript `bauen.py`, Formelumsetzer `tex2mathml.py`, Schriftteilmengen `src/schriften/`; Browsertests `simulation/tests/browsertest_bau.js` 75 von 75 auf dem geprüften Stand (Chromium; `browsertest_bau_ergebnis.txt`); Prototypen und Wahl `simulation/PROTOTYPEN.md` (Energiesäulen B, Vertiefung am Handy A); Bilder der Abdeckungsmatrix `simulation/bildschirmfotos/bau/` (54); Kann-Punkte Trinkzeit, Becher kalt, CSV gebaut und getestet; feste Wärmestrom-Pfeile = Bilanzraum S-5; mitlaufende Pfeile (K-1), QR-Code (K-2), V6 (K-6), überlineare Kurve (K-7), Druckansicht (K-8) nicht gebaut; `simulation/ABNAHME_IPHONE.md` |
| 5 Begleitmaterial | fertig (vor den Korrekturen aus Teil 4) | `simulation/EINSATZ_TUTORIUM.md`; Kurzkarten `simulation/kurzkarte/Kurzkarte_DE.pdf` und `Kurzkarte_EN.pdf` (je eine A4-Seite, Text auswählbar, gerendert geprüft, QR-Platzhalter), Erzeuger `kurzkarte.js` |
| 7 Übergabe an Codex | Entwurf | `simulation/X5_AUFTRAG.md` mit Platzhaltern `{{BAUCOMMIT}}`, `{{SHA}}`, `{{BYTES}}`; Abschnitt in `AGENTS.md` **noch nicht** geschrieben |
| 6 Baubericht | **offen** | `simulation/BAU_BERICHT.md` enthält bisher nur Teil 0 |

## 3 Rollenprüfungen (Teil 4, Runde 1)

Getrennte Rollenprüfungen desselben Modells, alle auf dem Stand aus Abschnitt 1.

| Rolle | Datei | Stand |
|:--|:--|:--|
| G1 Studentin (Handy, Deutsch) | `simulation/gutachten/G1_Studentin.md` | **vollständig**: 19 Befunde (1 blocker, 1 high, 8 medium, 9 low) |
| G2 Internationaler Student | `simulation/gutachten/G2_International.md` | **unvollständig**, Zwischenbericht (Durchlauf auf Englisch fast fertig): 20 Befunde (1 blocker, 2 high, 8 medium, 9 low); offen: nur Tastatur, Bildschirmtastatur, 768 und 1024 px, Kurslink mit Becher 3 oder Deckel, gesperrter Speicher |
| G3 Fachgutachter | `simulation/gutachten/G3_Fachgutachter.md` | **unvollständig**, Zwischenbericht: 30 von 30 Zuständen stimmen in allen angezeigten Zahlen mit der unabhängigen Rechnung überein, Auflösungen DE und EN richtig; 13 Befunde (0 blocker, 1 high, 3 medium, 9 low); offen: Becher 3 und Deckel im Messblatt, Kurslink, CSV, Wertetabelle, Vergleichslauf, englische Texte außer Auflösungen |
| G4 Lernpsychologie | `simulation/gutachten/G4_Lernpsychologie.md` | **vollständig**: 24 Befunde (1 blocker, 1 high, 14 medium, 8 low) |
| G5 Barrierefreiheit | `simulation/gutachten/G5_Barrierefreiheit.md` | **unvollständig**, Zwischenbericht mit Prüfliste WCAG 2.2 A/AA: axe-core in 48 Läufen ohne Verstoß; 22 Befunde aus der Prüfung von Hand (1 blocker, 4 high, 10 medium, 7 low); offen: echter Bildschirmleser, echte Geräte, Firefox und Safari, ln-Achse, V1 bis V5 einzeln, Frage 2 mit Kurslink, Kontrastmodus |
| G6 Gestaltung | `simulation/gutachten/G6_Gestaltung.md` | **unvollständig**, Zwischenbericht: 17 Befunde (0 blocker, 3 high, 4 medium, 10 low); Vergleich mit dem Lernzentrum nach „Berechnen“ nicht möglich (Pyodide offline blockiert); offene Prüfungen im Bericht |
| G7 Tutorin | `simulation/gutachten/G7_Tutorin.md` | **vollständig**: 15 Befunde (1 blocker, 3 high, 8 medium, 3 low) |
| G8 Technik | `simulation/gutachten/G8_Technik.md` | **unvollständig**, Zwischenbericht: 25 Angriffe und Prüfungen, 16 Befunde (0 blocker, 2 high, 5 medium, 9 low); ohne Befund: keine HTML-Einschleusung, keine fremden Anfragen, keine CSP-Verletzung, gesperrter Speicher, Dauerlauf 36 s, M-5 auch mit gedrosselter CPU |

Welche Zwischenberichte tatsächlich geschrieben wurden, zeigt Abschnitt 6 (wird beim letzten Commit nachgetragen).

**Wichtigste Befunde aus den vollständigen Gutachten (noch nicht zusammengeführt, noch nichts behoben):**

| Schwere | Befund | Rollen |
|:--|:--|:--|
| blocker | Frage 2: Sobald Kurswerte geladen sind, zeigt das Diagramm die Messpunkte schon vor der Vorhersage zu Frage 2 (auch während Frage 1); „über, unter, auf den Kurven“ ist dann ablesbar | G1-01, G4-01, G7-01 |
| high | Handy (M-6): Frage und Vorhersage stehen über dem angehefteten Diagramm; Frage, Vorhersage und Diagramm nie zugleich sichtbar; Anheften nicht abschaltbar | G1-02, G4-10 |
| high | Zwei offene Tabs überschreiben sich den Speicher (Vorhersage zu Frage 2 und Kurswerte gehen verloren) | G7-02, G8-01 |
| high | Beamer 1280 × 720 und 1366 × 768: Frage, Diagramm und Regler nie zugleich im Bild (M-6) | G7-03 |
| high | Hinweis „Werte werden nicht gespeichert“ am Handy ausgeblendet | G7-04 |
| blocker | Achsenbeschriftung rundet Teilstriche im Abstand 2,5 auf ganze Zahlen (2,5 wird „3“), Zeitachse in Frage 1 bei Zugabe um 11 bis 14 min und Wärmestrom-Ansicht | G2-01, G5-01 |
| high | Englische CSV: Komma im Spaltenkopf „model cup 2, black until the milk“ zerbricht die Spalten | G2-02 |
| high | Dezimalkomma im Englischen: getippte „2,5“ erscheint als „about 2,5 K“ (M-19) | G2-03 |
| high (INFERRED) | nur drei Reiter, erster heißt „Versuche“ statt „Auflösungen“ (M-18, E6); nach Bauauftrag und Lernzentrum K5 so gebaut, Frage an die TL | G3-13 |
| medium | Start-Auflösung „Tasse 2 war bis zur Zugabe heißer“ stimmt nur bis 55,7 min (Wortlaut aus Konzept 6.1, Lösung sagt „bis etwa 56 min“): Frage an die TL | G3-02 |
| medium | „Becher beim Eingießen kalt“ ändert Kurven, Rechenwerte und Energie nicht, nur eine Zusatzzeile | G3-03 |
| high | Angeheftetes Diagramm verdeckt am Handy den Tastaturfokus (WCAG 2.4.11, M-6), `scroll-padding-top` fehlt | G6-02, G5-02 |
| high | Fokus am Sprachknopf im dunklen Kopf nicht sichtbar (Kontrast 1,25:1, WCAG 2.4.7) | G5-03 |
| high | Vergleichslauf mit 1,5 bis 1,8:1 Kontrast und ohne Textfassung | G5-05 |
| high | Beschriftungen im Diagramm überlappen in Einzelfällen (EN „intersection“ auf den Kurven, Zugabe 5 min unter dem Vorhersagekasten, Raumlinie bei 120 min) (M-11) | G6-03 |
| high | `aria-valuetext` fehlt an allen 8 Reglern (M-12; deckt sich mit dem eigenen Befund) | G8-02, G5-04 |
| medium | Manipulierte Werte im Speicher legen die Seite ohne Ausweg lahm (7 von 24 Fällen); erster Klick nach Messblatt-Eingabe geht verloren; Messblatt nimmt Werte an, die die Übernahme mit falscher Begründung ablehnt; Link endet auf Komma | G8-03 bis G8-07 |
| medium | „Kurven zeigen“ scrollt die Kurven nicht ins Bild; Laptop: Frage, Diagramm und Regler nie zugleich (deckt sich mit G7-03); Energiesäulen ab 768 px nur 8 bis 8,8 px Schrift; Aufklappbereichen fehlt das ▶ | G6-04 bis G6-07 |
| medium (Auswahl) | Einheit im Zahlenfeld („3 K“) sperrt den Knopf mit falschem Hinweis (G1, G2); *kA* heißt im Englischen „heat loss“ statt „heat loss coefficient“; deutsche Indizes (ab, misch, mess) im Englischen nicht erklärt; Ausgangslage-Meldung bleibt nach DE → EN deutsch; Säulentitel „Energie bis zur Zugabe“ ohne „abgegeben“; Fehlvorstellung „Energie bleibt erhalten“ nur indirekt angegangen; „passt“ bewertet nur die Richtung; Eingaben wie „4 K“ sperren den Knopf mit irreführendem Hinweis; Prüfen in Frage 2 grau ohne Erklärung; Hinweise auf Frage 1 schon vor ihrer Vorhersage (Schnitt in Rechenwerten); Vorhersage-Marke zeigt immer die Startvorhersage; Ausgangslage V3 falsch benannt; Kurslink im offenen Tab ohne Wirkung; Schrift am Beamer zu klein; Messpunkte bei 60 min übereinander; Messblatt erst nach dem Aufdecken | G1, G4, G7 |

**Eigene Befunde des Baus** (vor der Zusammenführung notiert): `aria-valuetext` an den Schiebereglern fehlt (M-12); Anheften nicht abschaltbar (M-6, deckt sich mit G1-02); Lesehilfe ist ein Satz und nicht wegklickbar (S-7, Abweichung zu begründen); drei Reiter statt neun (M-18, nach Bauauftrag und Lernzentrum K5, als Abweichung zu dokumentieren); Name des ersten Reiters „Versuche“ (Bauauftrag, Lernzentrum) gegen E6 „Auflösungen“ (offene Frage an die TL mit Empfehlung „Versuche“).

**Fachliche Fragen an die TL, die sich schon abzeichnen:** (1) Blatt vom 31.10. sieht den Versuch bis 40 min und *kA* ohne Becher vor, die Seite folgt E8 (60 min, Übernahme mit Becher); Blatt, Versuch und Messblatt sollten denselben Ablauf haben (G1, G4, G7). (2) Reitername „Versuche“ gegen E6. (3) Soll der Schnittpunkt in Rechenwerten und Diagramm bis zur Vorhersage zu Frage 1 verborgen bleiben (G1, G4; das Konzept sieht das nicht vor)? (4) Vorabmessung der TL (S-9, Beispielmessung) fehlt noch.

## 4 Was beim Pausieren nicht committet war

Nichts Wesentliches: Alle Arbeitsstände bis zur Pause waren committet und gepusht, zuletzt die Gutachten G1, G4, G7 und der Zwischenstand von G3. Mit diesem Commit kommen dazu: diese Datei und die Zwischenberichte der abgebrochenen Rollen, soweit sie geschrieben wurden. Bewusst **nicht** im Repository: Prüfskripte und Bilder der Rollen im Scratchpad der Sitzung (`/tmp/claude-0/…/scratchpad/gutachten_G<Nr>/`); sie gehen mit der Sitzung verloren. Die Gutachten nennen diese Pfade nur als Beleg.

Hinweis: Die Prüfung „Übernahme ohne Wert bei 10 min“ in `browsertest_bau.js` wurde nach dem letzten Testlauf geschärft und ist auf dem geprüften Stand noch nicht gelaufen.

## 5 Nächste Schritte (nach Teil 4 des Bauauftrags)

1. **Runde 1 vervollständigen.** `git pull origin claude/simulation-tool-kaffee-4kcacl`. Die unvollständigen Rollen (siehe Abschnitt 6) in frischen Kontexten neu starten, mit dem Auftrag aus `BAU_AUFTRAG.md` 4.2 und diesen Regeln: Pfad der Seite, `KONZEPT.md`, eigener Blickwinkel; fertige Aufgabe `ergebnisse/kaffee/fertig/Kaffee_Aufgabe_Tutorium5_2026-10-31.pdf` und Lösung (nicht die ältere Fassung im Prüfpaket); nicht lesen: `BAU_BERICHT.md`, `PROTOTYPEN.md`, `ZUSTAENDE.md` (G1 bis G7), `simulation/tests/`, `simulation/bildschirmfotos/bau/`, andere Gutachten, Git-Protokoll; Format `| ID | Schwere | Befund | Beleg | Vorschlag | CONFIRMED/INFERRED |`, Schweregrade aus `BAU_AUFTRAG.md` 4.1; Bezeichnung „getrennte Rollenprüfung desselben Modells“. Den vorhandenen Zwischenbericht einer Rolle darf die neue Rolle als Ausgangspunkt lesen, damit nichts doppelt läuft. Die Seite bis dahin **nicht** ändern (sonst prüfen die Rollen einen anderen Stand).
2. **`simulation/gutachten/ZUSAMMENFUEHRUNG.md`** schreiben: jeder Befund aller acht Gutachten als `| ID | übernehmen / ablehnen / offen | Begründung mit Beleg | Folge |`; jede Zahl der Rollen nachrechnen; gleiche Befunde mehrerer Rollen zusammenfassen; die eigenen Befunde aus Abschnitt 3 mit aufnehmen.
3. **Beheben** (blocker, high, medium; low nach Sinn), voraussichtlich zuerst:
   - Messpunkte und Ansicht „ln“ erst nach der festgehaltenen Vorhersage zu Frage 2 zeigen (oder Festhalten vor dem Laden erlauben); Browsertest dafür.
   - Handy-Reihenfolge nach M-6 (Diagramm angeheftet, Frage direkt darunter, Frageleiste nach dem Festhalten kompakt), Schalter „Diagramm lösen/anheften“.
   - Speicher zwischen Tabs abgleichen (`storage`-Ereignis) oder Schreiben nur geänderter Teile; Kurslink auch im offenen Tab (`hashchange`).
   - Beamer: Diagrammhöhe an die Fensterhöhe koppeln, Regler „Zugabe nach“ direkt unter das Diagramm, Schrift für Projektion prüfen.
   - Speicherhinweis am Handy sichtbar; `aria-valuetext` an allen Schiebereglern.
   - Texte: Säulentitel „An den Raum abgegebene Wärme bis zur Zugabe“ (Wortlaut ist eine fachliche Formulierung: als Vorschlag an die TL, wenn er Konzepttexte ändert), Hinweis neben grauem Prüfknopf in Frage 2, Zahlfeld akzeptiert „4 K“ oder erklärt den Fehler.
   - Fachliche Inhalte (Fragen, Auflösungen, Lernziele) **nicht** eigenständig ändern; als offene Frage mit Empfehlung an die TL.
4. **Prüfen:** `python3 simulation/site/bauen.py`, dann
   - `python3 simulation/tests/test_texte.py`
   - `python3 simulation/tests/test_kern.py --html simulation/site/index.html`
   - `node simulation/tests/browsertest_bau.js`
   - `node simulation/tests/bilder_bau.js` (Bilder neu)
   - `node simulation/prototypen/prototypen.js` nur bei Bedarf (siehe Hinweis in `PROTOTYPEN.md`).
   Jede Korrektur gezielt prüfen und die betroffenen Regressionstests wiederholen.
5. **Runde 2** (höchstens drei Runden insgesamt): betroffene Rollen und eine neue Studentin, die die Seite nicht kennt. Nach Runde 3 endet die Bearbeitung.
6. **Teil 6:** `simulation/BAU_BERICHT.md` vervollständigen (Nachweistabelle M, S, K, F2-1 bis F2-17, K1 bis K11, E1 bis E8 mit Status bestanden / fehlgeschlagen / nicht geprüft / nicht anwendbar; Abweichungen; Übernahmen aus dem Lernzentrum; Testbefehle und Ergebnisse; Bilanz der Rollenprüfungen; offene Real-World-Nachweise iPhone, Studierende, Hörsaal, Bildschirmleser; Status „abnahmebereit“ oder „unvollständige Übergabe“; Fragen an die TL) und `simulation/PROTOKOLL_NOTIZEN.md` ergänzen.
7. **Teil 5 nachziehen**, falls Korrekturen Texte, Ablauf oder Zahlen ändern (`EINSATZ_TUTORIUM.md`, Kurzkarten neu erzeugen mit `node simulation/kurzkarte/kurzkarte.js`).
8. **Teil 7:** Platzhalter in `simulation/X5_AUFTRAG.md` füllen (letzter Commit, der `simulation/site` ändert; SHA-256 und Größe aus `simulation/site/BAUNACHWEIS.txt`), in `AGENTS.md` nur den kurzen, gekennzeichneten Abschnitt „Sechster Auftrag: Abnahme des Baus (Rolle X5)“ mit dem Startsatz „Nimm den Bau der Simulation ab nach simulation/X5_AUFTRAG.md (Rolle X5).“ und Verweis auf die Datei. Letzter Push, dann der TL die kurze Tabelle (was steht, Status, was die TL tun muss, Startsatz für Codex mit `git fetch origin claude/simulation-tool-kaffee-4kcacl` und `git checkout claude/simulation-tool-kaffee-4kcacl`). Nicht veröffentlichen, kein Pull Request.

## 6 Zwischenberichte beim Pausieren

Alle acht Gutachten liegen im Repository. Vollständig: G1, G4, G7. Als Zwischenstand (oben gekennzeichnet „Zwischenstand, nicht abgeschlossen“, mit Liste des noch nicht Geprüften): G2, G3, G5, G6, G8. Alle Rollen haben denselben Stand der Seite geprüft (SHA-256 `f519052c…6707`) und nur ihr Gutachten geändert; keine Rolle hat committet. Für Schritt 1 in Abschnitt 5 heißt das: G2, G3, G5, G6 und G8 vervollständigen (jeweils nur die offenen Punkte ihrer Liste), G1, G4, G7 nicht wiederholen.

Summe Runde 1 (vorläufig, noch nicht zusammengeführt, Doppelungen nicht abgezogen): 146 Befunde (aus den Befundtabellen gezählt), davon 5 blocker (zwei Sachverhalte: Messpunkte vor der Vorhersage zu Frage 2; Achsenbeschriftung bei Schrittweite 2,5), 17 high, 60 medium, 64 low. Keine Rolle hat eine falsche Modellzahl gefunden (G3: 30 von 30 Zuständen gleich).
