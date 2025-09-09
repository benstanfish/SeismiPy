import os
import pymupdf as pdf
import pandas as pd

file_name = './building_types/building_type_desc.pdf'

blocks = []
with pdf.open(os.path.abspath(file_name)) as doc:
    for page_no, page in enumerate(doc.pages()):
        for block in page.get_text('blocks'):
            lines = block[4].split('\n')
            for line in lines:
                print(line)