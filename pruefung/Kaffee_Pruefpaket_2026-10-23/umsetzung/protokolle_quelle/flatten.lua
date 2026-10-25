-- Vereinfacht Tabellen für eine schlanke Markdown-Fassung:
-- Tabellen mit einer Spalte oder mit verschachtelten Blöcken werden aufgelöst,
-- Zellen mit mehreren Absätzen werden mit " · " zusammengefügt.

local function cell_blocks(cell)
  return cell.contents
end

local function only_paras(blocks)
  for _, b in ipairs(blocks) do
    if b.t ~= "Para" and b.t ~= "Plain" then return false end
  end
  return true
end

local function join_paras(blocks)
  local inl = pandoc.Inlines({})
  for i, b in ipairs(blocks) do
    if i > 1 then inl:insert(pandoc.Str(" · ")) end
    inl:extend(b.content)
  end
  return { pandoc.Plain(inl) }
end

local function all_rows(tbl)
  local rows = {}
  for _, r in ipairs(tbl.head.rows) do table.insert(rows, r) end
  for _, body in ipairs(tbl.bodies) do
    for _, r in ipairs(body.head) do table.insert(rows, r) end
    for _, r in ipairs(body.body) do table.insert(rows, r) end
  end
  for _, r in ipairs(tbl.foot.rows) do table.insert(rows, r) end
  return rows
end

function Table(tbl)
  local ncols = #tbl.colspecs
  local nested = false
  for _, r in ipairs(all_rows(tbl)) do
    for _, c in ipairs(r.cells) do
      if not only_paras(cell_blocks(c)) then nested = true end
    end
  end
  if ncols == 1 or nested then
    local out = pandoc.Blocks({})
    for _, r in ipairs(all_rows(tbl)) do
      for _, c in ipairs(r.cells) do
        out:extend(cell_blocks(c))
      end
    end
    return out
  end
  for _, r in ipairs(all_rows(tbl)) do
    for _, c in ipairs(r.cells) do
      if #c.contents > 1 then c.contents = join_paras(c.contents) end
    end
  end
  -- Kopfzeile ergänzen, falls keine vorhanden ist (für Pipe-Tabellen)
  if #tbl.head.rows == 0 and #tbl.bodies > 0 and #tbl.bodies[1].body > 0 then
    local first = table.remove(tbl.bodies[1].body, 1)
    tbl.head.rows = { first }
  end
  return tbl
end

function Image(img)
  return {}
end
