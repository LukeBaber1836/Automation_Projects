from fpdf import FPDF

pdf_doc = FPDF(orientation='portrait', unit= 'pt', format='A4')
pdf_doc.add_page()

pdf_doc.image('cute_dog2.jpeg', w=80, h=80)

pdf_doc.set_font(family='Times', style='B', size=24)
pdf_doc.cell(w=0, h=50, txt="Cute Doggo", align='C', ln=1)

pdf_doc.set_font(family='Times', style='B', size=14)
pdf_doc.cell(w=0, h=20, txt="Description", ln=1)

pdf_doc.set_font(family='Times', size=12)
txt1 = """      The dog is a domesticated descendant of the wolf. Also called the domestic dog, it is derived from extinct Pleistocene wolves, and the modern wolf is the dog's nearest living relative. The dog was the first species to be domesticated by humans. Hunter-gatherers did this, over 15,000 years ago in Germany, which was before the development of agriculture. Due to their long association with humans, dogs have expanded to a large number of domestic individuals and gained the ability to thrive on a starch-rich diet that would be inadequate for other canids."""
pdf_doc.multi_cell(w=0, h=15, txt=txt1)

pdf_doc.set_font(family='Times', style='B', size=14)
pdf_doc.cell(w=70, h=20, txt="Kingdom: ")
pdf_doc.set_font(family='Times', size=14)
pdf_doc.cell(w=70, h=20, txt="Animalia", ln=1)

pdf_doc.set_font(family='Times', style='B', size=14)
pdf_doc.cell(w=70, h=20, txt="Phylum: ")
pdf_doc.set_font(family='Times', size=14)
pdf_doc.cell(w=70, h=20, txt="Chordata", ln=1)

pdf_doc.output('output.pdf')