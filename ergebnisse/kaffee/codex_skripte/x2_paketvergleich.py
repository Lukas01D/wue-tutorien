#!/usr/bin/env python3
"""Reproduziert vorhandene Ausgaben in /tmp und vergleicht die Textfassungen.

Dies ist ein Konsistenzcheck, kein unabhaengiger Zahlenbeweis.
Die unabhaengige Rechnung steht in x2_eigenrechnung.py.
Aufruf: python ergebnisse/kaffee/codex_skripte/x2_paketvergleich.py
"""

import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / 'pruefung/Kaffee_Pruefpaket_2026-10-23/umsetzung/Arbeitsordner'
KAFFEE = WORK / 'kaffee'
SAMMLUNG = WORK / 'sammlung'


def task_text(text):
    text = text.split('**[Ausgangssituation]{.underline}**', 1)[1]
    text = text.split('**[Lösung]{.underline}**', 1)[0]
    text = text.replace('::: seitenumbruch\n:::', '')
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    return re.sub(r'\s+', ' ', text).strip()


def without_layout(text):
    text = text.replace('::: seitenumbruch\n:::', '')
    text = re.sub(r'```\{=latex\}\s*\\needspace\{7\\baselineskip\}\s*```', '', text)
    return re.sub(r'\s+', ' ', text).strip()


def main():
    checks = 0

    def verify(name, actual, expected):
        nonlocal checks
        if actual != expected:
            raise AssertionError(name)
        checks += 1
        print(f'OK | {name}')

    verify('Kaffee- und Sammlungsmodell bytegleich',
           (KAFFEE / 'kaffee_modell.py').read_bytes(),
           (SAMMLUNG / 'rechnung/kaffee_modell.py').read_bytes())
    assignment = (KAFFEE / 'Kaffee_Aufgabe.md').read_text()
    solution = (KAFFEE / 'Kaffee_Loesung.md').read_text()
    student = (KAFFEE / 'Kaffee_Loesung_Studierende.md').read_text()
    collection = (SAMMLUNG / 'teile/t5a_kaffee.md').read_text()
    for name, text in [('Lehrloesung', solution), ('Studierendenloesung', student),
                       ('Sammlungsteil', collection)]:
        verify(f'Aufgabentext konsistent: {name}', task_text(text), task_text(assignment))
    marker = '**[Hinweise für die Tutoriumsleitung]{.underline}**'
    sources = '**[Quellen der Arbeitswerte]{.underline}**'
    verify('Studierendenloesung ohne TL-Hinweise', marker in student, False)
    verify('Studierendenloesung ohne zusaetzliche TL-Frage', 'Zusatzfrage für Schnelle' in student, False)
    verify('Loesungsteil fuer Studierende vollstaendig',
           without_layout(solution.split('**[Lösung]{.underline}**')[1].split(marker)[0]),
           without_layout(student.split('**[Lösung]{.underline}**')[1].split(sources)[0]))
    verify('Quellenblock in beiden Loesungen gleich',
           solution.split(sources)[1].strip(), student.split(sources)[1].strip())

    with tempfile.TemporaryDirectory(prefix='x2_paketvergleich_') as temp:
        base = Path(temp)
        coffee = base / 'kaffee'
        calculations = base / 'sammlung/rechnung'
        parts = base / 'sammlung/teile'
        for path in [coffee, calculations, parts]:
            path.mkdir(parents=True)
        for name in ['kaffee_modell.py', 'nachrechnung_kaffee.py']:
            shutil.copy2(KAFFEE / name, coffee / name)
        for name in ['kaffee_modell.py', 't5_kaffee_teil.py']:
            shutil.copy2(SAMMLUNG / 'rechnung' / name, calculations / name)
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
        run = subprocess.run([sys.executable, '-B', str(coffee / 'nachrechnung_kaffee.py')],
                             cwd=coffee, env=env, check=True, capture_output=True, text=True)
        verify('Nachrechnung reproduziert gespeicherte Ausgabe bytegenau',
               run.stdout, (KAFFEE / 'nachrechnung_kaffee_ausgabe.txt').read_text())
        subprocess.run([sys.executable, '-B', str(calculations / 't5_kaffee_teil.py')],
                       cwd=calculations, env=env, check=True, capture_output=True, text=True)
        verify('Sammlungsgenerator reproduziert Kaffee-Teil bytegenau',
               (parts / 't5a_kaffee.md').read_bytes(), (SAMMLUNG / 'teile/t5a_kaffee.md').read_bytes())
        verify('Sammlungsgenerator reproduziert Zahlenausgabe bytegenau',
               (calculations / 't5_kaffee_ausgabe.txt').read_bytes(),
               (SAMMLUNG / 'rechnung/t5_kaffee_ausgabe.txt').read_bytes())
        stale = [line.strip() for line in run.stdout.splitlines() if 'Typischer Fehler f:' in line]
        for line in stale:
            print(f'BEFUND | S2-Folgefehler: {line} (muss Teil g heissen)')

    print(f'\n{checks}/{checks} Konsistenzchecks bestanden. Bekannte Beschriftungsbefunde stehen im Bericht.')


if __name__ == '__main__':
    main()
