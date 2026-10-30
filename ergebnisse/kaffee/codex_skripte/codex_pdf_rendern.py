"""Original-PDFs als Bilder in eigenem Notizordner rendern, Material nicht verändern."""

from pathlib import Path
import subprocess


def main():
    here = Path(__file__).resolve().parent
    root = here.parents[2]
    material = root / 'pruefung/Kaffee_Pruefpaket_2026-10-23/material'
    output = here / 'pdf_notizen'
    output.mkdir(exist_ok=True)
    for name, prefix in [('A_aufgabe/Kaffee_Aufgabe.pdf', 'aufgabe'),
                         ('B_loesung/Kaffee_Loesung.pdf', 'loesung')]:
        subprocess.run(['pdftoppm', '-r', '110', '-png', str(material / name),
                        str(output / prefix)], check=True)
        print(f'{name}: Bilder in {output}, Präfix {prefix}')


if __name__ == '__main__':
    main()
