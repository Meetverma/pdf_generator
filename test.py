from xhtml2pdf import pisa

html = """
<h1 style="color: blue;">Hello Business Lead</h1>
<p>This PDF was generated with <b>xhtml2pdf</b>.</p>
"""

with open("out.pdf", "wb") as f:
    pisa.CreatePDF(html, dest=f)

print("✅ PDF created: out.pdf")
