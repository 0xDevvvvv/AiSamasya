from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.set_text_color(0, 0, 139)  # Dark Blue
        self.cell(0, 10, 'Waterfall Model Overview', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(169, 169, 169)  # Dark Gray
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_text_color(34, 139, 34)  # Forest Green
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.set_text_color(0, 0, 0)  # Black
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# Title and Introduction
pdf.chapter_title('Introduction')
pdf.chapter_body('The Waterfall Model is a fundamental software development methodology that outlines a linear and sequential approach. Each stage must be completed before moving to the next.')

# Section: Stages of the Waterfall Model
pdf.chapter_title('Stages of the Waterfall Model')
pdf.chapter_body(
    "1. **Requirements analysis and definition**: \n- Establishing the system's services, constraints, and goals in consultation with system users.\n- Defining them in detail to serve as a system specification.\n\n"
    "2. **System and software design**: \n- Allocating the requirements to either hardware or software systems.\n- Establishing an overall system architecture.\n- Identifying and describing the fundamental software system abstractions and their relationships.\n\n"
    "3. **Implementation and unit testing**: \n- Realizing the software design as a set of programs or program units.\n- Verifying that each unit meets its specification.\n\n"
    "4. **Integration and system testing**: \n- Integrating and testing individual program units or programs as a complete system.\n- Ensuring that the software requirements have been met.\n- Delivering the system to the customer.\n\n"
    "5. **Operation and maintenance**: \n- Installing the system and putting it into practical use.\n- Correcting errors not discovered in earlier stages.\n- Improving the implementation of system units.\n- Enhancing the system's services as new requirements are discovered."
)

# Section: Additional Notes
pdf.chapter_title('Additional Notes')
pdf.chapter_body(
    "The Waterfall Model is particularly appropriate for:\n"
    "- Embedded systems where the software has to interface with hardware systems.\n"
    "- Critical systems requiring extensive safety and security analysis.\n"
    "- Large software systems that are part of broader engineering systems developed by several partner companies."
)

# Save the PDF
pdf.output('Waterfall_Model_Overview.pdf')

print("PDF created successfully!")
