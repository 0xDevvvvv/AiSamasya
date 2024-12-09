from distutils.log import debug 
from fileinput import filename 
from flask import *
import PyPDF2

app = Flask(__name__) 

def pdftotext(pdf_filename, txt_filename):
    with open(pdf_filename, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()

        # Write the extracted text to a .txt file
        with open(txt_filename, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)

@app.route('/') 
def main(): 
    return render_template("index.html") 

@app.route('/success', methods=['POST'])
def success(): 
    if request.method == 'POST': 
        f = request.files['file'] 
        f.save(f.filename) 
        pdftotext(f.filename, 'output.txt')
        return render_template("Acknowledgement.html", name=f.filename) 

if __name__ == '__main__': 
    app.run(debug=True)