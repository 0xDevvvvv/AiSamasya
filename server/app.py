from fileinput import filename 
from flask import *
import PyPDF2
import google.generativeai as genai
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
import json
app = Flask(__name__) 
prs = Presentation()

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

def add_slide(prs, title, content, bg_color, title_color, content_color):
    for line in content:
        slide_layout = prs.slide_layouts[1]  # Title and Content layout
        slide = prs.slides.add_slide(slide_layout)
        slide.background.fill.solid()
        slide.background.fill.fore_color.rgb = convertrgb(bg_color)

        title_shape = slide.shapes.title
        title_shape.text = title
        title_shape.text_frame.paragraphs[0].font.size = Pt(36)
        title_shape.text_frame.paragraphs[0].font.bold = True
        title_shape.text_frame.paragraphs[0].font.color.rgb = convertrgb(title_color)
        title_shape.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

        content_shape = slide.placeholders[1]
        content_shape.text = line
        for paragraph in content_shape.text_frame.paragraphs:
            paragraph.font.size = Pt(32)
            paragraph.font.color.rgb = convertrgb(content_color)
            paragraph.alignment = PP_ALIGN.CENTER

def convertrgb(color_list):
    r=int(color_list[0])
    g=int(color_list[1])
    b=int(color_list[2])
    return RGBColor(r,g,b)

@app.route('/success', methods=['POST'])
def success(): 
    if request.method == 'POST': 
        f = request.files['file'] 
        f.save(f.filename) 
        pptname = f.filename + ".pptx"
        text = ""
        text += pdftotext(f.filename, 'output.txt')
        # Prompting
        prompt = text + """Summarise but make sure to include all the important content so that its easier 
        for an adhd person to understand, to the following JSON schema , give light vibrant colors such that
         the text is visible even with it
        with the rgb in the format [r,g,b] with no quotations at both ends:

        slide_content = {'title': str, 'contents': list[str],'bg_color':rgb(),'title_color':rgb(),'content_color':rgb()}
        Return: list[slide_content]"""
        response = model.generate_content(prompt)

        # Convert to JSON
        temp = response.text
        clean_temp = temp[temp.find("["):temp.rfind("]") + 1].strip()
        slides_content =json.loads(clean_temp)

        # Add slides to the presentation
        for slide_content in slides_content:
            add_slide(prs, slide_content["title"], slide_content["contents"], slide_content["bg_color"], slide_content["title_color"], slide_content["content_color"])

# Save the presentation
        prs.save(pptname)

        return render_template("Acknowledgement.html", name=f.filename) 

if __name__ == '__main__': 
    app.run()