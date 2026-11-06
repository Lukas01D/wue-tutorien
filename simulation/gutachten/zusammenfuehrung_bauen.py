# -*- coding: utf-8 -*-
"""Erzeugt ZUSAMMENFUEHRUNG.md aus den Befundtabellen der Gutachten G1 bis G8 und den Entscheidungen unten (Runde 1)."""
import glob, os, re
HIER = os.path.dirname(os.path.abspath(__file__))
U, A, O = "übernehmen", "ablehnen", "offen"
BT = "Browsertest `browsertest_bau.js`"
# Entscheidungen: ID -> (Entscheidung, Begründung mit Beleg, Folge). Nicht aufgeführte IDs: siehe GRUPPE.
GRUPPE = {
 "frage2_sperre": (U, "Messpunkte, Legende und ln-Punkte erst nach festgehaltener Vorhersage zu Frage 2 (`messFrei()` in `oberflaeche.js`); " + BT + " „Sperre Frage 2“", "behoben"),
 "achse": (U, "Nachkommastellen aus der Schrittweite (`stellenVon`); " + BT + " „Achsenbeschriftung bei Schrittweite 2,5“", "behoben, auch ln-Achse"),
 "handy_reihe": (U, "Am Handy nach der Freigabe Reihenfolge Diagramm, Frage, Regler (`html.handy`, Flex-Reihenfolge), Frageleiste nach dem Festhalten ohne gesperrte Felder, Schalter „Diagramm lösen“; " + BT + " „M-6 am Handy“, „Anheften abschaltbar“", "behoben"),
 "fokus_verdeckt": (U, "`scroll-padding-top` gleich der gemessenen Höhe des angehefteten Bereichs (CSS-Variable `--anheft`), Anheften aus bei Fokus in Textfeldern von Messblatt und Frageleiste", "behoben; echtes Gerät offen (ABNAHME_IPHONE.md)"),
 "tabs": (U, "`storage`-Ereignis lädt den Zustand neu und zeichnet; Laden prüft Typen und Bereiche; " + BT + " „zweiter Tab überschreibt nichts“", "behoben"),
 "hashchange": (U, "`hashchange` ruft die Kurslink-Prüfung; " + BT + " „Kurslink im schon offenen Tab“", "behoben"),
 "beamer": (U, "Diagrammhöhe an die Fensterhöhe gekoppelt, Regler „Zugabe nach“ direkt unter dem Diagramm, Frageleiste nach dem Festhalten kurz, Kernleiste in der Vertiefung angeheftet (Laptop); Empfehlung Browser-Zoom in EINSATZ_TUTORIUM.md", "behoben; Hörsaal offen"),
 "valuetext": (U, "`aria-valuetext` mit Einheit im Sprachformat, reiner Textname am Regler; " + BT + " „M-12“", "behoben"),
 "energie_klein": (U, "Schrift im SVG 15 und 14 statt 12 und 11, rechte Spalte ab 1200 px bis 300 px breit", "behoben; Beamer im Hörsaal offen"),
 "beschriftung": (U, "Schnitt-Beschriftung prüft Kurven, Punkte und Raumlinie; Vorhersagekasten zuerst platziert und Breite aus getBBox; Raumbeschriftung weicht nach links aus; Trinklinie dort beschriftet, wo keine Kurve kreuzt", "behoben; Einzelfälle bei 320 px möglich"),
 "rueckmeldung_zahl": (U, "Rückmeldung nennt „Auswahl passt“ und vergleicht die Zahl mit dem Modell der Standardlage; eigene Begründung über der Auflösung; " + BT + " „Rückmeldung vergleicht die Zahl“", "behoben"),
 "einheit_feld": (U, "„4 K“, „ca. 4“, „50 min“ gelten als Zahl; sonst Hinweis je Ursache am Feld (`aria-invalid`); " + BT + " „4 K als Zahl“", "behoben"),
 "f2_grau": (U, "Hinweis neben dem gesperrten Knopf („Erst Kurswerte laden … sonst Frage 2 überspringen“), Ausgangslage vor dem Laden richtig benannt", "behoben"),
 "schnitt_vor_f1": (U, "Schnittkreis, Beschriftung und Schnittzeit in den Rechenwerten erst nach der Vorhersage zu Frage 1; " + BT + " „Sperre Frage 1“. Die erklärenden Sätze in den Reitern (Konzepttexte A.2, A.8) bleiben: Frage an die TL", "behoben (Anzeige); Texte offen an TL"),
 "saeulentitel": (U, "Titel jetzt „Energie bis zur Zugabe: an den Raum abgegebene Wärme“ (Begriff des Konzepts bleibt, Zusatz klärt); als Änderung an einem Konzeptwort im Baubericht gekennzeichnet", "behoben, TL kann zurücknehmen"),
 "vorhersage_marke": (U, "Kasten zeigt die Vorhersage der aktuellen Frage; bei Frage 1 und V2 zusätzlich senkrechte Linie bei der vorhergesagten Zeit", "behoben"),
 "v3_ausgang": (U, "Eigener Text „Standardwerte, Becher an, kA aus der Messung nach 10 min (wie Teil g)“", "behoben"),
 "ohne_rueckfrage": (U, "„ohne Vorhersage aufdecken“ fragt nach (Rückfrage neben dem Knopf)", "behoben"),
 "rueckfrage_ort": (U, "Rückfragen stehen neben dem auslösenden Knopf, Fokus bei Abbrechen zurück", "behoben"),
 "csv_en": (U, "Felder mit Trennzeichen in Anführungszeichen (RFC 4180); " + BT + " „englische CSV“", "behoben"),
 "dezimal_en": (U, "Vorhersagezahl wird gelesen und im Format der Sprache angezeigt; " + BT + " „2,5 erscheint als 2.5“", "behoben"),
 "meldung_sprache": (U, "Beim Sprachwechsel Statuszeile geleert, offene Link-Frage neu gezeichnet, `?lang` aus der Adresse genommen", "behoben"),
 "speicher_handy": (U, "Hinweis „nicht gespeichert“ am Handy sichtbar, sobald gesperrt oder Schreiben scheitert", "behoben"),
 "fokus_kopf": (U, "Weißer Fokusring im dunklen Kopf", "behoben"),
 "vergleich": (U, "Vergleichslauf kräftiger (Deckkraft 0,5 und 0,6, eigene Strichart), Mischsprung, Zahlen als Satz unter dem Diagramm", "behoben"),
 "textalternative": (U, "Diagrammname und Beschreibung je Ansicht; Beschreibung trennt Mischen und Abkühlen; Wertetabelle mit Messwerten nach Frage 2 und Zeile nach der Milch; Beschreibung nur einmal (aria-describedby)", "behoben"),
 "eingabe_rand": (U, "Rand der Textfelder #7d8fa1 (3,4:1 auf Weiß)", "behoben"),
 "messblatt_fehler": (U, "Meldung nennt die Zelle, `aria-describedby`, Leeren nur bei gültiger Eingabe", "behoben"),
 "kA_radio": (U, "Fokus bleibt auf der gewählten Option", "behoben"),
 "ansage_start": (U, "Statusansage nach dem Festhalten mit Zahlen; Seite scrollt zu Diagramm und Frage", "behoben"),
 "aufklapp": (U, "Zeichen ▸ und ▾ an allen `summary`", "behoben"),
 "alert_neu": (U, "Fehlertext nur bei Änderung neu gesetzt", "behoben"),
 "hilfe_name": (U, "Hilfeknopf heißt „Hilfe zu …“, schließt mit Escape", "behoben"),
 "region": (U, "Scrollbereiche mit Rolle und Namen, nur wenn sie überlaufen", "behoben"),
 "ln_legende": (U, "Legende der Punktformen auch in „ln“", "behoben"),
 "messblatt_frueh": (U, "Messblatt ab Start eingebbar, „Übernehmen“ erst nach der Freigabe; " + BT + " „Messblatt vor der Freigabe“", "behoben"),
 "link_datei": (U, "Hinweis „Link gilt nur auf diesem Rechner“ bei `file:`; Text ohne Versprechen eines QR-Codes; QR-Code selbst (K-2) nicht gebaut", "behoben; K-2 offen"),
 "becher1_zeile0": (U, "Einleitung des Messblatts sagt: Becher 1 Zeile 0 nach dem Umrühren, keine Zeile „60 nach der Milch“; Becher 3 mit Milch bei Raumtemperatur", "behoben"),
 "marken": (U, "Modellendpunkte hohl, Becher-3-Messpunkte hohl und unter den anderen", "behoben"),
 "becher3_zeichen": (U, "Becher 3 ohne ϑ₂, eigener Unterschied Tasse 1 und Becher 3 in den Rechenwerten", "behoben"),
 "becher3_sprung": (U, "Mischsprung von Becher 3 (blau gepunktet) und hohle Endmarke", "behoben"),
 "zahlfeld_runden": (U, "Zahlfeld rundet auf die angezeigte Stellenzahl", "behoben"),
 "ungueltig_text": (U, "Rechenwerte und Wertetabelle zeigen „Keine Rechnung: Einstellung ungültig“; Lesehinweis leer; Hinweis am auslösenden Feld", "behoben"),
 "laden_robust": (U, "Laden prüft jedes Feld nach Typ und Bereich", "behoben"),
 "messblatt_klick": (U, "Messblatt-Eingabe zieht nur Hinweis und Knopf der Frage 2 nach, ohne die Leiste neu aufzubauen", "behoben"),
 "uebernahme_grund": (U, "Ablehnung nennt Wert und Bereich", "behoben"),
 "link_komma": (U, "Messreihen zuerst, Kopfwerte am Ende: kein Komma am Ende; " + BT + " „Kurslink endet nicht auf Komma“", "behoben"),
 "sprunglink": (U, "Fragmente ohne Vorsilbe `kurs` werden still übergangen", "behoben"),
 "schrift_basis": (U, "`body` mit 1rem statt 16px; angehefteter Bereich höchstens 33 vh plus Kernzahlen", "behoben"),
 "laenge": (U, "`overflow-wrap: anywhere`, `maxlength` an Zahl- und Begründungsfeld", "behoben"),
 "noscript": (U, "`noscript`-Hinweis zweisprachig", "behoben"),
 "quelltext": (A, "Eine Offline-Datei muss die Auflösungstexte enthalten; die Sperre gilt für Darstellung, Barrierefreiheitsbaum und Ansagen (ZUSTAENDE.md Regel 1). `KAFFEE.ergebnis()` gibt vor der Freigabe `null` zurück", "dokumentiert im Baubericht"),
 "doppelklick": (U, "Zweiter Klick innerhalb 400 ms nach einem Fragewechsel wird übergangen", "behoben"),
 "querformat": (U, "Teilweise: Diagrammhöhe bei niedrigen Fenstern ab 170 px, Pflichtregler direkt darunter, damit Diagramm und Regler zugleich sichtbar sind; echtes Nebeneinander (Konzept 5.2) nicht gebaut", "teilweise; Nebeneinander im Baubericht als Abweichung"),
 "achse0": (U, "Temperaturachse beginnt beim nächsten Zehner unter den Werten, nicht bei 0", "behoben"),
 "en_text": (U, "Englische Fassung nach Glossar Anhang C und Leitfaden 4 überarbeitet (heat loss coefficient, linearised, Approximate …, Starting point, mug included, Großschreibung an Achsen und Kursnamen, Sätze aus G2-14, Indizes ab, mess, misch erklärt, Namen der Messfelder, Tausender mit Leerzeichen). Einheiten in eckigen Klammern an Achsen und Tabellenköpfen bleiben (Lernzentrum K2)", "behoben"),
 "lang_link": (U, "Kurslink ohne `?lang`", "behoben"),
 "ln_clip": (U, "Geraden auf den Zeichenbereich beschnitten", "behoben"),
 "aufl_knopf": (U, "Knopf heißt bei offener Auflösung „Auflösung ausblenden“", "behoben"),
 "gesperrt_label": (U, "Zusatz „(nach der Startfrage verfügbar)“", "behoben"),
 "fragen_k3": (A, "Kleine Brüche im Satz sind Entscheidung K3 des Lernzentrums (VORBILD_LERNZENTRUM.md, Formelsatz)", "keine"),
 "nowrap": (U, "Satzzeichen nach einer Formel bleiben an der Formel (`span.nb` beim Bau)", "behoben"),
 "platzhalter": (U, "Platzhaltertext im leeren Diagramm umbrochen", "behoben"),
 "sprachknopf": (U, "Sprachknopf ohne Umbruch, aktuelle Sprache fett", "behoben"),
 "rechenwerte_doppelt": (U, "Bezugszeile vor der Vorhersage „Noch keine Rechenwerte“", "behoben"),
 "regler_neutral": (U, "Hinweis am gesperrten Regler in Nebentextfarbe; vor der Freigabe „Erst die Startfrage beantworten.“", "behoben"),
 "wertetabelle_rechts": (U, "Zahlen rechtsbündig, gleich breite Ziffern", "behoben"),
 "forced": (U, "Diagramm und Säulen behalten im Kontrastmodus ihre Farben auf weißem Grund (`forced-color-adjust: none`)", "behoben; echtes Windows offen"),
 "banner_fokus": (U, "Nach Übernehmen oder Nicht übernehmen Fokus auf die Bestätigung, Ansage, Escape schließt", "behoben"),
 "zusatzfrage": (U, "Grundlage „Versuch, Becher 3“ statt „Zusatzfrage (2)“", "behoben"),
 "richtwert_doppelt": (U, "Satz „Richtwert …“ nur noch als Fußnote", "behoben"),
 "ln_frei": (U, "Freie Gerade mit je einem Startpunkt pro Becher", "behoben"),
 "link_leer": (U, "Leeres Messblatt erzeugt keinen Link, Meldung", "behoben"),
 "schreib_hinweis": (U, "Hinweis sofort, wenn Schreiben scheitert", "behoben"),
 "reiter_name": (O, "Drei Reiter nach Bauauftrag und Lernzentrum K5 (Rangfolge: Bauauftrag vor Konzept M-18); Name „Versuche“ (Lernzentrum) gegen E6 „Auflösungen“: Frage an die TL, Empfehlung „Versuche“ beibehalten", "Frage an die TL"),
 "blatt_versuch": (O, "Blatt vom 31.10. (40 min, kA ohne Becher) und Seite (E8: 60 min, Übernahme mit Becher) weichen ab; kein Baufehler, Blatt nicht ändern (Auftrag)", "Frage an die TL"),
 "konzepttext": (O, "Wortlaut aus Konzept 6 oder Anhang A (Fragen, Auflösungen, Reitertexte); fachliche Texte ändert der Bau nicht eigenständig", "Frage an die TL mit Empfehlung im Baubericht"),
 "entschieden": (A, "Widerspricht einer Festlegung (ZUSTAENDE.md oder Konzept); siehe Begründung je Befund", "keine"),
 "kann": (A, "Kann-Punkt bewusst schlank gebaut (Bauauftrag 3.2); Erweiterung wäre ein neuer Auftrag", "keine"),
 "druck": (A, "Druckansicht K-8 ist nicht gebaut (Kann)", "keine"),
 "geraet": (O, "Nur am echten Gerät prüfbar", "ABNAHME_IPHONE.md / Hörsaal"),
 "scroll_tabelle": (A, "Messblatt rollt bei 320 bis 375 px im eigenen benannten Bereich; zulässig nach WCAG 1.4.10 für Tabellen", "keine"),
 "stand_kopf": (A, "Stand und Version stehen im Fuß; bewusste Abweichung von Konzept 5.1 (Kopf bleibt kurz wie im Lernzentrum)", "im Baubericht"),
}
ZUORD = {
 "frage2_sperre": "G1-01 G4-01 G7-01", "achse": "G2-01 G5-01 G2-21", "handy_reihe": "G1-02 G4-10 G6-01 G1-03 G6-04 G6-25 G4-11",
 "fokus_verdeckt": "G5-02 G6-02 G8-17 G2-22", "tabs": "G7-02 G8-01", "hashchange": "G1-10 G7-10 G8-04 G3-23", "beamer": "G7-03 G6-05 G4-09 G7-05",
 "valuetext": "G8-02 G5-04 G1-19 G2-24 G5-06", "energie_klein": "G7-06 G6-06 G6-24 G6-12", "beschriftung": "G6-03 G6-22 G5-18 G5-19",
 "rueckmeldung_zahl": "G1-04 G4-07 G3-01", "einheit_feld": "G1-05 G2-04 G5-10", "f2_grau": "G1-06 G6-26", "schnitt_vor_f1": "G1-07 G4-02",
 "saeulentitel": "G1-08", "vorhersage_marke": "G1-11 G4-08", "v3_ausgang": "G4-12 G2-11 G3-08 G5-25", "ohne_rueckfrage": "G1-15 G4-14",
 "rueckfrage_ort": "G5-12 G7-14", "csv_en": "G2-02 G3-16", "dezimal_en": "G2-03", "meldung_sprache": "G2-10 G8-09 G3-24 G8-10",
 "speicher_handy": "G7-04", "fokus_kopf": "G5-03", "vergleich": "G5-05 G3-21", "textalternative": "G5-07 G5-08 G4-18 G2-25 G5-21 G3-18",
 "eingabe_rand": "G5-09 G6-29", "messblatt_fehler": "G5-11", "kA_radio": "G5-13", "ansage_start": "G5-14", "aufklapp": "G5-15 G6-07",
 "alert_neu": "G5-16", "hilfe_name": "G5-17 G2-26", "region": "G5-20", "ln_legende": "G5-22", "messblatt_frueh": "G7-08",
 "link_datei": "G7-09", "becher1_zeile0": "G1-12 G7-11 G7-13", "marken": "G7-07 G6-19", "becher3_zeichen": "G7-15 G2-18 G3-15",
 "becher3_sprung": "G3-14 G6-27", "zahlfeld_runden": "G8-12 G3-19", "ungueltig_text": "G8-13 G2-17 G3-09 G6-20 G6-21",
 "laden_robust": "G8-03", "messblatt_klick": "G8-05", "uebernahme_grund": "G8-06", "link_komma": "G8-07", "sprunglink": "G8-08",
 "schrift_basis": "G8-20 G5-26", "laenge": "G8-14", "noscript": "G8-15", "quelltext": "G8-16", "doppelklick": "G8-19",
 "querformat": "G6-18 G8-18 G5-27", "achse0": "G6-15", "en_text": "G2-06 G2-05 G2-08 G2-09 G2-12 G2-13 G2-14 G2-15 G6-16 G2-16",
 "lang_link": "G2-19", "ln_clip": "G2-20", "aufl_knopf": "G2-23", "gesperrt_label": "G2-27", "nowrap": "G1-14 G6-17",
 "platzhalter": "G1-13 G6-10 G6-23", "sprachknopf": "G6-09", "rechenwerte_doppelt": "G6-11 G4-23", "regler_neutral": "G6-14",
 "wertetabelle_rechts": "G6-31", "forced": "G5-23", "banner_fokus": "G5-24 G6-28", "zusatzfrage": "G1-17", "richtwert_doppelt": "G3-22",
 "ln_frei": "G3-20", "link_leer": "G3-23", "schreib_hinweis": "G8-11", "reiter_name": "G3-13 G2-07",
 "blatt_versuch": "G1-09 G7-12", "druck": "G5-28", "scroll_tabelle": "G6-30", "stand_kopf": "G6-13", "fragen_k3": "G6-32",
}
EINZELN = {
 "G1-16": ("konzepttext", "Satz aus Anhang A.5 nennt den Mechanismus, kein Ergebnis"),
 "G1-18": ("konzepttext", "Fragetext Frage 2 (Konzept 6.1); Empfehlung: „Die Einstellungen werden beim Prüfen übernommen.“"),
 "G3-02": ("konzepttext", "Auflösung Start (Konzept 6.1); Empfehlung: „bis etwa 56 min heißer und gab bis zur Zugabe insgesamt mehr Wärme ab“"),
 "G3-03": ("kann", "K-4 als Zusatzzeile gebaut (Werte geprüft, M9); kalte Kurven wären eine neue Darstellung"),
 "G3-04": ("konzepttext", "„Wärmeabgabe kA“ ist der Wortlaut von M-9; Empfehlung: im Deutschen beibehalten, Hilfe erklärt W/K"),
 "G3-05": ("konzepttext", "Texte A.2 und A.8 nennen C_G; Empfehlung: Zusatz „mit Becher C_GB“"),
 "G3-06": ("konzepttext", "Lesehilfe A.2 nennt die Zahlen der Standardlage; Empfehlung: „(Standardwerte)“ ergänzen"),
 "G3-07": ("konzepttext", "Bei ungleichem kA meinen Temperatur- und Wärmestromschnitt Verschiedenes; die Ansichten benennen ihren Schnitt; Empfehlung: Hinweis im Lesehinweis Wärmestrom"),
 "G3-10": ("konzepttext", "Annahmentext A.6; Empfehlung an die TL"),
 "G3-11": ("konzepttext", "Auflösung V5 (Konzept 6.2); Empfehlung: „nach den Richtwerten etwa wie Keramik“"),
 "G3-12": ("kann", "K-3 mit fester Vorgabe 60 °C gebaut"),
 "G3-17": ("kann", "CSV nach M11 (Zeit, Modell, Messblatt) gebaut; Bedingungen fehlen dort nicht im Pflichtumfang"),
 "G4-03": ("konzepttext", "Fragetext Frage 1 (Text der TL, Konzept 6.1); Empfehlung im Baubericht"),
 "G4-04": ("konzepttext", "Teilweise übernommen (Säulentitel); Satz des Mitbewohners in der Startkarte und Erhaltungssatz in der Auflösung sind Inhalt: Empfehlung an die TL"),
 "G4-05": ("konzepttext", "Startfrage nach der Rechnung: Ablauf der TL (Konzept 3); Empfehlung im Baubericht"),
 "G4-06": ("entschieden", "Begründung freiwillig nach ZUSTAENDE.md Regel 3 (Konzept); Rückmeldung zeigt die Begründung jetzt mit"),
 "G4-13": ("entschieden", "ZUSTAENDE.md Regel 5: Vertiefung frei mit Hinweis"),
 "G4-15": ("konzepttext", "Auflösung V1 (Konzept 6.2); Empfehlung: ein Satz Begründung"),
 "G4-16": ("konzepttext", "Abschlusssatz und Kernsatz für Selbstlernende: Inhalt; Empfehlung an die TL"),
 "G4-17": ("konzepttext", "Fragenzuschnitt V1, V3, V5 (Konzept 6.2)"),
 "G4-19": ("entschieden", "Knöpfe „Standardwerte“ und „Wie im Versuch“ nach Konzept 5.1 Nr. 5"),
 "G4-20": ("konzepttext", "Verweis auf die Ansicht Wärmestrom in einer Auflösung: Inhalt"),
 "G4-21": ("entschieden", "Rechenwerte nach Konzept 5.1; Messblatt muss für die TL früh offen sein (G7-08)"),
 "G4-22": ("konzepttext", "Benennung der Fragen (Konzept 6)"),
 "G4-24": ("konzepttext", "Fragetext V4 (Konzept 6.2); Empfehlung: Werkzeug nennen"),
 "G5-28": ("druck", ""), "G6-08": ("entschieden", "„Weiter“ nach Frage 2 und „Vertiefung öffnen“ führen zu V1; dauerhafter Eintrag nicht gebaut (low)"),
 "G6-13": ("stand_kopf", ""), "G6-30": ("scroll_tabelle", ""), "G6-32": ("fragen_k3", ""),
}

# Runde 2: neue Befunde (IDs G?-R2-nn und G9-nn der neuen Studentin); Nachprüfungen stehen in den Gutachten *_R2.md
R2 = {
 "G1-R2-01": (U, "Rechenwerte und Vorhersagezeile zeigen die Vorhersage der aktuellen Frage (`aktuelleVorhersage`)", "behoben"),
 "G1-R2-02": (U, "Ausgangslage von Frage 2 vor dem Prüfen „Kurswerte, übernommen beim Prüfen“", "behoben"),
 "G1-R2-03": (U, "Schnittbeschriftung nur mit freiem Platz (prüft Kurven, Punkte, Raumlinie, Vorhersagelinie)", "behoben; Endmarken bei 60 min dicht (siehe G9-09)"),
 "G2-R2-01": (U, "Anheften nur bei Fokus im Messblatt aus, nicht in der Frageleiste: Knopf springt nicht mehr", "behoben"),
 "G2-R2-02": (U, "Statusansage beim Sprachwechsel geleert", "behoben"),
 "G2-R2-03": (U, "Beispiel je Frage (3,5 K; 50 min; 40 °C; 80 min)", "behoben"),
 "G2-R2-04": (U, "siehe G1-R2-02", "behoben"),
 "G2-R2-05": (U, "„sichtbar nach eurer Vorhersage zu Frage 1“ / „shown once you have made your prediction …“", "behoben"),
 "G2-R2-06": (U, "Ohne Schnitt vor der Zugabe Text „Tasse 2 gibt bis zur Zugabe insgesamt … mehr ab“", "behoben"),
 "G2-R2-07": (U, "Grund der Ungültigkeit am auslösenden Feld, Feld mit `aria-invalid`", "behoben"),
 "G2-R2-08": (U, "V5 englisch umformuliert; Stellenzahl folgt Konzept 6.2", "behoben"),
 "G3-R2-01": (U, "siehe G2-R2-06", "behoben"),
 "G4-R2-01": (U, "Teilweise: Rückblick am Handy nennt Q1 und Q2 direkt beim Auftrag; die Säulen selbst stehen weiter unter Frage und Regler", "teilweise"),
 "G4-R2-02": (U, "Wärmestrom-Ansicht nennt vor der Vorhersage zu Frage 1 keinen Schnitt", "behoben"),
 "G4-R2-03": (U, "siehe G1-R2-01", "behoben"),
 "G4-R2-04": (U, "Rückfrage schließt mit Escape, Fokus auf „Ja“ bleibt (Muster der Rückfragen); Grund steht im Text", "teilweise"),
 "G4-R2-05": (U, "Ansage „Ohne Vorhersage aufgedeckt“", "behoben"),
 "G4-R2-06": (U, "Nach dem Überspringen keine Eingaben mehr; ohne Kurswerte kein „ohne Vorhersage aufdecken“", "behoben"),
 "G5-R2-01": (U, "`scroll-padding-top` 56 px ab 768 px", "behoben"),
 "G5-R2-02": (U, "Diagrammhöhe `min(29vh, 45vh − 125px)`, Schalter außerhalb des angehefteten Bereichs; " + BT + " „angehefteter Bereich höchstens 45 %“", "behoben"),
 "G5-R2-03": (U, "Ersatzlegende als Text unter dem Diagramm", "behoben"),
 "G5-R2-04": (U, "Tabelle im Messblatt ohne zweiten Bereich gleichen Namens", "behoben"),
 "G5-R2-05": (U, "Aufklappzeichen mit leerem Alternativtext (`content: \"▸\" / \"\"`)", "behoben"),
 "G5-R2-06": (U, "Fester Text „Diagramm oben anheften“ mit `aria-pressed`", "behoben"),
 "G5-R2-07": (U, "Hinweis „außerhalb des sinnvollen Bereichs“", "behoben"),
 "G5-R2-08": (U, "Bestätigung nur über den Fokus, nicht zusätzlich als Ansage", "behoben"),
 "G6-R2-01": (U, "siehe G5-R2-03", "behoben"),
 "G6-R2-02": (U, "Vorhersagelinie als Hindernis für Beschriftungen; Kasten bleibt oben rechts", "behoben (Abstand Kasten zu Linie bleibt)"),
 "G6-R2-03": (U, "siehe G5-R2-01", "behoben"),
 "G6-R2-04": (U, "siehe G5-R2-02", "behoben"),
 "G6-R2-05": (U, "Köpfe der Wertetabelle rechtsbündig", "behoben"),
 "G6-R2-06": (U, "siehe G2-R2-01", "behoben"),
 "G7-R2-01": (U, "Fragetext nach dem Festhalten eingeklappt; Einsatzblatt: Zoom zuerst 100 %", "behoben im Rahmen; Hörsaal offen"),
 "G7-R2-02": (U, "Rechte Spalte 240 px ab 768 px, Schrift der Säulen größer", "behoben"),
 "G7-R2-03": (U, "Einsatzblatt nennt die Abweichung Blatt (40 min) gegen Seite (60 min) und verweist auf die Frage an die TL", "behoben"),
 "G7-R2-04": (U, "Einsatzblatt: Link auf der veröffentlichten Seite erzeugen, ein QR-Code mit dem Kurslink, Werkzeug außerhalb der Seite", "behoben"),
 "G7-R2-05": (U, "Einsatzblatt: Messblatt von Anfang an sichtbar", "behoben"),
 "G7-R2-06": (U, "Einsatzblatt: „Kurswerte löschen“ nach der Probe", "behoben"),
 "G7-R2-07": (U, "Bestätigung verschwindet nach 15 s", "behoben"),
 "G7-R2-08": (O, "Wortlaut Frage 2 (Konzept 6.1); Empfehlung im Baubericht", "Frage an die TL"),
 "G8-R2-01": (U, "CSV vor der Startvorhersage ohne Modellwerte; " + BT + " „CSV vor der Startvorhersage ohne Modellwerte“", "behoben"),
 "G8-R2-02": (U, "siehe G5-R2-02", "behoben"),
 "G8-R2-03": (U, "siehe G2-R2-01", "behoben"),
 "G8-R2-04": (U, "Messwert „60 nach der Milch“ nur bei Zugabe nach 60 min in der CSV", "behoben"),
 "G8-R2-05": (U, "Fokus bleibt nach dem Abgleich; offene Rückfragen schließen weiter (selten: zwei Tabs gleichzeitig)", "teilweise"),
 "G8-R2-06": (U, "Zweiter Klick eines Doppelklicks (`detail > 1`) wird bei Rückfragen und Auflösungen übergangen", "behoben"),
 "G8-R2-07": (A, "Erneute Rückfrage beim Zurückblättern ändert ohne „Übernehmen“ nichts", "keine"),
 "G9-01": (U, "siehe G2-R2-01", "behoben"),
 "G9-02": (U, "Vorhersagezeile steht im angehefteten Bereich, wenn der Kasten nicht in das Diagramm passt", "behoben"),
 "G9-03": (U, "Vorhersage neutral blau statt grün", "behoben"),
 "G9-04": (U, "Teilweise: Rückblick mit Auftrag und Q1, Q2; Sprung zu Frage 1 ist Festlegung (ZUSTAENDE P2)", "teilweise; Ablauf Frage an die TL"),
 "G9-05": (A, "Messpunkte bleiben als Messung sichtbar; die Vertiefung setzt ihre Ausgangslage", "keine"),
 "G9-06": (O, "siehe G1-09, G7-12", "Frage an die TL"),
 "G9-07": (O, "siehe G3-13", "Frage an die TL"),
 "G9-08": (O, "Wortlaut Frage 1 (Konzept 6.1)", "Frage an die TL"),
 "G9-09": (U, "Teilweise: Modellendpunkte hohl, Becher 1 oben; bei 60 min liegen mehrere Marken dicht", "teilweise"),
 "G9-10": (O, "siehe G7-R2-08", "Frage an die TL"),
 "G9-11": (A, "Die Ansage nennt die Zahlen der aktuellen Lage; ein gleicher Einleitungssatz ist gewollt", "keine"),
 "G9-12": (U, "siehe G2-R2-03, G5-R2-07", "behoben"),
 "G9-13": (U, "siehe G6-R2-02", "behoben"),
}


# Runde 3: Bearbeitung endet nach dieser Runde (BAU_AUFTRAG 4.3); offene Punkte mit Empfehlung für den nächsten Schritt
NR3 = "nach Runde 3 nicht mehr bearbeitet (Bauauftrag 4.3)"
R3 = {
 "G2-R3-01": (O, "Empfehlung: Beschriftung „Frage ausblenden“ bei offenem Aufklapper", NR3),
 "G2-R3-02": (O, "Empfehlung: Lesehinweis Wärmestrom ohne Schnitt-Satz, wenn kein Schnitt vor der Zugabe liegt", NR3),
 "G4-R3-01": (O, "Empfehlung: nach dem Überspringen nur den Satz „Frage 2 übersprungen“ zeigen", NR3),
 "G5-R3-01": (O, "Empfehlung: `scroll-padding-top` aus der gemessenen Höhe der Kernleiste setzen; tritt nur bei vergrößerter Grundschrift auf", NR3),
 "G5-R3-02": (O, "Empfehlung: bei großer Grundschrift nicht anheften (Höhe des Bereichs vor dem Anheften prüfen); Umweg „Diagramm lösen“ vorhanden", NR3),
 "G5-R3-03": (O, "Empfehlung: Mindestschrift im SVG bei kleiner Darstellung (Schrift nach dem Maßstab skalieren)", NR3),
 "G6-R3-01": (O, "Empfehlung: Schnittbeschriftung zusätzlich rechts vom Kreis suchen; der Kreis selbst ist da, der Lesehinweis erklärt ihn", NR3),
 "G6-R3-02": (O, "Empfehlung: mehr Kandidaten für die Beschriftung am Kurvenzug, Ersatzlegende erst danach", NR3),
 "G6-R3-03": (O, "siehe G5-R3-03", NR3),
 "G6-R3-04": (O, "Empfehlung: Platz der Ersatzlegende immer freihalten", NR3),
 "G6-R3-05": (O, "Empfehlung: Beschriftung der Trinklinie mit Kollisionsprüfung gegen Punkte und Marken", NR3),
 "G6-R3-06": (O, "Kleinere Restkollisionen mit Kurswerten", NR3),
 "G7-R3-01": (O, "Empfehlung: Dreieck für Becher 3 erst nach der Vorhersage zu Frage 2 zeigen", NR3),
 "G7-R3-02": (U, "Einsatzblatt nennt jetzt den Pfad `simulation/site/Kaffee_Simulation.html` und warnt vor der älteren Datei", "behoben (Begleitmaterial)"),
 "G8-R3-01": (O, "Empfehlung: Bestätigung „Ja“ in den ersten 400 ms übergehen, Tastenwiederholung (`ev.repeat`) übergehen", NR3),
 "G8-R3-02": (O, "Empfehlung: Schutz `detail > 1` auch für „Zurück“ und „Weiter“", NR3),
 "G8-R3-03": (O, "Empfehlung: Messwert „60 nach der Milch“ immer in eigener Zeile; Meldung vor der Freigabe ohne „Modellkurven“", NR3),
 "G10-01": (O, "Empfehlung: Beim Öffnen einer Vertiefungsfrage ohne Vorhersage Kernzahlen und Rechenwerte bis zur Vorhersage verdecken oder Standardwerte einstellen. Betrifft nur die Vertiefung V3; die Richtung (kleiner) ist ablesbar, die Zahlen der Auflösung nicht", NR3),
 "G10-02": (O, "Zeitbedarf: Messung mit Studierenden nötig (offener Nachweis)", "Probelauf der TL"),
 "G10-03": (O, "Empfehlung: Fragetext erst nach geöffneter Auflösung einklappen", NR3),
 "G10-04": (O, "siehe G5-R3-03, G6-19", NR3),
 "G10-05": (O, "siehe G7-R2-08 (Wortlaut Frage 2)", "Frage an die TL"),
 "G10-06": (O, "Empfehlung: Vorhersagezeile ohne Startvorhersage, solange die aktuelle Frage offen ist", NR3),
 "G10-07": (O, "Bestätigung verschwindet nach 15 s; Empfehlung: Schließen-Knopf", NR3),
 "G10-08": (O, "Empfehlung: Text je Zustand mit gleichbleibendem Namen für Bildschirmleser", NR3),
 "G10-09": (O, "Fragenzuschnitt V3 (Konzept 6.2)", "Frage an die TL"),
 "G10-10": (O, "Auflösung Frage 2 (Konzept 6.1, offen formuliert nach K6)", "Frage an die TL"),
}


BEH = "behoben in der Korrekturrunde (Test in `simulation/tests/browsertest_korrektur.js`)"
R4 = {
 "G1-R4-01": (U, "Zeitangabe „(bis etwa 56 min)“ der Startauflösung erst nach der Vorhersage zu Frage 1 (Rest des Wortlauts F3 bleibt); Variante an die TL (Q1)", BEH + "; Q1 an die TL"),
 "G1-R4-02": (U, "„Hinweis schließen“ setzt den Fokus auf die Frage", BEH),
 "G1-R4-03": (U, "Hinweis zur neutralen Ausgangslage steht in der Frageleiste; vor dem Festhalten heißt es „Ausgangslage beim Prüfen“", BEH),
 "G1-R4-04": (O, "Begründung V1 ist Wortlaut F8; Fachrolle G3 bestätigt „irreführend“ und schlägt Ersatz vor", "Frage an die TL (Q2)"),
 "G1-R4-05": (U, "„Schnitt“ zuerst nah am Kreis (auch mit weißem Rand), weit weg nur ohne Verbindungslinie entlang der Kurven", BEH),
 "G1-R4-06": (U, "Bestätigung des Kurslinks bleibt bis „Hinweis schließen“", BEH),
 "G1-R4-07": (U, "Endkreise und Mischsprünge sind Hindernisse für „Schnitt“", BEH),
 "G1-R4-08": (U, "angeheftet konstante Höhe (Mindesthöhe aus der größten gemessenen Zusatzhöhe)", BEH),
 "G1-R4-09": (U, "zweiter Tipp an derselben Stelle innerhalb 1 s trifft weder „Zurück“ noch den Aufklapper", BEH),
 "G1-R4-10": (U, "nach dem Anheften wird der Knopf unter das Diagramm gescrollt", BEH),
 "G1-R4-11": (O, "„Notiert für euch“ ist der Wortlaut zu F9", "Frage an die TL (Q5)"),
 "G1-R4-12": (U, "„ohne Vorhersage aufdecken“ öffnet die Auflösung sofort (wie der Text der Rückfrage); Auftrag danach: Frage an die TL (Q6)", BEH + "; Q6 an die TL"),
 "G1-R4-13": (O, "neue Bedienfunktion (Auswahl V1 bis V5 in der Frageleiste), nicht geänderte Stelle; Empfehlung für eine spätere Runde", "offen, Empfehlung"),
 "G1-R4-14": (O, "Hinweis zum Prüfen in V1 ist neuer Wortlaut", "Frage an die TL (Q6)"),
 "G3-R4-01": (U, "wie G1-R4-01", BEH + "; Q1 an die TL"),
 "G3-R4-02": (U, "Teilflächen, Beschreibung und Lesehinweis unter dem Diagramm nach dem Vorzeichen; allgemeine Sätze in Lesehilfe und Rechenweg sind Wortlaut: Frage an die TL (Q3)", BEH + "; Q3 an die TL"),
 "G3-R4-03": (U, "Rest von G3-05 (Entscheidung F12): „(mit Becher zuzüglich m_B c_B)“ in Lesehilfe und ln-Steigung, DE und EN", BEH),
 "G3-R4-04": (O, "wie G1-R4-04; Ersatzwortlaut von G3", "Frage an die TL (Q2)"),
 "G3-R4-05": (O, "Kernsatz aus Konzept 3", "Frage an die TL (Q4)"),
 "G3-R4-06": (U, "eigener Wortlaut des Baus: „mit Vorzeichen gerechnet ist sie Q2 − Q1“", BEH),
 "G3-R4-07": (U, "negativer Gesamtwert als „weniger“", BEH),
 "G3-R4-08": (U, "eigener Wortlaut: „außerhalb des Bereichs des Feldes“", BEH),
 "G3-R4-09": (U, "eigener Wortlaut: „Messwert … wieder verwenden“", BEH),
 "G3-R4-10": (U, "Code-Reiter: „gleichwertigen Wert nach 10 min (keine Messung)“ (Konzept 8.2 M8)", BEH),
 "G3-R4-11": (O, "Quellenangabe im Annahmentext", "Frage an die TL (Q7)"),
 "G5-R4-01": (U, "Raumbeschriftung ist Hindernis; Trinkbeschriftung ohne Platz in die Legende; Vorhersagelinie endet über der Raumbeschriftung; Skript der Rolle: 0 von 648 Zuständen mit Überdeckung", BEH),
 "G5-R4-02": (U, "Verbindungslinie nicht entlang der Kurven; Vergleichskurven und Trinklinie sind Hindernisse", BEH),
 "G5-R4-03": (U, "wie G1-R4-02 und G1-R4-06", BEH),
 "G5-R4-04": (U, "Meldung zusätzlich in der bleibenden Ansage, `aria-describedby` am fieldset (Bildschirmleser nicht geprüft)", BEH),
 "G5-R4-05": (U, "Feldname in der Meldung, `aria-describedby`, roter Rand auch gegen den allgemeinen Feldrand", BEH),
 "G5-R4-06": (U, "`ResizeObserver` prüft auch die Scrollbereiche", BEH),
}

def befunde():
    out = []
    for f in sorted(glob.glob(os.path.join(HIER, "G*_*.md"))):
        if f.endswith("_R2.md") or "G9_" in f or "G10_" in f or "_R3" in f: continue
        for z in open(f, encoding="utf-8"):
            m = re.match(r"^\|\s*(G\d-\d+)\s*\|\s*(blocker|high|medium|low)\s*\|\s*(.*?)\s*\|", z)
            if m:
                text = re.sub(r"\*\*|`", "", m.group(3))
                out.append((m.group(1), m.group(2), text[:110] + ("…" if len(text) > 110 else "")))
    return out
def main():
    zu = {}
    for g, ids in ZUORD.items():
        for i in ids.split():
            zu[i] = g
    zeilen, zaehl, fehlt = [], {}, []
    for i, sch, txt in befunde():
        if i in EINZELN:
            g, extra = EINZELN[i]; e, b, fo = GRUPPE[g]; b = extra or b
        elif i in zu:
            e, b, fo = GRUPPE[zu[i]]
        else:
            fehlt.append(i); continue
        zaehl[(sch, e)] = zaehl.get((sch, e), 0) + 1
        zeilen.append("| %s | %s | %s | %s: %s | %s |" % (i, sch, e, txt.replace("|", "/"), b.replace("|", "/"), fo))
    if fehlt:
        raise SystemExit("ohne Entscheidung: " + " ".join(fehlt))
    kopf = open(os.path.join(HIER, "zusammenfuehrung_kopf.md"), encoding="utf-8").read()
    bil = "\n| Schwere | übernehmen | ablehnen | offen |\n|:--|--:|--:|--:|\n" + "\n".join("| %s | %d | %d | %d |" % (s, zaehl.get((s, U), 0), zaehl.get((s, A), 0), zaehl.get((s, O), 0)) for s in ("blocker", "high", "medium", "low")) + "\n"
    with open(os.path.join(HIER, "ZUSAMMENFUEHRUNG.md"), "w", encoding="utf-8") as f:
        f.write(kopf + bil + "\n## Alle Befunde der Runde 1\n\n| ID | Schwere | Entscheidung | Befund (gekürzt): Begründung mit Beleg | Folge |\n|:--|:--|:--|:--|:--|\n" + "\n".join(zeilen) + "\n")
    r2, z2 = [], {}
    for f in sorted(glob.glob(os.path.join(HIER, "*_R2.md")) + glob.glob(os.path.join(HIER, "G9_*.md"))):
        for zl in open(f, encoding="utf-8"):
            m = re.match(r"^\|\s*(G\d-R2-\d+|G9-\d+)\s*\|\s*(blocker|high|medium|low)\s*\|\s*(.*?)\s*\|", zl)
            if m:
                i = m.group(1); e, b, fo = R2[i]; txt = re.sub(r"\*\*|`", "", m.group(3))[:110]
                z2[(m.group(2), e)] = z2.get((m.group(2), e), 0) + 1
                r2.append("| %s | %s | %s | %s: %s | %s |" % (i, m.group(2), e, txt.replace("|", "/"), b.replace("|", "/"), fo))
    bil2 = "\n| Schwere | übernehmen | ablehnen | offen |\n|:--|--:|--:|--:|\n" + "\n".join("| %s | %d | %d | %d |" % (sv, z2.get((sv, U), 0), z2.get((sv, A), 0), z2.get((sv, O), 0)) for sv in ("blocker", "high", "medium", "low")) + "\n"
    with open(os.path.join(HIER, "ZUSAMMENFUEHRUNG.md"), "a", encoding="utf-8") as f:
        f.write("\n## Runde 2\n\nGeprüfter Stand SHA-256 `ea6d3ad2…9c31` (394 754 Bytes): alle acht Rollen prüften ihre übernommenen Befunde nach (Ergebnisse in den Tabellen „Nachprüfung“ der Dateien `*_R2.md`), dazu die neue Studentin G9. Kein Befund der Runde 1 blieb ganz unbehoben außer G5-21 (nachgeholt) und G6-19 (nachgebessert). Korrigierter Stand für Runde 3: SHA-256 `1d90ce2f…292b` (399 063 Bytes).\n\n### Bilanz Runde 2\n" + bil2 + "\n### Neue Befunde der Runde 2\n\n| ID | Schwere | Entscheidung | Befund (gekürzt): Begründung mit Beleg | Folge |\n|:--|:--|:--|:--|:--|\n" + "\n".join(r2) + "\n")
    r3, z3 = [], {}
    for f in sorted(glob.glob(os.path.join(HIER, "*_R3.md")) + glob.glob(os.path.join(HIER, "G10_*.md"))):
        for zl in open(f, encoding="utf-8"):
            m = re.match(r"^\|\s*(G\d+-R3-\d+|G10-\d+)\s*\|\s*(blocker|high|medium|low)\s*\|\s*(.*?)\s*\|", zl)
            if m:
                i = m.group(1); e, b, fo = R3[i]; txt = re.sub(r"\*\*|`", "", m.group(3))[:110]
                z3[(m.group(2), e)] = z3.get((m.group(2), e), 0) + 1
                r3.append("| %s | %s | %s | %s: %s | %s |" % (i, m.group(2), e, txt.replace("|", "/"), b.replace("|", "/"), fo))
    bil3 = "\n| Schwere | übernehmen | ablehnen | offen |\n|:--|--:|--:|--:|\n" + "\n".join("| %s | %d | %d | %d |" % (sv, z3.get((sv, U), 0), z3.get((sv, A), 0), z3.get((sv, O), 0)) for sv in ("blocker", "high", "medium", "low")) + "\n"
    with open(os.path.join(HIER, "ZUSAMMENFUEHRUNG.md"), "a", encoding="utf-8") as f:
        f.write("\n## Runde 3 (letzte Runde)\n\nGeprüfter Stand SHA-256 `1d90ce2f…292b` (399 063 Bytes): G2, G4, G5, G6, G7, G8 prüften ihre Reste aus Runde 2 nach (Dateien `*_R3.md`), dazu die neue Studentin G10. Keine Rolle fand einen blocker oder eine falsche Zahl; alle Sperren vor den Vorhersagen hielten (G8 suchte in DOM, Titel, Ansagen, CSV, Prüfhaken und Barrierebaum). Nach Bauauftrag 4.3 endet die Bearbeitung nach dieser Runde; die neuen Befunde bleiben offen, mit Empfehlung. Ausnahme: das Einsatzblatt (Begleitmaterial, Teil 5) wurde nachgezogen.\n\n### Bilanz Runde 3\n" + bil3 + "\n### Neue Befunde der Runde 3\n\n| ID | Schwere | Entscheidung | Befund (gekürzt): Begründung mit Beleg | Folge |\n|:--|:--|:--|:--|:--|\n" + "\n".join(r3) + "\n")
    r4, z4 = [], {}
    for f in sorted(glob.glob(os.path.join(HIER, "*_R4.md"))):
        for zl in open(f, encoding="utf-8"):
            m = re.match(r"^\|\s*(G\d+-R4-\d+)\s*\|\s*(blocker|high|medium|low)\s*\|\s*(.*?)\s*\|", zl)
            if m:
                i = m.group(1); e, b, fo = R4[i]; txt = re.sub(r"\*\*|`", "", m.group(3))[:110]
                z4[(m.group(2), e)] = z4.get((m.group(2), e), 0) + 1
                r4.append("| %s | %s | %s | %s: %s | %s |" % (i, m.group(2), e, txt.replace("|", "/"), b.replace("|", "/"), fo))
    bil4 = "\n| Schwere | übernehmen | ablehnen | offen |\n|:--|--:|--:|--:|\n" + "\n".join("| %s | %d | %d | %d |" % (sv, z4.get((sv, U), 0), z4.get((sv, A), 0), z4.get((sv, O), 0)) for sv in ("blocker", "high", "medium", "low")) + "\n"
    with open(os.path.join(HIER, "ZUSAMMENFUEHRUNG.md"), "a", encoding="utf-8") as f:
        f.write(open(os.path.join(HIER, "zusammenfuehrung_r4_kopf.md"), encoding="utf-8").read() + "\n### Bilanz Runde 4\n" + bil4 + "\n### Befunde der Runde 4\n\n| ID | Schwere | Entscheidung | Befund (gekürzt): Begründung mit Beleg | Folge |\n|:--|:--|:--|:--|:--|\n" + "\n".join(r4) + "\n")
    print(len(zeilen), "Befunde", zaehl, "Runde 2:", len(r2), z2, "Runde 3:", len(r3), z3, "Runde 4:", len(r4), z4)
main()
