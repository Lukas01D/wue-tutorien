# Bilanzformen: Fassung v2 (28.10.2026)

> Grundlage: `Werkzeugkasten/vorlagen/bilanzformen/` (v1, erzeugt mit `Werkzeugkasten/arbeitsordner/ideen/bilanzformen.py`, Fassung vom 17.10.2026). v1 bleibt unverändert. Geändert sind das kompakte Schild und, nachgezogen, die große Übersicht.

## Inhalt dieses Ordners

| Ordner/Datei | Inhalt |
|---|---|
| `kompakt/` | alle neun Varianten (0, 1 bis 4, 12, 13, 24, 34) als SVG und PNG (300 dpi), 8,2 cm breit |
| `gross/` | alle zehn Varianten (0, 0b, 1 bis 4, 12, 13, 24, 34) als SVG und PNG (300 dpi), 16 cm breit |
| `quelle/bilanzformen_v2.py` | Skript für beide Fassungen |
| `Aenderungen_v2.md` | diese Datei |

Neu erzeugen (im WÜ-Ordner):
`BILANZ_FONTS="Werkzeugkasten/arbeitsordner/ideen/schriften_bilanz/" python3 Bilanzformen_FVT_2026-10-28_v2/quelle/bilanzformen_v2.py Bilanzformen_FVT_2026-10-28_v2 kompakt`
(mit `kompakt` am Ende nur das Schild, ohne beide Fassungen)

## Auftrag (von der TL bestätigt am 28.10.2026)

Grafik vor dem Anhängen an die Nachricht zum Stand der Tutorienaufgaben auf Richtigkeit und passende Fachbegriffe prüfen (Vorlesung 02, 05, 06; Duden; Literatur), dann eine v2 bauen.

## Änderungen am kompakten Schild

| # | Stelle | v1 | v2 | Grund |
|---|---|---|---|---|
| 1 | Untertitel „global“ | ganzes Bauteil | **ganzes Kontrollvolumen** | Begriff aus dem Skript (V05, V06: „Kontrollvolumen“, „Kontrollvolumen dA“); passt auch für Fluide und Behälter (Kaffee) |
| 2 | Typ oben rechts | DGL im Ort | **gewöhnliche DGL im Ort** | macht die Steigerung algebraisch, gewöhnliche DGL, partielle DGL sichtbar |
| 3 | Typ unten links | DGL in der Zeit | **gewöhnliche DGL in der Zeit** | wie 2 |
| 4 | Feld unten links | keine Bedingung | **_T_ homogen**, klein in Mittelblau rechts neben T(t) (T(t) bleibt mittig) | der Speicherterm m·cₚ·dT/dt braucht eine Temperatur für das ganze KV; ist T nicht homogen, gilt das Feld unten rechts. Nur unten links, weil stationär (dU/dt = 0) das Innere aus der globalen Bilanz herausfällt |
| 5 | alle Felder | Ergebnis, Typ | **Ergebnis, Typ, Beispielgleichung** | zeigt das Gesamtbild: was herauskommt, welcher Typ, wie die Gleichung dazu aussieht |
| 5a | Gleichungen und Zeilenköpfe | dU/dt mit Schrägstrich | **gestapelte Brüche** (auch dU/dt in den Zeilenköpfen) | Wunsch der TL (Feedback 28.10.2026, 22:39) |

Beispielgleichungen (klein, grau unter dem Typ):

| Feld | Gleichung | im Skript |
|---|---|---|
| stationär, global | Q̇_zu = Q̇_ab | V05: „Stationäre Wärmeleitung“, Q̇_zu = Q̇_ab |
| stationär, differentiell | d²T/dx² = 0 | V05, ebene Wand |
| instationär, global | m·cₚ·dT/dt = Q̇_zu − Q̇_ab | V02, Biot-Zahl, Fall Bi ≪ 1 |
| instationär, differentiell | ∂T/∂t = a·∂²T/∂x² | V02, Wärmeleitungsgleichung |

Daran sieht man: oben links keine Ableitung, unten links nur nach t, oben rechts nur nach x, unten rechts beides; erst dort steht das runde ∂.

## Änderungen an der großen Übersicht (nachgezogen am 28.10.2026)

| # | Stelle | v1 | v2 | Grund |
|---|---|---|---|---|
| 6 | Spaltenkopf „global“ | Bilanzraum: ganzes Bauteil / oder ganzer Apparat / kein Verlauf im Ort | **Bilanzraum: ganzes KV / z. B. Bauteil, Apparat, Behälter / liefert keinen Verlauf im Ort** | Kontrollvolumen wie im Skript (KV ist oben in der Grundgleichung eingeführt; ausgeschrieben passt es nicht in die Zeile). „kein Verlauf im Ort“ klang, als gäbe es innen kein Profil; global stationär darf innen ein Profil haben, die Bilanz löst es nur nicht auf. Jetzt parallel zu „liefert den Verlauf im Ort“ der Spalte differentiell |
| 7 | Feld instationär global, Ergebnis | T(t), im KV überall gleich (Bi ≪ 1 oder gut durchmischt) | **T(t), T im KV homogen (Bi ≪ 1 oder gut durchmischt)** | gleicher Begriff wie im Schild |
| 8 | Zeilenköpfe und Kasten „Speicherung“ | dU/dt mit Schrägstrich | **gestapelter Bruch**; die vier Kästen der Grundgleichung dafür 1,55 statt 1,05 cm hoch, Übersicht 0,5 cm höher | wie im Schild, alle Brüche gestapelt (Wunsch der TL) |

Alles andere in der großen Übersicht war schon passend (dort steht bereits „gewöhnliche DGL im Ort/in der Zeit“ und m·cₚ·dT/dt).

## Kleine Abweichungen vom Besprochenen (bitte prüfen)

- **cₚ statt c** in der Gleichung unten links: so verlangt es R17 (`03_REGELN.md`, „cₚ mit Index p“), und so steht es auch in der großen Übersicht.
- **Layout:** Felder höher (1,72 statt 1,36 cm, Schild 5,02 statt 4,3 cm hoch), Zeilenköpfe etwas schmaler (1,68 statt 1,8 cm) und Typangaben 6,3 statt 6,8 pt, damit „gewöhnliche DGL in der Zeit“ ins Feld passt. „T homogen“ in 5,6 pt, damit es rechts neben T(t) ins Feld passt. Kleinster Abstand Text zu Feldrand: 0,47 mm (fett im markierten Feld unten links).
- Gleichungen in eigenem Grau (#6E7387), etwas dunkler als das Grau ausgegrauter Felder, damit sie in der Übersicht nicht wie ausgegraut wirken.

## Geprüft und unverändert

- Zeilenköpfe dU/dt = 0 und dU/dt ≠ 0: passen zum Skript (V05 „Änderung der inneren Energie im KV“).
- „differentiell“: zulässig nach Duden („differenziell, differentiell“) und Schreibweise des Skripts.
- Element dx, dr, dA: wie V05 (Q̇ₓ, Q̇ᵣ) und V06 („Kontrollvolumen dA“).
- „global“ statt „integral“: bleibt; „integral“ kollidiert mit der „integrierten Form“ aus V06.
- d kursiv wie in der Vorlesung (die Norm DIN EN ISO 80000-2 setzt es aufrecht; bewusst nicht übernommen).
- T(x) bei Element dA (eigentlich T(A)): bleibt, um das Schild nicht zu überladen.

## Offen

1. **Übernahme in den Werkzeugkasten:** nach Freigabe `vorlagen/bilanzformen/` (groß und kompakt) ersetzen und das Skript in `arbeitsordner/ideen/` tauschen (am Ende der nächsten Runde). Dabei `LIESMICH.md` der Vorlage anpassen (Höhe des Schilds jetzt 5,0 cm).
2. **Folienfehler:** als PDF „Hinweise_Vorlesungsfolien_WUE_2026-10-28.pdf“ im Chat übergeben (V05 Folie 31: „partielle DGL“ bei d²T/dx² = 0; V06 Folie 21, nicht 20: ∂Q̇ = ṁ·∂h statt dQ̇ = ṁ·dh; dazu vier Schreibfehler in V02, V05, V06). Ablage und Weitergabe durch die TL.

## Vorschlag für das Entscheidungsprotokoll (Nummer beim Eintragen vergeben)

| Entscheidung | Grundlage | Von | Status | Rückweg |
|---|---|---|---|---|
| Kompaktes Bilanz-Schild v2: „ganzes Kontrollvolumen“, „gewöhnliche DGL im Ort/in der Zeit“, je Feld eine Beispielgleichung, Bedingung „T homogen“ unten links | Prüfung der Grafik am 28.10.2026 gegen V02, V05, V06 und Duden | TL | umgesetzt (v2), Übernahme in den Werkzeugkasten offen | v1 in `vorlagen/bilanzformen/kompakt/` |
| Große Übersicht v2 angeglichen: „Bilanzraum: ganzes KV“, „liefert keinen Verlauf im Ort“, „T im KV homogen“ | wie oben | TL | umgesetzt (v2), Übernahme offen | v1 in `vorlagen/bilanzformen/gross/` |
| Folienhinweise (2 fachlich, 4 Schreibfehler) als PDF für die Rückmeldung an den Lehrstuhl | wie oben | TL | PDF erstellt, Weitergabe durch die TL | keiner nötig |
| Bezeichnung der Bedingung: „T homogen“ (verworfen: „T konstant“, missverständlich zeitlich; „T einheitlich“, „T überall gleich“) | wie oben; „homogen“ passt zum Fachregister der Grafik | TL | umgesetzt | „T überall gleich“ |
