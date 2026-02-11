"""Convert a markdown resume to a styled PDF using markdown + xhtml2pdf."""

import sys
import markdown
from xhtml2pdf import pisa

CSS = """
@page {
    size: A4;
    margin: 18mm 20mm 18mm 20mm;
}

body {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 9.5pt;
    line-height: 1.4;
    color: #1a1a1a;
}

h1 {
    font-size: 17pt;
    margin-bottom: 0;
    padding-bottom: 0;
    color: #0d2137;
}

h2 {
    font-size: 11.5pt;
    color: #0d2137;
    border-bottom: 1.5px solid #0d2137;
    padding-bottom: 2pt;
    margin-top: 14pt;
    margin-bottom: 6pt;
    text-transform: uppercase;
    letter-spacing: 0.5pt;
}

h3 {
    font-size: 10.5pt;
    color: #1a3a5c;
    margin-top: 10pt;
    margin-bottom: 3pt;
}

h4 {
    font-size: 10pt;
    color: #1a3a5c;
    margin-top: 8pt;
    margin-bottom: 2pt;
}

p {
    margin-top: 2pt;
    margin-bottom: 5pt;
}

ul {
    margin-top: 1pt;
    margin-bottom: 5pt;
    padding-left: 16pt;
}

li {
    margin-bottom: 1.5pt;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 4pt;
    margin-bottom: 8pt;
    font-size: 9pt;
}

th {
    background-color: #0d2137;
    color: white;
    padding: 4pt 6pt;
    text-align: left;
    font-weight: bold;
}

td {
    padding: 3pt 6pt;
    border-bottom: 0.5pt solid #ddd;
}

hr {
    border: none;
    border-top: 0.75pt solid #bbb;
    margin: 10pt 0;
}

strong {
    color: #0d2137;
}

em {
    font-size: 8.5pt;
    color: #555;
}
"""


def convert(md_path: str, pdf_path: str) -> None:
    with open(md_path, encoding="utf-8") as f:
        md_text = f.read()

    html_body = markdown.markdown(
        md_text,
        extensions=["tables", "sane_lists"],
    )

    full_html = f"""<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<style>{CSS}</style>
</head><body>{html_body}</body></html>"""

    with open(pdf_path, "wb") as out:
        status = pisa.CreatePDF(full_html, dest=out)

    if status.err:
        print(f"Error generating PDF: {status.err}")
        sys.exit(1)
    else:
        print(f"PDF written to {pdf_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tools/md_to_pdf.py <input.md> [output.pdf]")
        sys.exit(1)

    md_file = sys.argv[1]
    pdf_file = sys.argv[2] if len(sys.argv) > 2 else md_file.rsplit(".", 1)[0] + ".pdf"
    convert(md_file, pdf_file)
