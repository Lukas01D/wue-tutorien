#!/bin/bash
# Baut alle drei Entwürfe und prüft sie (Schritt 4 nach DESIGN_AUFTRAG.md). Aufruf vom Repository aus:
#   bash simulation/design_entwuerfe/tests/alle_pruefen.sh
# Ergebnisse: simulation/design_entwuerfe/<entwurf>/test_ergebnisse/ und simulation/design_entwuerfe/tests/vergleich_kern_texte.txt
set -u
cd "$(dirname "$0")/../../.."
E=simulation/design_entwuerfe
declare -A TEXT=([messprotokoll]="Plex Sans" [kaffeehaus]="Source Sans 3" [hoersaal]="Atkinson Hyperlegible Next")
declare -A FORMEL=([messprotokoll]="Plex Math" [kaffeehaus]="STIX Two Math" [hoersaal]="Fira Math")
declare -A FETT=([messprotokoll]=600 [kaffeehaus]=600 [hoersaal]=700)
for n in messprotokoll kaffeehaus hoersaal; do
  python3 $E/bauen_entwurf.py $n | head -1
  mkdir -p $E/$n/test_ergebnisse
  python3 simulation/tests/test_kern.py --html $E/$n/index.html > $E/$n/test_ergebnisse/test_kern_html.txt 2>&1; tail -1 $E/$n/test_ergebnisse/test_kern_html.txt
  KAFFEE_ORDNER=$PWD/$E/$n KAFFEE_SCHRIFT_TEXT="${TEXT[$n]}" KAFFEE_SCHRIFT_FORMEL="${FORMEL[$n]}" KAFFEE_SCHRIFT_FETT=${FETT[$n]} \
    node $E/tests/browsertest_entwurf.js > /dev/null 2>&1; tail -1 $E/$n/test_ergebnisse/browsertest.txt
done
python3 $E/tests/vergleich_kern_texte.py > $E/tests/vergleich_kern_texte.txt; tail -1 $E/tests/vergleich_kern_texte.txt
