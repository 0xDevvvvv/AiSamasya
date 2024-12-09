import PyPDF2

def pdf_to_text(pdf_filename, txt_filename):
    with open(pdf_filename, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()

        # Write the extracted text to a .txt file
        with open(txt_filename, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)

# Usage
pdf_to_text(r'Waterfall_Model_Overview.pdf', 'output.txt')
