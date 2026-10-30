# Sichtprüfung der Ausgabeformate, Rolle X2

Prüfstand: `560b8d4c9b18860d6688a5e8f7a8be5d78a5f537`, 30.10.2026.
Dateipräfix für neue Ausgaben: `pruefung/Kaffee_Pruefpaket_2026-10-23/umsetzung/Arbeitsordner/`.
Alle unten angegebenen Seiten wurden gerendert und tatsächlich als Bilder angesehen.
Dateifingerabdrücke und Seitenzahlen stehen in `x2_render_ausgabe.json`.

| Originaldatei | Visuell geprüfte Seiten | Ergebnis |
|:---|:---|:---|
| `kaffee/Kaffee_Aufgabe.pdf` | 1 bis 4 | Bilder, Formeln und beide Tabellen vollständig |
| `kaffee/Kaffee_Loesung.pdf` | 1 bis 13 | Bilder, Formeln und Tabellen vollständig, Tutoriumshinweise vorhanden |
| `kaffee/Kaffee_Loesung_Studierende.pdf` | 1 bis 10 | Keine Tutoriumsleitungshinweise, fachlicher Lösungsteil und Quellen vorhanden |
| `sammlung/ausgabe/Aufgabensammlung_Tutorien_WUE_2026-10-30.pdf` | Kaffee 22 bis 25, Kaffeequellen 58 | Kaffeeabbildung, Formeln und Versuchstabelle vollständig |
| `kaffee/Kaffee_Aufgabe.docx` | 1 bis 4 nach Konvertierung | Keine fehlenden Bilder, Glyphen oder Tabelleninhalte |
| `kaffee/Kaffee_Loesung.docx` | 1 bis 14 nach Konvertierung | Inhalt vollständig, einzelne Quellenzeile auf letzter Seite |
| `kaffee/Kaffee_Loesung_Studierende.docx` | 1 bis 10 nach Konvertierung | Keine Tutoriumsleitungshinweise oder defekten Formeln |
| `sammlung/ausgabe/Aufgabensammlung_Tutorien_WUE_2026-10-30.docx` | Kaffee 25 bis 28 nach Konvertierung | Keine fehlenden Bilder oder abgeschnittenen Tabellen |
| alte `material/A_aufgabe/Kaffee_Aufgabe.pdf` | 1 bis 3 | Vergleich der Aufgabenanordnung und Abb. 1 |
| alte `material/B_loesung/Kaffee_Loesung.pdf` | 1 bis 9 | Vergleich der Lösungsanordnung und Abb. L1/L2 |

Die DOCX-Dateien wurden mit LibreOffice (`soffice`) in einem eigenen temporären Profil nach PDF konvertiert. Das ist keine native Microsoft-Word-Prüfung. Die andere Seitenzahl der Word-Lösung ist rendererabhängig.

## Kleine Satzbefunde

1. In allen drei neuen Einzel-PDFs endet Seite 2 mitten im Satz von Teil f nach „und erklären“. Seite 3 beginnt mit „Sie das Ergebnis.“ und bleibt nach g weitgehend leer. Stelle im Aufgaben-Markdown: Zeile 63 bis 67. Vorschlag: Teil f mit Ergebniszeile zusammenhalten oder vor f umbrechen. Inhalt fehlt nicht. In der LibreOffice-Word-Ansicht steht der Satz vollständig auf Seite 3.
2. `Kaffee_Loesung.docx` endet in der LibreOffice-Ansicht auf Seite 14 mit nur „Rechenskript: nachrechnung_kaffee.py mit kaffee_modell.py.“ (Lösungs-Markdown Zeile 260). Vorschlag: Absatzabstände oder Umbruch im Quellenblock leicht anpassen. Kein inhaltlicher Freigabeblocker.

Abb. L1 steht in den neuen PDF- und Word-Lösungen auf Seite 5. Die Aussage „Wärme ist eine Prozessgröße“ steht jeweils auf Seite 7. Abb. L2 steht jeweils auf Seite 8. Gegenüber der alten Abb. L2 (Lösungs-PDF Seite 6) sind die Linienarten, die Detailansicht des Schnittpunkts und die drei Endwertmarkierungen erkennbar verbessert. Die neue Abb. L1 ergänzt gegenüber der alten Fassung (Seite 4) den äußeren Bilanzraum für den Becher.

Reproduktion: `python ergebnisse/kaffee/codex_skripte/x2_render_artefakte.py --word`. Das Skript schreibt ausschließlich Bilder, extrahierte PDF-Texte, DOCX-Konvertierungen und ein Manifest in den angegebenen temporären Ausgabeordner. Es verändert keine Aufgabe, Lösung oder Sammlung.
