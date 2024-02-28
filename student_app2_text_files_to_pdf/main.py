import glob
from fpdf import FPDF
from pathlib import Path

pdf = FPDF(orientation="P", unit="mm", format="A4")
filepaths = glob.glob("PDFs/*.txt")
for filepath in filepaths:
    filename = Path(filepath).stem
    title = filename.title()
    pdf.add_page()
    pdf.set_font(family="Arial", size=16, style="B")
    pdf.cell(w=0, h=16, txt=f"{title}", align="L", ln=1)

pdf.output("output.pdf")
