# X5: Nachprüfung der Korrekturrunde

Geprüft am 06.11.2026, Rolle X5, unabhängig vom Bau durch Claude.
Grundlage ist `X5_AUFTRAG.md`, Abschnitt 9, mit `X5_ANTWORT.md`, den
Entscheidungen F1 bis F14 und Q1 bis Q7 in `KONZEPT.md` 12.1,
`ZUSTAENDE.md` und der Zusammenführung der Runde 4.

## Urteil

**Abnahmefähig mit Änderungen.** Alle elf ursprünglichen Befunde X5-01 bis
X5-11 sind in den nachgeprüften Fällen behoben. Die Entscheidungen zu den
Texten und Sperren sind in Deutsch und Englisch umgesetzt; die Beameransicht
besteht bei beiden verlangten Fenstergrößen. Die eigene Rechnung bestätigt
die Zahlen und die neue Begründung von V1.

Ein neuer **low**-Befund X5N-01 betrifft die zu pauschale Aussage im Baubericht,
der angeheftete Bereich bleibe stets unter 45 Prozent. Beim Schriftwechsel
gibt es eine kurze Überschreitung, bevor sich das Diagramm automatisch löst.
Der Nachweis soll zwischen Übergang und stabilem Zustand unterscheiden.
Ein weiterer blocker-, high- oder medium-Befund wurde nicht gefunden.

Das Urteil gilt für den betroffenen Umfang in Chromium. Die schon offenen
Nachweise mit echten Geräten, Bildschirmlesern und Studierenden bleiben offen.
Die Gestaltung wurde gemäß Entscheidung der TL beibehalten.

## Geprüfter Stand und Umgebung

| Punkt | Nachweis |
|:--|:--|
| Ausgangszweig | `claude/simulation-tool-kaffee-4kcacl`, von `origin` geholt |
| Geprüfter Commit, vor eigenen Änderungen festgestellt | `34bdfa6e996010ebfb9073b8062aa3eb72434cda` |
| Letzte Änderung der Seite | `6077a925ae7b98437b9715338b31193ee51588c2` |
| Eigener Zweig | `codex/x5-nachpruefung` |
| Artefakte | `site/index.html` und `site/Kaffee_Simulation.html`, bytegleich |
| SHA-256 beider Artefakte | `e6f95ca27a5c508344e6802195e9ea62f07ad743694761198057da98e757cc1d` |
| MODELL-Block, unverändert | `b32e3f9db9f82b09bfc0e300388ffbef72f875cec65540da668d765389f97d24`, aus dem fertigen Artefakt extrahiert und geprüft |
| Wiederholbarer Bau | `PYTHONPATH=/tmp/x5-python python3 simulation/site/bauen.py --pruefen`: **gleich** |
| Laufzeit | Linux, Python 3.12.14, Node 24.19.0, Playwright 1.62.0, Chromium 154.0.8037.57 |
| Prüfabhängigkeiten | fontTools 4.61.1, Brotli 1.2.1 in `/tmp/x5-python`, axe-core 4.11.0 in `/tmp/x5-tools` |

**Entscheidung der TL vom 06.11.2026:** Die Grenze von 450 000 Bytes ist
ersatzlos aufgehoben. Die Dateigröße wurde weder als Prüfkriterium noch als
Grund für einen Befund verwendet. Historische Grenzangaben im Bauauftrag
und im Baunachweis sind für diese Nachprüfung überholt. Der Bauvergleich
wurde zur Prüfung der identischen Ausgabe ausgeführt.

Geändert wurden ausschließlich dieser Bericht und eigene Prüfdateien unter
`x5n_skripte/`. Die vier ursprünglichen Skripte aus `x5_skripte/` wurden
bytegleich in den eigenen Ergebnisordner kopiert und dort ausgeführt.
Ihre SHA-256-Werte sind in `x5n_skripte/auswertung.json` festgehalten.
Alte Belege wurden nicht überschrieben. Wichtig für die Provenienz:
`pruefung_a.py` schreibt den alten Commit `da7deb1…` fest in seine JSON-Datei.
Dieser unveränderte Text ist kein ermittelter Laufstand. Für den neuen Lauf
gelten die oben geprüften Artefakthashes und `auswertung.json`.

Nicht erneut bewertet wurden unberührte Teile und Gestaltungsentwürfe.
Vergleichsaufrufe des unveränderten Altskripts benötigen lokal das Lernzentrum
v8, Tag `hauptadresse-v8-2026-11-05`, Commit
`c2af968fab5c883a52d8323771b7eebb5a969373`; es wurde nur unter `/tmp` gelesen.
Eine neue Gestaltungsabnahme wurde daraus nicht abgeleitet.

## A: Zahlen, Fachtexte und ursprüngliche Befunde

Die eigene Bilanzrechnung importiert kein Projektmodell. Sie verwendet die
Mischbilanz und die exponentielle Lösung von `C dT/dt = -kA (T - Tu)`.
Der erneute Lauf umfasst **441 Parametersätze und 23 814 Vergleiche**,
darunter 400 reproduzierbare Zufallssätze. Keine Abweichung überschreitet
die vorab festgelegten Toleranzen (absolut 1e-8, relativ 1e-9).
Die größte absolute Abweichung beträgt 1,15e-9.
Alle **76 Zahlentokens der Auflösungen** bestehen in DE und EN.

Zusätzlich wurden 3 872 tatsächlich gezeichnete Kurvenpunkte gegen diese
Rechnung geprüft. Größte Abweichung: 0,0913 SVG-Einheiten bei einer Grenze
von 0,2 einschließlich der Rundung von Achsen und Punktkoordinaten.

### Nachgerechnete Zahlen

| Größe oder Fall | Eigene Rechnung | Seite bzw. Auflösung | Urteil |
|:--|--:|:--|:--|
| Standard, Temperaturen | 34,046483 / 30,193282 °C | 34,05 / 30,19 °C | stimmt |
| Standard, Unterschied | 3,853201 K | 3,85 K | stimmt |
| Standard, Q1 / Q2 | 34,880847 / 38,571235 kJ | 34,88 / 38,57 kJ | stimmt |
| Mischtemperatur / kA | 70,466209 °C / 0,340247765 W/K | 70,47 °C / 0,3402 W/K | stimmt |
| Maximum ohne Becher | 55,744669 min, 3,861838 K | etwa 56 min, 3,86 K | stimmt |
| Deckel, Maximum / Unterschied bei 60 min | 99,54405 min / 3,509635 K | etwa 100 min / 3,51 K | stimmt |
| Becher, kA aus Messung | 0,444031471 W/K, 3,078831 K | 0,4440 W/K, 3,08 K | stimmt |
| Becher, Energiedifferenz geteilt durch C_GB | 3,733840 kJ / 1212,746 J/K = 3,078831 K | C_GB in beiden erläuternden Gleichungen, DE und EN | stimmt |
| V1, Milch für gleiche Endtemperaturen nach 30 min | 60,912266 °C | 60,9 °C, EN 60.9 °C | stimmt |
| V1, Milch für gleiche Endtemperaturen nach 60 min | 47,003093 °C | 47,0 °C, EN 47.0 °C | stimmt |
| V1, Milch für gleiche Endtemperaturen nach 90 min | 37,284502 °C | 37,3 °C, EN 37.3 °C | stimmt |
| V1, Q1 = Q2 bei diesen drei Milchtemperaturen | 26,049992 / 38,571235 / 44,589720 kJ | neue Begründung Q2 | stimmt |
| V4, kA von Tasse 1 bei 105 Prozent | 2,983093 K | 2,98 K | stimmt |
| V5, Thermobecher offen nach 30 min | 63,467111 °C | 63,5 °C | stimmt |

Bei V1 wurde die nötige Milchtemperatur unabhängig durch Nullstellensuche
bestimmt. Bei gleicher Milch in beiden Tassen entfällt ihr Beitrag aus der
Differenzbilanz. Für gleiche Endtemperaturen muss somit Q1 = Q2 gelten.
Die drei Nachrechnungen bestätigen außerdem die sinkende nötige
Milchtemperatur bei späterer Zugabe. Die Erklärung Q2 trägt die Zahlen.

### Abschluss der elf ursprünglichen Befunde

Alle Belegpfade in den folgenden Tabellen beziehen sich auf `x5n_skripte/`.

| Alter Befund | Ergebnis | Eigener Beleg |
|:--|:--|:--|
| X5-01, Ergebnis von V3 vor der Vorhersage | behoben | Alte Reproduktion `V3_Antwort_vor_Vorhersage` PASS. Zusätzlich V1 bis V5 jeweils mit bereits eingestellter Bedingung geöffnet: Rückkehr zu den Standardwerten, sichtbarer Hinweis und Ansage, Vorhersage weiterhin offen. `ergebnis_nachpruefung.json`, `Sperren_V1_V5`, DE und EN. |
| X5-02, fehlende Becherwärmekapazität | behoben | Beide Gleichungen und Lesehilfe unterscheiden C_G und C_GB; gerenderte MathML-Indizes in beiden Sprachen geprüft. Zahlengegenprobe in der Tabelle. `F3_F12_Q2_Q7`, `ergebnis_ergaenzung.json`, `energy_formula`. |
| X5-03, kA-Quelle und Messwert | behoben | 66,5 °C bleiben separat gespeichert, Ersatzwert 70,144996 °C eindeutig als berechnet bezeichnet; nach Neuladen kann die echte Messung wieder verwendet werden. Unzulässiger Wechsel wird mit sichtbarer und nach 250 ms vorgesehener Live-Meldung abgelehnt; Quelle, kA und Ergebnis unverändert. `X5_03`, DE und EN. |
| X5-04, verdeckter Fokus | behoben | 0 verdeckte Fokusmitten im Layoutlauf sowie in der zusätzlichen Rückwärtsfolge bei 768 × 1024 und 32 px. `ergebnis_layout.json`, `ergebnis_ergaenzung.json`. |
| X5-05, Überlauf und verschwindende Regler | behoben | 108 Layoutzustände einschließlich 200 Prozent Grundschrift, 0 Seitenüberläufe und 0 zu kleine Ziele. Regler bleiben bedienbar; Bildschirmfotos angesehen. `ergebnis_layout.json`. |
| X5-06, fehlender Schnitttext | behoben | 0 unbeschriftete vorhandene Schnittkreise in 72 Fällen des unveränderten Skripts. Weitere 126 Zustände bei 320, 360 und 390 px, DE und EN, ohne überlappende nichtnumerische Diagrammtexte, einschließlich Trinklinie und warmer Milch. `labels`, `Beschriftungen_Q3`. |
| X5-07, Nachkommastellen im Kurslink | behoben | Mehr als zwei Stellen werden sichtbar abgelehnt; angenommene Werte überstehen den Link unverändert. Alte Reproduktion PASS, Feldname und Fehlerbezug zusätzlich geprüft. `ergebnis_b.json`, `ergebnis_bedienung.json`. |
| X5-08, deutsche Fehlermeldung auf Englisch | behoben | Alte Reproduktion PASS; aktuelle Einstellungsfehler werden übersetzt, fremde Links erhalten den Grund in der gewählten Sprache. Die gleiche Schlüsselmenge umfasst 380 Texte pro Sprache, ohne Gedankenstriche und offene Platzhalter. |
| X5-09, verkleinerte Diagrammschrift | behoben | In der zusätzlichen Handyprobe kleinster tatsächlicher Text etwa 10,99 px; ursprünglicher Layoutlauf mindestens 9,90 px über alle Breiten einschließlich großer Grundschrift. Die alten Werte unter 7 px treten nicht mehr auf. Bilder `P2_360x640_de.png`, `VT_390x844_de.png` angesehen. |
| X5-10, zu hoher angehefteter Bereich | behoben im stabilen Zustand, Nachweis präzisieren | 379,75 px bei 844 px Fensterhöhe (44,99 Prozent), konstant bei sieben Zugabezeiten. Bei Platzmangel nach Schriftwechsel gelöst. Kurzer Übergang siehe X5N-01. |
| X5-11, fremdes Fragment | behoben | Alte Reproduktion PASS; fremdes Format wird gemeldet und entfernt, eigene Sprunganker bleiben zulässig. Link-Rückfrage, Ablehnen und Rückimport unverändert funktionsfähig. `ergebnis_b.json`. |

**Einordnung des unveränderten Quellenwechseltests:** `pruefung_b.py`
liefert 19 PASS und einen ERROR bei `Quellenwechsel_haelt_Kurven_bei_kA1`.
Playwrights `check()` erwartet ein bleibendes Häkchen bei „aus der Messung“.
Die Seite setzt es wegen des unzulässigen Ersatzwerts von 21,90 °C zurück.
Das entspricht ausdrücklich der vorgeschlagenen Ablehnung in X5-03.
Der ergänzende Test verwendet einen normalen Klick und prüft genau diese
Ablehnung einschließlich Fokus, Meldungsbezug, Live-Ansage und unveränderter
Kurven. Er besteht in beiden Sprachen. Der ERROR wurde im alten Lauf belassen
und weder als PASS gezählt noch als Produktfehler interpretiert.

## B: Geänderte Bedienung und Texte

Die ergänzenden eigenen Prüfungen bestehen mit **19 von 19** Fällen in
`nachpruefung.py` und **8 von 8** Fällen in `bedienung.py`.

### Betroffene Muss-Anforderungen

| ID | Ergebnis der Nachprüfung | Beleg |
|:--|:--|:--|
| M-1 | erfüllt | MODELL-Hash, eigene Rechnung, C_GB-Texte und Trennung des Ersatzwerts von der Messung |
| M-3 | erfüllt | P0 in DOM, Barrierefreiheitsbaum und Live-Regionen, Q1 vor und nach Frage 1, neutrale Ausgangslagen V1 bis V5 |
| M-6 | erfüllt im stabilen Zustand; X5N-01 zum Nachweis | Beamerbilder und Rechtecke unten; Anheften, Fokus und Zeitreihen |
| M-11 | erfüllt in den geprüften Zuständen | 72 Schnittproben und 126 zusätzliche Beschriftungszustände, Ersatzlegende bei Platzmangel |
| M-13 | erfüllt | 0 zu kleine Ziele im Layoutlauf, nutzbare Felder bei 200 Prozent Text |
| M-14 | erfüllt | 0 Überläufe bei 320 bis 1920 px und 200 Prozent Text |
| M-19 | erfüllt für den betroffenen Umfang | DE/EN-Läufe, Fehlermeldung, 380 Textschlüssel, Dezimalformate |
| M-21 | erfüllt | Link hin und zurück, Ablehnen ohne Änderung, beschädigte und fremde Links, zwei Nachkommastellen, Bestätigung und Fokus |
| M-22 | erfüllt für die geänderten Texte | F12 und Q2/Q3 mit eigener Energie- und Teilflächenrechnung, Becher in Lesehilfe und Rechenweg |

### Entscheidungen und ergänzte Abläufe

| Entscheidung | Ergebnis und eigener Beleg |
|:--|:--|
| F3/F6, Q1 | Starttext nennt die Energieaussage des Mitbewohners. Startauflösung enthält die Erhaltung von Kaffee, Milch und Raum. „bis etwa 56 min“ ist vor der Vorhersage zu Frage 1 nicht enthalten und erscheint danach, DE und EN. `Q1_F4_F11`. |
| F4 | Frage 1 ist zunächst offen; „wieder kleiner“ steht erst nach dem Festhalten im Prüfauftrag. `Q1_F4_F11`. |
| F5/F10 | Wortlaut von Frage 2 unterscheidet vorhandene und fehlende Kurswerte. Übernahme beim Prüfen, Auflösung weiterhin offen auf die eigene Messung bezogen. Alter Pflichtweglauf und `F3_F12_Q2_Q7`. |
| F8, Q4 | Abschluss erscheint nach geöffneter Auflösung von Frage 2 und enthält ausdrücklich „kalte Milch“ bzw. „cold milk“. `F3_F12_Q2_Q7`. |
| F9, Q5 | V1, V3, V5 enthalten „Notiert euch dazu“ und die entsprechende englische Aufforderung; V4 nennt die Regler und 105 Prozent; V5 kennzeichnet die Richtwerte. Sichtprüfung der Texte und eigener Fragenlauf. |
| F11 | Modell und Code bleiben vor der Startvorhersage gesperrt; Aussagen zum Verhalten am Schnitt erscheinen erst nach der Vorhersage zu Frage 1. Alte P0-Prüfung und `Q1_F4_F11`. |
| F12, Q3 | Wärmekapazitäten, Standardwertbedingung, Bezeichnungen der Schnitte, τ etwa 41 min, Faktor 0,56 und Verweis auf die Wärmestromansicht geprüft. Allgemeine Aussagen verwenden die Richtung der Wärmeabgabe. Umgekehrte Teilflächen mit 400 ml, kA1 bei 110 Prozent und 180 min unabhängig nachgerechnet. `F3_F12_Q2_Q7`, `Beschriftungen_Q3`. |
| Q2 | Neue V1-Erklärung in beiden Sprachen, Gleichheit Q1 = Q2 und Abhängigkeit vom Zugabezeitpunkt eigenständig bestätigt. Zahlen oben. |
| Q6 | V1 nennt nach dem Festhalten den Milchtemperaturregler. Bestätigtes „ohne Vorhersage aufdecken“ öffnet die Auflösung sofort und verwendet den Erklärauftrag ohne Rückfrage nach einer eigenen Vorhersage. `F3_F12_Q2_Q7`. |
| Q7 | „Ferreira 2025“ in beiden Sprachen, ohne Buchstabenzusatz. `F3_F12_Q2_Q7`. |

Die korrigierte Kurslinkbestätigung bleibt im eigenen Lauf auch nach 16 s
stehen. „Hinweis schließen“ setzt den Fokus auf `frage-titel`.
Nach erneutem Anheften ist der Knopf nicht verdeckt; ein zweiter Tipp nach
600 ms löst bei V3 kein „Zurück“ aus. Die Anhefthöhe bleibt bei sieben
Zugabezeiten konstant. Belege: `ergebnis_bedienung.json`.

Die neu eingeführten Nachkommastellenfehler nennen das Feld und sind durch
`aria-describedby` zugeordnet. Ein Sprachwechsel zeichnet das Messblatt wie
zuvor aus den gültigen Daten neu: Ein nicht angenommener Rohwert verschwindet
zusammen mit seinem Fehler, der letzte gültige Wert wird wieder angezeigt.
Das wurde ausdrücklich als Rücknahme einer ungültigen Eingabe geprüft,
nicht als Übersetzung einer weiterhin sichtbaren Fehlermeldung ausgegeben.

### Beamer und angesehene Bilder

In **DE und EN** liegen nach der Startvorhersage Frageleiste und vollständiges
Diagramm im Fenster. Nach Frage 1 liegt zusätzlich der ganze Zugaberegler
im Fenster. Gemessen nach dem von der Seite selbst ausgeführten Scrollen:

| Fenster | Nach Start: Diagramm oben bis unten | Nach Frage 1: Diagramm oben bis unten | Zugaberegler unten |
|:--|:--|:--|--:|
| 1280 × 720 | 415,70 bis 667,70 px | 344,22 bis 586,22 px | 686,11 px |
| 1366 × 768 | 415,70 bis 715,70 px | 344,22 bis 634,22 px | 734,11 px |

Beleg: `ergebnis_nachpruefung.json`, `Beamer`, acht Bildschirmfotos
`bilder/beamer_*`. Angesehen wurden insbesondere die beiden Zustände bei
1280 px in DE, die entsprechende EN-Ansicht sowie Handy-, Formel- und
vergrößerte Schriftansichten. Die vollständigen Screenshots zeigen auch die
weiteren Elemente; die Prüfung verlangt nicht, dass sämtliche Energiesäulen
nach der Startvorhersage zugleich vollständig ins Fenster passen.

## Befunde nach Schwere

| ID | Schwere | Befund | Beleg | Vorschlag |
|:--|:--|:--|:--|:--|
| X5N-01 | low | **Nachweis zur 45-Prozent-Grenze unterscheidet den Schriftwechsel nicht vom stabilen Zustand.** `BAU_BERICHT.md`, Nachweistabelle M-6 und Antwort zu X5-10 nennen 0 Überschreitungen bzw. höchstens 44,8 Prozent. Der unveränderte eigene Layoutlauf misst einmal 49,49 Prozent bei 390 × 844, EN und 200 Prozent Text. Die gezielte Zeitreihe zeigt unmittelbar nach der Schriftänderung 457,25 px bei 844 px (54,18 Prozent), anschließend automatische Lösung; ab 120 ms bis 2 s bleibt der Bereich gelöst. Die stabile Bedienung und der frühere dauerhafte Fehler sind damit unterschiedlich zu bewerten. | `ergebnis_layout.json`, `VT_200prozent_Text`, EN; `auswertung.json`, `transient_over_45_percent`; `ergebnis_bedienung.json`, `200prozent_zeitverlauf`, DE und EN. | Nachweistabelle und X5-Antwort auf den stabilen Zustand mit dokumentierter Wartebedingung beziehen und den Übergang nennen. Den ergänzenden Zeitverlauf als Beleg beifügen. Falls die Grenze auch während jedes Übergangs gelten soll, den Bereich beim Schriftwechsel zuerst lösen und erst nach der Neuberechnung wieder anheften. |

Schwere low: Der Übergang wurde gezielt durch eine Schriftänderung ausgelöst;
die Seite korrigiert ihn selbst. In den stabilen Zuständen war daraus weder
ein dauerhafter Überlauf noch ein verdeckter Fokus reproduzierbar.

## Grenzen und offene externe Nachweise

Die geänderten Abläufe wurden mit Chromium und simulierten Fenstergrößen
geprüft. Echtes iPhone/Safari, Android, WebKit, VoiceOver, TalkBack, echte
Bildschirmtastatur, nativer Browserzoom sowie der Probelauf mit zwei
Studierenden und die Lesbarkeit im Hörsaal wurden hier nicht nachgewiesen.
Eine CSS-Grundschrift von 200 Prozent ersetzt keinen nativen Zoomtest.

Der eigene neue `file:`-Versuch wird mit `ERR_BLOCKED_BY_ADMINISTRATOR`
verhindert (`file_probe.json`). Die unveränderten Bytes bestehen dagegen den
Offline-Lauf über eine lokale Playwright-Route im frischen Profil; die CSP
blockiert fremdes Inline-Skript. In den ergänzenden Seitenläufen wurden
keine externen Seitenanfragen oder JavaScript-Fehler beobachtet. axe-core
meldet in den vier alten Prüfzuständen keine Verstöße, pro Zustand bleibt
eine manuelle Prüfung offen. Das ersetzt keinen echten Bildschirmleser.

F13 (Vorabmessung der TL), der Probelauf und die bekannte spätere Empfehlung
G1-R4-13 bleiben außerhalb dieser Korrekturrunde offen. Es wurde nichts
veröffentlicht und kein Pull Request angelegt.
