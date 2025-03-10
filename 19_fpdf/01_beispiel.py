# Achtung: Es muss fpdf, nicht fpdf2 installiert werden
# pip install fpdf
from fpdf import FPDF
#https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html
pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_margins(0, 0, 0)
pdf.set_font('helvetica', 'B', 16)
pdf.cell(40, 10, 'Hello World!', 1, 1)
pdf.set_font('Times', '', 12)
pdf.cell(210, 10, 'Powered by Hochschule Osnabrück.', 0, 1, align="C")
pdf.image('./data/logo.jpg', x = 55, y = 35, w = 100, h = 0, type = '', link = '')
pdf.line(x1 = 65, y1 = 27.5, x2 = 145, y2 = 27.5)
pdf.rect(x = 55, y = 20, w = 100, h = 55, style = '')

pdf.cell(210, 10, 'Osnabrück ist suuuper', 0, 1, align="C")

pdf.set_fill_color(255, 255, 0)
pdf.set_draw_color(255, 0, 0)
pdf.rect(80, 115, 50, 10, style='DF')


pdf.output('sample.pdf', "F")