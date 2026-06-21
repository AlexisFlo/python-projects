from pypdf import PdfWriter
import os

output_name = 'Final_pdf.pdf'

merger = PdfWriter()

pdf_files = [f for f in os.listdir() if f.endswith('.pdf') and f != output_name]

for pdf in pdf_files:
  merger.append(pdf)

  merger.write(output_name)
  merger.close()
