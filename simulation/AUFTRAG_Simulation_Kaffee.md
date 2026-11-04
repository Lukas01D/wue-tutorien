# Auftrag: Simulation „Kaffee mit Milch“ als eigene Website

> Stand 04.11.2026, geschrieben im Projekt-Chat für die Tutoriumsleitung (TL, Lukas). Gilt für Claude (Cloud-Sitzung von Claude Code) und Codex. Deutsch, keine Gedankenstriche (– oder —), stattdessen Komma, Punkt, Doppelpunkt oder Klammern. Die TL entscheidet, ihr empfehlt klar.

## Ziel

Das Simulationstool der Kaffee-Aufgabe (Tutorium 5, dritte Ebene der Sitzung nach Versuch und Rechnung, D110) wird zu einer **eigenen, gut gestalteten Website mit festem Link**, so wie die Seiten des Lernzentrums. Es wird **fundiert ausgearbeitet und erweitert**: begründet mit Literatur zum Lernen mit Simulationen, zu Gestaltung und Bedienbarkeit und zur Fachdidaktik. Ergebnis für die TL: ein Link (und die Seite zusätzlich als Datei, die offline läuft).

## Ausgangslage

- **Werkzeug heute:** eine HTML-Datei, offline, Deutsch. Neueste Fassung auf dem Zweig `claude/kaffee-pruefung-sgvo1r`: `ergebnisse/kaffee/fertig/Kaffee_Simulation.html` (vier Fragen mit „Sagen Sie erst zu zweit voraus …“, ICAP). Auf `main` liegt die Fassung vom 31.10.2026 in `ergebnisse/kaffee/simulation/` mit Tests (`test_simulation.py`, `browsertest.js`).
- **Modell:** `kaffee_modell.py` (im Arbeitsordner der Kaffee-Aufgabe unter `pruefung/Kaffee_Pruefpaket_2026-10-23/umsetzung/Arbeitsordner/kaffee/`). Jede Zahl kommt aus diesem Modell oder einer begründeten, getesteten Erweiterung.
- **Geprüft:** Codex X3 (9338 Kurvenwerte, Bedienung, Fragen), Befunde behoben (`ergebnisse/kaffee/X3_CODEX_SIMULATION.md`).
- **Lernzentrum als Vorbild für Aussehen und Ablauf:** Die Simulationsseiten des Lernzentrums (öffentlich: <https://waermeuebertragung-werkstatt.qarri196.chatgpt.site>) haben seit Runde 11 diesen Aufbau: Simulation oben, Bild bis 780 px, Knöpfe rechts daneben, Regler darunter in drei Spalten, Kasten „Rechenwerte“ rechts neben den Reglern; am Handy bleibt das Bild oben. Erklärtexte in einer Reiterleiste unter der Simulation: Probier aus · Ergebnisse lesen · Versuche · Parameter · Physikalisches Problem · Annahmen · Was die Simulation macht · Modell im Detail · So rechnet der Code. Veröffentlicht werden diese Seiten von Codex über „Sites“ (Adressen `*.qarri196.chatgpt.site`), mit Baunachweis und Live-Abnahme durch Claude.
- **Erfahrungen aus diesem Projekt:** Die Kaffee-Sitzung hat drei Ebenen (Versuch, Rechnung, Simulation). Die TL plant den Versuch neu (eigene Becher, eventuell mit Deckel, Messung alle 10 Minuten, Graph); ihre Vorabmessung zu Hause soll Grundlage werden. Modellrechnung dazu: Der größte Unterschied der Tassen ist bei jedem kA rund 3,9 K und tritt ein, wenn der schwarze Kaffee etwa 35 °C erreicht; Dämmung verzögert ihn nur. Ein Deckel senkt kA laut Ferreira (2025) um 44 %.

## Rollen (Wechselspiel wie bisher)

| Wer | Aufgabe |
|---|---|
| Claude (Cloud-Sitzung) | Recherche, Konzept mit Belegen, Texte, Didaktik; Abnahme des Baus (Zahlen gegen das Modell, Didaktik, Gestaltung, Handy); Live-Abnahme nach der Veröffentlichung |
| Codex | unabhängige Prüfung des Konzepts (Rolle X4); **Programmierung** nach dem Konzept mit Tests (Rolle S-Bau); Veröffentlichung über Sites |
| TL | entscheidet nach jeder Phase; gibt die Veröffentlichung frei |

Wer etwas gebaut hat, prüft es nicht selbst ab.

## Phasen und Haltepunkte

### Phase 1: Recherche und Konzept (Claude)

1. Drei Rechercheaufträge parallel (Agenten), je mit Quelle, Fundstelle, Prüfstatus (Volltext, Abstract, Sekundärquelle) und wörtlichem Kurzzitat:
   - **Lernen mit Simulationen:** Gestaltungsprinzipien und Befunde, mindestens: PhET (Wieman, Adams und Perkins 2008; Adams et al. 2008; implizites Gerüst nach Podolefsky, Perkins und Adams 2010), entdeckendes Lernen und Anleitung (de Jong und van Joolingen 1998; Lazonder und Harmsen 2016), Überblicke zur Wirkung (Rutten, van Joolingen und van der Veen 2012; Smetana und Bell 2012; D'Angelo et al. 2014), Vorhersagen (Predict, Observe, Explain nach White und Gunstone 1992; Crouch et al. 2004 ist schon Grundlage), ICAP (Chi und Wylie 2014), physische und virtuelle Versuche zusammen (de Jong, Linn und Zacharia 2013). Die Liste ist ein Startpunkt: prüft jede Angabe an der Quelle, streicht, was nicht trägt, ergänzt Wichtiges.
   - **Gestaltung und Bedienbarkeit:** mehrere Darstellungen (Ainsworth 2006), Multimedia-Prinzipien (Mayer), kognitive Belastung, Diagrammgestaltung, Barrierefreiheit (WCAG 2.2, Farben, Tastatur, Bildschirmleser), Handy im Hörsaal.
   - **Fach und Modell:** sinnvolle Erweiterungen und ihre Grenzen, zum Beispiel Deckel, Bechermaterial (Edelstahl, Keramik), Verdunstung, nichtlineare Wärmeabgabe, kA aus allen Messpunkten statt aus zwei, Energie als Säulen oder Fläche, Bilanzraum sichtbar machen. Jede Erweiterung mit Quelle oder eigener Herleitung und mit Testfall.
2. Daraus `simulation/KONZEPT.md`: Lernziele der Simulation (passend zu Tutorium 5), Ablauf in der Sitzung (10 bis 15 Minuten, zu zweit, Vorhersage vor dem Prüfen), Anforderungen in drei Stufen (muss, sollte, kann) **je mit Beleg**, Seitenaufbau (Skizzen als Bild), Texte der Reiter, Fragen, Modell und Erweiterungen, Prüfplan (Zahlen, Bedienung, Handy, Barrierefreiheit), Aufwand.
3. **Entscheidungen für die TL** am Ende des Konzepts mit klarer Empfehlung, mindestens:
   - eigene Website oder Teil des Lernzentrums (Empfehlung der Übergabe: eigene Website, Aussehen wie die Simulationsseiten des Lernzentrums; die beiden Arbeitsstränge bleiben getrennt);
   - **Freischaltung:** Die Simulation verrät die Antwort auf die Vorab-Frage. Vorschlag: nur für die TL sichtbar, öffentlich erst zur Sitzung, oder ein Startzustand, der nichts verrät (Kurven erst nach eigener Vorhersage);
   - Sprache (nur Deutsch oder auch Englisch);
   - welche Erweiterungen.
4. Anhalten, committen, pushen. Der TL schreiben: „Bitte in Codex die Prüfung des Konzepts starten (Rolle X4, AGENTS.md).“

### Phase 1b: Prüfung des Konzepts (Codex, X4) und Entscheidung (TL)

Claude holt den Bericht, rechnet nach, legt der TL die Entscheidungen mit Empfehlung vor und hält an.

### Phase 2: Bau (Codex, S-Bau) und Abnahme (Claude)

- Codex baut nach dem entschiedenen Konzept in `simulation/site/` (eine Seite, CSS und JavaScript eingebettet oder daneben, keine fremden Server, offline lauffähig), mit Tests in `simulation/tests/` (Zahlen gegen `kaffee_modell.py` und gegen eine eigene Rechnung, Bedienung im Browser bei 390 und 1366 px, Barrierefreiheit), Bericht `simulation/BAU_BERICHT.md`.
- Claude nimmt ab: Zahlen unabhängig nachrechnen, Fragen in der Reihenfolge der Studierenden bearbeiten, Seiten ansehen, Texte prüfen. Befunde zurück an Codex, bis nichts Wichtiges offen ist.

### Phase 3: Veröffentlichung (Codex) und Live-Abnahme (Claude)

- Codex veröffentlicht über Sites unter einer eigenen Adresse (Vorschlag: `waermeuebertragung-kaffee`), Zugang wie von der TL entschieden, mit Baunachweis wie beim Lernzentrum.
- Claude prüft live (Dateien gleich dem Bau, Rechenwerte, Handy, Konsole ohne Fehler) und gibt der TL den Link.

## Regeln

- Zahlen nur aus dem Modell oder einer getesteten Erweiterung; Aufgabenblatt und Lösung nicht ändern (eigener Auftrag, wenn nötig).
- Indizes: beschreibende Indizes aufrecht (Ä24), Formelzeichen wie in Vorlesung und Aufgabe.
- Literatur: nur, was an der Quelle geprüft ist, mit Prüfstatus; Websuche über die Such- und Abrufwerkzeuge.
- **Protokolle:** Parallel läuft die Kaffee-Sitzung auf `claude/kaffee-pruefung-sgvo1r` (Protokolle Version 14.1). Deshalb keine Protokollnummern vergeben: Einträge als Entwurf in `simulation/PROTOKOLL_NOTIZEN.md` sammeln (Art K, G oder D, Datum, Text); die Nummern vergibt die Übernahme nach dem Merge.
- Nichts an andere senden; Änderungen an Texten der TL kennzeichnen; Zwischenstände kurz.
