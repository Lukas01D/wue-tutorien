# Prüfauftrag: unabhängige Gegenprüfung der Aufgabensammlung

Stand 21.10.2026. Gilt für alle Prüfer. Arbeitsordner: `/home/claude/work/sammlung/`.

Du hast an dieser Sammlung nicht mitgeschrieben. Deine Aufgabe ist eine strenge, unabhängige Prüfung deines Teils, so wie ein kritischer Kollege am Lehrstuhl sie machen würde, bevor die Professorin die Aufgaben sieht. Eindeutige kleine Fehler korrigierst du direkt; alles, was eine fachliche oder didaktische Entscheidung braucht, meldest du nur.

## 1. Zuerst lesen

1. `SPEZ.md` (Struktur, Schreibweise, Zahlenregeln, verbindlich).
2. Das Musterbeispiel `teile/t5a_kaffee.md` (erzeugt von `rechnung/t5_kaffee_teil.py`).
3. Formelsammlung des Lehrstuhls (Text): `/home/claude/work/lehrstuhl/md/00_2026_Formelsammlung_final.md`.
4. Deine Teildateien, Rechenskripte, Skizzen-Skripte, Skizzen (PNG ansehen!) und Quellen (siehe Auftrag).

## 2. Was du prüfst

**A. Zahlen und Physik (wichtigster Punkt)**
- Rechenskript laufen lassen (`cd rechnung && python3 tN_rechnung.py`); die Selbstprüfung muss bestehen.
- Zusätzlich **unabhängig nachrechnen**: Rechne die Kernergebnisse jeder Aufgabe mit einem eigenen kurzen Python-Skript (im Scratch-Ordner) aus den Werten der Tabelle nach, ohne das Rechenskript zu benutzen. Prüfe Formeln gegen die Formelsammlung (richtige Korrelation und Gültigkeitsbereich, charakteristische Länge, Stoffwerte bei der richtigen Temperatur, Faktor 2 und π, Einheiten, ln-Argumente, Vorzeichen).
- Ist jede Teilaufgabe mit den gegebenen Größen und der Formelsammlung lösbar? Fehlt eine Größe, ist eine überbestimmt oder widersprüchlich (Text der Ausgangssituation vs. Tabelle vs. Ergebniszeile)?
- Rundung: Ergebniszeilen wie die Skriptausgabe; Folgeteile rechnen mit dem gerundeten oder ungerundeten Wert konsistent.

**B. Struktur (SPEZ Abschnitt 4)**
- Je L- und Z-Block: H2-Titel → Ausgangssituation (L 60 bis 150, Z 30 bis 90 Wörter) → Skizze mit „Abb. n:“ → Frage(n), zuerst Vorab-Frage → Aufgabe n (neu) → Annahmen → Gegebene Größen (Tabelle) → Aufgabenstellung a) … (höchstens neun Teile) mit Ergebniszeile am Ende jedes rechnenden Teils.
- Zusatzaufgaben am Ende des Tutoriums; Nummern der Fragen, Aufgaben, Abbildungen laufen je Tutorium richtig durch.
- Die Vorab-Frage wird durch eine Rechnung der Aufgabe beantwortet (sonst melden).

**C. Skizzen**
- Jede PNG in `grafik/` deines Teils ansehen (Read-Tool). Verrät die Skizze die Antwort einer Vorab-Frage oder eines Teils (Profilform, Ergebniswert, gesuchter Bilanzraum)? Passen Formelzeichen und Beschriftungen zur Tabelle? Rechtschreibung, Gedankenstriche, Lesbarkeit, „nicht maßstäblich“ wo nötig.
- Fehler korrigierst du im Skript `skripte/abb_….py` und erzeugst die Grafik neu (`cd skripte && python3 abb_….py`).

**D. Sprache und Schreibweise (SPEZ Abschnitt 5)**
- Deutsch, Sie-Form, klar. **Keine Gedankenstriche** (– oder —, auch nicht in Skizzen, Tabellen, Quellen), kein Bindestrich als Gedankenstrich.
- Dezimalkomma (`{,}` in Mathe), keine Tausenderpunkte, Einheiten aufrecht, °C als `\mathrm{°C}`, ϑ in °C und *T* in K, Index u für Umgebung, Kennzahlen kursiv, typografische Anführungszeichen „…“.
- Im Fließtext vor Zahlen ein echtes Minuszeichen (−, U+2212) statt Bindestrich („−30 °C“).
- Keine Lösungswege, keine Lernziel-Kennzeichen, keine Quellen im Aufgabentext (außer Kurzbeleg bei ausdrücklichem Literaturvergleich).

**E. Querverweise**
- Verweise auf andere Teile oder Tutorien („aus Tutorium 2, Teil e“, „Aufgabe 1 Teil c“) zeigen auf existierende Stellen mit denselben Zahlen. Andere Tutorien darfst du dafür lesen, aber nicht ändern.

**F. Quellen**
- Jeder Arbeitswert der Tabellen und jeder Fakt der Ausgangssituation hat einen Eintrag in `quellen/…_quellen.md` oder ist dort als Arbeitswert gekennzeichnet. Keine absoluten Pfade, keine Gedankenstriche, Links in `<…>`.

**G. Layout (zum Schluss)**
- Deinen Teil einmal bauen: `python3 build/teil_bauen.py teile/<datei>.md <scratch>/bilder` und die Seitenbilder ansehen. Melde oder behebe: Formeln über den Rand, Tabellen zu breit oder umbrechende Gruppenköpfe, verwaiste Zeilen, Ergebniszeilen, die als Liste gesetzt werden.

## 3. Regeln für Änderungen

- **Direkt korrigieren** (eindeutig, lokal): Tippfehler, Grammatik, Gedankenstriche, Schreibweise und Notation, falsche Nummern oder Querverweise, fehlende oder falsch gerundete Ergebniszeile (Wert aus der Skriptausgabe), Beschriftungsfehler in Skizzen, Quellenformat.
- **Zahlenfehler**: Wenn eine Zahl eindeutig falsch ist (Rechenfehler, falsche Formel), Rechenskript **und** Text gemeinsam korrigieren, Skript laufen lassen, bis die Selbstprüfung besteht. Im Bericht vorher/nachher angeben.
- **Nur melden, nicht ändern**: andere Arbeitswerte, Teile streichen oder hinzufügen, Aufgabe umbauen, Schwierigkeit ändern, alles Didaktische mit mehreren vertretbaren Lösungen. Mit einer klaren Empfehlung.
- Struktur und Reihenfolge der Bausteine nicht verändern. Keine Lösungswege ergänzen.
- `teile/t5a_kaffee.md` wird von `rechnung/t5_kaffee_teil.py` erzeugt: Änderungen dort nur im Skript vornehmen und das Skript neu laufen lassen. Die Kaffee-Aufgabe wurde bereits einmal unabhängig geprüft; prüfe dort vor allem die neuen Teile f bis h und den Versuch.
- Nur Dateien deines Teils ändern (siehe Auftrag). `build/`, `ausgabe/`, `SPEZ.md` und Dateien anderer Prüfer nicht ändern. `build/sammlung_bauen.py` nicht ausführen (andere Prüfer arbeiten parallel).
- Prüfbilder und eigene Nachrechnungen nur im Scratch-Ordner, der im Auftrag genannt ist.

## 4. Bericht

Schreibe `pruefung/bericht_<Kürzel>.md` (Deutsch, keine Gedankenstriche):

1. **Erledigte Korrekturen:** Tabelle `| Nr. | Datei, Stelle | vorher | nachher | Grund |`.
2. **Offene Entscheidungen:** nummerierte Liste; je Punkt Befund, Folgen, **Empfehlung** (eine klare).
3. **Unabhängige Nachrechnung:** je Aufgabe die Kernergebnisse (Text vs. eigene Rechnung), Abweichung.
4. **Geprüft ohne Befund:** kurze Liste, damit sichtbar ist, was abgedeckt ist.

Deine Schlussantwort an mich: höchstens 250 Wörter, mit der Zahl der Korrekturen, den drei wichtigsten Befunden und dem Pfad des Berichts.
