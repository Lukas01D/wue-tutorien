#!/usr/bin/env bash
# A5: Bau und Veröffentlichung (Aufarbeitung vom 12.11.2026).
# Baut beide Seiten zweimal in einen leeren Ordner, vergleicht die Bytes miteinander und mit den Dateien im Repository
# und mit der Prüfsumme, die Codex für Sites-Version 5 nachgewiesen hat. Ändert nichts im Repository.
# Aufruf: bash simulation/aufarbeitung/a5_bau.sh   (Ausgabe nach ergebnisse/a5_bau.txt)
set -euo pipefail
HIER="$(cd "$(dirname "$0")" && pwd)"
SIM="$(dirname "$HIER")"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
VERSION5="5ffb4424171c40c426907b2cf25e484c3ecb8c56d7e5ac9a502966eb5b4bc034"   # Nachweis Codex, Zweig codex/kaffee-schlank-nachbesserung-veroeffentlichung
{
  echo "A5: Bau und Veröffentlichung"
  echo "Commit: $(git -C "$SIM" rev-parse --short HEAD)"
  echo
  mkdir -p "$TMP/a" "$TMP/b"
  for d in a b; do
    python3 "$SIM/site/bauen.py" --ziel "$TMP/$d" > /dev/null
    python3 "$SIM/minimal/bauen_minimal.py" --ziel "$TMP/$d/schlank.html" > /dev/null
  done
  for f in index.html schlank.html; do
    a=$(sha256sum "$TMP/a/$f" | cut -c1-64); b=$(sha256sum "$TMP/b/$f" | cut -c1-64)
    echo "$f: zwei Bauten $( [ "$a" = "$b" ] && echo gleich || echo VERSCHIEDEN ) ($a)"
  done
  r1=$(sha256sum "$SIM/site/index.html" | cut -c1-64); r2=$(sha256sum "$SIM/minimal/Kaffee_Simulation_schlank.html" | cut -c1-64)
  echo "Hauptseite im Repository gleich dem Bau: $( [ "$r1" = "$(sha256sum "$TMP/a/index.html" | cut -c1-64)" ] && echo ja || echo NEIN )"
  echo "Schlanke Seite im Repository gleich dem Bau: $( [ "$r2" = "$(sha256sum "$TMP/a/schlank.html" | cut -c1-64)" ] && echo ja || echo NEIN )"
  echo "Schlanke Seite gleich Sites-Version 5 (Nachweis Codex): $( [ "$r2" = "$VERSION5" ] && echo ja || echo NEIN )"
  echo "Fuß der schlanken Seite: $(grep -o '"stand":"[^"]*","version":"[^"]*"' "$SIM/minimal/Kaffee_Simulation_schlank.html")"
  echo "Größe der schlanken Seite: $(wc -c < "$SIM/minimal/Kaffee_Simulation_schlank.html") Bytes"
  python3 - "$SIM/minimal/Kaffee_Simulation_schlank.html" <<'PY'
import re, sys
h = open(sys.argv[1], encoding="utf-8").read()
js = h[h.index("<script>") + 8:h.index("</script>")]
css = h[h.index("<style>") + 7:h.index("</style>")]
schrift = sum(len(m) for m in re.findall(r"url\(data:font/woff2;base64,[^)]*\)", css))
texte = js[js.index("const TEXTE = "):js.index("\nconst BAU")]
print("Anteile: Skript %d Zeichen (davon Texte %d), Stil %d Zeichen (davon Schriften %d)" % (len(js), len(texte), len(css), schrift))
PY
} | tee "$HIER/ergebnisse/a5_bau.txt"
