#!/usr/bin/env python3
import re, markdown

SRC = "/home/user/jam-wear/02-branding/documento-de-marca.md"
OUT = "/tmp/claude-0/-home-user-jam-wear/f705063a-d171-5e25-b12d-49213946402a/scratchpad/doc-v4.html"

with open(SRC, encoding="utf-8") as f:
    md = f.read()

# Convert markdown -> HTML (tables + fenced). Keep it simple/standard.
html_body = markdown.markdown(md, extensions=["tables", "sane_lists"])

# --- Color scheme (established) ---
GREEN_CELL = "#d9ead3"   # é / faz
GREEN_HEAD = "#b6d7a8"
RED_CELL   = "#f4cccc"   # não é / não faz
RED_HEAD   = "#ea9999"
YELLOW     = "#fff2cc"   # destaque / em definição (soft)

# Identify 2-column contrast tables by their header text and paint left green / right red.
CONTRAST_MARKERS = [
    ("fala assim", "nunca fala assim"),
    ("visual faz", "visual nunca faz"),
    ("jam wear é", "jam wear não é"),
]

def paint_table(table_html):
    # Determine if this is a contrast table from its header row.
    head_match = re.search(r"<thead>(.*?)</thead>", table_html, re.S)
    if not head_match:
        return table_html
    head = head_match.group(1).lower()
    is_contrast = any(a in head and b in head for a, b in CONTRAST_MARKERS)
    if not is_contrast:
        return table_html

    # Paint header cells
    def head_cells(m):
        cells = re.findall(r"<th.*?</th>", m.group(1), re.S)
        if len(cells) == 2:
            c0 = re.sub(r"<th", f'<th style="background-color:{GREEN_HEAD}"', cells[0], count=1)
            c1 = re.sub(r"<th", f'<th style="background-color:{RED_HEAD}"', cells[1], count=1)
            return "<thead><tr>" + c0 + c1 + "</tr></thead>"
        return m.group(0)
    table_html = re.sub(r"<thead>(.*?)</thead>", head_cells, table_html, flags=re.S)

    # Paint body cells
    def body_row(m):
        cells = re.findall(r"<td.*?</td>", m.group(1), re.S)
        if len(cells) == 2:
            c0 = re.sub(r"<td", f'<td style="background-color:{GREEN_CELL}"', cells[0], count=1)
            c1 = re.sub(r"<td", f'<td style="background-color:{RED_CELL}"', cells[1], count=1)
            return "<tr>" + c0 + c1 + "</tr>"
        return m.group(0)
    table_html = re.sub(r"<tr>(.*?)</tr>", body_row, table_html, flags=re.S)
    return table_html

html_body = re.sub(r"<table>.*?</table>", lambda m: paint_table(m.group(0)), html_body, flags=re.S)

# Highlight inline status markers so they pop in the doc.
def hl(txt, color):
    return f'<span style="background-color:{color}">{txt}</span>'

html_body = html_body.replace("◆", hl("◆", YELLOW))
html_body = html_body.replace("⚠️", hl("⚠️", YELLOW))

# Base styling for the whole doc.
css = """
body { font-family: Arial, sans-serif; font-size: 11pt; color: #202124; line-height: 1.45; }
h1 { font-size: 22pt; color: #1a1a1a; }
h2 { font-size: 15pt; color: #1a1a1a; border-bottom: 1px solid #ccc; padding-bottom: 3px; margin-top: 26px; }
h3 { font-size: 12.5pt; color: #333; margin-top: 18px; }
table { border-collapse: collapse; width: 100%; margin: 10px 0; }
th, td { border: 1px solid #b7b7b7; padding: 6px 9px; vertical-align: top; text-align: left; }
th { background-color: #f1f3f4; }
blockquote { border-left: 3px solid #999; margin: 10px 0; padding: 4px 14px; background: #f8f9fa; font-weight: bold; }
code { background: #f1f3f4; padding: 1px 4px; border-radius: 3px; }
"""

doc = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><style>{css}</style></head>
<body>
{html_body}
</body></html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(doc)

# Quick sanity: ensure no astral-plane emoji slipped in (they corrupt on GDoc convert).
astral = sorted({c for c in doc if ord(c) > 0xFFFF})
print("OUT:", OUT)
print("bytes:", len(doc.encode("utf-8")))
print("astral chars present:", [hex(ord(c)) for c in astral] or "none")
print("contrast tables painted:", doc.count(GREEN_CELL))
