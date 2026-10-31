-- Lua-Filter der Aufgabensammlung (LaTeX und Word), Kopie für Variante B des Kaffee-Blatts
-- Abweichungen vom Original (kaffee/build/lehrstuhl.lua):
--   a) weitere Bausteine: Grundlagen, Lernziele, Einführung, Gegeben, Gesucht, Versuch
--   b) ::: zweispaltig: links Text (etwa 2/3), rechts das letzte Bild des Blocks (etwa 1/3);
--      LaTeX: zwei Minipages (links Flattersatz, weil die Spalte schmal ist), Bild als PDF (gleicher Name wie das PNG); Word: Tabelle mit zwei Zellen ohne Rahmen
--   c) LaTeX: needspace auch vor „Werte:“ (Tabelle) und „Frage 1 …:“
-- 1) ::: center und ::: seitenumbruch; Blatttitel („Tutorium …“) 18 pt
-- 2) Bausteine (Ausgangssituation, Frage n, Aufgabe n, Versuch, Lösung, Hinweise, Quellen) 14 pt, 18 pt davor und 6 pt danach
--    (mit \parskip von 4 pt: 14 pt davor, 2 pt danach zusätzlich)
-- 3) Bild und folgende Bildunterschrift („Abb. …“) zentriert und zusammen (LaTeX: minipage; Word: Formatvorlagen)
-- 4) LaTeX: vor „Gegebene Größen“, „Annahmen“ und „Aufgabenstellung“ genug Platz auf der Seite (needspace)
-- 5) LaTeX: Datenzeilen der Versuchstabelle (erste Kopfzelle „Becher“) mindestens 10 mm hoch

local function txt(el)
  return pandoc.utils.stringify(el)
end

function Div(el)
  if el.classes:includes("center") then
    local titel = txt(el):match("^Tutorium %d") ~= nil
    if FORMAT:match("latex") then
      table.insert(el.content, 1, pandoc.RawBlock("latex", titel and "\\begin{center}\\fontsize{18}{22}\\selectfont" or "\\begin{center}"))
      table.insert(el.content, pandoc.RawBlock("latex", "\\end{center}"))
      return el.content
    elseif FORMAT:match("docx") then
      el.attributes["custom-style"] = titel and "Blatttitel" or "Zentriert"
      return el
    end
  end
  if el.classes:includes("zweispaltig") then
    local bild = el.content[#el.content]
    assert(bild.t == "Para" and bild.content[1].t == "Image", "zweispaltig: letzter Block muss ein Bild sein")
    local links = {}
    for i = 1, #el.content - 1 do links[#links + 1] = el.content[i] end
    if FORMAT:match("latex") then
      local pdf = bild.content[1].src:gsub("%.png$", ".pdf")
      local out = { pandoc.RawBlock("latex", "\\par\\noindent\\begin{minipage}[t]{0.65\\linewidth}\\vspace{0pt}\\setlength{\\parskip}{4pt plus 1pt}\\RaggedRight") }
      for _, b in ipairs(links) do out[#out + 1] = b end
      out[#out + 1] = pandoc.RawBlock("latex", "\\end{minipage}\\hfill\\begin{minipage}[t]{0.33\\linewidth}\\vspace{2pt}\\includegraphics[width=\\linewidth]{" .. pdf .. "}\\end{minipage}\\par")
      return pandoc.Div(out)
    elseif FORMAT:match("docx") then
      local zeile = pandoc.Row({ pandoc.Cell(links), pandoc.Cell({ bild }) })
      local koerper = { attr = pandoc.Attr(), body = { zeile }, head = {}, row_head_columns = 0 }
      return pandoc.Table({ long = {} }, { { pandoc.AlignLeft, 0.66 }, { pandoc.AlignLeft, 0.34 } },
                          pandoc.TableHead(), { koerper }, pandoc.TableFoot())
    end
  end
  if el.classes:includes("seitenumbruch") then
    if FORMAT:match("latex") then
      return pandoc.RawBlock("latex", "\\newpage")
    elseif FORMAT:match("docx") then
      return pandoc.RawBlock("openxml", '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
    end
  end
end

function Table(el)
  if not FORMAT:match("latex") then return nil end
  local kopf = el.head.rows[1]
  if not (kopf and kopf.cells[1] and txt(kopf.cells[1].contents) == "Becher") then return nil end
  for _, body in ipairs(el.bodies) do
    for _, row in ipairs(body.body) do
      local c = row.cells[1].contents
      if #c > 0 and (c[1].t == "Plain" or c[1].t == "Para") then
        table.insert(c[1].content, 1, pandoc.RawInline("latex", "\\rule[-3.5mm]{0pt}{10mm}"))
      end
    end
  end
  return el
end

local function nur_bild(b)
  return b and b.t == "Para" and #b.content == 1 and b.content[1].t == "Image"
end

local BAUSTEINE = { "^Ausgangssituation", "^Frage %d", "^Aufgabe %d", "^Zusatzaufgabe %d", "^Zusatzaufgaben",
                    "^Versuch", "^Lösung", "^Hinweise für", "^Quellen der",
                    "^Grundlagen", "^Lernziele", "^Einführung", "^Gegeben", "^Gesucht" }

local function ist_baustein(b)
  -- Bausteine sind fett und unterstrichen geschrieben: **[Frage 1]{.underline}**
  if not (b and b.t == "Para" and #b.content > 0 and b.content[1].t == "Strong") then return false end
  local innen = b.content[1].content[1]
  if not (innen and (innen.t == "Underline" or (innen.t == "Span" and innen.classes:includes("underline")))) then return false end
  local s = txt(b.content[1])
  for _, m in ipairs(BAUSTEINE) do
    if s:match(m) then return true end
  end
  return false
end

local function rest_von(b)
  local rest = {}
  for i = 2, #b.content do rest[#rest + 1] = b.content[i] end
  return rest
end

local function platz(out, n)
  -- needspace vor dem Block einfügen; steht davor eine Überschrift, dann vor die Überschrift
  local raw = pandoc.RawBlock("latex", "\\needspace{" .. n .. "\\baselineskip}")
  if #out > 0 and out[#out].t == "Header" then
    table.insert(out, #out, raw)
  else
    table.insert(out, raw)
  end
end

local function zeilen(tbl)
  local n = 0
  for _, r in ipairs(tbl.head.rows) do n = n + 1 end
  for _, body in ipairs(tbl.bodies) do
    for _, r in ipairs(body.body) do n = n + 1 end
  end
  return n
end

local function zusammenhalten(blocks)
  local out = {}
  local i = 1
  while i <= #blocks do
    local b = blocks[i]
    local nxt = blocks[i + 1]
    if nur_bild(b) and nxt and nxt.t == "Para" and txt(nxt):match("^Abb%.") then
      table.insert(out, pandoc.RawBlock("latex", "\\par\\noindent\\begin{minipage}{\\linewidth}\\centering"))
      table.insert(out, b)
      table.insert(nxt.content, 1, pandoc.RawInline("latex", "\\small "))
      table.insert(out, pandoc.RawBlock("latex", "\\vspace{2pt}"))
      table.insert(out, nxt)
      table.insert(out, pandoc.RawBlock("latex", "\\end{minipage}\\par\\medskip"))
      i = i + 2
    else
      if b.t == "Para" then
        local s = txt(b)
        if s:match("^Gegebene Größen") or s:match("^Werte:") then
          local n = 12
          if nxt and nxt.t == "Table" then n = math.ceil(zeilen(nxt) * 1.5 + 3) end
          platz(out, n)
        elseif s:match("^Aufgabenstellung") or s:match("^Annahmen") or s:match("^Frage %d.*:$") then
          platz(out, 6)
        elseif ist_baustein(b) then
          platz(out, 5)
        end
      end
      if ist_baustein(b) then
        local inl = { pandoc.RawInline("latex", "{\\fontsize{14}{17}\\selectfont "), b.content[1], pandoc.RawInline("latex", "}") }
        for _, x in ipairs(rest_von(b)) do inl[#inl + 1] = x end
        table.insert(out, pandoc.RawBlock("latex", "\\addvspace{14pt}"))
        table.insert(out, pandoc.Para(inl))
        table.insert(out, pandoc.RawBlock("latex", "\\vspace{2pt}"))
      else
        table.insert(out, b)
      end
      i = i + 1
    end
  end
  return out
end

local function word_formate(blocks)
  local out = {}
  for i, b in ipairs(blocks) do
    if ist_baustein(b) then
      local inl = { b.content[1] }
      local rest = rest_von(b)
      if #rest > 0 then
        inl[#inl + 1] = pandoc.Span(rest, { ["custom-style"] = "BausteinZusatz" })
      end
      out[#out + 1] = pandoc.Div({ pandoc.Para(inl) }, { ["custom-style"] = "Baustein" })
    elseif nur_bild(b) then
      out[#out + 1] = pandoc.Div({ b }, { ["custom-style"] = "Abbildung" })
    elseif b.t == "Para" and txt(b):match("^Abb%.") and nur_bild(blocks[i - 1]) then
      out[#out + 1] = pandoc.Div({ b }, { ["custom-style"] = "Bildunterschrift" })
    else
      out[#out + 1] = b
    end
  end
  return out
end

function Pandoc(doc)
  if FORMAT:match("latex") then
    doc.blocks = zusammenhalten(doc.blocks)
  elseif FORMAT:match("docx") then
    doc.blocks = word_formate(doc.blocks)
  end
  return doc
end
