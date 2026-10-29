"""Erst nach der Eigenrechnung ausführen: geliefertes Modell kopieren und vergleichen."""

import hashlib
import importlib.util
from pathlib import Path
import shutil
import subprocess

from codex_eigenrechnung import rechnen
from codex_zusatzpruefung import zusatz


def main():
    here = Path(__file__).resolve().parent
    root = here.parents[2]
    material = root / 'pruefung/Kaffee_Pruefpaket_2026-10-23/material'
    original = material / 'C_modell'
    copies = here / 'paketvergleich'
    copies.mkdir(exist_ok=True)
    for name in ['kaffee_modell.py', 'nachrechnung_kaffee.py']:
        shutil.copy2(original / name, copies / name)
    result = subprocess.run(['python', 'nachrechnung_kaffee.py'], cwd=copies,
                            capture_output=True, text=True, check=True)
    (copies / 'nachrechnung_kaffee_ausgefuehrt.txt').write_text(result.stdout)
    assert result.stdout == (original / 'nachrechnung_kaffee_ausgabe.txt').read_text()
    print('Paketlauf stimmt exakt mit mitgelieferter Textausgabe überein: True')
    spec = importlib.util.spec_from_file_location('kopiertes_paketmodell', copies / 'kaffee_modell.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    r = rechnen()
    p = module.rechne()
    pairs = {
        'T1_0': 'a_theta_1_0_C', 'T1': 'd_theta_1_C', 'T2': 'd_theta_2_C',
        'T2_K': 'd_theta_2_vor_Milch_C', 'kA': 'c_kA_W_pro_K',
        'dT': 'd_Differenz_K', 'tau_K': 'tau_K_s', 'tau_G': 'tau_1_s',
        'th_M_gleich': 'h1_Kipptemperatur_C',
    }
    for key, own in pairs.items():
        value = p[key] - (273.15 if key in ['T1_0', 'T1', 'T2', 'T2_K'] else 0)
        assert abs(value - r[own]) < 1e-9, key
    assert abs(p['Q1'] / 1000 - r['e_Q1_kJ']) < 1e-9
    assert abs(p['Q2'] / 1000 - r['e_Q2_kJ']) < 1e-9
    b = module.becher()
    assert abs(b['kA'] - r['f_kA_W_pro_K']) < 1e-9
    assert abs(b['T1'] - 273.15 - r['f_theta_1_C']) < 1e-9
    assert abs(b['T2'] - 273.15 - r['f_theta_2_C']) < 1e-9
    hot = module.rechne(dict(module.P, th_M=60.0))
    assert abs(hot['T1'] - 273.15 - r['g_theta_1_C']) < 1e-9
    assert abs(hot['T2'] - 273.15 - r['g_theta_2_C']) < 1e-9
    print('Lineare Kernzahlen und Becher-/Heißmilchvariante: Übereinstimmung < 1e-9 in jeweiliger Einheit.')
    for row in zusatz()['Nichtlinear_exakt']:
        first, second = module.nichtlinear(row['n'])
        print(f"n={row['n']:.8f}: Euler minus exakt, T1={first-273.15-row['theta_1_C']:.8f} K, "
              f"T2={second-273.15-row['theta_2_C']:.8f} K")
    print('\nSHA256 der geprüften Kerndateien:')
    for name in [
        'A_aufgabe/Kaffee_Aufgabe.md', 'A_aufgabe/Kaffee_Aufgabe.pdf',
        'B_loesung/Kaffee_Loesung.md', 'B_loesung/Kaffee_Loesung.pdf',
        'C_modell/kaffee_modell.py', 'C_modell/nachrechnung_kaffee.py',
    ]:
        print(hashlib.sha256((material / name).read_bytes()).hexdigest(), name)


if __name__ == '__main__':
    main()
