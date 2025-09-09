import os
import pymupdf as pdf
import pandas as pd


prefacing_pages = 46
building_types_pages = [28, 30]
checkists_pages = [232, 293]

file_name = './data/ASCE 41-23.pdf'

output_path = os.path.join(os.path.abspath(os.path.dirname(file_name)), 'extracted_pages.pdf')

new_pdf = pdf.open()
with pdf.open(os.path.abspath(file_name)) as doc:
    start = building_types_pages[0] + prefacing_pages
    stop = building_types_pages[-1] + prefacing_pages    
    new_pdf.insert_pdf(doc, from_page=start, to_page=stop)

    start = checkists_pages[0] + prefacing_pages
    stop = checkists_pages[-1] + prefacing_pages
    new_pdf.insert_pdf(doc, from_page=start, to_page=stop)
    
    new_pdf.save(output_path)