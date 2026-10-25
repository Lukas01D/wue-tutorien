#!/bin/bash
# Setup-Skript für die Cloud-Umgebung „WÜ Tutorien“ (in die Umgebung kopieren, Feld „Setup script“).
# Installiert, was die Kaffee-Prüfung und die Umsetzung brauchen: Pandoc, XeLaTeX, LibreOffice (Writer),
# Poppler, ImageMagick, Schriften (Carlito, Latin Modern Math) und die Python-Pakete der Rechenmodelle.
set -e
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y -qq --no-install-recommends \
  pandoc texlive-xetex texlive-latex-recommended texlive-latex-extra fonts-lmodern \
  fonts-crosextra-carlito fonts-crosextra-caladea poppler-utils imagemagick
apt-get install -y -qq --no-install-recommends libreoffice-writer-nogui || \
  apt-get install -y -qq --no-install-recommends libreoffice-writer
python3 -m pip install -q --break-system-packages numpy scipy matplotlib CoolProp || \
  python3 -m pip install -q numpy scipy matplotlib CoolProp
fc-cache -f >/dev/null
echo "Umgebung bereit"
