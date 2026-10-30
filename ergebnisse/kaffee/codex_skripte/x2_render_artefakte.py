#!/usr/bin/env python3
"""Rendert die in Rolle X2 geprüften PDF- und DOCX-Ausgaben ohne Paketänderung.

Aufruf: python ergebnisse/kaffee/codex_skripte/x2_render_artefakte.py --word
Benötigt PyMuPDF; mit --word zusätzlich soffice. Bilder landen nur unter /tmp.
Die Sammlungsseiten beziehen sich auf Prüfcommit 560b8d4c9b18860d6688a5e8f7a8be5d78a5f537.
Ein erfolgreiches Rendern ersetzt keine Sichtprüfung der erzeugten Bilder.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET
import zipfile

import fitz


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "pruefung/Kaffee_Pruefpaket_2026-10-23/umsetzung/Arbeitsordner"
NAMES = ("Kaffee_Aufgabe", "Kaffee_Loesung", "Kaffee_Loesung_Studierende")
COLLECTION = "Aufgabensammlung_Tutorien_WUE_2026-10-30"


def fingerprint(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def render(path: Path, out: Path, pages: list[int] | None = None) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    with fitz.open(path) as doc:
        selected = pages or list(range(1, len(doc) + 1))
        for number in selected:
            page = doc[number - 1]
            page.get_pixmap(matrix=fitz.Matrix(1.3, 1.3)).save(out / f"seite_{number:02d}.png")
            (out / f"seite_{number:02d}.txt").write_text(page.get_text(), encoding="utf-8")
        return {"datei": str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
                "sha256": fingerprint(path), "seiten": len(doc),
                "gerenderte_seiten": selected, "bilderordner": str(out)}


def docx_structure(path: Path) -> dict:
    namespaces = {"m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
                  "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
                  "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"}
    with zipfile.ZipFile(path) as archive:
        document = ET.fromstring(archive.read("word/document.xml"))
        return {"datei": str(path.relative_to(ROOT)), "sha256": fingerprint(path),
                "formeln": len(document.findall(".//m:oMath", namespaces)),
                "bilder": len(document.findall(".//wp:inline", namespaces)),
                "tabellen": len(document.findall(".//w:tbl", namespaces))}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path("/tmp/x2_abnahme_render"))
    parser.add_argument("--word", action="store_true", help="DOCX mit LibreOffice nach PDF konvertieren")
    args = parser.parse_args()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    result = {"hinweis": "Sichtprüfung erforderlich. Word-Ansicht über LibreOffice, nicht Microsoft Word.",
              "pdf": [], "alte_pdf": [], "docx": [], "word_pdf": []}
    for name in NAMES:
        result["pdf"].append(render(WORK / "kaffee" / f"{name}.pdf", out / "pdf" / name))
    result["pdf"].append(render(WORK / "sammlung/ausgabe" / f"{COLLECTION}.pdf",
                                out / "pdf" / COLLECTION, [22, 23, 24, 25, 58]))
    material = ROOT / "pruefung/Kaffee_Pruefpaket_2026-10-23/material"
    for folder, name in [("A_aufgabe", "Kaffee_Aufgabe"), ("B_loesung", "Kaffee_Loesung")]:
        result["alte_pdf"].append(render(material / folder / f"{name}.pdf", out / "alt" / name))
    documents = [WORK / "kaffee" / f"{name}.docx" for name in NAMES]
    documents.append(WORK / "sammlung/ausgabe" / f"{COLLECTION}.docx")
    for path in documents:
        result["docx"].append(docx_structure(path))
        if args.word:
            destination = out / "word_pdf"
            destination.mkdir(exist_ok=True)
            profile = (out / "lo_profile").as_uri()
            command = ["soffice", f"-env:UserInstallation={profile}", "--headless", "--convert-to", "pdf",
                       "--outdir", str(destination), str(path)]
            subprocess.run(command, check=True, capture_output=True, text=True, timeout=180)
            converted = destination / f"{path.stem}.pdf"
            pages = [25, 26, 27, 28] if path.stem == COLLECTION else None
            result["word_pdf"].append(render(converted, out / "word_bilder" / path.stem, pages))
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    (out / "manifest.json").write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
