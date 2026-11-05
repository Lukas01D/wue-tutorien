# Bauauftrag: Simulation „Kaffee mit Milch“ (Rollentausch, Claude baut)

> Stand 05.11.2026, geschrieben im Projekt-Chat für die Tutoriumsleitung (TL, Lukas). Für die Claude-Sitzung „Simulationstool Kaffee“. Vor dem Abschicken von GPT gegengeprüft (24 Befunde P01 bis P24, eingearbeitet; Liste am Ende). Deutsch, keine Gedankenstriche (– oder —), stattdessen Komma, Punkt, Doppelpunkt oder Klammern.

## 0 Rahmen

**Rollentausch (Entscheidung der TL, 05.11.2026).** Diesmal baust du (Claude) die Simulation, nicht Codex wie in `AUFTRAG_Simulation_Kaffee.md`, `AGENTS.md` (Rolle S-Bau) und Konzept Abschnitt 11 vorgesehen; Codex nimmt danach unabhängig ab (Rolle X5, Teil 7). Wer baut, nimmt nicht selbst ab. Grundlage ist der Stand der Konzeptphase auf diesem Zweig (Fassung 2, Commit 93cb32e).

**Unbeaufsichtigt.** Die TL ist bis morgen nicht erreichbar. Arbeite alle Teile nacheinander durch. Bei einem Konflikt oder einer fehlenden Voraussetzung: Konflikt dokumentieren und die davon unabhängigen Aufgaben weiterbearbeiten.

**Qualität vor Verbrauch.** Nutze Agenten, wo sie helfen, sieh dir alles selbst an und bessere nach. Die Grenzen dafür setzen die Abbruchregeln in Teil 4.

**Rangfolge bei Widersprüchen** (P01):
1. dieser Bauauftrag;
2. Entscheidungen der TL: E1 bis E8 und K1 bis K11 (`simulation/X4_ENTSCHEIDUNGSVORLAGE.md`) sowie die Entscheidung K5 der TL im Lernzentrum (Runde 12: drei Reiter unter der Simulation), die hier ausdrücklich übernommen wird;
3. `simulation/KONZEPT.md` Fassung 2;
4. `simulation/AUFTRAG_Simulation_Kaffee.md`;
5. das Vorbild Lernzentrum.

**Entscheidungsgrenzen** (P01):
- Selbst entscheiden darfst du nur umkehrbare technische und gestalterische Einzelheiten innerhalb der entschiedenen Anforderungen.
- Fachliche Aussagen, Lernziele, Fragen, Auflösungen und entschiedene Punkte änderst du nicht eigenständig. Fehlt ein Wortlaut oder passt etwas nicht, meldest du das als offene Frage mit Empfehlung.

**Regeln aus dem Auftrag gelten weiter:**
- Zahlen nur aus `kaffee_modell.py` oder einer getesteten Erweiterung.
- Aufgabenblatt und Lösung nicht ändern.
- Indizes nach Ä24, keine Gedankenstriche.
- Protokolleinträge nur als Entwurf in `simulation/PROTOKOLL_NOTIZEN.md`.
- Nichts veröffentlichen, nichts an andere senden.
- Sprachen nach E3 (Deutsch und Englisch mit Umschalter), Ansprache „du“ nach E5.

**Git** (P02):
- Committe nur eigene Änderungen und pushe nach jedem Teil, ausschließlich auf `origin` in den Zweig `claude/simulation-tool-kaffee-4kcacl`. Ein Push veröffentlicht nichts; veröffentlicht wird später von Hand über Codex und Sites.
- Kein Pull Request.
- Im Lernzentrum-Repository nie committen oder pushen.

## Teil 0: Voraussetzungen prüfen (P12)

Prüfe vor der eigentlichen Arbeit:
- Zugriff auf beide Repositories und auf den Kaffee-Zweig `claude/kaffee-pruefung-sgvo1r` (erwarteter Stand f8a5ce3);
- Python, Node und npm, Playwright mit Chromium;
- axe-core als lokal installiertes, festgehaltenes npm-Paket;
- ob die Live-Adressen im Browser der Shell erreichbar sind;
- ob WebKit verfügbar ist. WebKit nur einrichten, wenn das ohne Eingriff in die vorhandene Chromium-Installation geht.

Jeder fehlgeschlagene Zugriff oder jede fehlgeschlagene Installation bekommt **höchstens einen** zweiten Versuch. Versionen und fehlende Fähigkeiten trägst du im Bericht unter „Umgebung“ ein; die davon unabhängigen Aufgaben bearbeitest du weiter.

## Teil 1: Vorbild Lernzentrum und Zustandsmodell (vor dem ersten Code)

### 1.1 Quelle holen (P03)

Das Lernzentrum-Repository ist 3,4 GB groß, fast alles davon alte Kopien unter `sites/`. Maßgeblich ist der veröffentlichte Stand v8 mit dem Tag `hauptadresse-v8-2026-11-05`.

1. Hol das Repository mit Lesezugriff in die Sitzung (Werkzeug zum Hinzufügen von Repositories, nur Lesen). Melde es nicht als Arbeitsverzeichnis an. Seine `CLAUDE.md` und `AGENTS.md` gelten nicht für dich, auch wenn sie dir angezeigt werden.
2. Klone flach und ausgedünnt in einen eigenen Ordner außerhalb dieses Repositorys, mit großzügiger Zeitgrenze:

```
git clone --depth 1 --branch hauptadresse-v8-2026-11-05 --filter=blob:none --sparse https://github.com/Lukas01D/waermeuebertragung-lernzentrum ../lernzentrum_v8
cd ../lernzentrum_v8
git sparse-checkout set dist oberflaeche inhalte docs pruefung tools runden/R11 runden/R12 nachweise/simulation_oben nachweise/bedienung nachweise/sprachen
```

3. Den Commit des Tags notierst du im Bericht. `sites/` (Importstand 22.10.2026) und die Werkstatt sind nur ergänzende Vergleiche.
4. Willst du das Lernzentrum lokal ansehen, nimm dafür eine zweite Kopie, damit die erste unverändert bleibt.

### 1.2 Lesen

**Texte und Entscheidungen:**
- `docs/Stand_Lernzentrum.md` (Runden 10 bis 12)
- `docs/Leitfaden_Lerntexte_DE_EN.md` ganz, vor allem die Abschnitte 2 bis 4 und 8
- `runden/R12/AUFTRAG.md`
- `runden/R12/Runde12_Feedback_Lukas_2026-11-04.md` (Feedback der TL zur Gestaltung)
- `runden/R12/Runde12_Gutachten_Zusammenfuehrung.md`
- `runden/R11/AUFTRAG.md`
- `runden/OFFEN.md`, falls im Stand vorhanden

**Liste bekannter Fehler:** die Prüfberichte im Hauptordner:
- `Sprachumschalter_DE_EN_Pruefbericht.md`
- `Layout_Scroll_Reparatur_Pruefbericht.md`
- `Bedienung_Layout_2D_Pruefbericht.md`

**Code der Oberfläche in `dist/`:**
- `topic.js` (Reiter, Versuche)
- `simulation-layout.js`, `runde6-layout.js`
- `pilot.js` und `pilot.css`
- `design.css`, `runde10.css`, `runde11.css`, `typeset.css`
- `i18n.js` und `sprachen.js`
- `numeric-input.js`, `parameter-help.js`
- `fonts/` (Fira, SIL OFL)

**Oberflächentexte:** `oberflaeche/sprachen.json`.

### 1.3 Ansehen

Sieh dir die Simulationsseiten von Thema 1 und 2 an, auf Deutsch und Englisch, bei 390 × 844 und 1366 × 768 px:
- live unter <https://waermeuebertragung-lernzentrum.qarri196.chatgpt.site> (Hauptadresse, v8) und <https://waermeuebertragung-werkstatt.qarri196.chatgpt.site>, falls der Browser der Shell sie erreicht;
- sonst lokal aus der Betrachtungskopie.

Die Bildschirmfotos behältst du als Vergleichsgrundlage.

### 1.4 `simulation/VORBILD_LERNZENTRUM.md`

**Inhalt:**
- Quellcommit;
- Gestaltungswerte als Tabelle: Farben, Schrift und Größen, Abstände, Umbruchbreiten, Rangfolge der Knöpfe, Reiter, Regler, Kasten Rechenwerte, Formelsatz;
- Aufbau der Simulationsseite nach Runde 12;
- Verhalten des Sprachumschalters;
- bekannte Fehler aus den Prüfberichten und wie du sie vermeidest;
- Schreibregeln aus dem Leitfaden;
- eine Zuordnung Konzept Fassung 2 → Aufbau v8 mit allen Abweichungen.

**Drei Reiter (K5):** Unter der Simulation stehen drei Reiter: Versuche, Modell, So rechnet der Code. Ordne die Texte aus Anhang A des Konzepts dort ein und kennzeichne das als Abweichung vom Konzept (Grund: K5). Du sortierst die Texte dabei nur um, inhaltlich änderst du sie nicht.

### 1.5 `simulation/ZUSTAENDE.md`: Ablauf und Zustände festlegen, bevor gebaut wird (P09, P10, P11)

**1. Pflichtweg als Zustandsfolge.**
- Lege die Zustände fest: Startkarte, Vorhersage, Freigabe der Ergebnisse, Frage 1, Frage 2.
- Lege für jeden Zustand fest, was sichtbar ist und was jeder der drei Reiter dann zeigt.
- Regel: Die eigene Vorhersage und ihre Begründung müssen möglich sein, bevor irgendetwas die Auflösung zeigt, auch nicht in „Modell“ oder „So rechnet der Code“. Danach wirken die Regler sofort.
- Einen Knopf „Berechnen“ gibt es nicht. Das Kaffeemodell rechnet sofort, und die Freigabe nach der Vorhersage übernimmt die Startkarte. Ausnahme: Das Konzept verlangt ausdrücklich einen getrennten Prüfschritt.

**2. Was erhalten bleibt.** Lege für Sprachwechsel, Reiterwechsel, Neuladen, Öffnen eines Kurslinks und „Zurücksetzen“ fest, welche Eingaben, Vorhersagen, Freigaben und Messwerte erhalten bleiben.
- Ein Sprachwechsel ändert keine fachlichen Werte.
- Die Kurswerte bleiben getrennt von den persönlichen Antworten.
- „Zurücksetzen“ macht die Seite für die nächste Gruppe sauber.
- Ist der Speicher gesperrt (privates Fenster), funktioniert die Seite trotzdem, nur ohne Speichern.

**3. Kurslink** (nach Konzept 9.4):
- versioniertes Format nur für Kursmesswerte;
- Größengrenze;
- Prüfung jedes Werts;
- beschädigte oder fremde Links ändern nichts und zeigen einen verständlichen Hinweis;
- vor der Veröffentlichung lokal getestet.

Dokumentiere auch: Ein Kurslink, den alle öffnen können, braucht die veröffentlichte Adresse. Ohne Netz ist der Ersatz die Offline-Datei mit Eintippen der Werte. Dass die Seite bis zum Sitzungstag nur für die TL sichtbar ist, regelt später die Veröffentlichung, nicht dieser Bau.

## Teil 2: Rechenkern zuerst, testgetrieben

### 2.1 Geprüften Kern sichern (P04)

**Grundlage ist das bestehende Werkzeug:**
- Modellblock, Gültigkeitsprüfungen, Messwertübernahme, Zahleneingabe und Tests aus `ergebnisse/kaffee/simulation/`;
- die neueste Fassung mit den vier Fragen holst du mit `git fetch origin claude/kaffee-pruefung-sgvo1r` und `git show origin/claude/kaffee-pruefung-sgvo1r:ergebnisse/kaffee/fertig/Kaffee_Simulation.html`.

**Vor jeder Änderung:**
- Halte Commit und SHA-256 der Ausgangsquellen im Bericht fest (`kaffee_modell.py`, MODELL-Block, bisherige Tests).
- Der MODELL-Block, die bisherigen Gültigkeitsprüfungen und die Referenztests bleiben unverändert.
- Erweiterungen stehen in einem eigenen ERWEITERUNG-Block ohne Bezug zur Oberfläche (Konzept 9.2), mit eigenen Tests.

**Python-Referenz:** `simulation/modell/kaffee_erweitert.py`, die `kaffee_modell.py` importiert.

**Zuordnung der Eingaben:** Prüfe zusätzlich, wie die Eingaben der Oberfläche auf die Modellparameter abgebildet werden, einschließlich der Einheiten (ml gegen kg, °C, min gegen s, W/K).

**Fehlerverdacht im Original:** Vermutest du einen Fehler im Original, dokumentierst du ihn als Befund. Das Original passt du nicht an.

### 2.2 Tests in `simulation/tests/` (P05, P06, P07)

**1. Feste Testfälle:** alle aus `simulation/recherche/claude_f2/f2_testfaelle.txt` und aus Abschnitt 8 des Konzepts.

**2. Zufallstests:**
- 10 000 Parametersätze im erlaubten Bereich, mit festem Zufallsstartwert und dokumentierter Verteilung;
- dazu gesondert die Grenzen und Sonderfälle;
- JavaScript gegen Python an festgelegten Zeitpunkten, insbesondere unmittelbar vor, bei und nach der Milchzugabe;
- absolute und relative Toleranzen je Ausgabegröße (°C, K, kJ, W, min) legst du fest, bevor du auswertest;
- Fehlerfälle werden reproduzierbar gespeichert;
- Toleranzen werden nie geweitet, nur damit ein Test besteht.

**3. Physikalische Prüfungen**, jeweils nur in ihrem Gültigkeitsbereich:
- Zwischen zwei Mischereignissen nähert sich jede Temperatur monoton der Raumtemperatur.
- Mischtemperaturen folgen aus den Wärmekapazitäten der Beteiligten.
- Energiebilanz:
  - Systemgrenze: Tasseninhalt, mit Becher, wenn er eingeschaltet ist;
  - Bezugstemperatur: Raumtemperatur;
  - abgegebene Wärme positiv, wie $Q_1$ und $Q_2$ im Konzept;
  - einschließlich der Milchzugabe.
- **Größter Unterschied** genau wie in Konzept Abschnitt 8.1 definiert:
  - Maximum über den Zeitpunkt $t_\mathrm{Z}$ der Milchzugabe in Tasse 2, Unterschied unmittelbar nach der Zugabe, gleiches *kA* beider Tassen;
  - Werte: 3,862 K ohne Becher, 3,090 K mit Becher, für jedes *kA* gleich; nur der Zeitpunkt verschiebt sich (55,7 min; mit *kA* · 0,56: 99,5 min);
  - Prüfe das über einen Bereich von *kA*. Angezeigt wird gerundet.
  - Der Unterschied nach festen 60 min ist eine andere Größe (zum Beispiel 3,51 K mit Deckel) und darf nicht damit verwechselt werden.
  - Widerspricht das Modell, meldest du einen fachlichen Konflikt. Weder Modell noch Erwartung passt du an.
- „*kA* festhalten“ und „*kA* aus der Messung“ wirken wie in F2-15 und 8.5 beschrieben; die Werte der Voreinstellungen stimmen mit der Tabelle in 8.2 (M8) überein.

**4. Ungültige und extreme Eingaben.**

### 2.3 Zahlen in Texten (P08)

- **Modellabhängige Ergebniszahlen** in Texten beider Sprachen: Ein Skript erzeugt sie aus ungerundeten Modellwerten oder prüft sie dagegen (wie `NACHRECHNUNG.md` im Lernzentrum).
- **Messdaten, Literaturwerte, Richtwerte und didaktische Vorgaben** bekommen einen Herkunftsnachweis.
- **Ausgenommen** sind Fragennummern, Jahreszahlen und bibliografische Angaben.
- **Deutsch und Englisch** verwenden dieselben Zahlenquellen und festgelegte Rundungsregeln (Dezimalkomma im Deutschen, Dezimalpunkt im Englischen).

## Teil 3: Bau der Oberfläche

### 3.1 Aufbau und Artefakt (P20)

**Quellen:** getrennt in `simulation/site/src/` (Texte DE und EN, CSS, Rechenkern, Oberfläche). Ein Bauskript fügt sie zu `simulation/site/index.html` zusammen, Kopie als `Kaffee_Simulation.html`. So können Agenten parallel arbeiten.

**Prüfung des fertigen Artefakts:**
- ohne Begleitdateien, in einem frischen Browserprofil, einmal als lokale Datei und einmal über einen lokalen Server;
- auch versuchte Anfragen nach außen werden protokolliert; erlaubt sind keine;
- die Content-Security-Policy ist im fertigen Artefakt wirksam und lässt dessen Funktionen zu (zum Beispiel Hashes für eingebettete Skripte);
- die Schrift ist eingebettet;
- die Datei bleibt einschließlich aller Einbettungen unter 450 000 Bytes unkomprimiert;
- beide Kopien sind bytegleich.

### 3.2 Reihenfolge (P16)

1. Pflichtweg
2. Vertiefung
3. Kann-Punkte, erst wenn alle Muss-Anforderungen nachweislich bestanden sind:
   - Trinkzeit bis 60 °C;
   - Becher kalt (M9, mit den Testwerten dort);
   - CSV-Download;
   - feste Wärmestrom-Pfeile;
   - mitlaufende Pfeile nur, wenn sauber machbar.

Neue physikalische Erweiterungen bekommen eigene Annahmen und Referenztests. Was entfällt, wird dokumentiert; das gilt nicht als Mangel des Pflichtumfangs.

### 3.3 Sprache und Formelsatz

- Englisch nach Leitfaden Abschnitt 4 und Glossar Anhang C, mit denselben Begriffen wie im Lernzentrum.
- Formelsatz und Einheiten wie in v8: Leitfaden Abschnitt 3 und die Entscheidungen K1 bis K4 der Runde 12 im Lernzentrum.

### 3.4 Zwei offene Gestaltungsfragen

Gemeint sind die Darstellung der Energiesäulen und die Vertiefung am Handy.
- Je zwei begrenzte Prototypen mit denselben Beispieldaten bauen.
- Als Bildschirmfoto vergleichen und begründet wählen.
- Die Bilder behalten.

### 3.5 Abdeckung, Geräte, Leistung (P13, P15, P21)

**Abdeckungsmatrix.** Lege sie vorab in `simulation/ZUSTAENDE.md` fest:
- Größen: 390 × 844, 360 × 640, Querformat 844 × 390, 1366 × 768, Beamer 1280 × 720 und 1920 × 1080;
- beide Sprachen;
- Pflichtweg und Vertiefung;
- die Zustände aus Konzept 5.4;
- die wichtigen Fehlerzustände.

Layoutzustände belegst du mit Bildern in `simulation/bildschirmfotos/`, Verhalten mit reproduzierbaren Tests. Nicht jede Parameterkombination braucht ein Bild.

**Geräte.**
- Kennzeichne Prüfungen in Chromium als Chromium-Prüfungen; dazu WebKit, falls verfügbar.
- Schreib `simulation/ABNAHME_IPHONE.md`: eine Abnahmeliste für die TL auf einem echten iPhone mit Safari:
  - Hoch- und Querformat;
  - Regler mit dem Finger;
  - Dezimaleingabe und Bildschirmtastatur;
  - Zoom, Scrollen;
  - Sprachwechsel;
  - Kurslink;
  - Download;
  - Offline-Datei aus der Dateien-App.
- Chromium oder WebKit ersetzen diesen Gerätenachweis nicht; er bleibt offen, bis die TL ihn erbringt.

**Leistung.**
- Grenzen legst du vor der Messung fest.
- Gemessen werden: Dateigröße, Zeit bis zur Bedienbarkeit und Reaktionszeit bei einer festgelegten Reglerfolge.
- Eine Bedienfolge von mindestens 30 s läuft ohne Fehler, ohne veraltete Ergebnisse und ohne anwachsende Rechenaufträge.
- Messwerte aus der Cloud kennzeichnest du als solche.

## Teil 4: Rollenprüfungen (wie die Gutachten der Runde 12 im Lernzentrum)

### 4.1 Durchführung (P17, P18)

- Acht getrennte Rollen in frischen Kontexten, so parallel, wie die Umgebung es zulässt.
- Jede Rolle bekommt den Pfad der gebauten Datei, das Konzept und ihren Blickwinkel. Bauverlauf und deine Einschätzung bekommt sie nicht.
- Vor der eigenen Abgabe liest keine Rolle andere Gutachten.
- Bezeichne die Ergebnisse als „getrennte Rollenprüfungen desselben Modells“; die unabhängige Prüfung mit einem anderen Modell ist X5.

Jede Rolle schreibt `simulation/gutachten/G<Nr>_<Rolle>.md` im Format:

`| ID | Schwere | Befund | Beleg | Vorschlag | CONFIRMED/INFERRED |`

**Schweregrade** (vorab festgelegt):

| Grad | Bedeutung |
|:--|:--|
| blocker | falsche Physik oder falsche Zahl; Seite unbenutzbar; Lösung vor der eigenen Vorhersage sichtbar |
| high | Muss-Anforderung verletzt; Barriere ohne Umweg; Datenverlust |
| medium | erschwert Nutzung oder Verständnis spürbar |
| low | kosmetisch |

### 4.2 Die acht Rollen

| Rolle | Auftrag |
|:--|:--|
| G1 Studentin im dritten Semester | Pflichtweg am Handy (390 × 844) auf Deutsch durchspielen. Zeit je Schritt schätzen (Ziel etwa 10 min) und als Expertenschätzung kennzeichnen. Stellen notieren, an denen sie hängt. Prüfen, ob die Seite vor der eigenen Vorhersage etwas verrät. |
| G2 Internationaler Student | Alles nur auf Englisch. Verständlichkeit, Fachbegriffe, Muster aus Leitfaden Abschnitt 4, gemischte Sprache, Einheiten. |
| G3 Fachgutachter Wärmeübertragung | Legt zuerst eigene Gleichungen und begründete Prüffälle aus Aufgabe und Konzept fest, ohne den Code zu lesen. Rechnet dann 30 Zustände unabhängig nach und vergleicht erst danach mit der Seite. Prüft Annahmen, Grenzen, Formelzeichen wie in Vorlesung und Aufgabe, Indizes Ä24 sowie Begründung und Kennzeichnung der *kA*-Voreinstellungen. |
| G4 Lernpsychologie und Fachdidaktik | Vorhersage vor dem Prüfen, ICAP, Lernziele aus Konzept Abschnitt 2, kognitive Belastung, Rückmeldungen. Wird die Fehlvorstellung „die Energie bleibt ja erhalten“ wirklich angegangen? |
| G5 Barrierefreiheit (P14) | Führt eine Prüfliste der anwendbaren Kriterien von WCAG 2.2 AA mit Nachweis je Kriterium: axe-core, nur Tastatur, Fokusreihenfolge, Namen für Bildschirmleser, Kontrast auch der Kurven, Farbsehschwäche simuliert, Zoom 200 und 400 % mit Umbruch, reduzierte Bewegung, Zielgrößen. Prüft, ob Kurven und Energiesäulen auch als Werte und Aussagen zugänglich sind, ob Fehlermeldungen verständlich sind und ob Aktualisierungen angesagt werden. Mit einem verfügbaren Bildschirmleser prüfen; sonst bleibt dieser Nachweis offen. Fehlerfreiheit in axe-core allein ist kein Konformitätsnachweis. |
| G6 Gestaltung | Bildschirmfotos von Lernzentrum und Kaffee-Seite nebeneinander, in gleichen Größen und Zuständen. Abweichungen werden nach Auswirkung bewertet; begründete Anpassungen an die Kaffee-Seite sind nicht automatisch Fehler. |
| G7 Tutorin im Hörsaal | Beamer bei 1280 × 720 und 1920 × 1080 (Schriftgrößen gegen übliche Empfehlungen für die Projektion; die Prüfung im echten Hörsaal bleibt offen). Kurswerte über den Link in der Sitzung, Zurücksetzen zwischen Gruppen, Ersatz ohne Netz, Zeitplan der Sitzung. |
| G8 Technik und Robustheit | Versucht die Seite zu brechen: seltsame Eingaben, schnelles Umschalten, Sprachwechsel mitten in einer Frage, gesperrter Speicher, beschädigte Kurslinks, Datei offline geöffnet, Anfragen nach außen, Konsole, Bedienfolge aus 3.5. |

### 4.3 Zusammenführung und Abbruch (P19)

1. `simulation/gutachten/ZUSAMMENFUEHRUNG.md`: jeder Befund mit

   `| ID | übernehmen / ablehnen / offen | Begründung mit Beleg | Folge |`

2. Behebe blocker, high und medium. low behebst du, soweit es sinnvoll ist.
3. Prüfe jede Korrektur gezielt und wiederhole die betroffenen Regressionstests.
4. Es gibt **höchstens drei Gutachtenrunden insgesamt**. Ab Runde 2 prüfen die betroffenen Rollen und eine neue Studentin, die die Seite noch nicht kennt.
5. Nach Runde 3 endet die Bearbeitung, auch wenn noch Befunde offen sind.

**Abnahmebereit** ist der Stand nur, wenn kein blocker, high oder medium mehr offen ist und alle Muss-Nachweise vorliegen. Sonst übergibst du ausdrücklich als **„unvollständige Übergabe“** mit Liste der offenen Punkte.

Inhaltliche Fragen, die die TL entscheiden muss, sammelst du mit klarer Empfehlung.

## Teil 5: Begleitmaterial (P22)

**1. `simulation/EINSATZ_TUTORIUM.md` (Deutsch)** mit diesen Inhalten:
- Ablauf der Simulationsphase Minute für Minute;
- Verbindung zu Versuch und Rechnung (drei Ebenen);
- Beamer;
- Kurslink erzeugen und teilen;
- Ersatz bei Netzausfall;
- typische Fragen der Studierenden mit Antwort;
- Auflösungen der Fragen.

Zeitangaben kennzeichnest du als Schätzung.

**2. Kurzkarte für die Studierenden**, Deutsch und Englisch:
- je eine gut lesbare A4-Seite als PDF, ohne Verkleinern nur zum Einhalten der Seitenzahl;
- Text auswählbar, beide PDFs gerendert geprüft, einschließlich Formeln und Einheiten;
- ein Platzhalter für den QR-Code, ohne erfundenen Link (er entsteht erst nach der Veröffentlichung).

Die zugängliche Fassung desselben Inhalts ist die Website selbst.

## Teil 6: Nachweise und Bericht (P23)

**`simulation/BAU_BERICHT.md` enthält:**
- **Umgebung:** Versionen, fehlende Fähigkeiten.
- **Quellcommits und Prüfsummen:** Ausgangsquellen, Lernzentrum-Tag, SHA-256 von `index.html`.
- **Nachweistabelle** für jede Anforderung (muss, sollte, kann, F2-1 bis F2-17, K1 bis K11, E1 bis E8): wo umgesetzt, welcher Test, welches Bildschirmfoto. Status nur „bestanden“, „fehlgeschlagen“, „nicht geprüft“ oder „nicht anwendbar“, die letzten drei mit Grund.
- **Abweichungen** vom Konzept mit Grund.
- **Übernahmen aus dem Lernzentrum:** Datei und Stelle.
- **Reproduzierbare Testbefehle und alle Testergebnisse.**
- **Bilanz der Rollenprüfungen.**
- **Offene Nachweise in der echten Welt:** iPhone, Studierende, Hörsaal, Bildschirmleser.
- **Status:** „abnahmebereit“ oder „unvollständige Übergabe“.
- **Fragen an die TL** mit Empfehlung.

Einträge in `simulation/PROTOKOLL_NOTIZEN.md` ergänzen.

## Teil 7: Übergabe an Codex (P23, P24)

**1. `simulation/X5_AUFTRAG.md`** mit der vollständigen Abnahmeanweisung für Codex:
- **Geprüft wird** genau der übergebene Commit, mit Prüfsumme des Artefakts.
- **Vollständig und unabhängig nachprüfen:** alle Muss-Anforderungen und die fachlichen Risikofälle, also Zahlen eigenständig nachrechnen, die Freigabe nach der Vorhersage und den Kurslink.
- **Stichprobenartig reichen** die ergänzenden Belege.
- **Weitere Prüfpunkte:**
  - Fragen in der Reihenfolge der Studierenden bearbeiten;
  - Handy;
  - Barrierefreiheit;
  - Texte in beiden Sprachen;
  - Nähe zum Aussehen des Lernzentrums.
- **Zwei Läufe** sind erlaubt: A für Zahlen und Fachliches, B für Bedienung, Sprache und Barrierefreiheit.
- **Grenzen für Codex:** keine Veröffentlichung, keine eigenständige Änderung fachlicher Entscheidungen.
- **Bericht:** `simulation/X5_CODEX_ABNAHME.md`.
- Änderungen nach dem geprüften Stand erfordern eine erneute Prüfung der betroffenen Punkte.

**2. In `AGENTS.md` nur ein kurzer, gekennzeichneter Abschnitt** „Sechster Auftrag: Abnahme des Baus (Rolle X5)“:
- Startsatz „Nimm den Bau der Simulation ab nach simulation/X5_AUFTRAG.md (Rolle X5).“;
- Verweis auf die Datei.

Bestehende Regeln bleiben unverändert.

**3. Abschluss.** Anhalten, letzter Push. Dann der TL in einer kurzen Tabelle sagen:
- was steht;
- welcher Status (abnahmebereit oder unvollständig);
- was die TL tun muss;
- den Startsatz für Codex mit `git fetch origin claude/simulation-tool-kaffee-4kcacl` und `git checkout claude/simulation-tool-kaffee-4kcacl`.

Noch nicht veröffentlichen, noch kein Pull Request.

## Anhang: Gegenprüfung durch GPT (05.11.2026)

Alle 24 Befunde sind geprüft. Übernommen: P01, P02, P04, P06 bis P12, P14 bis P21, P23. Angepasst übernommen:

| ID | Anpassung |
|:--|:--|
| P03 | Der Quellstand ist eindeutig: Tag `hauptadresse-v8-2026-11-05` im Lernzentrum-Repository. |
| P05 | Keine neue Herleitung nötig: Die Definition des größten Unterschieds steht in Konzept 8.1 (von Claude in R3 und von Codex in X4 unabhängig hergeleitet). Der Auftrag verweist darauf und grenzt sie vom Unterschied nach festen 60 min ab. |
| P13 | WebKit nur ohne Eingriff in die vorhandene Chromium-Installation; die iPhone-Liste ist für die TL. |
| P22 | Keine eigene HTML-Fassung der Kurzkarte; die zugängliche Fassung ist die Website. |
| P24 | Die vollständige Anweisung steht in `simulation/X5_AUFTRAG.md`, in `AGENTS.md` nur ein Verweis, weil Codex `AGENTS.md` von selbst liest. |
