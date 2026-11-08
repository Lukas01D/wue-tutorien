# -*- coding: utf-8 -*-
"""QR-Code der Kaffee-Simulation: nur die Adresse der Seite, ohne Kurslink (Entscheidung der TL zu A10, 08.11.2026).

Aufruf: python3 simulation/qr/qr_erzeugen.py   (braucht segno; prüft das Ergebnis mit OpenCV, falls installiert)
Ausgabe: QR_Kaffee_Simulation.svg (für Folien, beliebig skalierbar) und QR_Kaffee_Simulation.png (etwa 1200 px, für Tafelbild oder Druck).
Schwarz auf Weiß, Fehlerkorrektur M, Ruhezone 4 Module. Die Adresse bleibt bei der Veröffentlichung von Fassung 3 gleich.
"""
import os

import segno

ADRESSE = "https://waermeuebertragung-kaffee.qarri196.chatgpt.site/"
HIER = os.path.dirname(os.path.abspath(__file__))
NAME = os.path.join(HIER, "QR_Kaffee_Simulation")

qr = segno.make(ADRESSE, error="m", micro=False)
qr.save(NAME + ".svg", scale=10, border=4, dark="#000000", light="#ffffff", xmldecl=False,
        title="QR-Code: " + ADRESSE)
modul = max(1, 1200 // (qr.symbol_size(border=4)[0]))
qr.save(NAME + ".png", scale=modul, border=4, dark="#000000", light="#ffffff")
print("Version", qr.version, "Fehlerkorrektur", qr.error, "Module", qr.symbol_size(border=0)[0], "PNG-Modul", modul, "px")

try:
    import cv2
    # Lesen bei mehreren Bildgrößen (etwa wie ein Handy den Code auf Folie oder Tafel sieht)
    bild = cv2.imread(NAME + ".png")
    ergebnis = {}
    for breite in (160, 300, 600):
        f = breite / bild.shape[1]
        klein = cv2.resize(bild, None, fx=f, fy=f, interpolation=cv2.INTER_AREA)
        ergebnis[breite] = cv2.QRCodeDetector().detectAndDecode(klein)[0]
    ok = all(t == ADRESSE for t in ergebnis.values())
    print("Prüfung (OpenCV) bei 160, 300, 600 px:", "gleich der Adresse" if ok else "ABWEICHUNG: %r" % ergebnis)
    if not ok:
        raise SystemExit(1)
except ImportError:
    print("OpenCV nicht installiert: Lesen nicht geprüft")
