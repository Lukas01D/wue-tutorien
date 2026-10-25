-- Lua-Filter der Aufgabensammlung (LaTeX und Word)
-- 1) ::: center und ::: seitenumbruch
-- 2) LaTeX: Bild und folgende Bildunterschrift („Abb. …“) bleiben zusammen (minipage)
-- 3) LaTeX: vor „Gegebene Größen“, „Annahmen“ und „Aufgabenstellung“ genug Platz auf der Seite (needspace)

local function txt(el)
  return pandoc.utils.stringify(el)
end

function Div(el)
  if el.classes:includes("center") then
    if FORMAT:match("latex") then
      table.insert(el.content, 1, pandoc.RawBlock("latex", "\\begin{center}"))
      table.insert(el.content, pandoc.RawBlock("latex", "\\end{center}"))
      return el.content
    elseif FORMAT:match("docx") then
      el.attributes["custom-style"] = "Zentriert"
      return el
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

local function nur_bild(b)
  return b and b.t == "Para" and #b.content == 1 and b.content[1].t == "Image"
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
      table.insert(out, pandoc.RawBlock("latex", "\\par\\noindent\\begin{minipage}{\\linewidth}"))
      table.insert(out, b)
      table.insert(out, nxt)
      table.insert(out, pandoc.RawBlock("latex", "\\end{minipage}\\par\\smallskip"))
      i = i + 2
    else
      if b.t == "Para" then
        local s = txt(b)
        if s:match("^Gegebene Größen") then
          local n = 12
          if nxt and nxt.t == "Table" then n = math.ceil(zeilen(nxt) * 1.5 + 3) end
          platz(out, n)
        elseif s:match("^Aufgabenstellung") or s:match("^Annahmen") then
          platz(out, 6)
        elseif s:match("^Frage %d") or s:match("^Aufgabe %d") or s:match("^Zusatzaufgabe %d")
            or s:match("^Ausgangssituation") or s:match("^Versuch zu") then
          platz(out, 5)
        end
      end
      table.insert(out, b)
      i = i + 1
    end
  end
  return out
end

function Pandoc(doc)
  if FORMAT:match("latex") then
    doc.blocks = zusammenhalten(doc.blocks)
  end
  return doc
end
