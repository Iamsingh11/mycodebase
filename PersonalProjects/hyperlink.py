from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib import pdfencrypt

def create_pdf_with_hyperlink(output_filename):
    # Create a PDF canvas
    c = canvas.Canvas(output_filename, pagesize=letter)

    # Set the font and size
    c.setFont("Helvetica", 12)

    # Define the text and link
    text = "Click here to visit Google"
    link_url = "https://www.google.com"

    # Calculate the width and height of the text
    text_width = c.stringWidth(text, "Helvetica", 12)
    text_height = 12  # Assuming the height of the text is 12 (font size)

    # Coordinates of the text
    x = 100
    y = 700

    # Add the link annotation to the canvas
    c.linkURL(link_url, (x, y, x + text_width, y + text_height), relative=0)

    # Set the color of the link text
    c.setFillColor(colors.blue)

    # Draw the text on the canvas
    c.drawString(x, y, text)

    # Save the PDF
    c.save()

if __name__ == "__main__":
    create_pdf_with_hyperlink("pdf_with_hyperlink.pdf")
