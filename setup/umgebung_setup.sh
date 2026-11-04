#!/bin/bash
# Setup-Skript für die Cloud-Umgebung „WÜ Tutorien“ (in die Umgebung kopieren, Feld „Setup script“).
# Installiert, was die Kaffee-Prüfung und die Umsetzung brauchen: Pandoc, XeLaTeX, LibreOffice (Writer),
# Poppler, ImageMagick, Schriften (Carlito, Latin Modern Math) und die Python-Pakete der Rechenmodelle.
# texlive-lang-german: deutsche Trennmuster; ohne sie setzt XeLaTeX alle PDFs ohne Silbentrennung (TL 03.11.2026).
set -e
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y -qq --no-install-recommends \
  pandoc texlive-xetex texlive-latex-recommended texlive-latex-extra fonts-lmodern lmodern \
  texlive-plain-generic texlive-fonts-recommended texlive-lang-german \
  fonts-crosextra-carlito fonts-crosextra-caladea poppler-utils imagemagick
apt-get install -y -qq --no-install-recommends libreoffice-writer-nogui || \
  apt-get install -y -qq --no-install-recommends libreoffice-writer
# Word-Formeln bleiben beim Umwandeln nach PDF nur mit LibreOffice Math erhalten
apt-get install -y -qq --no-install-recommends libreoffice-math
python3 -m pip install -q --break-system-packages numpy scipy matplotlib CoolProp || \
  python3 -m pip install -q numpy scipy matplotlib CoolProp
fc-cache -f >/dev/null
# Prüfen, dass XeLaTeX die deutschen Trennmuster kennt (Eintrag „german“ in language.dat)
grep -q "^german" "$(kpsewhich language.dat)" || { echo "Deutsche Trennmuster fehlen"; exit 1; }
echo "Umgebung bereit"
