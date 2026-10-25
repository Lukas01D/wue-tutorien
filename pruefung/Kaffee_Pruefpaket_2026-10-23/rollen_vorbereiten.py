# -*- coding: utf-8 -*-
"""Legt für jede Prüferrolle einen eigenen Ordner mit Auftrag und nur ihrem Material an.

Aufruf:
    python3 rollen_vorbereiten.py <paketordner> <arbeitsordner> [--neu]

<paketordner>    entpacktes Prüfpaket (enthält material/, leseliste.json, 02_PRUEFAUFTRAG.md, 03_ROLLEN.md)
<arbeitsordner>  hier entsteht je Rolle ein Ordner <Kürzel>/ mit
                 AUFTRAG.md (gemeinsamer Prüfauftrag, Rolle, Materialliste, Pfade),
                 material/  (nur die Dateien der Leseliste, Lösung für Rolle S in erst_nach_eigener_rechnung/),
                 notizen/   (für eigene Rechnungen und Bilder);
                 BERICHT.md schreibt der Prüfer selbst.
--neu            ALLE vorhandenen Rollenordner im Arbeitsordner vorher löschen, samt BERICHT.md und notizen/
                 (für eine zweite Runde lieber einen neuen Arbeitsordner angeben, zum Beispiel arbeit_runde2)

Liegt im Paketordner eine Datei feedback_tutoriumsleitung.md, bekommt jede Rolle eine Kopie.
Das Skript endet mit Fehlercode 1, wenn eine Datei der Leseliste fehlt.
"""
import datetime
import json
import os
import re
import shutil
import sys


def lies(pfad):
    with open(pfad, encoding="utf-8") as f:
        return f.read()


def rollen_aus_markdown(text):
    """Abschnitte '## K: Name' aus 03_ROLLEN.md, jeweils bis zur nächsten Überschrift der Ebene 2."""
    teile = {}
    treffer = list(re.finditer(r"(?m)^## ([A-Z]): (.+)$", text))
    for i, m in enumerate(treffer):
        ende = treffer[i + 1].start() if i + 1 < len(treffer) else len(text)
        teile[m.group(1)] = (m.group(2).strip(), text[m.end():ende].strip())
    return teile


def kopiere(src, dst, fehlend):
    if not os.path.exists(src):
        fehlend.append(src)
        return []
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)
    kopiert = [dst]
    if src.endswith(".md"):
        # Bilder, auf die die Markdown-Datei verweist (media/...), mitnehmen
        for rel in sorted(set(re.findall(r"media/[A-Za-z0-9_.-]+\.(?:png|jpe?g|gif|emf|wmf|svg)", lies(src)))):
            s2 = os.path.join(os.path.dirname(src), rel)
            d2 = os.path.join(os.path.dirname(dst), rel)
            if os.path.exists(s2) and not os.path.exists(d2):
                os.makedirs(os.path.dirname(d2), exist_ok=True)
                shutil.copy2(s2, d2)
                kopiert.append(d2)
    return kopiert


def bilder_nachziehen(md_src, md_dst):
    """Bilder, auf die eine Markdown-Datei relativ verweist und die im Rollenordner noch fehlen, mitkopieren."""
    neu = []
    for rel in sorted(set(re.findall(r'(?:\]\(|src=")([^)"\s]+\.(?:png|jpe?g|gif|svg))', lies(md_src)))):
        s2 = os.path.normpath(os.path.join(os.path.dirname(md_src), rel))
        d2 = os.path.normpath(os.path.join(os.path.dirname(md_dst), rel))
        if os.path.exists(s2) and not os.path.exists(d2):
            os.makedirs(os.path.dirname(d2), exist_ok=True)
            shutil.copy2(s2, d2)
            neu.append(d2)
    return neu


def woerter(pfad):
    if pfad.endswith((".md", ".txt", ".py", ".json")):
        try:
            return len(lies(pfad).split())
        except UnicodeDecodeError:
            return 0
    return 0


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 2:
        print(__doc__)
        sys.exit(2)
    paket, ziel = (os.path.abspath(a) for a in args)
    neu = "--neu" in sys.argv
    daten = json.loads(lies(os.path.join(paket, "leseliste.json")))
    liste = daten["rollen"]
    beschreibung = daten.get("beschreibungen", {})
    gemeinsam = re.sub(r"^# .*\n+", "", lies(os.path.join(paket, "02_PRUEFAUFTRAG.md")), count=1)
    rollen = rollen_aus_markdown(lies(os.path.join(paket, "03_ROLLEN.md")))
    feedback = os.path.join(paket, "feedback_tutoriumsleitung.md")
    heute = datetime.date.today().strftime("%d.%m.%Y")
    fehlend, zeilen = [], []

    for k, eintrag in liste.items():
        if k not in rollen:
            fehlend.append(f"Rollentext für {k} fehlt in 03_ROLLEN.md")
            continue
        name, rollentext = rollen[k]
        ordner = os.path.join(ziel, k)
        if os.path.exists(ordner):
            if not neu:
                print(f"Ordner {ordner} gibt es schon; mit --neu neu anlegen.")
                sys.exit(2)
            shutil.rmtree(ordner)
        mat = os.path.join(ordner, "material")
        os.makedirs(mat)
        os.makedirs(os.path.join(ordner, "notizen"))

        dateien = []
        for rel in eintrag["dateien"]:
            dateien += [(p, beschreibung.get(rel, "")) for p in kopiere(os.path.join(paket, "material", rel), os.path.join(mat, rel), fehlend)]
        for rel in eintrag.get("erst_danach", []):
            dateien += [(p, (beschreibung.get(rel, "") + "; erst nach der eigenen Rechnung öffnen").lstrip("; ")) for p in
                        kopiere(os.path.join(paket, "material", rel), os.path.join(mat, "erst_nach_eigener_rechnung", rel), fehlend)]
        if os.path.exists(feedback):
            ziel_fb = os.path.join(mat, "erst_nach_eigener_rechnung" if eintrag.get("erst_danach") else "", "feedback_tutoriumsleitung.md")
            hinweis_fb = "Feedback der Tutoriumsleitung, bitte berücksichtigen" + ("; erst nach der eigenen Rechnung öffnen" if eintrag.get("erst_danach") else "")
            dateien += [(p, hinweis_fb) for p in kopiere(feedback, ziel_fb, fehlend)]
        for rel, unter in [(r, "") for r in eintrag["dateien"]] + [(r, "erst_nach_eigener_rechnung") for r in eintrag.get("erst_danach", [])]:
            if rel.endswith(".md"):
                dateien += [(p, "Bild aus " + os.path.basename(rel)) for p in
                            bilder_nachziehen(os.path.join(paket, "material", rel), os.path.join(mat, unter, rel))]

        tabelle = ["| Datei | Inhalt |", "|---|---|"]
        for p, hinweis in dateien:
            if "/media/" in p:
                continue
            tabelle.append(f"| `{os.path.relpath(p, ordner)}` | {hinweis} |")
        n_media = sum(1 for p, _ in dateien if "/media/" in p)
        if n_media:
            tabelle.append(f"| `material/.../media/` ({n_media} Bilder) | Bilder aus den Lehrstuhlunterlagen |")

        auftrag = (
            f"# Auftrag für Prüfer {k}: {name}\n\n"
            f"> Angelegt am {heute} mit `rollen_vorbereiten.py`. Dein Ordner: `{ordner}`. "
            f"Arbeite nur in diesem Ordner.\n\n"
            + gemeinsam.replace("{KUERZEL}", k).replace("{PRAEFIX}", eintrag.get("praefix", k)).replace("{ORDNER}", ordner).strip() + "\n\n"
            f"## 5. Deine Rolle: {name}\n\n{rollentext}\n\n"
            f"## 6. Dein Material (nur diese Dateien)\n\n" + "\n".join(tabelle) + "\n\n"
            f"## 7. Deine Pfade und Grenzen\n\n"
            f"- Bericht: `{os.path.join(ordner, 'BERICHT.md')}`\n"
            f"- Eigene Rechnungen, Bilder, Notizen: `{os.path.join(ordner, 'notizen')}/`\n"
            + (f"- Websuchen: höchstens {eintrag['websuchen']}\n" if eintrag["websuchen"] else "- Websuchen: keine\n")
        )
        with open(os.path.join(ordner, "AUFTRAG.md"), "w", encoding="utf-8") as f:
            f.write(auftrag)

        w = sum(woerter(p) for p, _ in dateien)
        n_pdf = sum(1 for p, _ in dateien if p.endswith((".pdf", ".docx")))
        n_bild = sum(1 for p, _ in dateien if p.endswith((".png", ".jpg", ".jpeg", ".svg", ".emf", ".wmf", ".gif")))
        zeilen.append(f"{k:2} {name:13} {len(dateien):3} Dateien  {w:6} Wörter Text  {n_pdf:2} PDF/Word  {n_bild:3} Bilder  Websuchen {eintrag['websuchen']:2}")

    print("Rollenordner in", ziel)
    print("\n".join(zeilen))
    if fehlend:
        print("\nFEHLT:")
        for f in fehlend:
            print("  ", f)
        sys.exit(1)
    print("\nAlle Dateien der Leselisten vorhanden.")


if __name__ == "__main__":
    main()
