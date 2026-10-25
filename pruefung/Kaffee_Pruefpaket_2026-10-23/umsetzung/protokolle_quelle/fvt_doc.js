// Gemeinsame Bausteine für die FVT-Dokumente der Tutoriumsplanung (aus build_doc.js vom 16.10.2026 übernommen).
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, AlignmentType,
  BorderStyle, ShadingType, ImageRun, Header, Footer, PageNumber, HeadingLevel, LevelFormat,
  VerticalAlign, TabStopType, Tab, ExternalHyperlink, LineRuleType,
} = require("docx");
const LR = LineRuleType.AUTO;

const HERE = __dirname;
let GRAF = path.join(HERE, "grafik");
const setGraf = (p) => { GRAF = p; };

// ------------------------------------------------------------------ Stil --
const FONT = "Segoe UI";
const BLUE = "0025AA";
const PETROL = "23A9C9";
const TEXT = "1F1F1F";
const GREY = "4A4F63";
const LINE = "C9D3EE";
const BOX = "EEF1FB";
const BOX_T = "E8F7FA";
const ZEBRA = "F6F8FC";
const W = 9070; // Textbreite in DXA (A4, 2,5 cm Rand links und rechts)

// ------------------------------------------------------ Mini-Auszeichnung --
// **fett**  *kursiv*  ~~gestrichen~~  ++neu (fett, blau)++  _{tief}  ^{hoch}  _{*kursiv tief*}
function runs(text, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+?\*\*|~~[^~]+?~~|\+\+[^+]+?\+\+|_\{[^}]*\}|\^\{[^}]*\}|\*[^*]+?\*)/g;
  let last = 0;
  let m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) out.push(new TextRun({ ...base, text: text.slice(last, m.index) }));
    const t = m[0];
    if (t.startsWith("**")) out.push(new TextRun({ ...base, text: t.slice(2, -2), bold: true }));
    // gestrichene und neue Passagen: innere Auszeichnung (kursiv, tief- und hochgestellt) bleibt erhalten
    else if (t.startsWith("~~")) out.push(...runs(t.slice(2, -2), { ...base, strike: true, color: "8A8F9E" }));
    else if (t.startsWith("++")) out.push(...runs(t.slice(2, -2), { ...base, bold: true, color: BLUE }));
    else if (t.startsWith("_{") || t.startsWith("^{")) {
      const inner = t.slice(2, -1);
      const pos = t.startsWith("_{") ? { subScript: true } : { superScript: true };
      if (inner === "*" || !inner.includes("*")) {
        out.push(new TextRun({ ...base, ...pos, text: inner }));
      } else {
        // kursive Teile innerhalb von Hoch- und Tiefstellung: *x*
        inner.split(/(\*[^*]+\*)/).filter((x) => x.length).forEach((part) => {
          if (part.length > 2 && part.startsWith("*") && part.endsWith("*")) {
            out.push(new TextRun({ ...base, ...pos, text: part.slice(1, -1), italics: true }));
          } else {
            out.push(new TextRun({ ...base, ...pos, text: part }));
          }
        });
      }
    } else out.push(new TextRun({ ...base, text: t.slice(1, -1), italics: true }));
    last = m.index + t.length;
  }
  if (last < text.length) out.push(new TextRun({ ...base, text: text.slice(last) }));
  return out;
}

// -------------------------------------------------------------- Absätze --
const P = (text, o = {}) => new Paragraph({
  alignment: o.align || AlignmentType.JUSTIFIED,
  spacing: { before: o.before ?? 60, after: o.after ?? 60, line: o.line ?? 276, lineRule: LR },
  keepNext: o.keepNext || false,
  children: runs(text, { size: o.size, color: o.color, bold: o.bold }),
});
const Small = (text, o = {}) => P(text, { size: 17, color: GREY, align: AlignmentType.LEFT, ...o });
const H1 = (text, o = {}) => new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: o.newPage || false, children: runs(text) });
const H2 = (text) => new Paragraph({ heading: HeadingLevel.HEADING_2, children: runs(text) });
const Bullet = (text, o = {}) => new Paragraph({
  numbering: { reference: o.ref || "bullets", level: o.level || 0 },
  alignment: AlignmentType.LEFT,
  spacing: { before: 30, after: 30, line: 264, lineRule: LR },
  children: runs(text, { size: o.size, color: o.color }),
});
const Spacer = (after = 80) => new Paragraph({ spacing: { before: 0, after, line: 240, lineRule: LR }, children: [] });

// -------------------------------------------------------------- Tabellen --
const NONE = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const THIN = { style: BorderStyle.SINGLE, size: 4, color: LINE };
const allBorders = (b) => ({ top: b, bottom: b, left: b, right: b });

function cell(content, o = {}) {
  const items = Array.isArray(content) ? content : [content];
  const children = items.map((c) => (c instanceof Paragraph ? c : new Paragraph({
    keepNext: o.keepNext || false,
    alignment: o.align || AlignmentType.LEFT,
    spacing: { before: 10, after: 10, line: 252, lineRule: LR },
    children: runs(String(c), { size: o.size ?? 17, bold: o.bold, color: o.color }),
  })));
  return new TableCell({
    width: { size: o.width, type: WidthType.DXA },
    shading: o.fill ? { fill: o.fill, type: ShadingType.CLEAR, color: "auto" } : undefined,
    margins: { top: o.mt ?? 60, bottom: o.mb ?? 60, left: o.ml ?? 100, right: o.mr ?? 100 },
    verticalAlign: o.valign || VerticalAlign.TOP,
    borders: o.borders || allBorders(THIN),
    children,
  });
}

function grid(headers, rows, widths, o = {}) {
  const sum = widths.reduce((a, b) => a + b, 0);
  const trs = [];
  if (headers) {
    trs.push(new TableRow({
      tableHeader: true,
      cantSplit: true,
      children: headers.map((h, i) => cell(h, { width: widths[i], fill: BLUE, color: "FFFFFF", bold: true, size: 17 })),
    }));
  }
  rows.forEach((r, ri) => {
    trs.push(new TableRow({
      cantSplit: true,
      children: r.map((c, i) => cell(c, {
        width: widths[i],
        fill: (o.firstColFill && i === 0) ? BOX : (o.zebra !== false && ri % 2 === 1 ? ZEBRA : undefined),
        bold: o.firstColBold && i === 0,
        color: o.firstColBold && i === 0 ? BLUE : undefined,
        size: o.size,
      })),
    }));
  });
  return new Table({ width: { size: sum, type: WidthType.DXA }, columnWidths: widths, rows: trs });
}

function box(paragraphs, o = {}) {
  const fill = o.fill || BOX;
  const edge = o.edge || BLUE;
  return new Table({
    width: { size: W, type: WidthType.DXA },
    columnWidths: [W],
    rows: [new TableRow({
      cantSplit: o.cantSplit ?? true,
      children: [new TableCell({
        width: { size: W, type: WidthType.DXA },
        shading: { fill, type: ShadingType.CLEAR, color: "auto" },
        margins: { top: 110, bottom: 110, left: 220, right: 180 },
        borders: { top: NONE, bottom: NONE, right: NONE, left: { style: BorderStyle.SINGLE, size: 24, color: edge } },
        children: paragraphs,
      })],
    })],
  });
}

const boxTitle = (text, color = BLUE) => new Paragraph({
  spacing: { before: 0, after: 60 }, keepNext: true,
  children: [new TextRun({ text, bold: true, color, size: 21 })],
});
const boxPara = (text, o = {}) => new Paragraph({
  alignment: AlignmentType.LEFT, spacing: { before: 30, after: 30, line: 264, lineRule: LR },
  children: runs(text, { size: o.size, color: o.color }),
});

// --------------------------------------------------------- Lernziel-Block --
function zieleTabelle(ziele) {
  const wl = 1500;
  const wr = W - wl;
  return new Table({
    width: { size: W, type: WidthType.DXA },
    columnWidths: [wl, wr],
    rows: ziele.map(([label, stufe, text]) => new TableRow({
      cantSplit: true,
      children: [
        new TableCell({
          width: { size: wl, type: WidthType.DXA },
          shading: { fill: BOX, type: ShadingType.CLEAR, color: "auto" },
          margins: { top: 80, bottom: 80, left: 120, right: 100 },
          borders: allBorders(THIN),
          verticalAlign: VerticalAlign.CENTER,
          children: [
            new Paragraph({ keepNext: true, spacing: { before: 0, after: 0 }, children: [new TextRun({ text: label, bold: true, color: BLUE, size: 19 })] }),
            new Paragraph({ keepNext: true, spacing: { before: 0, after: 0 }, children: [new TextRun({ text: stufe, color: GREY, size: 15 })] }),
          ],
        }),
        new TableCell({
          width: { size: wr, type: WidthType.DXA },
          margins: { top: 80, bottom: 80, left: 140, right: 120 },
          borders: allBorders(THIN),
          verticalAlign: VerticalAlign.CENTER,
          children: [new Paragraph({ keepNext: true, spacing: { before: 0, after: 0, line: 264, lineRule: LR }, children: runs(text, { size: 20 }) })],
        }),
      ],
    })),
  });
}

function bezugTabelle(rows) {
  const wl = 1500;
  const wr = W - wl;
  const b = allBorders(NONE);
  return new Table({
    width: { size: W, type: WidthType.DXA },
    columnWidths: [wl, wr],
    rows: rows.map(([k, v], i) => new TableRow({
      cantSplit: true,
      children: [
        cell(`**${k}**`, { width: wl, size: 16, color: GREY, borders: b, mt: 15, mb: 15, ml: 0, keepNext: i < rows.length - 1 }),
        cell(v, { width: wr, size: 16, color: GREY, borders: b, mt: 15, mb: 15, keepNext: i < rows.length - 1 }),
      ],
    })),
  });
}

function block(children) {
  // Eine Tabellenzeile, die nicht über Seiten umbrechen darf, hält den Block zusammen (Word und LibreOffice).
  return new Table({
    width: { size: W, type: WidthType.DXA },
    columnWidths: [W],
    rows: [new TableRow({
      cantSplit: true,
      children: [new TableCell({
        width: { size: W, type: WidthType.DXA },
        margins: { top: 0, bottom: 0, left: 0, right: 0 },
        borders: allBorders(NONE),
        children: [...children, new Paragraph({ spacing: { before: 0, after: 0, line: 240, lineRule: LR }, children: [] })],
      })],
    })],
  });
}

function tutorium(t) {
  const out = [H2(t.titel)];
  if (t.vorher) out.push(...t.vorher);
  const inner = [];
  inner.push(zieleTabelle([
    ["Ziel 1", t.stufe1 || "Anwenden", t.z1],
    ["Ziel 2", "Bewerten (Prüfen)", t.z2],
  ]));
  inner.push(new Paragraph({ keepNext: true, spacing: { before: 0, after: 60, line: 240, lineRule: LR }, children: [] }));
  inner.push(box([new Paragraph({
    keepNext: true,
    alignment: AlignmentType.LEFT, spacing: { before: 0, after: 0, line: 264, lineRule: LR },
    children: runs(`**Vorab-Frage:** ${t.frage}`, { size: 20 }),
  })], { fill: BOX_T, edge: PETROL }));
  inner.push(P(`**Auflösung für die Tutoriumsleitung:** ${t.antwort}`, { size: 17, color: GREY, before: 80, after: 60, keepNext: true }));
  inner.push(bezugTabelle([["Vorlesung", t.vorlesung], ["Modulhandbuch", t.modul], ["Grafik", t.grafik]]));
  out.push(block(inner));
  return out;
}

// ------------------------------------------------------------- Bilder --
const img = (p) => fs.readFileSync(path.join(GRAF, p));
function grafik(name, widthPx, ratio) {
  return new ImageRun({
    type: "svg",
    data: img(`${name}.svg`),
    fallback: { type: "png", data: img(`${name}.png`) },
    transformation: { width: widthPx, height: Math.round(widthPx * ratio) },
  });
}

function grafikPfad(datei, widthPx, ratio) {
  // datei ohne Endung, absoluter Pfad oder relativ zu GRAF
  const basis = path.isAbsolute(datei) ? datei : path.join(GRAF, datei);
  return new ImageRun({
    type: "svg",
    data: fs.readFileSync(`${basis}.svg`),
    fallback: { type: "png", data: fs.readFileSync(`${basis}.png`) },
    transformation: { width: widthPx, height: Math.round(widthPx * ratio) },
  });
}

// ------------------------------------------------------- Kopf und Fuß --
function makeHeader() {
  return new Header({
    children: [new Paragraph({
      tabStops: [{ type: TabStopType.RIGHT, position: W }],
      spacing: { before: 0, after: 0, line: 240, lineRule: LR },
      children: [
        new ImageRun({ type: "jpg", data: fs.readFileSync(path.join(HERE, "logo_upb.jpg")), transformation: { width: 118, height: 48 } }),
        new TextRun({ children: [new Tab()] }),
        new ImageRun({ type: "jpg", data: fs.readFileSync(path.join(HERE, "logo_fvt.jpg")), transformation: { width: 118, height: 48 } }),
      ],
    })],
  });
}

function makeFooter(text) {
  return new Footer({
    children: [new Paragraph({
      tabStops: [{ type: TabStopType.RIGHT, position: W }],
      border: { top: { style: BorderStyle.SINGLE, size: 4, color: LINE, space: 4 } },
      spacing: { before: 0, after: 0 },
      children: [
        new TextRun({ text, bold: true, size: 16, color: GREY }),
        new TextRun({ children: [new Tab(), "Seite ", PageNumber.CURRENT, " von ", PageNumber.TOTAL_PAGES], size: 16, color: GREY }),
      ],
    })],
  });
}

// Literaturtabelle mit Link und Prüfspalte
function refTable(rows, wl = 7470) {
  const wr = W - wl;
  return new Table({
    width: { size: W, type: WidthType.DXA },
    columnWidths: [wl, wr],
    rows: [
      new TableRow({ tableHeader: true, children: [cell("Quelle", { width: wl, fill: BLUE, color: "FFFFFF", bold: true }), cell("Geprüft", { width: wr, fill: BLUE, color: "FFFFFF", bold: true })] }),
      ...rows.map(([txt, url, chk], i) => new TableRow({
        cantSplit: true,
        children: [
          new TableCell({
            width: { size: wl, type: WidthType.DXA },
            shading: i % 2 ? { fill: ZEBRA, type: ShadingType.CLEAR, color: "auto" } : undefined,
            margins: { top: 50, bottom: 50, left: 100, right: 100 },
            borders: allBorders(THIN),
            children: [new Paragraph({
              spacing: { before: 0, after: 0, line: 252, lineRule: LR },
              indent: { left: 280, hanging: 280 },
              children: [
                ...runs(txt, { size: 16 }),
                ...(url ? [new TextRun({ text: " ", size: 16 }), new ExternalHyperlink({ link: url, children: [new TextRun({ text: url, size: 16, color: BLUE, underline: {} })] })] : []),
              ],
            })],
          }),
          cell(chk, { width: wr, size: 16, fill: i % 2 ? ZEBRA : undefined }),
        ],
      })),
    ],
  });
}

// Zweispaltige Schlüssel-Wert-Tabelle ohne Rahmen (z. B. Bezüge)
function kv(rows, wl = 1700) {
  const wr = W - wl;
  const b = allBorders(NONE);
  return new Table({
    width: { size: W, type: WidthType.DXA },
    columnWidths: [wl, wr],
    rows: rows.map(([k, v], i) => new TableRow({
      cantSplit: true,
      children: [
        cell(`**${k}**`, { width: wl, size: 17, color: GREY, borders: b, mt: 20, mb: 20, ml: 0, keepNext: i < rows.length - 1 }),
        cell(v, { width: wr, size: 17, borders: b, mt: 20, mb: 20, keepNext: i < rows.length - 1 }),
      ],
    })),
  });
}

function makeDoc({ title, description, footerText, children, landscape = false }) {
  return new Document({
    creator: "Tutorium Wärmeübertragung",
    title,
    description,
    styles: {
      default: {
        document: {
          run: { font: FONT, size: 20, color: TEXT, language: { value: "de-DE" } },
          paragraph: { spacing: { before: 60, after: 60, line: 276, lineRule: LR } },
        },
      },
      paragraphStyles: [
        { id: "Title", name: "Title", basedOn: "Normal", next: "Normal", run: { font: FONT, size: 36, bold: true, color: BLUE }, paragraph: { spacing: { before: 0, after: 80, line: 240, lineRule: LR } } },
        { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: 30, bold: true, color: BLUE }, paragraph: { spacing: { before: 360, after: 120, line: 240, lineRule: LR }, keepNext: true, keepLines: true, outlineLevel: 0 } },
        { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: 23, bold: true, color: BLUE }, paragraph: { spacing: { before: 280, after: 100, line: 240, lineRule: LR }, keepNext: true, keepLines: true, outlineLevel: 1 } },
        { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: 20, bold: true, color: BLUE }, paragraph: { spacing: { before: 200, after: 60, line: 240, lineRule: LR }, keepNext: true, keepLines: true, outlineLevel: 2 } },
      ],
    },
    numbering: {
      config: [
        {
          reference: "bullets",
          levels: [
            { level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 240 } }, run: { color: BLUE } } },
            { level: 1, format: LevelFormat.BULLET, text: "◦", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 240 } } } },
          ],
        },
        {
          reference: "check",
          levels: [
            { level: 0, format: LevelFormat.BULLET, text: "☐", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 400, hanging: 300 } }, run: { font: "Segoe UI Symbol", color: BLUE } } },
          ],
        },
        {
          reference: "teile",
          levels: [
            { level: 0, format: LevelFormat.LOWER_LETTER, text: "%1)", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 400, hanging: 340 } }, run: { bold: true, color: BLUE } } },
          ],
        },
      ],
    },
    sections: [{
      properties: {
        page: {
          size: { width: 11906, height: 16838 },
          margin: { top: 1588, bottom: 1247, left: 1418, right: 1418, header: 567, footer: 567 },
        },
      },
      headers: { default: makeHeader() },
      footers: { default: makeFooter(footerText) },
      children,
    }],
  });
}

const H3 = (text) => new Paragraph({ heading: HeadingLevel.HEADING_3, children: runs(text) });

function write(doc, out) {
  return Packer.toBuffer(doc).then((buf) => {
    fs.writeFileSync(out, buf);
    console.log("geschrieben:", out, buf.length, "Bytes");
  });
}

module.exports = {
  fs, path, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, AlignmentType, BorderStyle, ShadingType,
  ImageRun, ExternalHyperlink, VerticalAlign, LR, FONT, BLUE, PETROL, TEXT, GREY, LINE, BOX, BOX_T, ZEBRA, W,
  runs, P, Small, H1, H2, H3, Bullet, Spacer, NONE, THIN, allBorders, cell, grid, box, boxTitle, boxPara,
  zieleTabelle, bezugTabelle, block, grafikPfad, setGraf, refTable, kv, makeDoc, write,
};
