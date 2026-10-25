# Bündeln und Entscheidungsvorlage

Für die Koordination, nachdem alle sechs Berichte da sind.

## 1. Vorgehen

1. **Sammeln:** alle Vorschläge aus den sechs Berichten in eine Arbeitsliste (`pruefung/buendelung_arbeitsliste.md`), mit ihren Nummern (Prof1, Tech3, Did2, Rech4, Stud1, Gest2, …).
2. **Vereinen:** Vorschläge, die dasselbe wollen, zusammenführen; die Herkunft bleibt sichtbar („Prof2, Did4, Stud1“). Die ausgeschriebenen Präfixe bleiben auch in Tab und Protokollen, weil D, G und K dort Entscheidungen, Grundlagen und KI-Einträge bezeichnen. Sagen mehrere Rollen dasselbe, ist das ein starkes Signal; schreib die Zahl der Rollen dazu.
3. **Widersprüche zeigen:** Widersprechen sich Rollen (zum Beispiel „Teil f streichen“ gegen „Teil f ausbauen“), stehen beide Positionen nebeneinander, mit deiner Empfehlung.
4. **Nachrechnen:** Jede Zahl, die ein Vorschlag behauptet oder neu einführt, rechnest du selbst nach (Rechenmodell unter `material/C_modell/` oder eigenes Skript). Was nicht stimmt, wird korrigiert oder fällt mit Begründung heraus.
5. **Vorgaben:** Vorschläge mit dem Vermerk „Vorgabe in Frage gestellt“ bekommen eine eigene Liste; sie betreffen Entscheidungen, die schon gefallen sind.
6. **Ordnen:** **muss** (Fehler, Widerspruch, echtes Hindernis im Tutorium), **sollte** (deutliche Verbesserung), **kann** (Idee, Variante); innerhalb jeder Stufe nach Nutzen und Aufwand.
7. **Empfehlen:** zu jedem Vorschlag eine klare Empfehlung: annehmen, ablehnen oder Variante (welche). Begründung in einem Satz.
8. **Folgen:** zu jedem Vorschlag, was sich ändert (Aufgabentext, Lösung, Zahlen, Abbildungen, Versuch, Sammlung) und ob andere Vorschläge davon abhängen.

## 2. Tab „Änderungsvorschläge“ im Claude-Dokument

Neuer Tab im Dokument „Kaffee mit Milch (Tutorium 5)“ (<https://claude.ai/artifact/LCRkwWobg2nv739T5XC73d>). Aufbau:

1. **Titel und Kopf:** „Änderungsvorschläge“, Datum, dann drei bis fünf Sätze **Gesamturteil** (was ist stark, was ist das größte Problem, wie viele Vorschläge in welcher Stufe).
2. **So entscheidest du:** ein Satz: „In der Spalte ‚Entscheidung‘ wählen (offen, ja, nein, Variante); Anmerkungen in [ ] in die Spalte ‚Anmerkung‘ oder direkt in den Text.“
3. **Muss**, **Sollte**, **Kann:** je eine Tabelle mit den Spalten

   | Nr. | Herkunft | Ebene | Stelle | Vorschlag | Folgen | Empfehlung | Entscheidung | Anmerkung |
   |---|---|---|---|---|---|---|---|---|

   „Nr.“ fortlaufend über alle Stufen: Ä1, Ä2, … (nicht M1, S1 oder K1, weil S die Studierenden-Rolle und K das KI-Protokoll bezeichnet). „Vorschlag“ konkret, mit neuem Wortlaut oder neuen Zahlen, so knapp wie möglich. „Entscheidung“ als Auswahlfeld mit den Werten offen, ja, nein, Variante (vorbelegt mit „offen“). „Anmerkung“ leer.
4. **Widersprüche zwischen Rollen:** je Punkt beide Positionen und deine Empfehlung, mit Entscheidungsspalte.
5. **Vorgabe in Frage gestellt:** eigene kleine Tabelle, gleiche Spalten.
6. **Was bleiben sollte:** Stichpunkte aus den Berichten, zusammengefasst.
7. **Nicht übernommen:** Vorschläge, die beim Nachrechnen oder Prüfen herausgefallen sind, je mit einem Satz Begründung.
8. **Quellen:** die Links aus den Berichten, die für angenommene Vorschläge wichtig sind.

Sprache wie auf dem Blatt: Deutsch, keine Gedankenstriche, Formelzeichen im Fließtext schlicht (V_K, ϑ_1), längere Formeln als abgesetzte Formel.

## 3. Nachricht im Chat

- Gesamturteil in drei Sätzen.
- Die fünf wichtigsten Vorschläge, je eine Zeile.
- Eine klare Empfehlung (zum Beispiel „alle Muss-Punkte und Ä12, Ä15 annehmen, den Rest später“).
- Wie die Tutoriumsleitung entscheidet und was danach passiert.
- Keine Wiederholung der Tabellen.

## 4. Protokolle

Die Protokolle trägst du **vor** dem Anhalten ein (Startprompt, Schritt 4), damit die Prüfung auch nach einer langen Pause dokumentiert ist.

- **KI-Protokoll:** Eintrag **K34** (Datum, Auftrag „unabhängige Prüfung der Kaffee-Aufgabe mit sechs Rollen“, Tätigkeit: Paket, Rollenordner, sechs parallele Prüfer, Bündelung mit Nachrechnung; Ergebnis: Zahl der Vorschläge je Stufe; Prüfung: was nachgerechnet wurde; Probleme: was schiefging oder korrigiert wurde). Neuer Abschnitt **3.7 „Unabhängige Prüfung der Kaffee-Aufgabe (K34)“** mit einer Tabelle der wichtigsten Befunde (Spalten: Aussage im Entwurf, Ergebnis der Prüfung, Folge; eigene Datei `pruefergebnisse_kaffee_rollen.js`). Zeile im Änderungsverlauf (Version 9).
- **Entscheidungsprotokoll:** Grundlage **G40** („Prüfberichte P, T, D, R, S und G vom …“, Art N und F, verwendet in D93 ff.). Status von D88 und D89 auf „umgesetzt“ setzen. Die Entscheidungen **D93 ff.** (neuer Abschnitt 3.10) erst nach der Auswahl der Tutoriumsleitung, je angenommenem oder abgelehntem Vorschlag (mit seiner Nummer Ä…) oder als Sammelentscheidung. Änderungsverlauf (Version 9).
- **Umsetzung** (eigene Runde): weiterer Eintrag **K35**, Entscheidungen D93 ff. mit Status „umgesetzt“, Änderungsverlauf (Version 10). Sind Nummern inzwischen vergeben, die nächsten freien nehmen.
