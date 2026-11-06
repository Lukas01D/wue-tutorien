# Auftrag X5: Abnahme des Baus der Kaffee-Simulation (Codex)

> Für Codex. Geschrieben von Claude nach `simulation/BAU_AUFTRAG.md`, Teil 7. Startsatz der TL: „Nimm den Bau der Simulation ab nach simulation/X5_AUFTRAG.md (Rolle X5).“ Du prüfst unabhängig von Claude und mit einem anderen Modell; die Rollenprüfungen G1 bis G8 waren getrennte Prüfungen desselben Modells (Claude).

## 1 Was geprüft wird

- **Zweig:** `claude/simulation-tool-kaffee-4kcacl`. Vorher `git fetch origin claude/simulation-tool-kaffee-4kcacl` und `git checkout claude/simulation-tool-kaffee-4kcacl`.
- **Stand:** genau der Commit, auf den der Zweig beim Start zeigt. Notiere `git rev-parse HEAD` im Bericht. Letzter Commit, der die Seite selbst ändert: `cdab2c3`.
- **Artefakt:** `simulation/site/index.html` und die bytegleiche Kopie `simulation/site/Kaffee_Simulation.html`, SHA-256 `1d90ce2f84349754592a5dd572a760a5d212cd3383bcafbeb1cceaf06e07292b`, 399 063 Bytes. Stimmt die Prüfsumme nicht (`sha256sum simulation/site/index.html`), brich ab und melde das.
- **Neu bauen** (Gegenprobe der Reproduzierbarkeit): `python3 simulation/site/bauen.py --pruefen` muss „gleich“ ausgeben (Python 3 mit fontTools).
- Ändert sich nach dem geprüften Stand etwas an der Seite, müssen die betroffenen Punkte erneut geprüft werden.

## 2 Grundlagen (Rangfolge)

1. `simulation/BAU_AUFTRAG.md` (Bauauftrag der TL, Commit 6526feb)
2. Entscheidungen der TL: E1 bis E8 und K1 bis K11 (`simulation/X4_ENTSCHEIDUNGSVORLAGE.md`, `simulation/KONZEPT.md` Abschnitt 12), Lernzentrum K5 (drei Reiter)
3. `simulation/KONZEPT.md` Fassung 2 (Anforderungen M, S, K; Fragen Abschnitt 6; Modell und Erweiterungen Abschnitt 8)
4. `simulation/AUFTRAG_Simulation_Kaffee.md`
5. Aussehen des Lernzentrums v8 (Repository `Lukas01D/waermeuebertragung-lernzentrum` oder die lokale Kopie, falls vorhanden; Tag `hauptadresse-v8-2026-11-05`)

Ablauf und Zustände: `simulation/ZUSTAENDE.md`. Aufgabe und Lösung in der fertigen Fassung: `ergebnisse/kaffee/fertig/Kaffee_Aufgabe_Tutorium5_2026-10-31.pdf` und `Kaffee_Loesung_Tutorium5_2026-10-31.pdf`; Rechenskript der Lösung als wörtliche Kopie in `simulation/modell/kaffee_modell.py` (Herkunft `simulation/modell/HERKUNFT.md`).

## 3 Vollständig und unabhängig nachprüfen

Diese Punkte prüfst du **ganz** und mit **eigener** Rechnung oder eigenem Browserlauf, ohne dich auf Claudes Tests zu verlassen:

1. **Alle Muss-Anforderungen** M-1 bis M-22 (Konzept 4.1) in der Fassung, die der Bauauftrag und die Entscheidungen festlegen (zum Beispiel drei Reiter statt neun, K5 des Lernzentrums). Für jede: erfüllt, nicht erfüllt, mit Beleg.
2. **Fachliche Risikofälle, Zahlen eigenständig nachgerechnet** (eigenes Skript, nicht `kaffee_erweitert.py` und nicht der Code der Seite):
   - Standardwerte: $\vartheta_1$ 34,05 °C, $\vartheta_2$ 30,19 °C, 3,85 K, $Q_1$ 34,88 kJ, $Q_2$ 38,57 kJ, Mischtemperatur 70,47 °C, *kA* 0,3402 W/K.
   - Größter Unterschied nach Konzept 8.1 (Maximum über den Zeitpunkt der Zugabe, Unterschied direkt nach der Zugabe, gleiches *kA*): 3,862 K ohne Becher, 3,090 K mit Becher, für jedes *kA* gleich; Zeitpunkt 55,7 min, mit *kA* · 0,56 bei 99,5 min. Nicht verwechseln mit dem Unterschied nach festen 60 min (zum Beispiel 3,51 K mit Deckel).
   - Energiebilanz mit Milchbeitrag (Milch für Tasse 2 bei Raumtemperatur: 1,95 K), Becher (Teil g), *kA* aus der Messung nach 10 min, *kA* festhalten, Voreinstellungen der Tabelle 8.2.1, *kA* von Tasse 1 abweichend (105 %), Grenzwert bei sehr später Zugabe (1,91 K).
   - Jede Zahl in den Auflösungen der Fragen (Start, Frage 1, Frage 2, V1 bis V5), Deutsch und Englisch.
   - Kann-Punkte, soweit gebaut: Trinkzeit 60 °C (M10), Becher kalt (M9), CSV (M11).
3. **Freigabe nach der Vorhersage:** Vor der eigenen Vorhersage darf nichts das Ergebnis zeigen: keine Kurve, Zahl, Säule, Tabelle, Ansage, kein Text in den Reitern „Modell“ und „So rechnet der Code“ (ZUSTAENDE.md, Regel 1). Prüfe das im DOM, im Barrierefreiheitsbaum und in `aria-live`. Hinweis: Die Seite ist eine einzige Offline-Datei; die Texte aller Auflösungen stehen deshalb im Skript-Quelltext. Bewerte, ob das eine Verletzung ist (Claude hat es als technische Grenze dokumentiert, siehe Baubericht).
4. **Kurslink** (ZUSTAENDE.md Abschnitt 5): hin und zurück mit gleichen Werten, Rückfrage vor dem Ersetzen, „Nicht übernehmen“ ändert nichts, beschädigte und fremde Links ändern nichts und nennen den Grund, `#…` verschwindet aus der Adresse, nichts geht an einen Server.

## 4 Stichproben genügen

Für die ergänzenden Belege von Claude reichen Stichproben: Tests in `simulation/tests/` (Befehle im Baubericht), Bilder in `simulation/bildschirmfotos/bau/`, Prototypen (`simulation/PROTOTYPEN.md`), Gutachten und Zusammenführung (`simulation/gutachten/`), Begleitmaterial (`simulation/EINSATZ_TUTORIUM.md`, `simulation/kurzkarte/`).

## 5 Weitere Prüfpunkte

- Fragen in der Reihenfolge der Studierenden bearbeiten (Start, Frage 1, Frage 2, dann Vertiefung), mit eigener Vorhersage, auch mit falscher und mit „ohne Vorhersage aufdecken“.
- Handy (390 × 844 hoch, 844 × 390 quer, 360 × 640), Bedienung mit Tippen, Anheften des Diagramms, Bildschirmtastatur (simuliert durch kleinere Fensterhöhe).
- Barrierefreiheit nach WCAG 2.2 AA (Tastatur, Fokus, Namen, Ansagen, Kontrast, Umbruch bei 320 px, Zielgrößen).
- Texte in beiden Sprachen: Wortlaut der Fragen und Auflösungen wie Konzept 6 (in du-Form), Englisch nach Glossar Anhang C, keine Gedankenstriche, Dezimalkomma und Dezimalpunkt.
- Nähe zum Aussehen des Lernzentrums v8 (Farben, Schrift, Knopfhierarchie, Regler, Rechenwerte, Reiter); begründete Abweichungen stehen im Baubericht.
- Offline: Datei ohne Netz, CSP wirksam, keine Anfragen nach außen.

- **Bekannte offene Befunde:** Der Bau ist als „unvollständige Übergabe“ abgegeben (`simulation/BAU_BERICHT.md`, Abschnitt Status: unter anderem V3 vor der Vorhersage, G10-01; Schnitt ohne Beschriftung, G6-R3-01; große Grundschrift; Diagrammschrift am kleinen Handy). Bestätige oder widerlege sie mit eigenem Beleg und gib ihnen deine eigene Schwere; was du zusätzlich findest, ist besonders wichtig.

## 6 Zwei Läufe

Du darfst die Prüfung in zwei getrennten Läufen machen:

- **Lauf A: Zahlen und Fachliches** (Abschnitt 3, Punkte 1 bis 2, dazu die fachlichen Texte).
- **Lauf B: Bedienung, Sprache und Barrierefreiheit** (Abschnitt 3, Punkte 3 und 4, Abschnitt 5).

Beide Läufe schreiben in denselben Bericht (Abschnitte A und B).

## 7 Grenzen

- Nichts veröffentlichen, nichts an andere senden, keine Freischaltung.
- Keine eigenständige Änderung fachlicher Entscheidungen (Lernziele, Fragen, Auflösungen, entschiedene Punkte). Was du für falsch hältst, meldest du mit Beleg und Vorschlag.
- Am Code und an Texten nichts ändern; nur der Bericht und deine eigenen Prüfskripte (in einem eigenen Ordner, zum Beispiel `simulation/x5_skripte/`).
- Pushe auf einen eigenen Zweig (zum Beispiel `codex/x5-abnahme`), nicht auf den Zweig von Claude. Kein Pull Request.

## 8 Bericht

`simulation/X5_CODEX_ABNAHME.md` mit:

1. Geprüfter Commit (`git rev-parse HEAD`), SHA-256 des Artefakts, Umgebung (Browser, Versionen), was nicht prüfbar war.
2. Urteil: **abnahmefähig**, **abnahmefähig mit Änderungen** oder **nicht abnahmefähig**.
3. Tabelle der Muss-Anforderungen: ID, Ergebnis, Beleg.
4. Tabelle der nachgerechneten Zahlen: Größe, eigene Rechnung, Anzeige der Seite, Urteil.
5. Befunde nach Schwere (blocker, high, medium, low wie im Bauauftrag 4.1) im Format
   `| ID | Schwere | Befund | Beleg | Vorschlag |`, IDs X5-01, X5-02, …
6. Abschnitte A und B, falls du in zwei Läufen arbeitest.

## 9 Nachprüfung nach der Korrekturrunde (nur betroffene Punkte)

> Startsatz der TL: „Prüfe die Korrekturrunde nach simulation/X5_AUFTRAG.md, Abschnitt 9 (Nachprüfung X5).“ Vorher `git fetch origin claude/simulation-tool-kaffee-4kcacl` und `git checkout claude/simulation-tool-kaffee-4kcacl`. Bericht als `simulation/X5_CODEX_NACHPRUEFUNG.md` auf einem eigenen Zweig (zum Beispiel `codex/x5-nachpruefung`), Format wie Abschnitt 8; IDs X5N-01, X5N-02, …

- **Stand:** Commit, auf den der Zweig beim Start zeigt (`git rev-parse HEAD` im Bericht). Artefakt `simulation/site/index.html` und bytegleich `Kaffee_Simulation.html`, SHA-256 `e6f95ca27a5c508344e6802195e9ea62f07ad743694761198057da98e757cc1d`, 433 303 Bytes, letzter Commit an der Seite 6077a92. `python3 simulation/site/bauen.py --pruefen` muss „gleich“ ausgeben.
- **Grundlage:** zusätzlich zu Abschnitt 2 die Antwort `simulation/X5_ANTWORT.md`, die Entscheidungen F1 bis F14 (`simulation/BAU_BERICHT.md`, Fragen an die TL; Wortlaute in `simulation/KONZEPT.md` 12.1), `simulation/ZUSTAENDE.md` (Ergänzungen vom 06.11.2026) und die Zusammenführung Runde 4 (`simulation/gutachten/ZUSAMMENFUEHRUNG.md`, letzter Abschnitt).
- **Zu prüfen:**
  1. Deine Befunde X5-01 bis X5-11 mit deinen Reproduktionen (deine Skripte in `simulation/x5_skripte/` laufen unverändert; eine Kopie mit Läufen von Claude liegt in `simulation/x5_regression/`). Zu X5-03: Die Seite lehnt den Wechsel auf „aus der Messung“ ab, wenn der gleichwertige Wert außerhalb 30 bis 90 °C liegt; dein Schritt `Quellenwechsel_haelt_Kurven_bei_kA1` bricht deshalb beim Anklicken ab. Bewerte, ob das deinem Vorschlag entspricht.
  2. Die betroffenen Muss-Anforderungen: M-1, M-3, M-6, M-11, M-13, M-14, M-19, M-21, M-22 (Stand in der Nachweistabelle des Baubericht).
  3. Die übrigen Änderungen der Korrekturrunde (Liste in `simulation/X5_ANTWORT.md` und in der Zusammenführung): neue Wortlaute F3 bis F12 (Zahlen in DE und EN), Sperren vor den Vorhersagen (Startauflösung, Reiter „Modell“ und „So rechnet der Code“, V1 bis V5 beim Öffnen), Beschriftungen im Diagramm, Anheften am Handy, Meldungen und Fokus.
  4. Rechenkern unverändert (Block MODELL, SHA-256 `b32e3f9d…7d24`), eigene Stichprobe der Zahlen.
  5. Die Entscheidungen Q1 bis Q7 der TL (Konzept 12.1, zweite Tabelle) in DE und EN, insbesondere die Startauflösung vor und nach der Vorhersage zu Frage 1 (Q1) und die neue Begründung in V1 (Q2, fachlich).
  6. Den Befund aus der Gestaltungsprüfung: Beamer 1280 × 720 und 1366 × 768, nach der Startvorhersage Frageleiste und ganzes Diagramm im Bild, nach Frage 1 zusätzlich der Regler „Zugabe nach“. Die Gestaltung selbst ist nach Entscheidung der TL unverändert (kein Entwurf übernommen).
- **Nicht zu prüfen:** Was die Korrekturrunde nicht berührt hat; Gestaltungsentwürfe (Zweig `claude/simulation-design-assignment-w01on3`).
- **Grenzen** wie Abschnitt 7.
