import fitz
import tabula

# Kept running into SIGBUSS Error on M1 Mac --> will try on Intelx86 Windows 11
# details in PDF_file_converter/hs_err_pid20445.log

table = tabula.read_pdf('./PDF_file_converter/generated_pdfs/American Black Bear.pdf', pages=all)
print(table)

# with fitz.open("students.pdf") as pdf:
#     # Print 1 page
#     # page1 = pdf[0].get_text()
#     # print(page1)

#     # Print entire doc
#     # for page in pdf:
#     #     print(40*'-')
#     #     print(page.get_text())

#     # text = ''
#     # for page in pdf:
#     #     text = text + page.get_text()

#     print(text)