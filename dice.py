from graphics import *
from random import randint

r=randint(1,6)

win=GraphWin("Dice Game",500,500)
win.setBackground(color_rgb(0,0,0))

a=f"You rolled a {r}"
p=Point(250,100)
text=Text(p,a)
text.setFill(color_rgb(0,200,200))
text.draw(win)

pt1=Point(200,200)
pt2=Point(300,300)

pt3=Point(250,250)

pt4=Point(225,250)
pt5=Point(275,250)

pt6=Point(250,225)
pt7=Point(250,275)

pts1=Point(225,225)
pts2=Point(225,250)
pts3=Point(225,275)
pts4=Point(275,225)
pts5=Point(275,250)
pts6=Point(275,275)



dice=Rectangle(pt1,pt2)
dice.draw(win)
dice.setFill(color_rgb(255,0,0))
#for 1 dot
dot1=Circle(pt3,10)
dot1.setFill(color_rgb(255,255,255))
#close

#for 2 horizontal dots
dot2a=Circle(pt4,10)
dot2b=Circle(pt5,10)
dot2a.setFill(color_rgb(255,255,255))
dot2b.setFill(color_rgb(255,255,255))	
#close

#for 2 vertical dots
dotv1=Circle(pt6,10)
dotv2=Circle(pt7,10)
dotv1.setFill(color_rgb(255,255,255))
dotv2.setFill(color_rgb(255,255,255))
#close

#for final 6 dots
dot1s=Circle(pts1,10)
dot1s.setFill(color_rgb(255,255,255))
dot2s=Circle(pts2,10)
dot2s.setFill(color_rgb(255,255,255))
dot3s=Circle(pts3,10)
dot3s.setFill(color_rgb(255,255,255))
dot4s=Circle(pts4,10)
dot4s.setFill(color_rgb(255,255,255))
dot5s=Circle(pts5,10)
dot5s.setFill(color_rgb(255,255,255))
dot6s=Circle(pts6,10)
dot6s.setFill(color_rgb(255,255,255))

#close


if r==1:
	dot1.draw(win)
if r==2:
	dot2a.draw(win)
	dot2b.draw(win)
if r==3:
	dot1.draw(win)
	dot2a.draw(win)
	dot2b.draw(win)
if r==4:
	dot2a.draw(win)
	dot2b.draw(win)
	dotv1.draw(win)
	dotv2.draw(win) 
if r==5:
	dot2a.draw(win)
	dot2b.draw(win)
	dotv1.draw(win)
	dotv2.draw(win)
	dot1.draw(win)
if r==6:
	dot1s.draw(win)
	dot2s.draw(win)
	dot3s.draw(win)
	dot4s.draw(win)
	dot5s.draw(win)
	dot6s.draw(win)



win.getMouse()
win.close()