from tkinter import *
import random
import time

root = Tk()
root.title("Football Ping Pong Game")
root.resizable(0,0)


canvas = Canvas(root,width = 500, height = 500, bg  = 'Green')
canvas.pack()
#outer square
canvas.create_line(20,20,20,480,fill="white")
canvas.create_line(20,20,480,20,fill="white")
canvas.create_line(480,20,480,480,fill="white")
canvas.create_line(20,480,480,480,fill="white")

#goal post 1 
canvas.create_line(20,150,65,150,fill="white")
canvas.create_line(20,350,65,350,fill="white")
canvas.create_line(65,150,65,350,fill="white")

#goal post 2 
canvas.create_line(480,150,435,150,fill="white")
canvas.create_line(480,350,435,350,fill="white")
canvas.create_line(435,150,435,350,fill="white")

#kick off center
canvas.create_line(250,20,250,480,fill="white")
canvas.create_oval(225,225,275,275,fill="white")
canvas.create_oval(230,230,270,270,fill="green")
canvas.create_line(250,20,250,480,fill="white")

#striker 1
striker1 = canvas.create_rectangle(90,200,110,280,fill="black")

#striker 2
striker2 = canvas.create_rectangle(390,200,410,280,fill="black")

#striker movement
def key_pressed(event):
	k=event.char
	if k =='w':
		canvas.move(striker1,0,-25)
		root.update()
	if k =='s':
		canvas.move(striker1,0,25)
		root.update()

	if k =='i':
		canvas.move(striker2,0,-25)
		root.update()
	if k =='k':
		canvas.move(striker2,0,25)
		root.update()
root.bind("<Key>",key_pressed)

xspeed=random.randrange(-5,5)
yspeed=random.randrange(-5,5)

#ball
ball = canvas.create_oval(240,240,260,260,fill="black")

a = True
while a:
	canvas.move(ball,xspeed,yspeed)
	time.sleep(0.1)
	root.update()
	posBall = canvas.coords(ball)
	posStr1 = canvas.coords(striker1)
	posStr2 = canvas.coords(striker2)
	if posBall[3] >= 500 or posBall[1] <=0:
		yspeed=-yspeed
	if (posBall[2] >= 500 or posBall[2] == posStr2[0]) or (posBall[0] <=0 or posBall[0] == posStr1[2]):
		xspeed = -xspeed
		if posBall[2] >= 500 or posBall[0] <=0:
			break
			canvas.create_text(250,250,text="GAME OVER")

root.mainloop()