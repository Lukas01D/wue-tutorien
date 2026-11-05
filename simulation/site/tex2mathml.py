# -*- coding: utf-8 -*-
"""Kleiner Umsetzer von TeX-Formeln nach MathML für die Kaffee-Seite (zur Bauzeit, keine Laufzeitbibliothek).

Nur der Teil von TeX, den die Texte brauchen: Buchstaben (kursiv), \\mathrm{...} (aufrecht, Ä24), \\text{...}, Zahlen mit
Dezimalkomma 0{,}56 oder Dezimalpunkt 0.56 (eine Zahl), griechische Buchstaben, \\dot, \\frac, \\dfrac, \\exp, \\ln, \\sum,
Hoch- und Tiefstellung, \\cdot, \\, \\quad, \\left( \\right), \\le, \\ge, \\approx, \\to, \\infty, \\times, \\Delta.
Ein unbekannter Befehl ist ein Fehler (damit nichts still falsch gesetzt wird).
"""
import html
import re

GRIECHISCH = {"vartheta": "ϑ", "theta": "θ", "tau": "τ", "rho": "ρ", "alpha": "α", "lambda": "λ", "pi": "π", "varepsilon": "ε",
              "Delta": "Δ"}
GROSS_AUFRECHT = {"Delta"}
OPERATOREN = {"cdot": "·", "le": "≤", "ge": "≥", "approx": "≈", "to": "→", "times": "×", "pm": "±", "infty": "∞", "sum": "∑",
              "rightarrow": "→", "mid": "|"}
FUNKTIONEN = {"exp", "ln", "max", "min"}
LEER = {",": "0.167em", ";": "0.278em", "quad": "1em", "qquad": "2em", "!": "0em"}
TOKEN = re.compile(r"\\[A-Za-z]+|\\[,;!]|\d+(?:\{,\}\d+|[.,]\d+)?|[A-Za-z]|\{|\}|\^|_|\s+|.", re.S)


class Fehler(ValueError):
    pass


def _tokens(tex):
    return [t for t in TOKEN.findall(tex) if not t.isspace()]


class _Leser:
    def __init__(self, tex):
        self.t = _tokens(tex)
        self.i = 0

    def ende(self):
        return self.i >= len(self.t)

    def sieh(self):
        return self.t[self.i] if self.i < len(self.t) else None

    def nimm(self):
        t = self.t[self.i]
        self.i += 1
        return t

    def gruppe_roh(self):
        """Inhalt einer {...}-Gruppe als Text (für \\mathrm und \\text)."""
        if self.nimm() != "{":
            raise Fehler("{ erwartet")
        tiefe, teile = 1, []
        while True:
            t = self.nimm()
            if t == "{":
                tiefe += 1
            elif t == "}":
                tiefe -= 1
                if tiefe == 0:
                    break
            teile.append(t)
        return "".join(teile).replace("{,}", ",").replace("\\,", " ")

    def argument(self):
        if self.sieh() == "{":
            self.nimm()
            inhalt = self.folge(ende="}")
            self.nimm()
            return "<mrow>" + inhalt + "</mrow>"
        return self.atom()

    def atom(self):
        t = self.nimm()
        if t == "{":
            inhalt = self.folge(ende="}")
            self.nimm()
            return "<mrow>" + inhalt + "</mrow>"
        if re.fullmatch(r"\d+(?:\{,\}\d+|[.,]\d+)?", t):
            return "<mn>" + t.replace("{,}", ",") + "</mn>"
        if re.fullmatch(r"[A-Za-z]", t):
            return "<mi>" + t + "</mi>"
        if t.startswith("\\"):
            n = t[1:]
            if n in ("mathrm", "text"):
                roh = self.gruppe_roh()
                if n == "text":
                    return "<mtext>" + html.escape(roh) + "</mtext>"
                return '<mi mathvariant="normal">' + html.escape(roh) + "</mi>"
            if n in GRIECHISCH:
                if n in GROSS_AUFRECHT:
                    return '<mi mathvariant="normal">' + GRIECHISCH[n] + "</mi>"
                return "<mi>" + GRIECHISCH[n] + "</mi>"
            if n in OPERATOREN:
                return "<mo>" + OPERATOREN[n] + "</mo>"
            if n in FUNKTIONEN:
                return "<mi>" + n + "</mi><mo>&#x2061;</mo>"
            if n in ("frac", "dfrac"):
                z, nn = self.argument(), self.argument()
                if n == "dfrac":
                    return '<mstyle displaystyle="true"><mfrac>' + z + nn + "</mfrac></mstyle>"
                return "<mfrac>" + z + nn + "</mfrac>"
            if n == "dot":
                return '<mover accent="true">' + self.argument() + '<mo class="punkt">˙</mo></mover>'
            if n in LEER or t[1:] in LEER:
                return '<mspace width="' + LEER[t[1:]] + '"/>'
            if n in ("left", "right"):
                return "<mo>" + html.escape(self.nimm()) + "</mo>"
            raise Fehler("unbekannter Befehl " + t)
        if t in "+=<>()[]/|,;:!'.":
            return "<mo>" + html.escape(t) + "</mo>"
        if t == "-":
            return "<mo>−</mo>"
        if t in ("−", "·", "≤", "≥", "≈", "→", "°", "%"):
            return "<mo>" + t + "</mo>" if t != "°" else "<mi mathvariant=\"normal\">°</mi>"
        raise Fehler("unerwartetes Zeichen " + repr(t))

    def folge(self, ende=None):
        teile = []
        while not self.ende() and self.sieh() != ende:
            basis = self.atom()
            unten = oben = None
            while self.sieh() in ("_", "^"):
                op = self.nimm()
                arg = self.argument()
                if op == "_":
                    unten = arg
                else:
                    oben = arg
            if unten and oben:
                basis = "<msubsup>" + basis + unten + oben + "</msubsup>"
            elif unten:
                basis = "<msub>" + basis + unten + "</msub>"
            elif oben:
                basis = "<msup>" + basis + oben + "</msup>"
            teile.append(basis)
        return "".join(teile)


def tex_zu_mathml(tex, block=False):
    l = _Leser(tex)
    inhalt = l.folge()
    if not l.ende():
        raise Fehler("Rest nicht gelesen: " + "".join(l.t[l.i:]))
    anz = ' display="block"' if block else ""
    return '<math' + anz + '><mrow>' + inhalt + "</mrow></math>"


def ersetze_formeln(text):
    """$$...$$ als abgesetzte Formel, $...$ im Satz."""
    text = re.sub(r"\$\$(.+?)\$\$", lambda m: tex_zu_mathml(m.group(1), block=True), text, flags=re.S)
    return re.sub(r"\$(.+?)\$", lambda m: tex_zu_mathml(m.group(1)), text, flags=re.S)


if __name__ == "__main__":
    for f in [r"\dot{Q}_\mathrm{ab} = kA\,(\vartheta - \vartheta_\mathrm{u})", r"\frac{\mathrm{W}}{\mathrm{K}}",
              r"C_\mathrm{G}(\vartheta_1 - \vartheta_2) = Q_2 - Q_1 + m_\mathrm{M} c_{p,\mathrm{M}}(\vartheta_\mathrm{M1} - \vartheta_\mathrm{M2})",
              r"\ln\frac{\vartheta - \vartheta_\mathrm{u}}{\vartheta_0 - \vartheta_\mathrm{u}}", r"0{,}56\,kA", r"b = \sum t_i y_i / \sum t_i^2",
              r"T(t) = T_\mathrm{u} + (T_0 - T_\mathrm{u}) \exp\left(-\frac{kA}{C}\,t\right)", r"\vartheta_\mathrm{K,0}", r"t_\mathrm{Z}"]:
        print(f, "\n   ", tex_zu_mathml(f))
