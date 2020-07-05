from tkinter import *
import random
import time
root=Tk()
root.title("My Application")

label = Label(root,text="Moving Squares")
label.grid(row=0,column=4)



canvas=Canvas(root, width=800, height=600, bg="yellow")
canvas.grid(row=2,column=4)


xspeed=random.randrange(1,10)
yspeed=random.randrange(1,10)
xspeed2=random.randrange(1,10)
yspeed2=random.randrange(1,10)
colors=["red","pink","cyan","blue","black","magenta"]

ball=canvas.create_rectangle(10, 10, 60, 60, fill=random.choice(colors))
ball2=canvas.create_rectangle(60, 60, 110, 110, fill=random.choice(colors))
while True:
	canvas.move(ball, xspeed, yspeed)
	pos=canvas.coords(ball)
	if pos[3] >= 600 or pos[1] <=0:
		yspeed=-yspeed
	if pos[2] >= 800 or pos[0] <=0:
			xspeed = -xspeed
	canvas.move(ball2, xspeed2, yspeed2)
	pos2=canvas.coords(ball2)
	if pos2[3] >= 600 or pos2[1] <=0:
		yspeed2=-yspeed2
	if pos2[2] >= 800 or pos2[0] <=0:
			xspeed2 = -xspeed2
	root.update()
	root.update()
	time.sleep(0.1)
speedPlus=Button(root,text="Increase Speed")
speedPlus.grid(row=5,column=20)	

root.mainloop()