"""DOCX -> schlankes Markdown für die Projektablage (Überschriften aus den Absatzformaten wiederhergestellt)."""
import os, re, subprocess, sys, zipfile, html

HIER = os.path.dirname(os.path.abspath(__file__))

def headings(docx):
    xml = zipfile.ZipFile(docx).read("word/document.xml").decode("utf-8")
    out = []
    for p in re.findall(r"<w:p[ >].*?</w:p>", xml, flags=re.S):
        m = re.search(r'<w:pStyle w:val="(Heading[123]|Title)"', p)
        if not m:
            continue
        text = "".join(html.unescape(t) for t in re.findall(r"<w:t(?: [^>]*)?>(.*?)</w:t>", p, flags=re.S))
        lvl = {"Title": 1, "Heading1": 2, "Heading2": 3, "Heading3": 4}[m.group(1)]
        out.append((text.strip(), lvl))
    return out

def main(docx, md, hinweis):
    res = subprocess.run(["pandoc", "-f", "docx", "-t", "gfm", "--wrap=none",
                          "--lua-filter=" + os.path.join(HIER, "flatten.lua"), docx],
                         capture_output=True, text=True, check=True)
    lines = res.stdout.splitlines()
    hs = headings(docx)
    todo = list(hs)
    for i, line in enumerate(lines):
        plain = line.strip().replace("\\.", ".")
        for k, (t, lvl) in enumerate(todo):
            if plain == t or plain == f"**{t}**":
                lines[i] = "#" * lvl + " " + t
                todo.pop(k)
                break
    text = "\n".join(lines)
    text = text.replace("­", "")
    text = f"> {hinweis}\n\n" + text
    open(md, "w", encoding="utf-8").write(text + "\n")
    print(md, "Überschriften:", len(hs), "nicht gefunden:", len(todo), todo[:5])

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
