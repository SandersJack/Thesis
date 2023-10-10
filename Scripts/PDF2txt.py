from PyPDF2 import PdfReader
import numpy as np

print("Converting pdf to txt")
reader = PdfReader('build/main.pdf')
page = reader.pages
extracted_text = ""
for i in range(len(page)):
    extracted_text += page[i].extract_text()
file_name = "analysis/main.txt"
np.savetxt(file_name, [extracted_text], fmt='%s',encoding="utf-8")