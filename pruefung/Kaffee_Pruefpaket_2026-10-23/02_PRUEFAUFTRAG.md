# Gemeinsamer Prüfauftrag: Kaffee-Aufgabe für Tutorium 5

Die Abschnitte 1 bis 4 gelten für alle sechs Prüferinnen und Prüfer. Deine Rolle, dein Material und deine Pfade stehen in deinem `AUFTRAG.md` in den Abschnitten 5 bis 7. (Platzhalter in geschweiften Klammern wie `{ORDNER}` setzt `rollen_vorbereiten.py` ein.)

## 1. Worum es geht

Ein studentischer Tutor (die **Tutoriumsleitung**) gestaltet die acht Tutorien zur Vorlesung **Wärmeübertragung** neu. Vorlesung, Übung und Klausur verantwortet Prof. Dr. Julia Riese, Lehrstuhl für Fluidverfahrenstechnik, Universität Paderborn (Bachelor, Maschinenbau und verwandte Studiengänge). Eine Tutoriumssitzung dauert vermutlich 90 Minuten; nimm das als Annahme.

**Tutorium 5** heißt „Wärmebilanzen (instationär global)“. Die Aufgabe **„Kaffee mit Milch“** ist dort als Aufgabe 1 vorgesehen: Zwei gleiche Tassen Kaffee kühlen eine Stunde lang ab; in Tasse 1 kommt die kalte Milch sofort, in Tasse 2 erst nach 60 Minuten. Welche ist am Ende wärmer, und trägt das Argument „Die Energie bleibt erhalten, also ist es egal“? Dazu kommen ein Becher mit Wärmekapazität (Teil f), Milchschaum (Teil g), eine Zusatzfrage (Teil h) und ein Versuch im Tutorium.

Die Aufgabe ist ein **Entwurf**. Zahlen und Rechnung wurden schon zweimal gegengeprüft. Jetzt geht es um **Verbesserungen**: Ist die Aufgabe sinnvoll, lehrreich, fachlich sauber, im Tutorium machbar und passend zum Lehrstuhl? Deine Aufgabe ist, sie aus deiner Rolle heraus kritisch zu prüfen und **konkrete Änderungsvorschläge** zu machen. Du setzt nichts selbst um; die Tutoriumsleitung entscheidet.

## 2. Vorgaben

Diese Vorgaben gelten. Hältst du eine davon für falsch, schreib das als eigenen Vorschlag mit dem Vermerk **„Vorgabe in Frage gestellt“** und begründe es.

- **Struktur wie am Lehrstuhl:** Ausgangssituation mit Skizze, dann Frage(n) mit einer Vorab-Frage zuerst, dann die Aufgabe mit Annahmen, gegebenen Größen als Tabelle und Teilen a), b), …; das Ergebnis steht am Ende jedes rechnenden Teils. Minimalistisch, nicht zu komplex, aber didaktisch fordernd.
- Differentialgleichungen werden durch **Trennung der Variablen** gelöst, nicht mit dem Lösungsschema aus Kapitel 5 der Formelsammlung.
- Auf dem Blatt stehen **keine Lernziele**; die Lösung ist ein eigenes Dokument. **Plausibilitätsprüfungen** und das **Aufstellen und Begründen von Annahmen** sind gewollt.
- Schreibweise: Deutsch, Sie-Form, keine Gedankenstriche (– oder —), Dezimalkomma, ϑ in °C und *T* in K, Index u für Umgebung.

## 3. Regeln

1. **Nur dein Material:** Nutze nur die Dateien in deinem Ordner `{ORDNER}` und, soweit erlaubt, Websuchen. Keine anderen Ordner (auch nicht die der anderen Rollen), keine Projektablage, keine Suche in früheren Chats, keine Erinnerungen, keine Claude-Dokumente. Liegt ein Unterordner `material/erst_nach_eigener_rechnung/` vor, öffnest du ihn erst, wenn dein eigener Durchgang fertig ist.
2. **PDF-Dateien als Bild ansehen** und alles, was dabei entsteht, nur unter `{ORDNER}/notizen/` ablegen, je Datei mit eigenem Präfix, zum Beispiel `pdftoppm -r 80 -png {ORDNER}/material/A_aufgabe/Kaffee_Aufgabe.pdf {ORDNER}/notizen/aufgabe` (ergibt `aufgabe-1.png`, …). Die Markdown-Fassungen daneben sind zum Nachlesen von Text und Zahlen da. Word-Dateien rendern, wenn deine Rolle das Aussehen prüft: `soffice --headless --convert-to pdf --outdir {ORDNER}/notizen/word {ORDNER}/material/A_aufgabe/Kaffee_Aufgabe.docx`. **Nie ohne `--outdir` und nie im Ordner `material/` umwandeln:** Die gleichnamige PDF dort würde überschrieben.
3. **Websuchen** nur bis zu deiner Obergrenze (Abschnitt 7). Zitiere nur Quellen, die du geöffnet hast, mit Link; kennzeichne, was du nur aus einem Suchtreffer oder aus dem Gedächtnis weißt.
4. **Zahlen selbst nachrechnen**, bevor du eine Zahl behauptest (Python mit numpy und scipy ist vorhanden). Rechenskripte aus dem Material kopierst du vorher nach `{ORDNER}/notizen/` und startest sie dort (ohne `-I`, damit sie ihre Nachbarmodule finden). Eigene Skripte, Bilder und Notizen nur in `notizen/`.
5. Ändere nichts am Material. Du schreibst nur `BERICHT.md` und Dateien in `notizen/`.
6. Deutsch, klar, keine Gedankenstriche.
7. **Konzentriere dich auf deine Rolle;** die anderen Rollen decken ihre Blickwinkel ab. Klare Fehler außerhalb deiner Rolle meldest du kurz mit, als eigenen Vorschlag mit Ebene und Priorität.
8. **Arbeite zügig,** etwa 30 bis 40 Minuten. Lies nur, was du für deine Prüffragen brauchst.

## 4. Bericht

Schreibe `BERICHT.md` in deinem Ordner mit diesen Abschnitten (Rolle S zusätzlich ein „Protokoll je Teil“ vor Abschnitt 2, Rolle R ihre Wertetabelle als Abschnitt 2a):

1. **Gesamturteil** (drei bis fünf Sätze): Was ist stark, was ist das größte Problem, wie einsatzbereit ist die Aufgabe?
2. **Änderungsvorschläge**, nach Priorität geordnet, je Vorschlag in dieser Form (Nummern mit deinem Präfix: {PRAEFIX}1, {PRAEFIX}2, …):

   **{PRAEFIX}1: kurzer Titel**
   - Ebene: didaktisch, technisch, inhaltlich (Sinn, Relevanz, Umfang), sprachlich, praktisch (Durchführung) oder gestalterisch
   - Stelle: Aufgabe oder Lösung, Abschnitt oder Teil
   - Befund: was genau das Problem oder die Chance ist
   - Vorschlag: konkret, wo möglich mit neuem Wortlaut oder neuen Zahlen
   - Begründung: mit Beleg (Rechnung, Quelle mit Link, Lehrstuhlmaterial mit Fundstelle)
   - Priorität: muss, sollte oder kann · Aufwand: klein, mittel oder groß
   - Folgen: für Lösung, Zahlen, Abbildungen

3. **Was bleiben sollte:** Stärken, die bei Änderungen nicht verloren gehen dürfen.
4. **Offene Fragen** an die Tutoriumsleitung.

Lieber zehn gute, gut begründete Vorschläge als dreißig dünne. „Muss“ nur für Fehler, Widersprüche oder echte Hindernisse im Tutorium.

**Schlussantwort** an die Koordination: höchstens 200 Wörter mit Gesamturteil, den drei wichtigsten Vorschlägen und dem Pfad deines Berichts.
