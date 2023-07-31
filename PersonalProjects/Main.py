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
c.drawString(350, 720, "Location: Bengaluru")
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
c.drawString(300, 170, "Projects:")
c.setFont("Helvetica", 10)
c.drawString(-50, 155, "College: University of Petroleum and Energy Studies")
c.drawString(300, 155, "Time-Table Optimization (Genetic Algorithm)")
c.drawString(-50, 140, "Program: Bachelor of Technology")
c.drawString(300, 140, "Book Recommendation System (Python)")
c.drawString(-50, 125, "Course: Computer Science | CGPA: 3.2/4")


c.line(x1=-50, x2=500, y1=110, y2=105)
c.setFont("Helvetica-Bold", 12)
c.drawString(-50, 95, "Achievements")
c.setFont("Helvetica", 10)
c.drawString(-50, 80, "Dell Technologies : Hackathon Winner for creating a Deep Learning application to help visually impaired people -")
c.drawString(-50, 65, "for object & obstacle detection & navigation.")
c.drawString(-50, 50, "Minimizied server power consumption using game theory for servers")
c.drawString(-50, 35, "Winner of intra-college football championship, volleyball championship")
c.drawString(-50, 20, "Winning Captain of corporate Volleyball Championship at Dell")

c.line(x1=-50, x2=500, y1=5, y2=5)
c.setFont("Helvetica-Bold", 12)
c.drawString(-50, -10, "Hobbies:")
c.setFont("Helvetica", 10)
c.drawString(-50, -25, "Sketching, Digital arts, Travelling, Football, Sci-Fi movies, Gardening, Reading comic books")


c.showPage()
c.save()
#%%


'''
'''