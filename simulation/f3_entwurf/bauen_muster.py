# -*- coding: utf-8 -*-
"""Baut das Gestaltungsmuster Fassung 3 (eine Datei, Schriften eingebettet). Aufruf: python3 bauen_muster.py"""
import base64
import pathlib

ORDNER = pathlib.Path(__file__).resolve().parent
SCHRIFTEN = [("Plex Sans", 400, "PlexSans-400.woff2"), ("Plex Sans", 600, "PlexSans-600.woff2"),
             ("Plex Mono", 400, "PlexMono-400.woff2"), ("Plex Mono", 600, "PlexMono-600.woff2"),
             ("Plex Math", 400, "PlexMath.woff2")]
regeln = []
for familie, gewicht, datei in SCHRIFTEN:
    daten = base64.b64encode((ORDNER / "schriften" / datei).read_bytes()).decode("ascii")
    regeln.append(f'@font-face{{font-family:"{familie}";font-weight:{gewicht};font-style:normal;font-display:block;'
                  f'src:url(data:font/woff2;base64,{daten}) format("woff2");}}')
quelle = (ORDNER / "muster_src.html").read_text(encoding="utf-8")
ziel = quelle.replace("/*@SCHRIFTEN@*/", "\n".join(regeln))
(ORDNER / "muster.html").write_text(ziel, encoding="utf-8")
print("muster.html", len(ziel.encode("utf-8")), "Bytes")
