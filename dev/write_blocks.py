import os
import pymupdf as pdf
import pandas as pd


# prefacing_pages = 46
# building_types_pages = [28, 30]
# checkists_pages = [232, 293]

# file_name = './data/ASCE 41-23.pdf'
file_name = './building_types/building_types.pdf'
output_path = os.path.join(os.path.abspath(os.path.dirname(file_name)), 'building_types.xlsx')

lines = []
# tabular = []
with pdf.open(os.path.abspath(file_name)) as doc:
    # for page in doc.pages(start=building_types_pages[0] + prefacing_pages,
    #                       stop=building_types_pages[-1] + 1 + prefacing_pages):
    for page_no, page in enumerate(doc.pages()):
        for block_no, block in enumerate(page.get_text('blocks')):
            lines.append([page_no + 1, block_no + 1, block[4].replace('\n', '~~~')])
        # tables = page.find_tables()
        # for table in tables:
        #     tabular.append(table)

df = pd.DataFrame(lines, columns=['Page', 'Block', 'Text'])
df.to_excel(output_path, index=False)

# df_tab = pd.DataFrame(tabular)
# df.to_excel('output_tabular.xlsx', index=False)