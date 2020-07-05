from tkinter import *
from graphics import *
import time
import random
root=Tk()
root.resizable(100,100)
window=GraphWin("Example Window",1000,600)
window.setBackground(color_rgb(0,0,0))
pt=Point(random.randrange(10,600),random.randrange(10,600))
pt1=Point(random.randrange(10,600),random.randrange(10,600))
pt2=Point(random.randrange(10,600),random.randrange(10,600))
pt3=Point(random.randrange(10,600),random.randrange(10,600))
pt4=Point(random.randrange(10,600),random.randrange(10,600))
line=Line(pt1,pt2)
line.setFill(color_rgb(0,255,255))
cir=Circle(pt,50)
cir.setFill(color_rgb(255,255,255))
rect=Rectangle(pt4,pt3)
rect.setFill(color_rgb(255,0,0))

def createCircle():
	cir.draw(window)
	window.getMouse()
	window.close()
	
def createLine():
	line.draw(window)
	window.getMouse()
	window.close()

def createRectangle():
	rect.draw(window)
	window.getMouse()
	window.close()
	
CircleButton=Button(root,text="Draw a Circle",command=createCircle)
CircleButton.grid(row=2,column=2)
LineButton=Button(root,text="Draw a Line",command=createLine)
LineButton.grid(row=2,column=3)
RectangleButton=Button(root,text="Draw a Rectangle",command=createRectangle)
RectangleButton.grid(row=2,column=4)
root.mainloop()
