# Base program
'''
from reportlab.pdfgen import canvas
def hello(c):
    c.drawString(100,100,'Hello World')
c=canvas.Canvas("Hello.pdf")
hello(c)
c.showPage()
c.save()
'''
#Size of pdf
'''
from reportlab.lib.pagesizes import letter, A4
myCanvas=canvas.Canvas('myfile.pdf',pagesize=A4)
width,height=A4
myCanvas.showPage()
myCanvas.save()

#%%
'''
#Drawing operation

'''
def hello(c):
    from reportlab.lib.units import inch
    c.translate(inch,inch)
    c.setFont("Helvetica",14)
    c.setStrokeColorRGB(0.2,0.5,0.3)
    c.setFillColorRGB(1,0,1)
    c.line(0,0,0,1.7*inch)
    c.line(0,0,1*inch,0)
    c.rect(0.2*inch,0.2*inch,1*inch,1.5*inch, fill=1)
    c.rotate(90)
    c.setFillColorRGB(0,0,0.77)
    c.drawString(0.3*inch,-inch, "Hello World")
    c.showPage()
    c.save()
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
c=canvas.Canvas('HelloWorldRectangle.pdf', pagesize=A4)
width,height=A4
hello(c)
#%%
'''
