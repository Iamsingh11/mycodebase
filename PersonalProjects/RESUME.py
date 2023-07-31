from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def generate_pdf(output_filename):
    # Sample data for the table
    personal_data = [
        ['ABHISHEK SINGH'],
        ['Senior Software Engineer'],
        ['Dell Technologies'],
        ['official.singh11@gmail.com'],
    ]

    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    elements = []

    # Create a table and set its style
    table = Table(personal_data)
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.black),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    table.setStyle(style)

    # Add the table to the PDF document
    elements.append(table)

    # Build the PDF document
    doc.build(elements)

if __name__ == "__main__":
    generate_pdf("ABHISHEK SINGH.pdf")

#%%
