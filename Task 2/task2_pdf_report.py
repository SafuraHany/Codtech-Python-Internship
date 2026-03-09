from fpdf import FPDF

# Sample data (can also be read from a file)
student_data = [
    {"name": "Ali", "marks": 85},
    {"name": "Sara", "marks": 90},
    {"name": "John", "marks": 78},
    {"name": "Ayesha", "marks": 88}
]

# Create PDF
pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=16)
pdf.cell(200, 10, txt="Student Marks Report", ln=True, align='C')

pdf.ln(10)

pdf.set_font("Arial", size=12)

for student in student_data:
    line = f"Name: {student['name']}   Marks: {student['marks']}"
    pdf.cell(200, 10, txt=line, ln=True)

# Save PDF
pdf.output("report.pdf")

print("PDF report generated successfully!")