# Startprompt: Unabhängige Prüfung der Kaffee-Aufgabe

> In einen **neuen Chat im Projekt „Wärmeübertragung Tutorium“** das ZIP `Kaffee_Pruefpaket_2026-10-23.zip` anhängen und schreiben: **„Bitte führe die unabhängige Prüfung der Kaffee-Aufgabe durch. Folge genau der Datei 01_STARTPROMPT.md im angehängten Paket.“** Alternativ den Text ab der Linie einfügen.

---

Du koordinierst eine **unabhängige Prüfung der Aufgabe „Kaffee mit Milch“** (Tutorium 5, Aufgabe 1) für die Tutorien Wärmeübertragung. Sechs Prüfer mit getrennten Rollen und getrennten Materialien prüfen gleichzeitig und machen Änderungsvorschläge. Du bündelst sie zu einer Entscheidungsvorlage. **Umgesetzt wird erst, wenn ich (die Tutoriumsleitung) entschieden habe.**

Halte dich an die Schritte. Zwischen den Schritten schreibst du mir nur kurze Zwischenstände. Lies die Prüfmaterialien nicht vorab selbst ein, das ist Sache der Prüfer; du liest die Steuerdateien, später die Berichte und beim Bündeln gezielt das, was du zum Nachrechnen brauchst.

## Schritt 1: Paket bereitstellen

0. **Werkzeuge prüfen:** `which pandoc xelatex soffice node pdftoppm convert`, `fc-list | grep -ci carlito`, `python3 -c "import numpy, scipy, matplotlib"`, `node -e "require('docx')"`. Fehlendes im Zwischenstand nennen (für die Prüfung selbst reichen Python und `pdftoppm`; der Rest wird erst für die Umsetzung gebraucht). **Platz in der Projektablage:** Die Projekt-Info nennt `knowledge_size` und `max_knowledge_size`; für Berichte, Bündelung und Protokolle werden rund 60.000 gebraucht. Ist weniger frei, sag es mir im Zwischenstand und schlag vor, die Textfassung des Materials unter `claude/kaffee_pruefung/paket/material/` zu löschen (sie steckt vollständig im ZIP). Gelöscht wird erst nach meinem Ja.
1. Entpacke das angehängte ZIP in einen neuen, leeren Ordner `pruefung/` im Arbeitsverzeichnis. Darin liegt der Paketordner `Kaffee_Pruefpaket_2026-10-23/`.
   *Kein ZIP angehängt?* Frag mich zuerst danach. Nur wenn ich keins habe: Hol die Textfassung aus der Projektablage (`claude/kaffee_pruefung/paket/…`, gleiche Ordnerstruktur wie im ZIP) und erzeuge die PNG-Bilder der Kaffee-Aufgabe aus den SVG-Dateien. PDF, Word und die Bilder der Lehrstuhlunterlagen fehlen dann: Streiche fehlende Dateien aus `leseliste.json` im Paketordner, führe das Skript (Punkt 4) erneut aus und nenne die Lücken im Zwischenstand. Rolle G kann dann nur eingeschränkt prüfen.
2. Lies im Paketordner `02_PRUEFAUFTRAG.md`, `03_ROLLEN.md`, `04_BUENDELUNG.md` und `05_LESEVERTEILUNG.md`. Mehr nicht.
3. **Mein Feedback:** Öffne das Claude-Dokument „Kaffee mit Milch (Tutorium 5)“ (<https://claude.ai/artifact/LCRkwWobg2nv739T5XC73d>) mit den Docs-Werkzeugen (deren Anleitung vorher laden). Steht dort Text in [eckigen Klammern], schreib jede Anmerkung mit ihrer Stelle in `feedback_tutoriumsleitung.md` im Paketordner, geordnet unter „## Aufgabe“ und „## Lösung“. Kein Feedback oder kein Zugriff: ohne weiter, im Zwischenstand erwähnen.
4. **Rollenordner anlegen** (im Ordner `pruefung/`):
   `python3 Kaffee_Pruefpaket_2026-10-23/rollen_vorbereiten.py Kaffee_Pruefpaket_2026-10-23 arbeit`
   Das Skript kopiert je Rolle nur die Dateien ihrer Leseliste nach `arbeit/<Kürzel>/material/`, schreibt `arbeit/<Kürzel>/AUFTRAG.md` und legt `notizen/` an. Prüfe die Ausgabe: sechs Rollen (P, T, D, R, S, G) und die Zeile „Alle Dateien der Leselisten vorhanden“. Die erste Ausgabezeile („Rollenordner in …“) nennt den absoluten Pfad `<Rollenordner>`.

## Schritt 2: Sechs Prüfer starten

Starte alle sechs Prüfer **in einer einzigen Nachricht als Hintergrund-Agenten** (allgemeiner Agent, keine Modellvorgabe, also mit deinem Modell). Jeder bekommt nur diesen kurzen Auftrag, mit seinem Kürzel und dem absoluten `<Rollenordner>` aus Schritt 1:

> Du bist Prüfer `<Kürzel>` in einer unabhängigen Prüfung. Lies `<Rollenordner>/<Kürzel>/AUFTRAG.md` vollständig und arbeite genau danach. Arbeite nur in deinem Ordner `<Rollenordner>/<Kürzel>/`: keine anderen Ordner, keine Projektablage, keine Suche in früheren Chats, keine Erinnerungen, keine Claude-Dokumente. Schreib deinen Bericht nach `BERICHT.md` in deinem Ordner. Deine Schlussantwort hat höchstens 200 Wörter. Keine Gedankenstriche.

Wünsche ich nur einen Teil der Rollen, startest du nur diese, bündelst deren Berichte und nennst die fehlenden Rollen im Gesamturteil; Nachzügler ergänzt du später im Tab und im Protokoll.

Dann wartest du auf die Meldungen und machst nichts doppelt. Sobald ein Bericht fertig ist, legst du ihn in die Projektablage: `claude/kaffee_pruefung/ergebnisse/<Kürzel>_BERICHT.md` (so geht nichts verloren). Scheitert das Ablegen, weil die Projektablage voll ist, arbeitest du mit den Berichten im Arbeitsordner weiter und sagst es mir. Bricht ein Prüfer mit einem Fehler ab, startest du ihn einmal mit demselben Auftrag neu und sagst es mir.

*Kannst du keine Hintergrund-Agenten starten?* Sag es mir sofort und warte; dann gehen wir nach Abschnitt „Notfall“ in `00_ANLEITUNG.md` vor.

## Schritt 3: Bündeln

Wenn alle Berichte (`arbeit/<Kürzel>/BERICHT.md`) da sind, bündelst du sie nach `04_BUENDELUNG.md`. **Jede Zahlenbehauptung der Prüfer rechnest du selbst nach** (Rechenmodell im Paket unter `material/C_modell/`, vorher in einen eigenen Ordner kopieren), bevor du sie empfiehlst.

## Schritt 4: Vorlage zur Entscheidung und Protokolle

1. Lege die Vorlage als **neuen Tab „Änderungsvorschläge“** im Claude-Dokument an, in der Form aus `04_BUENDELUNG.md` (Anleitung der Docs-Werkzeuge zu Tabs und Auswahlfeldern vorher laden). Lege die Bündelung zusätzlich als `claude/kaffee_pruefung/ergebnisse/Buendelung.md` in die Projektablage.
2. **Protokolle jetzt eintragen** (nach `04_BUENDELUNG.md`, Abschnitt 4, und `umsetzung/protokolle_quelle/LIESMICH.txt`): KI-Protokoll K34 mit Abschnitt 3.7; Entscheidungsprotokoll G40, D88 und D89 auf „umgesetzt“; die Entscheidungen D93 ff. (Abschnitt 3.10) erst nach meiner Auswahl. Sind diese Nummern inzwischen vergeben (neuere Fassung in der Projektablage), die nächsten freien nehmen. Bauen, neue Seiten als Bild ansehen, die Markdown-Fassungen in der Projektablage ersetzen (`claude/KI-Protokoll_Tutorien_WUE.md`, `claude/Entscheidungsprotokoll_Tutorien_WUE.md`) und die geänderten Quelldateien (`*.js`) zusätzlich nach `claude/protokolle_quelle/` legen.
3. Schreib mir im Chat: Gesamturteil in drei Sätzen, die fünf wichtigsten Vorschläge, eine klare Empfehlung und wie ich entscheide.
4. **Halte dann an** und warte, bis ich schreibe, dass meine Entscheidungen eingetragen sind.

## Nach meiner Entscheidung (eigene Runde)

0. **Umgebung prüfen:** Gibt es `pruefung/Kaffee_Pruefpaket_2026-10-23/` noch? Wenn nicht: Bitte mich um das ZIP, entpacke es wie in Schritt 1, lege die Dateien aus `claude/protokolle_quelle/` über `umsetzung/protokolle_quelle/` und prüfe vor jedem Bau, dass das KI-Protokoll K34 und das Entscheidungsprotokoll G40 enthält. Die Berichte und die Bündelung liegen unter `claude/kaffee_pruefung/ergebnisse/`.
1. Lies meine Entscheidungen aus dem Tab (Spalten „Entscheidung“ und „Anmerkung“) und alles, was ich zusätzlich in [ ] geschrieben habe. Bei Unklarheiten fragst du nach, bevor du umsetzt.
2. **Umsetzen**, nur was ich angenommen habe, im Ordner `umsetzung/Arbeitsordner/`, in dieser Reihenfolge:
   a) **Rechenmodell:** `kaffee/kaffee_modell.py` ändern und nach `sammlung/rechnung/kaffee_modell.py` kopieren (beide gleich); `cd kaffee && python3 nachrechnung_kaffee.py > nachrechnung_kaffee_ausgabe.txt`.
   b) **Aufgabentext** nur in `sammlung/rechnung/t5_kaffee_teil.py` (Variable `md`), dann `python3 sammlung/rechnung/t5_kaffee_teil.py` (schreibt `sammlung/teile/t5a_kaffee.md`, aus dem Blatt und Sammlung gebaut werden).
   c) **Lösung und Hinweise** nur in den Blöcken `LOESUNG` und `HINWEISE` von `kaffee/build_kaffee.py`; geänderte Quellen auch in `sammlung/quellen/t5a_kaffee_quellen.md`.
   d) **Abbildungen:** Abb. 1 mit `python3 sammlung/skripte/abb_t5_kaffee.py` (schreibt `sammlung/grafik/t5_kaffee_tassen.*`); Abb. L1 und L2 mit `python3 kaffee/abb_loesung.py` (schreibt nach `kaffee/grafik/`). `kaffee/abb_kaffee.py` wird nicht mehr gebraucht.
   e) **Stand-Datum** auf heute setzen: Kopfzeile in `kaffee/build/kopf.tex` und `sammlung/build/kopf.tex`, `NAME` und `STAND` in `sammlung/build/sammlung_bauen.py`, Text „Stand …“ in der Kopfzeile von `kaffee/build/referenz_lehrstuhl.docx` und `sammlung/build/referenz_sammlung.docx` (Datei `word/header*.xml` im ZIP der Word-Datei).
   f) **Bauen:** `python3 kaffee/build_kaffee.py`, dann `python3 sammlung/build/sammlung_bauen.py sammlung/ausgabe`. Alle geänderten Seiten (PDF und Word) als Bild prüfen.
3. **Claude-Dokument nachziehen** (Tab mit der Aufgabe), Protokolle fortschreiben (D93 ff. mit meinen Entscheidungen, Umsetzung als K35), bauen und wie in Schritt 4 sichern.
4. **Zweite Runde Rolle S** mit der neuen Fassung. Im Ordner `pruefung/` die neuen Dateien ins Paket legen und einen **neuen** Arbeitsordner anlegen (nicht `--neu`: das löscht alle Berichte unter `arbeit/`):
   ```
   A=Kaffee_Pruefpaket_2026-10-23/umsetzung/Arbeitsordner; M=Kaffee_Pruefpaket_2026-10-23/material
   cp $A/kaffee/Kaffee_Aufgabe.pdf $A/kaffee/Kaffee_Aufgabe.docx $M/A_aufgabe/
   cp $A/sammlung/grafik/t5_kaffee_tassen.png $M/A_aufgabe/Abb1_Tassen.png
   cp $A/sammlung/grafik/t5_kaffee_tassen.svg $M/A_aufgabe/Abb1_Tassen.svg
   sed 's#grafik/t5_kaffee_tassen.png#Abb1_Tassen.png#' $A/kaffee/Kaffee_Aufgabe.md > $M/A_aufgabe/Kaffee_Aufgabe.md
   cp $A/kaffee/Kaffee_Loesung.pdf $A/kaffee/Kaffee_Loesung.docx $A/kaffee/grafik/AbbL1_Bilanzraum.* $A/kaffee/grafik/AbbL2_Temperaturverlauf.* $M/B_loesung/
   sed 's#grafik/t5_kaffee_tassen.png#../A_aufgabe/Abb1_Tassen.png#; s#grafik/AbbL#AbbL#g' $A/kaffee/Kaffee_Loesung.md > $M/B_loesung/Kaffee_Loesung.md
   cp $A/kaffee/kaffee_modell.py $A/kaffee/nachrechnung_kaffee.py $A/kaffee/nachrechnung_kaffee_ausgabe.txt $M/C_modell/
   mv Kaffee_Pruefpaket_2026-10-23/feedback_tutoriumsleitung.md Kaffee_Pruefpaket_2026-10-23/feedback_runde1.md 2>/dev/null
   python3 Kaffee_Pruefpaket_2026-10-23/rollen_vorbereiten.py Kaffee_Pruefpaket_2026-10-23 arbeit_runde2
   ```
   Starte dann nur S mit `<…>/arbeit_runde2/S/AUFTRAG.md` (Auftrag wie in Schritt 2) und zeig mir das Ergebnis.
5. **Übergabe:** Gib mir die neuen Dateien im Chat (Kaffee-Blatt und Lösung als PDF und Word, Sammlung als PDF und Word, Protokolle als Word und PDF). Ersetze in der Projektablage `claude/Kaffee_Aufgabe_Tutorium5_2026-10-21.md` (Inhalt von `kaffee/Kaffee_Loesung.md` mit einer Kopfzeile zum Stand) und `claude/Aufgabensammlung_Tutorien_WUE_2026-10-21.md` (Inhalt der neuen Sammlung als Markdown ohne die Steuerblöcke für LaTeX und Word). Gib mir zum Schluss den neuen Arbeitsstand als ZIP `Arbeitsstand_Kaffee_<JJJJ-MM-TT>.zip` (Inhalt: `umsetzung/Arbeitsordner/` und `umsetzung/protokolle_quelle/`), damit er in den Werkzeugkasten für künftige Aufgaben übernommen werden kann.

## Regeln

Deutsch. Keine Gedankenstriche (– oder —), stattdessen Komma, Punkt, Doppelpunkt oder Klammern. Sparsam lesen. Nichts an andere senden. Änderungen an meinen Texten kennzeichnen. Bei Entscheidungen eine klare Empfehlung geben; entscheiden tue ich.
