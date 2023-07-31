from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
c=canvas.Canvas('final.pdf',pagesize=A4)
c.translate(inch, inch)
width, height = A4
c.absolutePosition(10, 20)
c.setFont("Helvetica-Bold", 12)
c.drawString(-50, 750, "Abhishek Singh")
c.setFont("Helvetica", 10)
c.drawString(350, 750, "Email: official.singh11@gmail.com")
c.drawString(-50, 735, "Senior Software Engineer")
c.drawString(350, 735, "Mobile: +91 9889426699")
c.drawString(-50, 720, "Dell Technologies")
c.drawString(350, 720, "Location: Bangalore")
c.line(x1=-50, x2=500, y1=710, y2=710)
c.setFont("Helvetica-Bold", 12)
c.drawString(-50, 695, "Summary")
c.line(x1=-50, x2=500, y1=610, y2=610)

c.setFont("Helvetica-Bold", 12)
c.line(x1=-50, x2=500, y1=610, y2=610)
c.drawString(-50, 595, "Skills:")


c.setFont("Helvetica-Bold", 12)
c.line(x1=-50, x2=500, y1=555, y2=555)
c.drawString(-50, 540, "Work Experience:")

c.line(x1=-50, x2=500, y1=185, y2=185)
c.setFont("Helvetica-Bold", 12)
c.drawString(-50, 170, "Education:")
c.setFont("Helvetica", 10)
c.drawString(-50, 155, "College: University of Petroleum and Energy Studies")
c.drawString(-50, 140, "Program: Bachelor of Technology")
c.drawString(-50, 125, "Course: Computer Science")

c.line(x1=-50, x2=500, y1=110, y2=105)
c.setFont("Helvetica-Bold", 12)
c.drawString(-50, 95, "Achievements")


c.line(x1=-50, x2=500, y1=5, y2=5)
c.setFont("Helvetica-Bold", 12)
c.drawString(-50, 10, "Hobbies:")


c.showPage()
c.save()
#%%
