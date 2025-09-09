import os
import pymupdf as pdf
import pandas as pd


prefacing_pages = 46
file_name = './building_types/building_types.pdf'
output_path = os.path.join(os.path.abspath(os.path.dirname(file_name)), 'as_lines.xlsx')

new_pdf = pdf.open()
with pdf.open(os.path.abspath(file_name)) as doc:
    start = 0
    stop = doc.page_count
    lines = []
    for page_no, page in enumerate(doc.pages(start=start, stop=stop)):
        shape = page.new_shape()
        page_dict = page.get_text('dict')
        
    #     for block in page_dict:
    #         if block['type'] == 0: # 0 is a text block
    #             for line_no, line in enumerate(block['lines']):
    #                 line_text = ''
    #                 for span in line['spans']:
    #                     line_text += span['text']
    #             lines.append(page_no, line_no, line_text)

    # df = pd.DataFrame(lines, columns=['Page', 'Line', 'Text'])
    # df.to_excel(output_path, index=False)

        for block in page_dict['blocks']:
            for key in block.keys():
                print(key)
                # if key == 'type':
                #     print(block[key])
                if key == 'lines':
                    for span in block.lines.spans:
                        print(span)
                