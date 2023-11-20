import pandas as pd
from fpdf import FPDF

df = pd.read_excel('data.xlsx')
#print(df)

for index, row in df.iterrows():
    pdf_doc = FPDF(orientation='portrait', unit= 'pt', format='A4')
    pdf_doc.add_page()

    pdf_doc.set_font(family='Times', style='B', size=24)
    pdf_doc.cell(w=0, h=50, txt=row['name'], align='C', ln=1)
    
    # Kingdom, Phylum, Class, Order, Suborder
    for column in df.columns:
        pdf_doc.set_font(family='Times', style='B', size=14)
        pdf_doc.cell(w=70, h=20, txt=f"{column.title()}: ")

        pdf_doc.set_font(family='Times', size=14)
        pdf_doc.cell(w=70, h=20, txt=row[column], ln=1)

    pdf_doc.output(f"generated_pdfs/{row['name']}.pdf")

    
