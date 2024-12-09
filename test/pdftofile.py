import PyPDF2

def pdf_to_text(pdf_file, txt_file):
    # Open the PDF file
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        
        # Create a text file to write the extracted text
        with open(txt_file, 'w') as text_file:
            # Loop through each page in the PDF
            for page_num in range(reader.numPages):
                # Extract text from the page
                page = reader.getPage(page_num)
                text = page.extractText()
                
                # Write the extracted text to the text file
                text_file.write(text)

# Usage
pdf_to_text('ADHD_Friendly_Fascinating_World_of_Felines.pdf', 'output.txt')
print("PDF to text conversion complete!")
