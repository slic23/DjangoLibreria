from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello World!')
pdf.image("media/libros/portadas/pazyguerra.jpeg", x=10, y=20, w=100)
pdf.output('tuto1.pdf', 'F')
