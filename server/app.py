# from distutils.log import debug 
from fileinput import filename 
from flask import *
import PyPDF2
import google.generativeai as genai
app = Flask(__name__) 

genai.configure(api_key="AIzaSyAusjXdqax_JcIQMd5QBs_bLJGcc47KOAo")
model = genai.GenerativeModel("gemini-1.5-flash")


def pdftotext(pdf_filename, txt_filename):
    with open(pdf_filename, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        # print(text)
        return text
        # Write the extracted text to a .txt file
        # with open(txt_filename, 'w', encoding='utf-8') as txt_file:
        #     txt_file.write(text)

@app.route('/') 
def main(): 
    
    return render_template("index.html") 

@app.route('/success', methods=['POST'])
def success(): 
    if request.method == 'POST': 
        f = request.files['file'] 
        f.save(f.filename) 

        text = ""
        text += pdftotext(f.filename, 'output.txt')
        # print(text)
        prompt = text + """Summarise this content to the following JSON schema , give light vibrant colors with the RGBColor(r,g,b) format with no quotations:

        slide_content = {'title': str, 'contents': list[str],'bg_color':rgb(),'title_color':rgb(),'content_color':rgb()}
        Return: list[slide_content]"""
        response = model.generate_content(prompt)
        print(response.text)
        return render_template("Acknowledgement.html", name=f.filename) 

if __name__ == '__main__': 
    app.run()