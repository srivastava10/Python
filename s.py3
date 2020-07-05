from tkinter import *
import random
import time
root = Tk()
root.title("Game")
root.resizable(0,0)
root.geometry("500x700")
topFrame=Frame(root,width=500,height=500)
topFrame.pack()
bottomFrame=Frame(root,bg='cyan')
bottomFrame.pack()
label = Label(bottomFrame,text="Game")
label.pack()




canvas = Canvas(topFrame,width=500, height=500, bg="black")
canvas.pack()




colors=["red","pink","cyan","blue","white","magenta","yellow"]

ball = canvas.create_oval(10, 10, 50, 50, fill=random.choice(colors))
canvas.move(ball,400,425)

AIball=canvas.create_oval(10,10,50,50,fill="White")
canvas.move(AIball,10,425)

def key_pressed(event):
	k=event.char
	if k =='w':
		canvas.move(AIball,0,-25)
		root.update()
	if k =='a':
		canvas.move(AIball,-25,0)
		root.update()
	if k =='s':
		canvas.move(AIball,0,25)
		root.update()
	if k =='d':
		canvas.move(AIball,25,0)
		root.update()
	if k =='i':
		canvas.move(ball,0,-25)
		root.update()
	if k =='k':
		canvas.move(ball,0,25)
		root.update()
	if k =='j':
		canvas.move(ball,-25,0)
		root.update()
	if k =='l':
		canvas.move(ball,25,0)
		root.update()
canvas.create_text(250,250,text="First to reach the end wins",fill=random.choice(colors))



	
root.bind("<Key>",key_pressed)

root.mainloop()